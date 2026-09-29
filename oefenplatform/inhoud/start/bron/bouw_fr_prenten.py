#!/usr/bin/env python3
"""
Bouwt inhoud/start/frans-prenten.json: de hoofdstukken waarin je beschrijft
wat je op een prent ziet.

Deze twee staan bewust in een eigen bestand, los van frans.json. Zo kan Kim ze
importeren zonder de zeven andere hoofdstukken van Frans opnieuw in te lezen.

Dezelfde controles als bouw_frans.py (geen dubbels binnen het niveau, elke
vraag met uitleg, geen raadbare patronen), plus één die alleen hier zin heeft:
**elk hoofdstuk moet zijn prent hebben staan**. Een beschrijfhoofdstuk zonder
prent is een reeks vragen over niets.

Gebruik:

    python3 inhoud/start/bron/bouw_fr_prenten.py
"""

import json
import pathlib
import re
import sys
import unicodedata

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
DOEL = HIER.parent / "frans-prenten.json"
INHOUD = HIER.parent.parent
PRENTEN = INHOUD.parent / "public" / "prenten"
VAK = "frans"
NIVEAU = "start"
PER_HOOFDSTUK = 20

SPELING = 6
GRENS_LANGSTE = 0.4
WAAR_ONDER, WAAR_BOVEN = 0.35, 0.65


def sleutel(vraag):
    return re.sub(r"[^a-z0-9]+", " ", str(vraag).lower()).strip()


def slug(tekst):
    """Zelfde vereenvoudiging als lib/slug.ts."""
    zonder = unicodedata.normalize("NFD", tekst)
    zonder = "".join(t for t in zonder if unicodedata.category(t) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", zonder).strip("-")


def elders():
    """Elke vraag die al ergens anders in dit niveau staat, met waar ze staat."""
    gevonden = {}
    for pad in sorted(INHOUD.glob("*/*.json")):
        if pad.resolve() == DOEL.resolve():
            continue
        try:
            data = json.loads(pad.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for h in data.get("hoofdstukken", []):
            if (h.get("niveau") or pad.parent.name) != NIVEAU:
                continue
            for v in h.get("vragen", []):
                gevonden.setdefault(
                    sleutel(v.get("vraag", "")), f"{pad.name} / {h.get('titel')}"
                )
    return gevonden


def gokpatronen(titel, vragen):
    """Kan je scoren zonder naar de prent te kijken?"""
    fouten = []
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        opties = v.get("opties") or [""]
        juist = len(opties[v["antwoord"]])
        anders = [len(o) for i, o in enumerate(opties) if i != v["antwoord"]]
        if anders and juist > max(anders) + SPELING:
            langst += 1
    if mk and langst > GRENS_LANGSTE * len(mk):
        fouten.append(
            f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
            f"antwoord de langste optie. Maak de andere opties langer."
        )
    wn = [v["antwoord"] for v in vragen if v["type"] == "waarofniet"]
    if wn and not (WAAR_ONDER <= sum(1 for a in wn if a) / len(wn) <= WAAR_BOVEN):
        fouten.append(
            f"{titel}: {sum(1 for a in wn if a)} van de {len(wn)} "
            f"waar/niet-waar-vragen is waar."
        )
    return fouten


def main():
    import fr_prenten

    fouten = []
    gezien = {}
    ergens_anders = elders()
    hoofdstukken = []

    for titel, vragen in fr_prenten.HOOFDSTUKKEN:
        # De prent zelf. Zonder prent valt er niets te beschrijven.
        prent = PRENTEN / VAK / f"{slug(titel)}.webp"
        if not prent.exists():
            fouten.append(
                f"{titel}: de prent ontbreekt. Verwacht {prent.relative_to(INHOUD.parent)} "
                f"— zet ze klaar met inhoud/prenten/bron/maak_prenten.py."
            )

        if len(vragen) != PER_HOOFDSTUK:
            fouten.append(
                f"{titel}: {len(vragen)} vragen in plaats van {PER_HOOFDSTUK}"
            )

        for v in vragen:
            kop = f'{titel} / "{v["vraag"][:55]}"'
            s = sleutel(v["vraag"])
            if s in gezien:
                fouten.append(f"{kop}: staat ook in {gezien[s]}")
            elif s in ergens_anders:
                fouten.append(f"{kop}: staat al in {ergens_anders[s]}")
            gezien[s] = titel

            if not v.get("uitleg"):
                fouten.append(f"{kop}: geen uitleg")

            if v["type"] == "meerkeuze":
                opties = v.get("opties") or []
                if len(opties) < 3:
                    fouten.append(f"{kop}: minder dan drie opties")
                if len(set(opties)) != len(opties):
                    fouten.append(f"{kop}: twee keer dezelfde optie")
                if not isinstance(v["antwoord"], int) or not 0 <= v["antwoord"] < len(
                    opties
                ):
                    fouten.append(f"{kop}: antwoord wijst niet naar een optie")
            elif v["type"] == "waarofniet":
                if not isinstance(v["antwoord"], bool):
                    fouten.append(f"{kop}: waar of niet waar vraagt true of false")
                if v.get("opties"):
                    fouten.append(f"{kop}: waar of niet waar heeft geen opties")
            elif v["type"] == "invultekst":
                antwoorden = (
                    v["antwoord"]
                    if isinstance(v["antwoord"], list)
                    else [v["antwoord"]]
                )
                if not antwoorden or not all(
                    isinstance(a, str) and a.strip() for a in antwoorden
                ):
                    fouten.append(f"{kop}: invulantwoord ontbreekt")
                if v.get("opties"):
                    fouten.append(f"{kop}: een invulvraag heeft geen opties")
            else:
                fouten.append(f"{kop}: onbekend type {v['type']}")

        fouten += gokpatronen(titel, vragen)
        hoofdstukken.append(
            {"titel": titel, "niveau": NIVEAU, "gratis": False, "vragen": vragen}
        )

    if fouten:
        for f in fouten:
            print("FOUT:", f)
        return 1

    DOEL.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totaal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(
        f"geschreven: {DOEL.name} — {len(hoofdstukken)} hoofdstukken, {totaal} vragen"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
