import Link from "next/link";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { huidigSchooljaar, schooljaarEindeLabel } from "@/lib/schooljaar";
import { PRIJS_NU_EUR, TIJDELIJKE_PRIJS, TIJDELIJKE_PRIJS_KORT } from "@/lib/prijs";
import { createClient } from "@/lib/supabase/server";
import { maakKind } from "./kinderen/actions";

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
    .select("id, naam")
    .eq("profile_id", session.userId)
    .order("naam");

  return (
    <>
      <Header naam={profile?.full_name} rol={profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Mijn account</h1>
        <p className="mt-1 text-sm text-ink-dim">{session.email}</p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {gelukt === "plusklas" && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            Je plusklas-code is gelukt. Je hebt nu gratis volledige toegang tot alle hoofdstukken.
          </p>
        )}

        <div className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Toegang schooljaar {huidigSchooljaar()}</h2>

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
                Volledige toegang vrijgeven — €{PRIJS_NU_EUR} per schooljaar (tot en met{" "}
                {schooljaarEindeLabel()})
              </Link>
              {TIJDELIJKE_PRIJS && (
                <p className="mt-2 text-xs text-ink-dim">{TIJDELIJKE_PRIJS_KORT}</p>
              )}
              <p className="mt-3 text-sm text-ink-dim">
                Zit je kind in de externe plusklas? Op diezelfde pagina kan je je plusklas-code
                ingeven, ook als je die bij het registreren nog niet had.
              </p>
            </>
          )}
        </div>

        <div className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Mijn kinderen</h2>
          <p className="mt-1 text-sm text-ink-dim">
            Voeg je kind(eren) toe om hun voortgang en score per hoofdstuk te kunnen opvolgen.
          </p>

          <ul className="mt-4 space-y-2">
            {(kinderen ?? []).map((k) => (
              <li
                key={k.id}
                className="flex items-center justify-between rounded-lg border border-border px-3 py-2 text-sm"
              >
                <span className="text-ink">{k.naam}</span>
                <Link href={`/account/kinderen/${k.id}`} className="text-forest-dark hover:underline">
                  Voortgang bekijken &rarr;
                </Link>
              </li>
            ))}
            {!kinderen?.length && <li className="text-sm text-ink-dim">Nog geen kinderen toegevoegd.</li>}
          </ul>

          <form action={maakKind} className="mt-4 flex gap-2">
            <input
              name="naam"
              required
              placeholder="Naam van je kind"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
            <button
              type="submit"
              className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Toevoegen
            </button>
          </form>
        </div>

        <Link href="/" className="mt-6 inline-block text-sm text-ink-dim hover:text-ink">
          &larr; Terug naar alle vakken
        </Link>
      </main>
    </>
  );
}
