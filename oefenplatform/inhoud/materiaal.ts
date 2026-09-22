/*
  De pagina "Handig materiaal" — /materiaal

  Een gratis verzamelplek voor links en documenten: vakfiches, naslagwerken,
  interactieve tabellen, oefensites. Iedereen kan die pagina zien, ook wie geen
  account heeft en wie niet betaald heeft. Dat is met opzet: het is een extra
  dienst, geen onderdeel van het betalende aanbod.

  De links zelf staan NIET in dit bestand. Die voeg je toe op /beheer/materiaal,
  net zoals je op het ouderportaal lesmateriaal bij een klasje zet: titel, een
  link of een pdf, en de kop waaronder het hoort. Verwijderen kan daar ook.

  Hieronder staan enkel de vaste teksten van de pagina — de inleiding, de nota
  onderaan en de knop. Die mag je gerust aanpassen.
*/

export const materiaalTekst = {
  label: "Handig materiaal",
  titel: "Links die we zelf gebruiken",
  intro:
    "Hier verzamelen we online materiaal dat ons en onze kinderen verder helpt: officiële vakfiches, naslagwerken, interactieve tabellen en oefensites. Alles op deze pagina is gratis te gebruiken en staat los van een account of een abonnement.",
  nota:
    "Deze lijst groeit mee. Ken je iets wat hier thuishoort, of werkt een link niet meer? Laat het ons weten, dan zetten we het erbij.",
  /* Wat er staat zolang er nog niets toegevoegd is. */
  leegTekst: "Hier komt binnenkort materiaal bij.",
  /* De knop onderaan. Laat de link leeg om de knop te verbergen. */
  oproepTekst: "Een link doorgeven",
  oproepLink: "https://www.connectopia.one/contact",
  /* Waarschuwing bij het verlaten van ons platform. */
  externNota:
    "Deze links brengen je naar websites van anderen. Wij maken of beheren dat materiaal niet, en er kan reclame op staan.",
};

/*
  Voorstellen voor de kop bij het toevoegen. Je hoeft je hier niet aan te
  houden: typ gewoon een eigen kop en die verschijnt vanzelf op de pagina.
  De koppen staan op de pagina in de volgorde waarin je de eerste link van die
  kop toegevoegd hebt.
*/
export const materiaalGroepSuggesties = [
  "Officiële leerstof",
  "Wiskunde",
  "Wetenschap en techniek",
  "Talen",
  "Mens en maatschappij",
  "Oefenen en spelen",
];
