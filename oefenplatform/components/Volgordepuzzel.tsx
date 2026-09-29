"use client";

import { useMemo, useState } from "react";

/*
  De sleutel naar de oefeningen: zet de onderdelen van de leerbundel weer in
  de juiste volgorde.

  Gevraagd op 28 september 2026: "mss dat ze eerst een puzzel ofzo moeten
  oplossen om het hoofdstuk te ontgrendelen (enkel bij de interactieve
  leerbundels)". Dit is bewust geen toets. Wie de onderdelen net doorgeklikt
  heeft, lost hem in een halve minuut op; wie meteen doorklikte naar de
  oefeningen, moet even terug kijken. Fout kiezen kost niets: het onderdeel
  blijft gewoon staan tot het aan de beurt is.

  De volgorde komt uit de bundel zelf, dus er valt niets extra te onderhouden.
*/

function husselen<T>(lijst: T[], zaad: number): T[] {
  // Vaste volgorde per hoofdstuk: bij het opnieuw tekenen springen de knoppen
  // niet rond, en twee kinderen op hetzelfde hoofdstuk zien hetzelfde.
  const uit = [...lijst];
  let willekeur = zaad || 1;
  for (let i = uit.length - 1; i > 0; i--) {
    willekeur = (willekeur * 1103515245 + 12345) % 2147483648;
    const j = willekeur % (i + 1);
    [uit[i], uit[j]] = [uit[j], uit[i]];
  }
  return uit;
}

function zaadVan(tekst: string): number {
  let som = 0;
  for (const teken of tekst)
    som = (som * 31 + teken.codePointAt(0)!) % 2147483647;
  return som;
}

export function Volgordepuzzel({
  koppen,
  hoofdstukId,
  onOpgelost,
}: {
  koppen: string[];
  hoofdstukId: string;
  onOpgelost: () => void;
}) {
  const [gelegd, setGelegd] = useState<number[]>([]);
  const [mis, setMis] = useState<number | null>(null);

  const volgorde = useMemo(
    () =>
      husselen(
        koppen.map((_, i) => i),
        zaadVan(hoofdstukId),
      ),
    [koppen, hoofdstukId],
  );

  const af = gelegd.length === koppen.length;

  function kies(i: number) {
    if (af) return;
    if (i === gelegd.length) {
      const nieuw = [...gelegd, i];
      setMis(null);
      setGelegd(nieuw);
      if (nieuw.length === koppen.length) onOpgelost();
      return;
    }
    setMis(i);
  }

  return (
    <div className="rounded-xl border border-forest/40 bg-forest/5 px-5 py-5">
      <h3 className="font-display text-base font-semibold text-ink">
        🔑 De sleutel naar de oefeningen
      </h3>
      <p className="mt-1 text-sm text-ink-dim">
        Zet de onderdelen weer in de volgorde waarin ze in de bundel staan. Klik
        ze aan, van het eerste tot het laatste. Fout gekozen is niet erg, je mag
        gewoon verder proberen.
      </p>

      <ol className="mt-4 space-y-2">
        {gelegd.map((i, plaats) => (
          <li
            key={koppen[i]}
            className="flex items-center gap-3 rounded-lg border border-forest bg-surface px-4 py-2.5 text-sm"
          >
            <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-forest text-xs font-bold text-white">
              {plaats + 1}
            </span>
            <span className="text-ink">{koppen[i]}</span>
          </li>
        ))}
      </ol>

      {!af && (
        <div className="mt-3 space-y-2">
          {volgorde
            .filter((i) => !gelegd.includes(i))
            .map((i) => (
              <button
                key={koppen[i]}
                type="button"
                onClick={() => kies(i)}
                className={`block w-full rounded-lg border bg-surface px-4 py-2.5 text-left text-sm text-ink transition hover:border-forest ${
                  mis === i ? "border-danger" : "border-border"
                }`}
              >
                {koppen[i]}
              </button>
            ))}
          {mis !== null && (
            <p className="text-sm text-danger">
              Dat onderdeel komt later. Kijk nog eens welk stuk er nu aan de
              beurt is.
            </p>
          )}
        </div>
      )}

      {af && (
        <p className="mt-3 rounded-lg bg-forest/10 px-4 py-3 text-sm font-medium text-forest-dark">
          Gelukt. De oefeningen staan open.
        </p>
      )}
    </div>
  );
}
