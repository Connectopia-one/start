import type { Metadata } from "next";
import Link from "next/link";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import {
  gidsTekst,
  organisaties,
  organisatiesPerCategorie,
  type Organisatie,
} from "@/content/gids";

export const metadata: Metadata = {
  title: "Waar kan je terecht",
  description: gidsTekst.tekst,
};

export default function GidsPagina() {
  const categorieen = [...new Set(organisaties.map((o) => o.categorie))];

  return (
    <>
      <PaginaKop
        label={gidsTekst.label}
        titel={gidsTekst.titel}
        tekst={gidsTekst.tekst}
      />

      <Sectie className="py-6">
        <p className="rounded-[20px] bg-sage-soft px-6 py-5 text-[16px] text-ink">
          {gidsTekst.geenVoorkeur}
        </p>
      </Sectie>

      <Sectie className="grid gap-8 pt-0 pb-8">
        {categorieen.length === 0 ? (
          <p className="text-ink-dim">{gidsTekst.leegTekst}</p>
        ) : (
          categorieen.map((categorie) => {
            const lijst = organisatiesPerCategorie(categorie);
            /*
              Staat er in deze groep niemand met een logo, dan laten we de
              logobalk helemaal weg. Zo komt er geen lege strook te staan.
            */
            const metLogo = lijst.some((o) => o.logo);
            return (
            <div key={categorie}>
              <h2 className="text-2xl text-green">{categorie}</h2>
              <div className="mt-4 grid gap-4 sm:grid-cols-2">
                {lijst.map((organisatie) => (
                  <Kaart key={organisatie.naam}>
                    {metLogo ? <LogoBalk organisatie={organisatie} /> : null}
                    <div
                      className={`flex items-start justify-between gap-3 ${
                        metLogo ? "mt-4" : ""
                      }`}
                    >
                      <h3 className="text-xl text-green">{organisatie.naam}</h3>
                      {organisatie.regio ? (
                        <span className="rounded-full bg-sage-soft px-3 py-1 text-[13px] font-extrabold text-green">
                          {organisatie.regio}
                        </span>
                      ) : null}
                    </div>
                    {organisatie.omschrijving ? (
                      <p className="mt-2 text-[16px] text-ink-dim">
                        {organisatie.omschrijving}
                      </p>
                    ) : (
                      <p className="mt-2 text-[16px] text-ink-dim">
                        {gidsTekst.nogGeenOmschrijving}
                      </p>
                    )}
                    {organisatie.link ? (
                      <a
                        href={organisatie.link}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="mt-3 inline-block text-[15px] font-extrabold text-green underline-offset-4 hover:underline"
                      >
                        {organisatie.linkTekst ?? gidsTekst.linkTekstStandaard}{" "}
                        →
                      </a>
                    ) : null}
                  </Kaart>
                ))}
              </div>
            </div>
            );
          })
        )}
      </Sectie>

      <Sectie className="pb-16">
        <div className="rounded-[20px] bg-purple-soft px-7 py-7">
          <p className="max-w-[60ch] text-ink">{gidsTekst.nota}</p>
          <Link
            href={gidsTekst.oproepLink}
            className="mt-5 inline-block rounded-full bg-purple px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {gidsTekst.oproepTekst} →
          </Link>
        </div>
      </Sectie>
    </>
  );
}

/*
  Het logo bovenaan elk kaartje. Alle vakjes zijn even hoog en de logo's
  worden altijd binnen dezelfde hoogte geschaald, zodat geen enkele
  organisatie er groter uitkomt dan een andere.
  Heeft een organisatie nog geen logo, dan komt haar naam in het
  handschriftlettertype op diezelfde plaats.
*/
function LogoBalk({ organisatie }: { organisatie: Organisatie }) {
  return (
    <div className="flex h-20 items-center border-b border-border pb-4">
      {organisatie.logo ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={`/gids/${organisatie.logo}`}
          alt={`Logo van ${organisatie.naam}`}
          className="max-h-14 w-auto max-w-[80%] object-contain object-left"
        />
      ) : (
        <span className="font-hand text-[26px] leading-none text-sage">
          {organisatie.naam}
        </span>
      )}
    </div>
  );
}
