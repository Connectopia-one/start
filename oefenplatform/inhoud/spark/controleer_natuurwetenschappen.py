# -*- coding: utf-8 -*-
"""Rekent de rekenvragen van natuurwetenschappen na.

    python3 inhoud/spark/controleer_natuurwetenschappen.py

Waarom dit bestaat: bij een vraag als "wat is de massadichtheid?" kan de uitleg
kloppen terwijl de verkeerde optie aangevinkt staat. Zo'n fout leert een kind
iets verkeerds aan en valt bij nalezen makkelijk weg. Daarom rekent dit script
per vraag zelf uit wat eruit moet komen, en kijkt het of dát het aangeduide
antwoord is.

Elke regel in CONTROLES is: (een stukje van de vraagtekst dat maar bij één
vraag past, de uitkomst). De uitkomst wordt berekend, niet overgeschreven:
verandert er een getal in de vraag zonder dat de optie mee verandert, dan valt
dat hier door de mand.

Achteraan meldt het script welke vragen met een getal erin nog niet nagekeken
worden. Definitievragen met een getal in een naam mogen daarbij staan.
"""
import json
import pathlib
import re
import sys
from fractions import Fraction as F

BESTAND = pathlib.Path(__file__).parent / "natuurwetenschappen.json"

PI = F(314, 100)            # zoals π in de vragen zelf afgerond staat
DICHTHEID_WATER = F(1)      # g/cm³


def uit(waarde) -> str:
    """3 → "3", 5.4 → "5,4" — geschreven zoals het in de opties staat."""
    waarde = F(waarde)
    if waarde.denominator == 1:
        return str(waarde.numerator)
    tekst = f"{float(waarde):.6f}".rstrip("0").rstrip(".")
    return tekst.replace(".", ",")


def dichtheid(massa, volume) -> str:
    return uit(F(massa) / F(volume))


def kubus(zijde) -> str:
    return uit(F(zijde) ** 3)


def balk(lengte, breedte, hoogte) -> str:
    return uit(F(lengte) * F(breedte) * F(hoogte))


def cilinder(straal, hoogte) -> str:
    return uit(PI * F(straal) ** 2 * F(hoogte))


def bol(straal) -> str:
    return uit(F(4, 3) * PI * F(straal) ** 3)


def snelheid(weg, tijd) -> str:
    return uit(F(weg) / F(tijd))


def naar_kmh(meter_per_seconde) -> str:
    return uit(F(meter_per_seconde) * F(36, 10))


def naar_ms(km_per_uur) -> str:
    return uit(F(km_per_uur) / F(36, 10))


def drijft_of_zinkt(massa, volume) -> str:
    """Zegt zelf of het voorwerp drijft, zweeft of zinkt in water."""
    rho = F(massa) / F(volume)
    if rho < DICHTHEID_WATER:
        return "drijft"
    if rho > DICHTHEID_WATER:
        return "zinkt"
    return "zweeft"


def snelste(kandidaten) -> str:
    """Van een lijstje (naam, snelheid in km/h) de snelste."""
    return max(kandidaten, key=lambda paar: paar[1])[0]


def die_zinken(stoffen) -> str:
    """Van een lijstje (naam, massadichtheid in g/cm³) die in water zinken.

    Het script zoekt ze zelf op, zodat er in de vraag een stof bij mag komen
    zonder dat deze controle stilzwijgend verkeerd wordt.
    """
    return " | ".join(naam for naam, rho in stoffen if F(rho) > DICHTHEID_WATER)


