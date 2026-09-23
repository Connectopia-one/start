"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Het bestand zelf gaat zo NIET door de server action heen — dat omzeilt de
 * limiet van ~4,5MB die Vercel op reguliere server-verzoeken zet. Een vakfiche
 * is soms een lijvige pdf, dus dat is hier geen theoretisch probleem.
 */
export async function maakDoelUploadUrl(bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const veilig = bestandsnaam.replace(/[^a-zA-Z0-9._-]/g, "-");
  const path = `doelen/${Date.now()}-${veilig}`;

  const { data, error } = await admin.storage.from("materiaal").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function registreerDoelbestand(input: {
  niveau: string;
  vak?: string | null;
  titel: string;
  type: "link" | "pdf";
  link?: string | null;
  bestandspad?: string | null;
  geldigSinds?: string | null;
  omschrijving?: string | null;
}) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("doelbestanden").insert({
    niveau: input.niveau,
    vak: input.vak?.trim() || null,
    titel: input.titel.trim(),
    type: input.type,
    link: input.link?.trim() || null,
    bestandspad: input.bestandspad || null,
    geldig_sinds: input.geldigSinds?.trim() || null,
    omschrijving: input.omschrijving?.trim() || null,
  });

  if (error) throw new Error(error.message);
  revalidatePath("/beheer/doelen");
  revalidatePath("/onderwijsdoelen");
}

export async function verwijderDoelbestand(formData: FormData) {
  await requireBeheerder();

  const id = String(formData.get("id") || "");
  const bestandspad = String(formData.get("bestandspad") || "");

  const admin = createAdminClient();
  if (bestandspad) {
    await admin.storage.from("materiaal").remove([bestandspad]);
  }
  await admin.from("doelbestanden").delete().eq("id", id);

  revalidatePath("/beheer/doelen");
  revalidatePath("/onderwijsdoelen");
}
