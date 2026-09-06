"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function voegMateriaalToe(formData: FormData) {
  const session = await requireBeheerder();

  const klasjeId = String(formData.get("klasje_id") || "");
  const slug = String(formData.get("slug") || "");
  const type = String(formData.get("type") || "");
  const titel = String(formData.get("titel") || "").trim();
  const terug = `/beheer/klasjes/${slug}/materiaal`;

  if (!titel || !["pdf", "link", "aankondiging"].includes(type)) {
    redirect(`${terug}?fout=` + encodeURIComponent("Vul een titel in en kies een type."));
  }

  const admin = createAdminClient();
  let inhoud: string | null = null;
  let bestandspad: string | null = null;

  if (type === "pdf") {
    const bestand = formData.get("bestand");
    if (!(bestand instanceof File) || bestand.size === 0) {
      redirect(`${terug}?fout=` + encodeURIComponent("Kies een PDF-bestand om te uploaden."));
    }
    const file = bestand as File;
    bestandspad = `${klasjeId}/${Date.now()}-${file.name}`;
    const { error: uploadError } = await admin.storage
      .from("materialen")
      .upload(bestandspad, file, { contentType: file.type || "application/pdf" });
    if (uploadError) {
      redirect(`${terug}?fout=` + encodeURIComponent("Uploaden mislukt: " + uploadError.message));
    }
  } else if (type === "link") {
    inhoud = String(formData.get("link") || "").trim();
    if (!inhoud) redirect(`${terug}?fout=` + encodeURIComponent("Vul een link in."));
  } else {
    inhoud = String(formData.get("tekst") || "").trim();
    if (!inhoud) redirect(`${terug}?fout=` + encodeURIComponent("Vul een tekst in."));
  }

  const { error } = await admin.from("materialen").insert({
    klasje_id: klasjeId,
    type,
    titel,
    inhoud,
    bestandspad,
    created_by: session.userId,
  });

  if (error) {
    redirect(`${terug}?fout=` + encodeURIComponent(error.message));
  }

  revalidatePath(terug);
  redirect(`${terug}?succes=` + encodeURIComponent("Toegevoegd."));
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
