import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { vereisOuderPin } from "@/lib/ouderpin";
import { createClient } from "@/lib/supabase/server";
import { ExamenDetail } from "@/components/ExamenUitslag";

/* De uitslag van één examen, voor de ouder (en de beheerder). Achter de
   ouderpincode, want de juiste antwoorden staan erbij. */
export default async function ExamenUitslagPage({
  params,
}: {
  params: Promise<{ kindId: string; examenId: string }>;
}) {
  const session = await requireIngelogd();
  const { kindId, examenId } = await params;
  await vereisOuderPin(
    session.userId,
    `/account/kinderen/${kindId}/examens/${examenId}`,
  );
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, profile_id")
    .eq("id", kindId)
    .single();
  if (
    !kind ||
    (kind.profile_id !== session.userId &&
      session.profile?.role !== "beheerder")
  )
    notFound();

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
          href={`/account/kinderen/${kindId}#examens`}
          className="text-sm text-ink-dim hover:text-ink"
        >
          &larr; Voortgang — {kind.naam}
        </Link>
        {inhoud}
      </main>
    </>
  );
}
