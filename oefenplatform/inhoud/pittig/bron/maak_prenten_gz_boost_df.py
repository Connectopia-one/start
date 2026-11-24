"""Tekent de prenten voor de pittige vragen gezondheid, zorg en welzijn 🛠️ Boost dubbele finaliteit.

    python3 inhoud/pittig/bron/maak_prenten_gz_boost_df.py

Huid, gewricht, hersenen, ICF-schema, voedingsdriehoek, veiligheidstekens,
koelkast, gedekte tafel, grondplan en onderhoudsetiket: alles eigen tekenwerk
(boost_df_gz_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden, net als de andere vakken.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_df_gezondheid_zorg_en_welzijn  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_df_gz_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "gzw-boost-df"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)
