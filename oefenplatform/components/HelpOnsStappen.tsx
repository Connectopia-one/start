import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

/*
  De twee stappen van "Help ons beter worden": de enquête en een review.

  Staat bovenaan /enquete en /reviews, zodat een gezin altijd ziet wat al
  binnen is en wat nog moet. Kim keurt daarna zelf goed (Beheer → Enquêtes en
  reviews); pas dan verschijnt hier dat de beloning klaarstaat.

  Zolang supabase/enquete-en-reviews.sql niet gedraaid is, bestaan de tabellen
  nog niet. Dan tekent dit blokje niets, in plaats van de pagina te breken.
*/
export async function HelpOnsStappen({ userId }: { userId: string }) {
  const supabase = await createClient();
  const [enquete, review, beloning] = await Promise.all([
    supabase.from("enquetes").select("id").eq("profile_id", userId).maybeSingle(),
    supabase.from("reviews").select("id, goedgekeurd").eq("profile_id", userId).maybeSingle(),
    supabase.from("beloningen").select("soort").eq("profile_id", userId).maybeSingle(),
  ]);
  if (enquete.error || review.error) return null;

  return (
    <HelpOnsKaart
      enqueteKlaar={Boolean(enquete.data)}
      reviewKlaar={Boolean(review.data)}
      beloning={(beloning.data?.soort as Beloning | undefined) ?? null}
    />
  );
}

type Beloning = "vaste_prijs" | "gratis_toegang";

/*
  Het tekenen zelf. Zelfde opbouw als "Verder waar je was" eronder: een kopje
  en twee kaarten naast elkaar, even breed als de rest van de pagina. Kim op
  7 november 2026: het oude witte blok met twee tekstlinks was smaller dan de
  rest en leek dubbel met het oranje bericht. Nu zijn het twee vrolijke
  klikknoppen; wat al binnen is, kleurt groen met een vinkje.
*/
export function HelpOnsKaart({
  enqueteKlaar,
  reviewKlaar,
  beloning,
  bezoeker = false,
}: {
  enqueteKlaar: boolean;
  reviewKlaar: boolean;
  beloning: Beloning | null;
  /* Wie niet ingelogd is, ziet het blok ook (Kim, 7 november 2026). De
     reviews lezen kan zonder account; de enquête vraagt eerst om in te
     loggen, want we koppelen de antwoorden aan het gezin. */
  bezoeker?: boolean;
}) {
  const stappen = bezoeker
    ? [
        {
          href: "/enquete",
          emoji: "💬",
          titel: "Vul de enquête in",
          uitleg: "Log eerst in. Alleen wij lezen je antwoorden",
          klaar: false,
        },
        {
          href: "/reviews",
          emoji: "⭐",
          titel: "Lees de reviews",
          uitleg: "Echte reviews van onze gezinnen",
          klaar: false,
        },
      ]
    : [
    {
      href: "/enquete",
      emoji: "💬",
      titel: "Vul de enquête in",
      uitleg: "Alleen wij lezen je antwoorden",
      klaar: enqueteKlaar,
    },
    {
      href: "/reviews#schrijf",
      emoji: "⭐",
      titel: "Schrijf een eerlijke review",
      uitleg: "Komt op het reviewbord als wij hem ophangen",
      klaar: reviewKlaar,
    },
  ];

  return (
    <section className="mt-6">
      <h2 className="font-display text-base font-semibold text-ink">
        Help ons het platform beter maken
      </h2>
      <div className="mt-2 grid gap-3 sm:grid-cols-2">
        {stappen.map((s) => (
          <Link
            key={s.href}
            href={s.href}
            className={
              "group flex items-center gap-4 rounded-xl border px-4 py-3 transition hover:-translate-y-0.5 hover:shadow-sm " +
              (s.klaar
                ? "border-forest/40 bg-forest/10 hover:border-forest"
                : "border-amber/40 bg-amber/10 hover:border-amber")
            }
          >
            <span
              aria-hidden
              className={
                "flex h-11 w-11 shrink-0 items-center justify-center rounded-full text-xl transition group-hover:scale-110 " +
                (s.klaar ? "bg-forest text-white" : "bg-surface")
              }
            >
              {s.klaar ? "✓" : s.emoji}
            </span>
            <span className="min-w-0 flex-1 text-sm">
              <span className="block font-medium text-ink">{s.titel}</span>
              <span className="block text-xs text-ink-dim">
                {s.klaar ? "Gedaan, dank je wel!" : s.uitleg}
              </span>
            </span>
            <span aria-hidden className="shrink-0 text-ink-dim transition group-hover:translate-x-0.5 group-hover:text-ink">
              &rarr;
            </span>
          </Link>
        ))}
      </div>
      {beloning ? (
        <p className="mt-3 rounded-xl bg-forest/10 px-4 py-3 text-sm text-forest-dark">
          {beloning === "vaste_prijs"
            ? "Dank je wel! We hebben alles gelezen. Jouw prijs blijft 20 euro per schooljaar, ook als de prijs later stijgt."
            : "Dank je wel! We hebben alles gelezen. Je hebt gratis toegang tot en met 31 augustus 2027."}
        </p>
      ) : enqueteKlaar && reviewKlaar ? (
        <p className="mt-3 text-sm text-ink-dim">
          Allebei binnen, dank je wel! Kim leest alles zelf na. Zodra dat gebeurd is, zie je hier
          wat je als bedankje krijgt.
        </p>
      ) : null}
    </section>
  );
}
