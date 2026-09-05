# doc-no-repeat-types

> Don't repeat type info in docs; document intent, units, and invariants

## Why It Matters

`@param name {string} the name` restates the signature and rots when the type changes, while saying nothing about format, units, or constraints. Good TSDoc states what the type can't: allowed shape, side effects, error cases, and examples that actually compile.

## Bad

```ts
/**
 * @param id {string} the id
 * @returns {User} the user
 */
export function load(id: string): Promise<User> { return get(id); }
```

## Good

```ts
/**
 * Load a user by branded ID.
 *
 * @example
 *
 *     const u = await load(asUserId("u_1"));
 *
 * @throws {Error} When the user does not exist.
 */
export function load(id: UserId): Promise<User> { return get(id); }
```

## See Also

- [mod-export-types](mod-export-types.md) - Documented types must be exported
- [type-brand-nominal](type-brand-nominal.md) - Document brand invariants
