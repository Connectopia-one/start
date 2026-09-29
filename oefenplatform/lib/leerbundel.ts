import { KLIKBARE_BUNDELS } from "@/inhoud/leerbundels-interactief";
import { PUZZELFOTOS } from "@/inhoud/puzzelfotos";
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

/*
  Het beeld voor de legpuzzel op de eindhalte.

  Kim op 29 september 2026: "ik denk dat een fysieke puzzel van een afbeelding
  die ze op de juiste plaats moeten schuiven in thema leuker is." Het beeld
  komt dus uit het hoofdstuk zelf, niet uit een plaatjesbank.

  Eerste keuze is een **prent** die Kim voor dat hoofdstuk maakte; die staat in
  public/puzzels en in inhoud/puzzelfotos.ts. Is er geen, dan nemen we een
  **tekening** uit de leerbundel. Dat werkt, maar minder goed: het zijn schema's,
  en een stukje van een rooster ziet er precies hetzelfde uit als het stukje
  ernaast.

  Niet elke tekening leent zich ertoe: een strook van 6 keer zo breed als hoog
  levert stukjes op waar niets op staat. We nemen daarom de tekening die het
  dichtst bij een gewone liggende verhouding komt, en laten heel brede of heel
  smalle tekeningen vallen. Vindt hij er geen, dan valt het spel op de
  eindhalte terug op het volgordespel.
*/

export type Puzzelbeeld =
  | { soort: "prent"; url: string; verhouding: number; onderschrift?: string }
  | {
      soort: "tekening";
      html: string;
      verhouding: number;
      onderschrift?: string;
    };

/*
  De prent die Kim voor dit hoofdstuk maakte, als die er is.

  Anders dan bij de leerbundel telt " — pittig" hier wél mee: een pittig
  hoofdstuk heeft zijn eigen prent.
*/
export function puzzelPrent(
  vakSlug: string,
  hoofdstukTitel: string,
): Puzzelbeeld | null {
  const rij = PUZZELFOTOS[`${vakSlug}/${slugify(hoofdstukTitel)}`];
  if (!rij) return null;
  // Een prent die veel breder is dan hoog geeft een bord van een paar
  // centimeter hoog met flinterdunne stukjes. Dan liever een tekening.
  if (rij.verhouding < 0.55 || rij.verhouding > 2.6) return null;
  return { soort: "prent", url: rij.url, verhouding: rij.verhouding };
}

export function puzzelBeeld(bundel: KlikbareBundel): Puzzelbeeld | null {
  const kandidaten: Puzzelbeeld[] = [];
  for (const sectie of bundel.secties) {
    for (const blok of sectie.blokken) {
      if (blok.soort !== "figuur") continue;
      const kader = /viewBox="([\d.\s-]+)"/.exec(blok.html);
      if (!kader) continue;
      const maten = kader[1].trim().split(/\s+/).map(Number);
      if (maten.length < 4 || !maten[2] || !maten[3]) continue;
      const verhouding = maten[2] / maten[3];
      if (verhouding < 0.6 || verhouding > 3) continue;
      kandidaten.push({
        soort: "tekening",
        html: blok.html,
        verhouding,
        onderschrift: blok.onderschrift,
      });
    }
  }
  if (!kandidaten.length) return null;
  kandidaten.sort(
    (a, b) => Math.abs(a.verhouding - 1.4) - Math.abs(b.verhouding - 1.4),
  );
  return kandidaten[0];
}

/*
  Hoeveel stukken naast en onder elkaar. Twee dingen tegelijk: een stuk mag niet
  te plat worden, en het mogen er niet te veel zijn. Acht tot negen stukken
  schuift een kind los; bij vijftien zit het een halfuur te zwoegen.
*/
export function puzzelRooster(verhouding: number): {
  kolommen: number;
  rijen: number;
} {
  if (verhouding < 1.25) return { kolommen: 3, rijen: 3 };
  if (verhouding < 2.2) return { kolommen: 4, rijen: 2 };
  return { kolommen: 5, rijen: 2 };
}
