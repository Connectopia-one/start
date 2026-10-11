"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Wat er al betaald is: cash in de hand of een overschrijving die vooraf komt.
  Het schema staat in supabase/activiteiten.sql, tabel `ontvangsten`.
*/

const PAD = "/beheer/facturatie";

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

function terug(bericht: string, fout = false, maand = ""): never {
  revalidatePath(PAD);
  const vraag = new URLSearchParams();
  if (maand) vraag.set("maand", maand);
  vraag.set(fout ? "fout" : "succes", bericht);
  redirect(`${PAD}?${vraag.toString()}`);
}

/* Een bedrag zoals een mens het typt: 20, 20.5 of 20,50. */
function leesBedrag(waarde: FormDataEntryValue | null) {
  const tekst = String(waarde ?? "")
    .trim()
    .replace(/\s|€/g, "")
    .replace(",", ".");
  if (!tekst) return null;
  const getal = Number(tekst);
  if (!Number.isFinite(getal) || getal <= 0) return null;
  return Math.round(getal * 100) / 100;
}

export async function noteerOntvangst(formData: FormData) {
  const db = await admin();
  const maand = String(formData.get("maand") || "");
  const profileId = String(formData.get("profile_id") || "");
  const datum = String(formData.get("datum") || "").trim();
  const wijze = String(formData.get("wijze") || "cash").trim() || "cash";
  const opmerking = String(formData.get("opmerking") || "").trim();
  const bedrag = leesBedrag(formData.get("bedrag"));

  if (!profileId) terug("Kies eerst een gezin.", true, maand);
  if (bedrag === null) terug("Vul een bedrag in, bijvoorbeeld 50.", true, maand);

  const { error } = await db.from("ontvangsten").insert({
    profile_id: profileId,
    datum: datum || new Date().toISOString().slice(0, 10),
    bedrag,
    wijze,
    opmerking: opmerking || null,
  });

  if (error) terug(error.message, true, maand);
  terug("Genoteerd.", false, maand);
}

export async function wisOntvangst(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const maand = String(formData.get("maand") || "");

  const { error } = await db.from("ontvangsten").delete().eq("id", id);
  if (error) terug(error.message, true, maand);
  terug("Weggehaald.", false, maand);
}

/*
  De storting. Je kiest welke bedragen in dat ene envelopje zaten en op welke
  dag je het naar de rekening bracht; daarna staan ze niet meer bij "nog in de
  kas". Er is bewust geen knop die alles in één keer afvinkt: dan staat er een
  datum op geld dat nog in je tas zit.
*/
export async function markeerGestort(formData: FormData) {
  const db = await admin();
  const maand = String(formData.get("maand") || "");
  const ids = formData.getAll("ontvangst").map(String);
  const datum = String(formData.get("gestort_op") || "").trim();

  if (ids.length === 0) terug("Vink eerst aan wat je gestort hebt.", true, maand);

  const { error } = await db
    .from("ontvangsten")
    .update({ gestort_op: datum || new Date().toISOString().slice(0, 10) })
    .in("id", ids);

  if (error) terug(error.message, true, maand);
  terug(
    `${ids.length} ${ids.length === 1 ? "bedrag" : "bedragen"} op gestort gezet.`,
    false,
    maand,
  );
}

/* Verkeerd aangevinkt: terug naar de kas. */
export async function haalStortingTerug(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const maand = String(formData.get("maand") || "");

  const { error } = await db
    .from("ontvangsten")
    .update({ gestort_op: null })
    .eq("id", id);

  if (error) terug(error.message, true, maand);
  terug("Staat weer in de kas.", false, maand);
}
