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

export const vaknoten: Record<string, string> = {
  "start/engels":
    "Engels hoort niet bij de minimumdoelen van het lager onderwijs. Wij zetten " +
    "het er zelf bij, omdat we het graag aanbieden: kinderen komen vandaag veel " +
    "vroeger met Engels in aanraking, en een goede basis op jonge leeftijd kan " +
    "geen kwaad. Oefen dus gerust mee, maar weet dat je kind hier op school nog " +
    "niet op beoordeeld wordt.",
};

/** De noot bij dit vak in deze categorie, of niets. */
export function vindVaknoot(niveau: string, vak: string): string | undefined {
  return vaknoten[`${niveau}/${vak}`];
}
