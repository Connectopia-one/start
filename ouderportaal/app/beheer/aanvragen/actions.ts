"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { isStap } from "@/lib/aanvraagstappen";
import { zetStapVoorGezin } from "@/lib/aanvraagstap-bewaren";
import { MET_DE_HAND, SPAM_REDEN, SPAM_VOORVOEGSEL } from "@/lib/aanvraaglijsten";

/*
  Het beheer van de aanvragen die via de website binnenkomen. Ze staan in
  dezelfde databank; het schema staat in  website/supabase/aanvragen.sql
  en  website/supabase/aanvragen-status.sql

  Elke knop stuurt in "terug" mee waar je stond (welk tabblad, welke soort,
  welke filter), zodat je na een klik niet terug bovenaan "alles" staat.
*/

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

/* Enkel een adres binnen de aanvragen, nooit iets dat van buiten komt. */
function waarheen(formData: FormData | null) {
  const terug = String(formData?.get("terug") ?? "");
  return terug.startsWith("/beheer/aanvragen") ? terug : "/beheer/aanvragen";
}

function terug(formData: FormData | null, bericht: string, fout = false): never {
  revalidatePath("/beheer/aanvragen");
  revalidatePath("/beheer");
  const basis = waarheen(formData);
  const url = new URL(basis, "http://x");
  url.searchParams.delete("fout");
  url.searchParams.delete("succes");
  url.searchParams.set(fout ? "fout" : "succes", bericht);
  redirect(`${url.pathname}?${url.searchParams.toString()}`);
}

/* De uitleg als de kolommen van aanvragen-status.sql er nog niet zijn. */
function zonderSql(boodschap: string) {
  return /stappen|gearchiveerd/.test(boodschap)
    ? "Draai eerst website/supabase/aanvragen-status.sql in Supabase; daarna werkt deze knop."
    : boodschap;
}

export async function zetAfgehandeld(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const afgehandeld = String(formData.get("afgehandeld") || "") === "ja";

  const { error } = await db
    .from("aanvragen")
    .update({ afgehandeld, gezien: true })
    .eq("id", id);

  if (error) terug(formData, error.message, true);
  terug(
    formData,
    afgehandeld
      ? "Behandeld. Je vindt de aanvraag nu bij het tabblad Behandeld."
      : "De aanvraag staat terug bij Te behandelen.",
  );
}

/* Eén stap aan- of uitzetten: mail verstuurd, gebeld, ingeschreven... */
export async function zetStap(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const stap = String(formData.get("stap") || "");
  const aan = String(formData.get("aan") || "") === "ja";
  if (!isStap(stap)) terug(formData, "Die knop ken ik niet.", true);

  const { fout, aantal } = await zetStapVoorGezin(id, stap, aan);
  if (fout) terug(formData, zonderSql(fout), true);
  if (aantal > 1) {
    terug(formData, `Bewaard bij de ${aantal} kinderen met dezelfde mededeling.`);
  }
  terug(formData, "Bewaard.");
}

export async function zetArchief(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const archief = String(formData.get("archief") || "") === "ja";

  const { error } = await db
    .from("aanvragen")
    .update({ gearchiveerd: archief, gezien: true })
    .eq("id", id);
  if (error) terug(formData, zonderSql(error.message), true);
  terug(
    formData,
    archief
      ? "In het archief gezet."
      : "Uit het archief gehaald.",
  );
}

/* Alles wat behandeld is in één keer naar het archief, eventueel enkel van
   één soort. */
export async function archiveerBehandeld(formData: FormData) {
  const db = await admin();
  const onderwerp = String(formData.get("onderwerp") || "");

  let vraag = db
    .from("aanvragen")
    .update({ gearchiveerd: true, gezien: true })
    .eq("afgehandeld", true)
    .eq("gearchiveerd", false)
    .neq("soort", MET_DE_HAND);
  if (onderwerp) vraag = vraag.eq("onderwerp", onderwerp);
  const { error } = await vraag;
  if (error) terug(formData, zonderSql(error.message), true);
  terug(formData, "De behandelde aanvragen staan in het archief.");
}

/*
  Bij spam zetten, of terug bij de echte aanvragen. Er wordt niets gewist:
  enkel het voorvoegsel "spam: " in de soort gaat erbij of eraf, plus de zin
  die zegt waarom. Zie lib/aanvraaglijsten.ts.
*/
export async function zetSpam(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const spam = String(formData.get("spam") || "") === "ja";

  const { data, error: leesFout } = await db
    .from("aanvragen")
    .select("soort, gegevens")
    .eq("id", id)
    .single();
  if (leesFout || !data) terug(formData, leesFout?.message ?? "Niet gevonden.", true);

  const gewoon = data.soort.startsWith(SPAM_VOORVOEGSEL)
    ? data.soort.slice(SPAM_VOORVOEGSEL.length)
    : data.soort;
  const gegevens = { ...(data.gegevens as Record<string, string>) };
  if (spam) {
    gegevens[SPAM_REDEN] ??= "zelf bij spam gezet";
  } else {
    delete gegevens[SPAM_REDEN];
  }

  const { error } = await db
    .from("aanvragen")
    .update({
      soort: spam ? (SPAM_VOORVOEGSEL + gewoon).slice(0, 40) : gewoon,
      gegevens,
      gezien: true,
    })
    .eq("id", id);
  if (error) terug(formData, error.message, true);
  terug(
    formData,
    spam
      ? "Bij spam gezet. Je vindt het op het tabblad Spam."
      : "Teruggezet bij de echte aanvragen.",
  );
}

export async function markeerAllesGezien(formData: FormData) {
  const db = await admin();
  const { error } = await db
    .from("aanvragen")
    .update({ gezien: true })
    .eq("gezien", false);

  if (error) terug(formData, error.message, true);
  terug(formData, "Alles staat op gelezen.");
}

export async function verwijderAanvraag(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const { error } = await db.from("aanvragen").delete().eq("id", id);
  if (error) terug(formData, error.message, true);
  terug(formData, "Aanvraag verwijderd.");
}
