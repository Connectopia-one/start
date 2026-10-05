# -*- coding: utf-8 -*-
"""Zet de thema's samen in ../natuurwetenschappen.json.

    python3 bron/bouw_natuurwetenschappen.py

Boost dubbele finaliteit, tweede graad. Eén vakfiche voor bedrijf en
organisatie en voor maatschappij en welzijn. Ze weegt haar onderdelen zelf:
biologie 25 %, chemie 25 %, fysica 40 %, en wetenschappelijk onderzoek en
STEM 10 %. Dertien thema's in de verhouding drie, drie, vijf en twee komen
daar het dichtst bij, met het levensreddend handelen bij het thema over
veilig werken, zoals bij doorstroom.

Dit vak leunt op de thema's van 🚀 Boost doorstroom, maar de fysica is er een
pak lichter. Wat de fiche niet vraagt, wordt vervangen: arbeid, de formules
van de kinetische, gravitationele en elastische energie, de specifieke
warmtecapaciteit, de latente warmte, het warmtetransport, de vrije val, de
verticale worp, de veerconstante, de zwaarteveldsterkte, de hydrostatische
druk, het beginsel van Pascal en de gaswetten met de kelvinschaal. Achteraan
zegt de fiche uitdrukkelijk welke vier formules je moet kennen, en dat zijn
P = |ΔE| / Δt, het rendement, p = F / A en R = U / I.

Bij biologie zet de fiche de prikkels, de hormonen en de klieren samen onder
één kop, "Biologische feedback", terwijl doorstroom ze over drie thema's
spreidt. Daarom is dat hier een eigen bestand, `nwdf_feedback.py`, en geen
uitgedund doorstroomthema. De indeling van het leven (driedomeinensysteem,
vijfrijkensysteem) valt weg, en wat de fiche over micro-organismen wél zet
(de bouw, de weg waarlangs ze binnendringen) komt in de plaats.

De vervangingen staan in `df_natuurwetenschappen_vervangingen.py`. Achteraan
loopt er nog een controle over het hele bestand: er mag geen woord uit de
doorstroomfiche blijven staan dat hier niet thuishoort.

Verder precies als de andere vakken van deze categorie: twintig vragen per
deel, elk thema wordt twee hoofdstukken, geen woordelijke dubbels in het hele
vak, 20 à 30 % meerkeuzevragen met meerdere juiste antwoorden, en geen
raadbare patronen.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
DOORSTROOM = HIER.parent.parent / "boost-doorstroom" / "bron"
sys.path.insert(0, str(DOORSTROOM))
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "natuurwetenschappen.json"

import df_natuurwetenschappen_vervangingen as vervang  # noqa: E402

# De volgorde volgt de fiche: eerst biologie, dan chemie, dan fysica, en
# achteraan het veilig werken en het onderzoek.
THEMAS = [
    ("nwdf_feedback", "Biologische feedback en homeostase"),
    ("nw_micro", "Micro-organismen, het microbioom en bewaring"),
    ("nw_voortplanting", "Voortplanting en de hormonale regeling"),
    ("nw_mengsels", "Mengsels en zuivere stoffen"),
    ("nw_stoffen", "Chemische formules en chemische reacties"),
    ("nw_atoom", "De bouw van het atoom en het periodiek systeem"),
    ("nw_energie", "Energieomzettingen, vermogen en rendement"),
    ("nw_warmte", "Warmte, faseovergangen en inwendige energie"),
    ("nw_krachten", "Kracht als vector en bewegingstoestand"),
    ("nw_druk", "Druk in het dagelijkse leven"),
    ("nw_elektriciteit", "Elektriciteit, de wet van Ohm en veiligheid"),
    ("nw_veilig", "Veilig werken, meten en levensreddend handelen"),
    ("nw_onderzoek", "Grootheden, eenheden en wetenschappelijk onderzoek"),
]

# Woorden die bij de doorstroomfiche horen en niet bij deze. Staat er toch nog
# een, dan is er een vraag of een uitleg over het hoofd gezien.
VERBODEN = [
    "arbeid",
    "valversnelling",
    "vrije val",
    "verticale worp",
    "veerconstante",
    "zwaarteveldsterkte",
    "warmtecapaciteit",
    "latente warmte",
    "merkbare warmte",
    "calorimeter",
    "warmtetransport",
    "warmtegeleiding",
    "convectie",
    "hydrostatisch",
    "beginsel van pascal",
    "wet van pascal",
    "kelvin",
    "isotherm",
    "isochoor",
    "isobaar",
    "ideaal gas",
    "ideale gas",
    "driedomeinen",
    "vijfrijken",
    "prokaryo",
    "eukaryo",
    "relatieve atoommassa",
    "absolute massa",
    "atoommassa-eenheid",
    "de vakfiche",
    "de leerstof",
]


def verboden_woorden(hoofdstukken: list) -> list:
    meldingen = []
    for h in hoofdstukken:
        for nummer, v in enumerate(h["vragen"], start=1):
            stukken = [v["vraag"], v.get("uitleg", "")]
            stukken += list(v.get("opties", []))
            antwoord = v.get("antwoord")
            if isinstance(antwoord, str):
                stukken.append(antwoord)
            elif isinstance(antwoord, list):
                stukken += [a for a in antwoord if isinstance(a, str)]
            tekst = " ".join(stukken).lower()
            for woord in VERBODEN:
                if woord in tekst:
                    meldingen.append(
                        f"{h['titel']}: vraag {nummer} gebruikt nog {woord!r}, "
                        f"en dat staat niet in deze fiche."
                    )
    return meldingen


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


def hoofdstukken_van(modulenaam: str, thema: str, nog_te_vervangen: dict) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        nieuw = []
        for vraag in vragen:
            sleutel = " ".join(vraag["vraag"].split())
            nieuw.append(nog_te_vervangen.pop(sleutel) if sleutel in nog_te_vervangen else vraag)
        if len(nieuw) != 20:
            raise SystemExit(f"{titel} heeft {len(nieuw)} vragen, verwacht 20")
        for i, vraag in enumerate(nieuw, start=1):
            controleer(titel, i, vraag)
        uit.append(
            {
                "titel": titel,
                "niveau": "boost-dubbele-finaliteit",
                "gratis": False,
                "vragen": nieuw,
            }
        )
    return uit


def main():
    nog_te_vervangen = dict(vervang.VERVANGINGEN)
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        nieuw = hoofdstukken_van(modulenaam, thema, nog_te_vervangen)
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    if nog_te_vervangen:
        raise SystemExit(
            "Deze te vervangen vragen staan niet (meer) in de doorstroombestanden:\n  "
            + "\n  ".join(nog_te_vervangen)
        )

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


    for melding in verboden_woorden(hoofdstukken):
        raise SystemExit(melding)
    print("Niets uit de doorstroomfiche blijven staan.")


if __name__ == "__main__":
    main()
