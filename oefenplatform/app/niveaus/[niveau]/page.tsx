import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { VakTegels, type VakTegel } from "@/components/VakTegels";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import {
  PRIJS_NU_EUR,
  TIJDELIJKE_PRIJS,
  TIJDELIJKE_PRIJS_KORT,
} from "@/lib/prijs";
import { schooljaarEindeLabel } from "@/lib/schooljaar";
import {
  vindNiveau,
  vindGroep,
  niveausVanGroep,
  type Groep,
} from "@/lib/niveaus";
import { sorteerHoofdstukken } from "@/lib/hoofdstukvolgorde";
import { vakIcoon } from "@/lib/vakbeeld";

type Hoofdstuk = {
  id: string;
  titel: string;
  volgnummer: number;
  gratis: boolean;
  niveau: string;
};
type Vak = {
  id: string;
  naam: string;
  slug: string;
  hoofdstukken: Hoofdstuk[];
};

/*
  Eén niveau = één laag knoppen met de vakken erop. De hoofdstukken zelf staan
  een stap verder, op /niveaus/<niveau>/<vak>. Tot 24 september 2026 stond hier
  één doorlopende lijst met álle hoofdstukken van álle vakken; bij ✨ Spark zijn
  dat er intussen meer dan honderd, en dan moet een kind scrollen tot het zijn
  vak vindt.
*/
export default async function NiveauPage({
  params,
}: {
  params: Promise<{ niveau: string }>;
}) {
  const { niveau: niveauSlug } = await params;
  const niveau = vindNiveau(niveauSlug);

  /* Boost is geen categorie maar een groep: er hangt geen enkel hoofdstuk aan.
     Wie erop klikt, kiest eerst tussen doorstroom en dubbele finaliteit. Die
     twee hebben elk hun eigen vakfiches, dus ook hun eigen vakken. */
  const groep = niveau ? undefined : vindGroep(niveauSlug);
  if (!niveau && !groep) notFound();

  const session = await getSessionProfile();

  if (groep) return <GroepPagina groep={groep} session={session} />;
  if (!niveau) notFound();

  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select(
      "id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis, niveau)",
    )
    .order("volgorde", { ascending: true });

  const volledigeToegang = heeftVolledigeToegang(session?.profile ?? null);

  const { data: kinderen } = session
    ? await supabase
        .from("kinderen")
        .select("id, naam")
        .eq("profile_id", session.userId)
        .order("naam")
    : { data: [] };

  const tegels: VakTegel[] = ((vakken as Vak[] | null) ?? [])
    .map((vak) => ({
      id: vak.id,
      slug: vak.slug,
      naam: vak.naam,
      icoon: vakIcoon(vak.slug),
      hoofdstukIds: sorteerHoofdstukken(
        vak.hoofdstukken.filter((h) => h.niveau === niveau.slug),
      ).map((h) => h.id),
    }))
    .filter((vak) => vak.hoofdstukIds.length > 0);

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <Link href="/" className="text-sm text-ink-dim hover:text-ink">
          &larr; Alle categorieën
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {niveau.emoji} {niveau.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">{niveau.omschrijving}</p>
        <p className="mt-3 text-sm text-ink-dim">
          Kies een vak om aan de slag te gaan.
        </p>

        {!volledigeToegang && (
          <div className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Volledige toegang tot alle hoofdstukken kost{" "}
            <strong>€{PRIJS_NU_EUR} per schooljaar</strong>
            {TIJDELIJKE_PRIJS && <> ({TIJDELIJKE_PRIJS_KORT})</>}, geldig tot en
            met {schooljaarEindeLabel()} — de opbrengsten gaan volledig naar vzw
            Connectopia.{" "}
            <Link
              href={session ? "/betalen" : "/registreren"}
              className="font-medium text-forest-dark underline-offset-2 hover:underline"
            >
              {session ? "Nu vrijgeven" : "Account maken en starten"}
            </Link>
          </div>
        )}

        {tegels.length ? (
          <VakTegels
            niveauSlug={niveau.slug}
            vakken={tegels}
            kinderen={kinderen ?? []}
          />
        ) : (
          <p className="mt-8 text-sm text-ink-dim">
            Er is nog geen inhoud voor deze categorie.
          </p>
        )}
      </main>
    </>
  );
}

/*
  De tussenstap bij een groep: Boost heeft geen eigen hoofdstukken, maar twee
  categorieën eronder. Die keuze zetten we hier, zodat de startpagina op vier
  knoppen blijft staan in plaats van er voor elke finaliteit een bij te
  krijgen.

  Een categorie waar nog niets in staat, tonen we niet. Zo leidt geen enkele
  knop naar een lege pagina, en komt de tweede knop er vanzelf bij zodra er een
  hoofdstuk in geladen is.
*/
async function GroepPagina({
  groep,
  session,
}: {
  groep: Groep;
  session: Awaited<ReturnType<typeof getSessionProfile>>;
}) {
  const supabase = await createClient();
  const kinderen = niveausVanGroep(groep.slug);

  const { data } = await supabase
    .from("hoofdstukken")
    .select("niveau")
    .in(
      "niveau",
      kinderen.map((n) => n.slug),
    );
  const gevuld = new Set(
    ((data as { niveau: string }[] | null) ?? []).map((h) => h.niveau),
  );
  const zichtbaar = kinderen.filter((n) => gevuld.has(n.slug));

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <Link href="/" className="text-sm text-ink-dim hover:text-ink">
          &larr; Alle categorieën
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {groep.emoji} {groep.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">{groep.omschrijving}</p>
        <p className="mt-3 text-sm text-ink-dim">
          Vanaf de tweede graad hangt de leerstof af van je finaliteit. Kies
          hieronder welke bij jouw studierichting hoort.
        </p>

        {zichtbaar.length ? (
          <div className="mt-8 grid gap-4 sm:grid-cols-2">
            {zichtbaar.map((n) => (
              <Link
                key={n.slug}
                href={`/niveaus/${n.slug}`}
                className="rounded-xl border border-border bg-surface p-6 transition hover:border-forest hover:shadow-sm"
              >
                <span className="text-3xl">{n.emoji}</span>
                <h2 className="mt-2 font-display text-xl font-semibold text-ink">
                  {n.kort ?? n.naam}
                </h2>
                <p className="mt-1 text-sm text-ink-dim">{n.omschrijving}</p>
              </Link>
            ))}
          </div>
        ) : (
          <p className="mt-8 text-sm text-ink-dim">
            Er is nog geen inhoud voor deze categorie.
          </p>
        )}
      </main>
    </>
  );
}
