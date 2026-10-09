"use server";

import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { zoekPlusklasCode } from "@/lib/plusklas";

export async function login(formData: FormData) {
  const email = String(formData.get("email") || "").trim();
  const password = String(formData.get("password") || "");

  if (!email || !password) {
    redirect(`/login?fout=${encodeURIComponent("Vul zowel je e-mailadres als je wachtwoord in.")}`);
  }

  const supabase = await createClient();
  const { error } = await supabase.auth.signInWithPassword({ email, password });

  if (error) {
    /*
      Febe, een tester, probeerde op 9 oktober 2026 in te loggen met de
      toegangscode in het wachtwoordveld. Dat is een begrijpelijke vergissing:
      in de brief staat één code, en een inlogscherm vraagt één wachtwoord.
      Typte iemand een echte code, dan zeggen we dat in plaats van het
      nietszeggende "wachtwoord klopt niet".
    */
    const code = await zoekPlusklasCode(password);
    if (code) {
      redirect(
        `/login?fout=${encodeURIComponent(
          `${code} is een toegangscode, geen wachtwoord. Heb je nog geen account? Maak er hieronder een aan en vul de code in tijdens het registreren. Heb je er al een, log dan in met je eigen wachtwoord.`,
        )}`,
      );
    }
    redirect(`/login?fout=${encodeURIComponent("E-mailadres of wachtwoord klopt niet.")}`);
  }

  redirect("/account");
}

export async function logout() {
  const supabase = await createClient();
  await supabase.auth.signOut();
  redirect("/login");
}
