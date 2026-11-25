# -*- coding: utf-8 -*-
"""Uitdaging Wiskunde 🚀 Boost dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Casussen, tabellen, keuzelijsten, koppelen, sorteren,
volgorde, rekenvragen, vier klikvragen op twee zelf getekende prenten en een
open vraag. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Wiskunde Boost dubbele finaliteit. Bij wiskunde: geen meerkeuze met meer
dan één juist antwoord.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_wiskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Wiskunde"
BESTAND = "boost-df-wiskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/wiskunde-boost-df-uitdaging"
KAARS = "kosten-opbrengst.svg"
BOX = "boxplot-toets.svg"
# klikvakken: zie maak_prenten_boost_df_wiskunde.py
BREAKEVEN = [48.5, 45.5, 9.0, 13.6]
VAST = [8.5, 57.3, 9.0, 13.6]
MEDIAAN = [56.6, 26.3, 3.6, 36.8]
DOOS = [45.8, 26.3, 21.0, 36.8]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Kaarsjes voor de kerstmarkt (prent)
    klik("Een klas maakt kaarsjes voor de kerstmarkt. Klik op het punt waar de klas precies geen winst en geen verlies maakt.",
         KAARS, [BREAKEVEN],
         r"Waar de kosten en de opbrengst even groot zijn, snijden de twee rechten elkaar: bij \(5\) kaarsjes, \(30\) euro. Dat is het break-evenpunt."),
    klik("Klik op het punt dat de vaste kosten toont: wat de klas al betaalt nog voor er één kaarsje gemaakt is.",
         KAARS, [VAST],
         r"Bij \(0\) kaarsjes zijn de kosten \(20\) euro. Dat is het snijpunt van de kostenrechte met de verticale as, de \(b\) in \(ax + b\)."),
    met_prent(KAARS, mk(
        r"Welk voorschrift hoort bij de kosten \(K\) voor \(x\) kaarsjes?",
        [r"\(K = 20x + 2\)", r"\(K = 2x + 20\)", r"\(K = 6x\)", r"\(K = 4x + 20\)"],
        1,
        r"De rechte start bij \(20\) euro en stijgt \(2\) euro per kaarsje (van \(20\) naar \(40\) over \(10\) kaarsjes). Dus \(K = 2x + 20\).")),
    met_prent(KAARS, inv(
        "Hoeveel euro winst maakt de klas als ze 10 kaarsjes verkoopt? Geef enkel het getal.",
        "20",
        r"Bij \(10\) kaarsjes is de opbrengst \(60\) euro en zijn de kosten \(40\) euro. Winst is opbrengst min kosten: \(20\) euro.")),
    met_prent(KAARS, keuze(
        "De klas maakt verlies zolang ze [[*minder dan 5|meer dan 5|precies 5]] kaarsjes verkoopt. Eén kaarsje brengt [[*6|2|20]] euro op.",
        r"Links van het snijpunt ligt de opbrengst onder de kosten: verlies. De opbrengstrechte gaat door \((0, 0)\) en \((10, 60)\), dus \(6\) euro per kaarsje.")),
    met_prent(KAARS, tabel(
        "Klopt dit over de grafiek van de kaarsjes?",
        [
            ("De opbrengst is recht evenredig met het aantal kaarsjes.", J),
            ("De kosten zijn recht evenredig met het aantal kaarsjes.", F),
            ("De richtingscoëfficiënt van de opbrengst is groter dan die van de kosten.", J),
        ],
        r"De opbrengstrechte gaat door de oorsprong, de kostenrechte niet: die start bij \(20\). De opbrengst stijgt \(6\) per kaarsje, de kosten maar \(2\).")),

    # Boxplot van een toets (prent)
    klik("Bekijk de boxplot van de toets. Klik op de mediaan.",
         BOX, [MEDIAAN],
         r"De lijn in de doos is de mediaan, hier \(12\): de helft van de klas scoorde \(12\) of minder, de andere helft \(12\) of meer."),
    klik("Klik op het deel van de boxplot dat de middelste helft van de scores bevat.",
         BOX, [DOOS],
         r"De doos loopt van het eerste kwartiel (\(9\)) tot het derde kwartiel (\(14\)). Daartussen ligt de middelste helft van de gegevens."),
    met_prent(BOX, inv(
        "Hoe groot is de interkwartielafstand? Geef enkel het getal.",
        "5",
        r"Interkwartielafstand is het derde kwartiel min het eerste: \(14 - 9 = 5\).")),
    met_prent(BOX, inv(
        "Hoe groot is de variatiebreedte van de scores? Geef enkel het getal.",
        "15",
        r"Variatiebreedte is de grootste min de kleinste waarde: \(19 - 4 = 15\).")),
    met_prent(BOX, tabel(
        "Klopt dit over de toets?",
        [
            ("Ongeveer een kwart van de klas haalde 9 of minder.", J),
            ("Het gemiddelde is zeker 12.", F),
            ("De scores tussen 9 en 12 liggen dichter bij elkaar dan die tussen 12 en 14.", F),
        ],
        r"Onder het eerste kwartiel zit een kwart van de klas. Een boxplot toont de mediaan, niet het gemiddelde. Tussen \(9\) en \(12\) zitten evenveel leerlingen als tussen \(12\) en \(14\), maar over een bredere strook: die scores liggen dus verder uit elkaar.")),

    # Casus: koopjes
    casus(
        "Tijdens de koopjes krijgt een jas van 80 euro eerst 25 % korting. Aan de kassa gaat er nog eens 10 % af op die nieuwe prijs.",
        [
            inv("Hoeveel euro betaal je uiteindelijk? Geef enkel het getal.",
                "54",
                r"Na \(25\,\%\) korting blijft \(75\,\%\): \(0{,}75 \cdot 80 = 60\) euro. Daarna blijft \(90\,\%\): \(0{,}9 \cdot 60 = 54\) euro."),
            mk("Hoeveel procent korting is dat samen?",
               [r"\(35\,\%\)", r"\(32{,}5\,\%\)", r"\(30\,\%\)", r"\(27{,}5\,\%\)"],
               1,
               r"Je betaalt \(0{,}75 \cdot 0{,}9 = 0{,}675\) of \(67{,}5\,\%\) van de prijs. De korting is dus \(32{,}5\,\%\), niet \(25 + 10 = 35\,\%\)."),
            inv("Een vriendin betaalde voor een andere jas 56 euro na 30 % korting. Wat was de prijs vóór de korting, in euro? Geef enkel het getal.",
                "80",
                r"\(56\) euro is \(70\,\%\) van de oude prijs. Terugrekenen: \(56 : 0{,}7 = 80\) euro."),
        ],
    ),

    # Casus: een ladder
    casus(
        "Een ladder van 5 meter staat tegen een muur. De voet van de ladder staat 1,4 meter van de muur.",
        [
            inv("Hoe hoog reikt de ladder tegen de muur, in meter? Geef enkel het getal.",
                ["4,8", "4.8"],
                r"De ladder is de schuine zijde. Pythagoras: \(\sqrt{5^{2} - 1{,}4^{2}} = \sqrt{25 - 1{,}96} = \sqrt{23{,}04} = 4{,}8\) meter."),
            keuze(
                "Om de hoek tussen de ladder en de grond te vinden, ken je de aanliggende zijde en de schuine zijde. Je gebruikt dus de [[*cosinus|sinus|tangens]].",
                "Cosinus is aanliggende zijde gedeeld door schuine zijde."),
            mk("Hoe groot is de hoek tussen de ladder en de grond ongeveer?",
               [r"\(16^{\circ}\)", r"\(52^{\circ}\)", r"\(74^{\circ}\)", r"\(84^{\circ}\)"],
               2,
               r"\(\cos\alpha = \tfrac{1{,}4}{5} = 0{,}28\), dus \(\alpha \approx 74^{\circ}\). Een steile ladder, dat klopt met het beeld."),
        ],
    ),

    # Casus: tellen
    casus(
        "Het restaurant van de school biedt 3 voorgerechten, 4 hoofdgerechten en 2 desserts aan. In de klas van 30 leerlingen spelen er 18 voetbal, 12 tennis en 5 allebei.",
        [
            inv("Hoeveel verschillende menu's met één voorgerecht, één hoofdgerecht en één dessert kan je kiezen? Geef enkel het getal.",
                "24",
                r"Elke keuze vermenigvuldigt het aantal mogelijkheden: \(3 \cdot 4 \cdot 2 = 24\)."),
            inv("Hoeveel leerlingen van de klas spelen geen van beide sporten? Geef enkel het getal.",
                "5",
                r"Voetbal of tennis: \(18 + 12 - 5 = 25\) leerlingen, want de \(5\) die allebei spelen tel je anders dubbel. Geen van beide: \(30 - 25 = 5\)."),
            mk("Welk hulpmiddel past het best bij de vraag over de sporten?",
               ["een boomdiagram met alle paden", "een venndiagram", "een lijndiagram in de tijd", "een tabel met klassenmiddens"],
               1,
               "Twee groepen die elkaar overlappen, teken je het handigst als twee kringen. Begin bij de doorsnede."),
        ],
    ),

    # Casus: een misleidende grafiek
    casus(
        "Een gsm-merk toont in een reclame een staafdiagram. De verticale as begint bij 95 %. De staaf van het eigen merk (98 %) is vier keer zo hoog als die van de concurrent (96 %). Eronder staat: 'Het aandeel klanten dat meteen een tweede toestel koopt, steeg van 4 % naar 6 %!'",
        [
            tabel(
                "Klopt dit over de reclame?",
                [
                    ("Het verschil tussen de staven lijkt veel groter dan het is.", J),
                    ("Het echte verschil is 2 procentpunt.", J),
                    ("Een as die bij 95 % begint, is altijd fout.", F),
                ],
                "Het echte verschil is 98 min 96, dus 2 procentpunt. Een as mag ergens anders beginnen, maar dan moet dat duidelijk aangegeven zijn, anders misleidt het beeld."),
            mk("Van 4 % naar 6 %: met hoeveel procent is dat aandeel gestegen?",
               [r"\(2\,\%\)", r"\(20\,\%\)", r"\(50\,\%\)", r"\(150\,\%\)"],
               2,
               r"De stijging is \(2\) procentpunt. Ten opzichte van de \(4\) van het begin is dat \(\tfrac{2}{4} = 50\,\%\) meer."),
            open_("Welke twee vragen stel je best bij deze reclame voor je ze gelooft?",
                  "Hoeveel mensen werden er bevraagd en door wie? Waar begint de schaal van de as, en hoe groot is het echte verschil?",
                  "Kijk altijd naar de bron, de grootte van de groep en de assen van de grafiek."),
        ],
    ),

    # Losse vragen door elkaar
    sorteer(
        "Is het getal rationaal of irrationaal?",
        ["Rationaal", "Irrationaal"],
        [
            [r"\(\sqrt{2}\)", "Irrationaal"],
            [r"\(\pi\)", "Irrationaal"],
            [r"\(0{,}75\)", "Rationaal"],
            [r"\(\sqrt{16}\)", "Rationaal"],
            [r"\(\tfrac{1}{3}\)", "Rationaal"],
        ],
        r"\(\sqrt{16} = 4\) en \(0{,}75 = \tfrac{3}{4}\) zijn breuken. \(\tfrac{1}{3}\) is repeterend en dus ook rationaal. \(\sqrt{2}\) en \(\pi\) zijn onbegrensd en niet-repeterend."),
    volgorde(
        "Rangschik deze vijf getallen van klein naar groot.",
        [r"\(-2\)", r"\(-\sqrt{3}\)", r"\(-1{,}5\)", r"\(\tfrac{1}{4}\)", r"\(\sqrt{2}\)"],
        r"\(-\sqrt{3} \approx -1{,}73\) ligt tussen \(-2\) en \(-1{,}5\). \(\sqrt{2} \approx 1{,}41\) is groter dan \(0{,}25\)."),
    inv("Vereenvoudig \\(\\sqrt{50}\\). Typ bijvoorbeeld 2√5 of 2 wortel 5.",
        ["5√2", "5 √2", "5 wortel 2", "5wortel2", "5 wortel2"],
        r"\(\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}\)."),
    mk(r"Hoeveel is \(\left(2a^{2}\right)^{3}\)?",
       [r"\(6a^{5}\)", r"\(8a^{6}\)", r"\(2a^{6}\)", r"\(8a^{5}\)"],
       1,
       r"Elke factor gaat tot de derde: \(2^{3} = 8\) en \(\left(a^{2}\right)^{3} = a^{6}\)."),
    mk(r"Welk interval hoort bij alle \(x\) met \(-1 < x \leq 3\)?",
       [r"\(\left[-1, 3\right[\)", r"\(\left]-1, 3\right]\)", r"\(\left[-1, 3\right]\)", r"\(\left]-1, 3\right[\)"],
       1,
       r"\(-1\) hoort er niet bij: haakje naar buiten. \(3\) hoort er wel bij: haakje naar binnen."),
    inv(r"Schrijf \(0{,}00042\) als \(4{,}2 \cdot 10^{n}\). Hoeveel is \(n\)? Geef enkel het getal.",
        "-4",
        r"De komma schuift vier plaatsen naar rechts, dus \(0{,}00042 = 4{,}2 \cdot 10^{-4}\)."),
    inv(r"Los op: \(3(x - 2) = x + 8\). Hoeveel is \(x\)? Geef enkel het getal.",
        "7",
        r"Haakjes uitwerken: \(3x - 6 = x + 8\). Dan \(2x = 14\), dus \(x = 7\). Controle: \(3 \cdot 5 = 15\) en \(7 + 8 = 15\)."),
    mk(r"Wat is de oplossing van \(-2x + 6 \geq 0\)?",
       [r"alle \(x \geq 3\)", r"alle \(x \leq 3\)", r"alle \(x \leq -3\)", r"alle \(x \geq -3\)"],
       1,
       r"\(-2x \geq -6\). Delen door \(-2\) draait het teken om: \(x \leq 3\)."),
    mk(r"Het vermogen van een toestel is \(P = U \cdot I\). Hoe druk je de stroomsterkte \(I\) uit?",
       [r"\(I = P \cdot U\)", r"\(I = \dfrac{U}{P}\)", r"\(I = \dfrac{P}{U}\)", r"\(I = P - U\)"],
       2,
       r"Deel beide leden door \(U\): \(\dfrac{P}{U} = I\)."),
    inv("Drie volwassenen en twee kinderen betalen samen 39 euro voor de zwemkaart. Eén volwassene en één kind betalen samen 15 euro. Hoeveel euro kost een kaart voor een volwassene? Geef enkel het getal.",
        "9",
        r"Stelsel: \(3v + 2k = 39\) en \(v + k = 15\). Uit de tweede: \(k = 15 - v\). Invullen: \(3v + 30 - 2v = 39\), dus \(v = 9\) en \(k = 6\)."),
    mk(r"Wat is de richtingscoëfficiënt van de rechte door \((-2, 7)\) en \((2, -1)\)?",
       [r"\(2\)", r"\(-\tfrac{1}{2}\)", r"\(-2\)", r"\(4\)"],
       2,
       r"\(\dfrac{-1 - 7}{2 - (-2)} = \dfrac{-8}{4} = -2\). De rechte daalt, dus de richtingscoëfficiënt is negatief."),
    tabel(
        r"Klopt dit over de functie \(f(x) = 2x - 6\)?",
        [
            (r"De nulwaarde is \(3\).", J),
            (r"\(f(0)\) is negatief.", J),
            (r"De functie is positief voor alle \(x < 3\).", F),
            ("De functie stijgt.", J),
        ],
        r"\(2x - 6 = 0\) geeft \(x = 3\). \(f(0) = -6\). Omdat de functie stijgt, is ze positief rechts van \(3\), niet links."),
    inv("Twee driehoeken zijn gelijkvormig met factor 3. De kleine heeft een oppervlakte van 4 cm². Hoeveel cm² is de grote? Geef enkel het getal.",
        "36",
        r"Bij factor \(3\) wordt de oppervlakte \(3^{2} = 9\) keer zo groot: \(9 \cdot 4 = 36\) cm²."),
    tabel(
        "Klopt dit over rechten en vlakken in een balk?",
        [
            ("Twee ribben die elkaar niet snijden en niet in één vlak liggen, zijn kruisend.", J),
            ("Een balk heeft acht ribben.", F),
            ("Twee overstaande zijvlakken van een balk zijn evenwijdig.", J),
        ],
        "Een balk heeft twaalf ribben en zes zijvlakken. Overstaande zijvlakken snijden elkaar nooit."),
    inv("Na vier toetsen heeft Noor gemiddeld 12 op 20. Hoeveel moet ze op de vijfde toets halen om gemiddeld 13 te hebben? Geef enkel het getal.",
        "17",
        r"Nu heeft ze samen \(4 \cdot 12 = 48\) punten. Voor gemiddeld \(13\) over vijf toetsen heeft ze \(5 \cdot 13 = 65\) nodig: \(65 - 48 = 17\)."),
    koppel(
        "Welk diagram past het best bij elke vraag?",
        [
            ["Hoe veranderde de temperatuur elke dag van de maand?", "lijndiagram"],
            ["Welk deel van het budget gaat naar huur, eten en vrije tijd?", "cirkeldiagram"],
            ["Hoe zijn de lengtes van 200 leerlingen over klassen verdeeld?", "histogram"],
            ["Hoe ver liggen de scores van twee klassen uit elkaar?", "boxplot"],
        ],
        ["venndiagram", "boomdiagram"],
        "Een lijndiagram toont een verloop in de tijd, een cirkeldiagram delen van een geheel, een histogram klassen van numerieke gegevens en een boxplot de spreiding."),
    open_("In een bedrijf verdienen vier mensen 2000 euro per maand en de baas 12 000 euro. Leg uit waarom het gemiddelde loon hier een misleidend beeld geeft en welk getal beter past.",
          "Het gemiddelde is 4000 euro, maar niemand behalve de baas verdient zoveel. De uitschieter trekt het gemiddelde omhoog. De mediaan, 2000 euro, toont beter wat een gewone werknemer verdient.",
          "Het gemiddelde is gevoelig voor uitschieters, de mediaan niet."),
]
