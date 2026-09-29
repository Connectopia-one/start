"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { Legpuzzel } from "@/components/Legpuzzel";
import { Volgordespel } from "@/components/Volgordespel";
import {
  puzzelBeeld,
  type BundelBlok,
  type KlikbareBundel,
} from "@/lib/leerbundel";

/*
  De tocht door een hoofdstuk: de leerstof van de leerbundel, maar als haltes.

  Dit is een apart ding, geen andere weergave van de bundel. Kim op
  29 september 2026: "dit gaat echt een heel apart nieuw ding zijn. wel met de
  leerstof van de lesbundels maar dan leuker gegeven voor hun." De pdf en het
  hoofdstuk zelf blijven dus precies zoals ze waren.

  Aanleiding was de melding van een kind uit de testgroep: "ik vind leerbundels
  lezen heel saai. En heb daardoor de neiging om ze over te slaan. Met het
  gevolg dat ik de oefeningen niet kan."

  Daarom één halte tegelijk in plaats van een lap tekst, een stempel per halte
  die blijft staan, en op het einde een spelletje. Er zit geen slot op: elke
  halte is altijd aanklikbaar en de oefeningen staan gewoon open.

  De html in de blokjes komt uit onze eigen bronbestanden
  (inhoud/leerbundels/bron/*.py), niet van een bezoeker. Daarom mag ze hier
  rechtstreeks in de pagina.
*/

function stempelSleutel(hoofdstukId: string) {
  return `connectopia-tocht-${hoofdstukId}`;
}

function lees(sleutel: string): number[] {
  try {
    const rauw = window.localStorage.getItem(sleutel);
    const uit = rauw ? JSON.parse(rauw) : [];
    return Array.isArray(uit) ? uit.filter((n) => typeof n === "number") : [];
  } catch {
    return [];
  }
}

function schrijf(sleutel: string, waarden: number[]) {
  try {
    window.localStorage.setItem(sleutel, JSON.stringify(waarden));
  } catch {
    // Geen opslag (privévenster): dan onthoudt het gewoon niets.
  }
}

