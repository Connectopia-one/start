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
sys.path.insert(0, str(UIT.parent))

from notatie import sluitend, zonder_notatie  # noqa: E402  (pad moet eerst klaarstaan)
TITEL = "Uitdaging — alles door elkaar"

# Vanaf ✨ Spark mag een uitdaging ook in de vormen van het examen van de
# Examencommissie staan (Kim, 11 november 2026): tabel, keuzelijst, klikken op
# een prent, casus ... Die vragen kijkt hetzelfde nakijkwerk na als bij de
# pittige hoofdstukken (pittig/bron/bouw_pittig.py). Zo'n bron zet AANTAL
# (meestal 30) en mag casusgroepen {"casus": ..., "vragen": [...]} bevatten.
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "bouw_pittig", UIT.parent / "pittig" / "bron" / "bouw_pittig.py"
)
_pittig = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pittig)
EXAMENVORMEN = _pittig.EXAMENVORMEN

# Kim 11/11/2026: hoogbegaafde kinderen zien meteen als het juiste antwoord
# vaak het langste is. Daarom telt elke keer dat het juiste antwoord het
# langste is (geen speling meer) en mag dat hoogstens 30 % van de keren.
SPELING = 0
GRENS_LANGSTE = 0.3
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
    # de notatie eraf, anders is \(60\,000\) niet hetzelfde getal als 60000
    tekst = zonder_notatie(str(tekst)).replace("\\,", "").replace("\\%", "%")
    return tekst.replace(" ", "").replace("\u00a0", "").replace(".", ",").strip()


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
    for v in _pittig.plat(vragen):
        kop = v["vraag"][:60]
        if v["vraag"] in gezien:
            meldingen.append(f"{kop}: staat er twee keer in")
        gezien.add(v["vraag"])
        if v["type"] in EXAMENVORMEN:
            meldingen += _pittig.examenvorm(kop, v)
            continue
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
            a = v["antwoord"]
            if not (isinstance(a, str) and a.strip()) and not (
                isinstance(a, list) and a and all(isinstance(x, str) and x.strip() for x in a)
            ):
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
    vragen = _pittig.plat(vragen)
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        lengtes = [len(o) for o in (v.get("opties") or [""])]
        # "Geen van deze antwoorden" is bijna altijd de langste optie, en die
        # lengte zegt niets over de inhoud. Zulke opties blijven hier buiten.
        vrij = [i for i, o in enumerate((v.get("opties") or [""])) if not sluitend(o)]
        juist = [i for i in antw if i in vrij]
        anders = [lengtes[i] for i in vrij if i not in antw]
        if juist and anders and min(lengtes[i] for i in juist) > max(anders) + SPELING:
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
    aantal = getattr(module, "AANTAL", 20)
    if len(_pittig.plat(vragen)) != aantal:
        meldingen.append(f"{len(_pittig.plat(vragen))} vragen in plaats van {aantal}")
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
    for v in _pittig.plat(vragen):
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
