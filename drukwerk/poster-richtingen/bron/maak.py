# -*- coding: utf-8 -*-
"""Bouwt de poster met, per studierichting, de vakken die op het oefenplatform staan.

    python3 -I maak.py
    node render.js

Waarvoor: Kim vroeg dit op 11 oktober 2026, in één zin — "een poster op A4
maken waar elke richting staat en waaronder telkens staat welke vakken er voor
hun op het platform staan". Mensen vragen haar één voor één of hún richting
erbij zit; de poster van 8 oktober (`social/posts/`) telt de vakken per
categorie op, maar zegt niet voor wie ze zijn.

**Welke richting welk vak volgt, staat op bladzijde 1 van de vakfiche**, en de
bouwscripts van het oefenplatform schrijven dat in hun docstring. De tabel
RICHTINGEN hieronder is daar regel per regel uit overgenomen; de bron staat bij
elke categorie als commentaar. Gok nooit uit de naam van een vak: de
Nederlands-fiches van 🚀 Boost gelden bijvoorbeeld **niet** voor moderne talen,
dat is de uitzondering die je anders mist.

Het script controleert zichzelf twee kanten op:
- elk vak dat hier genoemd wordt, moet als `inhoud/<categorie>/<vak>.json`
  bestaan, anders stopt het;
- elk vakbestand dat bestaat maar bij geen enkele richting staat, wordt gemeld.
  Zo valt een nieuw vak meteen op in plaats van stilletjes te ontbreken.

Komt er een vak bij, zet het dan bij de richtingen van zijn fiche en draai dit
script opnieuw.
"""
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent
INHOUD = HIER.parent.parent.parent / "oefenplatform" / "inhoud"

# Bestanden die extra vragen bij een bestaand vak zetten in plaats van zelf een
# vak te zijn. Zelfde lijst als in social/posts/bron/maak_vakkenoverzicht.py.
SAMEN = re.compile(
    r"-(varianten|pittig|uitdaging|prenten|extra|meetkunde|meetkunde-metend|"
    r"rekenen-en-breuken|spelling|spelling-varianten|begrijpend-lezen)$"
)

NAMEN = {
    "aardrijkskunde": "aardrijkskunde",
    "biologie": "biologie",
    "chemie": "chemie",
    "coderen-en-computers": "coderen en computers",
    "de-ruimte": "de ruimte",
    "economie": "economie",
    "economie-en-bedrijfswetenschappen": "economie en bedrijfswetenschappen",
    "engels": "Engels",
    "filosofie-en-recht": "filosofie en recht",
    "frans": "Frans",
    "fysica": "fysica",
    "geschiedenis": "geschiedenis",
    "geschiedenis-van-belgie": "geschiedenis van België",
    "gezondheid-zorg-en-welzijn": "gezondheid, zorg en welzijn",
    "kunstbeschouwing-en-filosofie": "kunstbeschouwing en filosofie",
    "natuurwetenschappen": "natuurwetenschappen",
    "nederlands": "Nederlands",
    "ontwikkeling-en-pedagogisch-handelen": "ontwikkeling en pedagogisch handelen",
    "paradoxen-en-weetjes": "paradoxen en weetjes",
    "samenleving-en-economie": "samenleving en economie",
    "sociale-en-gedragswetenschappen": "sociale en gedragswetenschappen",
    "statistiek": "statistiek",
    "techniek": "techniek",
    "toegepaste-economie": "toegepaste economie",
    "wetenschap-en-techniek": "wetenschap en techniek",
    "wiskunde": "wiskunde",
    "wiskunde-basis": "wiskunde basis",
    "wiskunde-gevorderd": "wiskunde gevorderd",
}

# ── de categorieën zonder studierichting ────────────────────────────────────
ZONDER = [
    ("start", "🌱 Start", "5de en 6de leerjaar"),
    ("spark", "✨ Spark", "1ste en 2de middelbaar"),
    ("basis", "🧱 Basis", "de bouwstenen herhalen, voor elk niveau"),
    ("hoekje", "🔭 Uitdagingshoek", "naast de leerstof, voor wie ver doordenkt"),
]

