# fn-whole-expression

> Apply types to entire function expressions, not just parameters

## Why It Matters

Annotating only parameters (`(e: ChangeEvent) => ...`) leaves the return unchecked and breaks contextual inference for generics. Typing the whole expression (`const h: ChangeHandler = (e) => ...`) checks params *and* return at once and gives better errors at the assignment, not deep inside.

## Bad

```ts
function onChange(e: React.ChangeEvent<HTMLInputElement>) {
  return e.target.value; // return widened, no check against handler type
}
<input onChange={(e: never) => onChange(e as never)} />;
```

## Good

```ts
type ChangeHandler = (e: { target: { value: string } }) => void;
const onChange: ChangeHandler = (e) => {
  console.log(e.target.value.toUpperCase()); // e contextually typed + checked
};
```

## See Also

- [fn-return-type-branches](fn-return-type-branches.md) - Boundaries need types
- [mod-export-types](mod-export-types.md) - Export the handler types too
