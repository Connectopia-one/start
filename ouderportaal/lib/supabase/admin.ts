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
