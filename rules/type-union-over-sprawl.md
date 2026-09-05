# type-union-over-sprawl

> Prefer unions of interfaces over interfaces with unions

## Why It Matters

`{ kind: "circle" | "square"; radius?: number }` can't link `kind` to which fields exist, so every access needs `?.` or `!`. Splitting into `Circle | Square` lets the discriminant drive narrowing and keeps each member's required fields required.

## Bad

```ts
interface Props {
  variant: "link" | "button";
  href?: string;
  onClick?: () => void;
}
// <Props variant="button" href="/x" /> compiles but is nonsense
```

## Good

```ts
type Props =
  | { variant: "link"; href: string }
  | { variant: "button"; onClick: () => void };
```

## See Also

- [narrow-discriminated-union](narrow-discriminated-union.md) - Narrowing mechanics
- [anti-optional-sprawl](anti-optional-sprawl.md) - Anti-pattern
