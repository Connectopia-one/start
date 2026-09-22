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


def _svg(breedte, hoogte, inhoud):
    return (f'<svg viewBox="0 0 {breedte} {hoogte}" width="{breedte}" '
            f'xmlns="http://www.w3.org/2000/svg">{inhoud}</svg>')


def stappen(stappenlijst, breedte=470, kleur=None):
    """Vakjes met pijltjes ertussen: een stappenplan."""
    kleur = kleur or FOREST
    n = len(stappenlijst)
    pijl = 26
    vak = (breedte - (n - 1) * pijl) / n
    h = 62
    d = []
    for i, tekst in enumerate(stappenlijst):
        x = i * (vak + pijl)
        d.append(f'<rect x="{x:.1f}" y="6" width="{vak:.1f}" height="{h}" rx="10" '
                 f'fill="#ffffff" stroke="{kleur}" stroke-width="1.8"/>')
        regels = tekst.split("|")
        start = 6 + h / 2 - (len(regels) - 1) * 8
        for j, r in enumerate(regels):
            gewicht = 600 if j == 0 else 400
            vul = DARK if j == 0 else DIM
            d.append(f'<text x="{x + vak/2:.1f}" y="{start + j*16:.1f}" text-anchor="middle" '
                     f'dominant-baseline="middle" font-family="IBM Plex Sans,sans-serif" '
                     f'font-size="{11.5 if j == 0 else 10}" font-weight="{gewicht}" fill="{vul}">{r}</text>')
        if i < n - 1:
            px = x + vak + 5
            d.append(f'<path d="M{px} {6+h/2} h{pijl-14} m0 0 l-6 -5 m6 5 l-6 5" '
                     f'stroke="{kleur}" stroke-width="2" fill="none" stroke-linecap="round"/>')
    return _svg(breedte, h + 14, "".join(d))


