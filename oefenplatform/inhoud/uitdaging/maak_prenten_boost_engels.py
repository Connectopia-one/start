# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Engels 🚀 Boost doorstroom:
een kort verhaal en een mail aan een vriendin, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_boost_engels.py

De klikvakken in uitdaging/bron/boost_engels.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "engels-boost-uitdaging"
VERHAAL = [
    "Last Saturday, Tom and his sister went to the station by bike.",
    "It was raining hard and they were cycling as fast as they could.",
    "When they reached the platform, the train had already left.",
    "Tom's sister was angry, but Tom just laughed.",
    "\"Don't worry, there is another train in twenty minutes,\" he said.",
    "They will never forget that wet morning.",
]
MAIL = [
    "Hi Lisa,",
    "Thanks for your message, it was great to hear from you!",
    "Would you like to come to my birthday party on Saturday 12 June?",
    "It starts at 7 pm and you don't have to bring anything.",
    "You should take the bus, because parking is difficult.",
    "Let me know if you can come. Love, Sara",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "verhaal-trein.svg", "A rainy Saturday", VERHAAL, grootte=22)
    blad(UIT / "mail-feestje.svg", "An email to a friend", MAIL, grootte=22)
