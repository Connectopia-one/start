"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Het bestand gaat zo NIET door de server action heen, wat de limiet van
 * ~4,5MB omzeilt die Vercel op gewone server-verzoeken zet.
 */
export async function maakBulkLeerstofUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("leerstof").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

/**
 * Zet één geüpload bestand als leerstof bij een hoofdstuk.
 *
 * Staat "vervang" aan, dan gaan de bundels die er al bij dat hoofdstuk stonden
 * daarna weg — handig als je een verouderde bundel door een nieuwe versie
 * vervangt. We zetten bewust eerst de nieuwe erin en ruimen pas daarna op:
 * loopt er iets mis, dan staan er even twee bundels, nooit geen enkele.
 */
export async function registreerBulkLeerstof(input: {
  hoofdstukId: string;
  titel: string;
  bestandspad: string;
  vervang?: boolean;
}) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { data: oude } = input.vervang
    ? await admin.from("leerstof").select("id, bestandspad").eq("hoofdstuk_id", input.hoofdstukId)
    : { data: null };

  const { error } = await admin.from("leerstof").insert({
    hoofdstuk_id: input.hoofdstukId,
    titel: input.titel,
    bestandspad: input.bestandspad,
  });

  if (error) throw new Error(error.message);

  const teWissen = (oude ?? []).filter((r) => r.bestandspad !== input.bestandspad);
  if (teWissen.length > 0) {
    await admin.storage.from("leerstof").remove(teWissen.map((r) => r.bestandspad as string));
    await admin.from("leerstof").delete().in("id", teWissen.map((r) => r.id as string));
  }

  revalidatePath("/beheer/leerstof");
  revalidatePath("/");
}

/** Eén leerbundel weghalen bij een hoofdstuk, met bestand en al. */
export async function verwijderLeerstof(id: string) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { data: rij } = await admin.from("leerstof").select("bestandspad").eq("id", id).maybeSingle();
  if (rij?.bestandspad) {
    await admin.storage.from("leerstof").remove([rij.bestandspad as string]);
  }
  const { error } = await admin.from("leerstof").delete().eq("id", id);
  if (error) throw new Error(error.message);

  revalidatePath("/beheer/leerstof");
  revalidatePath("/");
}
