import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { maakTeamlid, wijzigTeamlidWachtwoord, verwijderTeamlid } from "./actions";

export default async function TeamBeheerPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const { data: teamleden } = await supabase
    .from("profiles")
    .select("id, full_name")
    .eq("role", "leerkracht")
    .order("full_name");

  return (
    <>
      <Header naam={naam} rol="beheerder" terugHref="/beheer" terugLabel="Beheer" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Team</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Accounts voor werknemers die mee lesgeven: zij kunnen foto&apos;s toevoegen en de
          inlichtingenfiches van de kinderen bekijken, maar geen klasjes of lesmateriaal beheren.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <ul className="mt-6 space-y-3">
          {(teamleden ?? []).map((lid) => (
            <li key={lid.id} className="rounded-lg border border-border bg-surface p-4">
              <p className="font-medium text-ink">{lid.full_name}</p>
              <form action={wijzigTeamlidWachtwoord} className="mt-2 flex gap-2">
                <input type="hidden" name="profile_id" value={lid.id} />
                <input
                  name="wachtwoord"
                  type="text"
                  minLength={8}
                  placeholder="Nieuw wachtwoord (min. 8 tekens)"
                  className="w-full rounded-md border border-border bg-paper px-3 py-1.5 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
                <button
                  type="submit"
                  className="shrink-0 rounded-md border border-border px-3 py-1.5 text-xs text-ink-dim hover:border-forest hover:text-forest-dark"
                >
                  Wachtwoord bijwerken
                </button>
              </form>
              <form action={verwijderTeamlid} className="mt-2">
                <input type="hidden" name="profile_id" value={lid.id} />
                <button type="submit" className="text-xs text-danger hover:underline">
                  Account verwijderen
                </button>
              </form>
            </li>
          ))}
          {(teamleden ?? []).length === 0 && (
            <li className="text-sm text-ink-dim">Nog geen teamleden toegevoegd.</li>
          )}
        </ul>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Teamlid toevoegen</h2>
          <form action={maakTeamlid} className="mt-4 space-y-4">
            <div className="space-y-1.5">
              <label htmlFor="naam" className="text-sm font-medium text-ink">
                Naam
              </label>
              <input
                id="naam"
                name="naam"
                required
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
                placeholder="Deel dit veilig met je werknemer"
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
