# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde op 🌍 Beyond dubbele finaliteit.

Gebaseerd op de vakfiche wiskunde van de 3de graad dubbele finaliteit, geldig
vanaf 1 januari 2027. Die fiche noemt bovenaan zelf twee toepassingen:
commerciële organisatie en de basisvorming dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De twaalf thema's volgen de weging van het examen zelf: zeven over analyse en
vijf over kansrekenen en statistiek, want die twee onderdelen wegen 60 en 40
procent. Het probleemoplossend denken staat vooraan: het weegt niet apart mee,
maar de stappen die het aanleert komen daarna in elk ander thema terug.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py
../../beyond-dubbele-finaliteit/wiskunde.json` doet daar het voorwerk voor;
het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-dubbele-finaliteit", de volle
categorieslug, zodat dekking.py de bundel bij het hoofdstuk vindt. Wiskunde
bestaat ook op 🌱 Start, ✨ Spark, 🚀 Boost en 🌍 Beyond doorstroom, en daar
klinken sommige thematitels bijna gelijk.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Wiskunde"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Problemen oplossen
BUNDELS["problemen-oplossen-van-situatie-naar-wiskunde-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Problemen oplossen: van situatie naar wiskunde",
    onder="De vier stappen, de strategieën die je onderweg kan gebruiken, en wat je op het examen in handen hebt.",
    secties=[
        dict(kop="De vier stappen", blokken=[
            ("p", "Elke opgave pak je in dezelfde volgorde aan. <strong>De eerste van de vier stappen is: "
                  "begrijp het probleem.</strong> Pas als je weet wat gevraagd wordt en wat je gegeven hebt, "
                  "heeft de rest zin. <strong>De tweede stap, meteen na het begrijpen, is een plan maken.</strong> "
                  "Daarna voer je het plan uit. <strong>De laatste van de vier stappen is reflecteren</strong>: "
                  "je kijkt terug en vraagt je af of je antwoord klopt en of dit een handige weg was."),
            ("fig", tabel(["Stap", "Wat je doet"], [
                ["1. Begrijp het probleem", "onderstreep wat gegeven is en wat gevraagd wordt"],
                ["2. Maak een plan", "kies een strategie, voer eventueel een variabele in"],
                ["3. Voer het plan uit", "reken, en schrijf je tussenstappen op"],
                ["4. Reflecteer", "controleer de uitkomst en vertaal ze terug naar de vraag"],
            ]), "De vier stappen, van lezen tot nakijken."),
            ("kader", "<strong>Wat doe je het eerst als je een lange opgave leest en meteen vastloopt?</strong> "
                      "Onderstrepen wat gegeven is en wat gevraagd wordt. Wie niet weet wat er gevraagd wordt, "
                      "kan geen plan maken."),
        ]),
        dict(kop="Mathematiseren en demathematiseren", blokken=[
            ("p", "<strong>Het omzetten van een concrete situatie naar wiskundetaal en wiskundige symbolen heet "
                  "mathematiseren.</strong> De omgekeerde weg, <strong>het terugvertalen van een wiskundige "
                  "uitkomst naar de situatie waar de opgave over ging, heet demathematiseren</strong>. "
                  "<strong>Demathematiseren betekent dus dat je je uitkomst terugvertaalt naar de situatie van "
                  "de opgave.</strong>"),
            ("p", "Een kaal getal is nog geen antwoord. <strong>Is je uitkomst 7,5 en was de vraag hoeveel bussen "
                  "er nodig zijn, dan antwoord je 8 bussen</strong>: een halve bus bestaat niet, en met zeven "
                  "bussen raakt niet iedereen mee."),
            ("weetje", "Een opgave vraagt hoeveel liter verf je nodig hebt voor een muur. "
                       "<strong>De context is dan de muur die je wil schilderen</strong>: de situatie uit de "
                       "werkelijkheid waar de opgave van vertrekt."),
        ]),
        dict(kop="Vraagstuk of probleem, met of zonder context", blokken=[
            ("p", "<strong>Een opgave die je kan oplossen met de leerstof van één hoofdstuk, heet een "
                  "vraagstuk.</strong> <strong>Een opgave die je niet aan één hoofdstuk kan koppelen en waarvoor "
                  "je leerstof moet combineren, heet een probleem.</strong> Bij een probleem kies je zelf de "
                  "strategie."),
            ("p", "Daarnaast kan een opgave met of zonder context zijn. <strong>Een opgave zonder context is "
                  "abstract en zuiver wiskundig</strong>; een opgave met context vertrekt van een situatie uit de "
                  "wereld rondom je. <strong>Een opgave met context is niet altijd moeilijker dan een opgave "
                  "zonder context</strong>: het verschil zit in de verpakking. En <strong>ook een opgave zonder "
                  "context kan een probleem zijn</strong>, want ook een zuiver wiskundige opgave kan leerstof uit "
                  "verschillende hoofdstukken combineren."),
        ]),
        dict(kop="Strategieën die vaak helpen", blokken=[
            ("p", "<strong>Een oplossingsstrategie zoals een schets maken of terugrekenen, heet een "
                  "heuristiek.</strong> <strong>Een heuristiek is geen stappenplan dat bij elk probleem altijd "
                  "tot de oplossing leidt</strong>: het is een aanpak die vaak helpt, en soms moet je een andere "
                  "proberen. <strong>Een schets maken is een van de strategieën die je bij een vraagstuk mag "
                  "gebruiken.</strong>"),
            ("fig", tabel(["Strategie", "Wanneer ze helpt"], [
                ["terugrekenen", "je weet wat er overblijft en zoekt het begin"],
                ["de gegevens in een tabel ordenen", "er staan veel getallen door elkaar"],
                ["een variabele invoeren", "je kent een waarde nog niet en noemt ze x"],
                ["slim gissen en testen", "je probeert, kijkt of het klopt en past aan"],
                ["alle mogelijkheden opschrijven", "er zijn er weinig"],
                ["speciale gevallen gebruiken", "je test een formule met x = 0 en x = 1"],
                ["simuleren", "je voert het vraagstuk zelf een aantal keer uit"],
                ["symmetrie gebruiken", "de figuur is links en rechts hetzelfde"],
                ["opsplitsen in deelproblemen", "de opgave is te groot in één keer"],
            ]), "De strategieën die de leerstof opsomt, en waar ze van pas komen."),
            ("p", "Enkele daarvan verdienen een woord extra. <strong>Slim gissen is geen blind gokken</strong>: je "
                  "gebruikt elke mislukte poging om je volgende schatting te verbeteren. <strong>Alle "
                  "mogelijkheden opschrijven is een goede strategie als er weinig mogelijkheden zijn</strong>; bij "
                  "een groot aantal zoek je beter naar een regel. <strong>Met symmetrie hoef je maar de helft uit "
                  "te rekenen.</strong> <strong>Een variabele is het getal of de letter die in een opgave een nog "
                  "onbekende waarde voorstelt</strong>, en de kleinere stukken waarin je een moeilijke opgave "
                  "splitst, heten <strong>deelproblemen</strong>. Elk deelprobleem is op zich haalbaar; samen geven ze het antwoord op het geheel."),
            ("p", "Soms zie je in een reeks getallen iets terugkeren. <strong>Een reeks zoals 3, 6, 9, 12 heeft "
                  "een patroon</strong>: er komt telkens drie bij. Wie het patroon ziet, hoeft niet elke stap "
                  "apart te berekenen. En <strong>een tabel met de winst per aantal stuks maak je het snelst "
                  "leesbaar als grafiek</strong>: dat is de voorstelling die het verloop het snelst zichtbaar maakt, want "
                  "ze toont in één oogopslag of iets stijgt, daalt of een top bereikt."),
        ]),
        dict(kop="Reflecteren: klopt je antwoord?", blokken=[
            ("p", "<strong>De stap waarin je achteraf nagaat of je antwoord klopt en of je aanpak handig was, "
                  "heet reflecteren.</strong> Die reflectie hoort bij het oplossen zelf: een antwoord dat je niet gecontroleerd hebt, is nog geen antwoord. "
                  "<strong>Bereken je dat een auto 540 kilometer per uur rijdt, dan ga je je berekening na, want "
                  "dat kan niet.</strong> Een onmogelijke waarde wijst op een rekenfout."),
        ]),
        dict(kop="ICT en nauwkeurigheid op het examen", blokken=[
            ("p", "<strong>Op het examen mag je ICT gebruiken om een grafiek te tekenen</strong>, om bewerkingen "
                  "uit te voeren en om statistische kengetallen te berekenen. <strong>Met de rekenapps bereken je "
                  "tijdens het examen de statistische kengetallen</strong>; ze staan via een link in het examen "
                  "zelf, en het loont om er thuis al mee te oefenen. <strong>Een gsm mag je niet gebruiken om te "
                  "rekenen</strong>: een gsm of smartwatch in de examenruimte geldt als fraude."),
            ("p", "<strong>Bij een berekening in meerdere stappen rond je een tussenresultaat niet af op één "
                  "cijfer.</strong> Je werkt met zo nauwkeurig mogelijke tussenresultaten en rondt pas op het "
                  "einde af, precies zo nauwkeurig als gevraagd. <strong>Is je uitkomst 0,333333… en vraagt de "
                  "opgave twee cijfers na de komma, dan noteer je 0,33.</strong>"),
            ("kader", "Praktisch. <strong>Bij het examen krijg je kladpapier en een balpen</strong>, en je mag "
                      "naar een geodriehoek, een passer of een meetlat vragen. <strong>Het examen wiskunde duurt "
                      "150 minuten</strong> en je legt het af in het examencentrum in Brussel, op de computer, "
                      "met gesloten vragen. <strong>Er is geen giscorrectie</strong>, dus een vraag onbeantwoord "
                      "laten levert zeker niets op. <strong>Veertig procent van het examen gaat over kansrekenen "
                      "en statistiek</strong>; de andere zestig procent gaat over analyse."),
        ]),
    ],
    onthoud=[
        "Begrijp het probleem, maak een plan, voer het plan uit, reflecteer.",
        "Mathematiseren is naar wiskunde vertalen, demathematiseren is terug naar de situatie.",
        "Een vraagstuk hoort bij één hoofdstuk, een probleem combineert leerstof.",
        "Een heuristiek helpt vaak, maar werkt niet altijd.",
        "Rond pas op het einde af, en zo nauwkeurig als gevraagd.",
        "Geen giscorrectie: laat geen enkele vraag open.",
    ],
)

# ───────────────────────── 2. Machtswortels en machten met rationale exponent
BUNDELS["machtswortels-en-machten-met-rationale-exponent-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Machtswortels en machten met rationale exponent",
    onder="Een wortel als macht schrijven, en daarna gewoon de rekenregels gebruiken.",
    secties=[
        dict(kop="Een wortel is een macht", blokken=[
            ("p", "<strong>De vierkantswortel uit 9 betekent hetzelfde als 9 tot de macht 1/2.</strong> Een wortel "
                  "schrijf je als een macht met een breuk als exponent, en de noemer van die breuk is de "
                  "wortelexponent. Zo is <strong>9 tot de macht 1/2 gelijk aan 3</strong>, want 3 maal 3 is 9, en "
                  "<strong>8 tot de macht 1/3 gelijk aan 2</strong>, want dat is de derdemachtswortel uit 8: het "
                  "getal dat je drie keer met zichzelf vermenigvuldigt om 8 te krijgen."),
            ("p", "Staat er ook nog een macht onder de wortel, dan komt die in de teller. <strong>De "
                  "derdemachtswortel uit 5 tot de macht 2 schrijf je als 5 tot de macht 2/3.</strong> De teller is "
                  "de macht onder de wortel, de noemer is de wortelexponent. Zo is <strong>16 tot de macht 3/4 "
                  "gelijk aan 8</strong>: de vierdemachtswortel uit 16 is 2, en 2 tot de macht 3 is 8. En "
                  "<strong>de vierkantswortel uit a tot de macht 5 schrijf je als a tot de macht 5/2</strong>."),
            ("p", "<strong>Elke n-de machtswortel kan je zo schrijven als een macht met een rationale "
                  "exponent</strong>, en dat is precies waarom het handig is: daarna kan je met de gewone "
                  "rekenregels verder."),
            ("fig", tabel(["Wortelvorm", "Als macht", "Uitkomst"], [
                ["wortel uit 9", "9 tot de macht 1/2", "3"],
                ["wortel uit 25", "25 tot de macht 1/2", "5"],
                ["wortel uit 100", "100 tot de macht 1/2", "10"],
                ["derdemachtswortel uit 8", "8 tot de macht 1/3", "2"],
                ["derdemachtswortel uit 27, in het kwadraat", "27 tot de macht 2/3", "9"],
                ["vierdemachtswortel uit 81", "81 tot de macht 1/4", "3"],
                ["vijfdemachtswortel uit 32", "32 tot de macht 1/5", "2"],
                ["wortel uit 4, tot de macht 3", "4 tot de macht 3/2", "8"],
            ]), "Dezelfde bewerking, twee schrijfwijzen."),
            ("weetje", "<strong>16 tot de macht 1/2 en de vierkantswortel uit 16 geven hetzelfde getal</strong>, "
                       "namelijk 4. Het zijn twee schrijfwijzen voor dezelfde bewerking."),
        ]),
        dict(kop="De rekenregels voor machten", blokken=[
            ("fig", tabel(["Regel", "Voorbeeld"], [
                ["zelfde grondtal, vermenigvuldigen: exponenten optellen", "2 tot de macht 3 maal 2 tot de macht 4 is 2 tot de macht 7"],
                ["zelfde grondtal, delen: exponenten aftrekken", "5 tot de macht 7 gedeeld door 5 tot de macht 4 is 5 tot de macht 3"],
                ["macht van een macht: exponenten vermenigvuldigen", "(3 tot de macht 2) tot de macht 5 is 3 tot de macht 10"],
                ["macht van een product: over beide factoren", "(2 maal 5) tot de macht 3 is 2 tot de macht 3 maal 5 tot de macht 3"],
                ["exponent nul", "7 tot de macht 0 is 1"],
                ["negatieve exponent", "2 tot de macht -3 is 1 gedeeld door 2 tot de macht 3, dus 0,125"],
            ]), "De regels die je overal nodig hebt."),
            ("p", "<strong>De rekenregels voor machten gelden ook als de exponent een breuk is.</strong> Daarom "
                  "schrijf je een wortel eerst als macht. Zo is <strong>3 tot de macht 1/2 maal 3 tot de macht 1/2 "
                  "gelijk aan 3</strong> (een half plus een half is één), <strong>a tot de macht 1/2 gedeeld door "
                  "a tot de macht 1/4 gelijk aan a tot de macht 1/4</strong>, en <strong>6 tot de macht 1/2 maal 6 "
                  "tot de macht 3/2 gelijk aan 36</strong>."),
            ("kader", "Twee valkuilen. <strong>Een macht met exponent nul is niet nul maar 1</strong>, zolang het "
                      "grondtal zelf niet nul is. Zo is 2 tot de macht -3 gelijk aan 1 gedeeld door 8, als decimaal getal 0,125. En <strong>een negatieve exponent maakt de uitkomst niet "
                      "negatief maar omgekeerd</strong>: 10 tot de macht -2 is 0,01, niet min 100."),
            ("p", "Twee regels die níét bestaan. <strong>Een macht van een som mag je niet over de twee termen "
                  "verdelen</strong>: (2 + 3) in het kwadraat is 25, terwijl 4 plus 9 maar 13 geeft. En "
                  "<strong>exponenten optellen mag alleen bij hetzelfde grondtal, niet als de grondtallen verschillen</strong>: 2 tot de macht 3 maal "
                  "5 tot de macht 3 geef je anders weer, namelijk als 10 tot de macht 3."),
        ]),
        dict(kop="Wat mag onder de wortel?", blokken=[
            ("p", "<strong>De vierkantswortel uit een negatief getal bestaat niet binnen de reële getallen</strong>, "
                  "want geen enkel reëel getal geeft in het kwadraat iets negatiefs. Bij een oneven wortelexponent "
                  "mag het wel: <strong>de derdemachtswortel uit min 27 is min 3</strong>, want min 3 maal min 3 "
                  "maal min 3 geeft min 27."),
            ("p", "<strong>De wortel uit 2 kan je niet als breuk van twee gehele getallen schrijven.</strong> Het "
                  "is een irrationaal getal: de decimalen stoppen niet en herhalen zich niet."),
        ]),
        dict(kop="Schatten en afronden", blokken=[
            ("p", "Je kan een wortel vaak al inklemmen zonder toestel. <strong>De wortel uit 50 ligt tussen 7 en "
                  "8</strong>, want 7 in het kwadraat is 49 en 8 in het kwadraat is 64. <strong>De "
                  "derdemachtswortel uit 100 ligt tussen 4 en 5</strong>, want 4 tot de macht 3 is 64 en 5 tot de "
                  "macht 3 is 125."),
            ("p", "Daarna reken je nauwkeurig verder. <strong>Geeft je rekentoestel 2,2360679… als wortel uit 5 en "
                  "worden er twee cijfers na de komma gevraagd, dan noteer je 2,24</strong>, want het derde cijfer "
                  "is een 6. <strong>De wortel uit 10 afgerond op één cijfer na de komma is 3,2.</strong> En "
                  "<strong>je mag een tussenresultaat niet zomaar afronden voor je verder rekent</strong>: elke "
                  "afronding onderweg maakt de afwijking groter."),
        ]),
        dict(kop="Waar je het tegenkomt", blokken=[
            ("p", "<strong>Een kubus met een inhoud van 64 kubieke centimeter heeft een ribbe van 4 "
                  "centimeter</strong>: de ribbe is de derdemachtswortel uit de inhoud. <strong>Een vierkant perk "
                  "met een oppervlakte van 169 vierkante meter heeft een zijde van 13 meter</strong>: de zijde is "
                  "de vierkantswortel uit de oppervlakte."),
        ]),
    ],
    onthoud=[
        "Een wortel is een macht met een breuk als exponent; de wortelexponent is de noemer.",
        "Zelfde grondtal: optellen bij vermenigvuldigen, aftrekken bij delen.",
        "Exponent nul geeft 1, een negatieve exponent geeft het omgekeerde.",
        "Een macht van een som verdelen mag niet.",
        "Rond pas op het einde af.",
    ],
)

# ───────────────────────── 3. Logaritmen
BUNDELS["logaritmen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Logaritmen",
    onder="De exponent terugvinden, en waarom schalen zoals die van Richter met logaritmen werken.",
    secties=[
        dict(kop="Wat een logaritme vraagt", blokken=[
            ("p", "<strong>Als je de logaritme van een getal berekent, vraag je tot welke macht je het grondtal "
                  "moet verheffen.</strong> Een logaritme is dus de omgekeerde bewerking van machtsverheffen: ze "
                  "geeft de exponent terug. <strong>Machtsverheffen en een logaritme nemen zijn elkaars omgekeerde "
                  "bewerking</strong>: bij een macht ken je de exponent en zoek je de uitkomst, bij een logaritme "
                  "ken je de uitkomst en zoek je de exponent."),
            ("p", "<strong>De uitspraak dat de logaritme van 16 met grondtal 2 gelijk is aan 4, zegt hetzelfde als "
                  "2 tot de macht 4 is 16.</strong> <strong>Schrijf je log zonder grondtal erbij, dan bedoel je de "
                  "logaritme met grondtal 10.</strong> Bij een ander grondtal schrijf je dat grondtal er klein bij."),
            ("fig", tabel(["Logaritme", "Omdat", "Uitkomst"], [
                ["log van 100, grondtal 10", "10 tot de macht 2 is 100", "2"],
                ["log van 1000, grondtal 10", "10 tot de macht 3 is 1000", "3"],
                ["log van 10000, grondtal 10", "10 tot de macht 4 is 10000", "4"],
                ["log van 1 miljoen, grondtal 10", "een 1 met zes nullen", "6"],
                ["log van 0,1, grondtal 10", "10 tot de macht -1 is een tiende", "-1"],
                ["log van 0,01, grondtal 10", "10 tot de macht -2 is 0,01", "-2"],
                ["log van 8, grondtal 2", "2 tot de macht 3 is 8", "3"],
                ["log van 1024, grondtal 2", "2 tot de macht 10 is 1024", "10"],
                ["log van 81, grondtal 3", "3 tot de macht 4 is 81", "4"],
                ["log van 125, grondtal 5", "5 tot de macht 3 is 125", "3"],
                ["log van 64, grondtal 4", "4 tot de macht 3 is 64", "3"],
            ]), "Logaritmen die je uit het hoofd kan."),
        ]),
        dict(kop="Wat kan en wat niet kan", blokken=[
            ("p", "<strong>De logaritme van 1 is bij elk grondtal nul</strong>, want elk grondtal tot de macht "
                  "nul geeft 1. <strong>De logaritme van 7 met grondtal 7 is 1</strong>, want je zoekt de exponent "
                  "waarmee 7 zichzelf geeft."),
            ("p", "<strong>De logaritme van 0 bestaat niet</strong>: je kan een positief grondtal tot geen enkele "
                  "macht verheffen om nul te krijgen, en <strong>het grondtal verandert daar niets aan, hoe groot "
                  "je het ook kiest</strong>. <strong>De logaritme van een negatief getal bestaat evenmin</strong>; "
                  "ze is dus zeker geen negatief getal."),
            ("p", "Wel geldt: <strong>hoe groter het getal, hoe groter zijn logaritme, bij een grondtal groter "
                  "dan 1</strong>, want om een groter getal te bereiken heb je een grotere exponent nodig. "
                  "<strong>Een logaritme met grondtal 10 van een getal groter dan 1 is altijd positief</strong>, "
                  "en <strong>de logaritme van een getal tussen 0 en 1 is negatief</strong>, want om onder de 1 "
                  "te komen heb je een negatieve exponent nodig."),
            ("kader", "<strong>De logaritme van 100 is niet bij elk grondtal gelijk aan 2.</strong> Bij grondtal "
                      "10 is ze 2, maar bij grondtal 2 ligt ze tussen 6 en 7. Het grondtal bepaalt de uitkomst mee."),
        ]),
        dict(kop="Inklemmen en benaderen", blokken=[
            ("p", "Zelfs zonder toestel weet je vaak al waar een logaritme ligt. <strong>De logaritme van 50 met "
                  "grondtal 10 ligt tussen 1 en 2</strong>, want 10 tot de macht 1 is 10 en 10 tot de macht 2 is "
                  "100. <strong>Los je 3 tot de macht x is 20 op, dan ligt x tussen 2 en 3</strong>, want 3 in het "
                  "kwadraat is 9 en 3 tot de macht 3 is 27."),
            ("p", "<strong>Een logaritme kan een getal met cijfers na de komma zijn</strong>; alleen bij mooie "
                  "machten van het grondtal krijg je een geheel getal. <strong>Geeft een rekentoestel 0,845098… "
                  "als logaritme van 7 met grondtal 10, dan betekent dat: 10 tot de macht 0,845 is ongeveer "
                  "7.</strong> Omgekeerd: <strong>geeft je toestel 2,69897, dan heeft het getal een paar honderd "
                  "als orde van grootte</strong>, want het gehele deel is 2. <strong>De logaritme van 300 met "
                  "grondtal 10 is ongeveer 2,48, dus 300 ligt tussen 10 tot de macht 2 en 10 tot de macht 3.</strong>"),
            ("p", "<strong>Een logaritme met grondtal 2 kan je ook berekenen met een toestel dat alleen grondtal "
                  "10 kent</strong>: je deelt de logaritme van het getal door de logaritme van 2, allebei met "
                  "grondtal 10."),
        ]),
        dict(kop="Waarvoor je ze gebruikt", blokken=[
            ("p", "Een logaritme haalt de onbekende uit de exponent. <strong>De vergelijking 2 tot de macht x is "
                  "32 los je op met een logaritme</strong>, en <strong>het antwoord is x is 5</strong>. Zo ook: "
                  "<strong>10 tot de macht x is 10000 geeft x is 4</strong>."),
            ("p", "Daarom komt een logaritme terug bij groei. <strong>Groeit een bedrag met 5 procent per jaar, "
                  "dan heb je een logaritme nodig om te berekenen na hoeveel jaar het verdubbeld is</strong>, want "
                  "het aantal jaren staat in de exponent. <strong>De tijd waarna een exponentieel groeiend aantal "
                  "twee keer zo groot is, heet de verdubbelingstijd</strong>; bij afname heet de tegenhanger de "
                  "halveringstijd. <strong>Vervalt een stof elk jaar tot de helft, dan is er na 3 jaar nog een "
                  "achtste over.</strong>"),
        ]),
        dict(kop="Logaritmische schalen", blokken=[
            ("p", "<strong>Een getal tien keer zo groot maken verhoogt zijn logaritme met grondtal 10 met "
                  "1.</strong> Daarom werken de decibelschaal en de schaal van Richter met logaritmen: elke stap "
                  "is een factor tien. <strong>Men gebruikt zo'n schaal voor aardbevingen omdat de krachten "
                  "enorm uit elkaar liggen</strong>; met een logaritme breng je waarden die duizenden keren "
                  "verschillen terug tot een handzame schaal."),
            ("p", "<strong>Een beving van 6 op de schaal van Richter is dan 100 keer sterker dan een van "
                  "4</strong>: twee stappen, dus tien maal tien. Hetzelfde idee zit in het voorbeeld hierboven: "
                  "<strong>is de logaritme van 2 ongeveer 0,30, dan is die van 20 ongeveer 1,30</strong>, want "
                  "één factor 10 erbij verhoogt de logaritme met precies 1."),
        ]),
    ],
    onthoud=[
        "Een logaritme is de exponent die je zoekt.",
        "log zonder grondtal betekent grondtal 10.",
        "De logaritme van 0 en van een negatief getal bestaat niet.",
        "De logaritme van 1 is nul, bij elk grondtal.",
        "Tien keer zo groot betekent 1 erbij op een logaritmische schaal.",
    ],
)

# ───────────────────────── 4. Een functie aflezen van haar grafiek
BUNDELS["een-functie-aflezen-van-haar-grafiek-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Een functie aflezen van haar grafiek",
    onder="Domein, bereik, nulwaarden, tekenverloop, verloopschema en wat ze betekenen in de situatie erachter.",
    secties=[
        dict(kop="Vier manieren om dezelfde functie te tonen", blokken=[
            ("p", "<strong>Verwoording, tabel, grafiek en voorschrift horen bij elkaar</strong>: dezelfde functie "
                  "kan je in woorden zeggen, in een tabel zetten, tekenen of als formule schrijven. "
                  "<strong>Een functievoorschrift en een tabel van dezelfde functie kunnen elkaar niet "
                  "tegenspreken</strong>; doen ze dat toch, dan zit er een fout in een van beide."),
            ("p", "<strong>Heb je een tabel en wil je er een grafiek van maken, dan zet je de koppels als punten "
                  "uit en verbindt ze: elk koppel uitzetten en verbinden geeft het verloop.</strong> <strong>De twee getallen tussen haakjes die de plaats van een punt "
                  "aangeven, heten de coördinaten</strong>: het eerste is de x-waarde, het tweede de "
                  "functiewaarde. <strong>Een grafiek schetsen zonder ICT betekent niet dat ze helemaal op schaal "
                  "moet zijn</strong>: bij een schets gaat het om de vorm. Nauwkeurig tekenen doe je met ICT, en "
                  "<strong>dat mag op het examen</strong>."),
        ]),
        dict(kop="Domein en bereik", blokken=[
            ("p", "<strong>Het domein is de verzameling van alle x-waarden waarvoor een functie bestaat</strong>, "
                  "en je schrijft het als dom f. <strong>Het bereik is de verzameling van alle functiewaarden die "
                  "een functie aanneemt</strong>, geschreven als ber f. <strong>Het bereik lees je af op de "
                  "verticale as</strong>, het domein op de horizontale."),
            ("p", "<strong>Loopt een grafiek van x is 1 tot x is 10 en nergens anders, dan is het domein alle "
                  "getallen van 1 tot en met 10.</strong> <strong>Schommelt de temperatuur in een koelkast elke "
                  "twintig minuten tussen 3 en 6 graden, dan is het bereik van 3 tot 6 graden</strong>; twintig "
                  "minuten is de periode. <strong>Twee functies met hetzelfde bereik kunnen een heel verschillende "
                  "grafiek hebben</strong>, want het bereik zegt alleen welke waarden voorkomen."),
            ("p", "<strong>Het stuk van het domein dat in de gegeven situatie zinvol is, heet het praktisch "
                  "domein.</strong> <strong>Het kan kleiner zijn dan het wiskundige domein</strong>: wiskundig mag "
                  "x negatief zijn, maar als x het aantal verkochte stuks is, begint het praktisch domein bij nul. "
                  "Er bestaat ook een praktisch bereik, op dezelfde manier."),
        ]),
        dict(kop="Nulwaarden, nulpunten en snijpunten", blokken=[
            ("p", "<strong>Een nulwaarde is de x-waarde van een snijpunt met de x-as</strong>; <strong>een "
                  "nulpunt is de coördinaat van dat snijpunt</strong>. De nulwaarde is dus één getal, het nulpunt "
                  "is het hele koppel: (3, 0) is een nulpunt, 3 is de nulwaarde."),
            ("p", "<strong>Een functie kan meerdere nulwaarden hebben</strong>, want de grafiek mag de x-as zo "
                  "vaak snijden als ze wil. <strong>Ligt een grafiek tussen x is 0 en x is 8 boven de x-as en "
                  "daarbuiten eronder, dan zijn de nulwaarden 0 en 8.</strong> <strong>Twee snijpunten met de "
                  "y-as kan niet</strong>: bij één x-waarde hoort hoogstens één functiewaarde. <strong>Een functie "
                  "heeft dus precies één snijpunt met de y-as, of geen</strong> als nul buiten het domein valt. "
                  "<strong>Snijdt een grafiek de y-as in (0, 5), dan is de functiewaarde bij x is 0 gelijk aan "
                  "5.</strong>"),
        ]),
        dict(kop="Tekenverloop en verloopschema", blokken=[
            ("p", "<strong>Het overzicht dat weergeeft waar een grafiek boven en waar ze onder de x-as ligt, heet "
                  "het tekenverloop.</strong> <strong>Een plusteken in het tekenverloop betekent dat de grafiek "
                  "daar boven de x-as ligt</strong>, een min dat ze eronder ligt en een nul dat ze de as snijdt. "
                  "<strong>Een verticale streep betekent dat de functie daar niet gedefinieerd is</strong>; voor "
                  "een heel interval gebruik je drie schuine strepen."),
            ("p", "<strong>Het overzicht dat weergeeft waar een functie stijgt, waar ze daalt en waar ze een top "
                  "bereikt, heet het verloopschema.</strong> Daarin staan min en max. <strong>Staat er min op x is "
                  "3, dan bereikt de functie daar een minimum</strong> — pas op, een min in het tekenverloop "
                  "betekent iets anders, namelijk onder de x-as."),
            ("fig", tabel(["Symbool", "In het tekenverloop", "In het verloopschema"], [
                ["+", "de grafiek ligt boven de x-as", "—"],
                ["−", "de grafiek ligt onder de x-as", "—"],
                ["0", "de grafiek snijdt de x-as", "—"],
                ["|", "de functie is daar niet gedefinieerd", "—"],
                ["///", "de functie bestaat op dat interval niet", "—"],
                ["min", "—", "de functie bereikt een minimum"],
                ["max", "—", "de functie bereikt een maximum"],
            ]), "Dezelfde tekens, twee verschillende schema's."),
        ]),
        dict(kop="Stijgen, dalen en toppen", blokken=[
            ("p", "<strong>Een functie die daalt, heeft niet overal negatieve functiewaarden</strong>: dalen zegt "
                  "iets over de richting, niet over het teken. Een grafiek kan van 10 naar 2 zakken en de hele "
                  "tijd boven de x-as blijven. <strong>Een constante functie stijgt noch daalt</strong>: haar "
                  "grafiek is een horizontale rechte."),
            ("p", "<strong>Loopt een grafiek eerst omhoog, bereikt ze een top en gaat ze dan omlaag, dan is die "
                  "top een maximum.</strong> <strong>Een maximum of een minimum heet met één woord een "
                  "extremum</strong>; het meervoud is extrema."),
            ("p", "Hoe een grafiek stijgt, zegt nog iets extra. <strong>Stijgt ze steeds steiler, dan heet dat een "
                  "toenemende stijging</strong>: niet alleen de waarde groeit, ook de snelheid waarmee ze groeit. "
                  "<strong>Een grafiek die stijgt met een afnemende stijging, gaat nog altijd omhoog</strong>, "
                  "alleen steeds trager. <strong>Daalt ze en wordt ze daarbij steeds minder steil, dan heet dat "
                  "een afnemende daling</strong>; vaak kruipt de grafiek dan naar een vaste waarde toe."),
            ("p", "Twee andere kenmerken komen erbij. <strong>Is de grafiek links en rechts van de y-as elkaars "
                  "spiegelbeeld, dan is de functie symmetrisch.</strong> <strong>Herhaalt een grafiek zich elke 24 "
                  "uur precies op dezelfde manier, dan heet die 24 uur de periode.</strong>"),
        ]),
        dict(kop="Wat het betekent in de situatie", blokken=[
            ("p", "Demathematiseren betekent dat je de wiskundige term vertaalt naar de situatie. <strong>Toont de "
                  "grafiek de winst in functie van het aantal geproduceerde stuks, dan is een nulwaarde het aantal "
                  "stuks waarbij de winst nul is</strong>: het break-evenpunt. <strong>Snijdt die winstgrafiek de "
                  "x-as bij 400 stuks, dan begint de winst vanaf 400 stuks</strong>; onder de x-as is er verlies."),
            ("p", "<strong>Stijgt de grafiek van de hartslag in functie van de tijd tussen minuut 2 en minuut 5, "
                  "dan gaat de hartslag in die minuten omhoog</strong> — stijgen slaat op de verandering, niet op "
                  "de hoogte. <strong>Bereikt de grafiek van het aantal bezoekers per uur om 15 uur haar hoogste "
                  "punt, dan ligt daar het maximum.</strong> En <strong>daalt de grafiek van de tijd die je nodig "
                  "hebt in functie van je snelheid, dan betekent sneller rijden minder tijd</strong>."),
        ]),
    ],
    onthoud=[
        "Domein op de horizontale as, bereik op de verticale.",
        "Nulwaarde is één getal, nulpunt is een koppel.",
        "Tekenverloop zegt boven of onder de x-as, verloopschema zegt stijgen of dalen.",
        "Hoogstens één snijpunt met de y-as, zoveel nulwaarden als je wil.",
        "Vertaal elk kenmerk terug naar de situatie van de opgave.",
    ],
)

# ───────────────────────── 5. Gemiddelde verandering en het differentiequotiënt
BUNDELS["gemiddelde-verandering-en-het-differentiequotient-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Gemiddelde verandering en het differentiequotiënt",
    onder="Hoe snel verandert iets gemiddeld, en wat je daaruit wel en niet mag besluiten.",
    secties=[
        dict(kop="Wat een differentiequotiënt berekent", blokken=[
            ("p", "<strong>Een differentiequotiënt berekent de gemiddelde verandering over een interval.</strong> "
                  "Je vergelijkt hoeveel de functiewaarde veranderde met hoeveel x veranderde. <strong>Het "
                  "differentiequotiënt van f over het interval van a tot b bereken je als f(b) min f(a), gedeeld "
                  "door b min a</strong>: bovenaan het verschil in functiewaarde, onderaan het verschil in x. "
                  "<strong>Teller en noemer omdraaien mag niet</strong>, want dan krijg je het omgekeerde getal."),
            ("fig", tabel(["Gegeven", "Berekening", "Differentiequotiënt"], [
                ["f(2) = 10 en f(6) = 30", "20 gedeeld door 4", "5"],
                ["f(0) = 8 en f(4) = 0", "min 8 gedeeld door 4", "−2"],
                ["f(1) = 4 en f(3) = 16", "12 gedeeld door 2", "6"],
                ["f(5) = 20 en f(9) = 20", "0 gedeeld door 4", "0"],
                ["bij x = 2 hoort 7, bij x = 10 hoort 31", "24 gedeeld door 8", "3"],
            ]), "Telkens: verschil in functiewaarde, gedeeld door verschil in x."),
            ("p", "<strong>Een negatief differentiequotiënt betekent dat de functie gemiddeld daalt over dat "
                  "interval.</strong> Het teken zegt iets over de richting, niet over de ligging van de grafiek. "
                  "<strong>Bij een stijgende functie is het differentiequotiënt over elk interval positief.</strong>"),
            ("kader", "Een gemiddelde verbergt wat er onderweg gebeurde. <strong>Een differentiequotiënt van nul "
                      "betekent dat de functie op het einde van het interval even hoog zit als bij het "
                      "begin</strong>; daartussen kan ze gestegen en weer gedaald zijn. Daarom <strong>vertelt het "
                      "differentiequotiënt je niet wat er op elk moment binnen het interval gebeurt</strong>. Een "
                      "auto met een gemiddelde van 50 kilometer per uur heeft misschien stilgestaan en daarna 100 "
                      "gereden, en <strong>een gemiddelde snelheid van 0 betekent niet dat je niet bewogen "
                      "hebt</strong>, alleen dat je weer op je vertrekpunt staat. <strong>Men zegt gemiddelde "
                      "verandering omdat ze over een heel interval uitgesmeerd is.</strong>"),
        ]),
        dict(kop="Wat je ervan ziet in de grafiek", blokken=[
            ("p", "<strong>De grafische betekenis van het differentiequotiënt over een interval is de "
                  "richtingscoëfficiënt van de rechte door de twee randpunten.</strong> Je trekt een rechte door "
                  "het beginpunt en het eindpunt; de steilheid van die rechte is het differentiequotiënt. "
                  "<strong>Zo'n rechte raakt de grafiek niet aan</strong>, ze snijdt haar in die twee punten."),
            ("p", "<strong>Het getal dat zegt hoe steil een rechte loopt, heet de "
                  "richtingscoëfficiënt.</strong> <strong>Een rechte door (1, 2) en (5, 10) heeft "
                  "richtingscoëfficiënt 2.</strong> <strong>Bij een rechte is het differentiequotiënt over elk "
                  "interval hetzelfde</strong>, want een rechte heeft overal dezelfde helling. Zo geeft "
                  "<strong>f(x) is 3x plus 1 over het interval van 0 tot 5 het differentiequotiënt 3</strong>, en "
                  "<strong>f(x) is 2x min 5 over eender welk interval 2</strong>: bij een eerstegraadsfunctie is "
                  "het getal voor de x de richtingscoëfficiënt."),
            ("p", "<strong>Bij een kromme hangt het differentiequotiënt wél af van welk interval je kiest.</strong> "
                  "Neem f(x) is x in het kwadraat: <strong>over het interval van 1 tot 3 is het "
                  "differentiequotiënt 4</strong>, en <strong>over het interval van 3 tot 5 is het 8</strong>. "
                  "Verderop groeit dezelfde functie dus sneller. Daarom zeg je er bij een kromme altijd bij over "
                  "welk interval je rekende."),
            ("p", "Vergelijken kan op twee manieren. <strong>Geven twee intervallen de differentiequotiënten 3 en "
                  "7, dan groeit de functie sneller in het tweede interval</strong>: een groter "
                  "differentiequotiënt betekent een steilere rechte. <strong>Van twee grafieken over hetzelfde "
                  "interval heeft de steilste het grootste differentiequotiënt.</strong> Je kan dus <strong>twee "
                  "differentiequotiënten vergelijken door naar de steilheid van hun rechten te kijken</strong>, of "
                  "gewoon door de twee getallen naast elkaar te leggen. <strong>Is het differentiequotiënt 2 in de "
                  "eerste helft van een interval en 8 in de tweede, dan wordt de grafiek steiler</strong>: een "
                  "toenemende stijging."),
            ("p", "<strong>Een groter differentiequotiënt betekent niet altijd een hogere functiewaarde.</strong> "
                  "Het zegt alleen iets over de verandering; een functie kan snel groeien en toch nog laag liggen."),
        ]),
        dict(kop="Waar het vandaan komt en waar het over gaat", blokken=[
            ("p", "<strong>Je kan een differentiequotiënt berekenen uit een tabel, uit een grafiek en uit een "
                  "voorschrift.</strong> Je hebt alleen twee functiewaarden nodig en de bijbehorende x-waarden."),
            ("p", "<strong>De eenheid van een differentiequotiënt is de eenheid van de functiewaarde per eenheid "
                  "van x.</strong> <strong>Bij het aantal inwoners in functie van het jaartal krijg je dus "
                  "inwoners per jaar</strong>, en verder euro per jaar, graden per uur of liter per minuut."),
            ("fig", tabel(["Situatie", "Berekening", "Betekenis"], [
                ["150 km in 2 uur", "150 gedeeld door 2", "75 kilometer per uur gemiddeld"],
                ["een bergweg klimt 120 m over 2000 m", "120 gedeeld door 2000", "6 procent gemiddelde helling"],
                ["een plant groeit van 12 naar 30 cm in 6 weken", "18 gedeeld door 6", "3 cm per week"],
                ["spaargeld van 1000 naar 1200 euro in 4 jaar", "200 gedeeld door 4", "50 euro per jaar"],
                ["de inhoud van een waterton gaat van 80 naar 20 liter in 10 minuten", "min 60 gedeeld door 10", "gemiddeld debiet 6 liter per minuut eruit"],
                ["500 klanten in januari, 2000 in mei", "1500 gedeeld door 4", "375 klanten per maand erbij"],
                ["van 20 naar 5 graden tussen 18 en 23 uur", "min 15 gedeeld door 5", "−3 graden per uur"],
            ]), "Hetzelfde rekenwerk, telkens met een andere naam in de praktijk."),
            ("p", "<strong>Verliest een tank gemiddeld 4 liter per minuut en bevat hij nu 100 liter, dan zit er na "
                  "15 minuten nog 40 liter in.</strong> Zo gebruik je een gemiddelde verandering ook om vooruit te "
                  "rekenen."),
        ]),
    ],
    onthoud=[
        "Differentiequotiënt: verschil in functiewaarde gedeeld door verschil in x.",
        "Het is de richtingscoëfficiënt van de rechte door de twee randpunten.",
        "Bij een rechte overal gelijk, bij een kromme afhankelijk van het interval.",
        "Het teken zegt stijgen of dalen, niet boven of onder de x-as.",
        "De eenheid is functiewaarde per eenheid van x.",
    ],
)

# ───────────────────────── 6. Exponentiële functies
BUNDELS["exponentiele-functies-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Exponentiële functies",
    onder="De x in de exponent: wat de groeifactor doet, wat de beginwaarde doet, en hoe de grafiek eruitziet.",
    secties=[
        dict(kop="Het voorschrift", blokken=[
            ("p", "<strong>Bij een exponentiële functie hoort het voorschrift f(x) is b maal a tot de macht "
                  "x.</strong> Het kenmerk is dat de x in de exponent staat; staat x in het grondtal, dan is het "
                  "een machtsfunctie. <strong>Het getal a heet de groeifactor</strong> en zegt met hoeveel je "
                  "vermenigvuldigt bij elke stap van één in x. <strong>Het getal b heet de beginwaarde</strong>, ook wel de startwaarde: "
                  "dat is de functiewaarde bij x is 0, want a tot de macht 0 is 1."),
            ("p", "<strong>Bij f(x) is 200 maal 1,05 tot de macht x is de functiewaarde bij x is 0 dus 200.</strong> "
                  "Zo ook: <strong>f(x) is 5 maal 2 tot de macht x geeft f(0) is 5</strong>. En met een exponent "
                  "erin: <strong>f(x) is 3 maal 2 tot de macht x geeft f(3) is 24</strong>, <strong>f(x) is 2 maal "
                  "3 tot de macht x geeft f(2) is 18</strong>, <strong>f(x) is 100 maal 0,5 tot de macht x geeft "
                  "f(2) is 25</strong> en <strong>f(x) is 2 tot de macht x geeft f(-2) is 0,25</strong>, want een "
                  "negatieve exponent keert de macht om."),
        ]),
        dict(kop="Wat de groeifactor doet", blokken=[
            ("p", "<strong>Bij een groeifactor groter dan 1 stijgt de exponentiële functie</strong>, want elke "
                  "stap vermenigvuldigt met meer dan één. <strong>Bij een groeifactor tussen 0 en 1 daalt "
                  "ze</strong>; <strong>0,8 is dus de groeifactor van een dalende exponentiële functie</strong>. "
                  "<strong>De groeifactor mag niet gelijk zijn aan 1</strong>, want dan blijft de functie "
                  "constant en heb je een rechte in plaats van een exponentiële functie. <strong>En de groeifactor "
                  "mag niet negatief zijn</strong>, want dan zou de grafiek springen tussen positieve en negatieve "
                  "waarden."),
            ("fig", tabel(["Groeifactor", "Beginwaarde", "De rij die erbij hoort", "Wat ze doet"], [
                ["3", "2", "2, 6, 18, 54", "stijgt snel"],
                ["2", "7", "7, 14, 28, 56", "verdubbelt telkens"],
                ["1,1", "100", "100, 110, 121, 133,1", "stijgt traag maar versnellend"],
                ["0,9", "50", "50, 45, 40,5, 36,45", "daalt met tien procent per stap"],
                ["0,5", "80", "80, 40, 20, 10", "halveert telkens"],
            ]), "De groeifactor vind je door een getal door het vorige te delen."),
            ("p", "<strong>Een rij als 4, 9, 14, 19 groeit lineair en niet exponentieel</strong>: daar komt telkens "
                  "5 bij. <strong>Bij een exponentiële functie hoort bij elke stap van één in x dezelfde "
                  "vermenigvuldiging</strong>, en dat is precies het verschil met lineaire groei. <strong>In een "
                  "tabel zie je dat snel door elk getal door het vorige te delen</strong>: komt er telkens "
                  "dezelfde factor uit, dan is het exponentieel."),
            ("p", "Twee voorbeelden van zo'n aflezing. <strong>Geeft een tabel bij x is 0 de waarde 6 en bij x is "
                  "1 de waarde 18, dan hoort daar f(x) is 6 maal 3 tot de macht x bij.</strong> <strong>Gaat een "
                  "grafiek door (0, 50) en (1, 45), dan is de groeifactor 0,9</strong>, dus er gaat elke stap tien "
                  "procent af. Omgekeerd: <strong>een groeifactor van 1,5 betekent dat er 50 procent per stap "
                  "bijkomt.</strong>"),
        ]),
        dict(kop="Hoe de grafiek loopt", blokken=[
            ("p", "<strong>Het domein van een exponentiële functie is alle reële getallen</strong>: je mag elke "
                  "exponent invullen, ook negatieve en gebroken. <strong>Het bereik van f(x) is 4 maal 2 tot de "
                  "macht x is alle positieve getallen</strong>: de functie wordt zo klein als je wil, maar blijft "
                  "positief, en ze groeit zonder bovengrens. <strong>De grafiek van een exponentiële functie met "
                  "positieve beginwaarde blijft helemaal boven de x-as</strong> en <strong>snijdt de x-as "
                  "nooit</strong>; er is dus geen nulwaarde."),
            ("p", "<strong>De grafiek van een stijgende exponentiële functie heeft een toenemende stijging</strong>: "
                  "ze wordt steeds steiler, want elke stap levert meer op dan de vorige. <strong>Een "
                  "exponentiële functie met groeifactor kleiner dan 1 heeft een afnemende daling</strong>: ze zakt "
                  "snel in het begin en daarna steeds trager. <strong>Wordt x heel groot bij zo'n dalende functie, "
                  "dan kruipt ze naar nul toe zonder die te bereiken.</strong> <strong>Zie je een grafiek die "
                  "traag begint en daarna steeds steiler omhoog schiet, dan past een exponentieel model</strong>: "
                  "een rechte wordt nooit steiler."),
        ]),
        dict(kop="Vergelijken en voorstellen", blokken=[
            ("p", "<strong>Hebben twee exponentiële functies dezelfde groeifactor maar beginwaarden 10 en 100, dan "
                  "ligt de tweede tien keer hoger.</strong> De beginwaarde rekt de grafiek verticaal uit; het "
                  "groeipercentage per stap blijft hetzelfde. <strong>Verdubbelt de beginwaarde en blijft de "
                  "groeifactor gelijk, dan verdubbelt elke functiewaarde.</strong>"),
            ("p", "<strong>Hebben twee exponentiële functies dezelfde beginwaarde maar groeifactoren 1,1 en 1,5, "
                  "dan stijgt die met 1,5 het snelst.</strong> Een grotere groeifactor betekent elke stap een "
                  "grotere vermenigvuldiging."),
            ("p", "<strong>Een exponentiële functie kan je net als elke andere in woorden en in een tabel "
                  "voorstellen</strong>, niet alleen als grafiek of voorschrift. En <strong>een exponentiële "
                  "grafiek met ICT tekenen en dan de kenmerken aflezen, mag</strong>: schetsen zonder ICT en "
                  "nauwkeurig tekenen met ICT horen allebei bij de leerstof."),
        ]),
        dict(kop="Waar je ze tegenkomt", blokken=[
            ("p", "<strong>Een bacteriekolonie die elk uur verdubbelt, past het best bij een exponentieel "
                  "model</strong>: verdubbelen is vermenigvuldigen. Een loon dat elk jaar 50 euro stijgt, is "
                  "lineair. <strong>Een rij als 100, 110, 121, 133,1 is exponentieel met factor 1,1</strong>."),
            ("p", "<strong>Op den duur groeit een exponentiële functie sneller dan elke lineaire functie.</strong> "
                  "In het begin kan de rechte vooroplopen, maar vroeg of laat haalt de exponentiële functie haar "
                  "in en loopt ze er ver voorbij."),
            ("kader", "<strong>Een exponentieel model blijft niet voor altijd geldig in de werkelijkheid.</strong> "
                      "Een bevolking of een kolonie loopt tegen grenzen aan, zoals plaats of voedsel. Het model "
                      "klopt dan alleen in het begin."),
        ]),
    ],
    onthoud=[
        "f(x) is b maal a tot de macht x: b is de beginwaarde, a de groeifactor.",
        "a groter dan 1 stijgt, a tussen 0 en 1 daalt; a is nooit 1 en nooit negatief.",
        "Domein: alle reële getallen. Bereik: alle positieve getallen.",
        "De grafiek raakt de x-as nooit.",
        "Deel in een tabel elk getal door het vorige om de groeifactor te vinden.",
    ],
)

# ───────────────────────── 7. Lineaire en exponentiële groeimodellen
BUNDELS["lineaire-en-exponentiele-groeimodellen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Lineaire en exponentiële groeimodellen",
    onder="Groeifactor en groeipercentage, verdubbelingstijd en halveringstijd, en waarom procenten niet optellen.",
    secties=[
        dict(kop="Twee soorten groei", blokken=[
            ("p", "<strong>Bij lineaire groei komt er elke tijdseenheid hetzelfde getal bij.</strong> <strong>Bij "
                  "exponentiële groei vermenigvuldig je elke tijdseenheid met dezelfde factor</strong>, waardoor "
                  "het bedrag dat erbij komt zelf ook steeds groter wordt. <strong>Een grafiek van lineaire groei "
                  "is een rechte</strong>, want elke stap in de tijd levert evenveel op."),
            ("p", "<strong>De beginwaarde van een groeimodel is de waarde op het tijdstip nul.</strong> <strong>Bij "
                  "lineaire groei lees je ze af als het snijpunt met de verticale as.</strong> <strong>Een "
                  "abonnement van 15 euro per maand plus 25 euro aansluiting past dus bij een lineair model met "
                  "beginwaarde 25.</strong>"),
            ("p", "<strong>Het kenmerk van lineaire groei is dat er elke tijdseenheid hetzelfde getal bij komt; het kenmerk van exponentiële groei is dat je elke tijdseenheid met dezelfde factor vermenigvuldigt.</strong> Daardoor wordt het bedrag dat erbij komt bij exponentiële groei zelf ook steeds groter."),
            ("fig", tabel(["Reeks", "Soort groei"], [
                ["20, 24, 28,8, 34,56", "exponentieel, factor 1,2"],
                ["60, 55, 50, 45", "lineair, telkens 5 eraf"],
                ["64, 48, 36, 27", "exponentieel, factor 0,75"],
                ["100, 110, 120, 130", "lineair, telkens 10 erbij"],
            ]), "Toont een tabel zo'n reeks, deel dan elk getal door het vorige of trek het vorige ervan af."),
            ("p", "<strong>Telt het ene model elke week 10 bij en groeit het andere met 10 procent per week, dan "
                  "haalt het model met 10 procent het andere op lange termijn in.</strong> Exponentiële groei wint "
                  "altijd van lineaire groei, al kan dat even duren."),
        ]),
        dict(kop="Groeifactor en groeipercentage", blokken=[
            ("p", "<strong>Bij een procentuele toename van p procent per tijdseenheid hoort de groeifactor 1 plus "
                  "p gedeeld door honderd.</strong> <strong>Bij een afname van p procent hoort 1 min p gedeeld "
                  "door honderd.</strong> Zo is <strong>de groeifactor bij 7 procent groei per jaar 1,07</strong>, "
                  "bij <strong>3 procent per maand 1,03</strong>, en bij <strong>20 procent daling per jaar "
                  "0,8</strong>. Omgekeerd: <strong>groeifactor 1,25 betekent 25 procent erbij</strong>, "
                  "<strong>groeifactor 1,1 betekent 10 procent per jaar</strong>, <strong>groeifactor 0,95 "
                  "betekent dat er 5 procent af gaat</strong> en <strong>een groeifactor van 2 betekent dat er "
                  "honderd procent bijkomt</strong>."),
            ("kader", "<strong>Een groeipercentage van 0 procent hoort bij een groeifactor van 1</strong>, niet "
                      "van 0. Bij factor 1 verandert er niets; factor 0 zou alles meteen wegvagen."),
            ("p", "Procenten tellen niet op. <strong>Twee keer tien procent erbij is samen eenentwintig procent, "
                  "niet twintig</strong>, want 1,1 maal 1,1 is 1,21: de tweede keer reken je op een groter bedrag. "
                  "Om dezelfde reden <strong>staat een prijs die eerst 20 procent stijgt en daarna 20 procent "
                  "daalt, níét weer op haar beginwaarde</strong>: 1,2 maal 0,8 is 0,96, dus vier procent lager."),
            ("p", "Twee rekenvoorbeelden. <strong>Stijgt een prijs van 80 naar 100 euro, dan is dat 25 "
                  "procent.</strong> <strong>Verliest een auto elk jaar 15 procent van zijn waarde, dan is een "
                  "auto van 20000 euro na een jaar 17000 euro waard.</strong>"),
        ]),
        dict(kop="Van de ene tijdseenheid naar de andere", blokken=[
            ("p", "Groeifactoren vermenigvuldig je, dus je zet ze om met machten en wortels, niet met delen. "
                  "<strong>Een groeifactor van 1,2 per jaar geeft over 2 jaar een factor 1,44</strong> (1,2 maal "
                  "1,2), en <strong>een groeifactor van 1,21 per 2 jaar geeft per jaar 1,1</strong> (de wortel "
                  "eruit)."),
            ("p", "<strong>Om een groeifactor per jaar om te zetten naar een factor per maand, neem je de "
                  "twaalfdemachtswortel</strong>, want twaalf maanden na elkaar moeten samen de jaarfactor geven. "
                  "<strong>Delen door twaalf is dus fout</strong>: delen hoort bij optellen, wortels horen bij "
                  "vermenigvuldigen. Op dezelfde manier: <strong>ken je de beginwaarde en de waarde na 10 jaar, "
                  "dan vind je de groeifactor per jaar als de tiendemachtswortel uit hun verhouding</strong>."),
        ]),
        dict(kop="Intrest, verval en verdubbeling", blokken=[
            ("p", "<strong>Intrest die ook op de intrest van vorige jaren berekend wordt, heet samengestelde "
                  "intrest</strong>; die is exponentieel. <strong>Enkelvoudige intrest hoort bij een lineair "
                  "model</strong>, want je rekent elk jaar op het beginbedrag. <strong>Zet je 1000 euro aan 10 "
                  "procent per jaar, dan staat er na 2 jaar 1210 euro</strong>, want het tweede jaar krijg je ook "
                  "intrest op de intrest van het eerste jaar. <strong>Een bedrag van 500 euro dat met 100 procent "
                  "per jaar groeit, is na 3 jaar 4000 euro.</strong>"),
            ("p", "<strong>De tijd waarna een exponentieel dalende hoeveelheid nog maar de helft bedraagt, heet de "
                  "halveringstijd.</strong> Bij radioactief verval heet dat de halfwaardetijd. <strong>Heeft een "
                  "stof een halveringstijd van 5 jaar, dan is er na 15 jaar nog een achtste over</strong>, en "
                  "<strong>bij een halveringstijd van 8 dagen is er na 16 dagen nog een vierde over</strong>. "
                  "<strong>Verdubbelt een populatie elke 3 jaar, dan is ze na 9 jaar 8 keer zo groot.</strong>"),
            ("p", "<strong>Verdubbelingstijd en halveringstijd hangen allebei alleen van de groeifactor af, niet "
                  "van de beginwaarde</strong>: of je met 100 of met 1000 begint, de tijd om te verdubbelen blijft "
                  "dezelfde. <strong>Om die tijd te berekenen gebruik je een logaritme</strong>, want de vraag na "
                  "hoeveel jaar iets verdubbeld is, is een vraag naar de exponent."),
            ("p", "<strong>Bij exponentiële afname bereikt de hoeveelheid nooit precies nul</strong>: je blijft met "
                  "een factor onder de 1 vermenigvuldigen."),
        ]),
        dict(kop="Wat procentuele groei betekent", blokken=[
            ("p", "<strong>Groeit een bevolking met 2 procent per jaar, dan groeit het aantal mensen dat er per "
                  "jaar bijkomt mee</strong>, want twee procent van een grotere bevolking is een groter aantal. "
                  "Dat is het verschil met lineaire groei."),
            ("kader", "<strong>In de werkelijkheid groeit een populatie zelden eindeloos exponentieel.</strong> "
                      "Plaats, voedsel en ziekte zetten vroeg of laat een rem op de groei, en dan past het model "
                      "alleen nog op het begin."),
        ]),
    ],
    onthoud=[
        "Lineair telt op, exponentieel vermenigvuldigt.",
        "Groeifactor = 1 plus of min het percentage gedeeld door honderd.",
        "Procenten tellen niet op: 1,1 maal 1,1 is 1,21.",
        "Tijdseenheid omzetten doe je met een wortel, niet met een deling.",
        "Verdubbelingstijd en halveringstijd hangen niet van de beginwaarde af.",
    ],
)

# ───────────────────────── 8. Kansen en de wet van Laplace
BUNDELS["kansen-en-de-wet-van-laplace-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kansen en de wet van Laplace",
    onder="Gunstige gevallen tellen, en het verschil tussen een kans en wat je in een proef meet.",
    secties=[
        dict(kop="De woorden", blokken=[
            ("p", "<strong>De verzameling van alle mogelijke uitkomsten van een kansexperiment heet de "
                  "uitkomstenverzameling</strong>, en je noteert ze met de letter U. Bij een dobbelsteen zitten "
                  "daar zes uitkomsten in; <strong>bij het trekken van één kaart uit een spel van 52 telt ze 52 "
                  "uitkomsten</strong>. <strong>Gooi je twee keer met een muntstuk, dan zitten er 4 uitkomsten "
                  "in</strong>: kop-kop, kop-munt, munt-kop en munt-munt. <strong>Gooi je met twee dobbelstenen, "
                  "dan telt ze 36 uitkomsten</strong>."),
            ("p", "<strong>Een gebeurtenis in de kansrekening is een deel van de uitkomstenverzameling.</strong> Een even worp is een "
                  "gebeurtenis: ze bestaat uit de uitkomsten 2, 4 en 6. Harten trekken is een gebeurtenis van "
                  "dertien uitkomsten."),
        ]),
        dict(kop="De wet van Laplace", blokken=[
            ("p", "<strong>De wet van Laplace zegt: de kans is het aantal gunstige uitkomsten gedeeld door het "
                  "totaal.</strong> <strong>Ze geldt alleen als alle uitkomsten even waarschijnlijk zijn</strong>, "
                  "zoals bij een eerlijke dobbelsteen. <strong>Bij een vervalste dobbelsteen mag je ze dus niet "
                  "gebruiken.</strong>"),
            ("fig", tabel(["Vraag", "Gunstig op totaal", "Kans"], [
                ["een 4 met één dobbelsteen", "1 op 6", "1/6"],
                ["een even getal met één dobbelsteen", "3 op 6", "1/2"],
                ["meer dan 4 met één dobbelsteen", "2 op 6", "1/3"],
                ["harten uit een spel van 52", "13 op 52", "1/4"],
                ["rood uit 3 rode en 7 blauwe knikkers", "3 op 10", "0,3"],
                ["geel uit 4 groene, 5 gele en 11 witte", "5 op 20", "0,25"],
                ["een bril bij 10 van de 25 leerlingen", "10 op 25", "0,4"],
                ["twee keer kop bij twee worpen", "1 op 4", "0,25"],
                ["twee zessen met twee dobbelstenen", "1 op 36", "1/36"],
                ["som 2 met twee dobbelstenen", "1 op 36", "1/36"],
            ]), "Tellen wat gunstig is, delen door alles wat kan."),
            ("weetje", "<strong>Gooi je met twee dobbelstenen, dan komt de som 7 het vaakst voor</strong>: zes van "
                       "de zesendertig uitkomsten geven zeven, meer dan bij elke andere som."),
        ]),
        dict(kop="Wat een kans kan zijn", blokken=[
            ("p", "<strong>Een kans ligt altijd tussen 0 en 1</strong>, dus <strong>1,5 kan nooit een kans "
                  "zijn</strong> en <strong>negatief kan ze evenmin</strong>: hoe onwaarschijnlijker, hoe dichter "
                  "bij nul. <strong>Een kans van 0 betekent dat de gebeurtenis onmogelijk is</strong>; <strong>een "
                  "kans van 1 betekent dat ze zeker gebeurt</strong>, bijvoorbeeld dat je met één dobbelsteen een "
                  "getal van 1 tot 6 gooit. <strong>De som van de kansen van alle uitkomsten in de "
                  "uitkomstenverzameling is 1</strong>, want er moet iets gebeuren."),
            ("p", "<strong>Een kans mag je ook als percentage schrijven</strong>: 0,25 is hetzelfde als 25 procent "
                  "of een vierde. <strong>Zegt een weerbericht 70 procent kans op regen, dan betekent dat dat het "
                  "in zeven van de tien vergelijkbare dagen regent.</strong>"),
        ]),
        dict(kop="De complementregel", blokken=[
            ("p", "<strong>De complementregel zegt: de kans dat iets gebeurt is 1 min de kans dat het niet "
                  "gebeurt.</strong> Ze is handig als het makkelijker is te tellen wat er fout kan gaan dan wat er "
                  "goed kan gaan."),
            ("p", "<strong>Is de kans op regen 0,3, dan is de kans op geen regen 0,7.</strong> <strong>De kans dat "
                  "je bij één worp met een dobbelsteen géén 6 gooit, is 5/6.</strong> <strong>Trek je uit een zak "
                  "van 20 balletjes waarvan er 11 wit zijn, dan is de kans op geen wit 0,45.</strong> <strong>Is "
                  "de kans dat een machine een goed stuk maakt 0,98, dan is de kans op een slecht stuk 0,02.</strong>"),
            ("p", "<strong>Bij een vraag als: wat is de kans op minstens één zes bij vier worpen, is de "
                  "complementregel handig omdat geen enkele zes makkelijker te tellen is.</strong> Minstens één "
                  "zes is een hele stapel gevallen; geen enkele zes is er maar één."),
        ]),
        dict(kop="Kans en relatieve frequentie", blokken=[
            ("p", "<strong>Een relatieve frequentie is niet precies hetzelfde als een kans.</strong> Een relatieve "
                  "frequentie meet je in een proef; een kans is de theoretische waarde. <strong>Gooi je 200 keer "
                  "met een muntstuk en krijg je 108 keer kop, dan is de relatieve frequentie van kop 0,54</strong>: "
                  "het aantal keer dat het voorkwam, gedeeld door het aantal pogingen. <strong>Komen er van 300 "
                  "leerlingen 24 met de trein, dan is de relatieve frequentie 0,08.</strong> <strong>Een relatieve "
                  "frequentie kan niet groter zijn dan 1</strong>, net als een kans."),
            ("p", "<strong>Hoe vaker je een kansexperiment herhaalt, hoe dichter de relatieve frequentie bij de "
                  "kans komt.</strong> Bij tien worpen kan je nog ver zitten; bij duizend worpen komt een eerlijk "
                  "muntstuk heel dicht bij de helft."),
            ("kader", "Twee hardnekkige denkfouten. <strong>Viel een muntstuk vijf keer na elkaar op kop, dan is "
                      "de kans op kop bij de volgende worp nog altijd een half</strong>: het muntstuk onthoudt "
                      "niets. En <strong>een kans van 1 op 1000 betekent niet dat je zeker wint als je duizend "
                      "keer meedoet</strong>; het is een gemiddelde op lange termijn, geen garantie."),
            ("p", "Nog twee voorbeelden met een loterij. <strong>Bij een loterij met 1 winnend lot op 1000 is de "
                  "kans om te winnen 0,001.</strong> <strong>Koop je er 5 loten van, dan is je kans 0,005.</strong>"),
        ]),
    ],
    onthoud=[
        "Wet van Laplace: gunstige uitkomsten gedeeld door alle uitkomsten.",
        "Ze geldt alleen als alle uitkomsten even waarschijnlijk zijn.",
        "Een kans ligt tussen 0 en 1; alle kansen samen geven 1.",
        "Complementregel: 1 min de kans dat het niet gebeurt.",
        "Een relatieve frequentie meet je, een kans bereken je.",
    ],
)

# ───────────────────────── 9. Kansbomen
BUNDELS["kansbomen-product-som-en-complement-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kansbomen: product, som en complement",
    onder="Vermenigvuldigen langs een pad, optellen tussen paden, en het verschil tussen met en zonder terugleggen.",
    secties=[
        dict(kop="Hoe een kansboom werkt", blokken=[
            ("p", "<strong>Je gebruikt een kansboom om een experiment in opeenvolgende stappen te bekijken.</strong> "
                  "Elke stap wordt een nieuwe laag takken. <strong>De weg van het begin tot helemaal achteraan "
                  "heet een pad</strong>, en elk pad is één mogelijke afloop van het hele experiment. <strong>Een "
                  "kansboom tekenen helpt vooral omdat je elke mogelijke afloop apart ziet staan</strong>, zodat "
                  "je geen enkel geval vergeet."),
            ("p", "<strong>De kansen staan bij de takken en niet bij de punten, omdat een tak één stap in het "
                  "experiment is.</strong> <strong>De kansen op de takken die uit één punt vertrekken, geven samen "
                  "1</strong>, want er moet iets gebeuren bij die stap. <strong>Ook de kansen van alle paden "
                  "samen geven 1</strong>, niet 2. En <strong>een tak kan nooit een kans groter dan 1 "
                  "dragen</strong>."),
            ("p", "Het aantal paden volgt uit de stappen. <strong>Gooi je drie keer met een muntstuk, dan heeft de "
                  "kansboom 8 paden.</strong> <strong>Heeft een boom twee stappen met telkens drie mogelijkheden, "
                  "dan zijn er 9 paden.</strong> <strong>Gooi je eerst met een muntstuk en dan met een "
                  "dobbelsteen, dan zijn er 12 paden.</strong> <strong>Bij drie stappen met telkens twee "
                  "mogelijkheden vertrekken er uit elk punt 2 takken</strong>: het aantal takken per punt is het "
                  "aantal mogelijkheden van die stap, het aantal paden is het product over alle stappen. "
                  "<strong>Een kansboom werkt ook als de twee stappen verschillende experimenten zijn</strong>, "
                  "bijvoorbeeld eerst een muntstuk en dan een dobbelsteen."),
        ]),
        dict(kop="De drie regels", blokken=[
            ("fig", tabel(["Regel", "Wat ze zegt", "Wanneer"], [
                ["productregel", "de kans op een pad is het product van de kansen op zijn takken", "binnen één pad"],
                ["somregel", "de kans op meerdere paden is de som van hun kansen", "tussen verschillende paden"],
                ["complementregel", "1 min de kans dat het niet gebeurt", "bij minstens, bij geen enkele"],
            ]), "Vermenigvuldigen langs een pad, optellen tussen paden."),
            ("p", "<strong>De kansen van twee takken binnen hetzelfde pad mag je niet optellen</strong>: binnen een "
                  "pad vermenigvuldig je. <strong>En de somregel mag je alleen gebruiken op paden die elkaar niet "
                  "overlappen</strong>; paden in een kansboom sluiten elkaar uit, en juist daarom mag je ze "
                  "optellen. Overlappende gevallen zou je dubbel tellen."),
            ("p", "Een paar rechtstreekse toepassingen. <strong>Heeft een pad takken 0,5 en 0,2, dan is de kans op "
                  "dat pad 0,1.</strong> <strong>Hebben twee paden kansen 0,12 en 0,18, dan is de kans dat een "
                  "van beide zich voordoet 0,3.</strong> <strong>Gooi je twee keer met een muntstuk, dan is de "
                  "kans op kop en dan nog eens kop 0,25</strong>, en <strong>bij drie keer kop is dat "
                  "0,125</strong>. <strong>Gooi je twee keer met een dobbelsteen, dan is de kans op twee keer een "
                  "zes 1/36.</strong>"),
            ("p", "De complementregel haalt je uit vragen met minstens. <strong>De kans op minstens één keer kop "
                  "bij twee worpen is 0,75</strong>, namelijk 1 min de kans op twee keer munt. <strong>De kans op "
                  "minstens één zes bij twee worpen met een dobbelsteen is 11/36.</strong> <strong>De "
                  "complementregel is vooral handig bij een vraag met het woord minstens.</strong>"),
        ]),
        dict(kop="Met of zonder terugleggen", blokken=[
            ("p", "<strong>Bij trekken zonder terugleggen veranderen de kansen op de tweede tak</strong>, want er "
                  "ligt één voorwerp minder in de zak. <strong>Bij trekken met terugleggen blijven de kansen bij "
                  "elke stap dezelfde</strong>, want de zak ziet er telkens hetzelfde uit."),
            ("fig", tabel(["Situatie", "Met terugleggen", "Zonder terugleggen"], [
                ["2 rode en 3 blauwe, twee keer rood", "0,4 maal 0,4 is 0,16", "0,4 maal 0,25 is 0,1"],
                ["7 goede en 3 slechte lampen, twee goede", "0,7 maal 0,7 is 0,49", "7/10 maal 6/9 is ongeveer 0,47"],
            ]), "Zonder terugleggen wordt de tweede kans kleiner."),
            ("p", "<strong>Zitten er in een doos 7 goede en 3 slechte lampen, dan is de kans dat één genomen lamp "
                  "goed is 0,7.</strong> Dat wordt de eerste tak van je boom. <strong>Zitten er in een klas 12 "
                  "meisjes en 8 jongens, dan is de kans dat de eerste gekozen leerling een meisje is 0,6</strong>, "
                  "en <strong>als dat zo is, is de kans dat de tweede ook een meisje is 11/19</strong>, want er "
                  "blijven nog 11 meisjes over op 19 leerlingen."),
        ]),
        dict(kop="Rekenen in de praktijk", blokken=[
            ("p", "<strong>Gooi je twee keer met een muntstuk, dan is de kans op precies één keer kop 0,5</strong>: "
                  "twee paden van elk 0,25, opgeteld met de somregel. <strong>Is een test 90 procent betrouwbaar "
                  "en doe je hem twee keer, dan is de kans dat hij twee keer juist is 0,81.</strong>"),
            ("p", "<strong>Keurt een fabriek 95 procent van de stukken goed, dan is de kans dat drie stukken na "
                  "elkaar allemaal goedgekeurd worden ongeveer 0,857</strong>, en <strong>de kans dat er minstens "
                  "één afgekeurd wordt ongeveer 0,143</strong>."),
            ("p", "<strong>Heeft een spel kans 0,4 om te winnen en speel je twee keer, dan is de kans op precies "
                  "één keer winnen 0,48</strong> (twee paden van 0,4 maal 0,6) <strong>en de kans om geen enkele "
                  "keer te winnen 0,36</strong>. <strong>Die drie kansen, twee keer winnen, precies één keer "
                  "winnen en nooit winnen, geven samen 1</strong>: 0,16 plus 0,48 plus 0,36. <strong>Is een bus op "
                  "tijd met kans 0,8, dan is de kans dat hij twee dagen na elkaar te laat is 0,04.</strong>"),
        ]),
    ],
    onthoud=[
        "Binnen een pad vermenigvuldigen, tussen paden optellen.",
        "De takken uit één punt geven samen 1, en alle paden samen ook.",
        "Minstens? Reken via het complement.",
        "Zonder terugleggen verandert de tweede kans.",
        "Aantal paden = het product van het aantal mogelijkheden per stap.",
    ],
)

# ───────────────────────── 10. Populatie, steekproef en representativiteit
BUNDELS["populatie-steekproef-en-representativiteit-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Populatie, steekproef en representativiteit",
    onder="Waarom de manier van kiezen zwaarder weegt dan het aantal.",
    secties=[
        dict(kop="De drie woorden", blokken=[
            ("p", "<strong>De hele groep waarover je iets wil weten, heet de populatie.</strong> <strong>Het deel "
                  "van de populatie dat je echt onderzoekt, heet de steekproef.</strong> <strong>De variabele is "
                  "het kenmerk dat je meet</strong>, bijvoorbeeld de lengte, het aantal uren slaap of het merk van "
                  "de fiets."),
            ("fig", tabel(["Onderzoek", "Populatie", "Steekproef", "Variabele"], [
                ["lengte van vijftienjarigen", "alle vijftienjarigen in België", "wie je echt opmeet", "de lengte"],
                ["slaap van studenten", "alle studenten", "de bevraagde studenten", "uren slaap"],
                ["gewicht van zakken van 500 g", "alle zakken", "tien zakken per uur", "het gewicht"],
            ]), "Drie onderzoeken, dezelfde drie begrippen."),
            ("p", "<strong>Je werkt met een steekproef omdat de hele populatie meten vaak onmogelijk of te duur "
                  "is.</strong> Het is een afweging: minder werk, maar wel onzekerheid over het besluit. "
                  "<strong>Een school van 800 leerlingen die er 80 bevraagt, heeft een steekproef van 10 procent "
                  "van de populatie.</strong>"),
            ("p", "De notatie houdt steekproef en populatie uit elkaar. <strong>Het steekproefgemiddelde krijgt "
                  "een streepje boven de x, het populatiegemiddelde de Griekse letter mu.</strong> <strong>De "
                  "standaardafwijking van een populatie noteer je met de Griekse letter sigma, die van een "
                  "steekproef met een gewone s.</strong> Je spreekt dan van de populatiestandaardafwijking en de steekproefstandaardafwijking. Zo zie je aan de notatie meteen waar een getal vandaan "
                  "komt."),
        ]),
        dict(kop="Aselect, vertekend, representatief", blokken=[
            ("p", "<strong>Een steekproef waarin elk lid van de populatie evenveel kans heeft om gekozen te "
                  "worden, heet aselect.</strong> Aselect betekent dat het toeval kiest, niet jij. <strong>Namen "
                  "uit een hoed trekken is zo'n manier</strong>; in de praktijk gebruikt men een toevalsgenerator."),
            ("p", "<strong>Een steekproef waarin bepaalde leden van de populatie bevoordeeld worden, heet "
                  "vertekend.</strong> Wordt je besluit over de populatie scheefgetrokken door je manier van kiezen, dan heet dat met één woord <strong>vertekening</strong>, soms ook "
                  "bias genoemd; de oorzaak zit dan in de opzet van het onderzoek, niet in het rekenwerk."),
            ("p", "<strong>Een representatieve steekproef lijkt in haar samenstelling op de populatie</strong>: "
                  "dezelfde verhoudingen in leeftijd, geslacht of woonplaats. <strong>Daarom kiest men bij een "
                  "peiling bewust mensen uit elke provincie en elke leeftijdsgroep: om de verhoudingen van de "
                  "populatie na te bootsen.</strong> <strong>Aselect trekken is geen vervanging van "
                  "representativiteit</strong>, het is juist de manier om ze waarschijnlijk te maken."),
            ("kader", "<strong>Een grotere steekproef is niet vanzelf representatief.</strong> Grootte helpt tegen "
                      "toeval, maar niet tegen vertekening: honderdduizend mensen op één festival zeggen nog "
                      "altijd niets over het hele land. <strong>Een vertekende steekproef kan je dan ook niet "
                      "rechtzetten door er meer mensen bij te nemen op dezelfde manier</strong>; je moet de manier van "
                      "kiezen aanpassen. Omgekeerd geldt wel: <strong>is een steekproef aselect, dan maakt een "
                      "grotere steekproef het besluit betrouwbaarder.</strong>"),
            ("p", "<strong>Ook een aselecte steekproef kan door puur toeval scheef uitvallen.</strong> De kans "
                  "erop wordt kleiner naarmate de steekproef groter is, en dat is iets anders dan een "
                  "vertekening. <strong>Eén persoon volstaat nooit</strong>, ook niet als die heel gemiddeld "
                  "lijkt: je weet vooraf niet wie gemiddeld is, en één meting zegt niets over de spreiding."),
        ]),
        dict(kop="Waar het misloopt", blokken=[
            ("fig", tabel(["Manier van bevragen", "Wie ontbreekt of te zwaar weegt"], [
                ["alleen leden van de sportclub over sporten", "wie niet sport; de uitkomst ligt te hoog"],
                ["een vrijwillige enquête online", "alleen wie zich betrokken voelt, vult ze in"],
                ["bellen tussen 9 en 17 uur op een werkdag", "wie overdag werkt"],
                ["alleen klanten die iets kochten", "de mening van wie niets kocht"],
                ["ouders bevragen op het oudercontact", "de ouders die niet komen"],
                ["de baas voert zelf de tevredenheidsgesprekken", "mensen antwoorden minder eerlijk"],
                ["een vragenlijst per post met 8 procent respons", "wie terugstuurt, kan systematisch anders zijn"],
            ]), "Telkens is het de manier van kiezen die het besluit kleurt."),
            ("p", "<strong>Een fabrikant die elke honderdste doos van de band test, neemt een systematische "
                  "steekproef.</strong> Dat werkt goed, zolang er geen patroon in de productie zit dat met dat "
                  "ritme meeloopt."),
            ("p", "<strong>Meet een onderzoeker de leeftijd van bezoekers op een rockfestival en besluit hij dat "
                  "de gemiddelde Belg 24 jaar is, dan veralgemeent hij een bijzondere groep naar iedereen.</strong> "
                  "Zijn steekproef is prima voor dat festival, maar niet voor het land. <strong>En hoe je de vraag "
                  "stelt, kan het antwoord beïnvloeden</strong>: een sturende vraag levert sturende antwoorden op."),
        ]),
        dict(kop="Wat je ermee mag besluiten", blokken=[
            ("p", "<strong>Een besluit uit een vertekende steekproef mag je niet op de hele populatie "
                  "toepassen.</strong> Dan schuift de fout mee naar je conclusie; je kan hoogstens iets zeggen "
                  "over de groep die oververtegenwoordigd was. <strong>Voorspelt een peiling een uitslag die er "
                  "ver naast zit, dan ligt het meestal aan een niet-representatieve steekproef</strong>, niet aan "
                  "de rekenkunde erna."),
            ("p", "<strong>Een steekproef van 1000 mensen kan wel degelijk betrouwbare uitspraken geven over "
                  "miljoenen mensen</strong>, als ze aselect en representatief is. Dat is precies waarom peilingen "
                  "met zo'n klein aantal toch werken. <strong>Onderzoekers vermelden hoe groot hun steekproef was "
                  "omdat het iets zegt over de betrouwbaarheid</strong>, samen met de manier van kiezen."),
            ("p", "<strong>Lees je dat uit een bevraging van 40 mensen blijkt dat 60 procent van de Belgen iets "
                  "vindt, dan is je eerste vraag: hoe werden die 40 mensen gekozen.</strong> Dat weegt zwaarder "
                  "dan het aantal."),
            ("kader", "<strong>Statistiek geeft geen zekerheid over de populatie.</strong> Ze geeft een "
                      "onderbouwde schatting met een zekere betrouwbaarheid. Zekerheid krijg je alleen door "
                      "iedereen te meten."),
        ]),
    ],
    onthoud=[
        "Populatie is het geheel, steekproef is wat je meet, variabele is wat je opschrijft.",
        "Aselect: het toeval kiest. Vertekend: bepaalde leden worden bevoordeeld.",
        "Groter helpt tegen toeval, niet tegen vertekening.",
        "Vraag altijd eerst hóé de steekproef gekozen werd.",
        "Statistiek geeft een schatting, geen zekerheid.",
    ],
)

# ───────────────────────── 11. Samenhang en causaliteit
BUNDELS["samenhang-en-causaliteit-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Samenhang en causaliteit",
    onder="Vier manieren waarop twee grootheden samen kunnen bewegen, en maar één daarvan is een oorzaak.",
    secties=[
        dict(kop="Samenhang is geen oorzaak", blokken=[
            ("p", "<strong>Samenhang tussen twee variabelen betekent dat ze samen veranderen.</strong> "
                  "<strong>Als de ene variabele de andere echt veroorzaakt, spreek je van causaliteit</strong>, of "
                  "van een causaal verband. <strong>Samenhang betekent niet altijd dat er een oorzakelijk verband "
                  "is</strong>; dat is de meest voorkomende denkfout in de statistiek. Samenhang is een "
                  "aanwijzing, geen bewijs."),
            ("p", "<strong>Samenhang kan ook negatief zijn</strong>: de ene gaat omhoog terwijl de andere omlaag "
                  "gaat. Ook dan bewegen ze samen. <strong>Twee grootheden die samen stijgen, hebben daarom nog "
                  "geen oorzakelijk verband</strong>: voor een oorzaak heb je een mechanisme nodig dat uitlegt hoe "
                  "het werkt. <strong>Een verband dat je niet kan verklaren, is dus nog geen oorzaak.</strong>"),
        ]),
        dict(kop="De vier gevallen", blokken=[
            ("p", "<strong>Bij een statistisch verband moet je vier gevallen kunnen onderscheiden: causaliteit, "
                  "omgewisselde causaliteit, een verborgen variabele en toeval.</strong> Pas als je de drie andere "
                  "kan uitsluiten, mag je over een oorzaak spreken."),
            ("fig", tabel(["Geval", "Wat er aan de hand is", "Voorbeeld"], [
                ["causaliteit", "A veroorzaakt echt B", "roken en longkanker"],
                ["omgewisselde causaliteit", "B veroorzaakt A, niet omgekeerd", "wie hoofdpijn heeft, drinkt minder"],
                ["verborgen variabele", "C beïnvloedt A én B", "warm weer, ijsjes en verdrinkingen"],
                ["toeval", "geen verband, alleen gelijkloop", "films van een acteur en kaasconsumptie"],
            ]), "Vier verklaringen voor hetzelfde patroon in de cijfers."),
            ("p", "<strong>Een factor die twee variabelen allebei beïnvloedt, zodat ze samen bewegen zonder elkaar "
                  "te veroorzaken, heet een verborgen variabele</strong>, soms ook een storende variabele. "
                  "<strong>Ze staat niet in de tabel van het onderzoek</strong>: ze is juist niet gemeten, en "
                  "daarom moet je ze zelf bedenken vanuit je kennis van de situatie."),
            ("p", "<strong>Oorzaak en gevolg kunnen in een onderzoek ook omgewisseld lijken.</strong> Uit de "
                  "cijfers alleen zie je vaak niet wat eerst kwam. <strong>Als A en B samenhangen, kan B evengoed "
                  "de oorzaak van A zijn.</strong>"),
            ("p", "<strong>En een sterke samenhang kan zuiver door toeval ontstaan</strong>, zeker bij korte "
                  "reeksen of als je in heel veel gegevens gaat zoeken tot er iets opvalt. <strong>Lopen twee "
                  "reeksen tien jaar lang bijna perfect samen zonder dat iemand kan uitleggen waarom, dan heet dat "
                  "een toevallige samenhang.</strong>"),
        ]),
        dict(kop="Voorbeelden om op te oefenen", blokken=[
            ("fig", tabel(["Vaststelling", "Meest waarschijnlijke verklaring"], [
                ["in de zomer meer ijsjes én meer verdrinkingen", "het warme weer, een derde verborgen variabele"],
                ["kinderen met grotere voeten lezen beter", "de leeftijd"],
                ["steden met meer brandweermannen hebben meer brandschade", "de grootte van de stad"],
                ["scholen met meer computers halen betere resultaten", "het budget van de school"],
                ["in landen met meer tv's leeft men langer", "rijkere landen hebben betere zorg én meer toestellen"],
                ["rode auto's hebben vaker ongevallen", "wie rood kiest, rijdt misschien anders"],
                ["mensen met een hond bewegen meer", "wie graag beweegt, neemt vaker een hond"],
                ["wie meer water drinkt, heeft minder hoofdpijn", "wie hoofdpijn heeft, drinkt minder"],
            ]), "Telkens: niet de eerste verklaring die opkomt."),
            ("p", "Dezelfde voorzichtigheid geldt bij krantenkoppen. <strong>Zegt een kop dat wie ontbijt betere "
                  "punten haalt, dan is de voorzichtige lezing dat ontbijten samenhangt met betere punten</strong>; "
                  "misschien speelt een rustiger gezinssituatie mee. <strong>Zegt een artikel dat koffie je leven "
                  "verlengt op basis van een bevraging, dan toont dat samenhang, geen oorzaak.</strong> <strong>En "
                  "halen leerlingen die veel huiswerk maken hogere punten, dan is er samenhang en is de richting "
                  "nog onduidelijk</strong>: misschien is motivatie de verborgen variabele."),
        ]),
        dict(kop="Hoe je een oorzaak wél aantoont", blokken=[
            ("p", "<strong>Je toont het sterkst aan dat A werkelijk B veroorzaakt met een proef waarin je A "
                  "verandert en de rest gelijk houdt.</strong> <strong>Een proef waarin je één factor verandert en "
                  "al de rest gelijk houdt, heet een gecontroleerde proef, of een gecontroleerd experiment.</strong> Alleen zo'n proef kan een "
                  "verborgen variabele uitsluiten; waarnemen alleen volstaat niet. <strong>Een onderzoek dat "
                  "alleen waarneemt, kan nooit met zekerheid een oorzaak aantonen.</strong>"),
            ("p", "<strong>De groep die het middel niet krijgt, heet de controlegroep.</strong> <strong>Een "
                  "controlegroep helpt om een causaal verband aan te tonen</strong>, want je vergelijkt met een "
                  "groep die alles hetzelfde meemaakt behalve die ene factor. <strong>Zegt een reclame dat wie hun "
                  "product gebruikt gezonder is, dan ontbreekt precies die vergelijking met een gelijkaardige "
                  "groep zonder het product.</strong> <strong>Hangen twee variabelen samen én vindt een "
                  "gecontroleerde proef hetzelfde, dan is een causaal verband veel aannemelijker.</strong>"),
            ("p", "Twee vragen helpen je verder. <strong>Is er een verklaring hoe de ene zaak de andere "
                  "hindert of bevordert?</strong> Een plausibel mechanisme is een van de sterkste argumenten voor "
                  "een oorzaak. En: <strong>gebeurde hetzelfde ook elders?</strong> Zet een gemeente meer "
                  "verlichting en daalt de criminaliteit, dan moet je nagaan of de criminaliteit elders ook daalde."),
            ("p", "<strong>Vragen naar de opzet van het onderzoek is daarom zinvol: de opzet bepaalt wat je mag "
                  "besluiten.</strong> Een proef met controlegroep draagt veel verder dan een bevraging achteraf. "
                  "<strong>De beste houding bij een opvallende statistiek in de krant is dan ook: vragen hoe de "
                  "gegevens verzameld zijn.</strong> De rekenkunde klopt meestal wel."),
            ("kader", "<strong>Een onderzoeker die een causaal verband suggereert, heeft daarmee niet automatisch "
                      "gelijk.</strong> Je mag en moet beoordelen of hij dat terecht doet, door de drie andere "
                      "verklaringen te overwegen. <strong>Samenhang is geen bewijs van causaliteit</strong>: dat "
                      "is de belangrijkste regel uit dit hoofdstuk, en de meest genegeerde in de krant."),
        ]),
    ],
    onthoud=[
        "Samenhang is geen bewijs van een oorzaak.",
        "Vier verklaringen: causaliteit, omgewisselde causaliteit, verborgen variabele, toeval.",
        "Een verborgen variabele staat niet in de tabel; je moet ze bedenken.",
        "Alleen een gecontroleerde proef met controlegroep sluit ze uit.",
        "Vraag altijd hoe de gegevens verzameld zijn.",
    ],
)

# ───────────────────────── 12. De normale verdeling en de Gausskromme
BUNDELS["de-normale-verdeling-en-de-gausskromme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De normale verdeling en de Gausskromme",
    onder="De klokvorm, wat gemiddelde en standaardafwijking eraan doen, en kansen als oppervlakte.",
    secties=[
        dict(kop="De klokvorm", blokken=[
            ("p", "<strong>De grafiek van een normale verdeling heeft de vorm van een klok</strong>: hoog in het "
                  "midden, laag en afvlakkend aan beide kanten. <strong>Die klokvormige kromme heet de "
                  "Gausskromme.</strong> <strong>Een normale verdeling is symmetrisch rond haar "
                  "gemiddelde</strong>: links en rechts van de top zien de helften er precies hetzelfde uit. "
                  "<strong>Daardoor vallen gemiddelde, mediaan en modus samen</strong>, precies in het midden."),
            ("p", "<strong>Twee getallen leggen een normale verdeling helemaal vast: het gemiddelde en de "
                  "standaardafwijking.</strong> Je noteert ze met de letter N en die twee getallen tussen haakjes; "
                  "<strong>het gemiddelde staat als eerste</strong>, de standaardafwijking als tweede. Zo weet een "
                  "lezer meteen waar de kromme ligt en hoe breed ze is."),
            ("p", "<strong>De top van de Gausskromme ligt bij het gemiddelde.</strong> <strong>De "
                  "standaardafwijking bepaalt hoe breed ze is</strong>: een grotere standaardafwijking geeft een "
                  "bredere en plattere klok, geen hogere en smallere. <strong>Is de lengte van volwassen mannen "
                  "normaal verdeeld met gemiddelde 178 cm, dan ligt de top bij 178 cm.</strong>"),
            ("p", "Vergelijken gaat dan vanzelf. <strong>Hebben twee Gausskrommen hetzelfde gemiddelde en is de "
                  "ene veel smaller, dan heeft die smalle de kleinste standaardafwijking</strong>: de waarden "
                  "kleven dicht bij het gemiddelde. <strong>Zijn ze even breed en ligt de ene meer naar rechts, "
                  "dan heeft die rechtse het grootste gemiddelde</strong>: verschuiven doet het gemiddelde, "
                  "uitrekken doet de standaardafwijking. <strong>Hebben twee klassen hetzelfde gemiddelde maar "
                  "heeft de ene een veel grotere standaardafwijking, dan liggen daar de punten verder uit "
                  "elkaar</strong>: meer heel sterke én meer heel zwakke resultaten."),
        ]),
        dict(kop="Oppervlakte is kans", blokken=[
            ("p", "<strong>De totale oppervlakte onder een Gausskromme is 1</strong>, want alle kansen samen geven "
                  "1. <strong>De oppervlakte onder een stuk van de kromme stelt de kans voor dat een waarde in dat "
                  "stuk valt.</strong> <strong>Daarom blijft die oppervlakte bij elke Gausskromme gelijk aan "
                  "1</strong>, en wordt de kromme platter als ze breder wordt."),
            ("p", "<strong>De kans dat een waarde onder het gemiddelde ligt, is 0,5</strong>, want de kromme is "
                  "symmetrisch. <strong>De kans dat een waarde boven het gemiddelde ligt, is even groot als de "
                  "kans eronder.</strong> <strong>Heeft een normale verdeling gemiddelde 100, dan is de kans dat "
                  "een waarde groter is dan 100 dus 0,5.</strong>"),
            ("p", "<strong>De kans op precies één waarde kan je niet als oppervlakte berekenen</strong>: één punt "
                  "heeft geen breedte. Je werkt altijd met een interval, bijvoorbeeld tussen 170 en 180 "
                  "centimeter. <strong>De normale verdeling is dan ook een continu model: ze werkt met waarden die "
                  "elke tussenwaarde kunnen aannemen</strong>, zoals lengte, gewicht en tijd."),
            ("p", "<strong>Op het examen bereken je de kans bij een normaal verdeelde grootheid met de "
                  "rekenapps.</strong> De oppervlakte onder de kromme is niet met de hand te berekenen; daarvoor "
                  "is ICT uitdrukkelijk toegelaten. <strong>Wil een fabrikant weten hoeveel procent van zijn "
                  "zakken onder 490 gram zit, dan berekent hij de oppervlakte onder de kromme links van "
                  "490.</strong>"),
        ]),
        dict(kop="68, 95 en de staarten", blokken=[
            ("fig", tabel(["Binnen hoeveel standaardafwijkingen", "Welk aandeel", "Wat erbuiten ligt"], [
                ["één", "ongeveer 68 procent", "ongeveer 32 procent"],
                ["twee", "ongeveer 95 procent", "ongeveer 5 procent"],
                ["drie", "bijna alles", "een heel kleine rest"],
            ]), "De vuistregel die je overal terugziet."),
            ("p", "<strong>Ongeveer 68 procent van de waarden ligt binnen één standaardafwijking van het "
                  "gemiddelde</strong>, en <strong>ongeveer 95 procent binnen twee</strong>. <strong>Buiten twee "
                  "standaardafwijkingen ligt dus ongeveer 5 procent</strong>, verdeeld over beide staarten. Daarom "
                  "noemt men een waarde buiten die grens al snel uitzonderlijk."),
            ("p", "Een voorbeeld met lengtes. <strong>Bij gemiddelde 178 cm en standaardafwijking 7 cm ligt "
                  "ongeveer 68 procent tussen 171 en 185 cm</strong>, en <strong>ongeveer 95 procent tussen 164 en "
                  "192 cm</strong>. Een voorbeeld met punten: <strong>bij gemiddelde 60 en standaardafwijking 10 "
                  "is een score van 85 uitzonderlijk hoog</strong>, want die ligt meer dan twee "
                  "standaardafwijkingen boven het gemiddelde."),
            ("p", "En een voorbeeld dat je overal tegenkomt. <strong>Een IQ-test met gemiddelde 100 en "
                  "standaardafwijking 15 geeft ongeveer 68 procent tussen 85 en 115</strong>, en <strong>ongeveer "
                  "2,5 procent boven 130</strong>: buiten twee standaardafwijkingen ligt 5 procent, verdeeld over "
                  "twee staarten."),
            ("p", "<strong>Een normale verdeling heeft geen begin en geen einde</strong>: de kromme kruipt aan "
                  "beide kanten eindeloos naar de as toe zonder ze te raken, dus er is geen bereik waarbuiten de kans precies nul is. Heel ver weg wordt de kans wel "
                  "verwaarloosbaar klein."),
        ]),
        dict(kop="Past het model?", blokken=[
            ("p", "<strong>Niet elke verzameling gegevens is normaal verdeeld.</strong> Veel wel, maar inkomens "
                  "bijvoorbeeld zijn scheef verdeeld, met een lange staart naar rechts. <strong>Je beoordeelt of "
                  "het model past door te kijken of het histogram klokvormig is.</strong> <strong>Een scheef "
                  "histogram met een lange staart aan één kant past slecht bij een normale verdeling</strong>, "
                  "want die is symmetrisch. <strong>Heeft een histogram van wachttijden veel korte wachttijden en "
                  "een lange staart naar rechts, dan past het model niet.</strong>"),
            ("p", "<strong>Je kan ook de dichtheidsfunctie over het histogram tekenen om te zien of het model "
                  "past</strong>, met het gemiddelde en de standaardafwijking van je gegevens als schatting. "
                  "<strong>Die twee gebruik je dus als schatting voor de twee getallen van de normale "
                  "verdeling</strong>, en <strong>het steekproefgemiddelde geldt als schatting voor het gemiddelde "
                  "van de populatie</strong>. Dat is de brug tussen je metingen en het model."),
            ("weetje", "<strong>Is de vullijn van een machine normaal verdeeld rond 500 gram, dan betekent een "
                       "kleine standaardafwijking dat de machine heel nauwkeurig vult</strong>: de zakken wijken "
                       "weinig van 500 gram af."),
        ]),
    ],
    onthoud=[
        "De Gausskromme is klokvormig en symmetrisch rond het gemiddelde.",
        "Het gemiddelde bepaalt waar ze ligt, de standaardafwijking hoe breed ze is.",
        "De oppervlakte eronder is 1, en een stuk oppervlakte is een kans.",
        "68 procent binnen één, 95 procent binnen twee standaardafwijkingen.",
        "Een scheef histogram past niet bij dit model.",
    ],
)
