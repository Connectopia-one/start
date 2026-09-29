"use client";

import { useState } from "react";
import { puzzelRooster, type Puzzelbeeld } from "@/lib/leerbundel";

/*
  De schuifpuzzel op de eindhalte: een tekening uit het hoofdstuk zelf, in
  stukken, met één leeg vakje. Klik een stuk dat naast het gat ligt en het
  schuift erin.

  Kim op 29 september 2026: "ik denk dat een fysieke puzzel van een afbeelding
  die ze op de juiste plaats moeten schuiven in thema leuker is."

  In thema is het letterlijk: het beeld komt uit de leerbundel van dít
  hoofdstuk, dus wie de tocht net gedaan heeft, herkent het. Welke tekening het
  wordt, kiest lib/leerbundel.ts (puzzelBeeld).

  Er zit geen slot op en er wordt niets bewaard: het is een spelletje.

  Geschud wordt er met echte zetten vanuit de opgeloste stand, nooit door de
  stukken zomaar door elkaar te gooien. Anders kan je een schuifpuzzel krijgen
  die niet op te lossen is — en dan zit een kind een halfuur voor niets te
  schuiven.
*/

function buren(plek: number, kolommen: number, rijen: number): number[] {
  const kolom = plek % kolommen;
  const rij = Math.floor(plek / kolommen);
  const uit: number[] = [];
  if (kolom > 0) uit.push(plek - 1);
  if (kolom < kolommen - 1) uit.push(plek + 1);
  if (rij > 0) uit.push(plek - kolommen);
  if (rij < rijen - 1) uit.push(plek + kolommen);
  return uit;
}

function schud(aantal: number, kolommen: number, rijen: number): number[] {
  const stand = Array.from({ length: aantal }, (_, i) => i);
  let gat = aantal - 1;
  let vorig = -1;
  // Even of oneven veel zetten bepaalt in welke helft van het bord het lege
  // vakje eindigt, dus dat laten we meeloten.
  const rondes = aantal * 30 + (Math.random() < 0.5 ? 0 : 1);
  for (let zet = 0; zet < rondes; zet++) {
    const keuze = buren(gat, kolommen, rijen).filter((p) => p !== vorig);
    const naar = keuze[Math.floor(Math.random() * keuze.length)];
    [stand[gat], stand[naar]] = [stand[naar], stand[gat]];
    vorig = gat;
    gat = naar;
  }
  // Heel soms komt het schudden toch weer op de opgeloste stand uit.
  if (stand.every((stuk, plek) => stuk === plek))
    return schud(aantal, kolommen, rijen);
  return stand;
}

export function Schuifpuzzel({ beeld }: { beeld: Puzzelbeeld }) {
  const { kolommen, rijen } = puzzelRooster(beeld.verhouding);
  const aantal = kolommen * rijen;
  const gatStuk = aantal - 1;

  const [stand, setStand] = useState<number[] | null>(null);
  const [zetten, setZetten] = useState(0);

  const gatPlek = stand ? stand.indexOf(gatStuk) : -1;
  const af = Boolean(stand && stand.every((stuk, plek) => stuk === plek));

  function begin() {
    setStand(schud(aantal, kolommen, rijen));
    setZetten(0);
  }

  function schuif(plek: number) {
    if (!stand || af) return;
    if (!buren(gatPlek, kolommen, rijen).includes(plek)) return;
    const nieuw = [...stand];
    [nieuw[gatPlek], nieuw[plek]] = [nieuw[plek], nieuw[gatPlek]];
    setStand(nieuw);
    setZetten(zetten + 1);
  }

  return (
    <div className="rounded-2xl border border-forest/40 bg-forest/5 px-5 py-5">
      <h2 className="font-display text-xl font-semibold text-ink">
        🧩 De schuifpuzzel
      </h2>
      <p className="mt-1 text-sm text-ink-dim">
        {stand && !af
          ? "Klik een stuk dat naast het lege vakje ligt, dan schuift het erin. Leg de tekening weer juist."
          : "Een tekening uit dit hoofdstuk, in stukken. Je schuift ze terug op hun plaats. Dit zet niets open of dicht, het is er voor de lol."}
      </p>

      <div
        className="mx-auto mt-4 w-full max-w-md overflow-hidden rounded-xl border border-border bg-paper"
        style={{ aspectRatio: String(beeld.verhouding) }}
      >
        {stand && !af ? (
          <div className="relative h-full w-full">
            {stand.map((stuk, plek) =>
              stuk === gatStuk ? null : (
                <button
                  key={stuk}
                  type="button"
                  onClick={() => schuif(plek)}
                  aria-label={`Stuk ${stuk + 1} verschuiven`}
                  className="absolute overflow-hidden border border-paper bg-paper transition-[left,top] duration-150 focus:z-10 focus:outline-2 focus:outline-forest"
                  style={{
                    width: `${100 / kolommen}%`,
                    height: `${100 / rijen}%`,
                    left: `${((plek % kolommen) * 100) / kolommen}%`,
                    top: `${(Math.floor(plek / kolommen) * 100) / rijen}%`,
                  }}
                >
                  <span
                    aria-hidden
                    className="pointer-events-none absolute [&_svg]:block [&_svg]:h-full [&_svg]:w-full"
                    style={{
                      width: `${kolommen * 100}%`,
                      height: `${rijen * 100}%`,
                      left: `${-(stuk % kolommen) * 100}%`,
                      top: `${-Math.floor(stuk / kolommen) * 100}%`,
                    }}
                    dangerouslySetInnerHTML={{ __html: beeld.html }}
                  />
                </button>
              ),
            )}
          </div>
        ) : (
          <div
            className="h-full w-full [&_svg]:block [&_svg]:h-full [&_svg]:w-full"
            dangerouslySetInnerHTML={{ __html: beeld.html }}
          />
        )}
      </div>

      {beeld.onderschrift && (
        <p className="mt-2 text-center text-xs text-ink-dim">
          {beeld.onderschrift}
        </p>
      )}

      {!stand && (
        <p className="mt-4 text-center">
          <button
            type="button"
            onClick={begin}
            className="rounded-full bg-forest px-5 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark"
          >
            Schud de stukken door elkaar
          </button>
        </p>
      )}

      {stand && !af && (
        <p className="mt-3 flex flex-wrap items-center justify-center gap-4 text-sm text-ink-dim">
          <span>
            {zetten} {zetten === 1 ? "zet" : "zetten"}
          </span>
          <button
            type="button"
            onClick={begin}
            className="underline underline-offset-2 hover:text-ink"
          >
            Opnieuw schudden
          </button>
        </p>
      )}

      {af && (
        <div className="mt-3 rounded-lg bg-forest/10 px-4 py-3 text-center">
          <p className="text-sm font-medium text-forest-dark">
            De tekening staat weer juist, in {zetten}{" "}
            {zetten === 1 ? "zet" : "zetten"}.
          </p>
          <button
            type="button"
            onClick={begin}
            className="mt-2 text-sm text-ink-dim underline underline-offset-2 hover:text-ink"
          >
            Nog eens spelen
          </button>
        </div>
      )}
    </div>
  );
}
