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
  /* Uit website/supabase/aanvragen-status.sql. Staan ze er nog niet, dan
     zijn ze leeg. */
  stappen?: string[];
  gearchiveerd?: boolean;
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
  if (vraag.startsWith(AFGEZEGD)) return false;
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

/*
  Eén regel op een lijst is één kind, niet één aanvraag.

  Kim op 28 oktober 2026: "als ouders hun kinderen in 1 aanvraag zetten telt
  die dit als 1 kind ipv 2". Een gezin met twee kinderen vult het formulier
  één keer in en typt "Olivia en Juliette", met als leeftijd "6 en 9". Die
  aanvraag wordt hier twee regels, elk met de gegevens van dezelfde ouder.

  We knippen op "en", een komma, "&", "+" en "/". Komt het aantal leeftijden
  overeen met het aantal namen, dan krijgt elk kind zijn eigen leeftijd; zo
  niet, dan staat de hele leeftijd bij elk kind, zodat er niets verloren gaat.
*/
export type Rij = {
  sleutel: string;
  kind: string;
  leeftijd: string | null;
  aanvraag: Aanvraag;
};

const SCHEIDING = /\s*(?:,|&|\+|\/|\ben\b)\s*/i;

function knip(tekst: string) {
  return tekst
    .split(SCHEIDING)
    .map((t) => t.trim())
    .filter(Boolean);
}

export function kinderenVan(aanvraag: Aanvraag): Rij[] {
  const naam = vindWaarde(aanvraag.gegevens, "naam van het kind")?.trim() ?? "";
  const leeftijd = vindWaarde(aanvraag.gegevens, "leeftijd")?.trim() || null;
  const namen = knip(naam);
  if (namen.length <= 1) {
    return [{ sleutel: aanvraag.id, kind: naam || "—", leeftijd, aanvraag }];
  }
  const leeftijden = leeftijd ? knip(leeftijd) : [];
  return namen.map((kind, i) => ({
    sleutel: `${aanvraag.id}-${i}`,
    kind,
    leeftijd:
      leeftijden.length === namen.length ? leeftijden[i] : leeftijd,
    aanvraag,
  }));
}

/*
  Reclame van robots. De website (website/lib/spamcheck.ts) bewaart een
  verdacht formulier met als soort "spam: <gewone soort>" en de reden in
  de gegevens. Het staat op het tabblad Spam van de aanvragen en nooit op
  een lijst. Terugzetten haalt het voorvoegsel er gewoon weer af.
*/
export const SPAM_VOORVOEGSEL = "spam: ";
export const SPAM_REDEN = "Waarom bij spam";

export function isSpam(aanvraag: Pick<Aanvraag, "soort">) {
  return aanvraag.soort.startsWith(SPAM_VOORVOEGSEL);
}

/* Kinderen die Kim zelf op een lijst zette, zonder dat er een formulier
   was. Ze staan ook in de tabel aanvragen, met deze soort. */
export const MET_DE_HAND = "met de hand";

/*
  Gaat een aanvraag over een kind dat ergens komt (een kamp, een plusklas, de
  winactie), of over iets anders?

  Kim op 2 november 2026: bij de lijsten "lijkt alles precies kampen", ook
  de aanvragen om op de website te komen. Dat komt doordat elk aangevinkt
  vakje een lijst werd: een professional die "Opname in de wegwijzer"
  aanvinkt, stond zo als een kampdag met een knop om fiches af te drukken.
  Een kinderlijst bouwen we nu enkel uit een aanvraag met de naam van een
  kind; de rest staat apart, als gewone lijst van wie wat aanvinkte.
*/
export function gaatOverEenKind(aanvraag: Aanvraag) {
  if (aanvraag.soort === MET_DE_HAND) return true;
  return Boolean(vindWaarde(aanvraag.gegevens, "naam van het kind")?.trim());
}

/* De naam van wie een andere aanvraag instuurde: de professional, de
   sponsor, de tiener die wil meetesten. */
export function afzenderVan(aanvraag: Aanvraag) {
  return (
    vindWaarde(aanvraag.gegevens, "naam van de ouders") ??
    aanvraag.gegevens["Naam"] ??
    vindWaarde(aanvraag.gegevens, "naam") ??
    "—"
  );
}

