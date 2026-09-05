# enum-erasable-only

> Write erasable-only syntax; no runtime enums/namespaces/parameter properties

## Why It Matters

Node 22.18+, Deno, Bun, and browsers strip types without type-checking. Non-erasable syntax (`enum`, `namespace`, parameter properties, `private` modifiers) can't be stripped — it needs emit — so it breaks native execution and trips `erasableSyntaxOnly`. Erasable code runs everywhere with identical semantics.

## Bad

```ts
enum Role { Admin, User } // runtime object, not erasable
class C {
  constructor(private name: string) {} // parameter property — not erasable
}
namespace Util { export const x = 1; }
```

## Good

```ts
type Role = "admin" | "user";
const Roles = { Admin: "admin", User: "user" } as const;
class C {
  name: string;
  constructor(name: string) { this.name = name; }
}
```

## See Also

- [enum-literal-union](enum-literal-union.md) - The replacement pattern
- [cfg-erasable-syntax-only](cfg-erasable-syntax-only.md) - Enforce it in tsconfig
