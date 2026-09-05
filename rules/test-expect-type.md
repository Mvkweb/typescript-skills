# test-expect-type

> Test types with `expectTypeOf` / `assertType`, not just runtime tests

## Why It Matters

Runtime tests pass while public types silently widen (`"GET"` → `string`), breaking consumers with no failure. Type-level assertions lock the exact type at the boundary, so refactors that change inference fail fast in CI instead of downstream.

## Bad

```ts
import { describe, expect, it } from "vitest";
import { load } from "./lib";
describe("load", () => {
  it("returns a user", async () => {
    expect((await load("1")).name).toBe("a"); // passes even if type widened to any
  });
});
```

## Good

```ts
import { expectTypeOf } from "expect-type";
import type { User } from "./lib";
const u = await load("1");
expectTypeOf(u).toEqualTypeOf<User>();
expectTypeOf(u.id).toBeString();
```

## See Also

- [mod-export-types](mod-export-types.md) - Export types so tests can name them
- [gen-no-unnecessary-params](gen-no-unnecessary-params.md) - Keep tested signatures simple
