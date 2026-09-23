import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Briefje } from "@/components/Briefje";
import { Briefjeformulier } from "@/components/Briefjeformulier";
import { PositieveToon } from "@/components/PositieveToon";
import { Icoon, Sectie, tekstKleur, vlakKleur } from "@/components/ui";
import type { Briefje as BriefjeType } from "@/content/prikbord";
import { borden, prikbord } from "@/content/prikbord";
import { haalBriefjes, prikbordKlaar } from "@/lib/prikbord-db";

/* Een bord toont wat er nú op hangt, dus geen opgeslagen versie. */
export const dynamic = "force-dynamic";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const bord = borden.find((b) => b.slug === slug);
  if (!bord) return {};
  return { title: `${bord.naam} · Prikbord`, description: bord.uitleg };
}

type Melding = keyof typeof prikbord.meldingen;

export default async function BordPagina({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ melding?: string }>;
}) {
  const { slug } = await params;
  const { melding } = await searchParams;
  const bord = borden.find((b) => b.slug === slug);
  if (!bord) notFound();

  const viaDatabank = prikbordKlaar();
  const opgehangen = viaDatabank ? await haalBriefjes(bord.slug) : [];

  /* Eerst wat bezoekers ophingen, daarna onze eigen vaste briefjes. */
  const briefjes: {
    briefje: BriefjeType;
    meldbaar?: { id: string; bord: string };
  }[] = [
    ...opgehangen.map((rij) => ({
      briefje: {
        tekst: rij.tekst,
        van: rij.naam ?? undefined,
        datum: rij.created_at.slice(0, 10),
        wanneer: rij.wanneer ?? undefined,
      },
      meldbaar: { id: rij.id, bord: bord.slug },
    })),
    ...bord.briefjes.map((briefje) => ({ briefje })),
  ];

  const bericht =
    melding && melding in prikbord.meldingen
      ? prikbord.meldingen[melding as Melding]
      : null;
  const goedNieuws = melding === "opgehangen" || melding === "gemeld";

  return (
    <>
      <header className="mx-auto w-full max-w-5xl px-5 pt-10 pb-2">
        <Link
          href="/prikbord"
          className="text-[15px] font-bold text-green underline-offset-4 hover:underline"
        >
          ← Alle borden
        </Link>

        <div className="mt-5 flex items-start gap-4">
          <Icoon kleur={bord.kleur}>{bord.icoon}</Icoon>
          <div>
            <h1 className={`text-3xl ${tekstKleur[bord.kleur]} sm:text-4xl`}>
              {bord.naam}
            </h1>
            <p className="text-[16px] text-ink-dim">{bord.ondertitel}</p>
          </div>
        </div>

        <p className="mt-4 max-w-[62ch] text-ink-dim">{bord.uitleg}</p>
      </header>

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

      {/* De andere borden, om snel te wisselen */}
      <Sectie className="py-5">
        <ul className="flex flex-wrap gap-2">
          {borden.map((ander) => (
            <li key={ander.slug}>
              <Link
                href={`/prikbord/${ander.slug}`}
                className={`inline-block rounded-full px-4 py-2 text-[15px] font-bold ${
                  ander.slug === bord.slug
                    ? `${vlakKleur[ander.kleur]} ${tekstKleur[ander.kleur]}`
                    : "border border-border bg-surface text-ink-dim hover:text-green"
                }`}
              >
                {ander.icoon} {ander.naam}
              </Link>
            </li>
          ))}
        </ul>
      </Sectie>

      <Sectie className="pt-0 pb-5">
        <PositieveToon klein />
      </Sectie>

      <Sectie className="pt-0 pb-10">
        {briefjes.length === 0 ? (
          <p className="font-hand text-2xl text-orange">{prikbord.leegTekst}</p>
        ) : (
          /* Zoals op een echt prikbord: de briefjes vullen de kolommen op. */
          <div className="rounded-[20px] border border-border bg-[#f1e8d7] p-5 pb-0 shadow-[inset_0_2px_8px_rgba(47,74,34,0.08)]">
            <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
              {briefjes.map((rij, nummer) => (
                <Briefje
                  key={rij.meldbaar?.id ?? `vast-${nummer}`}
                  briefje={rij.briefje}
                  nummer={nummer}
                  meldbaar={rij.meldbaar}
                />
              ))}
            </div>
          </div>
        )}
      </Sectie>

      <Sectie className="pt-0 pb-16">
        <div className="rounded-[20px] border border-border bg-surface p-7 shadow-[0_2px_10px_rgba(47,74,34,0.07)]">
          <h2 className="text-2xl text-green">{prikbord.formulier.titel}</h2>
          <p className="mt-2 max-w-[58ch] text-[16px] text-ink-dim">
            {prikbord.formulier.tekst}
          </p>
          <div className="mt-6">
            <Briefjeformulier
              bord={bord.slug}
              bordNaam={bord.naam}
              metWanneer={bord.slug === "samenkomen"}
              viaDatabank={viaDatabank}
            />
          </div>
        </div>
      </Sectie>
    </>
  );
}
