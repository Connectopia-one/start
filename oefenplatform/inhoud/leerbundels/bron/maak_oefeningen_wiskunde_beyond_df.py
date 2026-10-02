# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij wiskunde 🌍 Beyond dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere getallen, andere situaties, en opdrachten die je enkel op papier
kan maken (een tabel aanvullen, een redenering uitschrijven, een schets maken).
Wie hier iets bijschrijft, legt het eerst naast
`../../beyond-dubbele-finaliteit/wiskunde.json` en naast de vakfiche zelf.

Het vak heet hier gewoon Wiskunde, niet wiskunde gevorderd: de dubbele
finaliteit heeft er één fiche voor, met analyse voor zestig procent en
kansrekenen en statistiek voor veertig procent.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond-dubbele-finaliteit". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen.

Wiskunde staat hier in woorden en niet in symbolen, net als in de vragen en in
de leerbundels.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Wiskunde"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"

breuk = bundel.breuk

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf je tussenstappen op. Een antwoord zonder berekening is niet na te kijken, ook niet door jezelf.",
    "Zet bij elk antwoord de eenheid, als er een is. Een getal zonder eenheid is in een vraagstuk zelden een antwoord.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


# ============================================================
OEFENBUNDELS["oefenbundel-problemen-oplossen-van-situatie-naar-wiskunde-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Problemen oplossen: van situatie naar wiskunde",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vier stappen",
             opdracht="Bij elke opgave hieronder staat één stap van het oplossingsproces beschreven. "
                      "Schrijf erbij welke stap dat is: begrijpen, plannen, uitvoeren of reflecteren.",
             oefeningen=[
                 ("kort", "Je onderstreept in de opgave wat gevraagd wordt en wat gegeven is.",
                  "begrijpen", WW),
                 ("kort", "Je rekent de gekozen formule uit met de getallen van de opgave.",
                  "uitvoeren", WW),
                 ("kort", "Je vindt 540 kilometer per uur voor een auto en gaat je berekening opnieuw na.",
                  "reflecteren", WW),
                 ("kort", "Je beslist dat je het probleem in twee deelproblemen splitst.",
                  "plannen", WW),
                 ("kort", "Je maakt een schets van de situatie om te zien wat er bedoeld wordt.",
                  "begrijpen", WW),
                 ("kort", "Je controleert of je antwoord de juiste eenheid heeft.",
                  "reflecteren", WW),
             ]),
        dict(kop="Welke strategie?",
             opdracht="Kies bij elke situatie de strategie die het snelst tot een antwoord leidt, en "
                      "schrijf in één zin waarom.",
             oefeningen=[
                 ("open", "Je moet alle manieren vinden waarop je met munten van 1 en 2 euro precies "
                          "5 euro kan betalen. Welke strategie en waarom?",
                  "Alle mogelijkheden systematisch opschrijven: er zijn er maar een paar, en ordelijk "
                  "tellen laat er geen vergeten.", 3),
                 ("open", "Een zaal heeft 23 rijen en elke rij heeft 3 stoelen meer dan de vorige. Je moet "
                          "het totaal weten. Welke strategie en waarom?",
                  "Een patroon of regelmaat zoeken en een formule opstellen: 23 rijen één voor één optellen "
                  "duurt te lang en geeft meer kans op een rekenfout.", 3),
                 ("open", "Je moet weten hoeveel winst een handelaar maakt bij 0, 10, 20, 30 en 40 stuks, "
                          "en waar de winst het hoogst ligt. Welke strategie en waarom?",
                  "Een tabel maken en er een grafiek van tekenen: de grafiek maakt het verloop in één "
                  "oogopslag zichtbaar, dus ook waar de top ligt.", 3),
                 ("open", "Een figuur is links en rechts van een middellijn precies hetzelfde. Je moet de "
                          "oppervlakte berekenen. Welke strategie en waarom?",
                  "Symmetrie gebruiken: je rekent één helft uit en verdubbelt, dus maar half zoveel werk.", 3),
                 ("open", "Je zoekt een getal waarvan het kwadraat plus het getal zelf 156 geeft. Je mag "
                          "een rekentoestel gebruiken. Welke strategie en waarom?",
                  "Slim gissen en verbeteren: je probeert 12 (156 is bijna 12 maal 13), ziet of je te hoog "
                  "of te laag zit en stuurt bij. Het antwoord is 12.", 3),
             ]),
        dict(kop="Vertalen naar wiskunde",
             opdracht="Schrijf bij elke situatie het voorschrift of de vergelijking op. Zeg eerst in één "
                      "woord wat je onbekende is.",
             oefeningen=[
                 ("open", "Een fietsenverhuur vraagt 8 euro voorrijkosten en 3 euro per uur. Schrijf de "
                          "prijs in functie van het aantal uren.",
                  "Onbekende: het aantal uren x. Prijs is 8 plus 3 maal x.", 2),
                 ("open", "Een bad bevat 240 liter en loopt leeg met 12 liter per minuut. Schrijf de inhoud "
                          "in functie van de tijd in minuten.",
                  "Onbekende: de tijd t in minuten. Inhoud is 240 min 12 maal t.", 2),
                 ("open", "Een trui kost na 30 procent korting 42 euro. Schrijf de vergelijking voor de "
                          "oorspronkelijke prijs.",
                  "Onbekende: de oorspronkelijke prijs p. 0,7 maal p is 42, dus p is 60 euro.", 2),
                 ("open", "Het aantal leden van een club is dit jaar 240 en stijgt elk jaar met 5 procent. "
                          "Schrijf het aantal leden in functie van het aantal jaren.",
                  "Onbekende: het aantal jaren x. Aantal leden is 240 maal 1,05 tot de macht x.", 2),
             ]),
        dict(kop="Klopt dat antwoord?",
             opdracht="Bij elke opgave staat een antwoord. Beslis of het kan, en schrijf bij een onmogelijk "
                      "antwoord waaraan je het ziet.",
             oefeningen=[
                 ("open", "Een klas van 24 leerlingen; het gemiddelde aantal broers en zussen komt uit op 2,5.",
                  "Dat kan. Een gemiddelde hoeft geen geheel getal te zijn, ook al is het aantal broers en "
                  "zussen dat wel.", 2),
                 ("open", "Een zwembad van 25 meter; een zwemmer zwemt er volgens de berekening 42 banen in "
                          "3 minuten.",
                  "Dat kan niet. Dat zou meer dan 5 meter per seconde zijn, veel sneller dan een wereldrecord. "
                  "Waarschijnlijk is er met de eenheden iets misgelopen.", 3),
                 ("open", "Een korting van 20 procent op 60 euro geeft volgens de berekening 40 euro.",
                  "Dat kan niet. 20 procent van 60 is 12, dus de prijs wordt 48 euro. Er is 20 euro "
                  "afgetrokken in plaats van 20 procent.", 3),
                 ("open", "Een kans wordt berekend op 1,4.",
                  "Dat kan niet. Een kans ligt altijd tussen 0 en 1; boven 1 is er zeker een fout gemaakt.", 2),
             ]),
        dict(kop="ICT of met de hand?",
             opdracht="Beslis of je dit op het examen met ICT mag doen, en schrijf in één zin wat de regel is.",
             oefeningen=[
                 ("open", "De grafiek van een exponentiële functie tekenen om er de kenmerken van af te lezen.",
                  "Mag met ICT. Een grafiek tekenen en kenmerken aflezen is uitdrukkelijk toegelaten.", 2),
                 ("open", "De oppervlakte onder een Gausskromme bepalen tussen twee waarden.",
                  "Mag met ICT, en kan eigenlijk niet anders: daarvoor zijn de rekenapps bedoeld.", 2),
                 ("open", "Een vergelijking van de eerste graad oplossen zoals 3 maal x plus 4 is 19.",
                  "Dat doe je met de hand. Zulke eenvoudige bewerkingen moet je zonder toestel kunnen.", 2),
                 ("open", "Een antwoord van 2,34567 afronden voor je het opschrijft.",
                  "Je rondt pas op het einde af, op het aantal cijfers dat de opgave vraagt. Tussentijds "
                  "afronden scheelt soms in het eindantwoord.", 3),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-machtswortels-en-machten-met-rationale-exponent-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Machtswortels en machten met rationale exponent",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Machten met een gehele exponent",
             opdracht="Reken uit. Schrijf een negatieve exponent eerst om naar een breuk.",
             oefeningen=[
                 ("rij", [("zeven tot de macht nul", "1"),
                          ("drie tot de macht min twee", "een negende"),
                          ("vijf tot de macht min één", "een vijfde"),
                          ("twee tot de macht min vijf", "een tweeëndertigste")],
                  "Reken uit.", WW),
                 ("rij", [("twee tot de macht min drie, als decimaal getal", "0,125"),
                          ("tien tot de macht min twee, als decimaal getal", "0,01"),
                          ("vier tot de macht min één, als decimaal getal", "0,25"),
                          ("vijf tot de macht min twee, als decimaal getal", "0,04")],
                  "Reken uit en schrijf als decimaal getal.", WW),
                 ("rij", [("a tot de vierde maal a tot de zesde", "a tot de tiende"),
                          ("a tot de negende gedeeld door a tot de vierde", "a tot de vijfde"),
                          ("a tot de tweede, tot de vijfde macht", "a tot de tiende"),
                          ("drie a, in het kwadraat", "negen a kwadraat")],
                  "Vereenvoudig.", WL),
             ]),
        dict(kop="Van wortel naar macht en terug",
             opdracht="Vul de tabel aan. Links staat de wortelvorm, in het midden dezelfde uitdrukking als "
                      "macht met een rationale exponent, rechts de uitkomst als die een mooi getal is.",
             oefeningen=[
                 ("tabel", ["Wortelvorm", "Als macht", "Uitkomst"], [
                     ["de vierkantswortel uit 36", None, None],
                     ["de derdemachtswortel uit 27", None, None],
                     [None, "16 tot de macht een half", None],
                     ["de vierdemachtswortel uit 81", None, None],
                     [None, "8 tot de macht twee derde", None],
                     ["de derdemachtswortel uit 1000", None, None],
                 ],
                  "36 tot de macht een half is 6 · 27 tot de macht een derde is 3 · de vierkantswortel uit "
                  "16 is 4 · 81 tot de macht een vierde is 3 · de derdemachtswortel uit 8 in het kwadraat "
                  "is 4 · 1000 tot de macht een derde is 10", "150px"),
             ]),
        dict(kop="Rekenen met rationale exponenten",
             opdracht="Reken uit zonder toestel. Schrijf telkens eerst op welke rekenregel je gebruikt.",
             oefeningen=[
                 ("kort", "Hoeveel is 9 tot de macht een half?", "3", W),
                 ("kort", "Hoeveel is 125 tot de macht een derde?", "5", W),
                 ("kort", "Hoeveel is 4 tot de macht anderhalf?", "8", W),
                 ("kort", "Hoeveel is 16 tot de macht drie vierde?", "8", W),
                 ("kort", "Hoeveel is 32 tot de macht een vijfde?", "2", W),
                 ("kort", "Hoeveel is 100 tot de macht min een half?", "een tiende", WW),
                 ("open", "Reken 2 tot de macht een half maal 2 tot de macht een half uit, en leg uit "
                          "waarom dat 2 geeft.",
                  "Dezelfde grondtallen, dus exponenten optellen: een half plus een half is 1, en 2 tot de "
                  "macht 1 is 2. Het is ook de vierkantswortel uit 2 in het kwadraat.", 3),
                 ("open", "Waarom mag je bij 2 tot de macht 3 maal 5 tot de macht 3 de exponenten niet "
                          "optellen? Schrijf wel op wat je er dan wél van mag maken.",
                  "De grondtallen verschillen, en de regel geldt alleen bij hetzelfde grondtal. Je mag de "
                  "grondtallen samennemen: 2 maal 5 is 10, dus het is 10 tot de macht 3, oftewel 1000.", 3),
             ]),
        dict(kop="Bestaat het?",
             opdracht="Beslis of de uitdrukking een reëel getal oplevert. Schrijf bij nee waarom niet.",
             oefeningen=[
                 ("waar", "De vierkantswortel uit min 9 is een reëel getal.", False),
                 ("waar", "De derdemachtswortel uit min 8 is een reëel getal.", True),
                 ("waar", "Nul tot de macht min twee is een reëel getal.", False),
                 ("waar", "Min twee tot de macht drie is een reëel getal.", True),
                 ("open", "Leg in je eigen woorden uit waarom de vierkantswortel uit een negatief getal niet "
                          "bestaat, maar de derdemachtswortel wel.",
                  "Een kwadraat is nooit negatief, dus geen enkel reëel getal in het kwadraat geeft een "
                  "negatief getal. Bij een oneven macht blijft het minteken staan: min 2 tot de derde is "
                  "min 8, dus de derdemachtswortel uit min 8 is min 2.", 4),
             ]),
        dict(kop="In een situatie",
             opdracht="Werk uit. Schrijf je tussenstappen op.",
             oefeningen=[
                 ("open", "Een bedrag van 2000 euro groeit in 3 jaar naar 2315 euro. Schrijf op hoe je met "
                          "een rationale exponent de jaarlijkse groeifactor vindt. Rond af op drie cijfers "
                          "na de komma.",
                  "Je deelt eerst: 2315 gedeeld door 2000 is 1,1575. Dat is de groeifactor over 3 jaar. De "
                  "jaarlijkse groeifactor is 1,1575 tot de macht een derde, ongeveer 1,050. Dus ongeveer "
                  "5 procent per jaar.", 5),
                 ("open", "De oppervlakte van een vierkant is 50 vierkante centimeter. Schrijf de zijde als "
                          "macht met een rationale exponent, en geef de uitkomst op één cijfer na de komma.",
                  "De zijde is 50 tot de macht een half, ongeveer 7,1 centimeter.", 3),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-logaritmen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Logaritmen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van macht naar logaritme",
             opdracht="Vul de tabel aan. Links staat een machtsgelijkheid, rechts dezelfde gelijkheid als "
                      "logaritme.",
             oefeningen=[
                 ("tabel", ["Als macht", "Als logaritme"], [
                     ["twee tot de macht vijf is 32", None],
                     ["tien tot de macht drie is 1000", None],
                     [None, "de logaritme van 49 met grondtal 7 is 2"],
                     ["drie tot de macht vier is 81", None],
                     [None, "de logaritme van 0,001 met grondtal 10 is min 3"],
                 ],
                  "de logaritme van 32 met grondtal 2 is 5 · de logaritme van 1000 met grondtal 10 is 3 · "
                  "zeven tot de macht twee is 49 · de logaritme van 81 met grondtal 3 is 4 · tien tot de "
                  "macht min drie is 0,001", "230px"),
             ]),
        dict(kop="Reken uit zonder toestel",
             opdracht="Vraag je telkens af: tot welke macht moet ik het grondtal verheffen?",
             oefeningen=[
                 ("rij", [("de logaritme van 100 met grondtal 10", "2"),
                          ("de logaritme van 16 met grondtal 2", "4"),
                          ("de logaritme van 1 met grondtal 5", "0"),
                          ("de logaritme van 9 met grondtal 3", "2")],
                  "Reken uit.", WW),
                 ("rij", [("de logaritme van 0,1 met grondtal 10", "min 1"),
                          ("de logaritme van 64 met grondtal 4", "3"),
                          ("de logaritme van 6 met grondtal 6", "1"),
                          ("de logaritme van 1024 met grondtal 2", "10")],
                  "Reken uit.", WW),
                 ("kort", "Hoeveel is de logaritme van 1 miljoen met grondtal 10?", "6", W),
                 ("kort", "Hoeveel is de logaritme van 0,01 met grondtal 10?", "min 2", W),
             ]),
        dict(kop="Tussen welke twee gehele getallen?",
             opdracht="Je mag geen toestel gebruiken. Schrijf telkens de twee machten op waartussen het "
                      "getal ligt, en dan het antwoord.",
             oefeningen=[
                 ("kort", "De logaritme van 50 met grondtal 10 ligt tussen …", "1 en 2", W),
                 ("kort", "De logaritme van 3000 met grondtal 10 ligt tussen …", "3 en 4", W),
                 ("kort", "De logaritme van 100 met grondtal 2 ligt tussen …", "6 en 7", W),
                 ("kort", "De logaritme van 0,5 met grondtal 10 ligt tussen …", "min 1 en 0", W),
                 ("open", "Leg uit hoe je zonder toestel weet dat de logaritme van 3000 met grondtal 10 "
                          "tussen 3 en 4 ligt.",
                  "10 tot de macht 3 is 1000 en 10 tot de macht 4 is 10000. 3000 ligt daartussen, dus de "
                  "logaritme ook, tussen 3 en 4.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een bolletje bij je keuze. Bij elke bewering die niet waar is, schrijf je "
                      "eronder in één zin wat er wel geldt.",
             oefeningen=[
                 ("waar", "De logaritme van nul bestaat niet.", True),
                 ("waar", "De logaritme van 100 is bij elk grondtal gelijk aan 2.", False),
                 ("waar", "Bij een grondtal groter dan 1 geldt: hoe groter het getal, hoe groter de "
                          "logaritme.", True),
                 ("waar", "De logaritme van een negatief getal is negatief.", False),
                 ("waar", "Schrijf je log zonder grondtal erbij, dan bedoel je grondtal 10.", True),
                 ("open", "Schrijf in één zin waarom de logaritme van een negatief getal niet bestaat.",
                  "Een positief grondtal tot welke macht ook geeft nooit een negatief getal, dus er is geen "
                  "exponent die past.", 2),
             ]),
        dict(kop="Logaritmen gebruiken",
             opdracht="Werk uit. Je mag hier een toestel gebruiken; schrijf je stappen wel op.",
             oefeningen=[
                 ("open", "Een bedrag van 1000 euro groeit met 4 procent per jaar. Na hoeveel jaar is het "
                          "verdubbeld? Schrijf de vergelijking op en los ze op met een logaritme.",
                  "1,04 tot de macht x is 2, dus x is de logaritme van 2 met grondtal 1,04, ongeveer 17,7. "
                  "Na 18 jaar is het bedrag verdubbeld.", 5),
                 ("open", "Een stof vervalt met 10 procent per uur. Na hoeveel uur is er nog de helft over?",
                  "0,9 tot de macht x is 0,5, dus x is de logaritme van 0,5 met grondtal 0,9, ongeveer 6,6 uur.", 4),
                 ("open", "Een getal wordt tien keer zo groot gemaakt. Wat gebeurt er met zijn logaritme met "
                          "grondtal 10? Leg uit.",
                  "Die wordt 1 groter. Tien keer zo groot betekent één macht van 10 erbij, dus één bij de "
                  "exponent.", 3),
                 ("open", "Je toestel heeft alleen een knop voor grondtal 10. Hoe bereken je er de logaritme "
                          "van 50 met grondtal 2 mee?",
                  "Je deelt: de logaritme van 50 met grondtal 10 gedeeld door de logaritme van 2 met "
                  "grondtal 10, ongeveer 1,699 gedeeld door 0,301, dus ongeveer 5,64.", 4),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-een-functie-aflezen-van-haar-grafiek-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Een functie aflezen van haar grafiek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De woorden bij een grafiek",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("kort", "De verzameling van alle x-waarden waarvoor de functie bestaat.", "het domein", WW),
                 ("kort", "De verzameling van alle functiewaarden die de functie aanneemt.", "het bereik", WW),
                 ("kort", "Een x-waarde waarvoor de functiewaarde nul is.", "een nulpunt", WW),
                 ("kort", "Het hoogste punt van een grafiek in een bepaald gebied.", "een maximum", WW),
                 ("kort", "Het overzicht dat weergeeft waar een functie stijgt en waar ze daalt.",
                  "het verloopschema", WW),
                 ("kort", "Een grafiek die links en rechts van de y-as elkaars spiegelbeeld is.",
                  "de functie is even, de grafiek is symmetrisch om de y-as", WL),
                 ("kort", "De lengte van het stuk waarna een grafiek zich herhaalt.", "de periode", WW),
             ]),
        dict(kop="Tekenverloop en verloopschema",
             opdracht="Schrijf op wat elk teken betekent.",
             oefeningen=[
                 ("kort", "Een plusteken in het tekenverloop van een functie.",
                  "de functiewaarde is daar positief, de grafiek ligt boven de x-as", WL),
                 ("kort", "Een verticale streep in het tekenverloop.",
                  "daar is de functie niet gedefinieerd, of daar ligt een nulpunt", WL),
                 ("kort", "Min op x is 3 in het verloopschema.",
                  "de functie daalt vanaf x is 3", WL),
                 ("open", "Een grafiek loopt eerst omhoog tot x is 2, daalt dan tot x is 5 en stijgt daarna "
                          "weer. Schrijf het verloopschema in woorden en zeg wat er bij x is 2 en x is 5 ligt.",
                  "Stijgend tot 2, dalend van 2 tot 5, stijgend vanaf 5. Bij x is 2 ligt een maximum, bij "
                  "x is 5 een minimum.", 4),
             ]),
        dict(kop="Van tabel naar grafiek",
             opdracht="Zet de koppels uit op een assenstelsel en verbind ze. Zet er zelf een lijn met "
                      "getallen op de zijas bij, en schrijf naast je tekening wat je afleest.",
             oefeningen=[
                 ("teken", "Het aantal bezoekers van een winkel per uur: om 9 uur 20, om 11 uur 45, om "
                           "13 uur 60, om 15 uur 80, om 17 uur 35, om 19 uur 10. Teken de grafiek en "
                           "schrijf eronder wanneer het maximum valt en hoe groot het is.",
                  "De grafiek stijgt tot 15 uur en daalt daarna. Het maximum valt om 15 uur met 80 "
                  "bezoekers; het minimum om 19 uur met 10 bezoekers.", 70),
                 ("open", "Hoe noem je de twee getallen tussen haakjes die de plaats van een punt aangeven, "
                          "en welk getal staat vooraan?",
                  "De coördinaten. Vooraan staat de x-waarde, daarna de functiewaarde.", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een bolletje bij je keuze.",
             oefeningen=[
                 ("waar", "Het bereik lees je af op de verticale as.", True),
                 ("waar", "Twee functies met hetzelfde bereik kunnen een heel verschillende grafiek hebben.",
                  True),
                 ("waar", "Een functievoorschrift en een tabel van dezelfde functie kunnen elkaar "
                          "tegenspreken.", False),
                 ("waar", "Een grafiek schetsen zonder ICT betekent dat ze helemaal op schaal moet staan.",
                  False),
                 ("waar", "Een nulpunt is een punt waar de grafiek de x-as snijdt.", True),
             ]),
        dict(kop="Aflezen en terugvertalen",
             opdracht="Zeg telkens wat het getal of het kenmerk betekent in de situatie van de opgave.",
             oefeningen=[
                 ("open", "De grafiek van de temperatuur in een serre heeft een maximum bij 14 uur, met "
                          "32 graden. Schrijf dat in één zin in gewone taal.",
                  "Om 14 uur was het het warmst in de serre, namelijk 32 graden.", 2),
                 ("open", "De grafiek van de winst van een bedrijf in functie van het aantal verkochte "
                          "stuks heeft een nulpunt bij 150 stuks. Wat betekent dat?",
                  "Bij 150 stuks is de winst nul: daar wordt de kost precies goedgemaakt. Minder dan 150 "
                  "stuks geeft verlies.", 3),
                 ("open", "Een grafiek van het aantal bezoekers herhaalt zich elke 24 uur precies op "
                          "dezelfde manier. Hoe heet die 24 uur, en wat weet je daardoor over morgen?",
                  "Dat is de periode. Je mag verwachten dat morgen hetzelfde patroon terugkomt.", 3),
                 ("open", "Het bereik van de temperatuur in een koelkast is 3 tot 6 graden. Wat zegt dat "
                          "over de koelkast?",
                  "De temperatuur komt nooit lager dan 3 en nooit hoger dan 6 graden; ze schommelt "
                  "daartussen.", 2),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-gemiddelde-verandering-en-het-differentiequotient-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Gemiddelde verandering en het differentiequotiënt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het differentiequotiënt berekenen",
             opdracht="Reken uit: het verschil van de functiewaarden gedeeld door het verschil van de "
                      "x-waarden. Zet de eenheid erbij.",
             oefeningen=[
                 ("rij", [("180 kilometer in 3 uur", "60 kilometer per uur"),
                          ("van 10 naar 25 graden in 5 uur", "3 graden per uur"),
                          ("van 400 naar 100 liter in 6 minuten", "min 50 liter per minuut"),
                          ("van 20 naar 32 cm in 4 weken", "3 cm per week")],
                  "Bereken de gemiddelde verandering per eenheid.", WL),
                 ("kort", "Een spaarrekening gaat van 800 naar 1000 euro in 4 jaar. Hoeveel per jaar?",
                  "50 euro per jaar", WW),
                 ("kort", "Een stad telde in 2015 nog 40000 inwoners en in 2025 46000. Hoeveel per jaar?",
                  "600 inwoners per jaar", WW),
                 ("kort", "Een waterton gaat in 10 minuten van 90 naar 30 liter. Wat is het gemiddelde "
                          "debiet?", "min 6 liter per minuut, dus 6 liter per minuut eruit", WL),
                 ("kort", "Een bergweg klimt 150 meter over een afstand van 2500 meter. Hoeveel procent "
                          "bedraagt de gemiddelde helling?", "6 procent", WW),
             ]),
        dict(kop="De eenheid",
             opdracht="Schrijf bij elke functie welke eenheid het differentiequotiënt krijgt. Je hoeft niet "
                      "te rekenen.",
             oefeningen=[
                 ("rij", [("het aantal inwoners in functie van het jaartal", "inwoners per jaar"),
                          ("de temperatuur in functie van de tijd in uren", "graden per uur"),
                          ("de kostprijs in functie van het aantal stuks", "euro per stuk"),
                          ("de inhoud in functie van de tijd in minuten", "liter per minuut")],
                  "Welke eenheid?", WL),
             ]),
        dict(kop="Uit een tabel",
             opdracht="Vul de tabel aan met de gemiddelde verandering per jaar tussen elke twee opeenvolgende "
                      "jaren.",
             oefeningen=[
                 ("tabel", ["Jaar", "Aantal leden", "Verandering per jaar"], [
                     ["2020", "120", "—"],
                     ["2021", "150", None],
                     ["2022", "150", None],
                     ["2023", "210", None],
                     ["2024", "180", None],
                 ],
                  "2021: plus 30 per jaar · 2022: 0 per jaar · 2023: plus 60 per jaar · 2024: min 30 per jaar",
                  "120px"),
                 ("open", "In welk jaar groeide de club het snelst, en hoe zie je dat aan je getallen?",
                  "In 2023: daar is het differentiequotiënt het grootst, plus 60 per jaar.", 2),
             ]),
        dict(kop="Wat betekent het teken?",
             opdracht="Schrijf in één zin wat het getal betekent in de situatie.",
             oefeningen=[
                 ("open", "Het differentiequotiënt van de temperatuur in functie van de tijd is min 3 graden "
                          "per uur.",
                  "De temperatuur daalt gemiddeld met 3 graden per uur.", 2),
                 ("open", "Het differentiequotiënt van de voorraad in functie van de dagen is nul.",
                  "De voorraad is gemiddeld gelijk gebleven: evenveel bij als eraf, of niets veranderd.", 2),
                 ("open", "Van twee wandelaars heeft de ene een differentiequotiënt van 5 kilometer per uur "
                          "en de andere van 4 kilometer per uur, beide over dezelfde route. Wat besluit je?",
                  "De eerste wandelde gemiddeld sneller en was er dus eerder. Over de tussenstukken zegt het "
                  "niets: een gemiddelde verbergt wie waar gestopt is.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een bolletje bij je keuze.",
             oefeningen=[
                 ("waar", "Een gemiddelde verandering zegt niets over wat er tussen de twee tijdstippen "
                          "precies gebeurde.", True),
                 ("waar", "Als het differentiequotiënt positief is, is de functie over dat stuk gemiddeld "
                          "gestegen.", True),
                 ("waar", "Een differentiequotiënt kan je alleen uit een formule berekenen, niet uit een "
                          "tabel of een grafiek.", False),
                 ("waar", "Bij een rechte is het differentiequotiënt over elk stuk hetzelfde.", True),
             ]),
        dict(kop="Uit een grafiek",
             opdracht="Teken en lees af.",
             oefeningen=[
                 ("teken", "De inhoud van een vat: op 0 minuten 100 liter, op 5 minuten 70 liter, op "
                           "10 minuten 40 liter, op 15 minuten 40 liter, op 20 minuten 0 liter. Teken de "
                           "grafiek met getallen op de zijas, en schrijf eronder het differentiequotiënt "
                           "over de eerste tien minuten en over de laatste vijf.",
                  "Eerste tien minuten: min 60 gedeeld door 10 is min 6 liter per minuut. Laatste vijf "
                  "minuten: min 40 gedeeld door 5 is min 8 liter per minuut. Tussen 10 en 15 minuten "
                  "veranderde er niets.", 70),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-exponentiele-functies-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Exponentiële functies",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Beginwaarde en groeifactor aanwijzen",
             opdracht="Schrijf bij elk voorschrift de beginwaarde en de groeifactor op.",
             oefeningen=[
                 ("rij", [("f(x) is 5 maal 3 tot de macht x", "beginwaarde 5, groeifactor 3"),
                          ("f(x) is 200 maal 1,04 tot de macht x", "beginwaarde 200, groeifactor 1,04"),
                          ("f(x) is 0,8 tot de macht x", "beginwaarde 1, groeifactor 0,8"),
                          ("f(x) is 60 maal 0,5 tot de macht x", "beginwaarde 60, groeifactor 0,5")],
                  "Beginwaarde en groeifactor?", WL),
                 ("open", "Waarom is de beginwaarde altijd de functiewaarde bij x is nul?",
                  "Omdat elk grondtal tot de macht nul gelijk is aan 1. Er blijft dan alleen b over.", 2),
                 ("open", "Wat is het verschil tussen een exponentiële functie en een machtsfunctie? Geef "
                          "van elk een voorbeeld.",
                  "Bij een exponentiële functie staat de x in de exponent, bijvoorbeeld 2 tot de macht x. "
                  "Bij een machtsfunctie staat x in het grondtal, bijvoorbeeld x tot de macht 2.", 3),
             ]),
        dict(kop="Een tabel aanvullen",
             opdracht="Vul de tabel aan. Reken van links naar rechts: telkens maal de groeifactor.",
             oefeningen=[
                 ("tabel", ["x", "f(x) is 4 maal 3 tot de macht x"], [
                     ["0", None], ["1", None], ["2", None], ["3", None], ["4", None],
                 ], "4 · 12 · 36 · 108 · 324", "90px"),
                 ("tabel", ["x", "f(x) is 800 maal 0,5 tot de macht x"], [
                     ["0", None], ["1", None], ["2", None], ["3", None], ["4", None],
                 ], "800 · 400 · 200 · 100 · 50", "90px"),
             ]),
        dict(kop="De groeifactor uit twee waarden",
             opdracht="Werk uit. Schrijf je deling op.",
             oefeningen=[
                 ("open", "Een tabel geeft bij x is 0 de waarde 7 en bij x is 1 de waarde 21. Schrijf het "
                          "voorschrift op.",
                  "21 gedeeld door 7 is 3, dus de groeifactor is 3. Het voorschrift is f(x) is 7 maal 3 tot "
                  "de macht x.", 3),
                 ("open", "Een tabel geeft bij x is 0 de waarde 500 en bij x is 2 de waarde 320. Zoek de "
                          "groeifactor per stap van één.",
                  "320 gedeeld door 500 is 0,64 over twee stappen. De groeifactor per stap is de "
                  "vierkantswortel uit 0,64, dus 0,8.", 4),
                 ("open", "Een tabel geeft 5, 15, 45, 135. Hoe zie je in één blik dat dit exponentieel is, "
                          "en wat is de groeifactor?",
                  "Je deelt elk getal door het vorige: telkens 3. Omdat die deling altijd hetzelfde geeft, "
                  "is het exponentieel met groeifactor 3.", 3),
             ]),
        dict(kop="De grafiek",
             opdracht="Antwoord in één zin.",
             oefeningen=[
                 ("kort", "Wat is het domein van een exponentiële functie?", "alle reële getallen", WL),
                 ("kort", "Wat is het bereik van f(x) is 4 maal 2 tot de macht x?",
                  "alle positieve reële getallen, dus alles boven nul", WL),
                 ("open", "Wat gebeurt er met een dalende exponentiële functie als x heel groot wordt? "
                          "Gebruik het woord asymptoot.",
                  "De functiewaarde komt steeds dichter bij nul zonder nul te bereiken: de x-as is een "
                  "horizontale asymptoot.", 3),
                 ("teken", "Schets in één assenstelsel f(x) is 2 tot de macht x en g(x) is 0,5 tot de macht "
                           "x. Zet er de getallen bij op beide assen, en schrijf eronder wat de twee "
                           "grafieken gemeenschappelijk hebben.",
                  "Beide gaan door het punt met x is 0 en functiewaarde 1, beide blijven boven de x-as, en "
                  "ze zijn elkaars spiegelbeeld om de y-as. De ene stijgt, de andere daalt.", 75),
             ]),
        dict(kop="In een situatie",
             opdracht="Werk uit met je tussenstappen.",
             oefeningen=[
                 ("open", "Een bacteriënkolonie van 50 verdubbelt elk uur. Schrijf het voorschrift en bereken "
                          "hoeveel er na 6 uur zijn.",
                  "f(x) is 50 maal 2 tot de macht x. Na 6 uur: 50 maal 64 is 3200 bacteriën.", 4),
                 ("open", "Een auto van 24000 euro verliest elk jaar 18 procent van zijn waarde. Schrijf het "
                          "voorschrift en bereken de waarde na 4 jaar. Rond af op een euro.",
                  "De groeifactor is 0,82, dus f(x) is 24000 maal 0,82 tot de macht x. Na 4 jaar: 24000 maal "
                  "0,4521 is ongeveer 10851 euro.", 4),
                 ("open", "Een medicijn breekt af met 25 procent per uur. Na hoeveel volle uren is er nog "
                          "minder dan een tiende over? Je mag een toestel gebruiken.",
                  "0,75 tot de macht x moet onder 0,1 komen. Bij 8 uur is dat 0,100, bij 9 uur 0,075. Dus na "
                  "9 uur.", 4),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-lineaire-en-exponentiele-groeimodellen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Lineaire en exponentiële groeimodellen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk model?",
             opdracht="Beslis bij elke reeks of de groei lineair of exponentieel is, en schrijf het getal of "
                      "de factor erbij.",
             oefeningen=[
                 ("rij", [("12, 19, 26, 33", "lineair, telkens 7 erbij"),
                          ("10, 20, 40, 80", "exponentieel, factor 2"),
                          ("90, 81, 72,9, 65,61", "exponentieel, factor 0,9"),
                          ("200, 185, 170, 155", "lineair, telkens 15 eraf")],
                  "Lineair of exponentieel?", WL),
                 ("rij", [("48, 36, 27, 20,25", "exponentieel, factor 0,75"),
                          ("5, 10, 15, 20", "lineair, telkens 5 erbij"),
                          ("1000, 1050, 1102,5", "exponentieel, factor 1,05"),
                          ("7, 7, 7, 7", "geen groei, lineair met 0 erbij")],
                  "Lineair of exponentieel?", WL),
                 ("open", "Schrijf in je eigen woorden het kenmerk van lineaire groei en het kenmerk van "
                          "exponentiële groei.",
                  "Bij lineaire groei komt elke tijdseenheid hetzelfde getal bij. Bij exponentiële groei "
                  "vermenigvuldig je elke tijdseenheid met dezelfde factor, zodat het bedrag dat erbij komt "
                  "zelf ook groeit.", 3),
             ]),
        dict(kop="Groeifactor en percentage",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Per jaar", "Groeifactor"], [
                     ["6 procent erbij", None],
                     ["2,5 procent erbij", None],
                     [None, "0,88"],
                     ["15 procent eraf", None],
                     [None, "1,5"],
                     ["de waarde verdubbelt", None],
                 ],
                  "1,06 · 1,025 · 12 procent eraf · 0,85 · 50 procent erbij · 2", "140px"),
                 ("kort", "Een prijs stijgt drie jaar op rij met 10 procent. Met welke factor is ze dan in "
                          "totaal vermenigvuldigd? Rond af op drie cijfers.", "1,331", WW),
                 ("open", "Een winkel geeft eerst 20 procent korting en daarna nog 20 procent op de nieuwe "
                          "prijs. Is dat samen 40 procent korting? Reken het na.",
                  "Nee. 0,8 maal 0,8 is 0,64, dus er blijft 64 procent over en de korting is 36 procent, "
                  "niet 40.", 3),
             ]),
        dict(kop="Een model opstellen",
             opdracht="Schrijf het voorschrift op en zeg welk model het is.",
             oefeningen=[
                 ("open", "Een abonnement kost 30 euro aansluiting en daarna 12 euro per maand.",
                  "Lineair: prijs is 30 plus 12 maal x, met beginwaarde 30.", 2),
                 ("open", "Een spaarrekening van 1500 euro met 3 procent rente per jaar.",
                  "Exponentieel: bedrag is 1500 maal 1,03 tot de macht x.", 2),
                 ("open", "Een vijver met 60 waterlelies waarvan het aantal elk jaar met de helft toeneemt.",
                  "Exponentieel: aantal is 60 maal 1,5 tot de macht x.", 2),
                 ("open", "Een voorraad van 900 stuks waarvan er elke week 75 verkocht worden.",
                  "Lineair: voorraad is 900 min 75 maal x.", 2),
             ]),
        dict(kop="De twee vergelijken",
             opdracht="Werk uit. Vul eerst de tabel aan, antwoord dan.",
             oefeningen=[
                 ("tabel", ["Jaar", "Model A: 100 plus 20 maal x", "Model B: 100 maal 1,2 tot de macht x"], [
                     ["0", None, None], ["2", None, None], ["5", None, None], ["10", None, None],
                 ],
                  "jaar 0: 100 en 100 · jaar 2: 140 en 144 · jaar 5: 200 en ongeveer 249 · jaar 10: 300 en "
                  "ongeveer 619", "100px"),
                 ("open", "Welk model haalt het andere in, en wat besluit je daaruit over lineaire en "
                          "exponentiële groei op lange termijn?",
                  "Model B haalt model A in, al vanaf jaar 2. Exponentiële groei wint op lange termijn altijd "
                  "van lineaire groei, al kan dat even duren.", 3),
                 ("waar", "Bij exponentiële afname bereikt de hoeveelheid ooit precies nul.", False),
                 ("open", "Waarom groeit een populatie in de werkelijkheid zelden eindeloos exponentieel?",
                  "Ruimte, voedsel en andere middelen raken op. Het model past alleen in het begin; daarna "
                  "vlakt de groei af.", 3),
             ]),
        dict(kop="Uit een situatie beslissen",
             opdracht="Lees en beslis welk model past. Schrijf waarom.",
             oefeningen=[
                 ("open", "Een tabel toont 72, 66, 60, 54.",
                  "Lineair, telkens 6 eraf: het verschil blijft gelijk. Bij exponentiële afname zou het "
                  "verschil zelf ook kleiner worden.", 2),
                 ("open", "Een tabel toont 81, 54, 36, 24.",
                  "Exponentieel met factor twee derde, ongeveer 0,67: 54 gedeeld door 81 is hetzelfde als 36 "
                  "gedeeld door 54. Het verschil wordt steeds kleiner.", 3),
                 ("open", "Een gemeente plant elk jaar 40 bomen bij. Het aantal bomen gaat van 400 naar 440 "
                          "naar 480. Welk model, en hoeveel na 12 jaar?",
                  "Lineair: 400 plus 40 maal x. Na 12 jaar 880 bomen.", 3),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-kansen-en-de-wet-van-laplace-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kansen en de wet van Laplace",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De woorden",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("kort", "De verzameling van alle mogelijke uitkomsten van een kansexperiment.",
                  "de uitkomstenverzameling", WW),
                 ("kort", "Een deel van de uitkomstenverzameling.", "een gebeurtenis", WW),
                 ("kort", "Het aantal gunstige gevallen gedeeld door het totaal aantal gevallen.",
                  "de wet van Laplace", WW),
                 ("kort", "Alles wat niet bij een gebeurtenis hoort.", "het complement", WW),
                 ("open", "Hoeveel uitkomsten zitten er in de uitkomstenverzameling als je met twee "
                          "dobbelstenen gooit, en hoe kom je daaraan?",
                  "36. Zes mogelijkheden voor de eerste maal zes voor de tweede.", 2),
             ]),
        dict(kop="Kansen uitrekenen",
             opdracht="Schrijf elke kans als breuk, zo eenvoudig mogelijk.",
             oefeningen=[
                 ("rij", [("een even getal met één dobbelsteen", breuk(1, 2)),
                          ("een getal groter dan 4 met één dobbelsteen", breuk(1, 3)),
                          ("harten uit een spel van 52 kaarten", breuk(1, 4)),
                          ("een aas uit een spel van 52 kaarten", breuk(1, 13))],
                  "Schrijf als breuk.", WW),
                 ("rij", [("twee keer kop bij twee munten", breuk(1, 4)),
                          ("precies één keer kop bij twee munten", breuk(1, 2)),
                          ("som 7 met twee dobbelstenen", breuk(1, 6)),
                          ("som 12 met twee dobbelstenen", breuk(1, 36))],
                  "Schrijf als breuk.", WW),
                 ("kort", "In een zak zitten 5 rode, 3 blauwe en 2 groene knikkers. Wat is de kans op een "
                          "blauwe?", breuk(3, 10), WW),
                 ("kort", "Een klas heeft 12 meisjes en 13 jongens. Wat is de kans dat een willekeurige "
                          "leerling een meisje is?", breuk(12, 25), WW),
             ]),
        dict(kop="Complement en som",
             opdracht="Gebruik dat de kans op het complement 1 min de kans is.",
             oefeningen=[
                 ("kort", "De kans op regen is 0,35. Wat is de kans op geen regen?", "0,65", W),
                 ("kort", "De kans op minstens één zes bij twee worpen is 11 op 36. Wat is de kans op geen "
                          "enkele zes?", breuk(25, 36), WW),
                 ("kort", "De kans dat een toestel stuk gaat binnen het jaar is 0,04. Wat is de kans dat het "
                          "blijft werken?", "0,96", W),
                 ("open", "Leg uit waarom de som van de kansen van alle uitkomsten samen altijd 1 is.",
                  "Er moet altijd íets gebeuren. Alle uitkomsten samen vormen de hele "
                  "uitkomstenverzameling, en dat is zekerheid.", 2),
                 ("open", "Waarom is een kans nooit groter dan 1 en nooit kleiner dan 0?",
                  "Het aantal gunstige gevallen kan niet groter zijn dan het totaal, en niet negatief. 0 "
                  "betekent onmogelijk, 1 betekent zeker.", 3),
             ]),
        dict(kop="Kans of meting?",
             opdracht="Beslis en leg uit in één zin.",
             oefeningen=[
                 ("open", "Je gooit 10 keer met een munt en krijgt 7 keer kop. Betekent dat dat de kans op "
                          "kop niet een half is?",
                  "Nee. Bij weinig worpen kan de uitkomst flink afwijken van de kans. Hoe meer worpen, hoe "
                  "dichter de verhouding bij een half komt.", 3),
                 ("open", "Een dobbelsteen gaf vier keer op rij geen zes. Is de kans op een zes bij de "
                          "volgende worp daardoor groter?",
                  "Nee. De dobbelsteen heeft geen geheugen: de kans blijft een zesde.", 2),
                 ("waar", "De wet van Laplace mag je alleen gebruiken als alle uitkomsten even "
                          "waarschijnlijk zijn.", True),
                 ("open", "Waarom mag je de wet van Laplace niet gebruiken om de kans te berekenen dat het "
                          "morgen regent?",
                  "Regen en geen regen zijn niet even waarschijnlijk, en je kan de gevallen niet eerlijk "
                  "tellen. Daarvoor heb je gegevens nodig, geen symmetrie.", 3),
             ]),
        dict(kop="Tellen in een situatie",
             opdracht="Werk uit. Schrijf telkens op hoeveel gunstige gevallen en hoeveel gevallen in totaal.",
             oefeningen=[
                 ("open", "Een rad heeft 20 even grote vakjes: 4 met een prijs, de rest leeg. Wat is de kans "
                          "op een prijs, en wat is de kans op niets?",
                  "4 gunstige op 20, dus een vijfde of 0,2. De kans op niets is vier vijfde of 0,8.", 3),
                 ("open", "Een school van 400 leerlingen heeft 240 meisjes, waarvan 60 in het vijfde jaar. "
                          "Wat is de kans dat een willekeurige leerling een meisje uit het vijfde jaar is?",
                  "60 op 400, dus drie twintigsten of 0,15.", 3),
                 ("open", "In een doos liggen 12 lampen, waarvan 3 stuk. Je neemt er één. Wat is de kans dat "
                          "ze werkt?",
                  "9 werkende op 12, dus drie vierde of 0,75.", 3),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-kansbomen-product-som-en-complement-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kansbomen: product, som en complement",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke regel?",
             opdracht="Schrijf bij elke vraag welke regel je gebruikt: de productregel, de somregel of de "
                      "complementregel.",
             oefeningen=[
                 ("kort", "De kans op twee keer kop achter elkaar.", "de productregel", WW),
                 ("kort", "De kans op een twee of een vijf met één worp.", "de somregel", WW),
                 ("kort", "De kans op minstens één zes bij drie worpen.", "de complementregel", WW),
                 ("kort", "De kans op eerst rood en dan blauw uit een zak.", "de productregel", WW),
                 ("kort", "De kans op harten of ruiten uit één spel kaarten.", "de somregel", WW),
                 ("open", "Wanneer mag je twee kansen gewoon optellen, en wanneer niet?",
                  "Alleen als de twee gebeurtenissen elkaar uitsluiten, dus niet samen kunnen gebeuren. "
                  "Kunnen ze samen, dan tel je het gemeenschappelijke stuk dubbel.", 3),
             ]),
        dict(kop="Een kansboom tekenen",
             opdracht="Teken de boom met alle takken, zet de kans bij elke tak en reken de gevraagde kans uit.",
             oefeningen=[
                 ("teken", "Je gooit twee keer met een munt. Teken de kansboom en bereken de kans op precies "
                           "één keer kop.",
                  "Vier paden, elk met kans een vierde. Twee paden geven precies één keer kop (kop-munt en "
                  "munt-kop), dus een vierde plus een vierde is een half.", 75),
                 ("teken", "In een zak zitten 4 rode en 6 blauwe knikkers. Je neemt er twee zonder terugleggen. "
                           "Teken de kansboom en bereken de kans op twee rode.",
                  "Eerste tak rood: 4 op 10. Tweede tak rood: 3 op 9, want er is er één uit. Vier tienden "
                  "maal drie negenden is twaalf negentigsten, oftewel twee vijftienden.", 80),
             ]),
        dict(kop="Met of zonder terugleggen",
             opdracht="Vul de tabel aan met de kans op twee rode uit een zak met 5 rode en 5 witte knikkers.",
             oefeningen=[
                 ("tabel", ["", "Kans op de eerste rode", "Kans op de tweede rode", "Kans op twee rode"], [
                     ["met terugleggen", None, None, None],
                     ["zonder terugleggen", None, None, None],
                 ],
                  "met terugleggen: 5 op 10, 5 op 10, een vierde · zonder terugleggen: 5 op 10, 4 op 9, twee "
                  "negendes", "100px"),
                 ("open", "Waarom verandert de tweede kans bij zonder terugleggen, en bij met terugleggen niet?",
                  "Zonder terugleggen is er één knikker minder in de zak en één rode minder, dus de "
                  "verhouding verandert. Met terugleggen is de zak weer precies zoals in het begin.", 3),
             ]),
        dict(kop="Rekenen met de drie regels",
             opdracht="Reken uit. Schrijf je bewerking op.",
             oefeningen=[
                 ("kort", "De kans op drie keer kop achter elkaar.", breuk(1, 8), WW),
                 ("kort", "De kans op twee keer een zes met twee dobbelstenen.", breuk(1, 36), WW),
                 ("kort", "De kans op minstens één kop bij twee munten.", breuk(3, 4), WW),
                 ("kort", "De kans op minstens één zes bij twee worpen.", breuk(11, 36), WW),
                 ("kort", "De kans op een drie of een vier met één dobbelsteen.", breuk(1, 3), WW),
                 ("open", "Bereken de kans op minstens één zes bij vier worpen. Gebruik de complementregel en "
                          "rond af op twee cijfers na de komma.",
                  "De kans op geen enkele zes is vijf zesden tot de macht 4, ongeveer 0,48. Dus de kans op "
                  "minstens één zes is ongeveer 0,52.", 4),
                 ("open", "Een toets heeft 3 waar-of-niet-waar-vragen. Wat is de kans dat je ze met gokken "
                          "alle drie juist hebt, en wat is de kans dat je er minstens één fout hebt?",
                  "Alle drie juist: een half tot de macht 3 is een achtste. Minstens één fout is het "
                  "complement: zeven achtsten.", 4),
             ]),
        dict(kop="In een situatie",
             opdracht="Werk uit met je tussenstappen.",
             oefeningen=[
                 ("open", "Een machine maakt stukken waarvan 2 procent slecht is. Je neemt er twee. Wat is de "
                          "kans dat ze allebei goed zijn, en wat is de kans dat er minstens één slecht is?",
                  "0,98 maal 0,98 is 0,9604, dus ongeveer 96 procent allebei goed. Minstens één slecht is het "
                  "complement: ongeveer 4 procent.", 4),
                 ("open", "Twee lampen branden onafhankelijk van elkaar; elke lamp gaat met kans 0,1 stuk "
                          "binnen het jaar. Wat is de kans dat er na een jaar nog minstens één brandt?",
                  "Beide stuk: 0,1 maal 0,1 is 0,01. Minstens één brandt nog: 1 min 0,01 is 0,99.", 4),
                 ("open", "In een klas van 20 leerlingen worden er twee aangeduid, zonder dat iemand twee keer "
                          "kan. Wat is de kans dat de twee grootste leerlingen aangeduid worden?",
                  "2 op 20 maal 1 op 19 is twee driehonderdtachtigsten, oftewel 1 op 190.", 4),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-populatie-steekproef-en-representativiteit-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Populatie, steekproef en representativiteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Populatie, steekproef, variabele",
             opdracht="Vul de tabel aan voor elk onderzoek.",
             oefeningen=[
                 ("tabel", ["Onderzoek", "Populatie", "Steekproef", "Variabele"], [
                     ["Hoeveel uren sport een Vlaamse jongere per week? 300 jongeren bevraagd.",
                      None, None, None],
                     ["Wat weegt een zak chips van 200 gram echt? Elk uur 5 zakken gewogen.",
                      None, None, None],
                     ["Hoe lang doen de leerlingen van onze school over hun huiswerk? 60 leerlingen bevraagd.",
                      None, None, None],
                 ],
                  "1: alle Vlaamse jongeren · de 300 bevraagde jongeren · het aantal uren sport per week. "
                  "2: alle zakken chips van die productie · de gewogen zakken · het gewicht. "
                  "3: alle leerlingen van de school · de 60 bevraagde leerlingen · de tijd voor het huiswerk.",
                  "130px"),
                 ("open", "Waarom werk je met een steekproef in plaats van de hele populatie te meten?",
                  "Omdat de hele populatie meten vaak onmogelijk of te duur is. Je ruilt werk in voor "
                  "onzekerheid over je besluit.", 2),
                 ("kort", "Een school van 600 leerlingen bevraagt er 90. Hoeveel procent van de populatie is "
                          "de steekproef?", "15 procent", W),
             ]),
        dict(kop="Aselect, vertekend, representatief",
             opdracht="Beslis bij elke manier van kiezen of de steekproef aselect is, en schrijf bij een "
                      "vertekende steekproef wie ontbreekt of te zwaar weegt.",
             oefeningen=[
                 ("open", "Alle leden van de voetbalclub bevragen over hoeveel ze sporten.",
                  "Vertekend: wie niet sport zit er niet in, dus de uitkomst ligt te hoog.", 2),
                 ("open", "Namen uit een lijst van alle leerlingen laten kiezen door een toevalsgenerator.",
                  "Aselect: elke leerling heeft dezelfde kans.", 2),
                 ("open", "Bellen tussen 9 en 17 uur op een werkdag.",
                  "Vertekend: wie overdag werkt, neemt niet op.", 2),
                 ("open", "Een vragenlijst online zetten en afwachten wie ze invult.",
                  "Vertekend: alleen wie zich betrokken voelt, vult ze in.", 2),
                 ("open", "Elke honderdste doos van de band testen.",
                  "Een systematische steekproef, bruikbaar zolang er geen patroon in de productie met dat "
                  "ritme meeloopt.", 3),
                 ("open", "De baas voert zelf de tevredenheidsgesprekken met het personeel.",
                  "Vertekend: mensen antwoorden minder eerlijk tegen hun eigen baas.", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een bolletje bij je keuze. Verbeter elke onjuiste bewering in één zin.",
             oefeningen=[
                 ("waar", "Een grotere steekproef is altijd representatief.", False),
                 ("waar", "Een vertekende steekproef kan je rechtzetten door er meer mensen bij te nemen op "
                          "dezelfde manier.", False),
                 ("waar", "Als een steekproef aselect is, wordt het besluit betrouwbaarder bij een grotere "
                          "steekproef.", True),
                 ("waar", "Ook een aselecte steekproef kan door puur toeval scheef uitvallen.", True),
                 ("waar", "Een steekproef van 1000 mensen kan betrouwbare uitspraken geven over miljoenen "
                          "mensen.", True),
                 ("waar", "Statistiek geeft zekerheid over de populatie.", False),
             ]),
        dict(kop="De notatie",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("het gemiddelde van een populatie", "de Griekse letter mu"),
                          ("het gemiddelde van een steekproef", "x met een streepje erboven"),
                          ("de standaardafwijking van een populatie", "de Griekse letter sigma"),
                          ("de standaardafwijking van een steekproef", "een gewone s")],
                  "Welk symbool?", WL),
                 ("open", "Waarom gebruiken statistici verschillende letters voor de steekproef en de "
                          "populatie?",
                  "Zodat je aan de notatie meteen ziet of een getal gemeten is in de steekproef of gaat over "
                  "de hele populatie. Het ene is bekend, het andere wordt geschat.", 3),
             ]),
        dict(kop="Een besluit beoordelen",
             opdracht="Schrijf bij elk besluit of het mag, en waarom niet als het niet mag.",
             oefeningen=[
                 ("open", "Een onderzoeker meet de leeftijd van bezoekers op een rockfestival en besluit dat "
                          "de gemiddelde Belg 24 jaar is.",
                  "Mag niet. Festivalbezoekers zijn geen aselecte steekproef van alle Belgen. Het besluit "
                  "geldt hoogstens voor dat festival.", 3),
                 ("open", "Een krant schrijft dat uit een bevraging van 40 mensen blijkt dat 60 procent van "
                          "de Belgen iets vindt. Wat is je eerste vraag?",
                  "Hoe werden die 40 mensen gekozen? De manier van kiezen weegt zwaarder dan het aantal.", 2),
                 ("open", "Een peiling voorspelde een uitslag die er ver naast zat. Waar zit de fout meestal?",
                  "In een niet-representatieve steekproef, niet in het rekenwerk erna.", 2),
                 ("open", "Een fabrikant belooft dat elke zak minstens 500 gram bevat. Hoe zou je dat met een "
                          "steekproef nakijken, en wat meet je dan precies?",
                  "Aselect zakken uit de geproduceerde voorraad nemen, verspreid over de dag, en elk gewicht "
                  "opmeten. De variabele is het gewicht per verpakking; uit het steekproefgemiddelde en de "
                  "spreiding schat je wat de machine doet.", 4),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-samenhang-en-causaliteit-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Samenhang en causaliteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vier verklaringen",
             opdracht="Bij elke vaststelling hoort één van de vier: causaliteit, omgewisselde causaliteit, een "
                      "verborgen variabele of toeval. Schrijf welke, en noem bij een verborgen variabele welke.",
             oefeningen=[
                 ("open", "In de zomer worden er meer ijsjes verkocht en zijn er meer verdrinkingen.",
                  "Een verborgen variabele: het warme weer zorgt voor beide.", 2),
                 ("open", "Kinderen met grotere voeten lezen beter.",
                  "Een verborgen variabele: de leeftijd. Oudere kinderen hebben grotere voeten en lezen beter.", 2),
                 ("open", "Mensen die meer water drinken, hebben minder hoofdpijn.",
                  "Mogelijk omgewisselde causaliteit: wie hoofdpijn heeft, drinkt minder.", 2),
                 ("open", "Steden met meer brandweermannen hebben meer brandschade.",
                  "Een verborgen variabele: de grootte van de stad.", 2),
                 ("open", "Twee reeksen lopen tien jaar lang bijna perfect samen zonder dat iemand kan "
                          "uitleggen waarom.",
                  "Toeval, een toevallige samenhang. Bij korte reeksen of veel zoeken komt zo'n gelijkloop "
                  "vanzelf voor.", 2),
                 ("open", "Scholen met meer computers halen betere resultaten.",
                  "Een verborgen variabele: het budget van de school, en alles wat daarmee meekomt.", 2),
                 ("open", "Mensen met een hond bewegen meer.",
                  "Mogelijk omgewisselde causaliteit: wie graag beweegt, neemt vaker een hond.", 2),
                 ("open", "Roken en longkanker hangen samen.",
                  "Causaliteit: er is een mechanisme, en gecontroleerd onderzoek bevestigt het.", 2),
             ]),
        dict(kop="Krantenkoppen voorzichtig lezen",
             opdracht="Herschrijf de kop zo dat er alleen staat wat de cijfers echt toelaten.",
             oefeningen=[
                 ("open", "Wie ontbijt, haalt betere punten.",
                  "Ontbijten hangt samen met betere punten. Of het ontbijt zelf dat doet, blijkt er niet uit; "
                  "een rustiger gezinssituatie kan meespelen.", 3),
                 ("open", "Koffie verlengt je leven, blijkt uit een bevraging.",
                  "Koffiedrinken hangt samen met langer leven in deze bevraging. Een bevraging toont "
                  "samenhang, geen oorzaak.", 3),
                 ("open", "Veel huiswerk maken geeft hogere punten.",
                  "Wie veel huiswerk maakt, haalt gemiddeld hogere punten. De richting is onduidelijk, en "
                  "motivatie kan de verborgen variabele zijn.", 3),
                 ("open", "Onze gemeente plaatste meer straatlampen en de criminaliteit daalde.",
                  "Na het plaatsen van meer lampen daalde de criminaliteit. Je moet nagaan of ze elders ook "
                  "daalde voor je de lampen de oorzaak noemt.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Zet een bolletje bij je keuze.",
             oefeningen=[
                 ("waar", "Samenhang betekent altijd dat er een oorzakelijk verband is.", False),
                 ("waar", "Samenhang kan ook negatief zijn.", True),
                 ("waar", "Een verborgen variabele staat gewoon in de tabel van het onderzoek.", False),
                 ("waar", "Een onderzoek dat alleen waarneemt, kan nooit met zekerheid een oorzaak aantonen.",
                  True),
                 ("waar", "Een onderzoeker die een causaal verband suggereert, heeft daarmee automatisch "
                          "gelijk.", False),
                 ("waar", "Een controlegroep helpt om een causaal verband aan te tonen.", True),
             ]),
        dict(kop="Een onderzoek opzetten",
             opdracht="Werk uit. Schrijf telkens op wat je verandert, wat je gelijk houdt en wat je meet.",
             oefeningen=[
                 ("open", "Je wil weten of een nieuw soort plantenvoeding tomaten sneller doet groeien. "
                          "Beschrijf een gecontroleerd experiment met een controlegroep.",
                  "Twee gelijke groepen plantjes, dezelfde soort, dezelfde pot, dezelfde grond, hetzelfde "
                  "licht en water. Eén groep krijgt de voeding, de controlegroep niet. Je meet de hoogte na "
                  "een vaste tijd. Alleen de voeding verschilt, dus een verschil in groei mag je daaraan "
                  "toeschrijven.", 6),
                 ("open", "Een reclame zegt: wie ons product gebruikt, is gezonder. Wat ontbreekt er in dat "
                          "argument?",
                  "De vergelijking met een gelijkaardige groep die het product niet gebruikt. Zonder "
                  "controlegroep weet je niet of het product iets doet.", 3),
                 ("open", "Een verzekeraar merkt dat rode auto's vaker een ongeval hebben. Welke twee vragen "
                          "stel je voor je besluit dat de kleur gevaarlijk is?",
                  "Is er een verklaring hoe de kleur het rijden beïnvloedt? En is er een verborgen variabele, "
                  "bijvoorbeeld wie rood kiest en hoe die rijdt?", 4),
                 ("open", "Waarom is vragen naar de opzet van een onderzoek zinvoller dan vragen naar de "
                          "berekening?",
                  "De opzet bepaalt wat je mag besluiten. Het rekenwerk klopt meestal wel; de fout zit bijna "
                  "altijd in hoe de gegevens verzameld zijn.", 3),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-de-normale-verdeling-en-de-gausskromme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De normale verdeling en de Gausskromme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De klokvorm",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet de klokvormige kromme van een normale verdeling?", "de Gausskromme", WW),
                 ("kort", "Welke twee getallen leggen een normale verdeling helemaal vast?",
                  "het gemiddelde en de standaardafwijking", WL),
                 ("kort", "Waar ligt de top van de Gausskromme?", "bij het gemiddelde", WW),
                 ("kort", "Hoe groot is de totale oppervlakte onder een Gausskromme?", "1", W),
                 ("kort", "Welke drie kengetallen vallen bij een normale verdeling samen?",
                  "gemiddelde, mediaan en modus", WL),
                 ("open", "Wat verandert er aan de kromme als de standaardafwijking groter wordt, en waarom "
                          "wordt ze dan ook platter?",
                  "Ze wordt breder. Omdat de oppervlakte eronder altijd 1 blijft, moet ze bij een grotere "
                  "breedte lager worden.", 3),
             ]),
        dict(kop="Twee krommen vergelijken",
             opdracht="Beslis en leg in één zin uit.",
             oefeningen=[
                 ("open", "Twee Gausskrommen hebben hetzelfde gemiddelde; de ene is veel smaller. Welke heeft "
                          "de kleinste standaardafwijking?",
                  "De smalle: de waarden liggen dichter bij het gemiddelde.", 2),
                 ("open", "Twee Gausskrommen zijn even breed; de ene ligt meer naar rechts. Wat weet je over "
                          "hun gemiddelden en hun standaardafwijkingen?",
                  "De rechtse heeft het grootste gemiddelde; de standaardafwijkingen zijn gelijk. "
                  "Verschuiven doet het gemiddelde, uitrekken de standaardafwijking.", 3),
                 ("open", "Twee klassen hebben hetzelfde gemiddelde, maar de ene heeft een veel grotere "
                          "standaardafwijking. Wat betekent dat voor de punten?",
                  "Daar liggen de punten verder uit elkaar: meer heel sterke én meer heel zwakke resultaten.", 3),
                 ("open", "Een machine vult zakken van 500 gram en heeft een kleine standaardafwijking. Wat "
                          "zegt dat over de machine?",
                  "Ze vult heel nauwkeurig: de zakken wijken weinig van 500 gram af.", 2),
             ]),
        dict(kop="De vuistregel van 68 en 95",
             opdracht="Vul de tabel aan voor een normale verdeling met gemiddelde 180 en standaardafwijking 8.",
             oefeningen=[
                 ("tabel", ["Binnen hoeveel standaardafwijkingen", "Tussen welke waarden", "Welk aandeel"], [
                     ["één", None, None],
                     ["twee", None, None],
                 ],
                  "één: tussen 172 en 188, ongeveer 68 procent · twee: tussen 164 en 196, ongeveer 95 procent",
                  "150px"),
                 ("kort", "Een IQ-test heeft gemiddelde 100 en standaardafwijking 15. Tussen welke waarden "
                          "ligt ongeveer 68 procent?", "tussen 85 en 115", WW),
                 ("kort", "Hoeveel procent van die IQ-scores ligt boven 130?", "ongeveer 2,5 procent", WW),
                 ("kort", "Hoeveel procent ligt buiten twee standaardafwijkingen van het gemiddelde?",
                  "ongeveer 5 procent, verdeeld over beide staarten", WL),
                 ("open", "Een toets heeft gemiddelde 60 en standaardafwijking 10. Iemand scoort 85. Is dat "
                          "uitzonderlijk? Reken na.",
                  "85 ligt 25 boven het gemiddelde, dus 2,5 standaardafwijkingen. Buiten twee "
                  "standaardafwijkingen ligt maar 5 procent, verdeeld over twee kanten. Dus ja, "
                  "uitzonderlijk hoog.", 4),
             ]),
        dict(kop="Oppervlakte is kans",
             opdracht="Antwoord en leg uit waar nodig.",
             oefeningen=[
                 ("kort", "Hoe groot is de kans dat een waarde onder het gemiddelde ligt?", "0,5", W),
                 ("kort", "Een normale verdeling heeft gemiddelde 100. Wat is de kans op een waarde groter "
                          "dan 100?", "0,5", W),
                 ("open", "Waarom kan je de kans op precies één waarde niet als oppervlakte berekenen?",
                  "Eén punt heeft geen breedte, dus geen oppervlakte. Je werkt altijd met een interval.", 2),
                 ("open", "Een fabrikant wil weten hoeveel procent van zijn zakken onder 490 gram zit. "
                          "Beschrijf wat hij berekent en waarmee.",
                  "De oppervlakte onder de kromme links van 490. Dat gaat niet met de hand; daarvoor gebruikt "
                  "hij de rekenapps, die op het examen uitdrukkelijk toegelaten zijn.", 3),
                 ("waar", "Een normale verdeling heeft een begin en een einde: buiten een bepaald bereik is de "
                          "kans precies nul.", False),
             ]),
        dict(kop="Past het model?",
             opdracht="Beslis of een normale verdeling past, en schrijf waarom.",
             oefeningen=[
                 ("open", "Een histogram van de lengte van 500 volwassen mannen is mooi klokvormig.",
                  "Past. Klokvormig en symmetrisch rond één top is precies wat het model beschrijft.", 2),
                 ("open", "Een histogram van de inkomens in een land heeft een lange staart naar rechts.",
                  "Past niet. Het model is symmetrisch; dit is scheef verdeeld.", 2),
                 ("open", "Een histogram van wachttijden heeft veel heel korte wachttijden en een lange staart "
                          "naar rechts.",
                  "Past niet, om dezelfde reden: scheef in plaats van symmetrisch.", 2),
                 ("open", "Je hebt een reeks metingen en wil nakijken of het model past. Welke twee stappen zet "
                          "je, en welke twee getallen gebruik je?",
                  "Je tekent het histogram en kijkt of het klokvormig is, en je tekent de dichtheidsfunctie "
                  "erover. Als schatting gebruik je het gemiddelde en de standaardafwijking van je gegevens; "
                  "het steekproefgemiddelde geldt als schatting voor het populatiegemiddelde.", 5),
             ]),
    ],
)
