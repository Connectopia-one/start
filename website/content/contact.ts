/*
  De contactpagina. Een ouder kiest hier zelf: meteen bellen, of het nummer
  achterlaten om teruggebeld te worden.

  De vragen op het terugbelformulier staan niet hier maar in
  content/formulier.ts, bij "velden". Zo staan alle formuliervragen van de
  site op één plek.
*/

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
};
