const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: +(process.env.DSF || 2) });
  await p.goto('file://' + __dirname + '/nieuwsbrief.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const maat = await p.evaluate(() => {
    // het laatste blok in de gewone stroom, wat dat ook is
    const blokken = [...document.body.children].filter((el) => !el.classList.contains('voet') && el.tagName !== 'svg');
    const laatste = blokken[blokken.length - 1].getBoundingClientRect();
    const voet = document.querySelector('.voet').getBoundingClientRect();
    return { tijdOnder: Math.round(laatste.bottom), voetBoven: Math.round(voet.top), hoogte: document.body.scrollHeight };
  });
  console.log(JSON.stringify(maat), maat.tijdOnder < maat.voetBoven ? 'ok' : 'PAST NIET');
  await p.screenshot({ path: '../nieuwsbrief-najaar-2026.png' });
  await p.pdf({ path: '../nieuwsbrief-najaar-2026.pdf', width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
