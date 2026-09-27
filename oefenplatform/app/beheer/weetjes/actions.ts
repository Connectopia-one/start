"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

/** Hangt een weetje op, of haalt het weer van het bord. */
export async function zetOpgehangen(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const op = String(formData.get("naar") || "true") === "true";
  const supabase = await createClient();

  const { error } = await supabase
    .from("weetjes")
    .update({ goedgekeurd: op, opgehangen_op: op ? new Date().toISOString() : null })
    .eq("id", id);
  if (error) throw new Error(error.message);

  revalidatePath("/beheer/weetjes");
  revalidatePath("/weetjes");
}

/**
 * Past de tekst of de voornaam aan voor het ophangen.
 *
 * Een kind schrijft al eens iets met een tikfout of met zijn hele naam erbij;
 * dan is verbeteren vriendelijker dan weigeren.
 */
export async function pasWeetjeAan(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const tekst = String(formData.get("tekst") || "").trim();
  const voornaam = String(formData.get("voornaam") || "").trim();
  if (!tekst) return;

  const supabase = await createClient();
  const { error } = await supabase
    .from("weetjes")
    .update({ tekst: tekst.slice(0, 500), voornaam: voornaam.slice(0, 40) || null })
    .eq("id", id);
  if (error) throw new Error(error.message);

  revalidatePath("/beheer/weetjes");
  revalidatePath("/weetjes");
}

export async function wisWeetje(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const supabase = await createClient();
  const { error } = await supabase.from("weetjes").delete().eq("id", id);
  if (error) throw new Error(error.message);

  revalidatePath("/beheer/weetjes");
  revalidatePath("/weetjes");
}
