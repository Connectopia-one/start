# -*- coding: utf-8 -*-
"""Zet de themabestanden `fr_*.py` samen in ../frans.json.

    python3 bron/bouw_frans.py

Werkt precies zoals bouw_nederlands.py: elk thema is één bestand met een lijst
DEEL1 en een lijst DEEL2 van twintig vragen, en wordt hier twee hoofdstukken,
"<thema> — deel 1" en "<thema> — deel 2".

Let op: dit vak oefent **alleen het schriftelijke Frans**. Het examen van de
Examencommissie heeft ook luisteren, spreken en een gesprek, en dat kan een
oefenplatform met tekstvragen niet nabootsen. De hoofdstukken hieronder dekken
dus lezen, schrijven, woordenschat en grammatica. Dat staat ook op
/onderwijsdoelen bij het vak, zodat niemand denkt dat dit het hele examen is.

Frans stond nog nergens in de databank, dus er wordt hier niets hernoemd.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "frans.json"

# De volgorde is de volgorde in het platform: eerst lezen (30 % van het
# examen), dan schrijven (16 %), dan de woordenschat en de grammatica die je
# bij allebei nodig hebt. Het beschrijven van een foto staat er apart bij,
# omdat dat op het examen een eigen opdracht is.
THEMAS = [
    ("fr_lezen", "Een Franse tekst lezen"),
    ("fr_tekstsoorten", "Tekstsoorten, signaalwoorden en verwijswoorden"),
    ("fr_schrijven", "Schrijven: berichten, uitnodigingen en mails"),
    ("fr_foto", "Een foto of afbeelding beschrijven"),
    ("fr_mensen", "Woordenschat: mensen, familie, gevoelens en gezondheid"),
    ("fr_dagelijks", "Woordenschat: eten, wonen, kleding en dagelijkse dingen"),
    ("fr_school", "Woordenschat: school, beroepen, sport en vrije tijd"),
    ("fr_tijd", "Woordenschat: getallen, tijd, weer, reizen en landen"),
    ("fr_woordsoorten", "Grammatica: lidwoorden, naamwoorden en voornaamwoorden"),
    ("fr_werkwoorden", "Grammatica: werkwoorden, tijden en zinsbouw"),
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
        if not isinstance(antwoord, str) or not antwoord.strip():
            raise SystemExit(f"{plek} heeft geen ingevuld antwoord")
        if len(antwoord.split()) > 3:
            raise SystemExit(f"{plek} heeft een te lang invulantwoord: {antwoord!r}")
    else:
        raise SystemExit(f"{plek} heeft een onbekend type: {soort}")
    if not vraag.get("uitleg"):
        raise SystemExit(f"{plek} heeft geen uitleg")


def hoofdstukken_van(modulenaam: str, thema: str) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        if len(vragen) != 20:
            raise SystemExit(f"{titel} heeft {len(vragen)} vragen, verwacht 20")
        for i, vraag in enumerate(vragen, start=1):
            controleer(titel, i, vraag)
        meerdere = sum(1 for v in vragen if isinstance(v.get("antwoord"), list))
        if meerdere < 2:
            raise SystemExit(f"{titel} heeft maar {meerdere} vragen met meerdere juiste antwoorden")
        uit.append({"titel": titel, "niveau": "spark", "gratis": False, "vragen": vragen})
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
                raise SystemExit(f"Deze vraag staat twee keer, in {gezien[tekst]} en in {h['titel']}:\n  {v['vraag']}")
            gezien[tekst] = h["titel"]
            if v["type"] == "meerkeuze":
                meerkeuze += 1
                if isinstance(v["antwoord"], list):
                    meerdere += 1

    if meerkeuze:
        deel = meerdere / meerkeuze
        if not 0.20 <= deel <= 0.30:
            raise SystemExit(f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 20 à 30 %")
        print(f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden.")

    DOEL.write_text(json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
