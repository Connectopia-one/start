import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { PRIJS_NU_EUR, PRIJS_STRAKS_EUR, TIJDELIJKE_PRIJS, TIJDELIJKE_PRIJS_UITLEG } from "@/lib/prijs";
import { huidigSchooljaar, schooljaarEindeLabel } from "@/lib/schooljaar";
import { gebruikPlusklasCode, startBetaling } from "./actions";

export default async function BetalenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string }>;
}) {
  const session = await requireIngelogd();
  const { fout } = await searchParams;

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-md flex-1 px-6 py-16">
        <h1 className="font-display text-2xl font-semibold text-ink">Volledige toegang</h1>
        <p className="mt-2 text-sm text-ink-dim">
          Volledige toegang tot alle hoofdstukken van schooljaar {huidigSchooljaar()}. Dat kan op
          twee manieren: met een plusklas-code, of met een bijdrage. De opbrengsten gaan volledig
          naar vzw Connectopia.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

        <div className="mt-6 rounded-xl border border-border bg-surface p-6 text-center">
          <p className="font-display text-3xl font-semibold text-forest-dark">
            {TIJDELIJKE_PRIJS && (
              <span className="mr-2 align-middle text-lg font-normal text-ink-dim line-through">
                €{PRIJS_STRAKS_EUR}
              </span>
            )}
            €{PRIJS_NU_EUR}
            <span className="text-base font-normal text-ink-dim"> / schooljaar</span>
          </p>
          <p className="mt-1 text-xs text-ink-dim">geldig tot en met {schooljaarEindeLabel()}</p>
          {TIJDELIJKE_PRIJS && (
            <p className="mt-4 rounded-md bg-amber/10 px-4 py-3 text-left text-sm text-ink">
              {TIJDELIJKE_PRIJS_UITLEG}
            </p>
          )}
          <form action={startBetaling} className="mt-6">
            <button
              type="submit"
              className="w-full rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
            >
              Betalen met Mollie
            </button>
          </form>
        </div>

        <div className="mt-6 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Heb je een plusklas-code?</h2>
          <p className="mt-1 text-sm text-ink-dim">
            Zit je kind in de externe plusklas, dan kreeg je van ons een code. Vul ze hier in en je
            krijgt meteen gratis volledige toegang. Ook als je ze bij het registreren nog niet bij
            de hand had.
          </p>
          <form action={gebruikPlusklasCode} className="mt-4 flex flex-wrap gap-2">
            <input
              id="plusklas_code"
              name="plusklas_code"
              type="text"
              required
              autoComplete="off"
              autoCapitalize="characters"
              placeholder="Je plusklas-code"
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
      </main>
    </>
  );
}
