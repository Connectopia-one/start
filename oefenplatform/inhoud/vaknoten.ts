/*
  Een woordje bij een vak, boven de hoofdstukken.

  Alles hier is gewone tekst. Wil je iets aanpassen of er een noot bij zetten
  voor een ander vak, dan hoef je geen code te kennen: pas de zinnen hieronder
  aan, of zet er een blok bij in dezelfde vorm. De sleutel is de categorie en
  de slug van het vak zoals ze in het webadres staan, bijvoorbeeld
  /niveaus/start/engels wordt "start/engels".

  Staat er voor een vak niets, dan toont de pagina gewoon geen kadertje.

  Kim op 29 september 2026, over Engels bij 🌱 Start: "bij engels start moet er
  mss een tekst bij dat dit niet bij de onderwijsdoelen hoort maar dat we dit
  zelf graag hebben, en een goede basis op jongere leeftijd geen kwaad kan,
  zeker in de tijd dat kinderen sneller in aanraking komen met Engels."
*/


/*
  Kelly, een mama uit de testgroep, op 20 oktober 2026: haar zoon is niet
  sterk in Frans en begon bij de eerste oefening, een tekst. Die was te hoog
  gegrepen, en omdat ze bovenaan stond dacht hij dat het daarna nog moeilijker
  werd. De volgorde volgt de vakfiche van de Examencommissie, niet de
  moeilijkheid. Dat zeggen we nu boven Frans.
*/
const fransVolgorde =
  "De hoofdstukken staan in de volgorde van de vakfiche van de " +
  "Examencommissie, niet van makkelijk naar moeilijk. Een tekst lezen staat " +
  "bovenaan, maar is voor veel jongeren net het moeilijkste. Is Frans niet " +
  "je sterkste vak, begin dan gerust bij de woordenschat of de grammatica, " +
  "en kom later terug naar de teksten.";

export const vaknoten: Record<string, string> = {
  "start/engels":
    "Engels hoort niet bij de minimumdoelen van het lager onderwijs. Wij zetten " +
    "het er zelf bij, omdat we het graag aanbieden: kinderen komen vandaag veel " +
    "vroeger met Engels in aanraking, en een goede basis op jonge leeftijd kan " +
    "geen kwaad. Oefen dus gerust mee, maar weet dat je kind hier op school nog " +
    "niet op beoordeeld wordt.",

  "boost-doorstroom/natuurwetenschappen":
    "Dit is het vak voor de richtingen die hun wetenschappen in één examen " +
    "afleggen: economische wetenschappen, humane wetenschappen, moderne talen " +
    "en Latijn. Zit je in natuurwetenschappen, dan heb je de drie aparte vakken " +
    "biologie, chemie en fysica nodig in plaats van dit vak.",

  "boost-doorstroom/biologie":
    "Dit vak is er voor de richting natuurwetenschappen, die haar wetenschappen " +
    "in drie aparte examens aflegt: biologie, chemie en fysica. Volg je een " +
    "andere richting met één examen wetenschappen, dan heb je het vak " +
    "natuurwetenschappen nodig in plaats van dit vak.",

  "boost-doorstroom/chemie":
    "Dit vak is er voor de richting natuurwetenschappen, die haar wetenschappen " +
    "in drie aparte examens aflegt: biologie, chemie en fysica. Volg je een " +
    "andere richting met één examen wetenschappen, dan heb je het vak " +
    "natuurwetenschappen nodig in plaats van dit vak.",

  "boost-doorstroom/fysica":
    "Dit vak is er voor de richting natuurwetenschappen, die haar wetenschappen " +
    "in drie aparte examens aflegt: biologie, chemie en fysica. Volg je een " +
    "andere richting met één examen wetenschappen, dan heb je het vak " +
    "natuurwetenschappen nodig in plaats van dit vak.",

  "beyond-doorstroom/natuurwetenschappen":
    "Dit is het vak voor de richtingen die hun wetenschappen in één examen " +
    "afleggen, zoals economie-moderne talen, humane wetenschappen, Latijn en " +
    "moderne talen. Zit je in natuurwetenschappen of een andere richting met " +
    "drie examens wetenschappen, dan heb je de aparte vakken biologie, chemie " +
    "en fysica nodig in plaats van dit vak.",

  "beyond-doorstroom/biologie":
    "Dit vak is er voor de richtingen die hun wetenschappen in drie aparte " +
    "examens afleggen: biologie, chemie en fysica. Volg je een richting met één " +
    "examen wetenschappen, dan heb je het vak natuurwetenschappen nodig in " +
    "plaats van dit vak.",
  "beyond-doorstroom/chemie":
    "Dit vak is er voor de richtingen die hun wetenschappen in drie aparte " +
    "examens afleggen: biologie, chemie en fysica. Volg je een richting met één " +
    "examen wetenschappen, dan heb je het vak natuurwetenschappen nodig in " +
    "plaats van dit vak.",
  "beyond-doorstroom/statistiek":
    "Statistiek is een apart examen voor humane wetenschappen. Volg je een " +
    "andere richting, dan zit de statistiek die jij nodig hebt gewoon in " +
    "wiskunde gevorderd.",

  "beyond-doorstroom/fysica":
    "Dit vak is er voor de richtingen die hun wetenschappen in drie aparte " +
    "examens afleggen: biologie, chemie en fysica. Volg je een richting met één " +
    "examen wetenschappen, dan heb je het vak natuurwetenschappen nodig in " +
    "plaats van dit vak.",

  "spark/frans": fransVolgorde,

  "boost-doorstroom/frans": fransVolgorde,

  "boost-dubbele-finaliteit/frans": fransVolgorde,

  "beyond-doorstroom/frans": fransVolgorde,

  "beyond-dubbele-finaliteit/frans": fransVolgorde,
};

/** De noot bij dit vak in deze categorie, of niets. */
export function vindVaknoot(niveau: string, vak: string): string | undefined {
  return vaknoten[`${niveau}/${vak}`];
}
