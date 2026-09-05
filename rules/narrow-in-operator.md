# narrow-in-operator

> Prefer `in` / `typeof` / `instanceof` guards over truthiness for objects

## Why It Matters

Truthiness (`if (x)`) drops `0`, `""`, and `false` along with `null`, and doesn't narrow union members by shape. Structural guards (`"swim" in a`, `typeof x === "string"`, `x instanceof Date`) narrow precisely to the members that have that property or prototype.

## Bad

```ts
type Fish = { swim: () => void };
type Bird = { fly: () => void };
function move(a: Fish | Bird | null) {
  if (a) return "something"; // doesn't tell Fish from Bird
  return "none";
}
```

## Good

```ts
function move(a: Fish | Bird) {
  if ("swim" in a) return a.swim(); // narrowed to Fish
  return a.fly(); // narrowed to Bird
}
```

## Narrowing Ladder

From best to last-resort: discriminated-union `switch` > `in` operator > `typeof` / `instanceof` > user-defined predicate > `as` (only after validation). Prefer the earliest rung that works; each step down adds a layer the reader must trust.

## See Also

- [narrow-discriminated-union](narrow-discriminated-union.md) - Prefer `kind` when you own the types
- [null-strict-null](null-strict-null.md) - Check null explicitly, not via truthiness
