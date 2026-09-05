# narrow-type-predicate

> Write `x is T` predicates for `filter`/custom guards

## Why It Matters

`(x) => x !== null` inside `filter` doesn't narrow the result array — TS keeps `(T | null)[]`. A predicate return type teaches the checker the implication, so `filter(isNonNull)` yields `T[]` with no cast.

## Bad

```ts
const mixed: (string | null)[] = ["a", null, "b"];
const only = mixed.filter((x) => x !== null); // still (string | null)[]
const upper = only.map((s) => s.toUpperCase()); // error: possibly null
```

## Good

```ts
function isNonNull<T>(x: T | null | undefined): x is T {
  return x !== null && x !== undefined;
}
const only: string[] = mixed.filter(isNonNull); // narrowed
```

## Guards Must Verify

A lying guard is worse than `as`: the bug hides behind a name that says it's safe. Every claimed property must actually be checked, and the guard name must match the check (`isX` / `hasX`). Prefer discriminant narrowing when possible — the guard adds a layer the reader has to follow.

```ts
// Lying guard — checks kind, claims full Circle
function isCircle(s: Shape): s is Circle {
  return (s as Circle).radius !== undefined; // Square with radius passes!
}

// Honest guard — verifies the discriminant
function isCircle(s: Shape): s is Circle {
  return s.kind === "circle";
}
```

## See Also

- [narrow-assertion-fn](narrow-assertion-fn.md) - Throwing variant
- [coll-iterate-objects](coll-iterate-objects.md) - Typed helpers that use predicates
