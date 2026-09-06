"use server";

import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";

export async function registreren(formData: FormData) {
  const naam = String(formData.get("naam") || "").trim();
  const email = String(formData.get("email") || "").trim();
  const password = String(formData.get("password") || "");
  const plusklasCode = String(formData.get("plusklas_code") || "").trim();

  if (!naam || !email || !password) {
    redirect(`/registreren?fout=${encodeURIComponent("Vul je naam, e-mailadres en een wachtwoord in.")}`);
  }
  if (password.length < 8) {
    redirect(`/registreren?fout=${encodeURIComponent("Kies een wachtwoord van minstens 8 tekens.")}`);
  }

  const admin = createAdminClient();

  let isPlusklas = false;
  if (plusklasCode) {
    const { data: code } = await admin
      .from("plusklas_codes")
      .select("code")
      .eq("code", plusklasCode)
      .eq("actief", true)
      .maybeSingle();
    if (!code) {
      redirect(`/registreren?fout=${encodeURIComponent("Deze plusklas-code klopt niet (meer). Laat het veld leeg om verder te gaan als betalend account.")}`);
    }
    isPlusklas = true;
  }

  const supabase = await createClient();
  const { data, error } = await supabase.auth.signUp({ email, password });

  if (error || !data.user) {
    redirect(`/registreren?fout=${encodeURIComponent(error?.message === "User already registered" ? "Er bestaat al een account met dit e-mailadres." : "Registreren is niet gelukt, probeer opnieuw.")}`);
  }

  const { error: profielFout } = await admin.from("profiles").insert({
    id: data.user.id,
    full_name: naam,
    role: "ouder",
    is_plusklas: isPlusklas,
  });

  if (profielFout) {
    redirect(`/registreren?fout=${encodeURIComponent("Account aangemaakt, maar het profiel kon niet bewaard worden. Neem contact op met Connectopia.")}`);
  }

  if (data.session) {
    redirect("/account");
  }

  redirect("/registreren/bevestig-email");
}
