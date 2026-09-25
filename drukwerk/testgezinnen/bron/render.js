const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: +(process.env.DSF || 2) });
  await p.goto('file://' + __dirname + '/brief.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const maat = await p.evaluate(() => {
    const laatste = document.querySelector('.tijd').getBoundingClientRect();
    const voet = document.querySelector('.voet').getBoundingClientRect();
    return { tijdOnder: Math.round(laatste.bottom), voetBoven: Math.round(voet.top), hoogte: document.body.scrollHeight };
  });
  console.log(JSON.stringify(maat));
  await p.screenshot({ path: '../welkomstbrief-testgezinnen.png' });
  await p.pdf({ path: '../welkomstbrief-testgezinnen.pdf', width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
