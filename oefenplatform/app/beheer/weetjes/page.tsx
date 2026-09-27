import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { pasWeetjeAan, wisWeetje, zetOpgehangen } from "./actions";

export const dynamic = "force-dynamic";

function datum(iso: string) {
  return new Date(iso).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default async function BeheerWeetjesPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data } = await supabase
    .from("weetjes")
    .select("id, tekst, voornaam, leeftijd, goedgekeurd, aangemaakt_op, inzender:profiles(full_name)")
    .order("goedgekeurd", { ascending: true })
    .order("aangemaakt_op", { ascending: false });

  const rijen = data ?? [];
  const wachtend = rijen.filter((w) => !w.goedgekeurd);

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Weetjes</h1>
        <p className="mt-1 text-sm text-ink-dim">
          {wachtend.length === 0
            ? "Er wacht niets op jou."
            : `${wachtend.length} weetje${wachtend.length === 1 ? "" : "s"} wacht${
                wachtend.length === 1 ? "" : "en"
              } om opgehangen te worden.`}{" "}
          Niets komt op{" "}
          <Link href="/weetjes" className="text-forest-dark hover:underline">
            het prikbord
          </Link>{" "}
          voor jij erop klikt.
        </p>

        <div className="mt-8 space-y-4">
          {rijen.map((w) => {
            // Supabase geeft een gekoppelde tabel als object terug; de
            // typegenerator maakt er soms een lijst van.
            const inzender = (Array.isArray(w.inzender) ? w.inzender[0] : w.inzender) as
              | { full_name: string | null }
              | null;

            return (
              <article
                key={w.id}
                className={`rounded-xl border px-5 py-4 text-sm ${
                  w.goedgekeurd ? "border-border bg-paper opacity-70" : "border-amber/40 bg-surface"
                }`}
              >
                <form action={pasWeetjeAan} className="grid gap-2">
                  <input type="hidden" name="id" value={w.id} />
                  <textarea
                    name="tekst"
                    rows={2}
                    defaultValue={w.tekst}
                    maxLength={500}
                    className="w-full rounded-md border border-border bg-paper px-3 py-2 text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                  <div className="flex flex-wrap items-center gap-2">
                    <input
                      type="text"
                      name="voornaam"
                      defaultValue={w.voornaam ?? ""}
                      placeholder="voornaam"
                      maxLength={40}
                      className="w-40 rounded-md border border-border bg-paper px-3 py-1.5 text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                    />
                    {w.leeftijd ? (
                      <span className="text-xs text-ink-dim">{w.leeftijd} jaar</span>
                    ) : null}
                    <button type="submit" className="text-ink-dim hover:text-ink">
                      Tekst bewaren
                    </button>
                  </div>
                </form>

                <p className="mt-3 text-xs text-ink-dim">
                  {datum(w.aangemaakt_op)}
                  {inzender?.full_name ? ` · ingestuurd door ${inzender.full_name}` : ""}
                </p>

                <div className="mt-3 flex flex-wrap items-center gap-4">
                  <form action={zetOpgehangen}>
                    <input type="hidden" name="id" value={w.id} />
                    <input type="hidden" name="naar" value={w.goedgekeurd ? "false" : "true"} />
                    <button
                      type="submit"
                      className={
                        w.goedgekeurd
                          ? "text-ink-dim hover:text-ink"
                          : "rounded-md bg-forest px-3 py-1.5 font-medium text-white transition hover:bg-forest-dark"
                      }
                    >
                      {w.goedgekeurd ? "Van het bord halen" : "Ophangen"}
                    </button>
                  </form>
                  <form action={wisWeetje}>
                    <input type="hidden" name="id" value={w.id} />
                    <button type="submit" className="text-ink-dim hover:text-danger">
                      Wissen
                    </button>
                  </form>
                </div>
              </article>
            );
          })}

          {rijen.length === 0 && (
            <p className="text-sm text-ink-dim">
              Er is nog niets ingestuurd. Zodra een kind op{" "}
              <Link href="/weetjes" className="text-forest-dark hover:underline">
                het weetjesprikbord
              </Link>{" "}
              iets achterlaat, staat het hier.
            </p>
          )}
        </div>
      </main>
    </>
  );
}
