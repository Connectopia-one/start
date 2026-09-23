# -*- coding: utf-8 -*-
"""Het overzicht van de onderwijsdoelen die we voor 🌱 Start gebruikt hebben.

Dit is GEEN kopie van de officiële minimumdoelen. Het is ons eigen overzicht:
per vak de domeinen uit de minimumdoelen van het lager onderwijs, en welke
hoofdstukken wij daarvoor gemaakt hebben. Een ouder kan er in één blad mee
nakijken of er niets vergeten is.

De officiële tekst van de minimumdoelen staat bij de Vlaamse overheid. Wil je
die er ook bij, laad ze dan als apart document op via /beheer/doelen.

De aantallen hieronder komen uit de vragenbestanden zelf (../../start/*.json).
Draai dit script opnieuw als er hoofdstukken bijkomen.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

START = pathlib.Path(__file__).parent.parent.parent / "start"


def hoofdstukken(bestand):
    """De hoofdstukken uit een vragenbestand, met hun aantal vragen."""
    d = json.loads((START / bestand).read_text(encoding="utf-8"))
    return [(h["titel"], len(h["vragen"])) for h in d["hoofdstukken"]]


def lijst(bestand, extra=None):
    """Een opsomming van de hoofdstukken, met de aantallen samengeteld.

    `extra` is een tweede bestand met dezelfde hoofdstuktitels; dan tellen de
    vragen samen. Dat is zo bij wiskunde, waar de tweede reeks apart staat.
    """
    per_titel = {}
    volgorde = []
    for pad in [bestand] + ([extra] if extra else []):
        for titel, aantal in hoofdstukken(pad):
            if titel not in per_titel:
                volgorde.append(titel)
                per_titel[titel] = 0
            per_titel[titel] += aantal
    regels = "".join(
        f"<li><b>{titel}</b> — {per_titel[titel]} vragen</li>" for titel in volgorde
    )
    return f"<ul>{regels}</ul>"


BUNDEL = dict(
    vak="Alle vakken",
    niveau="🌱 Start — 5de en 6de leerjaar",
    soort="Overzicht",
    titel="De onderwijsdoelen die we gebruikt hebben",
    onder="Per vak: de domeinen uit de minimumdoelen van het lager onderwijs, en de hoofdstukken die wij daarvoor gemaakt hebben.",
    secties=[
        dict(kop="Waarover dit blad gaat", blokken=[
            ("p", "Onze oefeningen voor 🌱 Start zijn gemaakt aan de hand van de "
                  "<strong>minimumdoelen van het lager onderwijs</strong> van de Vlaamse overheid, "
                  "die gelden sinds <strong>1 september 2025</strong>. Het richtpunt is wat een kind "
                  "aan het einde van het <strong>zesde leerjaar</strong> moet kennen en kunnen."),
            ("p", "Op dit blad staat per vak welke domeinen de minimumdoelen onderscheiden, en welk "
                  "hoofdstuk bij ons daarbij hoort. Zo kan je nagaan of er niets ontbreekt, en waar "
                  "je kind op uitkomt als het een hoofdstuk kiest."),
            ("kader", "Dit is <strong>ons eigen overzicht</strong>, geen kopie van de officiële "
                      "tekst. De officiële minimumdoelen zijn van de Vlaamse overheid en zijn vrij "
                      "in te kijken. Wij hebben ze gelezen en er oefeningen bij gemaakt; de "
                      "formuleringen hieronder zijn de onze."),
        ]),
        dict(kop="Wiskunde", blokken=[
            ("p", "De minimumdoelen delen wiskunde op in <strong>zes domeinen</strong>. Wij hebben "
                  "voor elk domein een hoofdstuk gemaakt, met dezelfde naam, zodat de indeling "
                  "één op één te volgen is."),
            ("kader", lijst("wiskunde.json", "wiskunde-extra.json")),
            ("p", "Het domein <strong>probleemoplossend denken en vraagstukken</strong> staat bij "
                  "ons als „Vraagstukken en problemen oplossen”. Dat is hetzelfde domein; we hebben "
                  "de naam alleen wat korter gemaakt."),
        ]),
        dict(kop="Nederlands", blokken=[
            ("p", "Nederlands heeft <strong>vijf domeinen</strong> in de minimumdoelen. Ook hier "
                  "volgt elk hoofdstuk één domein."),
            ("kader", lijst("nederlands.json")),
            ("p", "<strong>Spelling</strong> hoort inhoudelijk bij taalsysteem en taalgebruik. Het "
                  "staat bij ons daarnaast ook als een apart, uitgebreider hoofdstuk, omdat dat het "
                  "gratis proefhoofdstuk is waarmee iemand zonder account het platform kan "
                  "uitproberen."),
            ("kader", lijst("nederlands-spelling.json")),
        ]),
        dict(kop="Wetenschap en techniek", blokken=[
            ("p", "De minimumdoelen onderscheiden hier <strong>vier gebieden</strong>. Elk gebied "
                  "heeft bij ons één hoofdstuk."),
            ("kader", lijst("wetenschap-en-techniek.json")),
        ]),
        dict(kop="Geschiedenis", blokken=[
            ("p", "De doelen gaan over <strong>historisch bewustzijn</strong>: kunnen omgaan met "
                  "tijd en met bronnen, en de grote periodes kunnen situeren. Wij hebben dat in "
                  "drie hoofdstukken gezet, met meer vragen per hoofdstuk dan bij de andere vakken, "
                  "omdat de plusklas hiermee start."),
            ("kader", lijst("geschiedenis.json")),
        ]),
        dict(kop="Aardrijkskunde", blokken=[
            ("p", "De doelen gaan over <strong>ruimtelijk bewustzijn</strong>: een kaart kunnen "
                  "lezen, je kunnen oriënteren, en weten hoe de eigen streek en de wijdere wereld "
                  "in elkaar zitten."),
            ("kader", lijst("aardrijkskunde.json")),
        ]),
        dict(kop="Engels", blokken=[
            ("p", "In het lager onderwijs gaat het om een <strong>eerste kennismaking</strong>: "
                  "woordenschat voor alledaagse situaties, en net genoeg grammatica om eenvoudige "
                  "zinnen te begrijpen en te maken."),
            ("kader", lijst("engels.json")),
        ]),
        dict(kop="Wat we niet aanbieden, en waarom", blokken=[
            ("p", "De minimumdoelen tellen acht vakdisciplines. Twee daarvan staan niet op ons "
                  "platform: <strong>muzische vorming</strong> en <strong>lichamelijke "
                  "opvoeding</strong>. Die leer je niet uit vragen met een juist antwoord, en een "
                  "oefenplatform is er dus niet de goede plek voor. <strong>Frans</strong> is in "
                  "opbouw."),
            ("p", "Zie je iets wat volgens jou wél thuishoort in een hoofdstuk, of net niet? Laat "
                  "het ons weten via <strong>info@matmgroep.com</strong>, dan kijken we het na."),
        ]),
    ],
)

if __name__ == "__main__":
    bundel.schrijf(BUNDEL, "onderwijsdoelen-lager-onderwijs")
