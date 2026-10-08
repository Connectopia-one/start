# -*- coding: utf-8 -*-
"""Bouwt de poster met alle vakken die op het oefenplatform staan.

    python3 -I maak_vakkenoverzicht.py
    PW=$(npm root -g)/playwright node render-vakken.js

Waarvoor: Kim op 8 oktober 2026, toen mensen haar één voor één begonnen te
vragen of hún vak erbij stond — "zo kan ik dit sturen naar alle mensen die nu
mij apart aan het vragen zijn of hun vak ertussen staat".

De lijst wordt **geteld uit `oefenplatform/inhoud/`**, niet met de hand
bijgehouden. Komt er een vak bij, dan draai je dit script opnieuw en staat het
erop. Een bestand dat enkel extra vragen bij een bestaand vak zet
(`-varianten`, `-pittig`, `-uitdaging`, `wiskunde-extra`, `nederlands-spelling`
en zo) telt niet als apart vak; die staan in SAMEN hieronder.

De namen van de vakken zijn die van de bestanden, met de hand netjes
geschreven in NAMEN. Staat een nieuw vak er niet bij, dan valt het op: het
krijgt dan zijn bestandsnaam met streepjes, en dat zie je meteen op de poster.
"""
import json
import pathlib
import re

HIER = pathlib.Path(__file__).parent
INHOUD = HIER.parent.parent.parent / "oefenplatform" / "inhoud"

# Bestanden die bij een ander vak horen in plaats van zelf een vak te zijn.
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

# (map, titel, wie het is, de kleur van het blok). KOLOMMEN zegt waar elk blok
# terechtkomt: twee kolommen naast elkaar, en wat in BREED staat gaat eronder
# over de volle breedte. Zo staan de twee kolommen even hoog; de browser kan
# dat zelf niet, want een blok mag niet middenin afgebroken worden.
BLOKKEN = [
    ("start", "🌱 Start", "5de en 6de leerjaar", "groen"),
    ("basis", "🧱 Basis", "de bouwstenen opnieuw, op eigen tempo", "groen"),
    ("spark", "✨ Spark", "1ste en 2de middelbaar, de hele A-stroom", "paars"),
    ("boost-doorstroom", "🚀 Boost · doorstroom", "3de en 4de middelbaar — economische wetenschappen, "
     "humane wetenschappen, Latijn, moderne talen, natuurwetenschappen", "oranje"),
    ("boost-dubbele-finaliteit", "🚀 Boost · dubbele finaliteit",
     "3de en 4de middelbaar — bedrijf en organisatie, maatschappij en welzijn", "oranje"),
    ("beyond", "🌍 Beyond · doorstroom", "5de en 6de middelbaar — economie-wiskunde, humane "
     "wetenschappen, Latijn-moderne talen, Latijn-wiskunde, moderne talen, "
     "wetenschappen-wiskunde", "blauw"),
    ("beyond-dubbele-finaliteit", "🌍 Beyond · dubbele finaliteit",
     "5de en 6de middelbaar — basisvorming en commerciële organisatie", "blauw"),
    ("hoekje", "🔭 De uitdagingshoek", "naast de leerstof, voor wie graag verder kijkt", "paars"),
]


LINKS = ["start", "basis", "spark", "boost-doorstroom"]
RECHTS = ["boost-dubbele-finaliteit", "beyond", "beyond-dubbele-finaliteit"]
BREED = ["hoekje"]


def vakken_van(map_):
    """De vakken van één map, met hun aantal hoofdstukken en vragen."""
    rijen = []
    for pad in sorted((INHOUD / map_).glob("*.json")):
        if SAMEN.search(pad.stem):
            continue
        d = json.loads(pad.read_text(encoding="utf-8"))
        hs = d.get("hoofdstukken", [])
        rijen.append((NAMEN.get(pad.stem, pad.stem), len(hs),
                      sum(len(h["vragen"]) for h in hs)))
    return rijen


def tel_alles():
    """Álle vragen, dus ook die van de bestanden die bij een vak horen."""
    h = v = 0
    for pad in INHOUD.glob("*/*.json"):
        if pad.parent.name in ("leerbundels-interactief", "prenten", "puzzels"):
            continue
        d = json.loads(pad.read_text(encoding="utf-8"))
        if "hoofdstukken" not in d:
            continue
        h += len(d["hoofdstukken"])
        v += sum(len(x["vragen"]) for x in d["hoofdstukken"])
    return h, v


def main():
    gemaakt = {}
    vakken_totaal = 0
    for map_, titel, wie, kleur in BLOKKEN:
        rijen = vakken_van(map_)
        vakken_totaal += len(rijen)
        pillen = "".join(f'<span class="vak">{naam}</span>' for naam, _, _ in rijen)
        hoeveel = "1 vak" if len(rijen) == 1 else f"{len(rijen)} vakken"
        gemaakt[map_] = f'''    <section class="blok {kleur}">
      <div class="blokkop"><h2>{titel}</h2><span class="hoeveel">{hoeveel}</span></div>
      <p class="wie">{wie}</p>
      <div class="vakken">{pillen}</div>
    </section>'''

    kolommen = ('  <div class="kolom">\n' + "\n".join(gemaakt[m] for m in LINKS) + "\n  </div>\n"
                '  <div class="kolom">\n' + "\n".join(gemaakt[m] for m in RECHTS) + "\n  </div>")
    breed = "\n".join(gemaakt[m] for m in BREED)
    blokken = [kolommen, '  <div class="breed">\n' + breed + "\n  </div>"]

    hoofdstukken, vragen = tel_alles()
    html = (HIER / "vakkenoverzicht-sjabloon.html").read_text(encoding="utf-8")
    uit = HIER / "vakkenoverzicht.html"
    uit.write_text(html
                   .replace("<!--BLOKKEN-->", "\n".join(blokken))
                   .replace("<!--VAKKEN-->", str(vakken_totaal))
                   .replace("<!--HOOFDSTUKKEN-->", f"{hoofdstukken:,}".replace(",", ".") )
                   .replace("<!--VRAGEN-->", f"{vragen:,}".replace(",", ".")),
                   encoding="utf-8")
    print(f"{uit} — {vakken_totaal} vakken, {hoofdstukken} hoofdstukken, {vragen} vragen")


if __name__ == "__main__":
    main()
