import type { Metadata } from "next";
import Link from "next/link";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { gidsTekst, organisaties } from "@/content/gids";

export const metadata: Metadata = {
  title: "Waar kan je terecht",
  description: gidsTekst.tekst,
};

export default function GidsPagina() {
  const categorieen = [...new Set(organisaties.map((o) => o.categorie))];

  return (
    <>
      <PaginaKop label={gidsTekst.label} titel={gidsTekst.titel} tekst={gidsTekst.tekst} />

      <Sectie className="grid gap-8 pb-8">
        {categorieen.length === 0 ? (
          <p className="text-ink-dim">{gidsTekst.leegTekst}</p>
        ) : (
          categorieen.map((categorie) => (
            <div key={categorie}>
              <h2 className="text-2xl text-green">{categorie}</h2>
              <div className="mt-4 grid gap-4 sm:grid-cols-2">
                {organisaties
                  .filter((o) => o.categorie === categorie)
                  .map((organisatie) => (
                    <Kaart key={organisatie.naam}>
                      <div className="flex items-start justify-between gap-3">
                        <h3 className="text-xl text-green">{organisatie.naam}</h3>
                        {organisatie.regio ? (
                          <span className="rounded-full bg-sage-soft px-3 py-1 text-[12px] font-extrabold text-green">
                            {organisatie.regio}
                          </span>
                        ) : null}
                      </div>
                      {organisatie.omschrijving ? (
                        <p className="mt-2 text-[15px] text-ink-dim">
                          {organisatie.omschrijving}
                        </p>
                      ) : (
                        <p className="mt-2 text-[15px] text-ink-dim italic">
                          {gidsTekst.nogGeenOmschrijving}
                        </p>
                      )}
                      {organisatie.link ? (
                        <a
                          href={organisatie.link}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="mt-3 inline-block text-sm font-extrabold text-green underline-offset-4 hover:underline"
                        >
                          Naar hun website →
                        </a>
                      ) : null}
                    </Kaart>
                  ))}
              </div>
            </div>
          ))
        )}
      </Sectie>

      <Sectie className="pb-16">
        <div className="rounded-[20px] bg-purple-soft px-7 py-7">
          <p className="max-w-[60ch] text-ink">{gidsTekst.nota}</p>
          <Link
            href={gidsTekst.oproepLink}
            className="mt-5 inline-block rounded-full bg-purple px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {gidsTekst.oproepTekst} →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
