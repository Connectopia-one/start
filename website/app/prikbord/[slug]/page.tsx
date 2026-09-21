import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Briefje } from "@/components/Briefje";
import { Briefjeformulier } from "@/components/Briefjeformulier";
import { Icoon, Sectie, tekstKleur, vlakKleur } from "@/components/ui";
import { borden, prikbord } from "@/content/prikbord";

export function generateStaticParams() {
  return borden.map((bord) => ({ slug: bord.slug }));
}

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

export default async function BordPagina({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const bord = borden.find((b) => b.slug === slug);
  if (!bord) notFound();

  return (
    <>
      <header className="mx-auto w-full max-w-5xl px-5 pt-10 pb-2">
        <Link
          href="/prikbord"
          className="text-sm font-bold text-green underline-offset-4 hover:underline"
        >
          ← Alle borden
        </Link>

        <div className="mt-5 flex items-start gap-4">
          <Icoon kleur={bord.kleur}>{bord.icoon}</Icoon>
          <div>
            <h1 className={`text-3xl ${tekstKleur[bord.kleur]} sm:text-4xl`}>
              {bord.naam}
            </h1>
            <p className="text-[15px] text-ink-dim">{bord.ondertitel}</p>
          </div>
        </div>

        <p className="mt-4 max-w-[62ch] text-ink-dim">{bord.uitleg}</p>
      </header>

      {/* De andere borden, om snel te wisselen */}
      <Sectie className="py-5">
        <ul className="flex flex-wrap gap-2">
          {borden.map((ander) => (
            <li key={ander.slug}>
              <Link
                href={`/prikbord/${ander.slug}`}
                className={`inline-block rounded-full px-4 py-2 text-[14px] font-bold ${
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

      <Sectie className="pt-0 pb-10">
        {bord.briefjes.length === 0 ? (
          <p className="font-hand text-2xl text-orange">{prikbord.leegTekst}</p>
        ) : (
          /* Zoals op een echt prikbord: de briefjes vullen de kolommen op. */
          <div className="rounded-[20px] border border-border bg-[#f1e8d7] p-5 pb-0 shadow-[inset_0_2px_8px_rgba(47,74,34,0.08)]">
            <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
              {bord.briefjes.map((briefje, nummer) => (
                <Briefje
                  key={`${briefje.tekst}-${nummer}`}
                  briefje={briefje}
                  nummer={nummer}
                />
              ))}
            </div>
          </div>
        )}
      </Sectie>

      <Sectie className="pt-0 pb-16">
        <div className="rounded-[20px] border border-border bg-surface p-7 shadow-[0_2px_10px_rgba(47,74,34,0.07)]">
          <h2 className="text-2xl text-green">{prikbord.formulier.titel}</h2>
          <p className="mt-2 max-w-[58ch] text-[15px] text-ink-dim">
            {prikbord.formulier.tekst}
          </p>
          <div className="mt-6">
            <Briefjeformulier bord={bord.naam} />
          </div>
        </div>
      </Sectie>
    </>
  );
}
