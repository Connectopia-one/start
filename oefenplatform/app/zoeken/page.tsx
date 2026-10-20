import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { Zoekvak } from "@/components/Zoekvak";
import { getSessionProfile } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { vindNiveau } from "@/lib/niveaus";
import { sorteerHoofdstukken } from "@/lib/hoofdstukvolgorde";

/*
  Zoeken binnen één niveau, eventueel binnen één vak.

  Kelly, een mama uit de testgroep, op 20 oktober 2026: "Bij aardrijkskunde
  zijn het andere titels dan het boek waarmee we werken. Daardoor vinden we
  niet alles (vlot). Een zoekfunctie zou handig zijn." Onze titels volgen de
  vakfiche van de Examencommissie, en elk boek noemt het anders. Daarom zoeken
  we niet alleen in de titels, maar ook in de vragen en de uitleg: wie
  "bevolkingspiramide" intypt, vindt het hoofdstuk waar die in voorkomt, hoe
  het ook heet.

  We tonen enkel welke hoofdstukken het woord bevatten, nooit de vragen zelf.
  Daarom mag het zoeken met de beheersleutel gebeuren: zo vindt ook wie nog
  geen volledige toegang heeft, waar iets staat.
*/

type Rij = {
  id: string;
  titel: string;
  volgnummer: number;
  gratis: boolean;
  niveau: string;
  vakken: { naam: string; slug: string } | null;
};

/* % en _ zijn jokers in ilike. Een aanhalingsteken of backslash zou de
   .or()-filter breken, waar de term tussen aanhalingstekens staat. */
function veilig(term: string) {
  return term.replace(/["\\]/g, " ").replace(/[%_]/g, " ").replace(/\s+/g, " ").trim();
}

export default async function ZoekPagina({
  searchParams,
}: {
  searchParams: Promise<{ niveau?: string; vak?: string; q?: string }>;
}) {
  const { niveau: niveauSlug = "", vak: vakSlug, q = "" } = await searchParams;
  const niveau = vindNiveau(niveauSlug);
  if (!niveau) notFound();

  const session = await getSessionProfile();
  const term = q.trim().slice(0, 60);
  const genoeg = veilig(term).length >= 3;

  let vakNaam: string | undefined;
  const titelTreffers = new Map<string, Rij>();
  const vraagTreffers = new Map<string, { rij: Rij; aantal: number }>();

  if (genoeg) {
    const db = createAdminClient();
    const patroon = `%${veilig(term)}%`;

    let titels = db
      .from("hoofdstukken")
      .select("id, titel, volgnummer, gratis, niveau, vakken!inner(naam, slug)")
      .eq("niveau", niveau.slug)
      .ilike("titel", patroon)
      .limit(100);
    if (vakSlug) titels = titels.eq("vakken.slug", vakSlug);

    let vragen = db
      .from("vragen")
      .select(
        "hoofdstuk_id, hoofdstukken!inner(id, titel, volgnummer, gratis, niveau, vakken!inner(naam, slug))",
      )
      .eq("hoofdstukken.niveau", niveau.slug)
      .or(`vraag.ilike."${patroon}",uitleg.ilike."${patroon}"`)
      .limit(1000);
    if (vakSlug) vragen = vragen.eq("hoofdstukken.vakken.slug", vakSlug);

    const [{ data: t }, { data: v }] = await Promise.all([titels, vragen]);

    for (const rij of (t ?? []) as unknown as Rij[]) titelTreffers.set(rij.id, rij);
    for (const r of (v ?? []) as unknown as { hoofdstukken: Rij }[]) {
      const rij = r.hoofdstukken;
      if (!rij || titelTreffers.has(rij.id)) continue;
      const al = vraagTreffers.get(rij.id);
      if (al) al.aantal += 1;
      else vraagTreffers.set(rij.id, { rij, aantal: 1 });
    }
  }

  if (vakSlug) {
    const db = createAdminClient();
    const { data } = await db
      .from("vakken")
      .select("naam")
      .eq("slug", vakSlug)
      .maybeSingle();
    vakNaam = (data as { naam: string } | null)?.naam;
  }

  const inTitel = sorteerHoofdstukken([...titelTreffers.values()]);
  /* Waar het woord het vaakst in voorkomt, staat bovenaan. */
  const inVragen = [...vraagTreffers.values()].sort((a, b) => b.aantal - a.aantal);
  const niets = genoeg && inTitel.length === 0 && inVragen.length === 0;

  const terug = vakSlug
    ? `/niveaus/${niveau.slug}/${vakSlug}`
    : `/niveaus/${niveau.slug}`;

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href={terug} className="text-sm text-ink-dim hover:text-ink">
          &larr; {vakNaam ? `${vakNaam} in ` : ""}
          {niveau.emoji} {niveau.naam}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Zoeken in {vakNaam ? `${vakNaam}, ` : ""}
          {niveau.emoji} {niveau.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Onze titels volgen de vakfiche, niet je boek. Typ daarom gerust een
          woord uit je boek of je cursus: we zoeken ook in de vragen en de
          uitleg.
        </p>

        <Zoekvak niveau={niveau.slug} vak={vakSlug} vakNaam={vakNaam} waarde={term} />

        {!genoeg && term.length > 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Typ minstens drie letters.
          </p>
        )}

        {niets && (
          <p className="mt-6 text-sm text-ink-dim">
            Niets gevonden voor &ldquo;{term}&rdquo;. Probeer een ander woord,
            of een deel van het woord.
            {vakSlug && (
              <>
                {" "}
                <Link
                  href={`/zoeken?niveau=${niveau.slug}&q=${encodeURIComponent(term)}`}
                  className="font-medium text-forest-dark underline-offset-2 hover:underline"
                >
                  Zoek in alle vakken van {niveau.naam}
                </Link>
                .
              </>
            )}
          </p>
        )}

        {inTitel.length > 0 && (
          <section className="mt-8">
            <h2 className="font-display text-lg font-semibold text-ink">
              In de titel
            </h2>
            <ul className="mt-3 grid gap-2">
              {inTitel.map((h) => (
                <Treffer key={h.id} rij={h} metVak={!vakSlug} />
              ))}
            </ul>
          </section>
        )}

        {inVragen.length > 0 && (
          <section className="mt-8">
            <h2 className="font-display text-lg font-semibold text-ink">
              In de vragen en de uitleg
            </h2>
            <ul className="mt-3 grid gap-2">
              {inVragen.map(({ rij, aantal }) => (
                <Treffer
                  key={rij.id}
                  rij={rij}
                  metVak={!vakSlug}
                  onder={aantal === 1 ? "1 vraag" : `${aantal} vragen`}
                />
              ))}
            </ul>
          </section>
        )}
      </main>
    </>
  );
}

function Treffer({
  rij,
  metVak,
  onder,
}: {
  rij: Rij;
  metVak: boolean;
  onder?: string;
}) {
  if (!rij.vakken) return null;
  return (
    <li>
      <Link
        href={`/vakken/${rij.vakken.slug}/${rij.volgnummer}`}
        className="flex items-center justify-between gap-3 rounded-xl border border-border bg-surface px-4 py-3 transition hover:border-forest"
      >
        <span>
          <span className="block text-sm font-medium text-ink">{rij.titel}</span>
          {(metVak || onder) && (
            <span className="block text-xs text-ink-dim">
              {[metVak ? rij.vakken.naam : null, onder].filter(Boolean).join(" · ")}
            </span>
          )}
        </span>
        <span aria-hidden className="text-ink-dim">
          &rarr;
        </span>
      </Link>
    </li>
  );
}
