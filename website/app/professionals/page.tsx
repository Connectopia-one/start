import type { Metadata } from "next";
import Link from "next/link";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { professionals, professionalsVelden } from "@/content/professionals";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: professionals.titel,
  description: professionals.tekst,
};

/* De kleur van het rondje bij elk punt, zoals overal op de site. */
const puntKleur = {
  green: "bg-sage-soft",
  purple: "bg-purple-soft",
  orange: "bg-orange-soft",
} as const;

export default function ProfessionalsPagina() {
  return (
    <>
      <PaginaKop
        label={professionals.label}
        titel={professionals.titel}
        handgeschreven={professionals.handgeschreven}
        tekst={professionals.tekst}
      />

      {/* Meteen duidelijk maken wat we niet zijn. */}
      <Sectie className="py-6">
        <div className="rounded-[20px] bg-sage-soft px-6 py-5">
          <h2 className="text-xl text-green">{professionals.nuance.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
            {professionals.nuance.tekst}
          </p>
        </div>
      </Sectie>

      {/* Wat een professional eraan heeft. */}
      <Sectie className="py-4">
        <h2 className="text-2xl text-green">{professionals.puntenTitel}</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          {professionals.punten.map((punt) => (
            <Kaart key={punt.titel} className="flex flex-col">
              <span
                aria-hidden
                className={`flex h-12 w-12 items-center justify-center rounded-full text-2xl ${puntKleur[punt.kleur]}`}
              >
                {punt.icoon}
              </span>
              <h3 className="mt-3 text-xl text-green">{punt.titel}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{punt.tekst}</p>
              <Link
                href={punt.link.href}
                className="mt-auto pt-3 text-[15px] font-extrabold text-green underline-offset-4 hover:underline"
              >
                {punt.link.tekst} →
              </Link>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* Dit geldt voor elk van onze werkingen, niet voor een ervan. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] border border-border bg-surface px-6 py-5">
          <h2 className="text-xl text-green">{professionals.altijd.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
            {professionals.altijd.tekst}
          </p>
          <ul className="mt-3 flex flex-wrap gap-2">
            {professionals.altijd.woorden.map((woord) => (
              <li
                key={woord}
                className="rounded-full bg-sage-soft px-4 py-1.5 text-[15px] font-extrabold text-green"
              >
                {woord}
              </li>
            ))}
          </ul>
        </div>
      </Sectie>

      {/* Wat we bezorgen. */}
      <Sectie className="py-6">
        <div className="rounded-[20px] bg-orange-soft px-6 py-5">
          <h2 className="text-2xl text-orange">
            {professionals.bezorgenTitel}
          </h2>
          <ul className="mt-3 grid gap-3 sm:grid-cols-3">
            {professionals.bezorgen.map((ding) => (
              <li key={ding.titel}>
                <p className="text-[16px] font-extrabold text-green">
                  {ding.titel}
                </p>
                <p className="text-[15px] text-ink-dim">{ding.tekst}</p>
              </li>
            ))}
          </ul>
          <p className="mt-4 text-[16px] font-bold text-green">
            {professionals.bezorgenSlot}
          </p>
        </div>
      </Sectie>

      {/* Het formulier. */}
      <Sectie className="grid gap-4 pb-16">
        <Kaart className="scroll-mt-24" id="aanvraag">
          <h2 className="text-2xl text-green">
            {professionals.formulierTitel}
          </h2>
          <p className="mt-2 max-w-[62ch] text-[16px] text-ink-dim">
            {professionals.formulierTekst}
          </p>
          <div className="mt-6">
            <Aanvraagformulier
              onderwerp={professionals.onderwerp}
              vragen={professionalsVelden}
              privacy={professionals.privacy}
              verborgen={[{ naam: "Soort aanvraag", waarde: "Professional" }]}
            />
          </div>
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">
            Liever gewoon bellen of mailen?
          </h2>
          <p className="mt-2 text-[16px] text-ink-dim">
            Mail ons op{" "}
            <a
              href={`mailto:${site.email}`}
              className="font-bold text-green underline-offset-4 hover:underline"
            >
              {site.email}
            </a>{" "}
            of bel{" "}
            <a
              href={site.telefoonLink}
              className="font-bold text-green underline-offset-4 hover:underline"
            >
              {site.telefoon}
            </a>
            .
          </p>
        </Kaart>
      </Sectie>
    </>
  );
}
