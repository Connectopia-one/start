"use client";

import { useState } from "react";

/**
 * Een rekenmachine bij het examen, zoals er een op de tafel mag liggen.
 *
 * Kim meldde op 14 oktober 2026 dat er bij de examens geen rekenmachine was:
 * "Wat ook hinderlijk is." Een kind dat voor de Examencommissie werkt, zit
 * vaak op een gsm en moet dan uit het examen stappen om te rekenen, en op dat
 * moment is het weg uit de vraag.
 *
 * Ze rekent zoals een gewone zakrekenmachine: tik een getal, een bewerking,
 * een getal, en dan is-gelijk. Geen voorrang van maal op plus, want dat is
 * net wat een zakrekenmachine ook niet doet; wie dat nodig heeft, rekent in
 * stappen. Met een komma, want in België schrijven we 3,5.
 */
const CIJFERS = ["7", "8", "9", "4", "5", "6", "1", "2", "3"];

type Bewerking = "+" | "-" | "x" | ":";

function toonbaar(getal: number): string {
  if (!Number.isFinite(getal)) return "kan niet";
  // Tien beduidende cijfers volstaan en houden 0,1 + 0,2 van 0,30000000000004
  // weg. Een heel groot of heel klein getal valt terug op de wetenschappelijke
  // notatie van de browser.
  const afgerond = Number(getal.toPrecision(10));
  const tekst =
    Math.abs(afgerond) >= 1e12 || (afgerond !== 0 && Math.abs(afgerond) < 1e-9)
      ? afgerond.toExponential(6)
      : String(afgerond);
  return tekst.replace(".", ",");
}

function getalUit(invoer: string): number {
  return Number(invoer.replace(",", "."));
}

