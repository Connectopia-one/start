"use server";

import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { oorsprong } from "@/lib/oorsprong";

export async function stuurResetLink(formData: FormData) {
  const email = String(formData.get("email") || "").trim();
  if (!email) {
    redirect("/wachtwoord-vergeten?fout=" + encodeURIComponent("Vul je e-mailadres in."));
  }

  const supabase = await createClient();

  const origin = await oorsprong();

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
