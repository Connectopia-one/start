# -*- coding: utf-8 -*-
"""Zet de vragen met meerdere juiste antwoorden in geschiedenis.json.

    python3 bron/zet_meerdere_antwoorden.py

Leest `meerdere_antwoorden.py`, vervangt daarmee de aangeduide vragen en
schrijft `geschiedenis.json` opnieuw. Het script mag zo vaak draaien als je
wil: het vervangt telkens dezelfde plaatsen.

Het bewaakt ook een aantal dingen die je met het blote oog niet ziet:

- elke vervangen vraag stond op die plaats echt als meerkeuze;
- elke nieuwe vraag heeft minstens twee juiste antwoorden;
- de nummers in `antwoord` bestaan en komen niet dubbel voor;
- geen twee opties van dezelfde vraag zijn gelijk;
- het aandeel meerkeuzevragen met meerdere antwoorden ligt tussen 20 en 30 %,
  zoals afgesproken. Staat er te veel of te weinig, dan weet je het meteen.
"""
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))

from meerdere_antwoorden import VERVANGINGEN  # noqa: E402

DOEL = HIER.parent / "geschiedenis.json"


def main():
    data = json.loads(DOEL.read_text(encoding="utf-8"))
    per_titel = {h["titel"]: h for h in data["hoofdstukken"]}

    onbekend = set(VERVANGINGEN) - set(per_titel)
    if onbekend:
        raise SystemExit(f"Onbekende hoofdstukken: {sorted(onbekend)}")

    vervangen = 0
    for titel, lijst in VERVANGINGEN.items():
        vragen = per_titel[titel]["vragen"]
        for volgnummer, nieuw in lijst:
            i = volgnummer - 1
            if not 0 <= i < len(vragen):
                raise SystemExit(f"{titel}: vraag {volgnummer} bestaat niet")
            if vragen[i]["type"] != "meerkeuze":
                raise SystemExit(f"{titel}: vraag {volgnummer} is geen meerkeuze")
            opties = nieuw["opties"]
            antwoord = nieuw["antwoord"]
            if len(set(opties)) != len(opties):
                raise SystemExit(f"{titel}: vraag {volgnummer} heeft twee gelijke opties")
            if len(set(antwoord)) != len(antwoord) or len(antwoord) < 2:
                raise SystemExit(f"{titel}: vraag {volgnummer} moet minstens twee juiste antwoorden hebben")
            if any(not 0 <= a < len(opties) for a in antwoord):
                raise SystemExit(f"{titel}: vraag {volgnummer} wijst een optie aan die niet bestaat")
            vragen[i] = {"type": "meerkeuze", "vraag": nieuw["vraag"], "opties": opties,
                         "antwoord": sorted(antwoord), "uitleg": nieuw["uitleg"]}
            vervangen += 1

    meerkeuze = meerdere = 0
    for h in data["hoofdstukken"]:
        for v in h["vragen"]:
            if v["type"] != "meerkeuze":
                continue
            meerkeuze += 1
            if isinstance(v["antwoord"], list):
                meerdere += 1
    deel = meerdere / meerkeuze
    if not 0.20 <= deel <= 0.30:
        raise SystemExit(f"{meerdere} van de {meerkeuze} is {deel:.0%}; mikken op 20 à 30 %")

    DOEL.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{vervangen} vragen vervangen.")
    print(f"{meerdere} van de {meerkeuze} meerkeuzevragen ({deel:.0%}) hebben meerdere juiste antwoorden.")


if __name__ == "__main__":
    main()
