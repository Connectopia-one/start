import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Kaart, Label, PaginaKop, Sectie } from "@/components/ui";
import { trajecten } from "@/content/aanbod";
import type { SoortSleutel } from "@/content/formulier";
import { formulierTekst, soorten, velden, verzenden } from "@/content/formulier";
import { site } from "@/content/site";

const soortSleutels = Object.keys(soorten) as SoortSleutel[];

/*
  Voor elke soort aanvraag en elk traject bestaat er een eigen adres, zodat de
  knop waarop een ouder klikt meteen het juiste formulier opent. Zonder dat er
  iets moet worden aangeklikt, en zonder dat er scripts aan te pas komen.
*/
export function generateStaticParams() {
  const paden: { slug: string }[] = soortSleutels.map((soort) => ({ slug: soort }));
  for (const soort of soortSleutels) {
    for (const traject of trajecten) {
      paden.push({ slug: `${soort}-${traject.slug}` });
    }
  }
  return paden;
}

function leesSlug(slug: string) {
  for (const soort of soortSleutels) {
    if (slug === soort) return { soort, traject: undefined };
    if (slug.startsWith(`${soort}-`)) {
      const trajectSlug = slug.slice(soort.length + 1);
      const traject = trajecten.find((t) => t.slug === trajectSlug);
      if (traject) return { soort, traject };
    }
  }
  return null;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const gelezen = leesSlug(slug);
  if (!gelezen) return { title: "Aanvraag" };
  const { soort, traject } = gelezen;
  return {
    title: traject ? `${soorten[soort].titel} — ${traject.naam}` : soorten[soort].titel,
    description: soorten[soort].tekst,
  };
}

export default async function AanvraagPagina({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const gelezen = leesSlug(slug);
  if (!gelezen) notFound();

  const { soort, traject } = gelezen;
  const tekst = soorten[soort];
  const onderwerp = traject ? `${tekst.onderwerp} — ${traject.naam}` : tekst.onderwerp;

  /*
    Zolang er geen formulierdienst is ingesteld, opent het formulier het
    mailprogramma van de ouder met alle antwoorden er al in.
  */
  const perMail = !verzenden.webadres;
  const actie = perMail
    ? `mailto:${verzenden.mailnaar}?subject=${encodeURIComponent(onderwerp)}`
    : verzenden.webadres!;

  return (
    <>
      <PaginaKop
        label={tekst.label}
        titel={traject ? `${tekst.titel} voor ${traject.naam}` : tekst.titel}
        tekst={tekst.tekst}
      />

      <Sectie className="grid gap-4 py-8">
        <Kaart>
          <form
            action={actie}
            method="post"
            encType={perMail ? "text/plain" : undefined}
            className="grid gap-5"
          >
            {/* Waar de aanvraag over gaat, zodat het in de mail meekomt. */}
            <div className="rounded-[16px] bg-sage-soft px-5 py-4">
              <Label>{formulierTekst.trajectVraag}</Label>
              <p className="mt-1 text-[17px] font-extrabold text-green">
                {traject ? traject.naam : formulierTekst.geenTraject}
              </p>
              <p className="text-[14px] text-ink-dim">{tekst.titel}</p>
              <input
                type="hidden"
                name="Aanbod"
                value={traject ? traject.naam : formulierTekst.geenTraject}
              />
              <input type="hidden" name="Soort aanvraag" value={tekst.titel} />
            </div>

            <div className="grid gap-5 sm:grid-cols-2">
              {velden.map((veld) => {
                const lang = veld.soort === "lang";
                const type =
                  veld.soort === "email" ? "email" : veld.soort === "telefoon" ? "tel" : "text";
                return (
                  <div key={veld.naam} className={lang ? "sm:col-span-2" : undefined}>
                    <label className="block">
                      <span className="text-[14px] font-bold text-ink">
                        {veld.label}
                        {veld.verplicht ? (
                          <span className="text-orange" aria-hidden>
                            {" "}
                            *
                          </span>
                        ) : null}
                      </span>
                      {lang ? (
                        <textarea
                          name={veld.naam}
                          rows={4}
                          required={veld.verplicht}
                          className="mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[15px] text-ink outline-none focus:border-green"
                        />
                      ) : (
                        <input
                          type={type}
                          name={veld.naam}
                          required={veld.verplicht}
                          autoComplete={
                            veld.soort === "email" ? "email" : veld.soort === "telefoon" ? "tel" : undefined
                          }
                          className="mt-1.5 block h-11 w-full rounded-full border border-border bg-cream px-4 text-[15px] text-ink outline-none focus:border-green"
                        />
                      )}
                    </label>
                    {veld.hulp ? (
                      <p className="mt-1 text-[13px] text-ink-dim">{veld.hulp}</p>
                    ) : null}
                  </div>
                );
              })}
            </div>

            {/* Wat er met de gegevens gebeurt. */}
            <div className="rounded-[16px] bg-purple-soft px-5 py-4">
              <p className="text-[14px] text-ink">{formulierTekst.privacy}</p>
              <label className="mt-3 flex items-start gap-2.5 text-[14px] font-bold text-ink">
                <input
                  type="checkbox"
                  name="Akkoord met het gebruik van de gegevens"
                  value="ja"
                  required
                  className="mt-0.5 h-[18px] w-[18px] shrink-0 accent-green"
                />
                {formulierTekst.akkoordTekst}
                <span className="text-orange" aria-hidden>
                  *
                </span>
              </label>
            </div>

            <div className="flex flex-wrap items-center gap-4">
              <button
                type="submit"
                className="rounded-full bg-green px-7 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
              >
                {formulierTekst.verstuurKnop} →
              </button>
              <Link
                href={formulierTekst.terugLink}
                className="text-[14px] font-bold text-green underline-offset-4 hover:underline"
              >
                {formulierTekst.terug}
              </Link>
            </div>

            {perMail ? (
              <p className="text-[13px] text-ink-dim">{formulierTekst.naVersturen}</p>
            ) : null}
          </form>
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">{formulierTekst.liever}</h2>
          <p className="mt-2 text-[15px] text-ink-dim">
            Mail ons op{" "}
            <a
              href={`mailto:${site.email}`}
              className="font-bold text-green underline-offset-4 hover:underline"
            >
              {site.email}
            </a>
            . We antwoorden zo snel als we kunnen.
          </p>
        </Kaart>
      </Sectie>
    </>
  );
}
