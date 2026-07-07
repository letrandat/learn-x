import os
from datetime import datetime, timezone

# Define paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONCEPT_PATH = os.path.join(ROOT_DIR, "projects", "agent-collab.md")
INDEX_PATH = os.path.join(ROOT_DIR, "index.md")
LOG_PATH = os.path.join(ROOT_DIR, "log.md")

# 1. Create the new concept file
concept_content = f"""---
type: project
title: Agent Collaboration Wiki
description: Integrating automated agents to collaborate on the OKF knowledge base.
tags: [agent, automation]
timestamp: {datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")}
---

# Agent Collaboration Wiki

This concept was created automatically by our local simulation agent.
It links back to our [Initial Wiki Project](wiki-init.md).
"""

os.makedirs(os.path.dirname(CONCEPT_PATH), exist_ok=True)
with open(CONCEPT_PATH, "w", encoding="utf-8") as f:
    f.write(concept_content)
print(f"Created: projects/agent-collab.md")

# 2. Update root index.md
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_lines = f.readlines()

new_index_entry = "* [Agent Collaboration Project](projects/agent-collab.md) - Integrating automated agents to collaborate on the OKF wiki.\n"
if not any("agent-collab.md" in line for line in index_lines):
    # Find list section and append
    index_lines.append(new_index_entry)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.writelines(index_lines)
    print("Updated: index.md")

# 3. Update log.md
today = datetime.now().strftime("%Y-%m-%d")
with open(LOG_PATH, "r", encoding="utf-8") as f:
    log_content = f.read()

log_lines = log_content.splitlines()
entry_heading = f"## {today}"
log_entry = f"\n{entry_heading}\n\n* **Creation** of `projects/agent-collab.md` via agent simulation.\n* **Update** of `index.md` listing the new Agent Collaboration concept."

# Check if today's header is already there
if entry_heading in log_content:
    # Append bullet points below the header
    for idx, line in enumerate(log_lines):
        if line.strip() == entry_heading:
            log_lines.insert(idx + 2, "* **Creation** of `projects/agent-collab.md` via agent simulation.")
            log_lines.insert(idx + 3, "* **Update** of `index.md` listing the new Agent Collaboration concept.")
            break
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")
else:
    # Insert new section below title (first line)
    title_line = log_lines[0]
    remaining = "\n".join(log_lines[1:])
    new_log = f"{title_line}\n{log_entry}\n{remaining}"
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(new_log)
print("Updated: log.md")
