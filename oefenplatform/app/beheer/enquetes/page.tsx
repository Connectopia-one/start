import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { huidigSchooljaar } from "@/lib/schooljaar";
import { ALLE_VRAGEN, type EnqueteAntwoorden } from "@/inhoud/enquete";
import {
  keurGoed,
  trekGoedkeuringIn,
  zetReviewNietGeplaatst,
  zetReviewOpgehangen,
} from "./actions";

/*
  Beheer → Enquêtes en reviews (Kim, 5 november 2026).

  Per gezin dat iets instuurde: de enquête (privé), de review (voor het bord)
  en Kims knop om goed te keuren. Bovenaan de tellers, zodat Kim achteraf
  feitelijk kan zeggen hoeveel gezinnen hielpen testen.

  Met de service-sleutel, want de mailadressen staan in auth.users.
*/

export const dynamic = "force-dynamic";
export const metadata = { title: "Enquêtes en reviews — Oefenplatform Connectopia" };

const TESTCODE = "TOPTESTER2026";

type Profiel = {
  id: string;
  full_name: string;
  role: string;
  is_plusklas: boolean;
  toegang_schooljaar: string | null;
  plusklas_code: string | null;
  gratis_tot?: string | null;
  vaste_prijs_eur?: number | null;
};

function datum(iso: string) {
  return new Date(iso).toLocaleDateString("nl-BE", { day: "numeric", month: "long" });
}

