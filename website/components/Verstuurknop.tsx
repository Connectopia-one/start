"use client";

import { useFormStatus } from "react-dom";
import { formulierTekst } from "@/content/formulier";

/*
  De verstuurknop van het aanvraagformulier.

  Waarom dit een apart stukje is: op een trage verbinding gebeurt er na het
  klikken even niets zichtbaars, en dan klikt iemand nog eens. Elke klik is een
  aparte verzending, dus dan stond dezelfde ouder twee keer in de lijst — dat
  viel op bij de winactie van 25 september 2026. Zolang het versturen bezig is,
  staat de knop nu uit en zegt hij dat.

  Zonder javascript valt useFormStatus terug op "niet bezig" en werkt de knop
  gewoon als een gewone verstuurknop; het formulier zelf is een gewoon
  formulier naar de server, dus dat blijft werken.
*/
export function Verstuurknop() {
  const { pending } = useFormStatus();
  return (
    <button
      type="submit"
      disabled={pending}
      className="rounded-full bg-green px-7 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:translate-y-0"
    >
      {pending ? "Bezig met versturen…" : `${formulierTekst.verstuurKnop} →`}
    </button>
  );
}
