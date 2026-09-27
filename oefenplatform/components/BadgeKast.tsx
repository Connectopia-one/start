"use client";

import { useEffect, useState } from "react";
import { haalTelling } from "@/app/voortgang-actions";
import { bewaarActiefKind, leesActiefKind } from "@/lib/actiefkind";
import { LEGE_TELLING, badges, verdiend, type Telling } from "@/lib/badges";

type Kind = { id: string; naam: string };

/**
 * De verzameling van één kind.
 *
 * Welk kind er kijkt staat in de browser, net als bij het oefenen zelf (zie
 * lib/actiefkind.ts), dus de telling wordt pas na het laden opgehaald. Tot dan
 * staat de kast er gewoon leeg bij: de badges komen erbij, de pagina hoeft er
 * niet op te wachten.
 */
export function BadgeKast({ kinderen }: { kinderen: Kind[] }) {
  const [kindId, setKindId] = useState<string | null>(null);
  const [telling, setTelling] = useState<Telling>(LEGE_TELLING);
  // Voor welk kind de telling binnen is. Hieruit volgt of we nog bezig zijn,
  // zodat het effect zelf geen state hoeft te zetten om dat te melden.
  const [geteldVoor, setGeteldVoor] = useState<string | null>(null);

  useEffect(() => {
    if (!kinderen.length) return;
    const bewaard = leesActiefKind();
    const geldig = bewaard && kinderen.some((k) => k.id === bewaard);
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setKindId(geldig ? bewaard : kinderen[0].id);
  }, [kinderen]);

  useEffect(() => {
    if (!kindId) return;
    let geannuleerd = false;
    haalTelling(kindId)
      .then((t) => {
        if (geannuleerd) return;
        setTelling(t);
        setGeteldVoor(kindId);
      })
      .catch(() => {
        // Lukt het tellen niet, dan blijft de kast leeg staan in plaats van
        // eeuwig "even tellen" te tonen.
        if (!geannuleerd) setGeteldVoor(kindId);
      });
    return () => {
      geannuleerd = true;
    };
  }, [kindId]);

  const kies = (id: string) => {
    setTelling(LEGE_TELLING);
    setGeteldVoor(null);
    setKindId(id);
    bewaarActiefKind(id);
  };

  const bezig = kindId !== null && geteldVoor !== kindId;
  const lijst = badges(telling);
  const aantal = lijst.filter(verdiend).length;

  return (
    <>
      {kinderen.length > 1 && (
        <div className="mt-6 flex flex-wrap items-center gap-2">
          <span className="text-sm text-ink-dim">Wie kijkt er?</span>
          {kinderen.map((k) => (
            <button
              key={k.id}
              type="button"
              onClick={() => kies(k.id)}
              className={`rounded-full px-3 py-1 text-sm transition ${
                k.id === kindId
                  ? "bg-forest text-white"
                  : "border border-border bg-surface text-ink hover:border-forest"
              }`}
            >
              {k.naam}
            </button>
          ))}
        </div>
      )}

      <p className="mt-6 text-sm text-ink-dim">
        {bezig ? "Even tellen…" : `${aantal} van de ${lijst.length} verdiend.`}
      </p>

      <div className="mt-4 grid gap-3 sm:grid-cols-2">
        {lijst.map((badge) => {
          const klaar = verdiend(badge);
          const deel = Math.min(1, badge.doel > 0 ? badge.nu / badge.doel : 0);
          return (
            <div
              key={badge.sleutel}
              className={`rounded-xl border p-4 ${
                klaar ? "border-amber/50 bg-amber/5" : "border-border bg-surface"
              }`}
            >
              <div className="flex items-start gap-3">
                {/* Een badge die nog niet verdiend is, staat er grijs bij in
                    plaats van verborgen: dan weet een kind wat er te halen valt. */}
                <span className={`text-2xl ${klaar ? "" : "opacity-30 grayscale"}`} aria-hidden>
                  {badge.emoji}
                </span>
                <div className="min-w-0 flex-1">
                  <p className={`font-display font-semibold ${klaar ? "text-ink" : "text-ink-dim"}`}>
                    {badge.naam}
                  </p>
                  <p className="text-sm text-ink-dim">{badge.uitleg}</p>

                  {!klaar && badge.doel > 1 && (
                    <div className="mt-2">
                      <div className="h-1.5 w-full overflow-hidden rounded-full bg-border">
                        <div
                          className="h-full rounded-full bg-forest"
                          style={{ width: `${Math.round(deel * 100)}%` }}
                        />
                      </div>
                      <p className="mt-1 text-xs text-ink-dim">
                        {badge.nu} van de {badge.doel}
                      </p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
}
