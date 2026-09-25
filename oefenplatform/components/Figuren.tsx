"use client";

/*
  Tekeningen en doe-oefeningen in een vraag, zonder dat de databank daarvoor
  iets nieuws hoeft te kennen.

  Een vraag kan een of meer "markeringen" tussen dubbele accolades bevatten:

    {{figuur cirkel 3/8}}   een cirkel in 8 stukken, waarvan er 3 gekleurd zijn
    {{figuur strook 2/5}}   hetzelfde als strook
    {{figuur raster 35/100}} een honderdveld met 35 gekleurde vakjes

    {{kleur cirkel 8}}      het kind kleurt zelf stukken in (invulvraag;
    {{kleur strook 5}}      het antwoord is hoeveel stukken gekleurd moeten zijn)
    {{kleur raster 100}}

    {{sleep klein-groot}}   het kind sleept de getallen op een lijn in volgorde
    {{sleep groot-klein}}   (invulvraag; de opties zijn de getallen in de juiste
                            volgorde, het antwoord is ze samen, gescheiden door " · ")

  Een kleur- of sleepvraag is dus gewoon een invulvraag: het platform bewaart en
  vergelijkt het antwoord zoals altijd, en de pagina waar ouders meekijken toont
  het als tekst.

  Daarnaast bestaan de tekeningen voor meetkunde en metend rekenen, met dezelfde
  soort markering ({{hoek 130}}, {{maat rechthoek 7x3}}, ...). Die staan in
  Tekeningen.tsx, met de volledige lijst erbij.
*/

import { useEffect, useMemo, useRef, useState, type PointerEvent as ReactPointerEvent } from "react";
import { TEKENINGEN, Tekening } from "@/components/Tekeningen";

export type Vorm = "cirkel" | "strook" | "raster";

export type Interactie =
  | { soort: "kleur"; vorm: Vorm; delen: number }
  | { soort: "sleep"; richting: "klein-groot" | "groot-klein" };

type Stuk =
  | { soort: "tekst"; tekst: string }
  | { soort: "figuur"; vorm: Vorm; teller: number; noemer: number }
  | { soort: "tekening"; naam: string; args: string[] };

const MARKERING = new RegExp(
  `\\{\\{\\s*(figuur|kleur|sleep|${TEKENINGEN.join("|")})\\s+([^}]*?)\\s*\\}\\}`,
  "g"
);
const VORMEN: Vorm[] = ["cirkel", "strook", "raster"];

/** Haalt de markeringen uit een vraag. */
export function leesVraag(vraag: string): { stukken: Stuk[]; interactie: Interactie | null; kaal: string } {
  const stukken: Stuk[] = [];
  let interactie: Interactie | null = null;
  let vorige = 0;
  for (const m of vraag.matchAll(MARKERING)) {
    if (m.index > vorige) stukken.push({ soort: "tekst", tekst: vraag.slice(vorige, m.index) });
    vorige = m.index + m[0].length;
    const [vormOfRichting, getal] = m[2].split(/\s+/);
    if (m[1] === "figuur") {
      const breuk = getal?.match(/^(\d+)\/(\d+)$/);
      if (VORMEN.includes(vormOfRichting as Vorm) && breuk) {
        stukken.push({ soort: "figuur", vorm: vormOfRichting as Vorm, teller: +breuk[1], noemer: +breuk[2] });
      }
    } else if (m[1] === "kleur") {
      const delen = Number(getal);
      if (VORMEN.includes(vormOfRichting as Vorm) && delen > 0) {
        interactie = { soort: "kleur", vorm: vormOfRichting as Vorm, delen };
      }
    } else if (m[1] === "sleep") {
      interactie = { soort: "sleep", richting: vormOfRichting === "groot-klein" ? "groot-klein" : "klein-groot" };
    } else {
      /* Een tekening voor meetkunde of metend rekenen; zie Tekeningen.tsx. */
      stukken.push({ soort: "tekening", naam: m[1], args: m[2].split(/\s+/) });
    }
  }
  if (vorige < vraag.length) stukken.push({ soort: "tekst", tekst: vraag.slice(vorige) });
  const kaal = stukken
    .filter((s): s is Extract<Stuk, { soort: "tekst" }> => s.soort === "tekst")
    .map((s) => s.tekst)
    .join(" ")
    .replace(/\s+/g, " ")
    .trim();
  return { stukken, interactie, kaal };
}

