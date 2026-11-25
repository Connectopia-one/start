# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Toegepaste economie 🚀 Boost
dubbele finaliteit: een rekenblad met een kleine bestelling en zes verzonnen
verrichtingen van een handelszaak.

    python3 inhoud/uitdaging/maak_prenten_boost_df_te.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _blad import blad  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "te-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"
B, H = 1000, 620
X0 = 40
KOL = [("", 50), ("A", 230), ("B", 110), ("C", 120), ("D", 150), ("E", 50), ("F", 150)]
Y_KOP, RIJ = 170, 52
CEL = {
    (1, "A"): "Artikel", (1, "B"): "Aantal", (1, "C"): "Prijs", (1, "D"): "Totaal", (1, "F"): "btw-tarief",
    (2, "A"): "Pennen", (2, "B"): "10", (2, "C"): "2,00", (2, "D"): "20,00", (2, "F"): "21%",
    (3, "A"): "Schriften", (3, "B"): "5", (3, "C"): "4,00", (3, "D"): "20,00",
    (4, "A"): "Mappen", (4, "B"): "2", (4, "C"): "5,00", (4, "D"): "10,00",
    (5, "A"): "Totaal excl. btw", (5, "D"): "50,00",
    (6, "A"): "btw", (6, "D"): "10,50",
    (7, "A"): "Totaal incl. btw", (7, "D"): "60,50",
}


def pct(x, y, w, h):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


def kolx(letter):
    x = X0
    for n, w in KOL:
        if n == letter:
            return x, w
        x += w
    raise KeyError(letter)


def rekenblad():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Rekenblad: bestelling van kantoorgerief</text>",
         # naamvak en formulebalk
         f"<rect x='40' y='84' width='120' height='48' fill='#f7f4ec' stroke='#888' stroke-width='2'/>",
         f"<text x='100' y='117' text-anchor='middle' {FONT} font-size='22' fill='{TEKST}'>D2</text>",
         f"<text x='185' y='117' {FONT} font-size='22' font-style='italic' fill='#777'>fx</text>",
         f"<rect x='220' y='84' width='740' height='48' fill='#ffffff' stroke='#888' stroke-width='2'/>",
         f"<text x='236' y='117' {FONT} font-size='22' fill='{TEKST}'>=B2*C2</text>"]
    breedte = sum(w for _, w in KOL)
    # kolomkoppen
    x = X0
    for n, w in KOL:
        d.append(f"<rect x='{x}' y='{Y_KOP - 36}' width='{w}' height='36' fill='#e9e6dc' stroke='#b9b29c'/>")
        d.append(f"<text x='{x + w / 2}' y='{Y_KOP - 11}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{TEKST}'>{n}</text>")
        x += w
    for r in range(1, 8):
        y = Y_KOP + (r - 1) * RIJ
        x = X0
        for n, w in KOL:
            vul = "#e9e6dc" if n == "" else "#ffffff"
            d.append(f"<rect x='{x}' y='{y}' width='{w}' height='{RIJ}' fill='{vul}' stroke='#cfc9b6'/>")
            if n == "":
                d.append(f"<text x='{x + w / 2}' y='{y + 34}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{TEKST}'>{r}</text>")
            t = CEL.get((r, n))
            if t:
                vet = " font-weight='800'" if r in (1, 7) else ""
                if n in ("B", "C", "D") and r > 1:
                    d.append(f"<text x='{x + w - 12}' y='{y + 34}' text-anchor='end' {FONT} font-size='21'{vet} fill='{TEKST}'>{t}</text>")
                else:
                    d.append(f"<text x='{x + 12}' y='{y + 34}' {FONT} font-size='21'{vet} fill='{TEKST}'>{t}</text>")
            x += w
    # geselecteerde cel D2
    dx, dw = kolx("D")
    d.append(f"<rect x='{dx}' y='{Y_KOP + RIJ}' width='{dw}' height='{RIJ}' fill='none' stroke='{GROEN}' stroke-width='4'/>")
    d.append("</svg>")
    (UIT / "rekenblad-bestelling.svg").write_text("\n".join(d), encoding="utf-8")

    def cel(r, n):
        x, w = kolx(n)
        return pct(x, Y_KOP + (r - 1) * RIJ, w, RIJ)
    return {"naamvak": pct(40, 84, 120, 48), "formulebalk": pct(220, 84, 740, 48),
            "F2": cel(2, "F"), "D5": cel(5, "D"), "D6": cel(6, "D"), "D7": cel(7, "D"), "D2": cel(2, "D")}


VERRICHTINGEN = [
    "We kopen handelsgoederen op krediet bij een leverancier.",
    "Een klant betaalt zijn openstaande factuur via de bank.",
    "We verkopen handelsgoederen op krediet aan een klant.",
    "We sturen een klant een creditnota voor beschadigde goederen.",
    "Op 31 december schrijven we de bestelwagen af.",
    "We halen 200 euro van de bank en leggen die in de kas.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print(rekenblad())
    blad(UIT / "zes-verrichtingen.svg", "Zes verrichtingen (verzonnen)", VERRICHTINGEN, grootte=22)
