// Drukt kalender.html af als pdf in de map erboven.
//   PW=$(npm root -g)/playwright node render.js
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'kalender.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const uit = path.join(__dirname, '..', 'social-media-kalender.pdf');
  await p.pdf({ path: uit, format: 'A4', printBackground: true });
  await b.close();
  console.log('geschreven:', uit);
})();
