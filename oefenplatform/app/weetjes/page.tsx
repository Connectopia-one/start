import Link from "next/link";
import { Header } from "@/components/Header";
import { Weetje, type WeetjeRij } from "@/components/Weetje";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { stuurWeetjeIn } from "./acties";

/* Een prikbord toont wat er nú op hangt, dus geen opgeslagen versie. */
export const dynamic = "force-dynamic";

export const metadata = {
  title: "Weetjesprikbord — Oefenplatform Connectopia",
  description:
    "Weetjes die kinderen zelf instuurden en die door Connectopia opgehangen werden op het prikbord van het oefenplatform.",
};

export default async function WeetjesPage({
  searchParams,
}: {
  searchParams: Promise<{ melding?: string; fout?: string }>;
}) {
  const { melding, fout } = await searchParams;
  const session = await getSessionProfile();
  const supabase = await createClient();

  /* De leesregel laat enkel opgehangen weetjes door; het filter hier maakt
     dat expliciet, zodat een beheerder die meekijkt ook het echte bord ziet. */
  const { data } = await supabase
    .from("weetjes")
    .select("id, tekst, voornaam, leeftijd")
    .eq("goedgekeurd", true)
    .order("opgehangen_op", { ascending: false });

  const weetjes = (data ?? []) as WeetjeRij[];

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">📌 Het weetjesprikbord</h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Weetjes die kinderen zelf instuurden. Weet jij er een waar iedereen van opkijkt? Schrijf
          het onderaan op, dan hangen wij het erbij.
        </p>

        {melding === "bedankt" && (
          <p className="mt-5 max-w-2xl rounded-md bg-forest/10 px-4 py-3 text-sm text-forest-dark">
            Bedankt! Je weetje is binnen. We lezen het na en hangen het erbij — kijk over een paar
            dagen nog eens.
          </p>
        )}
        {fout && (
          <p className="mt-5 max-w-2xl rounded-md bg-danger/10 px-4 py-3 text-sm text-danger">
            {fout}
          </p>
        )}

        {weetjes.length === 0 ? (
          <p className="mt-8 text-sm text-ink-dim">
            Het bord is nog leeg. Wie hangt het eerste briefje op?
          </p>
        ) : (
          /* Zoals op een echt prikbord: de briefjes vullen de kolommen op. */
          <div className="mt-8 rounded-[20px] border border-border bg-[#f1e8d7] p-5 pb-0 shadow-[inset_0_2px_8px_rgba(35,41,31,0.08)]">
            <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
              {weetjes.map((w, nummer) => (
                <Weetje key={w.id} weetje={w} nummer={nummer} />
              ))}
            </div>
          </div>
        )}

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Stuur je eigen weetje in</h2>

          {!session ? (
            <p className="mt-2 text-sm text-ink-dim">
              Insturen kan met een account.{" "}
              <Link href="/login" className="text-forest-dark underline underline-offset-2">
                Log in
              </Link>{" "}
              of{" "}
              <Link href="/registreren" className="text-forest-dark underline underline-offset-2">
                maak er een aan
              </Link>
              .
            </p>
          ) : (
            <>
              <p className="mt-2 max-w-2xl text-sm text-ink-dim">
                Alles wordt eerst nagelezen voor het op het bord komt, dus het duurt even. Zet er
                alleen je voornaam bij, geen achternaam en geen adres.
              </p>

              <form action={stuurWeetjeIn} className="mt-5 grid max-w-xl gap-4">
                <label className="grid gap-1 text-sm">
                  <span className="text-ink">Je weetje</span>
                  <textarea
                    name="tekst"
                    rows={3}
                    required
                    maxLength={500}
                    placeholder="Wist je dat een octopus drie harten heeft?"
                    className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                </label>

                <div className="grid gap-4 sm:grid-cols-2">
                  <label className="grid gap-1 text-sm">
                    <span className="text-ink">Je voornaam</span>
                    <input
                      type="text"
                      name="voornaam"
                      maxLength={40}
                      className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                    />
                  </label>
                  <label className="grid gap-1 text-sm">
                    <span className="text-ink">Hoe oud ben je? (mag je openlaten)</span>
                    <input
                      type="number"
                      name="leeftijd"
                      min={3}
                      max={21}
                      className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                    />
                  </label>
                </div>

                <button
                  type="submit"
                  className="justify-self-start rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
                >
                  Insturen
                </button>
              </form>
            </>
          )}
        </section>
      </main>
    </>
  );
}
