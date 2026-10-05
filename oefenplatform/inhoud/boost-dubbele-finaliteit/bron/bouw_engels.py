# -*- coding: utf-8 -*-
"""Zet de thema's samen in ../engels.json.

    python3 bron/bouw_engels.py

Boost dubbele finaliteit, tweede graad. Eén vakfiche voor bedrijf en
organisatie en voor maatschappij en welzijn. Bij doorstroom zijn het er twee
(Engels 1 en Engels 2); hier is alles in één fiche gegoten, en het gewicht
ligt anders:

    lezen                      30 %
    luisteren                  30 %
    schrijven                   8 %
    schriftelijke interactie    8 %
    spreken                     8 %
    mondelinge interactie 1     8 %
    mondelinge interactie 2     8 %

Het grootste verschil met doorstroom is het niveau: daar is het ERK-niveau B1,
hier A2. De woordvelden zijn woord voor woord dezelfde, maar de
grammaticalijst van A2 is korter. Daarom valt het thema over de modale
hulpwerkwoorden hier helemaal weg, en worden de past perfect, 'going to', de
future continuous, 'shall', de betrekkelijke bijzinnen en de conditionals
vervangen (zie `df_engels_vervangingen.py`).

Twee thema's zijn hier nieuw geschreven, voor leerstof die de A2-fiche wél
vraagt en de doorstroomfiche niet zo zet:

  * **Klank en spelling.** De fiche zet een rij 'fonologische elementen en
    spelling': uitspraak van klanken, woordaccent, articulatie, intonatie, de
    relatie tussen klank- en schriftbeeld, en de spelling van frequente
    woorden. Zie `endf_klank.py`.
  * **Spreken en gesprekken.** Spreken en de twee mondelinge interacties zijn
    samen 24 % van het examen, en de fiche zet er drie eigen
    beoordelingsrijen bij: lichaamstaal, spreektempo en vlotheid, en uitspraak
    en intonatie. Zie `endf_spreken.py`.

**Wat hier níét in zit:** luisteren en het gesprek zelf. Die vragen geluid en
een gesprekspartner, en dat kan een platform met tekstvragen niet nabootsen.
Dat is 30 % plus 16 % van het examen. Wat je erover moet wéten staat er wel.

Elke leesvraag staat op een echt Engels tekstje. Een vraag over lezen zonder
tekst is geen leesvraag.

Werkt verder precies als bouw_nederlands.py van deze categorie: de thema's
komen uit de doorstroombron, de vervangingen uit het bestand hiernaast, en elk
thema wordt twee hoofdstukken, "<thema> — deel 1" en "<thema> — deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
DOORSTROOM = HIER.parent.parent / "boost-doorstroom" / "bron"
sys.path.insert(0, str(DOORSTROOM))
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "engels.json"

import df_engels_vervangingen as vervang  # noqa: E402

# De volgorde loopt van de vaardigheden naar het materiaal: eerst lezen,
# schrijven en spreken, dan de cultuur die de fiche uitdrukkelijk vraagt, dan
# de woordvelden, en ten slotte de grammatica en de klank van de fichelijst.
THEMAS = [
    ("en_lezen", "Een Engelse tekst analyseren"),
    ("en_tekstsoorten", "Tekstsoorten, tekstverbanden en verwijswoorden"),
    ("en_schrijven", "Schrijven, schriftelijke interactie en literatuurbeleving"),
    ("endf_spreken", "Spreken, gesprekken en hoe je beoordeeld wordt"),
    ("en_cultuur", "De Engelstalige wereld: gewoontes en conventies"),
    ("en_dagelijks", "Woordvelden: mensen, gezondheid en het dagelijkse leven"),
    ("en_wereld", "Woordvelden: school, werk, reizen en de samenleving"),
    ("en_naamwoorden", "Nouns, articles, quantifiers en numerals"),
    ("en_voornaamwoorden", "Pronouns: de vijf soorten en de onbepaalde woorden"),
    ("en_adjectieven", "Adjectives, adverbs, comparatives en voorzetsels"),
    ("en_tegenwoordig", "De tegenwoordige tijden"),
    ("en_verleden", "Past simple, past continuous en de toekomst met will"),
    ("en_zinsbouw", "Zinsdelen, soorten zinnen en samengestelde zinnen"),
    ("endf_klank", "Klank, klemtoon, intonatie en spelling"),
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


def hoofdstukken_van(modulenaam: str, thema: str, nog_te_vervangen: dict) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        nieuw = []
        for vraag in vragen:
            sleutel = " ".join(vraag["vraag"].split())
            nieuw.append(nog_te_vervangen.pop(sleutel) if sleutel in nog_te_vervangen else vraag)
        if len(nieuw) != 20:
            raise SystemExit(f"{titel} heeft {len(nieuw)} vragen, verwacht 20")
        for i, vraag in enumerate(nieuw, start=1):
            controleer(titel, i, vraag)
        uit.append(
            {
                "titel": titel,
                "niveau": "boost-dubbele-finaliteit",
                "gratis": False,
                "vragen": nieuw,
            }
        )
    return uit


def main():
    nog_te_vervangen = dict(vervang.VERVANGINGEN)
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        nieuw = hoofdstukken_van(modulenaam, thema, nog_te_vervangen)
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

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

    # De wisselende woorden staan bij doorstroom, in varianten_en_boost.py. Ze
    # gelden hier alleen voor de hoofdstukken die woord voor woord hetzelfde
    # gebleven zijn; die staan in varianten_boost_df.py op een rij. Ze gaan er
    # meteen terug in, anders veegt een volgende bouw ze weg.
    import varianten_boost_df

    varianten_boost_df.zet_varianten(DOEL.name)


if __name__ == "__main__":
    main()
