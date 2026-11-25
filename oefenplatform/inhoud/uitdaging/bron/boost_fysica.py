# -*- coding: utf-8 -*-
"""Uitdaging Fysica 🚀 Boost doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen. Casussen, tabellen, keuzelijsten, slepen, koppelen, sorteren,
volgorde, veel rekenvragen, vier klikvragen op twee zelf getekende prenten en
een open onderzoeksvraag. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Fysica Boost doorstroom. We rekenen met g = 9,81 N/kg.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_fysica.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Fysica"
BESTAND = "boost-fysica-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/fysica-boost-uitdaging"
GRAFIEK = "twee-lopers-x-t.svg"
BAK = "waterbak-punten.svg"
# klikvakken: zie maak_prenten_boost_fysica.py
KRUIS = [46.5, 44.4, 8.0, 12.9]
LIJN_A = [[18.9, 67.5, 8.0, 12.9], [34.6, 54.3, 8.0, 12.9], [58.4, 34.4, 8.0, 12.9], [74.2, 21.2, 8.0, 12.9]]
PUNT_Q = [34.5, 49.2, 8.5, 11.7]
PUNT_R = [48.5, 74.2, 8.5, 11.7]
PUNT_S = [64.5, 49.2, 8.5, 11.7]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # x(t)-grafiek van twee lopers (prent)
    klik("Bekijk de x(t)-grafiek. Klik op het punt waar de twee lopers elkaar kruisen.",
         GRAFIEK, [KRUIS],
         "Waar de twee rechten elkaar snijden, staan de lopers op hetzelfde tijdstip op dezelfde plaats: na 10 seconden, op 40 meter."),
    klik("Klik op de lijn van de loper met de grootste snelheid, in grootte.",
         GRAFIEK, LIJN_A,
         "De steilheid van een x(t)-grafiek is de snelheid. A legt 80 meter af in 20 seconden (4 meter per seconde). B legt 40 meter af in 20 seconden (2 meter per seconde). A is dus sneller."),
    met_prent(GRAFIEK, inv(
        "Wat is de snelheid van loper B, in meter per seconde? Let op het teken en geef enkel het getal.",
        ["-2", "−2"],
        "B gaat van 60 naar 20 meter in 20 seconden: een verplaatsing van min 40 meter. Min 40 gedeeld door 20 is min 2 meter per seconde. Het minteken zegt dat B tegen de zin van de x-as in loopt.")),
    met_prent(GRAFIEK, mk(
        "Welke positiefunctie hoort bij loper B?",
        ["\\(x = 60 - 2 \\cdot t\\)", "\\(x = 20 + 2 \\cdot t\\)", "\\(x = 60 + 2 \\cdot t\\)", "\\(x = 2 - 60 \\cdot t\\)"],
        0,
        "In \\(x = x_{0} + v \\cdot t\\) is de beginpositie 60 meter en de snelheid min 2 meter per seconde.")),
    met_prent(GRAFIEK, inv(
        "Hoeveel meter liggen de twee lopers uit elkaar na 20 seconden? Geef enkel het getal.",
        "60",
        "Na 20 seconden staat A op 80 meter en B op 20 meter. Het verschil is 60 meter.")),

    # De waterbak (prent)
    klik("Bekijk de waterbak. Klik op het punt met de grootste hydrostatische druk.",
         BAK, [PUNT_R],
         "De hydrostatische druk hangt enkel af van de diepte onder het wateroppervlak. R ligt het diepst, op 3,5 meter."),
    klik("Klik op het punt waar de druk even groot is als in punt Q.",
         BAK, [PUNT_S],
         "S ligt op dezelfde diepte als Q, 2 meter. In een vloeistof in rust is de druk op dezelfde diepte overal gelijk."),
    met_prent(BAK, inv(
        "Hoe groot is de hydrostatische druk in punt R, in kilopascal? Rond af op een geheel getal en geef enkel het getal.",
        "34",
        "\\(p = \\rho \\cdot g \\cdot h = 1000 \\cdot 9{,}81 \\cdot 3{,}5 = 34\\,335\\) pascal, afgerond 34 kilopascal.")),
    met_prent(BAK, tabel(
        "Klopt dit over de waterbak?",
        [
            ("De druk in R is zeven keer zo groot als de hydrostatische druk in P.", J),
            ("Als de bak breder was, zou de druk in R groter zijn.", F),
            ("Een manometer in Q meet ook de luchtdruk boven het water mee.", J),
            ("In zout water zou de druk in Q kleiner zijn.", F),
        ],
        "R ligt op 3,5 meter en P op 0,5 meter: zeven keer zo diep, dus zeven keer zoveel hydrostatische druk. De breedte speelt geen rol, enkel de diepte en de dichtheid. Zout water is dichter en geeft dus een grotere druk.")),

    # Eenheden
    tabel(
        "Zet om naar de SI-eenheid.",
        [
            ("\\(54\\) km/h", "15 m/s"),
            ("\\(2{,}5\\) L", "0,0025 m³"),
            ("\\(27\\) °C", "300 K"),
            ("\\(450\\) g", "0,45 kg"),
        ],
        "Delen door 3,6 geeft meter per seconde. Een liter is een duizendste kubieke meter. Bij graden Celsius tel je 273 op voor kelvin. Duizend gram is een kilogram.",
        kolommen=["15 m/s", "0,0025 m³", "300 K", "0,45 kg"]),

    # Versnelde beweging
    casus(
        "Een auto staat stil aan een verkeerslicht. Als het groen wordt, versnelt hij eenparig tot \\(30\\) m/s in \\(6{,}0\\) s.",
        [
            inv("Hoe groot is de versnelling van de auto, in meter per seconde kwadraat? Geef enkel het getal.",
                "5",
                "\\(a = \\Delta v / \\Delta t = 30 / 6{,}0 = 5{,}0\\) meter per seconde kwadraat."),
            inv("Hoeveel meter legt de auto af in die zes seconden? Geef enkel het getal.",
                "90",
                "Vanuit rust is \\(x = \\frac{1}{2} \\cdot a \\cdot t^{2} = 0{,}5 \\cdot 5 \\cdot 36 = 90\\) meter. Je kan ook de oppervlakte onder de v(t)-grafiek nemen: een driehoek van 6 bij 30, gedeeld door 2."),
            mk("Hoe ziet de x(t)-grafiek van de auto er in die zes seconden uit?",
               ["een parabool die steeds steiler wordt", "een horizontale rechte op hoogte nul", "een rechte door de oorsprong die niet buigt", "een parabool die steeds vlakker wordt"],
               0,
               "Bij een eenparig versnelde beweging vanuit rust neemt de snelheid toe. De steilheid van de x(t)-grafiek is de snelheid, dus de grafiek wordt steeds steiler."),
        ],
    ),
    inv("Je laat een steen vallen vanuit rust. Hoe groot is zijn snelheid na \\(2{,}0\\) seconden, zonder luchtweerstand, in meter per seconde? Rond af op één decimaal.",
        ["19,6", "19.6"],
        "Bij een vrije val is \\(v = g \\cdot t = 9{,}81 \\cdot 2{,}0 = 19{,}62\\) meter per seconde, afgerond 19,6."),
    keuze(
        "Je gooit een bal recht omhoog. Op het hoogste punt is de snelheid [[*nul|het grootst]] en de versnelling [[*9,81 m/s² naar beneden|nul]].",
        "Op het hoogste punt keert de bal om: zijn snelheid is daar even nul. De zwaartekracht blijft werken, dus de versnelling is ook daar de valversnelling naar beneden."),

    # Krachten
    tabel(
        "Reken de kracht uit, in newton.",
        [
            ("de zwaartekracht op een kind van \\(50\\) kg", "490,5"),
            ("de veerkracht van een veer met \\(k = 200\\) N/m die \\(0{,}05\\) m uitgerekt is", "10"),
            ("de wrijvingskracht op een kist van \\(40\\) kg met \\(\\mu = 0{,}25\\) op een vlakke vloer", "98,1"),
        ],
        "\\(F_{z} = m \\cdot g = 50 \\cdot 9{,}81\\). \\(F_{v} = k \\cdot \\Delta l = 200 \\cdot 0{,}05\\). \\(F_{w} = \\mu \\cdot F_{N} = 0{,}25 \\cdot 40 \\cdot 9{,}81\\).",
        kolommen=["10", "98,1", "490,5"]),
    mk("Een parachutist valt met een constante snelheid. Welke uitspraak klopt?",
       ["De luchtweerstand is even groot als zijn gewicht.", "Zijn gewicht is groter dan de luchtweerstand op hem.", "Er werkt op dat moment geen zwaartekracht op hem.", "De luchtweerstand is groter dan zijn gewicht samen."],
       0,
       "Een constante snelheid betekent dat de resulterende kracht nul is. De luchtweerstand naar boven en de zwaartekracht naar beneden zijn dus even groot."),
    sleep(
        "Een kracht is een [[vectoriële]] grootheid: ze heeft een grootte, een richting, een zin en een [[aangrijpingspunt]]. Je meet een kracht met een [[dynamometer]].",
        ["scalaire", "manometer"],
        "Een vector heeft vier kenmerken. Een dynamometer meet krachten, een manometer meet de druk van een gas."),

    # Archimedes en moment
    inv("Een blok met een volume van \\(0{,}002\\) m³ zit helemaal onder water. Hoe groot is de archimedeskracht, in newton? Geef enkel het getal, met twee decimalen.",
        ["19,62", "19.62"],
        "\\(F_{A} = \\rho \\cdot V \\cdot g = 1000 \\cdot 0{,}002 \\cdot 9{,}81 = 19{,}62\\) newton."),
    tabel(
        "Zinkt, zweeft of drijft dit voorwerp in water?",
        [
            ("een blok met een dichtheid van \\(800\\) kg/m³", "Drijft"),
            ("een steen met een dichtheid van \\(2600\\) kg/m³", "Zinkt"),
            ("een voorwerp met een dichtheid van \\(1000\\) kg/m³", "Zweeft"),
        ],
        "Vergelijk de dichtheid met die van water, 1000 kilogram per kubieke meter. Kleiner: het voorwerp drijft. Groter: het zinkt. Even groot: het zweeft.",
        kolommen=["Zinkt", "Zweeft", "Drijft"]),
    casus(
        "Op een wip zit Noor (\\(30\\) kg) op \\(2{,}0\\) m van het draaipunt. Aan de andere kant gaat Milan (\\(40\\) kg) zitten.",
        [
            inv("Op hoeveel meter van het draaipunt moet Milan zitten om de wip in evenwicht te brengen? Geef enkel het getal.",
                ["1,5", "1.5"],
                "Bij evenwicht zijn de momenten links en rechts gelijk: \\(30 \\cdot 2{,}0 = 40 \\cdot d\\), dus \\(d = 1{,}5\\) meter. De massa's mag je gebruiken omdat g aan beide kanten wegvalt."),
            mk("Milan schuift nu naar het uiteinde van de wip. Wat gebeurt er?",
               ["Zijn kant zakt naar beneden.", "De wip blijft in evenwicht.", "Noors kant zakt naar beneden.", "Het draaipunt schuift mee op."],
               0,
               "Een langere arm geeft een groter moment. Milans moment wordt groter dan dat van Noor, dus zijn kant zakt."),
        ],
    ),

    # Druk
    inv("Bij een hydraulische pers duw je met \\(200\\) N op een zuiger van \\(0{,}01\\) m². De grote zuiger heeft een oppervlakte van \\(0{,}5\\) m². Hoe groot is de kracht op de grote zuiger, in newton? Geef enkel het getal.",
        ["10000", "10 000", "10.000"],
        "De druk is overal gelijk: \\(200 / 0{,}01 = 20\\,000\\) pascal. Op de grote zuiger is de kracht \\(20\\,000 \\cdot 0{,}5 = 10\\,000\\) newton."),

    # Gassen
    tabel(
        "Welke grootheid blijft gelijk bij dit proces van een vaste hoeveelheid gas?",
        [
            ("isotherm", "Temperatuur"),
            ("isobaar", "Druk"),
            ("isochoor", "Volume"),
        ],
        "Iso betekent gelijk. Therm gaat over temperatuur, baar over druk en choor over volume (ruimte).",
        kolommen=["Druk", "Volume", "Temperatuur"]),
    inv("Een gas van \\(6{,}0\\) L bij \\(1{,}0\\) bar wordt bij gelijke temperatuur samengedrukt tot \\(3{,}0\\) bar. Hoeveel liter is het nieuwe volume? Geef enkel het getal.",
        ["2", "2,0", "2.0"],
        "Bij een isotherm proces is \\(p \\cdot V\\) constant: \\(1{,}0 \\cdot 6{,}0 = 3{,}0 \\cdot V\\), dus \\(V = 2{,}0\\) liter."),
    inv("Een gesloten fles gas staat op \\(2{,}0\\) bar bij \\(300\\) K. Je verwarmt ze tot \\(360\\) K. Hoeveel bar wordt de druk? Geef enkel het getal.",
        ["2,4", "2.4"],
        "Bij een constant volume is \\(p / T\\) constant: \\(2{,}0 / 300 = p / 360\\), dus \\(p = 2{,}4\\) bar. Reken altijd met kelvin."),

    # Arbeid en energie
    casus(
        "Een lift van \\(600\\) kg gaat in \\(30\\) s eenparig \\(20\\) m omhoog.",
        [
            inv("Hoeveel joule potentiële energie wint de lift? Geef enkel het getal.",
                ["117720", "117 720", "117.720"],
                "\\(E_{p} = m \\cdot g \\cdot h = 600 \\cdot 9{,}81 \\cdot 20 = 117\\,720\\) joule."),
            mk("Hoe groot is het nuttig vermogen van de lift, ongeveer?",
               ["\\(3{,}9\\) kW", "\\(39\\) kW", "\\(0{,}39\\) kW", "\\(118\\) kW"],
               0,
               "Vermogen is energie gedeeld door tijd: \\(117\\,720 / 30 = 3924\\) watt, ongeveer 3,9 kilowatt."),
            inv("De motor neemt in die tijd \\(150\\,000\\) J elektrische energie op. Wat is het rendement, in procent? Rond af op een geheel getal.",
                "78",
                "\\(\\eta = 117\\,720 / 150\\,000 = 0{,}78\\), dus 78 procent."),
        ],
    ),
    keuze(
        "Een fietser rijdt een helling af zonder te trappen. Zijn [[*potentiële|kinetische]] energie neemt af en zijn [[*kinetische|potentiële]] energie neemt toe. Door de wrijving wordt een deel [[*warmte|chemische energie]].",
        "Bij het dalen wordt potentiële energie omgezet in kinetische energie. De wrijving zet een deel om in warmte, die niet verdwijnt maar wel minder bruikbaar is."),

    # Warmte
    inv("Hoeveel joule warmte heb je nodig om \\(2{,}0\\) kg water van \\(20\\) °C tot \\(70\\) °C op te warmen? Gebruik \\(c = 4186\\) J/(kg.K). Geef enkel het getal.",
        ["418600", "418 600", "418.600"],
        "\\(Q = m \\cdot c \\cdot \\Delta T = 2{,}0 \\cdot 4186 \\cdot 50 = 418\\,600\\) joule."),
    koppel(
        "Hoe gebeurt het warmtetransport hier vooral?",
        [
            ["een metalen lepel in hete soep wordt warm", "geleiding"],
            ["warme lucht stijgt op boven een radiator", "convectie"],
            ["je voelt de warmte van de zon op je gezicht", "straling"],
        ],
        ["condensatie", "verdamping"],
        "Bij geleiding geven deeltjes de energie aan elkaar door. Bij convectie stroomt de warme stof zelf mee. Straling heeft geen stof nodig."),
    volgorde(
        "Zet de faseovergangen van ijs tot stoom in de juiste volgorde, als je ijs van \\(-10\\) °C blijft verwarmen.",
        ["het ijs warmt op tot 0 °C", "het ijs smelt", "het water warmt op tot 100 °C", "het water verdampt", "de stoom warmt verder op"],
        "Een opwarmingscurve wisselt schuine en horizontale stukken af. Bij elk horizontaal stuk gebeurt er een faseovergang."),

    # Elektriciteit
    casus(
        "Twee weerstanden van \\(30\\,\\Omega\\) en \\(60\\,\\Omega\\) worden op een spanning van \\(12\\) V aangesloten.",
        [
            inv("Ze staan in serie. Hoe groot is de stroomsterkte, in ampère? Geef enkel het getal.",
                ["0,13", "0.13", "0,133", "0.133"],
                "In serie tel je de weerstanden op: 90 ohm. \\(I = U / R = 12 / 90 \\approx 0{,}13\\) ampère."),
            inv("Ze staan nu parallel. Hoe groot is de substitutieweerstand, in ohm? Geef enkel het getal.",
                "20",
                "\\(1/R = 1/30 + 1/60 = 3/60\\), dus \\(R = 20\\) ohm."),
            tabel(
                "Klopt dit over de parallelschakeling?",
                [
                    ("Over elke weerstand staat \\(12\\) V.", J),
                    ("Door de weerstand van \\(30\\,\\Omega\\) loopt de grootste stroom.", J),
                    ("De totale stroom is kleiner dan in de serieschakeling.", F),
                ],
                "Bij een parallelschakeling staat de volle spanning over elke tak. De kleinste weerstand laat de grootste stroom door. De substitutieweerstand is kleiner, dus de totale stroom is groter dan in serie."),
        ],
    ),

    # Licht
    sorteer(
        "Welk beeld geeft een bolle lens?",
        ["Reëel en omgekeerd", "Virtueel en rechtop"],
        [
            ["het voorwerp staat verder dan het dubbele van de brandpuntsafstand", "Reëel en omgekeerd"],
            ["het voorwerp staat tussen het brandpunt en de lens", "Virtueel en rechtop"],
            ["het voorwerp staat tussen het brandpunt en het dubbele ervan", "Reëel en omgekeerd"],
            ["je gebruikt de lens als vergrootglas", "Virtueel en rechtop"],
        ],
        "Staat het voorwerp verder dan het brandpunt, dan krijg je een reëel, omgekeerd beeld op een scherm. Dichter dan het brandpunt krijg je een virtueel, rechtopstaand beeld: zo werkt een vergrootglas."),
    keuze(
        "Een lichtstraal gaat schuin van lucht naar water. Hij breekt [[*naar de normaal toe|van de normaal weg]], omdat licht in water [[*trager|sneller]] gaat.",
        "Gaat licht naar een middenstof waar het trager gaat, dan breekt het naar de normaal toe."),
    mk("Waarom zie je jezelf wel in een spiegel en niet in een wit blad papier?",
       ["De spiegel kaatst regelmatig terug, het papier kaatst diffuus.", "Wit papier slorpt al het licht op dat erop valt en kaatst niets terug.", "Een spiegel maakt zelf licht en een blad papier doet dat helemaal niet.", "Een spiegel breekt het licht naar de normaal toe en papier niet."],
       0,
       "Beide kaatsen licht terug. De spiegel doet dat regelmatig, zodat de stralen geordend blijven en je een beeld ziet. Papier is ruw en kaatst het licht in alle richtingen."),

    # Onderzoek
    open_("Je wil onderzoeken hoe de valtijd van een papieren muffinvormpje afhangt van het aantal vormpjes dat je in elkaar stapelt. Schrijf een onderzoeksvraag en een hypothese, en zeg wat je verandert, wat je meet en wat je gelijk houdt.",
          "Onderzoeksvraag: hoe hangt de valtijd af van het aantal gestapelde vormpjes? Hypothese: hoe meer vormpjes, hoe korter de valtijd. Ik verander het aantal vormpjes (1 tot 5). Ik meet de valtijd met een chronometer, drie keer per aantal. Ik houd de valhoogte, het soort vormpje en de plaats (geen tocht) gelijk.",
          "Een goede onderzoeksvraag is open, onderzoekbaar en haalbaar. Verander maar één grootheid tegelijk en herhaal je metingen om toevallige fouten te verkleinen."),
]
