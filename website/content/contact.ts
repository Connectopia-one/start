/*
  De contactpagina. Een ouder kiest hier zelf: meteen bellen, of het nummer
  achterlaten om teruggebeld te worden.

  De gewone vragen op het terugbelformulier staan niet hier maar in
  content/formulier.ts, bij "velden". Zo staan alle formuliervragen van de
  site op één plek. Hieronder staan alleen de twee vragen die alleen op dit
  formulier horen: wanneer we mogen bellen.
*/

import type { Veld } from "@/content/formulier";

/*
  Wanneer het best past om te bellen. Twee groepjes aankruisvakjes, en een
  ouder mag er zoveel aanvinken als hij wil. Wat niet aangevinkt is, komt
  ook niet in de aanvraag terecht.

  Wil je een dag of een moment toevoegen of weghalen? Zet er een regel bij
  of haal er een weg. De "naam" is wat er in Beheer bij de aanvraag komt te
  staan, het "label" is wat de ouder leest.
*/
export const terugbelVragen: Veld[] = [
  {
    naam: "Bellen op welke dagen",
    label: "Op welke dagen bellen we je het best?",
    soort: "keuzes",
    hulp: "Kruis er gerust meerdere aan, dan vinden we sneller een moment.",
    kolommen: 3,
    keuzes: [
      { naam: "Bellen op maandag", label: "Maandag" },
      { naam: "Bellen op dinsdag", label: "Dinsdag" },
      { naam: "Bellen op woensdag", label: "Woensdag" },
      { naam: "Bellen op donderdag", label: "Donderdag" },
      { naam: "Bellen op vrijdag", label: "Vrijdag" },
      { naam: "Bellen maakt niet uit welke dag", label: "Maakt niet uit" },
    ],
  },
  {
    naam: "Bellen op welk moment",
    label: "En wanneer op de dag?",
    soort: "keuzes",
    kolommen: 3,
    keuzes: [
      { naam: "Bellen overdag", label: "Overdag (9u tot 17u)" },
      { naam: "Bellen 's avonds", label: "'s Avonds (na 17u)" },
      { naam: "Bellen maakt niet uit welk uur", label: "Maakt niet uit" },
    ],
  },
];

export const contactTekst = {
  label: "Contact",
  titel: "Hoe wil je ons bereiken?",
  handgeschreven: "Je hoeft er niet alleen voor te staan.",
  tekst:
    "Zit je met een vraag over je kind, over ons aanbod of over waar je terecht kan? Bel ons gerust, of laat je nummer achter en wij bellen jou terug. Een eerste gesprek is gratis en je legt nergens iets mee vast.",

  bellen: {
    titel: "Meteen bellen",
    tekst:
      "Het snelst als je vraag dringend is of als je liever gewoon even praat.",
    knopTekst: "Bel",
  },

  terugbellen: {
    titel: "Word teruggebeld",
    tekst:
      "Laat je gegevens achter en we bellen je terug. Handig als het nu niet uitkomt.",
    knopTekst: "Naar het formulier",
    /* Dit is de titel boven het formulier verderop de pagina. */
    formulierTitel: "Wij bellen jou",
    formulierTekst:
      "Vul in hoe we je kunnen bereiken en waarover het gaat. Dan weten we vooraf al waar je mee zit en hoeven we je niets twee keer te vragen. Enkel je naam, je nummer en je mailadres zijn nodig; de rest mag je leeg laten.",
    onderwerp: "Terugbelverzoek via de website",
  },

  mailen: {
    titel: "Liever mailen?",
    tekst: "Dat mag ook. We antwoorden zo snel als we kunnen.",
  },

  /* Verdwijnt vanzelf als er in volgOns (content/site.ts) niets staat. */
  volgen: {
    titel: "Volg je ons al?",
    tekst:
      "Daar zetten we als eerste wanneer een kamp opengaat, waar we mee bezig zijn en wat de kinderen maken.",
  },
};