# ── de categorieën met studierichtingen ─────────────────────────────────────
# Overgenomen uit de docstrings van inhoud/<categorie>/bron/bouw_<vak>.py, die
# bladzijde 1 van elke vakfiche weergeven.
#
# 🚀 Boost doorstroom, tweede graad:
#   aardrijkskunde en geschiedenis  -> alle vijf
#   Nederlands, Engels, Frans       -> vier, zónder moderne talen (dat heeft
#                                      eigen, zwaardere talenfiches)
#   natuurwetenschappen             -> vier, zónder de richting
#                                      natuurwetenschappen zelf
#   wiskunde gevorderd              -> vier, humane volgt wiskunde basis
#   economie                        -> economische wetenschappen
#   kunstbeschouwing en filosofie,
#   sociale en gedragswetenschappen -> humane wetenschappen
#   biologie, chemie, fysica        -> de richting natuurwetenschappen, die haar
#                                      wetenschappen in drie examens aflegt
GEDEELD_BOOST = ["aardrijkskunde", "geschiedenis"]
TALEN_BOOST = ["nederlands", "engels", "frans"]

BOOST_DOORSTROOM = [
    ("Economische wetenschappen",
     GEDEELD_BOOST + TALEN_BOOST + ["natuurwetenschappen", "wiskunde-gevorderd", "economie"]),
    ("Humane wetenschappen",
     GEDEELD_BOOST + TALEN_BOOST + ["natuurwetenschappen", "wiskunde-basis",
                                    "kunstbeschouwing-en-filosofie",
                                    "sociale-en-gedragswetenschappen"]),
    ("Latijn",
     GEDEELD_BOOST + TALEN_BOOST + ["natuurwetenschappen", "wiskunde-gevorderd"]),
    ("Moderne talen",
     GEDEELD_BOOST + ["natuurwetenschappen", "wiskunde-gevorderd"]),
    ("Natuurwetenschappen",
     GEDEELD_BOOST + TALEN_BOOST + ["biologie", "chemie", "fysica", "wiskunde-gevorderd"]),
]

# 🚀 Boost dubbele finaliteit: zeven fiches gelden voor allebei de richtingen,
# vier zijn van één richting.
GEDEELD_BOOST_DF = ["aardrijkskunde", "geschiedenis", "nederlands", "engels", "frans",
                    "natuurwetenschappen", "wiskunde"]
BOOST_DF = [
    ("Bedrijf en organisatie",
     GEDEELD_BOOST_DF + ["economie-en-bedrijfswetenschappen", "toegepaste-economie"]),
    ("Maatschappij en welzijn",
     GEDEELD_BOOST_DF + ["gezondheid-zorg-en-welzijn", "ontwikkeling-en-pedagogisch-handelen"]),
]

# 🌍 Beyond doorstroom, derde graad. Hier verschilt het per vak sterk:
#   aardrijkskunde, geschiedenis, samenleving en economie -> alle acht
#   Nederlands            -> zes, zonder moderne talen en Latijn-moderne talen
#   Engels                -> enkel de twee domeingebonden (van hun fiche gebouwd)
#   Frans                 -> humane, Latijn-wiskunde, wetenschappen-wiskunde,
#                            economie-wiskunde; de domeingebonden fiche staat op
#                            B1 en de onze op B1+, dus zij kunnen hem ook gebruiken
#   natuurwetenschappen   -> moderne talen, humane, Latijn-moderne talen,
#                            economie-wiskunde, bedrijfswetenschappen
#   biologie/chemie/fysica-> wetenschappen-wiskunde, Latijn-wiskunde
#   wiskunde gevorderd    -> economie-wiskunde, Latijn-wiskunde, wetenschappen-wiskunde
#   statistiek            -> humane wetenschappen
#   sociale en gedragsw.,
#   filosofie en recht    -> welzijnswetenschappen
GEDEELD_BEYOND = ["aardrijkskunde", "geschiedenis", "samenleving-en-economie"]

