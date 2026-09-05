# narrow-assertion-fn

> Use `asserts x is T` functions to validate at boundaries

## Why It Matters

Validation helpers that just return `boolean` leave narrowing to each call site. An assertion function bakes the contract in: if it returns, the value is `T`; if not, it throws. Boundaries (fetch, form input, env) get one validated choke point.

## Bad

```ts
function isUser(v: unknown): boolean {
  return typeof v === "object" && v !== null && "id" in v;
}
function handle(v: unknown) {
  if (!isUser(v)) throw new Error("bad");
  console.log(v.id); // error: v still unknown
}
```

## Good

```ts
type User = { id: string };
function assertUser(v: unknown): asserts v is User {
  if (typeof v !== "object" || v === null || !("id" in v)) {
    throw new Error("bad user");
  }
  if (typeof (v as Record<string, unknown>).id !== "string") {
    throw new Error("bad id");
  }
}
function handle(v: unknown) {
  assertUser(v);
  console.log(v.id.toUpperCase()); // narrowed to User
}
```

## See Also

- [narrow-type-predicate](narrow-type-predicate.md) - Non-throwing variant
- [any-unknown-over-any](any-unknown-over-any.md) - Validate unknown input
