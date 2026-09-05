# coll-readonly-collections

> Prefer `readonly` arrays / `Readonly<T>` for inputs you don't mutate

## Why It Matters

Mutable parameter types (`items: string[]`) promise nothing about mutation, so callers must defensively copy and reviewers must audit every method. `readonly string[]` documents "I won't mutate" in the signature; the compiler rejects `push`/`sort` inside, and both mutable and readonly callers remain assignable.

## Bad

```ts
function total(ns: number[]) {
  ns.sort(); // mutates caller's array as a side effect!
  return ns.reduce((a, b) => a + b, 0);
}
```

## Good

```ts
function total(ns: readonly number[]): number {
  // ns.push(1); // error — readonly
  return [...ns].sort((a, b) => a - b).reduce((a, b) => a + b, 0);
}
```

## See Also

- [coll-record-sync](coll-record-sync.md) - Readonly records too
- [type-valid-states](type-valid-states.md) - Immutability as validity
