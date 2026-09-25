import Link from "next/link";
import type { Metadata } from "next";
import { site } from "@/content/site";
import { verder } from "@/content/verder";
import { OntdekVerder } from "@/components/OntdekVerder";

export const metadata: Metadata = {
  title: "Bedankt",
  description: "Je bericht is bij ons toegekomen.",
};

/*
  Waar een bezoeker belandt nadat hij een formulier verstuurd heeft.

  Dit is ook het enige moment waarop de site zelf weet dat er iemand een
  aanvraag deed. Wil je later meten hoeveel mensen via een advertentie
  effectief inschrijven, dan is dit de pagina die dat telt.
*/
export default async function BedanktPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string }>;
}) {
  const { fout } = await searchParams;

  if (fout) {
    return (
      <div className="mx-auto w-full max-w-2xl px-6 py-16">
        <div className="rounded-[24px] bg-surface px-7 py-8 shadow-sm">
          <h1 className="text-[26px] font-extrabold text-green">
            Er liep iets mis
          </h1>
          <p className="mt-3 text-[17px] text-ink">
            Je bericht is niet bij ons toegekomen. Probeer het zo nog eens, of
            bereik ons gewoon rechtstreeks — dat werkt altijd.
          </p>
          <p className="mt-5 text-[17px] text-ink">
            <a className="font-bold text-green underline" href={`mailto:${site.email}`}>
              {site.email}
            </a>
            <br />
            <a className="font-bold text-green underline" href={site.telefoonLink}>
              {site.telefoon}
            </a>
          </p>
          <Link
            href="/contact"
            className="mt-7 inline-block rounded-full bg-green px-7 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
          >
            Terug naar contact →
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-16">
      <div className="rounded-[24px] bg-surface px-7 py-8 shadow-sm">
        <p className="text-[15px] font-bold uppercase tracking-wide text-orange">
          Goed ontvangen
        </p>
        <h1 className="mt-1 text-[30px] font-extrabold leading-tight text-green">
          Bedankt, je bericht is binnen.
        </h1>
        <p className="mt-4 text-[17px] text-ink">
          We lezen het zo snel mogelijk en nemen contact met je op. Je hoeft
          zelf niets meer te doen.
        </p>
        <p className="mt-3 text-[17px] text-ink">
          Dringend? Bel ons gerust op{" "}
          <a className="font-bold text-green underline" href={site.telefoonLink}>
            {site.telefoon}
          </a>
          .
        </p>
        {/* Enkel de startpagina hier: het aanbod staat als kaart hieronder. */}
        <div className="mt-7">
          <Link
            href="/"
            className="inline-block rounded-full bg-green px-7 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
          >
            Naar de startpagina →
          </Link>
        </div>
      </div>

      {/* Wie net iets verstuurd heeft, is het meest geneigd om nog verder te
          kijken. Zie content/verder.ts. */}
      <div className="mt-6 rounded-[24px] bg-surface px-7 py-8 shadow-sm">
        <OntdekVerder titel={verder.bedanktTitel} tekst={verder.bedanktTekst} />
      </div>
    </div>
  );
}
