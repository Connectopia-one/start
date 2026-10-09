# -*- coding: utf-8 -*-
"""Een hartstilstand, reanimatie en de AED.

Het tweede thema uit "ik reageer correct in een noodsituatie". De fiche geeft
hier één rijtje, en de volgorde erin is de hele leerstof:

    1 bepaal of de persoon bewusteloos is
    2 bel 112
    3 kijk of er een AED in de buurt is
    4 start borstcompressies
    5 beademing
    6 doorgaan tot de ambulance arriveert en de ambulancier het overneemt

Daarnaast vraagt de fiche wat een hartstilstand is, welke symptomen erbij
horen, en hoe je hartmassage en mond-op-mond beademing uitvoert. Ook hier
vraagt ze te beoordelen of iemand het in een gegeven situatie juist deed.

Over één ding is dit thema voorzichtig: de fiche geeft geen cijfers over
diepte, tempo of het aantal compressies per beademing. Die staan hier dan ook
niet in. Wie ze erbij verzint, zet een kind iets in het hoofd dat op een echte
reanimatiecursus anders geleerd wordt.

Deel 1 is de hartstilstand zelf en de zes stappen in hun volgorde.
Deel 2 is de uitvoering: borstcompressies, beademing en de AED.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een hartstilstand?",
        opties=[
            "het hart stopt met pompen, waardoor het bloed niet meer rondgaat",
            "het hart klopt zo snel dat het pijn doet midden in de borstkas",
            "de bloeddruk zakt even weg als je te snel uit je bed recht komt",
            "een bloedvat in het hart raakt vernauwd maar blijft nog net open",
        ],
        antwoord=0,
        uitleg="Zonder pompen komt er geen zuurstof meer bij de hersenen. Daarom telt elke seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee tekens wijzen op een hartstilstand?",
        opties=[
            "de persoon reageert niet en ademt niet normaal",
            "de persoon is bleek en heeft koude handen",
            "de persoon klaagt over hoofdpijn en duizeligheid",
            "de persoon ademt snel en praat verward",
        ],
        antwoord=0,
        uitleg="Niet reageren en niet normaal ademen zijn samen het alarmsignaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een vermoedelijke hartstilstand?",
        opties=[
            "bepalen of de persoon bewusteloos is",
            "112 bellen",
            "een AED zoeken",
            "beginnen met borstcompressies",
        ],
        antwoord=0,
        uitleg="Eerst nagaan of de persoon reageert. Anders druk je op de borstkas van iemand die gewoon slaapt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de tweede stap bij een hartstilstand?",
        opties=[
            "112 bellen",
            "een AED zoeken",
            "met borstcompressies beginnen",
            "beademen",
        ],
        antwoord=0,
        uitleg="De ambulance moet zo vroeg mogelijk onderweg zijn, dus bellen komt voor alle hulp die jij zelf geeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de derde stap bij een hartstilstand?",
        opties=[
            "kijken of er een AED in de buurt is",
            "112 bellen",
            "bepalen of de persoon bewusteloos is",
            "doorgaan tot de ambulance er is",
        ],
        antwoord=0,
        uitleg="Na het bellen zoek je een AED, zodat die er al is wanneer je hem nodig hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de vierde stap bij een hartstilstand?",
        opties=[
            "starten met borstcompressies",
            "beademen",
            "een AED zoeken",
            "de ambulance bellen",
        ],
        antwoord=0,
        uitleg="De borstcompressies komen voor de beademing in het rijtje van de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de laatste stap in het rijtje van de fiche?",
        opties=[
            "doorgaan tot de ambulancier het overneemt",
            "de persoon in een stabiele zijligging leggen",
            "de AED weer uitzetten",
            "de familie verwittigen",
        ],
        antwoord=0,
        uitleg="Je stopt niet zelf: je gaat door tot de hulpdiensten het van je overnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand begint onmiddellijk met borstcompressies en belt pas daarna 112. Wat liep er mis?",
        opties=[
            "bellen is stap 2 en komt dus voor de compressies",
            "er liep niets mis, de volgorde maakt niet uit",
            "hij had eerst moeten beademen",
            "hij had eerst de AED moeten aansluiten",
        ],
        antwoord=0,
        uitleg="Hoe later de ambulance vertrekt, hoe langer de persoon zonder professionele hulp blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bent alleen bij iemand die niet reageert en niet normaal ademt. Wat doe je met je gsm?",
        opties=[
            "112 bellen en de luidspreker aanzetten zodat je handen vrij blijven",
            "eerst enkele minuten reanimeren en pas daarna de hulpdiensten bellen",
            "een foto van het slachtoffer maken om aan de ambulancier te tonen",
            "iemand uit je contacten bellen die verpleegkundige is en dichtbij woont",
        ],
        antwoord=0,
        uitleg="Zo kan je ondertussen al beginnen en blijft de centrale je door de stappen loodsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting AED?",
        opties=[
            "automatische externe defibrillator",
            "acute eerste dienst",
            "ademhaling en defibrillatie",
            "automatische eerstehulpdoos",
        ],
        antwoord=0,
        uitleg="Het is een toestel dat met een stroomstoot het hartritme kan herstellen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je belt 112 voor je met borstcompressies begint.",
        antwoord=True,
        uitleg="Bellen is stap 2, de compressies zijn stap 4.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hartstilstand betekent dat het hart te snel klopt.",
        antwoord=False,
        uitleg="Bij een stilstand pompt het hart niet meer. Te snel kloppen is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Zodra de persoon weer een keer zucht, mag je stoppen met reanimeren.",
        antwoord=False,
        uitleg="De fiche zegt: doorgaan tot de ambulance er is en de ambulancier het overneemt.",
    ),
    dict(
        type="waarofniet",
        vraag="Iemand die niet reageert en niet normaal ademt, heeft mogelijk een hartstilstand.",
        antwoord=True,
        uitleg="Dat zijn precies de twee tekens waarop je moet reageren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze staan in het rijtje van zes stappen bij reanimatie?",
        opties=[
            "bepaal of de persoon bewusteloos is",
            "bel 112",
            "kijk of er een AED in de buurt is",
            "leg de persoon in stabiele zijligging",
        ],
        antwoord=[0, 1, 2],
        uitleg="De stabiele zijligging staat niet in dit rijtje. De andere drie stappen zijn compressies, beademing en doorgaan.",
    ),
    dict(
        type="invultekst",
        vraag="Welk nummer bel je bij een hartstilstand?",
        antwoord=["112"],
        uitleg="112 is de ziekenwagen. Dat is stap 2 van de zes.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel stappen bij reanimatie noemt de fiche? Antwoord met een cijfer.",
        antwoord=["6", "zes"],
        uitleg="Zes stappen, van bewustzijn nagaan tot doorgaan tot de ambulancier het overneemt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het toestel dat met een stroomstoot het hartritme kan herstellen? Antwoord met de afkorting.",
        antwoord=["AED", "aed"],
        uitleg="AED staat voor automatische externe defibrillator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zakt in elkaar op een drukke markt. Wat vraag je aan de omstaanders?",
        opties=[
            "dat één iemand 112 belt en één iemand een AED zoekt",
            "dat iedereen een stap achteruit gaat en wacht",
            "dat iemand de persoon water geeft",
            "dat iemand de persoon rechtzet op een stoel",
        ],
        antwoord=0,
        uitleg="Taken verdelen laat jou meteen beginnen en zet de andere stappen tegelijk in gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk zo snel mogelijk met reanimeren te beginnen?",
        opties=[
            "zonder rondgaand bloed krijgen de hersenen geen zuurstof",
            "anders koelt het lichaam van het slachtoffer te snel af",
            "anders raakt de hartspier verkrampt en komt ze niet meer los",
            "anders mag de ambulancier het niet meer van je overnemen",
        ],
        antwoord=0,
        uitleg="De compressies houden het bloed in beweging tot het hart weer kan overnemen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar leg je je handen bij hartmassage?",
        opties=[
            "midden op de borstkas",
            "links op de borstkas, boven het hart",
            "onderaan op de buik",
            "op de onderste rib aan de rechterkant",
        ],
        antwoord=0,
        uitleg="Midden op de borstkas, niet links: het hart ligt meer in het midden dan de meesten denken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe houd je je armen bij de borstcompressies?",
        opties=[
            "gestrekt, met je schouders recht boven je handen",
            "gebogen, zodat je kracht uit je armen komt",
            "gestrekt, met je schouders naast je handen",
            "gebogen, met je ellebogen tegen je zij",
        ],
        antwoord=0,
        uitleg="Met gestrekte armen duw je met je bovenlichaam, en dat houd je veel langer vol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat je de borstkas tussen twee compressies doen?",
        opties=[
            "volledig terugkomen",
            "half ingedrukt blijven",
            "ingedrukt blijven tot je beademt",
            "niets, je drukt gewoon door",
        ],
        antwoord=0,
        uitleg="Als de borstkas niet terugkomt, kan het hart zich ook niet opnieuw vullen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met het hoofd van het slachtoffer voor je beademt?",
        opties=[
            "je kantelt het hoofd achterover en tilt de kin op",
            "je legt het hoofd zo plat mogelijk op de grond",
            "je draait het hoofd voorzichtig naar de zijkant",
            "je tilt het hoofd op en legt er een kussen onder",
        ],
        antwoord=0,
        uitleg="Zo komt de luchtweg vrij. Zonder die handeling gaat de lucht niet naar de longen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met de neus bij mond-op-mond beademing?",
        opties=[
            "je knijpt ze dicht",
            "je laat ze open voor de lucht",
            "je bedekt ze met je hand",
            "je blaast er samen met de mond in",
        ],
        antwoord=0,
        uitleg="Anders ontsnapt de lucht langs de neus en bereikt ze de longen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je dat een beademing aankomt?",
        opties=[
            "de borstkas komt zichtbaar omhoog",
            "de wangen van het slachtoffer bollen op",
            "je hoort een fluitend geluid",
            "het slachtoffer slikt",
        ],
        antwoord=0,
        uitleg="De borstkas die omhoogkomt, is het enige betrouwbare teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je een AED hebt gehaald?",
        opties=[
            "je zet hem aan en volgt de gesproken instructies",
            "je geeft meteen een stroomstoot",
            "je wacht tot de ambulance er is",
            "je legt hem naast het slachtoffer tot je moe bent",
        ],
        antwoord=0,
        uitleg="Een AED praat je zelf door de stappen en beslist of er een stoot nodig is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Beslist de AED zelf of er een stroomstoot nodig is?",
        opties=[
            "ja, hij meet het hartritme en beslist dan",
            "nee, de hulpverlener beslist dat",
            "nee, dat mag enkel de ambulancier",
            "ja, maar enkel bij kinderen",
        ],
        antwoord=0,
        uitleg="Daarom heet hij automatisch. Jij volgt wat hij zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je terwijl de AED het hartritme meet?",
        opties=[
            "je raakt het slachtoffer niet aan",
            "je blijft doorgaan met compressies",
            "je beademt verder",
            "je legt het slachtoffer in zijligging",
        ],
        antwoord=0,
        uitleg="Aanraken verstoort de meting, en bij een stoot is het ook voor jou gevaarlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bent alleen, je bent uitgeput, en de ambulance is er nog niet. Wat doe je?",
        opties=[
            "je laat iemand anders overnemen en blijft zo doorgaan",
            "je stopt tot je weer kan",
            "je gaat over op enkel beademen",
            "je legt het slachtoffer in zijligging en wacht",
        ],
        antwoord=0,
        uitleg="De fiche zegt: doorgaan tot de ambulancier het overneemt. Wisselen met een omstaander houdt dat haalbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij hartmassage leg je je handen links op de borstkas.",
        antwoord=False,
        uitleg="Midden op de borstkas. Links is een bekende misvatting.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kantelt het hoofd achterover en tilt de kin op voor je beademt.",
        antwoord=True,
        uitleg="Die twee handelingen maken de luchtweg vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="Terwijl de AED het hartritme meet, blijf je gewoon doorduwen op de borstkas.",
        antwoord=False,
        uitleg="Je blijft van het slachtoffer af zolang de AED meet of een stoot geeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan aan de borstkas zien of een beademing aankomt.",
        antwoord=True,
        uitleg="Komt de borstkas omhoog, dan gaat de lucht naar de longen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij een goede uitvoering van borstcompressies?",
        opties=[
            "de handen midden op de borstkas",
            "gestrekte armen met de schouders erboven",
            "de borstkas volledig laten terugkomen",
            "de ellebogen gebogen houden om kracht te sparen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gebogen ellebogen kosten juist meer kracht en maken de compressies ondiep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij mond-op-mond beademing?",
        opties=[
            "het hoofd achterover kantelen",
            "de kin optillen",
            "de neus dichtknijpen",
            "het slachtoffer eerst rechtzetten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Rechtzetten hoort er niet bij: je reanimeert iemand liggend op een harde ondergrond.",
    ),
    dict(
        type="invultekst",
        vraag="Waar midden op het lichaam leg je je handen bij hartmassage? Antwoord met één woord.",
        antwoord=["borstkas", "borst"],
        uitleg="Midden op de borstkas, met gestrekte armen.",
    ),
    dict(
        type="invultekst",
        vraag="Wat knijp je dicht bij mond-op-mond beademing?",
        antwoord=["de neus", "neus"],
        uitleg="Anders ontsnapt de lucht langs de neus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand heeft gereanimeerd maar bleef tijdens het meten van de AED op de borstkas duwen. Wat liep er mis?",
        opties=[
            "je mag het slachtoffer niet aanraken terwijl de AED meet",
            "hij had tijdens de meting van de AED sneller moeten duwen",
            "hij had voor de meting eerst twee keer moeten beademen",
            "hij had de AED eerst moeten uitzetten voor hij verder duwde",
        ],
        antwoord=0,
        uitleg="De meting wordt dan verstoord en de AED kan geen juiste beslissing nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom reanimeer je op een harde ondergrond?",
        opties=[
            "op een zachte ondergrond zakt het lichaam mee en komen de compressies niet aan",
            "omdat je op een zachte ondergrond zelf uit evenwicht kan geraken en vallen",
            "omdat het slachtoffer op een zachte ondergrond anders te snel afkoelt",
            "omdat de plakkers van de AED anders niet goed blijven kleven",
        ],
        antwoord=0,
        uitleg="Op een matras of zetel duw je vooral de ondergrond in, niet de borstkas.",
    ),
]
