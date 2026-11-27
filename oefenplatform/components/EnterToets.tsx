"use client";

import { useEffect, useRef } from "react";

/*
  Enter werkt bij élke soort vraag, niet alleen in het invulvakje.

  Febe meldde op 6 oktober 2026: "Fijn dat ik al 1 vraag met een enter kon
  indienen. Maar helaas kan ik het niet overal doen." Bij een meerkeuzevraag
  staat er geen invulvakje, dus was er niets dat enter opving.

  Dit onderdeel toont zelf niets; het luistert alleen naar de entertoets en
  doet dan wat de quiz meegeeft: de vraag nakijken, of naar de volgende gaan.

  27 november 2026: ook de knoppen Waar en Niet waar (data-keuze) laten enter
  door. Wie Waar aanklikt, staat met de focus op die knop; enter klikte dan
  gewoon nog eens op Waar in plaats van na te kijken. Ook de vraag van de dag
  gebruikt dit nu.

  Een knop, een link, een invulvakje, een keuzelijst of iets in een formulier
  (het meldvakje) regelt enter zelf; daar blijven we af. Aankruisvakjes en
  bolletjes niet: die doen uit zichzelf niets met enter.
*/
export function EnterToets({ doe }: { doe: () => void }) {
  const laatste = useRef(doe);
  useEffect(() => {
    laatste.current = doe;
  });
  useEffect(() => {
    function opToets(e: KeyboardEvent) {
      if (e.key !== "Enter" || e.repeat) return;
      const doel = e.target as HTMLElement | null;
      const soort = doel?.tagName;
      const tekstvak =
        soort === "INPUT" &&
        !["radio", "checkbox"].includes((doel as HTMLInputElement).type);
      if (
        (soort === "BUTTON" && !doel?.hasAttribute("data-keuze")) ||
        soort === "A" ||
        soort === "TEXTAREA" ||
        soort === "SELECT" ||
        tekstvak ||
        doel?.closest("form")
      ) {
        return;
      }
      e.preventDefault();
      laatste.current();
    }
    window.addEventListener("keydown", opToets);
    return () => window.removeEventListener("keydown", opToets);
  }, []);
  return null;
}
