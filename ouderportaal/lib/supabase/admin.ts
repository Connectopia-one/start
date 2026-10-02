import "server-only";
import { createClient as createSupabaseClient } from "@supabase/supabase-js";

/**
 * Gebruikt de service-role sleutel en omzeilt daarmee alle RLS-regels.
 * Enkel gebruiken in server actions, na een expliciete requireBeheerder()-check —
 * nooit importeren in een Client Component.
 */
export function createAdminClient() {
  return createSupabaseClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { autoRefreshToken: false, persistSession: false } }
  );
}

/*
  De naam van het Supabase-project waar dit portaal mee praat.

  Er zijn er twee, eentje voor het ouderportaal en eentje voor het
  oefenplatform, en ze zien er in het dashboard precies hetzelfde uit. Draait
  een sql-bestand in het verkeerde project, dan lijkt alles gelukt terwijl de
  tabel hier niet bestaat. Door deze naam in een foutmelding te zetten, hoeft
  niemand te gokken welk project hij open moet doen.

  Het adres is sowieso publiek: het staat in elke pagina die de browser laadt.
*/
export function projectnaam(): string | null {
  const adres = process.env.NEXT_PUBLIC_SUPABASE_URL;
  if (!adres) return null;
  try {
    return new URL(adres).hostname.split(".")[0] || null;
  } catch {
    return null;
  }
}
