# -*- coding: utf-8 -*-
"""Zet de vragen van 🔭 de uitdagingshoek om in importbestanden.

    python3 inhoud/hoekje/bron/bouw_hoekje.py             # alles
    python3 inhoud/hoekje/bron/bouw_hoekje.py ruimte_1

De uitdagingshoek staat náást de leerstof, niet erin: hij hoort bij geen enkel
leerjaar en bij geen enkele vakfiche. Daarom draagt elk hoofdstuk het niveau
"hoekje" en staat het gratis open. Vier vakken, elk twee hoofdstukken van
twintig vragen.

Elke bron heet <vak>_<deel>.py en zet VAK, BESTAND, TITEL, VOLGORDE en VRAGEN
klaar. Het script weigert te schrijven zolang er iets niet klopt: een vraag
zonder uitleg, een antwoord dat buiten de opties valt, twee keer dezelfde
vraag, of een patroon waarmee je zou kunnen gokken (zie
inhoud/controleer_patronen.py voor die twee patronen en hun grenzen).
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
UIT = HIER.parent
NIVEAU = "hoekje"

SPELING = 5
GRENS_LANGSTE = 0.4
WAAR_ONDER, WAAR_BOVEN = 0.35, 0.65


def nakijken(naam, vragen):
    meldingen = []
    gezien = set()
    for v in vragen:
        kop = v["vraag"][:60]
        if v["vraag"] in gezien:
            meldingen.append(f"{kop}: staat er twee keer in")
        gezien.add(v["vraag"])
        if not v.get("uitleg"):
            meldingen.append(f"{kop}: geen uitleg")
        if v["type"] == "meerkeuze":
            opties = v.get("opties") or []
            antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
            if len(opties) < 3:
                meldingen.append(f"{kop}: minder dan drie opties")
            if any(not isinstance(i, int) or i < 0 or i >= len(opties) for i in antw):
                meldingen.append(f"{kop}: antwoord wijst naar een optie die er niet is")
            if len(set(opties)) != len(opties):
                meldingen.append(f"{kop}: twee keer dezelfde optie")
        elif v["type"] == "invultekst":
            if not isinstance(v["antwoord"], str) or not v["antwoord"].strip():
                meldingen.append(f"{kop}: invulantwoord ontbreekt")
            if v.get("opties"):
                meldingen.append(f"{kop}: een invulvraag heeft geen opties")
        elif v["type"] == "waarofniet":
            if not isinstance(v["antwoord"], bool):
                meldingen.append(f"{kop}: waar of niet waar vraagt true of false")
        else:
            meldingen.append(f"{kop}: onbekend type {v['type']}")
    return meldingen


def gokpatronen(vragen):
    meldingen = []
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        lengtes = [len(o) for o in (v.get("opties") or [""])]
        anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
        if anders and min(lengtes[i] for i in antw) > max(anders) + SPELING:
            langst += 1
    if mk and langst > GRENS_LANGSTE * len(mk):
        meldingen.append(
            f"bij {langst} van de {len(mk)} meerkeuzevragen is het juiste antwoord "
            f"de langste optie. Maak de andere opties langer."
        )
    wn = [v["antwoord"] for v in vragen if v["type"] == "waarofniet"]
    if wn and not (WAAR_ONDER <= sum(1 for a in wn if a) / len(wn) <= WAAR_BOVEN):
        meldingen.append(
            f"{sum(1 for a in wn if a)} van de {len(wn)} waar/niet-waar-vragen is waar."
        )
    return meldingen


def lees(naam):
    module = importlib.import_module(f"bron.{naam}")
    vragen = [dict(v) for v in module.VRAGEN]
    meldingen = nakijken(naam, vragen) + gokpatronen(vragen)
    if len(vragen) != 20:
        meldingen.append(f"{len(vragen)} vragen in plaats van 20")
    if meldingen:
        raise SystemExit(f"{naam} klopt nog niet:\n  - " + "\n  - ".join(meldingen))
    return module, vragen


def main():
    sys.path.insert(0, str(UIT))
    namen = sys.argv[1:] or sorted(
        p.stem for p in HIER.glob("*.py") if p.stem not in ("bouw_hoekje", "__init__")
    )

    per_bestand = {}
    for naam in namen:
        module, vragen = lees(naam)
        per_bestand.setdefault(module.BESTAND, []).append((module, vragen))

    # Alle titels samen moeten uniek blijven: twee hoofdstukken met dezelfde
    # naam worden bij het importeren één hoofdstuk.
    titels = [m.TITEL for delen in per_bestand.values() for m, _ in delen]
    if len(set(titels)) != len(titels):
        raise SystemExit("twee hoofdstukken dragen dezelfde titel")

    for bestand, delen in sorted(per_bestand.items()):
        delen.sort(key=lambda d: d[0].VOLGORDE)
        inhoud = {
            "hoofdstukken": [
                {
                    "titel": m.TITEL,
                    "niveau": NIVEAU,
                    # Het hoekje hoort niet bij het betalende aanbod.
                    "gratis": True,
                    "vragen": vragen,
                }
                for m, vragen in delen
            ]
        }
        doel = UIT / bestand
        doel.write_text(
            json.dumps(inhoud, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        soorten = {}
        for _, vragen in delen:
            for v in vragen:
                soorten[v["type"]] = soorten.get(v["type"], 0) + 1
        print(
            f"{doel.name:30} {delen[0][0].VAK:24} "
            f"{len(delen)} hoofdstukken, "
            + ", ".join(f"{a} {t}" for t, a in sorted(soorten.items()))
        )


if __name__ == "__main__":
    main()
