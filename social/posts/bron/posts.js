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
    fotoPositie  welk stuk van de foto je ziet, bv. "50% 30%"
    nadruk    de zin die in het gekleurde kader komt
    citaat    een citaat met een gekleurde streep ernaast
    voet      de groene balk: { hand, url, klein }

  Hou het rustig. Eén blok onder de titel leest het best op een gsm.
*/

module.exports = [
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
    fotoPositie: "45% 34%",
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
];
