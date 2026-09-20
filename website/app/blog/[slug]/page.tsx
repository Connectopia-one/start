import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Blok } from "@/content/blog";
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

function BlokWeergave({ blok }: { blok: Blok }) {
  switch (blok.soort) {
    case "kop":
      return <h2 className="mt-4 text-2xl text-green">{blok.tekst}</h2>;

    case "tekst":
      return <p className="text-[17px] text-ink-dim">{blok.tekst}</p>;

    case "citaat":
      return (
        <blockquote className="font-hand my-2 rounded-[20px] bg-sage-soft px-7 py-6 text-center text-2xl text-green">
          {blok.tekst}
        </blockquote>
      );

    case "lijst":
      return (
        <ul className="grid gap-3">
          {blok.punten.map((punt) => (
            <li
              key={punt.tekst.slice(0, 32)}
              className="rounded-2xl border-l-4 border-orange bg-orange-soft/40 px-5 py-4"
            >
              {punt.titel ? (
                <strong className="block font-extrabold text-orange">{punt.titel}</strong>
              ) : null}
              <span className="text-[16px] text-ink">{punt.tekst}</span>
            </li>
          ))}
        </ul>
      );

    case "afbeelding": {
      const plaatje = (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={`/blog/${blok.bestand}`}
          alt={blok.beschrijving}
          className="w-full rounded-2xl"
        />
      );
      return (
        <figure className={`my-2 w-full ${blok.klein ? "mx-auto max-w-sm" : ""}`}>
          {blok.link ? (
            <a
              href={blok.link}
              target="_blank"
              rel="noopener noreferrer"
              className="block transition hover:-translate-y-0.5"
            >
              {plaatje}
            </a>
          ) : (
            plaatje
          )}
          {blok.bijschrift ? (
            <figcaption className="mt-2 text-[13px] text-ink-dim">{blok.bijschrift}</figcaption>
          ) : null}
        </figure>
      );
    }

    case "knop":
      return (
        <p>
          <a
            href={blok.link}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block rounded-full bg-green px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {blok.tekst} →
          </a>
        </p>
      );
  }
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
        <Link
          href="/blog"
          className="text-sm font-extrabold text-sage underline-offset-4 hover:underline"
        >
          ← Terug naar de blog
        </Link>
        <p className="mt-4 text-[13px] font-bold text-sage">
          {datumInWoorden(bericht.datum)} · {bericht.auteur}
        </p>
        <h1 className="mt-2 text-3xl text-green sm:text-4xl">{bericht.titel}</h1>
        {bericht.labels && bericht.labels.length > 0 ? (
          <ul className="mt-4 flex flex-wrap gap-2">
            {bericht.labels.map((label) => (
              <li
                key={label}
                className="rounded-full bg-sage-soft px-3.5 py-1 text-[13px] font-bold text-green"
              >
                {label}
              </li>
            ))}
          </ul>
        ) : null}
      </header>

      <div className="mx-auto grid w-full max-w-3xl gap-4 px-5 py-10 pb-16">
        {bericht.blokken.map((blok, i) => (
          <BlokWeergave key={i} blok={blok} />
        ))}
      </div>
    </article>
  );
}
