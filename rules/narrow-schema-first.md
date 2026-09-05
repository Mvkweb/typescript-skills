# narrow-schema-first

> Use the repo's existing schema library before hand-writing property guards

## Why It Matters

A hand-written guard plus a duplicate interface plus (often) a schema drift apart: the guard checks `id` is a string, the interface adds `role`, the schema requires uuid — three truths. One schema owning validation with the type inferred from it (`z.infer`) keeps a single source of truth. Never add a new schema dependency for one guard; use what the codebase already trusts.

## Bad

```ts
interface User { id: string; role: "admin" | "member" }
function isUser(v: unknown): v is User {
  // hand-checked subset that rots when User gains a field
  return typeof v === "object" && v !== null && "id" in v;
}
```

## Good

```ts
import { z } from "zod"; // already the repo's schema lib — don't add one for this

const UserSchema = z.object({
  id: z.string().uuid(),
  role: z.enum(["admin", "member"]),
});
type User = z.infer<typeof UserSchema>;

function parseUser(input: unknown): User {
  return UserSchema.parse(input); // throws on bad shape
}
// Expected failure branch: UserSchema.safeParse(input)
```

## See Also

- [narrow-assertion-fn](narrow-assertion-fn.md) - Hand-rolled alternative when no schema lib exists
- [narrow-type-predicate](narrow-type-predicate.md) - Guards for logic, schemas for boundaries
