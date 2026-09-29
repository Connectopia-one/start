import { PRENTEN } from "@/inhoud/prenten";
import { slugify } from "@/lib/slug";

export type Prent = { url: string; breedte: number; hoogte: number };

/**
 * De prent die boven de vragen van dit hoofdstuk hoort, of niets.
 *
 * Voor de taalvakken: op het examen van de examencommissie krijg je een foto
 * of prent en moet je in die taal beschrijven wat je ziet. Een geschreven
 * beschrijving kan het platform niet nakijken, maar dezelfde woordenschat
 * (er is en er zijn, links en rechts, kleuren, aantallen, wie wat doet) valt
 * wel met meerkeuze te toetsen. De prent blijft dan boven de vragen staan,
 * net als de leestekst bij begrijpend lezen.
 *
 * De prent hangt aan de titel van het hoofdstuk, niet aan de databank: zet het
 * bestand in public/prenten/<vak>/ met inhoud/prenten/bron/maak_prenten.py en
 * het hoofdstuk vindt ze zelf. Er hoeft dus geen SQL voor gedraaid te worden.
 * Hernoem je een hoofdstuk, hernoem dan ook zijn prent.
 */
export function vindPrent(
  vakSlug: string,
  hoofdstukTitel: string,
): Prent | null {
  return PRENTEN[`${vakSlug}/${slugify(hoofdstukTitel)}`] ?? null;
}
