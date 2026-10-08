"use client";

import { useMemo, useState } from "react";
import { zetGroep, zetVolledigeToegang } from "./actions";

export type GezinRij = {
  id: string;
  naam: string;
  email: string;
  rol: string;
  isPlusklas: boolean;
  betaald: boolean;
  toegangSchooljaar: string | null;
  code: string | null;
  sinds: string;
  kinderen: string[];
};

export type CodeRij = { code: string; label: string | null; actief: boolean };

/** De vier knopjes waarmee je de lijst korter maakt. */
const SOORTEN = [
  { sleutel: "alles", naam: "Allemaal" },
  { sleutel: "open", naam: "Enkel de gratis hoofdstukken" },
  { sleutel: "gratis", naam: "Gratis toegang van jou" },
  { sleutel: "betaald", naam: "Betaald" },
] as const;

type Soort = (typeof SOORTEN)[number]["sleutel"];

function hoortBij(rij: GezinRij, soort: Soort) {
  if (soort === "gratis") return rij.isPlusklas;
  if (soort === "betaald") return rij.betaald;
  if (soort === "open") return !rij.isPlusklas && !rij.betaald;
  return true;
}

/**
 * Het mailadres zonder het cijfertje of het +labeltje erachter.
 *
 * Eén iemand maakt soms meerdere accounts aan met hetzelfde postvak:
 * thiangoedgezelschap2@gmail.com en thiangoedgezelschap3@gmail.com komen in
 * dezelfde mailbox terecht. Door het cijfer achteraan en een +labeltje weg te
 * laten, en bij gmail ook de puntjes (die negeert gmail zelf), vallen die
 * adressen samen en kan je ze samen tonen.
 *
 * Het blijft een vermoeden, geen bewijs: kim1@ en kim2@ kunnen ook twee
 * verschillende mensen zijn. Daarom staat het op het scherm als "lijkt op" en
 * zet het niets vast in de databank.
 */
function mailKern(email: string) {
  const [lokaal = "", domein = ""] = email.toLowerCase().split("@");
  let kern = lokaal.split("+")[0] ?? "";
  if (domein === "gmail.com" || domein === "googlemail.com") {
    kern = kern.replace(/\./g, "");
  }
  kern = kern.replace(/[._-]*\d+$/, "");
  /* Blijft er te weinig over (bv. "kim7" wordt "kim"), dan houden we het
     volledige adres, anders gooi je zomaar mensen bij elkaar. */
  if (kern.length < 4) kern = lokaal;
  return { kern, basis: `${kern}@${domein}`, domein };
}

