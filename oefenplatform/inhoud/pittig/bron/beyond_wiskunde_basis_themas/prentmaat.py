"""Maten van de zelfgetekende grafieken, gedeeld door de vragen (klikvakken) en
door maak_prenten_wiskunde_basis_beyond.py (tekenen).

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
