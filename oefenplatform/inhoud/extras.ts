/*
  De pagina "Leuke extra's" — /extras

  Kim, 9 november 2026: de pagina moest meer orde krijgen. Bovenaan staan nu
  vier grote knoppen, elk met een eigen pagina:

    🎲 Educatieve spellen      /extras/spellen      (de lijst hieronder)
    🔗 Leuke links             /extras/links        (via Beheer > Materiaal)
    🖨️ Afdrukbare documenten   /extras/documenten   (via Beheer > Materiaal)
    🎬 Leuke filmpjes          /extras/filmpjes     (via Beheer > Materiaal)

  Op elke pagina staat alles per schoolniveau: eerst de lagere school, dan de
  middelbare school, en wat voor iedereen is onderaan.

  Links, documenten en filmpjes zet je er zelf bij op /beheer/materiaal: daar
  kies je de soort en voor wie het is. Daar hoef je niets voor in dit bestand
  te veranderen.

  Een spel bijzetten doe je in drie stappen:
  1. Zet het spel als één html-bestand in public/spellen/, bijvoorbeeld
     public/spellen/mijn-spel.html.
  2. Zet hieronder in `spellen` een blokje bij met dezelfde slug. De slug is
     het stukje van het webadres: /extras/mijn-spel.
  3. Zet in `spelKaarten` een kaart per niveau waarvoor het spel is. Heeft het
     spel binnenin een niveaukeuze (zoals de begrippenarena's), zet dan bij
     `niveauInSpel` de naam van dat niveau: het spel opent dan meteen op het
     juiste niveau.

  De spellen kleuren geen vinkje of sterretje van een hoofdstuk in en tellen
  voor geen enkel rapport mee: het is gewoon iets leuks om de begrippen mee in
  te oefenen, alleen of met de hele klas.

  Alles hieronder is tekst, dus je mag hier gewoon in schrijven zonder dat er
  iets stuk kan.
*/

export type School = "lager" | "middelbaar" | "iedereen";
export type Soort = "spellen" | "links" | "documenten" | "filmpjes";

export const extrasTekst = {
  label: "Leuke extra's",
  titel: "Spelletjes, links en meer naast de leerstof",
  intro:
    "Alles wat hier staat, is gratis en je hebt er geen account voor nodig. Het telt nergens voor mee: het is er om op een andere manier met de leerstof bezig te zijn. Kies hieronder wat je zoekt. Op elke pagina staat alles per schoolniveau.",
  volledigScherm: "Op volledig scherm openen",
  terug: "Terug naar de leuke extra's",
  terugNaarSpellen: "Terug naar de educatieve spellen",
  /* Het regeltje onderaan dat naar de tipspagina wijst. */
  tipsVraag: "Zoek je hoe je het oefenplatform zelf het best gebruikt?",
  tipsLinkTekst: "Lees onze tips",
  tipsLink: "/tips",
};

/* De vier grote knoppen bovenaan /extras, in deze volgorde. */
export const soorten: {
  slug: Soort;
  icoon: string;
  titel: string;
  tekst: string;
  /* Wat er staat zolang er nog niets in zit. */
  leeg: string;
}[] = [
  {
    slug: "spellen",
    icoon: "🎲",
    titel: "Educatieve spellen",
    tekst:
      "De begrippenarena's, het wiskundespel en meer. Alleen, met het gezin of met de hele klas op het digibord.",
    leeg: "Hier komen binnenkort spellen bij.",
  },
  {
    slug: "links",
    icoon: "🔗",
    titel: "Leuke links",
    tekst:
      "Sites die we zelf gebruiken en de moeite vinden: naslagwerken, oefensites en plekken om verder te ontdekken.",
    leeg: "Hier komen binnenkort links bij.",
  },
  {
    slug: "documenten",
    icoon: "🖨️",
    titel: "Afdrukbare documenten",
    tekst:
      "Extra bundels en kaarten om af te drukken, zoals de veelgemaakte denkfouten bij breuken of procenten.",
    leeg: "Hier komen binnenkort documenten bij.",
  },
  {
    slug: "filmpjes",
    icoon: "🎬",
    titel: "Leuke filmpjes",
    tekst:
      "Korte filmpjes die iets uit de leerstof op een andere manier uitleggen of laten zien.",
    leeg: "Hier komen binnenkort filmpjes bij.",
  },
];

