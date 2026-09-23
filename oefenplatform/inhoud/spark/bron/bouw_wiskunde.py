# -*- coding: utf-8 -*-
"""Zet de themabestanden uit deze map samen in ../wiskunde.json.

    python3 bron/bouw_wiskunde.py

Elk thema is één bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen. Dit script maakt daar twee hoofdstukken van, "<thema> — deel 1" en
"<thema> — deel 2", en zet ze in het importbestand.

Waarom niet rechtstreeks in de JSON schrijven: in een Python-bestand kan er
uitleg bij staan, kan je de rekenvoorbeelden narekenen en leest een diff
achteraf leesbaar. De JSON is enkel wat Kim in het invoervak plakt.

Draai het gerust opnieuw: een thema dat er al in staat, wordt vervangen op
dezelfde plaats. De hoofdstukken die hier niet vandaan komen, blijven staan.
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "wiskunde.json"

# De naam van het thema is ook de titel van het hoofdstuk, en `hernoemVan` is
# hoe het hoofdstuk nu in Kim's databank staat: als één geheel, zonder deel.
THEMAS = [
    ("probleemoplossend", "Probleemoplossend denken"),
    ("redeneringen", "Wiskundige redeneringen en uitspraken"),
    ("meetkunde", "Meetkunde"),
    ("metend_rekenen", "Metend rekenen"),
    ("relaties", "Relaties en verandering"),
    ("data", "Data en onzekerheid"),
    ("verzamelingen", "Verzamelingen"),
]


def hoofdstukken_van(modulenaam: str, thema: str) -> list:
    mod = importlib.import_module(modulenaam)
    uit = []
    for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
        if len(vragen) != 20:
            raise SystemExit(f"{thema} deel {nummer} heeft {len(vragen)} vragen, verwacht 20")
        hoofdstuk = {"titel": f"{thema} — deel {nummer}", "niveau": "spark", "gratis": False}
        if nummer == 1:
            # Deel 1 neemt het bestaande hoofdstuk over in plaats van er een
            # tweede naast te zetten. Zie WISKUNDE.md.
            hoofdstuk["hernoemVan"] = thema
        hoofdstuk["vragen"] = vragen
        uit.append(hoofdstuk)
    return uit


def main():
    data = json.loads(DOEL.read_text(encoding="utf-8"))
    bestaand = data["hoofdstukken"]

    for modulenaam, thema in THEMAS:
        if not (HIER / f"{modulenaam}.py").exists():
            continue
        nieuw = hoofdstukken_van(modulenaam, thema)
        titels = {h["titel"] for h in nieuw}
        # Op de plaats van het oude thema, of anders achteraan.
        plaats = next((i for i, h in enumerate(bestaand) if h["titel"] in titels), len(bestaand))
        bestaand = [h for h in bestaand if h["titel"] not in titels]
        bestaand[plaats:plaats] = nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    data["hoofdstukken"] = bestaand
    DOEL.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    totaal = sum(len(h["vragen"]) for h in bestaand)
    print(f"\n{len(bestaand)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
