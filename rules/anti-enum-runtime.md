# anti-enum-runtime

> Don't use runtime `enum` when a union would do

## Why It Matters

`enum` emits a runtime object with reverse mappings, breaks erasable-syntax stripping, and serializes as numbers that are meaningless without the import. Unions + `as const` maps give identical checking with plain JS values that survive JSON, logs, and native runtimes.

## Bad

```ts
enum Status { Active, Done }
fetch("/s", { method: "POST", body: JSON.stringify({ s: Status.Done }) }); // sends 1
```

## Good

```ts
type Status = "active" | "done";
const Statuses = { Active: "active", Done: "done" } as const;
fetch("/s", { method: "POST", body: JSON.stringify({ s: Statuses.Done }) }); // sends "done"
```

## See Also

- [enum-literal-union](enum-literal-union.md) - The replacement
- [enum-erasable-only](enum-erasable-only.md) - Stripping compatibility
