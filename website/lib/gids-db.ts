import "server-only";
import { createClient } from "@supabase/supabase-js";
import type { Organisatie } from "@/content/gids";
import { gidsTekst } from "@/content/gids";

/*
  De organisaties die iemand via het formulier onderaan de gids aanbracht.
  Ze staan in de databank van Connectopia (dezelfde Supabase als het
  ouderportaal); het schema staat in  website/supabase/gids.sql

  Pas als ze in het ouderportaal goedgekeurd zijn, komen ze in de gids, bij
  de vaste lijst uit content/gids.ts. Zijn de sleutels nog niet ingesteld,
  dan toont de gids gewoon die vaste lijst.
*/

function verbinding() {
  const adres = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const sleutel = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!adres || !sleutel) return null;
  return createClient(adres, sleutel, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}

export function gidsDbKlaar() {
  return verbinding() !== null;
}

export async function haalGoedgekeurde(): Promise<Organisatie[]> {
  const db = verbinding();
  if (!db) return [];

  /* Eerst met het logo. Draaide supabase/gids-logo.sql nog niet, dan bestaat
     die kolom niet en lezen we gewoon zonder: dan staan ze er zonder logo,
     in plaats van helemaal niet. */
  const metLogo = await db
    .from("gids_aanmeldingen")
    .select("naam, omschrijving, regio, link, logo")
    .limit(200);
  const { data, error } = metLogo.error
    ? await db
        .from("gids_aanmeldingen")
        .select("naam, omschrijving, regio, link")
        .limit(200)
    : metLogo;
  if (error) {
    /* Bestaat de tabel nog niet, dan staat gewoon de vaste lijst er. */
    console.error("Gids lezen mislukt:", error.message);
    return [];
  }
  return (
    (data ?? []) as {
      naam: string;
      omschrijving: string;
      regio: string | null;
      link: string | null;
      logo?: string | null;
    }[]
  ).map((rij) => ({
    naam: rij.naam,
    categorie: gidsTekst.categorieAangebracht,
    omschrijving: rij.omschrijving,
    regio: rij.regio ?? undefined,
    link: rij.link ?? undefined,
    /* Het logo staat in de open bak "social"; daar maken we een volledig
       webadres van. */
    logo: rij.logo
      ? db.storage.from("social").getPublicUrl(rij.logo).data.publicUrl
      : undefined,
  }));
}

export async function bewaarAanmelding(rij: {
  naam: string;
  omschrijving: string;
  regio: string | null;
  link: string | null;
  wie: "zelf" | "iemand";
  volledigeNaam: string;
  contact: string;
}) {
  const db = verbinding();
  if (!db) return { fout: "geen-databank" as const };
  const { error } = await db.from("gids_aanmeldingen").insert({
    naam: rij.naam,
    omschrijving: rij.omschrijving,
    regio: rij.regio,
    link: rij.link,
    wie: rij.wie,
    volledige_naam: rij.volledigeNaam,
    contact: rij.contact,
  });
  if (error) {
    console.error("Organisatie aanbrengen mislukt:", error.message);
    return { fout: "mislukt" as const };
  }
  return { fout: null };
}
