/*
  De pagina Tips voor de klas: voor leerkrachten, leerondersteuners en
  zorgcoördinatoren. Kim op 26 oktober 2026, in haar eigen woorden: "dit noem
  ik dus ook structuur en ook duidelijke omkadering maar vloeiend."

  Een tip bijzetten: voeg onderaan in de lijst tips een blok toe. Het nummer
  ervoor komt vanzelf.
*/

import type { Kleur } from "@/content/site";

export const leerkrachtenTekst = {
  label: "Hulp, advies en tips",
  titel: "Tips voor de klas",
  handgeschreven: "Structuur mag vloeiend zijn.",
  tekst:
    "Voor leerkrachten, leerondersteuners en zorgcoördinatoren die een kind met hoogbegaafdheid, autisme of ADHD in de klas hebben, of een kind waarbij ze dat vermoeden. Kort uitgelegd, met wat wij in onze werking elke dag zien werken.",
};

export type Uitleg = {
  titel: string;
  tekst: string;
  icoon: string;
  kleur: Kleur;
};

export const uitlegTitel = "Eerst in het kort";

export const uitleg: Uitleg[] = [
  {
    titel: "HB en UHB",
    tekst:
      "Hoogbegaafd (HB) betekent meer dan slim zijn. Deze kinderen denken snel, gelaagd en diep, willen tot op de bodem gaan en voelen vaak ook intens. Uiterst hoogbegaafd (UHB) gaat daar nog een stap verder in. Het zegt niets over hoe goed een kind het op school doet: ook een kind met lage punten kan hoogbegaafd zijn.",
    icoon: "💡",
    kleur: "purple",
  },
  {
    titel: "De overlap met autisme en ADHD",
    tekst:
      "Hoogbegaafdheid komt geregeld samen voor met autisme (ASS) of ADHD. Dan verstoppen ze elkaar vaak: het kind compenseert zijn moeilijkheden met zijn verstand, of de begaafdheid valt niet op omdat iedereen naar het gedrag kijkt. Wat eruitziet als koppigheid of onrust, kan dus iets heel anders zijn.",
    icoon: "🧩",
    kleur: "orange",
  },
  {
    titel: "Een disharmonisch profiel",
    tekst:
      "Deze kinderen ontwikkelen zich zelden overal even snel. Op het ene vlak denken ze als een volwassene, op het andere hebben ze de steun nodig die bij hun leeftijd past, of zelfs meer. Dat is geen tegenspraak. Het betekent dat je per vlak moet kijken wat een kind nodig heeft.",
    icoon: "📊",
    kleur: "green",
  },
];

export type Tip = {
  titel: string;
  tekst: string[];
  /* Een zin die je zo kan gebruiken, in een kader onder de tip. */
  zin?: string;
};

export const tipsTitel = "Wat werkt in de klas";

export const tips: Tip[] = [
  {
    titel: "Geef structuur, maar maak ze vloeiend",
    tekst: [
      "Een vaste omkadering is heel belangrijk, zeker bij autisme. Maar hoe strakker het regime, hoe moeilijker een kind zich aanpast als het toch anders loopt. Een agenda die tot op de minuut vastligt, botst hard terug wanneer de planning door omstandigheden moet wijzigen.",
      "Werk daarom met een planning die je kan verhangen, zoals post-its op een bord. Het kind ziet nog altijd duidelijk wat er komt, en leert tegelijk dat een stap van plaats kan veranderen zonder dat alles instort. Dat is ook structuur en duidelijke omkadering, alleen vloeiend.",
    ],
  },
  {
    titel: "Leg uit, en zeg ook waarom",
    tekst: [
      "Een kind met HB, UHB of autisme wil echt weten waarom iets zo is. Een \"daarom\" wordt niet snel aanvaard, en dat is geen brutaliteit.",
      "Geef kort en duidelijk wat je verwacht en wat er gaat gebeuren. Laat daarna ruimte voor de waarom-vraag, en antwoord er zo duidelijk en eerlijk mogelijk op.",
    ],
  },
  {
    titel: "Parkeer de vraag van het sneltreinhoofd",
    tekst: [
      "Hoogbegaafde kinderen zijn in hun hoofd vaak al een paar stations verder. Hun vraag is dan echt interessant, maar hoort niet bij de opdracht van nu.",
      "Parkeer die vraag: schrijf ze op of zet er een sterretje bij, werk eerst af waar jullie mee bezig waren, en kom er daarna op terug. Doe dat dan ook echt, en ga er gerust uitgebreid op in. Zo voelt het kind zich gehoord, leert het bij het onderwerp te blijven, en weet het dat zijn vragen altijd welkom zijn, op het gepaste moment.",
    ],
    zin: "Topvraag! Maar dit is even niet waar we nu mee bezig zijn. Ik schrijf hem op en we komen er tijdens de pauze op terug.",
  },
];

/* Onderaan: waar ze verder mee kunnen. */
export const leerkrachtenSlot = {
  titel: "Samen verder kijken?",
  tekst:
    "Wij gaan graag in gesprek met de school, als ouders dat willen. Heb je zelf een vraag over een kind in je klas, stuur ons gerust een berichtje. We denken mee en verwijzen door als iemand anders beter kan helpen. We stellen zelf geen diagnoses.",
  links: [
    { tekst: "Stel je vraag", href: "/contact" },
    { tekst: "Voor professionals", href: "/professionals" },
    { tekst: "Observatielijst", href: "/observatielijst" },
  ],
};
