# -*- coding: utf-8 -*-
"""Schrijft ../wiskunde-extra-6de.json uit wiskunde_extra_6de.py en rekent na.

    python3 inhoud/start/bron/bouw_wiskunde_extra_6de.py
Importeren in vak Wiskunde (Start), nieuw hoofdstuk, zonder 'vervangen'.
"""
import json, pathlib, sys, collections
from fractions import Fraction as F
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER)); sys.path.insert(0, str(HIER.parent.parent / "basis" / "bron"))
import reken, wiskunde_extra_6de as bron

TITEL = "Nog meer voor het 6de leerjaar"
DOEL = HIER.parent / "wiskunde-extra-6de.json"

def main():
    fouten, gezien = [], set()
    for v in bron.VRAGEN:
        s = reken.plat(v["vraag"]).lower()
        if s in gezien: fouten.append("dubbel: " + v["vraag"])
        gezien.add(s)
        if "fiche" in json.dumps(v, ensure_ascii=False, default=str).lower(): fouten.append("fiche: " + v["vraag"])
        if v["type"] == "meerkeuze":
            if not 0 <= v["antwoord"] < len(v["opties"]): fouten.append("antwoord: " + v["vraag"])
            if len(set(v["opties"])) != len(v["opties"]): fouten.append("dubbele optie: " + v["vraag"])
        if "reken" not in v: continue
        w = F(v["reken"])
        if v["type"] == "invultekst":
            if reken.getal(v["antwoord"]) != w: fouten.append("invul klopt niet: " + v["vraag"])
            continue
        if reken.getal(v["opties"][v["antwoord"]]) != w: fouten.append("optie klopt niet: " + v["vraag"])
        for i, o in enumerate(v["opties"]):
            if i != v["antwoord"] and reken.getal(o) == w: fouten.append("twee juist: " + v["vraag"])
    mk = [v for v in bron.VRAGEN if v["type"] == "meerkeuze"]
    langst = sum(1 for v in mk if len(reken.plat(v["opties"][v["antwoord"]])) >= max(len(reken.plat(o)) for o in v["opties"]))
    wn = collections.Counter(v["antwoord"] for v in bron.VRAGEN if v["type"] == "waarofniet")
    print(len(bron.VRAGEN), "vragen;", collections.Counter(v["type"] for v in bron.VRAGEN), "; langste juist", langst, "/", len(mk), "; waar/niet", dict(wn))
    if len(bron.VRAGEN) != 40: fouten.append("niet 40")
    if fouten: print("\n".join(fouten)); sys.exit(1)
    vr = [{k: x for k, x in v.items() if k != "reken"} for v in bron.VRAGEN]
    DOEL.write_text(json.dumps({"hoofdstukken": [{"titel": TITEL, "niveau": "start", "vragen": vr}]}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("geschreven", DOEL)

main()