BEYOND_DOORSTROOM = [
    ("Economie-wiskunde",
     GEDEELD_BEYOND + ["nederlands", "frans", "natuurwetenschappen", "wiskunde-gevorderd"]),
    ("Humane wetenschappen",
     GEDEELD_BEYOND + ["nederlands", "frans", "natuurwetenschappen", "statistiek"]),
    ("Latijn-moderne talen",
     GEDEELD_BEYOND + ["natuurwetenschappen"]),
    ("Latijn-wiskunde",
     GEDEELD_BEYOND + ["nederlands", "frans", "biologie", "chemie", "fysica",
                       "wiskunde-gevorderd"]),
    ("Moderne talen",
     GEDEELD_BEYOND + ["natuurwetenschappen"]),
    ("Wetenschappen-wiskunde",
     GEDEELD_BEYOND + ["nederlands", "frans", "biologie", "chemie", "fysica",
                       "wiskunde-gevorderd"]),
    ("Bedrijfswetenschappen",
     GEDEELD_BEYOND + ["nederlands", "engels", "frans", "natuurwetenschappen"]),
    ("Welzijnswetenschappen",
     GEDEELD_BEYOND + ["nederlands", "engels", "frans",
                       "sociale-en-gedragswetenschappen", "filosofie-en-recht"]),
]

# 🌍 Beyond dubbele finaliteit: één stel fiches voor allebei.
GEDEELD_BEYOND_DF = ["aardrijkskunde", "geschiedenis", "nederlands", "engels", "frans",
                     "natuurwetenschappen", "wiskunde"]
BEYOND_DF = [
    ("Basisvorming", GEDEELD_BEYOND_DF),
    ("Commerciële organisatie", GEDEELD_BEYOND_DF),
]

MET = [
    ("boost-doorstroom", "🚀 Boost doorstroom", "3de en 4de middelbaar", BOOST_DOORSTROOM),
    ("boost-dubbele-finaliteit", "🚀 Boost dubbele finaliteit", "3de en 4de middelbaar", BOOST_DF),
    ("beyond-doorstroom", "🌍 Beyond doorstroom", "5de en 6de middelbaar", BEYOND_DOORSTROOM),
    ("beyond-dubbele-finaliteit", "🌍 Beyond dubbele finaliteit", "5de en 6de middelbaar", BEYOND_DF),
]

# De map in inhoud/ heet niet overal zoals de categorie in het platform.
MAP = {"beyond-doorstroom": "beyond"}

# Twee vakken dekken iets ruimer dan de fiche van die richting vraagt. Dat is
# geen fout, maar het hoort er wel bij te staan.
VOETNOTEN = [
    "Wetenschappen-wiskunde heeft een eigen, zwaardere aardrijkskundefiche; "
    "bodems en oceanen staan er bij ons nog niet in.",
    "Economische en humane wetenschappen van 🚀 Boost volgen de kortere fiche "
    "natuurwetenschappen, dus dat vak is bij ons iets ruimer dan wat jij moet kennen.",
]


def vakken_van(categorie):
    """De vakbestanden die écht in inhoud/<categorie>/ staan, als slugs."""
    map_ = INHOUD / MAP.get(categorie, categorie)
    uit = set()
    for pad in sorted(map_.glob("*.json")):
        slug = SAMEN.sub("", pad.stem)
        uit.add(slug)
    return uit


def controleer():
    """Elk genoemd vak moet bestaan, en elk bestaand vak moet genoemd zijn."""
    fouten, meldingen = [], []
    for cat, _, _, richtingen in MET:
        er = vakken_van(cat)
        genoemd = {v for _, lijst in richtingen for v in lijst}
        for v in sorted(genoemd - er):
            fouten.append(f"{cat}: {v} staat op de poster maar niet in inhoud/")
        for v in sorted(er - genoemd):
            meldingen.append(f"{cat}: {v} staat in inhoud/ maar bij geen enkele richting")
        for v in sorted(genoemd):
            if v not in NAMEN:
                fouten.append(f"{cat}: {v} heeft geen nette naam in NAMEN")
    for cat, _, _ in ZONDER:
        for v in sorted(vakken_van(cat)):
            if v not in NAMEN:
                fouten.append(f"{cat}: {v} heeft geen nette naam in NAMEN")
    return fouten, meldingen


