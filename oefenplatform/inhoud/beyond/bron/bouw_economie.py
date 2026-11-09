# -*- coding: utf-8 -*-
"""Zet de themabestanden `eco3_*.py` samen in ../economie.json.

    python3 bron/bouw_economie.py

🌍 Beyond, derde graad doorstroomfinaliteit, vak algemene economie. De fiche
`2027_algemene_economie_3DDO_3DDG` geldt voor economie-wiskunde en
bedrijfswetenschappen (bladzijde 1). Het vak-slug "economie" bestaat al voor
Boost; deze hoofdstukken krijgen niveau beyond-doorstroom.

Examen: 120 minuten, digitaal, gesloten en open vragen, geen giscorrectie.
Gewichten en het aantal thema's hier:

    de economie als systeem                        12,5 %  ->  3 thema's
    markt met volkomen concurrentie                12,5 %  ->  3 thema's
    markt met onvolkomen concurrentie              10   %  ->  2 thema's
    overheidsingrijpen op de markt                 10   %  ->  2 thema's
    arbeidsmarkt                                    7,5 %  ->  1 thema
    geld- en kapitaalmarkt                          7,5 %  ->  2 thema's
    inkomensongelijkheid, herverdeling, armoede     7,5 %  ->  1 thema
    internationale economie                        10   %  ->  2 thema's
    conjunctuur en conjunctuurbeleid               12,5 %  ->  3 thema's
    onderzoekscompetenties                         10   %  ->  1 thema

Samen twintig thema's, veertig hoofdstukken, achthonderd vragen. Elk thema is
een bestand met DEEL1 en DEEL2 van twintig vragen.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parents[1]))

from notatie import zichtbaar  # noqa: E402  (pad moet eerst klaarstaan)
DOEL = HIER.parent / "economie.json"

# De volgorde volgt de fiche van voor naar achter. Het aantal thema's per blok
# volgt de gewichten achteraan de fiche (zie hierboven).
THEMAS = [
    ("eco3_kringloop", "De economische kringloop en de macro-economische identiteiten"),
    ("eco3_duurzaam", "Alternatieve economische modellen, MVO en de SDG's"),
    ("eco3_bbp", "Het bbp, economische groei en welvaartsindicatoren"),
    ("eco3_vraag", "De vraagcurve en de prijselasticiteit van de vraag"),
    ("eco3_aanbod", "Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod"),
    ("eco3_surplus", "Consumenten- en producentensurplus en het welvaartsoptimum"),
    ("eco3_monopolie", "Marktvormen en het monopolie"),
    ("eco3_oligopolie", "Monopolistische concurrentie, oligopolie en speltheorie"),
    ("eco3_ingrijpen", "Prijsregulering, quota, belastingen en subsidies"),
    ("eco3_marktfalen", "Marktmacht, marktfalen, externe effecten en publieke goederen"),
    ("eco3_arbeid", "De arbeidsmarkt, werkloosheid en arbeidsmarktindicatoren"),
    ("eco3_geld", "Geld, monetaire aggregaten en geldschepping"),
    ("eco3_beleggen", "De financiële markt en beleggen"),
    ("eco3_ongelijkheid", "Inkomensongelijkheid, armoede en herverdeling"),
    ("eco3_handel", "Internationale handel en samenwerkingsverbanden"),
    ("eco3_wissel", "De wisselmarkt en de betalingsbalans"),
    ("eco3_conjunctuur", "De conjunctuur, conjunctuurindicatoren en de begroting"),
    ("eco3_evenwicht", "Het inkomensevenwicht, de multiplicator en het AV-AA-schema"),
    ("eco3_inflatie", "Inflatie, deflatie en prijsstabiliteit"),
    ("eco3_onderzoek", "Economisch onderzoek: onderzoeksvraag, methode en besluit"),
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
        lengtes = [len(zichtbaar(o)) for o in v["opties"]]
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
