import type { Metadata } from "next";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { site } from "@/content/site";
import { steun, steunVelden } from "@/content/steun";
import { sponsorsPerSoort } from "@/content/sponsors";

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

      {/* De verlanglijst, enkel als er een link is ingevuld. */}
      {steun.verlanglijst.link ? (
        <Sectie className="py-4">
          <div className="rounded-[20px] bg-purple-soft px-6 py-5">
            <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
              <div>
                <span className="text-[14px] font-bold text-purple">
                  {steun.verlanglijst.label}
                </span>
                <h2 className="mt-1 text-2xl text-green">
                  {steun.verlanglijst.titel}
                </h2>
                <p className="mt-2 max-w-[60ch] text-[16px] text-ink">
                  {steun.verlanglijst.tekst}
                </p>
              </div>
              <div className="shrink-0">
                <a
                  href={steun.verlanglijst.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block rounded-full bg-purple px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
                >
                  🎁 {steun.verlanglijst.knop} →
                </a>
                <p className="mt-1.5 text-[13.5px] text-ink-dim">
                  {steun.verlanglijst.noot}
                </p>
              </div>
            </div>
          </div>
        </Sectie>
      ) : null}

      {/* Wat er met je steun gebeurt, in echte foto's uit de werking. */}
      <Sectie className="py-4">
        <ul className="grid grid-cols-3 gap-3 sm:gap-4">
          {[
            {
              bestand: "het-knutselmagazijn.jpg",
              beschrijving:
                "Rekken vol doorzichtige bakken met knutselmateriaal, elk met een etiket.",
              bijschrift:
                "Ons knutselmagazijn: alles in een bak, met een etiket erop.",
            },
            {
              bestand: "bruggen-van-karton.jpg",
              beschrijving: "Drie kinderen bouwen bruggen van karton.",
              bijschrift: "Bruggen bouwen met karton, kokers en bekers.",
            },
            {
              bestand: "flessenraket-vullen.jpg",
              beschrijving:
                "Kinderen en een begeleider vullen een zelfgemaakte flessenraket.",
              bijschrift: "Een flessenraket vullen, met veel geduld.",
            },
          ].map((foto) => (
            <li key={foto.bestand}>
              <figure>
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={`/kijkje/${foto.bestand}`}
                  alt={foto.beschrijving}
                  loading="lazy"
                  className="aspect-square w-full rounded-2xl object-cover"
                />
                <figcaption className="mt-1.5 text-[12.5px] leading-snug text-ink-dim sm:text-[14px]">
                  {foto.bijschrift}
                </figcaption>
              </figure>
            </li>
          ))}
        </ul>
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
          <div className="mt-5 border-t border-border pt-4">
            <p className="text-[16px] font-extrabold text-green">
              {steun.bedrijven.voorgangers}
            </p>
            {[
              {
                kop: steun.bedrijven.kopSponsors,
                lijst: sponsorsPerSoort("sponsor"),
              },
              {
                kop: steun.bedrijven.kopPartners,
                lijst: sponsorsPerSoort("partner"),
              },
            ].map((groep) => (
              <div key={groep.kop} className="mt-3">
                <p className="text-[14px] font-bold text-ink-dim">
                  {groep.kop}
                </p>
                <ul className="mt-2 grid grid-cols-2 gap-3 sm:flex sm:flex-wrap sm:items-center">
                  {groep.lijst.map((sponsor) => {
                    const logo = sponsor.logo ? (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img
                        src={`/sponsors/${sponsor.logo}`}
                        alt={sponsor.naam}
                        className="max-h-full w-auto max-w-full object-contain"
                      />
                    ) : (
                      <span className="text-center text-[14px] font-extrabold text-green">
                        {sponsor.naam}
                      </span>
                    );
                    const vak =
                      "flex h-20 w-full items-center justify-center rounded-xl border border-border bg-white p-2.5 sm:w-40";
                    return (
                      <li key={sponsor.naam}>
                        {sponsor.link ? (
                          <a
                            href={sponsor.link}
                            target="_blank"
                            rel="noopener noreferrer"
                            className={`${vak} transition hover:-translate-y-0.5`}
                          >
                            {logo}
                          </a>
                        ) : (
                          <div className={vak}>{logo}</div>
                        )}
                      </li>
                    );
                  })}
                </ul>
              </div>
            ))}
            <a
              href="#aanbod"
              className="mt-5 inline-block rounded-full bg-purple px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
            >
              {steun.bedrijven.knop} →
            </a>
          </div>
        </div>
      </Sectie>

      {/* Voor iedereen: vele beetjes maken een groot geheel. */}
      <Sectie className="py-4">
        <div className="rounded-[20px] border border-border bg-surface px-6 py-6">
          <div className="grid gap-6 md:grid-cols-[1fr_minmax(0,300px)] md:items-center">
            <div>
              <span className="text-[14px] font-bold text-orange">
                {steun.particulier.label}
              </span>
              <h2 className="mt-1 text-2xl text-green">
                {steun.particulier.titel}
              </h2>
              <p className="font-hand mt-1 text-2xl text-orange">
                {steun.particulier.handgeschreven}
              </p>
              <p className="mt-2 max-w-[60ch] text-[16px] text-ink-dim">
                {steun.particulier.tekst}
              </p>
              <a
                href="#aanbod"
                className="mt-4 inline-block rounded-full bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
              >
                {steun.particulier.knop} →
              </a>
            </div>
            <div className="rounded-2xl bg-orange-soft px-5 py-5 text-center">
              <p className="text-3xl" aria-hidden="true">
                💛
              </p>
              {steun.rekening ? (
                <>
                  <p className="mt-2 text-[15px] font-bold text-ink-dim">
                    Een gift doe je op
                  </p>
                  <p className="mt-1 select-all text-xl font-extrabold tracking-wide text-green">
                    {steun.rekening}
                  </p>
                  <p className="mt-1 text-[15px] text-ink-dim">
                    op naam van Connectopia vzw
                  </p>
                </>
              ) : (
                <p className="mt-2 text-[15px] font-bold text-green">
                  Wil je een gift doen? Vul hieronder het formulier in of bel
                  ons, dan bezorgen we je onze gegevens.
                </p>
              )}
            </div>
          </div>
          <p className="mt-5 border-t border-border pt-3 text-[13.5px] text-ink-dim">
            {steun.particulier.attest}
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
          <h2 className="text-xl text-green">
            Liever gewoon bellen of mailen?
          </h2>
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
