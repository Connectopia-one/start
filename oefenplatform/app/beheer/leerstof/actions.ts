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

/** Zet één geüpload bestand als leerstof bij een hoofdstuk. */
export async function registreerBulkLeerstof(input: {
  hoofdstukId: string;
  titel: string;
  bestandspad: string;
}) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("leerstof").insert({
    hoofdstuk_id: input.hoofdstukId,
    titel: input.titel,
    bestandspad: input.bestandspad,
  });

  if (error) throw new Error(error.message);
  revalidatePath("/beheer/leerstof");
}
