# -*- coding: utf-8 -*-
"""Zet de themabestanden `ch_*.py` samen in ../chemie.json.

    python3 bron/bouw_chemie.py

Boost doorstroom, tweede graad. De vakfiche chemie van de doorstroomfinaliteit
geldt enkel voor de studierichting natuurwetenschappen: die richting legt haar
wetenschappen af in drie aparte examens, biologie, chemie en fysica, in plaats
van één examen natuurwetenschappen.

De verdeling van de thema's volgt de gewichten achteraan op de fiche: opbouw
van materie 10 % (twee thema's), chemische reacties 5 % (één), atoom- en
molecuulbouw 20 % (drie), organische en anorganische stoffen 40 % (vier),
berekeningen 15 % (één) en wetenschappelijk onderzoek en STEM 10 % (één).

Twee afspraken van de fiche zelf zijn hier overgenomen, omdat bronnen erover
verschillen: een binding met een verschil in elektronegativiteit onder 0,4 geldt
als apolair, en de relatieve atoommassa wordt op 0,1 afgerond. De vragen blijven
binnen de tabellen die een kind op het examen mag gebruiken: de
oplosbaarheidstabel, de tabel met oxidatiegetallen, de twee indicatoren
fenolftaleïne en lakmoes, en het getal van Avogadro 6,02.10²³ per mol.

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
DOEL = HIER.parent / "chemie.json"

# De volgorde volgt de fiche. Drie thema's voor de atoom- en molecuulbouw
# (20 %), vier voor de organische en anorganische stoffen (40 %), en één of twee
# voor elk van de andere koppen: samen twaalf thema's.
THEMAS = [
    ("ch_mengsels", "Mengsels, zuivere stoffen en scheidingstechnieken"),
    ("ch_stoffen", "Enkelvoudige en samengestelde stoffen"),
    ("ch_reacties", "Chemische reacties en energie"),
    ("ch_atoom", "De bouw van atomen en ionen"),
    ("ch_pse", "Het periodiek systeem der elementen"),
    ("ch_bindingen", "Chemische bindingen en roosters"),
    ("ch_anorganisch", "Anorganische stofklassen en naamgeving"),
    ("ch_organisch", "Organische stoffen en de alkanen"),
    ("ch_water", "Stoffen in water: polariteit, oplossen en pH"),
    ("ch_reactietypes", "Neerslag-, gas-, neutralisatie- en redoxreacties"),
    ("ch_rekenen", "Rekenen met mol, massa en concentratie"),
    ("ch_onderzoek", "Veilig werken, meten en onderzoek"),
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
