"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function maakGezin(formData: FormData) {
  await requireBeheerder();

  const fullName = String(formData.get("naam") || "").trim();
  const email = String(formData.get("email") || "").trim();
  const password = String(formData.get("wachtwoord") || "");

  if (!fullName || !email || password.length < 8) {
    redirect(
      "/beheer/gezinnen?fout=" +
        encodeURIComponent("Vul naam en e-mailadres in; wachtwoord moet minstens 8 tekens hebben.")
    );
  }

  const admin = createAdminClient();
  const { data: created, error } = await admin.auth.admin.createUser({
    email,
    password,
    email_confirm: true,
  });

  if (error || !created?.user) {
    redirect("/beheer/gezinnen?fout=" + encodeURIComponent(error?.message || "Aanmaken account mislukt."));
  }

  const { error: profileError } = await admin
    .from("profiles")
    .insert({ id: created.user.id, full_name: fullName, role: "ouder" });

  if (profileError) {
    redirect("/beheer/gezinnen?fout=" + encodeURIComponent(profileError.message));
  }

  revalidatePath("/beheer/gezinnen");
  redirect(`/beheer/gezinnen/${created.user.id}?succes=` + encodeURIComponent("Account aangemaakt."));
}

export async function upsertToegang(formData: FormData) {
  await requireBeheerder();

  const profileId = String(formData.get("profile_id") || "");
  const klasjeId = String(formData.get("klasje_id") || "");
  const materiaal = formData.get("materiaal") === "on";
  const fotos = formData.get("fotos") === "on";

  const admin = createAdminClient();

  if (!materiaal && !fotos) {
    await admin.from("toegang").delete().eq("profile_id", profileId).eq("klasje_id", klasjeId);
  } else {
    await admin
      .from("toegang")
      .upsert({ profile_id: profileId, klasje_id: klasjeId, materiaal, fotos }, { onConflict: "profile_id,klasje_id" });
  }

  revalidatePath(`/beheer/gezinnen/${profileId}`);
}

export async function verwijderGezin(formData: FormData) {
  await requireBeheerder();
  const profileId = String(formData.get("profile_id") || "");

  const admin = createAdminClient();
  await admin.auth.admin.deleteUser(profileId);

  revalidatePath("/beheer/gezinnen");
  redirect("/beheer/gezinnen?succes=" + encodeURIComponent("Account verwijderd."));
}
