/*
  De ingevulde inlichtingenfiche uit een formulier halen.

  Twee schermen tonen hetzelfde formulier (components/KindVelden.tsx): de ouder
  op /portaal/gezin en de beheerder op /beheer/gezinnen/<id>. Allebei moeten ze
  er exact dezelfde kolommen uit halen, anders bewaart het ene scherm een veld
  dat het andere laat vallen. Daarom staat dat hier één keer.

  Zet je er een veld bij, dan op vier plaatsen: supabase/inlichtingenfiche.sql,
  lib/kind.ts (het type en KINDVELDEN), dit bestand, en het formulier in
  components/KindVelden.tsx.
*/

function tekst(formData: FormData, naam: string): string | null {
  return String(formData.get(naam) || "").trim() || null;
}

export function ficheUitFormulier(formData: FormData) {
  return {
    naam: String(formData.get("naam") || "").trim(),
    geboortedatum: tekst(formData, "geboortedatum"),
    allergieen: tekst(formData, "allergieen"),
    diagnoses: tekst(formData, "diagnoses"),
    noodcontact_naam: tekst(formData, "noodcontact_naam"),
    noodcontact_telefoon: tekst(formData, "noodcontact_telefoon"),
    toestemming_fotos: formData.get("toestemming_fotos") === "on",
    toestemming_social_media: formData.get("toestemming_social_media") === "on",
    /* Wat een dag op een kamp nog nodig heeft. */
    medicatie: tekst(formData, "medicatie"),
    huisarts_naam: tekst(formData, "huisarts_naam"),
    huisarts_telefoon: tekst(formData, "huisarts_telefoon"),
    noodcontact2_naam: tekst(formData, "noodcontact2_naam"),
    noodcontact2_telefoon: tekst(formData, "noodcontact2_telefoon"),
    ophalen: tekst(formData, "ophalen"),
    alleen_naar_huis: formData.get("alleen_naar_huis") === "on",
    eten: tekst(formData, "eten"),
    wat_helpt: tekst(formData, "wat_helpt"),
    school: tekst(formData, "school"),
    leerjaar: tekst(formData, "leerjaar"),
  };
}
