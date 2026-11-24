/*
  De privacyverklaring en de wettelijke gegevens van de vzw, op /privacy.
  Gemaakt op 24 november 2026 op vraag van Kim, voor de lancering.

  Bovenaan staan de gegevens die de wet op elke website van een vzw vraagt
  (naam, rechtsvorm, zetel, ondernemingsnummer, rechtspersonenregister,
  mailadres). Ze staan ook kort in de voettekst van elke pagina.

  Het adres van de zetel staat hier omdat de wet dat vraagt. Zet het nergens
  anders op de site.

  Iets veranderen? Pas de zinnen hieronder aan. Verandert er iets aan de vzw
  (nieuwe zetel, ander mailadres), pas het dan ook aan in `vzw` hieronder;
  de voettekst neemt het vanzelf over.
*/

import { site } from "@/content/site";

export const vzw = {
  naam: "Connectopia vzw",
  rechtsvorm: "vereniging zonder winstoogmerk (vzw)",
  zetel: "Kluisstraat 16, 3570 Alken",
  ondernemingsnummer: "BE 1040.538.004",
  rpr: "RPR Antwerpen, afdeling Tongeren-Borgloon",
  opgericht: "9 juli 2026",
  email: site.email,
  telefoon: site.telefoon,
};

export const privacy = {
  label: "Privacy",
  titel: "Privacy en wettelijke gegevens",
  handgeschreven: "Jouw gegevens zijn bij ons in goede handen.",
  tekst:
    "Hier lees je wie we zijn, welke gegevens we van jou en je kind bijhouden, waarom we dat doen en wat je rechten zijn. We houden het kort en in gewone woorden. Heb je een vraag, mail ons gerust.",
  bijgewerkt: "24 november 2026",

  wieZijnWe: {
    titel: "Wie we zijn",
    inleiding:
      "Deze website, het ouderportaal en het oefenplatform zijn van Connectopia vzw. Wij zijn verantwoordelijk voor de gegevens die je ons geeft.",
  },

  secties: [
    {
      titel: "Welke gegevens we bijhouden",
      regels: [
        "Als je een formulier invult (een aanvraag, een kampinschrijving, een briefje voor het prikbord, een tip voor de gids of In de kijker): je naam, je e-mailadres, je gsm-nummer als je het invult, en wat je zelf in het formulier schrijft.",
        "Bij een kampinschrijving ook de voornaam, achternaam en leeftijd van je kind, de gekozen dagen, je gemeente als je die invult, je keuze over foto's en wat je ons laat weten (bijvoorbeeld een allergie of dat je kind vroeger wordt opgehaald).",
        "In het ouderportaal: je account, de gegevens van je kind die je ons geeft, berichten en documenten die we met je delen, en foto's van de activiteiten.",
        "Op het oefenplatform: je e-mailadres en account, de voornaam die je kind gebruikt, welke vragen en hoofdstukken je kind maakte, meldingen en reacties die je instuurt, en of je betaald hebt.",
      ],
    },
    {
      titel: "Waarom we ze gebruiken",
      regels: [
        "Om je aanvraag of inschrijving te regelen en je daarover te contacteren.",
        "Om de activiteiten veilig te laten verlopen, bijvoorbeeld door rekening te houden met een allergie.",
        "Om je toegang te geven tot het ouderportaal en het oefenplatform, en om de voortgang van je kind te bewaren.",
        "Om betalingen op te volgen.",
        "Om je, als je dat zelf vraagt of aanvinkt, iets te bezorgen of je mening te vragen.",
      ],
      slot:
        "We gebruiken je gegevens nooit voor reclame van anderen en we verkopen ze nooit. We gebruiken ze om te doen wat je ons vroeg (een overeenkomst), omdat de wet het vraagt (zoals de boekhouding), of omdat je ons toestemming gaf (zoals voor foto's). Toestemming kan je altijd intrekken.",
    },
    {
      titel: "Foto's van je kind",
      regels: [
        "Bij de inschrijving kies je zelf of we foto's mogen nemen, en waarvoor: ook voor de website en sociale media, enkel om naar de ouders te sturen, of liever niet.",
        "Foto's voor de ouders zetten we in het ouderportaal, waar enkel de ouders van die activiteit ze zien.",
        "Wil je dat we een foto weghalen, of verander je van mening? Laat het ons weten, dan doen we dat.",
      ],
    },
    {
      titel: "Wie je gegevens nog ziet",
      inleiding:
        "Enkel ons team (Kim, Melissa en Lut) en wie een activiteit begeleidt, en enkel wat ze daarvoor nodig hebben. We geven je gegevens niet door aan anderen. Wel gebruiken we een paar diensten die onze websites laten werken. Zij mogen je gegevens enkel voor ons gebruiken:",
      regels: [
        "Supabase, voor de databank van het ouderportaal en het oefenplatform. De gegevens staan op servers in Ierland, binnen de Europese Unie.",
        "Vercel, voor het online zetten van de websites. Vercel telt ook hoeveel mensen een pagina bekijken, zonder cookies en zonder te weten wie je bent.",
        "Mollie, uit Nederland, voor betalingen op het oefenplatform. Je bankgegevens gaan rechtstreeks naar Mollie, wij zien ze niet.",
        "one.com, uit Denemarken, voor onze mailbox en ons domein.",
      ],
      slot:
        "Komen gegevens toch buiten de Europese Unie terecht, dan gebeurt dat enkel bij diensten die zich houden aan de Europese afspraken daarover.",
    },
    {
      titel: "Hoe lang we ze bewaren",
      regels: [
        "Een aanvraag of inschrijving bewaren we zolang het nodig is om ze te regelen, en daarna nog hoogstens twee jaar, zodat we weten wie al meedeed.",
        "Een account op het ouderportaal of het oefenplatform blijft bestaan tot je vraagt om het te verwijderen.",
        "Wat de boekhouding nodig heeft (zoals betalingen) bewaren we zolang de wet het vraagt.",
        "Vraag je ons iets te verwijderen, dan doen we dat, tenzij de wet ons verplicht het nog te bewaren.",
      ],
    },
    {
      titel: "Cookies",
      regels: [
        "Deze website gebruikt geen cookies om je te volgen en toont geen advertenties. Daarom zie je hier ook geen cookiebanner.",
        "Op het ouderportaal en het oefenplatform onthoudt je browser dat je aangemeld bent, en het oefenplatform onthoudt een paar instellingen (zoals waar je was). Dat is nodig om ze te laten werken en wordt niet gedeeld.",
        "We sluiten geen berichten van Facebook of Instagram in. Klik je op een link naar onze pagina daar, dan geldt hun eigen privacybeleid.",
      ],
    },
    {
      titel: "Jouw rechten",
      regels: [
        "Je mag altijd vragen welke gegevens we van jou of je kind hebben.",
        "Je mag vragen om iets te verbeteren of te verwijderen.",
        "Je mag je toestemming intrekken, bijvoorbeeld voor foto's.",
        "Je mag vragen om je gegevens mee te krijgen, of bezwaar maken tegen hoe we ze gebruiken.",
      ],
      slot:
        "Mail ons daarvoor, dan antwoorden we zo snel mogelijk en zeker binnen een maand. Ben je niet tevreden over hoe we met je gegevens omgaan, dan mag je ook klacht indienen bij de Gegevensbeschermingsautoriteit (www.gegevensbeschermingsautoriteit.be).",
    },
  ],
};
