# -*- coding: utf-8 -*-
"""Uitdaging Wiskunde basis 🌍 Beyond doorstroom (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die de gemeenschappelijke
hoofdstukken door elkaar halen (machten en logaritmen, functies,
tweedegraads, exponentieel, sinus, afgeleiden, rijen, kansen, steekproeven en
de normale verdeling). De extra hoofdstukken voor bedrijfswetenschappen
blijven erbuiten, zodat iedereen de uitdaging kan maken. Een sinusgrafiek en
een kansboom om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde, rekenvragen en een korte uitleg in eigen woorden.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_wiskunde_basis.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Wiskunde basis"
BESTAND = "beyond-wiskunde-basis-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/wiskunde-basis-beyond-uitdaging"
SINUS = "sinus-grafiek.svg"
BOOM = "kansboom-bus.svg"

# klikvakken uit maak_prenten_beyond_wiskunde_basis.py
TOP = [24.9, 25.2, 6.8, 11.0]
DAL = [59.4, 70.3, 6.8, 11.0]
YAS = [7.6, 47.7, 6.8, 11.0]
NUL1 = [47.9, 59.0, 6.8, 11.0]
NUL2 = [71.0, 59.0, 6.8, 11.0]
EIND = {1: [71.2, 12.0, 25.6, 10.7], 2: [71.2, 37.0, 25.6, 10.7],
        3: [71.2, 58.4, 25.6, 10.7], 4: [71.2, 83.4, 25.6, 10.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Sinusgrafiek (prent)
    klik("Klik op het punt waar de grafiek van \\(f(x) = 2\\sin x + 1\\) haar grootste waarde bereikt.",
         SINUS, [TOP],
         "\\(\\sin x\\) is maximaal 1 bij \\(x = \\tfrac{\\pi}{2}\\). Dan is \\(f(x) = 2 \\cdot 1 + 1 = 3\\)."),
    klik("Klik op de nulwaarde van f die tussen \\(\\pi\\) en \\(\\tfrac{3\\pi}{2}\\) ligt.",
         SINUS, [NUL1],
         "\\(2\\sin x + 1 = 0\\) geeft \\(\\sin x = -\\tfrac{1}{2}\\). Tussen \\(\\pi\\) en \\(\\tfrac{3\\pi}{2}\\) is dat \\(x = \\tfrac{7\\pi}{6}\\)."),
    klik("Klik op het punt waar de sinusgrafiek de verticale as snijdt.",
         SINUS, [YAS],
         "Bij \\(x = 0\\) is \\(f(0) = 2 \\cdot 0 + 1 = 1\\): het punt \\((0, 1)\\)."),
    met_prent(SINUS, tabel(
        "Lees af en reken na voor \\(f(x) = 2\\sin x + 1\\).",
        [
            ("Amplitude", "2"),
            ("Evenwichtslijn y =", "1"),
            ("Minimum van f", "-1"),
            ("Maximum van f", "3"),
        ],
        "De amplitude is de factor voor de sinus: 2. De grafiek schommelt rond \\(y = 1\\), van \\(1 - 2 = -1\\) tot \\(1 + 2 = 3\\).",
        kolommen=["-1", "1", "2", "3"])),
    met_prent(SINUS, keuze(
        "De periode van f is [[*\\(2\\pi\\)|\\(\\pi\\)|\\(4\\pi\\)]]. Op het interval \\(\\left(\\tfrac{\\pi}{2}, \\tfrac{3\\pi}{2}\\right)\\) is f [[*dalend|stijgend|constant]].",
        "Een factor voor x ontbreekt, dus de periode blijft \\(2\\pi\\). Van de top bij \\(\\tfrac{\\pi}{2}\\) tot het dal bij \\(\\tfrac{3\\pi}{2}\\) daalt de grafiek.")),

    # Kansboom (prent)
    klik("Bekijk de kansboom. Klik op de uitkomst 'de bus was te laat, maar je was toch op tijd op school'.",
         BOOM, [EIND[2]],
         "Volg de tak 'bus te laat' en daarna 'op tijd op school'. Die kans is \\(0{,}2 \\cdot 0{,}1 = 0{,}02\\)."),
    klik("Klik op de uitkomst met de grootste kans.",
         BOOM, [EIND[4]],
         "Bus op tijd en op tijd op school: \\(0{,}8 \\cdot 0{,}9 = 0{,}72\\). Dat is veel groter dan de andere drie uitkomsten."),
    met_prent(BOOM, inv(
        "Hoe groot is de kans dat je te laat op school komt? Geef een decimaal getal.",
        ["0,26", "0.26"],
        "Tel de twee takken op: \\(0{,}2 \\cdot 0{,}9 + 0{,}8 \\cdot 0{,}1 = 0{,}18 + 0{,}08 = 0{,}26\\).")),
    met_prent(BOOM, mk(
        "Je komt te laat op school. Hoe groot is de kans dat de bus te laat was? Rond af op twee decimalen.",
        ["0,69", "0,18", "0,9", "0,26"],
        0,
        "Voorwaardelijke kans: \\(\\dfrac{0{,}18}{0{,}26} \\approx 0{,}69\\).")),

    # Machten, wortels en logaritmen
    tabel(
        "Bereken zonder rekenmachine.",
        [
            ("\\(\\log_{2} 32\\)", "5"),
            ("\\(8^{\\frac{2}{3}}\\)", "4"),
            ("\\(\\log 1000\\)", "3"),
            ("\\(\\sqrt[3]{-8}\\)", "-2"),
        ],
        "\\(2^{5} = 32\\), \\(8^{\\frac{2}{3}} = (\\sqrt[3]{8})^{2} = 2^{2} = 4\\), \\(10^{3} = 1000\\) en \\((-2)^{3} = -8\\).",
        kolommen=["-2", "3", "4", "5"]),
    inv("Los op: \\(3^{x} = 81\\). Geef x.",
        ["4"],
        "\\(81 = 3^{4}\\), dus \\(x = 4\\)."),
    keuze(
        "\\(\\log a + \\log b\\) is gelijk aan [[*\\(\\log(ab)\\)|\\(\\log(a+b)\\)|\\(\\log a \\cdot \\log b\\)]]. Het domein van \\(f(x) = \\log x\\) is [[*\\(x > 0\\)|\\(x \\geq 0\\)|alle reële getallen]].",
        "De som van twee logaritmen is de logaritme van het product. Je kan enkel de logaritme nemen van een strikt positief getal."),

    # Tweedegraadsfuncties en -vergelijkingen
    tabel(
        "Bekijk \\(f(x) = -2(x - 1)^{2} + 8\\).",
        [
            ("x-coördinaat van de top", "1"),
            ("y-coördinaat van de top", "8"),
            ("Grootste nulwaarde", "3"),
            ("Kleinste nulwaarde", "-1"),
        ],
        "De top staat in de vorm: \\((1, 8)\\). Nulwaarden: \\((x - 1)^{2} = 4\\), dus \\(x - 1 = \\pm 2\\): \\(x = 3\\) of \\(x = -1\\).",
        kolommen=["-1", "1", "3", "8"]),
    sorteer(
        "Hoeveel reële oplossingen heeft elke tweedegraadsvergelijking?",
        ["Twee", "Eén", "Geen"],
        [
            ["\\(x^{2} - 5x + 6 = 0\\)", "Twee"],
            ["\\(x^{2} + 2x + 5 = 0\\)", "Geen"],
            ["\\(x^{2} - 6x + 9 = 0\\)", "Eén"],
            ["\\(2x^{2} - 8 = 0\\)", "Twee"],
            ["\\(x^{2} + 4 = 0\\)", "Geen"],
        ],
        "Bekijk de discriminant \\(D = b^{2} - 4ac\\): positief geeft twee oplossingen, nul één, negatief geen."),
    inv("Los op: \\(x^{2} - 5x + 6 = 0\\). Geef de grootste oplossing.",
        ["3"],
        "\\(x^{2} - 5x + 6 = (x - 2)(x - 3)\\), dus \\(x = 2\\) of \\(x = 3\\)."),
    keuze(
        "Bij \\(f(x) = ax^{2} + bx + c\\) met \\(a < 0\\) is de parabool een [[*bergparabool|dalparabool]] en heeft f een [[*maximum|minimum]].",
        "Een negatieve a draait de parabool om: de top is het hoogste punt."),

    # Grafisch onderzoek en vergelijkingen grafisch
    tabel(
        "Klopt dit voor \\(f(x) = x^{2} - 4\\)?",
        [
            ("f is even: de grafiek is symmetrisch t.o.v. de y-as.", J),
            ("f is stijgend op \\(\\left]-\\infty, 0\\right]\\).", F),
            ("Het bereik van f is \\(\\left[-4, +\\infty\\right[\\).", J),
            ("f heeft een maximum in \\(x = 0\\).", F),
        ],
        "\\(f(-x) = f(x)\\), dus f is even. Links van 0 daalt f, rechts stijgt f. De kleinste waarde is \\(-4\\): een minimum."),
    mk("De grafieken van \\(f(x) = x^{2}\\) en \\(g(x) = x + 2\\) snijden elkaar. Wat zijn de x-waarden van de snijpunten?",
       ["\\(x = -1\\) en \\(x = 2\\)", "\\(x = 1\\) en \\(x = -2\\)", "\\(x = -1\\) en \\(x = -2\\)", "\\(x = -2\\) en \\(x = 2\\)"],
       0,
       "\\(x^{2} = x + 2\\) geeft \\(x^{2} - x - 2 = 0\\), dus \\((x - 2)(x + 1) = 0\\)."),

    # Exponentiële groei
    tabel(
        "Welke groeifactor per jaar hoort erbij?",
        [
            ("Een bedrag groeit met 3 % per jaar.", "1,03"),
            ("Een auto verliest 20 % van zijn waarde per jaar.", "0,8"),
            ("Een bevolking verdubbelt elk jaar.", "2"),
        ],
        "Groei met p % geeft factor \\(1 + \\tfrac{p}{100}\\), afname met p % geeft \\(1 - \\tfrac{p}{100}\\).",
        kolommen=["0,8", "1,03", "2"]),
    inv("Je zet 500 euro op een rekening met 3 % rente per jaar (samengestelde intrest). Hoeveel staat er na 2 jaar op? Rond af op de cent, enkel het getal.",
        ["530,45", "530.45"],
        "\\(500 \\cdot 1{,}03^{2} = 500 \\cdot 1{,}0609 = 530{,}45\\) euro."),
    mk("Een hoeveelheid groeit met 5 % per jaar. Na ongeveer hoeveel jaar is ze verdubbeld?",
       ["Ongeveer 14 jaar", "Ongeveer 20 jaar", "Ongeveer 10 jaar", "Ongeveer 100 jaar"],
       0,
       "\\(1{,}05^{t} = 2\\) geeft \\(t = \\dfrac{\\log 2}{\\log 1{,}05} \\approx 14{,}2\\) jaar."),
    keuze(
        "De grafiek van \\(f(x) = 3 \\cdot 0{,}5^{x}\\) is [[*dalend|stijgend]] en snijdt de y-as in [[*\\(y = 3\\)|\\(y = 0{,}5\\)|\\(y = 1\\)]].",
        "Een groeifactor tussen 0 en 1 geeft een dalende functie. Bij \\(x = 0\\) is \\(f(0) = 3 \\cdot 1 = 3\\)."),

    # Afgeleiden
    inv("Hoe steil is de grafiek van \\(f(x) = x^{3} - 4x\\) in \\(x = 2\\)? Geef de richtingscoëfficiënt van de raaklijn.",
        ["8"],
        "\\(f'(x) = 3x^{2} - 4\\), dus \\(f'(2) = 12 - 4 = 8\\)."),
    mk("Wat is de vergelijking van de raaklijn aan de grafiek van \\(f(x) = x^{3} - 4x\\) in \\(x = 2\\)?",
       ["\\(y = 8x - 16\\)", "\\(y = 8x\\)", "\\(y = 8x + 16\\)", "\\(y = 12x - 24\\)"],
       0,
       "\\(f(2) = 8 - 8 = 0\\) en \\(f'(2) = 8\\). De raaklijn door \\((2, 0)\\) is \\(y = 8(x - 2) = 8x - 16\\)."),
    tabel(
        "Wat zegt de afgeleide over de grafiek van f?",
        [
            ("\\(f'(a) > 0\\)", "f stijgt in a"),
            ("\\(f'(a) < 0\\)", "f daalt in a"),
            ("\\(f'(a) = 0\\) en f' wisselt van + naar −", "f heeft een maximum in a"),
        ],
        "Het teken van de afgeleide geeft aan of de functie stijgt of daalt. Waar de afgeleide van plus naar min gaat, ligt een maximum.",
        kolommen=["f stijgt in a", "f daalt in a", "f heeft een maximum in a"]),

    # Rijen
    tabel(
        "Een rekenkundige rij heeft \\(u_{1} = 3\\) en verschil \\(v = 4\\).",
        [
            ("\\(u_{5}\\)", "19"),
            ("\\(u_{10}\\)", "39"),
            ("Som van de eerste 10 termen", "210"),
        ],
        "\\(u_{5} = 3 + 4 \\cdot 4 = 19\\) en \\(u_{10} = 3 + 9 \\cdot 4 = 39\\). De som is \\(\\tfrac{10}{2}(3 + 39) = 210\\).",
        kolommen=["19", "39", "210"]),
    inv("Een meetkundige rij heeft \\(u_{1} = 2\\) en reden \\(q = 3\\). Bereken \\(u_{5}\\).",
        ["162"],
        "\\(u_{5} = 2 \\cdot 3^{4} = 2 \\cdot 81 = 162\\)."),
    sorteer(
        "Is de rij rekenkundig of meetkundig?",
        ["Rekenkundig", "Meetkundig"],
        [
            ["5, 8, 11, 14, ...", "Rekenkundig"],
            ["3, 6, 12, 24, ...", "Meetkundig"],
            ["100, 90, 80, 70, ...", "Rekenkundig"],
            ["81, 27, 9, 3, ...", "Meetkundig"],
        ],
        "Telkens hetzelfde getal erbij of eraf: rekenkundig. Telkens met hetzelfde getal vermenigvuldigen: meetkundig."),

    # Kansrekenen
    tabel(
        "In een klas van 25: 15 doen aan sport, 10 spelen een instrument, 6 doen allebei. Bereken.",
        [
            ("Aantal leerlingen dat sport of een instrument speelt (of beide)", "19"),
            ("Aantal leerlingen dat geen van beide doet", "6"),
            ("Aantal leerlingen dat enkel sport", "9"),
        ],
        "Somregel: \\(15 + 10 - 6 = 19\\). Dan doen \\(25 - 19 = 6\\) leerlingen geen van beide. Enkel sport: \\(15 - 6 = 9\\).",
        kolommen=["6", "9", "19"]),
    keuze(
        "Twee gebeurtenissen A en B zijn onafhankelijk als \\(P(A \\cap B)\\) [[*gelijk is aan|groter is dan]] \\(P(A) \\cdot P(B)\\).",
        "Onafhankelijk betekent dat het optreden van de ene de kans op de andere niet verandert: \\(P(A \\cap B) = P(A) \\cdot P(B)\\)."),

    # Steekproeven en normale verdeling
    mk("Een onderzoek stelt vast: leerlingen die meer ontbijten, halen betere punten. Welk besluit mag je trekken?",
       ["Er is samenhang, maar ontbijt is daarom nog niet de oorzaak.", "Ontbijten zorgt er altijd en zeker voor dat je betere punten haalt.", "Betere punten zorgen ervoor dat leerlingen meer ontbijten.", "De steekproef moet fout zijn, want er is geen echt verband."],
       0,
       "Samenhang is geen oorzakelijk verband. Een derde factor, zoals een regelmatig leven, kan allebei verklaren."),
    tabel(
        "IQ-scores zijn normaal verdeeld met \\(\\mu = 100\\) en \\(\\sigma = 15\\). Hoeveel procent ligt ongeveer in het interval?",
        [
            ("Tussen 85 en 115", "68 %"),
            ("Tussen 70 en 130", "95 %"),
            ("Boven 130", "2,5 %"),
        ],
        "Eén en twee standaardafwijkingen rond het gemiddelde bevatten 68 % en 95 %. Boven \\(\\mu + 2\\sigma\\) ligt de helft van de overige 5 %.",
        kolommen=["2,5 %", "68 %", "95 %"]),
    inv("Een IQ van 121 met \\(\\mu = 100\\) en \\(\\sigma = 15\\): bereken de z-score.",
        ["1,4", "1.4"],
        "\\(z = \\dfrac{121 - 100}{15} = \\dfrac{21}{15} = 1{,}4\\)."),

    # Gemengd
    koppel(
        "Koppel de functie aan haar soort.",
        [
            ["\\(f(x) = 2^{x}\\)", "exponentiële functie"],
            ["\\(f(x) = x^{2} - 1\\)", "tweedegraadsfunctie"],
            ["\\(f(x) = \\sin x\\)", "goniometrische functie"],
            ["\\(f(x) = \\log x\\)", "logaritmische functie"],
        ],
        ["eerstegraadsfunctie"],
        "Een variabele in de exponent is exponentieel, een kwadraat tweedegraads, sinus goniometrisch en log logaritmisch."),
    volgorde(
        "Rangschik van klein naar groot.",
        ["\\(\\log 0{,}1\\)", "\\(\\sin 0\\)", "\\(2^{-1}\\)", "\\(\\sqrt{2}\\)", "\\(\\log_{2} 8\\)"],
        "\\(\\log 0{,}1 = -1\\), \\(\\sin 0 = 0\\), \\(2^{-1} = 0{,}5\\), \\(\\sqrt{2} \\approx 1{,}41\\) en \\(\\log_{2} 8 = 3\\)."),
    sleep(
        "De afgeleide van \\(x^{n}\\) is [[\\(nx^{n-1}\\)]]. De afgeleide van een constante is [[0]].",
        ["\\(x^{n+1}\\)", "1"],
        "Machtsregel: exponent naar voren, exponent min één. Een constante verandert niet, dus haar afgeleide is 0."),
    mk("Voor welke x is \\(\\sin x = 1\\) op het interval \\(\\left[0, 2\\pi\\right]\\)?",
       ["\\(x = \\tfrac{\\pi}{2}\\)", "\\(x = \\pi\\)", "\\(x = 0\\)", "\\(x = \\tfrac{3\\pi}{2}\\)"],
       0,
       "Op de goniometrische cirkel is de sinus de y-coördinaat. Die is 1 bovenaan, bij \\(\\tfrac{\\pi}{2}\\)."),

    inv("Los op: \\(\\log_{2}(x + 1) = 3\\). Geef x.",
        ["7"],
        "\\(x + 1 = 2^{3} = 8\\), dus \\(x = 7\\)."),
    tabel(
        "Klopt dit over de goniometrische cirkel?",
        [
            ("\\(\\cos 0 = 1\\)", J),
            ("\\(\\sin \\pi = 1\\)", F),
            ("\\(\\sin^{2} x + \\cos^{2} x = 1\\) voor elke x", J),
            ("\\(\\pi\\) radialen is hetzelfde als 90 graden.", F),
        ],
        "Op de eenheidscirkel is \\(\\cos 0 = 1\\) en \\(\\sin \\pi = 0\\). De grondformule geldt altijd. \\(\\pi\\) radialen is 180 graden."),

    # Uitleg
    open_("Leg in 3 à 5 zinnen uit hoe je met de discriminant kan zien hoeveel nulwaarden een tweedegraadsfunctie heeft, en wat dat betekent voor de grafiek.",
          "Je berekent \\(D = b^{2} - 4ac\\). Is D positief, dan zijn er twee nulwaarden en snijdt de parabool de x-as in twee punten. Is D nul, dan is er één nulwaarde en raakt de top de x-as. Is D negatief, dan zijn er geen reële nulwaarden en ligt de parabool volledig boven of onder de x-as.",
          "Een goed antwoord geeft de formule van de discriminant en koppelt elk teken (positief, nul, negatief) aan het aantal snijpunten met de x-as."),
]
