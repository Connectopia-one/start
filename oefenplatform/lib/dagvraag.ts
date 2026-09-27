/**
 * De vraag van de dag, en het weekdoel dat eraan hangt.
 *
 * Elke dag staat er één vraag op de startpagina. Niet om er een dagelijkse
 * verplichting van te maken — Kim vroeg uitdrukkelijk het omgekeerde — maar
 * omdat er dan elke dag iets nieuws te rapen valt. Het doel dat een kind
 * bijhoudt is er daarom één per week: drie keer langskomen is genoeg. Dat is
 * haalbaar naast school, en een drukke week breekt niets stuk.
 *
 * Alles in dit bestand rekent in Belgische tijd. Een kind dat 's avonds om
 * elf uur oefent, hoort dezelfde vraag te zien als 's ochtends, en de dag
 * hoort om middernacht bij ons om te slaan, niet in Greenwich.
 */

/** Hoeveel dagen per week een kind moet langskomen om het weekdoel te halen. */
export const WEEKDOEL = 3;

const BELGIE = "Europe/Brussels";

/** Vandaag in Belgische tijd, als "2026-09-27". */
export function vandaagSleutel(nu: Date = new Date()): string {
  // en-CA schrijft een datum als jjjj-mm-dd, precies wat we willen.
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: BELGIE,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(nu);
}

/** De maandag van de week waarin die dag valt, als "2026-09-21". */
export function weekSleutel(nu: Date = new Date()): string {
  return maandagVan(vandaagSleutel(nu));
}

/** De maandag van de week waarin deze dag ("2026-09-27") valt. */
export function maandagVan(dag: string): string {
  const d = alsDatum(dag);
  // getUTCDay geeft zondag = 0; wij willen maandag = 0.
  const weekdag = (d.getUTCDay() + 6) % 7;
  d.setUTCDate(d.getUTCDate() - weekdag);
  return d.toISOString().slice(0, 10);
}

/** De maandag van de week ná deze maandag. */
export function volgendeWeek(maandag: string): string {
  const d = alsDatum(maandag);
  d.setUTCDate(d.getUTCDate() + 7);
  return d.toISOString().slice(0, 10);
}

/**
 * Een datum uit "2026-09-27", bewust in UTC. We rekenen hier alleen met hele
 * dagen, en in UTC bestaat er geen uur dat twee keer of niet voorkomt — bij een
 * zomeruurwissel zou een lokale datum stiekem een dag kunnen verschuiven.
 */
function alsDatum(dag: string): Date {
  const [jaar, maand, datum] = dag.split("-").map(Number);
  return new Date(Date.UTC(jaar, maand - 1, datum));
}

/** Hoe een dag eruitziet in een zin: "zaterdag 27 september". */
export function dagInWoorden(dag: string): string {
  return new Intl.DateTimeFormat("nl-BE", {
    timeZone: "UTC",
    weekday: "long",
    day: "numeric",
    month: "long",
  }).format(alsDatum(dag));
}
