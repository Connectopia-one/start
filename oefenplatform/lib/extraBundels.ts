/*
  Extra bundels per vak (supabase/extra-bundels.sql): examens op papier,
  lesbundels over het hele vak, ... los van de hoofdstukken.
*/
import type { Profile } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";

/*
  Kim, 10 november 2026: zolang niet elk vak een nieuwe lesbundel heeft,
  blijven de oude "Hele cursus downloaden" en de nieuwe lesbundel allebei
  staan. De nieuwe staat dan bij de extra bundels als "Uitgebreide lesbundel".
  Heeft elk vak er een, zet dit dan op true: dan opent "Hele cursus
  downloaden" de nieuwe lesbundel (vakken zonder lesbundel houden de oude).
*/
export const LESBUNDEL_VERVANGT_CURSUS = false;

export type ExtraSoort = "examen" | "lesbundel" | "andere";

export type ExtraBundel = {
  id: string;
  vak_id: string;
  niveau: string;
  soort: ExtraSoort;
  titel: string;
  omschrijving: string | null;
  bestandspad: string;
  verbetersleutel: boolean;
  created_at: string;
};

export const extraSoorten: { slug: ExtraSoort; icoon: string; naam: string }[] = [
  { slug: "examen", icoon: "📝", naam: "Examen op papier" },
  { slug: "lesbundel", icoon: "📖", naam: "Uitgebreide lesbundel over het hele vak" },
  { slug: "andere", icoon: "📎", naam: "Andere bundel" },
];

export function extraSoort(slug: string) {
  return extraSoorten.find((s) => s.slug === slug) ?? extraSoorten[2];
}

export function isBegeleiding(profile: Profile | null): boolean {
  return profile?.role === "beheerder" || profile?.role === "begeleider";
}

/**
 * Mag dit account deze extra bundel zien op de vakpagina? Een verbetersleutel
 * vraagt bij het openen voor een ouder nog de ouderpincode (zie de route).
 */
export function magExtraBundel(profile: Profile | null): boolean {
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
