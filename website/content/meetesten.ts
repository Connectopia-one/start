/*
  De pagina www.connectopia.one/meetesten.

  De gezinnen die thuisonderwijs geven, testen het oefenplatform al. Hier
  zoeken we er twee groepen bij, elk met hun eigen blik:
    - tieners die zelf examen doen bij de Examencommissie;
    - leerkrachten die tijdelijk onderwijs aan huis (TOAH) of bijles geven.

  Kim deelt deze pagina via twee posts op sociale media, in de groepen van
  de Examencommissie en in de groepen en vacaturepagina's van leerkrachten.
  De beelden staan in social/posts/bron/ onder "meetesten-examencommissie"
  en "meetesten-leerkrachten".

  Wat kan je hier aanpassen?
    open        zet op false als je genoeg testers hebt; het formulier
                verdwijnt dan en de zin bij "gesloten" komt in de plaats
    groepen     de twee kaders met wie we zoeken
    stappen     hoe het testen verloopt
    velden      de vragen op het formulier
*/

import type { Veld } from "@/content/formulier";

export const meetesten = {
  /* Staat het formulier open? */
  open: true,

  label: "Meetesten",
  titel: "Test ons oefenplatform mee",
  handgeschreven: "Wij geven je alles open, jij vertelt ons wat er beter kan",
  tekst:
    "Ons oefenplatform loopt van het 5de leerjaar tot het 6de middelbaar en groeit elke week. Gezinnen die thuisonderwijs geven, testen het al. Nu zoeken we er twee groepen bij die de leerstof van een heel andere kant bekijken. Je test een maand lang gratis, en wie daarna de evaluatie invult, krijgt een gratis jaarlicentie. Het aantal plaatsen is beperkt.",

  groepenTitel: "Wie we erbij zoeken",
  groepen: [
    {
      icoon: "🎓",
      kleur: "purple" as const,
      naam: "Tieners van de Examencommissie",
      voorWie: "Jij legt de examens zelf af",
      tekst:
        "De hoofdstukken van Boost en Beyond volgen de vakfiches van de Examencommissie. Jij weet als geen ander of dat klopt met wat je op je examen krijgt. Wat helpt je echt vooruit, en wat mist er nog?",
      punten: [
        "Oefen op je eigen tempo, zoveel je wil",
        "Zeg eerlijk wat te makkelijk, te moeilijk of onduidelijk is",
        "Vertel ons welke vakken we eerst moeten aanvullen",
      ],
    },
    {
      icoon: "📘",
      kleur: "blue" as const,
      naam: "Leerkrachten TOAH en bijles",
      voorWie: "Jij zit naast één leerling tegelijk",
      tekst:
        "Geef je tijdelijk onderwijs aan huis of bijles? Dan zie je elke week precies waar een leerling vastloopt. Die blik zoeken we: wat kan je gebruiken tijdens je uur, en wat zou jij anders doen?",
      punten: [
        "Gebruik het gratis bij de leerlingen die je begeleidt",
        "Zeg ons waar de uitleg te kort of te lang is",
        "Laat weten welke leerstof je mist voor jouw leerlingen",
      ],
    },
  ],

  stappenTitel: "Zo verloopt het",
  stappen: [
    {
      titel: "Je test een maand lang",
      tekst:
        "Een maand lang staat alles voor je open: alle niveaus, alle vakken, de leerbundels en de oefeningen. Je betaalt niets en er is geen opzeg.",
    },
    {
      titel: "Je vult de evaluatie in",
      tekst:
        "Op het einde van die maand vragen we je wat werkt, wat mist en wat beter kan. Je krijgt er een korte vragenlijst voor.",
    },
    {
      titel: "Je krijgt een jaar gratis",
      tekst:
        "Heb je je evaluatie ingediend, dan krijg je een gratis jaarlicentie. Een heel jaar toegang tot alles, zonder iets te betalen.",
    },
  ],

  /*
    Dit kader staat er met opzet streng in. Kim wil dat vooraf duidelijk is
    dat meetesten geen gratis toegang zonder meer is: wie niets laat weten,
    krijgt ook geen gratis jaar.
  */
  afspraakTitel: "Wat we van jou vragen",
  afspraakTekst:
    "Meetesten is geen gratis toegang zonder meer. We zetten alles voor je open omdat we je mening nodig hebben, dus we rekenen erop dat je er in die maand ook echt mee werkt.",
  afspraak: [
    "Werk er die maand echt mee, niet \u00e9\u00e9n keertje aan het begin",
    "Laat ons onderweg weten wat je opvalt, ook de kleine dingen",
    "Vul op het einde de evaluatie in; daar hangt je gratis jaar aan vast",
  ],

  /*
    Wie zich opgeeft maar niet gekozen wordt, mag niet met lege handen
    achterblijven. Daarom staan de prijzen er meteen bij.
    De tijdelijke prijs van 20 euro staat ook in oefenplatform/lib/prijs.ts;
    verandert die, pas dan allebei aan.
  */
  prijzenTitel: "Wil je nu al alles, en meteen voor een jaar?",
  prijzenTekst:
    "Dan hoef je niet te wachten tot we de testers kiezen. Zolang we volop bouwen, koop je een jaarlicentie voor 20 euro. Je maakt zelf een account aan op het oefenplatform en je kan meteen beginnen.",
  prijzenKnop: {
    tekst: "Maak een account aan",
    link: "https://oefenplatform.connectopia.one/registreren",
  },
  /* Voor wie eerst wil rondkijken voor hij iets aanmaakt. */
  prijzenLink: {
    tekst: "Of kijk eerst rond op het oefenplatform",
    link: "https://oefenplatform.connectopia.one",
  },
  prijzen: [
    {
      titel: "Nu, zolang we bouwen",
      tekst: "20 euro voor een heel jaar toegang tot alles.",
    },
    {
      titel: "Vanaf volgend schooljaar",
      tekst: "50 euro per gezin, voor 1 tot 5 personen.",
    },
    {
      titel: "Geef je tijdelijk onderwijs aan huis?",
      tekst: "Dan is het een licentie per leerkracht, voor maximaal 5 leerlingen.",
    },
  ],

  /* Het kader dat zegt waarom dit platform anders gemaakt is. */
  nuance: {
    titel: "Alles is door mensen geschreven",
    tekst:
      "In de oefeningen zit geen AI. Elke vraag, elke uitleg en elke leerbundel is door ons geschreven en nagelezen. Vind je toch een fout, dan zit er bij elk hoofdstuk een knop om het te melden, en wij schrijven je terug.",
  },

  formulierTitel: "Geef je op om mee te testen",
  formulierTekst:
    "Vink aan wat op jou past en laat je gegevens achter. We nemen contact op om je toegang in orde te brengen.",
  formulierPlaatsen:
    "Het aantal plaatsen is beperkt. Je hoort van ons of je erbij bent, en we laten het ook weten als het deze keer niet lukt.",
  onderwerp: "Aanmelding om mee te testen via de website",

  gesloten:
    "We hebben voorlopig genoeg testers. Heel erg bedankt aan iedereen die zich opgaf. Hou onze pagina's in de gaten, want we doen dit later opnieuw.",

  privacy:
    "We gebruiken deze gegevens enkel om je toegang te regelen en om je te vragen wat je van het platform vond. We geven ze niet door aan anderen. Wil je dat we ze verwijderen, laat het dan weten.",
};

