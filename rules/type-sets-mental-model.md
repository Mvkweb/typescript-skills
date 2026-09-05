# type-sets-mental-model

> Think of types as sets; `extends` = subset = assignable

## Why It Matters

Assignability clicks once types are sets of values: `"A"` is a one-value set inside `"A" | "B"`, so it's assignable the other way. `keyof (A & B) = keyof A | keyof B` and `keyof (A | B) = keyof A & keyof B` stop being trivia and become Venn logic. "Extends", "assignable to", and "subtype of" all mean "subset of".

## Bad

```ts
type AB = "A" | "B";
declare let ab12: "A" | "B" | 12;
const back: AB = ab12; // error — {"A","B",12} is not a subset of {"A","B"}
```

## Good

```ts
type AB = "A" | "B";
type AB12 = "A" | "B" | 12;
declare let ab: AB;
const fwd: AB12 = ab; // OK — {"A","B"} ⊆ {"A","B",12}

function getKey<K extends string>(key: K) { return key; }
getKey("x"); // OK — "x" ⊆ string
// getKey(12); // error — number ⊄ string
```

## See Also

- [gen-keyof-sets](gen-keyof-sets.md) - keyof set algebra in practice
- [gen-extends-constraint](gen-extends-constraint.md) - extends as subset bound
