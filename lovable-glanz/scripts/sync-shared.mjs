import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const sourceRoot = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const appRoot = resolve(sourceRoot, "lovable-glanz");

for (const [source, target] of [
  ["js/main.js", "public/js/main.js"],
  ["js/tracking.js", "public/js/tracking.js"],
  ["css/glanz-consent.css", "public/css/glanz-consent.css"],
]) {
  const output = resolve(appRoot, target);
  mkdirSync(dirname(output), { recursive: true });
  copyFileSync(resolve(sourceRoot, source), output);
}
