import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { Quiz } from "@/components/Quiz";
import { getSessionProfile } from "@/lib/auth";
import { hoofdstukToegankelijk } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import { PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";
import { schooljaarEindeLabel } from "@/lib/schooljaar";
import { vindNiveau } from "@/lib/niveaus";
import { HoofdstukTabs } from "@/components/HoofdstukTabs";

export default async function HoofdstukPage({
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

  const niveau = vindNiveau(hoofdstuk.niveau);

  const magVolledig = hoofdstukToegankelijk(hoofdstuk.gratis, session?.profile ?? null);

  const { data: vragen } = magVolledig
    ? await supabase
        .from("vragen")
        .select("id, type, vraag, opties, antwoord, uitleg, volgnummer")
        .eq("hoofdstuk_id", hoofdstuk.id)
        .order("volgnummer", { ascending: true })
    : { data: [] };

  const { data: kinderen } = session
    ? await supabase.from("kinderen").select("id, naam").eq("profile_id", session.userId).order("naam")
    : { data: [] };

  const { data: leerstofRijen } = magVolledig
    ? await supabase
        .from("leerstof")
        .select("id, titel, bestandspad")
        .eq("hoofdstuk_id", hoofdstuk.id)
        .order("created_at", { ascending: false })
    : { data: [] };

  const leerstof = await Promise.all(
    (leerstofRijen ?? []).map(async (l) => {
      const { data } = await supabase.storage.from("leerstof").createSignedUrl(l.bestandspad, 3600);
      return { id: l.id, titel: l.titel, url: data?.signedUrl ?? null };
    })
  );

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href={niveau ? `/niveaus/${niveau.slug}` : "/"} className="text-sm text-ink-dim hover:text-ink">
          &larr; {niveau ? `${niveau.emoji} ${niveau.naam}` : "Categorieën"}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {vak.naam} — {hoofdstuk.titel}
        </h1>

        {!magVolledig ? (
          <div className="mt-8 rounded-xl border border-amber/40 bg-amber/10 px-5 py-6 text-sm text-ink">
            <p className="font-medium">Dit hoofdstuk is nog op slot.</p>
            <p className="mt-2 text-ink-dim">
              Geef volledige toegang tot alle hoofdstukken vrij voor €{PRIJS_SCHOOLJAAR_EUR} per
              schooljaar (geldig tot en met {schooljaarEindeLabel()}), of vraag als plusklas-gezin
              de gratis toegangscode aan.
            </p>
            <Link
              href={session ? "/betalen" : "/registreren"}
              className="mt-4 inline-block rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
            >
              {session ? "Toegang vrijgeven" : "Account maken"}
            </Link>
          </div>
        ) : (
          <HoofdstukTabs
            aantalLeerstof={leerstof.length}
            oefeningen={<Quiz vragen={vragen ?? []} kinderen={kinderen ?? []} hoofdstukId={hoofdstuk.id} />}
            leerstof={
              <div className="mt-6 space-y-2">
                {leerstof.map((l) =>
                  l.url ? (
                    <a
                      key={l.id}
                      href={l.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center justify-between rounded-lg border border-border bg-surface px-4 py-3 text-sm hover:border-forest"
                    >
                      <span className="text-ink">📄 {l.titel}</span>
                      <span className="text-forest-dark">Openen &rarr;</span>
                    </a>
                  ) : null
                )}
                {!leerstof.length && (
                  <p className="text-sm text-ink-dim">Er is nog geen leerstof geüpload voor dit hoofdstuk.</p>
                )}
              </div>
            }
          />
        )}
      </main>
    </>
  );
}
