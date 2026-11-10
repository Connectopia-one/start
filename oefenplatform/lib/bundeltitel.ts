import { NIVEAUS } from "@/lib/niveaus";

/*
  Gaat een nieuwe bundel in de plaats van een bundel die er al hangt? Dat mag
  enkel als het dezelfde bundel is: dezelfde titel, los van hoofdletters,
  accenten, leestekens en de naam van de categorie op het einde. Een
  oefenbundel ("Oefenbundel reële getallen …") is dus nooit dezelfde als de
  leerbundel ("Reële getallen …") van hetzelfde hoofdstuk.

  Zowel het formulier (het vinkje) als de server (wat er echt gewist wordt)
  gebruiken deze ene regel. Op 10 november 2026 wiste de server nog alles bij
  het hoofdstuk, en ging bij het opnieuw opladen van een leerbundel ook de
  oefenbundel ernaast weg.
*/

export function woorden(tekst: string): string[] {
  return tekst
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/\.[a-z0-9]+$/, "")
    .replace(/[^a-z0-9]+/g, " ")
    .split(" ")
    .filter((w) => w.length >= 3);
}

const NIVEAUWOORDEN = new Set(NIVEAUS.flatMap((n) => n.slug.split("-")));

/* Bundels die opgeladen zijn toen de naam van de categorie nog in de titel
   bleef hangen, heten nog "… boost doorstroom". Die woorden tellen niet mee. */
function kaal(titel: string): string {
  const w = woorden(titel);
  while (w.length > 1 && NIVEAUWOORDEN.has(w[w.length - 1])) w.pop();
  return w.join(" ");
}

export function zelfdeBundel(a: string, b: string): boolean {
  return kaal(a) === kaal(b);
}
