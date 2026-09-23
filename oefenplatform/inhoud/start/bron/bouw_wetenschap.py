# -*- coding: utf-8 -*-
"""Zet de hoofdstukbestanden uit deze map samen in ../wetenschap-en-techniek.json.

    python3 bron/bouw_wetenschap.py

Elk hoofdstuk is één bestand met een lijst VRAGEN. Waarom niet rechtstreeks in
de JSON schrijven: in een Python-bestand kan er uitleg bij staan en leest een
diff achteraf leesbaar. De JSON is enkel wat Kim in het invoervak plakt.

Het script kijkt meteen drie dingen na: of elk hoofdstuk even veel vragen
heeft, of geen enkele vraag twee keer voorkomt, en of elk meerkeuzeantwoord
naar een bestaande optie wijst.
"""
import importlib
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "wetenschap-en-techniek.json"
PER_HOOFDSTUK = 40

# Volgorde zoals ze in het platform komen te staan. De vier eerste bestonden al
# en houden hun titel, zodat de import ze terugvindt in plaats van er nieuwe
# naast te zetten.
HOOFDSTUKKEN = [
    ("biologie_ecologie", "Biologie: leven en ecologie"),
    ("biologie_lichaam", "Biologie: het menselijk lichaam"),
    ("chemie", "Chemie: stoffen en mengsels"),
    ("natuurkunde_energie", "Natuurkunde: energie en krachten"),
    ("natuurkunde_licht", "Natuurkunde: licht, geluid en elektriciteit"),
    ("techniek", "Techniek: ontwerpen en maken"),
    ("aarde_en_ruimte", "De aarde en de ruimte"),
]


def sleutel(vraag: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", vraag.lower()).strip()


def main() -> int:
    fouten = []
    gezien = {}
    hoofdstukken = []

    for modulenaam, titel in HOOFDSTUKKEN:
        vragen = list(importlib.import_module(modulenaam).VRAGEN)

        if len(vragen) != PER_HOOFDSTUK:
            fouten.append(f"{titel}: {len(vragen)} vragen in plaats van {PER_HOOFDSTUK}")

        for v in vragen:
            s = sleutel(v["vraag"])
            if s in gezien:
                fouten.append(f'"{v["vraag"]}" staat in zowel {gezien[s]} als {titel}')
            gezien[s] = titel

            if v["type"] == "meerkeuze":
                opties = v.get("opties") or []
                if not isinstance(v["antwoord"], int) or not 0 <= v["antwoord"] < len(opties):
                    fouten.append(f'"{v["vraag"]}": antwoord wijst niet naar een optie')
            elif v["type"] == "waarofniet":
                if not isinstance(v["antwoord"], bool):
                    fouten.append(f'"{v["vraag"]}": waar-of-niet vraagt een boolean')
            elif v["type"] == "invultekst":
                if not isinstance(v["antwoord"], str) or not v["antwoord"].strip():
                    fouten.append(f'"{v["vraag"]}": invultekst vraagt een antwoord in tekst')
            else:
                fouten.append(f'"{v["vraag"]}": onbekend type {v["type"]}')

        hoofdstukken.append({"titel": titel, "niveau": "start", "vragen": vragen})

    if fouten:
        for f in fouten:
            print("FOUT:", f)
        return 1

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"geschreven: {DOEL.name} — {len(hoofdstukken)} hoofdstukken, {totaal} vragen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
