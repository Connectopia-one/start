"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function maakTeamlid(formData: FormData) {
  await requireBeheerder();

  const fullName = String(formData.get("naam") || "").trim();
  const email = String(formData.get("email") || "").trim();
  const password = String(formData.get("wachtwoord") || "");

  if (!fullName || !email || password.length < 8) {
    redirect(
      "/beheer/team?fout=" +
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
    redirect("/beheer/team?fout=" + encodeURIComponent(error?.message || "Aanmaken account mislukt."));
  }

  const { error: profileError } = await admin
    .from("profiles")
    .insert({ id: created.user.id, full_name: fullName, role: "leerkracht" });

  if (profileError) {
    redirect("/beheer/team?fout=" + encodeURIComponent(profileError.message));
  }

  revalidatePath("/beheer/team");
  redirect("/beheer/team?succes=" + encodeURIComponent(`Teamlid "${fullName}" aangemaakt.`));
}

export async function wijzigTeamlidWachtwoord(formData: FormData) {
  await requireBeheerder();

  const profileId = String(formData.get("profile_id") || "");
  const wachtwoord = String(formData.get("wachtwoord") || "");

  if (wachtwoord.length < 8) {
    redirect("/beheer/team?fout=" + encodeURIComponent("Wachtwoord moet minstens 8 tekens hebben."));
  }

  const admin = createAdminClient();
  const { error } = await admin.auth.admin.updateUserById(profileId, { password: wachtwoord });
  if (error) {
    redirect("/beheer/team?fout=" + encodeURIComponent(error.message));
  }

  revalidatePath("/beheer/team");
  redirect("/beheer/team?succes=" + encodeURIComponent("Nieuw wachtwoord ingesteld."));
}

export async function verwijderTeamlid(formData: FormData) {
  await requireBeheerder();
  const profileId = String(formData.get("profile_id") || "");

  const admin = createAdminClient();
  await admin.auth.admin.deleteUser(profileId);

  revalidatePath("/beheer/team");
  redirect("/beheer/team?succes=" + encodeURIComponent("Teamlid verwijderd."));
}
