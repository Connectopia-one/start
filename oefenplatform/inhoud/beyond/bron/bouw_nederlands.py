# -*- coding: utf-8 -*-
"""Zet de themabestanden `nl_*.py` samen in ../nederlands.json.

    python3 bron/bouw_nederlands.py

🌍 Beyond, derde graad. Er zijn **twee** vakfiches Nederlands (2027, 3DO), en
ze noemen allebei dezelfde zes studierichtingen: bedrijfswetenschappen,
economie-wiskunde, humane wetenschappen, Latijn-wiskunde (met extra
wetenschappen), welzijnswetenschappen en wiskunde-wetenschappen. Twee fiches
voor hetzelfde vak worden bij ons één vak, net als bij wiskunde G1/G2/G3.

Fiche 1 is het receptieve examen: lezen 30 %, luisteren 30 %, literatuur 20 %,
taalbeschouwing 20 %. Fiche 2 is het productieve examen: spreken 10 %,
schrijven 30 %, schriftelijke interactie 30 % en gesprek 30 %, met de literaire
competentie verwerkt in die drie laatste.

Hoe de eenentwintig thema's daaruit volgen. Lezen en luisteren staan samen op
30 % van het eerste examen en leveren zes thema's. Literatuur staat op 20 % van
het eerste examen én draagt een stuk van het tweede, en de termenlijst van de
fiche is daar veruit het dikst, dus het worden zes thema's. Taalbeschouwing
staat op 20 % en valt uiteen in twee thema's over taal en samenleving plus vijf
over het taalsysteem, want fonologie, spelling, woordsoorten, morfologie,
zinsbouw en semantiek staan alle zes als ondersteunende kennis op de twee
fiches. Schrijven, spreken en interactie halen samen 90 % van het tweede
examen, maar dat zijn prestaties, geen kennis: wat je er met vragen van kan
toetsen zijn de criteria, de strategieën en het register, en dat is twee
thema's waard.

Werkt precies als bij geschiedenis: elk thema is een bestand met een lijst
DEEL1 en een lijst DEEL2 van twintig vragen, en wordt hier twee hoofdstukken,
"<thema> — deel 1" en "<thema> — deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "nederlands.json"

# De volgorde volgt de twee fiches: eerst lezen en luisteren, dan literatuur,
# dan taalbeschouwing met het taalsysteem, en tot slot het productieve deel.
THEMAS = [
    ("nl_tekstsoorten", "Tekstsoorten en teksttypes"),
    ("nl_hoofdgedachte", "Onderwerp, hoofdgedachte en samenvatten"),
    ("nl_bronnen", "Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing"),
    ("nl_communicatie", "Het communicatiemodel en ruis"),
    ("nl_tekstopbouw", "Tekstopbouw, alineaverbanden en structuuraanduiders"),
    ("nl_argumentatie", "Argumentatie en drogredenen"),
    ("nl_genres", "Literaire begrippen en genres"),
    ("nl_verhaal", "Verhaalkenmerken en vertelperspectief"),
    ("nl_poezie", "Poëzie: dichtvormen, strofen en rijm"),
    ("nl_drama", "Dramatiek en theatertekens"),
    ("nl_stijlfiguren", "Stijlfiguren en beeldspraak"),
    ("nl_stromingen", "Literaire stromingen van de middeleeuwen tot nu"),
    ("nl_varieteiten", "Taalvariëteiten, registers en beleefdheid"),
    ("nl_identiteit", "Taal en identiteit: stereotypering, inclusie en non-verbale communicatie"),
    ("nl_spelling", "Klanken, spelling, diakritische tekens en interpunctie"),
    ("nl_woordsoorten", "Woordsoorten"),
    ("nl_morfologie", "Morfologie: samenstellingen, afleidingen en werkwoordstijden"),
    ("nl_zinsbouw", "Zinsontleding en zinsbouw"),
    ("nl_semantiek", "Semantiek: betekenisrelaties, gevoelswaarde en herkomst"),
    ("nl_schrijven", "Schrijven en schriftelijke interactie"),
    ("nl_spreken", "Spreken en gesprekken voeren"),
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
            {"titel": titel, "niveau": "beyond", "gratis": False, "vragen": vragen}
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
