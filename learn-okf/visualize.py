import os
import re
import json

def parse_frontmatter(content):
    """
    Simple regex-based YAML frontmatter parser to avoid external dependencies.
    """
    frontmatter = {}
    # Match the frontmatter block at the start of the file
    match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body_text = match.group(2)
    
    # Parse simple key-value pairs
    for line in yaml_text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            # Clean quotes and brackets
            val = re.sub(r'^["\'\[]?(.*?)["\'\]]?$', r'\1', val)
            if ',' in val and not val.startswith('{'):
                frontmatter[key] = [v.strip() for v in val.split(',')]
            else:
                frontmatter[key] = val
                
    return frontmatter, body_text

def extract_links(body, current_dir_rel):
    """
    Extract relative markdown links pointing to other concept files.
    """
    links = []
    # Match [label](path/to/file.md)
    matches = re.findall(r'\[([^\]]+)\]\(([^)]+\.md)\)', body)
    for label, target_path in matches:
        # Ignore external HTTP links or anchors
        if target_path.startswith(('http://', 'https://', '#')):
            continue
        
        # Normalize relative path
        target_clean = target_path.split('#')[0] # remove anchor
        rel_combined = os.path.normpath(os.path.join(current_dir_rel, target_clean))
        
        # Concept ID is the relative path without .md suffix
        concept_id = rel_combined.replace('\\', '/') # normalize slashes
        if concept_id.endswith('.md'):
            concept_id = concept_id[:-3]
            
        links.append({
            "label": label,
            "target": concept_id
        })
    return links

def scan_bundle(root_dir):
    nodes = {}
    edges = []
    
    # Folders to ignore
    ignore_dirs = {'.git', 'lessons', 'learning-records', 'reference', 'assets', 'scratch'}
    ignore_files = {'index.md', 'log.md', 'NOTES.md', 'MISSION.md', 'RESOURCES.md'}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Prune ignored directories in-place
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        
        for file in filenames:
            if not file.endswith('.md') or file in ignore_files:
                continue
                
            abs_path = os.path.join(dirpath, file)
            rel_path = os.path.relpath(abs_path, root_dir)
            concept_id = rel_path[:-3].replace('\\', '/')
            
            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            frontmatter, body = parse_frontmatter(content)
            
            concept_type = frontmatter.get('type', 'generic')
            title = frontmatter.get('title', os.path.basename(concept_id))
            description = frontmatter.get('description', '')
            
            nodes[concept_id] = {
                "id": concept_id,
                "type": concept_type,
                "title": title,
                "description": description
            }
            
            # Find links in body
            current_dir_rel = os.path.dirname(rel_path)
            file_links = extract_links(body, current_dir_rel)
            for link in file_links:
                edges.append({
                    "source": concept_id,
                    "target": link["target"],
                    "label": link["label"]
                })
                
    # Filter edges to only link existing nodes
    valid_edges = [e for e in edges if e["target"] in nodes]
    
    return list(nodes.values()), valid_edges

def generate_html(nodes, edges, output_file):
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Local OKF Wiki Graph</title>
  <style>
    :root {
      --bg-color: #0f172a;
      --card-bg: #1e293b;
      --text-color: #cbd5e1;
      --title-color: #f8fafc;
      --border-color: #334155;
      --accent: #38bdf8;
    }
    body {
      margin: 0;
      overflow: hidden;
      background-color: var(--bg-color);
      color: var(--text-color);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }
    #graph-container {
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0;
      left: 0;
    }
    #sidebar {
      position: absolute;
      top: 20px;
      left: 20px;
      width: 320px;
      max-height: calc(100vh - 40px);
      background: rgba(30, 41, 59, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
      overflow-y: auto;
      pointer-events: auto;
      z-index: 10;
    }
    h2 {
      margin-top: 0;
      color: var(--title-color);
      font-size: 1.25rem;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 10px;
    }
    .node-info {
      margin-top: 15px;
    }
    .meta-tag {
      display: inline-block;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 500;
      margin-bottom: 10px;
      text-transform: uppercase;
    }
    .description {
      font-size: 0.9rem;
      line-height: 1.5;
    }
    .instruction {
      font-size: 0.8rem;
      color: #64748b;
      margin-top: 10px;
      font-style: italic;
    }
  </style>
  <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
  <div id="sidebar">
    <h2>OKF Wiki Graph</h2>
    <div id="info-content">
      <p class="description">Hover or click a node in the graph to view its concept details and relationships.</p>
    </div>
    <div class="instruction">Scroll to zoom. Drag nodes to reposition.</div>
  </div>
  <svg id="graph-container"></svg>

  <script>
    const data = {
      nodes: %NODES%,
      links: %LINKS%
    };

    const width = window.innerWidth;
    const height = window.innerHeight;

    const svg = d3.select("#graph-container")
      .attr("viewBox", [0, 0, width, height]);

    const g = svg.append("g");

    // Add zoom behavior
    svg.call(d3.zoom()
      .extent([[0, 0], [width, height]])
      .scaleExtent([0.1, 4])
      .on("zoom", (event) => {
        g.attr("transform", event.transform);
      }));

    // Color scale for concept types
    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

    const simulation = d3.forceSimulation(data.nodes)
      .force("link", d3.forceLink(data.links).id(d => d.id).distance(150))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collision", d3.forceCollide().radius(60));

    // Draw links
    const link = g.append("g")
      .attr("stroke", "#475569")
      .attr("stroke-opacity", 0.6)
      .attr("stroke-width", 2)
      .selectAll("line")
      .data(data.links)
      .join("line");

    // Draw nodes
    const node = g.append("g")
      .selectAll("g")
      .data(data.nodes)
      .join("g")
      .call(drag(simulation))
      .on("mouseover", showInfo)
      .on("click", showInfo);

    node.append("circle")
      .attr("r", 12)
      .attr("fill", d => colorScale(d.type))
      .attr("stroke", "#f8fafc")
      .attr("stroke-width", 2);

    node.append("text")
      .attr("x", 16)
      .attr("y", 4)
      .text(d => d.title)
      .attr("fill", "#cbd5e1")
      .style("font-size", "12px")
      .style("font-weight", "500")
      .style("pointer-events", "none");

    simulation.on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

      node
        .attr("transform", d => `translate(${d.x},${d.y})`);
    });

    function showInfo(event, d) {
      const content = document.getElementById("info-content");
      content.innerHTML = `
        <div class="node-info">
          <div class="meta-tag">${d.type}</div>
          <h3 style="margin: 0 0 10px 0; color: #f8fafc;">${d.title}</h3>
          <p style="font-family: monospace; font-size: 0.8rem; color: #38bdf8; margin: 0 0 10px 0;">ID: ${d.id}</p>
          <p class="description">${d.description || 'No description provided.'}</p>
        </div>
      `;
    }

    function drag(simulation) {
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      }
      
      function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
      }
      
      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }
      
      return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
    }
  </script>
</body>
</html>
"""
    html_content = html_template.replace("%NODES%", json.dumps(nodes, indent=2))
    html_content = html_content.replace("%LINKS%", json.dumps(edges, indent=2))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Scanning bundle directory: {script_dir}")
    nodes, edges = scan_bundle(script_dir)
    print(f"Found {len(nodes)} concepts and {len(edges)} links.")
    
    output_html = os.path.join(script_dir, "wiki_graph.html")
    generate_html(nodes, edges, output_html)
    print(f"Successfully generated visualizer: {output_html}")
