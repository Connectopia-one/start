import type { Profile } from "@/lib/auth";
import { huidigSchooljaar } from "@/lib/schooljaar";

/** Heeft dit account volledige toegang tot alle hoofdstukken (niet enkel de gratis)? */
export function heeftVolledigeToegang(profile: Profile | null): boolean {
  if (!profile) return false;
  if (profile.role === "beheerder") return true;
  if (profile.is_plusklas) return true;
  return profile.toegang_schooljaar === huidigSchooljaar();
}

/** Mag dit account dit specifieke hoofdstuk zien? */
export function hoofdstukToegankelijk(hoofdstukGratis: boolean, profile: Profile | null): boolean {
  return hoofdstukGratis || heeftVolledigeToegang(profile);
}
