import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { verwijderMateriaal } from "./actions";
import { NieuwMateriaalForm } from "./NieuwMateriaalForm";

export default async function BeheerMateriaalPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const { slug } = await params;
  const { fout, succes } = await searchParams;
  const session = await requireBeheerder();
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const { data: klasje } = await supabase.from("klasjes").select("id, naam, slug").eq("slug", slug).single();
  if (!klasje) notFound();

  const { data: materialen } = await supabase
    .from("materialen")
    .select("id, type, titel, inhoud, bestandspad, created_at")
    .eq("klasje_id", klasje.id)
    .order("created_at", { ascending: false });

  return (
    <>
      <Header naam={naam} isBeheerder terugHref="/beheer" terugLabel="Beheer" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">{klasje.naam}</p>
        <h1 className="font-display text-2xl font-semibold text-ink">Lesmateriaal beheren</h1>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <ul className="mt-6 space-y-2">
          {(materialen ?? []).map((m) => (
            <li
              key={m.id}
              className="flex items-center justify-between gap-3 rounded-lg border border-border bg-surface p-3"
            >
              <div>
                <p className="text-xs uppercase tracking-wide text-ink-dim">
                  {m.type === "pdf" ? "Document" : m.type === "link" ? "Link" : "Aankondiging"}
                </p>
                <p className="font-medium text-ink">{m.titel}</p>
              </div>
              <form action={verwijderMateriaal}>
                <input type="hidden" name="id" value={m.id} />
                <input type="hidden" name="slug" value={slug} />
                <input type="hidden" name="bestandspad" value={m.bestandspad ?? ""} />
                <button type="submit" className="text-sm text-danger hover:underline">
                  Verwijderen
                </button>
              </form>
            </li>
          ))}
          {(materialen ?? []).length === 0 && (
            <li className="text-sm text-ink-dim">Nog niets toegevoegd.</li>
          )}
        </ul>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Nieuw item</h2>
          <NieuwMateriaalForm klasjeId={klasje.id} slug={slug} />
        </section>
      </main>
    </>
  );
}
