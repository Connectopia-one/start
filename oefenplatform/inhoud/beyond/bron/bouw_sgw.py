# -*- coding: utf-8 -*-
"""Zet de themabestanden `sg_*.py` samen in ../sociale-en-gedragswetenschappen.json.

    python3 bron/bouw_sgw.py

🌍 Beyond, derde graad doorstroomfinaliteit. De fiche
`2027_Sociale_en_gedragswetenschappen_3DDG` geldt volgens bladzijde 1 voor de
studierichting **welzijnswetenschappen**. Er bestaat een tweede fiche voor
**humane wetenschappen** (`_3DDO`); die is voor ongeveer drie kwart gelijk aan
deze. Kim vroeg op 9 oktober 2026 eerst de versie voor welzijnswetenschappen.
Lees het altijd af op bladzijde 1 in plaats van het te gokken.

De gewichtentabel achteraan verdeelt het examen in drie blokken. Het examen
duurt honderdvijftig minuten, het langste van alle fiches die we tot nu toe
hebben gezien, en er is geen giscorrectie.

    gedragswetenschappen   65 %  ->  13 thema's
    sociale wetenschappen  25 %  ->   5 thema's
    onderzoekscyclus       10 %  ->   2 thema's

Samen twintig thema's, veertig hoofdstukken, achthonderd vragen.

Gedragswetenschappen valt in de fiche uiteen in vijf onderdelen, en die
verdeling zit in de dertien thema's: ontwikkelingspsychologie vier,
sociale psychologie drie, persoonlijkheidspsychologie drie, pedagogiek twee
en communicatieve vaardigheden een.

Drie dingen die deze fiche anders maakt dan de andere:

  1. **Ze staat vol eigennamen, en die staan er letterlijk in.** Freud met vijf
     fasen en Erikson met acht, Pavlov, Watson en Skinner, Bandura, Piaget,
     Maslow, Rogers, Bronfenbrenner met vijf systemen, Vygotsky, Gray met BIS
     en BAS, Eysenck met PEN, Allport, Rotter, Sherif, Asch, Milgram, Zimbardo,
     Festinger, Tuckman, Heider, Weiner, Dweck, Durkheim, Mead, Parsons,
     Merton, Marx, Weber, Dahrendorf, Bourdieu, Davis en Moore, Goldthorpe,
     McCombs en Shaw, Gerbner, Hjarvard, Rosenberg, Gordon, Schalock en
     Verdugo, Rink, Bakker. Verzin er geen bij en verzin geen onderzoek bij een
     naam: wat hier staat, staat in de fiche.

  2. **Alles moet in een gegeven voorbeeld herkend worden.** Bijna elk leerdoel
     begint met "je herkent en benoemt ... in een gegeven voorbeeld". Daarom
     zijn hier veel vragen een kort geval met verzonnen namen, waarbij het kind
     het begrip moet aanwijzen, en niet de omschrijving van een begrip.

  3. **Het laatste blok is een onderzoekscyclus over alle leerstof van de
     sociale wetenschappen.** De zes criteria van een goede onderzoeksvraag
     (open, enkelvoudig, objectief, haalbaar, onderzoekbaar, relevant) krijgt
     het kind op het examen zelf ook, dus ze mogen hier gerust herkend worden
     in plaats van uit het hoofd opgesomd.

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
DOEL = HIER.parent / "sociale-en-gedragswetenschappen.json"

# De volgorde volgt de fiche van voor naar achter, zodat een kind de
# hoofdstukken in dezelfde orde terugvindt als in zijn cursus.
THEMAS = [
    # gedragswetenschappen (65 %): dertien thema's
    ("sg_ontwikkeling", "Ontwikkelingspsychologie: de begrippen en de drie basisvragen"),
    ("sg_biologisch", "Ontwikkeling: de biologische en de psychodynamische benadering"),
    ("sg_leren", "Ontwikkeling: de behavioristische en de cognitieve benadering"),
    ("sg_systemisch", "Ontwikkeling: de humanistische en de systemische benadering"),
    ("sg_sociaalgedrag", "Prosociaal gedrag, antisociaal gedrag en sociale cognitie"),
    ("sg_groepen", "Cognitieve dissonantie en processen in een groep"),
    ("sg_beinvloeding", "Sociale beïnvloeding: conformisme, inwilliging en gehoorzaamheid"),
    ("sg_persoonlijkheid", "Persoonlijkheid: wat ze is en hoe een brein reageert"),
    ("sg_persbenadering", "Persoonlijkheid: van Freud over Bandura naar Rogers"),
    ("sg_trekken", "Persoonlijkheid: trekken, de big five en HEXACO"),
    ("sg_opvoeding", "Opvoeden: milieus, dimensies, stijlen en middelen"),
    ("sg_pedmodellen", "Pedagogische modellen en opvoeden in bijzondere contexten"),
    ("sg_communicatie", "Communicatieve vaardigheden: kaders en gesprekstechnieken"),
    # sociale wetenschappen (25 %): vijf thema's
    ("sg_socialisatie", "Socialisatie: posities, rollen en vier visies"),
    ("sg_stratificatie", "Sociale stratificatie en de verklaringsmodellen"),
    ("sg_mobiliteit", "Sociale mobiliteit, meritocratie en het matheüseffect"),
    ("sg_media", "Mediatisering en de functies van de massamedia"),
    ("sg_beeldvorming", "Mediatheorieën, beeldvorming en persvrijheid"),
    # onderzoekscyclus (10 %): twee thema's
    ("sg_vraagstukken", "Maatschappelijke vraagstukken en de redeneeractiviteiten"),
    ("sg_onderzoek", "De onderzoekscyclus van oriënteren tot rapporteren"),
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
