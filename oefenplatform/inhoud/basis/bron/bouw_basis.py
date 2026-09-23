# -*- coding: utf-8 -*-
"""Zet de themabestanden uit deze map samen in ../wiskunde.json, en rekent
elke vraag na voor ze erin gaat.

    python3 inhoud/basis/bron/bouw_basis.py

Elk thema is één bestand met een lijst DEEL1 en een lijst DEEL2 van twintig
vragen. Daar komen twee hoofdstukken van, "<thema> — deel 1" en "— deel 2",
met niveau "basis".

Wat er nagekeken wordt, per vraag (zie reken.py voor het veld `reken`):
  - bij meerkeuze: de aangeduide optie is de juiste, en geen andere optie is
    dat ook; geen twee opties zijn gelijk;
  - bij invullen: het antwoord is de juiste uitkomst;
  - bij waar/niet: het antwoord klopt met wat Python uitrekent.
Een vraag zonder na te rekenen getal draagt `WOORD` en wordt geteld. Loopt er
iets mis, dan stopt het script en wordt de JSON niet geschreven.

Daarna telt het nog of er een patroon in de vragen zit dat een kind kan
uitbuiten zonder de leerstof te kennen, zoals "het juiste antwoord is altijd
het langste" of "het is altijd waar".
"""
import json
import pathlib
import sys
from fractions import Fraction

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
from reken import getal, WOORD  # noqa: E402


# Volgorde = volgorde in het platform. De titel is ook de titel van het
# hoofdstuk en bepaalt welke leerbundel erbij hoort (zie leerbundels/bron/maak_basis.py).
#
# Het derde veld is het bestand waarin het thema terechtkomt. wiskunde.json is
# de eerste reeks, die Kim op 23 september 2026 importeerde. Wat er later bij
# kwam, staat in wiskunde-extra.json, zodat ze niets twee keer importeert.
THEMAS = [
    ("komma", "Maal en gedeeld door 10, 100 en 1000", "wiskunde.json"),
    ("maten", "Maten omzetten", "wiskunde.json"),
    ("woorden", "Wiskundewoorden", "wiskunde.json"),
    ("breuken", "Breuken, kommagetallen en gehele getallen", "wiskunde.json"),
    ("ggd_kgv", "Delers en veelvouden: ggd en kgv", "wiskunde.json"),
    # Kim, 23 september 2026: kinderen dachten dat 0,7 kleiner was dan 0,65,
    # "vermits dat ze de waarde als 7 en 65 bezagen". Met sleep- en
    # kleuroefeningen (zie components/Figuren.tsx).
    ("kommagetallen", "Kommagetallen vergelijken, optellen en aftrekken", "wiskunde-extra.json"),
    ("breuken_beeld", "Breuken in beeld", "wiskunde-extra.json"),
]

fouten = []


def gelijk(tekst, reken):
    if isinstance(reken, str):
        return tekst.strip() == reken
    waarde = getal(tekst)
    return waarde is not None and waarde == Fraction(reken)


def controleer(v, waar):
    reken = v.pop("reken")
    if reken is WOORD:
        return "woord"
    if reken is None:
        fouten.append(f"{waar}: geen uitkomst om mee te vergelijken")
        return None
    if v["type"] == "meerkeuze":
        opties = v["opties"]
        if len(set(opties)) != len(opties):
            fouten.append(f"{waar}: twee opties zijn dezelfde: {opties}")
        if not gelijk(opties[v["antwoord"]], reken):
            fouten.append(f"{waar}: aangeduid {opties[v['antwoord']]!r}, maar het moet {reken!r} zijn")
        anderen = [o for i, o in enumerate(opties) if i != v["antwoord"] and gelijk(o, reken)]
        if anderen:
            fouten.append(f"{waar}: ook {anderen} is juist")
    elif v["type"] == "invultekst":
        if not gelijk(v["antwoord"], reken) or getal(v["antwoord"]) is None and not isinstance(reken, str):
            fouten.append(f"{waar}: invul {v['antwoord']!r}, maar het moet {reken!r} zijn")
        if " " in v["antwoord"].strip() and "{{" not in v["vraag"]:
            fouten.append(f"{waar}: houd een invulantwoord zonder spaties")
    elif v["type"] == "waarofniet":
        if not isinstance(reken, bool) or v["antwoord"] is not reken:
            fouten.append(f"{waar}: waar/niet {v['antwoord']!r}, maar het moet {reken!r} zijn")
    return "gerekend"


def main():
    per_bestand = {}
    tel = {"gerekend": 0, "woord": 0}
    langst = waar = waarofniet = meerkeuze = 0
    import importlib
    for modulenaam, thema, bestand in THEMAS:
        hoofdstukken = per_bestand.setdefault(bestand, [])
        mod = importlib.import_module(modulenaam)
        for nummer, vragen in ((1, mod.DEEL1), (2, mod.DEEL2)):
            if len(vragen) != 20:
                fouten.append(f"{thema} deel {nummer}: {len(vragen)} vragen, verwacht 20")
            for i, v in enumerate(vragen, 1):
                soort = controleer(v, f"{thema} deel {nummer} vraag {i}")
                if soort:
                    tel[soort] += 1
                if v["type"] == "meerkeuze":
                    meerkeuze += 1
                    lengtes = [len(o) for o in v["opties"]]
                    if lengtes[v["antwoord"]] == max(lengtes) and lengtes.count(max(lengtes)) == 1:
                        langst += 1
                if v["type"] == "waarofniet":
                    waarofniet += 1
                    waar += v["antwoord"] is True
            titels = {(v["vraag"], tuple(v.get("opties") or ())) for v in vragen}
            if len(titels) != len(vragen):
                fouten.append(f"{thema} deel {nummer}: een vraag staat er twee keer in")
            hoofdstukken.append({
                "titel": f"{thema} — deel {nummer}",
                "niveau": "basis",
                # het allereerste is het gratis proefhoofdstuk
                "gratis": bestand == "wiskunde.json" and not hoofdstukken,
                "vragen": vragen,
            })
            print(f"  {thema} — deel {nummer}: opent met “{vragen[0]['vraag']}”")

    if fouten:
        print("\nFOUT:")
        for f in fouten:
            print("  -", f)
        raise SystemExit(1)

    print(f"\n{tel['gerekend']} vragen nagerekend, {tel['woord']} woordvragen zonder getal.")
    print(f"Juiste optie is de langste in {langst} van {meerkeuze} meerkeuzevragen.")
    print(f"Waar/niet: {waar} keer waar, {waarofniet - waar} keer niet waar.")

    print()
    for bestand, hoofdstukken in per_bestand.items():
        (HIER.parent / bestand).write_text(
            json.dumps({"hoofdstukken": hoofdstukken}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        totaal = sum(len(h["vragen"]) for h in hoofdstukken)
        print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen in {bestand}")


if __name__ == "__main__":
    main()
