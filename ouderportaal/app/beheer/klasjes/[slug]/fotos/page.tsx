import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { voegFotosToe, verwijderFoto } from "./actions";

export default async function BeheerFotosPage({
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

  const { data: fotosData } = await supabase
    .from("fotos")
    .select("id, bestandspad, bijschrift, created_at")
    .eq("klasje_id", klasje.id)
    .order("created_at", { ascending: false });

  const fotos = fotosData ?? [];
  const metUrl = await Promise.all(
    fotos.map(async (f) => {
      const { data } = await supabase.storage.from("fotos").createSignedUrl(f.bestandspad, 60 * 10);
      return { ...f, url: data?.signedUrl ?? null };
    })
  );

  return (
    <>
      <Header naam={naam} isBeheerder terugHref="/beheer" terugLabel="Beheer" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">{klasje.naam}</p>
        <h1 className="font-display text-2xl font-semibold text-ink">Foto&apos;s beheren</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Enkel gezinnen waarvoor je &quot;Foto&apos;s&quot; hebt aangevinkt, kunnen deze zien.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
          {metUrl.map((f) =>
            f.url ? (
              <div key={f.id} className="overflow-hidden rounded-lg border border-border bg-surface">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={f.url} alt={f.bijschrift ?? ""} className="aspect-square w-full object-cover" />
                <form action={verwijderFoto} className="p-2">
                  <input type="hidden" name="id" value={f.id} />
                  <input type="hidden" name="slug" value={slug} />
                  <input type="hidden" name="bestandspad" value={f.bestandspad} />
                  <button type="submit" className="text-xs text-danger hover:underline">
                    Verwijderen
                  </button>
                </form>
              </div>
            ) : null
          )}
          {metUrl.length === 0 && (
            <p className="col-span-full text-sm text-ink-dim">Nog geen foto&apos;s.</p>
          )}
        </div>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Foto&apos;s toevoegen</h2>
          <form action={voegFotosToe} className="mt-4 space-y-4" encType="multipart/form-data">
            <input type="hidden" name="klasje_id" value={klasje.id} />
            <input type="hidden" name="slug" value={slug} />
            <div className="space-y-1.5">
              <label htmlFor="bestanden" className="text-sm font-medium text-ink">
                Foto&apos;s (je kan er meerdere tegelijk kiezen)
              </label>
              <input
                id="bestanden"
                name="bestanden"
                type="file"
                accept="image/*"
                multiple
                className="w-full text-sm"
              />
            </div>
            <div className="space-y-1.5">
              <label htmlFor="bijschrift" className="text-sm font-medium text-ink">
                Bijschrift (optioneel, geldt voor alle gekozen foto&apos;s)
              </label>
              <input
                id="bijschrift"
                name="bijschrift"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Uploaden
            </button>
          </form>
        </section>
      </main>
    </>
  );
}
