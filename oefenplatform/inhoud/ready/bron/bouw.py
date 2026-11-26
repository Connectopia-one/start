# -*- coding: utf-8 -*-
"""Bouwt een Ready-hoofdstuk (2 delen van 20) en kijkt het na.

    python3 bouw.py wiskunde_tafels
Schrijft ../<module met - i.p.v. _>.json met twee hoofdstukken, niveau ready,
elk met een korte uitleg.
"""
import json, pathlib, sys, collections, importlib, re
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
bron = importlib.import_module(sys.argv[1])
DOEL = HIER.parent / (sys.argv[1].replace("_", "-") + ".json")


def getal(s):
    if isinstance(s, list): s = s[0]
    s = str(s).replace("−", "-").replace(" ", "").replace("euro", "")
    s = s.replace(",", ".")
    return float(s) if re.fullmatch(r"-?\d+(\.\d+)?", s) else None


def kijk(vragen, naam):
    fouten, gezien = [], set()
    for v in vragen:
        s = v["vraag"].lower()
        if s in gezien: fouten.append("dubbel: " + v["vraag"])
        gezien.add(s)
        if "fiche" in json.dumps(v, ensure_ascii=False).lower(): fouten.append("fiche: " + v["vraag"])
        if v["type"] == "meerkeuze":
            if not 0 <= v["antwoord"] < len(v["opties"]): fouten.append("antwoord: " + v["vraag"])
            if len(set(v["opties"])) != len(v["opties"]): fouten.append("dubbele optie: " + v["vraag"])
        if "reken" in v:
            w = v["reken"]
            juist = v["antwoord"] if v["type"] == "invultekst" else v["opties"][v["antwoord"]]
            if getal(juist) != w: fouten.append("klopt niet: " + v["vraag"])
            if v["type"] == "meerkeuze":
                for i, o in enumerate(v["opties"]):
                    if i != v["antwoord"] and getal(o) == w: fouten.append("twee juist: " + v["vraag"])
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = sum(1 for v in mk if all(len(v["opties"][v["antwoord"]]) > len(o) for i, o in enumerate(v["opties"]) if i != v["antwoord"]))
    pos = collections.Counter(v["antwoord"] for v in mk)
    wn = collections.Counter(v["antwoord"] for v in vragen if v["type"] == "waarofniet")
    print(naam, len(vragen), "vragen;", dict(collections.Counter(v["type"] for v in vragen)),
          "; langste juist", langst, "/", len(mk), "; positie", dict(pos), "; waar/niet", dict(wn))
    if len(vragen) != 20: fouten.append("niet 20")
    if mk and langst / len(mk) > 0.4: fouten.append(f"{naam}: juiste antwoord te vaak het langste")
    if abs(wn[True] - wn[False]) > 2: fouten.append(f"{naam}: waar/niet waar niet in evenwicht")
    return fouten


fouten = kijk(bron.DEEL_1, "deel 1") + kijk(bron.DEEL_2, "deel 2")
for u in (bron.UITLEG_1, bron.UITLEG_2):
    if len(u) > 200: fouten.append(f"korte uitleg te lang ({len(u)} > 200)")
if fouten:
    print("\n".join(fouten)); sys.exit(1)
schoon = lambda vr: [{k: x for k, x in v.items() if k != "reken"} for v in vr]
DOEL.write_text(json.dumps({"hoofdstukken": [
    {"titel": f"{bron.TITEL} — deel 1", "niveau": "ready", "korte_uitleg": bron.UITLEG_1, "vragen": schoon(bron.DEEL_1)},
    {"titel": f"{bron.TITEL} — deel 2", "niveau": "ready", "korte_uitleg": bron.UITLEG_2, "vragen": schoon(bron.DEEL_2)},
]}, ensure_ascii=False, indent=1), encoding="utf-8")
print("geschreven", DOEL)
