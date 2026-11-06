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
      /** grijze voorbeeldtekst in het vak, positief én kritisch, zodat mensen weten wat ze kunnen zeggen */
      voorbeeld?: string;
      /** minimum aantal tekens; enkel bij de grote open vragen */
      minimum?: number;
      verplicht: boolean;
    };

export type EnqueteDeel = { titel: string; vragen: EnqueteVraag[] };

/** Bij de grote open vragen: "een paar zinnen". */
/* Was 80, daarna 30. Linda (november 2026) kreeg steeds "te weinig tekens" en
   wist niet meer wat ze nog moest schrijven. Er is geen minimum meer: het vak
   blijft groot, zodat het uitnodigt om iets te schrijven, maar wat iemand
   schrijft, is genoeg. */
export const MINIMUM_OPEN = 0;

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
        voorbeeld: "Bv. 5de leerjaar en 2de middelbaar.",
        vraag: "Welk leerjaar of welke leeftijd hebben de kinderen die oefenden?",
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
        voorbeeld: 'Bv. "Het inloggen lukte pas na een paar keer" of "Alles liep vlot".',
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
        voorbeeld: 'Bv. "Bij breuken stond een antwoord fout" of "Ik vond geen fouten".',
        vraag: "Vond je fouten of onduidelijke vragen? Welke?",
        verplicht: false,
      },
      {
        sleutel: "melding_snelheid",
        soort: "keuze",
        vraag: "Meldde je een fout? Hoe snel was die opgelost?",
        opties: [
          "Ik meldde niets",
          "Binnen een dag",
          "Binnen een week",
          "Na meer dan een week",
          "Nog niet opgelost",
        ],
        verplicht: true,
      },
    ],
  },
  {
    titel: "Rust en sfeer",
    vragen: [
      {
        sleutel: "aangenaam_score",
        soort: "score",
        vraag: "Hoe aangenaam vind je het platform om mee te werken?",
        van: 1,
        tot: 5,
        laag: "helemaal niet",
        hoog: "heel aangenaam",
        verplicht: true,
      },
      {
        sleutel: "prikkelarm_score",
        soort: "score",
        vraag: "Hoe prikkelarm vind je het platform?",
        van: 1,
        tot: 5,
        laag: "veel te druk",
        hoog: "heel rustig",
        verplicht: true,
      },
      {
        sleutel: "zelfstandig",
        soort: "keuze",
        vraag: "Kan je kind er zelfstandig mee werken?",
        opties: ["Ja, helemaal", "Meestal", "Met hulp", "Nee"],
        verplicht: true,
      },
      {
        sleutel: "prikkelarm_uitleg",
        soort: "open",
        voorbeeld: 'Bv. "Fijn dat er geen geluiden zijn" of "Er staat soms te veel tekst op één scherm".',
        vraag: "Wat zorgt voor rust, en wat geeft net te veel prikkels?",
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
        voorbeeld: 'Bv. "Ze oefent graag en vraagt er zelf naar" of "Hij haakte snel af, het was te veel lezen".',
        vraag: "Hoe reageerde je kind (of jijzelf) op het platform?",
        hulp: "Een paar zinnen is genoeg.",
        minimum: MINIMUM_OPEN,
        verplicht: true,
      },
      {
        sleutel: "leukst",
        soort: "open",
        voorbeeld: 'Bv. "De badges" of "De vraag van de dag".',
        vraag: "Wat was het leukst?",
        verplicht: false,
      },
      {
        sleutel: "minder_leuk",
        soort: "open",
        voorbeeld: 'Bv. "Lange uitleg" of "Dat je soms niet weet waar je moet klikken".',
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
        voorbeeld: 'Bv. "Duidelijker waar je moet beginnen" of "Meer oefeningen Frans".',
        vraag: "Wat is het belangrijkste dat we moeten verbeteren?",
        hulp: "Wees gerust kritisch, daar hebben we het meest aan.",
        minimum: MINIMUM_OPEN,
        verplicht: true,
      },
      {
        sleutel: "houden",
        soort: "open",
        voorbeeld: 'Bv. "De rustige opbouw" of "De uitleg bij elke fout".',
        vraag: "Wat moeten we zeker zo houden?",
        minimum: MINIMUM_OPEN,
        verplicht: true,
      },
      {
        sleutel: "missen",
        soort: "open",
        voorbeeld: 'Bv. "Een overzicht voor ouders" of "Oefeningen voor het 3de leerjaar".',
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
        voorbeeld: 'Bv. "Omdat het rustig en duidelijk is" of "Nog niet, eerst meer vakken".',
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
      ontbreekt.push(`${v.vraag} (schrijf er een korte zin bij)`);
    }
  }

  return { antwoorden, ontbreekt };
}
