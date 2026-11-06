/**
 * Verzamelbadges: wat een kind al bij elkaar geoefend heeft, in beeld.
 *
 * Er komt geen enkele nieuwe tabel aan te pas. Alles wordt geteld uit wat het
 * platform toch al bijhoudt — beantwoorde vragen (`voortgang`) en foutloos
 * afgewerkte hoofdstukken (`stickers`) — zodat een kind dat hier voor het eerst
 * komt meteen ziet wat het de voorbije weken al verdiend heeft, in plaats van
 * vanaf nul te moeten beginnen.
 *
 * Alle badges gaan over wat een kind deed, nooit over hoe snel of hoe foutloos
 * het was in vergelijking met iemand anders. Er is met opzet geen ranglijst:
 * de kinderen hier vergelijken zichzelf al genoeg.
 */

export type Telling = {
  /** Aantal beantwoorde vragen, juist of fout. */
  gemaakt: number;
  /** Aantal juist beantwoorde vragen. */
  juist: number;
  /**
   * In hoeveel hoofdstukken het kind al echt geoefend heeft, juist of fout:
   * minstens OEFEN_DREMPEL verschillende vragen beantwoord. Voor de
   * inzetbadges, zie hieronder.
   */
  hoofdstukkenGeoefend: number;
  /** Aantal hoofdstukken dat ooit volledig juist afgewerkt werd. */
  sterren: number;
  /** In hoeveel verschillende vakken er al een hoofdstuk foutloos afgewerkt is. */
  vakkenMetSter: number;
  /** Al een hoofdstuk van 🧱 Basis foutloos afgewerkt? */
  basisSter: boolean;
  /** Al een vraag uit 🔭 de uitdagingshoek juist? */
  hoekjeJuist: boolean;
  /**
   * Het hoogste aantal feilloze examens binnen één vak. Drie daarvan geven de
   * examenster van dat vak; zie EXAMENS_VOOR_STER in app/voortgang-actions.ts.
   */
  examensFeilloos: number;
};

/** Vanaf zoveel verschillende vragen telt een hoofdstuk als geoefend. */
export const OEFEN_DREMPEL = 10;

export type Badge = {
  sleutel: string;
  emoji: string;
  naam: string;
  uitleg: string;
  /** Hoever dit kind staat, en wat er nodig is. Gelijk of hoger betekent verdiend. */
  nu: number;
  doel: number;
};

export const LEGE_TELLING: Telling = {
  gemaakt: 0,
  juist: 0,
  hoofdstukkenGeoefend: 0,
  sterren: 0,
  vakkenMetSter: 0,
  basisSter: false,
  hoekjeJuist: false,
  examensFeilloos: 0,
};

/** De hele verzameling, in de volgorde waarin ze getoond wordt. */
export function badges(t: Telling): Badge[] {
  return [
    {
      sleutel: "op-weg",
      emoji: "🌱",
      naam: "Op weg",
      uitleg: "Je eerste vraag beantwoord.",
      nu: t.gemaakt,
      doel: 1,
    },
    /* Inzetbadges: ze tellen hoe vaak een kind de moed had om een hoofdstuk
       aan te pakken, niet hoeveel het juist had. Kim, november 2026, na de
       enquêtes waarin ouders vertelden over faalangst: "fout of goed, maar als
       een soort goed bezig". Een kind dat veel fouten maakt en doorzet,
       verdient ze net zo goed. */
    {
      sleutel: "goed-bezig",
      emoji: "💪",
      naam: "Goed bezig!",
      uitleg: "In 3 hoofdstukken geoefend. Juist of fout, je hebt het geprobeerd.",
      nu: t.hoofdstukkenGeoefend,
      doel: 3,
    },
    {
      sleutel: "goed-op-weg",
      emoji: "🚀",
      naam: "Al goed op weg!",
      uitleg: "In 10 hoofdstukken geoefend.",
      nu: t.hoofdstukkenGeoefend,
      doel: 10,
    },
    {
      sleutel: "super-veel-geleerd",
      emoji: "🧠",
      naam: "Al super veel geleerd!",
      uitleg: "In 15 hoofdstukken geoefend.",
      nu: t.hoofdstukkenGeoefend,
      doel: 15,
    },
    {
      sleutel: "doorzetter",
      emoji: "🔥",
      naam: "Echte doorzetter!",
      uitleg: "In 25 hoofdstukken geoefend.",
      nu: t.hoofdstukkenGeoefend,
      doel: 25,
    },
    {
      sleutel: "oefenreus",
      emoji: "🦒",
      naam: "Oefenreus!",
      uitleg: "In 50 hoofdstukken geoefend. Wat een werk!",
      nu: t.hoofdstukkenGeoefend,
      doel: 50,
    },
    {
      sleutel: "vijfentwintig",
      emoji: "🎯",
      naam: "Vijfentwintig",
      uitleg: "25 vragen juist.",
      nu: t.juist,
      doel: 25,
    },
    {
      sleutel: "honderd",
      emoji: "🏅",
      naam: "Honderd",
      uitleg: "100 vragen juist.",
      nu: t.juist,
      doel: 100,
    },
    {
      sleutel: "vijfhonderd",
      emoji: "🏆",
      naam: "Vijfhonderd",
      uitleg: "500 vragen juist. Dat is een halve encyclopedie.",
      nu: t.juist,
      doel: 500,
    },
    {
      sleutel: "eerste-ster",
      emoji: "⭐",
      naam: "Eerste ster",
      uitleg: "Een hoofdstuk helemaal foutloos afgewerkt.",
      nu: t.sterren,
      doel: 1,
    },
    {
      sleutel: "vijf-sterren",
      emoji: "🌟",
      naam: "Vijf sterren",
      uitleg: "Vijf hoofdstukken foutloos.",
      nu: t.sterren,
      doel: 5,
    },
    {
      sleutel: "twintig-sterren",
      emoji: "💫",
      naam: "Twintig sterren",
      uitleg: "Twintig hoofdstukken foutloos.",
      nu: t.sterren,
      doel: 20,
    },
    {
      sleutel: "breed",
      emoji: "🌈",
      naam: "Breed",
      uitleg: "In drie verschillende vakken een hoofdstuk foutloos.",
      nu: t.vakkenMetSter,
      doel: 3,
    },
    {
      sleutel: "stevige-basis",
      emoji: "🧱",
      naam: "Stevige basis",
      uitleg: "Een hoofdstuk van 🧱 Basis foutloos afgewerkt.",
      nu: t.basisSter ? 1 : 0,
      doel: 1,
    },
    {
      sleutel: "examenster",
      emoji: "🎓",
      naam: "Examenster",
      uitleg:
        "Drie keer een examen van hetzelfde vak zonder één fout. Kim vroeg deze op 14 oktober 2026.",
      nu: t.examensFeilloos,
      doel: 3,
    },
    {
      sleutel: "verre-denker",
      emoji: "🔭",
      naam: "Verre denker",
      uitleg: "Een vraag uit 🔭 de uitdagingshoek juist.",
      nu: t.hoekjeJuist ? 1 : 0,
      doel: 1,
    },
  ];
}

export function verdiend(badge: Badge): boolean {
  return badge.nu >= badge.doel;
}
