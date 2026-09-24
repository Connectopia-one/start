/**
 * Een icoon per vak, zodat een kind op de vakkenpagina meteen ziet waar het
 * moet klikken zonder eerst te lezen. Het staat hier en niet in de databank:
 * dan hoeft er voor een nieuw vak niets aan de tabellen te veranderen, en een
 * vak dat we nog niet kennen krijgt gewoon het standaardboekje.
 */
const ICONEN: Record<string, string> = {
  nederlands: "📖",
  frans: "🥐",
  engels: "🔤",
  wiskunde: "➗",
  natuurwetenschappen: "🔬",
  "wetenschap-en-techniek": "🔧",
  wetenschap: "🔬",
  techniek: "🔧",
  geschiedenis: "🏛️",
  aardrijkskunde: "🌍",
};

export function vakIcoon(slug: string): string {
  return ICONEN[slug] ?? "📘";
}

/*
  Lange vaknamen op een smalle telefoon.

  De knoppen staan twee naast elkaar, en "Natuurwetenschappen" past daar niet
  op één regel. Een browser breekt zo'n woord dan zonder koppelteken af
  ("Natuurwetensc / happen"), want automatisch afbreken werkt alleen met een
  Nederlands woordenboek dat niet elke browser bij zich heeft. Daarom zetten we
  zelf een zacht afbreekstreepje (U+00AD) op de plaats waar het woord mag
  splitsen: dat is onzichtbaar zolang het woord past, en wordt een koppelteken
  zodra het moet breken.
*/
const AFBREEKPUNTEN: Record<string, string> = {
  natuurwetenschappen: "Natuur\u00ADwetenschappen",
  "wetenschap-en-techniek": "Wetenschap en tech\u00ADniek",
  aardrijkskunde: "Aardrijks\u00ADkunde",
};

export function vakLabel(slug: string, naam: string): string {
  return AFBREEKPUNTEN[slug] ?? naam;
}
