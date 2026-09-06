import Link from "next/link";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { huidigSchooljaar, schooljaarEindeLabel } from "@/lib/schooljaar";
import { PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";

export default async function AccountPage() {
  const session = await requireIngelogd();
  const profile = session.profile;
  const volledigeToegang = heeftVolledigeToegang(profile);

  return (
    <>
      <Header naam={profile?.full_name} rol={profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Mijn account</h1>
        <p className="mt-1 text-sm text-ink-dim">{session.email}</p>

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
                Volledige toegang vrijgeven — €{PRIJS_SCHOOLJAAR_EUR} per schooljaar (tot en met{" "}
                {schooljaarEindeLabel()})
              </Link>
            </>
          )}
        </div>

        <Link href="/" className="mt-6 inline-block text-sm text-ink-dim hover:text-ink">
          &larr; Terug naar alle vakken
        </Link>
      </main>
    </>
  );
}
