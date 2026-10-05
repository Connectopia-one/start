/*
  Kijkje in de werking: de fotopagina.

  EEN FOTO BIJZETTEN
  1. Zet het bestand in  public/kijkje/
  2. Zet hieronder in de lijst "fotos" een blokje bij:

       {
         bestand: "bruggen-van-karton.jpg",      de naam van het bestand
         bijschrift: "Bruggen bouwen met karton, kokers en bekers.",
         alt: "Drie kinderen bouwen bruggen van karton",
         gezichten: true,                        optioneel, zie hieronder
       }

  Het bijschrift staat onder de foto en leest iedereen. De alt-tekst leest
  niemand hardop, maar ze wordt voorgelezen aan wie de foto niet kan zien, en
  ze verschijnt als de foto niet laadt. Beschrijf daarin wat er te zien is,
  zonder "foto van" ervoor.

  OVER "gezichten"
  Zet dat op true bij een foto waarop een kind duidelijk herkenbaar in beeld
  staat. De pagina doet daar niets mee: het staat er zodat je in één oogopslag
  ziet welke foto's toestemming van de ouders vragen, en welke je zonder zorgen
  ergens anders kan gebruiken. Een foto van achteren of van ver laat je gewoon
  leeg. Voor de foto's die hier nu staan, gaven de ouders hun toestemming.

  DE VOLGORDE
  De foto's staan in de volgorde van deze lijst. Wil je er een vooraan, zet het
  blokje dan hoger.
*/

export type Kijkfoto = {
  bestand: string;
  bijschrift: string;
  alt: string;
  gezichten?: boolean;
};

