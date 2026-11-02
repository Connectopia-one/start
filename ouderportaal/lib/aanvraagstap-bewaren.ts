import "server-only";
import { createAdminClient } from "@/lib/supabase/admin";
import { wisselStap, type Stap } from "@/lib/aanvraagstappen";

/*
  Een stap bewaren bij een aanvraag.

  Betaald is een uitzondering: een gezin met twee kinderen schrijft in met
  één overschrijving en één mededeling ("Kamp 12345"), maar elk kind is een
  eigen aanvraag. Zet je bij het ene kind betaald aan, dan geldt dat voor
  alle aanvragen met dezelfde mededeling. Anders moet je het per kind
  opnieuw aanklikken en vergeet je er een.

  Geeft een foutboodschap terug, of null als het lukte. Nooit gooien: een fout in een
  serveractie wordt anders de onleesbare React-fout 441.
*/
export async function zetStapVoorGezin(
  id: string,
  stap: Stap,
  aan: boolean,
): Promise<{ fout: string | null; aantal: number }> {
  const db = createAdminClient();
  const { data, error } = await db
    .from("aanvragen")
    .select("id, stappen, gegevens")
    .eq("id", id)
    .single();
  if (error || !data) return { fout: error?.message ?? "Niet gevonden.", aantal: 0 };

  type Rij = { id: string; stappen: string[] | null; gegevens: Record<string, string> };
  let rijen: Rij[] = [data as Rij];
  const mededeling = (data as Rij).gegevens?.["Mededeling"]?.trim();
  if (stap === "betaald" && mededeling) {
    const { data: gezin, error: gezinFout } = await db
      .from("aanvragen")
      .select("id, stappen, gegevens")
      .eq("gegevens->>Mededeling", mededeling);
    if (gezinFout) return { fout: gezinFout.message, aantal: 0 };
    if (gezin?.length) rijen = gezin as Rij[];
  }

  for (const rij of rijen) {
    const { error: fout } = await db
      .from("aanvragen")
      .update({ stappen: wisselStap(rij.stappen ?? [], stap, aan), gezien: true })
      .eq("id", rij.id);
    if (fout) return { fout: fout.message, aantal: 0 };
  }
  return { fout: null, aantal: rijen.length };
}
