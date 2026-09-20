import type { Metadata } from "next";
import Link from "next/link";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { berichtenOpDatum, blogTekst } from "@/content/blog";
import { datumInWoorden } from "@/lib/datum";

export const metadata: Metadata = {
  title: "Blog, tips en meer",
  description: blogTekst.tekst,
};

export default function BlogPagina() {
  return (
    <>
      <PaginaKop label={blogTekst.label} titel={blogTekst.titel} tekst={blogTekst.tekst} />

      <Sectie className="pb-16">
        {berichtenOpDatum.length === 0 ? (
          <p className="text-ink-dim">{blogTekst.leegTekst}</p>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2">
            {berichtenOpDatum.map((bericht) => (
              <Link key={bericht.slug} href={`/blog/${bericht.slug}`} className="block">
                <Kaart className="h-full transition hover:-translate-y-1">
                  <p className="text-[13px] font-bold text-sage">
                    {datumInWoorden(bericht.datum)} · {bericht.auteur}
                  </p>
                  <h2 className="mt-2 text-xl text-green">{bericht.titel}</h2>
                  <p className="mt-2 text-[15px] text-ink-dim">{bericht.samenvatting}</p>
                  {bericht.labels && bericht.labels.length > 0 ? (
                    <ul className="mt-3 flex flex-wrap gap-2">
                      {bericht.labels.map((label) => (
                        <li
                          key={label}
                          className="rounded-full bg-sage-soft px-3 py-0.5 text-[12.5px] font-bold text-green"
                        >
                          {label}
                        </li>
                      ))}
                    </ul>
                  ) : null}
                  <p className="mt-4 text-sm font-extrabold text-green">Lees verder →</p>
                </Kaart>
              </Link>
            ))}
          </div>
        )}
      </Sectie>
    </>
  );
}
