"""Tekent de prenten die Claude zelf maakt voor de pittige vragen geschiedenis 🌍 Beyond.

    python3 inhoud/pittig/bron/maak_prenten_geschiedenis_beyond.py

Schrijft naar public/examenvormen/geschiedenis-beyond/. Enkel eenvoudige
tekeningen zonder auteursrecht: tijdlijnen, schema's en grafieken met cijfers
uit de leerbundel. Foto's, affiches en spotprenten zoekt Kim zelf; die staan op
de prentenlijst.

De klikvakken (zones) in de vragen zijn in procent van de breedte en hoogte.
Wie hier iets verschuift, rekent de zones na met zone_jaar().
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "geschiedenis-beyond"
GROEN, DONKER, ACHTER = "#2f4a22", "#24331b", "#fffdf7"

# ---------------------------------------------------------------- tijdlijn 1750-2030
B, H = 1000, 210
X0, X1 = 50, 923
J0, J1 = 1750, 2030


def x_jaar(jaar):
    return X0 + (jaar - J0) / (J1 - J0) * (X1 - X0)


def zone_jaar(jaar, breed=20):
    """Een klikvak rond een jaar, in procent: breed is de breedte in jaren."""
    links = x_jaar(jaar - breed / 2) / B * 100
    return [round(links, 1), 25, round(breed / (J1 - J0) * (X1 - X0) / B * 100, 1), 55]


def tijdlijn():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(J0, J1 + 1, 10):
        x = x_jaar(j)
        if j % 50 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="102" x2="{x:.1f}" y2="118" stroke="{GROEN}" stroke-width="1.5"/>')
    d.append("</svg>")
    (UIT / "tijdlijn-1750-2030.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- volksraadpleging 1950
# Cijfers afgerond zoals in de leerbundel: bijna 58 %, ruim 70 %, amper 4 op 10.
STAVEN = [("België", 58), ("Vlaanderen", 72), ("Wallonië", 42)]
GB, GH, NUL, SCHAAL, SX, SW = 800, 470, 400, 3.2, [130, 350, 570], 140


def zone_staaf(i):
    """Klikvak over de hele kolom van staaf i, in procent."""
    return [round(SX[i] / GB * 100, 1), 12, round(SW / GB * 100, 1), 84]


def volksraadpleging():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {GB} {GH}" width="{GB}" height="{GH}" font-family="Arial, sans-serif">',
         f'<rect width="{GB}" height="{GH}" fill="{ACHTER}"/>',
         f'<text x="{GB/2}" y="34" font-size="24" text-anchor="middle" fill="{DONKER}" font-weight="bold">Volksraadpleging 1950: percentage ja-stemmen</text>']
    for pct in (0, 25, 50, 75, 100):
        y = NUL - pct * SCHAAL
        stijl = 'stroke-dasharray="8 6" stroke-width="2"' if pct == 50 else 'stroke-width="1"'
        d.append(f'<line x1="90" y1="{y}" x2="{GB-40}" y2="{y}" stroke="#b9b29c" {stijl}/>')
        d.append(f'<text x="80" y="{y+7}" font-size="18" text-anchor="end" fill="{DONKER}">{pct} %</text>')
    for (naam, pct), x in zip(STAVEN, SX):
        y = NUL - pct * SCHAAL
        d.append(f'<rect x="{x}" y="{y}" width="{SW}" height="{pct*SCHAAL}" rx="6" fill="{GROEN}"/>')
        d.append(f'<text x="{x+SW/2}" y="{y-10}" font-size="22" text-anchor="middle" fill="{DONKER}">± {pct} %</text>')
        d.append(f'<text x="{x+SW/2}" y="{NUL+34}" font-size="22" text-anchor="middle" fill="{DONKER}">{naam}</text>')
    d.append("</svg>")
    (UIT / "volksraadpleging-1950.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- vier kunstvakken (eigen tekening)
# Geen echte kunstwerken (auteursrecht): eigen tekeningen die de kenmerken tonen.
# Vak A herhaling van blikken, B stripbeeld met drukstippen, C reusachtig alledaags
# voorwerp, D minimal art. Elk vak is een kwart: zone [x, y, 50, 50].
def kunstvakken():
    W = 800
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" width="{W}" height="{W}" font-family="Arial, sans-serif">',
         '<defs><pattern id="stip" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="4" fill="#e8413c"/></pattern></defs>',
         f'<rect width="{W}" height="{W}" fill="#ffffff"/>']
    # vak A: zes dezelfde blikken in felle, vlakke kleuren
    kleuren = ["#e8413c", "#f6c700", "#1e88e5", "#43a047", "#ff7043", "#8e24aa"]
    for i, k in enumerate(kleuren):
        x, y = 40 + (i % 3) * 115, 60 + (i // 3) * 160
        d.append(f'<rect x="{x}" y="{y}" width="90" height="130" rx="8" fill="{k}" stroke="#000" stroke-width="4"/>')
        d.append(f'<rect x="{x}" y="{y+45}" width="90" height="40" fill="#fff" stroke="#000" stroke-width="3"/>')
        d.append(f'<text x="{x+45}" y="{y+73}" font-size="22" font-weight="bold" text-anchor="middle">SOEP</text>')
    # vak B: stripbeeld met drukstippen en tekstballon
    d.append('<rect x="420" y="30" width="350" height="340" fill="url(#stip)" stroke="#000" stroke-width="6"/>')
    d.append('<circle cx="540" cy="260" r="90" fill="#ffe0b2" stroke="#000" stroke-width="6"/>')
    d.append('<circle cx="510" cy="245" r="10"/><circle cx="570" cy="245" r="10"/>')
    d.append('<ellipse cx="540" cy="300" rx="22" ry="14" fill="#c62828" stroke="#000" stroke-width="4"/>')
    d.append('<path d="M600 60 h150 a20 20 0 0 1 20 20 v70 a20 20 0 0 1 -20 20 h-90 l-40 40 l10 -40 h-30 a20 20 0 0 1 -20 -20 v-70 a20 20 0 0 1 20 -20z" fill="#fff" stroke="#000" stroke-width="5"/>')
    d.append('<text x="675" y="125" font-size="34" font-weight="bold" text-anchor="middle">OH NEE!</text>')
    # vak C: reusachtige wasknijper op een plein, met een klein mensje
    d.append('<rect x="30" y="700" width="350" height="70" fill="#cfd8dc"/>')
    d.append('<rect x="150" y="470" width="34" height="250" rx="10" fill="#8d6e63" stroke="#000" stroke-width="4" transform="rotate(-6 167 595)"/>')
    d.append('<rect x="196" y="470" width="34" height="250" rx="10" fill="#8d6e63" stroke="#000" stroke-width="4" transform="rotate(6 213 595)"/>')
    d.append('<rect x="160" y="560" width="60" height="40" rx="6" fill="#9e9e9e" stroke="#000" stroke-width="4"/>')
    d.append('<circle cx="310" cy="690" r="7"/><line x1="310" y1="697" x2="310" y2="722" stroke="#000" stroke-width="4"/>')
    d.append('<line x1="310" y1="722" x2="302" y2="740" stroke="#000" stroke-width="4"/><line x1="310" y1="722" x2="318" y2="740" stroke="#000" stroke-width="4"/>')
    # vak D: minimal art, vier gelijke blokken in een reeks
    for i in range(4):
        d.append(f'<rect x="{440 + i*82}" y="560" width="62" height="62" fill="#9e9e9e"/>')
    # kaders en letters
    for x, y, l in ((0, 0, "A"), (400, 0, "B"), (0, 400, "C"), (400, 400, "D")):
        d.append(f'<rect x="{x+4}" y="{y+4}" width="392" height="392" fill="none" stroke="#2f4a22" stroke-width="4"/>')
        d.append(f'<circle cx="{x+30}" cy="{y+30}" r="20" fill="#2f4a22"/><text x="{x+30}" y="{y+38}" font-size="24" fill="#fff" text-anchor="middle" font-weight="bold">{l}</text>')
    d.append("</svg>")
    (UIT / "kunstvakken.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- betoging van bovenaf (eigen tekening)
# Een plein van bovenaf met verspreide betogers en één drukke hoek.
# Klikvak drukke hoek: zone_betoging().
BW, BH = 1000, 500
DRUK = (600, 90, 260, 210)  # x, y, breedte, hoogte van de drukke hoek


def zone_betoging():
    x, y, w, h = DRUK
    return [round(x / BW * 100, 1), round(y / BH * 100, 1), round(w / BW * 100, 1), round(h / BH * 100, 1)]


def betoging():
    import random
    rnd = random.Random(1890)
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BW} {BH}" width="{BW}" height="{BH}" font-family="Arial, sans-serif">',
         f'<rect width="{BW}" height="{BH}" fill="#d7d2c4"/>',
         '<rect x="0" y="0" width="1000" height="40" fill="#8d8778"/><rect x="0" y="460" width="1000" height="40" fill="#8d8778"/>',
         '<text x="20" y="27" font-size="20" fill="#fff">straat</text><text x="20" y="487" font-size="20" fill="#fff">straat</text>']
    x0, y0, w, h = DRUK
    for _ in range(420):
        cx, cy = x0 + rnd.random() * w, y0 + rnd.random() * h
        d.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="6" fill="#3e2723"/>')
    for _ in range(90):
        cx, cy = 30 + rnd.random() * 940, 60 + rnd.random() * 380
        if x0 - 10 < cx < x0 + w + 10 and y0 - 10 < cy < y0 + h + 10:
            continue
        d.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="6" fill="#3e2723"/>')
    d.append("</svg>")
    (UIT / "betoging-van-bovenaf.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- graanoogst China 1957-1962
# Officiële Chinese cijfers, afgerond, in miljoen ton graan.
OOGST = [(1957, 195), (1958, 200), (1959, 170), (1960, 144), (1961, 148), (1962, 160)]
OB, OH, ONUL, OSCH, OX0, OSW, OSTAP = 800, 470, 400, 1.5, 120, 80, 110


def zone_oogst(i):
    """Klikvak over de hele kolom van jaar i (0 = 1957), in procent."""
    return [round((OX0 + i * OSTAP - 10) / OB * 100, 1), 10, round((OSW + 20) / OB * 100, 1), 86]


def graanoogst():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {OB} {OH}" width="{OB}" height="{OH}" font-family="Arial, sans-serif">',
         f'<rect width="{OB}" height="{OH}" fill="{ACHTER}"/>',
         f'<text x="{OB/2}" y="34" font-size="24" text-anchor="middle" fill="{DONKER}" font-weight="bold">Graanoogst in China (miljoen ton)</text>']
    for t in (0, 50, 100, 150, 200):
        y = ONUL - t * OSCH
        d.append(f'<line x1="90" y1="{y}" x2="{OB-40}" y2="{y}" stroke="#b9b29c" stroke-width="1"/>')
        d.append(f'<text x="80" y="{y+7}" font-size="18" text-anchor="end" fill="{DONKER}">{t}</text>')
    for i, (jaar, ton) in enumerate(OOGST):
        x, y = OX0 + i * OSTAP, ONUL - ton * OSCH
        d.append(f'<rect x="{x}" y="{y}" width="{OSW}" height="{ton*OSCH}" rx="6" fill="{GROEN}"/>')
        d.append(f'<text x="{x+OSW/2}" y="{y-10}" font-size="20" text-anchor="middle" fill="{DONKER}">{ton}</text>')
        d.append(f'<text x="{x+OSW/2}" y="{ONUL+34}" font-size="22" text-anchor="middle" fill="{DONKER}">{jaar}</text>')
    d.append(f'<text x="{OB-40}" y="{OH-8}" font-size="14" text-anchor="end" fill="#6b7a5e">Afgeronde officiële Chinese cijfers</text>')
    d.append("</svg>")
    (UIT / "graanoogst-china.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- tijdlijn China 1945-2025
CB, CH, CX0, CX1, CJ0, CJ1 = 1000, 210, 50, 923, 1945, 2025


def x_china(jaar, j0=CJ0, j1=CJ1):
    return CX0 + (jaar - j0) / (j1 - j0) * (CX1 - CX0)


def zone_china(jaar, breed=3, j0=CJ0, j1=CJ1):
    """Klikvak rond een jaar op tijdlijn-china.svg (of een andere tijdlijn met j0-j1)."""
    links = x_china(jaar - breed / 2, j0, j1) / CB * 100
    return [round(links, 1), 25, round(breed / (j1 - j0) * (CX1 - CX0) / CB * 100, 1), 55]


# Israël-Palestina: zelfde tekening, van 1910 tot 2030.
IJ0, IJ1 = 1910, 2030


def zone_israel(jaar, breed=3):
    return zone_china(jaar, breed, IJ0, IJ1)


def tijdlijn_china(j0=CJ0, j1=CJ1, naam="tijdlijn-china.svg"):
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CB} {CH}" width="{CB}" height="{CH}" font-family="Arial, sans-serif">',
         f'<rect width="{CB}" height="{CH}" fill="{ACHTER}"/>',
         f'<line x1="{CX0}" y1="110" x2="{CX1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{CX1},98 {CX1+24},110 {CX1},122" fill="{GROEN}"/>']
    for j in range(j0, j1 + 1):
        x = x_china(j, j0, j1)
        if j % 10 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        elif j % 5 == 0:
            d.append(f'<line x1="{x:.1f}" y1="100" x2="{x:.1f}" y2="120" stroke="{GROEN}" stroke-width="2"/>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="105" x2="{x:.1f}" y2="115" stroke="{GROEN}" stroke-width="1"/>')
    d.append("</svg>")
    (UIT / naam).write_text("\n".join(d) + "\n", encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    tijdlijn()
    volksraadpleging()

    betoging()
    graanoogst()
    tijdlijn_china()
    tijdlijn_china(IJ0, IJ1, "tijdlijn-israel-palestina.svg")
    print("israel", {j: zone_israel(j) for j in (1917, 1947, 1948, 1967, 1973, 1978, 1987, 1993, 2000, 2002, 2023)})
    print("oogst", [zone_oogst(i) for i in range(6)])
    print("china", {j: zone_china(j) for j in (1949, 1958, 1966, 1978, 1989, 1997, 2013)})
    print("betoging", zone_betoging())
    print("staven", [zone_staaf(i) for i in range(3)])
    for j in (1789, 1815, 1830, 1871, 1914, 1945, 1989):
        print(j, zone_jaar(j))
