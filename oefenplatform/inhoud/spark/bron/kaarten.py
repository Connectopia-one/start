"""
Tekent de kaarten van de klik- en koppelvragen van geschiedenis ✨ Spark.

De kust en de rivieren komen uit Natural Earth (publiek domein), schaal 1:10m.
Haal eerst deze twee bestanden op en zet ze in één map:
  https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_land.geojson
  https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_rivers_lake_centerlines.geojson

Draaien: python3 inhoud/spark/bron/kaarten.py <map met die bestanden>
De kaarten komen in public/examenvormen/kaarten/. Het script drukt ook de
klikvakken af, in procent van de kaart, zoals een hotspot-vraag ze wil.
"""

import json
import math
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HIER, "..", "..", "..", "public", "examenvormen", "kaarten")
W = 1000

LAND, ZEE, RIVIER, INKT, GROEN = "#efe6cf", "#cfe3ea", "#3f86b5", "#24331b", "#2f4a22"


class Kaart:
    def __init__(self, west, oost, zuid, noord):
        self.w, self.o, self.z, self.n = west, oost, zuid, noord
        self.k = math.cos(math.radians((zuid + noord) / 2))
        self.s = W / ((oost - west) * self.k)
        self.h = round((noord - zuid) * self.s)

    def xy(self, lon, lat):
        return ((lon - self.w) * self.k * self.s, (self.n - lat) * self.s)

    def procent(self, west, oost, zuid, noord):
        """Een klikvak in lengte- en breedtegraden, als [x, y, b, h] in procent."""
        x1, y1 = self.xy(west, noord)
        x2, y2 = self.xy(oost, zuid)
        r = lambda v: round(v, 1)
        return [r(x1 / W * 100), r(y1 / self.h * 100), r((x2 - x1) / W * 100), r((y2 - y1) / self.h * 100)]

    def pad(self, punten, dicht):
        uit, vorig = [], None
        for lon, lat in punten:
            x, y = self.xy(lon, lat)
            p = (round(min(W + 20, max(-20, x)), 1), round(min(self.h + 20, max(-20, y)), 1))
            # Punten die minder dan anderhalve pixel van de vorige liggen, zie
            # je niet; zonder die punten blijft de kaart klein.
            if vorig is None or abs(p[0] - vorig[0]) + abs(p[1] - vorig[1]) >= 1.5:
                uit.append(p)
                vorig = p
        if len(uit) < 2:
            return ""
        d = "M" + " L".join(f"{x},{y}" for x, y in uit)
        return d + ("Z" if dicht else "")

    def binnen(self, punten, marge=1):
        return any(self.w - marge <= lon <= self.o + marge and self.z - marge <= lat <= self.n + marge for lon, lat in punten)


def ringen(geo):
    t, c = geo["type"], geo["coordinates"]
    if t == "Polygon":
        return c
    if t == "MultiPolygon":
        return [r for p in c for r in p]
    if t == "LineString":
        return [c]
    if t == "MultiLineString":
        return c
    return []


