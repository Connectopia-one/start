import type { Metadata } from "next";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { site } from "@/content/site";
import { steun, steunVelden } from "@/content/steun";

export const metadata: Metadata = {
  title: steun.titel,
  description: steun.tekst,
};

/* De kleur van het rondje bij elke manier, zoals overal op de site. */
const manierKleur = {
  green: "bg-sage-soft",
  purple: "bg-purple-soft",
  orange: "bg-orange-soft",
} as const;

export default async function SteunPagina() {
  return (
    <>
      <PaginaKop
        label={steun.label}
        titel={steun.titel}
        handgeschreven={steun.handgeschreven}
        tekst={steun.tekst}
      />

      {/* De manieren waarop iemand kan helpen. */}
      <Sectie className="py-6">
        <h2 className="text-2xl text-green">{steun.manierenTitel}</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          {steun.manieren.map((manier) => (
            <Kaart key={manier.titel}>
              <span
                aria-hidden
                className={`flex h-12 w-12 items-center justify-center rounded-full text-2xl ${manierKleur[manier.kleur]}`}
              >
                {manier.icoon}
              </span>
              <h3 className="mt-3 text-xl text-green">{manier.titel}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{manier.tekst}</p>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* Waar het geld naartoe gaat, en hoe je een gift doet. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] bg-orange-soft px-6 py-5">
          <h2 className="text-2xl text-orange">{steun.waarheenTitel}</h2>
          <ul className="mt-3 grid gap-2 sm:grid-cols-2">
            {steun.waarheen.map((regel) => (
              <li key={regel} className="text-[16px] text-ink">
                {regel}
              </li>
            ))}
          </ul>
          <p className="mt-4 text-[16px] font-bold text-green">
            {/*
              Staat het rekeningnummer er nog niet, dan beloven we het niet
              half: we zeggen gewoon dat we de gegevens bezorgen.
            */}
            {steun.rekening
              ? `Een gift doe je op ${steun.rekening}, op naam van Connectopia vzw.`
              : "Wil je een gift doen? Vul hieronder het formulier in of bel ons, dan bezorgen we je onze gegevens."}
          </p>
        </div>
      </Sectie>

      {/* Voor bedrijven: geen gift maar reclame, met een document erbij. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] border border-border bg-surface px-6 py-5">
          <span className="text-[14px] font-bold text-purple">
            {steun.bedrijven.label}
          </span>
          <h2 className="mt-1 text-2xl text-green">{steun.bedrijven.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
            {steun.bedrijven.tekst}
          </p>
          <ul className="mt-4 grid gap-2 sm:grid-cols-2">
            {steun.bedrijven.punten.map((punt) => (
              <li
                key={punt}
                className="rounded-[14px] bg-purple-soft px-4 py-2.5 text-[16px] font-bold text-green"
              >
                {punt}
              </li>
            ))}
          </ul>
        </div>
      </Sectie>

      {/* Wat een particulier er fiscaal aan heeft: niets, en dat zeggen we. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] border border-border bg-surface px-6 py-5">
          <h2 className="text-xl text-green">{steun.attesten.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
            {steun.attesten.tekst}
          </p>
        </div>
      </Sectie>

      {/* Voor wie twijfelt of zijn idee wel meetelt. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] bg-sage-soft px-6 py-5">
          <h2 className="text-xl text-green">{steun.breed.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
            {steun.breed.tekst}
          </p>
        </div>
      </Sectie>

      {/* Het formulier. */}
      <Sectie className="grid gap-4 pb-16 pt-4">
        <Kaart className="scroll-mt-24" id="aanbod">
          <h2 className="text-2xl text-green">{steun.formulierTitel}</h2>
          <p className="mt-2 max-w-[62ch] text-[16px] text-ink-dim">
            {steun.formulierTekst}
          </p>
          <div className="mt-6">
            <Aanvraagformulier
              onderwerp={steun.onderwerp}
              vragen={steunVelden}
              privacy={steun.privacy}
              verborgen={[{ naam: "Soort aanvraag", waarde: "Steun" }]}
            />
          </div>
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">Liever gewoon bellen of mailen?</h2>
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
