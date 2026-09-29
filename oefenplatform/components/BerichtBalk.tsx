"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

/*
  Het bericht van Kim aan de ouders, bovenaan het platform.

  Kim op 29 september 2026: "ik wou gewoon graag dat we de ouders via het
  platform kunnen een bericht sturen. zoals de feedback van het prikbord ook bij
  hun uitkomt."

  Er vertrekt dus geen mail; het staat in het platform zelf. Wegklikken wordt in
  de browser van de ouder onthouden, per bericht. Kan de browser niets bewaren
  (privévenster), dan staat het er de volgende keer gewoon weer: vervelender dan
  omgekeerd, maar dan mist niemand iets.
*/

export type Bericht = {
  id: string;
  titel: string;
  tekst: string;
  link: string | null;
  linktekst: string | null;
};

const SLEUTEL = "connectopia-bericht-weg";

function alWeggeklikt(id: string) {
  try {
    const rauw = window.localStorage.getItem(SLEUTEL);
    const lijst = rauw ? JSON.parse(rauw) : [];
    return Array.isArray(lijst) && lijst.includes(id);
  } catch {
    return false;
  }
}

export function BerichtBalk({ bericht }: { bericht: Bericht }) {
  const [weg, setWeg] = useState(false);

  // Wat de browser onthoudt, mag pas na het eerste tekenen meespelen: anders
  // verschilt wat de server maakte van wat de browser toont.
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setWeg(alWeggeklikt(bericht.id));
  }, [bericht.id]);

  function klikWeg() {
    setWeg(true);
    try {
      const rauw = window.localStorage.getItem(SLEUTEL);
      const lijst = rauw ? JSON.parse(rauw) : [];
      const nieuw = Array.isArray(lijst)
        ? [...lijst, bericht.id]
        : [bericht.id];
      window.localStorage.setItem(SLEUTEL, JSON.stringify(nieuw.slice(-30)));
    } catch {
      // Geen opslag: dan staat het er de volgende keer weer.
    }
  }

  if (weg) return null;

  return (
    <aside className="mb-6 rounded-xl border border-amber/50 bg-amber/10 px-5 py-4">
      <div className="flex items-start justify-between gap-4">
        <p className="font-display text-base font-semibold text-ink">
          📣 {bericht.titel}
        </p>
        <button
          type="button"
          onClick={klikWeg}
          aria-label="Dit bericht wegklikken"
          className="shrink-0 rounded-full px-2 py-0.5 text-lg leading-none text-ink-dim hover:bg-amber/20 hover:text-ink"
        >
          &times;
        </button>
      </div>
      <p className="mt-1 whitespace-pre-line text-sm text-ink">
        {bericht.tekst}
      </p>
      {bericht.link && (
        <p className="mt-3">
          <Link
            href={bericht.link}
            className="inline-block rounded-full bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
          >
            {bericht.linktekst || "Bekijken"} &rarr;
          </Link>
        </p>
      )}
    </aside>
  );
}