/** De vraagtekst met eventuele tekeningen erin, zonder de markeringen. */
export function VraagTekst({ tekst }: { tekst: string }) {
  const { stukken } = leesVraag(tekst);
  const woorden = stukken
    .filter((s) => s.soort === "tekst")
    .map((s) => (s as { tekst: string }).tekst)
    .join(" ")
    .replace(/\s+/g, " ")
    .trim();
  const figuren = stukken.filter((s) => s.soort === "figuur") as Extract<Stuk, { soort: "figuur" }>[];
  const tekeningen = stukken.filter((s) => s.soort === "tekening") as Extract<Stuk, { soort: "tekening" }>[];
  return (
    <>
      <p className="font-medium text-ink">{woorden}</p>
      {tekeningen.length > 0 && (
        <div className="mt-3 flex flex-wrap items-start gap-5">
          {tekeningen.map((t, i) => (
            <Tekening key={i} naam={t.naam} args={t.args} />
          ))}
        </div>
      )}
      {figuren.length > 0 && (
        <div className="mt-3 flex flex-wrap items-center gap-4">
          {figuren.map((f, i) => (
            <Figuur key={i} vorm={f.vorm} delen={f.noemer} gekleurd={new Set(range(f.teller))} />
          ))}
        </div>
      )}
    </>
  );
}

function range(n: number) {
  return Array.from({ length: n }, (_, i) => i);
}

// ---------------------------------------------------------------------------
// De tekening zelf. Met `onDruk` kan je er stukken in aanklikken.

function Figuur({
  vorm,
  delen,
  gekleurd,
  onDruk,
}: {
  vorm: Vorm;
  delen: number;
  gekleurd: Set<number>;
  onDruk?: (stuk: number, e: ReactPointerEvent<SVGElement>) => void;
}) {
  const vul = (i: number) => (gekleurd.has(i) ? "var(--forest)" : "#ffffff");
  const klikbaar = onDruk ? "cursor-pointer" : "";

  if (vorm === "cirkel") {
    const r = 70;
    const c = 76;
    // Afgerond, zodat server en browser exact hetzelfde pad tekenen.
    const punt = (a: number) => `${(c + r * Math.cos(a)).toFixed(2)} ${(c + r * Math.sin(a)).toFixed(2)}`;
    const stukken = range(delen).map((i) => {
      const a0 = (i / delen) * 2 * Math.PI - Math.PI / 2;
      const a1 = ((i + 1) / delen) * 2 * Math.PI - Math.PI / 2;
      const groot = a1 - a0 > Math.PI ? 1 : 0;
      const d =
        delen === 1
          ? `M ${c - r} ${c} a ${r} ${r} 0 1 0 ${2 * r} 0 a ${r} ${r} 0 1 0 ${-2 * r} 0`
          : `M ${c} ${c} L ${punt(a0)} A ${r} ${r} 0 ${groot} 1 ${punt(a1)} Z`;
      return (
        <path
          key={i}
          d={d}
          data-stuk={i}
          fill={vul(i)}
          stroke="var(--forest-dark)"
          strokeWidth={1.6}
          className={klikbaar}
          onPointerDown={onDruk ? (e) => onDruk(i, e) : undefined}
        />
      );
    });
    return (
      <svg viewBox="0 0 152 152" width={152} height={152} className="touch-none select-none">
        {stukken}
      </svg>
    );
  }

  if (vorm === "strook") {
    const b = Math.min(360, delen * 60);
    const w = b / delen;
    return (
      <svg viewBox={`0 0 ${b + 4} 48`} width="100%" style={{ maxWidth: b + 4 }} className="touch-none select-none">
        {range(delen).map((i) => (
          <rect
            key={i}
            x={2 + i * w}
            y={2}
            width={w}
            height={44}
            data-stuk={i}
            fill={vul(i)}
            stroke="var(--forest-dark)"
            strokeWidth={1.6}
            className={klikbaar}
            onPointerDown={onDruk ? (e) => onDruk(i, e) : undefined}
          />
        ))}
      </svg>
    );
  }

  // raster: honderd vakjes in tien rijen, of minder vakjes op één rij
  const kolommen = delen === 100 ? 10 : delen;
  const rijen = Math.ceil(delen / kolommen);
  const cel = delen === 100 ? 22 : 30;
  return (
    <svg
      viewBox={`0 0 ${kolommen * cel + 4} ${rijen * cel + 4}`}
      width="100%"
      style={{ maxWidth: kolommen * cel + 4 }}
      className="touch-none select-none"
    >
      {range(delen).map((i) => (
        <rect
          key={i}
          x={2 + (i % kolommen) * cel}
          y={2 + Math.floor(i / kolommen) * cel}
          width={cel}
          height={cel}
          data-stuk={i}
          fill={gekleurd.has(i) ? "var(--amber)" : "#ffffff"}
          stroke="var(--border)"
          strokeWidth={1}
          className={klikbaar}
          onPointerDown={onDruk ? (e) => onDruk(i, e) : undefined}
        />
      ))}
      <rect
        x={2}
        y={2}
        width={kolommen * cel}
        height={rijen * cel}
        fill="none"
        stroke="var(--forest-dark)"
        strokeWidth={1.6}
        pointerEvents="none"
      />
    </svg>
  );
}

