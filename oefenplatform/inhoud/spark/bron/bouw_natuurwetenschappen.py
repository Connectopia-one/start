# -*- coding: utf-8 -*-
"""Zet de themabestanden `nw_*.py` samen in ../natuurwetenschappen.json.

    python3 bron/bouw_natuurwetenschappen.py

Elk thema is één bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen. Dit script maakt daar twee hoofdstukken van, "<thema> — deel 1" en
"<thema> — deel 2", en schrijft het importbestand van nul af aan.

Het bewaakt onderweg wat je met het blote oog niet ziet:

- elk deel heeft precies twintig vragen;
- geen twee vragen in het hele vak zijn woordelijk gelijk;
- elke meerkeuzevraag heeft minstens drie opties en geen twee gelijke;
- een `antwoord` dat een lijstje is, heeft minstens twee geldige nummers
  (dat zijn de vragen waar je álle juiste antwoorden moet aanklikken);
- het aandeel van die vragen ligt tussen 20 en 30 % van de meerkeuzevragen,
  zoals Kim vroeg;
- een waarofniet-vraag heeft een boolean, een invultekst een korte tekst.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "natuurwetenschappen.json"

# De volgorde hieronder is de volgorde in het platform. Ze volgt de vakfiche:
# eerst het deel biologie (47,5 % van het examen), dan chemie en fysica
# (32,5 %), dan het deel onderzoek (20 %). Vijf, drie en twee thema's houdt
# die verhouding ook in het aantal vragen aan.
THEMAS = [
    ("nw_cellen", "Cellen, weefsels en organen"),
    ("nw_fotosynthese", "Fotosynthese en de plant"),
    ("nw_lichaam", "Het menselijk lichaam"),
    ("nw_voortplanting", "Voortplanting"),
    ("nw_ecologie", "Ecologie en biodiversiteit"),
    ("nw_materie", "Materie, stoffen en mengsels"),
    ("nw_massadichtheid", "Massadichtheid"),
    ("nw_kracht", "Energie, kracht en snelheid"),
    ("nw_meten", "Veilig werken, meten en eenheden"),
    ("nw_onderzoek", "Wetenschappelijk onderzoek"),
]

# Het hoofdstuk dat bij het opzetten van de databank al op ✨ Spark stond
# (zie supabase/schema.sql). Het eerste deel neemt het over in plaats van er
# een tweede naast te zetten, zodat er geen restje met drie voorbeeldvragen
# blijft staan.
OUD_EERSTE_HOOFDSTUK = "Cellen en toestanden van materie"


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
        # Een invulvraag mag meer dan één juist antwoord hebben: dan staat er
        # een lijstje tekst in plaats van één tekst (zie lib/antwoord.ts). Het
        # eerste is wat het kind te zien krijgt.
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
    """Kan je scoren zonder de leerstof te kennen?

    Twee patronen sluipen er bij het schrijven vanzelf in. Het juiste antwoord
    krijgt uitleg en wordt daardoor de langste optie, en bij waar of niet waar
    komt het antwoord vaker op waar uit. Allebei maken ze een hoofdstuk
    raadbaar. Een verschil van een paar letters ziet een kind niet, dus een
    vraag telt pas mee als het juiste antwoord er minstens zes langer is dan
    elke foute optie.
    """
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
    """Waar en niet waar moeten elkaar per thema in evenwicht houden.

    Per hoofdstuk staan er maar twee tot vier van die vragen, en dan zegt een
    verhouding niets. Daarom tellen we ze per thema, over deel 1 en deel 2
    samen.
    """
    meldingen = []
    per_thema = {}
    for h in hoofdstukken:
        thema = h["titel"].split(" — ")[0]
        for v in h["vragen"]:
            if v["type"] == "waarofniet":
                per_thema.setdefault(thema, []).append(v["antwoord"])
    for thema, antwoorden in per_thema.items():
        waar = sum(1 for a in antwoorden if a)
        if not (0.35 <= waar / len(antwoorden) <= 0.65):
            meldingen.append(
                f"{thema}: {waar} van de {len(antwoorden)} waar/niet-waar-vragen is waar. "
                f"Dat is te scheef om niet te kunnen gokken."
            )
    return meldingen


def hoofdstukken_van(modulenaam: str, thema: str, eerste: bool) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        titel = f"{thema} — deel {nummer}"
        if len(vragen) != 20:
            raise SystemExit(f"{titel} heeft {len(vragen)} vragen, verwacht 20")
        for i, vraag in enumerate(vragen, start=1):
            controleer(titel, i, vraag)
        hoofdstuk = {"titel": titel, "niveau": "spark", "gratis": False}
        if eerste and nummer == 1:
            hoofdstuk["hernoemVan"] = OUD_EERSTE_HOOFDSTUK
        hoofdstuk["vragen"] = vragen
        uit.append(hoofdstuk)
    return uit


def main():
    hoofdstukken = []
    for i, (modulenaam, thema) in enumerate(THEMAS):
        if not (HIER / f"{modulenaam}.py").exists():
            print(f"  {thema}: nog niet geschreven, overgeslagen")
            continue
        nieuw = hoofdstukken_van(modulenaam, thema, eerste=(i == 0))
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    gezien = {}
    meerkeuze = meerdere = 0
    for h in hoofdstukken:
        for v in h["vragen"]:
            tekst = " ".join(v["vraag"].lower().split())
            if tekst in gezien:
                raise SystemExit(f"Deze vraag staat twee keer, in {gezien[tekst]} en in {h['titel']}:\n  {v['vraag']}")
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
            raise SystemExit(f"{meerdere} van de {meerkeuze} meerkeuzevragen is {deel:.0%}; mikken op 20 à 30 %")
        print(f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden.")

    DOEL.write_text(json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
