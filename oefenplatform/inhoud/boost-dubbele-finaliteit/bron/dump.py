# -*- coding: utf-8 -*-
"""Dump de vragen van een themabestand compact: vraag + juiste antwoord(en)."""
import importlib, pathlib, sys
BRON = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(
    "/home/claude/start/oefenplatform/inhoud/boost-doorstroom/bron")
sys.path.insert(0, str(BRON))
m = importlib.import_module(sys.argv[1])
for naam in ("DEEL1", "DEEL2"):
    print("######", naam)
    for i, v in enumerate(getattr(m, naam), 1):
        t = v["type"]
        if t == "meerkeuze":
            a = v["antwoord"]
            a = a if isinstance(a, list) else [a]
            juist = " | ".join(v["opties"][k] for k in a)
        elif t == "waarofniet":
            juist = "WAAR" if v["antwoord"] else "NIET WAAR"
        else:
            a = v["antwoord"]
            juist = " / ".join(a) if isinstance(a, list) else str(a)
        print(f"{i:2d}. {v['vraag']}")
        print(f"    -> {juist}")
        if v.get("uitleg"):
            print(f"    ({v['uitleg']})")
