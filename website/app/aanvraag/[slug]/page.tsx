import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Aanvraagformulier } from "@/components/Aanvraagformulier";
import { Kaart, Label, PaginaKop, Sectie } from "@/components/ui";
import { trajecten } from "@/content/aanbod";
import type { SoortSleutel } from "@/content/formulier";
import { formulierTekst, soorten } from "@/content/formulier";
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


  return (
    <>
      <PaginaKop
        label={tekst.label}
        titel={traject ? `${tekst.titel} voor ${traject.naam}` : tekst.titel}
        tekst={tekst.tekst}
      />

      <Sectie className="grid gap-4 py-8">
        <Kaart>
          <Aanvraagformulier
            onderwerp={onderwerp}
            verborgen={[
              {
                naam: "Aanbod",
                waarde: traject ? traject.naam : formulierTekst.geenTraject.inMail,
              },
              { naam: "Soort aanvraag", waarde: tekst.titel },
            ]}
            kop={
              <div className="rounded-[16px] bg-sage-soft px-5 py-4">
                <Label>
                  {traject ? formulierTekst.trajectVraag : formulierTekst.geenTraject.label}
                </Label>
                <p className="mt-1 text-[17px] font-extrabold text-green">
                  {traject ? traject.naam : formulierTekst.geenTraject.titel}
                </p>
                <p className="text-[14px] text-ink-dim">
                  {traject ? tekst.titel : tekst.zonderAanbod}
                </p>
              </div>
            }
          />
          <Link
            href={formulierTekst.terugLink}
            className="mt-5 inline-block text-[14px] font-bold text-green underline-offset-4 hover:underline"
          >
            {formulierTekst.terug}
          </Link>
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
