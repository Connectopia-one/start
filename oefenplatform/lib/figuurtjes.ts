/*
  De figuurtjes die een kind kan kiezen met zijn sterretjes (Kim, november
  2026). Een sterretje per hoofdstuk dat het helemaal afwerkte, juist of fout:
  het gaat om het doorzetten, niet om foutloos zijn. Er is geen ranglijst en
  niets om te winnen van iemand anders.

  De eerste figuurtjes kosten één sterretje, zodat er meteen iets leuks is bij
  het eerste afgewerkte hoofdstuk. Later worden ze iets duurder, zodat er ook na
  veel hoofdstukken nog iets te kiezen valt. Een figuurtje toevoegen kan
  gewoon hier; verander de sleutel van een bestaand figuurtje niet meer.
*/
export type Figuurtje = { sleutel: string; emoji: string; naam: string; prijs: number };

export const FIGUURTJES: Figuurtje[] = [
  { sleutel: "vos", emoji: "🦊", naam: "Vos", prijs: 1 },
  { sleutel: "egel", emoji: "🦔", naam: "Egel", prijs: 1 },
  { sleutel: "uil", emoji: "🦉", naam: "Uil", prijs: 1 },
  { sleutel: "schildpad", emoji: "🐢", naam: "Schildpad", prijs: 1 },
  { sleutel: "kat", emoji: "🐱", naam: "Kat", prijs: 1 },
  { sleutel: "hond", emoji: "🐶", naam: "Hond", prijs: 1 },
  { sleutel: "konijn", emoji: "🐰", naam: "Konijn", prijs: 1 },
  { sleutel: "panda", emoji: "🐼", naam: "Panda", prijs: 1 },
  { sleutel: "pinguin", emoji: "🐧", naam: "Pinguïn", prijs: 2 },
  { sleutel: "koala", emoji: "🐨", naam: "Koala", prijs: 2 },
  { sleutel: "kikker", emoji: "🐸", naam: "Kikker", prijs: 2 },
  { sleutel: "octopus", emoji: "🐙", naam: "Octopus", prijs: 2 },
  { sleutel: "vlinder", emoji: "🦋", naam: "Vlinder", prijs: 2 },
  { sleutel: "lieveheersbeestje", emoji: "🐞", naam: "Lieveheersbeestje", prijs: 2 },
  { sleutel: "dolfijn", emoji: "🐬", naam: "Dolfijn", prijs: 2 },
  { sleutel: "luiaard", emoji: "🦥", naam: "Luiaard", prijs: 2 },
  { sleutel: "robot", emoji: "🤖", naam: "Robot", prijs: 3 },
  { sleutel: "raket", emoji: "🚀", naam: "Raket", prijs: 3 },
  { sleutel: "astronaut", emoji: "🧑‍🚀", naam: "Astronaut", prijs: 3 },
  { sleutel: "tovenaar", emoji: "🧙", naam: "Tovenaar", prijs: 3 },
  { sleutel: "ridder", emoji: "🛡️", naam: "Schild", prijs: 3 },
  { sleutel: "dinosaurus", emoji: "🦕", naam: "Dinosaurus", prijs: 3 },
  { sleutel: "walvis", emoji: "🐳", naam: "Walvis", prijs: 3 },
  { sleutel: "papegaai", emoji: "🦜", naam: "Papegaai", prijs: 3 },
  { sleutel: "draak", emoji: "🐉", naam: "Draak", prijs: 5 },
  { sleutel: "eenhoorn", emoji: "🦄", naam: "Eenhoorn", prijs: 5 },
  { sleutel: "regenboog", emoji: "🌈", naam: "Regenboog", prijs: 5 },
  { sleutel: "planeet", emoji: "🪐", naam: "Planeet", prijs: 5 },
  { sleutel: "kroon", emoji: "👑", naam: "Kroon", prijs: 8 },
  { sleutel: "komeet", emoji: "☄️", naam: "Komeet", prijs: 8 },
];

export const figuurtjeVan = (sleutel: string | null | undefined) =>
  FIGUURTJES.find((f) => f.sleutel === sleutel) ?? null;

/** Hoeveel sterretjes er al uitgegeven zijn aan deze figuurtjes. */
export const uitgegeven = (eigen: string[]) =>
  eigen.reduce((som, s) => som + (figuurtjeVan(s)?.prijs ?? 0), 0);
