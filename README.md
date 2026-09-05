# TypeScript Skills

<!-- gen:begin:badges -->
![rules](https://img.shields.io/badge/rules-63-3178C6?style=flat-square&logo=typescript&logoColor=white)
![categories](https://img.shields.io/badge/categories-19-89b4fa?style=flat-square&logo=typescript&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white)
![ci](https://github.com/Mvkweb/typescript-skills/actions/workflows/ci.yml/badge.svg)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)
<!-- gen:end:badges -->

By default, agents write decent TypeScript at best. These 63 rules pull that up to careful.

## Why

LLMs write TypeScript that compiles and breaks later. `any` instead of a type. `!` instead of a check. This skill is 63 small rules against exactly that. The agent reads the index, opens the rules that fit the code, and follows them.

## Install

```bash
npx add-skill Mvkweb/typescript-skills
```

Or clone it into your agent's skills dir. Then: `/typescript-skills review this function`.

## Example

```ts
// before
function firstWord(s: any) {
  return s.split(" ")[0]!;
}
```

```ts
// after — any-no-explicit-any, null-no-non-null-assertion, fn-return-type-branches
function firstWord(s: string): string | undefined {
  return s.split(" ")[0];
}
```

## What's in here

<!-- gen:begin:categories -->
63 rules split into 19 categories:

| Category | Rules | What it covers |
|----------|-------|----------------|
| **Any & Unknown Safety** | 4 | Ban any, narrow unknown |
| **Null & Undefined Safety** | 4 | Strict nulls, no ! |
| **Narrowing & Type Guards** | 6 | Unions, guards, schemas first |
| **Type Design & Domain Modeling** | 8 | Valid states, brands, derives |
| **Generics & Inference** | 4 | Minimal params, conditionals |
| **Functions & Signatures** | 4 | Return types, object args |
| **Error Handling** | 3 | unknown catch, Error-only |
| **Async & Concurrency** | 3 | No floats, Promise.all |
| **Objects, Arrays & Collections** | 4 | Indexed access, readonly |
| **Enums, Literals & Erasable Syntax** | 2 | Erasable code, unions |
| **Classes & OOP** | 2 | #private, no getters |
| **Modules & Declarations** | 2 | import type, export types |
| **Config & Compiler (TS 7)** | 5 | strict, erasable, TS7 split |
| **Performance (types + build)** | 2 | Emit speed, parallel flags |
| **Testing (types)** | 1 | expectTypeOf |
| **Documentation (TSDoc)** | 1 | Intent over types |
| **Linting & Tooling** | 1 | Lint/TS version split |
| **Project Structure** | 1 | devDeps, rootDir |
| **Anti-patterns** | 6 | Fix-ups index |
<!-- gen:end:categories -->

Every rule has a reason, a bad example, a good example, and links onward.

## How it works

[`SKILL.md`](./SKILL.md) is the index. [`rules/`](./rules) holds one file per rule. Prefixes match categories. That is the whole design.

## Manual install

```bash
git clone https://github.com/Mvkweb/typescript-skills.git <agent-skills-dir>/typescript-skills
```

Targets per agent:

- Claude Code (global): `~/.claude/skills/typescript-skills`
- Claude Code (one project): `.claude/skills/typescript-skills`
- OpenCode: `.opencode/skills/typescript-skills`
- Cursor: `.cursor/skills/typescript-skills`, or single file via `curl -o .cursorrules https://raw.githubusercontent.com/Mvkweb/typescript-skills/main/SKILL.md`
- Codex: `.codex/skills/typescript-skills`
- Copilot: `curl -o .github/copilot-instructions.md https://raw.githubusercontent.com/Mvkweb/typescript-skills/main/SKILL.md`
- Any AGENTS.md agent: `curl -o AGENTS.md https://raw.githubusercontent.com/Mvkweb/typescript-skills/main/SKILL.md`

Full rule list with links: [SKILL.md](./SKILL.md).

## Sources

Vanderkam's Effective TypeScript, Pocock's Total TypeScript tips, Goldberg's Learning TypeScript, Microsoft's Handbook, Cursor's pstack modeling rules. Synthesized, not copied. MIT.
