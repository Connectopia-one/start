"use client";

import { useState, type ReactNode } from "react";

export function HoofdstukTabs({
  oefeningen,
  leerstof,
  aantalLeerstof,
  rekenmachine,
}: {
  oefeningen: ReactNode;
  leerstof: ReactNode;
  aantalLeerstof: number;
  rekenmachine: ReactNode | null;
}) {
  /* Een ouder meldde op 9 oktober 2026: "ik merk toch dat zoontje de neiging
     heeft om gewoon direct aan de online oefeningen te beginnen, en moet dan
     telkens herhalen dat hij eerst de leerstof moet doorlezen." De oefeningen
     stonden vooraan en gingen vanzelf open. Daarom staat Leerstof nu eerst en
     opent een hoofdstuk daar. Is er nog geen leerstof, dan zou dat op een leeg
     tabblad uitkomen, en beginnen we gewoon bij de oefeningen. */
  const [tab, setTab] = useState<"oefeningen" | "leerstof" | "rekenmachine">(
    aantalLeerstof > 0 ? "leerstof" : "oefeningen",
  );

  return (
    <div className="mt-6">
      <div className="flex gap-2 border-b border-border">
        <button
          type="button"
          onClick={() => setTab("leerstof")}
          className={`px-3 py-2 text-sm font-medium ${
            tab === "leerstof" ? "border-b-2 border-forest text-forest-dark" : "text-ink-dim hover:text-ink"
          }`}
        >
          Leerstof {aantalLeerstof > 0 && `(${aantalLeerstof})`}
        </button>
        <button
          type="button"
          onClick={() => setTab("oefeningen")}
          className={`px-3 py-2 text-sm font-medium ${
            tab === "oefeningen" ? "border-b-2 border-forest text-forest-dark" : "text-ink-dim hover:text-ink"
          }`}
        >
          Oefeningen
        </button>
        {rekenmachine && (
          <button
            type="button"
            onClick={() => setTab("rekenmachine")}
            className={`px-3 py-2 text-sm font-medium ${
              tab === "rekenmachine" ? "border-b-2 border-forest text-forest-dark" : "text-ink-dim hover:text-ink"
            }`}
          >
            Rekenmachine
          </button>
        )}
      </div>

      <div className={tab === "leerstof" ? "" : "hidden"}>{leerstof}</div>
      <div className={tab === "oefeningen" ? "" : "hidden"}>{oefeningen}</div>
      {rekenmachine && <div className={tab === "rekenmachine" ? "" : "hidden"}>{rekenmachine}</div>}
    </div>
  );
}
