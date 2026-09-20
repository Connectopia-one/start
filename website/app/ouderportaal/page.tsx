import type { Metadata } from "next";
import Link from "next/link";
import { PaginaKop, Penseel, Sectie } from "@/components/ui";

export const metadata: Metadata = {
  title: "Ouderportaal",
  description:
    "Je gezin, de kalender, het materiaal en de foto's van de klasjes waar je kind bij zit.",
};

/*
  Zodra het ouderportaal online staat, zet je het adres in content/site.ts
  bij het onderdeel "/ouderportaal" (het veld "extern").
  Dan linken het menu en de startpagina er rechtstreeks naartoe
  en heb je deze pagina niet meer nodig.
*/
export default function OuderportaalPagina() {
  return (
    <>
      <PaginaKop
        label="Ouderportaal"
        titel="Je eigen plek bij Connectopia"
        tekst="Je gezin, de kalender, het materiaal en de foto's van de klasjes waar je kind bij zit."
      />
      <Sectie className="pb-16">
        <Penseel>Bijna klaar om open te zetten</Penseel>
        <p className="mt-5 max-w-[60ch] text-ink-dim">
          Het ouderportaal is gebouwd en wordt binnenkort gekoppeld. Ben je al ingeschreven en
          heb je iets nodig? Laat het ons gerust weten.
        </p>
        <Link
          href="/over-ons#contact"
          className="mt-6 inline-block rounded-full bg-green px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5"
        >
          Neem contact op →
        </Link>
      </Sectie>
    </>
  );
}
