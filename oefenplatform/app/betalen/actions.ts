"use server";

import { redirect } from "next/navigation";
import { requireIngelogd } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { huidigSchooljaar } from "@/lib/schooljaar";
import { mollieClient, PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";
import { createAdminClient } from "@/lib/supabase/admin";

export async function startBetaling() {
  const session = await requireIngelogd();
  if (heeftVolledigeToegang(session.profile)) {
    redirect("/account");
  }

  const schooljaar = huidigSchooljaar();
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL!;
  const admin = createAdminClient();

  const payment = await mollieClient().payments.create({
    amount: { currency: "EUR", value: PRIJS_SCHOOLJAAR_EUR.toFixed(2) },
    description: `Oefenplatform Connectopia — toegang schooljaar ${schooljaar}`,
    redirectUrl: `${siteUrl}/betalen/voltooid`,
    webhookUrl: `${siteUrl}/api/mollie/webhook`,
    metadata: { profile_id: session.userId, schooljaar },
  });

  await admin.from("betalingen").insert({
    profile_id: session.userId,
    schooljaar,
    bedrag: PRIJS_SCHOOLJAAR_EUR,
    mollie_payment_id: payment.id,
    status: "open",
  });

  const checkoutUrl = payment.getCheckoutUrl();
  if (!checkoutUrl) {
    redirect("/betalen?fout=" + encodeURIComponent("Betaling starten is niet gelukt, probeer opnieuw."));
  }
  redirect(checkoutUrl);
}
