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
  if (
    m.includes("already registered") ||
    m.includes("already been registered")
  ) {
    return "Er bestaat al een account met dit e-mailadres. Log in, of vraag een nieuw wachtwoord aan.";
  }
  if (
    m.includes("rate limit") ||
    m.includes("you can only request this after")
  ) {
    return "Er zijn net te veel accounts na elkaar aangemaakt, en de mailserver houdt dat tegen. Probeer over een uurtje opnieuw, of laat het ons weten.";
  }
  if (m.includes("password")) {
    return "Dit wachtwoord wordt niet aanvaard. Kies er een van minstens 8 tekens.";
  }
  if (
    m.includes("email") &&
    (m.includes("invalid") || m.includes("validate"))
  ) {
    return "Dit e-mailadres wordt niet aanvaard. Kijk het even na op een typfout.";
  }
  if (m.includes("signups not allowed") || m.includes("signup is disabled")) {
    return "Registreren staat op dit moment uit. Laat het ons weten, dan zetten we het weer open.";
  }
  return `Registreren is niet gelukt. De melding luidt: ${melding}`;
}

/**
 * Het profiel van een account dat al bestond bijwerken.
 *
 * Hier mag `role` niet mee: wie al beheerder of begeleider is en zich per
 * ongeluk opnieuw registreert, zou anders teruggezet worden op "ouder".
 * `is_plusklas` zetten we enkel áán, nooit uit: een leeg codeveld betekent
 * "ik vul niets in", niet "haal mijn gratis toegang weg". Hetzelfde geldt voor
 * `plusklas_code`: die schrijven we alleen als er écht een code ingevuld is,
 * zodat iemand die zich een tweede keer registreert zonder code niet uit zijn
 * groep valt.
 */
async function vulProfielAan(
  userId: string,
  naam: string,
  isPlusklas: boolean,
  code: string | null,
) {
  const admin = createAdminClient();
  const rij: Record<string, unknown> = { id: userId, full_name: naam };
  if (isPlusklas) rij.is_plusklas = true;
  if (code) rij.plusklas_code = code;
  return admin.from("profiles").upsert(rij, { onConflict: "id" });
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

  const supabase = await createClient();

  let isPlusklas = false;
  // De code zoals ze in de databank staat, niet zoals ze ingetikt werd. Daarmee
  // weten we later bij welke groep dit gezin hoort; zie supabase/groepen.sql.
  let gevondenCode: string | null = null;
  if (plusklasCode) {
    const code = await zoekPlusklasCode(plusklasCode);
    if (!code) {
      terug(
        "Deze plusklas-code klopt niet (meer). Laat het veld leeg om verder te gaan als betalend account — je kan de code later nog ingeven.",
      );
    }
    isPlusklas = true;
    gevondenCode = code;
  }

  // Ben je al ingelogd met precies dit adres, dan is deze registratie al
  // gelukt en kom je hier een tweede keer voorbij: door twee keer te klikken,
  // door het formulier opnieuw te versturen, of met de terugknop van de
  // browser. Supabase antwoordt dan "User already registered", en dat lazen
  // ouders als "het is mislukt" terwijl hun account er gewoon stond. Kim
  // meldde dat op 30 september 2026 voor haar zoon.
  //
  // Dus: eerst kijken of we onszelf tegenkomen, en zo ja gewoon afwerken.
  // De knop op slot zetten volstaat niet — die zit in de browser, en hier
  // hoort de controle die er altijd is. Zie components/Verzendknop.tsx.
  const { data: reeds } = await supabase.auth.getUser();
  if (
    reeds.user?.email &&
    reeds.user.email.toLowerCase() === email.toLowerCase()
  ) {
    const { error: aanvulFout } = await vulProfielAan(
      reeds.user.id,
      naam,
      isPlusklas,
      gevondenCode,
    );
    if (aanvulFout) {
      console.error("profiel aanvullen mislukt:", aanvulFout.message);
      terug(
        `Je account bestaat al en je bent ingelogd, maar het profiel kon niet bewaard worden (${aanvulFout.message}). Laat het ons weten, dan zetten we het recht.`,
      );
    }
    redirect("/account");
  }

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
    terug(
      "Registreren is niet gelukt. Probeer het opnieuw, of laat het ons weten.",
    );
  }

  // Bestaat het adres al en staat e-mailbevestiging aan, dan geeft Supabase
  // expres géén fout terug (anders kan je uitvissen wie er een account heeft).
  // Je herkent het aan een lege lijst identiteiten. Zonder deze controle liep
  // het verderop stuk op een profiel dat niet kon worden bewaard.
  if (data.user.identities && data.user.identities.length === 0) {
    terug(
      "Er bestaat al een account met dit e-mailadres. Log in, of vraag een nieuw wachtwoord aan.",
    );
  }

  const admin = createAdminClient();
  // Bewust een upsert: probeert iemand het een tweede keer nadat het de eerste
  // keer halverwege strandde, dan mag het profiel er gerust al staan.
  const { error: profielFout } = await admin
    .from("profiles")
    .upsert(
      {
        id: data.user.id,
        full_name: naam,
        role: "ouder",
        is_plusklas: isPlusklas,
        plusklas_code: gevondenCode,
      },
      { onConflict: "id" },
    );

  if (profielFout) {
    console.error("profiel bewaren mislukt:", profielFout.message);
    terug(
      `Je account is aangemaakt, maar het profiel kon niet bewaard worden (${profielFout.message}). Laat het ons weten, dan zetten we het recht.`,
    );
  }

  if (data.session) {
    redirect("/account");
  }

  redirect("/registreren/bevestig-email");
}
