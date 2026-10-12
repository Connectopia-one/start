# -*- coding: utf-8 -*-
"""Kijkt elk vragenbestand na op patronen waarmee je kan scoren zonder de
leerstof te kennen.

    python3 inhoud/controleer_patronen.py            # alle vakken
    python3 inhoud/controleer_patronen.py start/engels.json

Twee patronen sluipen er vanzelf in wanneer je vragen in bulk schrijft:

  * het juiste antwoord is de langste optie, omdat het volledige antwoord nu
    eenmaal meer uitleg nodig heeft dan een korte afleider;
  * bijna elke waar-of-niet-vraag staat op waar, omdat het vlotter schrijft om
    een juiste zin neer te zetten dan een foute;
  * bij een vraag met aankruisvakjes zijn er bijna altijd evenveel antwoorden
    juist. Een tester merkte dat op 12 oktober 2026 zelf op: "Ik krijg meestal
    / alleen maar vragen met 1 of 3 juiste antwoorden, niet met 2 of 4. Het is
    wel makkelijk om te bedenken dat het dus maar 1 of 3 juiste antwoorden
    zijn." Natellen gaf haar gelijk: van alle vragen met meer dan één juist
    antwoord had 80 procent er precies drie.

Een kind dat niets kent, klikt dan gewoon de langste aan en antwoordt altijd
waar. Dat kan je niet zien door een paar vragen na te lezen; je moet tellen.

De grenzen: hoogstens vier op de tien meerkeuzevragen met de langste optie als
antwoord, en tussen 35 en 65 procent van de waar-of-niet-vragen op waar. Een
verschil van vijf letters of minder telt niet mee als "langer": dat ziet een
kind toch niet, en bij getalantwoorden gaf dat vals alarm.

De bouwscripts van de vakken met een bronbestand doen deze controle zelf. Dit
script dient voor de vakken die rechtstreeks als JSON bijgehouden worden, en om
alles in één keer na te tellen.
"""
import glob
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from notatie import zichtbaar  # noqa: E402  (pad moet eerst klaarstaan)

HIER = pathlib.Path(__file__).parent
SPELING = 5          # letters verschil die niet meetellen
GRENS_LANGSTE = 0.4
WAAR_ONDER, WAAR_BOVEN = 0.35, 0.65
# Bij hoeveel aankruisvragen mag hetzelfde aantal juiste antwoorden hoogstens
# voorkomen? Met twee mogelijke aantallen (2 en 3) is 50 procent het evenwicht;
# 60 laat ademruimte zonder dat je erop kan gokken.
GRENS_AANTAL = 0.6
MINIMUM_AANKRUIS = 8   # minder dan dit zegt een percentage niets


def beurten(hoofdstuk):
    """Elke vraag, en daarnaast elke beurt van een vraag met wisselende woorden.

    Een kind dat een hoofdstuk een tweede keer maakt, krijgt die beurten op
    het scherm. Ze horen er dus bij als je telt of er te raden valt.
    """
    alle = []
    for v in hoofdstuk.get("vragen", []):
        alle.append(v)
        for variant in v.get("varianten") or []:
            heel = {k: w for k, w in v.items() if k != "varianten"}
            heel.update(variant)
            alle.append(heel)
    return alle


def tel(hoofdstuk):
    vragen = beurten(hoofdstuk)
    mk = [v for v in vragen if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        lengtes = [len(zichtbaar(o)) for o in (v.get("opties") or [""])]
        anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
        if anders and min(lengtes[i] for i in antw) > max(anders) + SPELING:
            langst += 1
    wn = [v["antwoord"] for v in vragen if v["type"] == "waarofniet"]
    # Hoeveel antwoorden zijn er juist bij de vragen met aankruisvakjes? Een
    # vraag met één juist antwoord heeft rondjes en hoort hier niet bij.
    aantallen = {}
    for v in mk:
        antw = v["antwoord"]
        if isinstance(antw, list) and len(antw) > 1:
            aantallen[len(antw)] = aantallen.get(len(antw), 0) + 1
    return langst, len(mk), sum(1 for a in wn if a), len(wn), aantallen


def controleer(pad):
    data = json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    meldingen = []
    tl = tm = tw = tt = 0
    totaal_aantallen = {}
    for h in data.get("hoofdstukken", []):
        langst, mk, waar, wn, aantallen = tel(h)
        tl, tm, tw, tt = tl + langst, tm + mk, tw + waar, tt + wn
        for k, n in aantallen.items():
            totaal_aantallen[k] = totaal_aantallen.get(k, 0) + n
        if mk and langst > GRENS_LANGSTE * mk:
            meldingen.append(
                f"{h['titel']}: bij {langst} van de {mk} meerkeuzevragen is het juiste "
                f"antwoord de langste optie. Maak de andere opties langer."
            )
        if wn >= 5 and not (WAAR_ONDER <= waar / wn <= WAAR_BOVEN):
            meldingen.append(
                f"{h['titel']}: {waar} van de {wn} waar/niet-waar-vragen is waar. "
                f"Dat is te scheef om niet te kunnen gokken."
            )
    if tt and not (WAAR_ONDER <= tw / tt <= WAAR_BOVEN):
        meldingen.append(
            f"over het hele vak: {tw} van de {tt} waar/niet-waar-vragen is waar."
        )
    aankruis = sum(totaal_aantallen.values())
    if aankruis >= MINIMUM_AANKRUIS:
        for k, n in sorted(totaal_aantallen.items()):
            if n > GRENS_AANTAL * aankruis:
                meldingen.append(
                    f"over het hele vak: bij {n} van de {aankruis} aankruisvragen "
                    f"zijn er precies {k} antwoorden juist. Dan weet een kind na "
                    f"een paar vragen hoeveel het er moet aanduiden."
                )
    return (tl, tm, tw, tt, totaal_aantallen), meldingen


def main():
    if len(sys.argv) > 1:
        paden = sys.argv[1:]
    else:
        paden = sorted(
            pad
            for map in (
                "basis",
                "start",
                "spark",
                "boost-doorstroom",
                "boost-dubbele-finaliteit",
                "beyond",
                "beyond-dubbele-finaliteit",
                "uitdaging",
                "pittig",
                "hoekje",
            )
            for pad in glob.glob(str(HIER / map / "*.json"))
        )
    mis = 0
    for pad in paden:
        (tl, tm, tw, tt, aantallen), meldingen = controleer(pad)
        if not tm and not tt:
            continue
        naam = pathlib.Path(pad).name
        langste = f"{tl / tm:.0%}" if tm else "-"
        waar = f"{tw / tt:.0%}" if tt else "-"
        aankruis = sum(aantallen.values())
        verdeling = (
            " ".join(f"{k}x:{n}" for k, n in sorted(aantallen.items()))
            if aankruis
            else "-"
        )
        print(
            f"{naam:38} langste antwoord {langste:>4}   waar {waar:>4}"
            f"   aankruis {verdeling}"
        )
        for m in meldingen:
            print("   -", m)
        mis += len(meldingen)
    if mis:
        print(f"\n{mis} melding(en).")
        sys.exit(1)
    print("\nNiets te raden.")


if __name__ == "__main__":
    main()
