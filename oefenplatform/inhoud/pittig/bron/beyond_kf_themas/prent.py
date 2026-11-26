"""Zelfgetekende prenten voor de pittige vragen kunstbeschouwing en filosofie 🌍 Beyond doorstroom.

Elk thema maakt zijn prenten met Prent(...). De klikvakken komen uit dezelfde
coördinaten als de tekening (zone()), zodat vraag en prent nooit uit elkaar
lopen. maak_prenten_kf_beyond.py schrijft alle prenten naar
public/examenvormen/kunst-filosofie-beyond/.
"""

B, H = 1000, 640
GROEN, DONKER, ACHTER, LIJN = "#2f4a22", "#24331b", "#ffffff", "#8a8470"
BLAUW, ORANJE, PAARS, ROOD, GEEL, LICHTGROEN, GRIJS = (
    "#3b6fa0", "#b5651d", "#7a4b8c", "#b03a2e", "#e8c547", "#a8c98a", "#d9d4c4")
FONT = 'font-family="Arial, sans-serif"'

ALLE = []


def _esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Prent:
    def __init__(self, naam, titel="", wat=""):
        self.naam, self.titel, self.wat = naam, titel, wat
        self.stukken = []
        ALLE.append(self)

    @property
    def bestand(self):
        return f"{self.naam}.svg"

    # tekenen -------------------------------------------------------------
    def svg(self, s):
        self.stukken.append(s)
        return self

    def tekst(self, x, y, t, grootte=20, anker="middle", kleur=DONKER, vet=False):
        w = ' font-weight="bold"' if vet else ""
        return self.svg(f'<text x="{x}" y="{y}" font-size="{grootte}" text-anchor="{anker}" fill="{kleur}"{w}>{_esc(t)}</text>')

    def rect(self, x, y, b, h, vul=GRIJS, rand=DONKER, r=0, dik=2):
        return self.svg(f'<rect x="{x}" y="{y}" width="{b}" height="{h}" rx="{r}" fill="{vul}" stroke="{rand}" stroke-width="{dik}"/>')

    def cirkel(self, x, y, r, vul=GRIJS, rand=DONKER, dik=2):
        return self.svg(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{vul}" stroke="{rand}" stroke-width="{dik}"/>')

    def ellips(self, x, y, rx, ry, vul=GRIJS, rand=DONKER, dik=2):
        return self.svg(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{vul}" stroke="{rand}" stroke-width="{dik}"/>')

    def lijn(self, x1, y1, x2, y2, kleur=DONKER, dik=2, stippel=False):
        s = ' stroke-dasharray="8 6"' if stippel else ""
        return self.svg(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{kleur}" stroke-width="{dik}"{s}/>')

    def pad(self, d, vul="none", rand=DONKER, dik=2):
        return self.svg(f'<path d="{d}" fill="{vul}" stroke="{rand}" stroke-width="{dik}"/>')

    def pijl(self, x1, y1, x2, y2, kleur=DONKER, dik=3):
        import math
        a = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - 16 * math.cos(a - 0.4), y2 - 16 * math.sin(a - 0.4))
        p2 = (x2 - 16 * math.cos(a + 0.4), y2 - 16 * math.sin(a + 0.4))
        self.lijn(x1, y1, x2, y2, kleur, dik)
        return self.svg(f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{kleur}"/>')

    def letter(self, x, y, t):
        """Een rond label met een letter, voor klikvragen."""
        self.cirkel(x, y, 20, "#ffffff", DONKER, 2)
        return self.tekst(x, y + 7, t, 20, vet=True)

    # klikvakken ----------------------------------------------------------
    @staticmethod
    def zone(x, y, b, h):
        """Klikvak [links, boven, breedte, hoogte] in procent van de prent."""
        return [round(x / B * 100, 1), round(y / H * 100, 1), round(b / B * 100, 1), round(h / H * 100, 1)]

    @classmethod
    def rond(cls, x, y, r=34):
        return cls.zone(x - r, y - r, 2 * r, 2 * r)

    def tekening(self):
        d = [f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>']
        if self.titel:
            d.append(f'<text x="{B/2}" y="34" font-size="22" text-anchor="middle" fill="{DONKER}" font-weight="bold">{_esc(self.titel)}</text>')
        return "\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" {FONT}>', *d, *self.stukken, "</svg>"]) + "\n"


def assen(p, xmin, xmax, ymin, ymax, xlabel, ylabel, xstap, ystap, links=110, rechts=930, boven=90, onder=540):
    """Tekent een assenstelsel met raster en geeft (X, Y) terug om coördinaten om te zetten."""
    def X(x):
        return links + (x - xmin) / (xmax - xmin) * (rechts - links)
    def Y(y):
        return onder - (y - ymin) / (ymax - ymin) * (onder - boven)
    x = xmin
    while x <= xmax + 1e-9:
        p.lijn(X(x), boven, X(x), onder, "#e4e1d6", 1)
        p.tekst(X(x), onder + 24 if ymin >= 0 else Y(0) + 24, f"{x:g}".replace(".", ","), 15)
        x += xstap
    y = ymin
    while y <= ymax + 1e-9:
        p.lijn(links, Y(y), rechts, Y(y), "#e4e1d6", 1)
        p.tekst(links - 10, Y(y) + 5, f"{y:g}".replace(".", ",").replace("-", "−"), 15, "end")
        y += ystap
    y0 = Y(0) if ymin <= 0 <= ymax else onder
    p.lijn(links, y0, rechts + 10, y0, DONKER, 2)
    p.lijn(links, onder, links, boven - 10, DONKER, 2)
    p.tekst(rechts + 5, y0 - 10, xlabel, 16, "end")
    p.tekst(links - 8, boven - 20, ylabel, 16, "start")
    return X, Y
