# narrow-discriminated-union

> Model state as discriminated unions with literal `kind`, not optional sprawl

## Why It Matters

A single interface with `radius?: number; sideLength?: number` lets invalid combos compile (`{ kind: "circle" }` with no radius) and forces `!` everywhere. A union `Circle | Square` keyed on `kind` makes illegal states unrepresentable: checking `kind` narrows the whole object and required fields stay required.

## Bad

```ts
interface Shape {
  kind: "circle" | "square";
  radius?: number;
  sideLength?: number;
}
function getArea(s: Shape) {
  if (s.kind === "circle") return Math.PI * s.radius! ** 2; // ! needed
  return s.sideLength! ** 2;
}
```

## Good

```ts
interface Circle { kind: "circle"; radius: number }
interface Square { kind: "square"; sideLength: number }
type Shape = Circle | Square;

function getArea(s: Shape) {
  switch (s.kind) {
    case "circle": return Math.PI * s.radius ** 2; // narrowed to Circle
    case "square": return s.sideLength ** 2;
  }
}
```

## See Also

- [narrow-exhaustive-never](narrow-exhaustive-never.md) - Prove you handled all members
- [anti-optional-sprawl](anti-optional-sprawl.md) - Anti-pattern
