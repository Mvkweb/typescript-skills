// checks/support/ambient.d.ts — test harness ONLY, not part of the skill.
//
// Loosely-typed stand-ins for helper names that Good examples reference but
// that are defined elsewhere (another rule, the reader's codebase). `any`
// here is deliberate: it silences name-resolution noise so `tsc` judges each
// example's own logic instead. Real checking still comes from the example's
// locally-declared types (brands, unions, generics).
//
// Every file gen.py emits is a module (`export {}`), so a rule that declares
// its own `User`/`Session`/etc. shadows these globals — no merge conflicts.
declare function getOne(id: string): any;
declare function get(id: string): any;
declare function load(...args: any[]): any;
declare function loadUser(id: string): any;
declare function save(...args: any[]): any;
declare function fetchData(): Promise<any>;
declare function run(): void;
declare function report(e: unknown): void;
declare function sendEmail(...args: any[]): any;
declare function showToast(...args: any[]): any;
declare function keepDraft(...args: any[]): any;
declare function getUser(id: string): any;
declare function getPosts(id: string): any;
declare function getAvatar(id: string): any;
declare function drawCircle(...args: any[]): any;
declare function drawRect(...args: any[]): any;
declare function openFile(...args: any[]): any;
declare function isUUID(s: string): boolean;
declare const fallback: any;
declare const uri: string;

interface Session {
  id: string;
}
interface GitDiff {
  files: string[];
}