export function InteractieveLeerbundel({
  bundel,
  hoofdstukId,
  naarOefeningen,
}: {
  bundel: KlikbareBundel;
  hoofdstukId: string;
  /** Terug naar het hoofdstuk met de gewone oefeningen. */
  naarOefeningen: string;
}) {
  const laatste = bundel.secties.length; // de eindhalte krijgt dit nummer
  const [halte, setHalte] = useState(0);
  const [gestempeld, setGestempeld] = useState<number[]>([]);
  const kop = useRef<HTMLDivElement>(null);

  // localStorage is een bron buiten React; pas na het eerste tekenen uitlezen,
  // anders verschilt wat de server maakte van wat de browser toont.
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setGestempeld(lees(stempelSleutel(hoofdstukId)));
  }, [hoofdstukId]);

  function ga(naar: number) {
    setHalte(naar);
    kop.current?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function stempelEnVerder(i: number) {
    if (!gestempeld.includes(i)) {
      const nieuw = [...gestempeld, i];
      setGestempeld(nieuw);
      schrijf(stempelSleutel(hoofdstukId), nieuw);
    }
    ga(Math.min(i + 1, laatste));
  }

  const klaar = gestempeld.length;
  const alles = klaar >= bundel.secties.length;
  const opEindhalte = halte >= laatste;

  return (
    <div className="mt-6" ref={kop}>
      <div className="rounded-2xl border border-forest/30 bg-forest/5 px-5 py-5">
        <p className="font-display text-lg font-semibold text-ink">
          🥾 De tocht door {bundel.titel}
        </p>
        <p className="mt-1 text-sm text-ink-dim">
          {bundel.onder} Je doet de haltes één voor één, in je eigen tempo. Je
          hoeft niets in één keer af te maken; wat je gehad hebt, blijft staan.
        </p>

        <div className="mt-4 flex flex-wrap items-center gap-1.5">
          {bundel.secties.map((sectie, i) => {
            const gedaan = gestempeld.includes(i);
            const hier = halte === i;
            return (
              <button
                key={sectie.kop}
                type="button"
                onClick={() => ga(i)}
                title={sectie.kop}
                aria-label={`Halte ${i + 1}: ${sectie.kop}`}
                aria-current={hier ? "step" : undefined}
                className={`flex h-8 w-8 items-center justify-center rounded-full border text-xs font-bold transition ${
                  hier
                    ? "border-forest bg-forest text-white"
                    : gedaan
                      ? "border-forest/50 bg-forest/15 text-forest-dark"
                      : "border-border bg-surface text-ink-dim hover:border-forest"
                }`}
              >
                {gedaan && !hier ? "✓" : i + 1}
              </button>
            );
          })}
          <button
            type="button"
            onClick={() => ga(laatste)}
            aria-label="De eindhalte"
            aria-current={opEindhalte ? "step" : undefined}
            className={`flex h-8 items-center justify-center rounded-full border px-3 text-xs font-bold transition ${
              opEindhalte
                ? "border-amber bg-amber/20 text-ink"
                : "border-border bg-surface text-ink-dim hover:border-amber"
            }`}
          >
            🏁
          </button>
        </div>

        <p className="mt-3 text-xs text-ink-dim">
          {alles
            ? "Alle haltes gehad. Je mag altijd nog eens terug."
            : `${klaar} van de ${bundel.secties.length} haltes gestempeld`}
        </p>
      </div>

      {opEindhalte ? (
        <Eindhalte
          bundel={bundel}
          hoofdstukId={hoofdstukId}
          naarOefeningen={naarOefeningen}
          opnieuw={() => ga(0)}
        />
      ) : (
        <Halte
          nummer={halte}
          totaal={bundel.secties.length}
          kop={bundel.secties[halte].kop}
          blokken={bundel.secties[halte].blokken}
          gestempeld={gestempeld.includes(halte)}
          opVerder={() => stempelEnVerder(halte)}
          opVorige={halte > 0 ? () => ga(halte - 1) : null}
        />
      )}

      <p className="mt-6 text-center">
        <Link
          href={naarOefeningen}
          className="text-sm text-ink-dim underline underline-offset-2 hover:text-ink"
        >
          Terug naar het hoofdstuk
        </Link>
      </p>
    </div>
  );
}

function Halte({
  nummer,
  totaal,
  kop,
  blokken,
  gestempeld,
  opVerder,
  opVorige,
}: {
  nummer: number;
  totaal: number;
  kop: string;
  blokken: BundelBlok[];
  gestempeld: boolean;
  opVerder: () => void;
  opVorige: (() => void) | null;
}) {
  return (
    <article className="mt-4 rounded-2xl border border-border bg-surface px-5 py-5">
      <p className="text-xs font-semibold uppercase tracking-wide text-ink-dim">
        Halte {nummer + 1} van {totaal}
        {gestempeld && " · al gehad"}
      </p>
      <h2 className="mt-1 font-display text-xl font-semibold text-ink">
        {kop}
      </h2>

      <div className="mt-4">
        {blokken.map((blok, j) => (
          <Blok key={j} blok={blok} />
        ))}
      </div>

      <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-border pt-4">
        {opVorige && (
          <button
            type="button"
            onClick={opVorige}
            className="text-sm text-ink-dim hover:text-ink"
          >
            &larr; Vorige halte
          </button>
        )}
        <button
          type="button"
          onClick={opVerder}
          className="ml-auto rounded-full bg-forest px-5 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark"
        >
          {nummer + 1 === totaal
            ? "Klaar, naar de eindhalte 🏁"
            : "Gehad, volgende halte →"}
        </button>
      </div>
    </article>
  );
}

