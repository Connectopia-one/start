"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

/*
  Afvinken, en meteen een woordje terug naar wie het meldde.

  Kim op 29 september 2026: wie op de meldknop duwt, hoorde daarna niets meer.
  Het moment van afhandelen gaat er nu bij, en een antwoord mag. Wie ingelogd
  was toen hij meldde, ziet dat de volgende keer bovenaan het platform. Zet je
  de melding terug open, dan verdwijnt dat weer; anders zou er een bedankje
  blijven staan voor iets wat nog niet af is.
*/
export async function zetAfgehandeld(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const naar = String(formData.get("naar") || "true") === "true";
  const antwoord = String(formData.get("antwoord") || "").trim();

  const supabase = await createClient();
  const { error } = await supabase
    .from("meldingen")
    .update({
      afgehandeld: naar,
      afgehandeld_op: naar ? new Date().toISOString() : null,
      antwoord: naar ? antwoord.slice(0, 500) || null : null,
    })
    .eq("id", id);
  if (error) throw new Error(error.message);
  revalidatePath("/beheer/meldingen");
  revalidatePath("/");
}

export async function wisMelding(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const supabase = await createClient();
  const { error } = await supabase.from("meldingen").delete().eq("id", id);
  if (error) throw new Error(error.message);
  revalidatePath("/beheer/meldingen");
}
