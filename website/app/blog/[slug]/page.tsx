import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { berichten } from "@/content/blog";
import { datumInWoorden } from "@/lib/datum";

export function generateStaticParams() {
  return berichten.map((bericht) => ({ slug: bericht.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const bericht = berichten.find((b) => b.slug === slug);
  if (!bericht) return {};
  return { title: bericht.titel, description: bericht.samenvatting };
}

export default async function BerichtPagina({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const bericht = berichten.find((b) => b.slug === slug);
  if (!bericht) notFound();

  return (
    <article>
      <header className="mx-auto w-full max-w-3xl px-5 pt-14">
        <Link href="/blog" className="text-sm font-extrabold text-sage underline-offset-4 hover:underline">
          ← Terug naar de blog
        </Link>
        <p className="mt-4 text-[13px] font-bold text-sage">
          {datumInWoorden(bericht.datum)} · {bericht.auteur}
        </p>
        <h1 className="mt-2 text-3xl text-green sm:text-4xl">{bericht.titel}</h1>
      </header>

      <div className="mx-auto w-full max-w-3xl px-5 py-10 pb-16">
        <div className="grid gap-4 text-[17px] text-ink-dim">
          {bericht.tekst.map((alinea) => (
            <p key={alinea.slice(0, 24)}>{alinea}</p>
          ))}
        </div>
      </div>
    </article>
  );
}
