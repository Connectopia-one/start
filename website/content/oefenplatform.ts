/*
  De pagina www.connectopia.one/oefenplatform.

  Waarom deze pagina bestaat: tot 12 oktober 2026 sprong de tegel op de
  startpagina rechtstreeks naar oefenplatform.connectopia.one. Wie nog geen lid
  was, kwam dus meteen op een inlogscherm terecht, zonder uitleg en zonder
  prijs. Een ouder die thuisonderwijs geeft schreef ons dat ze geen enkele
  manier vond om toegang te vragen. Deze pagina staat daartussen: eerst lezen
  wat het is, dan pas inloggen of starten.

  Wat kan je hier aanpassen zonder code?
    prijsNu / prijsStraks   de bedragen. LET OP: die moeten gelijk zijn aan
                            oefenplatform/lib/prijs.ts, want dat bestand bepaalt
                            wat er écht afgerekend wordt. Pas allebei aan.
    niveaus                 de acht categorieën en wat erin zit
    hoortErbij              wat er bij elk hoofdstuk hoort
    extras                  de dingen naast de leerstof
    stappen                 de drie stappen om te starten
*/

export const oefenplatform = {
  label: "Oefenplatform",
  titel: "Ons oefenplatform",
  handgeschreven: "Oefenen op het niveau van je kind, niet op dat van zijn leeftijd",
  tekst:
    "Interactieve oefeningen van het 5de leerjaar tot het 6de middelbaar, met bij elk hoofdstuk een leerbundel met de theorie en een oefenbundel om af te drukken. Je kind kiest zelf waar het begint, en je ziet per kind wat het al maakte.",

  /*
    De prijs. Houd deze twee getallen gelijk aan PRIJS_NU_EUR en
    PRIJS_STRAKS_EUR in oefenplatform/lib/prijs.ts.
  */
  prijsNu: 20,
  prijsStraks: 50,
  prijsUitleg:
    "Zolang het platform nog volop in opbouw is, kost een heel schooljaar €20 in plaats van €50. Dat is voor het hele gezin, niet per kind. Met die bijdrage kunnen we blijven verder ontwikkelen. Zodra het platform volledig is, wordt het €50 per schooljaar per gezin.",

  /* De twee knoppen bovenaan. */
  startKnop: { tekst: "Een hoofdstuk gratis proberen", href: "https://oefenplatform.connectopia.one" },
  accountKnop: { tekst: "Een account aanmaken", href: "https://oefenplatform.connectopia.one/registreren" },
  gratisZin: "Bij bijna elk vak staat een hoofdstuk open om uit te proberen, zonder account en zonder je gegevens achter te laten.",

  voorWieTitel: "Voor wie het gemaakt is",
  voorWie: [
    {
      icoon: "🏡",
      kleur: "green" as const,
      naam: "Gezinnen die thuisonderwijs geven",
      tekst:
        "De vragen zijn geschreven op de minimumdoelen van de Vlaamse overheid en op de vakfiches van de examencommissie, dus je weet waar je je kind mee voorbereidt.",
    },
    {
      icoon: "🎓",
      kleur: "purple" as const,
      naam: "Tieners die examen doen bij de examencommissie",
      tekst:
        "Boost en Beyond volgen de indeling van de examencommissie, met een eigen reeks voor doorstroom en voor dubbele finaliteit.",
    },
    {
      icoon: "🚀",
      kleur: "orange" as const,
      naam: "Kinderen die vooruit willen",
      tekst:
        "Je kind hoeft niet te blijven bij het leerjaar waar het in zit. Is het eraan toe, dan gaat het gewoon door naar het volgende niveau, zonder bij te betalen.",
    },
    {
      icoon: "🧱",
      kleur: "blue" as const,
      naam: "Kinderen die iets willen bijwerken",
      tekst:
        "In Basis staan de bouwstenen die overal terugkomen: komma's verschuiven, breuken, woordsoorten, de d- en t-regel, de Franse woordenschat. Zonder dat het aanvoelt als terug naar een lager leerjaar.",
    },
  ],

  niveausTitel: "De acht categorieën",
  niveausTekst:
    "Je kind kiest eerst een categorie, dan een vak, dan een hoofdstuk. Alles zit in dezelfde toegang, dus je kan vrij rondkijken en wisselen.",
  niveaus: [
    {
      emoji: "🧱",
      naam: "Basis",
      wat: "De bouwstenen herhalen, voor elk niveau",
      vakken: "Wiskunde, Nederlands en Frans",
    },
    {
      emoji: "🌱",
      naam: "Start",
      wat: "5de en 6de leerjaar",
      vakken:
        "Wiskunde, Nederlands, Frans, Engels, geschiedenis, aardrijkskunde, wetenschap en techniek",
    },
    {
      emoji: "✨",
      naam: "Spark",
      wat: "1ste en 2de middelbaar",
      vakken:
        "Wiskunde, Nederlands, Frans, Engels, geschiedenis, aardrijkskunde, natuurwetenschappen, techniek, samenleving en economie",
    },
    {
      emoji: "🚀",
      naam: "Boost",
      wat: "Tweede graad, met een reeks voor doorstroom en een voor dubbele finaliteit",
      vakken:
        "De vakken van de examencommissie, van wiskunde en talen tot biologie, chemie, fysica, economie en de zorgvakken",
    },
    {
      emoji: "🌍",
      naam: "Beyond",
      wat: "Derde graad, ook met doorstroom en dubbele finaliteit",
      vakken:
        "Dezelfde opbouw als Boost, met daarbij onder meer statistiek, filosofie en recht",
    },
    {
      emoji: "🔭",
      naam: "Uitdagingshoek",
      wat: "Verder dan de leerstof, voor wie graag ver doordenkt",
      vakken: "De ruimte, coderen en computers, de geschiedenis van België, paradoxen en weetjes",
    },
  ],
  niveausSlot:
    "Boost en Beyond hebben elk twee reeksen, voor doorstroom en voor dubbele finaliteit. Samen zijn dat acht categorieën.",

  hoortErbijTitel: "Wat er bij elk hoofdstuk hoort",
  hoortErbij: [
    {
      titel: "Een leerbundel met de theorie",
      tekst:
        "De uitleg die bij dat hoofdstuk hoort, om te lezen of af te drukken. Geen kind hoeft eerst ergens anders te gaan zoeken.",
    },
    {
      titel: "Een tocht door het hoofdstuk",
      tekst:
        "Dezelfde theorie, maar stap voor stap en klikbaar. Bij Start ligt er op het einde een puzzel met een tekening uit dat hoofdstuk.",
    },
    {
      titel: "Een oefenbundel om af te drukken",
      tekst:
        "Andere vragen dan de online oefeningen, met een antwoordblad achteraan en veel schrijfruimte. Zo kan je kind ook verder zonder scherm.",
    },
    {
      titel: "Uitleg bij elke fout",
      tekst:
        "Bij een fout antwoord komt er altijd uitleg bij wat wel klopt. Fouten maken is hier de bedoeling, niet iets om te vermijden.",
    },
  ],

  manierTitel: "Hoe we de vragen maken",
  manierTekst:
    "Wij schrijven de vragen zelf, op basis van de minimumdoelen van de Vlaamse overheid en de vakfiches van de examencommissie. Er komt geen AI aan te pas. We kijken ze ook na op raadbaarheid: het juiste antwoord mag niet opvallen omdat het langer is dan de andere, en waar mag niet vaker voorkomen dan niet waar.",
  manierWoorden: ["Geen AI in de oefeningen", "Geen afleidende animaties", "Rustig opgebouwd", "Zonder reclame"],
  manierMelden:
    "Klopt er toch iets niet, dan kan je het onderaan elk hoofdstuk melden. Wij kijken het na en schrijven terug.",

  extrasTitel: "Naast de leerstof",
  extrasTekst:
    "Dingen die erbij horen voor het plezier. Ze tellen niet mee voor een rapport en er is geen ranglijst.",
  extras: [
    { icoon: "❓", titel: "De vraag van de dag", tekst: "Eén vraag per dag per categorie, met een weekdoel van drie. Geen dagelijkse reeks die je kan breken." },
    { icoon: "🏅", titel: "Verzamelbadges", tekst: "Badges die je kind verzamelt op zijn eigen tempo, zonder vergelijking met anderen." },
    { icoon: "💡", titel: "Het weetjesprikbord", tekst: "Kinderen sturen hun eigen weetje in. Wij kijken het na voor het verschijnt." },
  ],

  stappenTitel: "Zo begin je",
  stappen: [
    { nummer: "1", titel: "Maak een account", tekst: "Eén account per gezin, met je e-mailadres en een wachtwoord." },
    { nummer: "2", titel: "Voeg je kinderen toe", tekst: "Elk kind krijgt zijn eigen voortgang, zijn eigen badges en zijn eigen vraag van de dag." },
    { nummer: "3", titel: "Breng de toegang in orde", tekst: "Betaal de bijdrage voor een heel schooljaar, of vul je toegangscode in als je er een kreeg." },
  ],

  vragenTitel: "Nog een vraag?",
  vragenTekst:
    "Twijfel je of het past bij je kind, of loopt er iets vast? Bel of mail gerust, we denken graag mee.",
};
