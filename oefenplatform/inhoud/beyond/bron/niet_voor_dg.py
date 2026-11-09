"""
Geschiedenis Beyond doorstroom: welke vragen gaan over leerstof die
bedrijfs- en welzijnswetenschappen niet nodig hebben (vakfiche 3DDG)?

Kim, 9 november 2026. Vergeleken regel per regel: de pdf's 3DDO en 3DDG van
de Examencommissie (2027) op Kims usb-stick. Samenvatting per hoofdstuk:
/mnt/project-files/pittig-geschiedenis-beyond/3ddg-welzijn-bedrijf.md en de
uitleg bovenaan het vak in oefenplatform/inhoud/vaknoten.ts.

Per hoofdstuk de nummers van de vragen (vanaf 1, zoals in het json-bestand;
bij pittig telt een casus met zijn deelvragen als één nummer). Die vragen
krijgen "niet_voor_dg": true. Toepassen, nadat de bestanden gebouwd zijn:

    python3 beyond/bron/niet_voor_dg.py        (uit oefenplatform/inhoud)

Bouw je geschiedenis.json of het pittige bestand opnieuw, draai dit script
dan daarna opnieuw. Verandert de volgorde of het aantal vragen van een
hoofdstuk, kijk dan ook deze nummers opnieuw na.
"""
import json
import pathlib
import sys

GEWOON = {
    "Restauratie, revolutie en het ontstaan van België — deel 1": [13, 14],
    "Restauratie, revolutie en het ontstaan van België — deel 2": [13, 14, 15, 16, 17, 18, 19, 20],
    "Industrialisatie en de sociale kwestie — deel 1": [10, 11, 12, 16, 17],
    "Industrialisatie en de sociale kwestie — deel 2": [7, 13, 14, 15, 16, 17, 18, 20],
    "Modern imperialisme, Congo en China — deel 1": [8, 9, 10, 11, 15],
    "Modern imperialisme, Congo en China — deel 2": [2, 8, 15],
    "De Eerste Wereldoorlog en de Russische revoluties — deel 1": [8, 9, 16, 18],
    "De Eerste Wereldoorlog en de Russische revoluties — deel 2": [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    "Interbellum: totalitarisme en crisis — deel 1": [1, 2, 3, 4, 5, 6, 7, 19, 20],
    "Interbellum: totalitarisme en crisis — deel 2": [1, 13, 14, 19, 20],
    "De Tweede Wereldoorlog en de Holocaust — deel 1": [10, 11],
    "De Tweede Wereldoorlog en de Holocaust — deel 2": [1, 2],
    "Een nieuwe wereldorde: VN, Koude Oorlog en Europa — deel 1": [6, 7, 8, 13, 16, 17],
    "Een nieuwe wereldorde: VN, Koude Oorlog en Europa — deel 2": [1, 2, 3, 7, 9, 11, 12, 13, 15, 16, 17],
    "Dekolonisatie en de wereld van vandaag — deel 1": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "Dekolonisatie en de wereld van vandaag — deel 2": [20],
    "België na 1945 — deel 1": [1, 2, 3, 4, 5, 13, 14],
    "België na 1945 — deel 2": [2, 3, 4, 14, 18, 20],
    "Denken, kunst en emancipatie — deel 1": [2, 3, 4, 5, 6, 19],
    "Denken, kunst en emancipatie — deel 2": [1, 2, 3, 4, 5, 6, 7],
    "Redeneren met historische bronnen — deel 1": [1, 2, 3, 15],
    "Redeneren met historische bronnen — deel 2": [6, 7, 8, 9, 10, 11, 12],
    "Beeldvorming, vergelijken en verleden-heden-toekomst — deel 2": [2, 3, 4],
    "De Volksrepubliek China: van Mao tot Xi — deel 2": [15, 16, 17, 18],
    "Denkstromingen en kunststromingen van de 19de en 20ste eeuw — deel 1": list(range(1, 21)),
}

PITTIG = {
    "Restauratie, revolutie en het ontstaan van België — pittig": [6, 16, 17, 18, 19, 20, 21, 24, 25],
    "Industrialisatie en de sociale kwestie — pittig": [6, 8, 9, 14, 17, 18, 19, 20, 21, 22, 24, 26],
    "Modern imperialisme, Congo en China — pittig": [4, 9, 10, 12, 15, 19, 28],
    "De Eerste Wereldoorlog en de Russische revoluties — pittig": [7, 11, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28],
    "Interbellum: totalitarisme en crisis — pittig": [1, 2, 3, 4, 5, 11, 21, 22, 24, 26],
    "De Tweede Wereldoorlog en de Holocaust — pittig": [10, 27, 28],
    "Een nieuwe wereldorde: VN, Koude Oorlog en Europa — pittig": [4, 5, 9, 10, 12, 13, 16, 18, 19, 20, 21, 22, 24, 28],
    "Dekolonisatie en de wereld van vandaag — pittig": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 28],
    "België na 1945 — pittig": [1, 2, 3, 4, 12, 13, 19, 20, 28],
    "Denken, kunst en emancipatie — pittig": [1, 2, 3, 4, 5, 6, 16, 17, 18, 19, 20],
    "Redeneren met historische bronnen — pittig": [1, 2, 3, 12, 13, 17, 19, 20],
    "Beeldvorming, vergelijken en verleden-heden-toekomst — pittig": [13],
    "De Volksrepubliek China: van Mao tot Xi — pittig": [3, 22, 23, 24],
    "Denkstromingen en kunststromingen van de 19de en 20ste eeuw — pittig": list(range(1, 13)),
}

BESTANDEN = [
    (pathlib.Path("beyond/geschiedenis.json"), GEWOON),
    (pathlib.Path("pittig/beyond-geschiedenis-pittig.json"), PITTIG),
]


def markeer(v: dict, aan: bool):
    doel = v["vragen"] if ("casus" in v and "vragen" in v and "type" not in v) else [v]
    for w in doel:
        if aan:
            w["niet_voor_dg"] = True
        else:
            w.pop("niet_voor_dg", None)


def main():
    totaal = 0
    for pad, lijst in BESTANDEN:
        data = json.loads(pad.read_text(encoding="utf-8"))
        titels = {h["titel"] for h in data["hoofdstukken"]}
        onbekend = set(lijst) - titels
        if onbekend:
            sys.exit(f"Onbekende hoofdstukken in {pad}: {onbekend}")
        for h in data["hoofdstukken"]:
            nrs = set(lijst.get(h["titel"], []))
            if nrs and max(nrs) > len(h["vragen"]):
                sys.exit(f"{h['titel']}: nummer te hoog")
            for i, v in enumerate(h["vragen"], 1):
                markeer(v, i in nrs)
            totaal += len(nrs)
        pad.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(pad, "gemarkeerd")
    print("Samen", totaal, "vragen of casussen met niet_voor_dg.")


if __name__ == "__main__":
    main()
