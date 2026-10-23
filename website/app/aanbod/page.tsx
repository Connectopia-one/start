import type { Metadata } from "next";
import Link from "next/link";
import { Quotes } from "@/components/Quotes";
import {
  Foto,
  Handjes,
  Icoon,
  Kaart,
  PaginaKop,
  Penseel,
  Sectie,
  tekstKleur,
} from "@/components/ui";
import {
  aanbodTekst,
  inbegrepen,
  proefles,
  trajecten,
  voorbehouden,
} from "@/content/aanbod";
import { aanvraagLink, soorten } from "@/content/formulier";

export const metadata: Metadata = {
  title: "Kampen, Young Engineers Hasselt-Genk en plusklas",
  description:
    "Kampen in elke vakantie, Young Engineers Hasselt-Genk, de Ontdekclub, plusklas en pluswerking in Hasselt (Level X 28) en Genk (T2 Campus). Kleine groepjes, prikkelarm, ook voor HB en UHB.",
};

export default function AanbodPagina() {
  return (
    <>
      <PaginaKop
        label={aanbodTekst.label}
        titel={aanbodTekst.titel}
        tekst={aanbodTekst.tekst}
      />

      {/* Kim op 21 oktober 2026: je moest te ver scrollen voor je zag wat we
          aanbieden. Daarom komen de trajecten nu meteen, met bovenaan een rij
          knopjes om er direct naartoe te springen. De uitleg over wat er
          inbegrepen is en de vrijgehouden plaatsen staat onder de trajecten. */}
      <Sectie className="py-6">
        <Penseel>{aanbodTekst.tariefNota}</Penseel>
        <ul className="mt-5 flex flex-wrap gap-2.5">
          {trajecten.map((traject) => (
            <li key={traject.slug}>
              <a
                href={`#${traject.slug}`}
                className="flex items-center gap-2 rounded-full border border-border bg-surface px-4 py-2 text-[15px] font-bold text-green hover:bg-sage-soft"
              >
                <span aria-hidden>{traject.icoon}</span>
                {traject.naam}
              </a>
            </li>
          ))}
        </ul>
      </Sectie>

      <Sectie className="grid gap-5 pb-8">
        {trajecten.map((traject) => (
          <Kaart key={traject.naam} id={traject.slug} className="scroll-mt-24">
            <div className="flex flex-wrap items-start gap-4">
              <Icoon kleur={traject.kleur}>{traject.icoon}</Icoon>
              <div className="min-w-[14rem] flex-1">
                <h2 className={`text-2xl ${tekstKleur[traject.kleur]}`}>
                  {traject.naam}
                </h2>
                <p className="text-[16px] font-bold text-ink-dim">
                  {traject.ondertitel}
                </p>
              </div>
              <div className="text-right">
                {traject.prijs ? (
                  <p className="text-xl font-extrabold text-green">
                    {traject.prijsWas ? (
                      <span className="mr-2 text-base font-bold text-ink-dim line-through">
                        {traject.prijsWas}
                      </span>
                    ) : null}
                    {traject.prijs}
                  </p>
                ) : null}
                <p className="text-[15px] font-bold text-ink-dim">
                  {traject.leeftijd}
                </p>
              </div>
            </div>

            {traject.foto ? (
              <Foto
                bestand={traject.foto.bestand}
                beschrijving={traject.foto.beschrijving}
                verhouding="vrij"
                className="mt-5"
              />
            ) : null}

            <p className="mt-4 max-w-[68ch] text-ink-dim">{traject.tekst}</p>

            <dl className="mt-5 grid gap-2 sm:grid-cols-2">
              {traject.regels.map((regel) => (
                <div
                  key={regel.label}
                  className="rounded-xl bg-sage-soft px-4 py-3"
                >
                  <dt className="text-[13px] font-extrabold text-green">
                    {regel.label}
                  </dt>
                  <dd className="text-[16px] text-ink">{regel.waarde}</dd>
                </div>
              ))}
            </dl>

            {traject.instappen ? (
              <div className="mt-4 rounded-2xl border border-dashed border-orange/50 bg-orange-soft/50 px-5 py-4">
                {/* Kopje "Instappen" en niet "Later instappen": bij ons kan
                    starten altijd, niet alleen bij een volgende ronde. */}
                <p className="text-[13px] font-extrabold text-orange">
                  Instappen
                </p>
                <p className="mt-1 text-[16px] text-ink">
                  {traject.instappen.tekst}
                </p>
                {traject.instappen.data && traject.instappen.data.length > 0 ? (
                  <ul className="mt-2 flex flex-wrap gap-2">
                    {traject.instappen.data.map((datum) => (
                      <li
                        key={datum}
                        className="rounded-full bg-surface px-3.5 py-1 text-[14px] font-bold text-orange"
                      >
                        {datum}
                      </li>
                    ))}
                  </ul>
                ) : null}
              </div>
            ) : null}

            {traject.punten ? (
              <ul className="mt-4 grid gap-1.5">
                {traject.punten.map((punt) => (
                  <li
                    key={punt}
                    className="flex gap-2.5 text-[16px] text-ink-dim"
                  >
                    <span aria-hidden className={tekstKleur[traject.kleur]}>
                      ●
                    </span>
                    {punt}
                  </li>
                ))}
              </ul>
            ) : null}

            {/* Info vragen of meteen inschrijven, allebei met een eigen formulier. */}
            <div className="mt-6 flex flex-wrap gap-3 border-t border-dashed border-border pt-5">
              {traject.inschrijvenLink ? (
                <a
                  href={traject.inschrijvenLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block rounded-full bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
                >
                  {soorten.inschrijven.knop} →
                </a>
              ) : (
                <Link
                  href={aanvraagLink("inschrijven", traject.slug)}
                  className="inline-block rounded-full bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
                >
                  {soorten.inschrijven.knop} →
                </Link>
              )}
              <Link
                href={aanvraagLink("info", traject.slug)}
                className="inline-block rounded-full border-2 border-green px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft"
              >
                {soorten.info.knop}
              </Link>
              {traject.links?.map((l) => (
                <a
                  key={l.link}
                  href={l.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block rounded-full border-2 border-green px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft"
                >
                  {l.tekst} ↗
                </a>
              ))}
            </div>
          </Kaart>
        ))}

        {/* Goed om te weten: wat er inbegrepen is en de vrijgehouden
            plaatsen (zie de uitleg in content/aanbod.ts), naast elkaar. */}
        <div className="grid gap-5 md:grid-cols-2">
          <div className="rounded-[20px] bg-sage-soft px-7 py-6">
            <h2 className="text-2xl text-green">{inbegrepen.titel}</h2>
            <p className="mt-2 text-[16px] text-ink">{inbegrepen.tekst}</p>
            <ul className="mt-4 grid gap-2">
              {inbegrepen.punten.map((punt) => (
                <li
                  key={punt}
                  className="rounded-[14px] bg-cream px-4 py-2.5 text-[16px] font-bold text-green"
                >
                  {punt}
                </li>
              ))}
            </ul>
          </div>
          <div className="flex flex-col rounded-[20px] border border-border bg-surface px-7 py-6">
            <h2 className="text-2xl text-green">{voorbehouden.titel}</h2>
            <p className="mt-2 text-[16px] text-ink-dim">
              {voorbehouden.tekst}
            </p>
            <Handjes className="mt-4 w-40 self-center md:mt-auto" />
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-5 rounded-[20px] bg-orange-soft px-7 py-6">
          <div className="min-w-[18rem] flex-1">
            <h2 className="text-2xl text-orange">{proefles.titel}</h2>
            <p className="mt-2 max-w-[56ch] text-ink">{proefles.tekst}</p>
          </div>
          <Link
            href={aanvraagLink("proefles")}
            className="inline-block rounded-full bg-orange px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {proefles.knopTekst} →
          </Link>
        </div>

        <div className="rounded-[20px] bg-green px-7 py-8 text-cream">
          <h2 className="text-2xl text-cream">
            {aanbodTekst.inschrijvenTekst}
          </h2>
          <Link
            href={aanvraagLink("info")}
            className="mt-5 inline-block rounded-full bg-cream px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5"
          >
            Neem contact op →
          </Link>
        </div>
      </Sectie>
      <Quotes />
    </>
  );
}
