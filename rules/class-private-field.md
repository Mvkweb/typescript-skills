# class-private-field

> Prefer `#private` ECMAScript fields over TS `private` for real privacy

## Why It Matters

TS `private` is compile-time only and erased at runtime — anyone can access `(x as never)["secret"]`, and it counts as non-erasable syntax in strict strip-types setups. `#` fields are runtime-enforced, work after emit, and communicate "do not touch" to JS consumers too.

## Bad

```ts
class Store {
  private token = "abc"; // accessible at runtime via bracket access
}
```

## Good

```ts
class Store {
  #token = "abc";
  reveal() { return this.#token.slice(0, 1) + "***"; }
}
```

## See Also

- [enum-erasable-only](enum-erasable-only.md) - Prefer runtime semantics
- [class-no-getter-abuse](class-no-getter-abuse.md) - Keep classes simple
