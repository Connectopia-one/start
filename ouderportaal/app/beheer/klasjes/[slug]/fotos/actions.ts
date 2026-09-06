"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function voegFotosToe(formData: FormData) {
  const session = await requireBeheerder();

  const klasjeId = String(formData.get("klasje_id") || "");
  const slug = String(formData.get("slug") || "");
  const bijschrift = String(formData.get("bijschrift") || "").trim() || null;
  const terug = `/beheer/klasjes/${slug}/fotos`;

  const bestanden = formData.getAll("bestanden").filter((b): b is File => b instanceof File && b.size > 0);
  if (bestanden.length === 0) {
    redirect(`${terug}?fout=` + encodeURIComponent("Kies minstens één foto."));
  }

  const admin = createAdminClient();

  for (const file of bestanden) {
    const bestandspad = `${klasjeId}/${Date.now()}-${Math.random().toString(36).slice(2, 8)}-${file.name}`;
    const { error: uploadError } = await admin.storage
      .from("fotos")
      .upload(bestandspad, file, { contentType: file.type || "image/jpeg" });
    if (uploadError) {
      redirect(`${terug}?fout=` + encodeURIComponent("Uploaden mislukt: " + uploadError.message));
    }
    await admin.from("fotos").insert({
      klasje_id: klasjeId,
      bestandspad,
      bijschrift,
      created_by: session.userId,
    });
  }

  revalidatePath(terug);
  redirect(`${terug}?succes=` + encodeURIComponent(`${bestanden.length} foto('s) toegevoegd.`));
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
