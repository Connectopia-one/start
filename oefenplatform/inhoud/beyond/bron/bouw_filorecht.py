# -*- coding: utf-8 -*-
"""Zet de themabestanden `fr_*.py` samen in ../filosofie-en-recht.json.

    python3 bron/bouw_filorecht.py

🌍 Beyond, derde graad doorstroomfinaliteit. Bladzijde 1 van de fiche
`2027_Filosofie_en_recht_3DDG` noemt **één** studierichting:
welzijnswetenschappen. Dit vak is dus het engste van de drie die Kim op
9 oktober 2026 vroeg, en het derde dat gemaakt is, na samenleving en economie
en na sociale en gedragswetenschappen.

Het examen duurt **120 minuten** en weegt:

    filosofie   60 %  ->  12 thema's
    recht       40 %  ->   8 thema's

Samen twintig thema's, veertig hoofdstukken, achthonderd vragen.

**De gevaarlijkste fout in dit vak.** De fiche noemt ruim veertig filosofen bij
naam, en bij elk staat precies wat je van hem moet kennen. Zet er geen naam bij
die niet in de fiche staat, en hang aan een naam geen stelling, boek of
experiment dat de fiche niet vermeldt. Een verzonnen citaat in de mond van een
echte filosoof is geen voorbeeld maar een vervalsing. Waar de fiche enkel een
naam geeft en geen inhoud, vraag dan naar wat ze wél zegt.

Drie dingen die deze fiche anders maken dan de andere:

  1. **Het examen is volledig digitaal**, met invulvragen, sleepvragen,
     dropdownvragen en meerkeuzevragen. Bij de meeste opdrachten hoort een
     bron: een prent, een foto of een stukje tekst. De vraagvormen hier mogen
     dus gerust op het examen lijken.

  2. **Spellingcontrole en een woordenboek mogen op het examen.** Daarom zijn
     de invulvragen hier op begrippen gericht en niet op spelling.

  3. **Vier bijlagen** horen bij de fiche, en het kind krijgt ze níet op het
     examen: de AUB-methode (argument, uitleg, bijvoorbeeld) met zeven soorten
     argumenten, een stappenplan om een filosofische tekst te analyseren, een
     schema met drie redeneeractiviteiten, en richtvragen bij een
     gedachte-experiment. De inhoud ervan wordt wel gevraagd, dus ze zit in de
     vragen.

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
DOEL = HIER.parent / "filosofie-en-recht.json"

# De volgorde volgt de fiche van voor naar achter: eerst filosofie, dan recht.
THEMAS = [
    # filosofie (60 %): twaalf thema's
    ("fr_eigenheid", "De eigenheid van de filosofie"),
    ("fr_kennis", "Bronnen van kennis, rationalisme en empirisme"),
    ("fr_falsificatie", "Van natuurfilosofie naar wetenschap: falsificatie en demarcatie"),
    ("fr_lichaamgeest", "Lichaam en geest: monisme en dualisme"),
    ("fr_mensdier", "Cultuur en natuur: mens, dier en machine"),
    ("fr_vrijheid1", "Vrijheid en determinisme van de oudheid tot de 19de eeuw"),
    ("fr_vrijheid2", "Vrijheid en determinisme in de 20ste eeuw"),
    ("fr_ethiek", "Ethiek: basisbegrippen en vier benaderingen"),
    ("fr_gevolgplicht", "Gevolgenethiek en plichtethiek"),
    ("fr_deugdzorg", "Deugdethiek en zorgethiek"),
    ("fr_geluk", "Ethiek en geluk"),
    ("fr_argumentatie", "Argumentatieleer: redeneervormen en drogredenen"),
    # recht (40 %): acht thema's
    ("fr_rechtsstaat", "De democratische rechtsstaat en haar principes"),
    ("fr_machten", "De scheiding der machten en de rechterlijke macht"),
    ("fr_justitie", "De functies van justitie, de rechtspraak en de deontologie"),
    ("fr_actueel", "Actuele thema's binnen recht"),
    ("fr_buitengerechtelijk", "Buitengerechtelijke procedures en juridische bijstand"),
    ("fr_piramide", "De gerechtelijke piramide: rechtbanken en hoven"),
    ("fr_procedures", "Burgerlijk recht en strafrecht: het verloop van een procedure"),
    ("fr_actoren", "Juridische termen en actoren"),
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
        if isinstance(antwoord, list) and len(nummers) == len(opties):
            raise SystemExit(f"{plek} heeft alle opties juist; dan valt er niets te kiezen")
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
    mk = [v for v in vragen if v["type"] == "meerkeuze" and not isinstance(v["antwoord"], list)]
    langst = 0
    for v in mk:
        a = v["antwoord"]
        lengtes = [len(o) for o in v["opties"]]
        anders = [lengtes[i] for i in range(len(lengtes)) if i != a]
        if anders and lengtes[a] > max(anders) + 5:
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
    meerkeuze = meerdere = invul = waarofniet = 0
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
            invul += v["type"] == "invultekst"
            waarofniet += v["type"] == "waarofniet"

    for h in hoofdstukken:
        for melding in gokpatronen(h["titel"], h["vragen"]):
            raise SystemExit(melding)
    for melding in evenwicht_waar(hoofdstukken):
        raise SystemExit(melding)

    if meerkeuze:
        deel = meerdere / meerkeuze
        if not 0.10 <= deel <= 0.25:
            raise SystemExit(
                f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 10 à 25 %"
            )
        print(
            f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden."
        )
    print(f"{meerkeuze} meerkeuzevragen, {waarofniet} waar of niet waar, {invul} invulvragen.")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
