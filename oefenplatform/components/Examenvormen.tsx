"use client";

/*
  De vraagvormen van het examen van de Examencommissie die na de tabel en de
  keuzelijst kwamen: volgorde, koppelen, sorteren in kolommen, woorden in een
  zin slepen, klikken op een prent, een open antwoord en tekenen. Hoe ze
  bewaard worden, staat in lib/examenvormen.ts.

  Slepen kan met de muis, maar alles werkt ook door te tikken: eerst wat je
  wil verplaatsen, dan waar het moet komen. Dat werkt op een telefoon en voor
  wie slepen moeilijk vindt; veel van onze kinderen zijn motorisch minder sterk.
*/

import { useEffect, useRef, useState } from "react";
import { Formule } from "@/components/Formule";
import {
  beginVolgorde,
  geschud,
  inZone,
  leesKoppeling,
  leesSleepzin,
  leesZones,
  volgordeJuist,
} from "@/lib/examenvormen";

type Basis = {
  id: string;
  vraag: string;
  opties: string[] | null;
  antwoord: unknown;
};

const KAARTJE =
  "rounded-md border px-3 py-1.5 text-sm transition select-none";

// ---------------------------------------------------------------------------
// Volgorde

export function VolgordeVraag({
  vraag,
  gekozen,
  nagekeken,
  onKies,
}: {
  vraag: Basis;
  gekozen: number[] | null;
  nagekeken: boolean;
  onKies: (volgorde: number[]) => void;
}) {
  const juist = volgordeJuist(vraag.opties, vraag.antwoord);
  const nu = gekozen ?? beginVolgorde(vraag.id, juist);
  // De beginvolgorde telt meteen als antwoord: wie ze goed vindt, mag zo
  // nakijken. Ze is nooit al de juiste, zie beginVolgorde.
  useEffect(() => {
    if (!gekozen) onKies(nu);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [gekozen]);
  const verplaats = (van: number, naar: number) => {
    if (naar < 0 || naar >= nu.length || van === naar) return;
    const lijst = [...nu];
    const [stap] = lijst.splice(van, 1);
    lijst.splice(naar, 0, stap);
    onKies(lijst);
  };

  return (
    <div className="mt-3 space-y-3">
      <ol className="space-y-1.5">
        {nu.map((k, plaats) => {
          const fout = nagekeken && juist[plaats] !== k;
          return (
            <li
              key={k}
              draggable={!nagekeken}
              onDragStart={(e) => e.dataTransfer.setData("text/plain", String(plaats))}
              onDragOver={(e) => e.preventDefault()}
              onDrop={(e) => {
                e.preventDefault();
                verplaats(Number(e.dataTransfer.getData("text/plain")), plaats);
              }}
              className={`flex items-center gap-2 rounded-md border px-3 py-2 text-sm ${
                fout ? "border-danger bg-danger/5" : "border-border bg-paper"
              } ${nagekeken ? "" : "cursor-grab"}`}
            >
              <span className="w-5 shrink-0 text-ink-dim">{plaats + 1}.</span>
              <span className="min-w-0 flex-1 text-ink">
                <Formule tekst={vraag.opties?.[k] ?? ""} />
              </span>
              {!nagekeken && (
                <span className="flex shrink-0 gap-1">
                  <button
                    type="button"
                    onClick={() => verplaats(plaats, plaats - 1)}
                    disabled={plaats === 0}
                    aria-label="Een plaats hoger"
                    className="rounded border border-border px-2 py-0.5 text-ink disabled:opacity-30"
                  >
                    ↑
                  </button>
                  <button
                    type="button"
                    onClick={() => verplaats(plaats, plaats + 1)}
                    disabled={plaats === nu.length - 1}
                    aria-label="Een plaats lager"
                    className="rounded border border-border px-2 py-0.5 text-ink disabled:opacity-30"
                  >
                    ↓
                  </button>
                </span>
              )}
            </li>
          );
        })}
      </ol>
      {!nagekeken && (
        <p className="text-xs text-ink-dim">
          Sleep een stap naar haar plaats, of schuif ze met de pijltjes.
        </p>
      )}
      {nagekeken && juist.some((k, i) => nu[i] !== k) && (
        <div className="rounded-md bg-paper px-3 py-2 text-sm text-ink">
          <p className="font-medium">De juiste volgorde:</p>
          <ol className="mt-1 list-decimal pl-5">
            {juist.map((k) => (
              <li key={k}>
                <Formule tekst={vraag.opties?.[k] ?? ""} />
              </li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Koppelen: per rij links kies je wat er rechts bij hoort.

export function KoppelVraag({
  vraag,
  gekozen,
  nagekeken,
  onKies,
}: {
  vraag: Basis;
  gekozen: number[];
  nagekeken: boolean;
  onKies: (rij: number, keuze: number) => void;
}) {
  const t = leesKoppeling(vraag.opties, vraag.antwoord);
  if (!t) return null;
  const volgorde = geschud(vraag.id, 1, t.kolommen.length);
  return (
    <div className="mt-3 space-y-2">
      {t.rijen.map((rij, r) => {
        const fout = nagekeken && gekozen[r] !== t.juist[r];
        return (
          <div
            key={r}
            className={`flex flex-wrap items-center gap-2 rounded-md border px-3 py-2 text-sm ${
              fout ? "border-danger bg-danger/5" : "border-border"
            }`}
          >
            <span className="min-w-0 flex-1 text-ink">
              <Formule tekst={rij} />
            </span>
            <select
              value={gekozen[r] ?? -1}
              disabled={nagekeken}
              onChange={(e) => onKies(r, Number(e.target.value))}
              aria-label={`Wat hoort bij ${rij}`}
              className="max-w-full rounded-md border border-border bg-paper px-2 py-1 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            >
              <option value={-1}>kies...</option>
              {volgorde.map((k) => (
                <option key={k} value={k}>
                  {t.kolommen[k]}
                </option>
              ))}
            </select>
            {fout && (
              <span className="w-full text-xs text-ink">
                Juist was: <strong>{t.kolommen[t.juist[r]]}</strong>
              </span>
            )}
          </div>
        );
      })}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Sorteren: elk kaartje in de juiste kolom.

export function SorteerVraag({
  vraag,
  gekozen,
  nagekeken,
  onKies,
}: {
  vraag: Basis;
  gekozen: number[];
  nagekeken: boolean;
  onKies: (kaartje: number, kolom: number) => void;
}) {
  const [vast, setVast] = useState<number | null>(null);
  const t = leesKoppeling(vraag.opties, vraag.antwoord);
  if (!t) return null;
  const volgorde = geschud(vraag.id, 1, t.rijen.length);
  const leg = (kolom: number) => {
    if (vast === null || nagekeken) return;
    onKies(vast, kolom);
    setVast(null);
  };
  const kaartje = (k: number) => {
    const fout = nagekeken && gekozen[k] !== t.juist[k];
    return (
      <button
        key={k}
        type="button"
        draggable={!nagekeken}
        disabled={nagekeken}
        onDragStart={(e) => e.dataTransfer.setData("text/plain", String(k))}
        onClick={() => setVast(vast === k ? null : k)}
        className={`${KAARTJE} ${
          fout
            ? "border-danger bg-danger/5 text-ink"
            : vast === k
              ? "border-forest bg-forest text-paper"
              : "border-border bg-paper text-ink hover:border-forest"
        }`}
      >
        <Formule tekst={t.rijen[k]} />
      </button>
    );
  };
  const nogLos = volgorde.filter((k) => (gekozen[k] ?? -1) < 0);

  return (
    <div className="mt-3 space-y-3">
      <div
        onDragOver={(e) => e.preventDefault()}
        onDrop={(e) => {
          e.preventDefault();
          onKies(Number(e.dataTransfer.getData("text/plain")), -1);
        }}
        onClick={(e) => {
          if (e.target === e.currentTarget && vast !== null) {
            onKies(vast, -1);
            setVast(null);
          }
        }}
        className="flex min-h-12 flex-wrap gap-2 rounded-md border border-dashed border-border p-2"
      >
        {nogLos.length ? nogLos.map(kaartje) : <span className="text-xs text-ink-dim">Alles ligt in een kolom.</span>}
      </div>
      <div className="grid gap-2" style={{ gridTemplateColumns: `repeat(auto-fit, minmax(9rem, 1fr))` }}>
        {t.kolommen.map((naam, c) => (
          <div
            key={c}
            onDragOver={(e) => e.preventDefault()}
            onDrop={(e) => {
              e.preventDefault();
              if (!nagekeken) onKies(Number(e.dataTransfer.getData("text/plain")), c);
            }}
            onClick={(e) => {
              if (e.target === e.currentTarget || (e.target as HTMLElement).dataset.kop) leg(c);
            }}
            className={`flex min-h-24 flex-col gap-2 rounded-md border p-2 ${
              vast !== null ? "cursor-pointer border-forest" : "border-border"
            }`}
          >
            <p data-kop="1" className="text-center text-sm font-medium text-ink">
              {naam}
            </p>
            {volgorde.filter((k) => gekozen[k] === c).map(kaartje)}
          </div>
        ))}
      </div>
      {!nagekeken && (
        <p className="text-xs text-ink-dim">
          Sleep elk kaartje naar een kolom, of tik een kaartje aan en daarna de kolom.
        </p>
      )}
      {nagekeken && t.juist.some((k, i) => gekozen[i] !== k) && (
        <div className="rounded-md bg-paper px-3 py-2 text-sm text-ink">
          <p className="font-medium">Zo hoorde het:</p>
          {t.kolommen.map((naam, c) => (
            <p key={c}>
              {naam}:{" "}
              {t.rijen.filter((_, i) => t.juist[i] === c).join(", ") || "niets"}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Een zin met lege vakken, en woorden om erin te slepen.

export function SleepZin({
  vraag,
  gekozen,
  nagekeken,
  onKies,
}: {
  vraag: Basis;
  gekozen: number[];
  nagekeken: boolean;
  onKies: (lijst: number[]) => void;
}) {
  const [vast, setVast] = useState<number | null>(null);
  const woorden = vraag.opties ?? [];
  const juist = Array.isArray(vraag.antwoord) ? (vraag.antwoord as number[]).map(Number) : [];
  const stukken = leesSleepzin(vraag.vraag);
  const aantal = stukken.filter((s) => s.soort === "vak").length;
  const volgorde = geschud(vraag.id, 1, woorden.length);
  const gebruikt = new Set(gekozen.filter((k) => k >= 0));

  const zet = (vak: number, woord: number) => {
    // Een woord ligt maar op één plaats tegelijk.
    const nu = Array.from({ length: aantal }, (_, i) => {
      const k = gekozen[i] ?? -1;
      return woord >= 0 && k === woord ? -1 : k;
    });
    nu[vak] = woord;
    onKies(nu);
  };
  const leg = zet;

  return (
    <div className="mt-1 space-y-3">
      <p className="font-medium leading-loose text-ink">
        {stukken.map((s, i) => {
          if (s.soort === "tekst") return <Formule key={i} tekst={s.tekst} />;
          const k = gekozen[s.nummer] ?? -1;
          const fout = nagekeken && k !== juist[s.nummer];
          return (
            <button
              key={i}
              type="button"
              disabled={nagekeken}
              onDragOver={(e) => e.preventDefault()}
              onDrop={(e) => {
                e.preventDefault();
                leg(s.nummer, Number(e.dataTransfer.getData("text/plain")));
              }}
              onClick={() => {
                if (vast !== null) {
                  leg(s.nummer, vast);
                  setVast(null);
                } else if (k >= 0) zet(s.nummer, -1);
              }}
              aria-label={`Leeg vak ${s.nummer + 1}`}
              className={`mx-1 inline-block min-w-20 rounded-md border-2 border-dashed px-2 py-0.5 text-sm font-normal ${
                fout ? "border-danger text-danger" : k >= 0 ? "border-forest text-ink" : vast !== null ? "border-forest" : "border-border text-ink-dim"
              }`}
            >
              {k >= 0 ? woorden[k] : " "}
            </button>
          );
        })}
      </p>
      {!nagekeken && (
        <>
          <div className="flex flex-wrap gap-2">
            {volgorde.map((w) => (
              <button
                key={w}
                type="button"
                draggable
                onDragStart={(e) => e.dataTransfer.setData("text/plain", String(w))}
                onClick={() => setVast(vast === w ? null : w)}
                className={`${KAARTJE} ${
                  vast === w
                    ? "border-forest bg-forest text-paper"
                    : gebruikt.has(w)
                      ? "border-border text-ink-dim line-through"
                      : "border-border bg-paper text-ink hover:border-forest"
                }`}
              >
                {woorden[w]}
              </button>
            ))}
          </div>
          <p className="text-xs text-ink-dim">
            Sleep een woord naar een leeg vak, of tik het woord aan en daarna het vak. Tik op een gevuld vak om het weer leeg te maken.
          </p>
        </>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Klikken op de juiste plaats in een prent.

export function HotspotVraag({
  vraag,
  afbeeldingUrl,
  gekozen,
  nagekeken,
  onKies,
}: {
  vraag: Basis;
  afbeeldingUrl: string | null | undefined;
  gekozen: number[] | null;
  nagekeken: boolean;
  onKies: (punt: number[]) => void;
}) {
  if (!afbeeldingUrl) {
    return <p className="mt-3 text-sm text-danger">De prent bij deze vraag ontbreekt. Meld dat even met de knop hieronder.</p>;
  }
  const zones = leesZones(vraag.antwoord);
  const juist = gekozen ? inZone(gekozen, zones) : false;
  return (
    <div className="mt-3">
      <div className="relative inline-block max-w-full">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          src={afbeeldingUrl}
          alt="Prent bij deze vraag: klik op de juiste plaats"
          draggable={false}
          onClick={(e) => {
            if (nagekeken) return;
            const r = e.currentTarget.getBoundingClientRect();
            onKies([
              Math.round(((e.clientX - r.left) / r.width) * 1000) / 10,
              Math.round(((e.clientY - r.top) / r.height) * 1000) / 10,
            ]);
          }}
          className={`block max-h-[28rem] max-w-full rounded-md border border-border ${nagekeken ? "" : "cursor-crosshair"}`}
        />
        {nagekeken &&
          zones.map(([x, y, b, h], i) => (
            <span
              key={i}
              className="pointer-events-none absolute rounded-md border-2 border-forest bg-forest/15"
              style={{ left: `${x}%`, top: `${y}%`, width: `${b}%`, height: `${h}%` }}
            />
          ))}
        {gekozen && (
          <span
            aria-hidden
            className={`pointer-events-none absolute h-5 w-5 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-white shadow ${
              nagekeken && !juist ? "bg-danger" : "bg-forest"
            }`}
            style={{ left: `${gekozen[0]}%`, top: `${gekozen[1]}%` }}
          />
        )}
      </div>
      {!nagekeken && <p className="mt-1 text-xs text-ink-dim">Klik op de plaats in de prent. Een tweede klik verzet je stip.</p>}
      {nagekeken && !juist && <p className="mt-1 text-xs text-ink">Het groene vak is de juiste plaats.</p>}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Een open antwoord, en het voorbeeld om jezelf na te kijken.

export function OpenVraag({
  vraag,
  gekozen,
  nagekeken,
  onKies,
}: {
  vraag: Basis;
  gekozen: string | null;
  nagekeken: boolean;
  onKies: (tekst: string) => void;
}) {
  const begin = (vraag.opties ?? []).join("\n");
  return (
    <textarea
      value={gekozen ?? begin}
      disabled={nagekeken}
      onChange={(e) => onKies(e.target.value)}
      rows={Math.max(5, (vraag.opties?.length ?? 0) * 2 + 2)}
      spellCheck={false}
      autoCorrect="off"
      autoCapitalize="off"
      autoComplete="off"
      placeholder="Typ hier je antwoord..."
      aria-label="Jouw antwoord"
      className="mt-3 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm leading-relaxed text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
    />
  );
}

/**
 * Wat een kind ziet nadat het antwoordde op een open vraag of een tekening:
 * het voorbeeldantwoord, en twee knoppen om zelf te zeggen of het juist was.
 */
export function ZelfNakijken({
  voorbeeld,
  onOordeel,
}: {
  voorbeeld: string;
  onOordeel: (juist: boolean) => void;
}) {
  return (
    <div className="mt-4 rounded-md border border-info/40 bg-info/5 px-3 py-3 text-sm text-ink">
      <p className="font-medium">Een voorbeeldantwoord</p>
      <p className="mt-1 whitespace-pre-line">
        <Formule tekst={voorbeeld} />
      </p>
      <p className="mt-3 text-ink-dim">
        Leg het naast jouw antwoord. Staat alles wat belangrijk is erin, ook in je eigen woorden?
      </p>
      <div className="mt-2 flex flex-wrap gap-2">
        <button
          type="button"
          onClick={() => onOordeel(true)}
          className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
        >
          Ik had het juist
        </button>
        <button
          type="button"
          onClick={() => onOordeel(false)}
          className="rounded-md border border-border px-4 py-2 text-sm text-ink hover:border-forest"
        >
          Nog niet helemaal
        </button>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Tekenen. De tekening blijft in de browser; bewaard wordt enkel dát er
// getekend is. Een tekening van een kind naar de databank sturen kost veel
// verkeer, en meer dan zelf nakijken doet er niemand mee.

export function TekenVraag({
  afbeeldingUrl,
  nagekeken,
  onKies,
}: {
  afbeeldingUrl: string | null | undefined;
  nagekeken: boolean;
  onKies: (waarde: string) => void;
}) {
  const doek = useRef<HTMLCanvasElement>(null);
  const bezig = useRef(false);
  const [gom, setGom] = useState(false);

  useEffect(() => {
    const c = doek.current;
    if (!c) return;
    const schaal = window.devicePixelRatio || 1;
    const breed = c.clientWidth;
    const hoog = c.clientHeight;
    c.width = breed * schaal;
    c.height = hoog * schaal;
    const ctx = c.getContext("2d");
    ctx?.scale(schaal, schaal);
  }, []);

  const punt = (e: React.PointerEvent<HTMLCanvasElement>) => {
    const r = e.currentTarget.getBoundingClientRect();
    return [e.clientX - r.left, e.clientY - r.top] as const;
  };

  return (
    <div className="mt-3 space-y-2">
      <div
        className="relative w-full overflow-hidden rounded-md border border-border bg-white"
        style={{
          backgroundImage: afbeeldingUrl
            ? `url("${afbeeldingUrl}")`
            : "linear-gradient(#e5e7eb 1px, transparent 1px), linear-gradient(90deg, #e5e7eb 1px, transparent 1px)",
          backgroundSize: afbeeldingUrl ? "contain" : "24px 24px",
          backgroundRepeat: afbeeldingUrl ? "no-repeat" : "repeat",
          backgroundPosition: "center",
        }}
      >
        <canvas
          ref={doek}
          aria-label="Tekenvak"
          className="block h-80 w-full touch-none"
          onPointerDown={(e) => {
            if (nagekeken) return;
            bezig.current = true;
            e.currentTarget.setPointerCapture(e.pointerId);
            const ctx = e.currentTarget.getContext("2d");
            const [x, y] = punt(e);
            ctx?.beginPath();
            ctx?.moveTo(x, y);
          }}
          onPointerMove={(e) => {
            if (!bezig.current) return;
            const ctx = e.currentTarget.getContext("2d");
            if (!ctx) return;
            const [x, y] = punt(e);
            ctx.globalCompositeOperation = gom ? "destination-out" : "source-over";
            ctx.lineWidth = gom ? 18 : 2.5;
            ctx.lineCap = "round";
            ctx.lineJoin = "round";
            ctx.strokeStyle = "#1f2a1a";
            ctx.lineTo(x, y);
            ctx.stroke();
          }}
          onPointerUp={() => {
            if (!bezig.current) return;
            bezig.current = false;
            onKies("getekend");
          }}
        />
      </div>
      {!nagekeken && (
        <div className="flex flex-wrap gap-2 text-sm">
          <button
            type="button"
            onClick={() => setGom(false)}
            aria-pressed={!gom}
            className={`rounded-md border px-3 py-1 ${!gom ? "border-forest bg-forest/5" : "border-border"}`}
          >
            ✏️ Potlood
          </button>
          <button
            type="button"
            onClick={() => setGom(true)}
            aria-pressed={gom}
            className={`rounded-md border px-3 py-1 ${gom ? "border-forest bg-forest/5" : "border-border"}`}
          >
            Gom
          </button>
          <button
            type="button"
            onClick={() => {
              const c = doek.current;
              c?.getContext("2d")?.clearRect(0, 0, c.width, c.height);
              onKies("");
            }}
            className="rounded-md border border-border px-3 py-1"
          >
            Alles wissen
          </button>
        </div>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Een casus: één situatie bovenaan, die bij elke vraag van de casus terugkomt.

export function Casus({ tekst }: { tekst: string }) {
  return (
    <div className="mb-3 rounded-md border-l-4 border-amber bg-amber/10 px-3 py-2 text-sm text-ink">
      <p className="text-xs font-medium uppercase tracking-wide text-ink-dim">Casus</p>
      <p className="mt-1 whitespace-pre-line">
        <Formule tekst={tekst} />
      </p>
    </div>
  );
}
