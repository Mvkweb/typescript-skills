# any-narrowest-scope

> Keep `any` (when unavoidable) in the narrowest scope, hide behind typed boundary

## Why It Matters

Sometimes interop forces `any` (untyped JS lib, `JSON.parse`, legacy callback). The damage is proportional to how far it spreads. Confining it to one line inside a function that returns a precise type gives you a single audit point instead of infection across the codebase.

## Bad

```ts
export function getUser(input: any): any {
  return input.user; // any in, any out — callers unchecked
}
```

## Good

```ts
type User = { id: string; name: string };

export function getUser(input: unknown): User {
  const raw = input as { user: unknown }; // narrow scope
  if (typeof raw.user !== "object" || raw.user === null) {
    throw new Error("bad user");
  }
  const { id, name } = raw.user as Record<string, unknown>;
  if (typeof id !== "string" || typeof name !== "string") {
    throw new Error("bad user fields");
  }
  return { id, name }; // typed boundary
}
```

## See Also

- [any-unknown-over-any](any-unknown-over-any.md) - Prefer unknown at boundary
- [type-brand-nominal](type-brand-nominal.md) - Validate into precise types
