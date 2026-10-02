# -*- coding: utf-8 -*-
"""Zet de themabestanden `wi_*.py` samen in ../wiskunde-gevorderd.json.

    python3 bron/bouw_wiskunde.py

🌍 Beyond, derde graad. Kim stuurde dríé vakfiches voor dit vak: G1, G2 en G3,
alle drie "3 doorstroomfinaliteit" en alle drie geldig van 1 januari 2027 tot
en met 31 december 2027. Ze gelden alle drie voor exact dezelfde richtingen:
economie-wiskunde, Latijn-wiskunde-wetenschappen en wetenschappen-wiskunde.
Dat staat bovenaan op elke fiche; lees het af in plaats van het te gokken.

Drie fiches voor hetzelfde vak worden bij ons één vak, net zoals Nederlands 1
en 2. Het heet **wiskunde gevorderd**, dezelfde naam als bij Boost, want de
andere derdegraadsrichtingen (humane wetenschappen, moderne talen, Latijn-
moderne talen) volgen wiskunde basis, een fiche die we nog niet hebben.

Twee en twintig thema's, verdeeld naar wat elke fiche vraagt en naar de
gewichtentabel die G2 en G3 achteraan zelf geven:

    G1  analyse                                 100 %  ->  10 thema's
    G2  analyse: integralen                      38 %  ->   2 thema's
        complexe getallen                        18 %  ->   1 thema
        telproblemen, kansrekenen en statistiek  44 %  ->   3 thema's
    G3  algebra: matrices en structuren          42 %  ->   3 thema's
        ruimtemeetkunde                          38 %  ->   2 thema's
        programmeren                             20 %  ->   1 thema

**Bij wiskunde geen meerkeuze met meerdere juiste antwoorden.** Dat mag bij
geschiedenis en Nederlands, waar een opsomming een oordeel vraagt, maar bij
wiskunde is er één uitkomst en anders is de vraag slecht gesteld. Het script
weigert er dan ook een.

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
DOEL = HIER.parent / "wiskunde-gevorderd.json"

# De volgorde volgt de drie fiches: eerst G1, de analyse van functies, dan G2
# met de integralen, de complexe getallen en de kansrekening, en ten slotte G3
# met de algebra, de ruimtemeetkunde en het programmeren. Binnen G1 loopt ze
# van het rekengereedschap naar het functieonderzoek.
THEMAS = [
    ("wi_machten", "Machtswortels, machten en logaritmen"),
    ("wi_veeltermen", "Veeltermen, deelbaarheid en Horner"),
    ("wi_vergelijkingen", "Vergelijkingen en ongelijkheden oplossen"),
    ("wi_grafiek", "Een functie aflezen van haar grafiek"),
    ("wi_tweedegraad", "Tweedegraadsfuncties en transformaties"),
    ("wi_exponentieel", "Exponentiële en logaritmische functies"),
    ("wi_gonio", "Goniometrische functies en goniometrie"),
    ("wi_limieten", "Limieten, continuïteit en asymptoten"),
    ("wi_afgeleiden", "Afgeleiden en het verloop van een functie"),
    ("wi_rijen", "Rijen en hun limiet"),
    ("wi_primitieven", "Primitieven en de onbepaalde integraal"),
    ("wi_integralen", "De bepaalde integraal en haar toepassingen"),
    ("wi_complexe", "Complexe getallen"),
    ("wi_tellen", "Telproblemen en het binomium"),
    ("wi_kansen", "Kansrekenen en kansverdelingen"),
    ("wi_statistiek", "Statistiek: normale verdeling en hypothesetoets"),
    ("wi_matrices", "Matrices en hun bewerkingen"),
    ("wi_stelsels", "Stelsels oplossen en matrixmodellen"),
    ("wi_structuren", "Algebraïsche structuren en groepen"),
    ("wi_ruimte", "Punten, vectoren en afstanden in de ruimte"),
    ("wi_vlakken", "Rechten en vlakken in de ruimte"),
    ("wi_programmeren", "Programmeren: algoritmen en structuren"),
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
            {"titel": titel, "niveau": "beyond-doorstroom", "gratis": False, "vragen": vragen}
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

    # Kim, 23 september 2026: bij wiskunde geen meerkeuze met meerdere juiste
    # antwoorden. Een som heeft één uitkomst; wie er twee laat aankruisen,
    # toetst het lezen van de opgave en niet het rekenen.
    if meerdere:
        raise SystemExit(
            f"{meerdere} meerkeuzevragen hebben meerdere juiste antwoorden; bij wiskunde mag dat niet"
        )
    print(f"\n{meerkeuze} meerkeuzevragen, allemaal met één juist antwoord.")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
