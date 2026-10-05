# -*- coding: utf-8 -*-
"""Zet de thema's samen in ../aardrijkskunde.json.

    python3 bron/bouw_aardrijkskunde.py

Boost dubbele finaliteit, tweede graad. Eén vakfiche voor maatschappij en
welzijn en voor bedrijf en organisatie. Ze weegt haar onderdelen zelf, en
precies zoals bij doorstroom: situeren 10 %, bevolking 20 %, stad en
platteland 10 %, economische processen 20 %, mondialisering 10 %,
duurzaamheid 10 %, het versterkte broeikaseffect 10 % en geografisch
onderzoek 10 %. De twee rubrieken van 20 % krijgen dus twee thema's, de rest
elk één. Samen tien, net als bij doorstroom.

Dit vak leunt op de thema's van 🚀 Boost doorstroom. De rubrieken zijn
dezelfde, maar deze fiche gaat minder diep. Wat ze niet vraagt, wordt
vervangen: de Human Development Index, het vruchtbaarheidscijfer, het
migratiesaldo, het demografisch transitiemodel met zijn fasen, de hiërarchie
van steden, inbreiding, stadslandbouw, protectionisme, outsourcing,
reconversie, bodemerosie, bodemdegradatie, de stralingsbalans en het albedo.

In de plaats komt wat ze wél zet: de scholingsgraad als sociaaleconomische
factor, de bevolkingsdichtheid uit bronnen lezen, de beïnvloedende factoren
op een rij, de koolstofcyclus tussen de vier sferen, en de SDG's naast de
vijf P's.

De vervangingen staan in `df_aardrijkskunde_vervangingen.py`. Achteraan loopt
er nog een controle over het hele bestand: er mag geen woord uit de
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
DOEL = HIER.parent / "aardrijkskunde.json"

import df_aardrijkskunde_vervangingen as vervang  # noqa: E402

# De volgorde en het aantal thema's volgen de gewichten van de fiche.
THEMAS = [
    ("ak_situeren", "Waar ligt het, en hoe weet je dat?"),
    ("ak_wonen", "Waar wonen de mensen?"),
    ("ak_bevolking", "Hoe een bevolking verandert"),
    ("ak_stad", "Stad en platteland"),
    ("ak_grondstoffen", "Grondstoffen, energie en industrie"),
    ("ak_landbouw", "Landbouw, handel en toerisme"),
    ("ak_mondialisering", "Mondialisering"),
    ("ak_duurzaam", "Duurzaam omgaan met de ruimte"),
    ("ak_broeikas", "Het versterkte broeikaseffect"),
    ("ak_onderzoek", "Een geografisch onderzoek voeren"),
]

# Woorden die bij de doorstroomfiche horen en niet bij deze. Staat er toch nog
# een, dan is er een vraag of een uitleg over het hoofd gezien.
VERBODEN = [
    "human development",
    "hdi",
    "vruchtbaarheidscijfer",
    "migratiesaldo",
    "demografische transitie",
    "demografisch transitiemodel",
    "transitiemodel",
    "bevolkingsstructuur",
    "hiërarchie",
    "inbreiding",
    "stadslandbouw",
    "outsourcing",
    "uitbesteding",
    "delokalisatie",
    "protectionisme",
    "vrijhandel",
    "reconversie",
    "bodemerosie",
    "bodemdegradatie",
    "stralingsbalans",
    "albedo",
    "tropische ziekte",
    "de vakfiche",
    "de fiche",
    "deze fiche",
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
