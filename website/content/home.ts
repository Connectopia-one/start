/* De teksten van de startpagina. */

export const home = {
  /*
    De bovenkant van de startpagina: twee deuren.

    Kim op 14 oktober 2026: "ik denk dat we de gewone kinderen afschrikken en
    hun ouders om naar de kampen en hobby's te komen omdat het eerste wat ze
    zien is ass en adhd en hoogbegaafdheid. (...) net dat is wat niet de
    bedoeling is, we maken gewoon iets wat voor iedereen past, anders ben je
    nog steeds een apart aanbod te creeren en kinderen op te splitsen."

    Daarom staat er geen omschrijving meer bovenaan waarin een bezoeker zich
    moet herkennen, maar een vraag met twee deuren. De diagnoses staan achter
    de tweede deur, als aanbod en niet als toegangsvoorwaarde.
  */
  hero: {
    titel: "Waar ben je naar op zoek?",
    handgeschreven: "Iedereen is welkom, met of zonder diagnose.",
    tekst:
      "Connectopia vzw brengt kinderen samen in kleine groepjes en helpt ouders hun weg vinden, in Hasselt en Genk.",
    deuren: [
      {
        icoon: "🔧",
        kleur: "green",
        titel: "Een activiteit voor mijn kind",
        tekst:
          "Kampen in elke vakantie, de Ontdekclub, Young Engineers, de plusklas en de pluswerking. Voor élk kind, in kleine groepjes, prikkelarm en op maat.",
        knop: "Bekijk ons aanbod",
        link: "/aanbod",
      },
      {
        icoon: "🧭",
        kleur: "purple",
        titel: "Hulp, advies en tips",
        tekst:
          "Over hoogbegaafdheid, UHB, ASS, ADHD, thuisonderwijs en de Examencommissie. De wegwijzer, de observatielijst, tips van andere ouders en wat we delen, alles bij elkaar.",
        knop: "Naar hulp en advies",
        link: "/hulp-en-advies",
      },
      {
        icoon: "🌱",
        kleur: "blue",
        titel: "Wie is Connectopia",
        tekst:
          "Ons verhaal, onze kernwaarden en het team achter de werking. Ervaringsdeskundigen met een netwerk van wél-specialisten.",
        knop: "Lees ons verhaal",
        link: "/over-ons",
      },
    ] as const,
  },

  /* De kleine lijntjes onder de twee deuren: wie gewoon binnen wil. */
  kleineLinks: [
    {
      tekst: "Ik zoek een psycholoog of begeleider",
      link: "/waar-kan-je-terecht",
      kleur: "purple",
    },
    {
      tekst: "Ik wil naar het ouderportaal",
      link: "/ouderportaal",
      kleur: "blue",
    },
    {
      tekst: "Naar het oefenplatform",
      link: "/oefenplatform",
      kleur: "orange",
    },
  ] as const,

  /*
    De brede foto onder de titel bovenaan.
    Zet het bestand in  public/fotos/  en vul hier de naam in.
    Wil je even geen foto?  foto: null,
  */
  foto: {
    bestand: "startpagina-plusklas.jpg",
    beschrijving:
      "Drie kinderen van de plusklas aan een tafel met een laptop en een open boek; twee jongens werken samen op de laptop.",
  },

  /*
    Het ronde knopje rechtsboven op de startpagina.
    Kim op 21 oktober 2026: "kan er vanvoor op de homepagina 1 klein rond
    knopje met Wil je ons steunen ? dat linkt naar de steun ons pagina."
    Zet op null als je het knopje even niet wil tonen:  steunKnop: null,
  */
  steunKnop: { tekst: "Wil je ons steunen?", link: "/steun-ons" },

  /*
    De groene balk onder de hero.
    Zet op null als je even geen aankondiging wil tonen:  aankondiging: null,
  */
  aankondiging: {
    tekst:
      "Officieel een vzw! Vanaf schooljaar 2026–2027 verlagen we onze prijzen.",
    handgeschreven: "En dat vieren we, samen met jullie",
    link: { tekst: "Bekijk de nieuwe tarieven", href: "/aanbod" },
  },

  blokken: {
    platform: {
      label: "Voor onze gezinnen",
      titel: "Direct naar jouw plek",
      tekst: "Voor ouders en kinderen die al bij ons ingeschreven zijn.",
    },
    kennis: {
      label: "Lezen en bijleren",
      titel: "Ons levende archief",
      tekst: "",
    },
  },

  /* Het tweede kaartje in het blok "Lezen en bijleren". */
  partnerBlok: {
    icoon: "🤝",
    titel: "Zelf iets delen?",
    omschrijving:
      "Ben je professional of partnerorganisatie en wil je een artikel bijdragen of in de gids staan? We horen het graag.",
    linkTekst: "Laat het weten",
    link: "/professionals",
  },

  /*
    In de kijker: filmpjes, artikels en berichten die we delen over
    hoogbegaafdheid, autisme en ADHD. De band staat er vooral om mensen te
    laten weten dat ze er zelf een mogen bijzetten; de pagina vult zich
    daarmee.
  */
  kijkerBand: {
    label: "In de kijker",
    titel: "Kwam jij iets goeds tegen?",
    tekst:
      "Filmpjes, artikels en berichten over hoogbegaafdheid, autisme, ADHD of een combinatie daarvan, bij elkaar op één pagina. Zag jij iets dat anderen moeten zien? Stuur het in, dan zetten we het erbij.",
    knop: "Naar In de kijker",
    link: "/in-de-kijker",
  },
  professionalsBand: {
    label: "Voor professionals",
    titel: "Ben je een professional?",
    tekst:
      "Kinesist, logopedist, coach, auticoach, arts of begeleider: we bezorgen je graag folders, een poster voor je wachtzaal of flyers om uit te delen. En wie met deze kinderen werkt, mag in onze gids Waar kan je terecht staan.",
    knop: "Ik werk met deze kinderen",
    link: "/professionals",
  },
};
