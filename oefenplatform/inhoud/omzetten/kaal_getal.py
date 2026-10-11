# -*- coding: utf-8 -*-
"""Staan er nog getallen in woorden, buiten de notatie? Geeft per bestand de
vragen waarin een cijfer of een breuk buiten \\( \\) staat."""
import json, re, sys
SPAN = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]|\{\{[^}]*\}\}", re.S)
CIJFER = re.compile(r"\d")
for pad in sys.argv[1:]:
    data = json.load(open(pad, encoding="utf-8"))
    raak = []
    for h in data["hoofdstukken"]:
        for v in h["vragen"]:
            for sleutel in ("vraag", "uitleg", "leestekst"):
                tekst = v.get(sleutel) or ""
                kaal = SPAN.sub(" ", tekst)
                if CIJFER.search(kaal):
                    raak.append((h["titel"], sleutel, kaal.strip()[:110]))
            for o in (v.get("opties") or []):
                if CIJFER.search(SPAN.sub(" ", o)):
                    raak.append((h["titel"], "optie", o))
    print(f"{pad}: {len(raak)}")
    for t, s, k in raak[:40]:
        print(f"   {t} [{s}] {k}")
