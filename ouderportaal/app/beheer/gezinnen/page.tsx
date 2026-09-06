import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { maakGezin } from "./actions";

export default async function GezinnenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const { data: gezinnen } = await supabase
    .from("profiles")
    .select("id, full_name")
    .eq("role", "ouder")
    .order("full_name");

  return (
    <>
      <Header naam={naam} isBeheerder terugHref="/beheer" terugLabel="Beheer" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Gezinnen</h1>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <ul className="mt-6 space-y-2">
          {(gezinnen ?? []).map((g) => (
            <li key={g.id}>
              <Link
                href={`/beheer/gezinnen/${g.id}`}
                className="block rounded-lg border border-border bg-surface p-3 font-medium text-ink hover:border-forest"
              >
                {g.full_name}
              </Link>
            </li>
          ))}
          {(gezinnen ?? []).length === 0 && (
            <li className="text-sm text-ink-dim">Nog geen gezinnen toegevoegd.</li>
          )}
        </ul>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Nieuw gezin toevoegen</h2>
          <p className="mt-1 text-sm text-ink-dim">
            Na het aanmaken kies je op de volgende pagina welke klasjes dit gezin mag zien, en of
            dat lesmateriaal, foto&apos;s, of beide zijn.
          </p>
          <form action={maakGezin} className="mt-4 space-y-4">
            <div className="space-y-1.5">
              <label htmlFor="naam" className="text-sm font-medium text-ink">
                Naam gezin
              </label>
              <input
                id="naam"
                name="naam"
                required
                placeholder="Bv. Familie Peeters"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
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
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <div className="space-y-1.5">
              <label htmlFor="wachtwoord" className="text-sm font-medium text-ink">
                Tijdelijk wachtwoord (minstens 8 tekens)
              </label>
              <input
                id="wachtwoord"
                name="wachtwoord"
                type="text"
                minLength={8}
                required
                placeholder="Deel dit veilig met het gezin"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Account aanmaken
            </button>
          </form>
        </section>
      </main>
    </>
  );
}
