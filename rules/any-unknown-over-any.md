# any-unknown-over-any

> Use `unknown` for values with an unknown type

## Why It Matters

`unknown` is the type-safe counterpart to `any`: you can accept anything, but you must narrow before use. This moves validation to the boundary where data enters (fetch, JSON, `catch`, message ports) and keeps the rest of the codebase fully checked.

## Bad

```ts
function handle(msg: any) {
  console.log(msg.kind.toUpperCase()); // crashes if shape differs
}
```

## Good

```ts
function handle(msg: unknown) {
  if (typeof msg !== "object" || msg === null) return;
  if (!("kind" in msg) || typeof msg.kind !== "string") return;
  console.log(msg.kind.toUpperCase()); // narrowed to string
}
```

## See Also

- [any-no-explicit-any](any-no-explicit-any.md) - Ban `any` in signatures
- [narrow-type-predicate](narrow-type-predicate.md) - Reusable narrowing
- [err-unknown-in-catch](err-unknown-in-catch.md) - `catch (e: unknown)`
