"""Maten van de zelfgetekende grafieken, gedeeld door de vragen (klikvakken) en
door maak_prenten_economie_beyond.py (tekenen).

Elke grafiek heeft een naam met haar venster (xmin, xmax, ymin, ymax). Een
klikvak is [links, boven, breedte, hoogte] in procent van de prent, en wordt
berekend uit coördinaten in het assenstelsel zelf. Zo lopen vraag en prent
nooit uit elkaar.
"""

B, H = 1000, 640
LINKS, RECHTS, BOVEN, ONDER = 70, 970, 30, 610

# naam: (xmin, xmax, ymin, ymax, stap_x, stap_y)
VENSTERS = {}


def venster(naam, xmin, xmax, ymin, ymax, stap_x=1, stap_y=1):
    VENSTERS[naam] = (xmin, xmax, ymin, ymax, stap_x, stap_y)
    return naam


def px(naam, x):
    xmin, xmax = VENSTERS[naam][:2]
    return LINKS + (x - xmin) / (xmax - xmin) * (RECHTS - LINKS)


def py(naam, y):
    ymin, ymax = VENSTERS[naam][2:4]
    return ONDER - (y - ymin) / (ymax - ymin) * (ONDER - BOVEN)


def _pct(x, y, w, h):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


def punt_zone(naam, x, y, straal=28):
    """Klikvak rond een punt (x, y) van de grafiek, straal in pixels."""
    cx, cy = px(naam, x), py(naam, y)
    return _pct(cx - straal, cy - straal, 2 * straal, 2 * straal)


def vak_zone(naam, x0, x1, y0, y1):
    """Klikvak over een stuk van het vlak: x van x0 tot x1, y van y0 tot y1."""
    a, b = px(naam, x0), px(naam, x1)
    c, d = py(naam, y1), py(naam, y0)
    return _pct(min(a, b), min(c, d), abs(b - a), abs(d - c))


def strook_zone(naam, x0, x1):
    """Klikvak over een verticale strook van de hele grafiek."""
    a, b = px(naam, x0), px(naam, x1)
    return _pct(a, BOVEN, b - a, ONDER - BOVEN)


def pix_zone(x, y, w, h):
    """Klikvak in pixels van de prent (voor prenten zonder assenstelsel)."""
    return _pct(x, y, w, h)


# Kleine tekenhulpjes voor prenten zonder assenstelsel (kansboom, kruistabel).
DONKER, GROEN, LICHT, RAND = "#24331b", "#2f4a22", "#eef3e6", "#b9b29c"


def s_tekst(x, y, t, grootte=20, anker="middle", kleur=DONKER, vet=False):
    w = ' font-weight="bold"' if vet else ""
    t = str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{grootte}" text-anchor="{anker}" fill="{kleur}"{w}>{t}</text>'


def s_lijn(x1, y1, x2, y2, kleur=GROEN, dikte=3):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{kleur}" stroke-width="{dikte}"/>'


def s_vak(x, y, w, h, vul="#fffdf7", rand=RAND, dikte=2, rond=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rond}" fill="{vul}" stroke="{rand}" stroke-width="{dikte}"/>'


def s_knoop(x, y, t, breed=110):
    return s_vak(x - breed / 2, y - 22, breed, 44, vul=LICHT, rand=GROEN, rond=12) + s_tekst(x, y + 7, t, 19, vet=True)


def _kanslabel(mx, my, kans, omhoog):
    """Kans naast de tak: boven een stijgende tak, onder een dalende."""
    return s_tekst(mx - 8, my - 14 if omhoog else my + 30, kans, 20, kleur="#7a4b8c", vet=True)


def kansboom(wortel, eerste, tweede):
    """Een kansboom met twee vertakkingen.

    wortel = (x, y); eerste = [(knoopnaam, kans, (x, y)), ...];
    tweede = {knoopnaam: [(naam, kans, (x, y)), ...]}.
    Geeft (svg-stukken, takmidden, knooppunten) terug, zodat klikvakken op
    dezelfde maten steunen.
    """
    stukken, midden, knopen = [], {}, {}
    wx, wy = wortel
    stukken.append(f'<circle cx="{wx}" cy="{wy}" r="9" fill="{GROEN}"/>')
    for naam, kans, (x, y) in eerste:
        stukken.append(s_lijn(wx + 9, wy, x - 55, y))
        mx, my = (wx + x - 46) / 2, (wy + y) / 2
        midden[naam] = (mx, my)
        stukken.append(_kanslabel(mx, my, kans, y < wy))
        knopen[naam] = (x, y)
        for naam2, kans2, (x2, y2) in tweede[naam]:
            stukken.append(s_lijn(x + 55, y, x2 - 55, y2))
            mx2, my2 = (x + x2) / 2, (y + y2) / 2
            midden[(naam, naam2)] = (mx2, my2)
            stukken.append(_kanslabel(mx2, my2, kans2, y2 < y))
            knopen[(naam, naam2)] = (x2, y2)
    for k, (x, y) in knopen.items():
        stukken.append(s_knoop(x, y, k if isinstance(k, str) else k[1]))
    return stukken, midden, knopen
