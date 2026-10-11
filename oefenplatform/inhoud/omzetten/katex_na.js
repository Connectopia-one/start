const katex = require(require('path').resolve(__dirname, '../../node_modules/katex'));
const fs = require('fs');
let bad = 0, n = 0;
function walk(v, cb) {
  if (typeof v === 'string') cb(v);
  else if (Array.isArray(v)) v.forEach(x => walk(x, cb));
  else if (v && typeof v === 'object') Object.values(v).forEach(x => walk(x, cb));
}
for (const f of process.argv.slice(2)) {
  walk(JSON.parse(fs.readFileSync(f, 'utf8')), (s) => {
    for (const m of s.matchAll(/\\\(([\s\S]*?)\\\)/g)) {
      n++;
      try { katex.renderToString(m[1], {throwOnError: true, strict: false}); }
      catch (e) { bad++; console.log(f + '  ' + JSON.stringify(m[1]) + '\n   -> ' + e.message.split('\n')[0]); }
    }
    const los = s.replace(/\\\([\s\S]*?\\\)/g, '');
    if (/\\\(|\\\)/.test(los)) console.log('ONGEPAARD  ' + f + '  ' + JSON.stringify(s));
  });
}
console.log(`${n} formules nagekeken, ${bad} fout.`);