function Eindhalte({
  bundel,
  hoofdstukId,
  naarOefeningen,
  opnieuw,
}: {
  bundel: KlikbareBundel;
  hoofdstukId: string;
  naarOefeningen: string;
  opnieuw: () => void;
}) {
  const beeld = puzzelBeeld(bundel);

  return (
    <div className="mt-4 space-y-4">
      <article className="rounded-2xl border border-amber/40 bg-amber/10 px-5 py-5">
        <p className="text-xs font-semibold uppercase tracking-wide text-ink-dim">
          🏁 Eindhalte
        </p>
        <h2 className="mt-1 font-display text-xl font-semibold text-ink">
          Onthoud dit
        </h2>
        {bundel.onthoud.length ? (
          <Afvinklijst punten={bundel.onthoud} hoofdstukId={hoofdstukId} />
        ) : (
          <p className="mt-2 text-sm text-ink-dim">
            Bij dit hoofdstuk staat geen lijstje om te onthouden.
          </p>
        )}
      </article>

      {/* Liefst de legpuzzel met een tekening uit het hoofdstuk. Heeft dit
          hoofdstuk geen bruikbare tekening, dan blijft het volgordespel. */}
      {beeld ? (
        <Legpuzzel beeld={beeld} />
      ) : (
        <Volgordespel
          koppen={bundel.secties.map((s) => s.kop)}
          hoofdstukId={hoofdstukId}
        />
      )}

      <div className="rounded-2xl border border-border bg-surface px-5 py-5 text-center">
        <p className="text-sm text-ink">Klaar met de tocht?</p>
        <Link
          href={naarOefeningen}
          className="mt-3 inline-block rounded-full bg-forest px-5 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark"
        >
          Naar de oefeningen &rarr;
        </Link>
        <p className="mt-3">
          <button
            type="button"
            onClick={opnieuw}
            className="text-sm text-ink-dim underline underline-offset-2 hover:text-ink"
          >
            Nog eens van bij het begin
          </button>
        </p>
      </div>
    </div>
  );
}

function Afvinklijst({
  punten,
  hoofdstukId,
}: {
  punten: string[];
  hoofdstukId: string;
}) {
  const sleutel = `connectopia-onthoud-${hoofdstukId}`;
  const [aan, setAan] = useState<number[]>([]);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setAan(lees(sleutel));
  }, [sleutel]);

  function wissel(i: number) {
    const nieuw = aan.includes(i) ? aan.filter((n) => n !== i) : [...aan, i];
    setAan(nieuw);
    schrijf(sleutel, nieuw);
  }

  return (
    <>
      <p className="mt-1 text-sm text-ink-dim">
        Vink af wat je al zeker weet. Wat blijft staan, lees je nog eens na.
      </p>
      <ul className="mt-3 space-y-2">
        {punten.map((punt, i) => (
          <li key={punt}>
            <label className="flex cursor-pointer items-start gap-3 rounded-lg border border-border bg-surface px-4 py-2.5 text-sm">
              <input
                type="checkbox"
                checked={aan.includes(i)}
                onChange={() => wissel(i)}
                className="mt-0.5 accent-forest"
              />
              <span className={aan.includes(i) ? "text-ink-dim" : "text-ink"}>
                {punt}
              </span>
            </label>
          </li>
        ))}
      </ul>
    </>
  );
}

function Blok({ blok }: { blok: BundelBlok }) {
  if (blok.soort === "figuur") {
    return (
      <figure className="mt-4 first:mt-0">
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
      <div className="mt-4 rounded-xl border border-amber/40 bg-amber/10 px-4 py-3 first:mt-0">
        <p className="text-sm font-semibold text-ink">💡 Weetje</p>
        <div
          className="mt-1 text-[15px] leading-relaxed text-ink"
          dangerouslySetInnerHTML={{ __html: blok.html }}
        />
      </div>
    );
  }

  if (blok.soort === "kader") {
    return (
      <div
        className="mt-4 overflow-x-auto rounded-xl border border-border bg-paper px-4 py-3 text-[15px] leading-relaxed text-ink first:mt-0"
        dangerouslySetInnerHTML={{ __html: blok.html }}
      />
    );
  }

  return (
    <div
      className="mt-4 text-[15px] leading-relaxed text-ink first:mt-0"
      dangerouslySetInnerHTML={{ __html: blok.html }}
    />
  );
}
