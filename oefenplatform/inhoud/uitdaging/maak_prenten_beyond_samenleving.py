# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Samenleving en economie 🌍
Beyond doorstroom: een vereenvoudigde loonbrief en een verdachte mail.
Alle namen en cijfers zijn verzonnen.

    python3 inhoud/uitdaging/maak_prenten_beyond_samenleving.py

De klikvakken in uitdaging/bron/beyond_samenleving.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "samenleving-beyond-uitdaging"
LOONBRIEF = [
    "Brutoloon: 3000,00 euro",
    "Persoonlijke RSZ-bijdrage (13,07 %): − 392,10 euro",
    "Belastbaar loon: 2607,90 euro",
    "Bedrijfsvoorheffing: − 540,00 euro",
    "Nettoloon: 2067,90 euro",
    "Maaltijdcheques: 20 stuks",
]
MAIL = [
    "Van: klantendienst@bankk-be-veilig.com",
    "Beste klant,",
    "Uw rekening wordt binnen 24 uur geblokkeerd!",
    "Klik op deze link en vul uw pincode en kaartnummer in.",
    "Wij danken u voor uw vertrouwen in onze bank.",
    "Met vriendelijke groeten, uw bank",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "loonbrief.svg", "Loonbrief van Sara, oktober (vereenvoudigd)", LOONBRIEF, grootte=23)
    blad(UIT / "mail-bank.svg", "Een mail in je inbox", MAIL, grootte=23)
