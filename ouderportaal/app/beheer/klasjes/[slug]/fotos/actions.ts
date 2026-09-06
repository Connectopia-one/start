"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Zo gaat het beeldbestand niet door de server action heen — dat omzeilt de
 * limiet van ~4,5MB die Vercel op reguliere server-verzoeken zet.
 */
export async function maakFotoUploadUrl(klasjeId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${klasjeId}/${Date.now()}-${Math.random().toString(36).slice(2, 8)}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("fotos").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function registreerFoto(input: {
  klasjeId: string;
  slug: string;
  bestandspad: string;
  bijschrift?: string | null;
}) {
  const session = await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("fotos").insert({
    klasje_id: input.klasjeId,
    bestandspad: input.bestandspad,
    bijschrift: input.bijschrift ?? null,
    created_by: session.userId,
  });

  if (error) throw new Error(error.message);
  revalidatePath(`/beheer/klasjes/${input.slug}/fotos`);
}

export async function verwijderFoto(formData: FormData) {
  await requireBeheerder();

  const id = String(formData.get("id") || "");
  const slug = String(formData.get("slug") || "");
  const bestandspad = String(formData.get("bestandspad") || "");

  const admin = createAdminClient();
  if (bestandspad) {
    await admin.storage.from("fotos").remove([bestandspad]);
  }
  await admin.from("fotos").delete().eq("id", id);

  revalidatePath(`/beheer/klasjes/${slug}/fotos`);
}
