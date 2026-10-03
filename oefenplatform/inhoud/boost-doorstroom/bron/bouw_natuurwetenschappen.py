# -*- coding: utf-8 -*-
"""Zet de themabestanden `nw_*.py` samen in ../natuurwetenschappen.json.

    python3 bron/bouw_natuurwetenschappen.py

Boost doorstroom, tweede graad. Er zijn **twee** vakfiches natuurwetenschappen
voor de doorstroomfinaliteit van de tweede graad, en ze staan allebei bovenaan
zelf wie ze gebruikt: de ene (50 blz) voor economische wetenschappen en humane
wetenschappen, de andere (53 blz) voor moderne talen en Latijn. Op 3 oktober
2026 zin per zin vergeleken: 440 van de 585 zinnen zijn letterlijk gelijk, de
hoofdstukken zijn dezelfde, en alles uit de eerste staat ook in de tweede. Dit
vak volgt daarom de uitgebreide fiche; wat daar bovenop komt (de gaswetten,
arbeid, redoxreacties, neerslag- en neutralisatiereacties, Lewisstructuren,
de absolute massa, het driedomeinen- en vijfrijkensysteem, het transport van
water en assimilaten, en de rust- en actiepotentiaal) staat in eigen thema's
of in een eigen deel, zodat wie de kortere fiche volgt die kan overslaan.

De verdeling van de thema's volgt de gewichten achteraan op de fiche: biologie
30 %, chemie 30 %, fysica 30 %, wetenschappelijk onderzoek en STEM 10 %.

Elk thema is een bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen. Dit script maakt daar twee hoofdstukken van, "<thema> — deel 1" en
"<thema> — deel 2", en schrijft het importbestand van nul af aan.

Dezelfde bewaking als bij de andere vakken: twintig vragen per deel, geen
woordelijke dubbels in het hele vak, minstens drie opties per meerkeuzevraag,
20 à 30 % vragen met meerdere juiste antwoorden, en geen raadbare patronen
(het juiste antwoord dat altijd de langste is, of waar dat te vaak waar is).
"""

import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "natuurwetenschappen.json"

# De volgorde volgt de fiche: eerst biologie, dan chemie, dan fysica, en
# achteraan wetenschappelijk onderzoek en STEM. Zeven thema's biologie, zes
# chemie, zes fysica en twee onderzoek: samen eenentwintig, in de verhouding
# van de gewichten op de fiche.
THEMAS = [
    ("nw_planten", "Water en homeostase bij planten"),
    ("nw_prikkel", "Van prikkel tot reactie, en het oog"),
    ("nw_zenuwstelsel", "Het zenuwstelsel"),
    ("nw_spieren", "Spieren, klieren en hormonen"),
    ("nw_voortplanting", "Voortplanting en de hormonale regeling"),
    ("nw_micro", "Biodiversiteit en micro-organismen"),
    ("nw_ecosysteem", "Gedrag, interactie en ecosystemen"),
    ("nw_mengsels", "Mengsels en zuivere stoffen"),
    ("nw_stoffen", "Enkelvoudige en samengestelde stoffen, en chemische reacties"),
    ("nw_atoom", "De bouw van het atoom en het periodiek systeem"),
    ("nw_binding", "Chemische bindingen en roosters"),
    ("nw_namen", "Stoffen classificeren en benoemen"),
    ("nw_water", "Stoffen in water, reacties en berekeningen"),
    ("nw_beweging", "Rechtlijnige bewegingen"),
    ("nw_krachten", "Vrije val, verticale worp en krachten"),
    ("nw_druk", "Druk en de gaswetten"),
    ("nw_energie", "Arbeid, energie, vermogen en rendement"),
    ("nw_warmte", "Warmte en faseovergangen"),
    ("nw_elektriciteit", "Elektriciteit en de wet van Ohm"),
    ("nw_veilig", "Veilig werken, meten en levensreddend handelen"),
    ("nw_onderzoek", "Grootheden, eenheden en wetenschappelijk onderzoek"),
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
    """Waar en niet waar moeten elkaar per hoofdstuk in evenwicht houden.

    Per hóófdstuk, niet per thema. Een kind maakt één hoofdstuk in één keer,
    dus daar moet het gokken niet lonen. `inhoud/controleer_patronen.py` kijkt
    op diezelfde manier; stonden die twee niet gelijk, dan kwam een scheef
    hoofdstuk hier door en pas veel later daar boven water.
    """
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
            {"titel": titel, "niveau": "boost-doorstroom", "gratis": False, "vragen": vragen}
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

    if meerkeuze:
        deel = meerdere / meerkeuze
        if not 0.20 <= deel <= 0.30:
            raise SystemExit(
                f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 20 à 30 %"
            )
        print(
            f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden."
        )

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
