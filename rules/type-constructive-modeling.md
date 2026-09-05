# type-constructive-modeling

> Build types from parts that are all legal instead of restricting loose types

## Why It Matters

A loose type plus runtime checks (`T[]` + "throw if empty", `{ start, end }` + "comment says start <= end") forces every consumer to repeat the check and hope. A constructive type (`NonEmpty<T>`, `[T, T][]` pairs, `{ start, durationMs }`) makes the bad value unrepresentable: an empty array or negative range can't be written, so no check is needed downstream.

## Bad

```ts
// Loose type + comment holding the invariant
type TimeRange = { start: Date; end: Date }; // start <= end (hope so)
function pickWinner(entries: string[]): string {
  if (entries.length === 0) throw new Error("no entries"); // every caller repeats this
  return entries[Math.floor(Math.random() * entries.length)];
}
```

## Good

```ts
type NonEmpty<T> = [T, ...T[]];
const isNonEmpty = <T>(arr: T[]): arr is NonEmpty<T> => arr.length > 0;

function pickWinner(entries: NonEmpty<string>): string {
  const i = Math.floor(Math.random() * entries.length);
  const winner = entries[i]; // string | undefined under noUncheckedIndexedAccess
  if (winner === undefined) throw new Error("unreachable: index in range");
  return winner;
}

// Range as start + duration: a negative range can't be written
type TimeRange = { start: Date; durationMs: number };
function rangeEnd(r: TimeRange): Date {
  return new Date(r.start.getTime() + r.durationMs);
}
```

## See Also

- [type-valid-states](type-valid-states.md) - Only valid states exist
- [type-simplest-total](type-simplest-total.md) - Don't over-strengthen; use where partiality forces lies
- [narrow-type-predicate](narrow-type-predicate.md) - Guard once to enter the strong type
