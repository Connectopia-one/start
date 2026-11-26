# -*- coding: utf-8 -*-
"""Zet de themabestanden `de_*.py` samen in ../duits.json.

    python3 bron/bouw_duits.py

Boost doorstroom, tweede graad, richting moderne talen (vakfiche
2027_Duits_2MT). Het ERK-niveau is A2 voor lezen en luisteren en A1+ voor
schrijven, spreken en gesprekken. Het examen weegt lezen 30 %, luisteren 30 %,
schrijven 8 %, schriftelijke interactie 8 %, spreken 8 % en twee gesprekken
elk 8 %.

**Wat hier níét in zit:** luisteren, spreken en de gesprekken. Die vragen
geluid en een gesprekspartner. Wat hier wél staat: lezen, schrijven en
schriftelijke interactie, en de woordenschat (alle woordvelden) en grammatica
die je daarvoor nodig hebt. Kim, 26 november 2026: Duits voorlopig enkel
schriftelijk aanbieden.

Elk thema is een bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen (helpers in de_hulp.py), en wordt hier twee hoofdstukken,
"<thema> — deel 1" en "<thema> — deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parents[1]))

from notatie import sluitend, zichtbaar  # noqa: E402  (pad moet eerst klaarstaan)
DOEL = HIER.parent / "duits.json"

# De volgorde loopt van de vaardigheden naar het materiaal: eerst lezen en
# schrijven, dan de omgangsvormen die het examen uitdrukkelijk vraagt, dan de
# woordvelden, en ten slotte de grammatica, in de volgorde van de lijst zelf.
THEMAS = [
    ("de_lezen", "Een Duitse tekst lezen"),
    ("de_tekstsoorten", "Tekstsoorten, signaalwoorden en verwijswoorden"),
    ("de_schrijven", "Schrijven en schriftelijke interactie"),
    ("de_ich", "Woordvelden: ik, mijn familie, mijn lichaam en kleding"),
    ("de_alltag", "Woordvelden: thuis, eten, winkelen en media"),
    ("de_welt", "Woordvelden: school, werk, vrije tijd, reizen en weer"),
    ("de_naamwoorden", "Lidwoorden, meervoud en naamvallen"),
    ("de_voornaamwoorden", "Voornaamwoorden: persoonlijk, bezittelijk, aanwijzend en vragend"),
    ("de_praesens", "Präsens en Imperativ"),
    ("de_perfekt", "Perfekt en Futur"),
    ("de_zinsbouw", "Zinsbouw: soorten zinnen, Satzklammer en voegwoorden"),
    ("de_voorzetsels", "Voorzetsels, telwoorden, bijwoorden en uitspraak"),
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
        lengtes = [len(zichtbaar(o)) for o in v["opties"]]
        # "Geen van deze antwoorden" is bijna altijd de langste optie, en die
        # lengte zegt niets over de inhoud. Zulke opties blijven hier buiten.
        vrij = [i for i, o in enumerate(v["opties"]) if not sluitend(o)]
        juist = [i for i in antw if i in vrij]
        anders = [lengtes[i] for i in vrij if i not in antw]
        if juist and anders and min(lengtes[i] for i in juist) > max(anders) + 5:
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

    # De wisselende woorden staan in varianten_boost_doorstroom.py, want ze
    # horen bij de taalvakken samen. Ze gaan er hier meteen terug in, anders
    # veegt een volgende bouw ze weg.
    import varianten_boost_doorstroom

    varianten_boost_doorstroom.zet_varianten(DOEL.name)

if __name__ == "__main__":
    main()
