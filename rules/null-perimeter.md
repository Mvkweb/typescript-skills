# null-perimeter

> Push `null`/`undefined` to the perimeter; don't sprinkle through aliases

## Why It Matters

If `null` appears in shared aliases (`type ID = string | null`), every consumer must null-check even when the value is always present in practice. Keeping domain types non-nullable and allowing `null` only at I/O edges (fetch results, missing cache entries) minimizes defensive code and makes absence explicit.

## Bad

```ts
type UserId = string | null; // null leaks everywhere

function profile(id: UserId) {
  // must check even when caller always has an id
  if (id === null) throw new Error("unreachable?");
  return load(id);
}
```

## Good

```ts
type UserId = string;

function findUser(id: UserId | null): User | null {
  if (id === null) return null; // perimeter only
  return load(id); // domain stays non-null
}
```

## See Also

- [null-strict-null](null-strict-null.md) - Checker that enforces this
- [type-valid-states](type-valid-states.md) - Types that can't be invalid
