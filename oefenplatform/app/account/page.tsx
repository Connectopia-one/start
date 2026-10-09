import Link from "next/link";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { huidigSchooljaar, schooljaarEindeLabel } from "@/lib/schooljaar";
import {
  PRIJS_NU_EUR,
  TIJDELIJKE_PRIJS,
  TIJDELIJKE_PRIJS_KORT,
} from "@/lib/prijs";
import { createClient } from "@/lib/supabase/server";
import { gebruikPlusklasCode } from "@/app/betalen/actions";
import { KinderenLijst } from "./KinderenLijst";

export default async function AccountPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; gelukt?: string }>;
}) {
  const session = await requireIngelogd();
  const { fout, gelukt } = await searchParams;
  const profile = session.profile;
  const volledigeToegang = heeftVolledigeToegang(profile);

  const supabase = await createClient();
  const { data: kinderen } = await supabase
    .from("kinderen")
    // "*" en niet de kolommen apart: zolang voortgangsbalk.sql nog niet
    // gedraaid is, bestaat toon_voortgang nog niet en zou een select op
    // die naam een fout geven. Dan zou het platform helemaal geen kinderen
    // meer zien, en dus ook geen voortgang meer bijhouden.
    .select("*")
    .eq("profile_id", session.userId)
    .order("naam");

  return (
    <>
      <Header naam={profile?.full_name} rol={profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Mijn account
        </h1>
        <p className="mt-1 text-sm text-ink-dim">{session.email}</p>

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {fout}
          </p>
        )}
        {gelukt === "plusklas" && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            Je toegangscode is gelukt. Je hebt nu gratis volledige toegang tot
            alle hoofdstukken.
          </p>
        )}

        <div className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            Toegang schooljaar {huidigSchooljaar()}
          </h2>

          {profile?.is_plusklas ? (
            <p className="mt-2 text-sm text-forest-dark">
              Je hebt gratis volledige toegang als plusklas-gezin.
            </p>
          ) : volledigeToegang ? (
            <p className="mt-2 text-sm text-forest-dark">
              Je hebt volledige toegang tot alle hoofdstukken, geldig tot en met{" "}
              {schooljaarEindeLabel()}.
            </p>
          ) : (
            <>
              <p className="mt-2 text-sm text-ink-dim">
                Je hebt nu enkel toegang tot de gratis proefhoofdstukken.
              </p>
              <Link
                href="/betalen"
                className="mt-4 inline-block rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
              >
                Volledige toegang vrijgeven — €{PRIJS_NU_EUR} per schooljaar
                (tot en met {schooljaarEindeLabel()})
              </Link>
              {TIJDELIJKE_PRIJS && (
                <p className="mt-2 text-xs text-ink-dim">
                  {TIJDELIJKE_PRIJS_KORT}
                </p>
              )}
              {/*
                Op 9 oktober 2026 zag Kim een gezin dat zijn toegangscode had
                ingetikt als de naam van zijn kind. Het codevakje bestond wel,
                maar enkel op /betalen, en dat is niet de plek waar iemand gaat
                zoeken. Daarom staat het nu ook hier, op de pagina waar je je
                kinderen toevoegt.
              */}
              <div className="mt-6 border-t border-border pt-5">
                <h3 className="text-sm font-medium text-ink">
                  Heb je een toegangscode?
                </h3>
                <p className="mt-1 text-sm text-ink-dim">
                  Kreeg je van ons een code, bijvoorbeeld omdat je meetest of
                  omdat je kind in de externe plusklas zit? Vul ze hier in en je
                  toegang staat meteen open. Het is geen wachtwoord en ook geen
                  naam van een kind.
                </p>
                <form
                  action={gebruikPlusklasCode}
                  className="mt-3 flex flex-wrap gap-2"
                >
                  <input type="hidden" name="terug" value="/account" />
                  <input
                    id="plusklas_code"
                    name="plusklas_code"
                    type="text"
                    required
                    autoComplete="off"
                    autoCapitalize="characters"
                    placeholder="Je toegangscode"
                    className="min-w-0 flex-1 rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                  <button
                    type="submit"
                    className="shrink-0 rounded-md border border-forest px-4 py-2 text-sm font-medium text-forest-dark transition hover:bg-forest hover:text-white"
                  >
                    Toegang vrijgeven
                  </button>
                </form>
              </div>
            </>
          )}
        </div>

        <div className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            Mijn kinderen
          </h2>
          <p className="mt-1 text-sm text-ink-dim">
            Voeg je kind(eren) toe om hun voortgang en score per hoofdstuk te
            kunnen opvolgen.
          </p>

          <KinderenLijst
            kinderen={(kinderen ?? []).map((k) => ({
              id: k.id,
              naam: k.naam,
              toonVoortgang: Boolean(k.toon_voortgang),
            }))}
          />
        </div>

        <Link
          href="/"
          className="mt-6 inline-block text-sm text-ink-dim hover:text-ink"
        >
          &larr; Terug naar alle vakken
        </Link>
      </main>
    </>
  );
}
