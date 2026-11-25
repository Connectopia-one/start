# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Frans 🌍 Beyond doorstroom:
een kort opiniestuk en een formele brief, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_beyond_frans.py

De klikvakken in uitdaging/bron/beyond_frans.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "frans-beyond-uitdaging"
ARTIKEL = [
    "Dans beaucoup de villes, on interdit les voitures dans le centre.",
    "Les commerçants craignent de perdre des clients.",
    "Pourtant, les rues sans voitures attirent souvent plus de promeneurs.",
    "À Gand, par exemple, l'air est devenu plus propre depuis 2017.",
    "À mon avis, chaque ville devrait essayer cette idée.",
    "Bref, un centre sans voitures est bon pour tout le monde.",
]
LETTRE = [
    "Madame, Monsieur,",
    "Je vous écris pour poser ma candidature à un stage dans votre hôtel.",
    "J'ai déjà travaillé deux étés dans un restaurant à Namur.",
    "Salut, ce serait trop cool de bosser chez vous !",
    "Je vous serais reconnaissante de bien vouloir me fixer un entretien.",
    "Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "artikel-voitures.svg", "Des villes sans voitures ?", ARTIKEL, grootte=22)
    blad(UIT / "lettre-stage.svg", "Une lettre de candidature", LETTRE, grootte=22)
