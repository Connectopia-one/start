import "server-only";
import { createClient } from "@supabase/supabase-js";

/*
  De briefjes die bezoekers zelf ophangen, komen in de databank van
  Connectopia (dezelfde Supabase als het ouderportaal). Het schema staat
  in  website/supabase/prikbord.sql

  Zijn de sleutels nog niet ingesteld, dan werkt de site gewoon verder:
  je ziet dan alleen de vaste briefjes uit content/prikbord.ts en het
  formulier zegt dat ophangen nog niet kan.
*/

export type DbBriefje = {
  id: string;
  bord: string;
  tekst: string;
  naam: string | null;
  wanneer: string | null;
  created_at: string;
};

function verbinding() {
  const adres = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const sleutel = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!adres || !sleutel) return null;
  return createClient(adres, sleutel, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}

/* Staat de databank klaar? Zo niet, dan tonen we het formulier niet. */
export function prikbordKlaar() {
  return verbinding() !== null;
}

export async function haalBriefjes(bord: string): Promise<DbBriefje[]> {
  const db = verbinding();
  if (!db) return [];
  const { data, error } = await db
    .from("prikbord_briefjes")
    .select("id, bord, tekst, naam, wanneer, created_at")
    .eq("bord", bord)
    .order("created_at", { ascending: false })
    .limit(100);
  if (error) {
    console.error("Prikbord lezen mislukt:", error.message);
    return [];
  }
  return (data ?? []) as DbBriefje[];
}

export async function bewaarBriefje(briefje: {
  bord: string;
  tekst: string;
  naam: string;
  volledigeNaam: string;
  contact: string;
  wanneer: string | null;
}) {
  const db = verbinding();
  if (!db) return { fout: "geen-databank" as const };
  const { error } = await db.from("prikbord_briefjes").insert({
    bord: briefje.bord,
    tekst: briefje.tekst,
    naam: briefje.naam,
    volledige_naam: briefje.volledigeNaam,
    contact: briefje.contact,
    wanneer: briefje.wanneer,
  });
  if (error) {
    console.error("Briefje ophangen mislukt:", error.message);
    return { fout: "mislukt" as const };
  }
  return { fout: null };
}

export async function meldBriefje(briefjeId: string, reden: string) {
  const db = verbinding();
  if (!db) return { fout: "geen-databank" as const };
  const { error } = await db
    .from("prikbord_meldingen")
    .insert({ briefje_id: briefjeId, reden });
  if (error) {
    console.error("Melding bewaren mislukt:", error.message);
    return { fout: "mislukt" as const };
  }
  return { fout: null };
}
