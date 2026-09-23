import type { Metadata } from "next";
import Link from "next/link";
import {
  Icoon,
  Kaart,
  PaginaKop,
  Sectie,
  tekstKleur,
  vlakKleur,
} from "@/components/ui";
import {
  gegevens,
  hulpNu,
  observatieTekst,
  onderdelen,
  openVragen,
  overlapTekst,
} from "@/content/observatielijst";

export const metadata: Metadata = {
  title: "Observatielijst voor ouders",
  description: observatieTekst.tekst,
};

/* Een schrijflijntje dat je zowel op je scherm als op papier kan invullen. */
function Lijn({ label }: { label?: string }) {
  return (
    <label className="block">
      {label ? (
        <span className="text-[14px] font-bold text-ink-dim">{label}</span>
      ) : null}
      <input
        type="text"
        aria-label={label}
        className="mt-0.5 block h-8 w-full border-0 border-b border-border bg-transparent text-[16px] text-ink outline-none focus:border-green"
      />
    </label>
  );
}

function Vinkje({ naam }: { naam: string }) {
  return (
    <input
      type="checkbox"
      aria-label={naam}
      className="h-[18px] w-[18px] accent-green"
    />
  );
}

export default function ObservatielijstPagina() {
  const kolommen = observatieTekst.kolommen;

  return (
    <>
      <PaginaKop
        label={observatieTekst.label}
        titel={observatieTekst.titel}
        handgeschreven={observatieTekst.handgeschreven}
        tekst={observatieTekst.tekst}
      />

      {/* De belangrijkste zin van de pagina: dit is geen diagnose. */}
      <Sectie className="py-6">
        <p className="rounded-[20px] border-2 border-orange bg-orange-soft px-6 py-5 text-[16px] font-bold text-ink">
          {observatieTekst.waarschuwing}
        </p>
      </Sectie>

      <Sectie className="niet-afdrukken grid gap-4 py-0 md:grid-cols-2">
        <Kaart>
          <h2 className="text-xl text-green">Hoe vul je dit in?</h2>
          <ul className="mt-3 grid gap-2">
            {observatieTekst.hoeInvullen.map((regel) => (
              <li key={regel} className="flex gap-2.5 text-[16px] text-ink-dim">
                <span aria-hidden className="text-green">
                  ●
                </span>
                {regel}
              </li>
            ))}
          </ul>
        </Kaart>
        <Kaart className="self-start">
          <h2 className="text-xl text-green">Afdrukken</h2>
          <p className="mt-3 text-[16px] text-ink-dim">
            {observatieTekst.afdrukken}
          </p>
        </Kaart>
      </Sectie>

      {/* De gegevens bovenaan het blad. */}
      <Sectie className="pt-10 pb-0">
        <Kaart className="afdruk-kaart">
          <h2 className="text-xl text-green">Over wie gaat dit blad?</h2>
          <div className="mt-4 grid gap-x-8 gap-y-4 sm:grid-cols-2">
            {gegevens.map((veld) => (
              <Lijn key={veld} label={veld} />
            ))}
          </div>
        </Kaart>
      </Sectie>

      {/* De hoofdstukken met de vragen. */}
      <Sectie className="grid gap-4 py-8">
        {onderdelen.map((onderdeel) => (
          <Kaart key={onderdeel.nummer} className="afdruk-kaart min-w-0">
            <div className="flex flex-wrap items-start gap-4">
              <Icoon kleur={onderdeel.kleur}>{onderdeel.icoon}</Icoon>
              <div className="min-w-0 flex-1">
                <h2 className={`text-2xl ${tekstKleur[onderdeel.kleur]}`}>
                  {onderdeel.nummer}. {onderdeel.titel}
                </h2>
                <p className="mt-1 text-[16px] text-ink-dim">
                  {onderdeel.inleiding}
                </p>
              </div>
            </div>

            {/* De kopjes boven de drie kolommen met vinkjes. */}
            <div className="mt-5 flex items-end gap-1 border-b border-border pb-1.5 sm:gap-2">
              <span className="flex-1" />
              {kolommen.map((kolom) => (
                <span
                  key={kolom}
                  className="w-10 text-center text-[12px] leading-tight font-bold text-ink-dim sm:w-14"
                >
                  {kolom}
                </span>
              ))}
            </div>

            <ul>
              {onderdeel.vragen.map((vraag) => (
                <li
                  key={vraag.tekst}
                  className="flex items-center gap-1 border-b border-border/60 py-2 sm:gap-2"
                >
                  <span className="min-w-0 flex-1 text-[16px] text-ink">
                    {vraag.tekst}
                    {vraag.toelichting ? (
                      <span className="text-ink-dim">
                        {" "}
                        ({vraag.toelichting})
                      </span>
                    ) : null}
                  </span>
                  {kolommen.map((kolom) => (
                    <span
                      key={kolom}
                      className="flex w-10 shrink-0 justify-center sm:w-14"
                    >
                      <Vinkje naam={`${vraag.tekst} — ${kolom}`} />
                    </span>
                  ))}
                </li>
              ))}
            </ul>

            {/* Waar zie je dit vooral: thuis, op school, of allebei. */}
            <div
              className={`mt-4 flex flex-wrap items-center gap-x-6 gap-y-2 rounded-[16px] px-5 py-3 ${vlakKleur[onderdeel.kleur]}`}
            >
              <span className="text-[15px] font-bold text-ink">
                {observatieTekst.plaatsVraag}
              </span>
              {observatieTekst.plaatsOpties.map((optie) => (
                <label
                  key={optie}
                  className="flex items-center gap-2 text-[15px] text-ink"
                >
                  <Vinkje naam={`${onderdeel.titel} — ${optie}`} />
                  {optie}
                </label>
              ))}
            </div>

            <div className="mt-3">
              <Lijn label={observatieTekst.notitieVraag} />
            </div>
          </Kaart>
        ))}
      </Sectie>

      {/* De vragen waar je zelf een antwoord bij schrijft. */}
      <Sectie className="py-0">
        <Kaart className="afdruk-kaart">
          <h2 className="text-2xl text-green">In je eigen woorden</h2>
          <p className="mt-1 text-[16px] text-ink-dim">
            Deze antwoorden zijn voor een specialist vaak het waardevolste stuk
            van het blad.
          </p>
          <div className="mt-5 grid gap-6">
            {openVragen.map((open) => (
              <div key={open.vraag}>
                <p className="text-[16px] font-bold text-ink">{open.vraag}</p>
                <div className="mt-1 grid gap-1">
                  {Array.from({ length: open.regels }, (_, i) => (
                    <Lijn key={i} label={undefined} />
                  ))}
                </div>
              </div>
            ))}
          </div>
        </Kaart>
      </Sectie>

      {/* Waarom er geen diagnose bij de vragen staat. */}
      <Sectie className="py-10">
        <Kaart className="afdruk-kaart">
          <h2 className="text-2xl text-green">{overlapTekst.titel}</h2>
          <p className="mt-3 max-w-[70ch] text-[16px] text-ink-dim">
            {overlapTekst.inleiding}
          </p>

          <div className="mt-6 grid gap-4 md:grid-cols-2">
            {overlapTekst.paren.map((paar) => (
              <div
                key={paar.titel}
                className="rounded-[16px] bg-cream px-5 py-4"
              >
                <h3 className="text-[18px] text-purple">{paar.titel}</h3>
                <p className="mt-2 text-[16px] text-ink-dim">{paar.tekst}</p>
              </div>
            ))}
          </div>

          <p className="mt-6 rounded-[16px] bg-purple-soft px-5 py-4 text-[16px] font-bold text-ink">
            {overlapTekst.nadruk}
          </p>
        </Kaart>
      </Sectie>

      {/* Wat je doet als je je nu zorgen maakt. */}
      <Sectie className="py-0">
        <div className="rounded-[20px] border-2 border-orange bg-surface px-6 py-5">
          <h2 className="text-xl text-orange">{hulpNu.titel}</h2>
          <p className="mt-2 text-[16px] text-ink">{hulpNu.tekst}</p>
        </div>
      </Sectie>

      <Sectie className="niet-afdrukken pb-16">
        <div className="rounded-[20px] bg-green px-7 py-8 text-cream">
          <h2 className="text-2xl text-cream">{observatieTekst.slot.titel}</h2>
          <p className="mt-3 max-w-[58ch] text-cream/85">
            {observatieTekst.slot.tekst}
          </p>
          <Link
            href={observatieTekst.slot.knopLink}
            className="mt-6 inline-block rounded-full bg-cream px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5"
          >
            {observatieTekst.slot.knopTekst} →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
