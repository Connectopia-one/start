/*
  Hoe Google ons vindt.

  Wat hier staat, leest een bezoeker niet op de pagina zelf. Het is wat Google
  bovenaan een zoekresultaat zet, en wat Google over de vzw te weten komt
  (naam, telefoon, mail, waar we werken). Daarom staat de regio er telkens
  in: iemand die "young engineers Hasselt" of "plusklas Genk" zoekt, moet ons
  herkennen aan het eerste wat hij leest.

  Aanpassen mag gerust. Houd een titel onder ongeveer 60 tekens en een
  omschrijving onder ongeveer 155, anders kapt Google ze af.
*/

export const vindbaarheid = {
  /* De naam zoals Google hem moet onthouden. Staat achter elke paginatitel. */
  naam: "Connectopia vzw",

  /* Andere namen waaronder mensen ons zoeken. */
  alternatieveNamen: ["Connectopia", "connectopia.one", "Young Engineers Hasselt-Genk"],

  /* De titel van de startpagina in Google. */
  titel: "Connectopia vzw | Kampen en Young Engineers Hasselt-Genk",

  /* De omschrijving onder die titel. */
  omschrijving:
    "Kampen, de Ontdekclub, Young Engineers Hasselt-Genk, plusklas en pluswerking in Hasselt en Genk. Voor nieuwsgierige kinderen, ook HB en UHB, in kleine groepjes en prikkelarm.",

  /* De gemeenten en de streek waar we werken. */
  regio: ["Hasselt", "Genk", "Limburg"],

  /*
    Het officiële adres van de vzw (de maatschappelijke zetel), door Kim
    doorgegeven op 23 oktober 2026. Maak je het leeg, dan geven we Google
    enkel de regio en de plaatsen waar we les geven.
  */
  adres: {
    straat: "Kluisstraat 16",
    postcode: "3570",
    gemeente: "Alken",
  },

  /* De plaatsen waar de lessen en kampen doorgaan. */
  locaties: [
    {
      naam: "Level X 28",
      straat: "Vilderstraat 28",
      postcode: "3500",
      gemeente: "Hasselt",
    },
    {
      naam: "Atheneum Hasselt",
      straat: "Kleine-Breemstraat 33",
      postcode: "3500",
      gemeente: "Hasselt",
    },
    {
      naam: "T2 Campus",
      straat: "Thor Park 8040",
      postcode: "3600",
      gemeente: "Genk",
    },
  ],
};
