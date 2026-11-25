# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Frans 🌍 Beyond dubbele
finaliteit: een aankondiging van een rommelmarkt en een berichtje van een
vriend, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_frans.py

De klikvakken in uitdaging/bron/beyond_df_frans.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "frans-beyond-df-uitdaging"
AFFICHE = [
    "Grande brocante au parc de la ville !",
    "Le dimanche 14 juin, de 8 heures à 17 heures.",
    "Entrée gratuite pour les visiteurs.",
    "Un emplacement pour vendre coûte 10 euros.",
    "Inscrivez-vous avant le 1er juin à la mairie.",
    "Il est interdit de vendre des animaux.",
]
SMS = [
    "Salut Léa ! Tu es libre samedi soir ?",
    "Il y a un concert gratuit sur la place du marché.",
    "Mon frère joue de la guitare dans le groupe.",
    "On pourrait manger une pizza avant le concert.",
    "Je passe te chercher à 19 heures en vélo.",
    "Réponds-moi vite ! Bisous, Hugo",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "affiche-brocante.svg", "Une affiche dans la rue", AFFICHE, grootte=23)
    blad(UIT / "sms-hugo.svg", "Un message de Hugo", SMS, grootte=23)
