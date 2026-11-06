import type { SupabaseClient } from "@supabase/supabase-js";

/*
  De korte uitleg onder de titel van een hoofdstuk (supabase/hoofdstuk-uitleg.sql).

  Apart opgehaald en niet in de gewone select, zodat een pagina niet breekt
  zolang de kolom nog niet bestaat: dan komt er gewoon een lege lijst terug.
*/
export async function haalKorteUitleg(
  supabase: SupabaseClient,
  ids: string[],
): Promise<Map<string, string>> {
  const uitleg = new Map<string, string>();
  if (!ids.length) return uitleg;
  const { data, error } = await supabase
    .from("hoofdstukken")
    .select("id, korte_uitleg")
    .in("id", ids);
  if (error || !data) return uitleg;
  for (const rij of data as { id: string; korte_uitleg: string | null }[]) {
    const tekst = rij.korte_uitleg?.trim();
    if (tekst) uitleg.set(rij.id, tekst);
  }
  return uitleg;
}
