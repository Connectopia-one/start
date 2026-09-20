import type { Metadata } from "next";
import Link from "next/link";
import { PaginaKop, Penseel, Sectie } from "@/components/ui";

export const metadata: Metadata = {
  title: "Oefenplatform",
  description:
    "Interactieve oefeningen per categorie, met voortgang per kind.",
};

/*
  Zodra het oefenplatform online staat, zet je het adres in content/site.ts
  bij het onderdeel "/oefenplatform" (het veld "extern").
  Dan linken het menu en de startpagina er rechtstreeks naartoe
  en heb je deze pagina niet meer nodig.
*/
export default function OefenplatformPagina() {
  return (
    <>
      <PaginaKop
        label="Oefenplatform"
        titel="Oefenen op jouw tempo"
        tekst="Interactieve oefeningen per categorie, met voortgang per kind."
      />
      <Sectie className="pb-16">
        <Penseel>Bijna klaar om open te zetten</Penseel>
        <p className="mt-5 max-w-[60ch] text-ink-dim">
          Het oefenplatform is gebouwd en wordt binnenkort gekoppeld. Ben je al ingeschreven en
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
