"""Tekent de prenten voor de pittige vragen economie en bedrijfswetenschappen 🛠️ Boost dubbele finaliteit.

    python3 inhoud/pittig/bron/maak_prenten_eb_boost_df.py

Organogram, vacature, contract, loonbrief, affiche, documenten en vrachtbrief: alles eigen tekenwerk
(boost_df_eb_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden, net als de andere vakken.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_df_economie_en_bedrijfswetenschappen  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_df_eb_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "ebw-boost-df"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)
