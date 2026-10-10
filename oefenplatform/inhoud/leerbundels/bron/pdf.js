const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const fs = require("fs");
const path = require("path");

/*
  Zet <naam>.html om in <naam>.pdf, en maakt er een png van de eerste bladzijde
  bij om snel te kunnen kijken.

  Formules: een bundel mag \( ... \) en \[ ... \] bevatten, de gewone
  LaTeX-markering (zie oefenplatform/lib/wiskunde.ts). Het html-bestand bewaart
  die markering zoals ze geschreven is; hier wordt ze vlak voor het afdrukken
  getekend met KaTeX. Zo blijft het bronbestand leesbaar en hoeft er niets
  dubbel bijgehouden te worden.

  KaTeX komt uit node_modules van het oefenplatform. Staat die map er niet, dan
  wordt er gewoon niets getekend en krijg je een waarschuwing: een bundel zonder
  formules heeft KaTeX niet nodig en mag daar niet op blijven hangen.
*/
const KATEX = path.join(__dirname, "..", "..", "..", "node_modules", "katex", "dist");

(async () => {
  const naam = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto("file://" + path.join(__dirname, naam + ".html"), {
    waitUntil: "networkidle",
  });

  const bron = await p.content();
  if (bron.includes("\\(") || bron.includes("\\[")) {
    const js = path.join(KATEX, "katex.min.js");
    const auto = path.join(KATEX, "contrib", "auto-render.min.js");
    if (fs.existsSync(js) && fs.existsSync(auto)) {
      // Als inhoud en niet als bestand: een script van schijf laden wordt op
      // een file://-pagina geweigerd.
      await p.addScriptTag({ content: fs.readFileSync(js, "utf8") });
      await p.addScriptTag({ content: fs.readFileSync(auto, "utf8") });
      await p.evaluate(() => {
        window.renderMathInElement(document.body, {
          delimiters: [
            { left: "\\[", right: "\\]", display: true },
            { left: "\\(", right: "\\)", display: false },
          ],
          // Een schrijffout in één formule mag de rest van de bundel niet
          // tegenhouden; ze komt dan in het rood te staan en valt dus op.
          throwOnError: false,
          strict: false,
        });
      });
    } else {
      console.warn(
        `  ! ${naam} bevat formules maar KaTeX staat niet in ${KATEX}.` +
          " Draai `npm install` in de map oefenplatform.",
      );
    }
  }

  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: path.join(__dirname, naam + ".pdf"),
    format: "A4",
    printBackground: true,
  });
  await p.setViewportSize({ width: 794, height: 1123 });
  await p.screenshot({ path: path.join(__dirname, naam + "-p1.png") });
  await b.close();
})();
