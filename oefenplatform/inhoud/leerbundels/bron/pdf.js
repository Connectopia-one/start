const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const path = require("path");
(async () => {
  const naam = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto("file://" + path.join(__dirname, naam + ".html"), { waitUntil: "networkidle" });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, naam + ".pdf"), format: "A4", printBackground: true });
  // ook een png van de eerste pagina, om snel te kunnen kijken
  await p.setViewportSize({ width: 794, height: 1123 });
  await p.screenshot({ path: path.join(__dirname, naam + "-p1.png") });
  await b.close();
})();
