# -*- coding: utf-8 -*-
"""Rekent de wiskundevragen na en controleert of het júiste antwoord aangeduid is.

    python3 inhoud/spark/controleer_wiskunde.py

Waarom dit bestaat: bij een vraag als "waar betaal je het minst?" kan de uitleg
kloppen terwijl de verkeerde optie aangevinkt staat. Zo'n fout leert een kind
iets verkeerds aan en valt bij nalezen makkelijk weg. Daarom rekent dit script
per vraag zelf uit wat eruit moet komen, en kijkt het of dat antwoord ook het
aangeduide is.

Elke regel in CONTROLES is: (stukje van de vraagtekst, de uitkomst).
De uitkomst moet als tekst in de aangeduide optie voorkomen — of, bij een
waar/niet-vraag, gelijk zijn aan het aangeduide antwoord.

Niet elke vraag staat hier: definitievragen ("wat is een noemer") vallen niet
na te rekenen. Elke vraag met een getal erin hoort er wél in.
"""
import json, pathlib, re, sys
from fractions import Fraction as F

BESTAND = pathlib.Path(__file__).parent / "wiskunde.json"


def euro(bedrag):
    """€ 56 → "56", € 39,60 → "39,60" (zoals het in de opties staat)."""
    bedrag = F(bedrag)
    if bedrag.denominator == 1:
        return str(bedrag.numerator)
    return f"{float(bedrag):.2f}".replace(".", ",")



