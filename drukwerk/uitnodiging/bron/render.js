/*
  Maakt twee afbeeldingen van één A4 elk, plus één pdf met de twee bladen.
  Het script meet zelf of alles nog op zijn blad past: het laatste blok mag
  niet over de voettekst vallen.
*/
const { chromium } = require('/opt/node22/lib/node_modules/playwright');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({
    viewport: { width: 794, height: 1123 },
    deviceScaleFactor: +(process.env.DSF || 2),
  });
  await p.goto('file://' + __dirname + '/uitnodiging.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);

  for (const id of ['blad1', 'blad2']) {
    const maat = await p.evaluate((id) => {
      const blad = document.getElementById(id);
      const top = blad.getBoundingClientRect().top;
      const blokken = [...blad.children].filter(
        (el) => !el.classList.contains('voet') && el.tagName !== 'svg',
      );
      const laatste = blokken[blokken.length - 1].getBoundingClientRect();
      const voet = blad.querySelector('.voet').getBoundingClientRect();
      return {
        tijdOnder: Math.round(laatste.bottom - top),
        voetBoven: Math.round(voet.top - top),
      };
    }, id);
    console.log(id, JSON.stringify(maat), maat.tijdOnder < maat.voetBoven ? 'ok' : 'PAST NIET');
    const naam = id === 'blad1' ? '1-aanbod' : '2-kampen';
    await p.locator('#' + id).screenshot({ path: `../uitnodiging-${naam}.png` });
    // Dezelfde afbeelding, maar licht genoeg om in een mail te plakken.
    await p.locator('#' + id).screenshot({
      path: `../uitnodiging-${naam}.jpg`,
      type: 'jpeg',
      quality: 88,
    });
  }

  await p.pdf({
    path: '../uitnodiging-najaar-2026.pdf',
    width: '210mm',
    height: '297mm',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await b.close();
})();
