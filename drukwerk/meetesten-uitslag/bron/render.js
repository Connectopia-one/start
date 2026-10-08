const { chromium } = require('/opt/node22/lib/node_modules/playwright');

/* Twee bladen A4: de brief voor wie geselecteerd is, en die voor wie dat niet
   is maar drie dagen mag proeven. Draaien met: node bron/render.js */
const bladen = [
  { bron: 'gekozen.html', uit: 'meetesten-gekozen' },
  { bron: 'niet-gekozen.html', uit: 'meetesten-drie-dagen' },
];

(async () => {
  const b = await chromium.launch();
  for (const blad of bladen) {
    const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: +(process.env.DSF || 2) });
    await p.goto('file://' + __dirname + '/' + blad.bron);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(400);
    const maat = await p.evaluate(() => {
      // het laatste blok in de gewone stroom, wat dat ook is
      const blokken = [...document.body.children].filter((el) => !el.classList.contains('voet') && el.tagName !== 'svg');
      const laatste = blokken[blokken.length - 1].getBoundingClientRect();
      const voet = document.querySelector('.voet').getBoundingClientRect();
      return { tijdOnder: Math.round(laatste.bottom), voetBoven: Math.round(voet.top), hoogte: document.body.scrollHeight };
    });
    console.log(blad.uit.padEnd(24), JSON.stringify(maat), maat.tijdOnder < maat.voetBoven ? 'ok' : 'PAST NIET');
    await p.screenshot({ path: __dirname + '/../' + blad.uit + '.png' });
    await p.pdf({ path: __dirname + '/../' + blad.uit + '.pdf', width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
    await p.close();
  }
  await b.close();
})();
