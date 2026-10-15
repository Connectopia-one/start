import type { Metadata } from "next";
import Link from "next/link";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { berichtenOpDatum, blogTekst, kaartfotoVan } from "@/content/blog";
import { datumInWoorden } from "@/lib/datum";

export const metadata: Metadata = {
  title: "Blog, tips en meer",
  description: blogTekst.tekst,
};

export default function BlogPagina() {
  return (
    <>
      <PaginaKop
        label={blogTekst.label}
        titel={blogTekst.titel}
        tekst={blogTekst.tekst}
      />

      <Sectie className="pb-16">
        {berichtenOpDatum.length === 0 ? (
          <p className="text-ink-dim">{blogTekst.leegTekst}</p>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2">
            {berichtenOpDatum.map((bericht) => {
              const foto = kaartfotoVan(bericht);
              return (
                <Link
                  key={bericht.slug}
                  href={`/blog/${bericht.slug}`}
                  className="block"
                >
                  <Kaart className="h-full overflow-hidden transition hover:-translate-y-1">
                    <div className="-mx-6 -mt-6 mb-5 aspect-[16/9] bg-sage-soft">
                      {foto ? (
                        // eslint-disable-next-line @next/next/no-img-element
                        <img
                          src={`/blog/${foto}`}
                          alt=""
                          loading="lazy"
                          className="h-full w-full object-cover"
                        />
                      ) : (
                        <div className="flex h-full items-center justify-center">
                          {/* eslint-disable-next-line @next/next/no-img-element */}
                          <img
                            src="/beeldmerk.png"
                            alt=""
                            className="h-1/2 w-auto opacity-80"
                          />
                        </div>
                      )}
                    </div>
                    <p className="text-[14px] font-bold text-sage">
                      {datumInWoorden(bericht.datum)} · {bericht.auteur}
                    </p>
                    <h2 className="mt-2 text-xl text-green">{bericht.titel}</h2>
                    <p className="mt-2 text-[16px] text-ink-dim">
                      {bericht.samenvatting}
                    </p>
                    {bericht.labels && bericht.labels.length > 0 ? (
                      <ul className="mt-3 flex flex-wrap gap-2">
                        {bericht.labels.map((label) => (
                          <li
                            key={label}
                            className="rounded-full bg-sage-soft px-3 py-0.5 text-[13.5px] font-bold text-green"
                          >
                            {label}
                          </li>
                        ))}
                      </ul>
                    ) : null}
                    <p className="mt-4 text-[15px] font-extrabold text-green">
                      Lees verder →
                    </p>
                  </Kaart>
                </Link>
              );
            })}
          </div>
        )}
      </Sectie>
    </>
  );
}
