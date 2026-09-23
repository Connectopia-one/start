/*
  Maakt van elke post in posts.js een beeld van 1080 x 1080 in de map erboven.

      PW=$(npm root -g)/playwright node render.js                 alles
      PW=$(npm root -g)/playwright node render.js dag-18-prikbord  één post

  Het script waarschuwt zelf als de inhoud onder de groene balk schuift of
  buiten het vierkant valt. Staat er "LET OP" bij, kort dan de tekst in of
  haal er een kaartje uit.
*/
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const posts = require('./posts.js');

const kleuren = { groen: '', paars: 'paars', oranje: 'oranje', blauw: 'blauw' };

function blad(p) {
  const stukken = [];
  if (p.tekst) stukken.push(`<p>${p.tekst}</p>`);

  const mid = [];
  if (p.citaat) mid.push(`<div class="citaat">${p.citaat}</div>`);
  if (p.kaarten) {
    const kaarten = p.kaarten
      .map(
        (k) => `<div class="kaart">
        <div class="ic">${k.ic || ''}</div>
        <div><div class="naam">${k.naam}</div><div class="wat">${k.wat}</div>${
          k.bij ? `<div class="bij">${k.bij}</div>` : ''
        }</div>
      </div>`
      )
      .join('\n      ');
    mid.push(`<div class="kaarten${p.kaartenTwee ? ' twee' : ''}">\n      ${kaarten}\n    </div>`);
  }
  if (p.woorden) {
    const woorden = p.woorden
      .map((w) => `<span class="woord">${w.ic ? `<span>${w.ic}</span>` : ''}${w.tekst}</span>`)
      .join('\n      ');
    mid.push(`<div class="woorden">\n      ${woorden}\n    </div>`);
  }
  if (p.nadruk) mid.push(`<div class="nadruk">${p.nadruk}</div>`);

  return `<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>${p.bestand}</title>
<link rel="stylesheet" href="stijl.css">
</head>
<body class="${[kleuren[p.kleur], p.foto ? 'metfoto' : ''].filter(Boolean).join(' ')}">
${p.foto ? `
  <div class="hero">
    <img src="${p.foto}" alt="" style="object-position: ${p.fotoPositie || '50% 45%'}">
    <svg class="golf" viewBox="0 0 148 10" preserveAspectRatio="none"><path d="M0 6 C 32 1, 63 1, 92 5 S 134 10, 148 3 L148 10 L0 10 Z" fill="#fbf6ea"/></svg>
  </div>` : ''}

  <div class="vorm" style="width: 520px; height: 520px; right: -190px; top: 250px; background: var(--sage-soft); opacity: .5"></div>
  <div class="vorm" style="width: 300px; height: 300px; left: -150px; top: 560px; background: var(--accent-soft); opacity: .6"></div>

  <svg class="blad" style="right: 96px; top: 96px; width: 78px; transform: rotate(35deg)" viewBox="0 0 40 40"><path d="M4 36 C 4 14, 18 4, 36 4 C 36 22, 26 36, 4 36 Z" fill="#8aa173"/><path d="M4 36 L 30 10" stroke="#fbf6ea" stroke-width="1.6" fill="none"/></svg>
  <svg class="blad" style="right: 68px; top: 160px; width: 50px; transform: rotate(-20deg)" viewBox="0 0 40 40"><path d="M4 36 C 4 14, 18 4, 36 4 C 36 22, 26 36, 4 36 Z" fill="#c6d4b3"/><path d="M4 36 L 30 10" stroke="#fbf6ea" stroke-width="1.6" fill="none"/></svg>

  <main>
    <header class="kop">
      <div class="pil">${p.pil}</div>
      <div class="hand">${p.hand}</div>
      <h1${p.titelKlein ? ' class="klein"' : ''}>${p.titel}</h1>
      ${stukken.join('\n      ')}
    </header>
    <section class="mid">
    ${mid.join('\n    ')}
    </section>
  </main>

  <footer class="actie">
    <svg class="tw" viewBox="0 0 40 40"><path d="M4 36 C 4 14, 18 4, 36 4 C 36 22, 26 36, 4 36 Z" fill="#8aa173"/></svg>
    <div class="links">
      <div class="hand">${p.voet.hand}</div>
      <div class="url">${p.voet.url}</div>
      ${p.voet.klein ? `<div class="klein">${p.voet.klein}</div>` : ''}
    </div>
    <div class="logo"><img src="logo-kim-transparant.png" alt="connectopia.one vzw"></div>
  </footer>

</body>
</html>
`;
}

(async () => {
  const kiezen = process.argv.slice(2).map((a) => a.replace(/\.(html|png)$/, ''));
  const doen = kiezen.length ? posts.filter((p) => kiezen.includes(p.bestand)) : posts;
  if (!doen.length) {
    console.log('Geen post gevonden met die naam.');
    process.exitCode = 1;
    return;
  }
  const b = await chromium.launch();
  let fout = 0;
  for (const p of doen) {
    const html = path.join(__dirname, p.bestand + '.html');
    fs.writeFileSync(html, blad(p));
    const pg = await b.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
    await pg.goto('file://' + html);
    await pg.evaluate(() => document.fonts.ready);
    await pg.waitForTimeout(200);
    const maat = await pg.evaluate(() => {
      const actie = document.querySelector('.actie').getBoundingClientRect();
      const kop = document.querySelector('.kop').getBoundingClientRect();
      const mid = document.querySelector('.mid');
      const inhoud = mid && mid.children.length ? mid.getBoundingClientRect() : kop;
      return {
        hoog: document.body.scrollHeight,
        kopBodem: Math.round(kop.bottom),
        inhoudBodem: Math.round(inhoud.bottom),
        actieTop: Math.round(actie.top),
        actieBodem: Math.round(actie.bottom),
      };
    });
    const klachten = [];
    if (maat.inhoudBodem > maat.actieTop) klachten.push('de inhoud loopt onder de groene balk');
    if (maat.kopBodem > maat.actieTop) klachten.push('de kop loopt onder de groene balk');
    if (maat.actieBodem > 1080 || maat.hoog > 1080) klachten.push('het blad is hoger dan 1080');
    console.log(
      p.bestand.padEnd(32),
      JSON.stringify(maat),
      klachten.length ? 'LET OP: ' + klachten.join(', ') : 'ok'
    );
    if (klachten.length) fout++;
    await pg.screenshot({ path: path.join(__dirname, '..', p.bestand + '.png') });
    await pg.close();
  }
  await b.close();
  if (fout) process.exitCode = 1;
})();