def teken(naam, kaart, data, rivieren=(), labels=(), letters=(), lijnen_dik=3):
    land, stromen = data
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {kaart.h}" width="{W}" height="{kaart.h}" font-family="Arial, sans-serif">',
             f'<rect width="{W}" height="{kaart.h}" fill="{ZEE}"/>']
    d = [kaart.pad(r, True) for f in land for r in ringen(f["geometry"]) if kaart.binnen(r)]
    delen.append(f'<path d="{" ".join(x for x in d if x)}" fill="{LAND}" stroke="#a89a78" stroke-width="1.2" fill-rule="evenodd"/>')
    for f in stromen:
        if f["properties"].get("name") in rivieren:
            for r in ringen(f["geometry"]):
                if kaart.binnen(r, 0):
                    delen.append(f'<path d="{kaart.pad(r, False)}" fill="none" stroke="{RIVIER}" stroke-width="{lijnen_dik}" stroke-linejoin="round"/>')
    for tekst, lon, lat, grootte, draai in labels:
        x, y = kaart.xy(lon, lat)
        t = f' transform="rotate({draai} {x:.0f} {y:.0f})"' if draai else ""
        delen.append(f'<text x="{x:.0f}" y="{y:.0f}" font-size="{grootte}" font-style="italic" fill="#2d5f7a" text-anchor="middle"{t}>{tekst}</text>')
    for teken_, lon, lat, punt in letters:
        x, y = kaart.xy(lon, lat)
        if punt:
            delen.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{INKT}" stroke="white" stroke-width="3"/>')
            x, y = x + 40, y - 40
        # Groot genoeg om te lezen als de kaart op een gsm boven een vraag
        # staat; die afbeelding is daar niet meer dan 256 pixels hoog.
        delen.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="36" fill="{GROEN}" stroke="white" stroke-width="4"/>')
        delen.append(f'<text x="{x:.0f}" y="{y + 15:.0f}" font-size="42" font-weight="bold" fill="white" text-anchor="middle">{teken_}</text>')
    delen.append("</svg>")
    with open(os.path.join(UIT, naam), "w", encoding="utf-8") as f:
        f.write("\n".join(delen) + "\n")
    print(naam, kaart.h, "px hoog,", os.path.getsize(os.path.join(UIT, naam)) // 1024, "kB")


NIJL = ("Nile", "Rosetta Branch", "Damietta Branch")
TWEESTROMEN = ("Tigris", "Dicle", "Euphrates", "Firat", "Al Furat", "Shatt al Arab")


def main():
    bron = sys.argv[1]
    os.makedirs(UIT, exist_ok=True)
    lees = lambda n: json.load(open(os.path.join(bron, n), encoding="utf-8"))["features"]
    data = (lees("ne_10m_land.geojson"), lees("ne_10m_rivers_lake_centerlines.geojson"))

    # Het oude nabije oosten: drie rivieren met een nummer. In Natural Earth
    # bestaat elke rivier uit stukken met hun eigen naam (de Eufraat heet in
    # Turkije Firat, in Syrië Al Furat), dus die tellen allemaal mee.
    oosten = Kaart(24, 54, 22, 39)
    teken("oude-nabije-oosten.svg", oosten, data, rivieren=NIJL + TWEESTROMEN,
          labels=[("Middellandse Zee", 29.5, 34.2, 26, 0), ("Rode Zee", 37.2, 23.6, 24, 62), ("Perzische Golf", 51.2, 27.4, 22, 0)],
          letters=[("1", 31.2, 27.2, False), ("2", 38.0, 34.9, False), ("3", 43.9, 37.6, False)])
    print("  Mesopotamië:", oosten.procent(42, 47.6, 30.6, 36.6))

    # De Griekse wereld: drie plaatsen met een letter, en een lege kaart.
    grieks = Kaart(20.4, 25.6, 36.2, 39.2)
    plaatsen = [("A", 23.73, 37.98, True), ("B", 22.43, 37.07, True), ("C", 21.63, 37.64, True)]
    zeeen = [("Egeïsche Zee", 24.9, 37.9, 30, 0), ("Ionische Zee", 21.0, 36.6, 30, 0)]
    teken("griekse-wereld.svg", grieks, data, labels=zeeen, letters=plaatsen)
    teken("griekse-wereld-leeg.svg", grieks, data, labels=zeeen)
    print("  Peloponnesos:", grieks.procent(21.1, 23.2, 36.4, 38.2))

    # De Middellandse Zee in de tijd van de Romeinen: vier steden met een letter.
    rome = Kaart(-10, 42, 28, 54)
    teken("romeinse-rijk.svg", rome, data,
          letters=[("A", 12.5, 41.9, True), ("B", 10.3, 36.85, True), ("C", 28.98, 41.01, True), ("D", 29.9, 31.2, True)])
    # Vijf vakken die samen het grootste deel van de zee dekken, zonder land:
    # van de kust van Spanje tot voorbij Kreta.
    zee = [(4.6, 8, 37.6, 41), (10.5, 14.8, 39.2, 40.6), (17.5, 20.5, 35.5, 38.5), (12.5, 21, 33.6, 36.2), (21, 26, 33.4, 34.9),
           (0.5, 4.4, 37.3, 38.6), (26, 33, 32.3, 34.4), (28.5, 32, 34.5, 35.9),
           (1, 3.8, 40, 40.9), (-4, -1, 35.7, 36.4), (14.5, 16, 42.5, 43.8), (24, 26, 38.5, 40)]
    print("  Middellandse Zee:", [rome.procent(*v) for v in zee])


if __name__ == "__main__":
    main()
