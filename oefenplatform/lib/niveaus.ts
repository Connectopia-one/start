export type NiveauSlug = "basis" | "start" | "spark" | "boost" | "beyond" | "hoekje";

export type Niveau = {
  slug: NiveauSlug;
  emoji: string;
  naam: string;
  omschrijving: string;
};

/*
  🧱 Basis is geen leerjaar maar herhaling: de bouwstenen (komma verschuiven,
  maten omzetten, breuken, de namen van de bewerkingen, ggd en kgv) voor een
  kind dat die nog niet vlot beheerst, in welke categorie het ook zit. Daarom
  staat het op de startpagina apart, onder de vier leerjaarcategorieën.

  🚀 De uitdagingshoek is dat andere uiterste: geen leerstof van een leerjaar,
  maar vragen die er net naast liggen (de ruimte, hoe een computer denkt, de
  geschiedenis van ons land, paradoxen). Voor wie klaar is met de gewone
  hoofdstukken en gewoon verder wil denken. Niet te verwarren met het
  hoofdstuk "Uitdaging — alles door elkaar", dat bij elk vak staat en wél
  binnen de leerstof van dat vak blijft.
*/
export const NIVEAUS: Niveau[] = [
  { slug: "basis", emoji: "🧱", naam: "Basis", omschrijving: "De bouwstenen herhalen, voor elk niveau" },
  { slug: "start", emoji: "🌱", naam: "Start", omschrijving: "5de & 6de leerjaar" },
  { slug: "spark", emoji: "✨", naam: "Spark", omschrijving: "1ste & 2de middelbaar" },
  { slug: "boost", emoji: "🚀", naam: "Boost", omschrijving: "3de & 4de middelbaar" },
  { slug: "beyond", emoji: "🌍", naam: "Beyond", omschrijving: "5de & 6de middelbaar" },
  {
    slug: "hoekje",
    emoji: "🔭",
    naam: "Uitdagingshoek",
    omschrijving: "Verder dan de leerstof, voor wie graag ver doordenkt",
  },
];

export function vindNiveau(slug: string): Niveau | undefined {
  return NIVEAUS.find((n) => n.slug === slug);
}

/** De vier categorieën die bij een leerjaar horen, zonder 🧱 Basis en 🔭 de hoek. */
export const LEERJAARNIVEAUS = NIVEAUS.filter(
  (n) => n.slug !== "basis" && n.slug !== "hoekje"
);
