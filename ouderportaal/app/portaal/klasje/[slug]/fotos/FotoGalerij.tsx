"use client";

import { useCallback, useEffect, useRef, useState } from "react";

type Foto = { id: string; url: string; bijschrift: string | null };

/*
  Het fotoraster voor ouders. Een klik op een foto toont hem groot over het
  hele scherm. Verder met de pijltjes (ook op het toetsenbord) of door te
  vegen op een gsm; sluiten met het kruisje, Escape of een klik ernaast.
*/
export function FotoGalerij({ fotos }: { fotos: Foto[] }) {
  const [open, setOpen] = useState<number | null>(null);
  const veegStart = useRef<number | null>(null);

  const sluit = useCallback(() => setOpen(null), []);
  const ga = useCallback(
    (stap: number) => setOpen((i) => (i === null ? null : (i + stap + fotos.length) % fotos.length)),
    [fotos.length],
  );

  useEffect(() => {
    if (open === null) return;
    function toets(e: KeyboardEvent) {
      if (e.key === "Escape") sluit();
      if (e.key === "ArrowRight") ga(1);
      if (e.key === "ArrowLeft") ga(-1);
    }
    window.addEventListener("keydown", toets);
    const vroeger = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", toets);
      document.body.style.overflow = vroeger;
    };
  }, [open, sluit, ga]);

  const huidig = open === null ? null : fotos[open];

  return (
    <>
      <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
        {fotos.map((f, i) => (
          <figure key={f.id} className="overflow-hidden rounded-lg border border-border bg-surface">
            <button
              type="button"
              onClick={() => setOpen(i)}
              className="block w-full cursor-zoom-in"
              aria-label={f.bijschrift ? `${f.bijschrift}, groot bekijken` : "Foto groot bekijken"}
            >
              {/* Pas laden als het vakje in beeld komt: zo haalt een ouder die enkel
                  de bovenste rij bekijkt niet het hele album binnen. */}
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={f.url}
                alt={f.bijschrift ?? ""}
                loading="lazy"
                decoding="async"
                className="aspect-square w-full object-cover"
              />
            </button>
            {f.bijschrift && (
              <figcaption className="px-2 py-1.5 text-xs text-ink-dim">{f.bijschrift}</figcaption>
            )}
          </figure>
        ))}
      </div>

      {huidig && (
        <div
          role="dialog"
          aria-modal="true"
          aria-label="Foto groot bekijken"
          onClick={sluit}
          onTouchStart={(e) => (veegStart.current = e.touches[0].clientX)}
          onTouchEnd={(e) => {
            if (veegStart.current === null) return;
            const verschil = e.changedTouches[0].clientX - veegStart.current;
            veegStart.current = null;
            if (Math.abs(verschil) > 50) ga(verschil < 0 ? 1 : -1);
          }}
          className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-black/90 p-4"
        >
          <button
            type="button"
            onClick={sluit}
            aria-label="Sluiten"
            className="absolute right-3 top-3 rounded-full bg-white/15 px-3 py-1 text-2xl leading-none text-white hover:bg-white/30"
          >
            ×
          </button>

          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={huidig.url}
            alt={huidig.bijschrift ?? ""}
            onClick={(e) => e.stopPropagation()}
            className="max-h-[85vh] max-w-full rounded-md object-contain"
          />
          <p className="mt-3 text-center text-sm text-white/85">
            {huidig.bijschrift ? `${huidig.bijschrift} · ` : ""}
            {open! + 1} van {fotos.length}
          </p>

          {fotos.length > 1 && (
            <>
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  ga(-1);
                }}
                aria-label="Vorige foto"
                className="absolute left-2 top-1/2 -translate-y-1/2 rounded-full bg-white/15 px-3 py-2 text-2xl text-white hover:bg-white/30"
              >
                ‹
              </button>
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  ga(1);
                }}
                aria-label="Volgende foto"
                className="absolute right-2 top-1/2 -translate-y-1/2 rounded-full bg-white/15 px-3 py-2 text-2xl text-white hover:bg-white/30"
              >
                ›
              </button>
            </>
          )}
        </div>
      )}
    </>
  );
}