export function Gezinslijst({
  rijen,
  codes,
  start,
}: {
  rijen: GezinRij[];
  codes: CodeRij[];
  /** Op welke soort de lijst meteen staat, uit ?toon= in het webadres. */
  start?: string;
}) {
  const [zoek, setZoek] = useState("");
  const [soort, setSoort] = useState<Soort>(
    SOORTEN.some((s) => s.sleutel === start) ? (start as Soort) : "alles",
  );

  /* Per gezin de kern van zijn mailadres, en hoeveel accounts diezelfde kern
     hebben. Eén keer berekenen voor de hele lijst. */
  const metKern = useMemo(
    () => rijen.map((r) => ({ rij: r, ...mailKern(r.email) })),
    [rijen],
  );

  const aantalPerBasis = useMemo(() => {
    const telling = new Map<string, number>();
    for (const r of metKern) {
      if (!r.rij.email) continue;
      telling.set(r.basis, (telling.get(r.basis) ?? 0) + 1);
    }
    return telling;
  }, [metKern]);

  /* De adressen die meer dan één account hebben, met het meeste bovenaan. Dit
     is het lijstje waarmee je ziet hoeveel codes er per postvak gebruikt zijn. */
  const meervoudig = useMemo(
    () =>
      [...aantalPerBasis.entries()]
        .filter(([, aantal]) => aantal > 1)
        .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
        .map(([basis, aantal]) => ({ basis, aantal })),
    [aantalPerBasis],
  );

  /* Hoeveel accounts er in elke soort zitten, voor op de knopjes. */
  const aantalPerSoort = useMemo(() => {
    const telling = {} as Record<Soort, number>;
    for (const { sleutel } of SOORTEN) {
      telling[sleutel] = rijen.filter((r) => hoortBij(r, sleutel)).length;
    }
    return telling;
  }, [rijen]);

  const vraag = zoek.trim().toLowerCase();
  const gevonden = useMemo(() => {
    const binnenSoort = metKern.filter(({ rij }) => hoortBij(rij, soort));
    if (!vraag) return binnenSoort;
    return binnenSoort.filter(({ rij, kern, basis }) => {
      const hooi = [
        rij.naam,
        rij.email,
        rij.code ?? "",
        kern,
        basis,
        rij.kinderen.join(" "),
      ]
        .join(" ")
        .toLowerCase();
      return hooi.includes(vraag);
    });
  }, [metKern, vraag, soort]);

  const codeLabel = (code: string) =>
    codes.find((c) => c.code === code)?.label ?? null;

  return (
    <>
      {meervoudig.length > 0 && (
        <section className="mt-6 rounded-lg border border-border bg-surface px-4 py-4">
          <h2 className="font-display text-base font-semibold text-ink">
            Mailadressen met meer dan één account
          </h2>
          <p className="mt-1 text-sm text-ink-dim">
            Deze adressen lijken op elkaar: een cijfertje of een plusje
            achteraan komt in hetzelfde postvak terecht. Klik erop om net die
            accounts te zien. Het blijft een vermoeden, want twee mensen kunnen
            ook een gelijkend adres hebben.
          </p>
          <div className="mt-3 flex flex-wrap gap-2">
            {meervoudig.map(({ basis, aantal }) => (
              <button
                key={basis}
                type="button"
                onClick={() => setZoek(basis.split("@")[0] ?? basis)}
                className="rounded-full border border-border px-3 py-1 text-xs font-medium text-ink hover:border-forest hover:text-forest-dark"
              >
                <span className="font-mono">{basis}</span>
                {" · "}
                {aantal} accounts
              </button>
            ))}
          </div>
        </section>
      )}

      <div className="mt-6">
        <label
          htmlFor="zoek-gezin"
          className="block text-sm font-medium text-ink"
        >
          Zoeken
        </label>
        <div className="mt-1 flex flex-wrap items-center gap-2">
          <input
            id="zoek-gezin"
            type="search"
            value={zoek}
            onChange={(e) => setZoek(e.target.value)}
            placeholder="een mailadres, een naam, een kind of een code"
            autoComplete="off"
            className="min-w-0 flex-1 rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
          {zoek && (
            <button
              type="button"
              onClick={() => setZoek("")}
              className="rounded-md border border-border px-3 py-2 text-sm font-medium text-ink hover:border-forest hover:text-forest-dark"
            >
              Alles tonen
            </button>
          )}
        </div>
        <p className="mt-1 text-xs text-ink-dim">
          Je mag een stukje van een adres typen. Zoek je op
          thiangoedgezelschap, dan komen alle accounts van dat postvak samen op
          het scherm.
        </p>
      </div>

      {/* Vier knopjes om de lijst korter te maken. Het zoekvakje werkt
          binnen de knop die aan staat. */}
      <div className="mt-4 flex flex-wrap gap-2">
        {SOORTEN.map(({ sleutel, naam }) => (
          <button
            key={sleutel}
            type="button"
            onClick={() => setSoort(sleutel)}
            aria-pressed={soort === sleutel}
            className={`rounded-full border px-3 py-1 text-xs font-medium ${
              soort === sleutel
                ? "border-forest bg-forest/10 text-forest-dark"
                : "border-border text-ink-dim hover:border-forest hover:text-forest-dark"
            }`}
          >
            {naam} ({aantalPerSoort[sleutel]})
          </button>
        ))}
      </div>

      <p className="mt-3 text-sm text-ink-dim">
        {vraag ? (
          <>
            {gevonden.length} van {aantalPerSoort[soort]}{" "}
            {aantalPerSoort[soort] === 1 ? "account" : "accounts"} gevonden.
          </>
        ) : soort === "alles" ? (
          <>
            {rijen.length} {rijen.length === 1 ? "account" : "accounts"},
            waarvan{" "}
            <span className="font-medium text-ink">
              {rijen.filter((r) => r.isPlusklas || r.betaald).length}
            </span>{" "}
            met volledige toegang.
          </>
        ) : (
          <>
            <span className="font-medium text-ink">{aantalPerSoort[soort]}</span>{" "}
            van de {rijen.length} accounts.
          </>
        )}
      </p>

      <ul className="mt-3 space-y-2">
        {gevonden.map(({ rij, basis }) => {
          const samen = aantalPerBasis.get(basis) ?? 1;
          const label = rij.code ? codeLabel(rij.code) : null;
          return (
            <li
              key={rij.id}
              className="rounded-lg border border-border bg-surface px-4 py-3"
            >
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <p className="text-sm font-medium text-ink">{rij.naam}</p>
                  <p className="mt-0.5 text-xs text-ink-dim">
                    {rij.kinderen.length === 0
                      ? "nog geen kind toegevoegd"
                      : `${rij.kinderen.length} ${
                          rij.kinderen.length === 1 ? "kind" : "kinderen"
                        }: ${rij.kinderen.join(", ")}`}
                    {" · sinds "}
                    {rij.sinds}
                    {rij.rol === "begeleider" && " · begeleider"}
                  </p>
                  {rij.email && (
                    <p className="mt-0.5 break-all font-mono text-xs text-ink-dim">
                      {rij.email}
                    </p>
                  )}
                  {samen > 1 && (
                    <button
                      type="button"
                      onClick={() => setZoek(basis.split("@")[0] ?? basis)}
                      className="mt-1 text-xs font-medium text-forest-dark underline hover:no-underline"
                    >
                      {samen} accounts met dit mailadres
                    </button>
                  )}
                </div>
                <div className="flex flex-col items-end gap-2">
                  <span
                    className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      rij.isPlusklas
                        ? "bg-forest/10 text-forest-dark"
                        : rij.betaald
                          ? "bg-amber/15 text-amber"
                          : "bg-ink-dim/10 text-ink-dim"
                    }`}
                  >
                    {rij.isPlusklas
                      ? "Gratis toegang van jou"
                      : rij.betaald
                        ? `Betaald ${rij.toegangSchooljaar}`
                        : "Enkel de gratis hoofdstukken"}
                  </span>
                  <form action={zetVolledigeToegang}>
                    <input type="hidden" name="id" value={rij.id} />
                    <input
                      type="hidden"
                      name="aan"
                      value={rij.isPlusklas ? "nee" : "ja"}
                    />
                    <button
                      type="submit"
                      className="rounded-full border border-border px-3 py-1 text-xs font-medium text-ink hover:border-forest hover:text-forest-dark"
                    >
                      {rij.isPlusklas
                        ? "Toegang uitzetten"
                        : "Toegang aanzetten"}
                    </button>
                  </form>
                </div>
              </div>

              <form
                action={zetGroep}
                className="mt-3 flex flex-wrap items-center gap-2 border-t border-border pt-3"
              >
                <input type="hidden" name="id" value={rij.id} />
                <label
                  htmlFor={`groep-${rij.id}`}
                  className="text-xs text-ink-dim"
                >
                  Via code
                </label>
                <select
                  id={`groep-${rij.id}`}
                  name="code"
                  defaultValue={rij.code ?? ""}
                  className="rounded-md border border-border bg-paper px-2 py-1 text-xs text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                >
                  <option value="">nog geen code</option>
                  {codes.map((c) => (
                    <option key={c.code} value={c.code}>
                      {c.code}
                      {c.label ? ` — ${c.label}` : ""}
                      {c.actief ? "" : " (uit)"}
                    </option>
                  ))}
                </select>
                <button
                  type="submit"
                  className="rounded-md border border-border px-2 py-1 text-xs font-medium text-ink hover:border-forest hover:text-forest-dark"
                >
                  Bewaren
                </button>
                {rij.code && (
                  <span className="text-xs text-ink-dim">
                    staat nu bij {rij.code}
                    {label ? ` — ${label}` : ""}
                  </span>
                )}
              </form>
            </li>
          );
        })}
        {!gevonden.length && (
          <li className="text-sm text-ink-dim">
            {rijen.length
              ? "Geen account gevonden met dat stukje tekst."
              : "Er heeft zich nog niemand geregistreerd."}
          </li>
        )}
      </ul>
    </>
  );
}
