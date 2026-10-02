"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { leesLink, haalBeeldBinnen, schoonLink } from "@/lib/linkuitlezen";
import type { Gevonden } from "@/lib/linkuitlezen";

/*
  Het beheer van de pagina "In de kijker" op de website: de berichten van
  sociale media. De tabel staat in dezelfde databank; het schema staat in
  website/supabase/social.sql

  Een bericht dat iemand van buiten instuurde, staat op "niet zichtbaar".
  Pas als jij het hier op de site zet, is het te zien.
*/

const BAK = "social";

const KANALEN = [
  "facebook",
  "instagram",
  "linkedin",
  "tiktok",
  "youtube",
  "anders",
] as const;

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

/*
  Een tijdelijke, rechtstreekse upload-link naar Supabase Storage. Zo gaat
  het beeld niet door de server action heen, en loopt het niet tegen de
  limiet van ongeveer 4,5MB die Vercel op een gewoon verzoek zet.
*/
export async function maakBeeldUploadUrl(bestandsnaam: string) {
  const db = await admin();
  const veilig = bestandsnaam.replace(/[^a-zA-Z0-9.-]/g, "-").slice(-60);
  const pad = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}-${veilig}`;

  const { data, error } = await db.storage.from(BAK).createSignedUploadUrl(pad);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { pad: data.path, token: data.token };
}

/*
  Waarom bewaren een antwoord teruggeeft in plaats van een fout te gooien.

  Gooit een server action in productie een fout, dan vervangt Next de melding
  door "Minified React error #441". Dat is de gemaskeerde serverfout, en dan
  staat er op het scherm niets meer over wat er echt misliep. Daarom geven we
  de melding gewoon terug als tekst.
*/
type Antwoord = { gelukt: true } | { gelukt: false; bericht: string };

function mislukt(bericht: string): Antwoord {
  return { gelukt: false, bericht };
}

/* De melding van de databank omzetten naar iets waar je iets aan hebt. */
function uitleg(fout: { message: string; code?: string }): string {
  const tekst = fout.message || "Er ging iets mis.";
  const ontbreekt =
    fout.code === "42P01" ||
    fout.code === "PGRST205" ||
    /does not exist|could not find the table/i.test(tekst);
  if (ontbreekt) {
    return "De tabel voor In de kijker bestaat nog niet. Draai eerst website/supabase/social.sql in Supabase.";
  }
  return tekst;
}

/*
  De link uitlezen, zodat de velden eronder al ingevuld staan. Het beeld
  halen we hier nog niet binnen: wie de link intypt en zich dan bedenkt, mag
  geen beeld achterlaten in onze bak. We geven het adres terug om te laten
  zien, en halen het pas echt binnen bij het bewaren.
*/
export async function haalLinkGegevens(link: string): Promise<Gevonden> {
  await requireBeheerder();
  return leesLink(schoonLink(link));
}

/*
  Het voorbeeldbeeld van een link bij ons opslaan. Zo doet de bezoeker van de
  website nooit een verzoek naar TikTok of YouTube, en blijft het beeld staan
  als hun eigen adres verloopt.
*/
async function beeldVanLinkBewaren(
  db: Awaited<ReturnType<typeof admin>>,
  adres: string,
): Promise<string | null> {
  try {
    const beeld = await haalBeeldBinnen(adres);
    if (!beeld) return null;

    const pad = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}-link.${beeld.extensie}`;
    const { error } = await db.storage
      .from(BAK)
      .upload(pad, beeld.bytes, { contentType: beeld.soort });
    if (error) return null;
    return pad;
  } catch {
    /* Geen beeld is geen reden om het bericht niet te bewaren. */
    return null;
  }
}

export async function bewaarNieuwePost(invoer: {
  titel: string | null;
  tekst: string;
  van: string;
  kanaal: string;
  link: string;
  eigen: boolean;
  beeld: string | null;
  /* Het beeld dat we bij de link vonden, als er zelf niets opgeladen werd. */
  beeldVanLink?: string | null;
}): Promise<Antwoord> {
  const db = await admin();

  const link = schoonLink(invoer.link);
  const tekst = invoer.tekst.trim();
  const van = invoer.van.trim();

  if (!link.startsWith("https://")) {
    return mislukt("De link moet met https:// beginnen.");
  }
  if (tekst.length < 2)
    return mislukt("Schrijf er even bij waar het over gaat.");
  if (van.length < 2) return mislukt("Vul in van wie het bericht is.");

  const kanaal = (KANALEN as readonly string[]).includes(invoer.kanaal)
    ? invoer.kanaal
    : "anders";

  /* Zelf opgeladen gaat voor op wat we bij de link vonden. */
  const beeld =
    invoer.beeld ??
    (invoer.beeldVanLink
      ? await beeldVanLinkBewaren(db, invoer.beeldVanLink)
      : null);

  const { error } = await db.from("kijker_posts").insert({
    titel: invoer.titel?.trim() || null,
    tekst,
    van,
    kanaal,
    link,
    beeld,
    eigen: invoer.eigen,
    /* Wat jij zelf toevoegt, staat meteen op de site. */
    zichtbaar: true,
    gezien: true,
  });

  if (error) return mislukt(uitleg(error));
  revalidatePath("/beheer/in-de-kijker");
  return { gelukt: true as const };
}

/* Een beeld bij een bericht dat er al staat, of een beeld vervangen. */
export async function zetBeeld(invoer: { id: string; beeld: string }) {
  const db = await admin();

  const { data: oud } = await db
    .from("kijker_posts")
    .select("beeld")
    .eq("id", invoer.id)
    .maybeSingle();

  const { error } = await db
    .from("kijker_posts")
    .update({ beeld: invoer.beeld })
    .eq("id", invoer.id);
  if (error) throw new Error(error.message);

  /* Het oude beeld mag weg, maar alleen als het echt in onze bak stond. */
  const vorige = (oud as { beeld: string | null } | null)?.beeld;
  if (vorige && vorige !== invoer.beeld && !vorige.startsWith("https://")) {
    await db.storage.from(BAK).remove([vorige]);
  }

  revalidatePath("/beheer/in-de-kijker");
}

export async function zetZichtbaar(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const zichtbaar = String(formData.get("zichtbaar") || "") === "ja";

  const { error } = await db
    .from("kijker_posts")
    .update({ zichtbaar, gezien: true })
    .eq("id", id);

  if (error) {
    redirect("/beheer/in-de-kijker?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/in-de-kijker");
  redirect(
    "/beheer/in-de-kijker?succes=" +
      encodeURIComponent(
        zichtbaar
          ? "Het bericht staat nu op de website."
          : "Het bericht staat niet meer op de website.",
      ),
  );
}

export async function verwijderPost(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const beeld = String(formData.get("beeld") || "");

  if (beeld && !beeld.startsWith("https://")) {
    await db.storage.from(BAK).remove([beeld]);
  }
  const { error } = await db.from("kijker_posts").delete().eq("id", id);

  if (error) {
    redirect("/beheer/in-de-kijker?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/in-de-kijker");
  redirect(
    "/beheer/in-de-kijker?succes=" + encodeURIComponent("Bericht verwijderd."),
  );
}

export async function markeerGezien(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  const vraag = db.from("kijker_posts").update({ gezien: true });
  const { error } = id
    ? await vraag.eq("id", id)
    : await vraag.eq("gezien", false);

  if (error) {
    redirect("/beheer/in-de-kijker?fout=" + encodeURIComponent(error.message));
  }
  revalidatePath("/beheer/in-de-kijker");
  revalidatePath("/beheer");
  redirect("/beheer/in-de-kijker");
}
