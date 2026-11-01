"use client";

import { useState } from "react";
import { lijstZin } from "@/lib/kind";

/*
  Een kind kiezen dat al in het ouderportaal staat, in plaats van alles over
  te typen. Kim op 1 november 2026: de kinderen van de plusklas komen ook naar
  kamp, en hun gegevens staan er al.

  Kiezen vult de vakken van het formulier hieronder in; Kim kan ze daarna nog
  aanpassen. Is de fiche van het kind nog niet in orde, dan zeggen we dat, maar
  kiezen mag gewoon.
*/

export type BestaandKindRij = {
  id: string;
  naam: string;
  leeftijd: string;
  ouder: string;
  gsm: string;
  mail: string;
  ontbreekt: string[];
};

const VAKKEN = ["kind", "leeftijd", "ouder", "gsm", "mail"] as const;

export function BestaandKind({ kinderen }: { kinderen: BestaandKindRij[] }) {
  const [gekozen, setGekozen] = useState<BestaandKindRij | null>(null);

  function kies(e: React.ChangeEvent<HTMLSelectElement>) {
    const kind = kinderen.find((k) => k.id === e.target.value) ?? null;
    setGekozen(kind);
    const form = e.currentTarget.form;
    if (!form) return;
    for (const vak of VAKKEN) {
      const veld = form.elements.namedItem(vak);
      if (veld instanceof HTMLInputElement) {
        veld.value = kind
          ? { kind: kind.naam, leeftijd: kind.leeftijd, ouder: kind.ouder, gsm: kind.gsm, mail: kind.mail }[vak]
          : "";
      }
    }
  }

  if (kinderen.length === 0) return null;

  return (
    <div className="rounded-md border border-forest/30 bg-forest/5 p-3">
      <label className="block text-sm">
        <span className="font-medium text-ink">
          Staat het kind al in het ouderportaal? Kies het hier
        </span>
        <select
          name="kind_id"
          defaultValue=""
          onChange={kies}
          className="mt-1 w-full rounded-md border border-border bg-white px-3 py-1.5 text-ink"
        >
          <option value="">Nee, ik typ het zelf</option>
          {kinderen.map((k) => (
            <option key={k.id} value={k.id}>
              {k.naam}
              {k.ouder ? ` (gezin ${k.ouder})` : ""}
              {k.ontbreekt.length ? " · fiche nog niet in orde" : ""}
            </option>
          ))}
        </select>
      </label>
      <p className="mt-1.5 text-xs text-ink-dim">
        De naam, de leeftijd en de gegevens van de ouder vullen zich dan
        vanzelf in. De fiche zelf staat al bij het kind.
      </p>
      {gekozen && gekozen.ontbreekt.length > 0 && (
        <p className="mt-2 rounded-md bg-amber/15 px-3 py-2 text-xs text-ink">
          De fiche van {gekozen.naam} is nog niet in orde: nog nodig is{" "}
          {lijstZin(gekozen.ontbreekt)}. Je kan het kind gewoon op de lijst
          zetten; vraag de ouder om de fiche aan te vullen op
          ouders.connectopia.one.
        </p>
      )}
    </div>
  );
}
