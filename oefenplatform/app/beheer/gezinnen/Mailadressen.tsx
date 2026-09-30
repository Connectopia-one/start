"use client";

import { useMemo, useRef, useState } from "react";

export type MailRij = {
  naam: string;
  email: string;
  toegang: boolean;
};

/**
 * Het lijstje mailadressen van de ouders die een login aangemaakt hebben,
 * met een knop om het in één keer te kopiëren.
 *
 * Twee knoppen, want een mailprogramma wil de adressen achter elkaar met een
 * puntkomma ertussen, terwijl je voor een persoonlijke mail per gezin liever
 * één adres per regel hebt om er telkens één uit te pikken.
 */
export function Mailadressen({ rijen }: { rijen: MailRij[] }) {
  const [enkelToegang, setEnkelToegang] = useState(false);
  const [gekopieerd, setGekopieerd] = useState<string | null>(null);
  const vak = useRef<HTMLTextAreaElement>(null);

  const adressen = useMemo(
    () =>
      rijen
        .filter((r) => (enkelToegang ? r.toegang : true))
        .map((r) => r.email),
    [rijen, enkelToegang],
  );

  async function kopieer(tekst: string, welke: string) {
    try {
      await navigator.clipboard.writeText(tekst);
      setGekopieerd(welke);
      setTimeout(() => setGekopieerd(null), 2500);
    } catch {
      /* Lukt het kopiëren niet, selecteer dan het vak zodat ze het zelf kan doen. */
      vak.current?.focus();
      vak.current?.select();
      setGekopieerd("selectie");
      setTimeout(() => setGekopieerd(null), 4000);
    }
  }

  return (
    <section className="mt-6 rounded-lg border border-border bg-surface px-4 py-4">
      <h2 className="font-display text-base font-semibold text-ink">
        Mailadressen
      </h2>
      <p className="mt-1 text-sm text-ink-dim">
        De mailadressen waarmee deze ouders hun login aangemaakt hebben. De
        lijst vult zichzelf aan zodra er iemand bij komt.
      </p>

      <label className="mt-3 flex items-center gap-2 text-sm text-ink">
        <input
          type="checkbox"
          checked={enkelToegang}
          onChange={(e) => setEnkelToegang(e.target.checked)}
          className="h-4 w-4 rounded border-border text-forest focus:ring-forest"
        />
        Enkel de gezinnen met volledige toegang
      </label>

      <textarea
        ref={vak}
        readOnly
        rows={Math.min(Math.max(adressen.length, 2), 10)}
        value={adressen.join("\n")}
        className="mt-3 w-full rounded-md border border-border bg-paper px-3 py-2 font-mono text-xs text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        aria-label="Mailadressen, één per regel"
      />

      <div className="mt-3 flex flex-wrap items-center gap-2">
        <button
          type="button"
          onClick={() => kopieer(adressen.join("; "), "achter-elkaar")}
          disabled={!adressen.length}
          className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-40"
        >
          Kopieer achter elkaar
        </button>
        <button
          type="button"
          onClick={() => kopieer(adressen.join("\n"), "per-regel")}
          disabled={!adressen.length}
          className="rounded-md border border-border px-3 py-2 text-sm font-medium text-ink hover:border-forest hover:text-forest-dark disabled:opacity-40"
        >
          Kopieer één per regel
        </button>
        <span className="text-xs text-ink-dim">
          {adressen.length} {adressen.length === 1 ? "adres" : "adressen"}
        </span>
        {gekopieerd === "achter-elkaar" && (
          <span className="text-xs text-forest-dark">
            Gekopieerd, met een puntkomma ertussen.
          </span>
        )}
        {gekopieerd === "per-regel" && (
          <span className="text-xs text-forest-dark">
            Gekopieerd, één per regel.
          </span>
        )}
        {gekopieerd === "selectie" && (
          <span className="text-xs text-ink-dim">
            Kopiëren lukt niet in deze browser. De lijst staat geselecteerd,
            gebruik ctrl+C.
          </span>
        )}
      </div>
    </section>
  );
}
