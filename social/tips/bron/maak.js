/*
  Maakt van de tipspagina van het oefenplatform tien vierkante beelden:
  een voorblad en de negen stappen, elk als een notitieblaadje.

      PW=$(npm root -g)/playwright node maak.js

  De teksten komen rechtstreeks uit oefenplatform/inhoud/tips.ts, zodat de
  beelden niet uit elkaar lopen met de pagina. Pas je daar een stap aan, draai
  dit script dan opnieuw en de beelden kloppen weer.

  Het script zegt per blad of de tekst binnen het blaadje past. Staat er
  "LET OP" bij, kort die stap dan in op de pagina zelf.
*/
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const path = require('path');

const HIER = __dirname;
const UIT = path.join(HIER, '..');
const POSTS = path.join(HIER, '..', '..', 'posts', 'bron');

/* De teksten uit tips.ts halen. Het is een gewoon JavaScript-object, dus we
   maken er even een module van en lezen het in. Zo staat er niets dubbel. */
function tips() {
  const bron = fs.readFileSync(
    path.join(HIER, '..', '..', '..', 'oefenplatform', 'inhoud', 'tips.ts'),
    'utf8'
  );
  const tijdelijk = path.join(HIER, '.tips-tijdelijk.js');
  fs.writeFileSync(tijdelijk, bron.replace('export const tipsTekst =', 'module.exports ='));
  const uit = require(tijdelijk);
  fs.unlinkSync(tijdelijk);
  return uit;
}

/* De kleuren van de blaadjes, in dezelfde volgorde als op de pagina. */
const BRIEFJES = ['geel', 'roze', 'groen', 'blauw'];

function kop(titel, blaadjes) {
  return `<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>${titel}</title>
<link rel="stylesheet" href="${POSTS}/stijl.css">
<style>
  /* Het notitieblaadje in het midden. */
  .briefje {
    position: relative; z-index: 2; align-self: flex-start; margin-left: 6px; width: 760px;
    border-radius: 30px; padding: 64px 68px 72px;
    box-shadow: 0 18px 40px rgba(42, 45, 38, .10);
    transform: rotate(-1.2deg);
  }
  .briefje.geel  { background: #fbf0cf; }
  .briefje.roze  { background: #fae5d1; }
  .briefje.groen { background: #dfe7d0; }
  .briefje.blauw { background: #dcebf6; }
  .briefje.recht { transform: rotate(1.1deg); }
  /* het punaisebolletje bovenaan, zoals op de pagina */
  .punaise {
    position: absolute; top: 34px; left: 50%; margin-left: -17px;
    width: 34px; height: 34px; border-radius: 50%; background: #c08a3e;
    box-shadow: 0 3px 0 rgba(42, 45, 38, .12);
  }
  .stap {
    font-weight: 900; font-size: 26px; letter-spacing: .14em;
    text-transform: uppercase; color: var(--orange);
  }
  .briefje h2 {
    font-weight: 900; color: var(--green); font-size: 60px; line-height: 1.06;
    letter-spacing: -.02em; margin-top: 14px;
  }
  .briefje p { margin-top: 26px; font-size: 33px; line-height: 1.38; color: #4a5142; font-weight: 600; }
  main.midden { justify-content: center; }
  /* het voorblad */
  .nummers { display: flex; gap: 14px; margin-top: 34px; flex-wrap: wrap; }
  .nummers span {
    width: 64px; height: 64px; border-radius: 50%; background: #fff;
    border: 2px solid var(--border); display: flex; align-items: center;
    justify-content: center; font-weight: 900; font-size: 30px; color: var(--green-mid);
  }
  .nota {
    margin-top: 30px; font-size: 27px; line-height: 1.35; color: var(--ink-dim);
    font-weight: 700; border-left: 6px solid var(--sage); padding-left: 22px;
  }
  /* Het pijltje rechts: Kim vroeg een teken dat er nog beelden volgen. Het
     staat los van het briefje, tegen de rand, zodat het niet in de tekst
     meeleest maar wel opvalt bij het doorschuiven. */
  .verder {
    position: absolute; z-index: 3; right: 44px; top: 50%; margin-top: -52px;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }
  .verder .bol {
    width: 78px; height: 78px; border-radius: 50%; background: var(--orange);
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 6px 16px rgba(217, 110, 37, .35);
  }
  /* De pijl is een tekening en geen teken uit het lettertype: Nunito heeft
     geen chevron, en dan valt er een leeg vakje op het beeld. */
  .verder .bol svg { width: 34px; height: 34px; }
  .verder .bij {
    font-family: "Caveat"; font-size: 34px; color: var(--orange); line-height: 1;
    white-space: nowrap;
  }
</style>
</head>
<body>
  <div class="vorm" style="width: 520px; height: 520px; right: -190px; top: 250px; background: var(--sage-soft); opacity: .5"></div>
  <div class="vorm" style="width: 300px; height: 300px; left: -150px; top: 560px; background: var(--accent-soft); opacity: .6"></div>
${blaadjes ? `
  <svg class="blad" style="right: 96px; top: 96px; width: 78px; transform: rotate(35deg)" viewBox="0 0 40 40"><path d="M4 36 C 4 14, 18 4, 36 4 C 36 22, 26 36, 4 36 Z" fill="#8aa173"/><path d="M4 36 L 30 10" stroke="#fbf6ea" stroke-width="1.6" fill="none"/></svg>
  <svg class="blad" style="right: 68px; top: 160px; width: 50px; transform: rotate(-20deg)" viewBox="0 0 40 40"><path d="M4 36 C 4 14, 18 4, 36 4 C 36 22, 26 36, 4 36 Z" fill="#c6d4b3"/><path d="M4 36 L 30 10" stroke="#fbf6ea" stroke-width="1.6" fill="none"/></svg>` : ''}`;
}

