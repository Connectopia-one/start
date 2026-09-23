/* De teksten van de startpagina. */

export const home = {
  hero: {
    titel: "Jouw kompas bij hoogbegaafdheid,",
    titelAccent: "ASS & ADHD",
    handgeschreven: "Iedereen is welkom, wij denken graag met je mee.",
    tekst:
      "We verbinden kinderen aan peers en ouders aan de juiste experts. Van naschoolse activiteiten tot pluswerkingen, alles op maat en in kleine groepjes.",
    knopPrimair: { tekst: "Start de wegwijzer", link: "/wegwijzer" },
    knopTweede: { tekst: "Bekijk ons aanbod", link: "/aanbod" },
  },

  /*
    De brede foto onder de titel bovenaan.
    Zet het bestand in  public/fotos/  en vul hier de naam in.
    Wil je even geen foto?  foto: null,
  */
  foto: {
    bestand: "startpagina.jpg",
    beschrijving:
      "Kinderen werken aan een lange tafel met laptops en boeken, een begeleidster kijkt mee.",
  },

  /* Het kaartje rechts in de hero: vier snelle ingangen. */
  kiesJeRichting: {
    titel: "Waar wil je naartoe?",
    keuzes: [
      {
        tekst: "Ik vermoed iets bij mijn kind",
        link: "/wegwijzer",
        kleur: "green",
      },
      {
        tekst: "Ik zoek een kamp of traject",
        link: "/aanbod",
        kleur: "orange",
      },
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
    ] as const,
  },

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
    watwedoen: {
      label: "Wat we doen",
      titel: "Drie wegen, elk één klik van hier",
      tekst:
        "Wie we zijn, wat we zelf organiseren, en waar je terecht kan als je verder wil zoeken.",
    },
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
    De band voor professionals, onderaan de startpagina.
    Hij nodigt uit, hij houdt niemand tegen: wie gewoon de site wil
    bekijken, scrolt er voorbij.
  */
  professionalsBand: {
    label: "Voor professionals",
    titel: "Ben je een professional?",
    tekst:
      "Kinesist, logopedist, coach, auticoach, arts of begeleider: we bezorgen je graag folders, een poster voor je wachtzaal of flyers om uit te delen. En wie met deze kinderen werkt, mag in onze wegwijzer staan.",
    knop: "Ik werk met deze kinderen",
    link: "/professionals",
  },
};
