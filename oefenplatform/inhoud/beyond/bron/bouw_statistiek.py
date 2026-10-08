# -*- coding: utf-8 -*-
"""Zet de themabestanden `st_*.py` samen in ../statistiek.json.

    python3 bron/bouw_statistiek.py

🌍 Beyond, derde graad doorstroomfinaliteit. De fiche 2027_Statistiek_3DO
geldt voor één studierichting: **humane wetenschappen**. Dat staat op
bladzijde 1; lees dat altijd af in plaats van het te gokken.

Kim vroeg dit vak op 8 oktober 2026 aan omdat er iemand klaarstond om eraan
te beginnen. Statistiek bestaat bij ons nog niet als apart vak: er zit wel
kansrekenen en statistiek in wiskunde gevorderd, maar dat is de G2-fiche van
economie-wiskunde en wetenschappen-wiskunde, met een heel andere nadruk.

De gewichtentabel achteraan de fiche verdeelt het examen in twee:

    Telproblemen, kansrekenen en statistiek   60 %  ->  10 thema's
    Werken met grote datasets                 40 %  ->   7 thema's

plus één thema voor de bouwsteen probleemoplossend denken, die de fiche zelf
"geïntegreerd" noemt. Samen achttien thema's, zesendertig hoofdstukken.

Twee dingen waarin deze fiche strenger is dan de meeste:

  1. **Bij telproblemen alleen combinaties.** De fiche vraagt letterlijk
     "telproblemen zonder herhaling waarbij de volgorde niet belangrijk is:
     combinaties", plus de faculteit. Permutaties en variaties staan er niet
     in, dus staan ze hier ook niet.

  2. **De begrippen en notaties van de bijlage zijn de enige die gelden.**
     De fiche zegt met zoveel woorden: "Alle andere begrippen en notaties
     worden als foutief beschouwd." Dus X ~ B(n, p), X ~ N(mu, sigma),
     Z ~ N(0,1), x met een streepje tegenover mu, p met een dakje tegenover
     p, s tegenover sigma.

**Bij statistiek geen meerkeuze met meerdere juiste antwoorden**, net zoals
bij wiskunde: een berekening heeft één uitkomst. Het script weigert er dan
ook een.

Twee thema's zijn rekenthema's met de rekenapps, op vraag van Kim op
8 oktober 2026: "ik denk dat je met statistiek wel meer oefeningen nodig hebt
die je met geogebra gaat moeten oplossen." Ze staan vol invulvragen met een
getal als antwoord, want kiezen uit vier getallen kan je nog gokken.

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
DOEL = HIER.parent / "statistiek.json"

# De volgorde volgt de fiche: eerst probleemoplossend denken, dan het blok van
# zestig procent (telproblemen, kansrekenen, hypothesetoetsen,
# betrouwbaarheidsintervallen, spreidingsdiagrammen) en ten slotte het blok
# van veertig procent over grote datasets. De twee rekenthema's met de
# rekenapps staan telkens aan het eind van hun blok, zodat een kind eerst de
# begrippen heeft gezien voor het de knoppen indrukt.
THEMAS = [
    ("st_problemen", "Problemen oplossen en ICT gebruiken"),
    ("st_telregels", "De telregels: product, som en complement"),
    ("st_combinaties", "Faculteit en combinaties"),
    ("st_binomiaal", "Kansvariabelen en de binomiale verdeling"),
    ("st_verwachting", "Verwachtingswaarde, variantie en standaardafwijking"),
    ("st_normaal", "De normale verdeling en standaardiseren"),
    ("st_steekproeven", "Populatie, steekproef en de steekproevenverdeling"),
    ("st_hypothese", "Hypothesen opstellen: H0, H1 en de richting"),
    ("st_pwaarde", "De p-waarde, het significantieniveau en de twee fouten"),
    ("st_betrouwbaarheid", "Betrouwbaarheidsinterval en foutenmarge"),
    ("st_spreidingsdiagram", "Spreidingsdiagrammen, trendlijn en correlatie"),
    ("st_ictkansen", "Kansen berekenen met de kansrekenmachine"),
    ("st_frequentietabel", "Frequentietabellen en gegevens groeperen"),
    ("st_grafieken", "De juiste grafische voorstelling kiezen"),
    ("st_kengetallen", "Centrummaten: gemiddelde, mediaan en modus"),
    ("st_spreiding", "Spreidingsmaten en de boxplot"),
    ("st_ictdata", "Een dataset doorrekenen met het rekenblad"),
    ("st_onderzoek", "Een statistisch onderzoek met de rekenapps"),
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
        if isinstance(antwoord, list):
            raise SystemExit(
                f"{plek} heeft meerdere juiste antwoorden; bij statistiek mag dat niet"
            )
        if not isinstance(antwoord, int) or not 0 <= antwoord < len(opties):
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
    meerkeuze = invul = waarofniet = 0
    for h in hoofdstukken:
        for v in h["vragen"]:
            tekst = " ".join(v["vraag"].lower().split())
            if tekst in gezien:
                raise SystemExit(
                    f"Deze vraag staat twee keer, in {gezien[tekst]} en in {h['titel']}:\n  {v['vraag']}"
                )
            gezien[tekst] = h["titel"]
            meerkeuze += v["type"] == "meerkeuze"
            invul += v["type"] == "invultekst"
            waarofniet += v["type"] == "waarofniet"

    for h in hoofdstukken:
        for melding in gokpatronen(h["titel"], h["vragen"]):
            raise SystemExit(melding)
    for melding in evenwicht_waar(hoofdstukken):
        raise SystemExit(melding)

    print(
        f"\n{meerkeuze} meerkeuzevragen, {waarofniet} waar of niet waar, {invul} invulvragen."
    )

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
