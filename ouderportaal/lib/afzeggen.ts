import type { SupabaseClient } from "@supabase/supabase-js";
import {
  AFGEZEGD,
  afgezegdVoor,
  maakGroepen,
  vindWaarde,
  type Aanvraag,
} from "@/lib/aanvraaglijsten";
import { zoekKind } from "@/lib/kindzoeken";
import { portaalKinderen } from "@/lib/portaalkinderen";

/*
  Een kind dat bij Kampen en lessen "van de lijst" gaat, ook bij de
  inschrijvingen van die dag als afgezegd noteren.

  Kim op 3 november 2026 haalde drie kinderen van een kamplijst, en meteen
  stond er "Er schreven nog 3 kinderen in die hier nog niet staan. Zet ze
  erbij". Van de lijst halen betekent: komt niet. Dus zetten we
  "Afgezegd voor <dag>" in de inschrijving, net als de knop op Lijsten uit
  de inschrijvingen (zie lib/aanvraaglijsten.ts).
*/
export async function noteerAfgezegd(
  db: SupabaseClient,
  dag: string,
  kindId: string,
) {
  const { data } = await db
    .from("aanvragen")
    .select("id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at")
    .limit(1000);
  const groep = maakGroepen((data ?? []) as Aanvraag[]).find(
    (g) => g.naam === dag,
  );
  if (!groep) return 0;

  const portaal = await portaalKinderen();
  let aantal = 0;
  for (const rij of groep.rijen) {
    const gevonden = zoekKind(
      rij.kind,
      {
        gsm: vindWaarde(rij.aanvraag.gegevens, "gsm"),
        mail: vindWaarde(rij.aanvraag.gegevens, "mail"),
      },
      portaal,
    );
    if (gevonden?.id !== kindId) continue;
    const namen = [...afgezegdVoor(rij.aanvraag, dag), rij.kind];
    const gegevens = { ...rij.aanvraag.gegevens, [AFGEZEGD + dag]: namen.join(", ") };
    const { error } = await db
      .from("aanvragen")
      .update({ gegevens })
      .eq("id", rij.aanvraag.id);
    if (!error) {
      rij.aanvraag.gegevens = gegevens;
      aantal++;
    }
  }
  return aantal;
}
