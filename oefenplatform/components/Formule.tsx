"use client";

/*
  Een stuk tekst waar formules in kunnen staan, getekend met KaTeX.

  Zie lib/wiskunde.ts voor hoe je een formule schrijft en waarom ze bestaat.

  Gebruik het overal waar tekst uit de databank op het scherm komt:

      <Formule tekst={vraag.uitleg} />

  Staat er geen formule in de tekst, dan is dit gewoon de tekst en gebeurt er
  niets extra. KaTeX zelf zit in de brok javascript van de oefenpagina's, dus
  een kind dat nederlands oefent haalt die niet binnen.

  De formule wordt op de server al getekend, zodat ze meteen juist op het
  scherm staat en niet eerst even als \sqrt{50} voorbijflitst.
*/

import katex from "katex";
import { splitsWiskunde, bevatWiskunde } from "@/lib/wiskunde";

/*
  Een formule met een schrijffout mag de pagina niet platleggen: een kind dat
  oefent, heeft niets aan een wit scherm. throwOnError false laat KaTeX de
  formule dan in het rood tonen, en zo zien we meteen waar het misloopt.
*/
function teken(latex: string, blok: boolean): string {
  return katex.renderToString(latex, {
    displayMode: blok,
    throwOnError: false,
    strict: false,
    output: "html",
  });
}

/*
  Hetzelfde, maar voor een stuk html dat al klaarstaat: de blokjes van de tocht
  komen als html uit onze eigen bronbestanden (zie InteractieveLeerbundel.tsx).
  Daar kan geen <Formule> tussen, dus wordt de latex hier in die html vervangen
  door wat KaTeX ervan maakt.
*/
export function formulesInHtml(html: string): string {
  if (!bevatWiskunde(html)) return html;
  return splitsWiskunde(html)
    .map((stuk) =>
      stuk.soort === "tekst"
        ? stuk.tekst
        : teken(stuk.latex, stuk.blok),
    )
    .join("");
}

/*
  Hoe lang een formule mag zijn voor ze haar eigen schuifruimte krijgt.

  Een korte formule (p, \\neg p, \\sqrt{50}) hoort gewoon in de zin te staan,
  op dezelfde schrijflijn als de letters eromheen. Een lange formule, zoals de
  uitgewerkte berekening van een elektrische veldsterkte, is op een gsm breder
  dan het scherm; die krijgt een eigen kadertje waarin je opzij kan schuiven,
  zodat niet de hele pagina meeschuift.
*/
const LANG = 30;

export function Formule({
  tekst,
  className,
}: {
  tekst: string | null | undefined;
  className?: string;
}) {
  if (!tekst) return null;
  if (!bevatWiskunde(tekst)) return <>{tekst}</>;

  return (
    /*
      Alles zit in één span, en dat is niet zomaar netjes: een <Formule> staat
      vaak in een label of een knop die met flex is opgemaakt (zie Quiz.tsx).
      Gaven we hier losse spans terug, dan werd elk stuk tekst en elke formule
      een eigen vak in die rij, en brak een antwoord als "de implicatie: als p
      waar is, dan volgt er iets anders uit" op een gsm in drie smalle kolommen
      naast elkaar. Kim meldde dat op 11 oktober 2026. Met één span eromheen is
      het weer één lopende zin.
    */
    <span className={className}>
      {splitsWiskunde(tekst).map((stuk, i) =>
        stuk.soort === "tekst" ? (
          stuk.tekst
        ) : stuk.blok ? (
          <span
            key={i}
            className="my-2 block overflow-x-auto"
            dangerouslySetInnerHTML={{ __html: teken(stuk.latex, true) }}
          />
        ) : stuk.latex.length > LANG ? (
          <span
            key={i}
            className="inline-block max-w-full overflow-x-auto align-middle"
            dangerouslySetInnerHTML={{ __html: teken(stuk.latex, false) }}
          />
        ) : (
          /*
            Geen inline-block en geen vertical-align hier: een vakje met
            overflow krijgt zijn schrijflijn onderaan in plaats van op de
            lijn van de letters, en dan zweefde het teken \neg boven de zin.
            Een gewone span laat KaTeX zelf op de juiste lijn staan.
          */
          <span
            key={i}
            dangerouslySetInnerHTML={{ __html: teken(stuk.latex, false) }}
          />
        ),
      )}
    </span>
  );
}
