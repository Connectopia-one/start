# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Frans 🚀 Boost dubbele
finaliteit: een verzonnen uitnodiging voor een buurtfeest in zes zinnen en zes
losse zinnen waarvan er twee een fout bevatten.

    python3 inhoud/uitdaging/maak_prenten_boost_df_frans.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _blad import blad, zone  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "frans-boost-df-uitdaging"

FETE = [
    "Samedi 16 mai, notre rue organise une grande fête des voisins.",
    "Le rendez-vous est à 15 h, devant l'école communale.",
    "Chaque famille apporte un plat ou un dessert à partager.",
    "S'il pleut, la fête aura lieu dans la salle de sport.",
    "Mais attention : les chiens ne sont pas admis dans la salle.",
    "Pour vous inscrire, envoyez un mail avant le 10 mai.",
]

ZINNEN = [
    "Ma sœur est contente de son bulletin.",
    "Hier, nous sommes allés au cinéma.",
    "J'ai acheté un kilo des pommes au marché.",
    "Il ne mange pas de viande le vendredi.",
    "Mes amies sont très sportifs.",
    "Je voudrais un café, s'il vous plaît.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "uitnodiging-buurtfeest.svg", "Fête des voisins (verzonnen)", FETE, grootte=22)
    blad(UIT / "zes-zinnen.svg", "Zes zinnen", ZINNEN, cursief=True, grootte=23)
