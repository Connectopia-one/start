import "server-only";
import { createClient as createSupabaseClient } from "@supabase/supabase-js";

/**
 * Gebruikt de service-role sleutel en omzeilt daarmee alle RLS-regels.
 * Enkel gebruiken in server actions, na een expliciete requireBeheerder()-check —
 * nooit importeren in een Client Component.
 */
export function createAdminClient() {
  return createSupabaseClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { autoRefreshToken: false, persistSession: false } }
  );
}

/*
  De naam van het Supabase-project waar dit portaal mee praat.

  Er zijn er twee, eentje voor het ouderportaal en eentje voor het
  oefenplatform, en ze zien er in het dashboard precies hetzelfde uit. Draait
  een sql-bestand in het verkeerde project, dan lijkt alles gelukt terwijl de
  tabel hier niet bestaat. Door deze naam in een foutmelding te zetten, hoeft
  niemand te gokken welk project hij open moet doen.

  Het adres is sowieso publiek: het staat in elke pagina die de browser laadt.
*/
export function projectnaam(): string | null {
  const adres = process.env.NEXT_PUBLIC_SUPABASE_URL;
  if (!adres) return null;
  try {
    return new URL(adres).hostname.split(".")[0] || null;
  } catch {
    return null;
  }
}

/*
  De uitleg bij een fout die zegt dat een tabel niet bestaat.

  Er zijn twee heel verschillende gevallen, en ze zien er op het scherm
  hetzelfde uit:

  - 42P01 komt uit de databank zelf: de tabel bestaat echt niet. Dan is het
    sql-bestand niet gedraaid, of in het verkeerde van de twee projecten.
  - PGRST205 komt uit de tussenlaag die Supabase voor de databank zet. Die
    onthoudt welke tabellen er zijn, en die lijst kan blijven hangen. De tabel
    staat er dan wél, maar de API ziet ze nog niet.

  Door die twee apart te benoemen hoeft niemand te gokken, en staat de code
  erbij voor het geval het nog iets anders is.
*/
/*
  Dezelfde uitleg, maar voor een kolom die nog niet bestaat.

  Een tabel die ontbreekt valt op: er staat meteen niets meer op het scherm.
  Een kolom die ontbreekt is gemener. De tabel is er, de bladzijde laadt, en
  enkel het bewaren mislukt — of een select die die kolom meevraagt geeft niets
  terug, zodat een ingevulde fiche er leeg uitziet. Dat is precies wat Kim op
  11 en 12 oktober 2026 beschreef als "hij bewaart het niet".

  Postgres geeft 42703 voor een onbekende kolom; PostgREST stuurt PGRST204 als
  zijn eigen lijst van kolommen nog niet bijgewerkt is.
*/
export function kolomOntbreekt(
  fout: { message?: string; code?: string },
  bestand: string,
): string | null {
  const tekst = fout.message || "";
  const isKolom =
    fout.code === "42703" ||
    fout.code === "PGRST204" ||
    /column .* does not exist/i.test(tekst) ||
    /could not find the '.*' column/i.test(tekst);
  if (!isKolom) return null;

  const project = projectnaam();
  const waar = project
    ? `het Supabase-project met het adres ${project}.supabase.co`
    : "het Supabase-project van het ouderportaal";

  return (
    `Deze fiche heeft een kolom nodig die nog niet in de databank staat. ` +
    `Draai ${bestand} in de SQL Editor van ${waar}. Je hebt twee projecten; ` +
    `in het andere staat het oefenplatform. (${tekst || "code " + (fout.code || "?")})`
  );
}

export function tabelOntbreekt(
  fout: { message?: string; code?: string },
  tabel: string,
  bestand: string,
): string | null {
  const tekst = fout.message || "";
  const echtWeg = fout.code === "42P01" || /does not exist/i.test(tekst);
  const cacheWeg =
    fout.code === "PGRST205" || /could not find the table/i.test(tekst);
  if (!echtWeg && !cacheWeg) return null;

  const project = projectnaam();
  const waar = project
    ? `het Supabase-project met het adres ${project}.supabase.co`
    : "het Supabase-project van het ouderportaal";

  /*
    PGRST205 betekent niet alleen "de lijst van de API is verouderd": ze komt
    ook als de tabel er in dít project gewoon niet is. Op 11 oktober 2026 stond
    hier dat de tabel "misschien al klaar" stond, en dat stuurde Kim een
    kwartier lang achter een vernieuwing aan terwijl ze het bestand in het
    andere project gedraaid had. Dus: het project eerst.
  */
  if (cacheWeg) {
    return (
      `De API van Supabase vindt de tabel ${tabel} niet. Dat heeft twee mogelijke ` +
      `oorzaken. Kijk eerst of je in ${waar} zit: je hebt twee projecten, en in ` +
      `het andere staat het oefenplatform. Draai ${bestand} daar. Staat de tabel ` +
      `er wel, dan moet de API haar lijst nog vernieuwen; draai dan deze ene ` +
      `regel: select pg_notify($$pgrst$$, $$reload schema$$); ` +
      `(code ${fout.code || "?"})`
    );
  }
  return (
    `De tabel ${tabel} bestaat nog niet. Draai ${bestand} in de SQL Editor van ${waar}. ` +
    `Onderaan moet een rij verschijnen, niet enkel "Success". Je hebt twee projecten; ` +
    `in het andere staat het oefenplatform. (code ${fout.code || "?"})`
  );
}
