# -*- coding: utf-8 -*-
"""Maakt de bundels van één bronbestand opnieuw en zet elke pdf bij zijn vak.

    python3 -I inhoud/omzetten/bouw_module.py maak_wiskunde_spark [maak_oefeningen_wiskunde_spark]

Zelfde werk als maak_alles.py, maar dan voor één module, zodat je niet elke
bundel van het platform opnieuw moet renderen.
"""
import importlib, pathlib, subprocess, sys
HIER = pathlib.Path(__file__).resolve().parent.parent / "leerbundels" / "bron"
sys.path.insert(0, str(HIER))
from maak_alles import slug

for modulenaam in sys.argv[1:]:
    mod = importlib.import_module(modulenaam)
    for soort, sleutel, maker, map_ in (
        ("leerbundel", "BUNDELS", "bundel", HIER.parent),
        ("oefenbundel", "OEFENBUNDELS", "oefenbundel", HIER.parent.parent / "oefenbundels"),
    ):
        for naam, b in getattr(mod, sleutel, {}).items():
            importlib.import_module(maker).schrijf(b, naam)
            subprocess.run(["node", str(HIER / "pdf.js"), naam], cwd=HIER, check=True)
            doel = map_ / slug(b["vak"])
            doel.mkdir(parents=True, exist_ok=True)
            (doel / f"{naam}.pdf").write_bytes((HIER / f"{naam}.pdf").read_bytes())
            print("  ", doel.name + "/" + naam + ".pdf")
