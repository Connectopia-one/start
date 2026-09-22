import "server-only";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Zoekt een actieve plusklas-code. Hoofdletters maken niet uit, en spaties
 * vooraan of achteraan evenmin — ouders typen de code over van een brief of
 * een bericht, en dan sluipt daar makkelijk een verschil in.
 *
 * Geeft de code terug zoals ze in de databank staat, of null als ze niet
 * bestaat of niet meer actief is.
 *
 * Dit draait enkel op de server, met de service-role-sleutel: de codes zijn
 * nooit rechtstreeks vanuit de browser te lezen.
 */
export async function zoekPlusklasCode(ingetikt: string): Promise<string | null> {
  const gezocht = ingetikt.trim().toLowerCase();
  if (!gezocht) return null;

  const admin = createAdminClient();
  const { data } = await admin.from("plusklas_codes").select("code").eq("actief", true);

  const gevonden = (data ?? []).find((rij) => rij.code.trim().toLowerCase() === gezocht);
  return gevonden?.code ?? null;
}
