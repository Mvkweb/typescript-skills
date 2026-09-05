# coll-nouncheckedindexedaccess

> Enable `noUncheckedIndexedAccess`; index access is `T | undefined`

## Why It Matters

By default `Record<string, string[]>` claims `obj.anything` is `string[]`, so `obj.foo.push()` compiles then crashes at runtime. With the flag, indexed access includes `undefined`, forcing the existence check where the bug actually lives. TS inference then understands the initialized branch.

## Bad

```ts
// noUncheckedIndexedAccess: false
const m: Record<string, string[]> = {};
m.foo.push("bar"); // compiles, crashes at runtime
```

## Good

```ts
// noUncheckedIndexedAccess: true
const m: Record<string, string[]> = {};
if (!m.foo) m.foo = []; // initialize once
m.foo.push("bar"); // narrowed to string[]
```

## See Also

- [cfg-strict-true](cfg-strict-true.md) - Companion strictness flags
- [coll-record-sync](coll-record-sync.md) - When Record is the right tool
