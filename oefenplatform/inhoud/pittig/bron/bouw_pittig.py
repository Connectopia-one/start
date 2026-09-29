# -*- coding: utf-8 -*-
"""Zet de pittige hoofdstukken om in importbestanden.

    python3 inhoud/pittig/bron/bouw_pittig.py            # alles
    python3 inhoud/pittig/bron/bouw_pittig.py start_wiskunde

Bij élk hoofdstuk van een vak hoort hier een tweede, moeilijker hoofdstuk met
twintig vragen: "Getallenkennis — pittig" naast "Getallenkennis". Dat kwam er
op 28 september 2026 na een melding van een kind uit de testgroep dat een
leerjaar gesprongen was: "En nog vind ik deze oefeningen te makkelijk. Er
zitten oefeningen in die al een keer eerder in rekenen zijn voorgekomen. En
als een beetje goed geheugen hebt onthoud je de antwoorden."

Twee dingen volgen daaruit, en het script bewaakt ze allebei:

1. Moeilijker mag geen nieuwe leerstof zijn. Alles staat op wat in het gewone
   hoofdstuk al aan bod komt, zodat de leerbundel blijft dekken. De verdieping
   zit in de vraag: twee stappen, omgekeerd redeneren, een veelgemaakte fout
   die juist lijkt, of een besluit dat je zelf moet trekken.
2. Geen enkele vraag mag al ergens in dit niveau staan. Het script legt elke
   vraag naast alle bestaande vragen van hetzelfde niveau en weigert bij een
   herhaling.

Verder weigert het te schrijven bij een vraag zonder uitleg, een antwoord
buiten de opties, een rekenveld dat niet uitkomt, of een patroon waarmee je
zou kunnen gokken (zie inhoud/controleer_patronen.py).
"""
import importlib
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent
UIT = HIER.parent
INHOUD = UIT.parent
ACHTERVOEGSEL = " — pittig"

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
    return str(tekst).replace(" ", "").replace(" ", "").replace(".", ",").strip()


def vergelijkbaar(vraag):
    """De vraag zonder opmaak, om herhalingen mee op te sporen."""
    zonder = re.sub(r"\{\{[^}]*\}\}", " ", str(vraag).lower())
    return re.sub(r"[^a-z0-9]+", "", zonder)


def bestaande_vragen():
    """Elke vraag die al ergens in inhoud/ staat, per niveau en met waar ze staat.

    Per niveau, want dezelfde vraagzin in 🧱 Basis en in 🌱 Start is geen
    herhaling voor een kind dat maar één van die twee doet. Binnen hetzelfde
    niveau is ze dat wél, en dat is net wat de melding aankaartte.
    """
    gezien = {}
    for pad in sorted(INHOUD.glob("*/*.json")):
        if pad.parent.name == "pittig":
            continue
        try:
            data = json.loads(pad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for h in data.get("hoofdstukken", []):
            niveau = h.get("niveau") or pad.parent.name
            for v in h.get("vragen", []):
                sleutel = (niveau, vergelijkbaar(v.get("vraag", "")))
                gezien.setdefault(sleutel, f"{pad.name} / {h.get('titel')}")
    return gezien


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
    delen += [d.split(None, 1)[0] for d in str(verwacht).split(" of ") if " " in d.strip()]
    # Een teken dat aan het getal vastgeschreven staat (55°, 87,5%) hoort niet
    # bij de berekening; hetzelfde onderscheid maakt components/Quiz.tsx.
    delen += [d.rstrip("°%€ ") for d in list(delen)]
    if kaal(uitkomst) not in [kaal(d) for d in delen]:
        return [f"{vraag['vraag'][:60]}: reken geeft {uitkomst}, er staat {verwacht}"]
    return []


def nakijken(module, niveau, titel, vragen, elders, gezien):
    meldingen = []
    for v in vragen:
        kop = f"{titel} / {v['vraag'][:50]}"
        sleutel = (niveau, vergelijkbaar(v["vraag"]))
        if sleutel in gezien:
            meldingen.append(f"{kop}: staat ook in {gezien[sleutel]}")
        elif sleutel in elders:
            meldingen.append(f"{kop}: staat al in {elders[sleutel]}")
        gezien[sleutel] = f"{module} / {titel}"
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


def gokpatronen(titel, vragen):
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
            f"{titel}: bij {langst} van de {len(mk)} meerkeuzevragen is het juiste "
            f"antwoord de langste optie. Maak de andere opties langer."
        )
    wn = [v["antwoord"] for v in vragen if v["type"] == "waarofniet"]
    if wn and not (WAAR_ONDER <= sum(1 for a in wn if a) / len(wn) <= WAAR_BOVEN):
        meldingen.append(
            f"{titel}: {sum(1 for a in wn if a)} van de {len(wn)} waar/niet-waar-vragen is waar."
        )
    return meldingen


def bouw(naam, elders):
    module = importlib.import_module(f"bron.{naam}")
    meldingen = []
    gezien = {}
    hoofdstukken = []
    for titel, vragen in module.HOOFDSTUKKEN:
        vragen = [dict(v) for v in vragen]
        meldingen += nakijken(naam, module.NIVEAU, titel, vragen, elders, gezien)
        meldingen += gokpatronen(titel, vragen)
        if len(vragen) != 20:
            meldingen.append(f"{titel}: {len(vragen)} vragen in plaats van 20")
        for v in vragen:
            v.pop("reken", None)
        hoofdstukken.append(
            {
                "titel": titel + ACHTERVOEGSEL,
                "niveau": module.NIVEAU,
                "gratis": False,
                "vragen": vragen,
            }
        )
    if meldingen:
        raise SystemExit(f"{naam} klopt nog niet:\n  - " + "\n  - ".join(meldingen))
    doel = UIT / module.BESTAND
    doel.write_text(
        json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    aantal = sum(len(h["vragen"]) for h in hoofdstukken)
    print(f"{doel.name:32} {module.VAK:24} {len(hoofdstukken)} hoofdstukken, {aantal} vragen")


def main():
    sys.path.insert(0, str(UIT))
    elders = bestaande_vragen()
    namen = sys.argv[1:] or sorted(
        p.stem for p in HIER.glob("*.py") if p.stem not in ("bouw_pittig", "__init__")
    )
    for naam in namen:
        bouw(naam, elders)


if __name__ == "__main__":
    main()
