import type { Metadata } from "next";
import Link from "next/link";
import { Icoon, Kaart, PaginaKop, Penseel, Sectie, tekstKleur } from "@/components/ui";
import { aanbodTekst, trajecten } from "@/content/aanbod";

export const metadata: Metadata = {
  title: "Ons aanbod",
  description: aanbodTekst.tekst,
};

export default function AanbodPagina() {
  return (
    <>
      <PaginaKop label={aanbodTekst.label} titel={aanbodTekst.titel} tekst={aanbodTekst.tekst} />

      <Sectie className="py-6">
        <Penseel>{aanbodTekst.tariefNota}</Penseel>
      </Sectie>

      <Sectie className="grid gap-5 pb-16">
        {trajecten.map((traject) => (
          <Kaart key={traject.naam} className="scroll-mt-24">
            <div className="flex flex-wrap items-start gap-4">
              <Icoon kleur={traject.kleur}>{traject.icoon}</Icoon>
              <div className="min-w-[14rem] flex-1">
                <h2 className={`text-2xl ${tekstKleur[traject.kleur]}`}>{traject.naam}</h2>
                <p className="text-[15px] font-bold text-ink-dim">{traject.ondertitel}</p>
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
                <p className="text-sm font-bold text-ink-dim">{traject.leeftijd}</p>
              </div>
            </div>

            <p className="mt-4 max-w-[68ch] text-ink-dim">{traject.tekst}</p>

            <dl className="mt-5 grid gap-2 sm:grid-cols-2">
              {traject.regels.map((regel) => (
                <div key={regel.label} className="rounded-xl bg-sage-soft px-4 py-3">
                  <dt className="text-[12px] font-extrabold tracking-[0.06em] text-green uppercase">
                    {regel.label}
                  </dt>
                  <dd className="text-[15px] text-ink">{regel.waarde}</dd>
                </div>
              ))}
            </dl>

            {traject.punten ? (
              <ul className="mt-4 grid gap-1.5">
                {traject.punten.map((punt) => (
                  <li key={punt} className="flex gap-2.5 text-[15px] text-ink-dim">
                    <span aria-hidden className={tekstKleur[traject.kleur]}>
                      ●
                    </span>
                    {punt}
                  </li>
                ))}
              </ul>
            ) : null}
          </Kaart>
        ))}

        <div className="rounded-[20px] bg-green px-7 py-8 text-cream">
          <h2 className="text-2xl text-cream">{aanbodTekst.inschrijvenTekst}</h2>
          <Link
            href={aanbodTekst.inschrijvenLink}
            className="mt-5 inline-block rounded-full bg-cream px-6 py-3 text-[15px] font-extrabold text-green transition hover:-translate-y-0.5"
          >
            Neem contact op →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
