# gen-conditional-over-overload

> Prefer conditional types to overload signatures where possible

## Why It Matters

Overloads duplicate signatures, rot independently, and resolve by order (fragile). A single signature with a conditional return type keeps input→output mapping in one place and composes with unions and inference.

## Bad

```ts
function load(id: string): User;
function load(ids: string[]): User[];
function load(x: string | string[]): User | User[] {
  return Array.isArray(x) ? x.map(getOne) : getOne(x);
}
```

## Good

```ts
function load<T extends string | string[]>(
  x: T,
): T extends string ? User : User[] {
  return (Array.isArray(x) ? x.map(getOne) : getOne(x)) as never;
}
const one = load("u1"); // User
const many = load(["u1"]); // User[]
```

## See Also

- [gen-extends-constraint](gen-extends-constraint.md) - Constrain the conditional
- [fn-whole-expression](fn-whole-expression.md) - Type the whole signature once
