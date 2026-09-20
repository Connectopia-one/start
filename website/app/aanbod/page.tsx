import type { Metadata } from "next";
import Link from "next/link";
import {
  Foto,
  Icoon,
  Kaart,
  PaginaKop,
  Penseel,
  Sectie,
  tekstKleur,
} from "@/components/ui";
import { aanbodTekst, proefles, trajecten } from "@/content/aanbod";
import { aanvraagLink, soorten } from "@/content/formulier";

export const metadata: Metadata = {
  title: "Ons aanbod",
  description: aanbodTekst.tekst,
};

export default function AanbodPagina() {
  return (
    <>
      <PaginaKop
        label={aanbodTekst.label}
        titel={aanbodTekst.titel}
        tekst={aanbodTekst.tekst}
      />

      <Sectie className="py-6">
        <Penseel>{aanbodTekst.tariefNota}</Penseel>

        <div className="mt-6 flex flex-wrap items-center gap-5 rounded-[20px] bg-orange-soft px-7 py-6">
          <div className="min-w-[18rem] flex-1">
            <h2 className="text-2xl text-orange">{proefles.titel}</h2>
            <p className="mt-2 max-w-[56ch] text-ink">{proefles.tekst}</p>
          </div>
          <Link
            href={aanvraagLink("proefles")}
            className="inline-block rounded-full bg-orange px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {proefles.knopTekst} →
          </Link>
        </div>
      </Sectie>

      <Sectie className="grid gap-5 pb-16">
        {trajecten.map((traject) => (
          <Kaart key={traject.naam} className="scroll-mt-24">
            <div className="flex flex-wrap items-start gap-4">
              <Icoon kleur={traject.kleur}>{traject.icoon}</Icoon>
              <div className="min-w-[14rem] flex-1">
                <h2 className={`text-2xl ${tekstKleur[traject.kleur]}`}>
                  {traject.naam}
                </h2>
                <p className="text-[15px] font-bold text-ink-dim">
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
                <p className="text-sm font-bold text-ink-dim">
                  {traject.leeftijd}
                </p>
              </div>
            </div>

            {traject.foto ? (
              <Foto
                bestand={traject.foto.bestand}
                beschrijving={traject.foto.beschrijving}
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
                  <dt className="text-[12px] font-extrabold tracking-[0.06em] text-green uppercase">
                    {regel.label}
                  </dt>
                  <dd className="text-[15px] text-ink">{regel.waarde}</dd>
                </div>
              ))}
            </dl>

            {traject.instappen ? (
              <div className="mt-4 rounded-2xl border border-dashed border-orange/50 bg-orange-soft/50 px-5 py-4">
                <p className="text-[12px] font-extrabold tracking-[0.06em] text-orange uppercase">
                  Later instappen
                </p>
                <p className="mt-1 text-[15px] text-ink">
                  {traject.instappen.tekst}
                </p>
                {traject.instappen.data && traject.instappen.data.length > 0 ? (
                  <ul className="mt-2 flex flex-wrap gap-2">
                    {traject.instappen.data.map((datum) => (
                      <li
                        key={datum}
                        className="rounded-full bg-surface px-3.5 py-1 text-[13px] font-bold text-orange"
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
                    className="flex gap-2.5 text-[15px] text-ink-dim"
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
              <Link
                href={aanvraagLink("inschrijven", traject.slug)}
                className="inline-block rounded-full bg-green px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
              >
                {soorten.inschrijven.knop} →
              </Link>
              <Link
                href={aanvraagLink("info", traject.slug)}
                className="inline-block rounded-full border-2 border-green px-6 py-3 text-[15px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft"
              >
                {soorten.info.knop}
              </Link>
            </div>
          </Kaart>
        ))}

        <div className="rounded-[20px] bg-green px-7 py-8 text-cream">
          <h2 className="text-2xl text-cream">
            {aanbodTekst.inschrijvenTekst}
          </h2>
          <Link
            href={aanvraagLink("info")}
            className="mt-5 inline-block rounded-full bg-cream px-6 py-3 text-[15px] font-extrabold text-green transition hover:-translate-y-0.5"
          >
            Neem contact op →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
