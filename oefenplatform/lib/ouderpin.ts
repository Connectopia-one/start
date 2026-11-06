import "server-only";
import { createHmac, randomBytes, scryptSync, timingSafeEqual } from "node:crypto";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Pincode voor ouders. Kim, november 2026: een kind dat zelfstandig oefent,
  logt in met het account van de ouder. Wil de ouder de voortgang en de lijst
  met foute vragen voor zichzelf houden, dan zet die in Mijn account een
  pincode. Wie dat niet doet, merkt hier niets van.

  De pincode zelf bewaren we nooit, enkel een hash, in een tabel die alleen de
  server mag lezen (supabase/ouder-pincode.sql). Na het juiste getal krijgt de
  browser een koekje dat een halfuur geldig is. Verandert de pincode, dan
  klopt het koekje niet meer.
*/

const KOEKJE = "ouderpin";
const GELDIG_MINUTEN = 30;

function sleutel() {
  return process.env.SUPABASE_SERVICE_ROLE_KEY ?? "";
}

export function geldigePin(pin: unknown): pin is string {
  return typeof pin === "string" && /^\d{4}$/.test(pin);
}

export function maakPinHash(pin: string) {
  const zout = randomBytes(16).toString("hex");
  const hash = scryptSync(pin, zout, 32).toString("hex");
  return `${zout}:${hash}`;
}

export function pinKlopt(pin: string, opgeslagen: string) {
  const [zout, hash] = opgeslagen.split(":");
  if (!zout || !hash) return false;
  const nu = scryptSync(pin, zout, 32);
  const was = Buffer.from(hash, "hex");
  return was.length === nu.length && timingSafeEqual(was, nu);
}

/** De hash van de pincode van deze ouder, of null als er geen is. */
export async function haalPinHash(userId: string): Promise<string | null> {
  const { data, error } = await createAdminClient()
    .from("ouder_pincodes")
    .select("pin_hash")
    .eq("profile_id", userId)
    .maybeSingle();
  // Zolang ouder-pincode.sql niet gedraaid is, bestaat de tabel niet. Dan is
  // er ook geen pincode, en mag niets daarop vastlopen.
  if (error || !data) return null;
  return data.pin_hash as string;
}

function handtekening(userId: string, hash: string, tot: number) {
  return createHmac("sha256", sleutel()).update(`${userId}|${hash}|${tot}`).digest("hex");
}

export async function isOntgrendeld(userId: string, hash: string) {
  const waarde = (await cookies()).get(KOEKJE)?.value ?? "";
  const [tot, sig] = waarde.split(".");
  const totGetal = Number(tot);
  if (!totGetal || totGetal < Date.now() || !sig) return false;
  const juist = handtekening(userId, hash, totGetal);
  return sig.length === juist.length && timingSafeEqual(Buffer.from(sig), Buffer.from(juist));
}

export async function ontgrendel(userId: string, hash: string) {
  const tot = Date.now() + GELDIG_MINUTEN * 60 * 1000;
  (await cookies()).set(KOEKJE, `${tot}.${handtekening(userId, hash, tot)}`, {
    httpOnly: true,
    sameSite: "lax",
    secure: true,
    path: "/",
    maxAge: GELDIG_MINUTEN * 60,
  });
}

export async function vergrendel() {
  (await cookies()).delete(KOEKJE);
}

/**
 * Staat er een pincode op dit account en is ze niet net ingegeven, dan gaat
 * de bezoeker eerst langs /account/pincode en daarna terug naar `terug`.
 * Geeft terug of er een pincode is.
 */
export async function vereisOuderPin(userId: string, terug: string): Promise<boolean> {
  const hash = await haalPinHash(userId);
  if (!hash) return false;
  if (!(await isOntgrendeld(userId, hash))) {
    redirect(`/account/pincode?terug=${encodeURIComponent(terug)}`);
  }
  return true;
}
