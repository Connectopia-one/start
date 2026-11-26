# -*- coding: utf-8 -*-
"""Zet de hoofdstukken in latijn/ samen in ../latijn.json.

    python3 bron/bouw_latijn.py

Boost doorstroom, tweede graad, richting Latijn (vakfiche 2027_Latijn_2DO).
Elk hoofdstuk is één opgelegd tekstfragment uit de fiche: de Latijnse tekst
staat als leestekst bovenaan (met woordenlijst: *woord* is aantikbaar), daarna
twintig vragen. De bestanden heten naar hun plaats: c = Caesar en Ovidius,
n = thema natuurfenomenen, g = thema geloof en bijgeloof, l = lectuuropdracht
(eigen Nederlandse teksten over de onderwerpen van de boeken op de fiche, met
bronnen), o = oefenen met een ongeziene tekst (12,5 % van het examen).
Malleus maleficarum (Institoris II, 1, 3) ontbreekt nog: de Latijnse tekst
was digitaal niet bereikbaar.

Bij meerkeuze worden de opties vast geschud (zaadje = de vraag), zodat het
juiste antwoord niet altijd vooraan staat in de papieren versies.
"""
import glob, importlib, json, os, pathlib, random, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER / "latijn"))
from _basis import ster  # noqa: E402
mods = sorted((pathlib.Path(f).stem for f in glob.glob(str(HIER / "latijn" / "[a-z][0-9]*.py"))), key=lambda m: (int(m[1:3]), m))
H = []
for m in mods:
    M = importlib.import_module(m)
    lees = M.INLEIDING + "\n\n" + (ster(M.ALINEAS, M.WOORDEN) if M.ALINEAS else "")
    lees += "\n\nBron: " + M.BRON
    for v in M.VRAGEN:
        if v["type"] == "meerkeuze":
            r = random.Random(v["vraag"]); idx = list(range(len(v["opties"]))); r.shuffle(idx)
            juist = v["opties"][v["antwoord"]]; v["opties"] = [v["opties"][k] for k in idx]; v["antwoord"] = v["opties"].index(juist)
    H.append({"titel": M.TITEL, "niveau": "boost-doorstroom", "gratis": False,
              "leestekst": lees.strip(), "woordenlijst": M.WOORDEN, "vragen": M.VRAGEN})
json.dump({"hoofdstukken": H}, open(HIER.parent / "latijn.json", "w"), ensure_ascii=False, indent=1)
print(len(H), "hoofdstukken,", sum(len(h["vragen"]) for h in H), "vragen")
