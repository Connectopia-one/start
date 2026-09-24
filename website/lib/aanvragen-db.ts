import "server-only";
import { createClient } from "@supabase/supabase-js";

/*
  Een ingevuld formulier van de website komt in de databank van Connectopia
  (dezelfde Supabase als het ouderportaal en het prikbord). Het schema staat
  in  website/supabase/aanvragen.sql

  Waarom niet meer per mail: tot 24 september 2026 opende het formulier het
  mailprogramma van de bezoeker. Dat werkt niet voor wie zijn mail in de
  browser leest, en een ouder die op zijn telefoon geen mailprogramma heeft
  ingesteld, geraakte er helemaal niet door.

  Er is met opzet geen terugval meer op die mail. Zo'n terugval hing af van
  een controle die bij het bouwen van de site gebeurde, en die uitkomst bleef
  daarna in de pagina zitten: bezoekers kregen dagen later nog het oude
  formulier te zien. Lukt het bewaren niet, dan komt de bezoeker nu op
  /bedankt?fout=1, met ons mailadres en telefoonnummer erbij.
*/

export type NieuweAanvraag = {
  onderwerp: string;
  soort: string;
  /* De vragen en antwoorden zoals ze op het formulier stonden. */
  gegevens: Record<string, string>;
};

function verbinding() {
  const adres = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const sleutel = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!adres || !sleutel) return null;
  return createClient(adres, sleutel, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}

export async function bewaarAanvraag(aanvraag: NieuweAanvraag) {
  const db = verbinding();
  if (!db) return { fout: "geen-databank" as const };
  const { error } = await db.from("aanvragen").insert({
    onderwerp: aanvraag.onderwerp,
    soort: aanvraag.soort,
    gegevens: aanvraag.gegevens,
  });
  if (error) {
    console.error("Aanvraag bewaren mislukt:", error.message);
    return { fout: "mislukt" as const };
  }
  return { fout: null };
}
