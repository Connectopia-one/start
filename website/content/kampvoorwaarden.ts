/*
  De inschrijvings- en annuleringsvoorwaarden van de vakantiekampen, op
  /kampen/voorwaarden. Kim schreef ze op 3 november 2026: een plaats is pas
  zeker na betaling, met een duidelijke annuleringsregeling. Op 5 november
  2026 herschreef Kim de annulering: geen terugbetaling bij annuleren of niet
  komen, behalve met een doktersbriefje of in een ernstige situatie.

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
    "Een plaats in een kamp is pas gereserveerd na betaling. Annuleer je of komt je kind niet, dan betalen we niets terug, behalve met een doktersbriefje of in een ernstige situatie. Hieronder lees je hoe dat werkt.",

  /* De korte zin bij het inschrijfformulier, op de bedankpagina en op de
     pagina Aanbod. */
  kort: "Je plaats is zeker zodra je betaling binnen is. Annuleren of niet komen wordt niet terugbetaald, behalve met een doktersbriefje of in een ernstige situatie.",

  waarom: {
    titel: "Waarom we dit doen",
    alineas: [
      "We werken in heel kleine groepen, zodat elk kind de aandacht krijgt die het nodig heeft. Daardoor telt elke plaats.",
      "Blijft een plaats leeg omdat een kind niet komt, dan kan er geen ander kind meer meedoen, terwijl er vaak kinderen op de wachtlijst staan. De begeleiding en het materiaal zijn dan ook al voorzien.",
      "Om eerlijk te zijn voor iedereen werken we daarom zo: wie betaalt, heeft zijn plaats zeker.",
    ],
  },

  inschrijving: {
    titel: "Inschrijving en betaling",
    regels: [
      "Je plaats is pas gereserveerd zodra we je betaling ontvangen hebben.",
      "Betaal liefst meteen na je inschrijving. Zolang de betaling niet binnen is, kunnen we de plaats niet vasthouden. Schrijven er intussen andere kinderen in die wel al betaald hebben, dan gaat de plaats naar hen.",
      "Is het kamp volzet, dan zetten we je kind graag op de wachtlijst. Komt er een plaats vrij, dan laten we het je meteen weten.",
      `Betalen kan via overschrijving op ${kampRegels.rekening} (${kampRegels.rekeninghouder}), met de mededeling die je na het inschrijven krijgt.`,
      "Heb je recht op een verhoogde tegemoetkoming? Dan betaal je de helft, zodra we het attest ontvangen hebben.",
    ],
  },

  annulering: {
    titel: "Annuleringsvoorwaarden",
    inleiding: `Kan je kind toch niet komen? Laat het ons zo snel mogelijk weten via ${site.email}.`,
    kolommen: ["Wat er gebeurt", "Wat je terugkrijgt"],
    rijen: [
      ["Je annuleert, op welk moment ook", "Geen terugbetaling"],
      ["Je kind komt niet opdagen", "Geen terugbetaling"],
      [
        "Je kind is ziek en je bezorgt ons een doktersbriefje",
        "Het bedrag voor de dagen die je kind gemist heeft",
      ],
      [
        "Er is een ernstige situatie, zoals een ongeval of een overlijden in de familie",
        "Neem contact met ons op, dan zoeken we samen een oplossing",
      ],
    ],
    slot: "Bezorg het doktersbriefje zo snel mogelijk via mail. Annuleren telt pas wanneer wij je bericht bevestigd hebben. Kreeg je geen bevestiging, bel of stuur ons dan even een berichtje.",
  },

  /* Het vinkje bij het inschrijven. */
  akkoord: "Ik ga akkoord met de inschrijvings- en annuleringsvoorwaarden",
  akkoordLink: "Lees de voorwaarden",
};
