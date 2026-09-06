"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

type NieuweVraag = {
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties?: string[] | null;
  antwoord: number | string | boolean;
  uitleg?: string | null;
};

function terugPad(vakSlug: string, volgnummer: string) {
  return `/beheer/vakken/${vakSlug}/${volgnummer}`;
}

export async function maakVraag(formData: FormData) {
  await requireBeheerder();
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const type = String(formData.get("type") || "meerkeuze") as NieuweVraag["type"];
  const vraag = String(formData.get("vraag") || "").trim();
  const optiesRaw = String(formData.get("opties") || "").trim();
  const antwoordRaw = String(formData.get("antwoord") || "").trim();
  const uitleg = String(formData.get("uitleg") || "").trim() || null;

  if (!vraag || !antwoordRaw) {
    redirect(terugPad(vakSlug, volgnummer) + "?fout=" + encodeURIComponent("Vul minstens de vraag en het antwoord in."));
  }

  const opties = type === "meerkeuze" ? optiesRaw.split("\n").map((r) => r.trim()).filter(Boolean) : null;
  let antwoord: number | string | boolean;
  if (type === "meerkeuze") antwoord = Number(antwoordRaw);
  else if (type === "waarofniet") antwoord = antwoordRaw.toLowerCase() === "waar" || antwoordRaw.toLowerCase() === "true";
  else antwoord = antwoordRaw;

  const admin = createAdminClient();
  const { count } = await admin
    .from("vragen")
    .select("id", { count: "exact", head: true })
    .eq("hoofdstuk_id", hoofdstukId);

  const { error } = await admin.from("vragen").insert({
    hoofdstuk_id: hoofdstukId,
    volgnummer: (count ?? 0) + 1,
    type,
    vraag,
    opties,
    antwoord,
    uitleg,
  });

  if (error) {
    redirect(terugPad(vakSlug, volgnummer) + "?fout=" + encodeURIComponent("Vraag toevoegen is niet gelukt: " + error.message));
  }

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

export async function bulkImportVragen(formData: FormData) {
  await requireBeheerder();
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const json = String(formData.get("json") || "").trim();

  let vragen: NieuweVraag[];
  try {
    vragen = JSON.parse(json);
    if (!Array.isArray(vragen)) throw new Error("Verwacht een JSON-array van vragen.");
  } catch (e) {
    redirect(
      terugPad(vakSlug, volgnummer) +
        "?fout=" +
        encodeURIComponent("Ongeldige JSON: " + (e instanceof Error ? e.message : "onbekende fout"))
    );
  }

  const admin = createAdminClient();
  const { count } = await admin
    .from("vragen")
    .select("id", { count: "exact", head: true })
    .eq("hoofdstuk_id", hoofdstukId);

  const rijen = vragen!.map((v, i) => ({
    hoofdstuk_id: hoofdstukId,
    volgnummer: (count ?? 0) + i + 1,
    type: v.type,
    vraag: v.vraag,
    opties: v.opties ?? null,
    antwoord: v.antwoord,
    uitleg: v.uitleg ?? null,
  }));

  const { error } = await admin.from("vragen").insert(rijen);
  if (error) {
    redirect(terugPad(vakSlug, volgnummer) + "?fout=" + encodeURIComponent("Bulk-import mislukt: " + error.message));
  }

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

export async function verwijderVraag(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  await admin.from("vragen").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}
