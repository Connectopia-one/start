"use client";

import { useMemo, useState } from "react";

/*
  Het spelletje op de eindhalte: zet de haltes weer in de juiste volgorde.

  Gevraagd op 28 september 2026: "mss dat ze eerst een puzzel ofzo moeten
  oplossen". Het zet niets op slot — Kim op 29 september 2026: de oefeningen
  blijven gewoon open, dit is een extraatje op het einde van de tocht. Wie de
  haltes net gehad heeft, lost het in een halve minuut op; wie meteen naar
  beneden sprong, moet even terugkijken. Fout kiezen kost niets.

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

export function Volgordespel({
  koppen,
  hoofdstukId,
}: {
  koppen: string[];
  hoofdstukId: string;
}) {
  const [gelegd, setGelegd] = useState<number[]>([]);
  const [mis, setMis] = useState<number | null>(null);
  const [misgeteld, setMisgeteld] = useState(0);

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
      setMis(null);
      setGelegd([...gelegd, i]);
      return;
    }
    setMis(i);
    setMisgeteld(misgeteld + 1);
  }

  function opnieuw() {
    setGelegd([]);
    setMis(null);
    setMisgeteld(0);
  }

  if (koppen.length < 2) return null;

  return (
    <div className="rounded-2xl border border-forest/40 bg-forest/5 px-5 py-5">
      <h2 className="font-display text-xl font-semibold text-ink">
        🧩 De tocht op een rij
      </h2>
      <p className="mt-1 text-sm text-ink-dim">
        Zet de haltes weer in de volgorde waarin je ze deed. Klik ze aan, van de
        eerste tot de laatste. Fout gekozen is niet erg, je mag gewoon verder
        proberen. Dit zet niets open of dicht, het is er voor de lol.
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
              Die halte komt later. Kijk nog eens welke er nu aan de beurt is.
            </p>
          )}
        </div>
      )}

      {af && (
        <div className="mt-3 rounded-lg bg-forest/10 px-4 py-3">
          <p className="text-sm font-medium text-forest-dark">
            {misgeteld === 0
              ? "In één keer juist. Jij hebt goed opgelet."
              : "Gelukt, de hele tocht staat op een rij."}
          </p>
          <button
            type="button"
            onClick={opnieuw}
            className="mt-2 text-sm text-ink-dim underline underline-offset-2 hover:text-ink"
          >
            Nog eens spelen
          </button>
        </div>
      )}
    </div>
  );
}
