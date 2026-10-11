# -*- coding: utf-8 -*-
"""Zoekt notatie die buiten een formule is blijven staan, in de bundels van
een module. × en − mogen buiten een formule staan (zo horen ze in een tekening
of in een zin), \\cdot en {,} niet: die zijn enkel voor KaTeX.

    python3 -I inhoud/omzetten/lek_bundel.py maak_wiskunde_spark …
"""
import importlib, pathlib, re, sys

HIER = pathlib.Path(__file__).resolve().parent.parent / "leerbundels" / "bron"
sys.path.insert(0, str(HIER))
FORMULE = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]|<[^>]*>", re.S)
TEKENS = re.compile(r"[≤≥∈∩∪∅²³π]")


def loop(x, waar):
    if isinstance(x, str):
        kaal = FORMULE.sub("", x)
        if re.search(r"\\[a-zA-Z]", kaal) or TEKENS.search(kaal) or "{,}" in kaal:
            print(f"  LEK {waar}: ...{kaal[:160]}")
    elif isinstance(x, dict):
        for v in x.values():
            loop(v, waar)
    elif isinstance(x, (list, tuple)):
        for v in x:
            loop(v, waar)


for modulenaam in sys.argv[1:]:
    mod = importlib.import_module(modulenaam)
    for sleutel in ("BUNDELS", "OEFENBUNDELS"):
        for naam, b in getattr(mod, sleutel, {}).items():
            loop(b, naam)
    print(f"{modulenaam} nagekeken")
