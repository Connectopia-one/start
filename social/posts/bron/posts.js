/*
  De teksten van alle vierkante posts (1080 x 1080).

  Een post aanpassen? Verander hieronder de tekst en render opnieuw:
      PW=$(npm root -g)/playwright node render.js

  Per post kan je invullen:
    bestand   de bestandsnaam van het beeld, zonder .png
    kleur     groen (standaard), paars, oranje of blauw
    pil       het woordje in de gekleurde pil bovenaan
    hand      de handgeschreven regel
    titel     de grote titel; <br> maakt een nieuwe regel, <span> zet een
              stuk in het lichtere groen
    tekst     een korte alinea onder de titel (mag weg)
    kaarten   hoogstens drie kaartjes: { ic, naam, wat, bij }
    woorden   korte woorden in bolletjes: { ic, tekst }
    titelKlein  zet de titel wat kleiner als hij lang is
    foto      een foto bovenaan, met de bestandsnaam uit deze map
    figuur    een uitgeknipte figuur rechtsonder (een png met doorzichtige
              achtergrond uit deze map); de tekst links wordt dan smaller
    figuurBreed  zet de figuur over de volle breedte onderaan in plaats van
              in de hoek, voor een uitsnede waar links en rechts allebei
              iets op staat; de tekst blijft er dan boven
    fotoPositie  welk stuk van de foto je ziet, bv. "50% 30%"
    laden     een laadbalk: { naam, procent, onder } — voor een post over
              iets dat er bijna is
    banner    een schuine wimpel in de rechterbovenhoek, bv. "Volzet"; de
              blaadjes in die hoek gaan dan weg
    nadruk    de zin die in het gekleurde kader komt
    citaat    een citaat met een gekleurde streep ernaast
    voet      de groene balk: { hand, url, klein }

  Hou het rustig. Eén blok onder de titel leest het best op een gsm.
*/

