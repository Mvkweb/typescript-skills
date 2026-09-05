# async-try-await

> `await` inside `try` when you intend to catch; return bare promise to propagate

## Why It Matters

`try { return fetch() } catch {}` without `await` never catches: the promise rejects after the function already returned. `await` inside `try` attaches the rejection to that scope; bare `return` deliberately delegates handling to the caller.

## Bad

```ts
async function load() {
  try {
    return fetchData(); // catch below NEVER fires — not awaited
  } catch {
    return fallback;
  }
}
```

## Good

```ts
async function load() {
  try {
    return await fetchData(); // caught here
  } catch {
    return fallback;
  }
}
async function loadOrThrow() {
  return fetchData(); // propagate — caller handles
}
```

## See Also

- [err-no-empty-catch](err-no-empty-catch.md) - Handle, don't swallow
- [async-no-floating-promises](async-no-floating-promises.md) - Returned promises stay tracked