export const meetestenVelden: Veld[] = [
  {
    naam: "Wie ben je",
    label: "Wie ben je?",
    soort: "keuzes",
    kolommen: 2,
    keuzes: [
      { naam: "Tiener Examencommissie", label: "Ik doe zelf examen bij de Examencommissie" },
      { naam: "Ouder van een tiener", label: "Ik ben de ouder van zo een tiener" },
      { naam: "Leerkracht TOAH", label: "Ik geef tijdelijk onderwijs aan huis" },
      { naam: "Bijlesleerkracht", label: "Ik geef bijles" },
    ],
  },
  {
    naam: "Naam",
    label: "Je naam",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "E-mailadres",
    label: "E-mailadres",
    soort: "email",
    verplicht: true,
    hulp: "Hierop bezorgen we je de toegang. Ben je jonger dan 16? Vul dan het adres van je ouder in.",
  },
  {
    naam: "Gsm-nummer",
    label: "Gsm-nummer",
    soort: "telefoon",
    hulp: "Mag leeg blijven. Handig als we iets snel willen vragen.",
  },
  {
    naam: "Welk niveau",
    label: "Welk niveau wil je testen?",
    soort: "tekst",
    verplicht: true,
    hulp: "Bijvoorbeeld 4de middelbaar doorstroom, 1ste middelbaar, of 6de leerjaar.",
  },
  {
    naam: "Welke vakken",
    label: "Welke vakken zijn voor jou het belangrijkst?",
    soort: "tekst",
    hulp: "Mag leeg blijven. Zo weten we waar we eerst aan verder werken.",
  },
  {
    naam: "Wat wil je ons laten weten",
    label: "Wil je ons nog iets laten weten?",
    soort: "lang",
    hulp: "Mag ook leeg blijven.",
  },
];
