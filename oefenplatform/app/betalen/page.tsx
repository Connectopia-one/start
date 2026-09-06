import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";
import { huidigSchooljaar } from "@/lib/schooljaar";
import { startBetaling } from "./actions";

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
          Betaling voor volledige toegang tot alle hoofdstukken van schooljaar{" "}
          {huidigSchooljaar()}. De opbrengsten gaan volledig naar vzw Connectopia.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

        <div className="mt-6 rounded-xl border border-border bg-surface p-6 text-center">
          <p className="font-display text-3xl font-semibold text-forest-dark">
            €{PRIJS_SCHOOLJAAR_EUR}
            <span className="text-base font-normal text-ink-dim"> / schooljaar</span>
          </p>
          <p className="mt-1 text-xs text-ink-dim">geldig tot einde schooljaar {huidigSchooljaar()}</p>
          <form action={startBetaling} className="mt-6">
            <button
              type="submit"
              className="w-full rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
            >
              Betalen met Mollie
            </button>
          </form>
        </div>
      </main>
    </>
  );
}
