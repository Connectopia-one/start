import type { Profile } from "@/lib/auth";
import { huidigSchooljaar } from "@/lib/schooljaar";

/** Heeft dit account volledige toegang tot alle hoofdstukken (niet enkel de gratis)? */
export function heeftVolledigeToegang(profile: Profile | null): boolean {
  if (!profile) return false;
  if (profile.role === "beheerder") return true;
  if (profile.is_plusklas) return true;
  if (gratisTotNogGeldig(profile.gratis_tot)) return true;
  return profile.toegang_schooljaar === huidigSchooljaar();
}

/** Mag dit account dit specifieke hoofdstuk zien? */
export function hoofdstukToegankelijk(hoofdstukGratis: boolean, profile: Profile | null): boolean {
  return hoofdstukGratis || heeftVolledigeToegang(profile);
}

/**
 * Gratis toegang met een einddatum (supabase/enquete-en-reviews.sql).
 * De datum zelf telt nog mee: "tot en met 31 augustus 2027".
 */
export function gratisTotNogGeldig(gratisTot: string | null | undefined, nu = new Date()): boolean {
  if (!gratisTot) return false;
  const vandaag = nu.toLocaleDateString("sv-SE", { timeZone: "Europe/Brussels" });
  return gratisTot >= vandaag;
}
