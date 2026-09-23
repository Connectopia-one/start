import type { Metadata } from "next";
import Link from "next/link";
import {
  Icoon,
  Kaart,
  Label,
  PaginaKop,
  Sectie,
  tekstKleur,
  vlakKleur,
} from "@/components/ui";
import { stappen, wegwijzerTekst } from "@/content/wegwijzer";

export const metadata: Metadata = {
  title: "Wegwijzer voor ouders",
  description: wegwijzerTekst.tekst,
};

export default function WegwijzerPagina() {
  return (
    <>
      <PaginaKop
        label={wegwijzerTekst.label}
        titel={wegwijzerTekst.titel}
        handgeschreven={wegwijzerTekst.handgeschreven}
        tekst={wegwijzerTekst.tekst}
      />

      <Sectie className="py-6">
        <p className="rounded-[20px] bg-purple-soft px-6 py-4 text-[16px] text-ink">
          {wegwijzerTekst.nota}
        </p>
      </Sectie>

      <Sectie className="grid gap-4 pb-8">
        {stappen.map((stap) => (
          <Kaart key={stap.nummer}>
            <div className="flex flex-wrap items-start gap-4">
              <Icoon kleur={stap.kleur}>{stap.icoon}</Icoon>
              <div className="min-w-[14rem] flex-1">
                <h2 className={`text-2xl ${tekstKleur[stap.kleur]}`}>
                  Stap {stap.nummer}: {stap.titel}
                </h2>
                <p className="text-[16px] font-bold text-ink-dim">
                  {stap.samenvatting}
                </p>
              </div>
            </div>

            <ul className="mt-4 grid gap-2">
              {stap.punten.map((punt) => (
                <li
                  key={punt}
                  className="flex gap-2.5 text-[16px] text-ink-dim"
                >
                  <span aria-hidden className={tekstKleur[stap.kleur]}>
                    ●
                  </span>
                  {punt}
                </li>
              ))}
            </ul>

            {/* De zin die mag opvallen, in een gekleurd kader. */}
            {stap.nadruk ? (
              <p
                className={`mt-5 rounded-[16px] px-5 py-4 text-[16px] font-bold text-ink ${vlakKleur[stap.kleur]}`}
              >
                {stap.nadruk}
              </p>
            ) : null}

            {/* Een kadertje met een knop, bijvoorbeeld om contact op te nemen. */}
            {stap.tip ? (
              <div className="mt-4 flex flex-wrap items-center gap-x-5 gap-y-3 rounded-[16px] border border-dashed border-border px-5 py-4">
                <p className="min-w-[14rem] flex-1 text-[16px] text-ink-dim">
                  <span className="font-hand mr-2 text-xl text-orange">
                    Tip:
                  </span>
                  {stap.tip.tekst}
                </p>
                <Link
                  href={stap.tip.knopLink}
                  className="inline-block rounded-full border-2 border-green px-5 py-2.5 text-[15px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft"
                >
                  {stap.tip.knopTekst} →
                </Link>
              </div>
            ) : null}
          </Kaart>
        ))}
      </Sectie>

      {/* Het blad dat je invult en meeneemt naar je gesprek. */}
      {wegwijzerTekst.observatieblok ? (
        <Sectie className="py-0">
          <Kaart className="border-2 border-orange">
            <Label>{wegwijzerTekst.observatieblok.label}</Label>
            <h2 className="mt-2 text-2xl text-green">
              {wegwijzerTekst.observatieblok.titel}
            </h2>
            <p className="mt-3 max-w-[66ch] text-[16px] text-ink">
              {wegwijzerTekst.observatieblok.tekst}
            </p>
            <Link
              href={wegwijzerTekst.observatieblok.knopLink}
              className="mt-5 inline-block rounded-full bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
            >
              {wegwijzerTekst.observatieblok.knopTekst} →
            </Link>
          </Kaart>
        </Sectie>
      ) : null}

      <Sectie className="pb-16">
        <div className="rounded-[20px] bg-green px-7 py-8 text-cream">
          <h2 className="text-2xl text-cream">{wegwijzerTekst.slot.titel}</h2>
          <p className="mt-3 max-w-[58ch] text-cream/85">
            {wegwijzerTekst.slot.tekst}
          </p>
          <Link
            href={wegwijzerTekst.slot.knopLink}
            className="mt-6 inline-block rounded-full bg-cream px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5"
          >
            {wegwijzerTekst.slot.knopTekst} →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
