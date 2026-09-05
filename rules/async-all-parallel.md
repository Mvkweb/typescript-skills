# async-all-parallel

> Use `Promise.all` for independent work, sequential `await` only when dependent

## Why It Matters

`await a(); await b()` when `b` doesn't need `a` serializes latency (2×RTT instead of 1×). `Promise.all` runs independent I/O concurrently with one failure point. Reserve sequential awaits for true data dependencies.

## Bad

```ts
const user = await getUser(id); // 200ms
const posts = await getPosts(id); // +200ms = 400ms, though independent
```

## Good

```ts
const [user, posts] = await Promise.all([getUser(id), getPosts(id)]); // ~200ms
// Dependent stays sequential:
const user2 = await getUser(id);
const avatar = await getAvatar(user2.avatarId);
```

## See Also

- [async-no-floating-promises](async-no-floating-promises.md) - Don't detach the combined promise
- [perf-parallel-flags](perf-parallel-flags.md) - Parallelism at build time too
