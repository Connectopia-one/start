import Link from "next/link";
import { redirect } from "next/navigation";
import { Header } from "@/components/Header";
import { requireIngelogd, veiligVolgende } from "@/lib/auth";
import { haalPinHash } from "@/lib/ouderpin";
import { controleerPin, pinVergeten } from "./actions";

export default async function PincodePage({
  searchParams,
}: {
  searchParams: Promise<{ terug?: string; fout?: string; vergeten?: string }>;
}) {
  const session = await requireIngelogd();
  const { terug: ruw, fout, vergeten } = await searchParams;
  const terug = veiligVolgende(ruw) ?? "/account";
  if (!(await haalPinHash(session.userId))) redirect(terug);

  const veld =
    "rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest";

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-md flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          <span aria-hidden>🔒</span> Enkel voor ouders
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Dit deel is afgeschermd met de pincode van de ouder. Geef ze in om
          verder te gaan.
        </p>

        {fout === "1" && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            Die pincode klopt niet.
          </p>
        )}

        <form action={controleerPin} className="mt-5 flex gap-2">
          <input type="hidden" name="terug" value={terug} />
          <input
            name="pin"
            type="password"
            inputMode="numeric"
            pattern="\d{4}"
            maxLength={4}
            required
            autoFocus
            autoComplete="off"
            placeholder="4 cijfers"
            aria-label="Pincode"
            className={`${veld} w-32 tracking-widest`}
          />
          <button
            type="submit"
            className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Openen
          </button>
        </form>

        <details className="mt-8 text-sm" open={vergeten === "1"}>
          <summary className="cursor-pointer text-ink-dim hover:text-ink">
            Pincode vergeten?
          </summary>
          <p className="mt-2 text-ink-dim">
            Geef het wachtwoord van je account in. Dan gaat de pincode eraf en
            kan je in Mijn account een nieuwe kiezen.
          </p>
          {fout === "2" && (
            <p className="mt-2 rounded-md bg-danger/10 px-3 py-2 text-danger">
              Dat wachtwoord klopt niet.
            </p>
          )}
          <form action={pinVergeten} className="mt-3 flex gap-2">
            <input type="hidden" name="terug" value={terug} />
            <input
              name="wachtwoord"
              type="password"
              required
              autoComplete="current-password"
              placeholder="Wachtwoord"
              aria-label="Wachtwoord"
              className={`${veld} flex-1`}
            />
            <button
              type="submit"
              className="rounded-md border border-border px-4 py-2 text-sm text-ink hover:border-forest"
            >
              Pincode wissen
            </button>
          </form>
        </details>

        <Link href="/" className="mt-8 inline-block text-sm text-ink-dim hover:text-ink">
          &larr; Terug naar het oefenen
        </Link>
      </main>
    </>
  );
}
