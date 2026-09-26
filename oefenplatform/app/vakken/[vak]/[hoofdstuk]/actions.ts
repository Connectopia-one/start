"use server";

import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

const SOORTEN = ["fout", "onduidelijk", "te-moeilijk", "te-makkelijk", "andere"] as const;
type Soort = (typeof SOORTEN)[number];

/**
 * Een melding bij een hoofdstuk: iets dat niet klopt, onduidelijk is of te
 * moeilijk of te makkelijk zit. Mag ook zonder account, want de gratis
 * hoofdstukken staan open. Wie ingelogd is, krijgt zijn account mee, zodat
 * Kim kan terugkoppelen; wie niet ingelogd is, blijft anoniem.
 */
export async function meldIets(formData: FormData) {
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vraagIdRuw = String(formData.get("vraag_id") || "").trim();
  const soortRuw = String(formData.get("soort") || "fout");
  const bericht = String(formData.get("bericht") || "").trim();

  if (!hoofdstukId) throw new Error("Er ging iets mis: het hoofdstuk ontbreekt.");
  if (!bericht) throw new Error("Schrijf er even bij wat er niet klopt.");
  if (bericht.length > 2000) throw new Error("Hou het bij maximaal 2000 tekens.");

  const soort: Soort = (SOORTEN as readonly string[]).includes(soortRuw)
    ? (soortRuw as Soort)
    : "fout";

  const session = await getSessionProfile();
  const supabase = await createClient();

  const { error } = await supabase.from("meldingen").insert({
    hoofdstuk_id: hoofdstukId,
    vraag_id: vraagIdRuw || null,
    profile_id: session?.userId ?? null,
    soort,
    bericht,
  });
  if (error) throw new Error("Versturen lukte niet: " + error.message);
}
