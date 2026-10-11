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
  /* Wat er op de factuur komt, bijvoorbeeld "Les Young Engineers". Leeg = de
     soort. Het maandoverzicht telt alles met dezelfde regel samen. */
  factuurregel: string | null;
  /* Wat één keer meedoen kost, per kind. Leeg = geen bedrag berekenen. */
  prijs: number | null;
};

/* De kolommen die elk scherm van een activiteit nodig heeft. Eén keer hier,
   zodat er geen scherm achterblijft als er een veld bijkomt. */
export const ACTIVITEITVELDEN =
  "id, naam, soort, datum, plaats, archief, factuurregel, prijs";

/*
  De tekst waaronder deze activiteit op een factuur komt.

  Vijf dagen Young Engineers moeten samen één regel worden, dus de tekst mag
  niet uit de naam komen: die verschilt per dag. Daarom een eigen veld, met de
  soort als terugval zodat er altijd iets staat.
*/
export function factuurLabel(activiteit: {
  factuurregel?: string | null;
  soort: string;
}) {
  const regel = (activiteit.factuurregel ?? "").trim();
  if (regel) return regel;
  return activiteit.soort.charAt(0).toUpperCase() + activiteit.soort.slice(1);
}

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

/* ---------------------------------------------------------------
   Maanden. Het maandoverzicht staat in het webadres als 2026-10, zodat je
   een maand kan doorsturen en de knoppen vooruit en achteruit werken.
   --------------------------------------------------------------- */

const MAAND_PATROON = /^\d{4}-(0[1-9]|1[0-2])$/;

export function maandSleutel(datum = new Date()) {
  return `${datum.getFullYear()}-${String(datum.getMonth() + 1).padStart(2, "0")}`;
}

/* Een maand uit het webadres, of deze maand als er onzin in staat. */
export function leesMaand(waarde: string | undefined) {
  return waarde && MAAND_PATROON.test(waarde) ? waarde : maandSleutel();
}

/* De eerste en de laatste dag, als tekst, om op te vragen in de databank.
   Dag 0 van de volgende maand is de laatste dag van deze. */
export function maandGrenzen(sleutel: string) {
  const [jaar, maand] = sleutel.split("-").map(Number);
  const laatste = new Date(Date.UTC(jaar, maand, 0)).getUTCDate();
  return {
    van: `${sleutel}-01`,
    tot: `${sleutel}-${String(laatste).padStart(2, "0")}`,
  };
}

export function schuifMaand(sleutel: string, stappen: number) {
  const [jaar, maand] = sleutel.split("-").map(Number);
  const d = new Date(Date.UTC(jaar, maand - 1 + stappen, 1));
  return `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, "0")}`;
}

const MAANDNAMEN = [
  "januari",
  "februari",
  "maart",
  "april",
  "mei",
  "juni",
  "juli",
  "augustus",
  "september",
  "oktober",
  "november",
  "december",
];

export function maandNaam(sleutel: string) {
  const [jaar, maand] = sleutel.split("-").map(Number);
  return `${MAANDNAMEN[maand - 1]} ${jaar}`;
}

/* Een korte datum voor een lijst: 14 oktober. */
export function korteDatum(datum: string | null) {
  if (!datum) return "";
  const [jaar, maand, dag] = datum.split("-").map(Number);
  if (!jaar || !maand || !dag) return datum;
  return `${dag} ${MAANDNAMEN[maand - 1]}`;
}

/* 7 oktober 2026, voor in een zin. */
export function langeDatum(datum: string | null) {
  if (!datum) return "";
  const [jaar, maand, dag] = datum.split("-").map(Number);
  if (!jaar || !maand || !dag) return datum;
  return `${dag} ${MAANDNAMEN[maand - 1]} ${jaar}`;
}

/* Een bedrag zoals het hier geschreven wordt: 20,00 euro. toLocaleString met
   een munt hangt af van welke taalbestanden er op de server staan, en dat is
   niets om een factuurbedrag aan op te hangen. */
export function euro(bedrag: number) {
  return `${bedrag.toFixed(2).replace(".", ",")} euro`;
}
