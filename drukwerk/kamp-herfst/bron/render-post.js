// Rendert de vierkante post voor sociale media (1080 x 1350 px).
//   PW=$(npm root -g)/playwright node render-post.js
const { chromium } = require(process.env.PW);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/post.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const maat = await p.evaluate(() => {
    const voet = document.querySelector('.voet').getBoundingClientRect();
    const laatste = document.querySelector('.altijd').getBoundingClientRect();
    return { hoogte: document.body.scrollHeight, voetTop: voet.top, inhoudBodem: laatste.bottom };
  });
  console.log(JSON.stringify(maat));
  if (maat.inhoudBodem > maat.voetTop) console.log('LET OP: de inhoud loopt onder de groene balk');
  await p.screenshot({ path: process.env.OUT || '../kamp-herfst-post.png' });
  await b.close();
})();
