import "server-only";
import { createClient } from "@supabase/supabase-js";

/*
  De berichten van sociale media die op /in-de-kijker staan, komen uit de
  databank van Connectopia (dezelfde Supabase als het ouderportaal). Het
  schema staat in  website/supabase/social.sql

  Zijn de sleutels nog niet ingesteld, dan werkt de pagina gewoon verder:
  je ziet dan alleen de berichten uit content/inkijker.ts en het formulier
  zegt dat insturen nog niet kan.
*/

export type DbPost = {
  id: string;
  titel: string | null;
  tekst: string;
  van: string;
  kanaal: string;
  link: string;
  beeld: string | null;
  eigen: boolean;
  created_at: string;
};

const BAK = "social";

function verbinding() {
  const adres = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const sleutel = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!adres || !sleutel) return null;
  return createClient(adres, sleutel, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}

/* Staat de databank klaar? Zo niet, dan tonen we het formulier niet. */
export function inkijkerKlaar() {
  return verbinding() !== null;
}

/*
  Het webadres van een beeld in de open bak "social". Staat er een volledig
  adres in de databank, dan gebruiken we dat gewoon zoals het er staat.
*/
export function beeldAdres(pad: string): string | null {
  if (pad.startsWith("https://")) return pad;
  const db = verbinding();
  if (!db) return null;
  return db.storage.from(BAK).getPublicUrl(pad).data.publicUrl;
}

/*
  De rommel achter het vraagteken weghalen.

  Wie op "kopieer link" klikt bij Instagram of TikTok, krijgt er volgcode bij:
  utm_source, igsh, en bij Instagram ook stkn. Dat laatste is een deelsleutel
  die aan het account van wie kopieerde hangt, en zoiets zetten we niet op de
  website. We halen alleen bekende volgparameters weg, nooit iets anders: de
  ?v= van een YouTube-filmpje moet blijven staan.

  Dezelfde lijst staat in ouderportaal/lib/linkuitlezen.ts; die twee moeten
  gelijk blijven.
*/
const WEG = new Set([
  "stkn",
  "igsh",
  "igshid",
  "fbclid",
  "gclid",
  "mibextid",
  "si",
  "feature",
  "share_id",
  "share_app_id",
  "_t",
  "_r",
  "utm_source",
  "utm_medium",
  "utm_campaign",
  "utm_content",
  "utm_term",
  "utm_name",
]);

export function schoonLink(link: string): string {
  const adres = link.trim();
  try {
    const url = new URL(adres);
    if (url.protocol !== "https:") return adres;
    for (const sleutel of [...url.searchParams.keys()]) {
      if (WEG.has(sleutel.toLowerCase())) url.searchParams.delete(sleutel);
    }
    url.search = url.searchParams.toString();
    return url.toString();
  } catch {
    return adres;
  }
}

export async function haalPosts(): Promise<DbPost[]> {
  const db = verbinding();
  if (!db) return [];
  const { data, error } = await db
    .from("kijker_posts")
    .select("id, titel, tekst, van, kanaal, link, beeld, eigen, created_at")
    .order("created_at", { ascending: false })
    .limit(60);
  if (error) {
    console.error("In de kijker lezen mislukt:", error.message);
    return [];
  }
  /* Ook de links die er al in staan, gaan schoon de pagina op. */
  return ((data ?? []) as DbPost[]).map((post) => ({
    ...post,
    link: schoonLink(post.link),
  }));
}

export async function bewaarPost(post: {
  titel: string | null;
  tekst: string;
  van: string;
  kanaal: string;
  link: string;
  volledigeNaam: string;
  contact: string;
}) {
  const db = verbinding();
  if (!db) return { fout: "geen-databank" as const };
  const { error } = await db.from("kijker_posts").insert({
    titel: post.titel,
    tekst: post.tekst,
    van: post.van,
    kanaal: post.kanaal,
    link: post.link,
    volledige_naam: post.volledigeNaam,
    contact: post.contact,
  });
  if (error) {
    console.error("Bericht insturen mislukt:", error.message);
    return { fout: "mislukt" as const };
  }
  return { fout: null };
}
