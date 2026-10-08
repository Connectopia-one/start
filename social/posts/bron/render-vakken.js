/*
  Maakt van vakkenoverzicht.html een beeld van 1080 x 1620 in de map erboven.

      python3 -I maak_vakkenoverzicht.py
      PW=$(npm root -g)/playwright node render-vakken.js

  Apart van render.js, want dat script maakt vierkante posts van 1080 x 1080
  en deze poster is een lijst: die moet hoger zijn om leesbaar te blijven op
  een gsm. Het script waarschuwt zelf als de inhoud buiten het blad valt;
  staat er LET OP, maak het blad dan hoger of de letters kleiner.
*/
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const path = require('path');

const BREED = 1080;
const HOOG = 1920;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: BREED, height: HOOG }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'vakkenoverzicht.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  const maten = await page.evaluate(() => ({
    hoogte: document.querySelector("footer").getBoundingClientRect().bottom + 50,
    breedte: 1080,
    onder: document.querySelector('footer').getBoundingClientRect().bottom,
  }));
  if (maten.hoogte > HOOG + 1 || maten.breedte > BREED + 1 || maten.onder > HOOG) {
    console.log(`LET OP: de inhoud is ${maten.hoogte} px hoog en ${maten.breedte} px breed, ` +
                `de voettekst eindigt op ${Math.round(maten.onder)}. Het blad is ${BREED} x ${HOOG}.`);
  } else {
    console.log(`past: ${maten.hoogte} x ${maten.breedte}, voettekst eindigt op ${Math.round(maten.onder)}`);
  }

  const uit = path.join(__dirname, '..', 'vakkenoverzicht.png');
  await page.screenshot({ path: uit });
  await browser.close();
  console.log(uit);
})();
