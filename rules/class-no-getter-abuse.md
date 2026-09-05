# class-no-getter-abuse

> Don't write Java-style get/set pairs; use plain properties or methods

## Why It Matters

`getFoo()`/`setFoo(v)` pairs add ceremony for what is just a property, and paired accessors with different types confuse assignability. Plain `readonly` properties for data, explicit methods (`load()`, `reset()`) for behavior — the call site reads the same in JS and TS.

## Bad

```ts
class User {
  private _name = "";
  getName() { return this._name; }
  setName(v: string) { this._name = v; }
}
u.setName("a"); u.getName();
```

## Good

```ts
class User {
  name = "";
  rename(v: string) {
    if (!v) throw new Error("empty name");
    this.name = v;
  }
}
u.rename("a"); u.name;
```

## See Also

- [class-private-field](class-private-field.md) - Real privacy when needed
- [type-valid-states](type-valid-states.md) - Validate at construction
