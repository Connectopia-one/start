"use client";

import Link from "next/link";
import { KindKeuze, useActiefKind, type Kind } from "@/components/KindKeuze";

export type HoofdstukTegel = {
  id: string;
  titel: string;
  volgnummer: number;
  gratis: boolean;
  /** Mag dit kind erin? Vrijgegeven of gratis. */
  mag: boolean;
};

/**
 * Het uitdagingshoofdstuk van een vak: één hoofdstuk dat alle andere door
 * elkaar haalt, met moeilijkere vragen. Het staat altijd achteraan en krijgt
 * een eigen kleurtje, zodat het opvalt zonder een extra kolom in de databank.
 */
function isUitdaging(titel: string) {
  return titel.trim().toLowerCase().startsWith("uitdaging");
}

/**
 * De hoofdstukken van één vak als vakjes in plaats van als lijst, met per
 * vakje of het actieve kind het al gemaakt heeft. Een hoofdstuk mag zo vaak
 * opnieuw als een kind wil, dus "gemaakt" is een geruststelling en geen slot.
 */
export function HoofdstukTegels({
  vakSlug,
  hoofdstukken,
  kinderen,
}: {
  vakSlug: string;
  hoofdstukken: HoofdstukTegel[];
  kinderen: Kind[];
}) {
  const { actiefKindId, status, kies } = useActiefKind(
    kinderen,
    hoofdstukken.map((h) => h.id)
  );

  const gemaakt = hoofdstukken.filter((h) => status.get(h.id)?.gemaakt).length;

  const opVolgorde = [...hoofdstukken].sort(
    (a, b) => Number(isUitdaging(a.titel)) - Number(isUitdaging(b.titel))
  );

  return (
    <>
      <KindKeuze kinderen={kinderen} actiefKindId={actiefKindId} onKies={kies} />

      {actiefKindId && (
        <p className="mt-4 text-sm text-ink-dim">
          {gemaakt === 0
            ? "Nog geen enkel hoofdstuk gemaakt. Kies er eentje om te starten."
            : `Al ${gemaakt} van de ${hoofdstukken.length} hoofdstukken gemaakt. Je mag ze zo vaak opnieuw doen als je wil.`}
        </p>
      )}

      <div className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {opVolgorde.map((h) => {
          const s = status.get(h.id);
          const uitdaging = isUitdaging(h.titel);
          return (
            <Link
              key={h.id}
              href={`/vakken/${vakSlug}/${h.volgnummer}`}
              className={`relative flex min-h-[6rem] flex-col rounded-xl border bg-surface p-4 transition hover:shadow-sm ${
                uitdaging
                  ? "border-amber/50 hover:border-amber"
                  : s?.gemaakt
                    ? "border-forest/40 hover:border-forest"
                    : "border-border hover:border-forest"
              }`}
            >
              {/* Het merkteken zweeft in de hoek in plaats van in een eigen
                  regel te staan: zo begint elk vakje met zijn titel, ook de
                  vakjes die nog geen teken hebben. */}
              {s?.perfect ? (
                <span aria-hidden title="Foutloos gemaakt" className="absolute right-3 top-3 text-lg">
                  ⭐
                </span>
              ) : s?.gemaakt ? (
                <span aria-hidden title="Al gemaakt" className="absolute right-3 top-3 text-lg">
                  ✅
                </span>
              ) : null}

              <span className={`flex-1 text-sm font-medium text-ink ${s?.gemaakt ? "pr-7" : ""}`}>
                {h.titel}
              </span>

              <span className="mt-3 flex flex-wrap items-center gap-2">
                {uitdaging ? (
                  <span className="rounded-full bg-amber/15 px-2.5 py-0.5 text-xs font-medium text-amber">
                    Extra uitdaging
                  </span>
                ) : null}
                {h.gratis ? (
                  <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                    Gratis
                  </span>
                ) : h.mag ? (
                  <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                    Vrijgegeven
                  </span>
                ) : (
                  <span className="rounded-full bg-ink-dim/10 px-2.5 py-0.5 text-xs font-medium text-ink-dim">
                    Op slot
                  </span>
                )}
                {s?.perfect ? (
                  <span className="text-xs text-forest-dark">Foutloos</span>
                ) : s?.gemaakt ? (
                  <span className="text-xs text-ink-dim">Al gemaakt</span>
                ) : null}
              </span>
            </Link>
          );
        })}
      </div>
    </>
  );
}
