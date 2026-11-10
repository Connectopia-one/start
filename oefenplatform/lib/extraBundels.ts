/*
  Extra bundels per vak (supabase/extra-bundels.sql): examens op papier,
  lesbundels over het hele vak, ... los van de hoofdstukken.
*/
import type { Profile } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";

export type ExtraSoort = "examen" | "lesbundel" | "andere";

export type ExtraBundel = {
  id: string;
  vak_id: string;
  niveau: string;
  soort: ExtraSoort;
  titel: string;
  omschrijving: string | null;
  bestandspad: string;
  alleen_begeleiding: boolean;
  created_at: string;
};

export const extraSoorten: { slug: ExtraSoort; icoon: string; naam: string }[] = [
  { slug: "examen", icoon: "📝", naam: "Examen op papier" },
  { slug: "lesbundel", icoon: "📖", naam: "Lesbundel over het hele vak" },
  { slug: "andere", icoon: "📎", naam: "Andere bundel" },
];

export function extraSoort(slug: string) {
  return extraSoorten.find((s) => s.slug === slug) ?? extraSoorten[2];
}

export function isBegeleiding(profile: Profile | null): boolean {
  return profile?.role === "beheerder" || profile?.role === "begeleider";
}

/** Mag dit account deze extra bundel openen? */
export function magExtraBundel(
  bundel: Pick<ExtraBundel, "alleen_begeleiding">,
  profile: Profile | null,
): boolean {
  if (bundel.alleen_begeleiding) return isBegeleiding(profile);
  return heeftVolledigeToegang(profile) || isBegeleiding(profile);
}

/** Eerst de examens, dan de lesbundels, dan de rest; daarbinnen op titel. */
export function sorteerExtraBundels<T extends Pick<ExtraBundel, "soort" | "titel">>(rijen: T[]): T[] {
  const volgorde = extraSoorten.map((s) => s.slug as string);
  return [...rijen].sort(
    (a, b) =>
      volgorde.indexOf(a.soort) - volgorde.indexOf(b.soort) ||
      a.titel.localeCompare(b.titel, "nl", { numeric: true }),
  );
}
