"use client";

import { useState } from "react";
import { puzzelRooster, type Puzzelbeeld } from "@/lib/leerbundel";

/*
  De puzzel op de eindhalte: een tekening uit het hoofdstuk zelf, in stukken.
  De stukken liggen apart, je klikt er een aan en zet het dan op zijn plaats.

  Dit was eerst een schuifpuzzel. Kim op 29 september 2026, met een
  schermafbeelding erbij: "hier kan je niets schuiven, misschien is de blokjes
  naar de zijkant zetten en dat je dan ze 1 voor 1 op de juiste plaats kan
  zetten beter?" Klopt: bij een schuifpuzzel kunnen er maar twee of drie
  stukken tegelijk bewegen, en alle andere doen niets als je erop klikt. Op een
  telefoon voelt dat alsof het spel kapot is.

  Nu kan elk stuk altijd ergens naartoe, en kan je alles weer weghalen. Fout
  leggen mag: er raakt niets vast, en de knop "kijk na" laat zien wat al goed
  staat.

  Er zit geen slot op en er wordt niets bewaard: het is een spelletje.
*/

function husselen(lijst: number[]): number[] {
  const uit = [...lijst];
  for (let i = uit.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [uit[i], uit[j]] = [uit[j], uit[i]];
  }
  return uit;
}

/** Het beeld, verschoven zodat net dit stuk in beeld staat. */
function Stuk({
  beeld,
  stuk,
  kolommen,
  rijen,
}: {
  beeld: Puzzelbeeld;
  stuk: number;
  kolommen: number;
  rijen: number;
}) {
  if (beeld.soort === "prent") {
    // De prent wordt zo groot als het hele bord gelegd en dan verschoven, het
    // aloude trucje met een achtergrondafbeelding.
    return (
      <span
        aria-hidden
        className="pointer-events-none absolute inset-0"
        style={{
          backgroundImage: `url(${beeld.url})`,
          backgroundSize: `${kolommen * 100}% ${rijen * 100}%`,
          backgroundPosition: `${((stuk % kolommen) / (kolommen - 1)) * 100}% ${(
            (Math.floor(stuk / kolommen) / (rijen - 1)) *
            100
          ).toFixed(2)}%`,
        }}
      />
    );
  }
  return (
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
  );
}

/** Het hele beeld, om te tonen hoe het moet worden. */
function HeelBeeld({
  beeld,
  className,
  style,
}: {
  beeld: Puzzelbeeld;
  className?: string;
  style?: React.CSSProperties;
}) {
  if (beeld.soort === "prent") {
    return (
      <div
        role="img"
        aria-label="De hele tekening"
        className={className}
        style={{
          ...style,
          backgroundImage: `url(${beeld.url})`,
          backgroundSize: "100% 100%",
        }}
      />
    );
  }
  return (
    <div
      className={`${className ?? ""} [&_svg]:block [&_svg]:h-full [&_svg]:w-full`}
      style={style}
      dangerouslySetInnerHTML={{ __html: beeld.html }}
    />
  );
}

