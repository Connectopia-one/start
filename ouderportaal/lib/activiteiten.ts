/*
  Activiteiten: de kampdagen, lessen en werkingen waar een kind bij hoort.

  Kim duidt dat zelf aan, los van wat een ouder op het inschrijfformulier
  aankruiste. Een aanvraag is een vraag; een deelname is een bevestiging. Zie
  supabase/activiteiten.sql.
*/

export type Activiteit = {
  id: string;
  naam: string;
  soort: string;
  datum: string | null;
  plaats: string | null;
  archief: boolean;
};

/* De soorten die er nu zijn. Het is vrije tekst in de databank, dus er mag er
   altijd een bijkomen; dit is enkel wat het keuzelijstje toont. */
export const SOORTEN = [
  "kamp",
  "les",
  "pluswerking",
  "plusklas",
  "proefles",
  "andere",
] as const;

export function datumTekst(datum: string | null) {
  if (!datum) return null;
  return new Date(datum).toLocaleDateString("nl-BE", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

/*
  Een dag eerst, op datum; wat geen datum heeft, zoals een wekelijkse les,
  komt daarachter op naam. Het archief gaat helemaal naar onder.
*/
export function sorteer(lijst: Activiteit[]) {
  return [...lijst].sort((a, b) => {
    if (a.archief !== b.archief) return a.archief ? 1 : -1;
    if (a.datum && b.datum) return a.datum.localeCompare(b.datum);
    if (a.datum) return -1;
    if (b.datum) return 1;
    return a.naam.localeCompare(b.naam, "nl");
  });
}

/* De leeftijd die een kind vandaag heeft. Op een lijst wil je dat zien staan,
   niet een geboortedatum waar je zelf van moet aftrekken. */
export function leeftijd(geboortedatum: string | null) {
  if (!geboortedatum) return null;
  const geboren = new Date(geboortedatum);
  if (Number.isNaN(geboren.getTime())) return null;
  const nu = new Date();
  let jaar = nu.getFullYear() - geboren.getFullYear();
  const maand = nu.getMonth() - geboren.getMonth();
  if (maand < 0 || (maand === 0 && nu.getDate() < geboren.getDate())) jaar--;
  return jaar >= 0 && jaar < 130 ? jaar : null;
}
