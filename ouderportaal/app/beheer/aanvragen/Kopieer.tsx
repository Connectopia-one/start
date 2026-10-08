"use client";

import { useState } from "react";

/*
  Een knopje dat één tekst naar het klembord zet.

  Kim vroeg dit voor het mailadres van een aanvraag: ze wil het kunnen plakken
  in haar mailprogramma zonder het over te typen of met de muis te selecteren.
  Het knopje toont de waarde zelf, zodat het ook dient om ze te lezen.

  navigator.clipboard werkt enkel op https en enkel na een klik, en sommige
  browsers weigeren het zonder iets te zeggen. Daarom staat er een tweede weg
  achter: een tijdelijk tekstvak dat we selecteren en laten kopiëren. Lukt ook
  dat niet, dan zeggen we dat eerlijk in plaats van "gekopieerd" te tonen.
*/
export function Kopieer({
  waarde,
  wat,
  label,
  stijl = "zacht",
}: {
  waarde: string;
  wat: string;
  label?: string;
  stijl?: "zacht" | "vol";
}) {
  const [stand, setStand] = useState<"klaar" | "gelukt" | "mislukt">("klaar");

  async function kopieer() {
    let gelukt = false;
    try {
      await navigator.clipboard.writeText(waarde);
      gelukt = true;
    } catch {
      try {
        const vak = document.createElement("textarea");
        vak.value = waarde;
        vak.setAttribute("readonly", "");
        vak.style.position = "fixed";
        vak.style.top = "0";
        vak.style.opacity = "0";
        document.body.appendChild(vak);
        vak.select();
        gelukt = document.execCommand("copy");
        document.body.removeChild(vak);
      } catch {
        gelukt = false;
      }
    }
    setStand(gelukt ? "gelukt" : "mislukt");
    window.setTimeout(() => setStand("klaar"), 2500);
  }

  const basis =
    stijl === "vol"
      ? "border-forest bg-forest text-white hover:bg-forest-dark"
      : "border-border bg-surface text-ink hover:border-forest";

  return (
    <button
      type="button"
      onClick={kopieer}
      aria-label={`Kopieer ${wat}`}
      title={`Kopieer ${wat}`}
      className={`inline-flex items-center gap-1.5 rounded-md border px-2.5 py-1.5 text-sm transition ${basis}`}
    >
      <svg
        aria-hidden="true"
        viewBox="0 0 20 20"
        className="h-3.5 w-3.5 shrink-0"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <rect x="7" y="7" width="9" height="10" rx="1.5" />
        <path d="M13 4.5H5.5A1.5 1.5 0 0 0 4 6v7.5" />
      </svg>
      <span className="max-w-[18rem] truncate">
        {stand === "gelukt"
          ? "Gekopieerd"
          : stand === "mislukt"
            ? "Selecteer het zelf"
            : (label ?? waarde)}
      </span>
    </button>
  );
}
