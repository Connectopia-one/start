/*
  Maakt de poster als png (scherp), jpg (licht om door te sturen) en pdf, op A4.

    node render.js
    DSF=3.125 node render.js     # scherper, voor wie op A3 laat drukken

  Het blad is een flexkolom met een rekstrook boven de voet, dus te veel inhoud
  schuift niet zichtbaar over de rand: ze wordt afgesneden. Daarom meet dit
  script twee dingen in plaats van één. `rek` is de witruimte die overblijft
  boven de groene voet; zakt die naar 0, dan is het blad vol. `teveel` is wat
  er buiten het blad valt; staat daar iets anders dan 0, dan is er al tekst weg.
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
    const rek = blad.querySelector('.rek').getBoundingClientRect();
    return {
      rek: Math.round(rek.height),
      teveel: Math.round(blad.scrollHeight - blad.clientHeight),
    };
  });
  const past = maat.teveel === 0 && maat.rek >= 0;
  console.log(JSON.stringify(maat), past ? 'ok' : 'PAST NIET');

  await p.locator('#poster').screenshot({ path: '../poster-richtingen.png' });
  await p.locator('#poster').screenshot({
    path: '../poster-richtingen.jpg',
    type: 'jpeg',
    quality: 88,
  });
  await p.pdf({
    path: '../poster-richtingen-A4.pdf',
    width: '210mm',
    height: '297mm',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await b.close();
})();
