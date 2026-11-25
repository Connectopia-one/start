# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Nederlands 🚀 Boost dubbele finaliteit.

    python3 inhoud/uitdaging/maak_prenten_boost_df_nederlands.py

Beide teksten zijn zelf geschreven, Velddorp is verzonnen. De klikvakken in
uitdaging/bron/boost_df_nederlands.py rekenen met ZINNEN en VERZEN hieronder:
elke regel is een even hoge strook, dus zone = strook van die regel.
"""
import pathlib
from xml.sax.saxutils import escape

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "nederlands-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND = "#2f4a22", "#2b2b2b", "#b9b29c"
B, KOP, STROOK = 1000, 90, 92

ZINNEN = [
    "Vanaf maart krijgt Velddorp een nieuw jeugdhuis in de oude bibliotheek.",
    "Het gemeentebestuur trekt er 250 000 euro voor uit.",
    "Dat is eindelijk eens een schitterende beslissing.",
    "Het oude jeugdhuis sloot vorig jaar, want het gebouw was niet meer veilig.",
    "Toch zijn niet alle buren tevreden: zij vrezen lawaai op vrijdagavond.",
    "Daarom sluit het jeugdhuis voortaan om middernacht de deuren.",
]
VERZEN = [
    "Het was de laatste avond van de zomervakantie.",
    "Lotte zat op het uiteinde van de pier en keek naar de zee.",
    "De golven fluisterden haar dingen toe die niemand anders hoorde.",
    "Haar broer zei niets; hij was een rots naast haar.",
    "Morgen zou alles anders zijn, dacht ze.",
    "Ze gooide een steentje in het water en stond op.",
]


def hoogte(n):
    return KOP + n * STROOK + 30


def zone(i, n):
    """Klikvak in procent voor regel i (vanaf 0) van n regels."""
    h = hoogte(n)
    return [2, round((KOP + i * STROOK) / h * 100, 1), 96, round(STROOK / h * 100, 1)]


def blad(naam, titel, regels, cursief=False):
    h = hoogte(len(regels))
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {h}' width='{B}' height='{h}'>",
         f"<rect width='{B}' height='{h}' fill='#ffffff'/>",
         f"<text x='40' y='58' {FONT} font-size='32' font-weight='800' fill='{GROEN}'>{escape(titel)}</text>"]
    for i, r in enumerate(regels):
        y = KOP + i * STROOK
        d.append(f"<rect x='24' y='{y + 6}' width='{B - 48}' height='{STROOK - 12}' rx='16' fill='#f7f4ec' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<circle cx='68' cy='{y + STROOK / 2}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='68' y='{y + STROOK / 2 + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{i + 1}</text>")
        stijl = " font-style='italic'" if cursief else ""
        d.append(f"<text x='108' y='{y + STROOK / 2 + 9}' {FONT} font-size='23'{stijl} fill='{TEKST}'>{escape(r)}</text>")
    d.append("</svg>")
    (UIT / naam).write_text("\n".join(d), encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad("bericht-jeugdhuis.svg", "Nieuw jeugdhuis voor Velddorp", ZINNEN)
    blad("verhaal-pier.svg", "Fragment uit een verhaal", VERZEN)
