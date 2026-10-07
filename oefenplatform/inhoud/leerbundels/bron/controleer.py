# -*- coding: utf-8 -*-
"""Rekent de getalvoorbeelden uit de wiskundebundels na.

    python3 controleer.py

Een scheve tekening zie je meteen; een fout rekenvoorbeeld niet. Daarom staat
elk getal dat in een wiskundebundel beweerd wordt hier nog eens, maar dan
uitgerekend in plaats van uitgeschreven. Zet je een nieuw voorbeeld in een
bundel, zet het hier dan ook bij.
"""
import math
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg
from fractions import Fraction

F = Fraction


def _gemiddelden(punten):
    n = len(punten)
    return sum(x for x, _ in punten) / n, sum(y for _, y in punten) / n


def helling(punten):
    """De richtingscoëfficiënt van de trendlijn door een puntenwolk."""
    gx, gy = _gemiddelden(punten)
    return (sum((x - gx) * (y - gy) for x, y in punten)
            / sum((x - gx) ** 2 for x, _ in punten))


def correlatie(punten):
    """De correlatiecoëfficiënt van een puntenwolk, tussen min 1 en 1."""
    gx, gy = _gemiddelden(punten)
    sxy = sum((x - gx) * (y - gy) for x, y in punten)
    sxx = sum((x - gx) ** 2 for x, _ in punten)
    syy = sum((y - gy) ** 2 for _, y in punten)
    return sxy / (sxx * syy) ** 0.5


def hoekgroepen_bij_evenwijdigen():
    """Welke van de acht hoeken in svg.evenwijdige_hoeken() even groot zijn.

    Het onderschrift bij die tekening beweert dat 1, 4, 5 en 8 gelijk zijn en
    2, 3, 6 en 7 ook. Dat volgt uit de stand van de snijlijn, en die staat in
    svg.py. Verzet iemand daar de snijpunten, dan klopt het onderschrift
    misschien niet meer — daarom rekenen we het hier na in plaats van erop te
    vertrouwen.

    Geeft de twee groepen terug, elk gesorteerd, plus of ze samen 180° zijn.
    """
    y1, y2, sx1, sx2 = 46, 130, 190, 282      # zoals in svg.evenwijdige_hoeken
    lang = math.hypot(sx2 - sx1, y2 - y1)
    v = ((sx2 - sx1) / lang, (y2 - y1) / lang)
    takken = [((-1, 0), (-v[0], -v[1])), ((1, 0), (-v[0], -v[1])),
              ((-1, 0), v), ((1, 0), v)]
    hoeken = {}
    for eerste in (1, 5):
        for j, (u, w) in enumerate(takken):
            cos = max(-1.0, min(1.0, u[0] * w[0] + u[1] * w[1]))
            hoeken[eerste + j] = round(math.degrees(math.acos(cos)), 6)
    per_grootte = {}
    for nummer, graden in hoeken.items():
        per_grootte.setdefault(graden, []).append(nummer)
    groepen = sorted(tuple(sorted(g)) for g in per_grootte.values())
    samen = abs(sum(per_grootte) - 180) < 1e-6 if len(per_grootte) == 2 else False
    return groepen, samen


# economie en bedrijfswetenschappen: de productie- en de kostenreeks
MARG = [2, 5, 7, 8, 6, 4, 2, 0, -3]
TOT = [sum(MARG[: i + 1]) for i in range(len(MARG))]


def TKOST(q):
    """De totale kosten uit het kostenhoofdstuk: 1200 + 4q + 0,0075q²."""
    return 1200 + 4 * q + F(75, 10000) * q * q


