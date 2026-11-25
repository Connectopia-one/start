# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Economie en
bedrijfswetenschappen 🚀 Boost dubbele finaliteit: een organogram en een
factuur. Alle namen en nummers zijn verzonnen.

    python3 inhoud/uitdaging/maak_prenten_boost_df_ebw.py

De klikvakken in uitdaging/bron/boost_df_ebw.py rekenen met de maten
hieronder (procent van de prent).
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "ebw-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

OB, OH = 1000, 560
# naam: (x-midden, y-boven, breedte, hoogte)
DOZEN = {
    "zaakvoerder": (500, 90, 240, 64, ["Zaakvoerder"]),
    "juridisch": (800, 190, 220, 64, ["Juridisch advies"]),
    "aankoop": (140, 300, 190, 64, ["Aankoop"]),
    "productie": (380, 300, 190, 64, ["Productie"]),
    "verkoop": (620, 300, 190, 64, ["Verkoop"]),
    "hr": (860, 300, 190, 64, ["Personeel (HR)"]),
    "binnen": (520, 430, 170, 64, ["Binnendienst"]),
    "buiten": (720, 430, 170, 64, ["Buitendienst"]),
}

FB, FH = 1000, 760
REGELS_Y = {"te_betalen": 600, "vervaldag": 196, "btw": 556}


def doos(d, naam, stippel=False):
    x, y, b, h, tekst = DOZEN[naam]
    extra = " stroke-dasharray='10 7'" if stippel else ""
    d.append(f"<rect x='{x - b / 2}' y='{y}' width='{b}' height='{h}' rx='16' fill='{ZACHT}' stroke='{GROEN}' stroke-width='2.5'{extra}/>")
    d.append(f"<text x='{x}' y='{y + h / 2 + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='700' fill='{TEKST}'>{tekst[0]}</text>")


def organogram():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {OB} {OH}' width='{OB}' height='{OH}'>",
         f"<rect width='{OB}' height='{OH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Organogram van een fietsenfabriek</text>"]
    lijn = f"stroke='{TEKST}' stroke-width='2.5' fill='none'"
    # van de zaakvoerder naar de vier afdelingen
    d.append(f"<path d='M500,154 L500,260 M140,260 L860,260 M140,260 L140,300 M380,260 L380,300 M620,260 L620,300 M860,260 L860,300' {lijn}/>")
    # staf: gestippeld naast de lijn
    d.append(f"<path d='M500,222 L690,222' stroke='{TEKST}' stroke-width='2.5' stroke-dasharray='8 6'/>")
    # verkoop naar binnendienst en buitendienst
    d.append(f"<path d='M620,364 L620,400 M520,400 L720,400 M520,400 L520,430 M720,400 L720,430' {lijn}/>")
    for naam in DOZEN:
        doos(d, naam, stippel=(naam == "juridisch"))
    d.append("</svg>")
    (UIT / "organogram-fabriek.svg").write_text("\n".join(d), encoding="utf-8")


def doos_zone(naam):
    x, y, b, h, _ = DOZEN[naam]
    return [round((x - b / 2) / OB * 100, 1), round(y / OH * 100, 1), round(b / OB * 100, 1), round(h / OH * 100, 1)]


def factuur():
    t = lambda x, y, s, size=20, w="400", anchor="start", kleur=TEKST: (
        f"<text x='{x}' y='{y}' text-anchor='{anchor}' {FONT} font-size='{size}' font-weight='{w}' fill='{kleur}'>{s}</text>")
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {FB} {FH}' width='{FB}' height='{FH}'>",
         f"<rect width='{FB}' height='{FH}' fill='#ffffff'/>",
         f"<rect x='30' y='20' width='{FB - 60}' height='{FH - 40}' rx='14' fill='none' stroke='{RAND}' stroke-width='2'/>",
         t(60, 72, "FACTUUR", 34, "800", kleur=GROEN),
         t(60, 112, "Tweewielers De Linde bv", 20, "700"),
         t(60, 138, "Ondernemingsnummer BE 0000.000.000"),
         t(940, 112, "Factuurnummer 2026-0412", anchor="end"),
         t(940, 140, "Factuurdatum 25 november 2026", anchor="end"),
         t(940, 168, "Jouw bestelbon nr. 88", anchor="end"),
         t(940, REGELS_Y["vervaldag"], "Te betalen vóór 25 december 2026", 20, "700", anchor="end"),
         t(60, 196, "Aan: Jeugdclub De Sprong vzw"),
         f"<rect x='60' y='240' width='880' height='44' fill='{ZACHT}'/>",
         t(76, 270, "Omschrijving", 20, "700"), t(560, 270, "Aantal", 20, "700", anchor="end"),
         t(740, 270, "Prijs per stuk", 20, "700", anchor="end"), t(924, 270, "Bedrag", 20, "700", anchor="end")]
    rijen = [("Fietshelm junior", 4, "45,00", "180,00"), ("Fietsslot met code", 2, "30,00", "60,00")]
    for i, (o, a, p, b) in enumerate(rijen):
        y = 324 + i * 44
        d += [t(76, y, o), t(560, y, str(a), anchor="end"), t(740, y, f"€ {p}", anchor="end"), t(924, y, f"€ {b}", anchor="end")]
    d.append(f"<line x1='60' y1='420' x2='940' y2='420' stroke='{RAND}' stroke-width='2'/>")
    d += [t(740, 468, "Totaal zonder btw", anchor="end"), t(924, 468, "€ 240,00", anchor="end"),
          t(740, 512, "Korting 5 %", anchor="end"), t(924, 512, "− € 12,00", anchor="end"),
          t(740, REGELS_Y["btw"], "Btw 21 %", anchor="end"), t(924, REGELS_Y["btw"], "€ 47,88", anchor="end"),
          f"<rect x='480' y='{REGELS_Y['te_betalen'] - 32}' width='460' height='46' fill='{ZACHT}' stroke='{GROEN}' stroke-width='2'/>",
          t(740, REGELS_Y["te_betalen"], "Te betalen", 22, "800", anchor="end"),
          t(924, REGELS_Y["te_betalen"], "€ 275,88", 22, "800", anchor="end"),
          t(60, 680, "Betaal op rekening BE00 0000 0000 0000 met vermelding van het factuurnummer.", 18)]
    d.append("</svg>")
    (UIT / "factuur-helmen.svg").write_text("\n".join(d), encoding="utf-8")


def regel_zone(naam, x=470, b=480):
    y = REGELS_Y[naam]
    return [round(x / FB * 100, 1), round((y - 34) / FH * 100, 1), round(b / FB * 100, 1), round(48 / FH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    organogram()
    factuur()
    print({n: doos_zone(n) for n in ("juridisch", "hr", "verkoop", "zaakvoerder")},
          {n: regel_zone(n) for n in REGELS_Y})
