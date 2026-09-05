# coll-record-sync

> Use `Record` to keep keys/values in sync; avoid bare index signatures

## Why It Matters

`{ [k: string]: T }` accepts any string and gives no key list for autocompletion or exhaustiveness. `Record<Union, T>` ties the map to a finite key set: adding a union member without a map entry errors, and `Object.keys` helpers stay typed.

## Bad

```ts
const labels: { [k: string]: string } = { home: "Home" };
// Missing "about" — no error. Typo "hme" — no error.
function label(k: string) { return labels[k]; }
```

## Good

```ts
type Page = "home" | "about";
const labels: Record<Page, string> = { home: "Home", about: "About" };
// Adding "contact" to Page without adding it here → error
```

## See Also

- [coll-nouncheckedindexedaccess](coll-nouncheckedindexedaccess.md) - Index results still need checks
- [gen-keyof-sets](gen-keyof-sets.md) - Derive key unions from objects
