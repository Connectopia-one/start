"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { vindNiveau } from "@/lib/niveaus";

/*
  Net als bij Handig materiaal gaat het bestand rechtstreeks naar de opslag,
  niet door de server heen (Vercel laat maar ~4,5 MB per verzoek toe, en een
  examen met foto's is al snel groter).
*/
export async function maakExtraBundelUploadUrl(bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const veilig = bestandsnaam.replace(/[^a-zA-Z0-9._-]/g, "-");
  const path = `${Date.now()}-${veilig}`;
  const { data, error } = await admin.storage.from("extrabundels").createSignedUploadUrl(path);
  if (error || !data) throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  return { path: data.path, token: data.token };
}

export async function registreerExtraBundel(input: {
  vakId: string;
  niveau: string;
  soort: string;
  titel: string;
  omschrijving?: string | null;
  bestandspad: string;
  verbetersleutel: boolean;
}) {
  await requireBeheerder();
  if (!vindNiveau(input.niveau)) throw new Error("Kies een categorie.");
  if (!["examen", "lesbundel", "andere"].includes(input.soort)) throw new Error("Kies een soort.");
  if (!input.titel.trim()) throw new Error("Vul een titel in.");

  const admin = createAdminClient();
  const { error } = await admin.from("extra_bundels").insert({
    vak_id: input.vakId,
    niveau: input.niveau,
    soort: input.soort,
    titel: input.titel.trim(),
    omschrijving: input.omschrijving?.trim() || null,
    bestandspad: input.bestandspad,
    verbetersleutel: input.verbetersleutel,
  });
  if (error) {
    await admin.storage.from("extrabundels").remove([input.bestandspad]);
    throw new Error(error.message);
  }
  revalidatePath("/beheer/extra-bundels");
  revalidatePath("/niveaus", "layout");
}

export async function verwijderExtraBundel(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  if (!id) return;
  const admin = createAdminClient();
  const { data } = await admin.from("extra_bundels").select("bestandspad").eq("id", id).single();
  if (data?.bestandspad) await admin.storage.from("extrabundels").remove([data.bestandspad]);
  await admin.from("extra_bundels").delete().eq("id", id);
  revalidatePath("/beheer/extra-bundels");
  revalidatePath("/niveaus", "layout");
}
