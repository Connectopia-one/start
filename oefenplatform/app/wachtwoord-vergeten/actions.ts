"use server";

import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export async function stuurResetLink(formData: FormData) {
  const email = String(formData.get("email") || "").trim();
  if (!email) {
    redirect("/wachtwoord-vergeten?fout=" + encodeURIComponent("Vul je e-mailadres in."));
  }

  const supabase = await createClient();
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL!;
  await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${siteUrl}/wachtwoord-resetten`,
  });

  // Altijd dezelfde melding, ook als het e-mailadres niet bestaat — zo lekken we
  // niet welke adressen wel/niet geregistreerd zijn.
  redirect("/wachtwoord-vergeten?verstuurd=1");
}