export default async function BeheerEnquetesPage() {
  const session = await requireBeheerder();
  const admin = createAdminClient();
  const schooljaar = huidigSchooljaar();

  const [enq, rev, bel, prof] = await Promise.all([
    admin.from("enquetes").select("profile_id, antwoorden, ingestuurd_op, bijgewerkt_op"),
    admin
      .from("reviews")
      .select("id, profile_id, tekst, sterren, naam_tonen, goedgekeurd, niet_geplaatst, bericht, aangemaakt_op"),
    admin.from("beloningen").select("profile_id, soort, goedgekeurd_op"),
    admin.from("profiles").select("*"),
  ]);

  if (enq.error || rev.error || bel.error) {
    return (
      <>
        <Header naam={session.profile?.full_name} rol="beheerder" />
        <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
          <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
            &larr; Beheer
          </Link>
          <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Enquêtes en reviews</h1>
          <p className="mt-4 rounded-md bg-amber/10 px-4 py-3 text-sm text-ink">
            De databank is hier nog niet klaar voor. Draai eerst{" "}
            <code>supabase/enquete-en-reviews.sql</code> in de SQL-editor van het oefenplatform.
          </p>
        </main>
      </>
    );
  }

  const profielen = (prof.data ?? []) as Profiel[];
  const profielPerId = new Map(profielen.map((p) => [p.id, p]));
  const enquetePerId = new Map((enq.data ?? []).map((e) => [e.profile_id, e]));
  const reviewPerId = new Map((rev.data ?? []).map((r) => [r.profile_id, r]));
  const beloningPerId = new Map((bel.data ?? []).map((b) => [b.profile_id, b]));

  const mailPerId = new Map<string, string>();
  for (let bladzijde = 1; bladzijde <= 10; bladzijde++) {
    const { data: lijst, error } = await admin.auth.admin.listUsers({ page: bladzijde, perPage: 200 });
    const gebruikers = lijst?.users ?? [];
    for (const u of gebruikers) if (u.email) mailPerId.set(u.id, u.email);
    if (error || gebruikers.length < 200) break;
  }

  const ids = [...new Set([...enquetePerId.keys(), ...reviewPerId.keys()])];
  const gezinnen = ids
    .map((id) => ({
      id,
      profiel: profielPerId.get(id),
      enquete: enquetePerId.get(id),
      review: reviewPerId.get(id),
      beloning: beloningPerId.get(id),
    }))
    // Eerst wie op jou wacht (allebei binnen, nog niet goedgekeurd), dan de rest.
    .sort((a, b) => {
      const wacht = (g: typeof a) => (g.enquete && g.review && !g.beloning ? 0 : g.beloning ? 2 : 1);
      return wacht(a) - wacht(b);
    });

  const testers = profielen.filter((p) => p.plusklas_code === TESTCODE).length;
  const allebei = gezinnen.filter((g) => g.enquete && g.review).length;
  const goedgekeurd = gezinnen.filter((g) => g.beloning).length;
  const reviewsWachten = (rev.data ?? []).filter((r) => !r.goedgekeurd && !r.niet_geplaatst).length;

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Enquêtes en reviews</h1>
        <p className="mt-1 text-sm text-ink-dim">
          De enquête lees alleen jij. Een review komt pas op{" "}
          <Link href="/reviews" className="text-forest-dark hover:underline">
            het reviewbord
          </Link>{" "}
          als jij hem ophangt, en gratis toegang of de vaste prijs gaat pas aan als jij goedkeurt.
        </p>

        <dl className="mt-6 grid grid-cols-2 gap-3 text-sm sm:grid-cols-5">
          {[
            ["Testgezinnen", testers],
            ["Enquêtes", enquetePerId.size],
            ["Reviews", reviewPerId.size],
            ["Allebei", allebei],
            ["Goedgekeurd", goedgekeurd],
          ].map(([label, n]) => (
            <div key={label} className="rounded-lg border border-border bg-surface px-3 py-2">
              <dt className="text-xs text-ink-dim">{label}</dt>
              <dd className="font-display text-xl font-semibold text-ink">{n}</dd>
            </div>
          ))}
        </dl>
        {reviewsWachten > 0 && (
          <p className="mt-3 text-sm text-ink">
            {reviewsWachten} review{reviewsWachten === 1 ? " wacht" : "s wachten"} om opgehangen te
            worden.
          </p>
        )}

        <div className="mt-8 space-y-5">
          {gezinnen.length === 0 && (
            <p className="text-sm text-ink-dim">
              Er is nog niets ingestuurd. Zodra een gezin de{" "}
              <Link href="/enquete" className="text-forest-dark hover:underline">
                enquête
              </Link>{" "}
              of een review instuurt, staat het hier.
            </p>
          )}

          {gezinnen.map(({ id, profiel, enquete, review, beloning }) => {
            const betaald = profiel?.toegang_schooljaar === schooljaar;
            const tester = profiel?.plusklas_code === TESTCODE;
            const antwoorden = (enquete?.antwoorden ?? {}) as EnqueteAntwoorden;
            const soort = betaald ? "vaste_prijs" : "gratis_toegang";

            return (
              <article
                key={id}
                className={`rounded-xl border px-5 py-4 text-sm ${
                  enquete && review && !beloning ? "border-amber/40 bg-surface" : "border-border bg-paper"
                }`}
              >
                <div className="flex flex-wrap items-baseline justify-between gap-2">
                  <h2 className="font-display text-base font-semibold text-ink">
                    {profiel?.full_name ?? "Onbekend account"}
                  </h2>
                  <span className="text-xs text-ink-dim">
                    {mailPerId.get(id) ?? ""}
                    {tester ? " · testgroep" : ""}
                    {betaald ? " · betaald" : ""}
                    {profiel?.is_plusklas && !tester ? ` · code ${profiel.plusklas_code ?? "van jou"}` : ""}
                  </span>
                </div>

                <p className="mt-2 text-ink">
                  {enquete ? "✅" : "⬜"} enquête{" "}
                  {enquete ? <span className="text-ink-dim">({datum(enquete.bijgewerkt_op)})</span> : null}
                  {" · "}
                  {review ? "✅" : "⬜"} review{" "}
                  {review ? <span className="text-ink-dim">({datum(review.aangemaakt_op)})</span> : null}
                </p>

                {enquete && (
                  <details className="mt-3 rounded-lg border border-border bg-surface px-4 py-3">
                    <summary className="cursor-pointer text-ink">De antwoorden lezen</summary>
                    <dl className="mt-3 grid gap-3">
                      {ALLE_VRAGEN.map((v) => {
                        const a = antwoorden[v.sleutel];
                        const tekst = Array.isArray(a) ? a.join(", ") : a;
                        return (
                          <div key={v.sleutel}>
                            <dt className="text-xs text-ink-dim">{v.vraag}</dt>
                            <dd className="whitespace-pre-line text-ink">{tekst || "—"}</dd>
                          </div>
                        );
                      })}
                    </dl>
                  </details>
                )}

                {review && (
                  <div className="mt-3 rounded-lg border border-border bg-surface px-4 py-3">
                    <p className="text-amber">
                      {"★".repeat(review.sterren)}
                      <span className="text-ink/20">{"★".repeat(5 - review.sterren)}</span>
                    </p>
                    <p className="mt-1 whitespace-pre-line text-ink">{review.tekst}</p>
                    {review.naam_tonen && (
                      <p className="mt-1 text-xs text-ink-dim">— {review.naam_tonen}</p>
                    )}
                    <div className="mt-3 flex flex-wrap items-end gap-3">
                      <form action={zetReviewOpgehangen}>
                        <input type="hidden" name="id" value={review.id} />
                        <input type="hidden" name="naar" value={review.goedgekeurd ? "false" : "true"} />
                        <button
                          type="submit"
                          className={
                            review.goedgekeurd
                              ? "text-ink-dim hover:text-ink"
                              : "rounded-md bg-forest px-3 py-1.5 font-medium text-white hover:bg-forest-dark"
                          }
                        >
                          {review.goedgekeurd ? "Van het bord halen" : "Ophangen op het reviewbord"}
                        </button>
                      </form>
                      {!review.goedgekeurd && !review.niet_geplaatst && (
                        <form action={zetReviewNietGeplaatst} className="flex flex-wrap items-end gap-2">
                          <input type="hidden" name="id" value={review.id} />
                          <input
                            type="text"
                            name="bericht"
                            maxLength={500}
                            placeholder="Woordje voor het gezin, bv. een achternaam weglaten"
                            className="w-64 max-w-full rounded-md border border-border bg-paper px-3 py-1.5 text-sm text-ink outline-none focus:border-forest"
                          />
                          <button
                            type="submit"
                            className="rounded-md border border-border px-3 py-1.5 text-ink-dim hover:border-danger hover:text-danger"
                          >
                            Niet ophangen
                          </button>
                        </form>
                      )}
                      {review.niet_geplaatst && (
                        <span className="text-xs text-ink-dim">
                          Niet opgehangen{review.bericht ? `: "${review.bericht}"` : ""}
                        </span>
                      )}
                    </div>
                  </div>
                )}

                <div className="mt-4 flex flex-wrap items-center gap-3">
                  {beloning ? (
                    <>
                      <span className="rounded-full bg-forest/10 px-3 py-1 text-xs font-medium text-forest-dark">
                        {beloning.soort === "vaste_prijs"
                          ? "Goedgekeurd: vaste prijs 20 euro"
                          : "Goedgekeurd: gratis toegang t.e.m. 31 augustus 2027"}{" "}
                        ({datum(beloning.goedgekeurd_op)})
                      </span>
                      <form action={trekGoedkeuringIn}>
                        <input type="hidden" name="profile_id" value={id} />
                        <button type="submit" className="text-xs text-ink-dim hover:text-danger">
                          Goedkeuring intrekken
                        </button>
                      </form>
                    </>
                  ) : enquete && review ? (
                    <form action={keurGoed}>
                      <input type="hidden" name="profile_id" value={id} />
                      <input type="hidden" name="soort" value={soort} />
                      <button
                        type="submit"
                        className="rounded-md bg-forest px-3 py-1.5 font-medium text-white hover:bg-forest-dark"
                      >
                        {soort === "vaste_prijs"
                          ? "Goedkeuren: vaste prijs 20 euro"
                          : "Goedkeuren: gratis toegang t.e.m. 31 augustus 2027"}
                      </button>
                    </form>
                  ) : (
                    <span className="text-xs text-ink-dim">
                      Goedkeuren kan zodra de enquête én de review binnen zijn.
                    </span>
                  )}
                </div>
              </article>
            );
          })}
        </div>
      </main>
    </>
  );
}
