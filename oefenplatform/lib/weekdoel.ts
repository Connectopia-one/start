/**
 * Hoe vaak een kind deze week de vraag van de dag deed.
 *
 * Bewust geen "elke dag op rij": Kim vroeg drie keer per week, precies omdat
 * een dagelijkse reeks die je kwijtspeelt eerder ontmoedigt dan aanmoedigt.
 * Drie van de zeven blijft haalbaar in een drukke week, en een keer overslaan
 * is geen ramp.
 *
 * Het staat in de browser, niet in de databank, om dezelfde reden als het
 * actieve kind (zie lib/actiefkind.ts): het hoort bij het toestel waarop
 * geoefend wordt. Er hangt niets aan vast dat verloren kan gaan — een leeg
 * telraam is hooguit jammer, nooit stuk. Alles zit daarom in een try/catch,
 * en privénavigatie of geblokkeerde opslag mag nooit iets breken.
 */

import {
  WEEKDOEL,
  maandagVan,
  vandaagSleutel,
  volgendeWeek,
  weekSleutel,
} from "@/lib/dagvraag";

export const WEEKDOEL_KEY = "oefenplatform_weekdoel";

export type Weekstand = {
  /** De maandag van de week die hier geteld wordt. */
  week: string;
  /** De dagen van deze week waarop de vraag gedaan werd. */
  dagen: string[];
  /** Hoeveel weken na elkaar het doel gehaald werd, deze week meegeteld. */
  wekenOpRij: number;
};

const LEEG: Weekstand = { week: "", dagen: [], wekenOpRij: 0 };

export function leesWeekstand(nu: Date = new Date()): Weekstand {
  let bewaard: Weekstand = LEEG;
  try {
    const tekst = localStorage.getItem(WEEKDOEL_KEY);
    if (tekst) {
      const gelezen = JSON.parse(tekst) as Partial<Weekstand>;
      bewaard = {
        week: typeof gelezen.week === "string" ? maandagVan(gelezen.week) : "",
        dagen: Array.isArray(gelezen.dagen)
          ? gelezen.dagen.filter((d) => typeof d === "string")
          : [],
        wekenOpRij: Number.isFinite(gelezen.wekenOpRij)
          ? Number(gelezen.wekenOpRij)
          : 0,
      };
    }
  } catch {
    // privénavigatie, geblokkeerde opslag of een kapot lijntje: gewoon opnieuw beginnen
  }
  return rolOver(bewaard, weekSleutel(nu));
}

/**
 * Zet de stand klaar voor de week waarin we nu zitten.
 *
 * De reeks weken blijft alleen staan als de vorige week gehaald werd én er
 * geen week tussen zit: wie een week helemaal oversloeg, begint opnieuw.
 */
function rolOver(stand: Weekstand, week: string): Weekstand {
  if (stand.week === week) return stand;
  const gehaald = stand.dagen.length >= WEEKDOEL;
  const aansluitend = stand.week !== "" && volgendeWeek(stand.week) === week;
  return {
    week,
    dagen: [],
    wekenOpRij: gehaald && aansluitend ? stand.wekenOpRij : 0,
  };
}

/**
 * Tekent vandaag af en bewaart dat. Een tweede keer op dezelfde dag telt niet
 * mee: het doel is drie dagen, niet drie vragen.
 */
export function tekenVandaagAf(
  stand: Weekstand,
  nu: Date = new Date(),
): Weekstand {
  const vandaag = vandaagSleutel(nu);
  if (stand.dagen.includes(vandaag)) return stand;

  const dagen = [...stand.dagen, vandaag];
  const nieuw: Weekstand = {
    ...stand,
    dagen,
    // De reeks loopt pas op op het moment dat het doel gehaald wordt, niet bij
    // het omslaan van de week: anders zou een week die je niet haalde toch
    // meetellen zolang je maar één keer langskwam.
    wekenOpRij:
      dagen.length === WEEKDOEL ? stand.wekenOpRij + 1 : stand.wekenOpRij,
  };

  try {
    localStorage.setItem(WEEKDOEL_KEY, JSON.stringify(nieuw));
  } catch {
    // niet kunnen bewaren mag het oefenen niet in de weg staan
  }
  return nieuw;
}

/*
  Welke vragen van vandaag dit toestel al beantwoord heeft.

  Er staat één vraag per dag én per categorie. Wie de vraag van 🌱 Start
  oploste en daarna op ✨ Spark klikt, krijgt een andere vraag en hoort die
  gewoon te kunnen oplossen. Tot 29 september 2026 keek het scherm alleen naar
  de dág: de tweede vraag stond dan meteen met het antwoord erbij en "je deed
  deze vraag vandaag al", terwijl het kind ze nog niet gezien had.

  Het weekdoel blijft wel per dag tellen. Drie dagen langskomen is het doel,
  geen drie vragen; wie op één dag vier categorieën doet, staat nog altijd op
  één bolletje.
*/

export const GEDANE_VRAGEN_KEY = "oefenplatform_dagvraag_gedaan";

type GedaneVragen = { dag: string; vragen: string[] };

function leesGedaneVragen(nu: Date = new Date()): GedaneVragen {
  const vandaag = vandaagSleutel(nu);
  try {
    const tekst = localStorage.getItem(GEDANE_VRAGEN_KEY);
    if (tekst) {
      const gelezen = JSON.parse(tekst) as Partial<GedaneVragen>;
      // Van gisteren houden we niets bij: morgen staan er nieuwe vragen.
      if (gelezen.dag === vandaag && Array.isArray(gelezen.vragen)) {
        return {
          dag: vandaag,
          vragen: gelezen.vragen.filter((v) => typeof v === "string"),
        };
      }
    }
  } catch {
    // privénavigatie of een kapot lijntje: dan begint de dag gewoon opnieuw
  }
  return { dag: vandaag, vragen: [] };
}

/** Deed dit toestel deze vraag vandaag al? */
export function vraagAlGedaan(vraagId: string, nu: Date = new Date()): boolean {
  return leesGedaneVragen(nu).vragen.includes(vraagId);
}

/** Tekent deze ene vraag af, los van het weekdoel. */
export function noteerVraagGedaan(
  vraagId: string,
  nu: Date = new Date(),
): void {
  const stand = leesGedaneVragen(nu);
  if (stand.vragen.includes(vraagId)) return;
  try {
    localStorage.setItem(
      GEDANE_VRAGEN_KEY,
      JSON.stringify({ dag: stand.dag, vragen: [...stand.vragen, vraagId] }),
    );
  } catch {
    // niet kunnen bewaren mag het oefenen niet in de weg staan
  }
}
