# narrow-exhaustive-never

> Use `never` in `default` for exhaustiveness checking

## Why It Matters

Switches over unions rot: someone adds `Triangle` and the old `default: return 0` silently handles it wrong. Assigning the leftover to `never` turns a missed case into a compile error at the exact switch that needs updating.

## Bad

```ts
type Shape = Circle | Square;
function getArea(s: Shape) {
  switch (s.kind) {
    case "circle": return 1;
    case "square": return 2;
    default: return 0; // silently swallows future members
  }
}
```

## Good

```ts
interface Circle { kind: "circle"; radius: number }
interface Square { kind: "square"; sideLength: number }
type Shape = Circle | Square;

function getArea(s: Shape) {
  switch (s.kind) {
    case "circle": return Math.PI * s.radius ** 2;
    case "square": return s.sideLength ** 2;
    default: {
      const _exhaustive: never = s;
      return _exhaustive;
    }
  }
}
// Adding Triangle → error: Type 'Triangle' is not assignable to 'never'
```

## See Also

- [narrow-discriminated-union](narrow-discriminated-union.md) - The unions to check
- [type-valid-states](type-valid-states.md) - Make invalid unrepresentable first
