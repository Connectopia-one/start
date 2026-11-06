"use server";

import { redirect } from "next/navigation";
import { createClient as createSupabaseClient } from "@supabase/supabase-js";
import { requireIngelogd, veiligVolgende } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import {
  geldigePin,
  haalPinHash,
  isOntgrendeld,
  maakPinHash,
  ontgrendel,
  pinKlopt,
  vergrendel,
} from "@/lib/ouderpin";

const wacht = (ms: number) => new Promise((r) => setTimeout(r, ms));

function terugNaar(formData: FormData) {
  return veiligVolgende(formData.get("terug")) ?? "/account";
}

/** De pincode ingeven om Mijn account en de voortgang te openen. */
export async function controleerPin(formData: FormData) {
  const session = await requireIngelogd();
  const terug = terugNaar(formData);
  const hash = await haalPinHash(session.userId);
  if (!hash) redirect(terug);
  const pin = String(formData.get("pin") ?? "").trim();
  if (!geldigePin(pin) || !pinKlopt(pin, hash)) {
    // Even wachten bij een fout getal: zo blijft eindeloos gokken saai.
    await wacht(1500);
    redirect(`/account/pincode?terug=${encodeURIComponent(terug)}&fout=1`);
  }
  await ontgrendel(session.userId, hash);
  redirect(terug);
}

/** Een pincode instellen of wijzigen. Wijzigen kan enkel als je al binnen bent. */
export async function zetPin(formData: FormData) {
  const session = await requireIngelogd();
  const huidige = await haalPinHash(session.userId);
  if (huidige && !(await isOntgrendeld(session.userId, huidige))) {
    redirect("/account/pincode?terug=/account");
  }
  const pin = String(formData.get("pin") ?? "").trim();
  const nogEens = String(formData.get("pin2") ?? "").trim();
  if (!geldigePin(pin)) {
    redirect(`/account?fout=${encodeURIComponent("Een pincode bestaat uit 4 cijfers.")}#pincode`);
  }
  if (pin !== nogEens) {
    redirect(`/account?fout=${encodeURIComponent("De twee pincodes zijn niet gelijk. Probeer het nog eens.")}#pincode`);
  }
  const hash = maakPinHash(pin);
  const { error } = await createAdminClient()
    .from("ouder_pincodes")
    .upsert({ profile_id: session.userId, pin_hash: hash, gewijzigd_op: new Date().toISOString() });
  if (error) {
    redirect(`/account?fout=${encodeURIComponent("De pincode kon niet bewaard worden. Probeer het later nog eens.")}#pincode`);
  }
  await ontgrendel(session.userId, hash);
  redirect("/account?gelukt=pincode#pincode");
}

/** De pincode weer uitzetten. Enkel als je al binnen bent. */
export async function zetPinUit() {
  const session = await requireIngelogd();
  const huidige = await haalPinHash(session.userId);
  if (huidige && !(await isOntgrendeld(session.userId, huidige))) {
    redirect("/account/pincode?terug=/account");
  }
  await createAdminClient().from("ouder_pincodes").delete().eq("profile_id", session.userId);
  await vergrendel();
  redirect("/account?gelukt=pincode-uit#pincode");
}

/** Meteen weer op slot, bijvoorbeeld voor je de computer aan je kind geeft. */
export async function vergrendelNu() {
  await vergrendel();
  redirect("/");
}

/**
 * Pincode vergeten: met het wachtwoord van het account gaat ze eraf. Het
 * wachtwoord kennen we enkel van de ouder, niet van het kind dat al
 * ingelogd is.
 */
export async function pinVergeten(formData: FormData) {
  const session = await requireIngelogd();
  const wachtwoord = String(formData.get("wachtwoord") ?? "");
  const terug = terugNaar(formData);
  if (!session.email || !wachtwoord) {
    redirect(`/account/pincode?terug=${encodeURIComponent(terug)}&vergeten=1&fout=2`);
  }
  // Een losse client zonder koekjes: dit controleert enkel het wachtwoord en
  // raakt de sessie in de browser niet.
  const los = createSupabaseClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    { auth: { autoRefreshToken: false, persistSession: false } },
  );
  const { data, error } = await los.auth.signInWithPassword({
    email: session.email,
    password: wachtwoord,
  });
  if (error || data.user?.id !== session.userId) {
    await wacht(1500);
    redirect(`/account/pincode?terug=${encodeURIComponent(terug)}&vergeten=1&fout=2`);
  }
  await los.auth.signOut().catch(() => {});
  await createAdminClient().from("ouder_pincodes").delete().eq("profile_id", session.userId);
  await vergrendel();
  redirect("/account?gelukt=pincode-vergeten#pincode");
}
