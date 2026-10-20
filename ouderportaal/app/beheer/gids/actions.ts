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

/* ──────────────────────────────────────────────────────────────── */

/*
  Een logo bij een aangebrachte organisatie.

  Kim op 20 oktober 2026: "wat ik wel merk is dat er geen foto's bijkomen bij
  de nieuwe personen bij waar kan ik terecht". Het formulier vroeg nooit om
  een logo, en hier kon je er geen opladen. Nu wel.

  Het bestand gaat rechtstreeks vanuit de browser naar de open bak "social"
  (die van In de kijker), in de map gids/. Zo ontwijken we de limiet van
  4,5MB van Vercel, zoals bij de beelden van In de kijker. De kolom "logo"
  maakt website/supabase/gids-logo.sql aan.
*/
const BAK = "social";

type Antwoord = { gelukt: true } | { gelukt: false; bericht: string };

function logoFout(bericht: string): string {
  if (/bucket not found/i.test(bericht)) {
    return 'De bak "social" bestaat nog niet. Die maakt website/supabase/social.sql aan.';
  }
  if (/logo/i.test(bericht) && /column|kolom|schema cache/i.test(bericht)) {
    return "De databank kent nog geen logo. Draai eenmalig website/supabase/gids-logo.sql in de Supabase van het ouderportaal.";
  }
  return bericht || "Er ging iets mis.";
}

export async function maakLogoUploadUrl(
  bestandsnaam: string,
): Promise<
  { gelukt: true; pad: string; token: string } | { gelukt: false; bericht: string }
> {
  const db = await admin();
  const veilig = bestandsnaam.replace(/[^a-zA-Z0-9.-]/g, "-").slice(-60);
  const pad = `gids/${Date.now()}-${Math.random().toString(36).slice(2, 8)}-${veilig}`;

  const { data, error } = await db.storage.from(BAK).createSignedUploadUrl(pad);
  if (error || !data) {
    return { gelukt: false, bericht: logoFout(error?.message ?? "") };
  }
  return { gelukt: true, pad: data.path, token: data.token };
}

export async function zetLogo(invoer: {
  id: string;
  logo: string | null;
}): Promise<Antwoord> {
  const db = await admin();

  const { data: oud } = await db
    .from("gids_aanmeldingen")
    .select("logo")
    .eq("id", invoer.id)
    .maybeSingle();

  const { error } = await db
    .from("gids_aanmeldingen")
    .update({ logo: invoer.logo })
    .eq("id", invoer.id);
  if (error) {
    /* Het nieuwe bestand staat al in de bak; zonder rij hoort het daar niet. */
    if (invoer.logo) await db.storage.from(BAK).remove([invoer.logo]);
    return { gelukt: false, bericht: logoFout(error.message) };
  }

  /* Het vorige logo mag weg, maar alleen als het echt in onze map stond. */
  const vorige = (oud as { logo: string | null } | null)?.logo;
  if (vorige && vorige !== invoer.logo && vorige.startsWith("gids/")) {
    await db.storage.from(BAK).remove([vorige]);
  }

  revalidatePath(PAD);
  return { gelukt: true };
}
