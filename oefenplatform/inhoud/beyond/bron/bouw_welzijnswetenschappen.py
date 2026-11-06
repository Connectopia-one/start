# -*- coding: utf-8 -*-
"""Zet de thema's `ww_*.py` samen in ../natuurwetenschappen-welzijnswetenschappen.json.

    python3 bron/bouw_welzijnswetenschappen.py

🌍 Beyond, derde graad, richting welzijnswetenschappen (Kim, 6 november 2026).

De vakfiche natuurwetenschappen voor welzijnswetenschappen (2027) bevat alles
van de gewone vakfiche natuurwetenschappen 3DO, die al in natuurwetenschappen.json
staat, plus één groot extra blok biologie: "Stofwisselingsfysiologie en
secretie" (enzymen, spijsvertering, uitscheiding, bloed, hart en bloedsomloop,
bloeddruk en lymfe, ademhaling). Alleen dat extra blok staat hier.

Het is een apart vak, "Natuurwetenschappen welzijnswetenschappen", in Beyond
doorstroom (Kim, 6 november 2026: eerst stonden de hoofdstukken bij het gewone
vak natuurwetenschappen met "Welzijnswetenschappen:" ervoor, maar dat was niet
overzichtelijk). Een leerling van die richting maakt dit vak én het gewone vak
natuurwetenschappen; de vaknoot zegt dat. Importeren via Beheer → Vakken →
Natuurwetenschappen welzijnswetenschappen.

De controles zijn dezelfde als in bouw_natuurwetenschappen.py.
"""

import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))

import bouw_natuurwetenschappen as nw  # noqa: E402

DOEL = HIER.parent / "natuurwetenschappen-welzijnswetenschappen.json"
VOORVOEGSEL = ""

THEMAS = [
    ("ww_enzymen", "Enzymen"),
    ("ww_spijsvertering", "Het spijsverteringsstelsel"),
    ("ww_uitscheiding", "Het uitscheidingsstelsel"),
    ("ww_bloed", "Het bloed"),
    ("ww_hart", "Het hart en de bloedsomloop"),
    ("ww_bloeddruk", "De bloeddruk en het lymfestelsel"),
    ("ww_ademhaling", "Het ademhalingsstelsel"),
]


def main():
    hoofdstukken = []
    for modulenaam, thema in THEMAS:
        if not (HIER / f"{modulenaam}.py").exists():
            print(f"  {thema}: nog niet geschreven, overgeslagen")
            continue
        nieuw = nw.hoofdstukken_van(modulenaam, VOORVOEGSEL + thema)
        hoofdstukken += nieuw
        print(f"  {thema}: {sum(len(h['vragen']) for h in nieuw)} vragen")

    # Geen vraag twee keer, ook niet tegenover de gewone natuurwetenschappen.
    gewoon = json.loads((HIER.parent / "natuurwetenschappen.json").read_text(encoding="utf-8"))
    gezien = {}
    for h in gewoon["hoofdstukken"]:
        for v in h["vragen"]:
            gezien[" ".join(v["vraag"].lower().split())] = h["titel"]
    meerkeuze = meerdere = 0
    for h in hoofdstukken:
        for v in h["vragen"]:
            tekst = " ".join(v["vraag"].lower().split())
            if tekst in gezien:
                raise SystemExit(
                    f"Deze vraag staat twee keer, in {gezien[tekst]} en in {h['titel']}:\n  {v['vraag']}"
                )
            gezien[tekst] = h["titel"]
            if v["type"] == "meerkeuze":
                meerkeuze += 1
                if isinstance(v["antwoord"], list):
                    meerdere += 1

    for h in hoofdstukken:
        for melding in nw.gokpatronen(h["titel"], h["vragen"]):
            raise SystemExit(melding)
    for melding in nw.evenwicht_waar(hoofdstukken):
        raise SystemExit(melding)

    if meerkeuze:
        deel = meerdere / meerkeuze
        print(f"\n{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden.")
        if not 0.15 <= deel <= 0.30:
            raise SystemExit("mikken op 20 à 30 %")

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {DOEL.name}")


if __name__ == "__main__":
    main()
