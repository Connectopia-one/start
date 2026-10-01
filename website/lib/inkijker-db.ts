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
  return (data ?? []) as DbPost[];
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
