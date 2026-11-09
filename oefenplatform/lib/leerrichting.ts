import { cookies } from "next/headers";

/*
  Kim, 9 november 2026, over geschiedenis Beyond: "dat ze kunnen klikken
  leren voor algemeen of leren voor welzijnswetenschappen want als ze zo alles
  moeten uitzoeken is echt wel moeilijk".

  Bedrijfs- en welzijnswetenschappen volgen bij geschiedenis een lichtere
  vakfiche (3DDG). Vragen over leerstof die zij niet nodig hebben, dragen het
  label niet_voor_dg (supabase/niet-voor-dg.sql). Kiest een leerling bovenaan
  het vak "bedrijfs- of welzijnswetenschappen", dan onthoudt een cookie dat,
  en dan vallen die vragen weg in de hoofdstukken en in het examen.
  Een cookie en geen kolom: zo werkt het ook zonder account en zonder sql.
*/
export const RICHTING_COOKIE = "leerrichting";

export async function leertVoorDg(): Promise<boolean> {
  return (await cookies()).get(RICHTING_COOKIE)?.value === "dg";
}
