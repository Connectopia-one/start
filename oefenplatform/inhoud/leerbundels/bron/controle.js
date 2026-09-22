/*
  Kijkt een bundel na op bladspiegel, vóór je hem levert.

      node controle.js mesopotamie-en-egypte

  Drie dingen die je met het blote oog makkelijk mist:
    1. een figuur of kader dat hoger is dan één blad, en dus nooit heel past;
    2. gewone tekst die buiten haar vakje loopt (scrollWidth > clientWidth);
    3. tekst in een SVG die buiten de viewBox valt. Die wordt NIET afgeknipt en
       geeft dus ook geen scrollWidth — zo liep de legende van de tijdlijn ooit
       ongemerkt van het blad. Daarvoor is getBBox nodig.

  Het printbaar vlak is 688 x 1009 px: A4 met @page margin 16mm 14mm 14mm 14mm.
*/
const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const path = require("path");

const BREED = 688;
const HOOG = 1009;

(async () => {
  const naam = process.argv[2];
  if (!naam) {
    console.error("Gebruik: node controle.js <bundelnaam>");
    process.exit(2);
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: BREED, height: HOOG } });
  await page.emulateMedia({ media: "print" });
  await page.goto("file://" + path.join(__dirname, naam + ".html"), { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);

  const klachten = await page.evaluate((hoog) => {
    const uit = [];
    const kort = (el) => (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 70);

    for (const el of document.querySelectorAll("figure, .kader, table")) {
      const h = el.getBoundingClientRect().height;
      if (h > hoog) uit.push(`te hoog voor één blad (${Math.round(h)}px): ${kort(el)}`);
    }

    for (const el of document.querySelectorAll("p, li, td, th, h1, h2, h3, figcaption")) {
      if (el.scrollWidth > el.clientWidth + 1) uit.push(`loopt buiten haar vakje: ${kort(el)}`);
    }

    for (const svgEl of document.querySelectorAll("svg")) {
      const vb = svgEl.viewBox?.baseVal;
      if (!vb || !vb.width) continue;
      for (const kind of svgEl.querySelectorAll("text, tspan")) {
        let doos;
        try {
          doos = kind.getBBox();
        } catch {
          continue;
        }
        if (!doos.width) continue;
        const marge = 0.5;
        if (
          doos.x < vb.x - marge ||
          doos.y < vb.y - marge ||
          doos.x + doos.width > vb.x + vb.width + marge ||
          doos.y + doos.height > vb.y + vb.height + marge
        ) {
          uit.push(`svg-tekst valt buiten de viewBox: "${(kind.textContent || "").trim()}"`);
        }
      }
    }
    return uit;
  }, HOOG);

  const bladen = await page.evaluate((hoog) => Math.ceil(document.body.scrollHeight / hoog), HOOG);
  await browser.close();

  if (klachten.length === 0) {
    console.log(`${naam}: in orde, ${bladen} blz.`);
  } else {
    console.log(`${naam}: ${klachten.length} probleem(en), ${bladen} blz.`);
    for (const k of klachten) console.log("  -", k);
    process.exit(1);
  }
})();
