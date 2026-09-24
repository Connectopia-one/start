import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { HoofdstukTegels, type HoofdstukTegel } from "@/components/HoofdstukTegels";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang, hoofdstukToegankelijk } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import { PRIJS_NU_EUR, TIJDELIJKE_PRIJS, TIJDELIJKE_PRIJS_KORT } from "@/lib/prijs";
import { schooljaarEindeLabel } from "@/lib/schooljaar";
import { vindNiveau } from "@/lib/niveaus";
import { sorteerHoofdstukken } from "@/lib/hoofdstukvolgorde";
import { vakIcoon } from "@/lib/vakbeeld";

/*
  De hoofdstukken van één vak binnen één niveau. Dit is de tweede laag knoppen:
  van /niveaus/<niveau> (de vakken) kom je hier, en van hier ga je naar
  /vakken/<vak>/<volgnummer> (de oefeningen zelf). Dat laatste webadres blijft
  zoals het was, zodat oude links en bladwijzers blijven werken.
*/
export default async function NiveauVakPage({
  params,
}: {
  params: Promise<{ niveau: string; vak: string }>;
}) {
  const { niveau: niveauSlug, vak: vakSlug } = await params;
  const niveau = vindNiveau(niveauSlug);
  if (!niveau) notFound();

  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: vak } = await supabase
    .from("vakken")
    .select("id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis, niveau)")
    .eq("slug", vakSlug)
    .single();
  if (!vak) notFound();

  const hoofdstukken = sorteerHoofdstukken(
    (vak.hoofdstukken as { id: string; titel: string; volgnummer: number; gratis: boolean; niveau: string }[]).filter(
      (h) => h.niveau === niveau.slug
    )
  );
  if (!hoofdstukken.length) notFound();

  const volledigeToegang = heeftVolledigeToegang(session?.profile ?? null);

  const { data: kinderen } = session
    ? await supabase.from("kinderen").select("id, naam").eq("profile_id", session.userId).order("naam")
    : { data: [] };

  const tegels: HoofdstukTegel[] = hoofdstukken.map((h) => ({
    id: h.id,
    titel: h.titel,
    volgnummer: h.volgnummer,
    gratis: h.gratis,
    mag: hoofdstukToegankelijk(h.gratis, session?.profile ?? null),
  }));

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <Link href={`/niveaus/${niveau.slug}`} className="text-sm text-ink-dim hover:text-ink">
          &larr; {niveau.emoji} {niveau.naam}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          <span aria-hidden>{vakIcoon(vak.slug)}</span> {vak.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {hoofdstukken.length} {hoofdstukken.length === 1 ? "hoofdstuk" : "hoofdstukken"} in{" "}
          {niveau.emoji} {niveau.naam}
        </p>

        {!volledigeToegang && (
          <div className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Volledige toegang tot alle hoofdstukken kost{" "}
            <strong>€{PRIJS_NU_EUR} per schooljaar</strong>
            {TIJDELIJKE_PRIJS && <> ({TIJDELIJKE_PRIJS_KORT})</>}, geldig tot en met{" "}
            {schooljaarEindeLabel()} — de opbrengsten gaan volledig naar vzw Connectopia.{" "}
            <Link href={session ? "/betalen" : "/registreren"} className="font-medium text-forest-dark underline-offset-2 hover:underline">
              {session ? "Nu vrijgeven" : "Account maken en starten"}
            </Link>
          </div>
        )}

        <HoofdstukTegels vakSlug={vak.slug} hoofdstukken={tegels} kinderen={kinderen ?? []} />
      </main>
    </>
  );
}
