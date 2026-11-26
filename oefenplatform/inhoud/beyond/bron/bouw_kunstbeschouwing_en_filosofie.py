# -*- coding: utf-8 -*-
"""Zet de thema's samen in ../kunstbeschouwing-en-filosofie.json.

    python3 bron/bouw_kunstbeschouwing_en_filosofie.py

🌍 Beyond, derde graad doorstroomfinaliteit. De fiche
`2027_Kunstbeschouwing en filosofie_3DDO` geldt voor één studierichting:
humane wetenschappen. Gevraagd door een ouder op 26 november 2026.

Het examen duurt 120 minuten en weegt:

    kunstbeschouwing   35 %  ->  7 thema's (kfb_*)
    filosofie          65 %  -> 15 thema's

Het deel filosofie is op twee stukken na woord voor woord hetzelfde als het
deel filosofie van de fiche Filosofie en recht (3DDG, welzijnswetenschappen).
Daarom gebruikt dit vak de twaalf filosofiethema's `fr_*` van filosofie en
recht opnieuw, met precies dezelfde vragen: een leerling volgt maar één van
de twee vakken. Wat deze fiche extra vraagt, staat in drie eigen thema's:
de zijnsleer en twee thema's politieke filosofie (kfb_*). De kritiek van Joan
Tronto op hoe de samenleving zorg organiseert, zit in het tweede thema
politieke filosofie.

Dezelfde waarschuwing als bij filosofie en recht: zet geen naam bij die niet
in de fiche staat, en hang aan een naam geen stelling die de fiche niet noemt.

Elk thema is een bestand met DEEL1 en DEEL2 van twintig vragen en wordt hier
twee hoofdstukken, "<thema> — deel 1" en "<thema> — deel 2".
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parents[1]))

from notatie import zichtbaar  # noqa: E402  (pad moet eerst klaarstaan)
DOEL = HIER.parent / "kunstbeschouwing-en-filosofie.json"

# De volgorde volgt de fiche: eerst kunstbeschouwing, dan filosofie.
THEMAS = [
    # kunstbeschouwing (35 %)
    ("kfb_kunstvormen", "Kunst, cultuur en de kunstvormen"),
    ("kfb_inhoud", "Inhoud, functies en context van een kunstuiting"),
    ("kfb_oudheid", "Kunst van de prehistorie, Egypte en de klassieke oudheid"),
    ("kfb_middeleeuwen", "Middeleeuwen, renaissance en barok"),
    ("kfb_modern", "Van romantiek tot popart: moderne en hedendaagse kunst"),
    ("kfb_elementen", "Niet-westerse invloeden en kunsthistorische elementen"),
    ("kfb_analyse", "Kunstanalyse en kunstreflectie"),
    # filosofie (65 %)
    ("fr_eigenheid", "De eigenheid van de filosofie"),
    ("fr_lichaamgeest", "Lichaam en geest: monisme en dualisme"),
    ("fr_mensdier", "Cultuur en natuur: mens, dier en machine"),
    ("fr_vrijheid1", "Vrijheid en determinisme van de oudheid tot de 19de eeuw"),
    ("fr_vrijheid2", "Vrijheid en determinisme in de 20ste eeuw"),
    ("fr_ethiek", "Ethiek: basisbegrippen en vier benaderingen"),
    ("fr_gevolgplicht", "Gevolgenethiek en plichtethiek"),
    ("fr_deugdzorg", "Deugdethiek en zorgethiek"),
    ("fr_geluk", "Ethiek en geluk"),
    ("kfb_zijnsleer", "Zijnsleer: schijn en werkelijkheid, worden en zijn"),
    ("fr_kennis", "Bronnen van kennis, rationalisme en empirisme"),
    ("fr_falsificatie", "Van natuurfilosofie naar wetenschap: falsificatie en demarcatie"),
    ("fr_argumentatie", "Argumentatieleer: redeneervormen en drogredenen"),
    ("kfb_polfil1", "Politieke filosofie: individu, gemeenschap en legitimiteit"),
    ("kfb_polfil2", "Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid"),
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
