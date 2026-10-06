import type { Metadata } from "next";
import Link from "next/link";
import { Briefje } from "@/components/Briefje";
import { Briefjeformulier } from "@/components/Briefjeformulier";
import { PositieveToon } from "@/components/PositieveToon";
import { PaginaKop, Sectie, tekstKleur, vlakKleur } from "@/components/ui";
import type { Briefje as BriefjeType, Bord } from "@/content/prikbord";
import { borden, prikbord } from "@/content/prikbord";
import { haalAlleBriefjes, prikbordKlaar } from "@/lib/prikbord-db";

/*
  Het prikbord toont wat er nú op hangt, van alle borden door elkaar, dus
  geen opgeslagen versie.
*/
export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Prikbord voor ouders",
  description: prikbord.tekst,
};

type Melding = keyof typeof prikbord.meldingen;

/* Een briefje zonder datum hangt onderaan, niet bovenaan. */
function sorteersleutel(briefje: BriefjeType) {
  return briefje.datum ?? "0000-00-00";
}

export default async function PrikbordPagina({
  searchParams,
}: {
  searchParams: Promise<{ melding?: string; bord?: string }>;
}) {
  const { melding, bord: gefilterd } = await searchParams;

  /* Filteren gebeurt op de pagina zelf, met ?bord=... in het webadres. */
  const filter = borden.find((b) => b.slug === gefilterd) ?? null;

  const viaDatabank = prikbordKlaar();
  const opgehangen = viaDatabank ? await haalAlleBriefjes() : [];
  const bordVan = new Map<string, Bord>(borden.map((b) => [b.slug, b]));

  /*
    Alles wat er hangt, met het bord erbij: eerst de briefjes die bezoekers
    zelf ophingen, daarna onze eigen vaste briefjes. Samen gesorteerd op
    datum, zodat het nieuwste bovenaan de muur hangt.
  */
  const alles: {
    briefje: BriefjeType;
    bord: Bord;
    meldbaar?: { id: string; bord: string };
  }[] = [
    ...opgehangen.flatMap((rij) => {
      const bord = bordVan.get(rij.bord);
      if (!bord) return [];
      return [
        {
          briefje: {
            tekst: rij.tekst,
            van: rij.naam ?? undefined,
            datum: rij.created_at.slice(0, 10),
            wanneer: rij.wanneer ?? undefined,
          },
          bord,
          meldbaar: { id: rij.id, bord: bord.slug },
        },
      ];
    }),
    ...borden.flatMap((bord) =>
      bord.briefjes.map((briefje) => ({ briefje, bord }))
    ),
  ]
    .filter((rij) => !filter || rij.bord.slug === filter.slug)
    .sort((a, b) =>
      sorteersleutel(b.briefje).localeCompare(sorteersleutel(a.briefje))
    );

  const bericht =
    melding && melding in prikbord.meldingen
      ? prikbord.meldingen[melding as Melding]
      : null;
  const goedNieuws = melding === "opgehangen" || melding === "gemeld";

  return (
    <>
      <PaginaKop
        label={prikbord.label}
        titel={prikbord.titel}
        handgeschreven={prikbord.handgeschreven}
        tekst={prikbord.tekst}
      />

      {bericht ? (
        <Sectie className="py-4">
          <p
            className={`rounded-[14px] px-5 py-4 text-[16px] font-bold ${
              goedNieuws
                ? "bg-sage-soft text-green"
                : "bg-orange-soft text-orange"
            }`}
          >
            {bericht}
          </p>
        </Sectie>
      ) : null}

      {/* De knoppen die de muur hieronder filteren, zonder de pagina te verlaten */}
      <Sectie className="py-5">
        <ul className="flex flex-wrap gap-2">
          <li>
            <Link
              href="/prikbord"
              aria-current={filter ? undefined : "true"}
              className={`inline-block rounded-full px-4 py-2 text-[15px] font-bold ${
                filter
                  ? "border border-border bg-surface text-ink-dim hover:text-green"
                  : "bg-sage-soft text-green"
              }`}
            >
              {prikbord.muurAlles}
            </Link>
          </li>
          {borden.map((bord) => (
            <li key={bord.slug}>
              <Link
                href={`/prikbord?bord=${bord.slug}`}
                aria-current={filter?.slug === bord.slug ? "true" : undefined}
                className={`inline-block rounded-full px-4 py-2 text-[15px] font-bold ${
                  filter?.slug === bord.slug
                    ? `${vlakKleur[bord.kleur]} ${tekstKleur[bord.kleur]}`
                    : "border border-border bg-surface text-ink-dim hover:text-green"
                }`}
              >
                {bord.icoon} {bord.naam}
              </Link>
            </li>
          ))}
        </ul>
      </Sectie>

      <Sectie className="pt-0 pb-5">
        <PositieveToon klein />
      </Sectie>

      <Sectie className="pt-0 pb-10">
        <h2 className="text-2xl text-green">
          {filter ? filter.naam : prikbord.muurTitel}
        </h2>
        {filter ? (
          <p className="mt-1 max-w-[62ch] text-[16px] text-ink-dim">
            {filter.uitleg}
          </p>
        ) : null}
        {alles.length === 0 ? (
          <p className="font-hand mt-3 text-2xl text-orange">
            {prikbord.leegTekst}
          </p>
        ) : (
          /* Zoals op een echt prikbord: de briefjes vullen de kolommen op. */
          <div className="mt-4 rounded-[20px] border border-border bg-[#f1e8d7] p-5 pb-0 shadow-[inset_0_2px_8px_rgba(47,74,34,0.08)]">
            <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
              {alles.map((rij, nummer) => (
                <Briefje
                  key={rij.meldbaar?.id ?? `vast-${rij.bord.slug}-${nummer}`}
                  briefje={rij.briefje}
                  nummer={nummer}
                  meldbaar={rij.meldbaar}
                  categorie={{
                    slug: rij.bord.slug,
                    naam: rij.bord.naam,
                    icoon: rij.bord.icoon,
                  }}
                  terug="/prikbord"
                />
              ))}
            </div>
          </div>
        )}
      </Sectie>

      <Sectie className="pt-0 pb-10">
        <div
          id="ophangen"
          className="rounded-[20px] border border-border bg-surface p-7 shadow-[0_2px_10px_rgba(47,74,34,0.07)]"
        >
          <h2 className="text-2xl text-green">{prikbord.formulier.titel}</h2>
          <p className="mt-2 max-w-[58ch] text-[16px] text-ink-dim">
            {prikbord.formulier.tekst}
          </p>
          <div className="mt-6">
            <Briefjeformulier
              bord={filter?.slug ?? borden[0].slug}
              bordNaam={filter?.naam ?? borden[0].naam}
              viaDatabank={viaDatabank}
              keuze={borden.map((bord) => ({
                slug: bord.slug,
                naam: bord.naam,
                ondertitel: bord.uitleg,
              }))}
              terug="/prikbord"
            />
          </div>
        </div>
      </Sectie>

      <Sectie className="pt-0 pb-16">
        <div className="rounded-[20px] bg-sage-soft px-7 py-7">
          <h2 className="text-2xl text-green">{prikbord.spelregels.titel}</h2>
          <ul className="mt-4 grid gap-2.5 sm:grid-cols-2">
            {prikbord.spelregels.punten.map((punt) => (
              <li key={punt} className="text-[16px] text-ink">
                {punt}
              </li>
            ))}
          </ul>
          <ul className="mt-6 grid gap-2 sm:grid-cols-2">
            {borden.map((bord) => (
              <li key={bord.slug} className="text-[15px] text-ink">
                <Link
                  href={`/prikbord?bord=${bord.slug}`}
                  className={`mr-2 inline-block rounded-full px-3 py-1 text-[14px] font-bold ${vlakKleur[bord.kleur]} ${tekstKleur[bord.kleur]}`}
                >
                  {bord.icoon} {bord.naam}
                </Link>
                <span className="text-ink-dim">{bord.ondertitel}</span>
              </li>
            ))}
          </ul>
        </div>
      </Sectie>
    </>
  );
}
