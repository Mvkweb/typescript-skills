# gen-keyof-sets

> Remember `keyof (A & B)` vs `keyof (A | B)` set logic; use `keyof typeof` for objects

## Why It Matters

`keyof` follows set rules, not intuition: intersecting value sets unions the keys, unioning values intersects the keys. Forgetting this yields `never` keys or over-broad helpers. Deriving unions from `keyof typeof obj` keeps string lists in sync with the source object.

## Bad

```ts
interface Person { name: string }
interface Lifespan { birth: Date }
type K = keyof (Person | Lifespan); // never — no common keys!
function get(o: Person, k: string) { return o[k as keyof Person]; }
```

## Good

```ts
const routes = { home: "/", about: "/about" } as const;
type Route = keyof typeof routes; // "home" | "about" — always in sync

type K1 = keyof (Person & Lifespan); // "name" | "birth"
type K2 = keyof (Person | Lifespan); // never — correct per set logic
```

## See Also

- [type-sets-mental-model](type-sets-mental-model.md) - The Venn intuition
- [coll-iterate-objects](coll-iterate-objects.md) - Typed keys in practice
