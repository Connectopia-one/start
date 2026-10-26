/*
  De pagina "Leuke extra's" — /extras

  Spelletjes die naast de leerstof staan. Ze kleuren geen vinkje of sterretje
  van een hoofdstuk in en tellen voor geen enkel rapport mee: het is gewoon
  iets leuks om de begrippen mee in te oefenen, alleen of met de hele klas.

  Een spel bijzetten doe je in twee stappen:
  1. Zet het spel als één html-bestand in public/spellen/, bijvoorbeeld
     public/spellen/mijn-spel.html.
  2. Zet hieronder in `spellen` een blokje bij met dezelfde slug. De slug is
     het stukje van het webadres: /extras/mijn-spel.

  Alles hieronder is tekst, dus je mag hier gewoon in schrijven zonder dat er
  iets stuk kan.
*/

export type Spel = {
  slug: string;
  icoon: string;
  titel: string;
  vak: string;
  voorWie: string;
  tekst: string;
};

export const extrasTekst = {
  label: "Leuke extra's",
  titel: "Spelletjes naast de leerstof",
  intro:
    "Hier staan spelletjes die we zelf maakten om begrippen op een andere manier in te oefenen. Ze tellen nergens voor mee, er is geen score die bewaard wordt en je hebt er geen account voor nodig. Speel ze alleen, met het gezin of met de hele klas op het digibord.",
  volledigScherm: "Op volledig scherm openen",
  terug: "Terug naar de leuke extra's",
};

export const spellen: Spel[] = [
  {
    slug: "begrippenarena",
    icoon: "🏛️",
    titel: "Begrippenarena Geschiedenis",
    vak: "Geschiedenis",
    voorWie: "🌱 Start en ✨ Spark",
    tekst:
      "De begrippen uit de leerbundels van geschiedenis, in zes spellen: een quiz, memory, raad het begrip, tempeltje (galgje met een Griekse tempel), flitskaarten en begrippenbingo. Kies een hoofdstuk, speel alleen of in teams.",
  },
  {
    slug: "wiskunde-dimensie",
    icoon: "🤖",
    titel: "De Wiskunde-dimensie",
    vak: "Wiskunde",
    voorWie: "vier niveaus, van starter tot genie",
    tekst:
      "Een game van Mats. Robothond Tollie en kat Majol verslaan de monsters uit de anti-wiskunde-dimensie met plus en min, maal en delen en getallenreeksen. Wie veel goed heeft na elkaar, krijgt vanzelf moeilijkere sommen. Geen tijdslimiet.",
  },
];

export function vindSpel(slug: string) {
  return spellen.find((spel) => spel.slug === slug);
}
