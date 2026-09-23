"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Het bestand zelf gaat zo NIET door de server action heen — dat omzeilt de
 * limiet van ~4,5MB die Vercel op reguliere server-verzoeken zet.
 */
export async function maakMateriaalUploadUrl(bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const veilig = bestandsnaam.replace(/[^a-zA-Z0-9._-]/g, "-");
  const path = `${Date.now()}-${veilig}`;

  const { data, error } = await admin.storage.from("materiaal").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function registreerMateriaal(input: {
  groep: string;
  type: "link" | "pdf";
  titel: string;
  link?: string | null;
  bestandspad?: string | null;
  omschrijving?: string | null;
}) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("materiaal").insert({
    groep: input.groep.trim() || "Allerlei",
    type: input.type,
    titel: input.titel.trim(),
    link: input.link?.trim() || null,
    bestandspad: input.bestandspad || null,
    omschrijving: input.omschrijving?.trim() || null,
  });

  if (error) throw new Error(error.message);
  revalidatePath("/beheer/materiaal");
  revalidatePath("/materiaal");
}

export async function verwijderMateriaal(formData: FormData) {
  await requireBeheerder();

  const id = String(formData.get("id") || "");
  const bestandspad = String(formData.get("bestandspad") || "");

  const admin = createAdminClient();
  if (bestandspad) {
    await admin.storage.from("materiaal").remove([bestandspad]);
  }
  await admin.from("materiaal").delete().eq("id", id);

  revalidatePath("/beheer/materiaal");
  revalidatePath("/materiaal");
}
