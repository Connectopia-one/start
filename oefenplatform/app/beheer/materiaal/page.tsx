import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { materiaalTekst } from "@/inhoud/materiaal";
import { verwijderMateriaal, wijzigMateriaalPlek } from "./actions";
import { schoolVan, soortVan } from "@/inhoud/extras";
import { NieuwMateriaalForm } from "./NieuwMateriaalForm";

type Rij = {
  id: string;
  groep: string;
  type: "link" | "pdf";
  titel: string;
  link: string | null;
  bestandspad: string | null;
  omschrijving: string | null;
  soort?: string | null;
  schoolniveau?: string | null;
};

export default async function BeheerMateriaalPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data, error } = await supabase
    .from("materiaal")
    .select("*")
    .order("created_at", { ascending: true });

  const rijen = (data ?? []) as Rij[];
  /* Zijn de kolommen soort en schoolniveau er al? (supabase/materiaal-soort.sql) */
  const groepen = Array.from(
    new Set(rijen.map((r) => r.groep).filter((g) => g && g !== "Allerlei")),
  );
  const kolommenKlaar = rijen.length === 0 || rijen.some((r) => "soort" in r);

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">
          {materiaalTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          Materiaal beheren
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Wat je hier toevoegt, staat meteen op{" "}
          <Link href="/extras" className="text-forest underline">
            de pagina Leuke extra&apos;s
          </Link>
          . Die pagina is gratis en voor iedereen zichtbaar, ook zonder account.
        </p>

        {error && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            De lijst kon niet geladen worden: {error.message}. Heb je{" "}
            <code>supabase/materiaal.sql</code> al één keer uitgevoerd?
          </p>
        )}

        {!kolommenKlaar && (
          <p className="mt-4 rounded-md bg-amber/10 px-3 py-2 text-sm text-ink">
            Voer eerst <code>supabase/materiaal-soort.sql</code> één keer uit in
            Supabase. Daarna kan je bij elk item kiezen onder welke knop het
            staat en voor wie het is.
          </p>
        )}

        <ul className="mt-6 space-y-2">
          {rijen.map((m) => (
            <li
              key={m.id}
              className="flex items-start justify-between gap-3 rounded-lg border border-border bg-surface p-3"
            >
              <div className="min-w-0">
                <p className="text-xs uppercase tracking-wide text-ink-dim">
                  {m.type === "pdf" ? "PDF" : "Link"}
                  {m.groep && m.groep !== "Allerlei" ? (
                    <> &middot; {m.groep}</>
                  ) : null}
                </p>
                <p className="font-medium text-ink">{m.titel}</p>
                {m.omschrijving && (
                  <p className="mt-0.5 text-sm text-ink-dim">
                    {m.omschrijving}
                  </p>
                )}
                {m.link && (
                  <p className="mt-0.5 truncate text-xs text-ink-dim">
                    {m.link}
                  </p>
                )}
                {kolommenKlaar && (
                  <form
                    action={wijzigMateriaalPlek}
                    className="mt-2 flex flex-wrap items-center gap-2 text-xs"
                  >
                    <input type="hidden" name="id" value={m.id} />
                    <select
                      name="soort"
                      defaultValue={soortVan(m)}
                      className="rounded border border-border bg-paper px-2 py-1"
                    >
                      <option value="links">🔗 Leuke links</option>
                      <option value="documenten">
                        🖨️ Afdrukbare documenten
                      </option>
                      <option value="filmpjes">🎬 Leuke filmpjes</option>
                    </select>
                    <select
                      name="schoolniveau"
                      defaultValue={schoolVan(m)}
                      className="rounded border border-border bg-paper px-2 py-1"
                    >
                      <option value="lager">Lagere school</option>
                      <option value="middelbaar">Middelbare school</option>
                      <option value="iedereen">Voor iedereen</option>
                    </select>
                    <button
                      type="submit"
                      className="text-forest-dark hover:underline"
                    >
                      Bewaren
                    </button>
                  </form>
                )}
              </div>
              <form action={verwijderMateriaal}>
                <input type="hidden" name="id" value={m.id} />
                <input
                  type="hidden"
                  name="bestandspad"
                  value={m.bestandspad ?? ""}
                />
                <button
                  type="submit"
                  className="shrink-0 text-sm text-danger hover:underline"
                >
                  Verwijderen
                </button>
              </form>
            </li>
          ))}
          {rijen.length === 0 && !error && (
            <li className="text-sm text-ink-dim">Nog niets toegevoegd.</li>
          )}
        </ul>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            Nieuw item
          </h2>
          <NieuwMateriaalForm groepen={groepen} />
        </section>
      </main>
    </>
  );
}
