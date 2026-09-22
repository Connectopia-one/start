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
