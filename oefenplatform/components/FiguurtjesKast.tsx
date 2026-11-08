"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  haalFiguurtjes,
  kiesFiguurtje,
  neemFiguurtje,
  type FiguurtjesStand,
} from "@/app/figuurtjes-actions";
import { FIGUURTJES } from "@/lib/figuurtjes";

/**
 * Figuurtjes kiezen met sterretjes, onder de badges van "Mijn verzameling".
 * Enkel zichtbaar als de ouder het voor dit kind aanzette (Mijn account).
 */
export function FiguurtjesKast({ kindId, naam }: { kindId: string | null; naam?: string }) {
  const [stand, setStand] = useState<FiguurtjesStand | null>(null);
  const [voor, setVoor] = useState<string | null>(null);
  const [bezig, setBezig] = useState<string | null>(null);
  const [fout, setFout] = useState<string | null>(null);

  useEffect(() => {
    if (!kindId) return;
    let weg = false;
    haalFiguurtjes(kindId)
      .then((s) => {
        if (weg) return;
        setStand(s);
        setVoor(kindId);
      })
      .catch(() => !weg && setVoor(kindId));
    return () => {
      weg = true;
    };
  }, [kindId]);

  if (!kindId || voor !== kindId || !stand) return null;

  if (!stand.aan)
    return (
      <p id="figuurtjes" className="mt-8 max-w-2xl rounded-md bg-info/10 px-4 py-3 text-sm text-ink">
        Wil je met je sterretjes figuurtjes kiezen? Een ouder kan dat aanzetten bij{" "}
        <Link href="/account" className="underline underline-offset-2">
          Mijn account
        </Link>
        .
      </p>
    );

  async function doe(sleutel: string, nieuw: boolean) {
    if (!kindId) return;
    setBezig(sleutel);
    setFout(null);
    const antwoord = nieuw ? await neemFiguurtje(kindId, sleutel) : await kiesFiguurtje(kindId, sleutel);
    if (antwoord.fout) setFout(antwoord.fout);
    const s = await haalFiguurtjes(kindId);
    setStand(s);
    setBezig(null);
  }

  const gekozen = FIGUURTJES.find((f) => f.sleutel === stand.gekozen);

  return (
    <section id="figuurtjes" className="mt-10">
      <h2 className="font-display text-xl font-semibold text-ink">🧸 Figuurtjes</h2>
      <p className="mt-1 max-w-2xl text-sm text-ink-dim">
        Elk hoofdstuk dat je helemaal afwerkt, geeft je een sterretje, ook als er fouten in zaten.
        Met je sterretjes kies je figuurtjes.
      </p>

      <div className="mt-4 flex flex-wrap items-center gap-4 rounded-xl border border-border bg-surface px-5 py-4">
        <span className="text-4xl" aria-hidden>
          {gekozen ? gekozen.emoji : "❔"}
        </span>
        <div className="text-sm">
          <p className="font-semibold text-ink">
            {gekozen ? `${naam ? naam + ", j" : "J"}e figuurtje: ${gekozen.naam}` : "Nog geen figuurtje gekozen"}
          </p>
          <p className="text-ink-dim">
            ⭐ {stand.over} {stand.over === 1 ? "sterretje" : "sterretjes"} om te gebruiken ·{" "}
            {stand.verdiend} {stand.verdiend === 1 ? "hoofdstuk" : "hoofdstukken"} afgewerkt
          </p>
        </div>
      </div>

      {fout && <p className="mt-3 text-sm text-danger">{fout}</p>}

      <div className="mt-4 grid grid-cols-3 gap-3 sm:grid-cols-5 lg:grid-cols-6">
        {FIGUURTJES.map((f) => {
          const heb = stand.eigen.includes(f.sleutel);
          const kan = !heb && stand.over >= f.prijs;
          const isGekozen = stand.gekozen === f.sleutel;
          return (
            <button
              key={f.sleutel}
              type="button"
              disabled={bezig !== null || (!heb && !kan) || isGekozen}
              onClick={() => doe(f.sleutel, !heb)}
              className={`flex flex-col items-center rounded-xl border px-2 py-3 text-center transition ${
                isGekozen
                  ? "border-forest bg-forest/10"
                  : heb
                    ? "border-border bg-surface hover:border-forest"
                    : kan
                      ? "border-amber/60 bg-amber/5 hover:border-amber"
                      : "border-border bg-surface"
              }`}
            >
              <span className={`text-3xl ${heb || kan ? "" : "opacity-30 grayscale"}`} aria-hidden>
                {f.emoji}
              </span>
              <span className={`mt-1 text-xs ${heb || kan ? "text-ink" : "text-ink-dim"}`}>{f.naam}</span>
              <span className="mt-0.5 text-[11px] text-ink-dim">
                {isGekozen ? "gekozen" : heb ? "kiezen" : `${f.prijs} ⭐`}
              </span>
            </button>
          );
        })}
      </div>
    </section>
  );
}
