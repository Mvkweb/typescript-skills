# anti-stringly-typed

> Don't use bare `string` where a literal union, brand, or enum-object fits

## Why It Matters

`string` accepts typos (`"centre"` vs `"center"`), mixes IDs, and defeats exhaustiveness. Narrow string sets error at the typo, enable `never` checks, and power autocompletion — with zero runtime cost.

## Bad

```ts
function align(x: string) {}
align("centre"); // typo compiles
function move(userId: string, groupId: string) {}
move("g1", "u9"); // swapped compiles
```

## Good

```ts
type Align = "left" | "right" | "center";
function align(x: Align) {}
// align("centre"); // error, did you mean "center"?
```

## See Also

- [enum-literal-union](enum-literal-union.md) - The union pattern
- [type-brand-nominal](type-brand-nominal.md) - Distinct string kinds
