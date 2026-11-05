/*
  De vragen van de enquête (Kim, 5 november 2026).

  De enquête is privé: alleen Kim leest de antwoorden, in Beheer → Enquêtes en
  reviews. Ze staan als één jsonb-veld in de tabel enquetes, met de sleutel
  van elke vraag hieronder. Een vraag toevoegen of de tekst aanpassen kan dus
  hier, zonder iets aan de databank te veranderen. Verander de sleutel van een
  bestaande vraag niet meer zodra er antwoorden binnen zijn, anders vindt
  Beheer die oude antwoorden niet terug.

  "Uitgebreid ingevuld" (de voorwaarde voor het gratis jaar): alle verplichte
  vragen beantwoord, en bij de drie grote open vragen minstens een paar
  zinnen. Kim kijkt het daarna nog zelf na voor ze goedkeurt.
*/

export type EnqueteVraag =
  | {
      sleutel: string;
      soort: "keuze";
      vraag: string;
      opties: string[];
      verplicht: boolean;
    }
  | {
      sleutel: string;
      soort: "meerdere";
      vraag: string;
      opties: string[];
      verplicht: boolean;
    }
  | {
      sleutel: string;
      soort: "score";
      vraag: string;
      van: number;
      tot: number;
      laag: string;
      hoog: string;
      verplicht: boolean;
    }
  | {
      sleutel: string;
      soort: "open";
      vraag: string;
      hulp?: string;
      /** minimum aantal tekens; enkel bij de grote open vragen */
      minimum?: number;
      verplicht: boolean;
    };

export type EnqueteDeel = { titel: string; vragen: EnqueteVraag[] };

/** Bij de grote open vragen: "een paar zinnen". */
export const MINIMUM_OPEN = 80;

