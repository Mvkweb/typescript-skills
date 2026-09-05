# type-valid-states

> Prefer types that only represent valid states

## Why It Matters

Types that allow impossible combinations push validation to every reader (`if (!radius && kind === "circle")`). Types that exclude them push the check to construction: once built, every value is usable without re-checking. Fewer branches, fewer bugs.

## Bad

```ts
type Form = { value: string; error: string | null; touched: boolean };
// touched=false + error set? value empty + no error? All compile.
```

## Good

```ts
type Form =
  | { status: "editing"; value: string }
  | { status: "error"; value: string; error: string }
  | { status: "submitted"; value: string };

function submit(f: Form) {
  if (f.status !== "editing") return; // only editing is submittable
}
```

## See Also

- [narrow-discriminated-union](narrow-discriminated-union.md) - How to encode it
- [type-union-over-sprawl](type-union-over-sprawl.md) - Unions over optional sprawl