CONTROLES = [
    # gezondheid, zorg en welzijn: de Sinner-cirkel blijft altijd het geheel
    ("sinner gewone was", 100, 25 + 25 + 25 + 25),
    ("sinner koude was", 100, 40 + 30 + 10 + 20),

    # (waar het staat, wat de bundel beweert, hoe je het narekent)

    # ── het gratis proefhoofdstuk Rekenen en breuken (23 september 2026)
    ("proef: 348 + 156 = 504",                      504,        348 + 156),
    ("proef: 300+100 en 48+56 = 504",               504,        (300 + 100) + (48 + 56)),
    ("proef: 1 000 − 365 = 635",                    635,        1000 - 365),
    ("proef: 25 × 4 = 100",                         100,        25 * 4),
    ("proef: 144 : 12 = 12",                        12,         144 // 12),
    ("proef: 0,5 × 24 = 12",                        12.0,       0.5 * 24),
    ("proef: 2 468 afgerond → 2 500",               2500,       round(2468, -2)),
    ("proef: 12 + 3 × 4 = 24",                      24,         12 + 3 * 4),
    ("proef: (7 + 3) × 5 = 50",                     50,         (7 + 3) * 5),
    ("proef: 7 + 3 × 5 = 22",                       22,         7 + 3 * 5),
    ("proef: 2,50 + 3,75 = 6,25",                   F(25, 4),   F(5, 2) + F(15, 4)),
    ("proef: 4,2 : 2 = 2,1",                        F(21, 10),  F(42, 10) / 2),
    ("proef: 2 000 : 250 = 8 glazen",               8,          2000 // 250),
    ("proef: 3/8 van 64 = 24",                      24,         64 // 8 * 3),
    ("proef: 1/5 van 45 = 9",                       9,          45 // 5),
    ("proef: 2/3 van 27 = 18",                      18,         27 // 3 * 2),
    ("proef: 1/4 + 2/4 = 3/4",                      F(3, 4),    F(1, 4) + F(2, 4)),
    ("proef: 5/8 − 2/8 = 3/8",                      F(3, 8),    F(5, 8) - F(2, 8)),
    ("proef: 6/8 = 3/4",                            F(3, 4),    F(6, 8)),
    ("proef: 10/15 = 2/3",                          F(2, 3),    F(10, 15)),
    ("proef: 2/6 = 1/3",                            F(1, 3),    F(2, 6)),
    ("proef: 4/8 = 1/2",                            F(1, 2),    F(4, 8)),
    ("proef: 2/4 = 1/2",                            F(1, 2),    F(2, 4)),
    ("proef: 2/3 > 3/8",                            True,       F(2, 3) > F(3, 8)),
    ("proef: 0,6 > 1/2",                            True,       F(6, 10) > F(1, 2)),
    ("proef: 10 % van 240 = 24",                    24.0,       0.10 * 240),
    ("proef: 25 % van 60 = 15",                     15.0,       0.25 * 60),
    ("proef: 50 % van 86 = 43",                     43.0,       0.50 * 86),
    ("proef: 20 % van 250 = 50",                    50.0,       0.20 * 250),
    ("proef: 25 % van 40 = 10, blijft 30",          30.0,       40 - 0.25 * 40),

    # ── wiskunde Start, bijgeschreven op 23 september 2026
    ("start getallenkennis: 45 000 : 1 000 = 45",   45,         45000 // 1000),
    ("start getallenkennis: 7 400 : 100 = 74",      74,         7400 // 100),
    ("start getallenkennis: 3 : 4 = 0,75",          0.75,       3 / 4),
    ("start getallenkennis: 1/5 = 20 %",            20.0,       float(F(1, 5)) * 100),
    ("start getallenkennis: 3/5 = 60 %",            60.0,       float(F(3, 5)) * 100),
    ("start getallenkennis: 2/5 = 40 %",            40.0,       float(F(2, 5)) * 100),
    ("start getallenkennis: 2/4 = 1/2",             F(1, 2),    F(2, 4)),
    ("start getallenkennis: 8/20 = 2/5",            F(2, 5),    F(8, 20)),
    ("start getallenkennis: rij +12 → 60",          60,         48 + 12),
    ("start getallenkennis: rij ×2 → 48",           48,         24 * 2),
    ("start bewerkingen: 24 × 25 = 600",            600,        24 * 25),
    ("start bewerkingen: 24 : 4 × 100 = 600",       600,        24 // 4 * 100),
    ("start bewerkingen: 756 : 7 = 108",            108,        756 // 7),
    ("start bewerkingen: 700:7 + 56:7 = 108",       108,        700 // 7 + 56 // 7),
    ("start bewerkingen: 924 : 4 = 231",            231,        924 // 4),
    ("start bewerkingen: 800:4 + 120:4 + 4:4",      231,        800 // 4 + 120 // 4 + 4 // 4),
    ("start bewerkingen: 832 : 8 = 104",            104,        832 // 8),
    ("start meten: 1 hectometer = 100 meter",       100,        10 ** 2),
    ("start meten: 1 liter = 100 centiliter",       100,        10 ** 2),
    ("start meten: 48 : 6 = 8",                     8,          48 // 6),
    ("start meten: 6 × 6 = 36",                     36,         6 * 6),
    ("start meten: 1 m² = 100 dm²",                 100,        10 * 10),
    ("start meten: 1 dm³ = 1 000 cm³",              1000,       10 * 10 * 10),
    ("start meten: kubus ribbe 3 → 27 cm³",         27,         3 ** 3),
    ("start meten: 0,75 kg = 750 g",                750.0,      0.75 * 1000),
    ("start meten: 750 g is het zwaarst",           750.0,      max(500, 0.75 * 1000, 1.2, 200)),
    ("start meetkunde: piramide 1 + 4 = 5 vlakken", 5,          1 + 4),
    ("start kansrekenen: middelste van 5 getallen", 7,          sorted([3, 5, 7, 9, 11])[2]),
    ("start kansrekenen: 5/20 = 25 %",              25.0,       float(F(5, 20)) * 100),
    ("start kansrekenen: 10/50 = 20 %",             20.0,       float(F(10, 50)) * 100),
    ("start vraagstukken: 30 : 3 = 10",             10,         30 // 3),
    ("start vraagstukken: 25 : 5 = 5, 3 × 5 = 15",  15,         3 * (25 // 5)),
    ("start vraagstukken: 4,50 : 3 = 1,50",         F(3, 2),    F(9, 2) / 3),
    ("start vraagstukken: 8 broden = 12 euro",      12,         2 * 6),
    ("start vraagstukken: 8 − 3 = 5 → 5/8",         F(5, 8),    F(8 - 3, 8)),
    ("start vraagstukken: 12 − 9 = 3 → 1/4",        F(1, 4),    F(12 - 9, 12)),

    ("getallenleer: 7 is ook rationaal",        F(7, 1),        F(7)),
    ("getallenleer: 1/8 < 1/4",                 True,           F(1, 8) < F(1, 4)),
    ("getallenleer: 1/4 + 1/6 = 5/12",          F(5, 12),       F(1, 4) + F(1, 6)),
    ("getallenleer: 1/4 = 3/12",                F(3, 12),       F(1, 4)),
    ("getallenleer: 1/6 = 2/12",                F(2, 12),       F(1, 6)),
    ("getallenleer: 6/8 vereenvoudigd = 3/4",   F(3, 4),        F(6, 8)),
    ("getallenleer: tegengestelde −5 + 5 = 0",  0,              -5 + 5),
    ("getallenleer: 2/3 × 3/2 = 1",             1,              F(2, 3) * F(3, 2)),
    ("getallenleer: |−7| = 7",                  7,              abs(-7)),
    ("getallenleer: 20 : 3 = 6 rest 2",         (6, 2),         (20 // 3, 20 % 3)),
    ("getallenleer: 5³ = 125",                  125,            5 ** 3),
    ("getallenleer: √49 = 7",                   7,              math.isqrt(49)),
    ("getallenleer: 2 + 3 × 4 = 14",            14,             2 + 3 * 4),
    ("getallenleer: (2 + 3) × 4 = 20",          20,             (2 + 3) * 4),
    ("getallenleer: 3 × (4 + 5) = 3×4 + 3×5",   3 * (4 + 5),    3 * 4 + 3 * 5),
    ("getallenleer: 5 − 3 ≠ 3 − 5",             True,           (5 - 3) != (3 - 5)),
    ("getallenleer: 2³ × 2⁴ = 2⁷",              2 ** 7,         2 ** 3 * 2 ** 4),
    ("getallenleer: (2³)² = 2⁶",                2 ** 6,         (2 ** 3) ** 2),
    ("getallenleer: 2⁻² = 1/4",                 F(1, 4),        F(2) ** -2),
    ("getallenleer: 12 = 2 × 2 × 3",            12,             2 * 2 * 3),
    ("getallenleer: 18 = 2 × 3 × 3",            18,             2 * 3 * 3),
    ("getallenleer: ggd(12, 18) = 6",           6,              math.gcd(12, 18)),
    ("getallenleer: kgv(12, 18) = 36",          36,             math.lcm(12, 18)),
    ("getallenleer: kgv uit priemfactoren",     36,             2 * 2 * 3 * 3),
    ("getallenleer: 3/8 = 0,375 = 37,5 %",      37.5,           float(F(3, 8)) * 100),
    ("getallenleer: 25 % van 40 = 10",          10,             0.25 * 40),
    ("getallenleer: 40 − 10 = 30",              30,             40 - 10),
    ("getallenleer: 0,75 × 40 = 30",            30,             0.75 * 40),
    ("getallenleer: 25 % = 1/4 = 0,25",         F(1, 4),        F(25, 100)),
    ("getallenleer: 4 broden € 6 → 1 brood € 1,50", F(3, 2),    F(6, 4)),
    ("getallenleer: 10 broden = € 15",          15,             10 * F(6, 4)),
    ("getallenleer: schaal 1:100, 3 cm → 300 cm", 300,          3 * 100),
    ("getallenleer: 300 cm = 3 m",              3,              300 / 100),
    ("getallenleer: 3,247 op 2 decimalen = 3,25", 3.25,         round(3.247, 2)),
    ("getallenleer: 3,247 op 1 decimaal = 3,2", 3.2,            round(3.247, 1)),
    ("getallenleer: 19 × 21 ligt rond 400",     True,           350 < 19 * 21 < 450),
    ("getallenleer: 20 × 20 = 400",             400,            20 * 20),
    ("getallenleer: priemgetallen tot 13",      [2, 3, 5, 7, 11, 13],
     [n for n in range(2, 14) if all(n % k for k in range(2, n))]),

    # --- negatieve getallen en procenten ---
    ("negatieve: \u22128 < \u22123",                    True,           -8 < -3),
    ("negatieve: \u22123 > \u22125",                    True,           -3 > -5),
    ("negatieve: \u22125 + 8 = 3",                  3,              -5 + 8),
    ("negatieve: 4 \u2212 9 = \u22125",                 -5,             4 - 9),
    ("negatieve: 5 \u2212 (\u22126) = 11",              11,             5 - (-6)),
    ("negatieve: \u22127 \u2212 (\u22123) = \u22124",            -4,             -7 - (-3)),
    ("negatieve: \u22126 \u2212 4 = \u221210",              -10,            -6 - 4),
    ("negatieve: \u22123 \u00d7 4 = \u221212",              -12,            -3 * 4),
    ("negatieve: \u22126 \u00d7 \u22122 = 12",              12,             -6 * -2),
    ("negatieve: \u221220 : 5 = \u22124",               -4,             -20 // 5),
    ("negatieve: (\u22122)\u00b3 = \u22128",               -8,             (-2) ** 3),
    ("negatieve: (\u22122)\u2074 = 16",                16,             (-2) ** 4),
    ("negatieve: 4 \u2212 7 = \u22123",                 -3,             4 - 7),
    ("negatieve: \u22123 \u00d7 (4 \u2212 7) = 9",          9,              -3 * (4 - 7)),
    ("negatieve: 50 % = de helft",              F(1, 2),        F(50, 100)),
    ("negatieve: 25 % = 1/4 = 0,25",            F(1, 4),        F(25, 100)),
    ("negatieve: 10 % van 80 = 8",              8,              F(10, 100) * 80),
    ("negatieve: 15 % van 200 = 30",            30,             F(15, 100) * 200),
    ("negatieve: 5 van 25 = 20 %",              F(20, 100),     F(5, 25)),
    ("negatieve: 3/4 = 75 %",                   F(75, 100),     F(3, 4)),
    ("negatieve: 30 % van 50 = 50 % van 30",    F(30, 100) * 50, F(50, 100) * 30),
    ("negatieve: 30 % van 50 = 15",             15,             F(30, 100) * 50),
    ("negatieve: 20 % van 60 = 12",             12,             F(20, 100) * 60),
    ("negatieve: 60 \u2212 12 = 48",                48,             60 - 12),
    ("negatieve: 0,80 \u00d7 60 = 48",              48,             F(80, 100) * 60),
    ("negatieve: 120 % van 50 = 60",            60,             F(120, 100) * 50),
    ("negatieve: 50 % van 60 = 30",             30,             F(50, 100) * 60),
    ("negatieve: 48 : 0,80 = 60",               60,             48 / F(80, 100)),
    ("negatieve: 40 \u2192 50 is 25 % erbij",       F(25, 100),     F(50 - 40, 40)),
    ("negatieve: door 50 delen geeft 20 %",     F(20, 100),     F(50 - 40, 50)),
    ("negatieve: 15 is 60 % \u2192 totaal 25",     25,             15 / F(60, 100)),
    ("negatieve: 100 +10 % = 110",              110,            F(110, 100) * 100),
    ("negatieve: 10 % van 110 = 11",            11,             F(10, 100) * 110),
    ("negatieve: 110 \u2212 11 = 99",               99,             110 - 11),
    ("negatieve: 100 +50 % = 150",              150,            F(150, 100) * 100),
    ("negatieve: de helft van 150 = 75",        75,             F(150, 2)),
    ("negatieve: 0,70 \u00d7 80 = 56",              56,             F(70, 100) * 80),
    ("negatieve: 80 \u2212 25 = 55",                55,             80 - 25),
    ("negatieve: \u20ac 25 korting is goedkoper",   True,           (80 - 25) < F(70, 100) * 80),

    # --- probleemoplossend denken ---
    ("probleem: een derde van 24 = 8",          8,              F(24, 3)),
    ("probleem: 24 − 8 = 16",                   16,             24 - 8),
    ("probleem: (5 + 7) × 3 = 36",              36,             (5 + 7) * 3),
    ("probleem: 36 : 3 = 12",                   12,             36 // 3),
    ("probleem: 12 − 7 = 5",                    5,              12 - 7),
    ("probleem: 32 : 0,80 = 40",                40,             32 / F(80, 100)),
    ("probleem: 3 truien × 2 broeken = 6",      6,              3 * 2),
    ("probleem: 3 cijfers, 2 plaatsen = 6",     6,              3 * 2),
    ("probleem: 3 vrienden = 3 handdrukken",    3,              3 * 2 // 2),
    ("probleem: 20 m om de 4 m = 6 palen",      6,              20 // 4 + 1),
    ("probleem: 100 : 14 = 7 rest 2",           (7, 2),         (100 // 14, 100 % 14)),
    ("probleem: 100 mensen, 8 rijen",           8,              -(-100 // 14)),
    ("probleem: 105 min = 1 u 45 min",          (1, 45),        divmod(105, 60)),
    ("probleem: 300 g voor 4 → 75 g",           75,             F(300, 4)),
    ("probleem: 6 × 75 = 450",                  450,            6 * 75),
    ("probleem: 19 × 21 ligt rond 400",         True,           350 < 19 * 21 < 450),

    # --- wiskundige redeneringen en uitspraken ---
    ("redenering: 2 is priem en even",          (True, True),
     (all(2 % d for d in range(2, 2)), 2 % 2 == 0)),
    ("redenering: 6 wel door 2, niet door 4",   (0, 2),         (6 % 2, 6 % 4)),
    ("redenering: 9 is niet deelbaar door 2",   1,              9 % 2),
    ("redenering: 123 cijfersom is 6",          6,              1 + 2 + 3),
    ("redenering: 123 : 3 = 41",                41,             123 // 3),
    ("redenering: 12 : 4 : 2 = 1,5",            F(3, 2),        F(12, 4) / 2),
    ("redenering: 4 : 2 zou 6 geven",           6,              12 // (4 // 2)),
    ("redenering: √(9 + 16) = 5",               5,              math.isqrt(9 + 16)),
    ("redenering: √9 + √16 = 7",                7,              math.isqrt(9) + math.isqrt(16)),
    ("redenering: 10 % en nog eens 10 % → 81",  81,             F(90, 100) * F(90, 100) * 100),
    ("redenering: dat is 19 % korting",         19,             100 - F(90, 100) * F(90, 100) * 100),
    ("redenering: 5 > 3 maar −5 < −3",          True,           5 > 3 and -5 < -3),
    ("redenering: uit 5 > 3 volgt 7 > 5",       True,           (5 + 2) > (3 + 2)),
    ("redenering: 10 deelbaar door 5",          0,              10 % 5),
    ("redenering: 2 + 3 × 4 = 14",              14,             2 + 3 * 4),
    ("redenering: (2 + 3) × 4 = 20",            20,             (2 + 3) * 4),
    ("redenering: 2a + 2b = 2(a + b)",          True,
     all(2 * a + 2 * b == 2 * (a + b) for a in range(5) for b in range(5))),

    # --- meetkunde ---
    ("meetkunde: 180 − 50 − 60 = 70",           70,             180 - 50 - 60),
    ("meetkunde: 180 : 3 = 60",                 60,             180 // 3),
    ("meetkunde: vierhoek 2 × 180 = 360",       360,            2 * 180),
    ("meetkunde: tophoek 40 → basishoek 70",    70,             (180 - 40) // 2),
    ("meetkunde: basishoek 50 → tophoek 80",    80,             180 - 2 * 50),
    ("meetkunde: nevenhoek van 70 is 110",      110,            180 - 70),
    ("meetkunde: binnenhoek 65 → 115",          115,            180 - 65),
    ("meetkunde: straal 6 → diameter 12",       12,             2 * 6),
    ("meetkunde: parallellogram 110 → 70",      70,             180 - 110),
    ("meetkunde: 90 en 45 → derde hoek 45",     45,             180 - 90 - 45),
    ("meetkunde: hoekgroepen 1-4-5-8 en 2-3-6-7",
     ([(1, 4, 5, 8), (2, 3, 6, 7)], True),      hoekgroepen_bij_evenwijdigen()),

    # --- metend rekenen ---
    ("metend: 3,5 km = 3500 m",                 3500,           F(35, 10) * 1000),
    ("metend: 2,5 uur = 150 min",               150,            F(25, 10) * 60),
    ("metend: kwartier = 900 s",                900,            15 * 60),
    ("metend: 2,5 m² = 250 dm²",                250,            F(25, 10) * 100),
    ("metend: 3 m² = 30 000 cm²",               30000,          3 * 100 * 100),
    ("metend: tuin 20 × 15 = 300 m²",           300,            20 * 15),
    ("metend: 300 m² = 3 are",                  3,              F(300, 100)),
    ("metend: 1 hectare = 10 000 m²",           10000,          100 * 100),
    ("metend: omtrek 7 bij 3 = 20",             20,             2 * (7 + 3)),
    ("metend: oppervlakte 7 bij 3 = 21",        21,             7 * 3),
    ("metend: omtrek vierkant 6 = 24",          24,             4 * 6),
    ("metend: oppervlakte vierkant 6 = 36",     36,             6 * 6),
    ("metend: omtrek 1×5 en 3×3 allebei 12",    (12, 12),       (2 * (1 + 5), 2 * (3 + 3))),
    ("metend: maar oppervlakte 5 en 9",         (5, 9),         (1 * 5, 3 * 3)),
    ("metend: driehoek (8 × 5) : 2 = 20",       20,             F(8 * 5, 2)),
    ("metend: trapezium (6+10) × 4 : 2 = 32",   32,             F((6 + 10) * 4, 2)),
    ("metend: ruit (8 × 6) : 2 = 24",           24,             F(8 * 6, 2)),
    ("metend: omtrek cirkel r 5 = 31,4",        F(314, 10),     2 * F(314, 100) * 5),
    ("metend: oppervlakte cirkel r 5 = 78,5",   F(785, 10),     F(314, 100) * 25),
    ("metend: omtrek cirkel d 10 = 31,4",       F(314, 10),     F(314, 100) * 10),
    ("metend: kubus 4³ = 64",                   64,             4 ** 3),
    ("metend: balk 5 × 3 × 2 = 30",             30,             5 * 3 * 2),
    ("metend: cilinder r3 h10 = 282,6",         F(2826, 10),    F(314, 100) * 9 * 10),
    ("metend: kubus rib 3, opp 6 × 9 = 54",     54,             6 * 3 * 3),
    ("metend: balk 5-4-2, opp = 76",            76,             2 * 20 + 2 * 10 + 2 * 8),
    ("metend: kubus 2 dm = 8 liter",            8,              2 ** 3),
    ("metend: zwembad 75 m³",                   75,             F(10 * 5 * 15, 10)),
    ("metend: 75 m³ = 75 000 liter",            75000,          75 * 1000),
    ("metend: halve cirkel r3 = 14,13",         F(1413, 100),   F(F(314, 100) * 9, 2)),
    ("metend: samen 36 + 14,13 = 50,13",        F(5013, 100),   36 + F(F(314, 100) * 9, 2)),
    ("metend: 100 − 4 × 4 = 84",                84,             100 - 4 * (2 * 2)),
    ("metend: √49 = 7",                         7,              math.isqrt(49)),
    ("metend: 48 : 8 = 6",                      6,              F(48, 8)),
    ("metend: zijde 3 → 9, zijde 6 → 36",       (9, 36),        (3 * 3, 6 * 6)),
    ("metend: 1200 : 15 = 80",                  80,             F(1200, 15)),
    ("metend: 12,467 op 2 decimalen = 12,47",   12.47,          round(12.467, 2)),
    ("metend: 5 × 250 = 1250 ml",               1250,           5 * 250),
    ("metend: dus 2 pakjes van een liter",      2,              -(-1250 // 1000)),

    # --- relaties en verandering ---
    ("relaties: 3x + 7x = 10x",                 10,             3 + 7),
    ("relaties: 4a + 3a − a = 6a",              6,              4 + 3 - 1),
    ("relaties: 3(x + 2) = 3x + 6",             True,
     all(3 * (x + 2) == 3 * x + 6 for x in range(-5, 6))),
    ("relaties: 2(3x−5)+4x = 10x−10",           True,
     all(2 * (3 * x - 5) + 4 * x == 10 * x - 10 for x in range(-5, 6))),
    ("relaties: x² − 3x bij x = 5 is 10",       10,             5 ** 2 - 3 * 5),
    ("relaties: 2a − b bij a=3, b=−4 is 10",    10,             2 * 3 - (-4)),
    ("relaties: (2 + 3)² = 25",                 25,             (2 + 3) ** 2),
    ("relaties: 4 + 12 + 9 = 25",               25,             4 + 12 + 9),
    ("relaties: (a+b)² = a²+2ab+b²",            True,
     all((a + b) ** 2 == a * a + 2 * a * b + b * b for a in range(-4, 5) for b in range(-4, 5))),
    ("relaties: (x+4)² = x²+8x+16",             True,
     all((x + 4) ** 2 == x * x + 8 * x + 16 for x in range(-5, 6))),
    ("relaties: (a+b)(a−b) = a²−b²",            True,
     all((a + b) * (a - b) == a * a - b * b for a in range(-4, 5) for b in range(-4, 5))),
    ("relaties: 7 × 3 = 21 en 25 − 4 = 21",     (21, 21),       (7 * 3, 25 - 4)),
    ("relaties: quotiënt 6:2 = 12:4 = 15:5",    (3, 3, 3),      (F(6, 2), F(12, 4), F(15, 5))),
    ("relaties: 6 × 4 = 24 = 12 × 2",           (24, 24),       (6 * 4, 12 * 2)),
    ("relaties: lucifers 3n+1 geeft 4, 7, 10",  [4, 7, 10],     [3 * n + 1 for n in (1, 2, 3)]),
    ("relaties: rij 3,7,11,15 → 19",            19,             15 + 4),
    ("relaties: rij 2,4,8,16 → 32",             32,             16 * 2),
    ("relaties: 2x + 5 = 17 → x = 6",           6,              F(17 - 5, 2)),
    ("relaties: 5x−3 = 2x+9 → 3x = 12",         (3, 12),        (5 - 2, 9 + 3)),
    ("relaties: dus x = 4",                     4,              F(12, 3)),
    ("relaties: 3(x−2) = 15 → x = 7",           7,              F(15, 3) + 2),
    ("relaties: taxi 3 + 2x = 19 → x = 8",      8,              F(19 - 3, 2)),
    ("relaties: 2(8+b) = 26 → b = 5",           5,              F(26, 2) - 8),
    # --- Data en onzekerheid ---
    ("data: gemiddelde van 4, 6, 8 is 6",       6,              F(4 + 6 + 8, 3)),
    ("data: mediaan van 3,7,9,12,20 is 9",      9,              sorted([3, 7, 9, 12, 20])[2]),
    ("data: mediaan van 2,4,6,10 is 5",         5,              F(4 + 6, 2)),
    ("data: modus van 3,7,7,9,12 is 7",         7,
     max(set([3, 7, 7, 9, 12]), key=[3, 7, 7, 9, 12].count)),
    ("data: frequentietabel telt op tot 22",    22,             4 + 9 + 6 + 2 + 1),
    ("data: reeks 3,5,6,8,10,16 gemiddelde 8",  8,              F(3 + 5 + 6 + 8 + 10 + 16, 6)),
    ("data: die reeks heeft mediaan 7",         7,              F(6 + 8, 2)),
    ("data: die reeks variatiebreedte 13",      13,             16 - 3),
    ("data: weeklonen gemiddelde 134",          134,            F(10 + 12 + 14 + 500, 4)),
    ("data: weeklonen mediaan 13",              13,             F(12 + 14, 2)),
    ("data: som van vier toetsen met gem. 14",  56,             14 * 4),
    # De twee reeksen die naast elkaar getekend staan: hetzelfde gemiddelde,
    # een heel andere spreiding. Daar hangt het hele onderschrift aan vast.
    ("data: reeks 12..16 gemiddelde 14",        14,             F(12 + 13 + 14 + 15 + 16, 5)),
    ("data: reeks 12..16 mediaan 14",           14,             sorted([12, 13, 14, 15, 16])[2]),
    ("data: reeks 12..16 variatiebreedte 4",    4,              16 - 12),
    ("data: reeks 10,11,12,12,25 gem. 14",      14,             F(10 + 11 + 12 + 12 + 25, 5)),
    ("data: die reeks heeft mediaan 12",        12,             sorted([10, 11, 12, 12, 25])[2]),
    ("data: die reeks variatiebreedte 15",      15,             25 - 10),
    ("data: vier van de vijf 12 of minder",     4,
     sum(1 for g in [10, 11, 12, 12, 25] if g <= 12)),
    # De temperatuurlijn: 12 u tot 17 u.
    ("data: 14 u naar 15 u is 6 graden",        6,              21 - 15),
    ("data: die sprong is de steilste",         6,
     max(b - a for a, b in zip([13, 14, 15, 21, 22, 20], [14, 15, 21, 22, 20]))),
    ("data: het warmst is het om 16 u",         22,             max([13, 14, 15, 21, 22, 20])),
    ("data: vierde toets voor gemiddelde 15",   17,             15 * 4 - (12 + 15 + 16)),
    ("data: 8 van 16 meer dan 9 van 30",        True,           F(8, 16) > F(9, 30)),
    ("data: 20 % van 360\u00b0 is 72\u00b0",            72,             F(20, 100) * 360),
    ("data: 90\u00b0 is een vierde",                 F(1, 4),        F(90, 360)),
    ("data: 15 van 40 geeft 135\u00b0",             135,            F(15, 40) * 360),
    ("data: taartdiagram 40/32/28 telt tot 1",  1,              F(40, 100) + F(32, 100) + F(28, 100)),
    ("data: die delen zijn 10, 8 en 7 van 25",  (F(40, 100), F(32, 100), F(28, 100)),
     (F(10, 25), F(8, 25), F(7, 25))),
    # --- Verzamelingen ---
    ("verz: {3,5,5,7} heeft 3 elementen",       3,              len({3, 5, 5, 7})),
    ("verz: {1,2,3} en {3,1,2} zijn gelijk",    True,           {1, 2, 3} == {3, 1, 2}),
    ("verz: {0} is niet leeg",                  1,              len({0})),
    ("verz: {2,4} \u2282 {1,2,3,4}, niet omgekeerd", (True, False),
     ({2, 4} <= {1, 2, 3, 4}, {1, 2, 3, 4} <= {2, 4})),
    ("verz: {a,b} heeft 4 deelverzamelingen",   4,              2 ** len({"a", "b"})),
    ("verz: {1,2,3} \u2229 {2,3,4} = {2,3}",       {2, 3},         {1, 2, 3} & {2, 3, 4}),
    ("verz: {1,2,3} \u222a {2,3,4} = {1,2,3,4}",   {1, 2, 3, 4},   {1, 2, 3} | {2, 3, 4}),
    ("verz: {1,2,3} \\ {2,3,4} = {1}",           {1},            {1, 2, 3} - {2, 3, 4}),
    ("verz: {1,2} \u222a {2,5} = {1,2,5}",        {1, 2, 5},      {1, 2} | {2, 5}),
    ("verz: {1,2,3,4} \\ {3,4} = {1,2}",         {1, 2},         {1, 2, 3, 4} - {3, 4}),
    ("verz: {1,3,5} \u2229 {2,4,6} is leeg",      set(),          {1, 3, 5} & {2, 4, 6}),
    ("verz: {1,2,3} \u222a \u2205 = {1,2,3}",        {1, 2, 3},      {1, 2, 3} | set()),
    ("verz: A\\B = {1} en B\\A = {3}",           ({1}, {3}),
     ({1, 2} - {2, 3}, {2, 3} - {1, 2})),
    ("verz: Frans-Duits venn 13 / 5 / 9",       (13, 5, 9),     (18 - 5, 5, 14 - 5)),
    ("verz: samen 27 van de 30, dus 3 geen",    (27, 3),        (13 + 5 + 9, 30 - (13 + 5 + 9))),
    ("verz: 12 + 8 \u2212 3 = 17",                  17,             12 + 8 - 3),
    ("verz: 7 + 5 \u2212 2 = 10",                   10,             7 + 5 - 2),
    ("verz: even \u2229 veelvouden van 3 = van 6",  6,
     min(n for n in range(1, 60) if n % 2 == 0 and n % 3 == 0)),
    ("verz: priem \u2229 even = {2}",              {2},
     {n for n in range(2, 200)
      if n % 2 == 0 and all(n % d for d in range(2, int(n ** 0.5) + 1))}),
    ("verz: rechthoek 3 bij 5 is geen vierkant", False,         3 == 5),
    # 🧱 Basis (maak_basis.py)
    ("basis komma: 345,6 heeft 3 honderdtallen", 300,           (3456 // 1000) * 100),
    ("basis komma: 3,45 × 10 = 34,5",            F(345, 10),     F(345, 100) * 10),
    ("basis komma: 3,45 × 100 = 345",            345,            F(345, 100) * 100),
    ("basis komma: 3,45 × 1000 = 3450",          3450,           F(345, 100) * 1000),
    ("basis komma: 2,7 × 1000 = 2700",           2700,           F(27, 10) * 1000),
    ("basis komma: 45 × 100 = 4500",             4500,           45 * 100),
    ("basis komma: 45 : 100 = 0,45",             F(45, 100),     F(45) / 100),
    ("basis komma: 7 : 1000 = 0,007",            F(7, 1000),     F(7) / 1000),
    ("basis komma: 34,50 = 34,5",                F(345, 10),     F(3450, 100)),
    ("basis maten: 1 dm = 0,1 m",                F(1, 10),       F(1, 10)),
    ("basis maten: 1 cl = 0,01 l",               F(1, 100),      F(1, 100)),
    ("basis maten: 1 mg = 0,001 g",              F(1, 1000),     F(1, 1000)),
    ("basis maten: 3,5 km = 3500 m",             3500,           F(35, 10) * 1000),
    ("basis maten: 250 cm = 2,5 m",              F(25, 10),      F(250, 100)),
    ("basis maten: 1,25 km = 1250 m",            1250,           F(125, 100) * 1000),
    ("basis maten: 1 l = 100 cl = 1000 ml",      (100, 1000),    (1 * 100, 1 * 1000)),
    ("basis woorden: 12 + 5 = 17",               17,             12 + 5),
    ("basis woorden: 17 − 5 = 12",               12,             17 - 5),
    ("basis woorden: 4 × 6 = 24",                24,             4 * 6),
    ("basis woorden: 24 : 6 = 4",                4,              24 // 6),
    ("basis woorden: 20 : 3 = 6 rest 2",         (6, 2),         divmod(20, 3)),
    ("basis woorden: 6 × 3 + 2 = 20",            20,             6 * 3 + 2),
    ("basis woorden: 12 : 3 = 4 en 3 : 12 = 0,25", (4, F(1, 4)), (F(12, 3), F(3, 12))),
    ("basis breuken: 3/4 = 0,75",                F(75, 100),     F(3, 4)),
    ("basis breuken: 1/2 = 0,5 en 2/5 = 0,4",    (F(5, 10), F(4, 10)), (F(1, 2), F(2, 5))),
    ("basis breuken: 7/10, 23/100, 5/1000",      (F(7, 10), F(23, 100), F(5, 1000)),
     (F(7) / 10, F(23) / 100, F(5) / 1000)),
    ("basis breuken: 3/5 = 6/10 = 0,6",          F(6, 10),       F(3, 5)),
    ("basis breuken: 1/4 = 25/100",              F(25, 100),     F(1, 4)),
    ("basis breuken: tabel 1/5 = 0,2, 1/10 = 0,1, 1/100 = 0,01",
     (F(2, 10), F(1, 10), F(1, 100)), (F(1, 5), F(1, 10), F(1, 100))),
    ("basis breuken: 0,75 = 75/100 = 3/4, ggd 25", (F(3, 4), 25), (F(75, 100), math.gcd(75, 100))),
    ("basis breuken: 8/4 = 2, 5/5 = 1",          (2, 1),         (F(8, 4), F(5, 5))),
    ("basis breuken: 4/4, 8/4, 12/4 zijn geheel", [F(4, 4), F(8, 4), F(12, 4)],
     [F(n, 4) for n in range(0, 13, 2) if F(n, 4).denominator == 1 and n > 0]),
    ("basis breuken: 7/2 = 3 rest 1 = 3,5",      (3, 1, F(35, 10)), (7 // 2, 7 % 2, F(7, 2))),
    ("basis ggd: delers van 12",                 [1, 2, 3, 4, 6, 12], [d for d in range(1, 13) if 12 % d == 0]),
    ("basis ggd: 3 × 4 = 12 zit in tafel van 3", True,          12 in range(3, 25, 3)),
    ("basis ggd: deelbaarheid 348, 235, 470",    (0, 0, 0),      (348 % 2, 235 % 5, 470 % 10)),
    ("basis ggd: 123 en 729 via cijfersom",      (6, 18, 0, 0),  (1 + 2 + 3, 7 + 2 + 9, 123 % 3, 729 % 9)),
    ("basis ggd: 316 deelbaar door 4",           (0, 4),         (316 % 4, 16 // 4)),
    ("basis ggd: ggd(12, 18) = 6",               6,              math.gcd(12, 18)),
    ("basis ggd: gemeenschappelijke delers 12/18", {1, 2, 3, 6},
     {d for d in range(1, 13) if 12 % d == 0 and 18 % d == 0}),
    ("basis ggd: kgv(4, 6) = 12",                12,             math.lcm(4, 6)),
    ("basis ggd: 12 en 24 in tafel 4 en 6 (tot 24)", {12, 24},
     {n for n in range(1, 25) if n % 4 == 0 and n % 6 == 0}),
    ("basis ggd: 12/18 = 2/3",                   F(2, 3),        F(12, 18)),
    ("basis ggd: 1/4 + 1/6 = 3/12 + 2/12 = 5/12", F(5, 12),      F(1, 4) + F(1, 6)),
    ("basis ggd: bus en tram samen om 8.12 u",   12,             math.lcm(4, 6)),
    ("basis ggd: priemgetallen tot 13",          [2, 3, 5, 7, 11, 13],
     [n for n in range(2, 14) if all(n % d for d in range(2, n))]),

    # ── Spark, nagekeken tegen de vragen op 23 september 2026 ──
    ("getallenleer: van klein naar groot",       [-5, -3, 0, F(1, 2), 1],
     sorted([F(1, 2), -3, 1, -5, 0])),
    ("getallenleer: 2 is het enige even priemgetal", [2],
     [n for n in range(2, 60) if n % 2 == 0 and all(n % d for d in range(2, n))]),
    ("negatieve: -3 + 7 = 4 °C",                 4,              -3 + 7),
    ("negatieve: van -5 naar 3 is 8 graden",     8,              3 - (-5)),
    ("negatieve: 25 % van 60 = 15",              15,             60 // 4),
    ("negatieve: 10 % van 80 = 8",               8,              80 // 10),
    ("probleem: 9.45 u + 2 u 20 min = 12.05 u",  (12, 5),
     divmod(9 * 60 + 45 + 2 * 60 + 20, 60)),
    ("probleem: hek rond 12 bij 8 = 40 m",       40,             2 * (12 + 8)),
    ("probleem: gras in 12 bij 8 = 96 m2",       96,             12 * 8),
    ("probleem: 20 voertuigen, 70 wielen -> 5 motors", 5,
     next(m for m in range(21) if 2 * m + 4 * (20 - m) == 70)),
    ("probleem: 3 opeenvolgende met som 48",     [15, 16, 17],
     [48 // 3 - 1, 48 // 3, 48 // 3 + 1]),
    ("probleem: kranen 6 u en 12 u samen",       4,
     int(1 / (F(1, 6) + F(1, 12)))),
    ("probleem: mama dubbel zo oud over 16 jaar", 16,
     next(j for j in range(60) if 40 + j == 2 * (12 + j))),
    ("probleem: 100 uur na 14.00 u",             18,             (14 + 100) % 24),
    ("probleem: 100 snoepjes, 4 over, 8 kinderen", True,
     96 % 8 == 0 and 8 > 4),
    ("probleem: rij 2, 5, 11, 23 -> 47",         47,             23 * 2 + 1),
    ("probleem: kubus 3 bij 3 bij 3 = 27",       27,             3 ** 3),
    ("redeneringen: 12 : 4 = 3 en 12 : 2 = 6",   (3, 6),         (12 // 4, 12 // 2)),
    ("redeneringen: 4 x 6 = 24 is even",         (24, True),     (4 * 6, 4 * 6 % 2 == 0)),
    ("redeneringen: 3 x 5 = 15 is oneven",       (15, True),     (3 * 5, 3 * 5 % 2 == 1)),
    ("redeneringen: 0,5 in het kwadraat = 0,25", F(1, 4),        F(1, 2) ** 2),
    ("redeneringen: twee driehoeken met oppervlakte 6", (6, 6),
     (F(6 * 2, 2), F(3 * 4, 2))),
    ("redeneringen: 3 en -3 hebben hetzelfde kwadraat", True,    3 ** 2 == (-3) ** 2),
    ("metend: een halve liter = 500 ml",         500,            1000 // 2),
    ("metend: 2,5 kg = 2500 g",                  2500,           int(2.5 * 1000)),
    ("relaties: 2x + 3 = 21 geeft x = 9",        9,              (21 - 3) // 2),
    ("relaties: x : 4 = 3 geeft x = 12",         12,             3 * 4),
    ("data: 5 + 3 = 8 metingen",                 8,              5 + 3),
    ("data: gemiddelde uit de frequentietabel",  F(27, 8),
     F(5 * 3 + 3 * 4, 5 + 3)),
    ("data: dat gemiddelde is 3,375",            F(3375, 1000),  F(27, 8)),
    # samenleving en economie ✨ Spark
    ("samenleving: 40 euro zakgeld min 25 euro uitgaven", 15,      40 - 25),
    ("samenleving: 300 euro fiets aan 25 euro per maand", 12,      300 // 25),
    ("samenleving: 1150 terugbetaald op 1000 geleend",    150,     1150 - 1000),
    ("samenleving: 9 miljoen uitgaven min 8 miljoen inkomsten", 1, 9 - 8),
    ("samenleving: 30 euro van elke 100 euro is 30 %",    30,      round(30 / 100 * 100)),
    ("verzamelingen: delers van 12 en veelvouden van 12", {12},
     {d for d in range(1, 13) if 12 % d == 0} & {v for v in range(1, 200) if v % 12 == 0}),

    # ── wiskunde basis 🚀 Boost doorstroom (7 oktober 2026)
    ("wb getallen: drie vijfde is 0,6",             0.6,        3 / 5),
    ("wb getallen: drie vijfde is 60 %",            60,         round(F(3, 5) * 100)),
    ("wb getallen: 12 % van 250 = 30",              30,         0.12 * 250),
    ("wb getallen: 45 000 = 4,5 × 10⁴",             45000,      4.5 * 10 ** 4),
    ("wb getallen: 0,003 = 3 × 10⁻³",               0.003,      3 * 10 ** -3),
    ("wb getallen: wortel van 81 = 9",              9,          math.isqrt(81)),
    ("wb getallen: derdemachtswortel van 27 = 3",   3,          round(27 ** (1 / 3))),
    ("wb getallen: derdemachtswortel van 64 = 4",   4,          round(64 ** (1 / 3))),
    ("wb getallen: wortel van 50 = 5 wortel 2",     math.sqrt(50), 5 * math.sqrt(2)),
    ("wb getallen: wortel van 8 = 2 wortel 2",      math.sqrt(8),  2 * math.sqrt(2)),
    ("wb getallen: wortel 3 maal wortel 12 = 6",    6.0,        round(math.sqrt(3) * math.sqrt(12), 9)),
    ("wb getallen: wortel 2 + 3 wortel 2 = 4 wortel 2", 4 * math.sqrt(2), math.sqrt(2) + 3 * math.sqrt(2)),
    ("wb getallen: wortel van 9+16 is 5, niet 7",   5.0,        math.sqrt(9 + 16)),
    ("wb getallen: 3 + 4 = 7 (het foute antwoord)", 7,          math.sqrt(9) + math.sqrt(16)),
    ("wb getallen: 2³ × 2² = 2⁵",                   2 ** 5,     2 ** 3 * 2 ** 2),
    ("wb getallen: 2⁵ = 32",                        32,         2 ** 5),
    ("wb getallen: 2⁶ gedeeld door 2 = 2⁵",         2 ** 5,     2 ** 6 // 2),
    ("wb getallen: 3⁴ gedeeld door 3² = 9",         9,          3 ** 4 // 3 ** 2),
    ("wb getallen: 10⁻² = 0,01",                    0.01,       10 ** -2),
    ("wb getallen: (−2)³ = −8",                     -8,         (-2) ** 3),
    ("wb getallen: (−3)² = 9",                      9,          (-3) ** 2),
    ("wb getallen: 3×7 + 3×3 = 3×10",               3 * 10,     3 * 7 + 3 * 3),
    ("wb getallen: 3 × 10 = 30",                    30,         3 * 10),
    ("wb getallen: 2 × 5 = 10, niet 2⁵",            10,         2 * 5),
    ("wb getallen: (2+3)+4 = 2+(3+4)",              (2 + 3) + 4, 2 + (3 + 4)),
    ("wb ordenen: 3,476 → 3,48",                    3.48,       round(3.476, 2)),
    ("wb ordenen: 12,3449 → 12,3",                  12.3,       round(12.3449, 1)),
    ("wb ordenen: 1 999 → 2 000 op honderdtallen",  2000,       round(1999, -2)),
    ("wb ordenen: midden van 4 en 7 = 5,5",         5.5,        (4 + 7) / 2),
    ("wb ordenen: 0,375 = 3/8",                     F(3, 8),    F(375, 1000)),
    ("wb ordenen: 0,8 is het grootste van vier",    0.8,        max(0.8, 0.75, 0.7, 2 / 3)),
    ("wb ordenen: 0,67 ligt het dichtst bij 2/3",   0.67,
     min((0.67, 0.6, 0.7, 0.75), key=lambda k: abs(k - 2 / 3))),
    ("wb ordenen: zeven vijfden = 1,4",             1.4,        7 / 5),
    ("wb ordenen: wortel 2 ligt tussen 1 en 2",     True,       1 < math.sqrt(2) < 2),
    ("wb ordenen: min 10 is kleiner dan min 3",     True,       -10 < -3),
    ("wb ordenen: min 0,5 is groter dan min 1,5",   True,       -0.5 > -1.5),
    ("wb logica: twee uitspraken geven 4 rijen",    4,          2 ** 2),
    ("wb logica: drie uitspraken geven 8 rijen",    8,          2 ** 3),
    ("wb logica: vier uitspraken geven 16 rijen",   16,         2 ** 4),
    ("wb logica: conjunctie waar in 1 van 4 rijen", 1,
     sum(1 for p in (True, False) for q in (True, False) if p and q)),
    ("wb logica: disjunctie waar in 3 van 4 rijen", 3,
     sum(1 for p in (True, False) for q in (True, False) if p or q)),
    ("wb logica: implicatie waar in 3 van 4 rijen", 3,
     sum(1 for p in (True, False) for q in (True, False) if (not p) or q)),
    ("wb bewijzen: 2 + 3 × 4 = 14",                 14,         2 + 3 * 4),
    ("wb bewijzen: (2 + 3) × 4 = 20",               20,         (2 + 3) * 4),
    ("wb bewijzen: 6 gedeeld door een half = 12",   12,         F(6) / F(1, 2)),
    ("wb bewijzen: 0² is niet groter dan nul",      False,      0 ** 2 > 0),
    ("wb bewijzen: min (min 3) is positief",        3,          -(-3)),
    ("wb bewijzen: zijde ×2 geeft oppervlakte ×4",  4,          4 ** 2 // 2 ** 2),

    # ── wiskunde basis: ruimtefiguren en vectoren
    ("wb vectoren: 5 N + 5 N dezelfde zin is 10 N", 10,         5 + 5),
    ("wb vectoren: 5 N tegengesteld heft op",       0,          5 - 5),

    # ── wiskunde basis: schaal en gelijkvormigheid
    ("wb schaal: 3 cm naar 12 cm is factor 4",      4,          F(12, 3)),
    ("wb schaal: zijden 2 en 10 geven factor 5",    5,          F(10, 2)),
    ("wb schaal: factor 1/2 geeft oppervlakte 1/4", F(1, 4),    F(1, 2) ** 2),
    ("wb schaal: factor 2 geeft oppervlakte ×4",    4,          2 ** 2),
    ("wb schaal: factor 2 geeft volume ×8",         8,          2 ** 3),
    ("wb schaal: factor 3 geeft oppervlakte ×9",    9,          3 ** 2),
    ("wb schaal: factor 3 geeft volume ×27",        27,         3 ** 3),
    ("wb schaal: vierkant 2 cm maal factor 4",      8,          2 * 4),
    ("wb schaal: die zijde geeft 64 cm²",           64,         (2 * 4) ** 2),
    ("wb schaal: 16 × oude oppervlakte 4 cm²",      64,         4 ** 2 * 4),
    ("wb schaal: 1 op 50, 4 cm is 200 cm",          200,        4 * 50),
    ("wb schaal: 1 op 100, 3 cm is 300 cm",         300,        3 * 100),
    ("wb schaal: 1 op 25 000, 4 cm is 1 000 m",     1000,       4 * 25000 // 100),
    ("wb driehoek: hoeken 40 en 60 geven 80",       80,         180 - 40 - 60),
    ("wb gelijkvormig: factor 2 op zijde 5",        10,         5 * 2),
    ("wb gelijkvormig: zijden 4 en 6, van 3 naar",  F(9, 2),    3 * F(6, 4)),
    ("wb schaduw: stok 1 m, 1,5 m schaduw, boom",   8,          1 * F(12) / F(3, 2)),
    ("wb schaduw: stok 2 m, 3 m schaduw, boom 10",  15,         10 * F(3, 2)),

    # ── wiskunde basis: Pythagoras en goniometrie
    ("wb pythagoras: 3 en 4 geven 5",               5,          math.isqrt(3 ** 2 + 4 ** 2)),
    ("wb pythagoras: 6 en 8 geven 10",              10,         math.isqrt(6 ** 2 + 8 ** 2)),
    ("wb pythagoras: 13 en 5 geven 12",             12,         math.isqrt(13 ** 2 - 5 ** 2)),
    ("wb pythagoras: 9, 12, 15 is rechthoekig",     True,       9 ** 2 + 12 ** 2 == 15 ** 2),
    ("wb pythagoras: 9² + 12² is 225",              225,        9 ** 2 + 12 ** 2),
    ("wb pythagoras: 5, 6, 8 is niet rechthoekig",  False,      5 ** 2 + 6 ** 2 == 8 ** 2),
    ("wb pythagoras: 5² + 6² is 61",                61,         5 ** 2 + 6 ** 2),
    ("wb pythagoras: 5, 12, 13 klopt",              True,       5 ** 2 + 12 ** 2 == 13 ** 2),
    ("wb pythagoras: 8, 15, 17 klopt",              True,       8 ** 2 + 15 ** 2 == 17 ** 2),
    ("wb pythagoras: 2, 3, 4 klopt niet",           False,      2 ** 2 + 3 ** 2 == 4 ** 2),
    ("wb afstand: (0,0) naar (3,4) is 5",           5.0,        math.dist((0, 0), (3, 4))),
    ("wb afstand: (1,1) naar (4,5) is 5",           5.0,        math.dist((1, 1), (4, 5))),
    ("wb ruimte: kubusdiagonaal ribbe 1 is √3",     round(3 ** 0.5, 6),
     round(math.dist((0, 0, 0), (1, 1, 1)), 6)),
    ("wb ladder: 5 m, voet 3 m, dus 4 m hoog",      4,          math.isqrt(5 ** 2 - 3 ** 2)),
    ("wb kast: 2 bij 1 m past schuin als 2,24 m",   2.24,       round(math.hypot(2, 1), 2)),
    ("wb veld: 30 bij 40 m geeft diagonaal 50",     50,         math.isqrt(30 ** 2 + 40 ** 2)),
    ("wb gonio: sinus van 3-4-5 is 0,6",            F(3, 5),    F(3, 5)),
    ("wb gonio: cosinus van 3-4-5 is 0,8",          F(4, 5),    F(4, 5)),
    ("wb gonio: tangens van 3-4-5 is 0,75",         F(3, 4),    F(3, 4)),
    ("wb gonio: sin² + cos² van 3-4-5 is 1",        1,          F(3, 5) ** 2 + F(4, 5) ** 2),
    ("wb gonio: sinus 0,6 geeft cosinus 0,8",       0.8,        round(float(1 - F(3, 5) ** 2) ** 0.5, 6)),
    ("wb gonio: bergpad 200 m onder 30° is 100 m",  100.0,      round(200 * math.sin(math.radians(30)), 6)),
    ("wb gonio: tangens van 45° is 1",              1.0,        round(math.tan(math.radians(45)), 6)),
    ("wb gonio: 20 m ver, 45°, boom 20 m hoog",     20.0,       round(20 * math.tan(math.radians(45)), 6)),

    # ── wiskunde basis: formules omvormen
    ("wb formule: y = 3x + 6, bij y = 18 is x 4",   4,          F(18 - 6, 3)),
    ("wb formule: driehoek opp 12, basis 6, h 4",   4,          F(2 * 12, 6)),
    ("wb formule: vierkant opp 49 geeft zijde 7",   7,          math.isqrt(49)),
    ("wb formule: 20 g in 4 cm³ is 5 g per cm³",    5,          F(20, 4)),
    ("wb formule: 12 V bij 3 A is 4 ohm",           4,          F(12, 3)),
    ("wb formule: 2 mol per l in 3 l is 6 mol",     6,          2 * 3),
    ("wb formule: 100 W × 20 s is 2 000 J",         2000,       100 * 20),

    # ── wiskunde basis: eerstegraadsvergelijkingen
    ("wb verg: 3x + 5 = 20 geeft x = 5",            5,          F(20 - 5, 3)),
    ("wb verg: 2x − 4 = 10 geeft x = 7",            7,          F(10 + 4, 2)),
    ("wb verg: 5x = 2x + 12 geeft x = 4",           4,          F(12, 5 - 2)),
    ("wb verg: 4(x − 1) = 12 geeft x = 4",          4,          F(12 + 4, 4)),
    ("wb verg: x + 2x = 21 geeft x = 7",            7,          F(21, 3)),
    ("wb verg: drie opeenvolgende, som 24",         8,          F(24, 3)),
    ("wb verg: schelen 6, som 20, kleinste 7",      7,          F(20 - 6, 2)),
    ("wb verg: en het andere is 13",                13,         F(20 - 6, 2) + 6),
    ("wb verg: 20 + 3x = 50 geeft x = 10",          10,         F(50 - 20, 3)),
    ("wb ongelijk: 3x − 2 < 7 geeft x < 3",         3,          F(7 + 2, 3)),
    ("wb ongelijk: −3x > 9 geeft x < −3",           -3,         F(9, -3)),
    ("wb taxi: 5 + 2x ≤ 25 geeft 10 km",            10,         F(25 - 5, 2)),

    # ── wiskunde basis: stelsels
    ("wb stelsel: som 10, verschil 2, x = 6",       6,          F(10 + 2, 2)),
    ("wb stelsel: en y = 4",                        4,          F(10 - 2, 2)),
    ("wb stelsel: y = 2x en x + y = 9, x = 3",      3,          F(9, 3)),
    ("wb stelsel: dan is y 6",                      6,          2 * F(9, 3)),
    ("wb stelsel: 3x − 1 = x + 5 geeft x = 3",      3,          F(5 + 1, 3 - 1)),
    ("wb stelsel: dan is y 8",                      8,          F(5 + 1, 3 - 1) + 5),
    ("wb stelsel: som 12, verschil 4, x = 8",       8,          F(12 + 4, 2)),
    ("wb stelsel: 2x + y = 11 met y = 3, x = 4",    4,          F(11 - 3, 2)),
    ("wb stelsel: 3x + y = 17 met y = 2, x = 5",    5,          F(17 - 2, 3)),
    ("wb stelsel: som 20, verschil 4, grootste 12", 12,         F(20 + 4, 2)),
    ("wb stelsel: 12 fruit, 4 peren meer, 4 appels", 4,         F(12 - 4, 2)),
    ("wb stelsel: en dus 8 peren",                  8,          F(12 - 4, 2) + 4),
    ("wb stelsel: 20 + 2x = 10 + 4x geeft 5 uur",   5,          F(20 - 10, 4 - 2)),
    ("wb stelsel: 20 − 2x = 14 − x geeft 6 uur",    6,          F(20 - 14, 2 - 1)),
    ("wb stelsel: beide kaarsen dan 8 cm",          8,          20 - 2 * 6),

    # ── wiskunde basis: tweedegraadsvergelijkingen
    ("wb tweede: (x − 4)² heeft −8x",               -8,         -2 * 4),
    ("wb tweede: (x − 4)² heeft +16",               16,         4 ** 2),
    ("wb tweede: (x−5)(x+5) is x² − 25",            -25,        -5 * 5),
    ("wb tweede: 6x² + 9x heeft 3x buiten haakjes", (2, 3),     (F(6, 3), F(9, 3))),
    ("wb tweede: x² + 5x + 6 is (x+2)(x+3)",        (5, 6),     (2 + 3, 2 * 3)),
    ("wb tweede: x² − 7x + 12 is (x−3)(x−4)",       (-7, 12),   (-3 + -4, -3 * -4)),
    ("wb tweede: x² − 2x − 8 is (x−4)(x+2)",        (-2, -8),   (-4 + 2, -4 * 2)),
    ("wb tweede: 2x² + 6x heeft wortels 0 en −3",   -3,         F(-6, 2)),
    ("wb tweede: D van x² − 5x + 6 is 1",           1,          (-5) ** 2 - 4 * 1 * 6),
    ("wb tweede: met wortels 2 en 3",               (2, 3),     (F(5 - 1, 2), F(5 + 1, 2))),
    ("wb tweede: D van x² + 2x + 1 is 0",           0,          2 ** 2 - 4 * 1 * 1),
    ("wb tweede: met dubbele wortel −1",            -1,         F(-2, 2)),
    ("wb tweede: D van x² + 9 is negatief",         True,       0 ** 2 - 4 * 1 * 9 < 0),
    ("wb tweede: x² = 49 geeft 7 en −7",            (7, -7),    (math.isqrt(49), -math.isqrt(49))),
    ("wb tweede: x² − 4x = 0 geeft 0 en 4",         (0, 4),     (0, F(4, 1))),
    ("wb tweede: rechthoek 40, lengte 3 meer",      (5, 8),     (5, 5 + 3)),
    ("wb tweede: en 5 × 8 is inderdaad 40",         40,         5 * 8),
    ("wb tweede: de andere oplossing is −8",        -8,         -8),

    # ── wiskunde basis: functies
    ("wb functie: f(x) = 2x + 1 geeft f(4) = 9",    9,          2 * 4 + 1),
    ("wb functie: f(x) = x² geeft f(−3) = 9",       9,          (-3) ** 2),
    ("wb functie: door (0,1) en (2,7) is a = 3",    3,          F(7 - 1, 2 - 0)),
    ("wb functie: f(x) = 2x − 6 heeft nulwaarde 3", 3,          F(6, 2)),
    ("wb functie: f(x) = x + 5 heeft nulwaarde −5", -5,         F(-5, 1)),
    ("wb functie: f(x) = −2x + 7 geeft f(0) = 7",   7,          -2 * 0 + 7),

    # ── wiskunde basis: de parabool
    ("wb parabool: x² − 4x + 3 heeft top-x 2",      2,          F(4, 2)),
    ("wb parabool: en top-y −1",                    -1,         2 ** 2 - 4 * 2 + 3),
    ("wb parabool: x² − 6x heeft top-x 3",          3,          F(6, 2)),
    ("wb parabool: 2x² − 8 snijdt de y-as in −8",   -8,         2 * 0 ** 2 - 8),
    ("wb parabool: −x² + 4 heeft top (0, 4)",       4,          -(0 ** 2) + 4),
    ("wb parabool: en nulwaarden 2 en −2",          (2, -2),    (math.isqrt(4), -math.isqrt(4))),
    ("wb parabool: (x − 4)² + 1 heeft top (4, 1)",  (4, 1),     (4, (4 - 4) ** 2 + 1)),
    ("wb parabool: x² − 4x + 3 is (x − 2)² − 1",    True,
     all(x ** 2 - 4 * x + 3 == (x - 2) ** 2 - 1 for x in range(-5, 6))),
    ("wb parabool: (x + 1)² − 2 heeft top (−1, −2)", (-1, -2),  (-1, (-1 + 1) ** 2 - 2)),
    ("wb parabool: x² − 4 is negatief tussen −2 en 2", True,
     all(x ** 2 - 4 < 0 for x in (-1.9, -1, 0, 1, 1.9))),
    ("wb parabool: x² + 2 heeft top (0, 2)",        2,          0 ** 2 + 2),

    # ── wiskunde basis: telproblemen
    ("wb tellen: 3 truien en 4 broeken is 12",      12,         3 * 4),
    ("wb tellen: twee dobbelstenen geven 36",       36,         6 * 6),
    ("wb tellen: munt en dobbelsteen geven 12",     12,         2 * 6),
    ("wb tellen: drie keer een munt geeft 8",       8,          2 ** 3),
    ("wb tellen: 3 kinderen in een rij, 6 manieren", 6,         math.factorial(3)),
    ("wb tellen: pincodes van 4 cijfers, 10 000",   10000,      10 ** 4),
    ("wb venn: 12 en 9 met 4 beide geeft 17",       17,         12 + 9 - 4),
    ("wb venn: 18 Frans, 7 twee talen, 11 enkel",   11,         18 - 7),
    ("wb vraagstuk: +5 en verdubbeld is 26, dus 8", 8,          F(26, 2) - 5),
    ("wb vraagstuk: 40 euro min 25 % is 30",        30,         40 * F(3, 4)),
    ("wb vraagstuk: na 20 % korting 40, oud 50",    50,         F(40) / F(8, 10)),
    ("wb vraagstuk: 10 procent van 250 is 25",      25,         F(250, 10)),
    ("wb vraagstuk: 18 euro in vier delen, 9",      9,          2 * F(18, 4)),

    # ── wiskunde basis: gegevens weergeven en samenvatten
    ("wb gegevens: 150 tot 190 geeft 4 klassen",    4,          (190 - 150) // 10),
    ("wb gegevens: 20 van de 50 is 40 procent",     40,         F(20, 50) * 100),
    ("wb gegevens: gemiddelde van 4, 6 en 8 is 6",  6,          F(4 + 6 + 8, 3)),
    ("wb gegevens: mediaan van 3,5,9,11,12 is 9",   9,          sorted([3, 5, 9, 11, 12])[2]),
    ("wb gegevens: mediaan van 2,4,6,10 is 5",      5,          F(4 + 6, 2)),
    ("wb gegevens: 6,7,7,8,32 heeft som 60",        60,         sum([6, 7, 7, 8, 32])),
    ("wb gegevens: en gemiddelde 12",               12,         F(sum([6, 7, 7, 8, 32]), 5)),
    ("wb gegevens: en mediaan 7",                   7,          sorted([6, 7, 7, 8, 32])[2]),
    ("wb gegevens: variatiebreedte 7,12,20 is 13",  13,         20 - 7),
    ("wb boxplot: de vijf kengetallen van de reeks", (2, 6, 10, 14, 20),
     svg._kwartielen([2, 5, 6, 7, 8, 10, 11, 12, 14, 15, 20])),
    ("wb boxplot: variatiebreedte 18",              18,         20 - 2),
    ("wb boxplot: interkwartielafstand 8",          8,          14 - 6),
    ("wb boxplot: de helft ligt niet op de helft",  True,       14 - 6 < 20 - 2),
    ("wb as: 98 en 100 vanaf 97 lijkt 3 keer",      3,          F(100 - 97, 98 - 97)),
    ("wb as: terwijl ze 2 procent schelen",         2,          round(F(100 - 98, 98) * 100)),

    # ── wiskunde basis: verbanden tussen twee grootheden
    ("wb verband: correlatie van de tien leerlingen", 0.99,
     round(correlatie([(152, 36), (156, 37), (160, 38), (163, 38), (165, 39),
                       (168, 40), (170, 41), (174, 41), (178, 43), (182, 44)]), 2)),
    ("wb verband: de trendlijn stijgt",             True,
     helling([(152, 36), (156, 37), (160, 38), (163, 38), (165, 39),
              (168, 40), (170, 41), (174, 41), (178, 43), (182, 44)]) > 0),

    # ── toegepaste economie 🚀 Boost dubbele finaliteit (7 oktober 2026)
    # balans en resultatenrekening
    ("te balans: 80 000 − 30 000 geeft 50 000",     50000,      80000 - 30000),
    ("te balans: 25 000 − 25 000 geeft nul",        0,          25000 - 25000),
    ("te balans: 120 000 − 95 000 is 25 000 winst", 25000,      120000 - 95000),
    ("te balans: 72 000 − 60 000 is 12 000 verlies", 12000,     72000 - 60000),
    # aankoopfactuur
    ("te aankoop: 1 000 min 10 % is 900",           900,        1000 - F(10, 100) * 1000),
    ("te aankoop: 21 % btw op 800 is 168",          168,        F(21, 100) * 800),
    ("te aankoop: 6 % btw op 200 is 12",            12,         F(6, 100) * 200),
    ("te aankoop: 500 plus 50 vervoer is 550",      550,        500 + 50),
    ("te aankoop: 21 % btw op 1 000 is 210",        210,        F(21, 100) * 1000),
    ("te aankoop: 1 000 plus btw is 1 210",         1210,       1000 + F(21, 100) * 1000),
    ("te aankoop: 21 % btw op 100 is 21",           21,         F(21, 100) * 100),
    # verkoopfactuur
    ("te verkoop: 2 000 min 5 % is 1 900",          1900,       2000 - F(5, 100) * 2000),
    ("te verkoop: 21 % btw op 1 900 is 399",        399,        F(21, 100) * 1900),
    ("te verkoop: 10 % korting op 500 is 50",       50,         F(10, 100) * 500),
    ("te verkoop: 6 % btw op 600 is 36",            36,         F(6, 100) * 600),
    ("te verkoop: 21 % btw op 400 is 84",           84,         F(21, 100) * 400),
    ("te verkoop: samen 120 euro btw",              120,        F(6, 100) * 600 + F(21, 100) * 400),
    ("te verkoop: 6 % btw op 500 is 30",            30,         F(6, 100) * 500),
    ("te verkoop: 500 plus die btw is 530",         530,        500 + F(6, 100) * 500),
    # de btw-aangifte
    ("te btw: bakker stort 18 min 6 is 12 door",    12,         18 - 6),
    ("te btw: 4 200 min 2 800 is 1 400 betalen",    1400,       4200 - 2800),
    ("te btw: 3 000 min 3 000 is een saldo nul",    0,          3000 - 3000),
    ("te btw: 21 % op 50 is 10,5",                  F(21, 2),   F(21, 100) * 50),
    # boeken
    ("te boeken: 21 % btw op 500 is 105",           105,        F(21, 100) * 500),
    ("te boeken: 500 plus 105 geeft 605",           605,        500 + 105),
    ("te boeken: 21 % btw op 2 000 is 420",         420,        F(21, 100) * 2000),
    ("te boeken: 2 000 plus 420 geeft 2 420",       2420,       2000 + 420),
    ("te boeken: 100 plus 21 geeft 121",            121,        100 + F(21, 100) * 100),
    # proefbalans en eindejaar
    ("te saldo: 5 000 debet min 3 200 credit",      1800,       5000 - 3200),
    ("te saldo: 1 500 credit min 900 debet",        600,        1500 - 900),
    ("te afschrijving: 20 000 over 5 jaar",         4000,       F(20000, 5)),
    ("te afschrijving: 30 000 over 6 jaar",         5000,       F(30000, 6)),
    ("te afschrijving: 15 000 aan 3 000 per jaar",  5,          F(15000, 3000)),
    ("te afschrijving: boekwaarde na 3 jaar",       8000,       20000 - 3 * 4000),
    # rekenblad
    ("te rekenblad: =(2+3)*4 geeft 20",             20,         (2 + 3) * 4),
    ("te rekenblad: =2+3*4 geeft 14",               14,         2 + 3 * 4),
    ("te rekenblad: AFRONDEN(12,348;2) geeft 12,35", 12.35,     round(12.348, 2)),
    ("te rekenblad: =SOM(A1:A5) telt 5 cellen",     5,          len(range(1, 6))),
    # afdrukken
    ("te afdrukken: 20 bladzijden op 10 bladen",    10,         F(20, 2)),

    # ─────────────────────────────── economie en bedrijfswetenschappen
    # bedrijfskolom: elke schakel voegt verkoopprijs min inkoopprijs toe
    ("eb kolom: de maalderij voegt 0,25 toe",       F(25, 100),  F(55, 100) - F(30, 100)),
    ("eb kolom: de bakker voegt 1,05 toe",          F(105, 100), F(160, 100) - F(55, 100)),
    ("eb kolom: de winkel voegt 1,20 toe",          F(120, 100), F(280, 100) - F(160, 100)),
    ("eb kolom: alle toegevoegde waarden samen 2,80", F(280, 100),
     F(30, 100) + F(25, 100) + F(105, 100) + F(120, 100)),
    # productie: de totale productie is de som van de marginale
    ("eb productie: eerste werker brengt er 2 bij", 2,          MARG[0]),
    ("eb productie: vierde werker brengt er 8 bij", 8,          MARG[3]),
    ("eb productie: zevende werker brengt er 2 bij", 2,         MARG[6]),
    ("eb productie: achtste brengt er niets bij",   0,          MARG[7]),
    ("eb productie: het totaal klimt tot 34",       34,         max(TOT)),
    ("eb productie: 34 bij zeven werkers",          34,         TOT[6]),
    ("eb productie: en nog 34 bij acht werkers",    34,         TOT[7]),
    ("eb productie: met de negende zakt het naar 31", 31,       TOT[8]),
    ("eb productie: de vierde brengt het meeste bij", 4,        MARG.index(max(MARG)) + 1),
    # kosten: TK = 1200 + 4q + 0,0075q²
    ("eb kosten: GCK is 6 euro bij 200 stuks",      6,          F(1200, 200)),
    ("eb kosten: GCK is 2 euro bij 600 stuks",      2,          F(1200, 600)),
    ("eb kosten: TK is 2 300 bij 200 stuks",        2300,       TKOST(200)),
    ("eb kosten: TK is 3 075 bij 300 stuks",        3075,       TKOST(300)),
    ("eb kosten: TK is 4 000 bij 400 stuks",        4000,       TKOST(400)),
    ("eb kosten: TK is 5 075 bij 500 stuks",        5075,       TKOST(500)),
    ("eb kosten: TK is 6 300 bij 600 stuks",        6300,       TKOST(600)),
    ("eb kosten: GK is 11,50 bij 200 stuks",        F(1150, 100), TKOST(200) / 200),
    ("eb kosten: GK is 10,25 bij 300 stuks",        F(1025, 100), TKOST(300) / 300),
    ("eb kosten: GK is 10,00 bij 400 stuks",        10,         TKOST(400) / 400),
    ("eb kosten: GK is 10,15 bij 500 stuks",        F(1015, 100), TKOST(500) / 500),
    ("eb kosten: GK is 10,50 bij 600 stuks",        F(1050, 100), TKOST(600) / 600),
    ("eb kosten: 400 stuks is het laagste gemiddelde", 400,
     min(range(100, 801), key=lambda q: TKOST(q) / q)),
    ("eb kosten: het 401ste stuk kost ongeveer 10 euro", 10,
     round(float(TKOST(401) - TKOST(400)))),
    # opbrengsten: prijs 13 euro, TO = 13q, winst = TO - TK
    ("eb winst: TO is 5 200 bij 400 stuks",         5200,       13 * 400),
    ("eb winst: TO is 7 800 bij 600 stuks",         7800,       13 * 600),
    ("eb winst: TO is 10 400 bij 800 stuks",        10400,      13 * 800),
    ("eb winst: winst 1 200 bij 400 stuks",         1200,       13 * 400 - TKOST(400)),
    ("eb winst: winst 1 425 bij 500 stuks",         1425,       13 * 500 - TKOST(500)),
    ("eb winst: winst 1 500 bij 600 stuks",         1500,       13 * 600 - TKOST(600)),
    ("eb winst: winst 1 425 bij 700 stuks",         1425,       13 * 700 - TKOST(700)),
    ("eb winst: winst 1 200 bij 800 stuks",         1200,       13 * 800 - TKOST(800)),
    ("eb winst: TK is 7 675 bij 700 stuks",         7675,       TKOST(700)),
    ("eb winst: TK is 9 200 bij 800 stuks",         9200,       TKOST(800)),
    ("eb winst: 600 stuks geeft de hoogste winst",  600,
     max(range(100, 1201), key=lambda q: 13 * q - TKOST(q))),
    ("eb winst: het 601ste stuk kost ongeveer 13 euro", 13,
     round(float(TKOST(601) - TKOST(600)))),
    ("eb winst: bij 16 euro is het optimum 800 stuks", 800,
     max(range(100, 1601), key=lambda q: 16 * q - TKOST(q))),
    # loonberekening: bruto 2 400, RSZ 13,07 %, voorheffing 320 uit de tabel
    ("eb loon: RSZ van 2 400 is 313,68",            F(31368, 100), 2400 * F(1307, 10000)),
    ("eb loon: belastbaar loon 2 086,32",           F(208632, 100), 2400 - 2400 * F(1307, 10000)),
    ("eb loon: nettoloon 1 766,32",                 F(176632, 100),
     2400 - 2400 * F(1307, 10000) - 320),
    ("eb loon: loonkost met een kwart erbij is 3 000", 3000,      2400 + F(2400, 4)),
]


def _rijen(module, slug, kop):
    """Hoeveel rijen staat er in de kadertabel onder die sectiekop? Zo kan een
    bundel niet 'de negen levensloopfasen' beloven en er acht opsommen."""
    import importlib
    m = importlib.import_module(module)
    b = m.BUNDELS[slug]
    for s in b["secties"]:
        if s["kop"] == kop:
            for soort, inhoud in s["blokken"]:
                if soort == "kader":
                    return inhoud.count("<tr>") - 1
    raise KeyError(f"{slug}: geen kadertabel onder {kop!r}")


_OP = "maak_ontwikkeling_en_pedagogisch_handelen"
CONTROLES += [
    ("op: vier soorten welbevinden", 4,
     _rijen(_OP, "welzijn-en-welbevinden-boost-dubbele-finaliteit", "De vier soorten welbevinden")),
    ("op: vier determinanten van Lalonde", 4,
     _rijen(_OP, "wat-bepaalt-onze-gezondheid-boost-dubbele-finaliteit",
            "De vier determinanten van Lalonde")),
    ("op: negen levensloopfasen", 9,
     _rijen(_OP, "ontwikkeling-de-basisbegrippen-boost-dubbele-finaliteit",
            "De negen levensloopfasen")),
    ("op: vijf ontwikkelingsdomeinen", 5,
     _rijen(_OP, "ontwikkeling-de-basisbegrippen-boost-dubbele-finaliteit",
            "De vijf ontwikkelingsdomeinen")),
    ("op: drie groeiprincipes", 3,
     _rijen(_OP, "de-fysieke-en-motorische-ontwikkeling-boost-dubbele-finaliteit",
            "De drie groeiprincipes")),
    ("op: drie stadia bij Kohlberg", 3,
     _rijen(_OP, "kohlberg-en-erikson-boost-dubbele-finaliteit",
            "Kohlberg: de morele ontwikkeling")),
    ("op: acht conflicten bij Erikson", 8,
     _rijen(_OP, "kohlberg-en-erikson-boost-dubbele-finaliteit",
            "Erikson: de persoonlijkheidsontwikkeling")),
    ("op: zeven soorten spel", 7,
     _rijen(_OP, "de-socio-emotionele-ontwikkeling-boost-dubbele-finaliteit", "De soorten spel")),
    ("op: vijf criteria voor een goede observatie", 5,
     _rijen(_OP, "waarnemen-en-observeren-boost-dubbele-finaliteit", "Een goede observatie")),
    ("op: zes basisbehoeften van Kind en Gezin", 6,
     _rijen(_OP, "gedrag-en-behoeften-boost-dubbele-finaliteit",
            "De zes basisbehoeften van Kind en Gezin")),
    ("op: vijf expressievormen", 5,
     _rijen(_OP, "vrije-tijd-spel-en-expressie-boost-dubbele-finaliteit", "De vijf expressievormen")),
    ("op: zes spelvormen", 6,
     _rijen(_OP, "spelvormen-en-speelgoed-boost-dubbele-finaliteit", "De zes spelvormen")),
    ("op: vier soorten activiteiten voor volwassenen", 4,
     _rijen(_OP, "activiteiten-voor-volwassenen-boost-dubbele-finaliteit",
            "De vier soorten activiteiten")),
    ("op: vijf manieren van kwaliteitsbewust werken", 5,
     _rijen(_OP, "activiteiten-voor-volwassenen-boost-dubbele-finaliteit",
            "Kwaliteitsbewust werken")),
    ("op: vijf babyreflexen", 5,
     _rijen(_OP, "de-fysieke-en-motorische-ontwikkeling-boost-dubbele-finaliteit",
            "De babyreflexen")),
    ("op: vier vormen van gehechtheid", 4,
     _rijen(_OP, "de-socio-emotionele-ontwikkeling-boost-dubbele-finaliteit", "Gehechtheid")),
]


def main():
    fout = 0
    for naam, beweerd, nagerekend in CONTROLES:
        if beweerd == nagerekend:
            print("  ok  ", naam)
        else:
            fout += 1
            print("  FOUT", naam, f"— bundel zegt {beweerd}, narekenen geeft {nagerekend}")
    print(f"\n{len(CONTROLES) - fout} van de {len(CONTROLES)} kloppen.")
    return 1 if fout else 0


if __name__ == "__main__":
    raise SystemExit(main())
