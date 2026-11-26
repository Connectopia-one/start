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

/*
  Kim, 9 november 2026, bij wiskunde basis Beyond: welzijnswetenschappen en
  bedrijfswetenschappen hebben daar elk een andere vakfiche. Daarom drie
  knoppen in plaats van twee: een andere richting, bedrijfswetenschappen of
  welzijnswetenschappen. De oude waarde "dg" (van voor die dag, één knop voor
  beide) blijft geldig: bij geschiedenis telt ze als bedrijfs- of
  welzijnswetenschappen, bij wiskunde als een andere richting tot de leerling
  opnieuw kiest.
*/
/*
  Kim, 26 november 2026, na een mail van een ouder: sociale en
  gedragswetenschappen Beyond heeft een andere vakfiche voor humane
  wetenschappen (3DDO, met een groot blok politiek) dan voor
  welzijnswetenschappen (3DDG). Daar kies je tussen die twee. "humane" telt
  overal elders als "algemeen" (een andere richting): zie basisRichting.
*/
export type Leerrichting = "algemeen" | "humane" | "bedrijf" | "welzijn" | "dg";

export function leesRichting(waarde: string | undefined): Leerrichting {
  return waarde === "bedrijf" || waarde === "welzijn" || waarde === "dg" || waarde === "humane"
    ? waarde
    : "algemeen";
}

/** Humane wetenschappen is overal een andere richting, behalve waar een vak ze apart noemt. */
export function basisRichting(r: Leerrichting): Exclude<Leerrichting, "humane"> {
  return r === "humane" ? "algemeen" : r;
}

export async function leerrichting(): Promise<Leerrichting> {
  return leesRichting((await cookies()).get(RICHTING_COOKIE)?.value);
}

/** Bedrijfs- of welzijnswetenschappen: de lichtere fiche 3DDG (geschiedenis). */
export async function leertVoorDg(): Promise<boolean> {
  return basisRichting(await leerrichting()) !== "algemeen";
}

/*
  Hoofdstukken die voor een richting wegvallen, herkend aan het begin van hun
  titel (zie Wegwijzer.weglaten in inhoud/vaknoten.ts). Zo hoeft er niets in
  de databank te veranderen.
*/
export function valtWeg(
  titel: string,
  weglaten: Partial<Record<Leerrichting, string[]>> | undefined,
  richting: Leerrichting,
): boolean {
  const begin =
    richting === "humane"
      ? (weglaten?.humane ?? weglaten?.algemeen)
      : weglaten?.[richting === "dg" ? "algemeen" : richting];
  if (!begin) return false;
  const t = titel.trim().toLowerCase();
  return begin.some((b) => t.startsWith(b.toLowerCase()));
}
