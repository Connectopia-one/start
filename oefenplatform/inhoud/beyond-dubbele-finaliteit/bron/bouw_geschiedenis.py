# -*- coding: utf-8 -*-
"""Zet de themabestanden `gs_*.py` samen in ../geschiedenis.json.

    python3 bron/bouw_geschiedenis.py

🌍 Beyond dubbele finaliteit, derde graad. Eén vakfiche, "3 dubbele
finaliteit", geldig van 1 januari 2027 tot en met 31 december 2027. Ze geldt
voor commerciële organisatie en voor de algemene vorming dubbele finaliteit;
dat staat bovenaan op de fiche, lees het af in plaats van het te gokken.

De fiche geeft achteraan zelf de gewichten van het examen:

    het historisch referentiekader              7,5 %
    samenlevingen in de moderne tijd           32,5 %
    samenlevingen in de hedendaagse tijd       25   %
    vergelijkingen kenmerken en samenlevingen   5   %
    bronnen                                    20   %
    beeldvorming                                5   %
    relatie verleden - heden - toekomst         5   %

Daar zijn de twintig thema's naar verdeeld: twee voor het referentiekader en
het vergelijken, elf voor de moderne tijd, vier voor de hedendaagse tijd, en
drie voor het werk met bronnen, de beeldvorming en de betekenisgeving. De
moderne tijd krijgt er het meest, want daar staat ook het meeste in: van het
Congres van Wenen tot de Holocaust.

Twee blokken van de fiche verdienen een woord. De kunststromingen zijn een
keuzelijst: een kandidaat kiest er één om voor te bereiden. De vragen hier
toetsen dus het stappenplan en de kenmerken van de stromingen in het
algemeen, en vragen nooit om één stroming van buiten te kennen. En het werk
met bronnen is een stappenplan, geen jaartal: die vragen gaan over
bruikbaarheid, betrouwbaarheid en de redeneerwijzen, met telkens een klein
stukje bron of context in de vraag zelf.

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
DOEL = HIER.parent / "geschiedenis.json"

# De volgorde volgt de fiche: eerst het gereedschap om in tijd, ruimte en
# domeinen te situeren, dan de moderne tijd van 1815 tot 1945, dan de
# hedendaagse tijd, en achteraan het werk met bronnen en beeldvorming, dat op
# alles wat ervoor staat toegepast wordt.
THEMAS = [
    ("gs_referentiekader", "Het historisch referentiekader: tijd, ruimte en domeinen"),
    ("gs_vergelijken", "Kenmerken van samenlevingen vergelijken"),
    ("gs_wenen", "Restauratie en revolutie: het Congres van Wenen"),
    ("gs_liberalisme", "Liberalisme en nationalisme"),
    ("gs_belgie", "Het ontstaan van België"),
    ("gs_industrie", "De eerste en de tweede industriële revolutie"),
    ("gs_ongelijkheid", "Ongelijkheden: klassenmaatschappij en sociale strijd"),
    ("gs_ideologie", "Marxisme, sociaaldemocratie, christendemocratie en migratie"),
    ("gs_imperialisme", "Modern imperialisme en de wedloop om Afrika"),
    ("gs_congo", "Congo: van Congo-Vrijstaat tot Belgisch Congo"),
    ("gs_wo1", "De Eerste Wereldoorlog en de Vrede van Versailles"),
    ("gs_interbellum", "Het interbellum: de opkomst van het totalitarisme"),
    ("gs_wo2", "De Tweede Wereldoorlog en de Holocaust"),
    ("gs_china", "China: van keizerrijk tot wereldmacht"),
    ("gs_wereldorde", "Een nieuwe wereldorde: de Verenigde Naties en de Koude Oorlog"),
    ("gs_europa", "De Europese eenmaking"),
    ("gs_dekolonisatie", "De dekolonisatie van Congo"),
    ("gs_naoorlogs", "België na 1945: breuklijnen, federale staat en emancipatie"),
    ("gs_kunst", "Kunst en cultuur: een kunstwerk analyseren"),
    ("gs_bronnen", "Redeneren met bronnen: bruikbaarheid en betrouwbaarheid"),
    ("gs_beeldvorming", "Beeldvorming, standplaatsgebondenheid en betekenisgeving"),
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
