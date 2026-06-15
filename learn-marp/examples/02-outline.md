# Locked outline (Stage 3 — plain text, NO Marp yet)
# You review and approve THIS before any Markdown is written.
# Arc: hook -> problem -> solution -> proof -> ask

1. Title — "Putting Redis in Front of Our Product API" + subtitle (the ask)
2. The pain — p99 ~800ms, DB hammered by repeat reads
3. The insight — 80/20: same popular products read over and over
4. The plan — cache-aside (lazy loading) pattern, one diagram-in-words
5. The code — the get_product cache-aside snippet
6. The risks — stale data, cache stampede, Redis SPOF
7. The mitigations — short+jittered TTL, invalidate-on-write, cluster failover
8. The payoff + ask — p99 ~150ms, DB load -70%; approve a 1-sprint spike

# 8 slides for a 10-min slot ≈ right (roughly 1 min/slide + Q&A).
