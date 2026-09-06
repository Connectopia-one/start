"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { slugify } from "@/lib/slug";

export async function maakVak(formData: FormData) {
  await requireBeheerder();
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) redirect("/beheer?fout=" + encodeURIComponent("Geef een naam op voor het vak."));

  const admin = createAdminClient();
  const { count } = await admin.from("vakken").select("id", { count: "exact", head: true });
  const { error } = await admin.from("vakken").insert({ naam, slug: slugify(naam), volgorde: count ?? 0 });
  if (error) redirect("/beheer?fout=" + encodeURIComponent("Kon vak niet aanmaken (bestaat de naam al?)."));

  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function verwijderVak(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();
  await admin.from("vakken").delete().eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function maakHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const titel = String(formData.get("titel") || "").trim();
  const gratis = formData.get("gratis") === "on";
  if (!vakId || !titel) redirect("/beheer/vakken?fout=" + encodeURIComponent("Geef een titel op voor het hoofdstuk."));

  const admin = createAdminClient();
  const { count } = await admin
    .from("hoofdstukken")
    .select("id", { count: "exact", head: true })
    .eq("vak_id", vakId);

  await admin.from("hoofdstukken").insert({
    vak_id: vakId,
    titel,
    volgnummer: (count ?? 0) + 1,
    gratis,
  });

  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function wisselGratis(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const gratis = formData.get("gratis") === "true";
  const admin = createAdminClient();
  await admin.from("hoofdstukken").update({ gratis: !gratis }).eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function verwijderHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();
  await admin.from("hoofdstukken").delete().eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}
