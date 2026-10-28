import Link from "next/link";
import type { Metadata } from "next";
import { kampRegels } from "@/content/kampen";
import { euro } from "@/lib/kampprijs";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: "Inschrijving ontvangen",
  description: "Je kampinschrijving is bij ons toegekomen.",
  robots: { index: false },
};

/*
  Na een kampinschrijving: wat er nu te betalen is, op welk rekeningnummer en
  met welke mededeling. Het bedrag en het nummer komen uit het webadres; er
  staat met opzet geen naam van een kind in.
*/
export default async function KampBedankt({
  searchParams,
}: {
  searchParams: Promise<{
    fout?: string;
    bedrag?: string;
    code?: string;
    later?: string;
    wacht?: string;
    vt?: string;
  }>;
}) {
  const { fout, bedrag, code, later, wacht, vt } = await searchParams;
  const nu = Number(bedrag ?? 0);

  if (fout) {
    return (
      <div className="mx-auto w-full max-w-2xl px-6 py-16">
        <div className="rounded-[24px] bg-surface px-7 py-8 shadow-sm">
          <h1 className="text-[26px] font-extrabold text-green">Er liep iets mis</h1>
          <p className="mt-3 text-[17px] text-ink">
            Je inschrijving is niet bij ons toegekomen. Probeer het zo nog eens,
            of bereik ons rechtstreeks.
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
            href="/kampen/inschrijven"
            className="mt-7 inline-block rounded-full bg-green px-7 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
          >
            Terug naar de inschrijving →
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-16">
      <div className="rounded-[24px] bg-surface px-7 py-8 shadow-sm">
        <p className="text-[15px] font-bold uppercase tracking-wide text-orange">
          Inschrijving ontvangen
        </p>
        <h1 className="mt-2 text-[28px] font-extrabold text-green">Bedankt!</h1>
        <p className="mt-3 text-[17px] text-ink">
          Je inschrijving is goed bij ons toegekomen.
          {nu > 0 ? " Je plaats is zeker zodra de betaling binnen is." : ""}
        </p>

        {nu > 0 ? (
          <div className="mt-6 rounded-[16px] bg-sage-soft px-5 py-4 text-[17px] text-ink">
            <p>
              Schrijf <strong>{euro(nu)}</strong> over {kampRegels.betaaltermijn}:
            </p>
            <p className="mt-2">
              Rekeningnummer: <strong>{kampRegels.rekening}</strong>
              <br />
              Op naam van: {kampRegels.rekeninghouder}
              <br />
              Mededeling: <strong>{code}</strong>
            </p>
            <p className="mt-2 text-[15px] text-ink-dim">
              Neem de mededeling precies zo over, dan weten we bij welke
              inschrijving je betaling hoort. Noteer ze even, ze staat nergens
              anders.
            </p>
          </div>
        ) : null}

        {later ? (
          <p className="mt-4 text-[16px] text-ink">
            Voor het kamp dat nog bevestigd moet worden ({euro(Number(later))}),
            betaal je pas als wij laten weten dat het doorgaat.
          </p>
        ) : null}
        {wacht ? (
          <p className="mt-4 text-[16px] text-ink">
            Voor een volzet kamp sta je op de wachtlijst. Daarvoor betaal je
            niets, tot we je laten weten dat er een plaats vrijkomt.
          </p>
        ) : null}
        {vt ? (
          <p className="mt-4 text-[16px] text-ink">
            Vergeet het attest van de verhoogde tegemoetkoming niet te mailen
            naar {site.email}.
          </p>
        ) : null}

        <p className="mt-6 text-[16px] text-ink-dim">
          Vragen? Mail naar{" "}
          <a className="font-bold text-green underline" href={`mailto:${site.email}`}>
            {site.email}
          </a>{" "}
          of bel {site.telefoon}.
        </p>
      </div>
    </div>
  );
}
