# -*- coding: utf-8 -*-
"""Het gereedschap achter de wisselende woorden (zie inhoud/varianten/README.md).

De lijsten zelf staan per niveau in `<niveau>/bron/varianten_<niveau>.py`. Dit
bestand zet ze in de vragenbestanden, kijkt elke beurt na als een volwaardige
vraag, en schrijft het uittreksel weg dat Kim importeert.

Een variant noemt alleen wat verandert; de rest komt van de vraag zelf. Zo
staat het ook in lib/spellingvariant.ts, en zo moet het hier nagekeken worden:
een beurt die op zichzelf niet klopt, klopt ook op het scherm niet.
"""
import json
import pathlib

HIER = pathlib.Path(__file__).parent
UITTREKSELS = HIER / "varianten"


def samen(vraag: dict, variant: dict) -> dict:
    """Een variant aangevuld met wat ze niet zelf zegt, net als in het platform."""
    heel = {k: v for k, v in vraag.items() if k != "varianten"}
    heel.update(variant)
    return heel


def keur(plek: str, vraag: dict):
    soort = vraag["type"]
    if soort == "meerkeuze":
        opties = vraag["opties"]
        assert len(opties) >= 3, f"{plek}: maar {len(opties)} opties"
        assert len(set(opties)) == len(opties), f"{plek}: twee gelijke opties"
        antwoord = vraag["antwoord"]
        nummers = antwoord if isinstance(antwoord, list) else [antwoord]
        assert nummers, f"{plek}: geen antwoord"
        assert len(set(nummers)) == len(nummers), f"{plek}: hetzelfde antwoord twee keer"
        for a in nummers:
            assert isinstance(a, int) and 0 <= a < len(opties), f"{plek}: antwoord {a} bestaat niet"
    elif soort == "waarofniet":
        assert isinstance(vraag["antwoord"], bool), f"{plek}: waar of niet waar zonder boolean"
    elif soort == "invultekst":
        antwoord = vraag["antwoord"]
        antwoorden = antwoord if isinstance(antwoord, list) else [antwoord]
        assert antwoorden, f"{plek}: geen ingevuld antwoord"
        for a in antwoorden:
            assert isinstance(a, str) and a.strip(), f"{plek}: geen ingevuld antwoord"
            assert len(a.split()) <= 3, f"{plek}: te lang invulantwoord {a!r}"
        assert vraag.get("opties") is None, f"{plek}: invulvraag met opties"
    else:
        raise AssertionError(f"{plek}: onbekend type {soort}")
    assert vraag.get("uitleg"), f"{plek}: geen uitleg"


def zet_varianten(map: pathlib.Path, bestand: str, varianten: dict, stil: bool = False) -> list:
    """Zet de varianten in <map>/<bestand>; geeft de hoofdstukken terug die er een kregen."""
    pad = map / bestand
    data = json.loads(pad.read_text(encoding="utf-8"))
    geraakt = []
    for (welk, hoofdstuk), lijsten in varianten.items():
        if welk != bestand:
            continue
        kandidaten = [h for h in data["hoofdstukken"] if h["titel"] == hoofdstuk]
        assert len(kandidaten) == 1, f"{bestand}: {hoofdstuk} staat {len(kandidaten)} keer"
        h = kandidaten[0]
        per_tekst = {v["vraag"]: v for v in h["vragen"]}
        for tekst in lijsten:
            assert tekst in per_tekst, f"{bestand} / {hoofdstuk}: geen vraag met de tekst {tekst!r}"

        # Eerst alles nakijken, dan pas wegschrijven.
        rondes = {}
        for tekst, lijst in lijsten.items():
            vraag = per_tekst[tekst]
            for n, variant in enumerate(lijst, start=2):
                plek = f"{bestand} / {hoofdstuk} / {tekst[:40]}…, beurt {n}"
                assert "type" not in variant, f"{plek}: een variant mag het type niet veranderen"
                heel = samen(vraag, variant)
                keur(plek, heel)
                assert isinstance(heel["antwoord"], list) == isinstance(vraag["antwoord"], list), (
                    f"{plek}: de ene vorm heeft meerdere juiste antwoorden en de andere niet")
                rondes.setdefault(n, []).append(heel["vraag"])

        # Geen enkele ronde mag twee keer dezelfde vraag tonen. De vragen
        # zonder varianten blijven in elke ronde staan, dus die tellen mee.
        vast = [v["vraag"] for v in h["vragen"] if v["vraag"] not in lijsten]
        for n, teksten in rondes.items():
            alle = vast + teksten
            dubbel = {t for t in alle if alle.count(t) > 1}
            assert not dubbel, f"{bestand} / {hoofdstuk}, beurt {n}: staat twee keer: {dubbel}"

        for tekst, lijst in lijsten.items():
            per_tekst[tekst]["varianten"] = lijst
        geraakt.append(h)
        if not stil:
            woorden = sum(len(v) for v in lijsten.values())
            print(f"  {hoofdstuk}: {len(lijsten)} vragen, {woorden} wisselende beurten")

    pad.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return geraakt


def hoofdlijn(map: pathlib.Path, niveau: str, varianten: dict):
    """Alles wegzetten en per vak een uittreksel maken om te importeren."""
    totaal = 0
    for bestand in sorted({b for b, _ in varianten}):
        print(bestand)
        geraakt = zet_varianten(map, bestand, varianten)
        UITTREKSELS.mkdir(exist_ok=True)
        deel = UITTREKSELS / f"{niveau}-{bestand.replace('.json', '')}-varianten.json"
        deel.write_text(
            json.dumps({"hoofdstukken": geraakt}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        vragen = sum(len(h["vragen"]) for h in geraakt)
        print(f"  → {deel.name}: {len(geraakt)} hoofdstukken, {vragen} vragen\n")
        totaal += sum(len(l) for (b, _), l in varianten.items() if b == bestand)
    print(f"{totaal} vragen met wisselende woorden.")
    return 0
