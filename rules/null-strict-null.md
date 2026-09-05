# null-strict-null

> Enable `strictNullChecks` (on by default in TS 7); never turn it off

## Why It Matters

Without `strictNullChecks`, `null` and `undefined` are assignable to everything, so the most common runtime crash (`Cannot read properties of null`) is invisible to the checker. With it on, nullable state must be handled explicitly. TS 7 defaults `strict: true`; disabling it voids most other rules.

## Bad

```ts
// strictNullChecks: false
function greet(name: string) {
  return name.toUpperCase(); // crashes if null passed, no error
}
greet(null);
```

## Good

```ts
function greet(name: string | null) {
  if (name === null) return "stranger";
  return name.toUpperCase(); // narrowed to string
}
```

## See Also

- [null-perimeter](null-perimeter.md) - Where null is allowed
- [cfg-strict-true](cfg-strict-true.md) - tsconfig setup