function pijl(tekst) {
  return `
  <div class="verder">
    <div class="bol"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M12 5l7 7-7 7"/></svg></div>
    <div class="bij">${tekst}</div>
  </div>`;
}

function voet(klein) {
  return `
  <footer class="actie">
    <svg class="tw" viewBox="0 0 40 40"><path d="M4 36 C 4 14, 18 4, 36 4 C 36 22, 26 36, 4 36 Z" fill="#8aa173"/></svg>
    <div class="links">
      <div class="hand">Alles staat op de pagina zelf</div>
      <div class="url">oefenplatform.connectopia.one/tips</div>
      ${klein ? `<div class="klein">${klein}</div>` : ''}
    </div>
    <div class="logo"><img src="${POSTS}/logo-kim-transparant.png" alt="connectopia.one vzw"></div>
  </footer>
</body>
</html>
`;
}

function voorblad(t) {
  const bolletjes = t.stappen.map((_, i) => `<span>${i + 1}</span>`).join('');
  return `${kop(t.titel, true)}
  <main>
    <header class="kop">
      <div class="pil">${t.label}</div>
      <div class="hand">In ${t.stappen.length} stappen</div>
      <h1>Tips om met het <span>oefenplatform</span> te werken</h1>
      <p>Geen handleiding met knopjes. Dit is hoe wij er zelf mee werken, als richtlijn. Iedereen is vrij om te kiezen hoe hij ermee omgaat.</p>
      <div class="nummers">${bolletjes}</div>
    </header>
    <section class="mid"><div class="nota">${t.nota}</div></section>
  </main>
${pijl('schuif door')}
${voet('Schuif door voor de negen stappen')}`;
}

function stapblad(stap, nummer, totaal) {
  const kleur = BRIEFJES[(nummer - 1) % BRIEFJES.length];
  const scheef = nummer % 2 === 0 ? ' recht' : '';
  return `${kop(stap.kop, false)}
  <main class="midden">
    <div class="briefje ${kleur}${scheef}">
      <div class="punaise"></div>
      <div class="stap">Stap ${nummer} van ${totaal}</div>
      <h2>${stap.kop}</h2>
      <p>${stap.tekst}</p>
    </div>
  </main>
${nummer < totaal ? pijl('volgende') : ''}
${voet(nummer < totaal ? '' : 'Alle stappen staan op de pagina zelf')}`;
}

(async () => {
  const t = tips();
  const bladen = [{ bestand: 'tips-00-voorblad', html: voorblad(t) }];
  t.stappen.forEach((stap, i) => {
    const nummer = i + 1;
    bladen.push({
      bestand: 'tips-' + String(nummer).padStart(2, '0') + '-' + slug(stap.kop),
      html: stapblad(stap, nummer, t.stappen.length),
    });
  });

  const kiezen = process.argv.slice(2).map((a) => a.replace(/\.(html|png)$/, ''));
  const doen = kiezen.length ? bladen.filter((b) => kiezen.includes(b.bestand)) : bladen;

  const b = await chromium.launch();
  let fout = 0;
  for (const blad of doen) {
    const html = path.join(HIER, blad.bestand + '.html');
    fs.writeFileSync(html, blad.html);
    const pg = await b.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
    await pg.goto('file://' + html);
    await pg.evaluate(() => document.fonts.ready);
    await pg.waitForTimeout(200);
    const maat = await pg.evaluate(() => {
      const actie = document.querySelector('.actie').getBoundingClientRect();
      const briefje = document.querySelector('.briefje');
      const kop = document.querySelector('.kop');
      const mid = document.querySelector('.mid');
      const inhoud = briefje || (mid && mid.children.length ? mid : kop);
      const vak = inhoud.getBoundingClientRect();
      return {
        hoog: document.body.scrollHeight,
        inhoudTop: Math.round(vak.top),
        inhoudBodem: Math.round(vak.bottom),
        actieTop: Math.round(actie.top),
        actieBodem: Math.round(actie.bottom),
      };
    });
    const klachten = [];
    if (maat.inhoudTop < 40) klachten.push('de inhoud loopt boven het blad uit');
    if (maat.inhoudBodem > maat.actieTop) klachten.push('de inhoud loopt onder de groene balk');
    if (maat.actieBodem > 1080 || maat.hoog > 1080) klachten.push('het blad is hoger dan 1080');
    console.log(
      blad.bestand.padEnd(38),
      JSON.stringify(maat),
      klachten.length ? 'LET OP: ' + klachten.join(', ') : 'ok'
    );
    if (klachten.length) fout++;
    await pg.screenshot({ path: path.join(UIT, blad.bestand + '.png') });
    await pg.close();
  }
  await b.close();
  if (fout) process.exitCode = 1;
})();

function slug(tekst) {
  return tekst
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}
