import type { Metadata } from "next";
import Link from "next/link";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { site } from "@/content/site";
import { winactie, winactieVelden } from "@/content/winactie";

export const metadata: Metadata = {
  title: winactie.titel,
  description: winactie.tekst,
};

/* De kleur van elke stap en elk niveau, in dezelfde volgorde als op de post. */
const stapKleur = ["bg-purple", "bg-orange", "bg-green-mid"];
const niveauKleur = [
  { vlak: "bg-sage-soft", tekst: "text-green-mid" },
  { vlak: "bg-purple-soft", tekst: "text-purple" },
];

export default async function WinactiePagina() {
  return (
    <>
      <PaginaKop
        label={winactie.label}
        titel={winactie.titel}
        handgeschreven={winactie.handgeschreven}
        tekst={winactie.tekst}
      />

      {/* De drie stappen. */}
      <Sectie className="py-8">
        <h2 className="text-2xl text-green">{winactie.stappenTitel}</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          {winactie.stappen.map((stap, i) => (
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

      {/* Welke niveaus er te testen zijn. */}
      <Sectie className="py-0">
        <h2 className="text-2xl text-green">{winactie.niveausTitel}</h2>
        <div className="mt-4 grid gap-4 sm:grid-cols-2">
          {winactie.niveaus.map((niveau, i) => (
            <Kaart key={niveau.naam} className="flex items-center gap-4">
              <span
                aria-hidden
                className={`flex h-14 w-14 shrink-0 items-center justify-center rounded-full text-3xl ${niveauKleur[i % niveauKleur.length].vlak}`}
              >
                {niveau.icoon}
              </span>
              <div>
                <p
                  className={`text-[14px] font-extrabold uppercase tracking-wider ${niveauKleur[i % niveauKleur.length].tekst}`}
                >
                  {niveau.naam}
                </p>
                <p className="text-xl font-extrabold text-green">
                  {niveau.voorWie}
                </p>
              </div>
            </Kaart>
          ))}
        </div>
      </Sectie>

      {/* Het inschrijfformulier. */}
      <Sectie className="grid gap-4 pb-16">
        <Kaart className="scroll-mt-24" id="inschrijven">
          <h2 className="text-2xl text-green">{winactie.formulierTitel}</h2>
          {winactie.open ? (
            <>
              <p className="mt-2 max-w-[62ch] text-[16px] text-ink-dim">
                {winactie.plaatsenTekst}
              </p>
              <div className="mt-6">
                <Aanvraagformulier
                  onderwerp={winactie.onderwerp}
                  vragen={winactieVelden}
                  verborgen={[
                    {
                      naam: "Soort aanvraag",
                      waarde: "Winactie oefenplatform",
                    },
                  ]}
                />
              </div>
            </>
          ) : (
            <p className="mt-2 text-[16px] text-ink-dim">{winactie.gesloten}</p>
          )}
        </Kaart>

        <Kaart>
          <h2 className="text-2xl text-green">{winactie.verderTitel}</h2>
          <p className="mt-2 text-[16px] text-ink-dim">{winactie.verderTekst}</p>
          <div className="mt-4 grid gap-4 md:grid-cols-3">
            {winactie.verder.map((stuk) => (
              <div
                key={stuk.link}
                className="flex flex-col rounded-[20px] border border-border bg-cream p-5"
              >
                <h3 className="text-xl text-green">{stuk.titel}</h3>
                <p className="mt-2 grow text-[16px] text-ink-dim">{stuk.tekst}</p>
                <Link
                  href={stuk.link}
                  className="mt-4 inline-block self-start rounded-full bg-green px-5 py-2 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
                >
                  {stuk.knop} &rarr;
                </Link>
              </div>
            ))}
          </div>
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">Nog een vraag?</h2>
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
