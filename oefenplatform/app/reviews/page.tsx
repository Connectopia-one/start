import Link from "next/link";
import { Blaadje, bordKlassen } from "@/components/Blaadje";
import { Header } from "@/components/Header";
import { HelpOnsStappen } from "@/components/HelpOnsStappen";
import { Verzendknop } from "@/components/Verzendknop";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { stuurReviewIn } from "./acties";

/*
  Het reviewbord (Kim, 5 november 2026).

  Alleen echte reviews van echte gebruikers, niets wat wij zelf schrijven.
  Daarom:
    * insturen kan enkel met een account op het platform,
    * één review per account,
    * niets komt op het bord voor Kim het ophangt (Beheer → Enquêtes en
      reviews), en dat is geen keuze tussen goede en slechte reviews: een
      kritische review hoort er net zo goed op,
    * onder elke review staat enkel de naam die het gezin zelf koos.

  Zelfde post-its als de weetjes en de tips. Zichtbaar zonder account, zodat
  een ouder die twijfelt kan lezen wat andere gezinnen ervan vinden.
*/

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Reviews — Oefenplatform Connectopia",
  description:
    "Wat gezinnen die het oefenplatform van Connectopia gebruiken er zelf van vinden. Alleen echte reviews van gebruikers.",
};

function Sterren({ aantal }: { aantal: number }) {
  return (
    <p className="text-[18px] tracking-wide text-amber" aria-label={`${aantal} op 5 sterren`}>
      {"★".repeat(aantal)}
      <span className="text-ink/20">{"★".repeat(5 - aantal)}</span>
    </p>
  );
}

type ReviewRij = {
  id: string;
  tekst: string;
  sterren: number;
  naam_tonen: string | null;
};

