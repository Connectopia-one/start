import "server-only";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Het mailadres van een account.

  Kim op 11 oktober 2026: "ik zie nergens van dit account het mailadres staan,
  bij niemand." Dat klopte: in `profiles` staan enkel de naam, de rol, het
  telefoonnummer en het adres. Het mailadres is waarmee iemand inlogt, en dat
  houdt Supabase zelf bij in auth.users. Je kan het dus niet zomaar meevragen
  met een gewone select; het moet via de beheerderskant van Supabase, met de
  sleutel die enkel op de server staat.

  Daarom hier, achter server-only: geen enkel scherm van een ouder mag hier
  per ongeluk aan.
*/

export async function mailadresVan(id: string): Promise<string | null> {
  const admin = createAdminClient();
  const { data, error } = await admin.auth.admin.getUserById(id);
  if (error) return null;
  return data.user?.email ?? null;
}

/*
  Alle mailadressen in één keer, voor een lijst. Supabase geeft ze per bladzij
  terug, dus we halen er een paar na elkaar op tot er niets meer komt. Meer
  dan tienduizend accounts gaan we hier niet hebben; dan nog stopt het.
*/
export async function alleMailadressen(): Promise<Map<string, string>> {
  const admin = createAdminClient();
  const adressen = new Map<string, string>();
  const perBlad = 1000;

  for (let blad = 1; blad <= 10; blad++) {
    const { data, error } = await admin.auth.admin.listUsers({
      page: blad,
      perPage: perBlad,
    });
    if (error) break;
    for (const gebruiker of data.users) {
      if (gebruiker.email) adressen.set(gebruiker.id, gebruiker.email);
    }
    if (data.users.length < perBlad) break;
  }

  return adressen;
}
