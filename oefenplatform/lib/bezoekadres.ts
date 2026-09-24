/*
  Een nummer uit de databank: acht-vier-vier-vier-twaalf tekens, zoals
  3f6b1c8a-9d2e-4a77-b1c0-5e8d9a2f4c31. Zo ziet elk kindnummer en elk
  hoofdstuknummer in dit platform eruit.
*/
const NUMMER = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

/**
 * Haalt uit een webadres alles wat over één bepaald kind gaat, voor het naar
 * de bezoekersteller vertrekt. Zie components/Bezoekersteller.tsx.
 *
 * In `/begeleiding/3f6b1c8a-…/testen/9d2e4a77-…` zit het nummer van een kind.
 * Dat nummer zegt op zichzelf niets, maar samen met de rest van een bezoek zou
 * het wel het spoor van één kind worden, en dat hoort nergens buiten onze eigen
 * databank thuis. Elk stuk dat eruitziet als zo'n nummer wordt daarom een
 * streepje, zodat er `/begeleiding/-/testen/-` overblijft: genoeg om te tellen
 * hoe vaak zo'n pagina bekeken wordt, te weinig om iemand te volgen.
 *
 * Alles achter het vraagteken gaat er ook af. Daar staan dingen als de code uit
 * een mail om een wachtwoord opnieuw in te stellen.
 */
export function zonderPersoonlijkeStukken(webadres: string): string {
  const [pad] = webadres.split("?");
  return pad
    .split("#")[0]
    .split("/")
    .map((stuk) => (NUMMER.test(stuk) ? "-" : stuk))
    .join("/");
}
