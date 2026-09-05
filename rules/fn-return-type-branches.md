# fn-return-type-branches

> Omit return types for simple inference; require them for multi-branch + all library exports

## Why It Matters

Annotating `(): string` on `() => "a"` adds maintenance with no safety — inference already knows. But multi-branch functions (if/switch/ternary) can silently return a widened or typo'd union; an explicit return type pins the contract and catches the wrong branch. Libraries always annotate: consumers need stable `.d.ts` and faster emit.

## Bad

```ts
function makeId() { // inferred string — annotation would just be noise
  return `id-${Math.random().toString(16).slice(2)}`;
}
function handle(e: Event) { // branches widen silently
  if (e.type === "click") return { focused: true, at: Date.now() };
  return { focused: false, at: Date.now(), extra: 1 }; // typo slips in
}
```

## Good

```ts
type State = { focused: boolean; at: number };
function handle(e: Event): State {
  if (e.type === "click") return { focused: true, at: Date.now() };
  // return { focused: false, at: Date.now(), extra: 1 }; // error: excess prop
  return { focused: false, at: Date.now() };
}
// Library: always annotate exports
export function parse(s: string): State { return JSON.parse(s); }
```

## See Also

- [fn-no-inferable-annotation](fn-no-inferable-annotation.md) - When to leave it off
- [perf-explicit-return-lib](perf-explicit-return-lib.md) - Emit performance for libs
