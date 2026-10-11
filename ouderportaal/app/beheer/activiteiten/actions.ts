"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Activiteiten aanmaken, archiveren en verwijderen, en kinderen eraan koppelen.
  Het schema staat in supabase/activiteiten.sql.
*/

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

function terug(pad: string, bericht: string, fout = false): never {
  revalidatePath(pad);
  redirect(`${pad}?${fout ? "fout" : "succes"}=${encodeURIComponent(bericht)}`);
}

export async function maakActiviteit(formData: FormData) {
  const db = await admin();
  const naam = String(formData.get("naam") || "").trim();
  const soort = String(formData.get("soort") || "kamp").trim() || "kamp";
  const datum = String(formData.get("datum") || "").trim();
  const plaats = String(formData.get("plaats") || "").trim();

  if (!naam) terug("/beheer/activiteiten", "Geef de activiteit een naam.", true);

  const { error } = await db.from("activiteiten").insert({
    naam,
    soort,
    datum: datum || null,
    plaats: plaats || null,
  });

  if (error) terug("/beheer/activiteiten", error.message, true);
  terug("/beheer/activiteiten", `${naam} staat erbij.`);
}

export async function zetArchief(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const archief = String(formData.get("archief") || "") === "ja";

  const { error } = await db
    .from("activiteiten")
    .update({ archief })
    .eq("id", id);

  if (error) terug("/beheer/activiteiten", error.message, true);
  terug(
    "/beheer/activiteiten",
    archief ? "Naar het archief gezet." : "Terug uit het archief.",
  );
}

export async function verwijderActiviteit(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  /* De deelnames gaan mee weg: de koppeling staat met on delete cascade in
     supabase/activiteiten.sql. De kinderen zelf blijven uiteraard staan. */
  const { error } = await db.from("activiteiten").delete().eq("id", id);
  if (error) terug("/beheer/activiteiten", error.message, true);
  terug("/beheer/activiteiten", "Activiteit verwijderd.");
}

export async function voegKindToe(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const pad = `/beheer/activiteiten/${activiteitId}`;

  if (!kindId) terug(pad, "Kies eerst een kind.", true);

  /* Twee keer hetzelfde kind toevoegen mag gewoon niets doen; de sleutel van
     de tabel is (activiteit, kind). */
  const { error } = await db
    .from("deelnames")
    .upsert(
      { activiteit_id: activiteitId, kind_id: kindId },
      { onConflict: "activiteit_id,kind_id" },
    );

  if (error) terug(pad, error.message, true);
  terug(pad, "Kind toegevoegd.");
}

export async function haalKindWeg(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const pad = `/beheer/activiteiten/${activiteitId}`;

  const { error } = await db
    .from("deelnames")
    .delete()
    .eq("activiteit_id", activiteitId)
    .eq("kind_id", kindId);

  if (error) terug(pad, error.message, true);
  terug(pad, "Kind van de lijst gehaald.");
}

export async function bewaarNotitie(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const notitie = String(formData.get("notitie") || "").trim();
  const pad = `/beheer/activiteiten/${activiteitId}`;

  const { error } = await db
    .from("deelnames")
    .update({ notitie: notitie || null })
    .eq("activiteit_id", activiteitId)
    .eq("kind_id", kindId);

  if (error) terug(pad, error.message, true);
  terug(pad, "Notitie bewaard.");
}

/*
  De vinkjes op de gezinspagina: bij welke activiteiten hoort dit kind?

  Het formulier stuurt alle activiteiten mee als `alle`, en enkel de
  aangevinkte als `activiteit`. Zonder die eerste lijst zouden we niet weten
  welke vinkjes net uitgezet zijn, want een leeg vakje stuurt niets mee.
*/
export async function zetDeelnames(formData: FormData) {
  const db = await admin();
  const kindId = String(formData.get("kind_id") || "");
  const profileId = String(formData.get("profile_id") || "");
  const pad = `/beheer/gezinnen/${profileId}`;

  const alle = formData.getAll("alle").map(String);
  const gekozen = new Set(formData.getAll("activiteit").map(String));
  const weg = alle.filter((id) => !gekozen.has(id));

  if (weg.length) {
    const { error } = await db
      .from("deelnames")
      .delete()
      .eq("kind_id", kindId)
      .in("activiteit_id", weg);
    if (error) terug(pad, error.message, true);
  }

  if (gekozen.size) {
    const { error } = await db.from("deelnames").upsert(
      [...gekozen].map((activiteit_id) => ({ activiteit_id, kind_id: kindId })),
      { onConflict: "activiteit_id,kind_id" },
    );
    if (error) terug(pad, error.message, true);
  }

  terug(pad, "Aangepast.");
}
