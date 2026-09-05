# anti-optional-sprawl

> Don't model exclusive states with piles of optionals

## Why It Matters

Five optionals encode 2⁵ = 32 combinations, most invalid; the checker can't help and every reader re-derives the real invariants. Unions enumerate the 2–3 valid shapes; invalid combinations don't compile.

## Bad

```ts
type Req = { url: string; body?: string; method?: string; retried?: boolean };
// GET with body? No method? All compile.
```

## Good

```ts
type Req =
  | { method: "GET"; url: string }
  | { method: "POST"; url: string; body: string; retried?: boolean };
```

## See Also

- [type-union-over-sprawl](type-union-over-sprawl.md) - The rule
- [type-valid-states](type-valid-states.md) - Only valid states
