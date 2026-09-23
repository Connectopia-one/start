import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { materiaalTekst } from "@/inhoud/materiaal";
import { verwijderMateriaal } from "./actions";
import { NieuwMateriaalForm } from "./NieuwMateriaalForm";

type Rij = {
  id: string;
  groep: string;
  type: "link" | "pdf";
  titel: string;
  link: string | null;
  bestandspad: string | null;
  omschrijving: string | null;
};

export default async function BeheerMateriaalPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data, error } = await supabase
    .from("materiaal")
    .select("id, groep, type, titel, link, bestandspad, omschrijving")
    .order("groep", { ascending: true })
    .order("created_at", { ascending: true });

  const rijen = (data ?? []) as Rij[];
  const groepen = Array.from(new Set(rijen.map((r) => r.groep)));

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">
          {materiaalTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">Materiaal beheren</h1>
        <p className="mt-2 text-sm text-ink-dim">
          Wat je hier toevoegt, staat meteen op{" "}
          <Link href="/materiaal" className="text-forest underline">
            de pagina Handig materiaal
          </Link>
          . Die pagina is gratis en voor iedereen zichtbaar, ook zonder account.
        </p>

        {error && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            De lijst kon niet geladen worden: {error.message}. Heb je{" "}
            <code>supabase/materiaal.sql</code> al één keer uitgevoerd?
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
                  {m.type === "pdf" ? "Document" : "Link"} &middot; {m.groep}
                </p>
                <p className="font-medium text-ink">{m.titel}</p>
                {m.omschrijving && <p className="mt-0.5 text-sm text-ink-dim">{m.omschrijving}</p>}
                {m.link && <p className="mt-0.5 truncate text-xs text-ink-dim">{m.link}</p>}
              </div>
              <form action={verwijderMateriaal}>
                <input type="hidden" name="id" value={m.id} />
                <input type="hidden" name="bestandspad" value={m.bestandspad ?? ""} />
                <button type="submit" className="shrink-0 text-sm text-danger hover:underline">
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
          <h2 className="font-display text-lg font-semibold text-ink">Nieuw item</h2>
          <NieuwMateriaalForm groepen={groepen} />
        </section>
      </main>
    </>
  );
}