export function Legpuzzel({ beeld }: { beeld: Puzzelbeeld }) {
  const { kolommen, rijen } = puzzelRooster(beeld.verhouding);
  const aantal = kolommen * rijen;
  // Hoe breed een stuk in de bak staat ten opzichte van zijn hoogte.
  const stukVerhouding = (beeld.verhouding * rijen) / kolommen;

  const [bak, setBak] = useState<number[] | null>(null);
  const [gelegd, setGelegd] = useState<(number | null)[]>(() =>
    Array.from({ length: aantal }, () => null),
  );
  const [gekozen, setGekozen] = useState<number | null>(null);
  const [nagekeken, setNagekeken] = useState(false);

  const af = gelegd.every((stuk, plek) => stuk === plek);
  const vol = gelegd.every((stuk) => stuk !== null);

  function begin() {
    setBak(husselen(Array.from({ length: aantal }, (_, i) => i)));
    setGelegd(Array.from({ length: aantal }, () => null));
    setGekozen(null);
    setNagekeken(false);
  }

  /** Legt het gekozen stuk op deze plek. Stond er al een stuk, dan gaat dat terug. */
  function leg(plek: number) {
    if (gekozen === null || !bak) return;
    const erop = gelegd[plek];
    const nieuw = [...gelegd];
    nieuw[plek] = gekozen;
    setGelegd(nieuw);
    setBak(
      erop === null
        ? bak.filter((s) => s !== gekozen)
        : bak.map((s) => (s === gekozen ? erop : s)),
    );
    setGekozen(null);
    setNagekeken(false);
  }

  /** Haalt een gelegd stuk weer weg. */
  function haalWeg(plek: number) {
    const stuk = gelegd[plek];
    if (stuk === null || !bak) return;
    const nieuw = [...gelegd];
    nieuw[plek] = null;
    setGelegd(nieuw);
    setBak([...bak, stuk]);
    setNagekeken(false);
  }

  return (
    <div className="rounded-2xl border border-forest/40 bg-forest/5 px-5 py-5">
      <h2 className="font-display text-xl font-semibold text-ink">
        🧩 De puzzel
      </h2>
      <p className="mt-1 text-sm text-ink-dim">
        {bak && !af
          ? "Klik een stuk onderaan aan, en klik dan het vakje waar het hoort. Fout gelegd? Klik het stuk gewoon weer weg."
          : "Een tekening uit dit hoofdstuk, in stukken. Je legt ze één voor één op hun plaats. Dit zet niets open of dicht, het is er voor de lol."}
      </p>

      <div
        className="mx-auto mt-4 grid w-full max-w-md overflow-hidden rounded-xl border border-border bg-paper"
        style={{
          aspectRatio: String(beeld.verhouding),
          gridTemplateColumns: `repeat(${kolommen}, 1fr)`,
          gridTemplateRows: `repeat(${rijen}, 1fr)`,
        }}
      >
        {af || !bak
          ? null
          : gelegd.map((stuk, plek) => {
              const juist = nagekeken && stuk !== null && stuk === plek;
              const mis = nagekeken && stuk !== null && stuk !== plek;
              return (
                <button
                  key={plek}
                  type="button"
                  onClick={() => (gekozen !== null ? leg(plek) : haalWeg(plek))}
                  aria-label={
                    stuk === null
                      ? `Leeg vakje ${plek + 1}`
                      : `Vakje ${plek + 1}, klik om het stuk weg te halen`
                  }
                  className={`relative overflow-hidden border transition ${
                    juist
                      ? "border-forest"
                      : mis
                        ? "border-amber"
                        : stuk === null
                          ? "border-dashed border-border bg-surface/60 hover:border-forest"
                          : "border-paper"
                  }`}
                >
                  {stuk !== null && (
                    <Stuk
                      beeld={beeld}
                      stuk={stuk}
                      kolommen={kolommen}
                      rijen={rijen}
                    />
                  )}
                </button>
              );
            })}
        {(af || !bak) && (
          <HeelBeeld
            beeld={beeld}
            className="h-full w-full"
            style={{ gridColumn: `span ${kolommen}`, gridRow: `span ${rijen}` }}
          />
        )}
      </div>

      {beeld.onderschrift && (
        <p className="mt-2 text-center text-xs text-ink-dim">
          {beeld.onderschrift}
        </p>
      )}

      {!bak && (
        <p className="mt-4 text-center">
          <button
            type="button"
            onClick={begin}
            className="rounded-full bg-forest px-5 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark"
          >
            Haal de stukken door elkaar
          </button>
        </p>
      )}

      {bak && !af && (
        <>
          {/* Zodra de stukken door elkaar liggen, is de tekening zelf weg. Een
              klein voorbeeld erbij, anders puzzelen ze blind. */}
          <div className="mt-4 flex items-center gap-3">
            <HeelBeeld
              beeld={beeld}
              className="w-28 shrink-0 overflow-hidden rounded-md border border-border bg-paper"
              style={{ aspectRatio: String(beeld.verhouding) }}
            />
            <p className="text-sm text-ink-dim">Zo moet het worden.</p>
          </div>

          <p className="mt-4 text-sm font-medium text-ink">
            De stukken{bak.length === 0 && " — allemaal gelegd"}
          </p>
          <div className="mt-2 flex min-h-20 flex-wrap items-center gap-2 rounded-xl border border-dashed border-border bg-surface/60 p-2">
            {bak.map((stuk) => (
              <button
                key={stuk}
                type="button"
                onClick={() => setGekozen(gekozen === stuk ? null : stuk)}
                aria-label={`Stuk ${stuk + 1}`}
                aria-pressed={gekozen === stuk}
                className={`relative h-16 overflow-hidden rounded-md border-2 transition ${
                  gekozen === stuk
                    ? "border-forest ring-2 ring-forest/40"
                    : "border-border hover:border-forest"
                }`}
                style={{ width: `${4 * stukVerhouding}rem` }}
              >
                <Stuk
                  beeld={beeld}
                  stuk={stuk}
                  kolommen={kolommen}
                  rijen={rijen}
                />
              </button>
            ))}
            {bak.length === 0 && (
              <p className="px-2 text-sm text-ink-dim">
                Alle stukken liggen. Klopt er iets niet? Klik een stuk aan om
                het terug te halen.
              </p>
            )}
          </div>

          <div className="mt-3 flex flex-wrap items-center justify-center gap-4 text-sm text-ink-dim">
            {vol && (
              <button
                type="button"
                onClick={() => setNagekeken(true)}
                className="underline underline-offset-2 hover:text-ink"
              >
                Kijk na wat juist staat
              </button>
            )}
            <button
              type="button"
              onClick={begin}
              className="underline underline-offset-2 hover:text-ink"
            >
              Opnieuw beginnen
            </button>
          </div>

          {nagekeken && (
            <p className="mt-2 text-center text-sm text-ink-dim">
              Een groene rand betekent: dat stuk staat juist. Een oranje rand
              hoort ergens anders.
            </p>
          )}
        </>
      )}

      {af && (
        <div className="mt-3 rounded-lg bg-forest/10 px-4 py-3 text-center">
          <p className="text-sm font-medium text-forest-dark">
            De tekening is weer heel. Goed gekeken.
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
