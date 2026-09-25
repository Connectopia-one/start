"use client";

import { useState } from "react";
import type { Woord } from "@/lib/woordenlijst";

export type { Woord };

/**
 * De tekst bij een hoofdstuk begrijpend lezen. Hij blijft boven de vragen
 * staan zolang het kind hem nodig heeft, want terugbladeren naar een tekst
 * die je net gelezen hebt is precies wat begrijpend lezen moeilijk maakt.
 *
 * Een woord tussen sterretjes (*echolocatie*) krijgt een stippellijntje;
 * erop tikken toont de uitleg uit de woordenlijst meteen onder de tekst.
 * Zo hoeft een kind niet naar onder te scrollen en zijn plaats te zoeken.
 */
export function Leestekst({
  tekst,
  woorden,
}: {
  tekst: string;
  woorden: Woord[];
}) {
  const [open, setOpen] = useState(true);
  const [gekozen, setGekozen] = useState<Woord | null>(null);

  const alinea = tekst.split(/\n\s*\n/).map((a) => a.trim()).filter(Boolean);
  const uitlegVan = (woord: string) =>
    woorden.find((w) => w.woord.toLowerCase() === woord.toLowerCase()) ?? {
      woord,
      uitleg: "",
    };

  return (
    <section className="rounded-xl border border-border bg-paper px-5 py-4">
      <div className="flex items-center justify-between gap-3">
        <h2 className="font-display text-base font-semibold text-ink">
          📖 Lees eerst deze tekst
        </h2>
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          aria-expanded={open}
          className="rounded-full border border-border bg-surface px-3 py-1 text-xs font-medium text-ink-dim hover:border-forest hover:text-forest-dark"
        >
          {open ? "Tekst wegklappen" : "Tekst terug tonen"}
        </button>
      </div>

      {open && (
        <>
          <div className="mt-3 space-y-3 text-[15px] leading-relaxed text-ink">
            {alinea.map((stuk, i) => (
              <p key={i}>
                {stuk.split(/(\*[^*\n]+\*)/g).map((deel, j) => {
                  if (!deel.startsWith("*") || !deel.endsWith("*") || deel.length < 3) {
                    return <span key={j}>{deel}</span>;
                  }
                  const woord = deel.slice(1, -1);
                  const item = uitlegVan(woord);
                  if (!item.uitleg) return <span key={j}>{woord}</span>;
                  return (
                    <button
                      key={j}
                      type="button"
                      onClick={() =>
                        setGekozen((g) => (g?.woord === item.woord ? null : item))
                      }
                      className="underline decoration-dotted decoration-forest underline-offset-4 hover:text-forest-dark"
                    >
                      {woord}
                    </button>
                  );
                })}
              </p>
            ))}
          </div>

          {gekozen && (
            <p className="mt-3 rounded-lg border border-forest/30 bg-surface px-3 py-2 text-sm text-ink">
              <strong className="text-forest-dark">{gekozen.woord}</strong>{" "}
              &mdash; {gekozen.uitleg}
            </p>
          )}

          {woorden.length > 0 && (
            <details className="mt-3">
              <summary className="cursor-pointer text-sm font-medium text-forest-dark">
                Moeilijke woorden ({woorden.length})
              </summary>
              <dl className="mt-2 space-y-1.5 text-sm">
                {woorden.map((w) => (
                  <div key={w.woord} className="flex flex-wrap gap-x-2">
                    <dt className="font-medium text-ink">{w.woord}</dt>
                    <dd className="text-ink-dim">{w.uitleg}</dd>
                  </div>
                ))}
              </dl>
            </details>
          )}
        </>
      )}
    </section>
  );
}
