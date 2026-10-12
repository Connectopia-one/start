import type { SupabaseClient } from "@supabase/supabase-js";
import { schikOpties } from "@/lib/optievolgorde";
import { bouwVarianten } from "@/lib/spellingvariant";

/*
  Eén rij uit de tabel "vragen" klaarmaken voor de browser.

  Twee bladzijden doen dit: de oefeningen van een hoofdstuk
  (app/vakken/<vak>/<volgnummer>) en het examen over een heel vak
  (app/niveaus/<niveau>/<vak>/examen). Allebei moeten ze exact hetzelfde doen,
  anders schudt de ene de opties wel en de andere niet, en staat het juiste
  antwoord op het examen plots altijd bovenaan.

  De rij komt binnen met "*". Dat is met opzet: zolang een sql-bestand als
  spellingvarianten.sql nog niet gedraaid is, bestaat de kolom "varianten" nog
  niet, en een select die die kolom bij naam vraagt zou het hele hoofdstuk leeg
  laten in plaats van één veld.
*/
export type VraagRij = Record<string, unknown>;

export async function maakVraag(supabase: SupabaseClient, rij: VraagRij) {
  // Alleen wat de browser nodig heeft. Door "*" staan er ook kolommen in die
  // daar niets te zoeken hebben.
  const v = {
    id: rij.id as string,
    type: rij.type as "meerkeuze" | "invultekst" | "waarofniet",
    vraag: rij.vraag as string,
    opties: (rij.opties ?? null) as string[] | null,
    antwoord: rij.antwoord as number | string | boolean | number[] | string[],
    uitleg: (rij.uitleg ?? null) as string | null,
    volgnummer: rij.volgnummer as number,
  };
  // Wisselende woorden bij spelling: elke beurt krijgt hier haar eigen
  // geschudde opties mee. Welke beurt een kind ziet, weet pas de browser,
  // want daar staat welk kind aan het oefenen is. Zie lib/spellingvariant.ts.
  const varianten = bouwVarianten(v, rij.varianten);
  // De opties krijgen hier hun volgorde, zodat het juiste antwoord niet altijd
  // bovenaan staat. Zie lib/optievolgorde.ts.
  const kern = { ...schikOpties(v), varianten };

  const pad = (rij.afbeelding_pad ?? null) as string | null;
  if (!pad) return { ...kern, afbeeldingUrl: null as string | null };
  if (pad.startsWith("http")) return { ...kern, afbeeldingUrl: pad };
  const { data } = await supabase.storage
    .from("vraagafbeeldingen")
    .createSignedUrl(pad, 3600);
  return { ...kern, afbeeldingUrl: data?.signedUrl ?? null };
}
