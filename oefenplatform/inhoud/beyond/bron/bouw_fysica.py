# -*- coding: utf-8 -*-
"""Zet de themabestanden `fy3_*.py` samen in ../fysica.json.

    python3 bron/bouw_fysica.py

🌍 Beyond, derde graad. De vakfiche fysica van de doorstroomfinaliteit noemt
bovenaan zelf twee studierichtingen: Latijn-wiskunde met extra wetenschappen en
wetenschappen-wiskunde. Die twee leggen hun wetenschappen af in drie aparte
examens, biologie, chemie en fysica, in plaats van één examen
natuurwetenschappen. Vandaar een eigen vak naast natuurwetenschappen.

Hoe de drieëntwintig thema's volgen uit de fiche. Achteraan weegt ze haar vijf
onderdelen zelf: elektriciteit en magnetisme 30 %, mechanica 25 %, de
gaswetten met de warmteleer en de trillingen en golven samen 20 %,
kwantumfysica met kernfysica 15 %, en wetenschappelijk onderzoek met STEM
10 %. Die verhouding geeft zeven thema's voor elektriciteit en magnetisme, zes
voor de mechanica, vijf voor de gaswetten en de golven, drie voor de kwantum-
en kernfysica en twee voor het onderzoek. Elk thema valt samen met een kop of
een duidelijk blok uit de fiche zelf, zodat er niets tussen valt.

Drie afspraken van de fiche staan hier overgenomen. Eén: het formularium, de
constanten en de tabel met geluidssnelheden staan in een bijlage die het kind
op het examen krijgt, dus hoeft het die niet van buiten te kennen, maar moet
het ze wel kunnen gebruiken; de vragen geven de nodige waarden mee. Twee:
veilig en duurzaam werken wordt op het examen niet uitgevoerd maar uitgelegd,
dus vragen de vragen daarover naar het waarom van een handeling. Drie:
veldlijnenpatronen, vectoren en grafieken tekenen kan hier niet, dus wordt er
naar het patroon of het verloop in woorden gevraagd.

Elk thema is een bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen. Dit script maakt daar twee hoofdstukken van, "<thema> — deel 1" en
"<thema> — deel 2", en schrijft het importbestand van nul af aan.

Dezelfde bewaking als bij de andere vakken: twintig vragen per deel, geen
woordelijke dubbels in het hele vak, minstens drie opties per meerkeuzevraag,
20 a 30 % vragen met meerdere juiste antwoorden, en geen raadbare patronen
(het juiste antwoord dat altijd de langste is, of waar dat te vaak waar is).
"""

import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "fysica.json"

# De volgorde volgt de fiche van voor naar achter.
THEMAS = [
    ("fy3_lading", "Elektrische lading, geleiders en influentie"),
    ("fy3_veld", "De wet van Coulomb en het elektrisch veld"),
    ("fy3_potentiaal", "Elektrische energie, potentiaal en spanning"),
    ("fy3_stroom", "Elektrodynamica: stroom, weerstand en schakelingen"),
    ("fy3_magneet", "Magneten en het magnetisch veld"),
    ("fy3_magkracht", "De magnetische kracht op een stroom en op een lading"),
    ("fy3_inductie", "Elektromagnetische inductie"),
    ("fy3_statica", "Statica: krachten, moment en evenwicht"),
    ("fy3_newton", "De wetten van Newton"),
    ("fy3_beweging", "Rechtlijnige beweging: ERB en EVRB"),
    ("fy3_worp", "De horizontale worp"),
    ("fy3_gravitatie", "De gravitatiekracht en de cirkelbeweging"),
    ("fy3_arbeid", "Arbeid, energie en vermogen"),
    ("fy3_gaswetten", "De gaswetten en de algemene gaswet"),
    ("fy3_warmte", "Warmteleer: temperatuur, warmte en faseovergangen"),
    ("fy3_trillingen", "Harmonische trillingen"),
    ("fy3_golven", "Golven en hun eigenschappen"),
    ("fy3_licht", "Licht, geluid en het elektromagnetisch spectrum"),
    ("fy3_kwantum", "Kwantumfysica: het foto-elektrisch effect en dualiteit"),
    ("fy3_kern", "De atoomkern, radioactief verval en halveringstijd"),
    ("fy3_straling", "Kernenergie, straling en haar effecten"),
    ("fy3_meten", "Veilig werken, meetinstrumenten en meetonzekerheid"),
    ("fy3_onderzoek", "Wetenschappelijk onderzoek, ontwerpen en STEM"),
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
