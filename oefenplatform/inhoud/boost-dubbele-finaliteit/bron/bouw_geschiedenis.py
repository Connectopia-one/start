# -*- coding: utf-8 -*-
"""Zet geschiedenis voor 🚀 Boost dubbele finaliteit samen in ../geschiedenis.json.

    python3 bron/bouw_geschiedenis.py

De vakfiche geschiedenis van de 2de graad **dubbele finaliteit**, geldig vanaf
1 januari 2027, geldt voor bedrijf en organisatie en voor maatschappij en
welzijn. Ze is voor 85 % dezelfde fiche als die van de doorstroomfinaliteit:
dezelfde zeven bouwstenen, bijna dezelfde gewichten (enkel het historisch
referentiekader gaat van 7,5 naar 10 % en bronnen van 17,5 naar 15 %) en
dezelfde elf onderwerpen.

Daarom bouwt dit script niet opnieuw. Het neemt de elf themabestanden `gs_*.py`
van de doorstroomfinaliteit over en past twee dingen aan:

1. het niveau wordt `boost-dubbele-finaliteit`;
2. elke vraag die draait om een begrip dat de DF-fiche **niet** noemt, wordt
   vervangen door een vraag over leerstof die er wél op staat.

Wat de DF-fiche laat vallen: koopkracht en levensstandaard, het domein als
zelfvoorzienend systeem, het ontstaan van de geldeconomie, het
encomiendasysteem, het handelskapitalisme en het mercantilisme, de oorzaken van
de bevolkingsgroei, de vernieuwing van de wetenschappelijke methode en de
organisatie van de katholieke Kerk als apart leerinhoud.

Wat ze daarbovenop vraagt en de doorstroomfiche niet: Bagdad als kruispunt van
internationale handel, en het standpunt over slavenhandel vergelijken in
verschillende bronnen. Die twee vervangen elk een vraag hierboven.

Zet je hier iets bij, leg het dan eerst naast de DF-fiche zelf. Een vraag die
enkel op de doorstroomfiche staat, hoort hier niet.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
DOORSTROOM = HIER.parent.parent / "boost-doorstroom" / "bron"
sys.path.insert(0, str(DOORSTROOM))
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "geschiedenis.json"

# Dezelfde elf thema's als bij de doorstroomfinaliteit.
THEMAS = [
    ("gs_kader", "Het historisch referentiekader"),
    ("gs_franken", "Van Rome naar de Franken"),
    ("gs_standen", "Standen, domein en stad"),
    ("gs_geloof", "Geloof, kunst en macht in de middeleeuwen"),
    ("gs_nieuwewereld", "De 'Nieuwe' Wereld en de driehoekshandel"),
    ("gs_humanisme", "Humanisme, Reformatie, renaissance en barok"),
    ("gs_vorsten", "Vorsten, opstand en de Verlichting"),
    ("gs_revoluties", "Amerika, Frankrijk en de industriële omwenteling"),
    ("gs_ottomaans", "Het Ottomaanse Rijk en samenlevingen vergelijken"),
    ("gs_bronnen", "Redeneren met historische bronnen"),
    ("gs_vandaag", "Beeldvorming en het verleden vandaag"),
]

import df_geschiedenis_vervangingen as vervang


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


def main():
    nog_te_vervangen = dict(vervang.VERVANGINGEN)
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        mod = importlib.import_module(modulenaam)
        for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
            titel = f"{thema} — deel {nummer}"
            nieuw = []
            for vraag in vragen:
                sleutel = " ".join(vraag["vraag"].split())
                if sleutel in nog_te_vervangen:
                    nieuw.append(nog_te_vervangen.pop(sleutel))
                else:
                    nieuw.append(vraag)
            if len(nieuw) != 20:
                raise SystemExit(f"{titel} heeft {len(nieuw)} vragen, verwacht 20")
            for i, vraag in enumerate(nieuw, start=1):
                controleer(titel, i, vraag)
            hoofdstukken.append(
                {"titel": titel, "niveau": "boost-dubbele-finaliteit",
                 "gratis": False, "vragen": nieuw}
            )
        print(f"  {thema}: 40 vragen")

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

    deel = meerdere / meerkeuze
    if not 0.20 <= deel <= 0.30:
        raise SystemExit(
            f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 20 à 30 %"
        )
    print(f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden.")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
