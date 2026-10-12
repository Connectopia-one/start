"""
Controleert of een vraag die zegt hoeveel letters het antwoord telt, ook klopt.

Waarom dit bestaat: op 12 oktober 2026 meldde een kind dat "Welk Engels woord
van zeven letters betekent publiek" niet kon kloppen, want audience heeft er
acht. Toen we erop zochten, stonden er zeven zulke vragen in de databank. Een
kind dat het woord wél kent, gaat dan twijfelen aan zichzelf in plaats van aan
de vraag. Daarom tellen we het voortaan na.

Draaien, vanuit  oefenplatform/inhoud :

    python3 controleer_letters.py

Het script leest alle vragenbestanden (de json's per categorie), zoekt elke
vraag met een getal in letters gevolgd door het woord "letters", en vergelijkt
dat getal met de lengte van elk aanvaard antwoord. Klopt geen enkel antwoord,
dan drukt het de vraag af.

Drie soorten vragen komen er terecht uit als melding terwijl ze juist zijn:
die waar het getal slaat op een afkorting en niet op het antwoord, zoals
"de drie letters van het IPO-model staan voor input, process en ___". Die
staan onderaan in OVERSLAAN. Komt er zo een vraag bij, zet er dan een stuk
van de vraagtekst bij in die lijst.
"""

import glob
import json
import re
import sys

GETAL = {
    "twee": 2, "drie": 3, "vier": 4, "vijf": 5, "zes": 6, "zeven": 7,
    "acht": 8, "negen": 9, "tien": 10, "elf": 11, "twaalf": 12,
    "dertien": 13, "veertien": 14, "vijftien": 15,
}

PATROON = re.compile(r"\b(" + "|".join(GETAL) + r")\s+letters", re.IGNORECASE)

# Vragen waar het getal over een afkorting gaat, niet over het antwoord.
OVERSLAAN = [
    "letters van de AUB-methode",
    "letters van het IPO-model",
    "letters van STEM",
]


def vragen_van(data):
    """Loopt door een vragenbestand, welke vorm het ook heeft."""
    if isinstance(data, dict):
        if "vraag" in data and isinstance(data["vraag"], str):
            yield data
        for waarde in data.values():
            yield from vragen_van(waarde)
    elif isinstance(data, list):
        for stuk in data:
            yield from vragen_van(stuk)


def main():
    gemeld = 0
    for pad in sorted(glob.glob("*/*.json")):
        try:
            data = json.load(open(pad, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for vraag in vragen_van(data):
            tekst = vraag["vraag"]
            if any(stuk in tekst for stuk in OVERSLAAN):
                continue
            gevonden = PATROON.search(tekst)
            if not gevonden:
                continue
            verwacht = GETAL[gevonden.group(1).lower()]
            antwoord = vraag.get("antwoord")
            lijst = antwoord if isinstance(antwoord, list) else [antwoord]
            lengtes = [len(str(a).replace(" ", "")) for a in lijst if isinstance(a, str)]
            if lengtes and verwacht not in lengtes:
                gemeld += 1
                print(f"{pad}: de vraag zegt {verwacht} letters, {lijst} heeft {lengtes}")
                print(f"   {tekst}")

    if gemeld:
        print(f"\n{gemeld} vragen met een verkeerd aantal letters.")
        return 1
    print("Alle vragen met een aantal letters kloppen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
