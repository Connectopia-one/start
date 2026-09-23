"use server";

import { revalidatePath } from "next/cache";
import { requireBegeleider } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Alle acties hieronder controleren twee dingen: is de gebruiker beheerder of
  begeleider, en hoort dit kind bij een gezin met een plusklascode. Die tweede
  check staat ook in de databank (zie supabase/plusklasfiche.sql), maar we doen
  hem hier nog eens, omdat deze acties met de service-sleutel werken en die
  alle regels van de databank overslaat.
*/
async function bevestigPlusklasKind(kindId: string) {
  const session = await requireBegeleider();
  const admin = createAdminClient();

  const { data } = await admin
    .from("kinderen")
    .select("id, profiles(is_plusklas)")
    .eq("id", kindId)
    .single();

  const gezin = (data as { profiles?: { is_plusklas?: boolean } } | null)
    ?.profiles;
  if (!data || !gezin?.is_plusklas) {
    throw new Error("Dit kind hoort niet bij een gezin van de plusklas.");
  }
  return { session, admin };
}

export async function voegNotitieToe(formData: FormData) {
  const kindId = String(formData.get("kindId") || "");
  const tekst = String(formData.get("tekst") || "").trim();
  const soort = String(formData.get("soort") || "opmerking");
  const datum = String(formData.get("datum") || "").trim();
  if (!kindId || !tekst) return;

  const { session, admin } = await bevestigPlusklasKind(kindId);

  const { error } = await admin.from("kind_notities").insert({
    kind_id: kindId,
    tekst,
    soort,
    datum: datum || null,
    auteur_id: session.userId,
    auteur_naam: session.profile?.full_name ?? null,
  });
  if (error) throw new Error(error.message);

  revalidatePath(`/begeleiding/${kindId}`);
}

export async function verwijderNotitie(formData: FormData) {
  const kindId = String(formData.get("kindId") || "");
  const id = String(formData.get("id") || "");
  if (!kindId || !id) return;

  const { admin } = await bevestigPlusklasKind(kindId);
  await admin.from("kind_notities").delete().eq("id", id).eq("kind_id", kindId);
  revalidatePath(`/begeleiding/${kindId}`);
}

/**
 * Een tijdelijke upload-link, zodat het bestand niet door de server action
 * heen moet. Zo loop je niet tegen de limiet van ongeveer 4,5MB aan die
 * Vercel op een gewoon verzoek zet — een ingescand werkje is zo groot.
 */
export async function maakWerkUploadUrl(kindId: string, bestandsnaam: string) {
  const { admin } = await bevestigPlusklasKind(kindId);
  const veilig = bestandsnaam.replace(/[^a-zA-Z0-9._-]/g, "-");
  const path = `${kindId}/${Date.now()}-${veilig}`;

  const { data, error } = await admin.storage
    .from("kinddossier")
    .createSignedUploadUrl(path);
  if (error || !data)
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  return { path: data.path, token: data.token };
}

export async function registreerWerk(input: {
  kindId: string;
  titel: string;
  bestandspad: string;
  omschrijving?: string | null;
  datum?: string | null;
}) {
  const { session, admin } = await bevestigPlusklasKind(input.kindId);

  const { error } = await admin.from("kind_documenten").insert({
    kind_id: input.kindId,
    titel: input.titel.trim(),
    bestandspad: input.bestandspad,
    omschrijving: input.omschrijving?.trim() || null,
    datum: input.datum?.trim() || null,
    auteur_id: session.userId,
    auteur_naam: session.profile?.full_name ?? null,
  });
  if (error) throw new Error(error.message);

  revalidatePath(`/begeleiding/${input.kindId}`);
}

export async function verwijderWerk(formData: FormData) {
  const kindId = String(formData.get("kindId") || "");
  const id = String(formData.get("id") || "");
  const bestandspad = String(formData.get("bestandspad") || "");
  if (!kindId || !id) return;

  const { admin } = await bevestigPlusklasKind(kindId);
  if (bestandspad)
    await admin.storage.from("kinddossier").remove([bestandspad]);
  await admin
    .from("kind_documenten")
    .delete()
    .eq("id", id)
    .eq("kind_id", kindId);

  revalidatePath(`/begeleiding/${kindId}`);
}
