import Link from "next/link";
import { login } from "./actions";

export default async function LoginPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string }>;
}) {
  const { fout } = await searchParams;

  return (
    <main className="flex flex-1 items-center justify-center bg-paper px-6 py-16">
      <div className="w-full max-w-sm">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          Connectopia
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">Oefenplatform</h1>
        <p className="mt-2 text-sm text-ink-dim">Log in met je e-mailadres en wachtwoord.</p>

        <form action={login} className="mt-8 space-y-4 rounded-xl border border-border bg-surface p-6">
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
          <div className="space-y-1.5">
            <label htmlFor="password" className="text-sm font-medium text-ink">
              Wachtwoord
            </label>
            <input
              id="password"
              name="password"
              type="password"
              required
              autoComplete="current-password"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </div>
          <button
            type="submit"
            className="w-full rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
          >
            Inloggen
          </button>
        </form>

        <p className="mt-4 text-center text-xs text-ink-dim">
          <Link href="/wachtwoord-vergeten" className="text-forest-dark underline-offset-2 hover:underline">
            Wachtwoord vergeten?
          </Link>
        </p>

        <p className="mt-4 text-center text-xs text-ink-dim">
          Nog geen account?{" "}
          <Link href="/registreren" className="text-forest-dark underline-offset-2 hover:underline">
            Registreer hier
          </Link>
        </p>
      </div>
    </main>
  );
}
