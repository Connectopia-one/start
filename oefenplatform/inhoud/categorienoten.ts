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
*/

export const categorienoten: Record<string, string> = {
  "boost-doorstroom":
    "Deze vakken gelden voor de doorstroomrichtingen van de tweede graad, " +
    "domeinoverschrijdend én domeingebonden. Twee dingen om te weten: leg je " +
    "je wetenschappen in één examen af, dan neem je natuurwetenschappen, en " +
    "leg je er drie af, dan neem je biologie, chemie en fysica. En wiskunde " +
    "staat er in twee versies, basis en gevorderd: je vakfiche zegt welke " +
    "van de twee jij nodig hebt.",

  "beyond-doorstroom":
    "Deze vakken gelden voor alle doorstroomrichtingen van de derde graad: " +
    "zowel de domeinoverschrijdende (economie-wiskunde, humane wetenschappen, " +
    "Latijn-moderne talen, Latijn-wiskunde, moderne talen, " +
    "wetenschappen-wiskunde) als de domeingebonden (bedrijfswetenschappen en " +
    "welzijnswetenschappen). De vakfiches van de Examencommissie noemen die " +
    "richtingen samen bovenaan, daarom staan ze hier niet apart. Leg je je " +
    "wetenschappen in één examen af, dan neem je natuurwetenschappen; leg je " +
    "er drie af, dan neem je biologie, chemie en fysica. De vakken die maar " +
    "bij één richting horen, zoals sociale en gedragswetenschappen, filosofie " +
    "en recht of samenleving en economie, zijn nog in de maak.",
};

/** De noot bij deze categorie, of niets. */
export function vindCategorienoot(niveau: string): string | undefined {
  return categorienoten[niveau];
}
