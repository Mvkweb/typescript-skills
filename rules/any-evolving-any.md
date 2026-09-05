# any-evolving-any

> Avoid evolving-`any` arrays; annotate accumulator types

## Why It Matters

`const xs = []` evolves: TS watches pushes and widens the element type as you go. Add a `string` after numbers and the inferred type silently becomes `(string | number)[]`, or worse, stays `any[]` under loose config. Annotating up front locks the contract before the first push.

## Bad

```ts
const values = []; // evolving any[]
values.push(1);
values.push("oops"); // no error at push site, error far away
const total: number[] = values;
```

## Good

```ts
const values: number[] = [];
values.push(1);
// values.push("oops"); // error here, where it belongs
```

## See Also

- [any-no-explicit-any](any-no-explicit-any.md) - Don't rely on implicit any
- [coll-readonly-collections](coll-readonly-collections.md) - Annotate inputs too
