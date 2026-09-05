# fn-no-inferable-annotation

> Don't annotate what inference already knows; annotate boundaries

## Why It Matters

`const x: number = 42` and `(s: string): string => s` restate the obvious and rot when logic changes. Inference handles locals; humans should annotate the seams (exports, network boundaries, discriminants) where intent matters and errors should surface.

## Bad

```ts
const name: string = "Ada";
const nums: number[] = [1, 2];
names.forEach((s: string): void => { console.log(s); }); // noise
```

## Good

```ts
const name = "Ada";
const nums = [1, 2];
const names = ["Ada", "Bo"];
names.forEach((s) => console.log(s.toUpperCase())); // contextual typing
export function total(ns: readonly number[]): number {
  return ns.reduce((a, b) => a + b, 0); // boundary annotated
}
```

## See Also

- [fn-return-type-branches](fn-return-type-branches.md) - The branch exception
- [type-satisfies-conformance](type-satisfies-conformance.md) - Check without widening
