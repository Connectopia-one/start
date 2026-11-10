"use client";

import { useEffect, useState } from "react";

/*
  Het bedankje voor wie op de meldknop duwde.

  Kim op 29 september 2026: "kan er als ik klik op afgehandeld bekomen dat er
  bij de persoon die de melding gemaakt word ook een melding komt dat we dit
  bekeken en behandeld hebben?"

  Er vertrekt dus geen mail, net als bij het bericht aan alle ouders: het staat
  bovenaan het platform, bij die ene persoon.

  Kim op 10 november 2026: "als ik ze weg klik blijven ze terug komen [...] na
  1 keer te lezen en weg te klikken moeten deze weg gaan." Wegklikken werd
  eerst enkel in de browser onthouden; op een ander toestel kwam het terug.
  Nu zet het kruisje ook gezien_op bij de melding zelf (app/melding-actions.ts),
  en de startpagina haalt enkel meldingen op die nog niet gezien zijn. De
  browser onthoudt het daarnaast nog, zodat het meteen weg is.

  Meldde iemand hetzelfde hoofdstuk twee keer, dan stonden er twee dezelfde
  bedankjes. Die worden op de startpagina samengenomen tot één bedankje (ids
  bevat dan alle meldingen erachter); wegklikken geldt voor allemaal.

  Zie supabase/melding-antwoord.sql en supabase/melding-gezien.sql.
*/

import { meldingGezien } from "@/app/melding-actions";

export type MeldingAntwoord = {
  id: string;
  /** Alle meldingen achter dit ene bedankje (zelfde hoofdstuk en antwoord). */
  ids: string[];
  antwoord: string | null;
  hoofdstuk: string | null;
};

const SLEUTEL = "connectopia-melding-gezien";

function gezien(): string[] {
  try {
    const rauw = window.localStorage.getItem(SLEUTEL);
    const lijst = rauw ? JSON.parse(rauw) : [];
    return Array.isArray(lijst) ? lijst : [];
  } catch {
    return [];
  }
}

export function MeldingAntwoorden({
  meldingen,
}: {
  meldingen: MeldingAntwoord[];
}) {
  const [weg, setWeg] = useState<string[]>([]);

  // Wat de browser onthoudt, mag pas na het eerste tekenen meespelen: anders
  // verschilt wat de server maakte van wat de browser toont.
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setWeg(gezien());
  }, []);

  function klikWeg(m: MeldingAntwoord) {
    setWeg((vorige) => [...vorige, ...m.ids]);
    void meldingGezien(m.ids);
    try {
      const nieuw = [...gezien(), ...m.ids];
      window.localStorage.setItem(SLEUTEL, JSON.stringify(nieuw.slice(-50)));
    } catch {
      // Geen opslag: dan staat het er de volgende keer weer.
    }
  }

  const tonen = meldingen.filter((m) => !m.ids.some((id) => weg.includes(id)));
  if (tonen.length === 0) return null;

  return (
    <div className="mb-6 space-y-3">
      {tonen.map((m) => (
        <aside
          key={m.id}
          className="rounded-xl border border-forest/30 bg-forest/5 px-5 py-4"
        >
          <div className="flex items-start justify-between gap-4">
            <p className="font-display text-base font-semibold text-ink">
              ✅ Bedankt voor je melding
            </p>
            <button
              type="button"
              onClick={() => klikWeg(m)}
              aria-label="Dit bedankje wegklikken"
              className="shrink-0 rounded-full px-2 py-0.5 text-lg leading-none text-ink-dim hover:bg-forest/10 hover:text-ink"
            >
              &times;
            </button>
          </div>
          <p className="mt-1 text-sm text-ink">
            We hebben ernaar gekeken en het is behandeld
            {m.hoofdstuk ? ` — het ging over ${m.hoofdstuk}` : ""}.
          </p>
          {m.antwoord && (
            <p className="mt-2 whitespace-pre-line rounded-lg bg-surface px-3 py-2 text-sm text-ink">
              {m.antwoord}
            </p>
          )}
        </aside>
      ))}
    </div>
  );
}
