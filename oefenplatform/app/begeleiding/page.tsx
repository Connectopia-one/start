import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBegeleider } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { begeleidingTekst as t } from "@/inhoud/begeleiding";

type Rij = {
  id: string;
  naam: string;
  profiles: { full_name: string; is_plusklas: boolean } | null;
  voortgang: { id: string; correct: boolean }[];
  stickers: { id: string }[];
};

export const metadata = {
  title: "Opvolging plusklas — Oefenplatform Connectopia",
};

export default async function BegeleidingPage() {
  const session = await requireBegeleider();
  const supabase = await createClient();

  /*
    Een begeleider krijgt door de regels in de databank alleen plusklaskinderen
    te zien. Voor jou als beheerder staan alle kinderen open, dus filteren we
    hier nog eens expliciet op het gezin — anders zie jij wél iedereen staan.
  */
  const { data } = await supabase
    .from("kinderen")
    .select(
      "id, naam, profiles(full_name, is_plusklas), voortgang(id, correct), stickers(id)",
    )
    .order("naam");

  const kinderen = ((data ?? []) as unknown as Rij[]).filter(
    (k) => k.profiles?.is_plusklas,
  );

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {t.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {t.titel}
        </h1>
        <p className="mt-3 text-sm text-ink-dim">{t.intro}</p>

        {kinderen.length === 0 ? (
          <p className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            {t.leegTekst}
          </p>
        ) : (
          <div className="mt-6 overflow-hidden rounded-lg border border-border">
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
                {kinderen.map((k) => {
                  const aantal = k.voortgang.length;
                  const correct = k.voortgang.filter((v) => v.correct).length;
                  return (
                    <tr key={k.id} className="border-t border-border">
                      <td className="px-3 py-2 font-medium text-ink">
                        {k.naam}
                      </td>
                      <td className="px-3 py-2 text-ink-dim">
                        {k.profiles?.full_name ?? "—"}
                      </td>
                      <td className="px-3 py-2 text-ink">{aantal || "—"}</td>
                      <td className="px-3 py-2 text-ink">
                        {aantal > 0
                          ? `${correct}/${aantal} (${Math.round((correct / aantal) * 100)}%)`
                          : "—"}
                      </td>
                      <td className="px-3 py-2 text-ink">
                        {k.stickers.length ? `🌟 ${k.stickers.length}` : "—"}
                      </td>
                      <td className="px-3 py-2">
                        <Link
                          href={`/begeleiding/${k.id}`}
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
      </main>
    </>
  );
}
