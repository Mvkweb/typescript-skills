# anti-assertion-abuse

> Don't use `as` to lie to the compiler; fix the type

## Why It Matters

`as` is unchecked erasure: `expr as T` compiles even when `expr` can't be `T` (via `as unknown as T` it always compiles). Lies propagate — every consumer trusts the wrong type. Fix the source type, narrow, or validate; reserve `as` for cases you can prove and comment.

## Bad

```ts
const s = "hello" as unknown as number; // compiles, nonsense
function get(o: object) {
  return (o as { radius: number }).radius; // crashes on Square
}
```

## Good

```ts
function getRadius(s: Circle | Square): number | null {
  return s.kind === "circle" ? s.radius : null; // narrowed, no cast
}
```

## See Also

- [narrow-discriminated-union](narrow-discriminated-union.md) - Narrow instead of casting
- [anti-any-abuse](anti-any-abuse.md) - Same debt via any