/* De koppen per schoolniveau, in deze volgorde op elke pagina. */
export const scholen: { slug: School; titel: string; tekst: string }[] = [
  {
    slug: "lager",
    titel: "Lagere school",
    tekst: "🧱 Basis en 🌱 Start, voor het 5de en 6de leerjaar",
  },
  {
    slug: "middelbaar",
    titel: "Middelbare school",
    tekst: "✨ Spark, 🚀 Boost en 🌍 Beyond, van het 1ste tot het 6de middelbaar",
  },
  {
    slug: "iedereen",
    titel: "Voor iedereen",
    tekst: "Leuk op elke leeftijd",
  },
];

/* Elk spel één keer: het html-bestand in public/spellen/ heet slug.html. */
export type Spel = {
  slug: string;
  icoon: string;
  titel: string;
};

export const spellen: Spel[] = [
  { slug: "begrippenarena", icoon: "🏛️", titel: "Begrippenarena Geschiedenis" },
  { slug: "woordenarena-engels", icoon: "💂", titel: "Woordenarena Engels" },
  { slug: "begrippenarena-natuur", icoon: "🔬", titel: "Begrippenarena Natuurwetenschappen" },
  { slug: "begrippenarena-wiskunde", icoon: "📐", titel: "Begrippenarena Wiskunde" },
  { slug: "begrippenarena-economie", icoon: "📊", titel: "Begrippenarena Economie" },
  { slug: "begrippenarena-aardrijkskunde", icoon: "🌋", titel: "Begrippenarena Aardrijkskunde" },
  { slug: "begrippenarena-nederlands", icoon: "📚", titel: "Begrippenarena Nederlands" },
  { slug: "woordenarena-frans", icoon: "🥖", titel: "Woordenarena Frans" },
  { slug: "begrippenarena-techniek", icoon: "⚙️", titel: "Begrippenarena Techniek" },
  { slug: "begrippenarena-mens", icoon: "🤝", titel: "Begrippenarena Mens en samenleving" },
  { slug: "begrippenarena-uitdagingshoek", icoon: "🔭", titel: "Begrippenarena Uitdagingshoek" },
  { slug: "wiskunde-dimensie", icoon: "🤖", titel: "De Wiskunde-dimensie" },
  /* Prikkelarme spellen voor het lager (Kim, 9 november 2026): geen klok,
     geen geluid, geen punten, een rustige tip bij een fout. */
  { slug: "breukenpizza", icoon: "🍕", titel: "Breukenpizza" },
  { slug: "foutenspeurder", icoon: "🔍", titel: "Foutenspeurder" },
  { slug: "tijdlijn", icoon: "🕰️", titel: "Tijdlijn leggen" },
  { slug: "kaartpuzzel", icoon: "🗺️", titel: "Kaartpuzzel" },
];

/*
  De kaarten op /extras/spellen. Een spel met meerdere niveaus krijgt een
  kaart per niveau, zodat meteen duidelijk is welk niveau je moet kiezen.
    spel          de slug uit `spellen` hierboven
    school        "lager", "middelbaar" of "iedereen"
    niveau        wat er groot op de kaart staat, bv. "🌱 Start · 5de en 6de leerjaar"
    niveauInSpel  mag weg; het niveau waarop het spel meteen opent
    tekst         één of twee zinnen over wat je er doet
*/
export type SpelKaart = {
  spel: string;
  school: School;
  niveau: string;
  niveauInSpel?: string;
  tekst: string;
};

