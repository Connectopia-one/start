import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { InteractieveLeerbundel } from "@/components/InteractieveLeerbundel";
import { getSessionProfile } from "@/lib/auth";
import { hoofdstukToegankelijk } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import { laadKlikbareBundel } from "@/lib/leerbundel";
import { vindNiveau } from "@/lib/niveaus";

/*
  De interactieve leerbundel, op een eigen bladzijde.

  Kim op 29 september 2026: "ik wil niets veranderen aan wat er al was maar
  echt een extra knop per hoofdstuk met aparte interactieve lesbundels."

  Daarom staat dit hier los. Het hoofdstuk zelf, de tabbladen en de pdf's om af
  te drukken blijven precies zoals ze waren; dit is een deur ernaast, met een
  knop bij het hoofdstuk.
*/

export default async function LeerbundelPage({
  params,
}: {
  params: Promise<{ vak: string; hoofdstuk: string }>;
}) {
  const { vak: vakSlug, hoofdstuk: volgnummerStr } = await params;
  const volgnummer = Number(volgnummerStr);

  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: vak } = await supabase
    .from("vakken")
    .select("id, naam, slug")
    .eq("slug", vakSlug)
    .single();
  if (!vak) notFound();

  const { data: hoofdstuk } = await supabase
    .from("hoofdstukken")
    .select("id, titel, volgnummer, gratis, niveau")
    .eq("vak_id", vak.id)
    .eq("volgnummer", volgnummer)
    .single();
  if (!hoofdstuk) notFound();

  const magVolledig = hoofdstukToegankelijk(
    hoofdstuk.gratis,
    session?.profile ?? null,
  );
  if (!magVolledig) notFound();

  const bundel = await laadKlikbareBundel(vak.slug, hoofdstuk.titel);
  if (!bundel) notFound();

  const niveau = vindNiveau(hoofdstuk.niveau);
  const terug = `/vakken/${vak.slug}/${hoofdstuk.volgnummer}`;

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href={terug} className="text-sm text-ink-dim hover:text-ink">
          &larr; {vak.naam} — {hoofdstuk.titel}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Interactieve leerbundel
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {niveau ? `${niveau.emoji} ${niveau.naam} · ` : ""}
          {vak.naam} — {hoofdstuk.titel}
        </p>

        <InteractieveLeerbundel
          bundel={bundel}
          hoofdstukId={hoofdstuk.id}
          naarOefeningen={terug}
        />
      </main>
    </>
  );
}