export default async function ReviewsPage({
  searchParams,
}: {
  searchParams: Promise<{ melding?: string; fout?: string }>;
}) {
  const { melding, fout } = await searchParams;
  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data } = await supabase
    .from("reviews")
    .select("id, tekst, sterren, naam_tonen")
    .eq("goedgekeurd", true)
    .order("opgehangen_op", { ascending: false });
  const reviews = (data ?? []) as ReviewRij[];

  const { data: eigen } = session
    ? await supabase
        .from("reviews")
        .select("tekst, sterren, naam_tonen, goedgekeurd, niet_geplaatst, bericht")
        .eq("profile_id", session.userId)
        .maybeSingle()
    : { data: null };

  const gemiddelde =
    reviews.length > 0 ? reviews.reduce((s, r) => s + r.sterren, 0) / reviews.length : null;

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">💬 Wat gezinnen ervan vinden</h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Echte reviews van gezinnen die het oefenplatform gebruiken. Wij schrijven hier zelf
          niets bij, en we hangen ook de kritische reviews op: daar leren we het meest van.
        </p>
        {gemiddelde !== null && (
          <p className="mt-3 text-sm text-ink">
            Gemiddeld <strong>{gemiddelde.toFixed(1).replace(".", ",")}</strong> op 5 sterren, uit{" "}
            {reviews.length} review{reviews.length === 1 ? "" : "s"}.
          </p>
        )}

        {session && <HelpOnsStappen userId={session.userId} />}

        {melding === "bedankt" && (
          <p className="mt-5 max-w-2xl rounded-md bg-forest/10 px-4 py-3 text-sm text-forest-dark">
            Dank je wel voor je review! Een echte mens leest hem na voor hij op het bord komt. Dat
            kan een paar dagen duren.
          </p>
        )}
        {fout && (
          <p className="mt-5 max-w-2xl rounded-md bg-danger/10 px-4 py-3 text-sm text-danger">
            {fout}
          </p>
        )}

        {reviews.length === 0 ? (
          <p className="mt-8 text-sm text-ink-dim">
            Het bord is nog leeg. Gebruik je het platform? Dan mag jij de eerste review ophangen.
          </p>
        ) : (
          <div className={`mt-8 ${bordKlassen}`}>
            <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
              {reviews.map((r, i) => (
                <Blaadje key={r.id} nummer={i}>
                  <Sterren aantal={r.sterren} />
                  <p className="mt-2 whitespace-pre-line text-[17px] leading-relaxed text-ink">
                    {r.tekst}
                  </p>
                  {r.naam_tonen && (
                    <p className="mt-3 text-[14px] text-ink-dim">— {r.naam_tonen}</p>
                  )}
                </Blaadje>
              ))}
            </div>
          </div>
        )}

        {eigen && (
          <section id="jouw-review" className="mt-10 rounded-xl border border-border bg-surface p-6">
            <h2 className="font-display text-lg font-semibold text-ink">Jouw review</h2>
            <p className="mt-1 text-sm text-ink-dim">Dit ziet alleen jij.</p>
            <div className="mt-4 rounded-lg border border-border bg-paper p-4">
              <Sterren aantal={eigen.sterren} />
              <p className="mt-2 whitespace-pre-line text-sm text-ink">{eigen.tekst}</p>
              {eigen.goedgekeurd ? (
                <p className="mt-2 text-sm text-forest-dark">✅ Hij hangt op het bord. Dank je wel!</p>
              ) : eigen.niet_geplaatst ? (
                <>
                  <p className="mt-2 text-sm text-ink">💬 We hebben hem nog niet opgehangen.</p>
                  {eigen.bericht && (
                    <p className="mt-1 rounded-md bg-amber/10 px-3 py-2 text-sm text-ink">
                      {eigen.bericht}
                    </p>
                  )}
                </>
              ) : (
                <p className="mt-2 text-sm text-ink-dim">⏳ We hebben hem gekregen en lezen hem na.</p>
              )}
            </div>
          </section>
        )}

        <section id="schrijf" className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            {eigen && !eigen.goedgekeurd ? "Je review aanpassen" : "Schrijf een review"}
          </h2>

          {!session ? (
            <p className="mt-2 text-sm text-ink-dim">
              Een review schrijven kan als je het platform gebruikt.{" "}
              <Link href="/login" className="text-forest-dark underline underline-offset-2">
                Log in
              </Link>{" "}
              met je account.
            </p>
          ) : eigen?.goedgekeurd ? (
            <p className="mt-2 text-sm text-ink-dim">
              Je review hangt al op het bord. Wil je iets veranderen? Mail ons gerust op
              info@matmgroep.com.
            </p>
          ) : (
            <>
              <p className="mt-2 max-w-2xl text-sm text-ink-dim">
                Vertel eerlijk hoe het oefenen bij jullie loopt: wat goed werkt, en wat beter kan.
                Eén review per gezin. Wij lezen hem na voor hij op het bord komt.
              </p>

              <form action={stuurReviewIn} className="mt-5 grid max-w-xl gap-4">
                <fieldset className="grid gap-2 text-sm">
                  <legend className="text-ink">Hoeveel sterren geef je?</legend>
                  <div className="flex gap-2">
                    {[1, 2, 3, 4, 5].map((n) => (
                      <label
                        key={n}
                        className="cursor-pointer rounded-md border border-border bg-paper px-3 py-1.5 text-amber has-[:checked]:border-forest has-[:checked]:bg-forest/10"
                      >
                        <input
                          type="radio"
                          name="sterren"
                          value={n}
                          required
                          defaultChecked={eigen?.sterren === n}
                          className="sr-only"
                        />
                        {"★".repeat(n)}
                      </label>
                    ))}
                  </div>
                </fieldset>

                <label className="grid gap-1 text-sm">
                  <span className="text-ink">Je review</span>
                  <textarea
                    name="tekst"
                    rows={5}
                    required
                    minLength={20}
                    maxLength={1200}
                    defaultValue={eigen?.tekst ?? ""}
                    placeholder={'Bv. "Mijn dochter oefent graag, vooral de vraag van de dag. De uitleg bij een fout helpt echt." of "Rustig platform, maar het starten was zoeken en ik mis nog oefeningen Frans."'}
                    className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                </label>

                <label className="grid gap-1 text-sm">
                  <span className="text-ink">Welke naam mag eronder staan? (mag je openlaten)</span>
                  <input
                    type="text"
                    name="naam_tonen"
                    maxLength={60}
                    defaultValue={eigen?.naam_tonen ?? ""}
                    placeholder="Bijvoorbeeld: Anja, mama van Thibo"
                    className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                  <span className="text-xs text-ink-dim">
                    Geen achternaam van je kind, en geen adres.
                  </span>
                </label>

                <label className="flex items-start gap-2 text-sm text-ink">
                  <input type="checkbox" name="toestemming" value="ja" required className="mt-1 accent-forest" />
                  <span>
                    Ik geef toestemming om deze review op het reviewbord van het oefenplatform te
                    tonen.
                  </span>
                </label>

                <Verzendknop
                  label={eigen ? "Aanpassen en opnieuw insturen" : "Review insturen"}
                  bezigLabel="Bezig met versturen…"
                  className="justify-self-start rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
                />
              </form>
            </>
          )}
        </section>
      </main>
    </>
  );
}