const zesSpellen =
  "In zes spellen: een quiz, memory, raad het begrip, galgje, flitskaarten en bingo.";

const zevenSpellenAk =
  "In zeven spellen: een quiz, memory, raad het begrip, vulkaangalgje, flitskaarten, bingo en fotoraden met echte foto's.";

const zevenSpellenNl =
  "In zeven spellen: een quiz, memory, raad het begrip, boekengalgje, flitskaarten, bingo en de zinsdelenjager, waarin je zelf het gevraagde zinsdeel aantikt.";

const zevenSpellenFr =
  "In zeven spellen: een quiz, memory, raad het woord, Eiffeltorengalgje, flitskaarten, bingo en le of la?, waarin je kiest of een woord mannelijk of vrouwelijk is.";

const zevenSpellenTech =
  "In zeven spellen: een quiz, memory, raad het begrip, robotgalgje, flitskaarten, bingo en de sorteerband, waarin je voorwerpen in de juiste bak sorteert, zoals geleider of isolator.";

const zevenSpellenMens =
  "In zeven spellen: een quiz, memory, raad het begrip, huizengalgje, flitskaarten, bingo en het sorteerspel, waarin je bijvoorbeeld een uitspraak bij het juiste stadium of de juiste macht legt.";

const zevenSpellenHoek =
  "In zeven spellen: een quiz, memory, raad het begrip, raketgalgje, flitskaarten, bingo en het sorteerspel, waarin je bijvoorbeeld kiest tussen planeet en maan of tussen feit en fabel.";

