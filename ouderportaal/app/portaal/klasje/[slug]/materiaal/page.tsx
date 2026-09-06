import { notFound } from "next/navigation";
import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

type Materiaal = {
  id: string;
  type: "pdf" | "link" | "aankondiging";
  titel: string;
  inhoud: string | null;
  bestandspad: string | null;
  created_at: string;
};

export default async function MateriaalPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const session = await requireIngelogd();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const isBeheerder = session.profile?.role === "beheerder";

  const supabase = await createClient();
  const { data: klasje } = await supabase
    .from("klasjes")
    .select("id, naam, slug")
    .eq("slug", slug)
    .single();

  if (!klasje) notFound();

  const { data: materialenData } = await supabase
    .from("materialen")
    .select("id, type, titel, inhoud, bestandspad, created_at")
    .eq("klasje_id", klasje.id)
    .order("created_at", { ascending: false });

  const materialen = (materialenData as Materiaal[] | null) ?? [];

  const metLinks = await Promise.all(
    materialen.map(async (m) => {
      if (m.type === "pdf" && m.bestandspad) {
        const { data } = await supabase.storage
          .from("materialen")
          .createSignedUrl(m.bestandspad, 60 * 10);
        return { ...m, downloadUrl: data?.signedUrl ?? null };
      }
      return { ...m, downloadUrl: null };
    })
  );

  return (
    <>
      <Header naam={naam} isBeheerder={isBeheerder} terugHref="/portaal" terugLabel="Overzicht" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">{klasje.naam}</p>
        <h1 className="font-display text-2xl font-semibold text-ink">Lesmateriaal</h1>

        {metLinks.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">Er staat hier nog niets klaar.</p>
        )}

        <ul className="mt-6 space-y-3">
          {metLinks.map((m) => (
            <li key={m.id} className="rounded-lg border border-border bg-surface p-4">
              <p className="text-xs uppercase tracking-wide text-ink-dim">
                {m.type === "pdf" ? "Document" : m.type === "link" ? "Link" : "Aankondiging"} &middot;{" "}
                {new Date(m.created_at).toLocaleDateString("nl-BE", {
                  day: "numeric",
                  month: "long",
                  year: "numeric",
                })}
              </p>
              <p className="mt-1 font-medium text-ink">{m.titel}</p>
              {m.type === "pdf" && m.downloadUrl && (
                <a
                  href={m.downloadUrl}
                  className="mt-2 inline-block text-sm font-medium text-forest-dark hover:underline"
                >
                  Downloaden &rarr;
                </a>
              )}
              {m.type === "link" && m.inhoud && (
                <a
                  href={m.inhoud}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="mt-2 inline-block text-sm font-medium text-forest-dark hover:underline"
                >
                  Openen &rarr;
                </a>
              )}
              {m.type === "aankondiging" && m.inhoud && (
                <p className="mt-2 whitespace-pre-wrap text-sm text-ink">{m.inhoud}</p>
              )}
            </li>
          ))}
        </ul>
      </main>
    </>
  );
}
