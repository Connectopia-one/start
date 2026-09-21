"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Het beheer van het prikbord op de website. De briefjes zelf staan in
  dezelfde databank; het schema staat in  website/supabase/prikbord.sql
*/

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

export async function zetZichtbaar(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const zichtbaar = String(formData.get("zichtbaar") || "") === "ja";

  const { error } = await db
    .from("prikbord_briefjes")
    .update({ zichtbaar, gezien: true })
    .eq("id", id);

  if (error) {
    redirect("/beheer/prikbord?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/prikbord");
  redirect(
    "/beheer/prikbord?succes=" +
      encodeURIComponent(
        zichtbaar
          ? "Briefje hangt weer op het bord."
          : "Briefje is van het bord gehaald.",
      ),
  );
}

export async function verwijderBriefje(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const { error } = await db.from("prikbord_briefjes").delete().eq("id", id);

  if (error) {
    redirect("/beheer/prikbord?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/prikbord");
  redirect(
    "/beheer/prikbord?succes=" + encodeURIComponent("Briefje verwijderd."),
  );
}

export async function markeerGezien(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const vraag = db.from("prikbord_briefjes").update({ gezien: true });
  const { error } = id
    ? await vraag.eq("id", id)
    : await vraag.eq("gezien", false);

  if (error) {
    redirect("/beheer/prikbord?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/prikbord");
  revalidatePath("/beheer");
  redirect("/beheer/prikbord");
}

export async function handelMeldingAf(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const { error } = await db
    .from("prikbord_meldingen")
    .update({ afgehandeld: true })
    .eq("id", id);

  if (error) {
    redirect("/beheer/prikbord?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/prikbord");
  redirect(
    "/beheer/prikbord?succes=" + encodeURIComponent("Melding afgevinkt."),
  );
}