# Mappen onder inhoud/ die geen vragen dragen maar wel json bevatten.
GEEN_VRAGEN = ("leerbundels-interactief", "prenten", "puzzels")


def tel():
    """Hoeveel vakken, hoofdstukken en vragen er in totaal staan.

    De vakken tellen we enkel in de categoriemappen hierboven, want mappen als
    pittig/, uitdaging/ en varianten/ dragen extra vragen bij een vak dat al
    geteld is. De hoofdstukken en de vragen tellen we wél overal, anders mis je
    net die extra's. Zelfde telling als social/posts/bron/maak_vakkenoverzicht.py,
    zodat de twee posters nooit een ander getal geven.
    """
    vakken = 0
    for cat, _, _ in ZONDER:
        vakken += len(vakken_van(cat))
    for cat, _, _, _ in MET:
        vakken += len(vakken_van(cat))

    hoofdstukken = vragen = 0
    for pad in INHOUD.glob("*/*.json"):
        if pad.parent.name in GEEN_VRAGEN:
            continue
        g = json.loads(pad.read_text(encoding="utf-8"))
        if "hoofdstukken" not in g:
            continue
        hoofdstukken += len(g["hoofdstukken"])
        vragen += sum(len(x["vragen"]) for x in g["hoofdstukken"])
    return vakken, hoofdstukken, vragen


def punten(n):
    """1843 wordt 1.843. Nederlandse duizendtallen, zonder locale."""
    return f"{n:,}".replace(",", ".")


def naam(slug):
    return NAMEN.get(slug, slug)


def rij(titel, lijst):
    # casefold, anders staan Engels, Frans en Nederlands vooraan en
    # aardrijkskunde erachter, want een hoofdletter sorteert eerst.
    namen = ", ".join(naam(v) for v in sorted(lijst, key=lambda v: naam(v).casefold()))
    return (f'      <div class="richting"><p class="wie">{titel}</p>'
            f'<p class="vakken">{namen}</p></div>')


def bouw():
    fouten, meldingen = controleer()
    for m in meldingen:
        print("LET OP:", m)
    if fouten:
        for f in fouten:
            print("FOUT:", f)
        sys.exit(1)

    stukken = []

    kaartjes = []
    for cat, titel, wie in ZONDER:
        namen = ", ".join(naam(v) for v in sorted(vakken_van(cat), key=naam))
        kaartjes.append(f'      <div class="kaartje"><p class="wie">{titel}'
                        f'<span>{wie}</span></p><p class="vakken">{namen}</p></div>')
    stukken.append('  <section class="blok zonder">\n'
                   '    <h2>Zonder studierichting</h2>\n'
                   '    <div class="kaartjes">\n' + "\n".join(kaartjes) + "\n    </div>\n  </section>")

    for cat, titel, wie, richtingen in MET:
        rijen = "\n".join(rij(t, l) for t, l in richtingen)
        stukken.append(f'  <section class="blok">\n'
                       f'    <h2>{titel} <small>{wie}</small></h2>\n'
                       f'    <div class="richtingen">\n{rijen}\n    </div>\n  </section>')

    vakken, hoofdstukken, vragen = tel()
    noten = "".join(f"<li>{n}</li>" for n in VOETNOTEN)
    sjabloon = (HIER / "sjabloon.html").read_text(encoding="utf-8")
    uit = (sjabloon
           .replace("<!--BLOKKEN-->", "\n".join(stukken))
           .replace("<!--NOTEN-->", noten)
           .replace("<!--TELLING-->",
                    f"{vakken} vakken, {punten(hoofdstukken)} hoofdstukken en "
                    f"{punten(vragen)} oefenvragen"))
    (HIER / "poster.html").write_text(uit, encoding="utf-8")
    aantal = sum(len(r) for _, _, _, r in MET)
    print(f"poster.html — {aantal} richtingen, {len(ZONDER)} categorieën zonder richting, "
          f"{vakken} vakken / {hoofdstukken} hoofdstukken / {vragen} vragen")


if __name__ == "__main__":
    bouw()
