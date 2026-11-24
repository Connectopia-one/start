"""Tekent de prenten voor de pittige vragen toegepaste economie 🛠️ Boost dubbele finaliteit.

    python3 inhoud/pittig/bron/maak_prenten_te_boost_df.py

Verkoopfactuur, btw-aangifte, bladzijde, kolomgrafiek, toestel, mappen, databank, bankuittreksel
en proef- en saldibalans: alles eigen tekenwerk
(boost_df_te_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden, net als de andere vakken.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_df_toegepaste_economie  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_df_te_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "te-boost-df"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)
