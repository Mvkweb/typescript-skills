# type-satisfies-conformance

> Use `satisfies` to check conformance without widening literals

## Why It Matters

Annotating `const c: Config = {...}` widens literals (`"GET"` → `string`) and hides typos until use. `as const` alone skips conformance checking. `satisfies` does both: validates against the target type while keeping the narrow inferred type for autocompletion and exhaustiveness.

## Bad

```ts
type Route = { path: string; method: "GET" | "POST" };
const r: Route = { path: "/a", method: "GET" };
//    ^? method: "GET" | "POST" — widened, typo-prone downstream
```

## Good

```ts
const r = { path: "/a", method: "GET" } satisfies Route;
//    ^? { path: string; method: "GET" } — narrow + checked
```

## See Also

- [fn-no-inferable-annotation](fn-no-inferable-annotation.md) - Let inference keep literals
- [enum-literal-union](enum-literal-union.md) - Literals stay precise
