# -*- coding: utf-8 -*-
"""Schrijft ../wiskunde-rekenen-en-breuken.json uit rekenen_en_breuken.py.

    python3 inhoud/start/bron/bouw_rekenen_en_breuken.py

Het hoofdstuk "Rekenen en breuken" bestaat al in het platform, met drie
voorbeeldvragen uit schema.sql. Dit bestand wordt geïmporteerd ZONDER
"Bestaande vragen vervangen", zodat die drie blijven staan en deze er
bijkomen.

Wat er nagekeken wordt voor er iets weggeschreven wordt:
  * geen vraag twee keer, en geen vraag die al in schema.sql staat;
  * elk meerkeuze-antwoord wijst naar een bestaande optie;
  * elke vraag met een veld `reken` komt uit op wat Python zelf uitrekent,
    en geen énkele andere optie komt op datzelfde getal uit.
Het veld `reken` gaat niet mee naar de JSON.
"""
import json
import pathlib
import re
import sys
from fractions import Fraction as F

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent.parent / "basis" / "bron"))

import reken                      # noqa: E402  (leest "3/4", "0,75", "€ 4,50")
import rekenen_en_breuken         # noqa: E402

DOEL = HIER.parent / "wiskunde-rekenen-en-breuken.json"
TITEL = "Rekenen en breuken"

# De drie vragen die al in supabase/schema.sql staan.
AL_IN_HET_PLATFORM = [
    "Wat is 3/4 van 100?",
    "Een rechthoek heeft 4 rechte hoeken.",
    "7 x 9 = ___",
]


def sleutel(vraag):
    return re.sub(r"[^a-z0-9]+", " ", vraag.lower()).strip()


def waarde(tekst):
    """Het getal in een optie of invulantwoord, als breuk. None als er geen is."""
    return reken.getal(str(tekst))


def main():
    vragen = rekenen_en_breuken.VRAGEN
    fouten = []

    gezien = {}
    for v in list(vragen) + [dict(vraag=q) for q in AL_IN_HET_PLATFORM]:
        s = sleutel(v["vraag"])
        if s in gezien:
            fouten.append(f"twee keer dezelfde vraag: {v['vraag']}")
        gezien[s] = True

    for v in vragen:
        if v["type"] == "meerkeuze":
            if not 0 <= v["antwoord"] < len(v["opties"]):
                fouten.append(f"antwoord wijst nergens naar: {v['vraag']}")
        if "reken" not in v:
            continue
        verwacht = v["reken"]
        if v["type"] == "invultekst":
            if waarde(v["antwoord"]) != F(verwacht):
                fouten.append(f"invulantwoord klopt niet: {v['vraag']} → {v['antwoord']}")
            continue
        juist = v["opties"][v["antwoord"]]
        if waarde(juist) != F(verwacht):
            fouten.append(f"aangeduide optie klopt niet: {v['vraag']} → {juist}")
        for i, optie in enumerate(v["opties"]):
            if i != v["antwoord"] and waarde(optie) == F(verwacht):
                fouten.append(f"twee opties zijn juist: {v['vraag']} → {optie}")

    if fouten:
        for f in fouten:
            print("  FOUT", f)
        return 1

    schoon = [{k: x for k, x in v.items() if k != "reken"} for v in vragen]
    DOEL.write_text(json.dumps(
        {"hoofdstukken": [{"titel": TITEL, "niveau": "start", "gratis": True, "vragen": schoon}]},
        ensure_ascii=False, indent=2) + "\n")
    print(f"  {len(schoon)} vragen geschreven in {DOEL.name}")
    print(f"  samen met de drie uit schema.sql: {len(schoon) + 3}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
