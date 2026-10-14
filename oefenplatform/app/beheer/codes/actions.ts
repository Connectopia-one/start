"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

export async function maakCode(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "").trim();
  const label = String(formData.get("label") || "").trim() || null;
  if (!code)
    redirect("/beheer/codes?fout=" + encodeURIComponent("Geef een code op."));

  const admin = createAdminClient();
  const { error } = await admin.from("plusklas_codes").insert({ code, label });
  if (error)
    redirect(
      "/beheer/codes?fout=" +
        encodeURIComponent("Kon code niet aanmaken (bestaat die al?)."),
    );

  revalidatePath("/beheer/codes");
  redirect("/beheer/codes");
}

export async function wisselActief(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "");
  const actief = formData.get("actief") === "true";
  const admin = createAdminClient();
  await admin
    .from("plusklas_codes")
    .update({ actief: !actief })
    .eq("code", code);
  revalidatePath("/beheer/codes");
  redirect("/beheer/codes");
}

/**
 * Zet voor deze groep de volle opvolging aan of uit.
 *
 * Kim op 14 oktober 2026: enkel de kindjes van de plusklas van Hasselt volgt
 * ze in detail op. Staat dit aan, dan is er per kind een fiche met de
 * opgeloste testen, de opmerkingen en het werk van thuis; staat het uit, dan
 * blijft het bij de tabel met de voortgang op /begeleiding. Niets gaat weg bij
 * het uitzetten: wat genoteerd staat, blijft staan.
 */
export async function wisselOpvolging(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "");
  const volledig = formData.get("volledig") === "true";
  const admin = createAdminClient();
  const { error } = await admin
    .from("plusklas_codes")
    .update({ volledige_opvolging: !volledig })
    .eq("code", code);
  if (error) {
    redirect(
      "/beheer/codes?fout=" +
        encodeURIComponent(
          "Dat lukte niet. Draai eerst supabase/volledige-opvolging.sql; dat bestand maakt dit vinkje.",
        ),
    );
  }
  revalidatePath("/beheer/codes");
  revalidatePath("/begeleiding");
  redirect("/beheer/codes");
}

export async function verwijderCode(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "");
  const admin = createAdminClient();
  await admin.from("plusklas_codes").delete().eq("code", code);
  revalidatePath("/beheer/codes");
  redirect("/beheer/codes");
}

/**
 * Zet in één keer de gratis toegang uit van iedereen die met deze code
 * binnenkwam. Bedoeld voor het einde van een testperiode: anders is dat
 * zestien keer op dezelfde knop klikken bij Gezinnen.
 *
 * Dit raakt enkel de gratis toegang die jij gaf. Wie voor dit schooljaar
 * betaald heeft, houdt zijn toegang, want die hangt aan toegang_schooljaar en
 * niet aan is_plusklas. En niets van wat een gezin opbouwde gaat weg: de
 * kinderen, hun voortgang en hun stickers blijven staan.
 */
export async function zetGroepToegangUit(formData: FormData) {
  await requireBeheerder();
  const code = String(formData.get("code") || "");
  if (!code) redirect("/beheer/codes");

  const admin = createAdminClient();
  const { data, error } = await admin
    .from("profiles")
    .update({ is_plusklas: false })
    .eq("plusklas_code", code)
    .eq("is_plusklas", true)
    .select("id");

  if (error) {
    redirect(
      "/beheer/codes?fout=" +
        encodeURIComponent(`De toegang uitzetten lukte niet: ${error.message}`),
    );
  }

  const aantal = data?.length ?? 0;
  revalidatePath("/beheer/codes");
  revalidatePath("/beheer/gezinnen");
  redirect(
    "/beheer/codes?melding=" +
      encodeURIComponent(
        aantal === 0
          ? `Niemand met de code ${code} had nog gratis toegang.`
          : aantal === 1
            ? `De gratis toegang van 1 account met de code ${code} staat uit.`
            : `De gratis toegang van ${aantal} accounts met de code ${code} staat uit.`,
      ),
  );
}
