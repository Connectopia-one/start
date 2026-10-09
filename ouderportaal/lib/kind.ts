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
].join(", ");

/* Twee velden die samen één regel vormen, bv. een naam en een telefoonnummer. */
export function samen(...delen: (string | null | undefined)[]) {
  return delen.filter(Boolean).join(" — ");
}
