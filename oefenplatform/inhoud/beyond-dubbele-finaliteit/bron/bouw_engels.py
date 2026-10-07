# -*- coding: utf-8 -*-
"""Zet de themabestanden `en2_*.py` samen in ../engels.json.

    python3 bron/bouw_engels.py

🌍 Beyond, derde graad dubbele finaliteit. Er zijn twee vakfiches, Engels 1 en
Engels 2, en ze gelden allebei voor commerciële organisatie en voor de
basisvorming van de dubbele finaliteit; dat staat bovenaan op de fiches zelf.
Het ERK-niveau is A2+, dus een stap lager dan de B1 van het Engels van de
doorstroomrichtingen.

Eén vak voor twee fiches. Engels 1 is een digitaal examen van 120 minuten over
lezen en luisteren. Engels 2 bestaat uit een spreekopdracht die je thuis
opneemt, schrijfopdrachten op het digitale examen en een gesprek. De
woordvelden en de grammaticalijst achter de twee examens zijn zo goed als
dezelfde.

**Wat hier níét in zit:** luisteren, spreken en het gesprek. Die vragen geluid
en een gesprekspartner, en dat kan een platform met tekstvragen niet nabootsen.
Wat je erover moet weten, de vereisten en de strategieën, staat wel in het
thema over schrijven.

De grammaticalijst van deze fiche is korter dan die van de doorstroomrichting:
geen gerund, geen semi-auxiliaries, geen indirecte rede, geen passieve vorm en
geen past perfect. Wat er wel in staat, staat hier: de present perfect simple
en continuous, de past simple en continuous, de drie manieren om over de
toekomst te spreken, de modalen, en de conditionals zero en first.

Elke leesvraag staat op een echt Engels tekstje. Een vraag over lezen zonder
tekst is geen leesvraag.

Werkt zoals de andere bouwscripts: elk thema is een bestand met een lijst DEEL1
en een lijst DEEL2 van twintig vragen, en wordt hier twee hoofdstukken,
"<thema> — deel 1" en "<thema> — deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "engels.json"

# De volgorde loopt van de vaardigheden naar het materiaal: eerst lezen en
# schrijven, dan de cultuur die de fiche uitdrukkelijk vraagt, dan de
# woordvelden, en ten slotte de grammatica in de volgorde van de lijst zelf.
THEMAS = [
    ("en2_lezen", "Een Engelse tekst lezen"),
    ("en2_tekstsoorten", "Tekstsoorten en de bedoeling van een tekst"),
    ("en2_cultuur", "De Engelstalige wereld: gewoontes en reizen"),
    ("en2_schrijven", "Schrijven, spreken en je beleving bij een tekst"),
    ("en2_dagelijks", "Woordvelden: dagelijks leven, eten en wonen"),
    ("en2_gezondheid", "Woordvelden: gezondheid, natuur en duurzaamheid"),
    ("en2_school", "Woordvelden: school, werk, geld en verkeer"),
    ("en2_kunst", "Woordvelden: kunst, geschiedenis en de samenleving"),
    ("en2_wetenschap", "Woordvelden: wetenschap, techniek en taal"),
    ("en2_naamwoorden", "Naamwoorden, lidwoorden en hoeveelheden"),
    ("en2_voornaamwoorden", "Voornaamwoorden en betrekkelijke bijzinnen"),
    ("en2_adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en voorzetsels"),
    ("en2_tegenwoordig", "De tegenwoordige tijden en de present perfect"),
    ("en2_verleden", "De verleden tijden"),
    ("en2_toekomst", "De toekomende tijd en de modale hulpwerkwoorden"),
    ("en2_zinsbouw", "Zinsbouw, zinsdelen en de voorwaardelijke bijzin"),
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
