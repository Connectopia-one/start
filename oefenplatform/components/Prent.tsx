"use client";

import Image from "next/image";
import { useEffect, useState } from "react";
import type { Prent as PrentGegevens } from "@/lib/prent";

/**
 * De prent bij een hoofdstuk waarin je moet beschrijven wat je ziet.
 *
 * Ze blijft boven de vragen staan zolang het kind ze nodig heeft, net als de
 * leestekst bij begrijpend lezen: terugbladeren naar een beeld dat je net
 * bekeken hebt, is precies wat zo'n oefening moeilijk maakt.
 *
 * Tikken op de prent maakt ze schermvullend. Vier op de vijf kinderen zitten
 * op een gsm, en daar is een slak op een steen of een lieveheersbeestje in het
 * gras anders niet te zien.
 */
export function Prent({
  prent,
  titel = "Kijk goed naar de prent",
}: {
  prent: PrentGegevens;
  titel?: string;
}) {
  const [open, setOpen] = useState(true);
  const [groot, setGroot] = useState(false);

  // Escape sluit de grote weergave, en zolang die openstaat scrollt de pagina
  // eronder niet mee.
  useEffect(() => {
    if (!groot) return;
    const opToets = (e: KeyboardEvent) => {
      if (e.key === "Escape") setGroot(false);
    };
    window.addEventListener("keydown", opToets);
    const vorige = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", opToets);
      document.body.style.overflow = vorige;
    };
  }, [groot]);

  return (
    <section className="rounded-xl border border-border bg-paper px-5 py-4">
      <div className="flex items-center justify-between gap-3">
        <h2 className="font-display text-base font-semibold text-ink">
          🖼️ {titel}
        </h2>
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          aria-expanded={open}
          className="rounded-full border border-border bg-surface px-3 py-1 text-xs font-medium text-ink-dim hover:border-forest hover:text-forest-dark"
        >
          {open ? "Prent wegklappen" : "Prent terug tonen"}
        </button>
      </div>

      {open && (
        <>
          <button
            type="button"
            onClick={() => setGroot(true)}
            className="mt-3 block w-full overflow-hidden rounded-lg border border-border bg-surface"
            aria-label="Toon de prent groot"
          >
            <Image
              src={prent.url}
              alt=""
              width={prent.breedte}
              height={prent.hoogte}
              sizes="(max-width: 768px) 100vw, 640px"
              className="h-auto w-full"
              priority
            />
          </button>
          <p className="mt-2 text-xs text-ink-dim">
            Tik op de prent om ze groot te bekijken.
          </p>
        </>
      )}

      {groot && (
        <div
          role="dialog"
          aria-modal="true"
          aria-label="De prent, groot"
          onClick={() => setGroot(false)}
          className="fixed inset-0 z-50 flex items-center justify-center bg-ink/80 p-4"
        >
          <Image
            src={prent.url}
            alt=""
            width={prent.breedte}
            height={prent.hoogte}
            sizes="100vw"
            className="max-h-full w-auto max-w-full rounded-lg object-contain"
          />
          <button
            type="button"
            onClick={() => setGroot(false)}
            className="absolute right-4 top-4 rounded-full bg-surface px-4 py-2 text-sm font-medium text-ink shadow"
          >
            Sluiten
          </button>
        </div>
      )}
    </section>
  );
}
