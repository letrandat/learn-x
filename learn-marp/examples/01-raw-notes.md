# messy notes for the talk (raw input — this is what you'd hand the LLM)

we keep hitting the DB too much. p99 latency ~800ms on the product endpoint.
most reads are the same popular products over and over. classic 80/20.

idea: put redis in front. cache-aside (lazy loading) pattern.

draft code:
def get_product(id):
    cached = redis.get(f"product:{id}")
    if cached:
        return json.loads(cached)
    row = db.query("select * from products where id=%s", id)
    redis.setex(f"product:{id}", 300, json.dumps(row))
    return row

ttl 5 min. invalidate the key on write.

risks: stale data, cache stampede on cold start, redis is a SPOF.
mitigations: short ttl, jittered ttl, redis cluster w/ failover.

expected: p99 ~800ms -> ~150ms, db read load down ~70%.

audience: our backend team, ~10 min slot, goal = get buy-in to run a spike next sprint.
