# null-no-non-null-assertion

> Avoid postfix `!`; narrow instead

## Why It Matters

`!` tells the compiler "trust me, not null" with zero runtime check. It silences the exact error `strictNullChecks` exists to surface, and breaks silently when refactored. Explicit narrowing survives moves and documents the invariant.

## Bad

```ts
function area(s: { radius?: number }) {
  return Math.PI * s.radius! ** 2; // crashes if radius missing
}
```

## Good

```ts
function area(s: { radius?: number }) {
  if (s.radius === undefined) throw new Error("radius required");
  return Math.PI * s.radius ** 2; // narrowed to number
}
```

## When `!` Is Acceptable

Almost never in app code. Tolerable in generated code or tests where presence is guaranteed by the harness — still prefer narrowing.

## See Also

- [anti-non-null-abuse](anti-non-null-abuse.md) - Anti-pattern
- [lint-tseslint-split](lint-tseslint-split.md) - Enforce `@typescript-eslint/no-non-null-assertion`
