"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function maakCode(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "").trim();
  const label = String(formData.get("label") || "").trim() || null;
  if (!code) redirect("/beheer/codes?fout=" + encodeURIComponent("Geef een code op."));

  const admin = createAdminClient();
  const { error } = await admin.from("plusklas_codes").insert({ code, label });
  if (error) redirect("/beheer/codes?fout=" + encodeURIComponent("Kon code niet aanmaken (bestaat die al?)."));

  revalidatePath("/beheer/codes");
  redirect("/beheer/codes");
}

export async function wisselActief(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "");
  const actief = formData.get("actief") === "true";
  const admin = createAdminClient();
  await admin.from("plusklas_codes").update({ actief: !actief }).eq("code", code);
  revalidatePath("/beheer/codes");
  redirect("/beheer/codes");
}

export async function verwijderCode(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "");
  const admin = createAdminClient();
  await admin.from("plusklas_codes").delete().eq("code", code);
  revalidatePath("/beheer/codes");
  redirect("/beheer/codes");
}
