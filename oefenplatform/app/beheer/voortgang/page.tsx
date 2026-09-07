import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

type Rij = {
  id: string;
  naam: string;
  profiles: { full_name: string } | null;
  voortgang: { id: string; correct: boolean }[];
};

export default async function BeheerVoortgangPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data: kinderen } = await supabase
    .from("kinderen")
    .select("id, naam, profiles(full_name), voortgang(id, correct)")
    .order("naam");

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Voortgang alle kinderen</h1>

        <div className="mt-6 overflow-hidden rounded-lg border border-border">
          <table className="w-full text-sm">
            <thead className="bg-paper text-left text-xs text-ink-dim">
              <tr>
                <th className="px-3 py-2">Kind</th>
                <th className="px-3 py-2">Gezin</th>
                <th className="px-3 py-2">Vragen beantwoord</th>
                <th className="px-3 py-2">Score</th>
                <th className="px-3 py-2"></th>
              </tr>
            </thead>
            <tbody>
              {((kinderen ?? []) as unknown as Rij[]).map((k) => {
                const aantal = k.voortgang.length;
                const correct = k.voortgang.filter((v) => v.correct).length;
                return (
                  <tr key={k.id} className="border-t border-border">
                    <td className="px-3 py-2 text-ink">{k.naam}</td>
                    <td className="px-3 py-2 text-ink-dim">{k.profiles?.full_name ?? "—"}</td>
                    <td className="px-3 py-2 text-ink">{aantal}</td>
                    <td className="px-3 py-2 text-ink">
                      {aantal > 0 ? `${correct}/${aantal} (${Math.round((correct / aantal) * 100)}%)` : "—"}
                    </td>
                    <td className="px-3 py-2">
                      <Link href={`/account/kinderen/${k.id}`} className="text-forest-dark hover:underline">
                        Detail &rarr;
                      </Link>
                    </td>
                  </tr>
                );
              })}
              {!kinderen?.length && (
                <tr>
                  <td colSpan={5} className="px-3 py-4 text-center text-sm text-ink-dim">
                    Nog geen kinderen geregistreerd.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </main>
    </>
  );
}
