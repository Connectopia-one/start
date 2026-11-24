import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireBegeleider } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { ExamenDetail } from "@/components/ExamenUitslag";

/* De uitslag van één examen, voor de begeleiding van de plusklas. */
export default async function BegeleidingExamenPage({
  params,
}: {
  params: Promise<{ kindId: string; examenId: string }>;
}) {
  const session = await requireBegeleider();
  const { kindId, examenId } = await params;
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, profiles(is_plusklas)")
    .eq("id", kindId)
    .single();
  const gezin = (kind as { profiles?: { is_plusklas: boolean } } | null)
    ?.profiles;
  if (!kind || !gezin?.is_plusklas) notFound();

  const inhoud = await ExamenDetail({
    supabase,
    kindId,
    examenId,
    kindNaam: kind.naam,
  });
  if (!inhoud) notFound();

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link
          href={`/begeleiding/${kindId}`}
          className="text-sm text-ink-dim hover:text-ink"
        >
          &larr; Fiche — {kind.naam}
        </Link>
        {inhoud}
      </main>
    </>
  );
}
