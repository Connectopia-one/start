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
