# -*- coding: utf-8 -*-
"""Zet de themabestanden `nl_*.py` samen in ../nederlands.json.

    python3 bron/bouw_nederlands.py

Werkt precies zoals bouw_natuurwetenschappen.py: elk thema is één bestand met
een lijst DEEL1 en een lijst DEEL2 van twintig vragen, en wordt hier twee
hoofdstukken, "<thema> — deel 1" en "<thema> — deel 2".

Nederlands had op ✨ Spark nog geen hoofdstuk in de databank staan — het
voorbeeldhoofdstuk uit supabase/schema.sql staat op 🌱 Start — dus er wordt
hier niets hernoemd.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "nederlands.json"

# De volgorde is de volgorde in het platform. Ze volgt de vakfiche: eerst wat
# je nodig hebt om te lezen en te luisteren (samen 60 % van het examen), dan
# schrijven, spreken en gesprekken (32 %), dan literatuur, en ten slotte de
# ondersteunende kennis over het taalsysteem, die je bij alles nodig hebt.
THEMAS = [
    ("nl_hoofdgedachte", "Onderwerp, hoofdgedachte en hoofdpunten"),
    ("nl_tekstsoorten", "Tekstsoorten en het communicatiemodel"),
    ("nl_betrouwbaar", "Feiten, meningen en betrouwbaarheid"),
    ("nl_structuur", "Tekststructuur en signaalwoorden"),
    ("nl_schrijven", "Schrijven, spreken en gesprekken voeren"),
    ("nl_register", "Register, taalvariatie en non-verbale communicatie"),
    ("nl_literatuur", "Literatuur en beeldspraak"),
    ("nl_spelling", "Spelling, leestekens en werkwoordsvormen"),
    ("nl_woordsoorten", "Woordsoorten en woordvorming"),
    ("nl_zinnen", "Zinsdelen, zinssoorten en congruentie"),
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


def gokpatronen(titel: str, vragen: list) -> list:
    """Kan je scoren zonder de leerstof te kennen?

    Het juiste antwoord krijgt bij het schrijven vanzelf de meeste uitleg mee
    en wordt daardoor de langste optie. Een verschil van een paar letters ziet
    een kind niet, dus een vraag telt pas mee als het juiste antwoord er
    minstens zes langer is dan elke foute optie.
    """
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
    """Waar en niet waar moeten elkaar in evenwicht houden.

    Een juiste zin schrijft vlotter dan een foute, dus komt het antwoord
    vanzelf te vaak op waar uit en loont het om altijd waar te antwoorden. We
    tellen per thema, over deel 1 en deel 2 samen, en daarnaast over het hele
    vak. Een thema met minder dan vier van die vragen slaan we over: daar zegt
    een verhouding niets, want ze kan niet eens tussen de grenzen vallen.
    """
    meldingen = []
    per_thema = {}
    for h in hoofdstukken:
        thema = h["titel"].split(" — ")[0]
        for v in h["vragen"]:
            if v["type"] == "waarofniet":
                per_thema.setdefault(thema, []).append(v["antwoord"])
    alles = [a for lijst in per_thema.values() for a in lijst]
    for thema, antwoorden in per_thema.items():
        if len(antwoorden) < 4:
            continue
        waar = sum(1 for a in antwoorden if a)
        if not (0.35 <= waar / len(antwoorden) <= 0.65):
            meldingen.append(
                f"{thema}: {waar} van de {len(antwoorden)} waar/niet-waar-vragen is waar. "
                f"Dat is te scheef om niet te kunnen gokken."
            )
    if alles:
        waar = sum(1 for a in alles if a)
        if not (0.35 <= waar / len(alles) <= 0.65):
            meldingen.append(
                f"over het hele vak: {waar} van de {len(alles)} waar/niet-waar-vragen is waar."
            )
    return meldingen


def main():
    hoofdstukken = []
    meldingen = []
    for modulenaam, thema in THEMAS:
        if not (HIER / f"{modulenaam}.py").exists():
            print(f"  {thema}: nog niet geschreven, overgeslagen")
            continue
        nieuw = hoofdstukken_van(modulenaam, thema)
        for h in nieuw:
            meldingen += gokpatronen(h["titel"], h["vragen"])
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    meldingen += evenwicht_waar(hoofdstukken)
    if meldingen:
        raise SystemExit("Zo valt er te raden:\n  - " + "\n  - ".join(meldingen))

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
