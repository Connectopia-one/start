# -*- coding: utf-8 -*-
"""Zet de themabestanden `en_*.py` samen in ../engels.json.

    python3 bron/bouw_engels.py

Boost doorstroom, tweede graad. Er zijn voor Engels twee vakfiches, Engels 1 en
Engels 2, en ze gelden allebei voor dezelfde vier richtingen: economische
wetenschappen, humane wetenschappen, natuurwetenschappen en Latijn. Dat staat
bovenaan op de fiches zelf. Het ERK-niveau is B1.

Eén vak voor twee fiches, net als bij Nederlands. Engels 1 is een examen lezen
(50 %) en luisteren (50 %). Engels 2 is een examen schrijven (29 %),
schriftelijke interactie (29 %), mondelinge interactie (30 %), spreken (8 %) en
literatuurbeleving (4 %). De woordenschatvelden en de grammaticalijst achter
allebei de examens zijn woord voor woord dezelfde, dus die twee keer schrijven
zou twee keer dezelfde vragen opleveren.

**Wat hier níét in zit:** luisteren, spreken en mondelinge interactie. Die
vragen geluid en een gesprekspartner, en dat kan een platform met tekstvragen
niet nabootsen. Dat is de helft van Engels 1 en 38 % van Engels 2. Wat hier wél
staat — lezen, schrijven, schriftelijke interactie, literatuurbeleving, en de
woordenschat en grammatica die je daarbij nodig hebt — is de andere helft van
Engels 1 en 62 % van Engels 2.

Elke leesvraag staat op een echt Engels tekstje. Een vraag over lezen zonder
tekst is geen leesvraag.

Werkt precies als bouw_nederlands.py: elk thema is een bestand met een lijst
DEEL1 en een lijst DEEL2 van twintig vragen, en wordt hier twee hoofdstukken,
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
# woordvelden, en ten slotte de grammatica van de fichelijst.
THEMAS = [
    ("en_lezen", "Een Engelse tekst analyseren"),
    ("en_tekstsoorten", "Tekstsoorten, tekstverbanden en verwijswoorden"),
    ("en_cultuur", "De Engelstalige wereld: gewoontes en conventies"),
    ("en_schrijven", "Schrijven, schriftelijke interactie en literatuurbeleving"),
    ("en_dagelijks", "Woordvelden: mensen, gezondheid en het dagelijkse leven"),
    ("en_wereld", "Woordvelden: school, werk, reizen en de samenleving"),
    ("en_naamwoorden", "Nouns, articles, quantifiers en numerals"),
    ("en_voornaamwoorden", "Pronouns: de zeven soorten"),
    ("en_adjectieven", "Adjectives, adverbs, comparatives en voorzetsels"),
    ("en_tegenwoordig", "De tegenwoordige tijden"),
    ("en_verleden", "De verleden en de toekomende tijden"),
    ("en_modalen", "Modal auxiliaries, imperative en infinitive"),
    ("en_zinsbouw", "Zinsdelen, soorten zinnen en bijzinnen"),
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
