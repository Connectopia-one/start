"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireIngelogd } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function maakKind(formData: FormData) {
  const session = await requireIngelogd();
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) redirect("/account?fout=" + encodeURIComponent("Geef een naam op voor je kind."));

  const admin = createAdminClient();
  const { error } = await admin.from("kinderen").insert({ profile_id: session.userId, naam });
  if (error) redirect("/account?fout=" + encodeURIComponent("Kon je kind niet toevoegen, probeer opnieuw."));

  revalidatePath("/account");
  redirect("/account");
}
