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