def macht(grondtal: int, exponent: int) -> str:
    """macht(2, 7) → "2⁷" — zoals de exponent in de opties geschreven staat."""
    hoog = str.maketrans("0123456789", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")
    return f"{grondtal}{str(exponent).translate(hoog)}"


def komma(getal: str) -> F:
    """"0,5" → 1/2. De opties staan met een komma, zoals in het Nederlands."""
    heel, _, deel = getal.partition(",")
    return F(int(heel)) + (F(int(deel), 10 ** len(deel)) if deel else 0)


def kleiner_kwadraat(opties) -> str:
    """Welke van deze getallen wordt kleiner als je het kwadrateert.

    Dat is het tegenvoorbeeld bij "het kwadraat is altijd groter dan het getal
    zelf". Het script zoekt het zelf op, zodat de opties in de vraag mogen
    wijzigen zonder dat deze controle stilzwijgend verkeerd wordt.
    """
    passend = [o for o in opties if komma(o) ** 2 < komma(o)]
    if len(passend) != 1:
        raise SystemExit(f"verwacht precies één tegenvoorbeeld, kreeg {passend}")
    return passend[0]


PI = F(314, 100)   # zoals in de vragen zelf staat


def komma_uit(waarde) -> str:
    """3,14 × 25 → "78,5" — zonder nullen achteraan, met een komma."""
    tekst = f"{float(waarde):.4f}".rstrip("0").rstrip(".")
    return tekst.replace(".", ",")


def als_python(uitdrukking: str) -> str:
    """"x² + 8x + 16" → "x**2 + 8*x + 16", zodat Python het kan uitrekenen.

    Alleen voor de eenvoudige vormen die in deze vragen voorkomen: cijfers,
    de letters a, b, x en y, plus, min, en machten geschreven met ² of ³.
    """
    tekst = uitdrukking.replace("\u2212", "-").replace("\u00b2", "**2").replace("\u00b3", "**3")
    tekst = re.sub(r"(?<=[\da-y])\s*(?=[a-y])", "*", tekst)   # 8x → 8*x, ab → a*b
    tekst = re.sub(r"(?<=[a-y])\s*(?=\()", "*", tekst)        # a( → a*(
    return tekst


def uitwerking(kandidaat: str, echte, **waarden) -> str:
    """Controleert of een uitgewerkte vorm hetzelfde geeft als het origineel.

    `echte` is een functie die de oorspronkelijke uitdrukking uitrekent. De
    kandidaat wordt op een handvol getallen getoetst; klopt hij overal, dan
    komt hij ongewijzigd terug zodat CONTROLES hem kan vergelijken met de
    aangeduide optie. Zo staat er in dit bestand niet gewoon hetzelfde
    antwoord overgeschreven, maar wordt het echt nagerekend.
    """
    letters = sorted(set(re.findall(r"[a-y]", als_python(kandidaat))))
    proeven = [-3, -1, 0, 2, 5, 7]
    for getallen in zip(*[proeven] * max(len(letters), 1)):
        omgeving = dict(zip(letters, getallen))
        if eval(als_python(kandidaat), {}, omgeving) != echte(**omgeving):
            raise SystemExit(f"{kandidaat!r} klopt niet bij {omgeving}")
    return kandidaat


def mediaan_of_modus(getallen, welke: str):
    """De mediaan of de modus van een rijtje, zelf uitgerekend.

    Zo staat het antwoord op zo'n vraag niet gewoon overgeschreven in dit
    bestand: als iemand een getal in de vraag verandert, verandert de
    verwachte uitkomst mee en valt een vergeten aanpassing meteen op.
    """
    op_volgorde = sorted(getallen)
    if welke == "mediaan":
        midden, oneven = divmod(len(op_volgorde), 2)
        if oneven:
            return op_volgorde[midden]
        return F(op_volgorde[midden - 1] + op_volgorde[midden], 2)
    vaakst = max(op_volgorde, key=op_volgorde.count)
    return vaakst


def verz(getallen) -> str:
    """Schrijft een verzameling op zoals in de vragen: {1, 2, 3}."""
    if not getallen:
        return "De lege verzameling"
    return "{" + ", ".join(str(g) for g in sorted(getallen)) + "}"


def priem(n: int) -> bool:
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def zelfde_schrijfwijze(waarde) -> str:
    """Zet een antwoord in één vaste vorm, zodat de vergelijking over
    schrijfwijze struikelt noch fouten verbergt.

    Twee dingen verschillen tussen de vragen en wat Python uitrekent:

    - Het minteken. In de vragen staat het echte minteken (−, U+2212), want dat
      leest in een zin beter dan het koppelteken van het toetsenbord. Python
      schrijft zijn eigen uitkomsten met dat koppelteken (-).
    - De duizendtalspatie. In het Nederlands schrijf je 75 000, Python schrijft
      75000.

    Zonder deze omzetting meldde de controle fouten die er niet waren.
    """
    tekst = str(waarde).replace("-", "\u2212")
    # enkel een spatie tússen cijfers weghalen; "7 cm" moet "7 cm" blijven
    return re.sub(r"(?<=\d)[ \u00a0\u202f](?=\d)", "", tekst)


CONTROLES = [
    # --- Negatieve getallen en procenten, deel 1 ---
    ("'s ochtends −3 °C",                   str(-3 + 7)),
    ("Welk getal is het kleinste",           str(min(-8, -3, 2))),
    ("Hoeveel is −5 + 8",                    str(-5 + 8)),
    ("Hoeveel is 4 − 9",                     str(4 - 9)),
    ("Hoeveel is −6 − 4",                    str(-6 - 4)),
    ("Hoeveel is −3 × 4",                    str(-3 * 4)),
    ("Hoeveel is −6 × −2",                   str(-6 * -2)),
    ("Twee negatieve getallen vermenigvuldigen", False),
    ("Hoeveel is −20 : 5",                   str(-20 // 5)),
    ("duiker zit op −12 meter",              str(-12 + 5)),
    ("Hoeveel is 10 % van 80",               str(int(0.10 * 80))),
    ("Hoeveel is 25 % van 60",               str(int(0.25 * 60))),
    ("jas van € 60 krijgt 20 % korting",     euro(60 * F(80, 100))),
    ("klas van 25 leerlingen dragen er 5",   str(int(F(5, 25) * 100))),
    ("30 % van 50 is hetzelfde als 50 % van 30", 0.30 * 50 == 0.50 * 30),
    # --- deel 2 ---
    ("Hoeveel is −7 − (−3)",                 str(-7 - (-3))),
    ("Hoeveel is 5 − (−6)",                  str(5 - (-6))),
    ("Hoeveel is (−2)³",                     str((-2) ** 3)),
    ("Hoeveel is (−2)⁴",                     str((-2) ** 4)),
    ("Hoeveel is −3 × (4 − 7)",              str(-3 * (4 - 7))),
    ("van −5 °C naar 3 °C",                  str(3 - (-5))),
    ("Hoeveel is 15 % van 200",              str(int(0.15 * 200))),
    ("spel kost € 48 na 20 % korting",       euro(F(48) / F(80, 100))),
    ("eerst 10 % omhoog en daarna 10 % omlaag", euro(F(40) * F(110, 100) * F(90, 100))),
    ("eerst 50 % duurder wordt en daarna 50 % goedkoper", 100 * 1.5 * 0.5 == 100),
    ("Van 40 naar 50 gaan",                  str(int(F(50 - 40, 40) * 100))),
    ("fiets kost € 250",                     euro(250 - F(12, 100) * 250)),
    ("Wat is 120 % van 50",                  str(int(F(120, 100) * 50))),
    ("klas zit 60 % meisjes",                str(int(F(15) / F(60, 100)))),
    ("korting van 25 % is hetzelfde als vermenigvuldigen met 0,75", F(75, 100) == F(3, 4)),
    ("Twee winkels",                         "€ 25"),  # 80−25=55 < 80×0,70=56
    # --- Getallenleer, deel 1 ---
    ("absolute waarde van −7",               str(abs(-7))),
    ("rest bij de deling 20 : 3",            str(20 % 3)),
    ("Hoeveel is √49",                       str(int(49 ** 0.5))),
    ("Hoeveel is 2 + 3 × 4",                 str(2 + 3 * 4)),
    # --- Getallenleer, deel 2 ---
    ("grootste gemeenschappelijke deler van 12 en 18", "6"),
    ("kleinste gemeenschappelijk veelvoud van 4 en 6", "12"),
    ("Hoeveel procent is 3/8",               "37,5"),
    ("trui kost € 40 en gaat 25 % in prijs omlaag", euro(F(40) * F(75, 100))),
    ("schaal 1 : 100 meet een muur 3 cm",    "3 m"),
    ("Vier broden kosten € 6",               euro(10 * F(6, 4))),
    ("Rond 3,247 af tot op twee decimalen",  "3,25"),
    ("−3 is groter dan −5",                  -3 > -5),
    ("Hoeveel is −2 + 2",                    str(-2 + 2)),
    ("Hoeveel is −4 × −4",                   str(-4 * -4)),
    ("Hoeveel procent is 3/4",               str(int(F(3, 4) * 100))),
    ("tegengestelde van −5",                 str(-(-5))),
    ("omgekeerde van 2/3",                   str(1 / F(2, 3))),
    ("12 is een priemgetal",                 all(12 % d for d in range(2, 12))),
    ("Hoeveel is 2³ × 2⁴",                   macht(2, 3 + 4)),
    ("Hoeveel is (2³)²",                     macht(2, 3 * 2)),
    ("Hoeveel is 2⁻²",                       str(F(1, 2 ** 2))),
    # --- Probleemoplossend denken, deel 1 ---
    ("Hoeveel kosten er zeven",              f"€ {euro(7 * F(120, 100))}"),
    ("is een derde afwezig",                 str(24 - 24 // 3)),
    ("hek rond te zetten",                   f"{2 * (12 + 8)} m"),
    ("rijdt 2 uur en 20 minuten",            "%d.%02d" % divmod(9 * 60 + 45 + 140, 60)),
    ("Drie vrienden delen",                  f"€ {45 // 3 - 2}"),
    ("Wat betaal je voor een kilo",          f"€ {2 * 3}"),
    ("Een film duurt 105 minuten",           "%d u %d min" % divmod(105, 60)),
    ("vier broodjes",                        f"€ {20 - 4 * F(250, 100)}"),
    ("hoeveel volledige lengtes",            str(1000 // 25)),
    ("Hoe lang doet hij over 45 km",         f"{45 // 15} uur"),
    ("6 rijen van 8 chocolaatjes",           str(6 * 8 - 12)),
    ("300 g rijst",                          f"{6 * F(300, 4)} g"),
    ("spaart € 15 per week",                 f"{240 // 15} weken"),
    ("drie truien en twee broeken",          str(3 * 2)),
    # --- Probleemoplossend denken, deel 2 ---
    ("kaars van 20 cm",                      str((20 - 5) // 3)),
    ("tel er 7 bij op",                      str(36 // 3 - 7)),
    ("2, 5, 11, 23",                         str(23 * 2 + 1)),
    ("samen 20 voertuigen en 70 wielen",     str((20 * 4 - 70) // 2)),
    ("cijfers 1, 2 en 3",                    str(3 * 2)),
    ("een tweede kraan doet er 12 uur over", f"{1 / (F(1, 6) + F(1, 12))} uur"),
    ("Ieder geeft ieder ander een hand",     str(3 * 2 // 2)),
    ("na 20 % korting € 32",                 f"€ {32 / F(80, 100)}"),
    ("schrijf je het cijfer 1",              str(sum(str(n).count("1") for n in range(1, 21)))),
    ("om de 4 meter een paal",               str(20 // 4 + 1)),
    ("drie opeenvolgende getallen is 48",    str(48 // 3 - 1)),
    ("Wat kost een kilo peren",              f"€ {euro(F(11 - 3 * 2, 2))}"),
    ("rijen van 14 stoelen",                 str(-(-100 // 14))),
    ("over 100 uur",                         "%d.00 u" % ((14 + 100) % 24)),
    ("kubus van 3 bij 3 bij 3",              str(3 ** 3)),
    ("Anna is nu 12",                        f"{(40 - 12) - 12} jaar"),
    ("4 flessen voor de prijs van 3",        f"{int(F(2, 8) * 100)} %"),
    ("er blijven er 4 over",                 str([d for d in (7, 8, 9) if 96 % d == 0][0])),
    # --- Wiskundige redeneringen en uitspraken ---
    # Hier is het antwoord meestal een oordeel, geen getal. Wat je wél kan
    # narekenen is het tegenvoorbeeld zelf: klopt het getal dat aangeduid staat
    # ook echt als tegenvoorbeeld?
    ("dan is het deelbaar door 4.” Welk getal", str(next(n for n in (6, 8, 12) if n % 2 == 0 and n % 4))),
    ("Alle priemgetallen zijn oneven",        str(next(n for n in (2, 9, 15) if n % 2 == 0 and all(n % d for d in range(2, n))))),
    ("kleiner dan of gelijk aan 5",           "x ≤ 5"),
    ("altijd groter dan het getal zelf",      kleiner_kwadraat(("0,5", "2", "10"))),
    # --- Meetkunde: hoeken uitrekenen ---
    ("Hoeveel graden is een gestrekte hoek",  "180"),
    ("som van de hoeken van een driehoek",    "180"),
    ("zijn 50° en 60°",                       f"{180 - 50 - 60}°"),
    ("som van de hoeken van een vierhoek",    str(2 * 180)),
    ("elke hoek van een gelijkzijdige driehoek", str(180 // 3)),
    ("straal van 6 cm",                       f"{2 * 6} cm"),
    ("Hoeveel symmetrieassen heeft een vierkant", "4"),
    ("rechthoek die geen vierkant is",        "2"),
    ("de hoek er recht tegenover",            "70°"),
    ("Hoe groot is zijn nevenhoek",           f"{180 - 70}°"),
    ("binnenhoek van 65°",                    f"{180 - 65}°"),
    ("de tophoek 40°",                        f"{(180 - 40) // 2}°"),
    ("een basishoek 50°",                     f"{180 - 2 * 50}°"),
    ("90°, 100° en 85°",                      f"{360 - 90 - 100 - 85}°"),
    ("symmetrieassen heeft een gelijkzijdige driehoek", "3"),
    ("parallellogram is één hoek 110°",       f"{180 - 110}°"),
    ("hoeken van 90° en 45°",                 "Hij is rechthoekig én gelijkbenig"),
    # --- Metend rekenen ---
    # PI staat als 3,14 in de vragen zelf, dus reken er hier ook mee.
    ("Hoeveel centimeter is 1 meter",        "100"),
    ("Hoeveel meter is 3,5 km",              f"{int(F(35, 10) * 1000)} m"),
    ("Hoeveel minuten is 2,5 uur",           str(int(F(25, 10) * 60))),
    ("seconden zijn er in een kwartier",     str(15 * 60)),
    ("Hoeveel gram is 2,5 kg",               f"{int(F(25, 10) * 1000)} g"),
    ("halve liter",                          f"{int(F(1, 2) * 1000)} ml"),
    ("omtrek van een rechthoek van 7 cm bij 3 cm", str(2 * (7 + 3))),
    ("oppervlakte van een rechthoek van 7 cm bij 3 cm", str(7 * 3)),
    ("vierkant heeft een zijde van 6 cm",    f"{4 * 6} cm"),
    ("basis van 8 cm en een hoogte van 5 cm", f"{F(8 * 5, 2)} cm²"),
    ("basis van 9 cm en een hoogte van 4 cm", f"{9 * 4} cm²"),
    ("straal van 5 cm. Hoe groot is de omtrek", f"{komma_uit(2 * PI * 5)} cm"),
    ("straal van 5 cm. Hoe groot is de oppervlakte", f"{komma_uit(PI * 25)} cm²"),
    ("kubus met een ribbe van 4 cm",         str(4 ** 3)),
    ("balk is 5 cm bij 3 cm bij 2 cm",       f"{5 * 3 * 2} cm³"),
    ("2,5 m² in dm²",                        f"{int(F(25, 10) * 100)} dm²"),
    ("Rond 12,467 af",                       "12,47"),
    ("oppervlakte van 49 cm²",               "7 cm"),
    ("48 cm² en een lengte van 8 cm",        f"{48 // 8} cm"),
    ("evenwijdige zijden van 6 cm en 10 cm", f"{F((6 + 10) * 4, 2)} cm²"),
    ("diagonalen van 8 cm en 6 cm",          f"{F(8 * 6, 2)} cm²"),
    ("diameter van 10 cm",                   f"{komma_uit(PI * 10)} cm"),
    ("kubus met een ribbe van 3 cm",         f"{6 * 3 * 3} cm²"),
    ("balk is 5 cm bij 4 cm bij 2 cm",       f"{2 * (5 * 4) + 2 * (5 * 2) + 2 * (4 * 2)} cm²"),
    ("cilinder heeft een straal van 3 cm",   f"{komma_uit(PI * 9 * 10)} cm³"),
    ("kubus van 2 dm bij 2 dm bij 2 dm",     str(2 ** 3)),
    ("zwembad van 10 m bij 5 m",             f"{int(F(10 * 5 * 15, 10) * 1000)} l"),
    ("3 m² in cm²",                          f"{3 * 100 * 100} cm²"),
    ("2 m³ in liter",                        f"{2 * 1000} l"),
    ("tuin van 20 m bij 15 m",               f"{F(20 * 15, 100)} are"),
    ("daarop een halve cirkel",              f"{komma_uit(36 + F(PI * 9, 2))} cm²"),
    ("in elke hoek een vierkantje van 2 cm", f"{100 - 4 * (2 * 2)} cm²"),
    ("wandelpad van 1,2 km",                 f"{1200 // 15} m"),
    ("5 keer het recept",                    f"{-(-5 * 250 // 1000)} pakjes"),
    ("schaal 1 : 200",                       f"{4 * 200 // 100} m"),
    # --- Relaties en verandering ---
    ("getalwaarde van 3x",                   str(3 * 4)),
    ("getalwaarde van 2a + 5",               str(2 * 6 + 5)),
    ("Herleid: 4a + 3a",                     f"{4 + 3 - 1}a"),
    ("Los op: x + 7 = 12",                   str(12 - 7)),
    ("Los op: 3x = 21",                      str(21 // 3)),
    ("Los op: 2x + 5 = 17",                  f"x = {(17 - 5) // 2}"),
    ("Los op: x − 4 = −9",                   f"x = {-9 + 4}"),
    ("Drie broden kosten",                   f"€ {euro(5 * F(750, 100) / 3)}"),
    ("bij 4 het getal 12",                   f"y = {int(F(6, 2))}x"),
    ("rij begint met 3, 7, 11, 15",          str(15 + 4)),
    ("getalwaarde van x² − 3x",              str(5 ** 2 - 3 * 5)),
    ("getalwaarde van 2a − b",               str(2 * 3 - (-4))),
    ("Los op: 5x − 3 = 2x + 9",              f"x = {(9 + 3) // (5 - 2)}"),
    ("Los op: 3(x − 2) = 15",                f"x = {15 // 3 + 2}"),
    ("Los op: x : 4 = 3",                    f"x = {3 * 4}"),
    ("Het dubbele ervan plus 3 is 21",       f"2x + 3 = {21}"),
    ("€ 2 per kilometer",                    f"{(19 - 3) // 2} km"),
    ("Zes werklui",                          f"{6 * 4 // 12} dagen"),
    ("2 kosten er 7, 3 kosten er 10",        f"{(10 - 4) // 2}n + 1"),
    ("rij begint met 2, 4, 8, 16",           str(16 * 2)),
    ("omtrek van een rechthoek is 26 cm",    f"2(8 + b) = {26}"),
    ("enkel links door 4",                   "Wat je links doet, moet je ook rechts doen"),
    ("Wat betekent de 3",                    "Drie stappen langs de horizontale as"),
    ("welk getal is de coëfficiënt",         "5"),
    ("Werk de haakjes weg: 3(x + 2)",        uitwerking("3x + 6", lambda x: 3 * (x + 2))),
    ("Werk uit: (x + 4)²",                   uitwerking("x² + 8x + 16", lambda x: (x + 4) ** 2)),
    ("Werk uit: 2(3x − 5) + 4x",             uitwerking("10x − 10", lambda x: 2 * (3 * x - 5) + 4 * x)),
    ("Werk uit: (a + b)²",                   uitwerking("a² + 2ab + b²", lambda a, b: (a + b) ** 2)),
    ("Werk uit: (a + b)(a − b)",             uitwerking("a² − b²", lambda a, b: (a + b) * (a - b))),
    ("graad van de veelterm",                "2"),
    ("omgekeerd evenredig verband met factor 24", "y = 24 : x"),
    # --- Data en onzekerheid ---
    ("gemiddelde van 4, 6 en 8",             str(F(4 + 6 + 8, 3))),
    ("gemiddelde van 2, 5, 5 en 8",          str(F(2 + 5 + 5 + 8, 4))),
    ("modus van 3, 7, 7, 9, 12",             str(mediaan_of_modus([3, 7, 7, 9, 12], "modus"))),
    ("mediaan van 3, 7, 9, 12, 20",          str(mediaan_of_modus([3, 7, 9, 12, 20], "mediaan"))),
    ("variatiebreedte van 4, 9, 11 en 20",   str(20 - 4)),
    ("hele cirkel in een cirkeldiagram",     "360"),
    ("25 komen er 10 met de fiets",          f"{int(F(10, 25) * 100)} %"),
    ("groep is 20 % van het geheel",         f"{int(F(20, 100) * 360)}°"),
    ("gemiddelde van 10, 10, 10 en 10",      str(F(40, 4))),
    ("mediaan van 2, 4, 6 en 10",            str(mediaan_of_modus([2, 4, 6, 10], "mediaan"))),
    ("Welke maat geeft het eerlijkste beeld", "De mediaan"),
    ("gemiddelde van vier toetsen is 14",    str(14 * 4)),
    ("moet je op de vierde halen",           str(15 * 4 - (12 + 15 + 16))),
    ("het derde en vierde getal zijn 6 en 8", f"Ja, (6 + 8) : 2 = {F(6 + 8, 2)}"),
    ("variatiebreedte 0",                    "Alle waarden zijn 20"),
    ("sector van 90°",                       "Een vierde"),
    ("40 leerlingen komen er 15 te voet",    f"{komma_uit(F(15, 40) * 360)}°"),
    ("mediaan van 5, 3, 9, 1 en 7",          str(mediaan_of_modus([5, 3, 9, 1, 7], "mediaan"))),
    ("waarde 4 komt 3 keer voor. Hoeveel metingen", str(5 + 3)),
    ("Wat is het gemiddelde?",               komma_uit(F(5 * 3 + 3 * 4, 8))),
    ("kleinste 3 en de grootste 3",          "3"),
    # --- Verzamelingen, deel 1 ---
    ("doorsnede van {1, 2, 3} en {2, 3, 4}", verz({1, 2, 3} & {2, 3, 4})),
    ("unie van {1, 2} en {2, 5}",            verz({1, 2} | {2, 5})),
    ("B = {3, 4}. Wat is A \\ B",              verz({1, 2, 3, 4} - {3, 4})),
    ("doorsnede van {1, 3, 5} en {2, 4, 6}", verz({1, 3, 5} & {2, 4, 6})),
    ("Hoeveel elementen heeft de verzameling {3, 5, 5, 7}", str(len({3, 5, 5, 7}))),
    ("De volgorde waarin je de elementen opschrijft", [1, 2, 3] == [3, 1, 2]),
    ("Hoeveel elementen heeft A?",           str(len({2, 4, 6, 8}))),
    ("Elke verzameling is een deelverzameling van zichzelf", {1, 2} <= {1, 2}),
    ("unie van {1, 2, 3} en de lege verzameling", verz({1, 2, 3} | set())),
    ("12 aan voetbal en 8 aan zwemmen",      str(len(set(range(12)) | set(range(9, 17))))),
    # --- Verzamelingen, deel 2 ---
    ("doorsnede van de even getallen en de veelvouden van 3",
     "De veelvouden van "
     + str(min(n for n in range(1, 100) if n % 2 == 0 and n % 3 == 0))),
    ("B = {4, 5, 6}. Wat is A \u222a B",       verz({1, 2, 3, 4, 5} | {4, 5, 6})),
    ("B = {4, 5, 6}. Wat is B \\ A",           verz({4, 5, 6} - {1, 2, 3, 4, 5})),
    ("A \\ B is altijd hetzelfde als B \\ A",  ({1, 2} - {2, 3}) == ({2, 3} - {1, 2})),
    ("A heeft 7 elementen, B heeft 5",       str(7 + 5 - 2)),
    ("Wat is {1, 2, 3} \u2229 {1, 2, 3}",      verz({1, 2, 3} & {1, 2, 3})),
    ("Hoeveel deelverzamelingen heeft {a, b}", str(2 ** len({"a", "b"}))),
    ("Wat is P \u2229 E",
     verz({n for n in range(1, 200) if priem(n) and n % 2 == 0})),
    ("D \u2229 V",
     verz({n for n in range(1, 400)
           if 12 % n == 0 and n % 12 == 0})),
    ("18 Frans, 14 Duits en 5 allebei",      str(30 - (18 + 14 - 5))),
    ("Als A \u2282 B, dan is A \u2229 B gelijk aan A",
     ({1, 2} & {1, 2, 3}) == {1, 2}),
]

# Vragen die je niet kúnt narekenen omdat het antwoord een woord is. Het juiste
# antwoord staat hier gewoon uitgeschreven. Dat lijkt dubbelop, maar het vangt
# de fout op die bij het bewerken het makkelijkst gebeurt: opties die van plek
# wisselen terwijl het nummer van het antwoord blijft staan.
WOORDEN = [
    ("Wat betekent 50 %",                    "De helft"),
    ("hoe heet het getal 4",                 "noemer"),
    ("hoe heet het getal 3",                 "teller"),
    ("welk getal is de exponent",            "3"),
    ("Welke eigenschap gebruik je",          "Distributief"),
    ("alleen deelbaar is door 1 en door zichzelf", "priemgetal"),
    ("je snapt niet meteen wat er gevraagd wordt", "De opgave nog eens lezen en opschrijven wat je weet en wat je zoekt"),
    ("mag je het toch opschrijven",          False),
    ("veel gegevens door elkaar",            "De gegevens in een tabel of schema zetten"),
    ("Schatten voor je rekent",              False),
    ("Op welke dag ben je klaar",            "De achtste dag"),
    ("samen 3 potloden",                     "Je berekening opnieuw nakijken, want dit klinkt onwaarschijnlijk"),
    ("is het slim om een andere te proberen", True),
    ("laatste stap bij het oplossen",        "Nakijken of je antwoord de gestelde vraag beantwoordt"),
    # --- Wiskundige redeneringen: het antwoord is een oordeel ---
    ("dan is het deelbaar door 2.” Klopt dat", "Ja, altijd"),
    ("Alle veelvouden van 6 zijn even",       "Enkele veelvouden opschrijven: 6, 12, 18, 24"),
    ("En de omgekeerde uitspraak",            "De eerste klopt, de omgekeerde niet"),
    ("dus −5 > −3",                           "Bij negatieve getallen draait de volgorde om: −5 < −3"),
    ("Als a × b = 0",                         "a = 3 en b = 0"),
    ("12 : 4 : 2",                            "Delen gaat van links naar rechts: 12 : 4 = 3, dan 3 : 2 = 1,5"),
    ("Klopt de dubbele pijl",                 "Ja, het geldt in allebei de richtingen"),
    ("is samen 20 % korting",                 "De tweede korting wordt van een kleiner bedrag genomen: samen is het 19 %"),
    ("alle getallen die deelbaar zijn door 5", "De eerste klopt, de tweede niet"),
    ("√9 + √16",                              "Nee, √25 = 5. Een wortel mag je niet zo splitsen bij een som"),
    ("dan is het groter dan 5.” Welke pijl",  "⇒, want omgekeerd geldt het niet: 7 is groter dan 5 maar niet dan 10"),
    ("Een hoek van 130°",                    "stompe hoek"),
    ("1 liter is hetzelfde als 1 dm³",       True),
    ("verticale as niet bij 0",              "Kleine verschillen lijken veel groter dan ze zijn"),
    ("klas A heeft variatiebreedte 4",       "In klas B liggen de resultaten veel verder uit elkaar"),
    ("1,7 kinderen",                         "Een gemiddelde hoeft geen bestaand aantal te zijn"),
    ("Tussen 14 u en 15 u",                  "Het werd in dat uur snel warmer"),
    ("laatste stap van een statistisch onderzoek", "Een antwoord formuleren op je onderzoeksvraag"),
    # --- Verzamelingen: het antwoord is notatie of een naam ---
    ("Hoe schrijf je de verzameling met 1, 2 en 3 erin", "{1, 2, 3}"),
    ("Wat betekent het teken \u2208",        "is een element van"),
    ("Welke uitspraak klopt voor A = {2, 4, 6}", "4 \u2208 A"),
    ("Wat betekent B \u2282 A",                 "Elk element van B zit ook in A"),
    ("B = {2, 4}. Wat klopt",                "B \u2282 A"),
    ("Welk teken staat voor de doorsnede",   "\u2229"),
    ("Hoe noem je een verzameling zonder elementen", "De lege verzameling"),
    ("Waarvoor dient een venndiagram",       "Om met cirkels te tonen wat verzamelingen gemeen hebben"),
    ("B = {1, 2}. Wat klopt",                "A en B zijn gelijk"),
    ("staat een element in het overlappende deel", "Het zit in allebei de verzamelingen"),
    ("\u2124 die van de gehele getallen",       "\u2115 \u2282 \u2124"),
    ("V is de verzameling vierkanten",       "V \u2282 R"),
    ("doorsnede van de ruiten en de rechthoeken", "De vierkanten"),
    ("rechten die a snijden",                "De lege verzameling"),
    ("gelijkbenige driehoeken",              "Z \u2282 G"),
    ("linkercirkel volledig ingekleurd",     "A \\ B"),
    ("wat is het verschil?",                 "{0} heeft \u00e9\u00e9n element, \u2205 heeft er geen"),
    ("Hoe schrijf je wiskundig dat 5 niet in A zit", "5 \u2209 A"),
    ("Waarom is een venndiagram handig",     "Je ziet meteen wie dubbel geteld wordt"),
]


def main():
    data = json.loads(BESTAND.read_text(encoding="utf-8"))
    vragen = [(h["titel"], v) for h in data["hoofdstukken"] for v in h["vragen"]]

    fout = 0
    gezien = set()
    for fragment, uitkomst in CONTROLES + WOORDEN:
        treffers = [(t, v) for t, v in vragen if fragment in v["vraag"]]
        if len(treffers) != 1:
            print(f"  FOUT  {fragment!r} past op {len(treffers)} vragen, verwacht precies 1")
            fout += 1
            continue
        titel, vraag = treffers[0]
        gezien.add(vraag["vraag"])

        verwacht = zelfde_schrijfwijze(uitkomst)

        if vraag["type"] == "waarofniet":
            ok = vraag["antwoord"] == uitkomst
            gekregen = vraag["antwoord"]
        elif vraag["type"] == "meerkeuze":
            opties = [zelfde_schrijfwijze(o) for o in vraag["opties"]]
            aangeduid = opties[vraag["antwoord"]]
            if verwacht in opties:
                ok = aangeduid == verwacht
            else:
                ok = verwacht in aangeduid
            gekregen = vraag["opties"][vraag["antwoord"]]
        else:
            ok = verwacht == zelfde_schrijfwijze(vraag["antwoord"])
            gekregen = vraag["antwoord"]

        if ok:
            print(f"  ok    {titel[:34]:34} {fragment[:38]}")
        else:
            fout += 1
            print(f"  FOUT  {titel} — {vraag['vraag']}")
            print(f"        aangeduid: {gekregen!r}, maar narekenen geeft {uitkomst!r}")

    # Welke vragen met een getal erin staan nog niet in de lijst? De getallen in
    # een tekening ({{hoek 90 ?}}) tellen niet mee: daar valt niets aan na te
    # rekenen, die horen bij de vraagtekst zoals ze getekend wordt.
    import re
    zonder_tekening = lambda t: re.sub(r"\{\{[^}]*\}\}", "", t)
    ongedekt = [v["vraag"] for _, v in vragen
                if v["vraag"] not in gezien and re.search(r"\d", zonder_tekening(v["vraag"]))]
    totaal = len(CONTROLES) + len(WOORDEN)
    print(f"\n{totaal - fout} van de {totaal} nagekeken en juist aangeduid.")
    if ongedekt:
        print(f"{len(ongedekt)} vragen met een getal staan nog niet in CONTROLES:")
        for v in ongedekt[:12]:
            print("   -", v[:90])
    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main())
