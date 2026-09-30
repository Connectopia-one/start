# -*- coding: utf-8 -*-
"""Zet de thema's samen in ../nederlands.json.

    python3 bron/bouw_nederlands.py

Boost dubbele finaliteit, tweede graad. Eén vakfiche voor bedrijf en
organisatie en voor maatschappij en welzijn. Bij doorstroom zijn het er twee
(Nederlands 1 en Nederlands 2); hier is alles in één fiche gegoten, en het
gewicht ligt heel anders:

    lezen, luisteren en taalbeschouwing   60 %
    schrijven en schriftelijke interactie 16 %
    gesprekken                            16 %
    spreken                                8 %

Negen thema's komen uit de doorstroombron: het communicatiemodel, de
tekstsoorten, de samenhang van een tekst, bronkritiek, taalvariatie, de
woordsoorten, de werkwoorden, de zinsdelen, de spelling en de betekenis.
Die leerstof staat woord voor woord ook op de DF-fiche.

Drie thema's zijn hier nieuw geschreven, want de doorstroomversie past niet:

  * **Argumenteren.** Deel 2 van doorstroom gaat bijna helemaal over
    drogredenen (cirkelredenering, vals dilemma, hellend vlak). Die staan
    níét op de DF-fiche. Die vraagt: het verschil tussen feit en mening,
    stelling, standpunt, argument en conclusie, en zelf argumenteren.
  * **Literatuur.** Doorstroom heeft twee thema's over verteller, verteltijd,
    rijmschema, toneel en literaire stromingen. De DF-fiche vraagt enkel
    fictie, non-fictie, personages, verhaallijn, tijd en ruimte, en dat je je
    eigen beleving kan verwoorden.
  * **Communiceren.** De DF-fiche besteedt 24 % aan spreken en gesprekken en
    zet daar leerstof bij die bij doorstroom niet zo staat: non-verbale
    communicatie, beleefdheidsconventies en de criteria waaraan een tekst of
    een spreekopdracht moet voldoen.

Spreken en een gesprek voeren zelf oefen je niet achter een scherm; wat je er
wél over moet weten, staat in dat laatste thema.

Vragen uit de doorstroommodules kunnen hier één voor één vervangen worden via
`df_nederlands_vervangingen.py`, op dezelfde manier als bij geschiedenis: de
sleutel is de letterlijke vraagtekst, en staat ze er niet meer, dan stopt het
script.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
DOORSTROOM = HIER.parent.parent / "boost-doorstroom" / "bron"
sys.path.insert(0, str(DOORSTROOM))
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "nederlands.json"

import df_nederlands_vervangingen as vervang  # noqa: E402

# De volgorde loopt van de tekst als geheel naar de bouwstenen en dan naar het
# spreken: eerst wat een tekst wil en hoe hij in elkaar zit, dan hoe je hem
# weegt, dan het taalsysteem zelf, dan literatuur en communicatie.
THEMAS = [
    ("nl_communicatie", "Zender, ruis en de zeven tekstsoorten"),
    ("nl_samenhang", "Hoofdgedachte, alinea en structuuraanduiders"),
    ("nldf_argumenteren", "Feit en mening, stelling, argument en conclusie"),
    ("nl_bronkritiek", "Bronnen wegen: objectief, gekleurd of nep"),
    ("nl_variatie", "Standaardtaal, tussentaal en register"),
    ("nl_woordsoorten", "De woordsoorten op een rij"),
    ("nl_werkwoorden", "Werkwoorden, tijden en woordvorming"),
    ("nl_zinsdelen", "Zinsdelen en samengestelde zinnen"),
    ("nl_spelling", "Spelling, leestekens en klanken"),
    ("nl_betekenis", "Betekenis, beeldspraak en gevoelswaarde"),
    ("nldf_literatuur", "Fictie, personages, verhaallijn, tijd en ruimte"),
    ("nldf_communiceren", "Lichaamstaal, beleefdheid en een tekst die werkt"),
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


if __name__ == "__main__":
    main()
