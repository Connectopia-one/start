import { notFound } from "next/navigation";
import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

type Foto = {
  id: string;
  bestandspad: string;
  bijschrift: string | null;
  created_at: string;
};

export default async function FotosPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const session = await requireIngelogd();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const { data: klasje } = await supabase
    .from("klasjes")
    .select("id, naam, slug")
    .eq("slug", slug)
    .single();

  if (!klasje) notFound();

  const { data: fotosData } = await supabase
    .from("fotos")
    .select("id, bestandspad, bijschrift, created_at")
    .eq("klasje_id", klasje.id)
    .order("created_at", { ascending: false });

  const fotos = (fotosData as Foto[] | null) ?? [];

  const metUrl = await Promise.all(
    fotos.map(async (f) => {
      const { data } = await supabase.storage.from("fotos").createSignedUrl(f.bestandspad, 60 * 10);
      return { ...f, url: data?.signedUrl ?? null };
    })
  );

  return (
    <>
      <Header naam={naam} rol={rol} terugHref="/portaal" terugLabel="Overzicht" />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">{klasje.naam}</p>
        <h1 className="font-display text-2xl font-semibold text-ink">Foto&apos;s</h1>

        {metUrl.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">Er staan hier nog geen foto&apos;s.</p>
        )}

        <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
          {metUrl.map((f) =>
            f.url ? (
              <figure key={f.id} className="overflow-hidden rounded-lg border border-border bg-surface">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={f.url} alt={f.bijschrift ?? ""} className="aspect-square w-full object-cover" />
                {f.bijschrift && (
                  <figcaption className="px-2 py-1.5 text-xs text-ink-dim">{f.bijschrift}</figcaption>
                )}
              </figure>
            ) : null
          )}
        </div>
      </main>
    </>
  );
}
