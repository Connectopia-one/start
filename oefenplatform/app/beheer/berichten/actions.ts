"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

/*
  Berichten van Kim aan de ouders. Zie supabase/berichten.sql.

  Er vertrekt nergens een mail: het bericht verschijnt bovenaan het platform
  bij iedereen die ingelogd is.
*/

function opnieuwTekenen() {
  revalidatePath("/beheer/berichten");
  revalidatePath("/");
}

export async function plaatsBericht(formData: FormData) {
  await requireBeheerder();
  const titel = String(formData.get("titel") || "").trim();
  const tekst = String(formData.get("tekst") || "").trim();
  const link = String(formData.get("link") || "").trim();
  const linktekst = String(formData.get("linktekst") || "").trim();
  if (!titel || !tekst) return;

  const supabase = await createClient();
  const { error } = await supabase.from("berichten").insert({
    titel: titel.slice(0, 120),
    tekst: tekst.slice(0, 2000),
    link: link.slice(0, 300) || null,
    linktekst: linktekst.slice(0, 60) || null,
    actief: true,
  });
  if (error) throw new Error(error.message);

  opnieuwTekenen();
}

/** Zet een bericht aan of uit. Uit betekent: meteen bij iedereen weg. */
export async function zetBerichtActief(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const naar = String(formData.get("naar") || "true") === "true";

  const supabase = await createClient();
  const { error } = await supabase
    .from("berichten")
    .update({ actief: naar })
    .eq("id", id);
  if (error) throw new Error(error.message);

  opnieuwTekenen();
}

export async function wisBericht(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");

  const supabase = await createClient();
  const { error } = await supabase.from("berichten").delete().eq("id", id);
  if (error) throw new Error(error.message);

  opnieuwTekenen();
}
