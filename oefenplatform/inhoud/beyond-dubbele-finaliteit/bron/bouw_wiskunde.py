# -*- coding: utf-8 -*-
"""Zet de themabestanden `wi_*.py` samen in ../wiskunde.json.

    python3 bron/bouw_wiskunde.py

🌍 Beyond dubbele finaliteit, derde graad. Eén vakfiche, "3 dubbele
finaliteit", geldig van 1 januari 2027 tot en met 31 december 2027. Ze geldt
voor commerciële organisatie en voor de basisvorming dubbele finaliteit; dat
staat bovenaan op de fiche, lees het af in plaats van het te gokken.

Het vak heet hier gewoon **wiskunde**, niet wiskunde gevorderd: deze fiche is
de basisvorming van de dubbele finaliteit en vraagt duidelijk minder dan de
drie doorstroomfiches. Geen limieten, geen afgeleiden, geen integralen, geen
goniometrie; wel machten met rationale exponent, logaritmen, het aflezen van
een grafiek, het differentiequotiënt, exponentiële groei, kansrekenen en
statistiek.

De fiche geeft achteraan zelf de gewichten van het examen:

    Analyse                     60 %  ->  7 thema's
    Kansrekenen en statistiek   40 %  ->  5 thema's

Probleemoplossend denken is een eigen bouwsteen in de fiche, maar weegt niet
apart mee op het examen; het komt er geïntegreerd aan bod. Wij geven het toch
één thema, want heuristieken en het omzetten van een situatie naar wiskunde
zijn precies waar een kind op vastloopt, en dan oefent het die stappen los van
de rest.

**Bij wiskunde geen meerkeuze met meerdere juiste antwoorden.** Dat mag bij
geschiedenis en Nederlands, waar een opsomming een oordeel vraagt, maar bij
wiskunde is er één uitkomst en anders is de vraag slecht gesteld. Het script
weigert er dan ook een.

Werkt verder als elk ander bouwscript: elk thema is een bestand met een lijst
DEEL1 en een lijst DEEL2 van twintig vragen, en wordt hier twee hoofdstukken,
"<thema> — deel 1" en "<thema> — deel 2".
"""

import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "wiskunde.json"

# De volgorde volgt de fiche: eerst de analyse, van het rekengereedschap naar
# het functieonderzoek en de groeimodellen, dan de kansrekening en de
# statistiek. Het probleemoplossend denken staat vooraan, want de stappen die
# het aanleert komen daarna in elk ander thema terug.
THEMAS = [
    ("wi_problemen", "Problemen oplossen: van situatie naar wiskunde"),
    ("wi_machten", "Machtswortels en machten met rationale exponent"),
    ("wi_logaritmen", "Logaritmen"),
    ("wi_grafiek", "Een functie aflezen van haar grafiek"),
    ("wi_verandering", "Gemiddelde verandering en het differentiequotiënt"),
    ("wi_exponentieel", "Exponentiële functies"),
    ("wi_groei", "Lineaire en exponentiële groeimodellen"),
    ("wi_kansen", "Kansen en de wet van Laplace"),
    ("wi_kansboom", "Kansbomen: product, som en complement"),
    ("wi_steekproef", "Populatie, steekproef en representativiteit"),
    ("wi_causaliteit", "Samenhang en causaliteit"),
    ("wi_normaal", "De normale verdeling en de Gausskromme"),
]


