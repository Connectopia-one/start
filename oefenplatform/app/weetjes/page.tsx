import Link from "next/link";
import { Header } from "@/components/Header";
import { bordKlassen } from "@/components/Blaadje";
import { Weetje, type WeetjeRij } from "@/components/Weetje";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { stuurWeetjeIn, verbeterWeetje } from "./acties";

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

  /* Je eigen briefjes, ook die nog wachten of die niet opgehangen werden.
     De leesregel in supabase/weetjes-bericht.sql laat alleen je eigen rijen
     door, dus niemand ziet hier wat een ander instuurde. */
  const { data: eigenData } = session
    ? await supabase
        .from("weetjes")
        .select("id, tekst, goedgekeurd, niet_geplaatst, bericht, aangemaakt_op")
        .eq("profile_id", session.userId)
        .order("aangemaakt_op", { ascending: false })
    : { data: [] };

  const eigen = (eigenData ?? []) as {
    id: string;
    tekst: string;
    goedgekeurd: boolean;
    niet_geplaatst: boolean;
    bericht: string | null;
    aangemaakt_op: string;
  }[];

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">📌 Het weetjesprikbord</h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Weetjes die kinderen zelf instuurden. Weet jij er een waar iedereen van opkijkt? Schrijf
          het onderaan op, dan hangen wij het erbij.
        </p>

        {/* Kim vroeg deze uitleg uitdrukkelijk: een kind dat instuurt en niets
            hoort, blijft anders elke dag kijken of zijn briefje er al hangt. */}
        <p className="mt-4 max-w-2xl rounded-md bg-info/10 px-4 py-3 text-sm text-ink">
          Wij lezen elk briefje eerst na voor het op het bord komt. Daar zit een echte mens achter,
          dus soms duurt dat even — maar we bekijken alles zo snel mogelijk. Log je in, dan zie je
          hieronder altijd wat er met jouw briefje gebeurd is.
        </p>

        {melding === "bedankt" && (
          <p className="mt-5 max-w-2xl rounded-md bg-forest/10 px-4 py-3 text-sm text-forest-dark">
            Bedankt! Je weetje is binnen. We lezen het na en hangen het erbij — kijk over een paar
            dagen nog eens.
          </p>
        )}
        {melding === "opnieuw" && (
          <p className="mt-5 max-w-2xl rounded-md bg-forest/10 px-4 py-3 text-sm text-forest-dark">
            Je aangepaste weetje is binnen. We kijken er opnieuw naar.
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
          <div className={`mt-8 ${bordKlassen}`}>
            <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
              {weetjes.map((w, nummer) => (
                <Weetje key={w.id} weetje={w} nummer={nummer} />
              ))}
            </div>
          </div>
        )}

        {eigen.length > 0 && (
          <section className="mt-10 rounded-xl border border-border bg-surface p-6">
            <h2 className="font-display text-lg font-semibold text-ink">Jouw briefjes</h2>
            <p className="mt-1 text-sm text-ink-dim">
              Dit ziet alleen jij. Hier staat wat er met elk van je weetjes gebeurd is.
            </p>

            <ul className="mt-5 space-y-4">
              {eigen.map((w) => (
                <li key={w.id} className="rounded-lg border border-border bg-paper p-4">
                  <p className="text-sm text-ink">{w.tekst}</p>

                  {w.goedgekeurd ? (
                    <p className="mt-2 text-sm text-forest-dark">
                      ✅ Het hangt op het bord. Bedankt!
                    </p>
                  ) : w.niet_geplaatst ? (
                    <>
                      <p className="mt-2 text-sm text-ink">
                        💬 We hebben dit briefje niet opgehangen.
                      </p>
                      {w.bericht && (
                        <p className="mt-1 rounded-md bg-amber/10 px-3 py-2 text-sm text-ink">
                          {w.bericht}
                        </p>
                      )}
                      {/* Niet plaatsen is geen eindpunt: pas het aan en stuur
                          het gerust opnieuw in. */}
                      <form action={verbeterWeetje} className="mt-3 grid gap-2">
                        <input type="hidden" name="id" value={w.id} />
                        <textarea
                          name="tekst"
                          rows={2}
                          required
                          maxLength={500}
                          defaultValue={w.tekst}
                          className="w-full rounded-md border border-border bg-surface px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                        />
                        <button
                          type="submit"
                          className="justify-self-start rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white transition hover:bg-forest-dark"
                        >
                          Aanpassen en opnieuw insturen
                        </button>
                      </form>
                    </>
                  ) : (
                    <p className="mt-2 text-sm text-ink-dim">
                      ⏳ We hebben het gekregen en kijken het na.
                    </p>
                  )}
                </li>
              ))}
            </ul>
          </section>
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
                Zet er alleen je voornaam bij, geen achternaam en geen adres. Klopt er iets niet
                helemaal, dan laten we het je hierboven weten en mag je het aanpassen.
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
