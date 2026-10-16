"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Het beheer van de organisaties die iemand aanbracht voor de gids
  "Waar kan je terecht" op de website. Het schema staat in
  website/supabase/gids.sql

  Een aanmelding staat op "niet zichtbaar". Pas als jij ze hier in de gids
  zet, staat ze op de website, bij de vaste lijst uit website/content/gids.ts.
*/

const PAD = "/beheer/gids";

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

function terug(soort: "fout" | "succes", tekst: string): never {
  redirect(`${PAD}?${soort}=${encodeURIComponent(tekst)}`);
}

/* Naam, omschrijving, regio en website aanpassen voor je ze goedkeurt. */
export async function bewaarAanmelding(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const naam = String(formData.get("naam") || "").trim();
  const omschrijving = String(formData.get("omschrijving") || "").trim();
  const regio = String(formData.get("regio") || "").trim();
  let link = String(formData.get("link") || "").trim();
  if (link && !/^https?:\/\//i.test(link)) link = `https://${link}`;
  link = link.replace(/^http:\/\//i, "https://");

  if (naam.length < 2 || naam.length > 120) terug("fout", "Vul een naam in.");
  if (omschrijving.length < 10 || omschrijving.length > 400) {
    terug("fout", "De omschrijving moet tussen 10 en 400 tekens lang zijn.");
  }

  const { error } = await db
    .from("gids_aanmeldingen")
    .update({
      naam,
      omschrijving,
      regio: regio ? regio.slice(0, 80) : null,
      link: link ? link.slice(0, 400) : null,
      gezien: true,
    })
    .eq("id", id);

  if (error) terug("fout", error.message);
  revalidatePath(PAD);
  terug("succes", "Aanpassing bewaard.");
}

export async function zetZichtbaar(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const zichtbaar = String(formData.get("zichtbaar") || "") === "ja";

  const { error } = await db
    .from("gids_aanmeldingen")
    .update({ zichtbaar, gezien: true })
    .eq("id", id);

  if (error) terug("fout", error.message);
  revalidatePath(PAD);
  revalidatePath("/beheer");
  terug(
    "succes",
    zichtbaar
      ? "De organisatie staat nu in de gids op de website."
      : "De organisatie staat niet meer in de gids.",
  );
}

export async function verwijderAanmelding(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const { error } = await db.from("gids_aanmeldingen").delete().eq("id", id);

  if (error) terug("fout", error.message);
  revalidatePath(PAD);
  revalidatePath("/beheer");
  terug("succes", "Aanmelding verwijderd.");
}

export async function markeerGezien(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const vraag = db.from("gids_aanmeldingen").update({ gezien: true });
  const { error } = id
    ? await vraag.eq("id", id)
    : await vraag.eq("gezien", false);

  if (error) terug("fout", error.message);
  revalidatePath(PAD);
  revalidatePath("/beheer");
  redirect(PAD);
}