CONTROLES = [
    # ── Massadichtheid ──────────────────────────────────────────────
    ("massa van 300 g en een volume van 100 cm³", dichtheid(300, 100) + " g/cm³"),
    ("kubus met een ribbe van 2 cm?", kubus(2) + " cm³"),
    ("balk van 5 cm op 4 cm op 2 cm", balk(5, 4, 2)),
    ("staat op 50 mL", uit(65 - 50) + " cm³"),
    ("1 liter is evenveel als", uit(1000)),
    ("Hoeveel kubieke meter is 2 liter", uit(F(2, 1000)) + " m³"),
    ("Hoeveel liter gaat er in 0,5 m³", uit(F(5, 10) * 1000) + " L"),
    ("massadichtheid van 1 g/cm³. Hoeveel is dat in kg/m³", uit(1 * 1000) + " kg/m³"),
    ("2700 kg/m³. In g/cm³", uit(F(2700, 1000))),
    ("massa van 72 g en is een kubus met een ribbe van 2 cm",
     dichtheid(72, F(kubus(2))) + " g/cm³"),
    ("Hoeveel weegt 3 cm³ goud", uit(19 * 3) + " g"),
    ("Een stuk van 780 g heeft een volume", uit(F(780) / F(78, 10))),
    ("cilinder met een straal van 2 cm en een hoogte van 10 cm", cilinder(2, 10) + " cm³"),
    ("bol met een straal van 3 cm", bol(3) + " cm³"),
    ("water stijgt van 40 mL naar 55 mL", dichtheid(F(405, 10), 55 - 40) + " g/cm³"),
    ("fles bevat 2 L olie", uit(F(9, 10) * 2000 / 1000) + " kg"),
    ("10 cm³ weegt 27 g", dichtheid(27, 10)),
    ("massa van 60 g en een volume van 75 cm³", drijft_of_zinkt(60, 75)),
    ("massadichtheid van 1200 kg/m³", "zinken"),
    ("Welke van deze zinken in water",
     die_zinken([("IJzer", F(78, 10)), ("Aluminium", F(27, 10)),
                 ("Kurk", F(24, 100)), ("Olie", F(9, 10))])),

    # ── Energie, kracht en snelheid ─────────────────────────────────
    ("legt 100 m af in 20 s", snelheid(100, 20) + " m/s"),
    ("auto rijdt 90 km in 2 uur", snelheid(90, 2)),
    ("Hoeveel km/h is 5 m/s", naar_kmh(5) + " km/h"),
    ("Hoeveel m/s is 72 km/h", naar_ms(72) + " m/s"),
    ("Twee uur is", uit(2 * 3600)),
    ("fietser rijdt 30 s aan 4 m/s", uit(4 * 30) + " m"),
    ("wandelaar over 300 m aan 5 m/s", uit(F(300) / 5) + " s"),
    ("trein rijdt aan 36 km/h", naar_ms(36)),
    ("Wie gaat het snelst",
     snelste([("A", F(15) * F(36, 10)), ("B", F(50)), ("C", F(1) / F(2, 60))])),
    ("allebei 200 N in dezelfde zin", uit(200 + 200) + " N"),
    ("allebei 150 N, maar in tegengestelde zin", uit(150 - 150) + " N"),
    ("eerste uur 60 km en het tweede uur 80 km", snelheid(60 + 80, 2) + " km/h"),
    ("hardloper doet 400 m in 50 s", naar_kmh(snelheid(400, 50)) + " km/h"),

    # ── Veilig werken, meten en eenheden ────────────────────────────
    ("Hoeveel meter is 2 km", uit(2 * 1000) + " m"),
    ("500 g is", uit(F(500, 1000))),
    ("Hoeveel liter is 250 mL", uit(F(250, 1000)) + " L"),
    ("Hoeveel is 3 mm in meter", uit(F(3, 1000)) + " m"),
    ("Hoeveel gram is 1,5 kg", uit(F(15, 10) * 1000) + " g"),
    ("75 cm is", uit(F(75, 100))),
    ("leeg bekerglas (120 g)", uit(370 - 120) + " g"),

    # ── Wetenschappelijk onderzoek ──────────────────────────────────
    ("bij 4 s een afstand van 20 m", snelheid(20, 4) + " m/s"),
]


def antwoordtekst(vraag) -> str:
    """Wat er als juist aangeduid staat, als tekst."""
    if vraag["type"] == "meerkeuze":
        nummers = vraag["antwoord"] if isinstance(vraag["antwoord"], list) else [vraag["antwoord"]]
        return " | ".join(vraag["opties"][n] for n in nummers)
    return str(vraag["antwoord"])


def main() -> int:
    data = json.loads(BESTAND.read_text(encoding="utf-8"))
    vragen = [(h["titel"], v) for h in data["hoofdstukken"] for v in h["vragen"]]

    fout = 0
    gezien = set()
    for fragment, uitkomst in CONTROLES:
        treffers = [(t, v) for t, v in vragen if fragment in v["vraag"]]
        if len(treffers) != 1:
            print(f"  FOUT  {fragment!r} past op {len(treffers)} vragen, verwacht precies 1")
            fout += 1
            continue
        titel, vraag = treffers[0]
        gezien.add(vraag["vraag"])
        gekregen = antwoordtekst(vraag)
        # Een uitkomst met " | " erin hoort bij een vraag met meerdere juiste
        # antwoorden: elk stuk moet aangeduid staan, en er mag niets bij staan.
        delen = uitkomst.split(" | ")
        aangeduid = gekregen.split(" | ")
        if len(delen) == len(aangeduid) and all(
                d.lower() in a.lower() for d, a in zip(delen, aangeduid)):
            print(f"  ok    {titel[:36]:36} {fragment[:40]}")
        else:
            fout += 1
            print(f"  FOUT  {titel} — {vraag['vraag']}")
            print(f"        aangeduid: {gekregen!r}, maar narekenen geeft {uitkomst!r}")

    ongedekt = [(t, v["vraag"]) for t, v in vragen
                if v["vraag"] not in gezien and re.search(r"\d", v["vraag"])]
    print(f"\n{len(CONTROLES) - fout} van de {len(CONTROLES)} nagekeken en juist aangeduid.")
    if ongedekt:
        print(f"{len(ongedekt)} vragen met een getal erin staan niet in CONTROLES:")
        for titel, tekst in ongedekt:
            print(f"   - {titel}: {tekst[:80]}")
    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main())
