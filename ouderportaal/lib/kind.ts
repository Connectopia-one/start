/*
  De inlichtingenfiche van één kind.

  Drie schermen tonen dezelfde fiche: de ouder op /portaal/gezin, het team op
  /team/kinderen en de beheerder op /beheer/gezinnen. Vroeger schreef elk
  scherm zijn eigen lijstje kolommen uit, en dan loopt dat uiteen zodra er een
  veld bij komt. Nu staat de lijst hier, één keer.

  Zet je er een veld bij? Dan op vier plaatsen:
    1. supabase/inlichtingenfiche.sql, zodat de kolom bestaat
    2. hier, in het type en in KINDVELDEN
    3. app/portaal/gezin/actions.ts, in fichevelden(), zodat het bewaard wordt
    4. app/portaal/gezin/page.tsx, zodat de ouder het kan invullen
*/

export type Kind = {
  id: string;
  naam: string;
  geboortedatum: string | null;
  allergieen: string | null;
  diagnoses: string | null;
  noodcontact_naam: string | null;
  noodcontact_telefoon: string | null;
  toestemming_fotos: boolean;
  toestemming_social_media: boolean;
  /* Wat een dag op een kamp nog nodig heeft. */
  medicatie: string | null;
  huisarts_naam: string | null;
  huisarts_telefoon: string | null;
  noodcontact2_naam: string | null;
  noodcontact2_telefoon: string | null;
  ophalen: string | null;
  alleen_naar_huis: boolean;
  eten: string | null;
  wat_helpt: string | null;
  school: string | null;
  leerjaar: string | null;
  /* Wanneer er voor het laatst iets aan deze fiche veranderd is. */
  updated_at: string;
};

export const KINDVELDEN = [
  "id",
  "naam",
  "geboortedatum",
  "allergieen",
  "diagnoses",
  "noodcontact_naam",
  "noodcontact_telefoon",
  "toestemming_fotos",
  "toestemming_social_media",
  "medicatie",
  "huisarts_naam",
  "huisarts_telefoon",
  "noodcontact2_naam",
  "noodcontact2_telefoon",
  "ophalen",
  "alleen_naar_huis",
  "eten",
  "wat_helpt",
  "school",
  "leerjaar",
  "updated_at",
].join(", ");

/* Twee velden die samen één regel vormen, bv. een naam en een telefoonnummer. */
export function samen(...delen: (string | null | undefined)[]) {
  return delen.filter(Boolean).join(" — ");
}

/*
  Is deze fiche klaar voor een kamp?

  Kim op 12 oktober 2026: "kan ik op een manier zien wie nog geen
  inlichtingsfiche invulde? Want dit moet voor de start van het kamp in orde
  zijn? Nu moet ik elk kind afzonderlijk openklikken."

  De moeilijkheid: de meeste velden mogen met opzet leeg blijven. Een leeg vak
  bij allergieën kan "geen allergieën" betekenen of "nog niet ingevuld", en dat
  verschil is van buitenaf niet te zien. We kijken daarom enkel naar de velden
  die voor een kind op een kamp nóóit leeg horen te zijn. Staan die er, dan is
  de fiche in orde; staat er iets niet bij, dan zeggen we precies wat.

  Vandaar ook dat hier geen "nagekeken"-vinkje staat: een vinkje dat een ouder
  vergeet aan te kruisen, maakt een fiche die wél in orde is toch rood, en dan
  gaat Kim bellen voor niets.
*/
export function watOntbreekt(kind: Kind): string[] {
  const ontbreekt: string[] = [];
  if (!kind.geboortedatum) ontbreekt.push("de geboortedatum");
  if (!kind.noodcontact_telefoon && !kind.noodcontact2_telefoon) {
    ontbreekt.push("een noodnummer");
  }
  if (!kind.ophalen && !kind.alleen_naar_huis) {
    ontbreekt.push("wie het mag ophalen");
  }
  return ontbreekt;
}

/* Hetzelfde voor het gezin zelf: zonder deze twee bereiken we niemand. */
export function watOntbreektGezin(gezin: {
  telefoon: string | null;
  adres: string | null;
}): string[] {
  const ontbreekt: string[] = [];
  if (!gezin.telefoon) ontbreekt.push("het telefoonnummer");
  if (!gezin.adres) ontbreekt.push("het adres");
  return ontbreekt;
}

/* "de geboortedatum en een noodnummer" */
export function lijstZin(delen: string[]): string {
  if (delen.length <= 1) return delen[0] ?? "";
  return delen.slice(0, -1).join(", ") + " en " + delen[delen.length - 1];
}
