# -*- coding: utf-8 -*-
"""Maakt alle leerbundels opnieuw en zet elke pdf bij zijn vak.

    python3 maak_alles.py            # alles
    python3 maak_alles.py nederlands # alleen dat vak

Handig na een aanpassing aan stijl.css of aan een tekening in svg.py: die
raken immers elke bundel, niet alleen de bundel die je aan het schrijven was.
"""
import importlib, pathlib, re, subprocess, sys, unicodedata

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))


def slug(naam):
    plat = unicodedata.normalize("NFKD", naam).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plat.lower()).strip("-")


def main(filter_vak=None):
    gemaakt = []
    for pad in sorted(HIER.glob("maak_*.py")):
        if pad.name == "maak_alles.py":
            continue
        mod = importlib.import_module(pad.stem)
        for naam, b in getattr(mod, "BUNDELS", {}).items():
            vak = slug(b["vak"])
            if filter_vak and vak != filter_vak:
                continue
            bundel = importlib.import_module("bundel")
            bundel.schrijf(b, naam)
            subprocess.run(["node", str(HIER / "pdf.js"), naam], cwd=HIER, check=True)
            doel = HIER.parent / vak
            doel.mkdir(exist_ok=True)
            (doel / f"{naam}.pdf").write_bytes((HIER / f"{naam}.pdf").read_bytes())
            gemaakt.append(f"{vak}/{naam}.pdf")
    for g in gemaakt:
        print("  ", g)
    print(len(gemaakt), "bundels")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
