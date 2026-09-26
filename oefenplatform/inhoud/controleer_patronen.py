# -*- coding: utf-8 -*-
"""Kijkt elk vragenbestand na op patronen waarmee je kan scoren zonder de
leerstof te kennen.

    python3 inhoud/controleer_patronen.py            # alle vakken
    python3 inhoud/controleer_patronen.py start/engels.json

Twee patronen sluipen er vanzelf in wanneer je vragen in bulk schrijft:

  * het juiste antwoord is de langste optie, omdat het volledige antwoord nu
    eenmaal meer uitleg nodig heeft dan een korte afleider;
  * bijna elke waar-of-niet-vraag staat op waar, omdat het vlotter schrijft om
    een juiste zin neer te zetten dan een foute.

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

HIER = pathlib.Path(__file__).parent
SPELING = 5          # letters verschil die niet meetellen
GRENS_LANGSTE = 0.4
WAAR_ONDER, WAAR_BOVEN = 0.35, 0.65


def tel(hoofdstuk):
    mk = [v for v in hoofdstuk.get("vragen", []) if v["type"] == "meerkeuze"]
    langst = 0
    for v in mk:
        antw = v["antwoord"] if isinstance(v["antwoord"], list) else [v["antwoord"]]
        lengtes = [len(o) for o in (v.get("opties") or [""])]
        anders = [lengtes[i] for i in range(len(lengtes)) if i not in antw]
        if anders and min(lengtes[i] for i in antw) > max(anders) + SPELING:
            langst += 1
    wn = [v["antwoord"] for v in hoofdstuk.get("vragen", []) if v["type"] == "waarofniet"]
    return langst, len(mk), sum(1 for a in wn if a), len(wn)


def controleer(pad):
    data = json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    meldingen = []
    tl = tm = tw = tt = 0
    for h in data.get("hoofdstukken", []):
        langst, mk, waar, wn = tel(h)
        tl, tm, tw, tt = tl + langst, tm + mk, tw + waar, tt + wn
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
    return (tl, tm, tw, tt), meldingen


def main():
    if len(sys.argv) > 1:
        paden = sys.argv[1:]
    else:
        paden = sorted(
            pad
            for map in ("basis", "start", "spark", "uitdaging", "hoekje")
            for pad in glob.glob(str(HIER / map / "*.json"))
        )
    mis = 0
    for pad in paden:
        (tl, tm, tw, tt), meldingen = controleer(pad)
        if not tm and not tt:
            continue
        naam = pathlib.Path(pad).name
        langste = f"{tl / tm:.0%}" if tm else "-"
        waar = f"{tw / tt:.0%}" if tt else "-"
        print(f"{naam:38} langste antwoord {langste:>4}   waar {waar:>4}")
        for m in meldingen:
            print("   -", m)
        mis += len(meldingen)
    if mis:
        print(f"\n{mis} melding(en).")
        sys.exit(1)
    print("\nNiets te raden.")


if __name__ == "__main__":
    main()
