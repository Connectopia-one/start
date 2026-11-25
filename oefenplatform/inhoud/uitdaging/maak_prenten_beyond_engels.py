# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Engels 🌍 Beyond doorstroom:
een kort opiniestuk en een klachtenmail, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_beyond_engels.py

De klikvakken in uitdaging/bron/beyond_engels.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "engels-beyond-uitdaging"
ARTIKEL = [
    "More and more schools in Europe are banning smartphones during lessons.",
    "Supporters say pupils concentrate better when their phones are switched off.",
    "However, critics argue that phones can also be useful learning tools.",
    "In one school, teachers noticed that pupils talked more during the breaks.",
    "In my opinion, a total ban goes too far.",
    "Therefore, schools should rather teach pupils to use their phones wisely.",
]
MAIL = [
    "Dear Sir or Madam,",
    "I am writing to complain about the headphones I ordered on 3 March.",
    "When they arrived, the left side did not work at all.",
    "Honestly, this is total rubbish, mate!",
    "I would be grateful if you could send me a new pair or refund my money.",
    "Yours faithfully, Emma Peeters",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "artikel-smartphones.svg", "Should schools ban smartphones?", ARTIKEL, grootte=22)
    blad(UIT / "mail-klacht.svg", "An email to an online shop", MAIL, grootte=22)
