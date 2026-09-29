"use client";

import { useEffect, useState } from "react";
import type { BundelBlok, KlikbareBundel } from "@/lib/leerbundel";

/*
  De leerbundel als losse onderdelen om op te klikken.

  Gevraagd na een melding van een kind uit de testgroep op 28 september 2026:
  "ik vind het goed dat er leerbundels zijn om te oefenen. Maar ik vind
  leerbundels lezen heel saai. En heb daardoor de neiging om ze over te slaan.
  Met het gevolg dat ik de oefeningen niet kan."

  Eén lange pdf vraagt dat je alles in één ruk doorworstelt. Hier neem je één
  onderdeel tegelijk, zie je meteen hoeveel je al gehad hebt, en blijft wat je
  gelezen hebt aangevinkt staan als je later terugkomt.

  De html in de blokjes komt uit onze eigen bronbestanden
  (inhoud/leerbundels/bron/*.py), niet van een bezoeker. Daarom mag ze hier
  rechtstreeks in de pagina.
*/

function bewaarSleutel(hoofdstukId: string) {
  return `connectopia-bundel-gelezen-${hoofdstukId}`;
}

function lees(sleutel: string): number[] {
  try {
    const rauw = window.localStorage.getItem(sleutel);
    if (!rauw) return [];
    const uit = JSON.parse(rauw);
    return Array.isArray(uit) ? uit.filter((n) => typeof n === "number") : [];
  } catch {
    return [];
  }
}

function schrijf(sleutel: string, waarden: number[]) {
  try {
    window.localStorage.setItem(sleutel, JSON.stringify(waarden));
  } catch {
    // Geen opslag beschikbaar (privévenster): dan onthoudt het gewoon niets.
  }
}

export function KlikbareLeerbundel({
  bundel,
  hoofdstukId,
  puzzel,
}: {
  bundel: KlikbareBundel;
  hoofdstukId: string;
  puzzel?: React.ReactNode;
}) {
  const [open, setOpen] = useState<number | null>(null);
  const [gelezen, setGelezen] = useState<number[]>([]);

  // localStorage is een bron buiten React; pas na het eerste tekenen uitlezen,
  // anders verschilt wat de server maakte van wat de browser toont.
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setGelezen(lees(bewaarSleutel(hoofdstukId)));
  }, [hoofdstukId]);

  function klik(i: number) {
    if (open === i) {
      setOpen(null);
      return;
    }
    setOpen(i);
    if (!gelezen.includes(i)) {
      const nieuw = [...gelezen, i];
      setGelezen(nieuw);
      schrijf(bewaarSleutel(hoofdstukId), nieuw);
    }
  }

  const totaal = bundel.secties.length;
  const klaar = gelezen.length;
  const alles = klaar >= totaal;

  return (
    <div className="mt-6">
      <div className="rounded-xl border border-border bg-surface px-5 py-5">
        <p className="text-xs font-semibold uppercase tracking-wide text-ink-dim">
          {bundel.vak}
        </p>
        <h2 className="mt-1 font-display text-xl font-semibold text-ink">
          {bundel.titel}
        </h2>
        <p className="mt-1 text-sm text-ink-dim">{bundel.onder}</p>

        <div className="mt-4 flex items-center gap-3">
          <div className="h-2 flex-1 overflow-hidden rounded-full bg-paper">
            <div
              className="h-full rounded-full bg-forest transition-all"
              style={{ width: `${totaal ? (klaar / totaal) * 100 : 0}%` }}
            />
          </div>
          <span className="shrink-0 text-xs font-medium text-ink-dim">
            {klaar} van {totaal}
          </span>
        </div>
        <p className="mt-2 text-xs text-ink-dim">
          {alles
            ? "Je hebt alle onderdelen bekeken. Je mag er altijd naar terug."
            : "Klik een onderdeel open om het te lezen. Je hoeft niet alles in één keer te doen."}
        </p>
      </div>

      <ul className="mt-3 space-y-2">
        {bundel.secties.map((sectie, i) => {
          const isOpen = open === i;
          const isGelezen = gelezen.includes(i);
          return (
            <li
              key={sectie.kop}
              className={`overflow-hidden rounded-xl border bg-surface ${
                isOpen ? "border-forest" : "border-border"
              }`}
            >
              <button
                type="button"
                onClick={() => klik(i)}
                aria-expanded={isOpen}
                className="flex w-full items-center gap-3 px-4 py-3 text-left"
              >
                <span
                  className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full text-xs font-bold ${
                    isGelezen ? "bg-forest text-white" : "bg-paper text-ink-dim"
                  }`}
                  aria-hidden="true"
                >
                  {isGelezen ? "✓" : i + 1}
                </span>
                <span className="flex-1 text-sm font-semibold text-ink">
                  {sectie.kop}
                </span>
                <span
                  className={`shrink-0 text-ink-dim transition-transform ${
                    isOpen ? "rotate-180" : ""
                  }`}
                  aria-hidden="true"
                >
                  ▾
                </span>
              </button>

              {isOpen && (
                <div className="border-t border-border px-4 py-4">
                  {sectie.blokken.map((blok, j) => (
                    <Blok key={j} blok={blok} />
                  ))}
                </div>
              )}
            </li>
          );
        })}
      </ul>

      {bundel.onthoud.length > 0 && (
        <div className="mt-4 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4">
          <h3 className="font-display text-base font-semibold text-ink">
            Onthoud dit
          </h3>
          <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink">
            {bundel.onthoud.map((punt) => (
              <li key={punt}>{punt}</li>
            ))}
          </ul>
        </div>
      )}

      {puzzel && (
        <div className="mt-4">{alles ? puzzel : <NogNietKlaar />}</div>
      )}
    </div>
  );
}

function NogNietKlaar() {
  return (
    <p className="rounded-xl border border-dashed border-border-strong px-5 py-4 text-sm text-ink-dim">
      Als je alle onderdelen bekeken hebt, krijg je hier de sleutel naar de
      oefeningen.
    </p>
  );
}

function Blok({ blok }: { blok: BundelBlok }) {
  if (blok.soort === "figuur") {
    return (
      <figure className="mt-3 first:mt-0">
        <div
          className="overflow-x-auto [&_svg]:h-auto [&_svg]:max-w-full [&_table]:w-full"
          dangerouslySetInnerHTML={{ __html: blok.html }}
        />
        {blok.onderschrift && (
          <figcaption className="mt-2 text-center text-xs text-ink-dim">
            {blok.onderschrift}
          </figcaption>
        )}
      </figure>
    );
  }

  if (blok.soort === "weetje") {
    return (
      <div className="mt-3 rounded-lg border border-amber/40 bg-amber/10 px-4 py-3 first:mt-0">
        <p className="text-sm font-medium text-ink">💡 Weetje</p>
        <div
          className="mt-1 text-sm text-ink [&_a]:underline"
          dangerouslySetInnerHTML={{ __html: blok.html }}
        />
      </div>
    );
  }

  if (blok.soort === "kader") {
    return (
      <div
        className="mt-3 overflow-x-auto rounded-lg border border-border bg-paper px-4 py-3 text-[15px] leading-relaxed text-ink first:mt-0"
        dangerouslySetInnerHTML={{ __html: blok.html }}
      />
    );
  }

  return (
    <div
      className="mt-3 text-[15px] leading-relaxed text-ink first:mt-0"
      dangerouslySetInnerHTML={{ __html: blok.html }}
    />
  );
}