// ---------------------------------------------------------------------------
// Zelf kleuren. Klik een stuk aan om het te kleuren of weer wit te maken; bij
// het honderdveld kan je ook met ingedrukte muis (of vinger) over de vakjes
// vegen.

export function KleurVraag({
  vorm,
  delen,
  uitgeschakeld,
  onAntwoord,
}: {
  vorm: Vorm;
  delen: number;
  uitgeschakeld: boolean;
  onAntwoord: (waarde: string) => void;
}) {
  const [gekleurd, setGekleurd] = useState<Set<number>>(new Set());
  // Een kopie buiten React, zodat snel vegen over veel vakjes na elkaar geen
  // vakje overslaat omdat de vorige wijziging nog niet getekend was.
  const stand = useRef<Set<number>>(new Set());
  const veeg = useRef<null | boolean>(null);

  function zet(stuk: number, aan: boolean) {
    if (stand.current.has(stuk) === aan) return;
    const nieuw = new Set(stand.current);
    if (aan) nieuw.add(stuk);
    else nieuw.delete(stuk);
    stand.current = nieuw;
    setGekleurd(nieuw);
    onAntwoord(nieuw.size ? String(nieuw.size) : "");
  }

  useEffect(() => {
    const stop = () => (veeg.current = null);
    window.addEventListener("pointerup", stop);
    window.addEventListener("pointercancel", stop);
    return () => {
      window.removeEventListener("pointerup", stop);
      window.removeEventListener("pointercancel", stop);
    };
  }, []);

  function beweeg(e: ReactPointerEvent<HTMLDivElement>) {
    if (veeg.current === null || uitgeschakeld) return;
    const el = document.elementFromPoint(e.clientX, e.clientY);
    const stuk = el?.getAttribute("data-stuk");
    if (stuk !== null && stuk !== undefined) zet(Number(stuk), veeg.current);
  }

  return (
    <div className="mt-3">
      <div onPointerMove={beweeg} className={uitgeschakeld ? "pointer-events-none" : ""}>
        <Figuur
          vorm={vorm}
          delen={delen}
          gekleurd={gekleurd}
          onDruk={(stuk, e) => {
            if (uitgeschakeld) return;
            e.preventDefault();
            const aan = !stand.current.has(stuk);
            veeg.current = aan;
            zet(stuk, aan);
          }}
        />
      </div>
      <p className="mt-2 text-xs text-ink-dim">
        Gekleurd: {gekleurd.size} van de {delen}
        {!uitgeschakeld && gekleurd.size > 0 && (
          <>
            {" · "}
            <button
              type="button"
              onClick={() => {
                stand.current = new Set();
                setGekleurd(new Set());
                onAntwoord("");
              }}
              className="underline underline-offset-2"
            >
              wis alles
            </button>
          </>
        )}
      </p>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Getallen in volgorde slepen. Een kaartje sleep je naar een plaats op de lijn,
// of je tikt het aan en tikt daarna de plaats aan: dat laatste werkt ook op een
// telefoon en voor wie slepen moeilijk vindt.

/** "0,65" → 0.65, "3/4" → 0.75, "1 1/2" → 1.5. null als het geen getal is. */
export function alsGetal(tekst: string): number | null {
  const t = tekst.replace(/−/g, "-").replace(/[€\s]+$/g, "").trim();
  let m = t.match(/^(-?\d+) (\d+)\/(\d+)$/);
  if (m) return Number(m[1]) + Number(m[2]) / Number(m[3]);
  m = t.match(/^(-?\d+)\/(\d+)$/);
  if (m) return Number(m[1]) / Number(m[2]);
  m = t.match(/^-?\d+(,\d+)?$/);
  if (m) return Number(t.replace(",", "."));
  return null;
}

/** Een vaste, geschudde volgorde uit het id van de vraag, nooit al de juiste. */
function geschud(items: string[], zaadtekst: string): string[] {
  let h = 0x811c9dc5;
  for (let i = 0; i < zaadtekst.length; i++) h = Math.imul(h ^ zaadtekst.charCodeAt(i), 0x01000193);
  const volgend = () => {
    h = Math.imul(h ^ (h >>> 13), 0x5bd1e995) >>> 0;
    return (h >>> 0) / 4294967296;
  };
  const uit = [...items];
  for (let poging = 0; poging < 5; poging++) {
    for (let i = uit.length - 1; i > 0; i--) {
      const j = Math.floor(volgend() * (i + 1));
      [uit[i], uit[j]] = [uit[j], uit[i]];
    }
    if (uit.some((x, i) => x !== items[i])) return uit;
  }
  return [...uit.slice(1), uit[0]];
}

export const SLEEP_SCHEIDING = " · ";

export function SleepVraag({
  id,
  items,
  richting,
  uitgeschakeld,
  onAntwoord,
}: {
  id: string;
  items: string[];
  richting: "klein-groot" | "groot-klein";
  uitgeschakeld: boolean;
  onAntwoord: (waarde: string) => void;
}) {
  const begin = useMemo(() => geschud(items, id), [items, id]);
  const [plaatsen, setPlaatsen] = useState<(string | null)[]>(() => items.map(() => null));
  const [gekozen, setGekozen] = useState<string | null>(null);
  const [sleep, setSleep] = useState<{ item: string; x: number; y: number } | null>(null);
  // Wat er gesleept wordt, ook buiten React bewaard: de loslaat-luisteraar
  // hieronder moet het lezen zonder op een nieuwe tekening te wachten.
  const gesleept = useRef<{ item: string; bewogen: boolean } | null>(null);
  const stand = useRef(plaatsen);

  const inBak = begin.filter((x) => !plaatsen.includes(x));

  function bewaar(nieuw: (string | null)[]) {
    stand.current = nieuw;
    setPlaatsen(nieuw);
    onAntwoord(nieuw.every((x) => x !== null) ? nieuw.join(SLEEP_SCHEIDING) : "");
  }

  function zetOp(item: string, plaats: number) {
    const nieuw = [...stand.current];
    const van = nieuw.indexOf(item);
    if (van >= 0) nieuw[van] = nieuw[plaats]; // wisselen met wat er stond
    nieuw[plaats] = item;
    bewaar(nieuw);
    setGekozen(null);
  }

  function terugNaarBak(plaats: number) {
    const nieuw = [...stand.current];
    nieuw[plaats] = null;
    bewaar(nieuw);
  }

  // slepen met muis of vinger
  const zetOpRef = useRef(zetOp);
  useEffect(() => {
    zetOpRef.current = zetOp;
  });
  useEffect(() => {
    const beweeg = (e: PointerEvent) => {
      if (!gesleept.current) return;
      gesleept.current.bewogen = true;
      setSleep({ item: gesleept.current.item, x: e.clientX, y: e.clientY });
    };
    const los = (e: PointerEvent) => {
      const g = gesleept.current;
      if (!g) return;
      gesleept.current = null;
      setSleep(null);
      const el = document.elementFromPoint(e.clientX, e.clientY)?.closest("[data-plaats]");
      if (g.bewogen && el) zetOpRef.current(g.item, Number(el.getAttribute("data-plaats")));
      else if (!g.bewogen) setGekozen((k) => (k === g.item ? null : g.item));
    };
    window.addEventListener("pointermove", beweeg);
    window.addEventListener("pointerup", los);
    window.addEventListener("pointercancel", los);
    return () => {
      window.removeEventListener("pointermove", beweeg);
      window.removeEventListener("pointerup", los);
      window.removeEventListener("pointercancel", los);
    };
  }, []);

  const pak = (item: string) => (e: ReactPointerEvent<HTMLButtonElement>) => {
    if (uitgeschakeld) return;
    e.preventDefault();
    e.stopPropagation();
    gesleept.current = { item, bewogen: false };
  };

  const [links, rechts] = richting === "klein-groot" ? ["klein", "groot"] : ["groot", "klein"];

  const kaartje = (item: string, actief: boolean) =>
    `touch-none select-none rounded-lg border-2 px-3 py-2 text-base font-semibold tabular-nums shadow-sm transition ${
      actief ? "border-amber bg-amber/10 text-ink" : "border-forest bg-surface text-forest-dark"
    } ${uitgeschakeld ? "cursor-default" : "cursor-grab"}`;

  return (
    <div className="mt-4">
      <div className="flex items-end gap-2">
        {plaatsen.map((item, i) => (
          <div
            key={i}
            data-plaats={i}
            onClick={() => {
              if (uitgeschakeld) return;
              if (gekozen) zetOp(gekozen, i);
              else if (item) terugNaarBak(i);
            }}
            className={`flex h-14 min-w-0 flex-1 items-center justify-center rounded-lg border-2 border-dashed ${
              gekozen && !uitgeschakeld ? "border-amber bg-amber/5" : "border-border bg-paper"
            }`}
          >
            {item ? (
              <button type="button" onPointerDown={pak(item)} className={kaartje(item, false)}>
                {item}
              </button>
            ) : (
              <span className="text-xs text-ink-dim">{i + 1}</span>
            )}
          </div>
        ))}
      </div>
      <div className="relative mt-2 h-4">
        <div className="absolute left-0 right-3 top-2 h-0.5 bg-ink" />
        <div className="absolute right-0 top-[3px] h-0 w-0 border-y-[6px] border-l-[12px] border-y-transparent border-l-ink" />
      </div>
      <div className="flex justify-between text-xs text-ink-dim">
        <span>{links}</span>
        <span>{rechts}</span>
      </div>

      {inBak.length > 0 && !uitgeschakeld && (
        <div className="mt-4 flex flex-wrap gap-2 rounded-lg bg-paper p-3">
          {inBak.map((item) => (
            <button
              key={item}
              type="button"
              onPointerDown={pak(item)}
              className={kaartje(item, gekozen === item)}
            >
              {item}
            </button>
          ))}
          <p className="w-full text-xs text-ink-dim">
            Sleep elk getal naar zijn plaats, of tik een getal aan en daarna een plaats.
          </p>
        </div>
      )}

      {uitgeschakeld && <EchteLijn items={items} />}

      {sleep && (
        <div
          className="pointer-events-none fixed z-50 -translate-x-1/2 -translate-y-1/2 rounded-lg border-2 border-amber bg-surface px-3 py-2 text-base font-semibold shadow-lg"
          style={{ left: sleep.x, top: sleep.y }}
        >
          {sleep.item}
        </div>
      )}
    </div>
  );
}

/** Na het controleren: waar de getallen écht op de getallenlijn liggen. */
function EchteLijn({ items }: { items: string[] }) {
  const waarden = items.map(alsGetal);
  if (waarden.some((w) => w === null)) return null;
  const w = waarden as number[];
  const min = Math.min(...w);
  const max = Math.max(...w);
  // Liggen ze allemaal tussen 0 en 1, dan tonen we de hele lijn van 0 tot 1
  // in tienden: zo zie je meteen dat 0,7 verder ligt dan 0,65. Anders kiezen
  // we een stap waarbij er hoogstens tien streepjes zijn.
  let van: number, tot: number, stap: number;
  if (min >= 0 && max <= 1 && max - min >= 0.1) {
    [van, tot, stap] = [0, 1, 0.1];
  } else {
    stap = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001].reverse().find((s) => (max - min) / s <= 8) ?? 1;
    van = Math.floor(min / stap - 1e-9) * stap;
    tot = Math.ceil(max / stap + 1e-9) * stap;
    if (tot - van < stap * 2) tot = van + stap * 2;
  }
  const breedte = 340;
  const m = 16;
  const x = (v: number) => m + ((v - van) / (tot - van)) * (breedte - 2 * m);
  const streepjes = Math.round((tot - van) / stap);
  const label = (v: number) => String(Math.round(v * 1000) / 1000).replace(".", ",");
  return (
    <div className="mt-4 rounded-lg bg-paper p-3">
      <p className="text-xs text-ink-dim">Zo liggen ze echt op de getallenlijn:</p>
      <svg viewBox={`0 0 ${breedte} ${40 + items.length * 14}`} width="100%">
        <line x1={m} y1={20} x2={breedte - m} y2={20} stroke="var(--ink)" strokeWidth={1.6} />
        {range(streepjes + 1).map((i) => (
            <g key={i}>
              <line x1={x(van + i * stap)} y1={15} x2={x(van + i * stap)} y2={25} stroke="var(--ink-dim)" />
              <text x={x(van + i * stap)} y={11} textAnchor="middle" fontSize={9} fill="var(--ink-dim)">
                {label(van + i * stap)}
              </text>
            </g>
          ))}
        {items.map((item, i) => (
          <g key={item}>
            <circle cx={x(w[i])} cy={20} r={4.5} fill="var(--amber)" />
            <line x1={x(w[i])} y1={24} x2={x(w[i])} y2={30 + i * 14} stroke="var(--amber)" strokeDasharray="2 2" />
            <text
              x={x(w[i])}
              y={30 + i * 14 + 10}
              textAnchor="middle"
              fontSize={11}
              fontWeight={600}
              fill="var(--forest-dark)"
            >
              {item}
            </text>
          </g>
        ))}
      </svg>
    </div>
  );
}
