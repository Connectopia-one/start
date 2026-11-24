"""Tekent de prenten voor de pittige vragen fysica 🔭 Beyond doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_fys_beyond.py

Alles is eigen tekenwerk (beyond_fys_themas/prent.py), Kim hoeft niets te zoeken.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import beyond_fysica  # noqa: E402,F401  (laadt alle thema's)
from beyond_fys_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "fysica-beyond"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)
