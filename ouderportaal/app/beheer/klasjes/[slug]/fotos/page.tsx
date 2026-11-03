import { notFound } from "next/navigation";
import { requireStaff } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { maakFotoLinks } from "@/lib/fotoLinks";
import { Header } from "@/components/Header";
import { verwijderFoto } from "./actions";
import { NieuweFotosForm } from "./NieuweFotosForm";
import { FotoTegel } from "./FotoTegel";
import { AllesVerkleinen } from "./AllesVerkleinen";
import { AllesDownloaden } from "./AllesDownloaden";

export default async function BeheerFotosPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const { slug } = await params;
  const { fout, succes } = await searchParams;
  const session = await requireStaff();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";
  const isBeheerder = rol === "beheerder";

  const supabase = await createClient();
  const { data: klasje } = await supabase.from("klasjes").select("id, naam, slug").eq("slug", slug).single();
  if (!klasje) notFound();

  const { data: fotosData } = await supabase
    .from("fotos")
    .select("id, bestandspad, bijschrift, created_at")
    .eq("klasje_id", klasje.id)
    .order("created_at", { ascending: false });

  const fotos = fotosData ?? [];
  const links = await maakFotoLinks(supabase, fotos.map((f) => f.bestandspad));
  const metUrl = fotos.map((f) => ({ ...f, url: links.get(f.bestandspad) ?? null }));
  const nietGeladen = metUrl.filter((f) => !f.url).length;

  return (
    <>
      <Header
        naam={naam}
        rol={rol}
        terugHref={isBeheerder ? "/beheer" : "/team"}
        terugLabel={isBeheerder ? "Beheer" : "Team"}
      />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">{klasje.naam}</p>
        <h1 className="font-display text-2xl font-semibold text-ink">Foto&apos;s beheren</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Enkel gezinnen waarvoor &quot;Foto&apos;s&quot; is aangevinkt, kunnen deze zien.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <p className="mt-4 text-sm text-ink-dim">
          {metUrl.length === 1 ? "1 foto" : `${metUrl.length} foto's`} in dit klasje.
        </p>
        {nietGeladen > 0 && (
          <p className="mt-2 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {nietGeladen === 1 ? "1 foto kon" : `${nietGeladen} foto's konden`} nu niet geladen worden. Ze
            staan wel online. <a href={`/beheer/klasjes/${slug}/fotos`} className="font-medium underline">Laad de pagina opnieuw</a>.
          </p>
        )}

        <AllesVerkleinen
          slug={slug}
          fotos={metUrl.flatMap((f) => (f.url ? [{ id: f.id, url: f.url, bestandspad: f.bestandspad }] : []))}
        />
        <AllesDownloaden
          klasjeNaam={klasje.naam}
          slug={slug}
          fotos={metUrl.flatMap((f) => (f.url ? [{ id: f.id, url: f.url, aangemaakt: f.created_at }] : []))}
        />

        <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
          {metUrl.map((f) =>
            f.url ? (
              <FotoTegel
                key={f.bestandspad}
                id={f.id}
                url={f.url}
                bestandspad={f.bestandspad}
                bijschrift={f.bijschrift}
                slug={slug}
              >
                {isBeheerder && (
                  <form action={verwijderFoto} className="p-2">
                    <input type="hidden" name="id" value={f.id} />
                    <input type="hidden" name="slug" value={slug} />
                    <input type="hidden" name="bestandspad" value={f.bestandspad} />
                    <button type="submit" className="text-xs text-danger hover:underline">
                      Verwijderen
                    </button>
                  </form>
                )}
              </FotoTegel>
            ) : (
              <div
                key={f.bestandspad}
                className="flex aspect-square flex-col items-center justify-center gap-2 rounded-lg border border-dashed border-border bg-surface p-3 text-center text-xs text-ink-dim"
              >
                <span>Deze foto laadde niet.</span>
                <a href={`/beheer/klasjes/${slug}/fotos`} className="font-medium text-forest underline">
                  Opnieuw proberen
                </a>
              </div>
            )
          )}
          {metUrl.length === 0 && (
            <p className="col-span-full text-sm text-ink-dim">Nog geen foto&apos;s.</p>
          )}
        </div>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Foto&apos;s toevoegen</h2>
          <NieuweFotosForm klasjeId={klasje.id} slug={slug} />
        </section>
      </main>
    </>
  );
}
