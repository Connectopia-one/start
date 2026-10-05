# -*- coding: utf-8 -*-
"""Zet de themabestanden `frdf_*.py` samen in ../frans.json.

    python3 bron/bouw_frans.py

Boost dubbele finaliteit, tweede graad. Eén vakfiche, geldig van 1 januari
2027 tot en met 31 december 2027, voor bedrijf en organisatie en voor
maatschappij en welzijn. Dat staat bovenaan op de fiche zelf.

Het ERK-niveau is hier A2. Bij doorstroom is het B1, en daar zijn het ook twee
fiches (Frans 1 en Frans 2) in plaats van één. Daarom staat Frans hier niet in
`df_frans_vervangingen.py` naast de doorstroomvragen, zoals bij aardrijkskunde
of natuurwetenschappen: de doorstroomkant van Frans is zelf nog maar één thema
ver, en de grammaticalijst van A2 is korter en anders. Alles hier is dus voor
dit niveau geschreven.

Wat de A2-lijst níét vraagt en de B1-lijst wel: de plus-que-parfait, de
subjonctif, de conditionnel als tijd (alleen nog de conditionnel de politesse),
de betrekkelijke bijzinnen met qui/que/dont en de passieve vorm. Wat er wel
staat, staat in de volgorde van de fiche zelf.

Het gewicht van het examen:

    lezen                      30 %
    luisteren                  30 %
    schrijven                   8 %
    schriftelijke interactie    8 %
    spreken                     8 %
    mondelinge interactie 1     8 %
    mondelinge interactie 2     8 %

**Wat hier níét in zit:** luisteren, spreken en het gesprek zelf. Die vragen
geluid en een gesprekspartner, en dat kan een platform met tekstvragen niet
nabootsen. Wat je erover moet wéten staat er wel: de strategieën, de
beoordelingsrijen en de omgangsvormen.

Elke leesvraag staat op een echt Frans tekstje. Een vraag over lezen zonder
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
DOEL = HIER.parent / "frans.json"

# De volgorde loopt van de vaardigheden naar het materiaal: eerst lezen en
# schrijven, dan de omgangsvormen die de fiche uitdrukkelijk vraagt, dan de
# woordvelden, en ten slotte de grammatica, in de volgorde van de lijst zelf.
THEMAS = [
    ("frdf_lezen", "Een Franse tekst begrijpen"),
    ("frdf_tekstsoorten", "Tekstsoorten, tekstverbanden en leesstrategieën"),
    ("frdf_cultuur", "De Franstalige wereld: omgangsvormen en gewoontes"),
    ("frdf_schrijven", "Schrijven, schriftelijke interactie en leesbeleving"),
    ("frdf_spreken", "Spreken, gesprekken, klank en spelling"),
    ("frdf_mens", "Woordvelden: mens, familie, gevoelens en gezondheid"),
    ("frdf_dagelijks", "Woordvelden: eten, kleding, wonen en winkelen"),
    ("frdf_school", "Woordvelden: school, werk en de professionele wereld"),
    ("frdf_onderweg", "Woordvelden: tijd, weer, reizen en vervoer"),
    ("frdf_naamwoorden", "Zelfstandige naamwoorden, lidwoorden en determinanten"),
    ("frdf_voornaamwoorden", "Voornaamwoorden: sujet, COD, COI en de wederkerende"),
    ("frdf_adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en de trappen"),
    ("frdf_tegenwoordig", "Présent, impératif en de wederkerende werkwoorden"),
    ("frdf_verleden", "Passé composé, imparfait en passé récent"),
    ("frdf_toekomst", "Futur proche, futur simple en de conditionnel de politesse"),
    ("frdf_zinsbouw", "Zinsbouw, zinsdelen, voegwoorden en de overeenkomst"),
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


# Woorden die bij het A2-niveau van deze fiche niet horen. Wie ze in een vraag
# of een uitleg schrijft, leert iets uit de doorstroomfiche.
VERBODEN = [
    "plus-que-parfait",
    "subjonctif",
    "gérondif",
    "participe présent",
    "passé simple",
    "voorwaardelijke wijs",
    "betrekkelijk voornaamwoord",
    "betrekkelijke bijzin",
    "passieve vorm",
    "de vakfiche",
    "de fiche",
    "deze fiche",
    "de leerstof",
]


def verboden_woorden(hoofdstukken: list):
    for h in hoofdstukken:
        for nummer, v in enumerate(h["vragen"], start=1):
            stukken = [v["vraag"], v.get("uitleg", "")]
            stukken += v.get("opties", [])
            antwoord = v["antwoord"]
            if isinstance(antwoord, str):
                stukken.append(antwoord)
            elif isinstance(antwoord, list):
                stukken += [a for a in antwoord if isinstance(a, str)]
            tekst = " ".join(stukken).lower()
            for woord in VERBODEN:
                if woord in tekst:
                    raise SystemExit(
                        f"{h['titel']}: vraag {nummer} gebruikt nog {woord!r}"
                    )


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
            {
                "titel": titel,
                "niveau": "boost-dubbele-finaliteit",
                "gratis": False,
                "vragen": vragen,
            }
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
    verboden_woorden(hoofdstukken)

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
    print("Niets uit de doorstroomfiche blijven staan.")


if __name__ == "__main__":
    main()
