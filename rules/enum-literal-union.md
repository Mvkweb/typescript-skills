# enum-literal-union

> Prefer string literal unions + `as const` objects over `enum`

## Why It Matters

`enum` adds a runtime object, reverse mappings, and non-standard semantics for what is usually just a closed set of strings. A literal union gives the same checking with plain JS semantics, better declaration emit, and free exhaustiveness via `never`.

## Bad

```ts
enum Method { GET, POST }
function call(m: Method) {}
call(Method.GET);
// Serializes as 0 — meaningless over the wire without the enum import
```

## Good

```ts
type Method = "GET" | "POST";
const Methods = { Get: "GET", Post: "POST" } as const;
function call(m: Method) {}
call(Methods.Get); // "GET" — meaningful everywhere
```

## See Also

- [enum-erasable-only](enum-erasable-only.md) - Why enums break stripping
- [narrow-exhaustive-never](narrow-exhaustive-never.md) - Exhaustiveness over unions
