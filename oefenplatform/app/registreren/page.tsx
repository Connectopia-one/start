import Link from "next/link";
import { redirect } from "next/navigation";
import { Wachtwoordveld } from "@/components/Wachtwoordveld";
import { Verzendknop } from "@/components/Verzendknop";
import { getSessionProfile } from "@/lib/auth";
import { registreren } from "./actions";

export default async function RegistrerenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string }>;
}) {
  const { fout } = await searchParams;

  // Wie al ingelogd is, heeft hier niets te zoeken. Zonder dit kwam iemand
  // die na een geslaagde registratie op de terugknop drukte, opnieuw op dit
  // formulier uit, en kreeg hij te horen dat zijn adres al bestond.
  const sessie = await getSessionProfile();
  if (sessie) redirect("/account");

  return (
    <main className="flex flex-1 items-center justify-center bg-paper px-6 py-16">
      <div className="w-full max-w-sm">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          Connectopia
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          Registreren
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Maak een account aan om te oefenen. Zit je kind in de externe
          plusklas? Vul dan de plusklas-code in die je van ons kreeg voor gratis
          volledige toegang.
        </p>

        <form
          action={registreren}
          className="mt-8 space-y-4 rounded-xl border border-border bg-surface p-6"
        >
          {fout && (
            <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
              {fout}
            </p>
          )}
          <div className="space-y-1.5">
            <label htmlFor="naam" className="text-sm font-medium text-ink">
              Naam
            </label>
            <input
              id="naam"
              name="naam"
              type="text"
              required
              autoComplete="name"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </div>
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
          <Wachtwoordveld
            id="password"
            naam="password"
            label="Wachtwoord"
            autoComplete="new-password"
            minLength={8}
            hulp="Minstens 8 tekens."
          />
          <div className="space-y-1.5">
            <label
              htmlFor="plusklas_code"
              className="text-sm font-medium text-ink"
            >
              Plusklas-code{" "}
              <span className="font-normal text-ink-dim">(optioneel)</span>
            </label>
            <input
              id="plusklas_code"
              name="plusklas_code"
              type="text"
              autoComplete="off"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </div>
          <Verzendknop
            label="Account aanmaken"
            bezigLabel="Bezig met aanmaken…"
            className="w-full rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
          />
        </form>

        <p className="mt-6 text-center text-xs text-ink-dim">
          Heb je al een account?{" "}
          <Link
            href="/login"
            className="text-forest-dark underline-offset-2 hover:underline"
          >
            Log hier in
          </Link>
        </p>
      </div>
    </main>
  );
}
