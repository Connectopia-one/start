"use client";

import Link from "next/link";
import { KindKeuze, useActiefKind, type Kind } from "@/components/KindKeuze";
import { vakLabel } from "@/lib/vakbeeld";

export type VakTegel = {
  id: string;
  slug: string;
  naam: string;
  icoon: string;
  /** De hoofdstukken van dit vak binnen dit niveau, in volgorde. */
  hoofdstukIds: string[];
};

/**
 * De vakken van één niveau als knoppen, met per vak hoeveel hoofdstukken het
 * actieve kind er al van gemaakt heeft. Vroeger stond hier één lange lijst met
 * alle hoofdstukken van alle vakken onder elkaar; een kind moest dan eerst
 * voorbij honderd regels scrollen voor het bij zijn vak was.
 */
export function VakTegels({
  niveauSlug,
  vakken,
  kinderen,
}: {
  niveauSlug: string;
  vakken: VakTegel[];
  kinderen: Kind[];
}) {
  const alleIds = vakken.flatMap((v) => v.hoofdstukIds);
  const { actiefKindId, status, kies } = useActiefKind(kinderen, alleIds);

  return (
    <>
      <KindKeuze kinderen={kinderen} actiefKindId={actiefKindId} onKies={kies} />

      {/* Twee naast elkaar, ook op een telefoon: dan zijn het echte knopjes om
          op te tikken in plaats van brede balken onder elkaar. */}
      <div className="mt-6 grid grid-cols-2 gap-3 sm:gap-4 lg:grid-cols-3">
        {vakken.map((vak) => {
          const gemaakt = vak.hoofdstukIds.filter((id) => status.get(id)?.gemaakt).length;
          const totaal = vak.hoofdstukIds.length;
          const deel = totaal ? Math.round((gemaakt / totaal) * 100) : 0;
          return (
            <Link
              key={vak.id}
              href={`/niveaus/${niveauSlug}/${vak.slug}`}
              className="flex flex-col rounded-xl border border-border bg-surface p-4 transition hover:border-forest hover:shadow-sm sm:p-5"
            >
              <span aria-hidden className="text-3xl">
                {vak.icoon}
              </span>
              <span lang="nl" className="mt-2 font-display text-base font-semibold break-words hyphens-auto text-ink sm:text-lg">
                {vakLabel(vak.slug, vak.naam)}
              </span>
              <span className="mt-0.5 text-sm text-ink-dim">
                {totaal} {totaal === 1 ? "hoofdstuk" : "hoofdstukken"}
              </span>

              {/* Het balkje verschijnt pas als we weten wie er oefent: zonder
                  kind zou een lege balk suggereren dat er niets gemaakt is. */}
              {actiefKindId && (
                <span className="mt-3 block">
                  <span className="block h-1.5 w-full overflow-hidden rounded-full bg-border">
                    <span
                      className="block h-full rounded-full bg-forest transition-all"
                      style={{ width: `${deel}%` }}
                    />
                  </span>
                  <span className="mt-1.5 block text-xs text-ink-dim">
                    {gemaakt === 0
                      ? "Nog niet begonnen"
                      : gemaakt === totaal
                        ? "Alles gemaakt 🎉"
                        : `${gemaakt} van de ${totaal} gemaakt`}
                  </span>
                </span>
              )}
            </Link>
          );
        })}
      </div>
    </>
  );
}
