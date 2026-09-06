"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { slugify } from "@/lib/slug";

export async function maakKlasje(formData: FormData) {
  await requireBeheerder();

  const naam = String(formData.get("naam") || "").trim();
  if (!naam) redirect("/beheer?fout=" + encodeURIComponent("Geef het klasje een naam."));

  const admin = createAdminClient();
  let slug = slugify(naam);
  if (!slug) slug = `klasje-${Date.now()}`;

  const { error } = await admin.from("klasjes").insert({ naam, slug });
  if (error) {
    const boodschap = error.code === "23505" ? "Er bestaat al een klasje met (bijna) deze naam." : error.message;
    redirect("/beheer?fout=" + encodeURIComponent(boodschap));
  }

  revalidatePath("/beheer");
  redirect("/beheer?succes=" + encodeURIComponent(`Klasje "${naam}" aangemaakt.`));
}

export async function hernoemKlasje(formData: FormData) {
  await requireBeheerder();

  const id = String(formData.get("id") || "");
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) redirect("/beheer?fout=" + encodeURIComponent("De naam mag niet leeg zijn."));

  const admin = createAdminClient();
  const { error } = await admin.from("klasjes").update({ naam }).eq("id", id);
  if (error) redirect("/beheer?fout=" + encodeURIComponent(error.message));

  revalidatePath("/beheer");
  redirect("/beheer?succes=" + encodeURIComponent("Naam bijgewerkt."));
}