export const kijkje = {
  label: "Kijkje in de werking",
  titel: "Zo ziet een dag bij ons eruit",
  handgeschreven: "bouwen, denken, proberen",
  tekst:
    "Foto's uit de plusklassen, de pluswerkingen en de kampen. Geen opgezette beelden: dit is gewoon wat er op tafel ligt en wat de kinderen ermee doen.",

  /*
    De zin onderaan de pagina. Hier staat waarom we foto's tonen en hoe we met
    beeld van kinderen omgaan.
  */
  slotTitel: "Over deze foto's",
  slot: [
    "We tonen graag wat er bij ons gebeurt, want een foto van een tafel vol karton zegt meer dan een bladzijde uitleg.",
    "Staat je kind op een foto en wil je dat liever niet? Laat het ons weten, dan halen we ze er meteen af.",
  ],

  /*
    Het strookje van drie foto's dat op "Wie is Connectopia" staat, met een
    link naar deze pagina. Wil je er andere foto's in, vul dan drie andere
    bestandsnamen in; ze moeten ook in de lijst hieronder staan.
  */
  strook: {
    titel: "Kijkje in de werking",
    tekst:
      "Een tafel vol karton, een bord vol planeten en kinderen die er zelf iets van maken.",
    knop: "Bekijk alle foto's",
    bestanden: [
      "wat-zou-jij-hiermee-creeren.jpg",
      "van-tekening-naar-maquette.jpg",
      "plusklas-tafel.jpg",
    ],
  },

  fotos: [
    {
      bestand: "wat-zou-jij-hiermee-creeren.jpg",
      bijschrift:
        "Wat zou jij hiermee creëren? Een tafel vol karton, kurk en eierdozen wacht op ideeën.",
      alt: "Knutselmateriaal op tafel onder de vraag Wat zou jij hiermee creëren?",
    },
    {
      bestand: "van-tekening-naar-maquette.jpg",
      bijschrift: "Eerst een plan op papier, dan bouwen met karton en folie.",
      alt: "Tekening van een stad met maquettes van karton en aluminiumfolie",
    },
    {
      bestand: "cirkel-met-de-bordpasser.jpg",
      bijschrift: "Een cirkel tekenen met de grote passer aan het bord.",
      alt: "Kind tekent een cirkel op het bord met een grote passer",
    },
    {
      bestand: "zonnestelsel-aan-het-bord.jpg",
      bijschrift: "Samen de planeten op de juiste plaats hangen.",
      alt: "Kinderen hangen planeten op het bord met een begeleider",
    },
    {
      bestand: "bruggen-van-karton.jpg",
      bijschrift: "Bruggen bouwen met karton, kokers en bekers.",
      alt: "Drie kinderen bouwen bruggen van karton",
      gezichten: true,
    },
    {
      bestand: "brain-train-spel.jpg",
      bijschrift: "Ons zelfgemaakte brain train spel van eierdozen.",
      alt: "Kinderen leggen geschilderde eierdoosstukken in een raster",
      gezichten: true,
    },
    {
      bestand: "bekerpiramide.jpg",
      bijschrift: "Samen een piramide van bekers bouwen.",
      alt: "Twee kinderen bouwen een piramide van bekers",
      gezichten: true,
    },
    {
      bestand: "flessenraket-vullen.jpg",
      bijschrift: "De flessenraket vullen, met een trechter en veel geduld.",
      alt: "Kinderen en een begeleider vullen een zelfgemaakte flessenraket",
      gezichten: true,
    },
    {
      bestand: "samen-aan-tafel.jpg",
      bijschrift: "Even samen aan tafel, met de zon en de planeten op de muur.",
      alt: "Kinderen en begeleiders zitten rond een tafel in de plusklas",
      gezichten: true,
    },
    {
      bestand: "opzoekwerk-in-de-plusklas.jpg",
      bijschrift: "Opzoekwerk: wie ging er naar de maan, en wat klopt daarvan?",
      alt: "Twee kinderen zoeken iets op een laptop op en schrijven mee in een schrift",
      gezichten: true,
    },
    {
      bestand: "naar-huis-na-de-plusklas.jpg",
      bijschrift: "Naar huis na een geslaagde dag, voldaan en met de rugzak om.",
      alt: "Kinderen met rugzakken lopen na de plusklas naar buiten",
    },
    {
      bestand: "plusklas-tafel.jpg",
      bijschrift: "In de plusklas ligt altijd iets klaar om in te duiken.",
      alt: "Tafel met boeken, denkspellen en een LEGO-doolhof",
    },
    {
      bestand: "klaar-voor-de-dag.jpg",
      bijschrift: "Boeken, spellen en materiaal klaar voor een nieuwe dag.",
      alt: "Boeken over ruimte en wetenschap met eierdozen en pingpongballen",
    },
    {
      bestand: "alles-ligt-klaar.jpg",
      bijschrift: "Stiften, scharen en lijm: alles ligt klaar.",
      alt: "Bakken met knutselmateriaal",
    },
    {
      bestand: "de-katteket-natekenen.jpg",
      bijschrift:
        "De Katteket: helemaal met de hand nagetekend, naast het voorbeeld op het scherm.",
      alt: "Een getekende poster met kattenastronauten naast een laptop met hetzelfde beeld",
    },
    {
      bestand: "tekenen-naar-voorbeeld.jpg",
      bijschrift: "Eerst de lijnen in potlood, de kleur komt later.",
      alt: "Kind tekent aan een werktafel met een tablet en een bak stiften ernaast",
      gezichten: true,
    },
    {
      bestand: "samen-een-denkspel.jpg",
      bijschrift: "Samen een denkspel oplossen, en dan die duim omhoog.",
      alt: "Een begeleidster en een kind aan een schoolbank met een denkspel tussen hen in",
      gezichten: true,
    },
    {
      bestand: "bouwen-met-een-begeleider.jpg",
      bijschrift: "Bouwen volgens plan, met hulp waar het vastloopt.",
      alt: "Kind en begeleidster bouwen een constructie met bouwstenen aan een schoolbank",
      gezichten: true,
    },
    {
      bestand: "de-aarde-en-de-maan-bouwen.jpg",
      bijschrift: "De aarde, de maan en de zon in elkaar zetten, met tandwielen en een motortje.",
      alt: "Twee kinderen buigen zich over een houten bouwpakket met een wereldbol",
    },
    {
      bestand: "een-boek-over-natuurkunde.jpg",
      bijschrift: "Een boek over natuurkunde, en even niet gestoord worden.",
      alt: "Kind leest een boek over natuurkunde aan een houten tafel",
      gezichten: true,
    },
    {
      bestand: "werken-waar-het-goed-voelt.jpg",
      bijschrift:
        "Werken waar het goed voelt: op de grond, met de moleculen binnen handbereik.",
      alt: "Kind zit op de vloer te typen op een laptop, naast molecuulmodellen en een tijdklok",
    },
    {
      bestand: "lego-werelden.jpg",
      bijschrift: "Eigen werelden in een doos: van de oceaan tot het bos.",
      alt: "Zelfgebouwde LEGO-landschappen en voertuigen in een kartonnen doos",
    },
    {
      bestand: "bloemen-zoeken-op-de-campus.jpg",
      bijschrift: "Bloemen zoeken in het veld naast de campus.",
      alt: "Twee kinderen zoeken bloemen in een veld met hoog gras en wilde bloemen",
      gezichten: true,
    },
    {
      bestand: "op-bezoek-in-het-atheneum.jpg",
      bijschrift: "Op bezoek in het atheneum, waar ze ook aan hoogbegaafden denken.",
      alt: "Kind steekt twee duimen op naast een banner van het atheneum",
      gezichten: true,
    },
    {
      bestand: "het-knutselmagazijn.jpg",
      bijschrift: "Het knutselmagazijn: alles in een bak, met een etiket erop.",
      alt: "Rekken vol doorzichtige bakken met knutselmateriaal, elk met een etiket",
    },
    {
      bestand: "telewerkhokjes-t2.jpg",
      bijschrift: "Op de T2-campus kunnen ouders telewerken in rustige hokjes.",
      alt: "Houten telewerkhokjes met tafel op de T2-campus",
    },
  ] satisfies Kijkfoto[],
};
