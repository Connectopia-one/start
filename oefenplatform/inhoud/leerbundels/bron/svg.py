# -*- coding: utf-8 -*-
"""Kleine tekenhulpjes voor de illustraties in de leerbundels."""

FOREST = "#2f5d50"
DARK = "#234539"
AMBER = "#c17f2b"
INK = "#23291f"
DIM = "#6b7260"
BORDER = "#e4ded0"
PAPER = "#faf7f1"

def getallenlijn(breedte, links, rechts, merken, hoogte=86, label_y=None):
    """Een horizontale getallenlijn met streepjes en labels.
    merken = lijst van (waarde, label, kleur, dik) """
    m = 34
    y = 44
    span = rechts - links
    def x(v):
        return m + (v - links) / span * (breedte - 2 * m)
    d = [f'<line x1="{m}" y1="{y}" x2="{breedte-m}" y2="{y}" stroke="{INK}" stroke-width="2"/>']
    d.append(f'<path d="M{breedte-m} {y} l-9 -5 v10 z" fill="{INK}"/>')
    d.append(f'<path d="M{m} {y} l9 -5 v10 z" fill="{INK}"/>')
    for waarde, label, kleur, dik in merken:
        px = x(waarde)
        h = 13 if dik else 8
        d.append(f'<line x1="{px:.1f}" y1="{y-h}" x2="{px:.1f}" y2="{y+h}" stroke="{kleur}" stroke-width="{3 if dik else 1.6}"/>')
        if label:
            # een dik merkteken krijgt zijn label bovenaan, de rest onderaan,
            # zodat twee labels die dicht bij elkaar liggen elkaar niet raken
            ty = (y - h - 7) if dik else (y + h + 15)
            d.append(f'<text x="{px:.1f}" y="{ty}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="{12 if dik else 11}" fill="{kleur}" font-weight="{600 if dik else 400}">{label}</text>')
    return f'<svg viewBox="0 0 {breedte} {hoogte}" width="{breedte}" xmlns="http://www.w3.org/2000/svg">' + "".join(d) + "</svg>"

def breukstroken(breedte=460):
    rijen = [(1, "1 geheel"), (2, "1/2"), (3, "1/3"), (4, "1/4"), (5, "1/5")]
    h = 26
    gap = 9
    labelbreedte = 62
    balk = breedte - labelbreedte - 8
    d = []
    for i, (n, label) in enumerate(rijen):
        y = i * (h + gap)
        d.append(f'<text x="0" y="{y+17}" font-family="IBM Plex Sans,sans-serif" font-size="11" fill="{DIM}">{label}</text>')
        for k in range(n):
            x = labelbreedte + k * (balk / n)
            kleur = FOREST if k == 0 else "#ffffff"
            tekst = "#ffffff" if k == 0 else DIM
            d.append(f'<rect x="{x:.1f}" y="{y}" width="{balk/n:.1f}" height="{h}" fill="{kleur}" stroke="{DARK}" stroke-width="1.3" rx="3"/>')
            binnen = "1 geheel" if n == 1 else f"1/{n}"
            d.append(f'<text x="{x + balk/n/2:.1f}" y="{y+17}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{tekst}">{binnen}</text>')
    hoogte = len(rijen) * (h + gap)
    return f'<svg viewBox="0 0 {breedte} {hoogte}" width="{breedte}" xmlns="http://www.w3.org/2000/svg">' + "".join(d) + "</svg>"

def procentraster(gevuld=25, breedte=230):
    cel = breedte / 10
    d = []
    for r in range(10):
        for k in range(10):
            n = r * 10 + k
            kleur = AMBER if n < gevuld else "#ffffff"
            d.append(f'<rect x="{k*cel:.1f}" y="{r*cel:.1f}" width="{cel:.1f}" height="{cel:.1f}" fill="{kleur}" stroke="{BORDER}" stroke-width="1"/>')
    d.append(f'<rect x="0" y="0" width="{breedte}" height="{breedte}" fill="none" stroke="{DARK}" stroke-width="1.8"/>')
    return f'<svg viewBox="0 0 {breedte} {breedte}" width="{breedte}" xmlns="http://www.w3.org/2000/svg">' + "".join(d) + "</svg>"