def maatladder(eenheden, breedte=470, onder=None):
    """Een trapje van grote naar kleine eenheid, met maal/deel-pijlen."""
    n = len(eenheden)
    vak = breedte / n
    h = 34
    d = []
    for i, e in enumerate(eenheden):
        x = i * vak
        y = 10 + i * 0  # alles op één lijn houdt het rustig
        kleur = FOREST if e in ("m", "l", "g") else "#ffffff"
        tekst = "#ffffff" if kleur == FOREST else DARK
        d.append(f'<rect x="{x+3:.1f}" y="{y}" width="{vak-6:.1f}" height="{h}" rx="8" '
                 f'fill="{kleur}" stroke="{DARK}" stroke-width="1.4"/>')
        d.append(f'<text x="{x+vak/2:.1f}" y="{y+h/2+1}" text-anchor="middle" dominant-baseline="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="12" font-weight="600" fill="{tekst}">{e}</text>')
    d.append(f'<path d="M{vak*0.5:.1f} {10+h+14} H{breedte-vak*0.5:.1f} l-7 -5 m7 5 l-7 5" '
             f'stroke="{AMBER}" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
    d.append(f'<text x="{breedte/2:.1f}" y="{10+h+32}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{AMBER}">{onder or "elke stap naar rechts: × 10"}</text>')
    return _svg(breedte, 10 + h + 42, "".join(d))


def klok(uur, minuut, straal=64):
    """Een klokwijzerplaat met de wijzers op het gevraagde uur."""
    import math
    m = straal + 8
    br = m * 2
    d = [f'<circle cx="{m}" cy="{m}" r="{straal}" fill="#ffffff" stroke="{DARK}" stroke-width="2.2"/>']
    for i in range(12):
        hoek = math.radians(i * 30 - 90)
        r1, r2 = straal - 9, straal - 2
        d.append(f'<line x1="{m + r1*math.cos(hoek):.1f}" y1="{m + r1*math.sin(hoek):.1f}" '
                 f'x2="{m + r2*math.cos(hoek):.1f}" y2="{m + r2*math.sin(hoek):.1f}" '
                 f'stroke="{DIM}" stroke-width="{2.2 if i % 3 == 0 else 1.2}"/>')
        rt = straal - 21
        d.append(f'<text x="{m + rt*math.cos(hoek):.1f}" y="{m + rt*math.sin(hoek):.1f}" '
                 f'text-anchor="middle" dominant-baseline="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" fill="{DIM}">{12 if i == 0 else i}</text>')
    hu = math.radians((uur % 12) * 30 + minuut * 0.5 - 90)
    hm = math.radians(minuut * 6 - 90)
    d.append(f'<line x1="{m}" y1="{m}" x2="{m + (straal-32)*math.cos(hu):.1f}" y2="{m + (straal-32)*math.sin(hu):.1f}" '
             f'stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>')
    d.append(f'<line x1="{m}" y1="{m}" x2="{m + (straal-16)*math.cos(hm):.1f}" y2="{m + (straal-16)*math.sin(hm):.1f}" '
             f'stroke="{AMBER}" stroke-width="3" stroke-linecap="round"/>')
    d.append(f'<circle cx="{m}" cy="{m}" r="3.5" fill="{DARK}"/>')
    return _svg(br, br, "".join(d))


def staafdiagram(paren, breedte=330, hoogte=180, kleur=None):
    """paren = [(label, waarde), ...]"""
    kleur = kleur or FOREST
    links, onder, boven = 30, 28, 14
    top = max(w for _, w in paren)
    n = len(paren)
    vak = (breedte - links) / n
    bb = vak * 0.56
    vlak = hoogte - onder - boven
    d = [f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>']
    for s in range(0, top + 1, max(1, top // 4)):
        y = hoogte - onder - s / top * vlak
        d.append(f'<line x1="{links-4}" y1="{y:.1f}" x2="{links}" y2="{y:.1f}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(f'<text x="{links-7}" y="{y+3.5:.1f}" text-anchor="end" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{s}</text>')
    for i, (label, w) in enumerate(paren):
        h = w / top * vlak
        x = links + i * vak + (vak - bb) / 2
        d.append(f'<rect x="{x:.1f}" y="{hoogte-onder-h:.1f}" width="{bb:.1f}" height="{h:.1f}" fill="{kleur}" rx="3"/>')
        d.append(f'<text x="{x+bb/2:.1f}" y="{hoogte-onder+14}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{INK}">{label}</text>')
    return _svg(breedte, hoogte, "".join(d))


def taartdiagram(delen, straal=72):
    """delen = [(label, deel, kleur), ...]  — deel telt op tot 1."""
    import math
    m = straal + 6
    d = []
    hoek = -90.0
    for label, deel, kleur in delen:
        span = deel * 360
        a1 = math.radians(hoek)
        a2 = math.radians(hoek + span)
        groot = 1 if span > 180 else 0
        x1, y1 = m + straal * math.cos(a1), m + straal * math.sin(a1)
        x2, y2 = m + straal * math.cos(a2), m + straal * math.sin(a2)
        d.append(f'<path d="M{m} {m} L{x1:.1f} {y1:.1f} A{straal} {straal} 0 {groot} 1 {x2:.1f} {y2:.1f} Z" '
                 f'fill="{kleur}" stroke="#ffffff" stroke-width="2"/>')
        am = math.radians(hoek + span / 2)
        rt = straal * 0.62
        d.append(f'<text x="{m + rt*math.cos(am):.1f}" y="{m + rt*math.sin(am):.1f}" text-anchor="middle" '
                 f'dominant-baseline="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" '
                 f'font-weight="600" fill="#ffffff">{label}</text>')
        hoek += span
    return _svg(m * 2, m * 2, "".join(d))


def dobbelsteen(ogen, zijde=54):
    """Eén dobbelsteen met het gevraagde aantal ogen."""
    plek = {
        1: [(.5, .5)],
        2: [(.28, .28), (.72, .72)],
        3: [(.28, .28), (.5, .5), (.72, .72)],
        4: [(.28, .28), (.72, .28), (.28, .72), (.72, .72)],
        5: [(.28, .28), (.72, .28), (.5, .5), (.28, .72), (.72, .72)],
        6: [(.28, .25), (.72, .25), (.28, .5), (.72, .5), (.28, .75), (.72, .75)],
    }[ogen]
    d = [f'<rect x="2" y="2" width="{zijde-4}" height="{zijde-4}" rx="9" fill="#ffffff" stroke="{DARK}" stroke-width="2"/>']
    for fx, fy in plek:
        d.append(f'<circle cx="{fx*zijde:.1f}" cy="{fy*zijde:.1f}" r="4.4" fill="{DARK}"/>')
    return _svg(zijde, zijde, "".join(d))


def naast_elkaar(svgs, gap=18):
    """Zet een paar tekeningetjes netjes naast elkaar."""
    kolommen = "".join(f'<div>{s}</div>' for s in svgs)
    return (f'<div style="display:flex;gap:{gap}px;align-items:flex-end;'
            f'justify-content:center;flex-wrap:wrap;">{kolommen}</div>')


def hoekenrij(breedte=470):
    """Scherpe, rechte, stompe en gestrekte hoek naast elkaar."""
    import math
    vak = breedte / 4
    h = 104
    d = []
    for i, (graden, naam) in enumerate([(45, "scherp"), (90, "recht"), (130, "stomp"), (180, "gestrekt")]):
        cx = i * vak + vak / 2
        cy = 66
        arm = 40
        a = math.radians(-graden)
        d.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+arm}" y2="{cy}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>')
        d.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+arm*math.cos(a):.1f}" y2="{cy+arm*math.sin(a):.1f}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>')
        r = 15
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        groot = 1 if graden > 180 else 0
        if graden == 90:
            d.append(f'<path d="M{cx+11} {cy} v-11 h-11" fill="none" stroke="{AMBER}" stroke-width="1.8"/>')
        else:
            d.append(f'<path d="M{cx+r} {cy} A{r} {r} 0 {groot} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{AMBER}" stroke-width="1.8"/>')
        d.append(f'<text x="{cx+arm/2:.1f}" y="{cy+22}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{DARK}">{naam}</text>')
        d.append(f'<text x="{cx+arm/2:.1f}" y="{cy+35}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{DIM}">{graden}°</text>')
    return _svg(breedte, h, "".join(d))


def vormenrij(breedte=470):
    """Vierkant, rechthoek, driehoek, cirkel, ruit en trapezium, met naam."""
    vak = breedte / 6
    h = 96
    cy = 40
    d = []
    vormen = [
        ("vierkant", '<rect x="{x0}" y="{y0}" width="46" height="46" fill="#ffffff" stroke="{k}" stroke-width="2" rx="2"/>'),
        ("rechthoek", '<rect x="{x0}" y="{y0}" width="58" height="36" fill="#ffffff" stroke="{k}" stroke-width="2" rx="2"/>'),
        ("driehoek", '<polygon points="{cx},{y0} {x1},{y1} {x2},{y1}" fill="#ffffff" stroke="{k}" stroke-width="2"/>'),
        ("cirkel", '<circle cx="{cx}" cy="{cym}" r="24" fill="#ffffff" stroke="{k}" stroke-width="2"/>'),
        ("ruit", '<polygon points="{cx},{y0} {x2},{cym} {cx},{y1} {x1},{cym}" fill="#ffffff" stroke="{k}" stroke-width="2"/>'),
        ("trapezium", '<polygon points="{xa},{y0} {xb},{y0} {x2},{y1} {x1},{y1}" fill="#ffffff" stroke="{k}" stroke-width="2"/>'),
    ]
    for i, (naam, sjabloon) in enumerate(vormen):
        cx = i * vak + vak / 2
        d.append(sjabloon.format(k=DARK, x0=cx - 23, y0=cy - 22, y1=cy + 24, cx=cx,
                                 x1=cx - 26, x2=cx + 26, cym=cy + 1, xa=cx - 14, xb=cx + 14))
        d.append(f'<text x="{cx:.1f}" y="{h-8}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">{naam}</text>')
    return _svg(breedte, h, "".join(d))


def ruimtefiguren(breedte=470):
    """Kubus, balk, cilinder, kegel en bol, met naam eronder."""
    vak = breedte / 5
    h = 110
    d = []
    def blok(cx, b, hh, diep):
        x, y = cx - b / 2, 62 - hh
        return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{b}" height="{hh}" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                f'<path d="M{x:.1f} {y:.1f} l{diep} -{diep} h{b} l-{diep} {diep}" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                f'<path d="M{x+b:.1f} {y:.1f} l{diep} -{diep} v{hh} l-{diep} {diep}" fill="#f2efe7" stroke="{DARK}" stroke-width="1.9"/>')
    namen = ["kubus", "balk", "cilinder", "kegel", "bol"]
    for i, naam in enumerate(namen):
        cx = i * vak + vak / 2
        if naam == "kubus":
            d.append(blok(cx, 40, 40, 13))
        elif naam == "balk":
            d.append(blok(cx, 54, 30, 12))
        elif naam == "cilinder":
            d.append(f'<path d="M{cx-22} 28 v30 a22 8 0 0 0 44 0 v-30" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                     f'<ellipse cx="{cx}" cy="28" rx="22" ry="8" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>')
        elif naam == "kegel":
            d.append(f'<path d="M{cx} 22 L{cx-22} 58 A22 8 0 0 0 {cx+22} 58 Z" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                     f'<path d="M{cx-22} 58 A22 8 0 0 1 {cx+22} 58" fill="none" stroke="{DARK}" stroke-width="1.9"/>')
        else:
            d.append(f'<circle cx="{cx}" cy="44" r="23" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                     f'<ellipse cx="{cx}" cy="44" rx="23" ry="8" fill="none" stroke="{BORDER}" stroke-width="1.5"/>')
        d.append(f'<text x="{cx:.1f}" y="{h-12}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">{naam}</text>')
    return _svg(breedte, h, "".join(d))


def cirkel_straal(breedte=300):
    m, r = breedte / 2, 66
    cy = r + 12
    d = [f'<circle cx="{m}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{DARK}" stroke-width="2"/>',
         f'<line x1="{m-r}" y1="{cy}" x2="{m+r}" y2="{cy}" stroke="{AMBER}" stroke-width="2.2"/>',
         f'<line x1="{m}" y1="{cy}" x2="{m}" y2="{cy-r}" stroke="{FOREST}" stroke-width="2.6"/>',
         f'<circle cx="{m}" cy="{cy}" r="3.4" fill="{DARK}"/>',
         f'<text x="{m+8}" y="{cy-r/2:.1f}" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{FOREST}">straal</text>',
         f'<text x="{m-r/2-8:.1f}" y="{cy-7}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{AMBER}">diameter</text>']
    return _svg(breedte, cy + r + 14, "".join(d))


def rechthoek_maten(lengte_cm, breedte_cm, breedte=330):
    schaal = min(220 / lengte_cm, 120 / breedte_cm)
    b, h = lengte_cm * schaal, breedte_cm * schaal
    x, y = (breedte - b) / 2, 26
    d = [f'<rect x="{x:.1f}" y="{y}" width="{b:.1f}" height="{h:.1f}" fill="rgba(47,93,80,.08)" stroke="{DARK}" stroke-width="2"/>']
    for k in range(1, int(lengte_cm)):
        d.append(f'<line x1="{x+k*schaal:.1f}" y1="{y}" x2="{x+k*schaal:.1f}" y2="{y+h:.1f}" stroke="{BORDER}" stroke-width="1"/>')
    for k in range(1, int(breedte_cm)):
        d.append(f'<line x1="{x:.1f}" y1="{y+k*schaal:.1f}" x2="{x+b:.1f}" y2="{y+k*schaal:.1f}" stroke="{BORDER}" stroke-width="1"/>')
    d.append(f'<text x="{x+b/2:.1f}" y="{y-9}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{DARK}">{lengte_cm} cm</text>')
    d.append(f'<text x="{x-9:.1f}" y="{y+h/2:.1f}" text-anchor="end" dominant-baseline="middle" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{DARK}">{breedte_cm} cm</text>')
    d.append(f'<text x="{x+b/2:.1f}" y="{y+h+20:.1f}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11" fill="{DIM}">omtrek {2*(lengte_cm+breedte_cm)} cm · oppervlakte {lengte_cm*breedte_cm} cm²</text>')
    return _svg(breedte, y + h + 30, "".join(d))


def lijngrafiek(punten, breedte=330, hoogte=180, labels=None):
    links, onder, boven = 30, 28, 14
    top = max(punten)
    n = len(punten)
    vlak = hoogte - onder - boven
    stap = (breedte - links - 10) / (n - 1)
    d = [f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>']
    pts = []
    for i, w in enumerate(punten):
        x = links + i * stap
        y = hoogte - onder - w / top * vlak
        pts.append(f"{x:.1f},{y:.1f}")
        d.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{FOREST}"/>')
        if labels:
            d.append(f'<text x="{x:.1f}" y="{hoogte-onder+14}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{labels[i]}</text>')
    d.insert(2, f'<polyline points="{" ".join(pts)}" fill="none" stroke="{FOREST}" stroke-width="2.2"/>')
    return _svg(breedte, hoogte, "".join(d))


def kleurstalen(paren, breedte=470):
    """paren = [(engelse naam, nederlandse naam, hex), ...]"""
    perrij = 4
    vak = breedte / perrij
    rijen = (len(paren) + perrij - 1) // perrij
    rh = 60
    d = []
    for i, (en, nl, hex_) in enumerate(paren):
        r, k = divmod(i, perrij)
        x, y = k * vak, r * rh
        d.append(f'<rect x="{x+6:.1f}" y="{y+4}" width="30" height="30" rx="7" fill="{hex_}" stroke="{DARK}" stroke-width="1.2"/>')
        d.append(f'<text x="{x+44:.1f}" y="{y+17}" font-family="IBM Plex Sans,sans-serif" font-size="11.5" font-weight="600" fill="{DARK}">{en}</text>')
        d.append(f'<text x="{x+44:.1f}" y="{y+31}" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">{nl}</text>')
    return _svg(breedte, rijen * rh - 12, "".join(d))


def woordvolgorde(delen, breedte=470):
    """delen = [(label, voorbeeld, kleur), ...] — blokken op een rij."""
    n = len(delen)
    vak = breedte / n
    h = 62
    d = []
    for i, (label, voorbeeld, kleur) in enumerate(delen):
        x = i * vak
        d.append(f'<rect x="{x+4:.1f}" y="4" width="{vak-8:.1f}" height="{h}" rx="9" '
                 f'fill="{kleur}22" stroke="{kleur}" stroke-width="1.7"/>')
        d.append(f'<text x="{x+vak/2:.1f}" y="24" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10" fill="{DIM}">{label}</text>')
        d.append(f'<text x="{x+vak/2:.1f}" y="46" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="12.5" font-weight="600" fill="{DARK}">{voorbeeld}</text>')
    return _svg(breedte, h + 12, "".join(d))


def persoonsvormen(groepen, breedte=470):
    """groepen = [(personen, vorm, kleur), ...] — wie hoort bij welke vorm."""
    n = len(groepen)
    vak = breedte / n
    # de hoogte hangt af van de groep met de meeste personen eronder,
    # anders valt het onderste vakje buiten de tekening
    meeste = max(len(p.split("|")) for p, _, _ in groepen)
    h = 16 + meeste * 15 + 16 + 30
    d = []
    for i, (personen, vorm, kleur) in enumerate(groepen):
        x = i * vak + vak / 2
        regels = personen.split("|")
        for j, r in enumerate(regels):
            d.append(f'<text x="{x:.1f}" y="{16 + j*15}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                     f'font-size="11.5" fill="{DIM}">{r}</text>')
        ty = 16 + len(regels) * 15
        d.append(f'<path d="M{x:.1f} {ty} v12 m0 0 l-4 -5 m4 5 l4 -5" stroke="{kleur}" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
        d.append(f'<rect x="{x-38:.1f}" y="{ty+16}" width="76" height="30" rx="8" fill="{kleur}" />')
        d.append(f'<text x="{x:.1f}" y="{ty+36}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="14" font-weight="600" fill="#ffffff">{vorm}</text>')
    return _svg(breedte, h + 6, "".join(d))


def spreekballonnen(regels, breedte=470):
    """regels = [(spreker, tekst, links?), ...]"""
    d = []
    y = 6
    for spreker, tekst, links in regels:
        bb = breedte * 0.68
        x = 6 if links else breedte - bb - 6
        kleur = FOREST if links else AMBER
        d.append(f'<rect x="{x:.1f}" y="{y}" width="{bb:.1f}" height="42" rx="12" '
                 f'fill="{kleur}18" stroke="{kleur}" stroke-width="1.5"/>')
        d.append(f'<text x="{x+13:.1f}" y="{y+17}" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{kleur}" font-weight="600">{spreker}</text>')
        d.append(f'<text x="{x+13:.1f}" y="{y+33}" font-family="IBM Plex Sans,sans-serif" font-size="12" fill="{DARK}">{tekst}</text>')
        y += 50
    return _svg(breedte, y, "".join(d))


def stamboom(breedte=470):
    """Een klein familieoverzicht met de Engelse woorden erbij."""
    d = []
    def vak(x, y, en, nl, kleur=FOREST):
        d.append(f'<rect x="{x}" y="{y}" width="104" height="38" rx="9" fill="#ffffff" stroke="{kleur}" stroke-width="1.6"/>')
        d.append(f'<text x="{x+52}" y="{y+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11.5" font-weight="600" fill="{DARK}">{en}</text>')
        d.append(f'<text x="{x+52}" y="{y+30}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{DIM}">{nl}</text>')
    m = breedte / 2
    vak(m - 168, 4, "grandfather", "grootvader", DIM)
    vak(m + 64, 4, "grandmother", "grootmoeder", DIM)
    vak(m - 168, 70, "father", "vader")
    vak(m + 64, 70, "mother", "moeder")
    vak(m - 168, 136, "brother", "broer", AMBER)
    vak(m - 52, 136, "me", "ik", AMBER)
    vak(m + 64, 136, "sister", "zus", AMBER)
    for x in (m - 116, m + 116):
        d.append(f'<line x1="{x}" y1="42" x2="{x}" y2="70" stroke="{BORDER}" stroke-width="1.6"/>')
    d.append(f'<line x1="{m-116}" y1="108" x2="{m+116}" y2="108" stroke="{BORDER}" stroke-width="1.6"/>')
    for x in (m - 116, m, m + 116):
        d.append(f'<line x1="{x}" y1="108" x2="{x}" y2="136" stroke="{BORDER}" stroke-width="1.6"/>')
    return _svg(breedte, 184, "".join(d))


def plattegrond(breedte=470):
    """Een heel eenvoudig stratenplannetje om de weg mee uit te leggen."""
    h = 190
    d = [f'<rect x="0" y="0" width="{breedte}" height="{h}" fill="#ffffff" stroke="{BORDER}" stroke-width="1.4" rx="10"/>']
    # straten
    d.append(f'<rect x="0" y="118" width="{breedte}" height="26" fill="#f0ece2"/>')
    d.append(f'<rect x="196" y="0" width="26" height="{h}" fill="#f0ece2"/>')
    d.append(f'<line x1="0" y1="131" x2="{breedte}" y2="131" stroke="#ffffff" stroke-width="2" stroke-dasharray="10 9"/>')
    d.append(f'<line x1="209" y1="0" x2="209" y2="{h}" stroke="#ffffff" stroke-width="2" stroke-dasharray="10 9"/>')

    def gebouw(x, y, b, hh, naam, kleur):
        d.append(f'<rect x="{x}" y="{y}" width="{b}" height="{hh}" rx="6" fill="{kleur}22" stroke="{kleur}" stroke-width="1.6"/>')
        d.append(f'<text x="{x+b/2}" y="{y+hh/2+4}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="11" font-weight="600" fill="{DARK}">{naam}</text>')

    gebouw(28, 38, 130, 52, "the school", FOREST)
    gebouw(258, 32, 96, 58, "the church", DIM)
    gebouw(258, 156, 96, 26, "the shop", AMBER)
    gebouw(370, 38, 82, 52, "the park", FOREST)
    d.append(f'<text x="24" y="172" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">'
             f'Turn right at the school.</text>')
    return _svg(breedte, h, "".join(d))


def spanningsboog(breedte=470):
    """De spanningsboog van een verhaal: begin, opbouw, hoogtepunt, einde."""
    h = 178
    basis = 128
    d = [f'<path d="M30 {basis} C 150 {basis-10}, 210 40, 300 34 C 360 30, 400 70, {breedte-30} {basis}" '
         f'fill="none" stroke="{FOREST}" stroke-width="2.6"/>']
    # de labels staan bewust aan de kant waar de lijn niet loopt,
    # anders snijdt de boog dwars door de tekst
    punten = [(30, basis, "begin", "wie, waar, wanneer", "onder"),
              (170, basis - 46, "probleem", "er loopt iets mis", "boven"),
              (300, 34, "hoogtepunt", "het spannendst", "boven"),
              (breedte - 30, basis, "einde", "het loopt af", "onder")]
    for x, y, naam, onder, kant in punten:
        d.append(f'<circle cx="{x}" cy="{y:.0f}" r="5" fill="{AMBER}"/>')
        anker = "start" if x < 100 else ("end" if x > breedte - 100 else "middle")
        if kant == "boven":
            yn, yo = y - 26, y - 12
        else:
            yn, yo = y + 20, y + 34
        d.append(f'<text x="{x}" y="{yn:.0f}" text-anchor="{anker}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="11.5" font-weight="600" fill="{DARK}">{naam}</text>')
        d.append(f'<text x="{x}" y="{yo:.0f}" text-anchor="{anker}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10" fill="{DIM}">{onder}</text>')
    return _svg(breedte, h, "".join(d))


def tekstopbouw(delen, breedte=470):
    """delen = [(naam, wat er in staat, hoogte-factor), ...] — blokken onder elkaar."""
    d = []
    y = 4
    for naam, wat, factor in delen:
        hh = 30 * factor
        d.append(f'<rect x="4" y="{y:.0f}" width="{breedte-8}" height="{hh:.0f}" rx="9" '
                 f'fill="rgba(47,93,80,.07)" stroke="{FOREST}" stroke-width="1.5"/>')
        d.append(f'<text x="20" y="{y+hh/2-3:.0f}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="12" font-weight="600" fill="{DARK}">{naam}</text>')
        d.append(f'<text x="20" y="{y+hh/2+13:.0f}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" fill="{DIM}">{wat}</text>')
        y += hh + 8
    return _svg(breedte, y, "".join(d))


def zinsdelen(delen, breedte=470):
    """Een zin in gekleurde blokjes, met eronder wat elk deel is."""
    n = len(delen)
    d = []
    x = 4
    totaal = sum(len(w) for w, _, _ in delen)
    h = 70
    for woord, naam, kleur in delen:
        b = (breedte - 8 - (n - 1) * 6) * (len(woord) / totaal)
        d.append(f'<rect x="{x:.1f}" y="4" width="{b:.1f}" height="34" rx="8" fill="{kleur}22" stroke="{kleur}" stroke-width="1.6"/>')
        d.append(f'<text x="{x+b/2:.1f}" y="26" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="13" font-weight="600" fill="{DARK}">{woord}</text>')
        d.append(f'<text x="{x+b/2:.1f}" y="55" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10" fill="{kleur}">{naam}</text>')
        x += b + 6
    return _svg(breedte, h, "".join(d))


def deeltjes(breedte=470):
    """Vast, vloeibaar en gas: hoe de deeltjes erin liggen."""
    import random
    random.seed(7)
    vak = breedte / 3
    h = 138
    bh, bb = 84, vak - 30
    d = []
    for i, (naam, onder) in enumerate([("vast", "netjes op hun plaats"),
                                       ("vloeibaar", "tegen elkaar, maar ze schuiven"),
                                       ("gas", "ver uit elkaar, ze vliegen rond")]):
        x = i * vak + 15
        d.append(f'<rect x="{x:.1f}" y="6" width="{bb:.1f}" height="{bh}" rx="8" fill="#ffffff" stroke="{DARK}" stroke-width="1.7"/>')
        if naam == "vast":
            for r in range(4):
                for k in range(5):
                    d.append(f'<circle cx="{x+14+k*(bb-28)/4:.1f}" cy="{18+r*19:.1f}" r="5" fill="{FOREST}"/>')
        elif naam == "vloeibaar":
            for r in range(3):
                for k in range(5):
                    dx = random.uniform(-3, 3)
                    d.append(f'<circle cx="{x+14+k*(bb-28)/4+dx:.1f}" cy="{44+r*17+random.uniform(-3,3):.1f}" r="5" fill="{FOREST}"/>')
        else:
            for _ in range(8):
                d.append(f'<circle cx="{x+12+random.uniform(0,bb-24):.1f}" cy="{14+random.uniform(0,bh-16):.1f}" r="5" fill="{FOREST}"/>')
        d.append(f'<text x="{x+bb/2:.1f}" y="{bh+26}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11.5" font-weight="600" fill="{DARK}">{naam}</text>')
        d.append(f'<text x="{x+bb/2:.1f}" y="{bh+40}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{onder}</text>')
    return _svg(breedte, h, "".join(d))


def stroomkring(breedte=380):
    """Een eenvoudige gesloten stroomkring met batterij, lampje en schakelaar."""
    h = 160
    x0, y0, x1, y1 = 40, 34, breedte - 40, 124
    d = [f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="14" fill="none" stroke="{DARK}" stroke-width="2.4"/>']
    # batterij, onderaan
    mx = (x0 + x1) / 2
    d.append(f'<rect x="{mx-28}" y="{y1-9}" width="56" height="18" fill="{PAPER}" stroke="none"/>')
    for i, (dx, hh, dik) in enumerate([(-12, 20, 2.6), (-2, 11, 4.5), (8, 20, 2.6), (18, 11, 4.5)]):
        d.append(f'<line x1="{mx+dx}" y1="{y1-hh/2}" x2="{mx+dx}" y2="{y1+hh/2}" stroke="{DARK}" stroke-width="{dik}"/>')
    d.append(f'<text x="{mx}" y="{y1+30}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">batterij</text>')
    # lampje, bovenaan
    d.append(f'<rect x="{mx-18}" y="{y0-16}" width="36" height="32" fill="{PAPER}" stroke="none"/>')
    d.append(f'<circle cx="{mx}" cy="{y0}" r="14" fill="#fff8e6" stroke="{AMBER}" stroke-width="2.2"/>')
    d.append(f'<path d="M{mx-7} {y0-7} l14 14 M{mx+7} {y0-7} l-14 14" stroke="{AMBER}" stroke-width="1.8"/>')
    d.append(f'<text x="{mx}" y="{y0-24}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">lampje</text>')
    # schakelaar, rechts
    d.append(f'<rect x="{x1-9}" y="{(y0+y1)/2-18}" width="18" height="36" fill="{PAPER}" stroke="none"/>')
    d.append(f'<circle cx="{x1}" cy="{(y0+y1)/2-16}" r="3" fill="{DARK}"/>')
    d.append(f'<circle cx="{x1}" cy="{(y0+y1)/2+16}" r="3" fill="{DARK}"/>')
    d.append(f'<line x1="{x1}" y1="{(y0+y1)/2+16}" x2="{x1+13}" y2="{(y0+y1)/2-12}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>')
    # het label onder de schakelaar, anders valt het buiten de tekening
    d.append(f'<text x="{x1}" y="{(y0+y1)/2+40}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">schakelaar</text>')
    return _svg(breedte, h, "".join(d))


def hefboom(breedte=400):
    """Een hefboom met last, steunpunt en kracht."""
    h = 120
    y = 62
    d = [f'<line x1="30" y1="{y}" x2="{breedte-30}" y2="{y}" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>',
         f'<polygon points="{breedte*0.34},{y+4} {breedte*0.28},{y+34} {breedte*0.40},{y+34}" fill="{DIM}"/>',
         f'<text x="{breedte*0.34}" y="{y+48}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">steunpunt</text>',
         f'<rect x="42" y="{y-34}" width="34" height="30" rx="5" fill="{FOREST}"/>',
         f'<text x="59" y="{y-40}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{FOREST}">last</text>',
         f'<path d="M{breedte-60} {y-34} v26 m0 0 l-5 -6 m5 6 l5 -6" stroke="{AMBER}" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
         f'<text x="{breedte-60}" y="{y-40}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{AMBER}">kracht</text>']
    return _svg(breedte, h, "".join(d))


def plantdelen(breedte=340):
    """Een plant met wortel, stengel, blad en bloem benoemd."""
    h = 210
    mx = breedte * 0.40
    d = [f'<path d="M{mx} 176 V62" stroke="{FOREST}" stroke-width="4" stroke-linecap="round"/>',
         f'<path d="M{mx} 118 q-38 -22 -52 4 q34 20 52 -4" fill="rgba(47,93,80,.18)" stroke="{FOREST}" stroke-width="1.8"/>',
         f'<path d="M{mx} 142 q38 -22 52 4 q-34 20 -52 -4" fill="rgba(47,93,80,.18)" stroke="{FOREST}" stroke-width="1.8"/>']
    for hoek in range(0, 360, 60):
        import math
        a = math.radians(hoek)
        d.append(f'<ellipse cx="{mx+16*math.cos(a):.1f}" cy="{48+16*math.sin(a):.1f}" rx="11" ry="8" '
                 f'transform="rotate({hoek} {mx+16*math.cos(a):.1f} {48+16*math.sin(a):.1f})" fill="#e8b820" stroke="{AMBER}" stroke-width="1.4"/>')
    d.append(f'<circle cx="{mx}" cy="48" r="9" fill="{AMBER}"/>')
    d.append(f'<path d="M{mx} 176 q-26 12 -34 28 M{mx} 176 q26 12 34 28 M{mx} 176 v26" stroke="#7a5230" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    for x, y, naam in [(mx + 34, 48, "bloem"), (mx + 60, 146, "blad"), (mx + 22, 100, "stengel"), (mx + 48, 200, "wortel")]:
        d.append(f'<text x="{x:.0f}" y="{y}" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{DARK}">{naam}</text>')
    return _svg(breedte, h, "".join(d))


def ontwerpcyclus(breedte=380):
    """De cyclus van ontwerpen: probleem, idee, maken, testen, verbeteren."""
    import math
    h = 250
    mx, my, r = breedte / 2, 122, 84
    stappen_ = ["1 probleem", "2 idee", "3 maken", "4 testen", "5 verbeteren"]
    d = []
    for i in range(len(stappen_)):
        a1 = math.radians(i * 72 - 90 + 9)
        a2 = math.radians((i + 1) * 72 - 90 - 9)
        x1, y1 = mx + r * math.cos(a1), my + r * math.sin(a1)
        x2, y2 = mx + r * math.cos(a2), my + r * math.sin(a2)
        d.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{BORDER}" stroke-width="2.4"/>')
        am = math.radians((i + 1) * 72 - 90 - 9)
        d.append(f'<path d="M{x2:.1f} {y2:.1f} l{-7*math.cos(am-0.4):.1f} {-7*math.sin(am-0.4):.1f} M{x2:.1f} {y2:.1f} l{-7*math.cos(am+0.4):.1f} {-7*math.sin(am+0.4):.1f}" stroke="{BORDER}" stroke-width="2.4" stroke-linecap="round"/>')
    for i, naam in enumerate(stappen_):
        a = math.radians(i * 72 - 90)
        x, y = mx + r * math.cos(a), my + r * math.sin(a)
        d.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="30" fill="#ffffff" stroke="{FOREST}" stroke-width="1.9"/>')
        nr, woord = naam.split(" ", 1)
        d.append(f'<text x="{x:.1f}" y="{y-3:.1f}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{nr}</text>')
        d.append(f'<text x="{x:.1f}" y="{y+11:.1f}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" font-weight="600" fill="{DARK}">{woord}</text>')
    return _svg(breedte, h, "".join(d))


def windroos(straal=78):
    """Een windroos met de vier hoofdrichtingen en de vier tussenrichtingen."""
    import math
    m = straal + 26
    d = []
    for hoek, naam in [(-90, "N"), (0, "O"), (90, "Z"), (180, "W")]:
        a = math.radians(hoek)
        x, y = m + straal * math.cos(a), m + straal * math.sin(a)
        d.append(f'<polygon points="{m + 9*math.cos(a+1.57):.1f},{m + 9*math.sin(a+1.57):.1f} '
                 f'{x:.1f},{y:.1f} {m + 9*math.cos(a-1.57):.1f},{m + 9*math.sin(a-1.57):.1f}" '
                 f'fill="{FOREST if naam == "N" else "#ffffff"}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(f'<text x="{m + (straal+15)*math.cos(a):.1f}" y="{m + (straal+15)*math.sin(a)+4:.1f}" '
                 f'text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="14" '
                 f'font-weight="600" fill="{DARK}">{naam}</text>')
    for hoek, naam in [(-45, "NO"), (45, "ZO"), (135, "ZW"), (225, "NW")]:
        a = math.radians(hoek)
        d.append(f'<line x1="{m}" y1="{m}" x2="{m + straal*0.72*math.cos(a):.1f}" y2="{m + straal*0.72*math.sin(a):.1f}" '
                 f'stroke="{BORDER}" stroke-width="1.6"/>')
        d.append(f'<text x="{m + (straal+3)*math.cos(a):.1f}" y="{m + (straal+3)*math.sin(a)+4:.1f}" '
                 f'text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{DIM}">{naam}</text>')
    d.append(f'<circle cx="{m}" cy="{m}" r="5" fill="{DARK}"/>')
    return _svg(m * 2, m * 2, "".join(d))


def schaalbalk(breedte=330):
    """Een schaalbalk zoals op een kaart, met wat ze betekent."""
    h = 74
    bb = breedte - 60
    x0 = 30
    d = []
    for i in range(4):
        kleur = DARK if i % 2 == 0 else "#ffffff"
        d.append(f'<rect x="{x0 + i*bb/4:.1f}" y="18" width="{bb/4:.1f}" height="15" fill="{kleur}" stroke="{DARK}" stroke-width="1.3"/>')
    for i in range(5):
        d.append(f'<text x="{x0 + i*bb/4:.1f}" y="48" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" fill="{DIM}">{i}</text>')
    d.append(f'<text x="{x0 + bb/2:.1f}" y="66" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="11" fill="{DARK}">kilometer</text>')
    d.append(f'<text x="{x0 + bb/2:.1f}" y="12" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{FOREST}">1 cm op de kaart = 1 km in het echt</text>')
    return _svg(breedte, h, "".join(d))


def rasterkaart(breedte=400):
    """Een kaartje met een raster, om coördinaten mee te oefenen."""
    kop = 22
    cel = (breedte - kop - 8) / 4
    h = kop + cel * 4 + 8
    d = [f'<rect x="{kop}" y="{kop}" width="{cel*4:.1f}" height="{cel*4:.1f}" fill="#f4f7f2" stroke="{DARK}" stroke-width="1.6"/>']
    for i in range(1, 4):
        d.append(f'<line x1="{kop + i*cel:.1f}" y1="{kop}" x2="{kop + i*cel:.1f}" y2="{kop + 4*cel:.1f}" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(f'<line x1="{kop}" y1="{kop + i*cel:.1f}" x2="{kop + 4*cel:.1f}" y2="{kop + i*cel:.1f}" stroke="{BORDER}" stroke-width="1.2"/>')
    for i, letter in enumerate("ABCD"):
        d.append(f'<text x="{kop + i*cel + cel/2:.1f}" y="{kop-7}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{DIM}">{letter}</text>')
        d.append(f'<text x="{kop-8}" y="{kop + i*cel + cel/2 + 4:.1f}" text-anchor="end" font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" fill="{DIM}">{i+1}</text>')
    # een rivier, een bos, een kerk en een station
    d.append(f'<path d="M{kop} {kop+cel*1.2:.1f} q{cel} {cel*0.6} {cel*2} 0 q{cel} {-cel*0.6} {cel*2} {cel*0.5}" fill="none" stroke="#3b6ea5" stroke-width="3.4"/>')
    for dx, dy in [(0.35, 2.4), (0.65, 2.7), (0.45, 3.0)]:
        cx, cy = kop + dx * cel, kop + dy * cel
        d.append(f'<polygon points="{cx:.1f},{cy-11:.1f} {cx-9:.1f},{cy+5:.1f} {cx+9:.1f},{cy+5:.1f}" fill="#2f7d4f"/>')
    cx, cy = kop + 2.5 * cel, kop + 2.5 * cel
    d.append(f'<rect x="{cx-7:.1f}" y="{cy-4:.1f}" width="14" height="16" fill="{DARK}"/>')
    d.append(f'<path d="M{cx} {cy-22:.1f} v11 M{cx-5:.1f} {cy-17:.1f} h10" stroke="{DARK}" stroke-width="2.4"/>')
    cx, cy = kop + 3.5 * cel, kop + 3.4 * cel
    d.append(f'<rect x="{cx-14:.1f}" y="{cy-7:.1f}" width="28" height="14" rx="4" fill="{AMBER}"/>')
    d.append(f'<circle cx="{cx-7:.1f}" cy="{cy+8:.1f}" r="3.4" fill="{DARK}"/><circle cx="{cx+7:.1f}" cy="{cy+8:.1f}" r="3.4" fill="{DARK}"/>')
    return _svg(breedte, h, "".join(d))


def tijdlijn(perioden, merken, breedte=470):
    """Een tijdlijn met gekleurde periodes en een paar jaartallen erop.

    perioden = [(naam, van, tot, kleur), ...]
    merken   = [(jaar, label, "boven" of "onder"), ...]

    De naam van een periode past alleen in de balk als die breed genoeg is;
    anders staat hij in het rijtje eronder. Jaartallen kiezen zelf geen kant:
    die geef je mee, zodat twee labels nooit op elkaar vallen.
    """
    m = 26
    y = 74
    links = min(p[1] for p in perioden)
    rechts = max(p[2] for p in perioden)
    span = rechts - links

    def x(v):
        return m + (v - links) / span * (breedte - 2 * m)

    d = []
    buiten = []
    for naam, van, tot, kleur in perioden:
        x0, x1 = x(van), x(tot)
        d.append(f'<rect x="{x0:.1f}" y="{y-13}" width="{x1-x0:.1f}" height="26" fill="{kleur}" stroke="#ffffff" stroke-width="1.5"/>')
        if x1 - x0 >= 7.2 * len(naam):
            d.append(f'<text x="{(x0+x1)/2:.1f}" y="{y+4}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                     f'font-size="9.5" font-weight="600" fill="#ffffff">{naam}</text>')
        else:
            buiten.append((naam, kleur))

    for jaar, label, kant in merken:
        px = x(jaar)
        boven = kant == "boven"
        y2 = y - 22 if boven else y + 22
        d.append(f'<line x1="{px:.1f}" y1="{y - 13 if boven else y + 13}" x2="{px:.1f}" y2="{y2:.0f}" stroke="{DARK}" stroke-width="1.5"/>')
        d.append(f'<circle cx="{px:.1f}" cy="{y2:.0f}" r="3.4" fill="{DARK}"/>')
        anker = "middle"
        if px < 46:
            anker = "start"
        elif px > breedte - 46:
            anker = "end"
        d.append(f'<text x="{px:.1f}" y="{y2 - 9 if boven else y2 + 14:.0f}" text-anchor="{anker}" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="10.5" font-weight="600" fill="{DARK}">{label}</text>')

    h = y + 48
    if buiten:
        bx = m
        for naam, kleur in buiten:
            d.append(f'<rect x="{bx:.1f}" y="{h-8}" width="11" height="11" rx="2.5" fill="{kleur}"/>')
            d.append(f'<text x="{bx+16:.1f}" y="{h+1}" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{DIM}">{naam}</text>')
            bx += 22 + 5.6 * len(naam)
        h += 16
    return _svg(breedte, h, "".join(d))


def eeuwenbalk(breedte=470):
    """Waarom de jaren 1301 tot 1400 samen de 14de eeuw vormen."""
    h = 96
    vak = (breedte - 20) / 3
    d = []
    for i, (van, tot, eeuw) in enumerate([(1201, 1300, "13de eeuw"), (1301, 1400, "14de eeuw"), (1401, 1500, "15de eeuw")]):
        x = 10 + i * vak
        kleur = FOREST if i == 1 else "#ffffff"
        tekst = "#ffffff" if i == 1 else DARK
        d.append(f'<rect x="{x:.1f}" y="20" width="{vak-6:.1f}" height="44" rx="8" fill="{kleur}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(f'<text x="{x + (vak-6)/2:.1f}" y="40" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="12.5" font-weight="600" fill="{tekst}">{eeuw}</text>')
        d.append(f'<text x="{x + (vak-6)/2:.1f}" y="56" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" fill="{tekst}">{van} – {tot}</text>')
    return _svg(breedte, 72, "".join(d))


def hierogliefen(breedte=470):
    """
    Een cartouche met vijf hiërogliefen, met onder elk teken wat het betekent.

    Bewust een tekening en geen foto: de tekens zelf zijn duizenden jaren oud
    en vrij, maar een foto van een tempelmuur is dat niet. Voor een kind leest
    dit bovendien duidelijker dan verweerde steen.
    """
    h = 164
    cy = 58
    x0, x1 = 26, 424
    d = []

    # De cartouche: de ovale omlijsting waarin Egyptenaren een koningsnaam zetten.
    d.append(f'<rect x="{x0}" y="16" width="{x1-x0}" height="84" rx="42" '
             f'fill="{PAPER}" stroke="{DARK}" stroke-width="2.6"/>')
    d.append(f'<rect x="{x1+6}" y="26" width="11" height="64" rx="5" '
             f'fill="{PAPER}" stroke="{DARK}" stroke-width="2.6"/>')

    lijn = dict(stroke=DARK, fill="none")
    vak = (x1 - x0 - 26) / 5
    tekens = []

    for i in range(5):
        cx = x0 + 13 + vak * (i + 0.5)
        tekens.append(cx)
        if i == 0:
            # rietblad: rechte stengel met een spits blad bovenaan
            d.append(f'<path d="M{cx:.1f} {cy+24} V{cy-4}" stroke="{DARK}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
            d.append(f'<path d="M{cx:.1f} {cy-4} C{cx-11:.1f} {cy-12} {cx-9:.1f} {cy-25} {cx:.1f} {cy-30} '
                     f'C{cx+9:.1f} {cy-25} {cx+11:.1f} {cy-12} {cx:.1f} {cy-4} Z" '
                     f'stroke="{DARK}" stroke-width="2.2" fill="none"/>')
        elif i == 1:
            # uil: van voren gezien, met twee ogen en een snavel
            d.append(f'<path d="M{cx:.1f} {cy-28} C{cx+16:.1f} {cy-28} {cx+17:.1f} {cy-4} {cx+12:.1f} {cy+14} '
                     f'L{cx+6:.1f} {cy+26} L{cx-6:.1f} {cy+26} L{cx-12:.1f} {cy+14} '
                     f'C{cx-17:.1f} {cy-4} {cx-16:.1f} {cy-28} {cx:.1f} {cy-28} Z" '
                     f'stroke="{DARK}" stroke-width="2.2" fill="none"/>')
            d.append(f'<circle cx="{cx-6:.1f}" cy="{cy-17}" r="3.2" fill="{DARK}"/>')
            d.append(f'<circle cx="{cx+6:.1f}" cy="{cy-17}" r="3.2" fill="{DARK}"/>')
            d.append(f'<path d="M{cx:.1f} {cy-11} l-3.5 7 h7 z" fill="{DARK}"/>')
        elif i == 2:
            # water: de golvende lijn
            d.append(f'<path d="M{cx-23:.1f} {cy+2} q5.75 -10 11.5 0 t11.5 0 t11.5 0 t11.5 0" '
                     f'stroke="{DARK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
        elif i == 3:
            # mond: een vlakke, puntige ovaal
            d.append(f'<path d="M{cx-22:.1f} {cy} q22 -10 44 0 q-22 10 -44 0 Z" '
                     f'stroke="{DARK}" stroke-width="2.2" fill="none"/>')
        else:
            # oog: dezelfde vorm maar boller, met pupil en wenkbrauw erboven
            d.append(f'<path d="M{cx-22:.1f} {cy+2} q22 -17 44 0 q-22 17 -44 0 Z" '
                     f'stroke="{DARK}" stroke-width="2.2" fill="none"/>')
            d.append(f'<circle cx="{cx:.1f}" cy="{cy+2}" r="5.5" fill="{DARK}"/>')
            d.append(f'<path d="M{cx-21:.1f} {cy-11} q21 -12 42 -3" '
                     f'stroke="{DARK}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')

    uitleg = [("i", "rietblad"), ("m", "uil"), ("n", "water"), ("r", "mond"), ("oog", "oog van Horus")]
    for cx, (boven, onder) in zip(tekens, uitleg):
        d.append(f'<text x="{cx:.1f}" y="126" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="15" font-weight="600" fill="{AMBER}">{boven}</text>')
        d.append(f'<text x="{cx:.1f}" y="144" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" fill="{DIM}">{onder}</text>')

    return _svg(breedte, h, "".join(d))


def _veelhoek(cx, cy, punten, stijl):
    """Een gesloten vorm uit losse punten, geplaatst rond (cx, cy)."""
    pad = " ".join(f"{cx+x:.1f},{cy+y}" for x, y in punten)
    return f'<polygon points="{pad}" {stijl}/>'


def stenen_werktuigen(breedte=470):
    """
    Vier werktuigen uit de steentijd, met eronder waarvan ze gemaakt zijn.

    Net als bij de hiërogliefen een tekening en geen foto: zo staat er niets
    in de bundel waarvan de herkomst onduidelijk is. De afgeschilferde randjes
    zijn met opzet getekend, want daaraan herken je bewerkte vuursteen.
    """
    h = 148
    cy = 62
    d = []
    vak = (breedte - 40) / 4
    lijn = f'stroke="{DARK}" stroke-width="2" fill="none"'
    dun = f'stroke="{DIM}" stroke-width="1.1" fill="none" stroke-linecap="round"'

    for i in range(4):
        cx = 20 + vak * (i + 0.5)

        if i == 0:
            # vuistbijl: een onregelmatige amandelvorm, want bewerkte steen
            # heeft rechte afslagvlakjes en geen vloeiende ronding
            punten = [(0, -34), (9, -27), (17, -15), (22, -1), (23, 11), (18, 21),
                      (10, 28), (0, 31), (-10, 28), (-18, 21), (-23, 11), (-22, -1),
                      (-17, -15), (-9, -27)]
            d.append(_veelhoek(cx, cy, punten, lijn))
            for a, b, c2, e in [(18, -10, 6, -4), (21, 4, 8, 6), (15, 19, 5, 14),
                                (-18, -8, -6, -3), (-21, 5, -8, 7), (-15, 19, -5, 14),
                                (5, -27, 2, -16), (-6, -25, -2, -15)]:
                d.append(f'<path d="M{cx+a:.1f} {cy+b} L{cx+c2:.1f} {cy+e}" {dun}/>')

        elif i == 1:
            # pijlpunt met weerhaken en een steeltje om in te binden
            punten = [(0, -34), (14, 4), (9, 16), (4, 10), (4, 28), (-4, 28),
                      (-4, 10), (-9, 16), (-14, 4)]
            d.append(_veelhoek(cx, cy, punten, lijn))
            d.append(f'<path d="M{cx:.1f} {cy-28} V{cy+6}" {dun}/>')
            for a, b, c2, e in [(7, -18, 2, -16), (10, -7, 4, -6), (13, 2, 5, 3),
                                (-7, -18, -2, -16), (-10, -7, -4, -6), (-13, 2, -5, 3)]:
                d.append(f'<path d="M{cx+a:.1f} {cy+b} L{cx+c2:.1f} {cy+e}" {dun}/>')

        elif i == 2:
            # mes: rechte rug links, scherpe snede rechts
            punten = [(-11, -32), (-4, -29), (2, -17), (7, -3), (8, 9), (5, 21),
                      (1, 30), (-11, 30)]
            d.append(_veelhoek(cx, cy, punten, lijn))
            d.append(f'<path d="M{cx-8:.1f} {cy-26} L{cx-6:.1f} {cy+26}" {dun}/>')
            for a, b, c2, e in [(7, -18, 0, -16), (8, -5, 1, -4), (7, 7, 0, 8), (4, 19, -2, 19)]:
                d.append(f'<path d="M{cx+a:.1f} {cy+b} L{cx+c2:.1f} {cy+e}" {dun}/>')

        else:
            # bijl: een stenen kop, met touw op een houten steel gebonden
            d.append(f'<path d="M{cx-4:.1f} {cy-18} h8 v46 a4 4 0 0 1 -8 0 Z" {lijn}/>')
            d.append(f'<path d="M{cx-22:.1f} {cy-26} L{cx+18:.1f} {cy-34} L{cx+23:.1f} {cy-16} '
                     f'L{cx-19:.1f} {cy-9} Z" {lijn}/>')
            for y in (-20, -14):
                d.append(f'<path d="M{cx-7:.1f} {cy+y} L{cx+7:.1f} {cy+y-2}" {dun}/>')
            d.append(f'<path d="M{cx+18:.1f} {cy-31} L{cx+21:.1f} {cy-18}" {dun}/>')

    namen = [("vuistbijl", "steen"), ("pijlpunt", "vuursteen"),
             ("mes", "vuursteen"), ("bijl", "steen en hout")]
    for i, (naam, stof) in enumerate(namen):
        cx = 20 + vak * (i + 0.5)
        d.append(f'<text x="{cx:.1f}" y="118" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="12.5" font-weight="600" fill="{AMBER}">{naam}</text>')
        d.append(f'<text x="{cx:.1f}" y="134" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10" fill="{DIM}">{stof}</text>')

    return _svg(breedte, h, "".join(d))


# Aardetinten voor de tekeningen bij geschiedenis: oker, roodbruin, steen.
OKER = "#c17f2b"
ROOD = "#a2521f"
STEEN = "#d9cfb8"
WAND = "#ece2cf"


def grotschildering(breedte=470):
    """
    Een rotswand met dieren in oker en roodbruin, en een handafdruk.

    Nagetekend in de stijl van de grotschilderingen, niet overgenomen van een
    foto: de schilderingen zelf zijn vijftienduizend jaar oud en vrij, maar een
    foto van een grotwand is dat niet.
    """
    h = 196
    d = []

    d.append(f'<path d="M8 16 C48 6 96 12 146 9 C212 5 278 13 338 8 C398 3 446 12 462 20 '
             f'L459 172 C416 184 348 176 288 180 C218 184 148 178 88 182 C48 185 18 178 9 170 Z" '
             f'fill="{WAND}" stroke="{BORDER}" stroke-width="2"/>')

    # Allebei de dieren zijn één gesloten silhouet, poten inbegrepen. Zo kan
    # een kop niet losraken van zijn lichaam, en zo zien die schilderingen er
    # ook uit: gevulde vlakken, geen lijntekeningen.

    # oerrund, naar rechts gekeerd
    d.append(f'<path d="M66 72 C78 62 100 56 128 52 C146 50 158 50 190 44 '
             f'L222 54 L214 68 L192 74 L178 84 '
             f'L174 86 L172 128 L164 128 L163 88 L150 92 '
             f'L146 92 L144 130 L137 130 L136 92 L110 96 '
             f'L106 96 L104 130 L97 130 L96 94 L86 92 '
             f'L82 92 L80 128 L73 128 L72 88 L64 82 Z" fill="{OKER}"/>')
    for pad in ["M190 44 C197 30 215 24 227 31", "M183 47 C186 33 202 24 214 27"]:
        d.append(f'<path d="{pad}" stroke="{DARK}" stroke-width="3.6" fill="none" stroke-linecap="round"/>')
    d.append(f'<path d="M180 48 l-11 -7 l3 12 Z" fill="{DARK}"/>')
    d.append(f'<circle cx="204" cy="56" r="2.6" fill="{WAND}"/>')
    d.append(f'<path d="M66 74 C54 78 48 92 54 104" stroke="{OKER}" stroke-width="4" fill="none" stroke-linecap="round"/>')

    # paard, naar links gekeerd
    d.append(f'<path d="M398 102 C386 95 366 91 340 93 C324 94 314 96 306 98 '
             f'C296 99 286 104 282 113 C280 119 292 120 306 122 '
             f'L310 124 L312 160 L305 160 L303 124 C312 130 318 132 326 132 '
             f'L330 132 L332 162 L325 162 L322 132 C334 136 342 136 352 134 '
             f'L356 136 L360 160 L353 160 L350 134 C360 133 366 131 374 128 '
             f'L378 128 L384 158 L377 158 L372 126 C382 124 390 121 396 118 Z" fill="{ROOD}"/>')
    d.append(f'<path d="M350 90 C334 88 318 91 305 97" stroke="{DARK}" stroke-width="4.2" fill="none" stroke-linecap="round"/>')
    d.append(f'<circle cx="297" cy="107" r="2.4" fill="{WAND}"/>')
    d.append(f'<path d="M400 104 C413 107 417 122 409 133" stroke="{ROOD}" stroke-width="3.6" fill="none" stroke-linecap="round"/>')

    # rij stippen, zoals de tekens die naast de dieren staan
    for i in range(7):
        d.append(f'<circle cx="{72 + i*17}" cy="166" r="3.6" fill="{ROOD}"/>')

    # handafdruk: de hand lag op de wand, er werd verf omheen geblazen
    hx, hy = 228, 108
    d.append(f'<ellipse cx="{hx}" cy="{hy}" rx="25" ry="27" fill="{ROOD}" opacity="0.8"/>')
    d.append(f'<ellipse cx="{hx}" cy="{hy+7}" rx="9.5" ry="11.5" fill="{WAND}"/>')
    for hoek in (-46, -22, 2, 24):
        d.append(f'<g transform="rotate({hoek} {hx} {hy+7})">'
                 f'<rect x="{hx-3}" y="{hy-16}" width="6" height="17" rx="3" fill="{WAND}"/></g>')
    d.append(f'<g transform="rotate(-74 {hx} {hy+9})">'
             f'<rect x="{hx-3.5}" y="{hy-7}" width="7" height="15" rx="3.5" fill="{WAND}"/></g>')

    return _svg(breedte, h, "".join(d))


def piramides(breedte=470):
    """De drie piramides van Gizeh met de sfinx, en een mens voor de schaal."""
    h = 176
    grond = 142
    d = []
    d.append(f'<path d="M0 {grond} H{breedte}" stroke="{DIM}" stroke-width="1.4"/>')

    for top_x, top_y, half in [(150, 26, 92), (262, 52, 74), (352, 84, 46)]:
        d.append(f'<path d="M{top_x} {top_y} L{top_x+half} {grond} L{top_x-half} {grond} Z" '
                 f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.8"/>')
        # de ribbe die naar ons toe wijst, zodat je ziet dat het een lichaam is
        d.append(f'<path d="M{top_x} {top_y} L{top_x - half*0.32:.0f} {grond}" '
                 f'stroke="{DARK}" stroke-width="1.4" fill="none"/>')

    # sfinx: liggend lijf met de poten naar voren, kop met hoofddoek
    d.append(f'<path d="M378 {grond} V124 C378 119 383 116 390 116 L416 116 L418 92 L426 86 '
             f'L442 86 L450 92 L448 116 L452 121 L458 133 L458 {grond} Z" '
             f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.8"/>')
    d.append(f'<path d="M421 102 H447" stroke="{DARK}" stroke-width="1.2"/>')
    d.append(f'<path d="M438 {grond} V133 M448 {grond} V134" stroke="{DARK}" stroke-width="1.2"/>')

    # mens, om te tonen hoe groot die dingen zijn
    d.append(f'<circle cx="58" cy="{grond-22}" r="4" fill="{DARK}"/>')
    d.append(f'<path d="M58 {grond-18} V{grond-8} M58 {grond-15} L52 {grond-11} M58 {grond-15} L64 {grond-11} '
             f'M58 {grond-8} L53 {grond} M58 {grond-8} L63 {grond}" '
             f'stroke="{DARK}" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
    d.append(f'<text x="58" y="{grond+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10" fill="{DIM}">een mens</text>')
    d.append(f'<text x="150" y="{grond+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="11" font-weight="600" fill="{AMBER}">147 m hoog</text>')
    d.append(f'<text x="428" y="{grond+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10" fill="{DIM}">de sfinx</text>')
    return _svg(breedte, h, "".join(d))


def griekse_tempel(breedte=470):
    """Het Parthenon: een tempel op zuilen, met de delen benoemd."""
    h = 190
    d = []
    links, rechts = 100, 404
    vloer = 150

    # drie treden
    for i, inspring in enumerate([0, 7, 14]):
        y = vloer - i * 7
        d.append(f'<rect x="{links-18+inspring}" y="{y}" width="{rechts-links+36-2*inspring}" height="7" '
                 f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.4"/>')

    kap = vloer - 21
    # acht zuilen
    n = 8
    ruimte = (rechts - links) / (n - 1)
    for i in range(n):
        x = links + i * ruimte
        d.append(f'<rect x="{x-8:.1f}" y="{kap-72}" width="16" height="72" fill="{STEEN}" stroke="{DARK}" stroke-width="1.4"/>')
        for g in range(1, 4):
            d.append(f'<path d="M{x-8+g*4:.1f} {kap-68} V{kap-4}" stroke="{DIM}" stroke-width="0.8"/>')
        d.append(f'<rect x="{x-11:.1f}" y="{kap-79}" width="22" height="7" fill="{STEEN}" stroke="{DARK}" stroke-width="1.4"/>')

    balk = kap - 79
    d.append(f'<rect x="{links-22}" y="{balk-16}" width="{rechts-links+44}" height="16" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')
    d.append(f'<path d="M{links-28} {balk-16} L{(links+rechts)/2:.0f} {balk-58} L{rechts+28} {balk-16} Z" '
             f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.8"/>')

    for x, y, tekst, anker in [(60, balk-42, "fronton", "end"), (60, kap-40, "zuil", "end")]:
        d.append(f'<text x="{x}" y="{y}" text-anchor="{anker}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="11" font-weight="600" fill="{AMBER}">{tekst}</text>')
    d.append(f'<path d="M64 {balk-46} L{links-16} {balk-30}" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    d.append(f'<path d="M64 {kap-44} L{links-11} {kap-40}" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    return _svg(breedte, h, "".join(d))


def amfitheater(breedte=470):
    """Het Colosseum: drie rijen bogen onder elkaar, rechtsboven afgebrokkeld."""
    h = 190
    d = []
    grond = 158
    links, rechts = 30, 440
    d.append(f'<path d="M0 {grond} H{breedte}" stroke="{DIM}" stroke-width="1.4"/>')

    n = 11
    breed = (rechts - links) / n
    for laag, (y, hh) in enumerate([(grond - 38, 38), (grond - 76, 38), (grond - 112, 36)]):
        for i in range(n):
            x = links + i * breed
            d.append(f'<rect x="{x:.1f}" y="{y}" width="{breed:.1f}" height="{hh}" '
                     f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.3"/>')
            bx = x + breed / 2
            r = 11
            d.append(f'<path d="M{bx-r} {y+hh-3} V{y+15} a{r} {r} 0 0 1 {2*r} 0 V{y+hh-3} Z" '
                     f'fill="{PAPER}" stroke="{DARK}" stroke-width="1.3"/>')

    # de bovenste muur staat nog maar voor een deel overeind, met een
    # gerafelde breuk: zo herken je een ruïne en niet een flatgebouw
    top = grond - 112
    muur = f"M{links} {top} H{links + breed*6.6:.0f} "
    brokken = [(0, -26), (9, -22), (16, -28), (26, -18), (34, -25), (42, -12), (52, -19), (60, -6)]
    for dx, dy in brokken:
        muur += f"L{links + breed*6.6 + dx:.0f} {top - 30 + (dy + 30) - 30:.0f} "
    muur += f"L{links + breed*6.6 + 60:.0f} {top} Z"
    d.append(f'<path d="M{links} {top} H{links + breed*6.6:.0f} L{links + breed*6.6 + 6:.0f} {top-24} '
             f'L{links + breed*6.6 + 14:.0f} {top-30} L{links + breed*6.6 + 24:.0f} {top-19} '
             f'L{links + breed*6.6 + 33:.0f} {top-27} L{links + breed*6.6 + 43:.0f} {top-14} '
             f'L{links + breed*6.6 + 52:.0f} {top-20} L{links + breed*6.6 + 60:.0f} {top-8} '
             f'L{links + breed*6.6 + 66:.0f} {top} Z" fill="{STEEN}" stroke="{DARK}" stroke-width="1.3"/>')
    d.append(f'<rect x="{links}" y="{top-30}" width="{breed*6.6:.0f}" height="30" '
             f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.3"/>')
    for i in range(6):
        d.append(f'<rect x="{links + i*breed + breed/2 - 5:.1f}" y="{top-22}" width="10" height="13" '
                 f'fill="{PAPER}" stroke="{DARK}" stroke-width="1.1"/>')
    return _svg(breedte, h, "".join(d))


def aquaduct(breedte=470):
    """Een aquaduct: bogen op bogen, met bovenaan de goot waarin het water liep."""
    h = 200
    d = []
    grond = 172
    d.append(f'<path d="M0 {grond} H{breedte}" stroke="{DIM}" stroke-width="1.4"/>')

    # onderste rij: brede, hoge bogen
    onder_y, onder_h = grond - 76, 76
    n1 = 5
    b1 = (breedte - 60) / n1
    for i in range(n1):
        x = 30 + i * b1
        d.append(f'<rect x="{x:.1f}" y="{onder_y}" width="{b1:.1f}" height="{onder_h}" fill="{STEEN}" stroke="{DARK}" stroke-width="1.5"/>')
        bx = x + b1 / 2
        r = b1 / 2 - 11
        d.append(f'<path d="M{bx-r:.1f} {grond} V{onder_y+30} a{r:.1f} {r:.1f} 0 0 1 {2*r:.1f} 0 V{grond} Z" '
                 f'fill="{PAPER}" stroke="{DARK}" stroke-width="1.5"/>')

    # bovenste rij: dubbel zoveel, kleinere bogen
    boven_y, boven_h = onder_y - 52, 52
    n2 = 10
    b2 = (breedte - 60) / n2
    for i in range(n2):
        x = 30 + i * b2
        d.append(f'<rect x="{x:.1f}" y="{boven_y}" width="{b2:.1f}" height="{boven_h}" fill="{STEEN}" stroke="{DARK}" stroke-width="1.3"/>')
        bx = x + b2 / 2
        r = b2 / 2 - 6
        d.append(f'<path d="M{bx-r:.1f} {onder_y} V{boven_y+20} a{r:.1f} {r:.1f} 0 0 1 {2*r:.1f} 0 V{onder_y} Z" '
                 f'fill="{PAPER}" stroke="{DARK}" stroke-width="1.3"/>')

    # de goot bovenop, links opengewerkt zodat je het water ziet
    goot_y = boven_y - 20
    d.append(f'<rect x="30" y="{goot_y}" width="{breedte-60}" height="20" fill="{STEEN}" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(f'<rect x="30" y="{goot_y+5}" width="120" height="15" fill="{PAPER}" stroke="{DARK}" stroke-width="1.3"/>')
    d.append(f'<rect x="32" y="{goot_y+12}" width="116" height="7" fill="#9dc3d8"/>')
    d.append(f'<text x="160" y="{goot_y-6}" font-family="IBM Plex Sans,sans-serif" font-size="11" '
             f'font-weight="600" fill="{AMBER}">hier liep het water</text>')
    d.append(f'<path d="M156 {goot_y-10} L120 {goot_y+8}" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    return _svg(breedte, h, "".join(d))


def heirbaan(breedte=470):
    """Doorsnede van een Romeinse weg: vier lagen, met de namen ernaast."""
    h = 196
    d = []
    mid = 158
    top = 52
    d.append(f'<text x="{mid}" y="30" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" fill="{DIM}">Een doorsnede, alsof je de weg middendoor zaagt.</text>')

    lagen = [(top, 18, "kasseien"), (top + 18, 24, "zand en grind"),
             (top + 42, 28, "gebroken steen met kalk"), (top + 70, 32, "grote platte stenen")]
    halve = [124, 118, 112, 106]

    for i, (y, hh, naam) in enumerate(lagen):
        hb = halve[i]
        if i == 0:
            # de bovenkant is bol, zodat het regenwater naar de kant loopt
            d.append(f'<path d="M{mid-hb} {y+7} Q{mid} {y-6} {mid+hb} {y+7} V{y+hh} H{mid-hb} Z" '
                     f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.5"/>')
        else:
            d.append(f'<rect x="{mid-hb}" y="{y}" width="{2*hb}" height="{hh}" '
                     f'fill="{STEEN if i % 2 == 0 else WAND}" stroke="{DARK}" stroke-width="1.5"/>')
        ly = y + hh / 2 + (3 if i == 0 else 0)
        d.append(f'<path d="M{mid+hb} {ly:.0f} H{mid+hb+14}" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
        d.append(f'<text x="{mid+hb+19}" y="{ly+4:.0f}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" font-weight="600" fill="{AMBER}">{naam}</text>')

    # kasseien, meegebogen met de bolle bovenkant
    for i in range(11):
        x = mid - 118 + i * 21.5
        zak = ((x - mid) / 124) ** 2 * 13
        d.append(f'<rect x="{x:.0f}" y="{top+1+zak:.0f}" width="18" height="12" rx="2.5" '
                 f'fill="{WAND}" stroke="{DARK}" stroke-width="1"/>')
    for i in range(20):
        d.append(f'<circle cx="{mid-110 + (i*11) % 220}" cy="{top+24 + (i*7) % 14}" r="2.2" fill="{DIM}" opacity="0.5"/>')
    for i in range(9):
        d.append(f'<path d="M{mid-100 + i*24} {top+78} l10 -6 l11 5 l-9 8 Z" fill="{DIM}" opacity="0.35"/>')

    d.append(f'<path d="M{mid-132} {top+102} H{mid+132}" stroke="{DIM}" stroke-width="1.4"/>')
    d.append(f'<text x="{mid-132}" y="{top+116}" font-family="IBM Plex Sans,sans-serif" font-size="9.5" '
             f'fill="{DIM}">de vaste grond eronder</text>')
    return _svg(breedte, h, "".join(d))


WATER = "#9dc3d8"


def burcht(breedte=470):
    """Een middeleeuwse burcht: gracht, muur met kantelen, torens en een donjon."""
    h = 204
    d = []
    grond, waterboven, wateronder = 168, 168, 192

    # donjon, achter de muur: de woontoren waar de heer zelf zat
    d.append(f'<rect x="270" y="56" width="58" height="112" fill="{WAND}" stroke="{DARK}" stroke-width="1.6"/>')
    d.append(f'<path d="M264 56 L299 28 L334 56 Z" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')
    d.append(f'<path d="M299 28 V14 L322 20 L299 26" fill="{ROOD}" stroke="{DARK}" stroke-width="1.3"/>')
    for x in (284, 308):
        d.append(f'<path d="M{x} 96 v-14 a5 5 0 0 1 10 0 v14 Z" fill="{DARK}"/>')

    # ringmuur met kantelen
    d.append(f'<rect x="96" y="104" width="278" height="{grond-104}" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')
    for i in range(14):
        d.append(f'<rect x="{100 + i*20}" y="96" width="12" height="9" fill="{STEEN}" stroke="{DARK}" stroke-width="1.2"/>')

    # twee ronde torens met een spits dak
    for tx in (78, 356):
        d.append(f'<rect x="{tx}" y="82" width="40" height="{grond-82}" fill="{WAND}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(f'<path d="M{tx-7} 82 L{tx+20} 44 L{tx+47} 82 Z" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(f'<path d="M{tx+15} 124 v-15 a5 5 0 0 1 10 0 v15 Z" fill="{DARK}"/>')

    # poortgebouw met de doorgang
    d.append(f'<rect x="198" y="88" width="74" height="{grond-88}" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')
    for i in range(4):
        d.append(f'<rect x="{201 + i*19}" y="80" width="12" height="9" fill="{STEEN}" stroke="{DARK}" stroke-width="1.2"/>')
    d.append(f'<path d="M218 {grond} V132 a17 17 0 0 1 34 0 V{grond} Z" fill="{DARK}"/>')

    # gracht
    d.append(f'<rect x="0" y="{waterboven}" width="{breedte}" height="{wateronder-waterboven}" fill="{WATER}"/>')
    for i in range(9):
        d.append(f'<path d="M{18 + i*50} 180 q9 -5 18 0" stroke="#ffffff" stroke-width="1.4" fill="none" opacity="0.75"/>')

    # brug over de gracht
    d.append(f'<rect x="218" y="{waterboven-4}" width="34" height="{wateronder-waterboven+8}" '
             f'fill="{WAND}" stroke="{DARK}" stroke-width="1.5"/>')
    for y in (172, 180, 188):
        d.append(f'<path d="M218 {y} H252" stroke="{DIM}" stroke-width="1"/>')

    for x, y, tekst, anker in [(72, 70, "toren", "end"), (398, 92, "kantelen", "start"), (398, 202, "gracht", "end")]:
        d.append(f'<text x="{x}" y="{y}" text-anchor="{anker}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" font-weight="600" fill="{AMBER}">{tekst}</text>')
    d.append(f'<path d="M76 66 L92 60" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    d.append(f'<path d="M394 88 L342 94" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    d.append(f'<path d="M404 198 L414 186" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    return _svg(breedte, h, "".join(d))


def verlucht_handschrift(breedte=470):
    """Een opengeslagen handschrift: een versierde beginletter en regels met de hand."""
    h = 210
    d = []
    boven, onder = 20, 186
    links, rechts = 30, 440
    mid = (links + rechts) / 2

    d.append(f'<path d="M{links} {boven+8} C{mid-40} {boven-4} {mid-10} {boven+2} {mid} {boven+10} '
             f'C{mid+10} {boven+2} {mid+40} {boven-4} {rechts} {boven+8} '
             f'L{rechts} {onder-6} C{mid+40} {onder-16} {mid+10} {onder-10} {mid} {onder-2} '
             f'C{mid-10} {onder-10} {mid-40} {onder-16} {links} {onder-6} Z" '
             f'fill="{PAPER}" stroke="{DARK}" stroke-width="1.8"/>')
    d.append(f'<path d="M{mid} {boven+10} V{onder-2}" stroke="{BORDER}" stroke-width="1.6"/>')

    # versierde beginletter linksboven
    d.append(f'<rect x="{links+16}" y="{boven+22}" width="46" height="46" fill="{OKER}" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<path d="M{links+28} {boven+32} h14 a13 13 0 0 1 0 26 h-14 Z" fill="{PAPER}" stroke="{DARK}" stroke-width="2"/>')

    # geschreven regels: korte streepjes, met hier en daar een rode regel
    def regels(x0, x1, y0, n, inspring_eerste=0):
        for r in range(n):
            y = y0 + r * 12
            begin = x0 + (inspring_eerste if r < 4 else 0)
            kleur = ROOD if r in (0, 7) else INK
            eind = x1 - (26 if r == n - 1 else 0)
            d.append(f'<path d="M{begin} {y} H{eind}" stroke="{kleur}" stroke-width="2.4" '
                     f'stroke-linecap="round" opacity="{0.9 if kleur == ROOD else 0.55}"/>')

    regels(links + 16, mid - 22, boven + 80, 7)
    regels(mid + 20, rechts - 18, boven + 30, 12)

    # rank in de marge
    d.append(f'<path d="M{links+10} {boven+24} C{links+2} {boven+60} {links+18} {boven+96} {links+8} {onder-24}" '
             f'stroke="{FOREST}" stroke-width="1.6" fill="none"/>')
    for y in (boven + 44, boven + 72, boven + 106, boven + 134):
        d.append(f'<path d="M{links+9} {y} q10 -6 14 2 q-11 5 -14 -2 Z" fill="{FOREST}" opacity="0.7"/>')
        d.append(f'<circle cx="{links+16}" cy="{y+9}" r="2.6" fill="{ROOD}"/>')

    d.append(f'<text x="{links+39}" y="{onder+18}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">de beginletter</text>')
    d.append(f'<text x="{rechts-80}" y="{onder+18}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10" fill="{DIM}">elke regel met de hand overgeschreven</text>')
    return _svg(breedte, h, "".join(d))


def drukpers(breedte=470):
    """De drukpers met losse letters: schroef, pers en het vel papier."""
    h = 212
    d = []
    grond = 186
    d.append(f'<path d="M0 {grond} H{breedte}" stroke="{DIM}" stroke-width="1.4"/>')

    # houten raamwerk
    for x in (132, 252):
        d.append(f'<rect x="{x}" y="34" width="18" height="{grond-34}" fill="{WAND}" stroke="{DARK}" stroke-width="1.6"/>')
    d.append(f'<rect x="124" y="34" width="134" height="20" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')
    d.append(f'<rect x="124" y="{grond-18}" width="134" height="18" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')

    # de schroef, die de pers naar beneden duwt
    d.append(f'<rect x="185" y="54" width="12" height="46" fill="{STEEN}" stroke="{DARK}" stroke-width="1.4"/>')
    for i in range(6):
        d.append(f'<path d="M185 {58 + i*7} l12 -5" stroke="{DARK}" stroke-width="1.2" fill="none"/>')
    # hefboom om aan te draaien
    d.append(f'<path d="M191 62 H300" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>')
    d.append(f'<circle cx="306" cy="62" r="7" fill="{WAND}" stroke="{DARK}" stroke-width="1.6"/>')

    # de pers zelf: het vlakke blok dat op het papier drukt
    d.append(f'<rect x="150" y="100" width="82" height="16" fill="{STEEN}" stroke="{DARK}" stroke-width="1.6"/>')

    # de bak met de letters, die onder de pers wordt geschoven
    d.append(f'<rect x="152" y="140" width="88" height="14" fill="{DARK}"/>')
    d.append(f'<rect x="156" y="126" width="92" height="14" fill="{PAPER}" stroke="{DARK}" stroke-width="1.4"/>')
    for i in range(7):
        d.append(f'<path d="M{164 + i*12} 130 v6" stroke="{DIM}" stroke-width="1.6"/>')

    for x, y, tekst, anker, lx, ly, lx2, ly2 in [
        (120, 66, "schroef", "end", 124, 62, 182, 68),
        (120, 112, "de pers", "end", 124, 108, 146, 108),
        (300, 130, "vel papier", "start", 296, 126, 250, 132),
        (300, 152, "losse letters", "start", 296, 149, 244, 147),
    ]:
        d.append(f'<text x="{x}" y="{y}" text-anchor="{anker}" font-family="IBM Plex Sans,sans-serif" '
                 f'font-size="10.5" font-weight="600" fill="{AMBER}">{tekst}</text>')
        d.append(f'<path d="M{lx} {ly} L{lx2} {ly2}" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')
    return _svg(breedte, h, "".join(d))


def stoommachine(breedte=470):
    """Van vuur naar draaiend wiel: ketel, stoom, zuiger en vliegwiel."""
    h = 210
    d = []
    grond = 176
    d.append(f'<path d="M0 {grond} H{breedte}" stroke="{DIM}" stroke-width="1.4"/>')

    # ketel met vuur eronder
    d.append(f'<rect x="24" y="96" width="104" height="52" rx="14" fill="{STEEN}" stroke="{DARK}" stroke-width="1.8"/>')
    d.append(f'<rect x="40" y="148" width="72" height="{grond-148}" fill="{WAND}" stroke="{DARK}" stroke-width="1.4"/>')
    for i in range(4):
        x = 52 + i * 16
        d.append(f'<path d="M{x} {grond-4} c-5 -8 2 -10 1 -16 c6 5 9 10 8 16 Z" fill="{AMBER}"/>')
    d.append(f'<text x="76" y="{grond+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">vuur</text>')

    # stoomleiding naar de cilinder
    d.append(f'<path d="M128 112 H176" stroke="{DARK}" stroke-width="6" fill="none"/>')
    for i in range(3):
        d.append(f'<circle cx="{140 + i*14}" cy="{100 - i*5}" r="{5 + i}" fill="none" stroke="{DIM}" stroke-width="1.3"/>')
    d.append(f'<text x="152" y="80" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">stoom</text>')

    # cilinder met zuiger
    d.append(f'<rect x="176" y="86" width="42" height="80" fill="{WAND}" stroke="{DARK}" stroke-width="1.8"/>')
    d.append(f'<rect x="181" y="120" width="32" height="12" fill="{DARK}"/>')
    d.append(f'<path d="M197 120 V56" stroke="{DARK}" stroke-width="4"/>')
    d.append(f'<text x="197" y="{grond+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">zuiger</text>')

    # balans: de wip die de op-en-neerbeweging doorgeeft
    d.append(f'<path d="M197 56 L356 44" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>')
    # drijfstang naar het vliegwiel
    d.append(f'<path d="M356 44 L380 108" stroke="{DARK}" stroke-width="4" stroke-linecap="round"/>')

    # vliegwiel
    cx, cy, r = 388, 128, 44
    d.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{DARK}" stroke-width="6"/>')
    d.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{DARK}"/>')
    for hoek in range(0, 360, 45):
        d.append(f'<g transform="rotate({hoek} {cx} {cy})"><path d="M{cx} {cy} V{cy-r+4}" '
                 f'stroke="{DARK}" stroke-width="2.2"/></g>')
    d.append(f'<text x="{cx}" y="{grond+16}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">vliegwiel</text>')
    return _svg(breedte, h, "".join(d))


def mijnschacht(breedte=470):
    """Een schachtbok boven de grond, en eronder de schacht tot in de steenkool."""
    h = 228
    d = []
    maaiveld = 116
    d.append(f'<rect x="0" y="{maaiveld}" width="{breedte}" height="{h-maaiveld}" fill="{WAND}"/>')
    d.append(f'<path d="M0 {maaiveld} H{breedte}" stroke="{DARK}" stroke-width="1.8"/>')

    # de bok: twee schuine poten en een rechte toren
    for x0, x1 in [(96, 148), (236, 184)]:
        d.append(f'<path d="M{x0} {maaiveld} L{x1} 36" stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>')
    d.append(f'<rect x="148" y="30" width="36" height="{maaiveld-30}" fill="none" stroke="{DARK}" stroke-width="3"/>')
    for i in range(5):
        y = 38 + i * 16
        d.append(f'<path d="M148 {y} L184 {y+16} M184 {y} L148 {y+16}" stroke="{DARK}" stroke-width="1.2"/>')
    for i in range(4):
        d.append(f'<path d="M{100 + i*10} {maaiveld - i*18} L{236 - i*13} {maaiveld - i*18}" '
                 f'stroke="{DIM}" stroke-width="1.1"/>')

    # de twee wielen waarmee de kooi op en neer gaat
    for cx in (152, 180):
        d.append(f'<circle cx="{cx}" cy="26" r="17" fill="none" stroke="{DARK}" stroke-width="3.4"/>')
        d.append(f'<circle cx="{cx}" cy="26" r="3" fill="{DARK}"/>')
    d.append(f'<text x="214" y="22" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">de wielen draaien de kabel op</text>')
    d.append(f'<path d="M210 19 L196 24" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')

    # gebouw aan de voet
    d.append(f'<rect x="248" y="78" width="96" height="{maaiveld-78}" fill="{STEEN}" stroke="{DARK}" stroke-width="1.5"/>')
    for i in range(4):
        d.append(f'<rect x="{258 + i*22}" y="90" width="12" height="14" fill="{PAPER}" stroke="{DARK}" stroke-width="1"/>')

    # de schacht, recht naar beneden
    d.append(f'<rect x="152" y="{maaiveld}" width="28" height="86" fill="{PAPER}" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(f'<path d="M166 {maaiveld} V150" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<rect x="156" y="150" width="20" height="22" fill="{STEEN}" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(f'<text x="196" y="164" font-family="IBM Plex Sans,sans-serif" font-size="10.5" '
             f'font-weight="600" fill="{AMBER}">de kooi met de mijnwerkers</text>')
    d.append(f'<path d="M192 160 L180 160" stroke="{AMBER}" stroke-width="1.2" fill="none"/>')

    # gang naar de steenkoollaag
    d.append(f'<rect x="180" y="192" width="176" height="18" fill="{PAPER}" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(f'<path d="M166 172 V201 H180" stroke="{DARK}" stroke-width="1.5" fill="none"/>')
    d.append(f'<rect x="0" y="210" width="{breedte}" height="18" fill="{DARK}"/>')
    d.append(f'<text x="{breedte-10}" y="206" text-anchor="end" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10.5" font-weight="600" fill="{AMBER}">de laag steenkool</text>')
    return _svg(breedte, h, "".join(d))
