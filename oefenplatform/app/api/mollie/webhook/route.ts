import { NextResponse, type NextRequest } from "next/server";
import { mollieClient } from "@/lib/mollie";
import { createAdminClient } from "@/lib/supabase/admin";

// Mollie stuurt hier een POST (form-encoded, veld "id") telkens de status van
// een betaling wijzigt. Moet altijd 200 teruggeven, ook bij een onbekende id,
// anders blijft Mollie het opnieuw proberen.
export async function POST(request: NextRequest) {
  const formData = await request.formData();
  const paymentId = String(formData.get("id") || "");
  if (!paymentId) return NextResponse.json({ ok: true });

  const payment = await mollieClient().payments.get(paymentId);
  const admin = createAdminClient();

  const nieuweStatus = payment.status === "paid"
    ? "betaald"
    : payment.status === "failed"
      ? "mislukt"
      : payment.status === "canceled"
        ? "geannuleerd"
        : payment.status === "expired"
          ? "verlopen"
          : "open";

  await admin
    .from("betalingen")
    .update({ status: nieuweStatus, betaald_op: nieuweStatus === "betaald" ? new Date().toISOString() : null })
    .eq("mollie_payment_id", paymentId);

  if (nieuweStatus === "betaald") {
    const metadata = (payment.metadata ?? {}) as { profile_id?: string; schooljaar?: string };
    const profileId = String(metadata.profile_id || "");
    const schooljaar = String(metadata.schooljaar || "");
    if (profileId && schooljaar) {
      await admin.from("profiles").update({ toegang_schooljaar: schooljaar }).eq("id", profileId);
    }
  }

  return NextResponse.json({ ok: true });
}
