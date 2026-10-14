import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { haalCijfers } from "@/lib/begeleidingsgroepen";

type Rij = {
  id: string;
  naam: string;
  profiles: { full_name: string } | null;
};

export default async function BeheerVoortgangPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  /* De cijfers laat de databank zelf tellen. Vroeger haalde deze tabel élk
     antwoord van élk kind op om er de lengte van te nemen; dat is zwaar, en
     boven de duizend rijen gaf de databank niet alles terug, dus klopten de
     aantallen niet meer bij een kind dat veel oefent. Zie
     lib/begeleidingsgroepen.ts. */
  const [{ data: kinderen }, cijfers] = await Promise.all([
    supabase
      .from("kinderen")
      .select("id, naam, profiles(full_name)")
      .order("naam"),
    haalCijfers(),
  ]);

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Voortgang alle kinderen
        </h1>

        <div className="mt-6 overflow-x-auto rounded-lg border border-border">
          <table className="kaartjes w-full text-sm">
            <thead className="bg-paper text-left text-xs text-ink-dim">
              <tr>
                <th className="px-3 py-2">Kind</th>
                <th className="px-3 py-2">Gezin</th>
                <th className="px-3 py-2">Vragen beantwoord</th>
                <th className="px-3 py-2">Score</th>
                <th className="px-3 py-2">Sterren</th>
                <th className="px-3 py-2">Laatst geoefend</th>
                <th className="px-3 py-2"></th>
              </tr>
            </thead>
            <tbody>
              {((kinderen ?? []) as unknown as Rij[]).map((k) => {
                const cijfer = cijfers.get(k.id);
                const aantal = cijfer?.aantal ?? 0;
                const correct = cijfer?.juist ?? 0;
                return (
                  <tr key={k.id} className="border-t border-border">
                    <td data-label="Kind" className="px-3 py-2 text-ink">
                      {k.naam}
                    </td>
                    <td data-label="Gezin" className="px-3 py-2 text-ink-dim">
                      {k.profiles?.full_name ?? "—"}
                    </td>
                    <td
                      data-label="Vragen beantwoord"
                      className="px-3 py-2 text-ink"
                    >
                      {aantal}
                    </td>
                    <td data-label="Score" className="px-3 py-2 text-ink">
                      {aantal > 0
                        ? `${correct}/${aantal} (${Math.round((correct / aantal) * 100)}%)`
                        : "—"}
                    </td>
                    <td data-label="Sterren" className="px-3 py-2 text-ink">
                      {cijfer?.sterren ? `🌟 ${cijfer.sterren}` : "—"}
                    </td>
                    <td
                      data-label="Laatst geoefend"
                      className="px-3 py-2 text-ink-dim"
                    >
                      {cijfer?.laatst
                        ? new Date(cijfer.laatst).toLocaleDateString("nl-BE", {
                            day: "numeric",
                            month: "long",
                          })
                        : "nog niet gestart"}
                    </td>
                    <td className="px-3 py-2">
                      <Link
                        href={`/account/kinderen/${k.id}`}
                        className="text-forest-dark hover:underline"
                      >
                        Detail &rarr;
                      </Link>
                    </td>
                  </tr>
                );
              })}
              {!kinderen?.length && (
                <tr>
                  <td
                    colSpan={7}
                    className="px-3 py-4 text-center text-sm text-ink-dim"
                  >
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
