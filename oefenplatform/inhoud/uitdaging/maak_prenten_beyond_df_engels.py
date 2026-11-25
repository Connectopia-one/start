# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Engels 🌍 Beyond dubbele
finaliteit: een online review van een jeugdherberg en een bericht van een
vriendin, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_engels.py

De klikvakken in uitdaging/bron/beyond_df_engels.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "engels-beyond-df-uitdaging"
REVIEW = [
    "We stayed three nights at this hostel in Edinburgh last August.",
    "The hostel is only five minutes' walk from the castle.",
    "The staff were really friendly and helped us plan our trips.",
    "Unfortunately, the showers were often cold in the morning.",
    "Breakfast costs £6, which is quite cheap for the city.",
    "I would definitely recommend it to young travellers.",
]
BERICHT = [
    "Hi Jess! Guess what? I've just got my driving licence!",
    "I passed the test this morning at the first attempt.",
    "My dad is going to lend me his car this weekend.",
    "Shall we drive to the beach on Saturday?",
    "We could leave at ten and have lunch there.",
    "Let me know by Thursday, OK? Love, Mia",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "review-hostel.svg", "A review of a youth hostel", REVIEW, grootte=22)
    blad(UIT / "bericht-mia.svg", "A message from Mia", BERICHT, grootte=22)