export const ENQUETE: EnqueteDeel[] = [
  {
    titel: "Over jullie",
    vragen: [
      {
        sleutel: "wie",
        soort: "keuze",
        vraag: "Wie oefende er op het platform?",
        opties: ["Mijn kind", "Meerdere kinderen", "Ikzelf", "Leerlingen of bijleskinderen"],
        verplicht: true,
      },
      {
        sleutel: "leeftijd",
        soort: "open",
        vraag: "Welk leerjaar of welke leeftijd hebben de kinderen die oefenden?",
        hulp: "Bijvoorbeeld: 5de leerjaar en 2de middelbaar.",
        verplicht: true,
      },
      {
        sleutel: "hoe_vaak",
        soort: "keuze",
        vraag: "Hoe vaak werd er gemiddeld geoefend?",
        opties: ["Bijna elke dag", "Een paar keer per week", "Af en toe", "Eén of twee keer"],
        verplicht: true,
      },
    ],
  },
  {
    titel: "Starten",
    vragen: [
      {
        sleutel: "starten_score",
        soort: "score",
        vraag: "Hoe makkelijk was het om te starten (account maken, iemand toevoegen, eerste oefening)?",
        van: 1,
        tot: 5,
        laag: "heel moeilijk",
        hoog: "heel makkelijk",
        verplicht: true,
      },
      {
        sleutel: "starten_moeilijk",
        soort: "open",
        vraag: "Liep er iets moeilijk bij het starten of bij het inloggen?",
        verplicht: false,
      },
    ],
  },
  {
    titel: "De oefeningen",
    vragen: [
      {
        sleutel: "onderdelen",
        soort: "meerdere",
        vraag: "Welke onderdelen werden het meest gebruikt?",
        opties: [
          "🧱 Basis",
          "Start",
          "Spark",
          "Boost",
          "Beyond",
          "🔭 Uitdagingshoek",
          "Vraag van de dag",
          "Examens",
          "Leerbundels en oefenbundels",
        ],
        verplicht: true,
      },
      {
        sleutel: "niveau",
        soort: "keuze",
        vraag: "Waren de vragen op het juiste niveau?",
        opties: ["Te makkelijk", "Goed", "Te moeilijk", "Verschilt per vak"],
        verplicht: true,
      },
      {
        sleutel: "uitleg_score",
        soort: "score",
        vraag: "Hoe duidelijk was de uitleg bij een fout antwoord?",
        van: 1,
        tot: 5,
        laag: "niet duidelijk",
        hoog: "heel duidelijk",
        verplicht: true,
      },
      {
        sleutel: "fouten",
        soort: "open",
        vraag: "Vond je fouten of onduidelijke vragen? Welke?",
        verplicht: false,
      },
    ],
  },
  {
    titel: "Hoe was het voor wie oefende?",
    vragen: [
      {
        sleutel: "ervaring",
        soort: "open",
        vraag: "Hoe reageerde je kind (of jijzelf) op het platform?",
        hulp: "Een paar zinnen is genoeg.",
        minimum: MINIMUM_OPEN,
        verplicht: true,
      },
      {
        sleutel: "leukst",
        soort: "open",
        vraag: "Wat was het leukst?",
        verplicht: false,
      },
      {
        sleutel: "minder_leuk",
        soort: "open",
        vraag: "Wat was minder leuk of frustrerend?",
        verplicht: false,
      },
    ],
  },
  {
    titel: "Beter maken",
    vragen: [
      {
        sleutel: "verbeteren",
        soort: "open",
        vraag: "Wat is het belangrijkste dat we moeten verbeteren?",
        hulp: "Wees gerust kritisch, daar hebben we het meest aan.",
        minimum: MINIMUM_OPEN,
        verplicht: true,
      },
      {
        sleutel: "houden",
        soort: "open",
        vraag: "Wat moeten we zeker zo houden?",
        minimum: MINIMUM_OPEN,
        verplicht: true,
      },
      {
        sleutel: "missen",
        soort: "open",
        vraag: "Wat mis je nog op het platform?",
        verplicht: false,
      },
    ],
  },
  {
    titel: "Tot slot",
    vragen: [
      {
        sleutel: "punten",
        soort: "score",
        vraag: "Hoeveel punten geef je het oefenplatform?",
        van: 1,
        tot: 10,
        laag: "slecht",
        hoog: "uitstekend",
        verplicht: true,
      },
      {
        sleutel: "aanraden",
        soort: "keuze",
        vraag: "Zou je het platform aanraden aan andere ouders?",
        opties: ["Ja", "Misschien", "Nee"],
        verplicht: true,
      },
      {
        sleutel: "aanraden_waarom",
        soort: "open",
        vraag: "Waarom wel of niet?",
        verplicht: false,
      },
    ],
  },
];

export const ALLE_VRAGEN: EnqueteVraag[] = ENQUETE.flatMap((d) => d.vragen);

export type EnqueteAntwoorden = Record<string, string | string[]>;

/** Leest de antwoorden uit een formulier en zegt wat er nog ontbreekt. */
export function leesEnquete(formData: FormData): {
  antwoorden: EnqueteAntwoorden;
  ontbreekt: string[];
} {
  const antwoorden: EnqueteAntwoorden = {};
  const ontbreekt: string[] = [];

  for (const v of ALLE_VRAGEN) {
    if (v.soort === "meerdere") {
      const gekozen = formData
        .getAll(v.sleutel)
        .map(String)
        .filter((o) => v.opties.includes(o));
      antwoorden[v.sleutel] = gekozen;
      if (v.verplicht && gekozen.length === 0) ontbreekt.push(v.vraag);
      continue;
    }

    const waarde = String(formData.get(v.sleutel) ?? "").trim().slice(0, 3000);
    if (v.soort === "keuze" && waarde && !v.opties.includes(waarde)) continue;
    if (v.soort === "score") {
      const n = Number(waarde);
      if (waarde && (!Number.isInteger(n) || n < v.van || n > v.tot)) continue;
    }
    antwoorden[v.sleutel] = waarde;

    if (v.verplicht && !waarde) {
      ontbreekt.push(v.vraag);
    } else if (v.soort === "open" && v.minimum && waarde.length < v.minimum) {
      ontbreekt.push(`${v.vraag} (schrijf er een paar zinnen bij)`);
    }
  }

  return { antwoorden, ontbreekt };
}
