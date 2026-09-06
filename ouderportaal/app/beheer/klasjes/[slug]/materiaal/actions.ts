"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Het bestand zelf gaat zo NIET door de server action heen — dat omzeilt de
 * limiet van ~4,5MB die Vercel op reguliere server-verzoeken zet.
 */
export async function maakMateriaalUploadUrl(klasjeId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${klasjeId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("materialen").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function registreerMateriaal(input: {
  klasjeId: string;
  slug: string;
  type: "pdf" | "link" | "aankondiging";
  titel: string;
  inhoud?: string | null;
  bestandspad?: string | null;
}) {
  const session = await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("materialen").insert({
    klasje_id: input.klasjeId,
    type: input.type,
    titel: input.titel,
    inhoud: input.inhoud ?? null,
    bestandspad: input.bestandspad ?? null,
    created_by: session.userId,
  });

  if (error) throw new Error(error.message);
  revalidatePath(`/beheer/klasjes/${input.slug}/materiaal`);
}

export async function verwijderMateriaal(formData: FormData) {
  await requireBeheerder();

  const id = String(formData.get("id") || "");
  const slug = String(formData.get("slug") || "");
  const bestandspad = String(formData.get("bestandspad") || "");

  const admin = createAdminClient();
  if (bestandspad) {
    await admin.storage.from("materialen").remove([bestandspad]);
  }
  await admin.from("materialen").delete().eq("id", id);

  revalidatePath(`/beheer/klasjes/${slug}/materiaal`);
}
