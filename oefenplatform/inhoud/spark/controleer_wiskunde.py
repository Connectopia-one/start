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
import json, pathlib, sys
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


def mintekens(waarde) -> str:
    """Zet elk minteken in dezelfde vorm.

    In de vragen staat het echte minteken (−, U+2212) omdat dat in een zin
    mooier leest dan het koppelteken van het toetsenbord. Python schrijft zijn
    eigen uitkomsten met dat koppelteken (-). Zonder deze omzetting zou
    "−8" niet gelijk zijn aan "-8" en meldde de controle een fout die er niet is.
    """
    return str(waarde).replace("-", "\u2212")

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

        verwacht = mintekens(uitkomst)

        if vraag["type"] == "waarofniet":
            ok = vraag["antwoord"] == uitkomst
            gekregen = vraag["antwoord"]
        elif vraag["type"] == "meerkeuze":
            opties = [mintekens(o) for o in vraag["opties"]]
            aangeduid = opties[vraag["antwoord"]]
            if verwacht in opties:
                ok = aangeduid == verwacht
            else:
                ok = verwacht in aangeduid
            gekregen = vraag["opties"][vraag["antwoord"]]
        else:
            ok = verwacht == mintekens(vraag["antwoord"])
            gekregen = vraag["antwoord"]

        if ok:
            print(f"  ok    {titel[:34]:34} {fragment[:38]}")
        else:
            fout += 1
            print(f"  FOUT  {titel} — {vraag['vraag']}")
            print(f"        aangeduid: {gekregen!r}, maar narekenen geeft {uitkomst!r}")

    # Welke vragen met een getal erin staan nog niet in de lijst?
    import re
    ongedekt = [v["vraag"] for _, v in vragen
                if v["vraag"] not in gezien and re.search(r"\d", v["vraag"])]
    totaal = len(CONTROLES) + len(WOORDEN)
    print(f"\n{totaal - fout} van de {totaal} nagekeken en juist aangeduid.")
    if ongedekt:
        print(f"{len(ongedekt)} vragen met een getal staan nog niet in CONTROLES:")
        for v in ongedekt[:12]:
            print("   -", v[:90])
    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main())
