# -*- coding: utf-8 -*-
"""Rekent de getalvoorbeelden uit de wiskundebundels na.

    python3 controleer.py

Een scheve tekening zie je meteen; een fout rekenvoorbeeld niet. Daarom staat
elk getal dat in een wiskundebundel beweerd wordt hier nog eens, maar dan
uitgerekend in plaats van uitgeschreven. Zet je een nieuw voorbeeld in een
bundel, zet het hier dan ook bij.
"""
import math
from fractions import Fraction

F = Fraction

CONTROLES = [
    # (waar het staat, wat de bundel beweert, hoe je het narekent)
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
    ("getallenleer: kgv(4, 6) = 12",            12,             math.lcm(4, 6)),
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
