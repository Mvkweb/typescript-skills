# gen-extends-constraint

> Use `extends` to constrain and narrow generics

## Why It Matters

Unconstrained `<T>` accepts everything including `null`, forcing defensive code inside. `T extends string` (or a shape) moves the requirement to the call site with a clear error, and lets the body use string methods without narrowing.

## Bad

```ts
function longest<T>(a: T, b: T) {
  // @ts-expect-error — length may not exist
  return a.length >= b.length ? a : b;
}
```

## Good

```ts
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b; // length known
}
longest("ab", "c"); // OK
// longest(1, 2); // error: number has no length
```

## See Also

- [gen-no-unnecessary-params](gen-no-unnecessary-params.md) - Earn the parameter first
- [type-sets-mental-model](type-sets-mental-model.md) - extends as subset
