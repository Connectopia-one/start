import type { Metadata } from "next";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Icoon, Kaart, PaginaKop, Sectie } from "@/components/ui";
import { contactTekst, terugbelVragen } from "@/content/contact";
import { vragenMetExtra } from "@/content/formulier";
import { site, volgOns } from "@/content/site";

export const metadata: Metadata = {
  title: "Contact",
  description: contactTekst.tekst,
};

export default async function ContactPagina() {
  return (
    <>
      <PaginaKop
        label={contactTekst.label}
        titel={contactTekst.titel}
        handgeschreven={contactTekst.handgeschreven}
        tekst={contactTekst.tekst}
      />

      {/* De twee keuzes: nu bellen, of teruggebeld worden. */}
      <Sectie className="grid gap-4 py-8 md:grid-cols-2">
        <Kaart className="flex flex-col">
          <Icoon kleur="green">📞</Icoon>
          <h2 className="mt-3 text-2xl text-green">
            {contactTekst.bellen.titel}
          </h2>
          <p className="mt-2 text-[16px] text-ink-dim">
            {contactTekst.bellen.tekst}
          </p>
          <a
            href={site.telefoonLink}
            className="mt-auto inline-block rounded-full bg-green px-6 py-3.5 pt-3.5 text-center text-[18px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
          >
            {contactTekst.bellen.knopTekst} {site.telefoon}
          </a>
        </Kaart>

        <Kaart className="flex flex-col">
          <Icoon kleur="orange">✍️</Icoon>
          <h2 className="mt-3 text-2xl text-orange">
            {contactTekst.terugbellen.titel}
          </h2>
          <p className="mt-2 text-[16px] text-ink-dim">
            {contactTekst.terugbellen.tekst}
          </p>
          <a
            href="#terugbellen"
            className="mt-auto inline-block rounded-full border-2 border-green px-6 py-3 text-center text-[16px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft"
          >
            {contactTekst.terugbellen.knopTekst} ↓
          </a>
        </Kaart>
      </Sectie>

      {/* Het terugbelformulier. */}
      <Sectie className="py-0">
        <Kaart className="scroll-mt-24" id="terugbellen">
          <h2 className="text-2xl text-green">
            {contactTekst.terugbellen.formulierTitel}
          </h2>
          <p className="mt-2 max-w-[62ch] text-[16px] text-ink-dim">
            {contactTekst.terugbellen.formulierTekst}
          </p>
          <div className="mt-6">
            <Aanvraagformulier
              onderwerp={contactTekst.terugbellen.onderwerp}
              /* Plus de vraag wanneer het best past om te bellen. */
              vragen={vragenMetExtra(terugbelVragen)}
              verborgen={[
                { naam: "Soort aanvraag", waarde: "Terugbelverzoek" },
              ]}
              /* Gaat je vraag niet over een kind? Dan hoef je dat niet in te vullen. */
              optioneel={[
                "Naam van het kind",
                "Leeftijd van het kind",
                "Gemeente",
              ]}
            />
          </div>
        </Kaart>
      </Sectie>

      <Sectie className="grid gap-4 pb-16 md:grid-cols-2">
        <Kaart>
          <h2 className="text-xl text-green">{contactTekst.mailen.titel}</h2>
          <p className="mt-2 text-[16px] text-ink-dim">
            {contactTekst.mailen.tekst} Mail ons op{" "}
            <a
              href={`mailto:${site.email}`}
              className="font-bold text-green underline-offset-4 hover:underline"
            >
              {site.email}
            </a>
            .
          </p>
        </Kaart>

        {/* Een knop per kanaal uit volgOns in content/site.ts. */}
        {volgOns.length > 0 ? (
          <Kaart className="flex flex-col">
            <h2 className="text-xl text-green">{contactTekst.volgen.titel}</h2>
            <p className="mt-2 text-[16px] text-ink-dim">
              {contactTekst.volgen.tekst}
            </p>
            <div className="mt-4 flex flex-wrap gap-3">
              {volgOns.map((kanaal) => (
                <a
                  key={kanaal.naam}
                  href={kanaal.adres}
                  className="inline-block rounded-full border-2 border-green px-6 py-3 text-center text-[16px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft"
                >
                  {kanaal.naam}
                </a>
              ))}
            </div>
          </Kaart>
        ) : null}
      </Sectie>
    </>
  );
}
