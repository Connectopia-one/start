"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

/*
  Kims knoppen bij de enquêtes en reviews.

  Goedkeuren gebeurt nooit vanzelf (Kim, 5 november 2026: "ik keur het graag
  na mijn review van hun antwoorden goed"). Twee soorten beloning:
    * een testgezin krijgt gratis toegang tot en met 31 augustus 2027,
    * een gezin dat al betaalde, houdt de vaste prijs van 20 euro.
  Allebei kunnen ongedaan gemaakt worden, voor het geval je je vergist.
*/

const GRATIS_TOT = "2027-08-31";
const VASTE_PRIJS_EUR = 20;

function herlaad() {
  revalidatePath("/beheer/enquetes");
  revalidatePath("/beheer/gezinnen");
  revalidatePath("/reviews");
  revalidatePath("/enquete");
}

export async function keurGoed(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("profile_id") || "");
  const soort = String(formData.get("soort") || "");
  if (!id || (soort !== "gratis_toegang" && soort !== "vaste_prijs")) return;

  const supabase = await createClient();
  const { error: fout1 } = await supabase
    .from("profiles")
    .update(soort === "gratis_toegang" ? { gratis_tot: GRATIS_TOT } : { vaste_prijs_eur: VASTE_PRIJS_EUR })
    .eq("id", id);
  if (fout1) throw new Error(fout1.message);

  const { error: fout2 } = await supabase
    .from("beloningen")
    .upsert({ profile_id: id, soort, goedgekeurd_op: new Date().toISOString() });
  if (fout2) throw new Error(fout2.message);

  herlaad();
}

/** Een goedkeuring terugdraaien. De enquête en review zelf blijven staan. */
export async function trekGoedkeuringIn(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("profile_id") || "");
  if (!id) return;

  const supabase = await createClient();
  const { data: beloning } = await supabase
    .from("beloningen")
    .select("soort")
    .eq("profile_id", id)
    .maybeSingle();
  if (!beloning) return;

  const { error } = await supabase
    .from("profiles")
    .update(beloning.soort === "gratis_toegang" ? { gratis_tot: null } : { vaste_prijs_eur: null })
    .eq("id", id);
  if (error) throw new Error(error.message);

  await supabase.from("beloningen").delete().eq("profile_id", id);
  herlaad();
}

/** Een review ophangen, of weer van het bord halen. */
export async function zetReviewOpgehangen(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const op = String(formData.get("naar") || "true") === "true";
  const supabase = await createClient();

  const { error } = await supabase
    .from("reviews")
    .update({
      goedgekeurd: op,
      opgehangen_op: op ? new Date().toISOString() : null,
      niet_geplaatst: false,
    })
    .eq("id", id);
  if (error) throw new Error(error.message);
  herlaad();
}

/**
 * Een review (nog) niet ophangen, met een woordje voor het gezin.
 *
 * Bedoeld voor een review met een achternaam van een kind of iets anders dat
 * niet op een openbaar bord hoort, niet om kritiek tegen te houden.
 */
export async function zetReviewNietGeplaatst(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const bericht = String(formData.get("bericht") || "").trim();
  const supabase = await createClient();

  const { error } = await supabase
    .from("reviews")
    .update({
      niet_geplaatst: true,
      goedgekeurd: false,
      opgehangen_op: null,
      bericht: bericht.slice(0, 500) || null,
    })
    .eq("id", id);
  if (error) throw new Error(error.message);
  herlaad();
}
