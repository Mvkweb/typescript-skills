# type-schema-derived

> Derive from existing schema/generated types via `Pick`/`Omit`/`Parameters`/`ReturnType` before declaring new interfaces

## Why It Matters

Reduplicating a shape from a `.proto`, OpenAPI spec, or DB migration guarantees drift: the source adds a field, the copy doesn't, and the mismatch surfaces at runtime. Deriving (`Pick<Msg, "a" | "b">`, `Awaited<ReturnType<typeof load>>`) tracks the source automatically and says exactly which slice you need.

## Bad

```ts
// Duplicate shape — drifts when the generated type changes
type CheckSummary = {
  totalCount: number;
  checks: { name: string; status: string }[];
};
function renderChecks(s: CheckSummary) {}
```

## Good

```ts
import type { ChecksMessage } from "./generated";
function renderChecks(s: Pick<ChecksMessage, "totalCount" | "checks">) {}

type LoadedUser = Awaited<ReturnType<typeof loadUser>>;
type HandlerArgs = Parameters<typeof handle>;
```

## See Also

- [narrow-schema-first](narrow-schema-first.md) - Infer from runtime schemas too
- [mod-export-types](mod-export-types.md) - Export the source types so others can derive
