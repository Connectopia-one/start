import Link from "next/link";
import { BerichtBalk, type Bericht } from "@/components/BerichtBalk";
import { Dagvraag } from "@/components/Dagvraag";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { LEERJAARNIVEAUS, vindNiveau } from "@/lib/niveaus";
import { startUitleg, basisUitleg, hoekjeUitleg } from "@/inhoud/onderwijsdoelen";

export default async function HomePage() {
  const basis = vindNiveau("basis")!;
  const hoekje = vindNiveau("hoekje")!;
  const session = await getSessionProfile();

  /* Het bericht van Kim aan de ouders. Enkel voor wie ingelogd is: dit gaat
     over onze eigen gezinnen, niet over bezoekers. Zie supabase/berichten.sql. */
  let bericht: Bericht | null = null;
  if (session) {
    const supabase = await createClient();
    const { data } = await supabase
      .from("berichten")
      .select("id, titel, tekst, link, linktekst")
      .eq("actief", true)
      .order("aangemaakt_op", { ascending: false })
      .limit(1)
      .maybeSingle();
    bericht = (data as Bericht | null) ?? null;
  }

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        {bericht && <BerichtBalk bericht={bericht} />}

        <h1 className="font-display text-2xl font-semibold text-ink">
          Oefenen voor de examencommissie
        </h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Interactieve oefeningen, gemaakt door Connectopia. Kies hieronder een categorie om te
          starten.
        </p>

        {/* Wie hier voor het eerst komt, weet nog niet wat dit is en waarop het
            steunt. Vier korte zinnen, en een link voor wie het naadje van de
            kous wil. De volledige tekst staat op /over-ons. */}
        <section className="mt-5 max-w-2xl rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">{startUitleg.kop}</h2>
          <ul className="mt-2 space-y-1.5 text-sm text-ink-dim">
            {startUitleg.punten.map((punt) => (
              <li key={punt} className="flex gap-2">
                <span aria-hidden className="text-forest">
                  &bull;
                </span>
                <span>{punt}</span>
              </li>
            ))}
          </ul>
          <p className="mt-3 text-sm">
            <Link
              href={startUitleg.link}
              className="text-forest-dark underline-offset-2 hover:underline"
            >
              {startUitleg.linkTekst}
            </Link>
          </p>
        </section>

        {/* Elke dag één vraag, met een doel van drie dagen per week. Staat
            bewust vóór de categorieën: wie even tijd heeft, is met één klik
            bezig in plaats van eerst te moeten kiezen waar te beginnen. */}
        <div className="max-w-2xl">
          <Dagvraag />
        </div>

        <p className="mt-5 max-w-2xl rounded-md bg-info/10 px-4 py-3 text-sm text-ink">
          💡 Kies de categorie die het beste past bij wat je kind <strong>al kan</strong> — niet
          per se het officiële leerjaar of de leeftijd. Een kind mag gerust een categorie hoger of
          lager oefenen dan de klas waarin het zit.
        </p>

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          {LEERJAARNIVEAUS.map((n) => (
            <Link
              key={n.slug}
              href={`/niveaus/${n.slug}`}
              className="rounded-xl border border-border bg-surface p-6 transition hover:border-forest hover:shadow-sm"
            >
              <span className="text-3xl">{n.emoji}</span>
              <h2 className="mt-2 font-display text-xl font-semibold text-ink">{n.naam}</h2>
              <p className="mt-1 text-sm text-ink-dim">{n.omschrijving}</p>
            </Link>
          ))}
        </div>

        {/* Herhaling van de bouwstenen staat los van de vier leerjaren: een kind
            uit eender welke categorie kan het nodig hebben. */}
        <Link
          href={`/niveaus/${basis.slug}`}
          className="mt-4 flex items-center justify-between gap-4 rounded-xl border border-border bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm"
        >
          <span>
            <span className="font-display text-lg font-semibold text-ink">
              {basis.emoji} {basis.naam}
            </span>
            <span className="mt-1 block text-sm text-ink-dim">{basisUitleg}</span>
          </span>
          <span aria-hidden className="shrink-0 text-forest">&rarr;</span>
        </Link>

        {/* En het andere uiterste: een hoekje dat naast de leerstof ligt in
            plaats van erin. Het hoort bij geen leerjaar, dus staat het hier
            apart en niet tussen de vier categorieën. */}
        <Link
          href={`/niveaus/${hoekje.slug}`}
          className="mt-4 flex items-center justify-between gap-4 rounded-xl border border-border bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm"
        >
          <span>
            <span className="font-display text-lg font-semibold text-ink">
              {hoekje.emoji} {hoekje.naam}
            </span>
            <span className="mt-1 block text-sm text-ink-dim">{hoekjeUitleg}</span>
          </span>
          <span aria-hidden className="shrink-0 text-forest">&rarr;</span>
        </Link>

        {/* Twee extraatjes naast het oefenen zelf: wat een kind al bij elkaar
            verdiende, en het bord waar de kinderen zelf op schrijven. */}
        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          <Link
            href="/badges"
            className="rounded-xl border border-border bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm"
          >
            <span className="font-display text-lg font-semibold text-ink">⭐ Mijn verzameling</span>
            <span className="mt-1 block text-sm text-ink-dim">
              De badges die je al bij elkaar oefende. Geen ranglijst, alleen je eigen kast.
            </span>
          </Link>

          <Link
            href="/weetjes"
            className="rounded-xl border border-border bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm"
          >
            <span className="font-display text-lg font-semibold text-ink">📌 Het weetjesprikbord</span>
            <span className="mt-1 block text-sm text-ink-dim">
              Weetjes die kinderen zelf instuurden. Hang er gerust een van jou bij.
            </span>
          </Link>
        </div>

        {/* Los van de vier categorieën, want het hoort niet bij het betalende
            aanbod: een gratis verzameling links naar bestaand materiaal. */}
        <Link
          href="/materiaal"
          className="mt-6 flex items-center justify-between gap-4 rounded-xl border border-dashed border-forest/50 bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm"
        >
          <span>
            <span className="font-display text-lg font-semibold text-ink">
              🔗 Handig materiaal
            </span>
            <span className="mt-1 block text-sm text-ink-dim">
              Links die we zelf gebruiken: vakfiches, naslagwerken en oefensites. Gratis, ook
              zonder account.
            </span>
          </span>
          <span aria-hidden className="shrink-0 text-forest">&rarr;</span>
        </Link>
      </main>
    </>
  );
}
