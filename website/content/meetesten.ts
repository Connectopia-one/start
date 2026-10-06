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
  handgeschreven: "Wij bouwen, jij vertelt ons wat er beter kan",
  tekst:
    "Ons oefenplatform groeit elke week. Gezinnen die thuisonderwijs geven, testen het al. Nu zoeken we er twee groepen bij die de leerstof van een heel andere kant bekijken. Herken je jezelf hieronder? Dan mag je gratis mee testen.",

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
      titel: "Je krijgt alles open",
      tekst:
        "Alle niveaus, alle vakken, de leerbundels en de oefeningen. Je hoeft niets te betalen en er is geen opzeg.",
    },
    {
      titel: "Je laat ons weten wat je denkt",
      tekst:
        "Na een paar weken vragen we je kort wat werkt, wat mist en wat beter kan. In een mail of aan de telefoon, wat jij liever hebt.",
    },
    {
      titel: "Je houdt je toegang",
      tekst:
        "Wie ons zijn ervaring bezorgt, houdt gratis toegang tot het einde van het schooljaar 2026-2027.",
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
