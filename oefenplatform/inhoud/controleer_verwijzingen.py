# -*- coding: utf-8 -*-
"""Kijkt na of elke vraag op zichzelf te beantwoorden is.

    python3 inhoud/controleer_verwijzingen.py            # alle vakken
    python3 inhoud/controleer_verwijzingen.py spark/engels.json

Een vraag die zegt "hetzelfde tekstje" of "volgens dat waslabel" leunt op de
tekst van een vraag die ervoor stond. Dat ging goed zolang een kind een
hoofdstuk van vraag 1 tot vraag 20 maakte, en het gaat sindsdien op drie
plaatsen mis:

  * op het examen over een heel vak lopen de vragen van alle hoofdstukken
    door elkaar, dus die tekst staat er nergens meer. Kim meldde het op
    14 oktober 2026 met een schermafbeelding van vraag 6 van 40: "Dezelfde
    tekst over de schoolyard. Welke hoofdpunten staan erin?" en geen tekst;
  * wie terugkomt in een hoofdstuk en enkel de vragen vraagt die hij nog niet
    juist had, krijgt de vraag zonder haar tekst;
  * bij de vraag van de dag staat één vraag helemaal alleen.

De regel is dus: de tekst hoort in de vraag die ze nodig heeft, ook als dat
betekent dat drie vragen na elkaar dezelfde tekst dragen. Een hoofdstuk met
een eigen leestekst (begrijpend lezen) is de uitzondering: daar staat de tekst
boven de hele reeks en geeft het oefenplatform ze ook op het examen mee.
"""
import glob
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent

# Een bron met een eigen naam: zegt een vraag "dat waslabel", dan bestond er
# een tekst waar dat label in stond. "de tekst" of "de teksten" is te algemeen
# om daaruit te besluiten dat er een tekst ontbreekt.
SPECIFIEK = (
    r"(tekstje|zoekertje|waslabel|nieuwsbericht|krantenstukje|stagebrief|"
    r"schoolbrief|affiche|prijslijst|openingsuren|weerbericht|formulier|"
    r"agenda|rapport|verslagje|gesprekje|berichtje|recept|forum|bijsluiter|"
    r"uitnodiging|filmreview|hotelbeoordeling|reisverslag|campagnetekst|blog|"
    r"strip|cartoon|gedicht|dialoog|mail|e-mail|brief|bericht|review|"
    r"interview)"
)
AANWIJZEND = r"(die|dat|deze|dit|datzelfde|dezelfde|hetzelfde)"
NOGMAALS = (r"(dezelfde|hetzelfde|datzelfde|nog eens|nog altijd|nog dat|"
            r"nog het|nog de|nog die|bovenstaande)")
TERUG = re.compile(
    # "Hetzelfde zoekertje.", "Nog eens die tekst."
    r"\b" + NOGMAALS + r"\s+(\w+\s+)?(" + SPECIFIEK + r"|tekst)\b"
    # "het tekstje over Namen", "die tekst over het museum"
    r"|\b(" + AANWIJZEND + r"|het|de)\s+(" + SPECIFIEK + r"|tekst)\s+over\b"
    # "volgens het zoekertje", "op dat formulier", "in dat recept"
    r"|\b(volgens|van|in|uit|op)\s+(" + AANWIJZEND + r"|het|de)\s+"
    r"(\w+\s+)?" + SPECIFIEK + r"\b",
    re.I,
)

# Haalt de vraag zelf een tekst aan, dan staat ze er gewoon bij.
AANHALING = re.compile(r"['‘’“”«»\"]")

# De vijf vragen die zo klinken maar een algemene uitspraak zijn: "hetzelfde
# bericht" gaat daar over twee ontvangers of twee lezers, niet over een tekst
# die ergens anders staat. Nagekeken op 14 oktober 2026. Verandert zo'n vraag
# van tekst, dan valt ze hier weer uit en kijk je ze opnieuw na.
GOED = {
    "Welke tekstsoorten kunnen allebei in dezelfde tekst zitten?",
    "Waarom zeggen twee lezers soms iets heel anders over hetzelfde gedicht?",
    "Je stuurt eerst een spraakbericht en daarna dezelfde tekst als mail. "
    "Welk element van het communicatiemodel verandert daardoor?",
    "Je vindt hetzelfde bericht op vijf sites, allemaal met exact dezelfde "
    "zinnen. Wat besluit je?",
    "Hetzelfde bericht kan bij twee ontvangers een ander effect hebben.",
}

MAPPEN = (
    "basis", "start", "spark", "boost-doorstroom", "boost-dubbele-finaliteit",
    "beyond", "beyond-dubbele-finaliteit", "uitdaging", "pittig", "hoekje",
    "varianten",
)


def controleer(pad):
    meldingen = []
    data = json.loads(pathlib.Path(pad).read_text())
    for h in data.get("hoofdstukken", []):
        if h.get("leestekst"):
            continue
        for i, v in enumerate(h.get("vragen", []), 1):
            tekst = v.get("vraag", "")
            if tekst in GOED or AANHALING.search(tekst):
                continue
            if TERUG.search(tekst):
                meldingen.append(f'{h["titel"]} nr {i}: {tekst[:90]}')
    return meldingen


def main():
    paden = sys.argv[1:] or sorted(
        pad
        for map in MAPPEN
        for pad in glob.glob(str(HIER / map / "*.json"))
    )
    mis = 0
    for pad in paden:
        pad = pad if pathlib.Path(pad).exists() else str(HIER / pad)
        meldingen = controleer(pad)
        for m in meldingen:
            print(f"{pathlib.Path(pad).name}: {m}")
        mis += len(meldingen)
    if mis:
        print(f"\n{mis} vraag(en) leunen op een tekst die er niet bij staat.")
        sys.exit(1)
    print("Elke vraag staat op zichzelf.")


if __name__ == "__main__":
    main()
