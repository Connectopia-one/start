"use client";

import { useState } from "react";

/** De soorten vragen in de keuzelijst Type, in beide formulieren dezelfde. */
export function TypeOpties() {
  return (
    <>
      <option value="meerkeuze">Meerkeuze</option>
      <option value="waarofniet">Waar of niet waar</option>
      <option value="invultekst">Invultekst</option>
      <optgroup label="Zoals op het examen van de Examencommissie">
        <option value="tabel">Tabel: per rij juist of fout</option>
        <option value="keuzelijst">Keuzelijst in een zin</option>
        <option value="volgorde">In de juiste volgorde zetten</option>
        <option value="koppelen">Koppelen</option>
        <option value="sorteren">Slepen naar kolommen</option>
        <option value="sleepzin">Woorden in een zin slepen</option>
        <option value="hotspot">Klikken op de prent</option>
        <option value="open">Open antwoord</option>
        <option value="tekenen">Tekenen</option>
      </optgroup>
    </>
  );
}

/**
 * Hoe je elke vorm van het examen intikt, in het formulier zelf. Die vormen
 * (zie lib/vraagvorm.ts en lib/examenvormen.ts) lezen hun velden anders dan
 * de andere types, en dat moet je kunnen zien zonder het ergens op te zoeken.
 */
export function VormHulp() {
  const p = "mt-2";
  const kop = "font-medium text-ink";
  return (
    <details className="rounded-md border border-border bg-paper px-3 py-2 text-xs text-ink-dim">
      <summary className="cursor-pointer text-ink">Hoe tik je de vormen van het examen in?</summary>
      <p className={p}>
        <span className={kop}>Tabel, per rij juist of fout.</span> Bij Vraag de opdracht, bijvoorbeeld
        &ldquo;Zijn deze uitspraken over de Romeinen juist of fout?&rdquo;. Bij Opties elke uitspraak op een eigen
        regel. Bij Antwoord per rij het juiste woord, met een komma ertussen: juist, fout, juist. Wil je andere
        kolommen, zet ze dan vooraan met een dubbelpunt erachter: Ja | Nee | Soms: ja, soms, nee.
      </p>
      <p className={p}>
        <span className={kop}>Keuzelijst in een zin.</span> Zet elke keuzelijst tussen dubbele haken, de opties
        gescheiden door een verticale streep, met een sterretje voor het juiste woord: De raaklijn is een
        [[*stijgende|dalende|horizontale]] rechte. Antwoord en Opties laat je leeg.
      </p>
      <p className={p}>
        <span className={kop}>In de juiste volgorde zetten.</span> Bij Opties de stappen in de juiste volgorde, één
        per regel. Het platform schudt ze zelf. Antwoord laat je leeg.
      </p>
      <p className={p}>
        <span className={kop}>Koppelen.</span> Bij Opties elk paar op een eigen regel, met een gelijkheidsteken
        ertussen: Caesar = Rome. Een antwoord te veel zet je op een regel die met het gelijkheidsteken begint:
        = Athene. Antwoord laat je leeg.
      </p>
      <p className={p}>
        <span className={kop}>Slepen naar kolommen.</span> Bij Opties elk kaartje met zijn kolom: piramide =
        Egypte. Bij Antwoord eventueel alle kolommen met een streep ertussen, Egypte | Griekenland | Rome, zo kan
        er ook een kolom leeg blijven.
      </p>
      <p className={p}>
        <span className={kop}>Woorden in een zin slepen.</span> Zet het juiste woord tussen dubbele haken in de zin:
        De Nijl stroomt door [[Egypte]]. Bij Opties de woorden die er te veel zijn, één per regel. Antwoord laat je
        leeg.
      </p>
      <p className={p}>
        <span className={kop}>Klikken op de prent.</span> Kies een afbeelding. Daarna trek je op de prent een vak
        rond de juiste plaats; het Antwoord vult zichzelf in. Meer dan één juiste plaats mag.
      </p>
      <p className={p}>
        <span className={kop}>Open antwoord.</span> Bij Antwoord een voorbeeldantwoord. Bij Opties eventueel de
        regels die al in het tekstvak staan, zoals Stap 1: en Stap 2:. Het kind kijkt zichzelf na met jouw
        voorbeeld.
      </p>
      <p className={p}>
        <span className={kop}>Tekenen.</span> Bij Antwoord een voorbeeldantwoord in woorden. Een afbeelding, zoals
        een rooster of een kaart, komt onder het tekenvak te liggen.
      </p>
      <p className={p}>
        <span className={kop}>Casus.</span> Bij elke vorm kan je een casus invullen: een situatie die boven de
        vraag staat. Geef de vragen van dezelfde casus precies dezelfde tekst.
      </p>
      <p className={p}>Een kind krijgt bij deze vormen alleen punten als alles juist is, net als op het examen.</p>
    </details>
  );
}

