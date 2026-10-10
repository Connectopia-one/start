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

      /*
        Een formule mag nooit breder worden dan de kolom waarin ze staat.
        Op het antwoordblad staan twee smalle kolommen naast elkaar, en een
        te brede formule schoof daar gewoon over de buurkolom heen. Omdat
        .katex op nowrap staat (een formule mag niet middenin afbreken),
        lost afbreken dat niet op: wat te breed is, wordt hier kleiner
        gezet. Tot 60 procent; blijft ze dan nog te breed, dan is de opgave
        zelf te lang en moet ze korter geschreven worden.
      */
      /*
        Meten moet op de breedte van een blad gebeuren, niet op die van het
        browservenster. Dat venster is standaard 1280 px breed; daar paste
        elke formule, dus werd er niets verkleind, en p.pdf() zette de
        bladzijde daarna zelf opnieuw op A4, waar ze alsnog over de
        buurkolom schoof. 688 px is 182 mm bij 96 dpi: A4 min de marges van
        @page in stijl.css.
      */
      await p.emulateMedia({ media: "print" });
      await p.setViewportSize({ width: 688, height: 1123 });

      await p.evaluate(() => {
        for (const el of document.querySelectorAll(".katex")) {
          let ouder = el.parentElement;
          while (ouder && !ouder.clientWidth) ouder = ouder.parentElement;
          if (!ouder) continue;
          /*
            clientWidth telt de binnenmarge mee. Op het antwoordblad staat
            elk nummer in de marge van 30 px, en een formule die op een
            volgende regel begint start dus 30 px verder. Reken je met de
            volle clientWidth, dan steekt ze precies die 30 px uit.
          */
          const vorm = getComputedStyle(ouder);
          const ruimte =
            ouder.clientWidth -
            parseFloat(vorm.paddingLeft || 0) -
            parseFloat(vorm.paddingRight || 0);
          /*
            De hoogte van de doos opmeten helpt niet. Een formule op haar
            eigen regel krijgt van KaTeX een blok dat precies zo breed is
            als de kolom, en elk element daarbinnen ook; wat eruit steekt
            zijn de letters zelf. Daarom wordt hier gemeten waar de inhoud
            staat en niet waar de doos eindigt. Enkel binnen .katex-html:
            daarnaast zet KaTeX dezelfde formule nog eens in MathML, voor
            wie voorleessoftware gebruikt, en die telt anders mee.
          */
          const bereik = document.createRange();
          bereik.selectNodeContents(el.querySelector(".katex-html") || el);
          let links = Infinity;
          let rechts = -Infinity;
          for (const vak of bereik.getClientRects()) {
            links = Math.min(links, vak.left);
            rechts = Math.max(rechts, vak.right);
          }
          const breed = Math.max(
            el.getBoundingClientRect().width,
            rechts > links ? rechts - links : 0,
          );
          if (breed > ruimte && ruimte > 0) {
            /*
              In pixels en niet in procent. Een formule op haar eigen regel
              staat bij KaTeX al op 1,21 em; zet je daar een percentage
              overheen, dan gooi je die 1,21 weg en wordt ze veel kleiner
              dan nodig.
            */
            const nu = parseFloat(getComputedStyle(el).fontSize);
            el.style.display = "inline-block";
            el.style.fontSize =
              Math.max(nu * 0.6, nu * (ruimte / breed) * 0.97) + "px";
          }
        }
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
  await p.emulateMedia({ media: "screen" });
  await p.setViewportSize({ width: 794, height: 1123 });
  await p.screenshot({ path: path.join(__dirname, naam + "-p1.png") });
  await b.close();
})();