export function Rekenmachine() {
  const [open, setOpen] = useState(false);
  const [invoer, setInvoer] = useState("0");
  const [vorige, setVorige] = useState<number | null>(null);
  const [bewerking, setBewerking] = useState<Bewerking | null>(null);
  // Begint het volgende cijfer een nieuw getal? Dat is zo na een bewerking en
  // na is-gelijk.
  const [opnieuw, setOpnieuw] = useState(true);

  const reken = (links: number, rechts: number, wat: Bewerking): number => {
    if (wat === "+") return links + rechts;
    if (wat === "-") return links - rechts;
    if (wat === "x") return links * rechts;
    return rechts === 0 ? NaN : links / rechts;
  };

  const cijfer = (c: string) => {
    if (invoer === "kan niet" || opnieuw) {
      setInvoer(c);
      setOpnieuw(false);
      return;
    }
    if (invoer.replace(/[-,]/g, "").length >= 12) return;
    setInvoer(invoer === "0" ? c : invoer + c);
  };

  const komma = () => {
    if (invoer === "kan niet" || opnieuw) {
      setInvoer("0,");
      setOpnieuw(false);
      return;
    }
    if (!invoer.includes(",")) setInvoer(invoer + ",");
  };

  const zet = (wat: Bewerking) => {
    const nu = getalUit(invoer);
    if (invoer === "kan niet") return;
    if (vorige !== null && bewerking && !opnieuw) {
      const uit = reken(vorige, nu, bewerking);
      setVorige(Number.isFinite(uit) ? uit : null);
      setInvoer(toonbaar(uit));
    } else {
      setVorige(nu);
    }
    setBewerking(wat);
    setOpnieuw(true);
  };

  const gelijk = () => {
    if (vorige === null || !bewerking || invoer === "kan niet") return;
    const uit = reken(vorige, getalUit(invoer), bewerking);
    setInvoer(toonbaar(uit));
    setVorige(null);
    setBewerking(null);
    setOpnieuw(true);
  };

  const wis = () => {
    setInvoer("0");
    setVorige(null);
    setBewerking(null);
    setOpnieuw(true);
  };

  const terug = () => {
    if (opnieuw || invoer === "kan niet") return wis();
    const korter = invoer.slice(0, -1);
    setInvoer(korter === "" || korter === "-" ? "0" : korter);
  };

  const omkeren = () => {
    if (invoer === "kan niet" || invoer === "0") return;
    setInvoer(invoer.startsWith("-") ? invoer.slice(1) : "-" + invoer);
  };

  const procent = () => {
    if (invoer === "kan niet") return;
    setInvoer(toonbaar(getalUit(invoer) / 100));
    setOpnieuw(false);
  };

  const wortel = () => {
    if (invoer === "kan niet") return;
    const nu = getalUit(invoer);
    setInvoer(nu < 0 ? "kan niet" : toonbaar(Math.sqrt(nu)));
    setOpnieuw(false);
  };

  const opToets = (e: React.KeyboardEvent) => {
    const t = e.key;
    const doe: Record<string, () => void> = {
      "+": () => zet("+"),
      "-": () => zet("-"),
      "*": () => zet("x"),
      x: () => zet("x"),
      "/": () => zet(":"),
      ":": () => zet(":"),
      "=": gelijk,
      Enter: gelijk,
      Backspace: terug,
      Escape: wis,
      ",": komma,
      ".": komma,
    };
    if (/^[0-9]$/.test(t)) {
      e.preventDefault();
      cijfer(t);
      return;
    }
    if (doe[t]) {
      e.preventDefault();
      doe[t]();
    }
  };

  const knop =
    "rounded-lg border border-border bg-paper px-0 py-3 text-base font-medium text-ink transition hover:border-forest hover:text-forest-dark active:bg-surface";
  const grijs =
    "rounded-lg border border-border bg-surface px-0 py-3 text-base text-ink-dim transition hover:border-forest hover:text-ink";

  if (!open) {
    return (
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="mt-4 rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim transition hover:border-forest hover:text-ink"
      >
        🧮 Rekenmachine
      </button>
    );
  }

  return (
    <section
      className="mt-4 max-w-xs rounded-xl border border-border bg-surface p-3"
      onKeyDown={opToets}
    >
      <div className="flex items-center justify-between gap-3">
        <h2 className="text-sm font-medium text-ink">🧮 Rekenmachine</h2>
        <button
          type="button"
          onClick={() => setOpen(false)}
          className="text-xs text-ink-dim underline underline-offset-2 hover:text-ink"
        >
          wegklappen
        </button>
      </div>
      <input
        readOnly
        value={invoer}
        aria-label="Uitkomst"
        className="mt-2 w-full rounded-lg border border-border bg-paper px-3 py-2 text-right font-display text-2xl text-ink outline-none focus:border-forest"
      />
      <div className="mt-1 h-4 text-right text-xs text-ink-dim">
        {vorige !== null && bewerking
          ? `${toonbaar(vorige)} ${bewerking === "x" ? "×" : bewerking === ":" ? "÷" : bewerking}`
          : ""}
      </div>
      <div className="mt-1 grid grid-cols-4 gap-2">
        <button type="button" onClick={wis} className={grijs}>
          C
        </button>
        <button type="button" onClick={terug} className={grijs}>
          ⌫
        </button>
        <button type="button" onClick={procent} className={grijs}>
          %
        </button>
        <button type="button" onClick={() => zet(":")} className={grijs}>
          ÷
        </button>
        {CIJFERS.slice(0, 3).map((c) => (
          <button
            key={c}
            type="button"
            onClick={() => cijfer(c)}
            className={knop}
          >
            {c}
          </button>
        ))}
        <button type="button" onClick={() => zet("x")} className={grijs}>
          ×
        </button>
        {CIJFERS.slice(3, 6).map((c) => (
          <button
            key={c}
            type="button"
            onClick={() => cijfer(c)}
            className={knop}
          >
            {c}
          </button>
        ))}
        <button type="button" onClick={() => zet("-")} className={grijs}>
          −
        </button>
        {CIJFERS.slice(6, 9).map((c) => (
          <button
            key={c}
            type="button"
            onClick={() => cijfer(c)}
            className={knop}
          >
            {c}
          </button>
        ))}
        <button type="button" onClick={() => zet("+")} className={grijs}>
          +
        </button>
        <button type="button" onClick={wortel} className={grijs}>
          √
        </button>
        <button type="button" onClick={() => cijfer("0")} className={knop}>
          0
        </button>
        <button type="button" onClick={komma} className={knop}>
          ,
        </button>
        <button
          type="button"
          onClick={gelijk}
          className="rounded-lg border border-forest bg-forest px-0 py-3 text-base font-medium text-paper transition hover:bg-forest-dark"
        >
          =
        </button>
      </div>
      <button
        type="button"
        onClick={omkeren}
        className="mt-2 w-full rounded-lg border border-border bg-surface py-2 text-sm text-ink-dim transition hover:border-forest hover:text-ink"
      >
        plus of min (±)
      </button>
      <p className="mt-2 text-xs text-ink-dim">
        Ze rekent van links naar rechts, net als een zakrekenmachine: maal gaat
        hier niet voor plus. Reken dus in stappen.
      </p>
    </section>
  );
}
