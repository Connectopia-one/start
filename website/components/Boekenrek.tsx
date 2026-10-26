"use client";

import { useState } from "react";
import { boeken, onderwerpen, type Onderwerp } from "@/content/boekentips";

/*
  Het raster met kaften op /boekentips, met bovenaan een knop per onderwerp.
  Een boek met meerdere onderwerpen staat onder elk ervan.
*/
export function Boekenrek() {
  const [gekozen, setGekozen] = useState<Onderwerp | null>(null);
  const zichtbaar = gekozen
    ? boeken.filter((boek) => boek.onderwerpen.includes(gekozen))
    : boeken;

  const knop = (actief: boolean) =>
    `rounded-full border px-4 py-1.5 text-[15px] font-extrabold transition ${
      actief
        ? "border-green bg-green text-cream"
        : "border-border bg-surface text-green hover:border-green"
    }`;

  return (
    <>
      <div className="flex flex-wrap gap-2" role="group" aria-label="Kies een onderwerp">
        <button
          type="button"
          className={knop(gekozen === null)}
          aria-pressed={gekozen === null}
          onClick={() => setGekozen(null)}
        >
          Alles ({boeken.length})
        </button>
        {onderwerpen.map((onderwerp) => (
          <button
            key={onderwerp}
            type="button"
            className={knop(gekozen === onderwerp)}
            aria-pressed={gekozen === onderwerp}
            onClick={() => setGekozen(onderwerp)}
          >
            {onderwerp}
          </button>
        ))}
      </div>

      <ul className="mt-6 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-4">
        {zichtbaar.map((boek) => (
          <li
            key={boek.slug}
            className="flex flex-col gap-2 rounded-[20px] border border-border bg-surface p-4 shadow-[0_2px_10px_rgba(47,74,34,0.07)]"
          >
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={`/boekentips/${boek.slug}.jpg`}
              alt={`De kaft van ${boek.titel}`}
              loading="lazy"
              className="mx-auto h-auto max-h-56 w-auto max-w-full rounded-md shadow-[4px_8px_14px_rgba(40,35,20,0.22)]"
            />
            <h2 lang="nl" className="mt-2 text-[17px] leading-snug break-words hyphens-auto text-green">
              {boek.titel}
            </h2>
            {boek.makers || boek.uitgeverij ? (
              <p className="text-[13px] text-sage">
                {[boek.makers, boek.uitgeverij].filter(Boolean).join(" · ")}
              </p>
            ) : null}
            <p className="text-[14px] text-ink-dim">{boek.tekst}</p>
            <div className="mt-auto flex flex-wrap gap-1.5 pt-2">
              {boek.onderwerpen.map((onderwerp) => (
                <span
                  key={onderwerp}
                  className="rounded-full bg-sage-soft px-2.5 py-0.5 text-[12px] font-extrabold text-green"
                >
                  {onderwerp}
                </span>
              ))}
            </div>
          </li>
        ))}
      </ul>
    </>
  );
}
