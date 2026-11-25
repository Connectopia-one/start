# -*- coding: utf-8 -*-
"""Uitdaging Wiskunde 🚀 Boost doorstroom (25 november 2026), in de vormen
van het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen, van logica en reële getallen tot de parabool, goniometrie,
telproblemen en statistiek. Casussen, tabellen, keuzelijsten, koppelen,
sorteren, volgorde, rekenvragen, klikvragen op twee zelf getekende prenten
en een open vraag. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Wiskunde Boost doorstroom. Geen meerkeuze met meer dan één juist antwoord.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_wiskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Wiskunde"
BESTAND = "boost-wiskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/wiskunde-boost-uitdaging"
PARABOOL = "parabool-en-rechte.svg"
WOLK = "puntenwolk-studietijd.svg"
# klikvakken: zie maak_prenten_boost_wiskunde.py
TOP = [40.8, 18.9, 8.4, 10.9]
SNIJPUNT = [49.1, 29.6, 8.4, 10.9]
NUL_LINKS = [24.1, 61.7, 8.4, 10.9]
NUL_RECHTS = [57.4, 61.7, 8.4, 10.9]
UITSCHIETER = [62.0, 62.1, 6.0, 9.7]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Parabool en rechte (prent)
    klik("Bekijk de grafieken. Klik op de top van de parabool f.",
         PARABOOL, [TOP],
         "De top is het hoogste punt van deze bergparabool: \\((1, 4)\\). Daar gaat f van stijgen over naar dalen."),
    klik("Klik op het snijpunt van f en g dat niet op de x-as ligt.",
         PARABOOL, [SNIJPUNT],
         "f en g snijden elkaar in \\((-1, 0)\\) en in \\((2, 3)\\). Het punt \\((2, 3)\\) ligt niet op de x-as."),
    klik("Klik op een nulwaarde van f.",
         PARABOOL, [NUL_LINKS, NUL_RECHTS],
         "De nulwaarden zijn de x-waarden waar de parabool de x-as snijdt: \\(-1\\) en \\(3\\)."),
    met_prent(PARABOOL, mk(
        "Welk voorschrift hoort bij de parabool f?",
        ["\\(f(x) = -x^{2} + 2x + 3\\)", "\\(f(x) = x^{2} - 2x - 3\\)", "\\(f(x) = -x^{2} - 2x + 3\\)", "\\(f(x) = -x^{2} + 2x + 4\\)"],
        0,
        "Het is een bergparabool, dus de coëfficiënt van \\(x^{2}\\) is negatief. Ze snijdt de y-as in 3 en heeft als nulwaarden \\(-1\\) en \\(3\\): \\(-(x + 1)(x - 3) = -x^{2} + 2x + 3\\).")),
    met_prent(PARABOOL, tabel(
        "Klopt dit over de grafieken?",
        [
            ("De symmetrieas van f is de rechte \\(x = 1\\).", J),
            ("Het bereik van f is \\(\\left]-\\infty, 4\\right]\\).", J),
            ("f stijgt voor alle \\(x > 1\\).", F),
            ("De richtingscoëfficiënt van g is 2.", F),
        ],
        "De symmetrieas gaat door de top, \\(x = 1\\). De hoogste functiewaarde is 4, dus het bereik is \\(\\left]-\\infty, 4\\right]\\). Rechts van de top daalt f. g stijgt 1 eenheid per eenheid naar rechts: de richtingscoëfficiënt is 1.")),
    met_prent(PARABOOL, mk(
        "Voor welke x-waarden ligt de grafiek van f boven die van g?",
        ["\\(-1 < x < 2\\)", "\\(-1 < x < 3\\)", "\\(x < -1\\) of \\(x > 2\\)", "\\(0 < x < 2\\)"],
        0,
        "De grafieken snijden elkaar in \\(x = -1\\) en \\(x = 2\\). Daartussen ligt de parabool boven de rechte.")),

    # Puntenwolk (prent)
    klik("Bekijk de puntenwolk. Klik op de uitschieter.",
         WOLK, [UITSCHIETER],
         "Eén leerling studeerde 6 uur maar haalde maar 5 op 20. Dat punt ligt ver van de rest van de wolk: het is een uitschieter."),
    met_prent(WOLK, keuze(
        "De puntenwolk toont een [[*positief|negatief]] verband: wie langer studeert, haalt [[*meestal|altijd]] meer punten.",
        "De wolk loopt van linksonder naar rechtsboven: dat is een positief verband. Het geldt niet voor iedereen, zie de uitschieter, dus meestal en niet altijd.")),
    met_prent(WOLK, mk(
        "Wat mag je besluiten uit deze puntenwolk?",
        ["Er is een verband, maar dat bewijst nog geen oorzaak en gevolg.", "Elk extra uur studeren levert precies één punt meer op voor iedereen.", "De leerling met 5 op 20 heeft zeker gelogen over zijn studietijd.", "Studietijd en punten hebben niets met elkaar te maken in deze klas."],
        0,
        "Een puntenwolk toont dat twee grootheden samen veranderen. Een verband is nog geen bewijs van oorzaak en gevolg, en het geldt niet exact voor iedereen.")),

    # Logica
    tabel(
        "Vul de waarheidstabel van \\(p \\Rightarrow q\\) aan.",
        [
            ("p waar, q waar", "Waar"),
            ("p waar, q vals", "Vals"),
            ("p vals, q waar", "Waar"),
            ("p vals, q vals", "Waar"),
        ],
        "Een implicatie is enkel vals als de voorwaarde waar is en het gevolg vals. Is p vals, dan is de implicatie altijd waar.",
        kolommen=["Waar", "Vals"]),
    keuze(
        "Een alarm gaat af als de deur open is of als het raam open is. Daarvoor gebruik je een [[*OF-poort|EN-poort|NIET-poort]]. Een lamp die enkel brandt als twee schakelaars aan staan, werkt met een [[*EN-poort|OF-poort|NIET-poort]].",
        "Een OF-poort geeft 1 zodra minstens één ingang 1 is. Een EN-poort geeft enkel 1 als beide ingangen 1 zijn."),

    # Reële getallen
    sorteer(
        "Is dit getal rationaal of irrationaal?",
        ["Rationaal", "Irrationaal"],
        [
            ["\\(\\sqrt{2}\\)", "Irrationaal"],
            ["\\(0{,}333\\ldots\\)", "Rationaal"],
            ["\\(\\pi\\)", "Irrationaal"],
            ["\\(\\sqrt{16}\\)", "Rationaal"],
            ["\\(\\tfrac{22}{7}\\)", "Rationaal"],
            ["\\(\\sqrt{5}\\)", "Irrationaal"],
        ],
        "Een rationaal getal kan je als breuk schrijven: zijn decimale vorm stopt of herhaalt zich. \\(\\sqrt{16} = 4\\). \\(\\tfrac{22}{7}\\) is een breuk, ook al ligt het dicht bij \\(\\pi\\)."),
    tabel(
        "Reken uit zonder rekenmachine.",
        [
            ("\\(\\sqrt{3} \\cdot \\sqrt{27}\\)", "\\(9\\)"),
            ("\\((2^{3})^{2}\\)", "\\(64\\)"),
            ("\\(2^{-3}\\)", "\\(\\tfrac{1}{8}\\)"),
            ("\\(\\sqrt{50}\\)", "\\(5\\sqrt{2}\\)"),
        ],
        "\\(\\sqrt{3 \\cdot 27} = \\sqrt{81} = 9\\). Macht van een macht: exponenten vermenigvuldigen, \\(2^{6} = 64\\). Een negatieve exponent geeft het omgekeerde. \\(\\sqrt{50} = \\sqrt{25 \\cdot 2} = 5\\sqrt{2}\\).",
        kolommen=["\\(\\tfrac{1}{8}\\)", "\\(9\\)", "\\(64\\)", "\\(5\\sqrt{2}\\)"]),
    inv("Bereken \\(\\dfrac{2^{5} \\cdot 2^{3}}{2^{6}}\\). Geef enkel het getal.",
        "4",
        "Bij vermenigvuldigen tel je de exponenten op en bij delen trek je ze af: \\(2^{5 + 3 - 6} = 2^{2} = 4\\)."),

    # Notatie en intervallen
    mk("Hoe schrijf je \\(0{,}00052\\) in de wetenschappelijke notatie?",
       ["\\(5{,}2 \\cdot 10^{-4}\\)", "\\(5{,}2 \\cdot 10^{4}\\)", "\\(52 \\cdot 10^{-5}\\)", "\\(5{,}2 \\cdot 10^{-3}\\)"],
       0,
       "Vooraan staat een getal tussen 1 en 10. De komma schuift vier plaatsen naar rechts, dus de exponent is min vier."),
    mk("Welk interval hoort bij \\(-2 \\leq x < 5\\)?",
       ["\\(\\left[-2, 5\\right[\\)", "\\(\\left]-2, 5\\right]\\)", "\\(\\left[-2, 5\\right]\\)", "\\(\\left]-2, 5\\right[\\)"],
       0,
       "\\(-2\\) hoort erbij, dus de haak staat naar het getal toe. \\(5\\) hoort er niet bij, dus die haak staat van het getal weg."),

    # Ruimte en gelijkvormigheid
    inv("Twee driehoeken zijn gelijkvormig met factor \\(3\\). De kleine driehoek heeft een oppervlakte van \\(5\\) cm². Hoeveel cm² is de oppervlakte van de grote? Geef enkel het getal.",
        "45",
        "Lengtes worden 3 keer zo groot, oppervlaktes \\(3^{2} = 9\\) keer: \\(9 \\cdot 5 = 45\\) cm²."),
    tabel(
        "Klopt dit in de ruimte?",
        [
            ("Twee rechten die elkaar niet snijden, zijn altijd evenwijdig.", F),
            ("Drie punten die niet op één rechte liggen, bepalen precies één vlak.", J),
            ("Twee verschillende vlakken die elkaar snijden, hebben een rechte gemeen.", J),
            ("Een rechte en een vlak kunnen precies twee punten gemeen hebben.", F),
        ],
        "In de ruimte kunnen rechten ook kruisend zijn: niet evenwijdig en toch zonder snijpunt. Een rechte heeft met een vlak nul, één of oneindig veel punten gemeen, nooit precies twee."),

    # Pythagoras en goniometrie
    inv("Een ladder van \\(5\\) m staat tegen een muur. De voet staat \\(3\\) m van de muur. Hoe hoog reikt de ladder, in meter? Geef enkel het getal.",
        "4",
        "Pythagoras: \\(h^{2} + 3^{2} = 5^{2}\\), dus \\(h^{2} = 16\\) en \\(h = 4\\) meter."),
    inv("Een balk is \\(3\\) cm lang, \\(4\\) cm breed en \\(12\\) cm hoog. Hoe lang is de ruimtediagonaal, in cm? Geef enkel het getal.",
        "13",
        "Eerst de diagonaal van het grondvlak: \\(\\sqrt{9 + 16} = 5\\). Dan met de hoogte: \\(\\sqrt{25 + 144} = \\sqrt{169} = 13\\) cm."),
    mk("In een rechthoekige driehoek is de overstaande rechthoekszijde van hoek \\(\\alpha\\) \\(6\\) cm en de schuine zijde \\(12\\) cm. Hoe groot is \\(\\alpha\\)?",
       ["\\(30^\\circ\\)", "\\(45^\\circ\\)", "\\(60^\\circ\\)", "\\(27^\\circ\\)"],
       0,
       "\\(\\sin \\alpha = \\tfrac{6}{12} = 0{,}5\\), dus \\(\\alpha = 30^\\circ\\)."),
    inv("Een boom werpt een schaduw van \\(20\\) m. De zonnestralen maken een hoek van \\(35^\\circ\\) met de grond. Hoe hoog is de boom, in meter? Rond af op één decimaal.",
        ["14,0", "14", "14.0"],
        "\\(\\tan 35^\\circ = \\dfrac{h}{20}\\), dus \\(h = 20 \\cdot \\tan 35^\\circ \\approx 14{,}0\\) meter."),
    inv("In driehoek ABC is \\(b = 5\\), \\(c = 8\\) en de ingesloten hoek \\(\\hat{A} = 60^\\circ\\). Hoe lang is zijde a? Geef enkel het getal.",
        "7",
        "Cosinusregel: \\(a^{2} = 25 + 64 - 2 \\cdot 5 \\cdot 8 \\cdot \\cos 60^\\circ = 89 - 40 = 49\\), dus \\(a = 7\\)."),
    tabel(
        "Reken met vectoren.",
        [
            ("de norm van \\((6, 8)\\)", "\\(10\\)"),
            ("\\((1, 2) + (3, -1)\\)", "\\((4, 1)\\)"),
            ("\\(3 \\cdot (2, -1)\\)", "\\((6, -3)\\)"),
        ],
        "Norm: \\(\\sqrt{36 + 64} = 10\\). Som: coördinaat per coördinaat optellen. Een veelvoud: elke coördinaat vermenigvuldigen.",
        kolommen=["\\(10\\)", "\\((4, 1)\\)", "\\((6, -3)\\)"]),

    # Formules en vergelijkingen
    koppel(
        "Koppel elke formule aan de juiste omvorming.",
        [
            ["\\(v = \\dfrac{s}{t}\\), naar t", "\\(t = \\dfrac{s}{v}\\)"],
            ["\\(P = U \\cdot I\\), naar I", "\\(I = \\dfrac{P}{U}\\)"],
            ["\\(E = m \\cdot c^{2}\\), naar m", "\\(m = \\dfrac{E}{c^{2}}\\)"],
            ["\\(A = l \\cdot b\\), naar b", "\\(b = \\dfrac{A}{l}\\)"],
        ],
        ["\\(t = s \\cdot v\\)", "\\(m = E - c^{2}\\)"],
        "Je doet telkens dezelfde bewerking in beide leden tot de gevraagde grootheid alleen staat."),
    inv("Los op: \\(5(x - 2) = 3x + 4\\). Geef enkel de waarde van x.",
        "7",
        "\\(5x - 10 = 3x + 4\\), dus \\(2x = 14\\) en \\(x = 7\\)."),

    # Stelsels en tweedegraadsvergelijkingen
    casus(
        "Drie volwassenen en twee kinderen betalen samen \\(46\\) euro in de bioscoop. Twee volwassenen en vier kinderen betalen samen \\(44\\) euro.",
        [
            inv("Hoeveel euro kost een ticket voor een volwassene? Geef enkel het getal.",
                "12",
                "Stel a voor een volwassene en k voor een kind: \\(3a + 2k = 46\\) en \\(2a + 4k = 44\\). Uit de tweede: \\(a = 22 - 2k\\). Invullen: \\(66 - 6k + 2k = 46\\), dus \\(k = 5\\) en \\(a = 12\\)."),
            inv("Hoeveel euro kost een ticket voor een kind? Geef enkel het getal.",
                "5",
                "Met \\(a = 12\\) in \\(3a + 2k = 46\\): \\(36 + 2k = 46\\), dus \\(k = 5\\) euro."),
        ],
    ),
    tabel(
        "Gebruik de discriminant. Hoeveel reële oplossingen heeft elke vergelijking?",
        [
            ("\\(x^{2} - 4x + 4 = 0\\)", "Eén"),
            ("\\(x^{2} + x + 1 = 0\\)", "Geen"),
            ("\\(x^{2} - 5x + 6 = 0\\)", "Twee"),
        ],
        "Kijk naar de discriminant \\(b^{2} - 4ac\\): \\(16 - 16 = 0\\) geeft één oplossing, \\(1 - 4 < 0\\) geen, \\(25 - 24 > 0\\) twee.",
        kolommen=["Geen", "Eén", "Twee"]),
    mk("Wat zijn de oplossingen van \\(x^{2} - 7x + 10 = 0\\)?",
       ["\\(2\\) en \\(5\\)", "\\(-2\\) en \\(-5\\)", "\\(1\\) en \\(10\\)", "\\(-2\\) en \\(5\\)"],
       0,
       "Zoek twee getallen met product 10 en som 7: 2 en 5. Dus \\((x - 2)(x - 5) = 0\\)."),

    # Functies en de rechte
    mk("Welk voorschrift hoort bij de rechte door \\((1, 3)\\) en \\((3, 7)\\)?",
       ["\\(y = 2x + 1\\)", "\\(y = 2x + 3\\)", "\\(y = 4x - 1\\)", "\\(y = x + 2\\)"],
       0,
       "De richtingscoëfficiënt is \\(\\tfrac{7 - 3}{3 - 1} = 2\\). Met \\((1, 3)\\): \\(3 = 2 \\cdot 1 + q\\), dus \\(q = 1\\)."),
    casus(
        "Een taxi rekent \\(3\\) euro instap en \\(2\\) euro per gereden kilometer.",
        [
            inv("Hoeveel euro kost een rit van \\(12\\) km? Geef enkel het getal.",
                "27",
                "\\(K(x) = 2x + 3\\), dus \\(K(12) = 24 + 3 = 27\\) euro."),
            inv("Hoeveel kilometer kan je rijden met \\(35\\) euro? Geef enkel het getal.",
                "16",
                "\\(2x + 3 = 35\\), dus \\(2x = 32\\) en \\(x = 16\\) km."),
        ],
    ),

    # Tellen
    inv("Een restaurant heeft \\(3\\) voorgerechten, \\(4\\) hoofdgerechten en \\(2\\) desserts. Hoeveel verschillende menu's van drie gangen kan je kiezen? Geef enkel het getal.",
        "24",
        "Volgens de productregel: \\(3 \\cdot 4 \\cdot 2 = 24\\) menu's."),
    inv("Hoeveel pincodes van vier cijfers bestaan er als geen enkel cijfer twee keer mag voorkomen? Geef enkel het getal.",
        ["5040", "5 040", "5.040"],
        "Voor het eerste cijfer heb je 10 keuzes, dan 9, dan 8, dan 7: \\(10 \\cdot 9 \\cdot 8 \\cdot 7 = 5040\\)."),
    tabel(
        "In een klas van \\(30\\) leerlingen spelen er \\(17\\) voetbal, \\(12\\) tennis en \\(5\\) allebei. Vul aan.",
        [
            ("enkel voetbal", "12"),
            ("enkel tennis", "7"),
            ("geen van de twee", "6"),
        ],
        "Teken een venndiagram: in de doorsnede 5. Enkel voetbal: \\(17 - 5 = 12\\). Enkel tennis: \\(12 - 5 = 7\\). Samen \\(12 + 5 + 7 = 24\\), dus \\(30 - 24 = 6\\) erbuiten.",
        kolommen=["6", "7", "12"]),

    # Statistiek
    tabel(
        "Bekijk de reeks 3, 5, 5, 6, 8, 9, 13. Vul aan.",
        [
            ("het gemiddelde", "7"),
            ("de mediaan", "6"),
            ("de modus", "5"),
            ("de variatiebreedte", "10"),
        ],
        "Gemiddelde: \\(49 / 7 = 7\\). De mediaan is het middelste van de zeven getallen: 6. De modus komt het vaakst voor: 5. Variatiebreedte: \\(13 - 3 = 10\\).",
        kolommen=["5", "6", "7", "10"]),
    mk("In dezelfde reeks verandert 13 in 50. Welke centrummaat verandert dan?",
       ["het gemiddelde", "de mediaan van de reeks", "de modus van de reeks", "geen enkele centrummaat"],
       0,
       "De mediaan en de modus blijven 6 en 5. Het gemiddelde springt naar \\(86 / 7 \\approx 12{,}3\\): het is gevoelig voor uitschieters."),

    # Misleiding
    volgorde(
        "Zet de vier stappen om een wiskundig probleem aan te pakken in de juiste volgorde.",
        ["begrijp het probleem", "maak een plan", "voer het plan uit", "kijk terug en controleer"],
        "Eerst begrijp je wat er gevraagd is, dan kies je een aanpak, voer je die uit en kijk je na of het antwoord zinvol is."),

    # Open vraag
    open_("Abonnement A kost \\(10\\) euro per maand plus \\(0{,}10\\) euro per gebruikte MB. Abonnement B kost vast \\(20\\) euro per maand. Vanaf hoeveel MB per maand is B voordeliger? Schrijf je redenering op.",
          "Kost A: \\(10 + 0{,}10x\\). Kost B: \\(20\\). Gelijk als \\(10 + 0{,}10x = 20\\), dus \\(0{,}10x = 10\\) en \\(x = 100\\). Bij meer dan 100 MB is A duurder dan 20 euro, dus vanaf 100 MB (strikt: meer dan 100 MB) is B voordeliger.",
          "Een goed antwoord stelt de twee kostfuncties op, zoekt waar ze gelijk zijn en besluit wat er gebeurt bij meer gebruik."),
]
