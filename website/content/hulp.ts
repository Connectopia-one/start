/*
  De pagina Hulp en advies: alles wat met zoeken, uitzoeken en bijleren te
  maken heeft, bij elkaar.

  Kim op 14 oktober 2026: "niet iedereen wilt direct de wegwijzer, al veel
  zijn die stap voorbij en zoeken nu al direct naar tips." Daarom is de
  wegwijzer hier één tegel tussen de andere en geen verplichte eerste stap.

  Een tegel bijzetten of de volgorde veranderen doe je hieronder; de pagina
  past zich vanzelf aan.
*/

import type { Kleur } from "@/content/site";

export const hulpTekst = {
  label: "Hulp, advies en tips",
  titel: "Wat zoek je?",
  handgeschreven: "Je hoeft niet bij het begin te beginnen.",
  tekst:
    "Sta je nog bij het eerste vermoeden, of ben je die stap al lang voorbij en zoek je gewoon iets dat werkt? Alles staat hier naast elkaar. Kies maar waar je nu nood aan hebt.",
};

export type HulpTegel = {
  titel: string;
  tekst: string;
  icoon: string;
  kleur: Kleur;
  link: string;
};

export const hulpTegels: HulpTegel[] = [
  {
    titel: "Wegwijzer voor ouders",
    tekst:
      "Stap voor stap, van het eerste vermoeden tot ver na de diagnose. Met wat je kan doen in elke stap.",
    icoon: "🗺️",
    kleur: "blue",
    link: "/wegwijzer",
  },
  {
    titel: "Observatielijst",
    tekst:
      "Zet op papier wat je bij je kind ziet, om mee te nemen naar school of naar een gesprek.",
    icoon: "📋",
    kleur: "orange",
    link: "/observatielijst",
  },
  {
    titel: "Thuisonderwijs en de Examencommissie",
    tekst:
      "In gewone taal uitgelegd: wat huisonderwijs is, welke examens erbij horen, en wat kan terwijl je kind gewoon naar school gaat.",
    icoon: "🏡",
    kleur: "green",
    link: "/thuisonderwijs",
  },
  {
    titel: "Waar kan je terecht",
    tekst:
      "Psychologen, logopedisten, coaches en bijlesleerkrachten die we kennen en vertrouwen, ook bij dubbele diagnoses.",
    icoon: "🧭",
    kleur: "purple",
    link: "/waar-kan-je-terecht",
  },
  {
    titel: "Blog, tips en meer",
    tekst:
      "Onze eigen stukken en die van partners, over opvoeden, school, diagnoses en alles wat ouders bezighoudt.",
    icoon: "📰",
    kleur: "green",
    link: "/blog",
  },
  {
    titel: "Prikbord voor ouders",
    tekst:
      "Zoekertjes, samenkomsten, aanraders en mooie momenten van andere ouders. Je mag er zelf een briefje ophangen.",
    icoon: "📌",
    kleur: "purple",
    link: "/prikbord",
  },
  {
    titel: "Filmpjes en artikels die we delen",
    tekst:
      "Wat ouders en wij tegenkomen over hoogbegaafdheid, autisme en ADHD, en de moeite vinden om door te geven.",
    icoon: "▶️",
    kleur: "orange",
    link: "/in-de-kijker",
  },
];

/* De uitnodiging onderaan: wie er niet uit raakt, mag het gewoon vragen. */
export const hulpSlot = {
  titel: "Raak je er niet uit?",
  tekst:
    "Stuur ons gerust een berichtje met waar je vastzit. We denken mee en verwijzen je door als iemand anders je beter kan helpen. We stellen zelf geen diagnoses.",
  knop: "Stel je vraag",
  link: "/contact",
};
