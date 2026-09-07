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

  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${origin}/wachtwoord-resetten`,
  });

  if (error) {
    // Supabase geeft voor dit endpoint sowieso geen "bestaat niet"-fout terug
    // (dat verbergt het zelf al) — een fout hier is dus altijd iets anders
    // (bv. snelheidslimiet op e-mails) en is veilig om te tonen.
    console.error("resetPasswordForEmail fout:", error.message);
    redirect("/wachtwoord-vergeten?fout=" + encodeURIComponent(error.message));
  }

  redirect("/wachtwoord-vergeten?verstuurd=1");
}
