"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";

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

/*
  Toch juist rekenen.

  Kim, 6 november 2026, na de enquête: een kind dat de vraag eigenlijk juist
  had maar fout gerekend werd (een synoniem, een schrijfwijze), meldt dat met
  de meldknop. Kim kijkt het na en kan dan met één klik het laatste antwoord
  van dat kind op die vraag alsnog juist zetten. Staan daarna alle vragen van
  het hoofdstuk juist, dan krijgt het kind alsnog zijn ster.

  Enkel de kinderen van wie meldde, enkel hun laatste antwoord op deze vraag,
  en enkel als dat fout stond. Er wordt niets gewist.
*/
export async function rekenTochJuist(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();

  const { data: melding } = await admin
    .from("meldingen")
    .select("vraag_id, hoofdstuk_id, profile_id")
    .eq("id", id)
    .single();
  if (!melding?.vraag_id || !melding.profile_id) return;

  const { data: kinderen } = await admin
    .from("kinderen")
    .select("id")
    .eq("profile_id", melding.profile_id);

  const { data: vragen } = await admin
    .from("vragen")
    .select("id")
    .eq("hoofdstuk_id", melding.hoofdstuk_id);
  const vraagIds = (vragen ?? []).map((v) => v.id as string);

  for (const kind of kinderen ?? []) {
    const { data: laatste } = await admin
      .from("voortgang")
      .select("id, correct")
      .eq("kind_id", kind.id)
      .eq("vraag_id", melding.vraag_id)
      .order("beantwoord_op", { ascending: false })
      .limit(1)
      .maybeSingle();
    if (!laatste || laatste.correct) continue;

    await admin.from("voortgang").update({ correct: true }).eq("id", laatste.id);

    // Alsnog een ster als nu elke vraag van het hoofdstuk juist staat.
    const { data: antwoorden } = await admin
      .from("voortgang")
      .select("vraag_id, correct, beantwoord_op")
      .eq("kind_id", kind.id)
      .eq("hoofdstuk_id", melding.hoofdstuk_id)
      .order("beantwoord_op", { ascending: false });
    const gezien = new Map<string, boolean>();
    for (const a of antwoorden ?? []) {
      if (a.vraag_id && !gezien.has(a.vraag_id)) gezien.set(a.vraag_id, a.correct);
    }
    const allesJuist =
      vraagIds.length > 0 && vraagIds.every((v) => gezien.get(v) === true);
    if (allesJuist) {
      await admin
        .from("stickers")
        .upsert(
          { kind_id: kind.id, hoofdstuk_id: melding.hoofdstuk_id },
          { onConflict: "kind_id,hoofdstuk_id", ignoreDuplicates: true },
        );
    }
  }

  revalidatePath("/beheer/meldingen");
}
