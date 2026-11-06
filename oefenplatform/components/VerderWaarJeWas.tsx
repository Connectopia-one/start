import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

/*
  "Verder waar je was": per kind één knop naar het hoofdstuk waar het laatst
  een vraag in beantwoordde.

  Uit de enquête van november 2026. Sarah (mama van Merlijn): "Hij vond niet
  direct zijn lessen terug, waardoor hij dan afgeleid werd." Marjolein en Linda:
  het is ver terug naar het beginscherm. Zo staat het laatste hoofdstuk meteen
  bovenaan, zonder eerst langs categorie en vak te klikken.

  Nog niets geoefend, of gaat het ophalen mis, dan tekent dit niets.
*/
type Rij = {
  kind_id: string;
  hoofdstuk: {
    titel: string;
    volgnummer: number;
    vak: { slug: string; naam: string } | { slug: string; naam: string }[] | null;
  } | null;
};

export async function VerderWaarJeWas({ userId }: { userId: string }) {
  const supabase = await createClient();
  const { data: kinderen } = await supabase
    .from("kinderen")
    .select("id, naam")
    .eq("profile_id", userId)
    .order("naam");
  if (!kinderen?.length) return null;

  const { data, error } = await supabase
    .from("voortgang")
    .select(
      "kind_id, hoofdstuk:hoofdstukken(titel, volgnummer, vak:vakken(slug, naam))",
    )
    .in(
      "kind_id",
      kinderen.map((k) => k.id),
    )
    .not("hoofdstuk_id", "is", null)
    .order("beantwoord_op", { ascending: false })
    .limit(200);
  if (error || !data) return null;

  // De eerste rij per kind is de jongste.
  const laatste = new Map<string, Rij>();
  for (const rij of data as unknown as Rij[]) {
    if (!laatste.has(rij.kind_id) && rij.hoofdstuk) laatste.set(rij.kind_id, rij);
  }

  const knoppen = kinderen
    .map((k) => {
      const rij = laatste.get(k.id);
      const h = rij?.hoofdstuk;
      const vak = Array.isArray(h?.vak) ? h?.vak[0] : h?.vak;
      if (!h || !vak) return null;
      return {
        kind: k.naam as string,
        href: `/vakken/${vak.slug}/${h.volgnummer}`,
        vak: vak.naam,
        titel: h.titel,
      };
    })
    .filter((k): k is NonNullable<typeof k> => k !== null);
  if (!knoppen.length) return null;

  const meerdere = kinderen.length > 1;

  return (
    <section className="mb-8">
      <h2 className="font-display text-base font-semibold text-ink">
        Verder waar je was
      </h2>
      <div className="mt-2 grid gap-2 sm:grid-cols-2">
        {knoppen.map((k) => (
          <Link
            key={k.kind + k.href}
            href={k.href}
            className="flex items-center justify-between gap-3 rounded-xl border border-forest/40 bg-forest/5 px-4 py-3 transition hover:border-forest"
          >
            <span className="text-sm">
              {meerdere && (
                <span className="block text-xs text-ink-dim">{k.kind}</span>
              )}
              <span className="block font-medium text-ink">{k.titel}</span>
              <span className="block text-xs text-ink-dim">{k.vak}</span>
            </span>
            <span aria-hidden className="shrink-0 text-forest-dark">
              &rarr;
            </span>
          </Link>
        ))}
      </div>
    </section>
  );
}
