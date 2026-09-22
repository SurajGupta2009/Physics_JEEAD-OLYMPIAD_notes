#!/usr/bin/env node
// Optional integration with the repository's already-vendored KaTeX renderer.
// The copied topic's dependency-free Python gate does not require this renderer.
const fs = require('fs');
const path = require('path');
// __dirname is topic/tools; the repository is two levels up.
const bundled = path.join(__dirname, '../../docs/site/katex/katex.min.js');
const target = process.env.KATEX_PATH || bundled;
if (!fs.existsSync(target)) {
  console.log('KaTeX integration skipped: set KATEX_PATH to a local katex.min.js to enable it.');
  process.exit(0);
}
const katex = require(path.resolve(target));
const source = fs.readFileSync(path.join(__dirname, '../Electromagnetic-waves.md'), 'utf8');
const pattern = /\$\$([\s\S]*?)\$\$|(?<![\\$])\$(?!\$)([^\n]*?)(?<!\\)\$(?!\$)/g;
let count = 0;
for (const match of source.matchAll(pattern)) {
  const display = match[1] !== undefined;
  const tex = display ? match[1] : match[2];
  try {
    katex.renderToString(tex, {displayMode: display, throwOnError: true, strict: 'error'});
  } catch (error) {
    console.error(`Math at source offset ${match.index}: ${tex}\n${error.message}`);
    process.exit(1);
  }
  count++;
}
if (!count) throw new Error('No math found');
console.log(`all ${count} Markdown math expressions passed KaTeX`);
