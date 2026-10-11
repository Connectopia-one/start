/*
  Een woordje bovenaan een categorie, boven de vakknoppen.

  Alles hier is gewone tekst. De sleutel is de categorie zoals ze in het
  webadres staat, bijvoorbeeld /niveaus/beyond-doorstroom wordt
  "beyond-doorstroom". Staat er voor een categorie niets, dan toont de pagina
  gewoon geen kadertje. Een noot bij één vak zet je in vaknoten.ts.

  Waarom dit bestaat: Febe, een tester, vroeg op 9 oktober 2026 waar haar
  richting stond. Ze volgt welzijnswetenschappen, en dat is doorstroom
  domeingebonden; bij ons staat enkel doorstroom en dubbele finaliteit. Je kan
  dat niet raden van buitenaf, dus staat het er nu bij.

  Waarom het uit stukken bestaat in plaats van uit één alinea: Kim las de noot
  van 🌍 Beyond doorstroom op 11 oktober 2026 terug en zei "dit is heel veel
  tekst maar vind het echt niet duidelijk". Er stonden vier boodschappen in één
  blok: voor wie het is, welke richtingen dat zijn, wat je bij wetenschappen
  kiest, en wat er nog niet af is. Elk van die vier heeft nu zijn eigen plek, en
  de lange opsomming van richtingen zit achter een klikje.

  Hou elk stuk kort. Eén zin in `kop`, één zin per punt, en zet alles wat niet
  meteen nodig is in `richtingen` (dat staat dichtgeklapt).
*/

export type Richtinggroep = {
  /** Bijvoorbeeld "Domeinoverschrijdend". */
  kop: string;
  /** De richtingen zelf, één per regel op het scherm. */
  lijst: string[];
};

export type Categorienoot = {
  /** Eén zin: voor wie zijn deze vakken? */
  kop: string;
  /** Korte weetjes, elk met een vet woord vooraan. */
  punten?: { kop: string; tekst: string }[];
  /** De volledige lijst richtingen, dichtgeklapt achter een klikje. */
  richtingen?: {
    /** De tekst op het klikje zelf. */
    klik: string;
    groepen: Richtinggroep[];
    /** Eén zin eronder, bijvoorbeeld waarom ze niet apart staan. */
    slot?: string;
  };
  /** Wat er nog niet is, in één zin. */
  komtNog?: string;
};

