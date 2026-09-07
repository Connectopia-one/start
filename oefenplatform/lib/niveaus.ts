export type NiveauSlug = "start" | "spark" | "boost" | "beyond";

export type Niveau = {
  slug: NiveauSlug;
  emoji: string;
  naam: string;
  omschrijving: string;
};

export const NIVEAUS: Niveau[] = [
  { slug: "start", emoji: "🌱", naam: "Start", omschrijving: "5de & 6de leerjaar" },
  { slug: "spark", emoji: "✨", naam: "Spark", omschrijving: "1ste & 2de middelbaar" },
  { slug: "boost", emoji: "🚀", naam: "Boost", omschrijving: "3de & 4de middelbaar" },
  { slug: "beyond", emoji: "🌍", naam: "Beyond", omschrijving: "5de & 6de middelbaar" },
];

export function vindNiveau(slug: string): Niveau | undefined {
  return NIVEAUS.find((n) => n.slug === slug);
}
