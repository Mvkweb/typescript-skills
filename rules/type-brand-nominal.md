# type-brand-nominal

> Use brands for nominal typing (IDs, units, validated strings)

## Why It Matters

TypeScript is structural: `UserId` and `GroupId` are both `string` and freely mixable. A brand (`string & { __brand: "UserId" }`) makes them distinct with zero runtime cost. Swapped arguments and mixed units become compile errors instead of data corruption.

## Bad

```ts
function addToGroup(userId: string, groupId: string) {}
addToGroup("group-1", "user-9"); // swapped, compiles fine
```

## Good

```ts
type UserId = string & { readonly __brand: "UserId" };
type GroupId = string & { readonly __brand: "GroupId" };
declare function asUserId(s: string): UserId;
declare function asGroupId(s: string): GroupId;

function addToGroup(userId: UserId, groupId: GroupId) {}
addToGroup(asUserId("u9"), asGroupId("g1")); // OK
// addToGroup(asGroupId("g1"), asUserId("u9")); // error
```

## See Also

- [narrow-assertion-fn](narrow-assertion-fn.md) - Validate into brands at boundaries
- [anti-stringly-typed](anti-stringly-typed.md) - Don't use bare strings