/**
 * Een vak trekken op de prent van een klikvraag. Wat je trekt, komt in het
 * antwoordveld als x, y, breedte, hoogte in procent; met meer vakken staat er
 * een puntkomma tussen.
 */
export function ZonePrikker({
  src,
  waarde,
  onWaarde,
}: {
  src: string;
  waarde: string;
  onWaarde: (w: string) => void;
}) {
  const [begin, setBegin] = useState<[number, number] | null>(null);
  const [nu, setNu] = useState<[number, number] | null>(null);
  const zones = waarde
    .split(";")
    .map((z) => z.split(",").map((n) => Number(n.trim())))
    .filter((z) => z.length === 4 && z.every(Number.isFinite));
  const procent = (e: React.PointerEvent<HTMLDivElement>): [number, number] => {
    const r = e.currentTarget.getBoundingClientRect();
    const rond = (n: number) => Math.round(Math.min(100, Math.max(0, n)) * 10) / 10;
    return [rond(((e.clientX - r.left) / r.width) * 100), rond(((e.clientY - r.top) / r.height) * 100)];
  };
  const vak = (a: [number, number], b: [number, number]) => [
    Math.min(a[0], b[0]),
    Math.min(a[1], b[1]),
    Math.round(Math.abs(a[0] - b[0]) * 10) / 10,
    Math.round(Math.abs(a[1] - b[1]) * 10) / 10,
  ];

  return (
    <div className="space-y-1">
      <div
        className="relative inline-block max-w-full cursor-crosshair touch-none select-none"
        onPointerDown={(e) => {
          e.currentTarget.setPointerCapture(e.pointerId);
          const p = procent(e);
          setBegin(p);
          setNu(p);
        }}
        onPointerMove={(e) => begin && setNu(procent(e))}
        onPointerUp={(e) => {
          if (!begin) return;
          const z = vak(begin, procent(e));
          setBegin(null);
          setNu(null);
          if (z[2] < 1 || z[3] < 1) return;
          onWaarde([...zones.map((x) => x.join(", ")), z.join(", ")].join("; "));
        }}
      >
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={src} alt="Prent om de juiste plaats op aan te duiden" draggable={false} className="block max-h-80 max-w-full rounded-md border border-border" />
        {[...zones, ...(begin && nu ? [vak(begin, nu)] : [])].map(([x, y, b, h], i) => (
          <span
            key={i}
            className="pointer-events-none absolute border-2 border-forest bg-forest/20"
            style={{ left: `${x}%`, top: `${y}%`, width: `${b}%`, height: `${h}%` }}
          />
        ))}
      </div>
      <p className="text-xs text-ink-dim">
        Trek een vak rond de juiste plaats.{" "}
        {zones.length > 0 && (
          <button type="button" className="underline" onClick={() => onWaarde("")}>
            Alle vakken wissen
          </button>
        )}
      </p>
    </div>
  );
}
