import Link from "next/link";
import { stuurResetLink } from "./actions";

export default async function WachtwoordVergetenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; verstuurd?: string }>;
}) {
  const { fout, verstuurd } = await searchParams;

  return (
    <main className="flex flex-1 items-center justify-center bg-paper px-6 py-16">
      <div className="w-full max-w-sm">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          Connectopia
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">Wachtwoord vergeten</h1>

        {verstuurd ? (
          <div className="mt-8 rounded-xl border border-border bg-surface p-6 text-sm text-ink">
            <p>
              Als er een account bestaat met dit e-mailadres, hebben we net een e-mail gestuurd
              met een link om een nieuw wachtwoord in te stellen.
            </p>
            <Link href="/login" className="mt-4 inline-block text-forest-dark underline-offset-2 hover:underline">
              Terug naar inloggen
            </Link>
          </div>
        ) : (
          <>
            <p className="mt-2 text-sm text-ink-dim">
              Vul je e-mailadres in — we sturen je een link om een nieuw wachtwoord in te stellen.
            </p>
            <form action={stuurResetLink} className="mt-8 space-y-4 rounded-xl border border-border bg-surface p-6">
              {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
              <div className="space-y-1.5">
                <label htmlFor="email" className="text-sm font-medium text-ink">
                  E-mailadres
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  required
                  autoComplete="email"
                  className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
              </div>
              <button
                type="submit"
                className="w-full rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
              >
                Reset-link versturen
              </button>
            </form>
            <p className="mt-6 text-center text-xs text-ink-dim">
              <Link href="/login" className="text-forest-dark underline-offset-2 hover:underline">
                Terug naar inloggen
              </Link>
            </p>
          </>
        )}
      </div>
    </main>
  );
}
