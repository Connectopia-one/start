import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBegeleider } from "@/lib/auth";
import { haalGroepen, ZONDER_GROEP } from "@/lib/begeleidingsgroepen";
import { begeleidingTekst as t } from "@/inhoud/begeleiding";

export const metadata = {
  title: "Opvolging — Oefenplatform Connectopia",
};

/*
  De opvolging, per groep.

  Tot 6 oktober 2026 stond hier één lijst met álle plusklaskinderen door
  elkaar. Kim: "ik wou de groep van de plusklas apart opvolgen van de
  testgroepen, maar iedereen staat overal", en daarna: "of dat ik kan filteren
  erop".

  Dus: een rij knoppen bovenaan met één knop per code, en daaronder alleen de
  kinderen van de groep die aanstaat. Welke groep dat is zit in het webadres
  (?groep=...), zodat je een groep kan bewaren als bladwijzer en de terugknop
  van de browser werkt. Bij welke groep een gezin hoort, hangt af van de code
  waarmee het registreerde; zie lib/begeleidingsgroepen.ts en
  supabase/groepen.sql.
*/
export default async function BegeleidingPage({
  searchParams,
}: {
  searchParams: Promise<{ groep?: string }>;
}) {
  const session = await requireBegeleider();
  const { groep: gevraagd } = await searchParams;
  const groepen = await haalGroepen();

  // De gevraagde groep, anders de eerste die kinderen heeft, anders de eerste.
  const gekozen =
    groepen.find((g) => g.sleutel === gevraagd) ??
    groepen.find((g) => g.kinderen.length > 0) ??
    groepen[0];

  const totaal = groepen.reduce((som, g) => som + g.kinderen.length, 0);

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {t.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {t.groepen.titel}
        </h1>
        <p className="mt-3 text-sm text-ink-dim">{t.groepen.intro}</p>

        {groepen.length === 0 ? (
          <p className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            {t.groepen.leeg}
          </p>
        ) : (
          <>
            {/* De filterknoppen: één per groep, met het aantal kinderen erbij. */}
            <nav
              aria-label={t.groepen.filterLabel}
              className="mt-5 flex flex-wrap gap-2"
            >
              {groepen.map((g) => {
                const aan = g.sleutel === gekozen?.sleutel;
                return (
                  <Link
                    key={g.sleutel}
                    href={`/begeleiding?groep=${encodeURIComponent(g.sleutel)}`}
                    aria-current={aan ? "page" : undefined}
                    className={`rounded-full border px-4 py-1.5 text-sm font-medium transition ${
                      aan
                        ? "border-forest bg-forest text-white"
                        : "border-border bg-surface text-ink hover:border-forest/50"
                    }`}
                  >
                    {g.label || g.naam}
                    <span
                      className={aan ? "ml-2 text-white/70" : "ml-2 text-ink-dim"}
                    >
                      {g.kinderen.length}
                    </span>
                  </Link>
                );
              })}
            </nav>

            {totaal === 0 && (
              <p className="mt-5 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
                {t.leegTekst}
              </p>
            )}

            {gekozen && (
              <>
                <div className="mt-6 flex flex-wrap items-baseline gap-x-3 gap-y-1">
                  <h2 className="font-display text-lg font-semibold text-ink">
                    {gekozen.label || gekozen.naam}
                  </h2>
                  {gekozen.sleutel !== ZONDER_GROEP && (
                    <p className="font-mono text-xs text-ink-dim">
                      {gekozen.naam}
                    </p>
                  )}
                  {!gekozen.actief && (
                    <span className="rounded-full bg-ink-dim/10 px-2.5 py-0.5 text-xs text-ink-dim">
                      {t.groepen.inactief}
                    </span>
                  )}
                </div>

                {gekozen.sleutel === ZONDER_GROEP && (
                  <p className="mt-3 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
                    {t.groepen.zonderGroepUitleg}
                  </p>
                )}

                {gekozen.kinderen.length === 0 ? (
                  <p className="mt-4 rounded-xl border border-border bg-surface px-5 py-4 text-sm text-ink-dim">
                    {t.groepen.groepLeeg}
                  </p>
                ) : (
                  <div className="mt-4 overflow-x-auto rounded-lg border border-border">
                    <table className="w-full text-sm">
                      <thead className="bg-paper text-left text-xs text-ink-dim">
                        <tr>
                          <th className="px-3 py-2">Kind</th>
                          <th className="px-3 py-2">Gezin</th>
                          <th className="px-3 py-2">Vragen</th>
                          <th className="px-3 py-2">Score</th>
                          <th className="px-3 py-2">Stickers</th>
                          <th className="px-3 py-2"></th>
                        </tr>
                      </thead>
                      <tbody>
                        {gekozen.kinderen.map((k) => {
                          const aantal = k.voortgang.length;
                          const correct = k.voortgang.filter(
                            (v) => v.correct,
                          ).length;
                          return (
                            <tr key={k.id} className="border-t border-border">
                              <td className="px-3 py-2 font-medium text-ink">
                                {k.naam}
                              </td>
                              <td className="px-3 py-2 text-ink-dim">
                                {k.profiles?.full_name ?? "—"}
                              </td>
                              <td className="px-3 py-2 text-ink">
                                {aantal || "—"}
                              </td>
                              <td className="px-3 py-2 text-ink">
                                {aantal > 0
                                  ? `${correct}/${aantal} (${Math.round((correct / aantal) * 100)}%)`
                                  : "—"}
                              </td>
                              <td className="px-3 py-2 text-ink">
                                {k.stickers.length
                                  ? `🌟 ${k.stickers.length}`
                                  : "—"}
                              </td>
                              <td className="px-3 py-2">
                                <Link
                                  href={`/begeleiding/${k.id}?groep=${encodeURIComponent(gekozen.sleutel)}`}
                                  className="font-medium text-forest-dark hover:underline"
                                >
                                  Fiche &rarr;
                                </Link>
                              </td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                )}
              </>
            )}
          </>
        )}
      </main>
    </>
  );
}
