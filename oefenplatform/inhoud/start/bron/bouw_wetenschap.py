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


def gokpatronen(titel, vragen):
    """Kan je scoren zonder de leerstof te kennen?

    Twee patronen sluipen er bij het schrijven vanzelf in, en allebei maken ze
    een hoofdstuk raadbaar:

      * het juiste antwoord is de langste optie, want net dat antwoord vraagt
        uitleg en de foute opties krijgen er drie woorden. Wie altijd de
        langste aanklikt, mag niet meer dan vier op de tien juist hebben;
      * waar en niet-waar houden elkaar niet in evenwicht, en dan loont het om
        overal hetzelfde te antwoorden.

    Een verschil van een paar letters ziet een kind niet, dus we tellen een
    vraag pas als het juiste antwoord er minstens zes langer is dan elke
    foute optie.
    """
    fouten = []
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        lengtes = [len(o) for o in (v.get("opties") or [""])]
        anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
        if anders and min(lengtes[i] for i in antw) > max(anders) + 5:
            langst += 1
    if mk and langst > 0.4 * len(mk):
        fouten.append(
            f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
            f"antwoord duidelijk de langste optie. Maak de andere opties langer."
        )

    wn = [v["antwoord"] for v in vragen if v["type"] == "waarofniet"]
    waar = sum(1 for a in wn if a)
    if wn and not (0.35 <= waar / len(wn) <= 0.65):
        fouten.append(
            f"{titel}: {waar} van de {len(wn)} waar/niet-waar-vragen is waar. "
            f"Dat is te scheef om niet te kunnen gokken."
        )
    return fouten


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
                # Een invulvraag mag meer dan één juist antwoord hebben: dan
                # staat er een lijstje tekst (zie lib/antwoord.ts).
                antwoorden = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
                if not antwoorden or not all(isinstance(a, str) and a.strip() for a in antwoorden):
                    fouten.append(f'"{v["vraag"]}": invultekst vraagt een antwoord in tekst')
            else:
                fouten.append(f'"{v["vraag"]}": onbekend type {v["type"]}')

        fouten.extend(gokpatronen(titel, vragen))

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
