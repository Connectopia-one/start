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
    <>
      {splitsWiskunde(tekst).map((stuk, i) =>
        stuk.soort === "tekst" ? (
          <span key={i}>{stuk.tekst}</span>
        ) : (
          <span
            key={i}
            className={stuk.blok ? "my-2 block overflow-x-auto" : className}
            /* De html komt van KaTeX zelf, uit de latex hierboven; de gewone
               tekst eromheen gaat door React en wordt dus ontsmet. */
            dangerouslySetInnerHTML={{ __html: teken(stuk.latex, stuk.blok) }}
          />
        ),
      )}
    </>
  );
}
