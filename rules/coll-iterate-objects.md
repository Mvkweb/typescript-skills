# coll-iterate-objects

> Iterate objects with typed `Object.keys`/`entries` helpers, not untyped `for-in`

## Why It Matters

`Object.keys` returns `string[]`, losing the key union and forcing casts at every use. One typed helper (`objectKeys<T>`) restores `keyof T`, so iteration stays checked and `noUncheckedIndexedAccess` can do its job on the values.

## Bad

```ts
const cfg = { host: "x", port: 1 };
for (const k in cfg) {
  console.log(cfg[k]); // error: string not assignable to "host" | "port"
}
```

## Good

```ts
function objectKeys<T extends object>(o: T): (keyof T)[] {
  return Object.keys(o) as (keyof T)[];
}
for (const k of objectKeys(cfg)) {
  console.log(cfg[k]); // typed: string | number
}
```

## See Also

- [gen-keyof-sets](gen-keyof-sets.md) - Key algebra behind the helper
- [coll-nouncheckedindexedaccess](coll-nouncheckedindexedaccess.md) - Values may still be undefined
