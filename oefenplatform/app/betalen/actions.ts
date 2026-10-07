"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireIngelogd } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { huidigSchooljaar } from "@/lib/schooljaar";
import { isTestSleutel, mollieClient } from "@/lib/mollie";
import { zoekPlusklasCode } from "@/lib/plusklas";
import { PRIJS_NU_EUR } from "@/lib/prijs";
import { createAdminClient } from "@/lib/supabase/admin";

export async function startBetaling() {
  const session = await requireIngelogd();
  if (heeftVolledigeToegang(session.profile)) {
    redirect("/account");
  }

  if (isTestSleutel()) {
    redirect(
      "/betalen?fout=" +
        encodeURIComponent(
          "Betalen staat even stil: we zetten de betalingen juist. Stuur een mailtje naar info@matmgroep.com en we regelen je toegang met de hand.",
        ),
    );
  }

  const schooljaar = huidigSchooljaar();
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL!;
  const admin = createAdminClient();

  const payment = await mollieClient().payments.create({
    amount: { currency: "EUR", value: PRIJS_NU_EUR.toFixed(2) },
    description: `Oefenplatform Connectopia — toegang schooljaar ${schooljaar}`,
    redirectUrl: `${siteUrl}/betalen/voltooid`,
    webhookUrl: `${siteUrl}/api/mollie/webhook`,
    metadata: { profile_id: session.userId, schooljaar },
  });

  await admin.from("betalingen").insert({
    profile_id: session.userId,
    schooljaar,
    bedrag: PRIJS_NU_EUR,
    mollie_payment_id: payment.id,
    status: "open",
  });

  const checkoutUrl = payment.getCheckoutUrl();
  if (!checkoutUrl) {
    redirect("/betalen?fout=" + encodeURIComponent("Betaling starten is niet gelukt, probeer opnieuw."));
  }
  redirect(checkoutUrl);
}

/**
 * Een plusklas-code alsnog ingeven, nadat het account al aangemaakt is.
 * Wie bij het registreren het codeveld leeg liet, kan zo toch nog gratis
 * volledige toegang krijgen zonder een tweede account te moeten maken.
 */
export async function gebruikPlusklasCode(formData: FormData) {
  const session = await requireIngelogd();
  if (heeftVolledigeToegang(session.profile)) {
    redirect("/account");
  }

  const ingetikt = String(formData.get("plusklas_code") || "").trim();
  if (!ingetikt) {
    redirect("/betalen?fout=" + encodeURIComponent("Vul je plusklas-code in."));
  }

  const code = await zoekPlusklasCode(ingetikt);
  if (!code) {
    redirect(
      "/betalen?fout=" +
        encodeURIComponent(
          "Deze plusklas-code klopt niet (meer). Kijk ze na, of vraag ze opnieuw op bij Connectopia.",
        ),
    );
  }

  const admin = createAdminClient();
  // We bewaren ook mét welke code, zodat dit gezin in het juiste opvolgscherm
  // terechtkomt. Zie supabase/groepen.sql.
  const { error } = await admin
    .from("profiles")
    .update({ is_plusklas: true, plusklas_code: code })
    .eq("id", session.userId);

  if (error) {
    redirect(
      "/betalen?fout=" +
        encodeURIComponent("Je code klopt, maar we konden ze niet bewaren. Probeer het nog eens."),
    );
  }

  revalidatePath("/account");
  redirect("/account?gelukt=plusklas");
}
