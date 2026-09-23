// Rendert één bladzijde van de flyer naar png en pdf (A5, 148 x 210 mm).
//   PW=$(npm root -g)/playwright HTML=voor.html OUT=../flyer-professionals-voor.png PDF=voor.pdf DSF=3.125 node render.js
const { chromium } = require(process.env.PW);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({
    viewport: { width: 559, height: 794 },
    deviceScaleFactor: +(process.env.DSF || 1),
  });
  await p.goto('file://' + __dirname + '/' + (process.env.HTML || 'voor.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  // kijkt of de inhoud binnen de bladzijde blijft en niet onder de voettekst schuift
  const maat = await p.evaluate(() => {
    const voet = document.querySelector('.voet').getBoundingClientRect();
    const laatste = [...document.querySelectorAll('body > section')].pop().getBoundingClientRect();
    return { hoogte: document.body.scrollHeight, voetTop: voet.top, inhoudBodem: laatste.bottom };
  });
  console.log(JSON.stringify(maat));
  if (maat.inhoudBodem > maat.voetTop) console.log('LET OP: de inhoud loopt onder de voettekst');
  if (maat.hoogte > 795) console.log('LET OP: de bladzijde is te hoog');
  await p.screenshot({ path: process.env.OUT || 'preview.png' });
  if (process.env.PDF) {
    await p.pdf({ path: process.env.PDF, width: '148mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  }
  await b.close();
})();
