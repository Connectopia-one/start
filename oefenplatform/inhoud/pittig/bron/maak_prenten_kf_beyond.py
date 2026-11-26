"""Tekent de eigen prenten voor de pittige vragen kunstbeschouwing en filosofie 🌍 Beyond doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_kf_beyond.py

Alles eigen tekenwerk (beyond_kf_themas/prent.py): schema's van bouwstijlen,
zuilen, perspectief en tijdlijnen, geen foto's van bestaande kunstwerken.
"""
import pathlib
import sys

# Als pakket "bron" laden, net als het bouwscript.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.beyond_kf  # noqa: E402,F401  (laadt alle thema's)
from bron.beyond_kf_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "kunst-filosofie-beyond"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)
