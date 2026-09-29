import { KLIKBARE_BUNDELS } from "@/inhoud/leerbundels-interactief";
import { slugify } from "@/lib/slug";

/*
  De klikbare leerbundel: dezelfde theorie als in de pdf, maar op het scherm,
  opgedeeld in onderdelen waar een kind één voor één op klikt.

  De bestanden komen uit inhoud/leerbundels/bron/maak_interactief.py, dat
  dezelfde bron leest als de pdf. Er is dus geen tweede versie van de tekst die
  kan achterlopen.

  Er hangt geen kolom in de databank aan vast. Een hoofdstuk vindt zijn bundel
  aan zijn eigen titel: "Getallenkennis" in het vak wiskunde zoekt de sleutel
  "wiskunde/getallenkennis". Een pittig hoofdstuk deelt de bundel van het
  gewone hoofdstuk, want het gaat over dezelfde leerstof.
*/

export type BundelBlok = {
  soort: "tekst" | "weetje" | "kader" | "figuur";
  html: string;
  onderschrift?: string;
};

export type BundelSectie = {
  kop: string;
  blokken: BundelBlok[];
};

export type KlikbareBundel = {
  vak: string;
  titel: string;
  onder: string;
  secties: BundelSectie[];
  onthoud: string[];
};

const PITTIG = /\s*—\s*pittig$/i;

export function bundelSleutel(vakSlug: string, hoofdstukTitel: string): string {
  const basis = hoofdstukTitel.replace(PITTIG, "");
  return `${vakSlug}/${slugify(basis)}`;
}

export async function laadKlikbareBundel(
  vakSlug: string,
  hoofdstukTitel: string,
): Promise<KlikbareBundel | null> {
  const laden = KLIKBARE_BUNDELS[bundelSleutel(vakSlug, hoofdstukTitel)];
  if (!laden) return null;
  const mod = await laden();
  return mod.default as KlikbareBundel;
}

/** Of dit hoofdstuk een interactieve bundel heeft, zonder ze in te laden. */
export function heeftKlikbareBundel(
  vakSlug: string,
  hoofdstukTitel: string,
): boolean {
  return Boolean(KLIKBARE_BUNDELS[bundelSleutel(vakSlug, hoofdstukTitel)]);
}
