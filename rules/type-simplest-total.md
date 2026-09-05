# type-simplest-total

> Keep `T[]` while every operation stays total; strengthen only where looseness forces lies

## Why It Matters

Strengthening everything (`NonEmpty` everywhere) spreads complexity to call sites that handle empty fine (`reduce` with init, `map`, `length` checks). The tells that a stronger type is owed: `!`, `as T`, or a "should never happen" throw at the use site. Fix the signature there; leave total code on the loose type.

## Bad

```ts
// Partiality smuggled past the compiler
function newestSession(sessions: Session[]): Session {
  return sessions.at(0)!; // lies if empty
}
```

## Good

```ts
// Total on the loose type — no strengthening needed
const sum = (xs: number[]): number => xs.reduce((a, b) => a + b, 0); // [] is 0, fine

// Partial use site — strengthen the input so the assertion disappears
import type { NonEmpty } from "./model";
function newestSession(sessions: NonEmpty<Session>): Session {
  return sessions[0];
}
// …or weaken the result: (sessions: Session[]) => Session | undefined
```

## See Also

- [type-constructive-modeling](type-constructive-modeling.md) - The strong types to reach for
- [null-no-non-null-assertion](null-no-non-null-assertion.md) - The `!` this rule eliminates
