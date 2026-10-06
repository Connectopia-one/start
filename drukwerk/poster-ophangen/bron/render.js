/*
  Maakt de poster als png (scherp), jpg (licht om door te sturen) en pdf,
  op A4. Het script meet zelf of de inhoud niet onder de voettekst schuift.
    node render.js
  Een scherpere afbeelding, bijvoorbeeld om op A3 te laten drukken:
    DSF=3.125 node render.js
*/
const { chromium } = require('/opt/node22/lib/node_modules/playwright');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({
    viewport: { width: 794, height: 1123 },
    deviceScaleFactor: +(process.env.DSF || 2),
  });
  await p.goto('file://' + __dirname + '/poster.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);

  const maat = await p.evaluate(() => {
    const blad = document.getElementById('poster');
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
  });
  console.log(JSON.stringify(maat), maat.tijdOnder < maat.voetBoven ? 'ok' : 'PAST NIET');

  await p.locator('#poster').screenshot({ path: '../poster-connectopia.png' });
  await p.locator('#poster').screenshot({
    path: '../poster-connectopia.jpg',
    type: 'jpeg',
    quality: 88,
  });
  await p.pdf({
    path: '../poster-connectopia-A4.pdf',
    width: '210mm',
    height: '297mm',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await b.close();
})();
