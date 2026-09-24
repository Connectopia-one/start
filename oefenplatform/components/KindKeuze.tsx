"use client";

import { useEffect, useState } from "react";
import { bewaarActiefKind, leesActiefKind } from "@/lib/actiefkind";
import { haalHoofdstukStatus, type HoofdstukStatus } from "@/app/voortgang-actions";

export type Kind = { id: string; naam: string };

/**
 * Houdt bij welk kind aan het oefenen is, en haalt op wat dat kind van deze
 * hoofdstukken al gemaakt heeft.
 *
 * De keuze staat in de browser (zie lib/actiefkind.ts), dus de server kan ze
 * niet meegeven bij het opbouwen van de pagina. Daarom halen we de voortgang
 * pas na het laden op. Zolang dat loopt tonen we gewoon niets extra: de lijst
 * is meteen bruikbaar, de vinkjes komen erbij.
 */
export function useActiefKind(kinderen: Kind[], hoofdstukIds: string[]) {
  const [actiefKindId, setActiefKindId] = useState<string | null>(null);
  const [status, setStatus] = useState<Map<string, HoofdstukStatus>>(new Map());

  useEffect(() => {
    if (!kinderen.length) return;
    const opgeslagen = leesActiefKind();
    const geldig = opgeslagen && kinderen.some((k) => k.id === opgeslagen);
    // Synchroniseert met localStorage (een externe bron) na mount — bewust hier,
    // niet in de initializer, om een server/client-mismatch te vermijden.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setActiefKindId(geldig ? opgeslagen : kinderen[0].id);
  }, [kinderen]);

  // De lijst hoofdstukken is per pagina vast; we hangen het effect aan de
  // samengevoegde sleutel zodat het niet bij elke render opnieuw loopt.
  const sleutel = hoofdstukIds.join(",");
  useEffect(() => {
    if (!actiefKindId || !sleutel) return;
    let geannuleerd = false;
    haalHoofdstukStatus(actiefKindId, sleutel.split(","))
      .then((rijen) => {
        if (geannuleerd) return;
        setStatus(new Map(rijen.map((r) => [r.hoofdstukId, r])));
      })
      .catch(() => {
        // Lukt het niet, dan blijft de lijst gewoon zonder vinkjes staan.
      });
    return () => {
      geannuleerd = true;
    };
  }, [actiefKindId, sleutel]);

  const kies = (id: string) => {
    // Eerst leegmaken: anders blijven de vinkjes van het vorige kind even
    // staan terwijl die van het nieuwe nog onderweg zijn.
    setStatus(new Map());
    setActiefKindId(id);
    bewaarActiefKind(id);
  };

  return { actiefKindId, status, kies };
}

/**
 * De knoppenrij om te kiezen wie er oefent. Staat er maar één kind, dan heeft
 * kiezen geen zin en tonen we niets.
 */
export function KindKeuze({
  kinderen,
  actiefKindId,
  onKies,
}: {
  kinderen: Kind[];
  actiefKindId: string | null;
  onKies: (id: string) => void;
}) {
  if (kinderen.length < 2) return null;
  return (
    <div className="mt-6 flex flex-wrap items-center gap-2">
      <span className="text-sm text-ink-dim">Wie oefent er?</span>
      {kinderen.map((k) => (
        <button
          key={k.id}
          type="button"
          onClick={() => onKies(k.id)}
          className={`rounded-full px-3 py-1 text-sm transition ${
            k.id === actiefKindId
              ? "bg-forest text-white"
              : "border border-border bg-surface text-ink hover:border-forest"
          }`}
        >
          {k.naam}
        </button>
      ))}
    </div>
  );
}
