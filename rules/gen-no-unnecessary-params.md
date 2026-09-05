# gen-no-unnecessary-params

> Avoid unnecessary type parameters; use what's there

## Why It Matters

Extra `<T>`s that appear once (or only to be immediately constrained) add inference sites, worse errors, and slower checking for no power. Most helpers need zero or one well-constrained parameter; concrete types or `unknown` + narrowing cover the rest.

## Bad

```ts
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
function wrap<T>(v: T): { value: T } {
  return { value: v };
}
// Call sites must often spell <string> explicitly for no benefit
```

## Good

```ts
// No generic needed — concrete input, concrete output
function firstString(arr: string[]): string | undefined {
  return arr[0];
}
// One param, used twice — genuine generic
function wrap<T>(v: T): { value: T } {
  return { value: v };
}
```

## See Also

- [gen-extends-constraint](gen-extends-constraint.md) - When a param earns its keep
- [fn-no-inferable-annotation](fn-no-inferable-annotation.md) - Less annotation, more inference
