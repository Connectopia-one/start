"use server";

import { revalidatePath } from "next/cache";
import { requireIngelogd } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function wijzigContactgegevens(formData: FormData) {
  const session = await requireIngelogd();
  const telefoon = String(formData.get("telefoon") || "").trim() || null;
  const adres = String(formData.get("adres") || "").trim() || null;

  const admin = createAdminClient();
  await admin.from("profiles").update({ telefoon, adres }).eq("id", session.userId);

  revalidatePath("/portaal/gezin");
}

export async function voegKindToe(formData: FormData) {
  const session = await requireIngelogd();
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) return;

  const geboortedatum = String(formData.get("geboortedatum") || "").trim() || null;
  const allergieen = String(formData.get("allergieen") || "").trim() || null;
  const diagnoses = String(formData.get("diagnoses") || "").trim() || null;
  const noodcontactNaam = String(formData.get("noodcontact_naam") || "").trim() || null;
  const noodcontactTelefoon = String(formData.get("noodcontact_telefoon") || "").trim() || null;
  const toestemmingFotos = formData.get("toestemming_fotos") === "on";
  const toestemmingSocialMedia = formData.get("toestemming_social_media") === "on";

  const admin = createAdminClient();
  await admin.from("kinderen").insert({
    profile_id: session.userId,
    naam,
    geboortedatum,
    allergieen,
    diagnoses,
    noodcontact_naam: noodcontactNaam,
    noodcontact_telefoon: noodcontactTelefoon,
    toestemming_fotos: toestemmingFotos,
    toestemming_social_media: toestemmingSocialMedia,
  });

  revalidatePath("/portaal/gezin");
}

export async function wijzigKind(formData: FormData) {
  const session = await requireIngelogd();
  const kindId = String(formData.get("kind_id") || "");
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) return;

  const geboortedatum = String(formData.get("geboortedatum") || "").trim() || null;
  const allergieen = String(formData.get("allergieen") || "").trim() || null;
  const diagnoses = String(formData.get("diagnoses") || "").trim() || null;
  const noodcontactNaam = String(formData.get("noodcontact_naam") || "").trim() || null;
  const noodcontactTelefoon = String(formData.get("noodcontact_telefoon") || "").trim() || null;
  const toestemmingFotos = formData.get("toestemming_fotos") === "on";
  const toestemmingSocialMedia = formData.get("toestemming_social_media") === "on";

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
      updated_at: new Date().toISOString(),
    })
    .eq("id", kindId)
    .eq("profile_id", session.userId);

  revalidatePath("/portaal/gezin");
}

export async function verwijderKind(formData: FormData) {
  const session = await requireIngelogd();
  const kindId = String(formData.get("kind_id") || "");

  const admin = createAdminClient();
  await admin.from("kinderen").delete().eq("id", kindId).eq("profile_id", session.userId);

  revalidatePath("/portaal/gezin");
}
