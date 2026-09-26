# -*- coding: utf-8 -*-
"""Zet de uitdagingshoofdstukken om in importbestanden.

    python3 inhoud/uitdaging/bron/bouw_uitdaging.py            # alles
    python3 inhoud/uitdaging/bron/bouw_uitdaging.py start_wiskunde

Eén uitdagingshoofdstuk per vak: twintig moeilijkere vragen die de hoofdstukken
van dat vak door elkaar halen. Elke bron heet <niveau>_<vak>.py en zet NIVEAU,
VAK, BESTAND en VRAGEN klaar.

Het script weigert te schrijven zolang er iets niet klopt: een vraag zonder
uitleg, een antwoord dat buiten de opties valt, twee keer dezelfde vraag, een
rekenveld dat niet uitkomt, of een patroon waarmee je zou kunnen gokken
(zie inhoud/controleer_patronen.py voor die twee patronen en hun grenzen).
"""
import importlib
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
UIT = HIER.parent
TITEL = "Uitdaging — alles door elkaar"

SPELING = 5
GRENS_LANGSTE = 0.4
WAAR_ONDER, WAAR_BOVEN = 0.35, 0.65


def getal(waarde):
    """Schrijft een uitgerekende waarde zoals een kind ze zou intypen."""
    if isinstance(waarde, float):
        if abs(waarde - round(waarde)) < 1e-9:
            waarde = round(waarde)
        else:
            waarde = f"{waarde:.10f}".rstrip("0").rstrip(".")
    return str(waarde).replace(".", ",")


def kaal(tekst):
    return str(tekst).replace(" ", "").replace(" ", "").replace(".", ",").strip()


def narekenen(vraag):
    """Rekent het veld reken na tegen het antwoord dat in de vraag staat."""
    if "reken" not in vraag:
        return []
    uitkomst = getal(eval(vraag["reken"]))  # noqa: S307 - eigen bronbestand
    if vraag["type"] == "invultekst":
        verwacht = vraag["antwoord"]
    else:
        verwacht = vraag["opties"][vraag["antwoord"]]
    delen = [kaal(d) for d in str(verwacht).split(" of ")]
    # Bij een optie als "20 minuten" telt het getal vooraan, niet de eenheid erna.
    delen += [d.split(None, 1)[0] for d in str(verwacht).split(" of ") if " " in d.strip()]
    if kaal(uitkomst) not in [kaal(d) for d in delen]:
        return [f"{vraag['vraag'][:60]}: reken geeft {uitkomst}, er staat {verwacht}"]
    return []


def nakijken(module, vragen):
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
            if isinstance(v["antwoord"], list) and "wiskunde" in module:
                meldingen.append(f"{kop}: bij wiskunde geen meerkeuze met meerdere antwoorden")
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
        meldingen += narekenen(v)
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


def bouw(naam):
    module = importlib.import_module(f"bron.{naam}")
    vragen = [dict(v) for v in module.VRAGEN]
    meldingen = nakijken(naam, vragen) + gokpatronen(vragen)
    if len(vragen) != 20:
        meldingen.append(f"{len(vragen)} vragen in plaats van 20")
    if meldingen:
        raise SystemExit(f"{naam} klopt nog niet:\n  - " + "\n  - ".join(meldingen))
    for v in vragen:
        v.pop("reken", None)
    inhoud = {
        "hoofdstukken": [
            {"titel": TITEL, "niveau": module.NIVEAU, "gratis": False, "vragen": vragen}
        ]
    }
    doel = UIT / module.BESTAND
    doel.write_text(
        json.dumps(inhoud, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    soorten = {}
    for v in vragen:
        soorten[v["type"]] = soorten.get(v["type"], 0) + 1
    print(f"{doel.name:34} {module.VAK:24} " +
          ", ".join(f"{a} {t}" for t, a in sorted(soorten.items())))


def main():
    sys.path.insert(0, str(UIT))
    namen = sys.argv[1:] or sorted(
        p.stem for p in HIER.glob("*.py") if p.stem not in ("bouw_uitdaging", "__init__")
    )
    for naam in namen:
        bouw(naam)


if __name__ == "__main__":
    main()
