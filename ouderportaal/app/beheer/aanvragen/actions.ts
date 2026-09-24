"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Het beheer van de aanvragen die via de website binnenkomen. Ze staan in
  dezelfde databank; het schema staat in  website/supabase/aanvragen.sql
*/

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

function terug(bericht: string, fout = false): never {
  revalidatePath("/beheer/aanvragen");
  redirect(
    `/beheer/aanvragen?${fout ? "fout" : "succes"}=${encodeURIComponent(bericht)}`
  );
}

export async function zetAfgehandeld(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const afgehandeld = String(formData.get("afgehandeld") || "") === "ja";

  const { error } = await db
    .from("aanvragen")
    .update({ afgehandeld, gezien: true })
    .eq("id", id);

  if (error) terug(error.message, true);
  terug(
    afgehandeld
      ? "Aanvraag staat op afgehandeld."
      : "Aanvraag staat weer open."
  );
}

export async function markeerAllesGezien() {
  const db = await admin();
  const { error } = await db
    .from("aanvragen")
    .update({ gezien: true })
    .eq("gezien", false);

  if (error) terug(error.message, true);
  terug("Alles staat op gelezen.");
}

export async function verwijderAanvraag(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const { error } = await db.from("aanvragen").delete().eq("id", id);
  if (error) terug(error.message, true);
  terug("Aanvraag verwijderd.");
}
