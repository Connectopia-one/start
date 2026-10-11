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
  "boost-doorstroom": {
    kop:
      "Deze vakken gelden voor alle doorstroomrichtingen van de tweede graad, " +
      "domeinoverschrijdend én domeingebonden.",
    punten: [
      {
        kop: "Wetenschappen",
        tekst:
          "Leg je ze in één examen af, neem dan natuurwetenschappen. Leg je er " +
          "drie af, neem dan biologie, chemie en fysica.",
      },
      {
        kop: "Wiskunde",
        tekst:
          "Er staan twee versies: basis en gevorderd. Je vakfiche zegt welke " +
          "van de twee jij nodig hebt.",
      },
    ],
  },

  "beyond-doorstroom": {
    kop:
      "Deze vakken gelden voor alle doorstroomrichtingen van de derde graad, " +
      "domeinoverschrijdend én domeingebonden.",
    punten: [
      {
        kop: "Wetenschappen",
        tekst:
          "Leg je ze in één examen af, neem dan natuurwetenschappen. Leg je er " +
          "drie af, neem dan biologie, chemie en fysica.",
      },
      {
        kop: "Bedrijfswetenschappen en welzijnswetenschappen",
        tekst:
          "Voor wiskunde en voor natuurwetenschappen heb jij een eigen " +
          "vakfiche. Die twee staan hieronder nog niet.",
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
    komtNog:
      "Nog in de maak: wiskunde en natuurwetenschappen voor " +
      "bedrijfswetenschappen en welzijnswetenschappen, sociale en " +
      "gedragswetenschappen, filosofie en recht, algemene economie, " +
      "bedrijfswetenschappen en recht, en samenleving en economie.",
  },
};

/** De noot bij deze categorie, of niets. */
export function vindCategorienoot(niveau: string): Categorienoot | undefined {
  return categorienoten[niveau];
}
