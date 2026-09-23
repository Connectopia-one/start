import "server-only";
import type { createAdminClient } from "@/lib/supabase/admin";

type Tabel = "hoofdstukken" | "vragen";
type OuderKolom = "vak_id" | "hoofdstuk_id";

/**
 * Deelt vrije volgnummers uit binnen één vak (voor hoofdstukken) of één
 * hoofdstuk (voor vragen).
 *
 * Tel daarvoor niet hoeveel rijen er al staan. Wie een hoofdstuk of een vraag
 * verwijdert, laat een gat achter: van zes hoofdstukken blijven er dan vijf
 * over, genummerd 2 tot en met 6. "Vijf plus één" is 6, en dat nummer is al
 * bezet. De databank laat elk nummer maar één keer toe per vak (en per
 * hoofdstuk voor vragen), dus het toevoegen mislukte dan met een foutmelding
 * over een "duplicate key".
 *
 * We nemen daarom telkens het láágste nummer dat nog vrij is. Staat er een gat
 * omdat je net iets verwijderde, dan gaat het nieuwe hoofdstuk op die plek
 * terug staan in plaats van achteraan de lijst. Is er geen gat, dan komt het
 * gewoon achteraan, net als vroeger.
 *
 * De teruggegeven functie onthoudt wat ze al uitdeelde, zodat je ze bij een
 * import ook meerdere keren na elkaar kan gebruiken.
 */
export async function vrijeVolgnummers(
  admin: ReturnType<typeof createAdminClient>,
  tabel: Tabel,
  ouderKolom: OuderKolom,
  ouderId: string
): Promise<() => number> {
  const { data } = await admin.from(tabel).select("volgnummer").eq(ouderKolom, ouderId);
  const bezet = new Set<number>(
    (data ?? []).map((rij) => rij.volgnummer as number).filter((n) => typeof n === "number")
  );

  let kandidaat = 0;
  return () => {
    do {
      kandidaat += 1;
    } while (bezet.has(kandidaat));
    bezet.add(kandidaat);
    return kandidaat;
  };
}

/** Eén vrij volgnummer, voor wie er maar eentje nodig heeft. */
export async function volgendVolgnummer(
  admin: ReturnType<typeof createAdminClient>,
  tabel: Tabel,
  ouderKolom: OuderKolom,
  ouderId: string
): Promise<number> {
  const neem = await vrijeVolgnummers(admin, tabel, ouderKolom, ouderId);
  return neem();
}
