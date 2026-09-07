"use server";

import { redirect } from "next/navigation";
import { headers } from "next/headers";
import { createClient } from "@/lib/supabase/server";

export async function stuurResetLink(formData: FormData) {
  const email = String(formData.get("email") || "").trim();
  if (!email) {
    redirect("/wachtwoord-vergeten?fout=" + encodeURIComponent("Vul je e-mailadres in."));
  }

  const supabase = await createClient();

  // Afgeleid van het echte inkomende verzoek in plaats van een omgevingsvariabele
  // (NEXT_PUBLIC_SITE_URL) — zo kan een verkeerd ingestelde variabele deze link
  // niet meer laten verwijzen naar het verkeerde adres (bv. localhost).
  const requestHeaders = await headers();
  const host = requestHeaders.get("host");
  const proto = requestHeaders.get("x-forwarded-proto") ?? "https";
  const origin = host?.startsWith("localhost") ? `http://${host}` : `${proto}://${host}`;

  await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${origin}/wachtwoord-resetten`,
  });

  // Altijd dezelfde melding, ook als het e-mailadres niet bestaat — zo lekken we
  // niet welke adressen wel/niet geregistreerd zijn.
  redirect("/wachtwoord-vergeten?verstuurd=1");
}
