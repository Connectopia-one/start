import type { Metadata } from "next";
import {
  Kaart,
  NaarLink,
  PaginaKop,
  Sectie,
  icoonKleur,
} from "@/components/ui";
import { oefenplatform } from "@/content/oefenplatform";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: oefenplatform.titel,
  description: oefenplatform.tekst,
};

/* Dezelfde knopvorm als elders op de site, maar met NaarLink, want de twee
   knoppen hieronder wijzen naar oefenplatform.connectopia.one. */
const knopPrimair =
  "inline-block rounded-full border-2 border-green bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:border-green-mid hover:bg-green-mid";
const knopTweede =
  "inline-block rounded-full border-2 border-green px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5 hover:bg-sage-soft";

export default function OefenplatformPagina() {
  return (
    <>
      <PaginaKop
        label={oefenplatform.label}
        titel={oefenplatform.titel}
        handgeschreven={oefenplatform.handgeschreven}
        tekst={oefenplatform.tekst}
      />

      {/* De prijs en de twee knoppen, meteen bovenaan. Dit is wat een ouder
          die hier binnenkomt als eerste wil weten. */}
      <Sectie className="py-6">
        <div className="rounded-[20px] bg-sage-soft px-6 py-6">
          <p className="text-3xl font-extrabold text-green">
            €{oefenplatform.prijsNu}
            <span className="text-base font-normal text-ink-dim">
              {" "}
              per schooljaar, voor het hele gezin
            </span>
          </p>
          <p className="mt-3 max-w-[68ch] text-[16px] text-ink">
            {oefenplatform.prijsUitleg}
          </p>
          <div className="mt-5 flex flex-wrap gap-3">
            <NaarLink
              href={oefenplatform.startKnop.href}
              className={knopPrimair}
            >
              {oefenplatform.startKnop.tekst}
            </NaarLink>
            <NaarLink
              href={oefenplatform.accountKnop.href}
              className={knopTweede}
            >
              {oefenplatform.accountKnop.tekst}
            </NaarLink>
          </div>
          <p className="mt-3 max-w-[68ch] text-[15px] text-ink-dim">
            {oefenplatform.gratisZin}
          </p>
        </div>
      </Sectie>

      {/* Voor wie. */}
      <Sectie className="py-4">
        <h2 className="text-2xl text-green">{oefenplatform.voorWieTitel}</h2>
        <div className="mt-4 grid gap-4 sm:grid-cols-2">
          {oefenplatform.voorWie.map((groep) => (
            <Kaart key={groep.naam} className="flex flex-col">
              <span
                aria-hidden
                className={`flex h-12 w-12 items-center justify-center rounded-full text-2xl ${icoonKleur[groep.kleur]}`}
              >
                {groep.icoon}
              </span>
              <h3 className="mt-3 text-xl text-green">{groep.naam}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{groep.tekst}</p>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* De niveaus. */}
      <Sectie className="py-4">
        <h2 className="text-2xl text-green">{oefenplatform.niveausTitel}</h2>
        <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
          {oefenplatform.niveausTekst}
        </p>
        <ul className="mt-4 grid gap-3">
          {oefenplatform.niveaus.map((niveau) => (
            <li
              key={niveau.naam}
              className="rounded-[20px] border border-border bg-surface px-5 py-4"
            >
              <p className="text-[17px] font-extrabold text-green">
                <span aria-hidden className="mr-2">
                  {niveau.emoji}
                </span>
                {niveau.naam}
                <span className="font-normal text-ink-dim">
                  {" — "}
                  {niveau.wat}
                </span>
              </p>
              <p className="mt-1 text-[15px] text-ink-dim">{niveau.vakken}</p>
            </li>
          ))}
        </ul>
        <p className="mt-3 max-w-[68ch] text-[15px] text-ink-dim">
          {oefenplatform.niveausSlot}
        </p>
      </Sectie>

      {/* Wat er bij elk hoofdstuk hoort. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] bg-orange-soft px-6 py-5">
          <h2 className="text-2xl text-orange">
            {oefenplatform.hoortErbijTitel}
          </h2>
          <ul className="mt-4 grid gap-4 sm:grid-cols-2">
            {oefenplatform.hoortErbij.map((ding) => (
              <li key={ding.titel}>
                <p className="text-[16px] font-extrabold text-green">
                  {ding.titel}
                </p>
                <p className="mt-1 text-[15px] text-ink-dim">{ding.tekst}</p>
              </li>
            ))}
          </ul>
        </div>
      </Sectie>

      {/* Hoe de vragen gemaakt worden. */}
      <Sectie className="py-4">
        <Kaart>
          <h2 className="text-2xl text-green">{oefenplatform.manierTitel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
            {oefenplatform.manierTekst}
          </p>
          <ul className="mt-4 flex flex-wrap gap-2">
            {oefenplatform.manierWoorden.map((woord) => (
              <li
                key={woord}
                className="rounded-full bg-sage-soft px-4 py-1.5 text-[15px] font-extrabold text-green"
              >
                {woord}
              </li>
            ))}
          </ul>
          <p className="mt-4 max-w-[68ch] text-[16px] text-ink-dim">
            {oefenplatform.manierMelden}
          </p>
        </Kaart>
      </Sectie>

      {/* De extraatjes. */}
      <Sectie className="py-4">
        <h2 className="text-2xl text-green">{oefenplatform.extrasTitel}</h2>
        <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
          {oefenplatform.extrasTekst}
        </p>
        <div className="mt-4 grid gap-4 sm:grid-cols-3">
          {oefenplatform.extras.map((extra) => (
            <Kaart key={extra.titel}>
              <span aria-hidden className="text-2xl">
                {extra.icoon}
              </span>
              <h3 className="mt-2 text-lg text-green">{extra.titel}</h3>
              <p className="mt-1 text-[15px] text-ink-dim">{extra.tekst}</p>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* De uitdagingshoek, vroeger een band op de startpagina. */}
      <Sectie className="py-4">
        <div className="grid items-center gap-5 rounded-[20px] bg-purple-soft px-6 py-7 sm:grid-cols-[1fr_auto] sm:px-8">
          <div>
            <span className="text-[14px] font-bold text-purple">
              {oefenplatform.hoekLabel}
            </span>
            <h2 className="mt-1.5 text-2xl text-green">
              {oefenplatform.hoekTitel}
            </h2>
            <p className="mt-2 max-w-[60ch] text-[16px] text-ink-dim">
              {oefenplatform.hoekTekst}
            </p>
          </div>
          <a
            href={oefenplatform.hoekLink}
            className="inline-block justify-self-start rounded-full bg-purple px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 sm:justify-self-end"
          >
            {oefenplatform.hoekKnop} →
          </a>
        </div>
      </Sectie>

      {/* Zo begin je. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] bg-purple-soft px-6 py-5">
          <h2 className="text-2xl text-purple">{oefenplatform.stappenTitel}</h2>
          <ol className="mt-4 grid gap-4 sm:grid-cols-3">
            {oefenplatform.stappen.map((stap) => (
              <li key={stap.nummer}>
                <span
                  aria-hidden
                  className="flex h-9 w-9 items-center justify-center rounded-full bg-purple text-[16px] font-extrabold text-cream"
                >
                  {stap.nummer}
                </span>
                <p className="mt-2 text-[16px] font-extrabold text-green">
                  {stap.titel}
                </p>
                <p className="mt-1 text-[15px] text-ink-dim">{stap.tekst}</p>
              </li>
            ))}
          </ol>
          <div className="mt-5 flex flex-wrap gap-3">
            <NaarLink
              href={oefenplatform.accountKnop.href}
              className={knopPrimair}
            >
              {oefenplatform.accountKnop.tekst}
            </NaarLink>
          </div>
        </div>
      </Sectie>

      {/* Nog een vraag? */}
      <Sectie className="pb-16">
        <Kaart>
          <h2 className="text-xl text-green">{oefenplatform.vragenTitel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
            {oefenplatform.vragenTekst}
          </p>
          <p className="mt-3 text-[16px] text-ink-dim">
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
            . Liever teruggebeld worden? Dat kan via{" "}
            <a
              href="/contact"
              className="font-bold text-green underline-offset-4 hover:underline"
            >
              onze contactpagina
            </a>
            .
          </p>
        </Kaart>
      </Sectie>
    </>
  );
}
