# -*- coding: utf-8 -*-
"""Zet de notatie in hoofdstukken die enkel in een json staan (geen bronbestand).

    python3 -I json_omzet.py <bestand.json> "<stuk van de titel>" ...
"""
import json, sys
EIGEN = sys.argv[1:]
sys.argv = [sys.argv[0]]          # naar_notatie.py leest zelf argv
exec(open(__file__.replace("json_omzet.py", "naar_notatie.py")).read().split("for pad in")[0])

pad, stukken = EIGEN[0], EIGEN[1:]
data = json.load(open(pad, encoding="utf-8"))
geraakt = 0
for h in data["hoofdstukken"]:
    if not any(s in h["titel"] for s in stukken):
        continue
    for v in h["vragen"]:
        for sleutel in ("vraag", "uitleg"):
            if isinstance(v.get(sleutel), str):
                v[sleutel] = zet_om(v[sleutel])
        if isinstance(v.get("opties"), list):
            v["opties"] = [zet_om(o) if isinstance(o, str) else o for o in v["opties"]]
        geraakt += 1
    print(f"  {h['titel']}: {len(h['vragen'])} vragen")
open(pad, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"{geraakt} vragen omgezet in {pad}")