export const categorienoten: Record<string, Categorienoot> = {
  // Nageteld op 11 oktober 2026 tegen inhoud/boost-doorstroom/ (veertien
  // vakken). Welke richting welke wiskunde en welke natuurwetenschappen volgt,
  // staat bovenaan op de fiches zelf; zie de docstrings van
  // bron/bouw_wiskunde.py en bron/bouw_natuurwetenschappen.py.
  "boost-doorstroom": {
    kop:
      "Deze vakken gelden voor de vijf doorstroomrichtingen van de tweede " +
      "graad.",
    punten: [
      {
        kop: "Wetenschappen",
        tekst:
          "Leg je ze in één examen af: natuurwetenschappen. Leg je er drie " +
          "af: biologie, chemie en fysica.",
      },
      {
        kop: "Wiskunde",
        tekst:
          "Humane wetenschappen volgt wiskunde basis, de vier andere " +
          "richtingen wiskunde gevorderd. Dat staat ook op je vakfiche.",
      },
      {
        kop: "Economische en humane wetenschappen",
        tekst:
          "Jouw fiche natuurwetenschappen is de kortere van de twee, dus dat " +
          "vak is hier iets ruimer dan wat jij moet kennen.",
      },
    ],
    richtingen: {
      klik: "Staat mijn richting hierbij?",
      groepen: [
        {
          kop: "Doorstroom, tweede graad",
          lijst: [
            "economische wetenschappen",
            "humane wetenschappen",
            "Latijn",
            "moderne talen",
            "natuurwetenschappen",
          ],
        },
      ],
      slot:
        "De vakfiches van de Examencommissie noemen die richtingen samen " +
        "bovenaan, daarom staan ze hier niet apart.",
    },
    komtNog: "Nog in de maak: Latijn en Duits.",
  },

  // De elf fiches van deze categorie zijn alle elf gebouwd (stand 11 oktober
  // 2026), dus hier hoort geen komtNog. Welke vier vakken bij welke richting
  // horen, staat in de docstrings van bron/bouw_*.py.
  "boost-dubbele-finaliteit": {
    kop:
      "Deze vakken gelden voor de dubbele finaliteit van de tweede graad. " +
      "Zeven ervan zijn voor allebei de richtingen.",
    punten: [
      {
        kop: "Bedrijf en organisatie",
        tekst:
          "Daarbovenop zijn economie en bedrijfswetenschappen en toegepaste " +
          "economie voor jou.",
      },
      {
        kop: "Maatschappij en welzijn",
        tekst:
          "Daarbovenop zijn gezondheid, zorg en welzijn en ontwikkeling en " +
          "pedagogisch handelen voor jou.",
      },
    ],
  },

  // Zeven vakken, en dat zijn precies de vakken van de basisvorming. De
  // richtingsvakken van commerciële organisatie bestaan nog niet; zie
  // connectopia-beyond-structuur in memory.
  "beyond-dubbele-finaliteit": {
    kop:
      "Deze vakken zijn de basisvorming van de dubbele finaliteit van de " +
      "derde graad: ze gelden voor elke richting.",
    punten: [
      {
        kop: "Commerciële organisatie",
        tekst:
          "De vakken die enkel bij jouw richting horen, staan er nog niet. " +
          "De basisvorming hieronder is wel al voor jou.",
      },
    ],
    komtNog: "Nog in de maak: de richtingsvakken van commerciële organisatie.",
  },

  "beyond-doorstroom": {
    kop:
      "Deze vakken gelden voor alle doorstroomrichtingen van de derde graad, " +
      "domeinoverschrijdend én domeingebonden.",
    punten: [
      {
        kop: "Wetenschappen",
        tekst:
          "Leg je ze in één examen af: natuurwetenschappen. Leg je er drie " +
          "af: biologie, chemie en fysica.",
      },
      {
        kop: "Wiskunde",
        tekst:
          "Hier staat enkel wiskunde gevorderd. Humane wetenschappen, moderne " +
          "talen en Latijn-moderne talen volgen wiskunde basis, en dat vak is " +
          "nog in de maak.",
      },
      {
        kop: "Bedrijfswetenschappen en welzijnswetenschappen",
        tekst:
          "Jullie wiskunde en natuurwetenschappen volgen een eigen vakfiche " +
          "en staan er nog niet. De rest geldt wel voor jullie.",
      },
    ],
    richtingen: {
      klik: "Staat mijn richting hierbij?",
      groepen: [
        {
          kop: "Domeinoverschrijdend",
          lijst: [
            "economie-wiskunde",
            "humane wetenschappen",
            "Latijn-moderne talen",
            "Latijn-wiskunde",
            "moderne talen",
            "wetenschappen-wiskunde",
          ],
        },
        {
          kop: "Domeingebonden",
          lijst: ["bedrijfswetenschappen", "welzijnswetenschappen"],
        },
      ],
      slot:
        "De vakfiches van de Examencommissie noemen die richtingen samen " +
        "bovenaan, daarom staan ze hier niet apart.",
    },
    // Nageteld op 11 oktober 2026 tegen inhoud/beyond/ (veertien vakken).
    // Kim merkte op dat sociale en gedragswetenschappen, filosofie en recht en
    // samenleving en economie er intussen wél stonden. Tel dit dus na in de map
    // in plaats van de zin van de vorige keer over te nemen.
    komtNog:
      "Nog in de maak: Latijn, wiskunde basis, algemene economie, " +
      "bedrijfswetenschappen en recht, en de eigen wiskunde en " +
      "natuurwetenschappen van bedrijfswetenschappen en welzijnswetenschappen.",
  },
};

/** De noot bij deze categorie, of niets. */
export function vindCategorienoot(niveau: string): Categorienoot | undefined {
  return categorienoten[niveau];
}
