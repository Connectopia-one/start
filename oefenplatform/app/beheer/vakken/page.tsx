import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { maakVak, verwijderVak, maakHoofdstuk, wisselGratis, verwijderHoofdstuk } from "../actions";

type Hoofdstuk = { id: string; titel: string; volgnummer: number; gratis: boolean };
type Vak = { id: string; naam: string; slug: string; hoofdstukken: Hoofdstuk[] };

export default async function BeheerVakkenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout } = await searchParams;
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis)")
    .order("volgorde", { ascending: true });

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Vakken &amp; hoofdstukken</h1>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

        <div className="mt-6 space-y-8">
          {(vakken as Vak[] | null)?.map((vak) => (
            <section key={vak.id} className="rounded-xl border border-border bg-surface p-5">
              <div className="flex items-center justify-between">
                <h2 className="font-display text-lg font-semibold text-ink">{vak.naam}</h2>
                <form action={verwijderVak}>
                  <input type="hidden" name="id" value={vak.id} />
                  <button type="submit" className="text-xs text-danger hover:underline">
                    Vak verwijderen
                  </button>
                </form>
              </div>

              <ul className="mt-4 space-y-2">
                {vak.hoofdstukken
                  .sort((a, b) => a.volgnummer - b.volgnummer)
                  .map((h) => (
                    <li
                      key={h.id}
                      className="flex items-center justify-between rounded-lg border border-border px-3 py-2 text-sm"
                    >
                      <Link
                        href={`/beheer/vakken/${vak.slug}/${h.volgnummer}`}
                        className="text-forest-dark hover:underline"
                      >
                        {h.volgnummer}. {h.titel}
                      </Link>
                      <div className="flex items-center gap-3">
                        <form action={wisselGratis}>
                          <input type="hidden" name="id" value={h.id} />
                          <input type="hidden" name="gratis" value={String(h.gratis)} />
                          <button
                            type="submit"
                            className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                              h.gratis ? "bg-forest/10 text-forest-dark" : "bg-ink-dim/10 text-ink-dim"
                            }`}
                          >
                            {h.gratis ? "Gratis" : "Op slot"}
                          </button>
                        </form>
                        <form action={verwijderHoofdstuk}>
                          <input type="hidden" name="id" value={h.id} />
                          <button type="submit" className="text-xs text-danger hover:underline">
                            Verwijderen
                          </button>
                        </form>
                      </div>
                    </li>
                  ))}
              </ul>

              <form action={maakHoofdstuk} className="mt-4 flex flex-wrap items-center gap-2">
                <input type="hidden" name="vak_id" value={vak.id} />
                <input
                  name="titel"
                  required
                  placeholder="Titel nieuw hoofdstuk"
                  className="min-w-0 flex-1 rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
                <label className="flex items-center gap-1.5 text-xs text-ink-dim">
                  <input type="checkbox" name="gratis" className="accent-forest" />
                  Gratis
                </label>
                <button
                  type="submit"
                  className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                >
                  Toevoegen
                </button>
              </form>
            </section>
          ))}
        </div>

        <form action={maakVak} className="mt-8 flex gap-2">
          <input
            name="naam"
            required
            placeholder="Naam nieuw vak (bv. Wiskunde)"
            className="w-full rounded-md border border-border bg-surface px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
          <button
            type="submit"
            className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Vak toevoegen
          </button>
        </form>
      </main>
    </>
  );
}
