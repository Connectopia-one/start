/*
  Lijsten trekken uit de aanvragen van de website.

  Kim op 11 oktober 2026: "kan ik in het beheerscherm ergens een tab bij hebben
  dat ik onmiddellijk een lijst heb van de kindjes per kamp of per inschrijving,
  zodat ik direct lijsten kan trekken met de belangrijke info."

  Een aanvraag bewaart de antwoorden in `gegevens`, met de vraag zoals de
  bezoeker ze las als sleutel. De aankruisvakjes van het inschrijfformulier
  komen daar binnen als een eigen sleutel met de waarde "ja", bijvoorbeeld
  "Hasselt maandag 2 november": "ja". Elke aangekruiste keuze is dus al een
  groep; we hoeven hier geen lijst kampdagen bij te houden. Zet de website er
  morgen een kampdag bij, dan verschijnt die hier vanzelf.
*/

export type Aanvraag = {
  id: string;
  onderwerp: string;
  soort: string;
  gegevens: Record<string, string>;
  gezien: boolean;
  afgehandeld: boolean;
  created_at: string;
};

/*
  Uit de antwoorden halen we het mailadres en het telefoonnummer naar boven,
  want dat is wat je nodig hebt om iemand terug te contacteren. De namen van
  de vakjes staan in website/content/formulier.ts; herkennen op een woord in
  de vraag werkt ook als die vraag ooit anders geformuleerd wordt.
*/
export function vindWaarde(gegevens: Record<string, string>, woord: string) {
  const sleutel = Object.keys(gegevens).find((k) =>
    k.toLowerCase().includes(woord),
  );
  return sleutel ? gegevens[sleutel] : null;
}

/* Het vinkje waarmee iemand toestemming geeft, is geen keuze waar je een
   lijst van trekt: dat staat bij iederéén op ja. */
function isKeuze(vraag: string, antwoord: string) {
  if (antwoord.trim().toLowerCase() !== "ja") return false;
  return !vraag.toLowerCase().includes("akkoord");
}

const MAANDEN = [
  "januari",
  "februari",
  "maart",
  "april",
  "mei",
  "juni",
  "juli",
  "augustus",
  "september",
  "oktober",
  "november",
  "december",
];

/*
  De groepen op volgorde van de kalender zetten, niet op alfabet. Anders komt
  "Genk woensdag 4 november" voor "Hasselt maandag 2 november", en dat leest
  niet als een reeks kampdagen.

  We zoeken een dag en een maand in de naam van de keuze ("maandag 2 november",
  "21 december"). Het schooljaar begint in september, dus september krijgt
  rang 0 en augustus rang 11; zo volgt december op november en komt februari
  daarna, zonder dat er ergens een jaartal moet staan. Een keuze zonder datum,
  zoals "Een latere vakantie", krijgt geen rang en komt achteraan.
*/
export function datumRang(naam: string): number | null {
  const tekst = naam.toLowerCase();
  const maand = MAANDEN.findIndex((m) => tekst.includes(m));
  if (maand < 0) return null;
  const nummer = Number(tekst.match(/\d{1,2}/)?.[0] ?? 0);
  const schoolmaand = (maand + 4) % 12; /* september wordt 0 */
  return schoolmaand * 100 + nummer;
}

export type Groep = {
  naam: string;
  onderwerpen: string[];
  aanvragen: Aanvraag[];
};

/*
  Per aangekruiste keuze de aanvragen die ze aankruisten. Eén aanvraag kan in
  meerdere groepen staan: wie twee kampdagen aanvinkt, hoort op allebei de
  lijsten thuis.
*/
export function maakGroepen(aanvragen: Aanvraag[]): Groep[] {
  const perNaam = new Map<string, Aanvraag[]>();
  for (const aanvraag of aanvragen) {
    for (const [vraag, antwoord] of Object.entries(aanvraag.gegevens)) {
      if (!isKeuze(vraag, antwoord)) continue;
      perNaam.set(vraag, [...(perNaam.get(vraag) ?? []), aanvraag]);
    }
  }

  const groepen: Groep[] = [...perNaam.entries()].map(([naam, lijst]) => ({
    naam,
    onderwerpen: [...new Set(lijst.map((a) => a.onderwerp))],
    /* Binnen een groep op naam van het kind, want zo lees je een lijst af. */
    aanvragen: [...lijst].sort((a, b) =>
      (vindWaarde(a.gegevens, "naam van het kind") ?? "").localeCompare(
        vindWaarde(b.gegevens, "naam van het kind") ?? "",
        "nl",
      ),
    ),
  }));

  return groepen.sort((a, b) => {
    const ra = datumRang(a.naam);
    const rb = datumRang(b.naam);
    if (ra !== null && rb !== null) return ra - rb;
    if (ra !== null) return -1;
    if (rb !== null) return 1;
    return a.naam.localeCompare(b.naam, "nl");
  });
}

/* De kolommen van een lijst, in de volgorde waarin je ze nodig hebt op een
   dag zelf: eerst wie het is, dan hoe je de ouder bereikt. */
export const KOLOMMEN = [
  { kop: "Kind", woord: "naam van het kind" },
  { kop: "Leeftijd", woord: "leeftijd" },
  { kop: "Ouder", woord: "naam van de ouders" },
  { kop: "Gsm", woord: "gsm" },
  { kop: "E-mail", woord: "mail" },
  { kop: "Gemeente", woord: "gemeente" },
] as const;

/* De hele groep als tabel met tabs ertussen, klaar om in een rekenblad of in
   een tekstverwerker te plakken. */
export function alsTabel(groep: Groep) {
  const regels = [
    [...KOLOMMEN.map((k) => k.kop), "Boodschap"].join("\t"),
    ...groep.aanvragen.map((a) =>
      [
        ...KOLOMMEN.map((k) => vindWaarde(a.gegevens, k.woord) ?? ""),
        (vindWaarde(a.gegevens, "vraag of boodschap") ?? "").replace(/\s+/g, " "),
      ].join("\t"),
    ),
  ];
  return regels.join("\n");
}

/* De mailadressen van een groep, elk één keer, achter puntkomma's voor het
   bcc-vak. */
export function adressenVan(aanvragen: Aanvraag[]) {
  return Array.from(
    new Set(
      aanvragen
        .map((a) => vindWaarde(a.gegevens, "mail")?.trim())
        .filter((m): m is string => !!m && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m))
        .map((m) => m.toLowerCase()),
    ),
  );
}
