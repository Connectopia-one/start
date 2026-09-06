export type KalenderDag = {
  datum: string; // YYYY-MM-DD
  type: "les" | "kamp" | "geenles";
  label: string;
  detail?: string;
};

// Schooljaar 2026-2027 — overgenomen uit de planning (Maandkalender Plusklassen 2026-2027).
// Vaste lesdagen: dinsdag = Atheneum Hasselt, woensdag = T2 Campus Genk, zaterdag = Level X 28 Hasselt.
export const KALENDER_2026_2027: KalenderDag[] = [
  // september 2026
  { datum: "2026-09-12", type: "les", label: "Level X 28 Hasselt", detail: "Start" },
  { datum: "2026-09-15", type: "les", label: "Atheneum Hasselt", detail: "Start · traject 1" },
  { datum: "2026-09-16", type: "les", label: "T2 Campus Genk", detail: "Start" },
  { datum: "2026-09-19", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-09-22", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-09-23", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-09-29", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-09-30", type: "les", label: "T2 Campus Genk" },

  // oktober 2026
  { datum: "2026-10-03", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-10-06", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-10-07", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-10-10", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-10-13", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-10-14", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-10-17", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-10-20", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-10-21", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-10-24", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-10-27", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-10-28", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-10-31", type: "les", label: "Level X 28 Hasselt" },

  // november 2026
  { datum: "2026-11-02", type: "kamp", label: "Herfstkamp" },
  { datum: "2026-11-03", type: "kamp", label: "Herfstkamp" },
  { datum: "2026-11-04", type: "kamp", label: "Herfstkamp" },
  { datum: "2026-11-05", type: "kamp", label: "Herfstkamp" },
  { datum: "2026-11-10", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-11-11", type: "geenles", label: "Wapenstilstand" },
  { datum: "2026-11-14", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-11-17", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-11-18", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-11-21", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-11-24", type: "les", label: "Atheneum Hasselt", detail: "Laatste les traject 1" },
  { datum: "2026-11-25", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-11-28", type: "les", label: "Level X 28 Hasselt" },

  // december 2026
  { datum: "2026-12-02", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-12-05", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-12-08", type: "les", label: "Atheneum Hasselt", detail: "Start traject 2" },
  { datum: "2026-12-09", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-12-12", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2026-12-15", type: "les", label: "Atheneum Hasselt" },
  { datum: "2026-12-16", type: "les", label: "T2 Campus Genk" },
  { datum: "2026-12-19", type: "geenles", label: "Geen les" },
  { datum: "2026-12-21", type: "kamp", label: "Kerstkamp 1" },
  { datum: "2026-12-22", type: "kamp", label: "Kerstkamp 1" },
  { datum: "2026-12-23", type: "kamp", label: "Kerstkamp 1" },
  { datum: "2026-12-26", type: "geenles", label: "Geen les" },
  { datum: "2026-12-28", type: "kamp", label: "Kerstkamp 2" },
  { datum: "2026-12-29", type: "kamp", label: "Kerstkamp 2" },
  { datum: "2026-12-30", type: "kamp", label: "Kerstkamp 2" },

  // januari 2027
  { datum: "2027-01-05", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-01-06", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-01-09", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-01-12", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-01-13", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-01-16", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-01-19", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-01-20", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-01-23", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-01-26", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-01-27", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-01-30", type: "les", label: "Level X 28 Hasselt" },

  // februari 2027
  { datum: "2027-02-02", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-02-03", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-02-06", type: "geenles", label: "Geen les" },
  { datum: "2027-02-08", type: "kamp", label: "Krokuskamp 1" },
  { datum: "2027-02-09", type: "kamp", label: "Krokuskamp 1" },
  { datum: "2027-02-10", type: "kamp", label: "Krokuskamp 1" },
  { datum: "2027-02-11", type: "kamp", label: "Krokuskamp 2" },
  { datum: "2027-02-12", type: "kamp", label: "Krokuskamp 2" },
  { datum: "2027-02-13", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-02-16", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-02-17", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-02-20", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-02-23", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-02-24", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-02-27", type: "les", label: "Level X 28 Hasselt" },

  // maart 2027
  { datum: "2027-03-02", type: "les", label: "Atheneum Hasselt", detail: "Laatste les traject 2" },
  { datum: "2027-03-03", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-03-06", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-03-10", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-03-13", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-03-16", type: "les", label: "Atheneum Hasselt", detail: "Start traject 3" },
  { datum: "2027-03-17", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-03-20", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-03-23", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-03-24", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-03-27", type: "geenles", label: "Geen les" },
  { datum: "2027-03-30", type: "kamp", label: "Paaskamp 1" },
  { datum: "2027-03-31", type: "kamp", label: "Paaskamp 1" },

  // april 2027
  { datum: "2027-04-01", type: "kamp", label: "Paaskamp 2" },
  { datum: "2027-04-02", type: "kamp", label: "Paaskamp 2" },
  { datum: "2027-04-05", type: "kamp", label: "Paaskamp 3" },
  { datum: "2027-04-06", type: "kamp", label: "Paaskamp 3" },
  { datum: "2027-04-07", type: "kamp", label: "Paaskamp 4" },
  { datum: "2027-04-08", type: "kamp", label: "Paaskamp 4" },
  { datum: "2027-04-13", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-04-14", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-04-17", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-04-20", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-04-21", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-04-24", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-04-27", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-04-28", type: "les", label: "T2 Campus Genk" },

  // mei 2027
  { datum: "2027-05-01", type: "geenles", label: "Dag van de Arbeid" },
  { datum: "2027-05-04", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-05-05", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-05-08", type: "geenles", label: "Hemelvaart" },
  { datum: "2027-05-11", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-05-12", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-05-15", type: "geenles", label: "Pinksteren" },
  { datum: "2027-05-18", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-05-19", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-05-22", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-05-25", type: "les", label: "Atheneum Hasselt" },
  { datum: "2027-05-26", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-05-29", type: "les", label: "Level X 28 Hasselt" },

  // juni 2027
  { datum: "2027-06-01", type: "les", label: "Atheneum Hasselt", detail: "Einde 3e traject · laatste les" },
  { datum: "2027-06-02", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-06-05", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-06-09", type: "les", label: "T2 Campus Genk" },
  { datum: "2027-06-12", type: "les", label: "Level X 28 Hasselt" },
  { datum: "2027-06-16", type: "les", label: "T2 Campus Genk", detail: "Laatste les" },
  { datum: "2027-06-19", type: "les", label: "Level X 28 Hasselt", detail: "Laatste les" },
];

export function kalenderPerMaand(): { jaar: number; maand: number; naam: string }[] {
  return [
    { jaar: 2026, maand: 8, naam: "September 2026" },
    { jaar: 2026, maand: 9, naam: "Oktober 2026" },
    { jaar: 2026, maand: 10, naam: "November 2026" },
    { jaar: 2026, maand: 11, naam: "December 2026" },
    { jaar: 2027, maand: 0, naam: "Januari 2027" },
    { jaar: 2027, maand: 1, naam: "Februari 2027" },
    { jaar: 2027, maand: 2, naam: "Maart 2027" },
    { jaar: 2027, maand: 3, naam: "April 2027" },
    { jaar: 2027, maand: 4, naam: "Mei 2027" },
    { jaar: 2027, maand: 5, naam: "Juni 2027" },
  ];
}

export function dagInfo(datum: string): KalenderDag | undefined {
  return KALENDER_2026_2027.find((d) => d.datum === datum);
}