module.exports = [
  {
    bestand: "oefenplatform-tijdelijke-prijs",
    kleur: "paars",
    figuur: "laptop-website.png",
    figuurBreed: true,
    pil: "Tijdelijke prijs",
    hand: "Zolang we volop bouwen",
    titel: "20 euro in plaats van 50<br><span>voor een heel schooljaar</span>",
    titelKlein: true,
    tekst:
      "Voor een heel gezin. Nu al te oefenen: 5de en 6de leerjaar, 1ste en 2de middelbaar. De andere jaren komen er stap voor stap bij.",
    voet: { hand: "Proef gratis een hoofdstuk op", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "we-zijn-gestart",
    kleur: "oranje",
    figuur: "zoon-duimen.png",
    pil: "Het is zover",
    hand: "Na maanden bouwen",
    titel: "Yes!<br><span>We zijn gestart</span>",
    tekst:
      "Onze website en ons oefenplatform staan online. Kom gerust rondkijken: wie we zijn, wat we doen, en waar je met je vragen terechtkan.",
    nadruk:
      "Testgezinnen: jullie mail is onderweg. Zie je hem niet staan? Kijk zeker ook even in je spam of ongewenste mail.",
    voet: { hand: "Alles staat klaar op", url: "www.connectopia.one" },
  },

  {
    bestand: "testgezinnen-bijna-zover",
    kleur: "oranje",
    pil: "Winactie",
    hand: "Nog heel even geduld",
    titel: "De testgezinnen<br><span>horen het vandaag</span>",
    tekst:
      "We hebben geloot uit alle inschrijvingen. De tien gezinnen die eruit kwamen, krijgen straks een bericht van ons met hun toegang.",
    laden: { naam: "Oefenplatform", procent: 96, onder: "we doen nu de laatste testen" },
    voet: { hand: "Wie we zijn lees je op", url: "www.connectopia.one" },
  },

  {
    bestand: "dag-05-wegwijzer",
    kleur: "blauw",
    pil: "Wegwijzer",
    hand: "Je hoeft dit niet alleen uit te zoeken",
    titel: "Vermoeden of<br><span>diagnose?</span>",
    tekst:
      "Een route in vijf stappen: van het eerste gesprek op school tot wat er bestaat aan ondersteuning, en wat het met je gezin doet.",
    woorden: [
      { tekst: "1. Ik twijfel" },
      { tekst: "2. Het traject" },
      { tekst: "3. En nu?" },
      { tekst: "4. Wat bestaat er" },
      { tekst: "5. Jij en je gezin" },
    ],
    voet: { hand: "Stap voor stap op", url: "connectopia.one/wegwijzer" },
  },

  {
    bestand: "dag-06-blog-autisme",
    kleur: "paars",
    pil: "Blog",
    hand: "Nieuw op de blog",
    titel: "Autisme bij<br><span>begaafde kinderen</span>",
    citaat:
      "Slimme kinderen krijgen soms ten onrechte de diagnose autisme. Maar de omgekeerde fout bestaat ook: autisme dat onzichtbaar blijft achter een perfect gekopieerd maatpak.",
    voet: { hand: "Lees het hele stuk op", url: "connectopia.one/blog" },
  },

  {
    bestand: "dag-07-externe-plusklas",
    kleur: "groen",
    pil: "Aanbod",
    hand: "Elke dinsdag in Hasselt",
    titel: "De externe<br><span>plusklas</span>",
    kaarten: [
      { ic: "🚀", naam: "Wanneer", wat: "Dinsdag, 9u tot 15u" },
      { ic: "📍", naam: "Waar", wat: "Atheneum Hasselt" },
    ],
    kaartenTwee: true,
    nadruk:
      "<b>6 tot 12 jaar · €50 per dag</b><br>Drie trajecten van tien dagen. Later instappen kan.",
    voet: { hand: "Alles over de plusklas op", url: "connectopia.one/aanbod" },
  },

  {
    bestand: "dag-08-observatielijst",
    kleur: "oranje",
    pil: "Gratis",
    hand: "Zonder inschrijven, meteen af te drukken",
    titel: "Wat zie jij<br><span>bij je kind?</span>",
    tekst:
      "Een lijst met kenmerken van hoogbegaafdheid, autisme en ADHD. Vul in wat je herkent en neem het blad mee naar je gesprek.",
    nadruk:
      "<b>Geen test en geen diagnose.</b> Gewoon een blad dat je gedachten ordent, zodat je gesprek niet bij nul begint.",
    voet: { hand: "Haal je blad op", url: "connectopia.one/observatielijst" },
  },

  {
    bestand: "dag-11-14-15-young-engineers",
    kleur: "blauw",
    pil: "Young Engineers",
    hand: "Naschools, met LEGO® en techniek",
    titel: "Bouwen, testen<br><span>en trots zijn</span>",
    tekst:
      "Met LEGO® en techniek echte uitdagingen aangaan, samenwerken en trots zijn op je werk. Elke week, in lessen van 1u15.",
    woorden: [
      { ic: "⚙️", tekst: "Dinsdag in Hasselt" },
      { ic: "🔧", tekst: "Woensdag in Genk" },
      { ic: "🛠️", tekst: "Zaterdag in Hasselt" },
    ],
    voet: {
      hand: "Inschrijven kan het hele jaar op",
      url: "connectopia.one/aanbod",
      klein: "€20 per les van 1u15 · 6 tot 12 jaar",
    },
  },

  {
    bestand: "dag-12-extra-kamp-hasselt",
    kleur: "oranje",
    foto: "dag-12-extra-kamp-hasselt.jpg",
    fotoPositie: "38% 46%",
    pil: "Herfstkamp",
    hand: "Hasselt, maandag 2 en dinsdag 3 november",
    titel: "Young<br><span>Engineer Held</span>",
    nadruk:
      "Bij Level X 28, Vilderstraat 28. <b>Van 9u tot 15u, €40 per dag</b>, voor kinderen van 6 tot 12 jaar.",
    voet: { hand: "Inschrijven op", url: "connectopia.one/aanbod" },
  },

  {
    bestand: "dag-13-blog-leren-leren",
    kleur: "paars",
    pil: "Blog",
    hand: "Nieuw op de blog",
    titel: "Leren leren,<br><span>zoals in de muziekschool</span>",
    citaat:
      "Vaak ligt het probleem niet bij de leerstof, maar bij de studiemethode. Bijlesdocent en violist Lucas Dumoulin over wat het onderwijs kan leren van de muziekschool.",
    voet: { hand: "Lees het hele stuk op", url: "connectopia.one/blog" },
  },

  {
    bestand: "dag-18-prikbord",
    kleur: "oranje",
    pil: "Prikbord",
    hand: "Voor en door ouders",
    titel: "Vijf borden,<br><span>één plek om te delen</span>",
    tekst:
      "Hang een briefje op, lees wat anderen ophingen en vind elkaar. Op het prikbord hangen we geen kritiek, wel ervaringen.",
    woorden: [
      { ic: "🔍", tekst: "Zoekertjes" },
      { ic: "☕️", tekst: "Samenkomen" },
      { ic: "💛", tekst: "Aanraders" },
      { ic: "📚", tekst: "Uitgezocht" },
      { ic: "📷", tekst: "Momenten" },
    ],
    voet: { hand: "Hang je briefje op via", url: "connectopia.one/prikbord" },
  },

  {
    bestand: "dag-19-blog-diep-gedacht",
    kleur: "paars",
    pil: "Blog",
    hand: "Nieuw op de blog",
    titel: "Diep gedacht en<br><span>intens gevoeld</span>",
    citaat:
      "Een boek van tien hoogbegaafde vrouwen die openhartig over hun leven vertellen, omkaderd door elf experts. Tine Geysen vertelt hoe het ontstond.",
    voet: { hand: "Lees het hele stuk op", url: "connectopia.one/blog" },
  },

  {
    bestand: "dag-19-extra-kamp-genk",
    kleur: "blauw",
    foto: "dag-19-extra-kamp-genk.jpg",
    fotoPositie: "52% 24%",
    pil: "Herfstkamp",
    hand: "Genk, woensdag 4 en donderdag 5 november",
    titel: "Creatieve<br><span>duizendpoot</span>",
    nadruk:
      "Van techniek tot design, op T2 Campus. <b>Van 9u tot 15u, €40 per dag</b>, voor kinderen van 6 tot 12 jaar.",
    voet: { hand: "Inschrijven op", url: "connectopia.one/aanbod" },
  },

  {
    bestand: "dag-21-waar-kan-je-terecht",
    kleur: "groen",
    pil: "Waar kan je terecht",
    hand: "Alfabetisch, zonder voorkeur",
    titel: "Diensten die<br><span>we zelf kennen</span>",
    tekst:
      "Van psycholoog en logopedist tot bijlesleerkracht met kennis van hoogbegaafdheid, ook bij dubbele diagnoses.",
    nadruk:
      "We verwijzen alleen door naar mensen en organisaties waar we <b>zelf vertrouwen</b> in hebben.",
    voet: { hand: "De hele gids staat op", url: "connectopia.one/waar-kan-je-terecht" },
  },

  {
    bestand: "dag-24-oefenplatform",
    kleur: "groen",
    pil: "Oefenplatform",
    hand: "Oefenen op je eigen tempo",
    titel: "Zelf oefenen,<br><span>thuis aan tafel</span>",
    tekst:
      "Wiskunde, Nederlands, Engels, geschiedenis, aardrijkskunde en wetenschap en techniek, met uitleg bij elk hoofdstuk.",
    kaarten: [
      { ic: "🌱", naam: "Start", wat: "5de &amp; 6de leerjaar" },
      { ic: "✨", naam: "Spark", wat: "1ste graad middelbaar" },
    ],
    kaartenTwee: true,
    voet: { hand: "Oefenen doe je op", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "dag-25-blog-zomer",
    kleur: "paars",
    pil: "Blog",
    hand: "Nieuw op de blog",
    titel: "De zomer:<br><span>vreugde of stress?</span>",
    citaat:
      "Voor veel kinderen is de zomervakantie vrijheid en avontuur. Voor menig ouder is het een periode van intensieve logistieke en emotionele puzzels.",
    voet: { hand: "Lees het hele stuk op", url: "connectopia.one/blog" },
  },

  {
    bestand: "dag-26-over-ons",
    kleur: "groen",
    pil: "Over ons",
    hand: "Iedereen heeft talent. Wij geven het de ruimte.",
    titel: "Dit is ons verhaal<br><span>en het begin van dat van jou</span>",
    titelKlein: true,
    tekst:
      "Wij zijn ervaringsdeskundige ouders met een pedagogische achtergrond en een netwerk van specialisten. Onze kracht ligt in het verbinden.",
    woorden: [
      { ic: "💡", tekst: "Nieuwsgierigheid" },
      { ic: "⚙️", tekst: "Creativiteit" },
      { ic: "🤝", tekst: "Samenwerking" },
      { ic: "🌱", tekst: "Persoonlijke groei" },
    ],
    voet: { hand: "Lees ons verhaal op", url: "connectopia.one/over-ons" },
  },

  {
    bestand: "dag-29-voor-professionals",
    kleur: "blauw",
    pil: "Voor professionals",
    hand: "Kinesist, logopedist, coach of arts?",
    titel: "Werk jij met<br><span>deze kinderen?</span>",
    tekst:
      "Wij brengen kinderen van 6 tot 12 jaar met hoogbegaafdheid, ASS of ADHD samen met gelijkgestemden, in Hasselt en Genk.",
    nadruk:
      "<b>Wij stellen geen diagnoses en geven geen therapie.</b> We vullen aan wat jij doet: een plek waar een kind peers vindt, en ouders die voorbereid bij je binnenkomen.",
    voet: { hand: "Wat we voor elkaar kunnen doen:", url: "connectopia.one/professionals" },
  },

  {
    bestand: "extra-alles-op-een-plek",
    kleur: "groen",
    pil: "Connectopia vzw",
    hand: "Jouw kompas bij hoogbegaafdheid, ASS en ADHD",
    titel: "Alles op<br><span>één plek</span>",
    woorden: [
      { ic: "🧭", tekst: "Wegwijzer" },
      { ic: "🚀", tekst: "Aanbod" },
      { ic: "📍", tekst: "Waar kan je terecht" },
      { ic: "✍️", tekst: "Blog" },
      { ic: "📌", tekst: "Prikbord" },
      { ic: "🏡", tekst: "Ouderportaal" },
      { ic: "🧮", tekst: "Oefenplatform" },
    ],
    voet: { hand: "Ruimte voor nieuwsgierigheid, talent en uitdaging", url: "www.connectopia.one" },
  },

  {
    bestand: "oefenplatform-prikkelarm",
    kleur: "groen",
    pil: "Oefenplatform",
    hand: "Rustig gebouwd, met opzet",
    titel: "Prikkelarm,<br><span>omdat het helpt</span>",
    tekst:
      "Wij werken in de eerste plaats met hoogbegaafde kinderen, vaak met ASS of ADHD erbij. Die leren op een andere manier en hebben nood aan duidelijkheid, structuur en rust.",
    woorden: [
      { ic: "🍃", tekst: "Geen animaties" },
      { ic: "🎨", tekst: "Rustige kleuren" },
      { ic: "📋", tekst: "Duidelijke instructies" },
    ],
    nadruk:
      "<b>Maar het is er voor iedereen.</b> Of je kind nu hoogbegaafd is, extra ondersteuning nodig heeft of gewoon wat wil bijoefenen.",
    voet: { hand: "Kijk gerust rond op", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "oefenplatform-voor-wie",
    kleur: "blauw",
    pil: "Voor wie",
    hand: "Van 5de leerjaar tot 6de middelbaar",
    titel: "Voor wie is dit<br><span>platform bedoeld?</span>",
    titelKlein: true,
    tekst:
      "Je hoeft bij ons niet aangesloten te zijn om mee te oefenen. Het platform staat open voor elk kind dat er iets aan heeft.",
    woorden: [
      { ic: "🎓", tekst: "Examencommissie" },
      { ic: "💡", tekst: "Hoogbegaafd" },
      { ic: "♾️", tekst: "ASS of ADHD" },
      { ic: "🚀", tekst: "Alvast vooruit" },
    ],
    nadruk:
      "<b>Ook wie thuis leert.</b> De hoofdstukken volgen de leerstof van het leerjaar, dus je kan er de examens van de Examencommissie mee voorbereiden.",
    voet: { hand: "Proef een gratis hoofdstuk op", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "oefenplatform-gratis-voor-leden",
    kleur: "oranje",
    pil: "Gratis voor leden",
    hand: "Zit je kind bij ons in een werking?",
    titel: "Dan oefent het<br><span>gratis mee</span>",
    tekst:
      "Kinderen die bij ons aangesloten zijn via de plusklas, een pluswerking of een ander traject krijgen gratis toegang tot alle materiaal op het platform.",
    woorden: [
      { ic: "🚀", tekst: "Externe plusklas, dinsdag" },
      { ic: "🎓", tekst: "Pluswerking woensdag" },
      { ic: "🎨", tekst: "Pluswerking zaterdag" },
    ],
    nadruk:
      "<b>En er hoort begeleiding bij.</b> Wij kijken mee wat een kind al maakte, zodat het op de dag zelf verder kan waar het vastliep.",
    voet: { hand: "Ons aanbod staat op", url: "connectopia.one/aanbod" },
  },

  {
    bestand: "oefenplatform-weetjesprikbord",
    kleur: "oranje",
    pil: "Weetjesprikbord",
    hand: "Weet jij er een waar iedereen van opkijkt?",
    titel: "Wist je dat<br><span>een koe vier magen heeft?</span>",
    titelKlein: true,
    tekst:
      "Op het weetjesprikbord hangen de kinderen zelf hun weetje op. Wij lezen elk briefje eerst na, en dan hangt het erbij.",
    woorden: [
      { ic: "🐭", tekst: "De tanden van een muis blijven groeien" },
      { ic: "🧊", tekst: "Een tesseract is een 4D-kubus" },
      { ic: "🍌", tekst: "In een banaan zit een beetje radioactieve stof" },
    ],
    nadruk:
      "<b>Nieuwsgierigheid mag.</b> Een weetje is geen oefening: geen punten, geen juist antwoord. Het mag gewoon straf zijn.",
    voet: { hand: "Hang jouw weetje op via", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "oefenplatform-vier-niveaus",
    kleur: "groen",
    pil: "Oefenplatform",
    hand: "Je kiest zelf waar je begint",
    titel: "Vier niveaus,<br><span>één platform</span>",
    woorden: [
      { ic: "🌱", tekst: "Start · 5de en 6de leerjaar" },
      { ic: "✨", tekst: "Spark · 1ste en 2de middelbaar" },
      { ic: "🚀", tekst: "Boost · 3de en 4de middelbaar" },
      { ic: "🌍", tekst: "Beyond · 5de en 6de middelbaar" },
    ],
    nadruk:
      "<b>En er is meer:</b> 🧱 Basis om bouwstenen te herhalen, 🔭 de uitdagingshoek, badges en het weetjesprikbord.",
    voet: { hand: "Kies je niveau op", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "oefenplatform-uitdagingshoek",
    kleur: "paars",
    pil: "Uitdagingshoek",
    hand: "Verder dan de leerstof",
    titel: "Voor wie graag<br><span>ver doordenkt</span>",
    tekst:
      "Vragen die naast de leerstof liggen, voor als een kind al lang klaar is en nog honger heeft. Geen leerjaar, geen punten die ergens meetellen.",
    woorden: [
      { ic: "🪐", tekst: "De ruimte" },
      { ic: "💻", tekst: "Coderen en computers" },
      { ic: "📜", tekst: "Geschiedenis van België" },
      { ic: "🤯", tekst: "Paradoxen" },
    ],
    nadruk:
      "<b>Zo een vraag bijvoorbeeld:</b> als het heelal oneindig vol sterren staat, waarom is de nacht dan donker?",
    voet: { hand: "De uitdagingshoek vind je op", url: "oefenplatform.connectopia.one" },
  },

  {
    bestand: "meetesten-examencommissie",
    kleur: "paars",
    pil: "Testers gezocht",
    hand: "Doe jij examen bij de Examencommissie?",
    titel: "Oefen gratis<br><span>en zeg ons wat beter kan</span>",
    titelKlein: true,
    tekst:
      "Onze hoofdstukken volgen de vakfiches van de Examencommissie. Klopt dat met wat jij op je examen krijgt?",
    woorden: [
      { ic: "📚", tekst: "Van het 5de leerjaar tot het 6de middelbaar" },
      { ic: "📄", tekst: "Doorstroom en dubbele finaliteit" },
    ],
    nadruk:
      "<b>Een maand gratis testen.</b> Vul je daarna de evaluatie in en je krijgt een gratis jaarlicentie: een heel jaar toegang tot alles.",
    voet: {
      hand: "Geef je op via",
      url: "connectopia.one/meetesten",
      klein: "Plaatsen zijn beperkt",
    },
  },

  {
    bestand: "meetesten-leerkrachten",
    kleur: "blauw",
    pil: "Leerkrachten",
    hand: "Geef je TOAH of bijles?",
    titel: "Kijk mee met<br><span>ons oefenplatform</span>",
    titelKlein: true,
    tekst:
      "Jij ziet elke week waar één leerling vastloopt. Ons platform loopt van het 5de leerjaar tot het 6de middelbaar. Wat kan je gebruiken tijdens je uur?",
    woorden: [
      { ic: "🧭", tekst: "Uitleg bij elk hoofdstuk" },
      { ic: "✍️", tekst: "Geen AI in de oefeningen" },
    ],
    nadruk:
      "<b>Een maand gratis bij je leerlingen.</b> Vul je daarna de evaluatie in en je krijgt een gratis jaarlicentie, voor maximaal 5 leerlingen.",
    voet: {
      hand: "Geef je op via",
      url: "connectopia.one/meetesten",
      klein: "Plaatsen zijn beperkt · 5de leerjaar tot 6de middelbaar",
    },
  },

  {
    // Kim, 8 oktober 2026: de oproep voor testers is volzet. Zelfde post als
    // meetesten-examencommissie, met een wimpel erover. Wie niet gekozen is,
    // kan nog altijd mee aan de proefprijs; zie connectopia-oefenplatform-prijs.
    bestand: "meetesten-volzet",
    kleur: "paars",
    banner: "Volzet",
    pil: "Oproep afgesloten",
    hand: "Doe jij examen bij de Examencommissie?",
    titel: "Bedankt voor<br><span>de vele aanmeldingen</span>",
    titelKlein: true,
    tekst:
      "De plaatsen om een maand gratis te testen zijn ingevuld. We kiezen de testers uit iedereen die het formulier invulde.",
    woorden: [
      { ic: "📝", tekst: "Gekozen uit wie het formulier invulde" },
      { ic: "📬", tekst: "Wie erbij is, hoort het vandaag nog" },
    ],
    nadruk:
      "<b>Toch meteen aan de slag?</b> Zolang het platform in opbouw is kost een heel jaar toegang tot alles 20 euro, voor het hele gezin.",
    voet: {
      hand: "Starten kan via",
      url: "oefenplatform.connectopia.one",
      klein: "Van het 5de leerjaar tot het 6de middelbaar",
    },
  },
];
