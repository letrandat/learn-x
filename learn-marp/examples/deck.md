---
marp: true
theme: gaia
size: 16:9
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: skip -->

# Putting Redis in Front of Our Product API

A 1-sprint spike to cut p99 latency and DB load

---

## The pain

- Product endpoint **p99 ≈ 800ms**
- The database is doing most of the work
- A lot of that work is **repeated reads** of the same rows

> Every popular product hits Postgres on every request.

---

## The insight

- Reads follow the classic **80/20** rule
- A small set of popular products drives most traffic
- We fetch the **same data over and over**

**If it rarely changes and is read constantly — cache it.**

---

## The plan: cache-aside

1. Request comes in → check Redis first
2. **Hit** → return cached value
3. **Miss** → read DB, write to Redis, return value

<!-- _footer: a.k.a. "lazy loading" — the cache fills on demand -->

---

## The code

```python
def get_product(id):
    cached = redis.get(f"product:{id}")
    if cached:                       # cache hit
        return json.loads(cached)
    row = db.query(                  # cache miss
        "select * from products where id=%s", id)
    redis.setex(f"product:{id}", 300, json.dumps(row))
    return row                       # TTL = 5 min
```

---

## The risks

- **Stale data** — cache lags writes
- **Cache stampede** — cold start, many misses at once
- **SPOF** — Redis goes down, everything falls back to DB

---

## The mitigations

- Short, **jittered TTL** → spreads expiries, avoids stampede
- **Invalidate the key on write** → bounds staleness
- **Redis cluster + failover** → kills the single point of failure

---

<!-- _class: lead -->

## The payoff

**p99 800ms → ~150ms · DB read load −70%**

Asking for **one sprint** to run the spike. 👍
