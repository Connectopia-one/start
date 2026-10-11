"use server";

import { revalidatePath } from "next/cache";
import { requirePortaalSessie } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Bij welk gezin horen de gegevens van dit scherm?

  Normaal bij jezelf. Kijk je als beheerder mee met een gezin, dan toont het
  scherm de gegevens van dat gezin, en dan horen ze daar ook bewaard te worden.

  Hier stond eerst een slot: tijdens het meekijken wierp elke actie een fout.
  Dat was precies verkeerd om. Kim op 11 oktober 2026: "ik heb al 3 x proberen
  de inlichtingsfiche in te vullen en dit wordt niet bewaard." Een fout uit een
  server action komt niet als een zin op het scherm maar verdwijnt, dus het
  scherm deed gewoon niets, drie keer na elkaar. En er was geen andere weg:
  een kind toevoegen voor een gezin dat zijn fiche niet zelf invult kon
  nergens. Nu bewaart dit scherm bij het gezin waar je naar kijkt, en staat er
  bovenaan dat scherm dat dat zo is.

  De les: een actie die mag mislukken geeft een zin terug; een actie die niets
  hoort te doen hoort niet te bestaan. Zie ook lib/meekijken.ts.
*/
async function gezinVanDitScherm() {
  const sessie = await requirePortaalSessie();
  return sessie.userId;
}

/*
  De velden van de inlichtingenfiche die bij een kamp horen. Ze staan apart
  omdat voegKindToe en wijzigKind er allebei exact hetzelfde mee doen; wie er
  een veld bij zet, zet het hier en nergens anders.
*/
function fichevelden(formData: FormData) {
  const tekst = (naam: string) =>
    String(formData.get(naam) || "").trim() || null;

  return {
    medicatie: tekst("medicatie"),
    huisarts_naam: tekst("huisarts_naam"),
    huisarts_telefoon: tekst("huisarts_telefoon"),
    noodcontact2_naam: tekst("noodcontact2_naam"),
    noodcontact2_telefoon: tekst("noodcontact2_telefoon"),
    ophalen: tekst("ophalen"),
    alleen_naar_huis: formData.get("alleen_naar_huis") === "on",
    eten: tekst("eten"),
    wat_helpt: tekst("wat_helpt"),
    school: tekst("school"),
    leerjaar: tekst("leerjaar"),
  };
}

export async function wijzigContactgegevens(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const telefoon = String(formData.get("telefoon") || "").trim() || null;
  const adres = String(formData.get("adres") || "").trim() || null;

  const admin = createAdminClient();
  await admin
    .from("profiles")
    .update({ telefoon, adres })
    .eq("id", gezinId);

  revalidatePath("/portaal/gezin");
}

export async function voegKindToe(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) return;

  const geboortedatum =
    String(formData.get("geboortedatum") || "").trim() || null;
  const allergieen = String(formData.get("allergieen") || "").trim() || null;
  const diagnoses = String(formData.get("diagnoses") || "").trim() || null;
  const noodcontactNaam =
    String(formData.get("noodcontact_naam") || "").trim() || null;
  const noodcontactTelefoon =
    String(formData.get("noodcontact_telefoon") || "").trim() || null;
  const toestemmingFotos = formData.get("toestemming_fotos") === "on";
  const toestemmingSocialMedia =
    formData.get("toestemming_social_media") === "on";

  const admin = createAdminClient();

  // Klikt iemand twee keer op Toevoegen omdat de pagina traag laadt, dan zou
  // hetzelfde kind er twee keer in komen. Staat die naam er al, dan doen we niets.
  const { data: bestaande } = await admin
    .from("kinderen")
    .select("naam")
    .eq("profile_id", gezinId);
  const alGekend = (bestaande ?? []).some(
    (k: { naam: string }) => k.naam.trim().toLowerCase() === naam.toLowerCase(),
  );
  if (alGekend) {
    revalidatePath("/portaal/gezin");
    return;
  }

  await admin.from("kinderen").insert({
    profile_id: gezinId,
    naam,
    geboortedatum,
    allergieen,
    diagnoses,
    noodcontact_naam: noodcontactNaam,
    noodcontact_telefoon: noodcontactTelefoon,
    toestemming_fotos: toestemmingFotos,
    toestemming_social_media: toestemmingSocialMedia,
    ...fichevelden(formData),
  });

  revalidatePath("/portaal/gezin");
}

export async function wijzigKind(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const kindId = String(formData.get("kind_id") || "");
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) return;

  const geboortedatum =
    String(formData.get("geboortedatum") || "").trim() || null;
  const allergieen = String(formData.get("allergieen") || "").trim() || null;
  const diagnoses = String(formData.get("diagnoses") || "").trim() || null;
  const noodcontactNaam =
    String(formData.get("noodcontact_naam") || "").trim() || null;
  const noodcontactTelefoon =
    String(formData.get("noodcontact_telefoon") || "").trim() || null;
  const toestemmingFotos = formData.get("toestemming_fotos") === "on";
  const toestemmingSocialMedia =
    formData.get("toestemming_social_media") === "on";

  const admin = createAdminClient();
  await admin
    .from("kinderen")
    .update({
      naam,
      geboortedatum,
      allergieen,
      diagnoses,
      noodcontact_naam: noodcontactNaam,
      noodcontact_telefoon: noodcontactTelefoon,
      toestemming_fotos: toestemmingFotos,
      toestemming_social_media: toestemmingSocialMedia,
      ...fichevelden(formData),
      updated_at: new Date().toISOString(),
    })
    .eq("id", kindId)
    .eq("profile_id", gezinId);

  revalidatePath("/portaal/gezin");
}

export async function verwijderKind(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const kindId = String(formData.get("kind_id") || "");

  const admin = createAdminClient();
  await admin
    .from("kinderen")
    .delete()
    .eq("id", kindId)
    .eq("profile_id", gezinId);

  revalidatePath("/portaal/gezin");
}
