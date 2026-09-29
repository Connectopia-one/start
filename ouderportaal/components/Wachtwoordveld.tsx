"use client";

import { useId, useState } from "react";

/*
  Een wachtwoordveld met een oogje om mee te kijken wat je typt.

  Gevraagd op 29 september 2026: ouders die hun wachtwoord ingaven, konden
  niet nakijken wat er stond. Op een telefoon is dat de gewoonste oorzaak van
  een mislukte aanmelding.

  Het oogje staat standaard dicht, en gaat nooit vanzelf open. Zolang het
  wachtwoord zichtbaar is, zegt de knop dat ook, voor wie het scherm niet ziet.
*/

export function Wachtwoordveld({
  naam,
  label,
  autoComplete,
  minLength,
  hulp,
  id,
}: {
  naam: string;
  label: string;
  autoComplete: "current-password" | "new-password";
  minLength?: number;
  hulp?: string;
  id?: string;
}) {
  const eigenId = useId();
  const veldId = id ?? eigenId;
  const [zichtbaar, setZichtbaar] = useState(false);

  return (
    <div className="space-y-1.5">
      <label htmlFor={veldId} className="text-sm font-medium text-ink">
        {label}
      </label>
      <div className="relative">
        <input
          id={veldId}
          name={naam}
          type={zichtbaar ? "text" : "password"}
          required
          minLength={minLength}
          autoComplete={autoComplete}
          className="w-full rounded-md border border-border bg-paper py-2 pl-3 pr-12 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
        <button
          type="button"
          onClick={() => setZichtbaar((aan) => !aan)}
          aria-pressed={zichtbaar}
          aria-label={zichtbaar ? "Wachtwoord verbergen" : "Wachtwoord tonen"}
          title={zichtbaar ? "Wachtwoord verbergen" : "Wachtwoord tonen"}
          className="absolute inset-y-0 right-0 flex w-12 items-center justify-center rounded-r-md text-ink-dim transition hover:text-forest-dark focus:outline-none focus-visible:ring-1 focus-visible:ring-forest"
        >
          {zichtbaar ? <OogDicht /> : <OogOpen />}
        </button>
      </div>
      {hulp && <p className="text-xs text-ink-dim">{hulp}</p>}
    </div>
  );
}

function OogOpen() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 24 24"
      className="h-5 w-5"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  );
}

function OogDicht() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 24 24"
      className="h-5 w-5"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M2.5 12S6 5.5 12 5.5c1.5 0 2.8.4 4 1" />
      <path d="M21.5 12s-1.4 2.6-4 4.4" />
      <path d="M9.9 9.9a3 3 0 0 0 4.2 4.2" />
      <path d="M14.5 17.9c-.8.2-1.6.3-2.5.3-6 0-9.5-6.2-9.5-6.2" />
      <path d="M4 20 20 4" />
    </svg>
  );
}
