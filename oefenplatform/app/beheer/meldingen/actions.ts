"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

export async function zetAfgehandeld(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const naar = String(formData.get("naar") || "true") === "true";
  const supabase = await createClient();
  const { error } = await supabase.from("meldingen").update({ afgehandeld: naar }).eq("id", id);
  if (error) throw new Error(error.message);
  revalidatePath("/beheer/meldingen");
}

export async function wisMelding(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const supabase = await createClient();
  const { error } = await supabase.from("meldingen").delete().eq("id", id);
  if (error) throw new Error(error.message);
  revalidatePath("/beheer/meldingen");
}
