/*
  Maakt de flyer op A5 als png, jpg en pdf. Het script meet zelf of de
  inhoud niet onder de groene voettekst schuift.
    node render.js
  Scherper, bijvoorbeeld voor de drukker:
    DSF=4 node render.js
*/
const { chromium } = require('/opt/node22/lib/node_modules/playwright');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({
    viewport: { width: 559, height: 794 },
    deviceScaleFactor: +(process.env.DSF || 3),
  });
  await p.goto('file://' + __dirname + '/flyer.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);

  const maat = await p.evaluate(() => {
    const blad = document.getElementById('flyer');
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

  await p.locator('#flyer').screenshot({ path: '../flyer-stem-naschools.png' });
  await p.locator('#flyer').screenshot({
    path: '../flyer-stem-naschools.jpg',
    type: 'jpeg',
    quality: 88,
  });
  await p.pdf({
    path: '../flyer-stem-naschools-A5.pdf',
    width: '148mm',
    height: '210mm',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await b.close();
})();
