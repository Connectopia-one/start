# -*- coding: utf-8 -*-
"""Kijkt na of een leerbundel élke vraag van zijn hoofdstuk dekt.

    python3 dekking.py ../../spark/natuurwetenschappen.json
    python3 dekking.py ../../spark/geschiedenis.json --woorden

De afspraak met Kim: een leerbundel moet elke vraag van zijn hoofdstuk
behandelen, en met dezelfde woorden als de vraag. Tot nu werd dat met de hand
nagelezen. Dit script doet het voorwerk: het haalt uit elke vraag (de vraagtekst en
het juiste antwoord, niet de uitleg) de inhoudswoorden, en meldt welke daarvan
nergens in de bundel staan.

Welke bundel bij welk hoofdstuk hoort, leest het uit de map van het vak: een
hoofdstuk "Voortplanting — deel 2" hoort bij `voortplanting.html`. Staat de
bundel er niet met die naam, dan geeft `--bundel` uitkomst.

Het is voorwerk, geen oordeel: een woord dat hier ontbreekt, kan best met een
synoniem in de bundel staan, en een woord dat hier niet gemeld wordt, kan er
toevallig staan zonder dat het uitgelegd is. Lees de lijst dus zelf na.
"""
import argparse
import json
import pathlib
import re
import sys
import unicodedata

HIER = pathlib.Path(__file__).parent

# Woorden die in elke tekst staan en dus niets zeggen over de inhoud.
STOP = set("""
aangeduid aantal achter achteraan achteraf afbeelding allebei alleen alles altijd
andere anders antwoord bepaalde bepaald beste betekent beter bevat bijvoorbeeld
blijft blijven daarom daardoor daarbij daarna dezelfde dingen door doordat eerst
eerste enkel erbij ervan even gebeurt gebruik gebruikt gebruiken geeft gelijk
gemaakt genoeg gewoon grote groter grootste heeft helemaal hetzelfde hierbij
hierdoor hoeveel hoger hoogste horen hoort iemand ieder iedereen indien juist
juiste kleine kleiner kleinste klopt kloppen komen komt krijgen krijgt kunnen
langer later lijkt maakt maken meer meest meestal minder moeten moet mogelijk
nergens niets nodig nooit omdat omgekeerde onder ongeveer ontbreekt opnieuw
plaats precies samen sommige soms staat staan steeds stuk tegelijk terug tijdens
tussen uiteindelijk uitleg vaak veel verder verschil verschillende volgens voor
vooral voorbeeld voorbeelden vraag vragen waarbij waardoor waarom waarvoor
wanneer weinig welke werken werkt worden wordt zeggen zelf zelfde zoals zonder
zorgt zullen
aanleggen adellijke bedoelt bedoelden bedoelde beroemde beschrijft betekenen
bevinden bevond bewust daaruit daarmee denken doorheen erover gebeurde gebeuren
gedaan gemeen gevolgen gezien groeien groeit handelen hoeven kenden kiezen komst
konden krijgt laten leggen leiden liggen ligge maakte meestemmen mochten nemen
noemde noemen noemt ontstaan ontstond onthouden opzoeken passen raken reden
schrijven spraken staande stellen sterk sterke sturen tegen tonen trekken vallen
vandaag vandaan verandert veranderen verdween verspreid verspreidden vertellen
voerde volgen volgt vonden vroeg vroeger waaraan waarin waarmee wijzen zeggen
zetten zitten zouden zoeken
""".split())

EENHEID = re.compile(r"^\d+([,.]\d+)?$")


def plat(tekst: str) -> str:
    """Kleine letters, zonder accenten en zonder leestekens."""
    zonder = unicodedata.normalize("NFKD", tekst)
    zonder = "".join(c for c in zonder if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9³²/]+", " ", zonder.lower())


UITGANGEN = ("en", "den", "ten", "de", "te", "d", "t", "e", "s")


def staat_erin(woord: str, tekst: str) -> bool:
    """Of het woord (of een verbogen vorm ervan) in de bundeltekst staat.

    Een vraag schrijft "de cellen delen zich", een bundel "de cel deelt zich".
    Zonder deze soepelheid zou het script vooral verbuigingen melden.
    """
    if woord in tekst:
        return True
    for uitgang in UITGANGEN:
        if woord.endswith(uitgang):
            stam = woord[: -len(uitgang)]
            if len(stam) >= 4 and stam in tekst:
                return True
    for uitgang in ("", "en", "e", "s", "t"):
        if len(woord) >= 4 and woord + uitgang in tekst:
            return True
    return False


def kernwoorden(vraag: dict) -> set:
    stukken = [vraag["vraag"]]
    antwoord = vraag.get("antwoord")
    if vraag["type"] == "meerkeuze":
        nummers = antwoord if isinstance(antwoord, list) else [antwoord]
        stukken += [vraag["opties"][n] for n in nummers]
    elif vraag["type"] == "invultekst":
        stukken.append(str(antwoord))
    woorden = set()
    for stuk in stukken:
        for woord in plat(stuk).split():
            if len(woord) >= 5 and woord not in STOP and not EENHEID.match(woord):
                woorden.add(woord)
    return woorden


def tekst_van_bundel(pad: pathlib.Path) -> str:
    html = pad.read_text(encoding="utf-8")
    html = re.sub(r"<style.*?</style>", " ", html, flags=re.S)
    return plat(re.sub(r"<[^>]+>", " ", html))


def slug(naam: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", plat(naam)).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("bestand", help="het vragenbestand, bv. ../../spark/natuurwetenschappen.json")
    ap.add_argument("--bundel", action="append", default=[],
                    help="hoofdstuktitel=bundelnaam, als de naam niet uit de titel volgt")
    ap.add_argument("--alles", action="store_true", help="ook de hoofdstukken zonder gaten tonen")
    args = ap.parse_args()

    data = json.loads(pathlib.Path(args.bestand).read_text(encoding="utf-8"))
    handmatig = dict(paar.split("=", 1) for paar in args.bundel)

    gaten = 0
    for h in data["hoofdstukken"]:
        titel = h["titel"]
        naam = handmatig.get(titel) or slug(re.split(r"\s+—\s+deel", titel)[0])
        pad = HIER / f"{naam}.html"
        if not pad.exists():
            print(f"!! {titel}: geen bundel {naam}.html")
            gaten += 1
            continue
        bundeltekst = tekst_van_bundel(pad)
        ontbreekt = {}
        for i, vraag in enumerate(h["vragen"], start=1):
            mist = sorted(w for w in kernwoorden(vraag) if not staat_erin(w, bundeltekst))
            if mist:
                ontbreekt[i] = mist
        if ontbreekt or args.alles:
            print(f"\n{titel}  →  {naam}.html")
            for i, mist in ontbreekt.items():
                print(f"   vraag {i:2}: {', '.join(mist)}")
            gaten += len(ontbreekt)
    print(f"\n{gaten} vragen met woorden die niet in hun bundel staan.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