def controleer(titel: str, nummer: int, vraag: dict):
    plek = f"{titel}: vraag {nummer}"
    soort = vraag["type"]
    if soort == "meerkeuze":
        opties = vraag["opties"]
        if len(opties) < 3:
            raise SystemExit(f"{plek} heeft maar {len(opties)} opties")
        if len(set(opties)) != len(opties):
            raise SystemExit(f"{plek} heeft twee gelijke opties")
        antwoord = vraag["antwoord"]
        nummers = antwoord if isinstance(antwoord, list) else [antwoord]
        if isinstance(antwoord, list) and len(set(nummers)) < 2:
            raise SystemExit(f"{plek} moet minstens twee juiste antwoorden hebben")
        if len(set(nummers)) != len(nummers):
            raise SystemExit(f"{plek} noemt hetzelfde antwoord twee keer")
        if any(not isinstance(a, int) or not 0 <= a < len(opties) for a in nummers):
            raise SystemExit(f"{plek} wijst een optie aan die niet bestaat")
    elif soort == "waarofniet":
        if not isinstance(vraag["antwoord"], bool):
            raise SystemExit(f"{plek} is waar of niet waar en heeft geen boolean")
    elif soort == "invultekst":
        antwoord = vraag["antwoord"]
        antwoorden = antwoord if isinstance(antwoord, list) else [antwoord]
        if not antwoorden:
            raise SystemExit(f"{plek} heeft geen ingevuld antwoord")
        for a in antwoorden:
            if not isinstance(a, str) or not a.strip():
                raise SystemExit(f"{plek} heeft geen ingevuld antwoord")
            if len(a.split()) > 3:
                raise SystemExit(f"{plek} heeft een te lang invulantwoord: {a!r}")
    else:
        raise SystemExit(f"{plek} heeft een onbekend type: {soort}")
    if not vraag.get("uitleg"):
        raise SystemExit(f"{plek} heeft geen uitleg")


def gokpatronen(titel: str, vragen: list) -> list:
    """Kan je scoren zonder de leerstof te kennen?"""
    meldingen = []
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        lengtes = [len(o) for o in v["opties"]]
        anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
        if anders and min(lengtes[i] for i in antw) > max(anders) + 5:
            langst += 1
    if mk and langst > 0.4 * len(mk):
        meldingen.append(
            f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
            f"antwoord duidelijk de langste optie. Maak de andere opties langer."
        )
    return meldingen


def evenwicht_waar(hoofdstukken: list) -> list:
    """Waar en niet waar moeten elkaar per hoofdstuk in evenwicht houden."""
    meldingen = []
    per_thema = {}
    for h in hoofdstukken:
        for v in h["vragen"]:
            if v["type"] == "waarofniet":
                per_thema.setdefault(h["titel"], []).append(v["antwoord"])
    for thema, antwoorden in per_thema.items():
        waar = sum(1 for a in antwoorden if a)
        if not (0.35 <= waar / len(antwoorden) <= 0.65):
            meldingen.append(
                f"{thema}: {waar} van de {len(antwoorden)} waar/niet-waar-vragen is waar. "
                f"Dat is te scheef om niet te kunnen gokken."
            )
    return meldingen


def hoofdstukken_van(modulenaam: str, thema: str) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        if len(vragen) != 20:
            raise SystemExit(f"{titel} heeft {len(vragen)} vragen, verwacht 20")
        for i, vraag in enumerate(vragen, start=1):
            controleer(titel, i, vraag)
        uit.append(
            {"titel": titel, "niveau": "beyond-dubbele-finaliteit", "gratis": False, "vragen": vragen}
        )
    return uit


def main():
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        if not (HIER / f"{modulenaam}.py").exists():
            print(f"  {thema}: nog niet geschreven, overgeslagen")
            continue
        nieuw = hoofdstukken_van(modulenaam, thema)
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    gezien = {}
    meerkeuze = meerdere = 0
    for h in hoofdstukken:
        for v in h["vragen"]:
            tekst = " ".join(v["vraag"].lower().split())
            if tekst in gezien:
                raise SystemExit(
                    f"Deze vraag staat twee keer, in {gezien[tekst]} en in {h['titel']}:\n  {v['vraag']}"
                )
            gezien[tekst] = h["titel"]
            if v["type"] == "meerkeuze":
                meerkeuze += 1
                if isinstance(v["antwoord"], list):
                    meerdere += 1

    for h in hoofdstukken:
        for melding in gokpatronen(h["titel"], h["vragen"]):
            raise SystemExit(melding)
    for melding in evenwicht_waar(hoofdstukken):
        raise SystemExit(melding)

    # Kim, 23 september 2026: bij wiskunde geen meerkeuze met meerdere juiste
    # antwoorden. Een som heeft één uitkomst; wie er twee laat aankruisen,
    # toetst het lezen van de opgave en niet het rekenen.
    if meerdere:
        raise SystemExit(
            f"{meerdere} meerkeuzevragen hebben meerdere juiste antwoorden; bij wiskunde mag dat niet"
        )
    print(f"\n{meerkeuze} meerkeuzevragen, allemaal met één juist antwoord.")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
