import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { zetRol } from "./actions";

type Rij = {
  id: string;
  full_name: string;
  role: string;
  is_plusklas: boolean;
};

export const metadata = { title: "Begeleiders — Oefenplatform Connectopia" };

export default async function BegeleidersPage() {
  const session = await requireBeheerder();

  /*
    De leesregel op profiles laat een beheerder alles zien, maar we gebruiken
    hier de service-sleutel omdat we ook accounts zonder kind willen tonen.
  */
  const admin = createAdminClient();
  const { data } = await admin
    .from("profiles")
    .select("id, full_name, role, is_plusklas")
    .order("full_name");

  const rijen = (data ?? []) as Rij[];
  const begeleiders = rijen.filter((r) => r.role === "begeleider");
  const rest = rijen.filter((r) => r.role !== "begeleider");

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Begeleiders
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Een begeleider kan de opvolgfiches van de plusklaskinderen bekijken,
          er opmerkingen bij schrijven en werk opladen. Een begeleider komt niet
          in dit beheerscherm en ziet niets van gezinnen buiten de plusklas.
        </p>

        <section className="mt-8">
          <h2 className="font-display text-lg font-semibold text-ink">
            Nu begeleider ({begeleiders.length})
          </h2>
          {begeleiders.length === 0 ? (
            <p className="mt-2 text-sm text-ink-dim">
              Nog niemand. Kies hieronder een account uit de lijst.
            </p>
          ) : (
            <ul className="mt-3 space-y-2">
              {begeleiders.map((r) => (
                <li
                  key={r.id}
                  className="flex items-center justify-between gap-3 rounded-lg border border-border bg-surface px-4 py-3"
                >
                  <span className="text-sm font-medium text-ink">
                    {r.full_name}
                  </span>
                  <form action={zetRol}>
                    <input type="hidden" name="id" value={r.id} />
                    <input type="hidden" name="rol" value="ouder" />
                    <button
                      type="submit"
                      className="text-sm text-ink-dim underline-offset-2 hover:text-danger hover:underline"
                    >
                      Geen begeleider meer
                    </button>
                  </form>
                </li>
              ))}
            </ul>
          )}
        </section>

        <section className="mt-10">
          <h2 className="font-display text-lg font-semibold text-ink">
            Alle andere accounts
          </h2>
          <div className="mt-3 overflow-hidden rounded-lg border border-border">
            <table className="w-full text-sm">
              <thead className="bg-paper text-left text-xs text-ink-dim">
                <tr>
                  <th className="px-3 py-2">Naam</th>
                  <th className="px-3 py-2">Rol</th>
                  <th className="px-3 py-2">Plusklas</th>
                  <th className="px-3 py-2"></th>
                </tr>
              </thead>
              <tbody>
                {rest.map((r) => (
                  <tr key={r.id} className="border-t border-border">
                    <td className="px-3 py-2 text-ink">{r.full_name}</td>
                    <td className="px-3 py-2 text-ink-dim">{r.role}</td>
                    <td className="px-3 py-2 text-ink-dim">
                      {r.is_plusklas ? "ja" : "—"}
                    </td>
                    <td className="px-3 py-2">
                      {r.role === "beheerder" || r.id === session.userId ? (
                        <span className="text-xs text-ink-dim">—</span>
                      ) : (
                        <form action={zetRol}>
                          <input type="hidden" name="id" value={r.id} />
                          <input type="hidden" name="rol" value="begeleider" />
                          <button
                            type="submit"
                            className="text-sm font-medium text-forest-dark hover:underline"
                          >
                            Begeleider maken
                          </button>
                        </form>
                      )}
                    </td>
                  </tr>
                ))}
                {rest.length === 0 && (
                  <tr>
                    <td
                      colSpan={4}
                      className="px-3 py-4 text-center text-sm text-ink-dim"
                    >
                      Geen andere accounts.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </>
  );
}
