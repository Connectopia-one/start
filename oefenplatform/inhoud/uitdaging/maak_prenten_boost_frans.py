# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Frans 🚀 Boost doorstroom:
een kort verhaal en een formele mail, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_boost_frans.py

De klikvakken in uitdaging/bron/boost_frans.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "frans-boost-uitdaging"
VERHAAL = [
    "Samedi dernier, Léa est allée au marché avec sa grand-mère.",
    "Il faisait beau et la place était pleine de monde.",
    "Elles avaient oublié leur sac, alors elles en ont acheté un.",
    "Pendant qu'elles payaient, un chien a volé une baguette !",
    "Tout le monde a ri, même le boulanger.",
    "Samedi prochain, Léa reviendra avec un grand sac.",
]
MAIL = [
    "Madame, Monsieur,",
    "Je suis élève en quatrième année et j'habite à Liège.",
    "Je voudrais travailler comme bénévole dans votre bibliothèque.",
    "Pourriez-vous me dire quels jours vous avez besoin d'aide ?",
    "Je vous remercie d'avance de votre réponse.",
    "Je vous prie d'agréer mes salutations distinguées. Emma Lambert",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "verhaal-marche.svg", "Au marché", VERHAAL, grootte=22)
    blad(UIT / "mail-benevole.svg", "Un e-mail à la bibliothèque", MAIL, grootte=21)