export const spelKaarten: SpelKaart[] = [
  /* Lagere school */
  {
    spel: "woordenarena-engels",
    school: "lager",
    niveau: "🌱 Start · 5de en 6de leerjaar",
    niveauInSpel: "start",
    tekst:
      "Ruim tachtig Engelse woorden en zinnetjes uit de leerbundels van Start: dagen, kleuren, familie, je lichaam, jezelf voorstellen en wat je zegt in de klas. In zes spellen.",
  },
  {
    spel: "begrippenarena-wiskunde",
    school: "lager",
    niveau: "🧱 Basis en 🌱 Start · 5de en 6de leerjaar",
    niveauInSpel: "lager",
    tekst: `De wiskundewoorden van de lagere school, zoals som, quotiënt en noemer. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena",
    school: "lager",
    niveau: "🌱 Start · 5de en 6de leerjaar",
    niveauInSpel: "start",
    tekst: `De begrippen uit de leerbundels geschiedenis van Start. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-aardrijkskunde",
    school: "lager",
    niveau: "🌱 Start · 5de en 6de leerjaar",
    niveauInSpel: "start",
    tekst: `Kaartlezen, België en Europa en de wereld: van legende en windroos tot polders, oase en Europese Unie. ${zevenSpellenAk}`,
  },
  {
    spel: "begrippenarena-nederlands",
    school: "lager",
    niveau: "🧱 Basis en 🌱 Start · 5de en 6de leerjaar",
    niveauInSpel: "lager",
    tekst: `De taalwoorden van de lagere school, van hoofdgedachte en persoonsvorm tot fabel en cliffhanger. ${zevenSpellenNl}`,
  },
  {
    spel: "woordenarena-frans",
    school: "lager",
    niveau: "🧱 Basis en 🌱 Start · 5de en 6de leerjaar",
    niveauInSpel: "lager",
    tekst: `Bijna honderdvijftig Franse woorden uit de leerbundels: de dagen, de familie, de school, de markt, de dieren en de zee. ${zevenSpellenFr}`,
  },
  {
    spel: "begrippenarena-techniek",
    school: "lager",
    niveau: "🌱 Start · Wetenschap en techniek, 5de en 6de leerjaar",
    niveauInSpel: "lager",
    tekst: `Ruim negentig begrippen uit de zeven leerbundels wetenschap en techniek, van fotosynthese en het menselijk lichaam tot stroomkringen, ontwerpen en de ruimte. ${zevenSpellenTech}`,
  },
  {
    spel: "wiskunde-dimensie",
    school: "lager",
    niveau: "🌱 Start · vier niveaus, van starter tot genie",
    tekst:
      "Een game van Mats. Robothond Tollie en kat Majol verslaan de monsters uit de anti-wiskunde-dimensie met plus en min, maal en delen en getallenreeksen. Wie veel goed heeft na elkaar, krijgt vanzelf moeilijkere sommen. Geen tijdslimiet.",
  },
  {
    spel: "breukenpizza",
    school: "lager",
    niveau: "🧱 Basis en 🌱 Start · rustig spel",
    tekst:
      "Welke breuk zie je op de pizza? Of kleur zelf de stukken in tot je dezelfde breuk hebt. Geen klok en geen punten, wel een tip als je even vastzit.",
  },
  {
    spel: "foutenspeurder",
    school: "lager",
    niveau: "🌱 Start · 5de en 6de leerjaar · rustig spel",
    tekst:
      "In elke berekening zit één foute stap. Tik hem aan en lees waarom hij fout is. Met breuken, procenten en rekenen en meten.",
  },
  {
    spel: "tijdlijn",
    school: "lager",
    niveau: "🌱 Start · 5de en 6de leerjaar · rustig spel",
    tekst:
      "Zet de kaartjes in de juiste volgorde, van vroeger naar nu: de grote periodes, de oudheid, de geschiedenis van ons land en uitvindingen.",
  },
  {
    spel: "kaartpuzzel",
    school: "lager",
    niveau: "🧱 Basis en 🌱 Start · rustig spel",
    tekst:
      "Zoek de provincies van België of de landen van Europa op een lege kaart. Tik je mis, dan hoor je in welke richting je moet zoeken.",
  },

  /* Middelbare school */
  {
    spel: "begrippenarena-wiskunde",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste graad (1ste en 2de middelbaar)",
    niveauInSpel: "spark",
    tekst: `De wiskundewoorden van de 1ste graad. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst: `De begrippen uit de leerbundels geschiedenis van Spark. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-natuur",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst: `Honderdzestig begrippen uit de tien leerbundels natuurwetenschappen van Spark, van de cel tot wetenschappelijk onderzoek. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-natuur",
    school: "middelbaar",
    niveau: "🚀 Boost · biologie, chemie en fysica",
    niveauInSpel: "boost",
    tekst: `Ruim honderd begrippen uit biologie, chemie, fysica en natuurwetenschappen van Boost (ook dubbele finaliteit), van het zenuwstelsel en ecologie tot atomen, krachten en de wet van Ohm. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-natuur",
    school: "middelbaar",
    niveau: "🌍 Beyond · biologie, chemie en fysica",
    niveauInSpel: "beyond",
    tekst: `Ruim honderdtwintig begrippen uit biologie, chemie, fysica en natuurwetenschappen van Beyond (ook dubbele finaliteit), van afweer, DNA en evolutie tot evenwichten, redox, magnetisme en kernfysica. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-aardrijkskunde",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst: `Honderdzestig begrippen uit de tien leerbundels aardrijkskunde van Spark, van kaart lezen en klimaatzones tot verwering en Geopunt. ${zevenSpellenAk}`,
  },
  {
    spel: "begrippenarena-nederlands",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst: `Honderd begrippen uit de tien leerbundels Nederlands van Spark, van tekstsoorten en signaalwoorden tot beeldspraak en zinsdelen. ${zevenSpellenNl}`,
  },
  {
    spel: "woordenarena-frans",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst: `Ruim tweehonderdvijftig Franse woorden uit de leerbundels van Spark, van eten en drinken en de school tot mensen beschrijven en de tijd. ${zevenSpellenFr}`,
  },
  {
    spel: "begrippenarena-techniek",
    school: "middelbaar",
    niveau: "✨ Spark · Techniek, 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst: `Honderddertig begrippen uit de elf leerbundels techniek van Spark, van materialen en stroomkringen tot overbrengingen, het technisch proces en algoritmen. ${zevenSpellenTech}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "✨ Spark · Samenleving en economie",
    niveauInSpel: "se_spark",
    tekst: `Bijna negentig begrippen uit de tien leerbundels samenleving en economie, van identiteit en eerste hulp tot democratie, België, de economische kringloop en veilig online. ${zevenSpellenMens}`,
  },
  {
    spel: "woordenarena-engels",
    school: "middelbaar",
    niveau: "✨ Spark · 1ste en 2de middelbaar",
    niveauInSpel: "spark",
    tekst:
      "Bijna tweehonderd Engelse woorden uit de leerbundels van Spark, met de valse vrienden, Brits tegenover Amerikaans en de onregelmatige werkwoorden. In zes spellen.",
  },
  {
    spel: "woordenarena-engels",
    school: "middelbaar",
    niveau: "🚀 Boost · ook dubbele finaliteit",
    niveauInSpel: "boost",
    tekst:
      "Ruim honderd Engelse woorden uit de woordvelden van Boost: gevoelens en gezondheid, thuis en kleding, school en beroepen, reizen en winkelen. In zes spellen.",
  },
  {
    spel: "woordenarena-engels",
    school: "middelbaar",
    niveau: "🌍 Beyond · ook dubbele finaliteit",
    niveauInSpel: "beyond",
    tekst:
      "Bijna tweehonderdvijftig Engelse woorden uit de woordvelden van Beyond, van wonen en gezondheid tot werk, geld, kunst, politiek en wetenschap. In zes spellen.",
  },
  {
    spel: "begrippenarena-wiskunde",
    school: "middelbaar",
    niveau: "🚀 Boost · 2de graad (3de en 4de middelbaar)",
    niveauInSpel: "boost",
    tekst: `De wiskundewoorden van de 2de graad. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-aardrijkskunde",
    school: "middelbaar",
    niveau: "🚀 Boost · 2de graad, doorstroom en dubbele finaliteit",
    niveauInSpel: "boost",
    tekst: `Ruim honderdtwintig begrippen, van bevolking en migratie tot mondialisering, duurzaamheid en het versterkte broeikaseffect. ${zevenSpellenAk}`,
  },  {
    spel: "begrippenarena-nederlands",
    school: "middelbaar",
    niveau: "🚀 Boost · 2de graad, doorstroom en dubbele finaliteit",
    niveauInSpel: "boost",
    tekst: `Ruim honderdvijfentwintig begrippen, van ruis en framing tot woordsoorten, zinsdelen, vertelperspectief en rijmschema's. ${zevenSpellenNl}`,
  },
  {
    spel: "woordenarena-frans",
    school: "middelbaar",
    niveau: "🚀 Boost · 2de graad, doorstroom en dubbele finaliteit",
    niveauInSpel: "boost",
    tekst: `Bijna tweehonderd Franse woorden, van op restaurant en de mens tot de samenleving en de woorden van de grammatica. ${zevenSpellenFr}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🚀 Boost · Sociale en gedragswetenschappen",
    niveauInSpel: "sgw_boost",
    tekst: `Bijna negentig begrippen, van Piaget, Kohlberg en Erikson tot cultuur, socialisatie, sociale groepen en status. ${zevenSpellenMens}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🚀 Boost · Kunstbeschouwing en filosofie",
    niveauInSpel: "kf_boost",
    tekst: `Bijna zestig begrippen, van kunstcriteria en kunststromingen tot de eerste filosofen, lichaam en geest en ethiek. ${zevenSpellenMens}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🚀 Boost dubbele finaliteit · Gezondheid, zorg en welzijn",
    niveauInSpel: "gzw",
    tekst: `Bijna vijftig begrippen, van zintuigen en eerste hulp tot voedselveiligheid, interieurzorg en linnenzorg. ${zevenSpellenMens}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🚀 Boost dubbele finaliteit · Ontwikkeling en pedagogisch handelen",
    niveauInSpel: "oph",
    tekst: `Ruim veertig begrippen, van welzijn en de ontwikkeling van kind tot oudere tot observeren, communiceren en spel. ${zevenSpellenMens}`,
  },

  {
    spel: "begrippenarena",
    school: "middelbaar",
    niveau: "🚀 Boost · ook dubbele finaliteit",
    niveauInSpel: "boost",
    tekst: `Ruim honderdveertig begrippen, van het referentiekader en de Franken tot de Verlichting, de industriële revolutie en werken met bronnen. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-economie",
    school: "middelbaar",
    niveau: "🚀 Boost · 2de graad (3de en 4de middelbaar)",
    niveauInSpel: "boost",
    tekst: `Bijna tachtig begrippen economie van de 2de graad, van behoeften en nut tot de marketingmix en dubbel boekhouden. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-economie",
    school: "middelbaar",
    niveau: "🚀 Boost dubbele finaliteit · Toegepaste economie",
    niveauInSpel: "toegepast",
    tekst: `Bijna honderdveertig begrippen, van de balans, het MAR en de btw tot het rekenblad, printen, bestanden en databanken. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-wiskunde",
    school: "middelbaar",
    niveau: "🌍 Beyond · 3de graad (5de en 6de middelbaar)",
    niveauInSpel: "beyond",
    tekst: `De wiskundewoorden van de 3de graad. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-wiskunde",
    school: "middelbaar",
    niveau: "🌍 Beyond · wiskunde basis (5de en 6de middelbaar)",
    niveauInSpel: "basis",
    tekst: `Ruim tachtig begrippen bij het vak wiskunde basis, van functies, afgeleiden en rijen tot kansen, de normale verdeling en de extra's voor bedrijfswetenschappen. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena",
    school: "middelbaar",
    niveau: "🌍 Beyond · ook dubbele finaliteit",
    niveauInSpel: "beyond",
    tekst: `Honderdzestig begrippen, van het referentiekader tot China, Israël-Palestina en de kunststromingen. Ook bruikbaar voor Beyond dubbele finaliteit, dat grotendeels dezelfde hoofdstukken heeft. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-natuur",
    school: "middelbaar",
    niveau: "🌍 Beyond · welzijnswetenschappen",
    niveauInSpel: "welzijn",
    tekst: `Ruim honderd begrippen over het menselijk lichaam, voor de richting welzijnswetenschappen. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-economie",
    school: "middelbaar",
    niveau: "🌍 Beyond · 3de graad doorstroom (5de en 6de middelbaar)",
    niveauInSpel: "beyond",
    tekst: `Honderd begrippen algemene economie, van de kringloop en de markt tot geld, inflatie en economisch onderzoek. ${zesSpellen}`,
  },
  {
    spel: "begrippenarena-economie",
    school: "middelbaar",
    niveau: "🌍 Beyond · bedrijfswetenschappen (5de en 6de middelbaar)",
    niveauInSpel: "bedrijf",
    tekst: `Bijna tachtig begrippen bedrijfswetenschappen en recht, van ondernemingsvormen en boekhouden tot kerncijfers, marketing, de arbeidsovereenkomst en databanken. ${zesSpellen}`,
  },  {
    spel: "begrippenarena-aardrijkskunde",
    school: "middelbaar",
    niveau: "🌍 Beyond · 3de graad, doorstroom en dubbele finaliteit",
    niveauInSpel: "beyond",
    tekst: `Ruim tweehonderddertig begrippen in eenentwintig hoofdstukken, van het heelal en de atmosfeer tot platentektoniek, gesteenten en ruimtelijke ordening. ${zevenSpellenAk}`,
  },  {
    spel: "begrippenarena-nederlands",
    school: "middelbaar",
    niveau: "🌍 Beyond · 3de graad, doorstroom en dubbele finaliteit",
    niveauInSpel: "beyond",
    tekst: `Honderdvijfenvijftig begrippen in negentien hoofdstukken, van drogredenen en stijlfiguren tot literaire stromingen, semantiek en zinsbouw. ${zevenSpellenNl}`,
  },
  {
    spel: "woordenarena-frans",
    school: "middelbaar",
    niveau: "🌍 Beyond · 3de graad, doorstroom en dubbele finaliteit",
    niveauInSpel: "beyond",
    tekst: `Vijfenzeventig Franse woorden voor literatuur, mens en samenleving, met verbindingswoorden en uitdrukkingen om je mening te geven. ${zevenSpellenFr}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🌍 Beyond · Sociale en gedragswetenschappen",
    niveauInSpel: "sgw_beyond",
    tekst: `Vijfenzeventig begrippen, van de ontwikkelingstheorieën en sociale psychologie tot persoonlijkheid, opvoeden, sociologie en media. ${zevenSpellenMens}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🌍 Beyond · Filosofie en recht",
    niveauInSpel: "filorecht",
    tekst: `Bijna veertig begrippen, van rationalisme en falsificatie tot vrijheid, ethiek, de rechtsstaat en justitie. ${zevenSpellenMens}`,
  },
  {
    spel: "begrippenarena-mens",
    school: "middelbaar",
    niveau: "🌍 Beyond · Samenleving en economie",
    niveauInSpel: "se_beyond",
    tekst: `Ruim vijftig begrippen, van identiteit en reanimatie tot belastingen, de markt, je loonfiche, krediet, beleggen en verzekeren. ${zevenSpellenMens}`,
  },

  {
    spel: "begrippenarena-uitdagingshoek",
    school: "iedereen",
    niveau: "🔭 Uitdagingshoek · De ruimte",
    niveauInSpel: "ruimte",
    tekst: `Bijna tachtig begrippen uit de uitdagingshoek, van lichtjaar en zwart gat tot zonnestorm, komeet en Joeri Gagarin. ${zevenSpellenHoek}`,
  },
  {
    spel: "begrippenarena-uitdagingshoek",
    school: "iedereen",
    niveau: "🔭 Uitdagingshoek · Coderen en computers",
    niveauInSpel: "code",
    tekst: `Tachtig begrippen, van bit en byte tot algoritme, phishing, de Caesarcode en hexadecimale kleurcodes. ${zevenSpellenHoek}`,
  },
  {
    spel: "begrippenarena-uitdagingshoek",
    school: "iedereen",
    niveau: "🔭 Uitdagingshoek · Geschiedenis van België",
    niveauInSpel: "belgie",
    tekst: `Bijna tachtig begrippen, van Ambiorix en Karel V tot de Belgische Revolutie, het IJzerfront en de staatshervormingen. ${zevenSpellenHoek}`,
  },
  {
    spel: "begrippenarena-uitdagingshoek",
    school: "iedereen",
    niveau: "🔭 Uitdagingshoek · Paradoxen en weetjes",
    niveauInSpel: "paradox",
    tekst: `Bijna zeventig begrippen, van het hotel van Hilbert en de verjaardagsparadox tot overlevingsbias en het duivenhokprincipe. ${zevenSpellenHoek}`,
  },
];

export function vindSpel(slug: string) {
  return spellen.find((spel) => spel.slug === slug);
}

/* Bij een link of document dat nog geen soort kreeg in Beheer: een pdf is een
   document, al de rest een link. */
export function soortVan(rij: { soort?: string | null; type: string }): Soort {
  if (rij.soort === "links" || rij.soort === "documenten" || rij.soort === "filmpjes") {
    return rij.soort;
  }
  return rij.type === "pdf" ? "documenten" : "links";
}

export function schoolVan(rij: { schoolniveau?: string | null }): School {
  if (rij.schoolniveau === "lager" || rij.schoolniveau === "middelbaar") return rij.schoolniveau;
  return "iedereen";
}
