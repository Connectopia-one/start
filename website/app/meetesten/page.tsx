import type { Metadata } from "next";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Kaart, Knop, PaginaKop, Sectie } from "@/components/ui";
import { meetesten, meetestenVelden } from "@/content/meetesten";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: meetesten.titel,
  description: meetesten.tekst,
};

/* De kleur van het rondje bij elke groep, zoals overal op de site. */
const groepKleur = {
  purple: { vlak: "bg-purple-soft", tekst: "text-purple" },
  blue: { vlak: "bg-blue-soft", tekst: "text-blue" },
} as const;

/* De kleur van de bol met het stapnummer, in dezelfde volgorde als op de post. */
const stapKleur = ["bg-purple", "bg-orange", "bg-green-mid"];

export default async function MeetestenPagina() {
  return (
    <>
      <PaginaKop
        label={meetesten.label}
        titel={meetesten.titel}
        handgeschreven={meetesten.handgeschreven}
        tekst={meetesten.tekst}
      />

      {/* De twee groepen die we erbij zoeken. */}
      <Sectie className="py-8">
        <h2 className="text-2xl text-green">{meetesten.groepenTitel}</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-2">
          {meetesten.groepen.map((groep) => (
            <Kaart key={groep.naam} className="flex flex-col">
              <span
                aria-hidden
                className={`flex h-12 w-12 items-center justify-center rounded-full text-2xl ${groepKleur[groep.kleur].vlak}`}
              >
                {groep.icoon}
              </span>
              <p
                className={`mt-3 text-[14px] font-extrabold uppercase tracking-wider ${groepKleur[groep.kleur].tekst}`}
              >
                {groep.voorWie}
              </p>
              <h3 className="text-xl text-green">{groep.naam}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{groep.tekst}</p>
              <ul className="mt-3 grid gap-2">
                {groep.punten.map((punt) => (
                  <li
                    key={punt}
                    className="flex gap-2 text-[16px] text-ink"
                  >
                    <span aria-hidden className="text-green-mid">
                      ✓
                    </span>
                    <span>{punt}</span>
                  </li>
                ))}
              </ul>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* Hoe het testen verloopt. */}
      <Sectie className="py-0">
        <h2 className="text-2xl text-green">{meetesten.stappenTitel}</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          {meetesten.stappen.map((stap, i) => (
            <Kaart key={stap.titel}>
              <span
                aria-hidden
                className={`flex h-11 w-11 items-center justify-center rounded-full text-xl font-black text-cream ${stapKleur[i % stapKleur.length]}`}
              >
                {i + 1}
              </span>
              <h3 className="mt-3 text-xl text-green">{stap.titel}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{stap.tekst}</p>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* Wat een tester ervoor teruggeeft. */}
      <Sectie className="py-8">
        <div className="rounded-[20px] bg-purple-soft px-6 py-5">
          <h2 className="text-2xl text-purple">{meetesten.afspraakTitel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
            {meetesten.afspraakTekst}
          </p>
          <ul className="mt-3 grid gap-2">
            {meetesten.afspraak.map((punt) => (
              <li key={punt} className="flex gap-2 text-[16px] text-ink">
                <span aria-hidden className="text-purple">
                  ✓
                </span>
                <span>{punt}</span>
              </li>
            ))}
          </ul>
        </div>
      </Sectie>

      {/* Voor wie niet gekozen wordt: wat het anders kost. */}
      <Sectie className="py-8">
        <div className="rounded-[20px] bg-orange-soft px-6 py-5">
          <h2 className="text-2xl text-orange">{meetesten.prijzenTitel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
            {meetesten.prijzenTekst}
          </p>
          <ul className="mt-4 grid gap-3 sm:grid-cols-3">
            {meetesten.prijzen.map((prijs) => (
              <li key={prijs.titel}>
                <p className="text-[16px] font-extrabold text-green">
                  {prijs.titel}
                </p>
                <p className="text-[15px] text-ink-dim">{prijs.tekst}</p>
              </li>
            ))}
          </ul>
          <div className="mt-5 flex flex-wrap items-center gap-4">
            <Knop href={meetesten.prijzenKnop.link}>
              {meetesten.prijzenKnop.tekst}
            </Knop>
            <a
              href={meetesten.prijzenLink.link}
              className="text-[16px] font-extrabold text-green underline-offset-4 hover:underline"
            >
              {meetesten.prijzenLink.tekst} →
            </a>
          </div>
        </div>
      </Sectie>

      {/* Waarom het platform gemaakt is zoals het gemaakt is. */}
      <Sectie className="py-8">
        <div className="rounded-[20px] bg-sage-soft px-6 py-5">
          <h2 className="text-xl text-green">{meetesten.nuance.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
            {meetesten.nuance.tekst}
          </p>
        </div>
      </Sectie>

      {/* Het formulier. */}
      <Sectie className="grid gap-4 pb-16">
        <Kaart className="scroll-mt-24" id="opgeven">
          <h2 className="text-2xl text-green">{meetesten.formulierTitel}</h2>
          {meetesten.open ? (
            <>
              <p className="mt-2 max-w-[62ch] text-[16px] text-ink-dim">
                {meetesten.formulierTekst}
              </p>
              <p className="mt-3 rounded-[16px] bg-sage-soft px-4 py-3 text-[16px] font-bold text-green">
                {meetesten.formulierPlaatsen}
              </p>
              <div className="mt-6">
                <Aanvraagformulier
                  onderwerp={meetesten.onderwerp}
                  vragen={meetestenVelden}
                  privacy={meetesten.privacy}
                  verborgen={[
                    { naam: "Soort aanvraag", waarde: "Meetesten" },
                  ]}
                />
              </div>
            </>
          ) : (
            <p className="mt-2 text-[16px] text-ink-dim">
              {meetesten.gesloten}
            </p>
          )}
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">Liever eerst iets vragen?</h2>
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
