# -*- coding: utf-8 -*-
"""Zoekt notatie die buiten een formule is blijven staan, in een vragenbestand.

    python3 -I inhoud/omzetten/lek_json.py <bestand.json> …
"""
import json, re, sys

FORMULE = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]", re.S)
TEKENS = re.compile(r"[≤≥∈∩∪∅²³π]")


def loop(x, waar):
    if isinstance(x, str):
        kaal = FORMULE.sub("", x)
        if re.search(r"\\[a-zA-Z]", kaal) or TEKENS.search(kaal) or "{,}" in kaal:
            print(f"  LEK {waar}: {x[:150]}")
    elif isinstance(x, dict):
        for v in x.values():
            loop(v, waar)
    elif isinstance(x, list):
        for v in x:
            loop(v, waar)


for pad in sys.argv[1:]:
    data = json.load(open(pad, encoding="utf-8"))
    for h in data["hoofdstukken"]:
        loop(h, h["titel"])
    print(f"{pad} nagekeken")
