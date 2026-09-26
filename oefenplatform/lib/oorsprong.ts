import { headers } from "next/headers";

/**
 * Het adres waarop deze site nú bereikt wordt, afgeleid van het binnenkomende
 * verzoek zelf.
 *
 * Bewust niet uit NEXT_PUBLIC_SITE_URL of uit de instelling "Site URL" van
 * Supabase: staat daar iets verkeerds (klassiek: localhost), dan komt er een
 * bevestigingslink in de mailbox van een ouder die op geen enkel toestel werkt,
 * en merk je dat zelf niet omdat jouw eigen account al lang bestaat.
 */
export async function oorsprong(): Promise<string> {
  const kop = await headers();
  const host = kop.get("x-forwarded-host") ?? kop.get("host") ?? "";
  const proto = kop.get("x-forwarded-proto") ?? "https";
  return host.startsWith("localhost") ? `http://${host}` : `${proto}://${host}`;
}
