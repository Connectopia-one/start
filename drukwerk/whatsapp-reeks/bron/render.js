/*
  Maakt zes staande beelden van 1080 x 1350 om via whatsapp door te sturen.
  Het script kijkt per beeld of de inhoud er nog op past.
    node render.js
*/
const { chromium } = require('/opt/node22/lib/node_modules/playwright');

const NAMEN = {
  b1: '1-wie-we-zijn',
  b2: '2-waarom',
  b3: '3-aanbod-week',
  b4: '4-aanbod-weekend',
  b5: '5-kampen',
  b6: '6-zo-begin-je',
};

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + __dirname + '/reeks.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);

  for (const [id, naam] of Object.entries(NAMEN)) {
    const maat = await p.evaluate((id) => {
      const beeld = document.getElementById(id);
      const binnen = beeld.querySelector('.binnen');
      const vak = binnen.getBoundingClientRect();
      const laatste = binnen.lastElementChild.getBoundingClientRect();
      return {
        tijdOnder: Math.round(laatste.bottom - vak.top),
        plaats: Math.round(vak.height),
      };
    }, id);
    console.log(id, JSON.stringify(maat), maat.tijdOnder <= maat.plaats ? 'ok' : 'PAST NIET');
    await p.locator('#' + id).screenshot({ path: `../gsm/connectopia-${naam}.jpg`, type: 'jpeg', quality: 90 });
  }

  /* Dezelfde zes beelden, maar op verhaalformaat (1080 x 1920). */
  await p.setViewportSize({ width: 1080, height: 1920 });
  await p.evaluate(() => document.body.classList.add('verhaal'));
  await p.waitForTimeout(300);
  for (const [id, naam] of Object.entries(NAMEN)) {
    const maat = await p.evaluate((id) => {
      const binnen = document.getElementById(id).querySelector('.binnen');
      const vak = binnen.getBoundingClientRect();
      const laatste = binnen.lastElementChild.getBoundingClientRect();
      return {
        tijdOnder: Math.round(laatste.bottom - vak.top),
        plaats: Math.round(vak.height),
      };
    }, id);
    console.log('verhaal', id, JSON.stringify(maat), maat.tijdOnder <= maat.plaats ? 'ok' : 'PAST NIET');
    await p.locator('#' + id).screenshot({ path: `../verhaal/connectopia-${naam}.jpg`, type: 'jpeg', quality: 90 });
  }

  await b.close();
})();
