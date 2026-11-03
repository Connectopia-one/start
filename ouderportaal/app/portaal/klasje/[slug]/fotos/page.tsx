import { notFound } from "next/navigation";
import { requirePortaalSessie } from "@/lib/auth";
import { MeekijkBalk } from "@/components/MeekijkBalk";
import { createClient } from "@/lib/supabase/server";
import { maakFotoLinks } from "@/lib/fotoLinks";
import { Header } from "@/components/Header";
import { FotoGalerij } from "./FotoGalerij";

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
  const session = await requirePortaalSessie();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const { data: klasje } = await supabase
    .from("klasjes")
    .select("id, naam, slug")
    .eq("slug", slug)
    .single();

  if (!klasje) notFound();

  /* Zie de nota bij het lesmateriaal: de regels van het gezin gelden hier ook. */
  if (session.alsOuder) {
    const { data: toegang } = await supabase
      .from("toegang")
      .select("fotos")
      .eq("profile_id", session.userId)
      .eq("klasje_id", klasje.id)
      .maybeSingle();
    if (!toegang?.fotos) notFound();
  }

  const { data: fotosData } = await supabase
    .from("fotos")
    .select("id, bestandspad, bijschrift, created_at")
    .eq("klasje_id", klasje.id)
    .order("created_at", { ascending: false });

  const fotos = (fotosData as Foto[] | null) ?? [];

  const links = await maakFotoLinks(supabase, fotos.map((f) => f.bestandspad));
  const metUrl = fotos.map((f) => ({ ...f, url: links.get(f.bestandspad) ?? null }));
  const nietGeladen = metUrl.filter((f) => !f.url).length;

  return (
    <>
      {session.meekijken && (
        <MeekijkBalk naam={session.meekijken.naam} terug="/beheer/gezinnen" />
      )}
      <Header
        naam={naam}
        rol={rol}
        terugHref="/portaal"
        terugLabel="Overzicht"
      />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">
          {klasje.naam}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          Foto&apos;s
        </h1>

        {metUrl.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Er staan hier nog geen foto&apos;s.
          </p>
        )}

        {nietGeladen > 0 && (
          <p className="mt-6 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            {nietGeladen === 1 ? "1 foto kon" : `${nietGeladen} foto's konden`} even niet geladen worden.{" "}
            <a href={`/portaal/klasje/${slug}/fotos`} className="font-medium underline">
              Laad de pagina opnieuw
            </a>{" "}
            om ze te zien.
          </p>
        )}

        <FotoGalerij
          fotos={metUrl.flatMap((f) => (f.url ? [{ id: f.id, url: f.url, bijschrift: f.bijschrift }] : []))}
        />
      </main>
    </>
  );
}
