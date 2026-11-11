# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging samenleving en economie ✨ Spark
(zelf getekend): een leeg mailvenster en een stukje rekenblad.

    python3 inhoud/uitdaging/maak_prenten_spark_samenleving.py

De klikvakken in uitdaging/bron/spark_samenleving.py staan in procent van
deze prenten; wie hier iets verschuift, moet die mee aanpassen.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "samenleving-spark"
FONT = "font-family='Nunito, Arial, sans-serif'"
TEKST = "#2b2b2b"


def mail():
    d = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 420' width='800' height='420'>",
         "<rect width='800' height='420' fill='#ffffff'/>",
         f"<rect x='10' y='10' width='780' height='400' rx='12' fill='#f7f7f7' stroke='{TEKST}' stroke-width='2'/>",
         "<rect x='10' y='10' width='780' height='46' rx='12' fill='#2f4a22'/>",
         f"<text x='30' y='41' {FONT} font-size='20' font-weight='700' fill='#ffffff'>Nieuw bericht</text>"]
    for i, label in enumerate(["Aan:", "CC:", "BCC:", "Onderwerp:"]):
        y = 70 + i * 45
        d.append(f"<text x='30' y='{y + 26}' {FONT} font-size='18' fill='{TEKST}'>{label}</text>")
        d.append(f"<rect x='150' y='{y}' width='620' height='36' rx='6' fill='#ffffff' stroke='#b9b9b9'/>")
    d.append("<rect x='30' y='255' width='740' height='140' rx='6' fill='#ffffff' stroke='#b9b9b9'/>")
    d.append("</svg>")
    (UIT / "mailvenster.svg").write_text("\n".join(d), encoding="utf-8")


def rekenblad():
    d = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 360' width='800' height='360'>",
         "<rect width='800' height='360' fill='#ffffff'/>",
         "<rect x='0' y='0' width='800' height='45' fill='#e8eee3'/>",
         "<rect x='0' y='0' width='60' height='360' fill='#e8eee3'/>"]
    for i, k in enumerate("ABCDE"):
        x = 60 + i * 148
        d.append(f"<text x='{x + 74}' y='30' text-anchor='middle' {FONT} font-size='18' font-weight='700' fill='{TEKST}'>{k}</text>")
    for r in range(7):
        y = 45 + r * 45
        if r < 7:
            d.append(f"<text x='30' y='{y + 30}' text-anchor='middle' {FONT} font-size='18' font-weight='700' fill='{TEKST}'>{r + 1}</text>")
    for i in range(6):
        x = 60 + i * 148
        d.append(f"<line x1='{x}' y1='0' x2='{x}' y2='360' stroke='#b9b9b9'/>")
    for r in range(8):
        y = 45 + r * 45
        d.append(f"<line x1='0' y1='{y}' x2='800' y2='{y}' stroke='#b9b9b9'/>")
    waarden = {(0, 0): "Maand", (1, 0): "Zakgeld", (2, 0): "Uitgaven",
               (0, 1): "januari", (1, 1): "30", (2, 1): "18",
               (0, 2): "februari", (1, 2): "30", (2, 2): "22",
               (0, 3): "maart", (1, 3): "30", (2, 3): "15"}
    for (k, r), w in waarden.items():
        d.append(f"<text x='{60 + k * 148 + 10}' y='{45 + r * 45 + 30}' {FONT} font-size='18' fill='{TEKST}'>{w}</text>")
    d.append("</svg>")
    (UIT / "rekenblad.svg").write_text("\n".join(d), encoding="utf-8")


def zone_cel(kolom, rij):
    """Klikvak van een cel (kolom 0 = A, rij 1 = rij 1), in procent."""
    return [round((60 + kolom * 148) / 800 * 100, 1), round((45 + (rij - 1) * 45) / 360 * 100, 1),
            round(148 / 800 * 100, 1), round(45 / 360 * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    mail()
    rekenblad()
    print("C3", zone_cel(2, 3), "B4", zone_cel(1, 4))
