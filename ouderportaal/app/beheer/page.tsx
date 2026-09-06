import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { maakKlasje, hernoemKlasje } from "./actions";

export default async function BeheerPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const [{ data: klasjes }, { count: gezinnenCount }] = await Promise.all([
    supabase.from("klasjes").select("id, naam, slug").order("naam"),
    supabase.from("profiles").select("id", { count: "exact", head: true }).eq("role", "ouder"),
  ]);

  return (
    <>
      <Header naam={naam} rol="beheerder" terugHref="/portaal" terugLabel="Ouderportaal" />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Beheer</h1>
        <p className="mt-1 text-sm text-ink-dim">
          {gezinnenCount ?? 0} gezin{(gezinnenCount ?? 0) === 1 ? "" : "nen"} &middot;{" "}
          {(klasjes ?? []).length} klasje{(klasjes ?? []).length === 1 ? "" : "s"}
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <div className="mt-8 grid gap-8 sm:grid-cols-2">
          <section>
            <div className="flex items-center justify-between">
              <h2 className="font-display text-lg font-semibold text-ink">Klasjes</h2>
            </div>
            <ul className="mt-3 space-y-2">
              {(klasjes ?? []).map((k) => (
                <li key={k.id} className="rounded-lg border border-border bg-surface p-3">
                  <form action={hernoemKlasje} className="flex gap-2">
                    <input type="hidden" name="id" value={k.id} />
                    <input
                      name="naam"
                      defaultValue={k.naam}
                      className="w-full rounded-md border border-transparent bg-transparent px-1 py-0.5 font-medium text-ink outline-none hover:border-border focus:border-forest focus:bg-paper focus:ring-1 focus:ring-forest"
                    />
                    <button
                      type="submit"
                      className="shrink-0 rounded-md border border-border px-2 py-0.5 text-xs text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      Bewaren
                    </button>
                  </form>
                  <div className="mt-1 flex gap-3 text-sm">
                    <Link href={`/beheer/klasjes/${k.slug}/materiaal`} className="text-forest-dark hover:underline">
                      Lesmateriaal
                    </Link>
                    <Link href={`/beheer/klasjes/${k.slug}/fotos`} className="text-forest-dark hover:underline">
                      Foto&apos;s
                    </Link>
                  </div>
                </li>
              ))}
              {(klasjes ?? []).length === 0 && (
                <li className="text-sm text-ink-dim">Nog geen klasjes aangemaakt.</li>
              )}
            </ul>

            <form action={maakKlasje} className="mt-4 flex gap-2">
              <input
                name="naam"
                required
                placeholder="Naam nieuw klasje"
                className="w-full rounded-md border border-border bg-surface px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
              <button
                type="submit"
                className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
              >
                Toevoegen
              </button>
            </form>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">Gezinnen</h2>
            <p className="mt-3 text-sm text-ink-dim">
              Accounts van ouders aanmaken en per klasje instellen of ze lesmateriaal en/of foto&apos;s
              mogen zien.
            </p>
            <Link
              href="/beheer/gezinnen"
              className="mt-4 inline-block rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Gezinnen beheren &rarr;
            </Link>

            <h2 className="mt-8 font-display text-lg font-semibold text-ink">Team</h2>
            <p className="mt-3 text-sm text-ink-dim">
              Accounts voor werknemers: zij kunnen foto&apos;s toevoegen en fiches bekijken, maar
              geen klasjes of lesmateriaal beheren.
            </p>
            <Link
              href="/beheer/team"
              className="mt-4 inline-block rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Team beheren &rarr;
            </Link>
          </section>
        </div>
      </main>
    </>
  );
}
