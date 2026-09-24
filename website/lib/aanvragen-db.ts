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

  Staan de sleutels niet ingesteld, dan valt het formulier terug op die mail,
  zodat de site nooit stuk is.
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

/*
  Staat de databank klaar? Zo niet, dan mailt het formulier zoals vroeger.

  We kijken niet alleen of de sleutels ingesteld zijn maar ook of de tabel er
  echt al staat. Dat is met opzet: de sleutels staan er al voor het prikbord,
  dus zonder die tweede controle zou het formulier naar een tabel sturen die
  nog niet bestaat, en kreeg elke bezoeker een foutmelding. Nu blijft het
  formulier mailen tot het schema uitgevoerd is, en schakelt het daarna
  vanzelf over.
*/
export async function aanvragenKlaar() {
  const db = verbinding();
  if (!db) return false;
  const { error } = await db
    .from("aanvragen")
    .select("id", { count: "exact", head: true })
    .limit(1);
  if (!error) return true;
  /*
    De website mag deze tabel met opzet niet lezen, alleen aanvullen. Een
    foutmelding over rechten is dus juist het bewijs dat de tabel er staat en
    dat de rechten kloppen. Elke andere fout — de tabel bestaat nog niet, of
    de databank is onbereikbaar — laat het formulier terugvallen op de mail,
    want dan komt een aanvraag tenminste nog ergens aan.
  */
  return (
    error.code === "42501" ||
    /permission denied|not authorized|row-level security/i.test(
      error.message ?? ""
    )
  );
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