export type Groep = {
  naam: string;
  onderwerpen: string[];
  aanvragen: Aanvraag[];
  rijen: Rij[];
  /* Wie voor deze dag afzegde: staat niet meer op de lijst, wel eronder. */
  afgezegd: Rij[];
};

/*
  Afzeggen voor één dag.

  Kim op 3 november 2026: "ik kan nu olivia en juliette niet verwijderen die
  afgezegd hebben". De inschrijving zelf blijft bestaan (daar staat wat de
  ouder vroeg en of er betaald is); in de gegevens komt er een sleutel
  "Afgezegd voor <dag>" bij met de namen van de kinderen die niet komen.
  Zo kan je bij een gezin van twee ook maar één kind laten afzeggen, en is
  het ongedaan te maken.
*/
export const AFGEZEGD = "Afgezegd voor ";

const gewoon = (naam: string) =>
  naam.normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toLowerCase();

export function afgezegdVoor(aanvraag: Aanvraag, dag: string) {
  const waarde = aanvraag.gegevens[AFGEZEGD + dag] ?? "";
  return waarde
    .split(",")
    .map((n) => n.trim())
    .filter(Boolean);
}

export function heeftAfgezegd(rij: Rij, dag: string) {
  return afgezegdVoor(rij.aanvraag, dag).some(
    (n) => gewoon(n) === gewoon(rij.kind),
  );
}

/*
  Per aangekruiste keuze de aanvragen die ze aankruisten. Eén aanvraag kan in
  meerdere groepen staan: wie twee kampdagen aanvinkt, hoort op allebei de
  lijsten thuis.
*/
export function maakGroepen(aanvragen: Aanvraag[]): Groep[] {
  const perNaam = new Map<string, Aanvraag[]>();
  for (const aanvraag of aanvragen) {
    /* Een robot vinkt alles aan; dat hoort op geen enkele lijst. */
    if (isSpam(aanvraag)) continue;
    for (const [vraag, antwoord] of Object.entries(aanvraag.gegevens)) {
      if (!isKeuze(vraag, antwoord)) continue;
      perNaam.set(vraag, [...(perNaam.get(vraag) ?? []), aanvraag]);
    }
  }

  const groepen: Groep[] = [...perNaam.entries()].map(([naam, lijst]) => {
    /* Binnen een groep op naam van het kind, want zo lees je een lijst af. */
    const alle = lijst
      .flatMap(kinderenVan)
      .sort((a, b) => a.kind.localeCompare(b.kind, "nl"));
    const rijen = alle.filter((r) => !heeftAfgezegd(r, naam));
    const blijven = new Set(rijen.map((r) => r.aanvraag.id));
    return {
      naam,
      onderwerpen: [...new Set(lijst.map((a) => a.onderwerp))],
      /* Een gezin waarvan elk kind afzegde, krijgt ook geen mail meer
         van deze dag. */
      aanvragen: lijst.filter((a) => blijven.has(a.id)),
      rijen,
      afgezegd: alle.filter((r) => heeftAfgezegd(r, naam)),
    };
  });

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

/* Wat er in een kolom komt: de naam en de leeftijd van dit ene kind, de
   rest van de aanvraag waar het uit komt. */
export function waardeVan(rij: Rij, woord: string) {
  if (woord === "naam van het kind") return rij.kind;
  if (woord === "leeftijd") return rij.leeftijd;
  return vindWaarde(rij.aanvraag.gegevens, woord);
}

/* De hele groep als tabel met tabs ertussen, klaar om in een rekenblad of in
   een tekstverwerker te plakken. */
export function alsTabel(groep: Groep) {
  const regels = [
    [...KOLOMMEN.map((k) => k.kop), "Boodschap"].join("\t"),
    ...groep.rijen.map((rij) =>
      [
        ...KOLOMMEN.map((k) => waardeVan(rij, k.woord) ?? ""),
        (vindWaarde(rij.aanvraag.gegevens, "vraag of boodschap") ?? "").replace(/\s+/g, " "),
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
