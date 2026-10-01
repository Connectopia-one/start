# -*- coding: utf-8 -*-
"""Zet de leerbundels van 🌱 Start en ✨ Spark om naar json, voor de klikbare bundel.

De pdf blijft bestaan en verandert niet. Dit script leest dezelfde
BUNDELS-dicts en schrijft ze weg als gegevens, zodat het oefenplatform de
bundel op het scherm kan tonen als een reeks onderdelen waar een kind op klikt.

    python3 maak_interactief.py

Waarom: een kind uit de testgroep meldde dat een leerbundel lezen saai is en
dat ze hem daarom overslaat, met als gevolg dat de oefeningen niet lukken.
Eén lange pdf vraagt dat je alles in één keer doorworstelt; klikbare onderdelen
laten toe om er één tegelijk te nemen.

🌱 Start en ✨ Spark. 🧱 Basis houdt voorlopig zijn pdf.

Kim op 29 september 2026: "of de interactieve leerbundels ook bij spark kunnen
maar zonder de puzzels? dus gewoon het leerpad." Het spelletje op de eindhalte
staat daarom enkel bij Start; dat wordt in de pagina zelf beslist.
"""
import importlib
import json
import pathlib
import re
import sys
import unicodedata

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent.parent / "leerbundels-interactief"


def slug(naam):
    """Zelfde regel als lib/slug.ts, zodat een hoofdstuktitel het bestand vindt."""
    plat = unicodedata.normalize("NFKD", naam).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plat.lower()).strip("-")


def niveau_van(b):
    """De korte naam van het niveau, zoals in lib/niveaus.ts.

    Een bundel zonder eigen niveau is Start; bundel.py zet dat als standaard.
    De andere schrijven het voluit ("✨ Spark — 1ste en 2de middelbaar").
    """
    voluit = b.get("niveau")
    if not voluit:
        return "start"
    if "Spark" in voluit:
        return "spark"
    if "Basis" in voluit:
        return "basis"
    # Boost splitst in twee categorieën; kijk dus naar de finaliteit en niet
    # enkel naar het woord "Boost".
    if "Boost" in voluit and "doorstroom" in voluit:
        return "boost-doorstroom"
    if "Boost" in voluit and "dubbele finaliteit" in voluit:
        return "boost-dubbele-finaliteit"
    if "Beyond" in voluit:
        return "beyond"
    raise ValueError("onbekend niveau: " + voluit)


NIVEAUS = ("start", "spark", "boost-doorstroom", "boost-dubbele-finaliteit", "beyond")


def blok_naar_data(b):
    soort = b[0]
    if soort == "p":
        return {"soort": "tekst", "html": b[1]}
    if soort == "weetje":
        return {"soort": "weetje", "html": b[1]}
    if soort == "kader":
        return {"soort": "kader", "html": b[1]}
    if soort == "fig":
        return {
            "soort": "figuur",
            "html": b[1],
            "onderschrift": b[2] if len(b) > 2 and b[2] else "",
        }
    raise ValueError("onbekend blok: " + soort)


def bundel_naar_data(b):
    return {
        "vak": b["vak"],
        "titel": b["titel"],
        "onder": b["onder"],
        "secties": [
            {"kop": s["kop"], "blokken": [blok_naar_data(x) for x in s["blokken"]]}
            for s in b["secties"]
        ],
        "onthoud": list(b.get("onthoud", [])),
    }


def main():
    DOEL.mkdir(parents=True, exist_ok=True)
    for oud in DOEL.glob("*.json"):
        oud.unlink()

    register = {}
    for pad in sorted(HIER.glob("maak_*.py")):
        if pad.name in ("maak_alles.py", "maak_interactief.py", "maak_zips.py"):
            continue
        mod = importlib.import_module(pad.stem)
        for naam, b in getattr(mod, "BUNDELS", {}).items():
            niveau = niveau_van(b)
            if niveau not in NIVEAUS:
                continue
            data = bundel_naar_data(b)
            bestand = f"{slug(b['vak'])}--{naam}.json"
            (DOEL / bestand).write_text(
                json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
            )
            # Meestal heet het hoofdstuk net zo als de bundel. Waar dat niet zo
            # is, staat de naam van het hoofdstuk in de bundel zelf, bij
            # "hoofdstukken".
            titels = [b["titel"], *b.get("hoofdstukken", [])]
            for titel in titels:
                sleutel = f"{niveau}/{slug(b['vak'])}/{slug(titel)}"
                if sleutel in register:
                    raise SystemExit(f"twee bundels op dezelfde sleutel: {sleutel}")
                register[sleutel] = bestand

    regels = [
        "// Gemaakt door inhoud/leerbundels/bron/maak_interactief.py — niet met de hand aanpassen.",
        "// De sleutel is <niveau>/<vak-slug>/<hoofdstuk-slug>; zie lib/leerbundel.ts.",
        "",
        "export const KLIKBARE_BUNDELS: Record<string, () => Promise<{ default: unknown }>> = {",
    ]
    for sleutel in sorted(register):
        regels.append(f'  "{sleutel}": () => import("./{register[sleutel]}"),')
    regels.append("};")
    regels.append("")
    (DOEL / "index.ts").write_text("\n".join(regels), encoding="utf-8")

    totaal = sum(p.stat().st_size for p in DOEL.glob("*.json"))
    print(f"{len(register)} bundels, samen {totaal / 1024:.0f} kB")
    for sleutel in sorted(register):
        print("  ", sleutel)


if __name__ == "__main__":
    main()
