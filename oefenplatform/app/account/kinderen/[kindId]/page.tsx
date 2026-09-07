import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

type Rij = {
  id: string;
  correct: boolean;
  beantwoord_op: string;
  vragen: {
    id: string;
    hoofdstukken: {
      id: string;
      titel: string;
      vakken: { id: string; naam: string };
    };
  };
};

type HoofdstukStat = { titel: string; aantal: number; correct: number; laatst: string };
type VakStat = { naam: string; hoofdstukken: Map<string, HoofdstukStat> };

export default async function KindVoortgangPage({
  params,
}: {
  params: Promise<{ kindId: string }>;
}) {
  const session = await requireIngelogd();
  const { kindId } = await params;
  const supabase = await createClient();

  const { data: kind } = await supabase.from("kinderen").select("id, naam, profile_id").eq("id", kindId).single();
  if (!kind || (kind.profile_id !== session.userId && session.profile?.role !== "beheerder")) notFound();

  const { data: rijen } = await supabase
    .from("voortgang")
    .select("id, correct, beantwoord_op, vragen(id, hoofdstukken(id, titel, vakken(id, naam)))")
    .eq("kind_id", kindId)
    .order("beantwoord_op", { ascending: false });

  const vakken = new Map<string, VakStat>();
  let totaalAantal = 0;
  let totaalCorrect = 0;

  for (const rij of (rijen ?? []) as unknown as Rij[]) {
    const hoofdstuk = rij.vragen?.hoofdstukken;
    const vak = hoofdstuk?.vakken;
    if (!hoofdstuk || !vak) continue;

    totaalAantal += 1;
    if (rij.correct) totaalCorrect += 1;

    if (!vakken.has(vak.id)) vakken.set(vak.id, { naam: vak.naam, hoofdstukken: new Map() });
    const vakStat = vakken.get(vak.id)!;
    if (!vakStat.hoofdstukken.has(hoofdstuk.id)) {
      vakStat.hoofdstukken.set(hoofdstuk.id, { titel: hoofdstuk.titel, aantal: 0, correct: 0, laatst: rij.beantwoord_op });
    }
    const hStat = vakStat.hoofdstukken.get(hoofdstuk.id)!;
    hStat.aantal += 1;
    if (rij.correct) hStat.correct += 1;
    if (rij.beantwoord_op > hStat.laatst) hStat.laatst = rij.beantwoord_op;
  }

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href="/account" className="text-sm text-ink-dim hover:text-ink">
          &larr; Mijn account
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Voortgang — {kind.naam}</h1>

        {totaalAantal > 0 ? (
          <p className="mt-1 text-sm text-ink-dim">
            In totaal {totaalAantal} vraag{totaalAantal === 1 ? "" : "en"} beantwoord, waarvan{" "}
            {totaalCorrect} juist ({Math.round((totaalCorrect / totaalAantal) * 100)}%).
          </p>
        ) : (
          <p className="mt-1 text-sm text-ink-dim">Nog geen vragen beantwoord.</p>
        )}

        <div className="mt-6 space-y-6">
          {[...vakken.entries()].map(([vakId, vak]) => (
            <section key={vakId}>
              <h2 className="font-display text-lg font-semibold text-forest-dark">{vak.naam}</h2>
              <div className="mt-2 overflow-hidden rounded-lg border border-border">
                <table className="w-full text-sm">
                  <thead className="bg-paper text-left text-xs text-ink-dim">
                    <tr>
                      <th className="px-3 py-2">Hoofdstuk</th>
                      <th className="px-3 py-2">Score</th>
                      <th className="px-3 py-2">Laatst geoefend</th>
                    </tr>
                  </thead>
                  <tbody>
                    {[...vak.hoofdstukken.values()].map((h) => (
                      <tr key={h.titel} className="border-t border-border">
                        <td className="px-3 py-2 text-ink">{h.titel}</td>
                        <td className="px-3 py-2 text-ink">
                          {h.correct}/{h.aantal} ({Math.round((h.correct / h.aantal) * 100)}%)
                        </td>
                        <td className="px-3 py-2 text-ink-dim">
                          {new Date(h.laatst).toLocaleDateString("nl-BE", { day: "numeric", month: "short", year: "numeric" })}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          ))}
        </div>
      </main>
    </>
  );
}
