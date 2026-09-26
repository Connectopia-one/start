"use server";

import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { zoekPlusklasCode } from "@/lib/plusklas";
import { oorsprong } from "@/lib/oorsprong";

function terug(bericht: string): never {
  redirect(`/registreren?fout=${encodeURIComponent(bericht)}`);
}

/**
 * De foutmelding van Supabase omzetten naar iets dat een ouder begrijpt.
 *
 * Alles wat we niet herkennen, tonen we gewoon letterlijk. Dat is lelijker,
 * maar oneindig veel bruikbaarder dan "probeer opnieuw": zonder de echte tekst
 * kan niemand — ook wij niet — zien waarom het misloopt.
 */
function inMensentaal(melding: string): string {
  const m = melding.toLowerCase();
  if (m.includes("already registered") || m.includes("already been registered")) {
    return "Er bestaat al een account met dit e-mailadres. Log in, of vraag een nieuw wachtwoord aan.";
  }
  if (m.includes("rate limit") || m.includes("you can only request this after")) {
    return "Er zijn net te veel accounts na elkaar aangemaakt, en de mailserver houdt dat tegen. Probeer over een uurtje opnieuw, of laat het ons weten.";
  }
  if (m.includes("password")) {
    return "Dit wachtwoord wordt niet aanvaard. Kies er een van minstens 8 tekens.";
  }
  if (m.includes("email") && (m.includes("invalid") || m.includes("validate"))) {
    return "Dit e-mailadres wordt niet aanvaard. Kijk het even na op een typfout.";
  }
  if (m.includes("signups not allowed") || m.includes("signup is disabled")) {
    return "Registreren staat op dit moment uit. Laat het ons weten, dan zetten we het weer open.";
  }
  return `Registreren is niet gelukt. De melding luidt: ${melding}`;
}

export async function registreren(formData: FormData) {
  const naam = String(formData.get("naam") || "").trim();
  const email = String(formData.get("email") || "").trim();
  const password = String(formData.get("password") || "");
  const plusklasCode = String(formData.get("plusklas_code") || "").trim();

  if (!naam || !email || !password) {
    terug("Vul je naam, e-mailadres en een wachtwoord in.");
  }
  if (password.length < 8) {
    terug("Kies een wachtwoord van minstens 8 tekens.");
  }

  const admin = createAdminClient();

  let isPlusklas = false;
  if (plusklasCode) {
    const code = await zoekPlusklasCode(plusklasCode);
    if (!code) {
      terug(
        "Deze plusklas-code klopt niet (meer). Laat het veld leeg om verder te gaan als betalend account — je kan de code later nog ingeven."
      );
    }
    isPlusklas = true;
  }

  const supabase = await createClient();
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    // Zonder dit valt de bevestigingslink terug op de "Site URL" van Supabase.
    // Zie lib/oorsprong.ts en app/auth/bevestigen/route.ts.
    options: { emailRedirectTo: `${await oorsprong()}/auth/bevestigen` },
  });

  if (error) {
    console.error("signUp fout:", error.message);
    terug(inMensentaal(error.message));
  }
  if (!data.user) {
    console.error("signUp gaf geen gebruiker terug");
    terug("Registreren is niet gelukt. Probeer het opnieuw, of laat het ons weten.");
  }

  // Bestaat het adres al en staat e-mailbevestiging aan, dan geeft Supabase
  // expres géén fout terug (anders kan je uitvissen wie er een account heeft).
  // Je herkent het aan een lege lijst identiteiten. Zonder deze controle liep
  // het verderop stuk op een profiel dat niet kon worden bewaard.
  if (data.user.identities && data.user.identities.length === 0) {
    terug(
      "Er bestaat al een account met dit e-mailadres. Log in, of vraag een nieuw wachtwoord aan."
    );
  }

  // Bewust een upsert: probeert iemand het een tweede keer nadat het de eerste
  // keer halverwege strandde, dan mag het profiel er gerust al staan.
  const { error: profielFout } = await admin
    .from("profiles")
    .upsert(
      { id: data.user.id, full_name: naam, role: "ouder", is_plusklas: isPlusklas },
      { onConflict: "id" }
    );

  if (profielFout) {
    console.error("profiel bewaren mislukt:", profielFout.message);
    terug(
      `Je account is aangemaakt, maar het profiel kon niet bewaard worden (${profielFout.message}). Laat het ons weten, dan zetten we het recht.`
    );
  }

  if (data.session) {
    redirect("/account");
  }

  redirect("/registreren/bevestig-email");
}
