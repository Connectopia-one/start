/*
  De inschrijvings- en annuleringsvoorwaarden van de vakantiekampen, op
  /kampen/voorwaarden. Kim schreef ze op 3 november 2026: een plaats is pas
  zeker na betaling, met een duidelijke annuleringsregeling.

  Bij het inschrijven op /kampen/inschrijven vinkt de ouder aan dat die met
  deze voorwaarden akkoord gaat. Die zin staat hieronder bij `akkoord`.

  Iets veranderen? Pas de zinnen hieronder aan. Het rekeningnummer en de
  naam van de vzw komen uit content/kampen.ts, zodat ze maar op één plek
  staan.
*/

import { kampRegels } from "@/content/kampen";
import { site } from "@/content/site";

export const kampVoorwaarden = {
  label: "Vakantiekampen",
  titel: "Inschrijvings- en annuleringsvoorwaarden",
  handgeschreven: "Wie betaalt, heeft zijn plaats zeker.",
  tekst:
    "Een plaats in een kamp is pas definitief na betaling, en er geldt een duidelijke annuleringsregeling. Hieronder lees je hoe dat werkt.",

  waarom: {
    titel: "Waarom we dit doen",
    alineas: [
      "Onze kampen werken met kleine groepen, zodat elk kind de aandacht krijgt die het nodig heeft. Daardoor zijn de plaatsen beperkt.",
      "De laatste tijd zagen we jammer genoeg vaker dat kinderen ingeschreven werden en dan niet kwamen, of pas op het laatste moment afzegden. Die plaats bleef dan leeg, terwijl andere kinderen graag hadden willen meedoen.",
      "Om eerlijk te zijn voor iedereen werken we daarom vanaf nu zo: wie betaalt, heeft zijn plaats zeker.",
    ],
  },

  inschrijving: {
    titel: "Inschrijving en betaling",
    regels: [
      "Je inschrijving is definitief zodra we je betaling ontvangen hebben.",
      "Betaal liefst meteen na je inschrijving. Zolang de betaling niet binnen is, kunnen we de plaats niet vasthouden. Schrijven er intussen andere kinderen in die wel al betaald hebben, dan gaat de plaats naar hen.",
      "Is het kamp volzet, dan zetten we je kind graag op de wachtlijst. Komt er een plaats vrij, dan laten we het je meteen weten.",
      `Betalen kan via overschrijving op ${kampRegels.rekening} (${kampRegels.rekeninghouder}), met de mededeling die je na het inschrijven krijgt.`,
      "Heb je recht op een verhoogde tegemoetkoming? Dan betaal je de helft, zodra we het attest ontvangen hebben.",
    ],
  },

  annulering: {
    titel: "Annuleringsvoorwaarden",
    inleiding: `Kan je kind toch niet komen? Laat het ons zo snel mogelijk weten via ${site.email}. Dan kunnen we de plaats nog aan een ander kind geven.`,
    kolommen: ["Wanneer je annuleert", "Wat je betaalt"],
    rijen: [
      ["Tot 14 dagen voor de start van het kamp", "Niets, je krijgt alles terug"],
      ["Van 14 tot 7 dagen voor de start", "50% van de kampprijs"],
      [
        "Minder dan 7 dagen voor de start, of niet komen zonder te verwittigen",
        "De volledige kampprijs",
      ],
      ["Ziek, met doktersattest", "Het volledige bedrag als tegoed voor een volgend kamp"],
    ],
    slot: "Annuleren telt pas wanneer wij je bericht bevestigd hebben. Kreeg je geen bevestiging, bel of stuur ons dan even een berichtje.",
  },

  /* Het vinkje bij het inschrijven. */
  akkoord: "Ik ga akkoord met de inschrijvings- en annuleringsvoorwaarden",
  akkoordLink: "Lees de voorwaarden",
};
