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

def breukstroken(breedte=460, noemers=(1, 2, 3, 4, 5)):
    """Stroken onder elkaar, elk in een ander aantal gelijke stukken verdeeld.

    Geef `noemers` mee om andere breuken te tonen, bv. (1, 2, 4, 8) om te laten
    zien dat elke stap een halvering is. Let erop dat het onderschrift bij de
    figuur echt over de getoonde breuken gaat.
    """
    rijen = [(n, "1 geheel" if n == 1 else f"1/{n}") for n in noemers]
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
    """Vakjes met pijltjes ertussen: een stappenplan.

    Een vakje is smal — bij vier stappen zo'n 98 punten — en tekst die niet
    past loopt er stil buiten. Zet daarom een | in de tekst waar de regel mag
    afbreken; de tweede regel wordt dan wat kleiner en grijzer gezet.
    """
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


def staafdiagram(paren, breedte=330, hoogte=180, kleur=None, stap=None):
    """paren = [(label, waarde), ...]

    stap bepaalt om de hoeveel de streepjes op de zij-as staan. Laat je hem
    weg, dan kiest de tekening er zelf vier, wat niet altijd ronde getallen
    geeft — bij grote waarden zet je hem dus beter zelf.
    """
    kleur = kleur or FOREST
    links, onder, boven = 30, 28, 14
    top = max(w for _, w in paren)
    n = len(paren)
    vak = (breedte - links) / n
    bb = vak * 0.56
    vlak = hoogte - onder - boven
    d = [f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>']
    for s in range(0, top + 1, stap or max(1, top // 4)):
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
        # De legende breekt af zodra ze de rand raakt. Bij zeven periodes passen
        # de namen anders niet op één regel en valt de laatste er stil buiten.
        bx = m
        for naam, kleur in buiten:
            breed = 22 + 5.6 * len(naam)
            if bx > m and bx + breed > breedte - m + 10:
                bx = m
                h += 17
            d.append(f'<rect x="{bx:.1f}" y="{h-8}" width="11" height="11" rx="2.5" fill="{kleur}"/>')
            d.append(f'<text x="{bx+16:.1f}" y="{h+1}" font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{DIM}">{naam}</text>')
            bx += breed
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


# ---------------------------------------------------------------------------
# Tekeningen bij aardrijkskunde.
#
# Ook hier tekenen we zelf in plaats van een foto te zoeken: een doorsnede van
# de kust of de lagen van het regenwoud zijn schema's zoals ze in elk handboek
# staan, en dan weten we zeker waar het beeld vandaan komt.
#
# Wat we NIET tekenen is een landkaart. Een kaart uit het hoofd natekenen
# wordt scheef, en scheve grenzen horen niet in lesmateriaal. Daarvoor hoort
# een echte kaart met een vrije licentie in de bundel.
# ---------------------------------------------------------------------------

ZAND = "#e0cfa0"
ZAND_DONKER = "#c9b47f"
GRAS = "#7ba368"
GRAS_LICHT = "#dfeada"
ZEE = "#5b93b8"
ROTS = "#9a948a"
SNEEUW = "#f4f8fa"
LUCHT = "#dbe9f2"
LOOF = "#3f7a46"
LOOF_DONKER = "#2c5a33"
LAVA = "#c2410c"

_teller = [0]


def _id(naam):
    """Een uniek id, zodat twee figuren op dezelfde pagina elkaar niet bijten."""
    _teller[0] += 1
    return f"{naam}{_teller[0]}"


def _tekst(x, y, tekst, grootte=10.5, kleur=None, anker="middle", vet=False):
    kleur = kleur or INK
    dik = ' font-weight="600"' if vet else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anker}" '
            f'font-family="IBM Plex Sans,sans-serif" font-size="{grootte}"{dik} '
            f'fill="{kleur}">{tekst}</text>')


def _kussen(x, y, tekst, grootte=9.5, kleur=None, anker="end", vet=False):
    """Tekst op een wit vlakje, voor labels die over een tekening heen komen."""
    br = len(tekst) * grootte * 0.55 + 10
    x0 = {"end": x - br, "start": x, "middle": x - br / 2}[anker]
    return (f'<rect x="{x0:.1f}" y="{y-grootte:.1f}" width="{br:.1f}" height="{grootte+7:.1f}" '
            f'rx="4" fill="#ffffff" opacity="0.88"/>' + _tekst(x, y, tekst, grootte, kleur, anker, vet))


def kustdoorsnede(breedte=470):
    """Een dwarsdoorsnede van de Belgische kust: zee, strand, duin, polder.

    Het punt van de tekening is de stippellijn: de polder ligt lager dan de
    zee, en het duin houdt het water tegen.
    """
    h = 205
    zee_y = 108
    land = ("M0 160 L70 150 L150 108 L195 100 L225 60 "
            "Q252 46 282 92 L315 122 L462 122 L462 172 L0 172 Z")
    d = [f'<rect x="0" y="0" width="{breedte}" height="{h-33}" fill="#ffffff"/>',
         f'<path d="{land}" fill="{ZAND}" stroke="{DARK}" stroke-width="1.6" stroke-linejoin="round"/>']
    # de polder: gras bovenop, want daar wordt geboerd
    knip = _id("polder")
    d.append(f'<clipPath id="{knip}"><path d="{land}"/></clipPath>')
    d.append(f'<rect x="300" y="122" width="170" height="52" fill="{GRAS}" clip-path="url(#{knip})"/>')
    # de zee
    d.append(f'<polygon points="0,{zee_y} 150,{zee_y} 70,150 0,160" fill="{ZEE}"/>')
    for gy, gx1, gx2 in [(118, 12, 52), (130, 30, 66), (124, 74, 108)]:
        d.append(f'<path d="M{gx1} {gy} q10 -4 20 0 q10 4 20 0" fill="none" '
                 f'stroke="#ffffff" stroke-width="1.6" opacity="0.7"/>')
    # zeeniveau doorgetrokken over het land
    d.append(f'<line x1="150" y1="{zee_y}" x2="458" y2="{zee_y}" stroke="{ZEE}" '
             f'stroke-width="1.4" stroke-dasharray="6 5"/>')
    d.append(_tekst(458, zee_y - 5, "zeeniveau", 9.5, ZEE, "end"))
    # helmgras op het duin
    for hx, hy in [(232, 62), (245, 54), (258, 52), (270, 62), (222, 76)]:
        d.append(f'<path d="M{hx} {hy} l-4 -11 M{hx} {hy} l0 -13 M{hx} {hy} l4 -11" '
                 f'fill="none" stroke="{GRAS}" stroke-width="1.5" stroke-linecap="round"/>')
    # een boerderijtje en een sloot in de polder
    d.append(f'<path d="M340 122 h26 v-13 l-13 -9 l-13 9 Z" fill="#ffffff" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<path d="M395 136 h56" stroke="{ZEE}" stroke-width="3" stroke-linecap="round"/>')
    # hoogteverschil
    d.append(f'<line x1="410" y1="{zee_y}" x2="410" y2="122" stroke="{DARK}" stroke-width="1.2"/>')
    d.append(_tekst(392, 158, "de polder ligt lager dan de zee", 9.5, "#ffffff"))
    for x, naam in [(72, "zee"), (172, "strand"), (252, "duin"), (392, "polder")]:
        d.append(_tekst(x, 192, naam, 11.5, AMBER, "middle", True))
    return _svg(breedte, h, "".join(d))


def reliefprofiel(breedte=470):
    """Het hoogteprofiel van België, van de kust tot het Signal de Botrange."""
    h = 200
    links, basis, top_y = 38, 152, 20
    top_m = 700
    vlak = basis - top_y

    def y(m):
        return basis - m / top_m * vlak

    punten = [(0.00, 0), (0.14, 5), (0.24, 20), (0.36, 50), (0.48, 90),
              (0.58, 140), (0.66, 190), (0.74, 300), (0.82, 430),
              (0.90, 560), (0.96, 650), (1.00, 694)]
    xs = [links + f * (breedte - links - 8) for f, _ in punten]
    pad = " ".join(f"{x:.1f},{y(m):.1f}" for x, (_, m) in zip(xs, punten))
    d = [f'<polygon points="{pad} {xs[-1]:.1f},{basis} {links},{basis}" '
         f'fill="#dfe8dd" stroke="{DARK}" stroke-width="1.8" stroke-linejoin="round"/>']
    # hoogte-as
    d.append(f'<line x1="{links}" y1="{top_y}" x2="{links}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    d.append(f'<line x1="{links}" y1="{basis}" x2="{breedte-8}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    for m in (0, 200, 400, 600):
        d.append(f'<line x1="{links-4}" y1="{y(m):.1f}" x2="{links}" y2="{y(m):.1f}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(links - 7, y(m) + 3.5, f"{m}", 9.5, DIM, "end"))
    d.append(_tekst(links - 7, 14, "meter", 9.5, DIM, "end"))
    # de grens tussen laag, midden en hoog België
    for grens_x in (250, 321):
        d.append(f'<line x1="{grens_x}" y1="{top_y}" x2="{grens_x}" y2="{basis}" '
                 f'stroke="{DIM}" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.6"/>')
    for x, naam, bij in [(144, "Laag-België", "tot 100 m"),
                         (285, "Midden-België", "100 tot 200 m"),
                         (391, "Hoog-België", "meer dan 200 m")]:
        d.append(_tekst(x, 172, naam, 10, AMBER, "middle", True))
        d.append(_tekst(x, 186, bij, 9, DIM))
    d.append(f'<circle cx="{xs[-1]:.1f}" cy="{y(694):.1f}" r="3.6" fill="{DARK}"/>')
    d.append(_tekst(breedte - 12, 14, "Signal de Botrange, 694 m", 10, DARK, "end"))
    return _svg(breedte, h, "".join(d))


def rivierloop(breedte=470):
    """Een rivier van de bron tot de monding, van bovenaf gezien."""
    import math
    h = 190
    x0, x1 = 44, 438
    boven, onder = [], []
    x = x0
    while x <= x1:
        t = (x - x0) / (x1 - x0)
        mid = 84 + 26 * t * math.sin((x - x0) / 36)
        halve = 2.4 + 9 * t ** 1.4
        if t > 0.88:
            halve += (t - 0.88) / 0.12 * 15
        boven.append(f"{x:.1f},{mid - halve:.1f}")
        onder.append(f"{x:.1f},{mid + halve:.1f}")
        x += 4
    d = [f'<rect x="428" y="0" width="{breedte-428}" height="142" fill="{ZEE}" opacity="0.4"/>',
         f'<polygon points="{" ".join(boven)} {" ".join(reversed(onder))}" fill="{ZEE}"/>']
    # een zijrivier die er van bovenaf bij komt
    d.append(f'<path d="M168 16 q16 26 6 40 q-8 12 4 22" fill="none" stroke="{ZEE}" '
             f'stroke-width="5" stroke-linecap="round"/>')
    # heuvels bij de bron, boven de rivier zodat ze elkaar niet raken
    for bx, bb, bh in [(10, 30, 26), (34, 38, 40), (66, 28, 22)]:
        d.append(f'<polygon points="{bx},66 {bx+bb/2:.0f},{66-bh} {bx+bb},66" fill="{ROTS}" opacity="0.45"/>')
    d.append(f'<path d="M44 84 L44 70" stroke="{ZEE}" stroke-width="4" stroke-linecap="round"/>')
    d.append(f'<circle cx="44" cy="68" r="5.5" fill="{DARK}"/>')
    for x, naam, bij in [(44, "bron", ""), (124, "bovenloop", "smal en snel"),
                         (232, "middenloop", ""), (340, "benedenloop", "breed en traag"),
                         (436, "monding", "")]:
        d.append(f'<line x1="{x}" y1="140" x2="{x}" y2="150" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(x, 164, naam, 11, AMBER, "middle", True))
        if bij:
            d.append(_tekst(x, 177, bij, 9, DIM))
    d.append(_tekst(178, 12, "zijrivier", 9.5, DIM, "start"))
    d.append(_tekst(462, 132, "zee", 9.5, ZEE, "end"))
    return _svg(breedte, h, "".join(d))


def klimaatdiagram(temperaturen, neerslag, breedte=470, plaats=""):
    """Een klimaatdiagram: balkjes voor de neerslag, een lijn voor de temperatuur.

    temperaturen = 12 waarden in graden, neerslag = 12 waarden in millimeter.
    """
    h = 212
    links, rechts, boven, onder = 40, 42, 22, 38
    basis = h - onder
    vlak = basis - boven
    bb = breedte - links - rechts
    top_mm = max(100, (max(neerslag) // 25 + 1) * 25)
    top_gr = max(20, (max(temperaturen) // 5 + 1) * 5)
    vak = bb / 12
    d = []
    for i, mm in enumerate(neerslag):
        hoogte = mm / top_mm * vlak
        x = links + i * vak + vak * 0.22
        d.append(f'<rect x="{x:.1f}" y="{basis-hoogte:.1f}" width="{vak*0.56:.1f}" '
                 f'height="{hoogte:.1f}" fill="{ZEE}" opacity="0.55" rx="2"/>')
    pts = []
    for i, gr in enumerate(temperaturen):
        px = links + i * vak + vak / 2
        py = basis - gr / top_gr * vlak
        pts.append(f"{px:.1f},{py:.1f}")
    d.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ROOD}" stroke-width="2.4"/>')
    for p in pts:
        px, py = p.split(",")
        d.append(f'<circle cx="{px}" cy="{py}" r="2.8" fill="{ROOD}"/>')
    d.append(f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    d.append(f'<line x1="{breedte-rechts}" y1="{boven}" x2="{breedte-rechts}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    d.append(f'<line x1="{links}" y1="{basis}" x2="{breedte-rechts}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    for s in range(0, int(top_mm) + 1, 25):
        yy = basis - s / top_mm * vlak
        d.append(_tekst(links - 6, yy + 3.5, f"{s}", 9, ZEE, "end"))
    for s in range(0, int(top_gr) + 1, 5):
        yy = basis - s / top_gr * vlak
        d.append(_tekst(breedte - rechts + 6, yy + 3.5, f"{s}", 9, ROOD, "start"))
    d.append(_tekst(links - 6, 14, "mm", 9.5, ZEE, "end"))
    d.append(_tekst(breedte - rechts + 6, 14, "°C", 9.5, ROOD, "start"))
    for i, letter in enumerate("JFMAMJJASOND"):
        d.append(_tekst(links + i * vak + vak / 2, basis + 14, letter, 9.5, DIM))
    if plaats:
        d.append(_tekst(links + bb / 2, basis + 30, plaats, 10, INK))
    return _svg(breedte, h, "".join(d))


def haven(breedte=470):
    """Een zeehaven van opzij: een schip, een containerkraan en de kaai."""
    h = 208
    water_y, bodem = 118, 168
    d = [f'<rect x="0" y="{water_y}" width="240" height="{bodem-water_y}" fill="{ZEE}" opacity="0.55"/>',
         f'<rect x="240" y="{water_y}" width="{breedte-240}" height="{bodem-water_y}" fill="#d9d4c8"/>',
         f'<line x1="240" y1="{water_y}" x2="{breedte}" y2="{water_y}" stroke="{DIM}" stroke-width="1.6"/>']
    # het schip, met de stuurhut achteraan
    d.append(f'<path d="M26 112 L216 112 L204 144 L44 144 Z" fill="{DARK}"/>')
    d.append(f'<rect x="30" y="76" width="30" height="34" fill="#ffffff" stroke="{DARK}" stroke-width="1.3"/>')
    d.append(f'<rect x="36" y="82" width="18" height="8" fill="{ZEE}" opacity="0.6"/>')
    for i, kleur in enumerate([AMBER, FOREST, ROOD, AMBER, FOREST, ROOD]):
        d.append(f'<rect x="{70+i*24}" y="94" width="21" height="16" fill="{kleur}" opacity="0.85"/>')
        if i < 4:
            d.append(f'<rect x="{70+i*24}" y="78" width="21" height="15" fill="{kleur}" opacity="0.55"/>')
    # de containerkraan: twee poten op de kaai, een lange arm over het schip
    d.append(f'<path d="M262 {water_y} V46 M344 {water_y} V46" stroke="{DARK}" stroke-width="5" fill="none"/>')
    d.append(f'<path d="M262 60 H344" stroke="{DARK}" stroke-width="3"/>')
    d.append(f'<path d="M146 42 H414" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/>')
    d.append(f'<path d="M303 42 V10" stroke="{DARK}" stroke-width="4"/>')
    d.append(f'<path d="M303 12 L160 40 M303 12 L410 38" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
    # de kabel met een container eraan
    d.append(f'<path d="M172 42 V66" stroke="{DIM}" stroke-width="1.6"/>')
    d.append(f'<rect x="158" y="66" width="28" height="6" fill="{DARK}"/>')
    d.append(f'<rect x="160" y="48" width="24" height="17" fill="{AMBER}" opacity="0.9"/>')
    # containers op de kaai en een vrachtwagen eronder
    for r in range(3):
        for c in range(6):
            kleur = [AMBER, FOREST, ROOD][(r + c) % 3]
            d.append(f'<rect x="{352+c*19}" y="{water_y-16-r*15}" width="17" height="13" '
                     f'fill="{kleur}" opacity="{0.85 - r*0.12:.2f}"/>')
    d.append(f'<rect x="276" y="{water_y-22}" width="24" height="16" rx="3" fill="{FOREST}"/>')
    d.append(f'<rect x="300" y="{water_y-16}" width="20" height="10" rx="2" fill="{FOREST}" opacity="0.7"/>')
    d.append(f'<circle cx="284" cy="{water_y-4}" r="4.4" fill="{DARK}"/>')
    d.append(f'<circle cx="312" cy="{water_y-4}" r="4.4" fill="{DARK}"/>')
    for x, naam in [(110, "zeeschip"), (300, "containerkraan"), (410, "containers")]:
        d.append(_tekst(x, 190, naam, 11, AMBER, "middle", True))
    d.append(_tekst(462, 136, "kaai", 9.5, DIM, "end"))
    return _svg(breedte, h, "".join(d))


def stadsplan(breedte=470):
    """Een stad van bovenaf, schematisch: kern, ring, woonwijken, bedrijven."""
    h = 226
    cx, cy = 168, 110
    d = [f'<circle cx="{cx}" cy="{cy}" r="104" fill="{GRAS_LICHT}"/>',
         f'<circle cx="{cx}" cy="{cy}" r="72" fill="#efe7d6"/>',
         f'<circle cx="{cx}" cy="{cy}" r="72" fill="none" stroke="{AMBER}" stroke-width="7" opacity="0.8"/>',
         f'<circle cx="{cx}" cy="{cy}" r="40" fill="#e0d6c0" stroke="{DARK}" stroke-width="1.4"/>']
    # straatjes in de oude kern
    for a in range(0, 360, 45):
        import math
        r = math.radians(a)
        d.append(f'<line x1="{cx+10*math.cos(r):.1f}" y1="{cy+10*math.sin(r):.1f}" '
                 f'x2="{cx+38*math.cos(r):.1f}" y2="{cy+38*math.sin(r):.1f}" stroke="#ffffff" stroke-width="2.2"/>')
    d.append(f'<rect x="{cx-7}" y="{cy-9}" width="14" height="18" fill="{DARK}"/>')
    # invalswegen door de ring naar buiten
    for a in (20, 110, 200, 290):
        import math
        r = math.radians(a)
        d.append(f'<line x1="{cx+40*math.cos(r):.1f}" y1="{cy+40*math.sin(r):.1f}" '
                 f'x2="{cx+112*math.cos(r):.1f}" y2="{cy+112*math.sin(r):.1f}" stroke="#ffffff" stroke-width="3.4"/>')
    # rivier, dwars door de stad
    d.append(f'<path d="M34 24 q62 56 74 96 q12 42 58 76" fill="none" stroke="{ZEE}" '
             f'stroke-width="7" opacity="0.7" stroke-linecap="round"/>')
    # bedrijventerrein rechts, aan de autoweg
    d.append(f'<rect x="332" y="60" width="126" height="86" rx="8" fill="#e6e1d4" stroke="{DIM}" stroke-width="1.4"/>')
    for i in range(3):
        for j in range(2):
            d.append(f'<rect x="{344+i*40}" y="{74+j*38}" width="30" height="26" fill="{DIM}" opacity="0.45"/>')
    d.append(f'<line x1="272" y1="103" x2="332" y2="103" stroke="{AMBER}" stroke-width="5"/>')
    for x, y, naam in [(cx, 202, "oude kern"), (70, 206, "woonwijken"), (395, 162, "bedrijven")]:
        d.append(_tekst(x, y, naam, 10.5, DARK, "middle", True))
    d.append(_tekst(48, 26, "rivier", 10.5, ZEE, "middle", True))
    d.append(f'<line x1="{cx}" y1="152" x2="{cx}" y2="192" stroke="{DIM}" stroke-width="1.1"/>')
    d.append(f'<line x1="70" y1="196" x2="96" y2="164" stroke="{DIM}" stroke-width="1.1"/>')
    d.append(_tekst(262, 78, "ring", 10.5, AMBER, "middle", True))
    return _svg(breedte, h, "".join(d))


def aardbolgordels(breedte=470):
    """De aarde van opzij, met de evenaar, de keerkringen en de klimaatgordels."""
    import math
    h = 272
    cx, cy, r = 200, 118, 95
    knip = _id("bol")
    pool = "#a8cce4"
    gematigd = GRAS_LICHT
    tropisch = "#f4e3c4"

    def yl(graden):
        return cy - r * math.sin(math.radians(graden))

    d = [f'<clipPath id="{knip}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>']
    banden = [(cy - r - 2, yl(66.5), pool), (yl(66.5), yl(23.5), gematigd),
              (yl(23.5), yl(-23.5), tropisch), (yl(-23.5), yl(-66.5), gematigd),
              (yl(-66.5), cy + r + 2, pool)]
    for y1, y2, kleur in banden:
        d.append(f'<rect x="{cx-r-2}" y="{y1:.1f}" width="{2*r+4}" height="{y2-y1:.1f}" '
                 f'fill="{kleur}" clip-path="url(#{knip})"/>')
    d.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{DARK}" stroke-width="1.8"/>')
    lijnen = [(66.5, "noordpoolcirkel", False), (23.5, "kreeftskeerkring", False),
              (0, "evenaar", True), (-23.5, "steenbokskeerkring", False),
              (-66.5, "zuidpoolcirkel", False)]
    for graden, naam, vet in lijnen:
        y = yl(graden)
        halve = math.sqrt(max(r * r - (y - cy) ** 2, 0))
        streep = "" if vet else ' stroke-dasharray="5 4"'
        d.append(f'<line x1="{cx-halve:.1f}" y1="{y:.1f}" x2="{cx+halve:.1f}" y2="{y:.1f}" '
                 f'stroke="{DARK}" stroke-width="{2.2 if vet else 1.3}"{streep}/>')
        d.append(f'<line x1="{cx+halve:.1f}" y1="{y:.1f}" x2="302" y2="{y:.1f}" '
                 f'stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(308, y + 3.5, naam, 10, DARK if vet else DIM, "start", vet))
    d.append(_tekst(cx, cy - r - 8, "noordpool", 9.5, DIM))
    d.append(_tekst(cx, cy + r + 16, "zuidpool", 9.5, DIM))
    legenda = [("poolgebied", pool), ("gematigd gebied", gematigd), ("tropisch gebied", tropisch)]
    x = 48
    for naam, kleur in legenda:
        d.append(f'<rect x="{x}" y="{h-26}" width="14" height="14" rx="3" fill="{kleur}" stroke="{DIM}" stroke-width="1"/>')
        d.append(_tekst(x + 20, h - 15, naam, 10.5, INK, "start"))
        x += 24 + len(naam) * 6.4
    return _svg(breedte, h, "".join(d))


def seizoenen(breedte=470):
    """De aarde rond de zon, met de as altijd even schuin en in dezelfde richting."""
    import math
    h = 276
    mx, my, rx, ry = 235, 124, 172, 84
    d = [f'<ellipse cx="{mx}" cy="{my}" rx="{rx}" ry="{ry}" fill="none" stroke="{BORDER}" '
         f'stroke-width="1.6" stroke-dasharray="6 6"/>',
         f'<polygon points="168,44 154,48.4 168,53" fill="{DIM}"/>',
         f'<circle cx="{mx}" cy="{my}" r="26" fill="{AMBER}"/>']
    for a in range(0, 360, 30):
        rr = math.radians(a)
        d.append(f'<line x1="{mx+29*math.cos(rr):.1f}" y1="{my+29*math.sin(rr):.1f}" '
                 f'x2="{mx+37*math.cos(rr):.1f}" y2="{my+37*math.sin(rr):.1f}" '
                 f'stroke="{AMBER}" stroke-width="2.4" stroke-linecap="round"/>')
    d.append(_tekst(mx, my + 4, "zon", 11, "#ffffff", "middle", True))
    scheef = math.radians(23.5)
    ax, ay = 26 * math.sin(scheef), 26 * math.cos(scheef)
    standen = [(mx - rx, my, "zomer (juni)", my + 40),
               (mx + rx, my, "winter (december)", my + 40),
               (mx, my - ry, "lente (maart)", my - ry - 30),
               (mx, my + ry, "herfst (september)", my + ry + 40)]
    for ex, ey, naam, ly in standen:
        d.append(f'<circle cx="{ex}" cy="{ey}" r="22" fill="{ZEE}" opacity="0.35" '
                 f'stroke="{DARK}" stroke-width="1.5"/>')
        d.append(f'<line x1="{ex-ax:.1f}" y1="{ey+ay:.1f}" x2="{ex+ax:.1f}" y2="{ey-ay:.1f}" '
                 f'stroke="{DARK}" stroke-width="2"/>')
        d.append(f'<circle cx="{ex+ax:.1f}" cy="{ey-ay:.1f}" r="3" fill="{DARK}"/>')
        d.append(_tekst(ex, ly, naam, 11, AMBER, "middle", True))
    d.append(_tekst(mx, h - 8, "Het bolletje is de noordpool. De as staat altijd even schuin, "
                               "en altijd in dezelfde richting.", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def bergprofiel(breedte=470):
    """Een berg in de Alpen, met de boomgrens en de sneeuwgrens erop."""
    h = 208
    links, basis, top_y, top_m = 44, 170, 26, 4000

    def y(m):
        return basis - m / top_m * (basis - top_y)

    punten = [(links, 170), (70, 161), (100, 136), (130, 145), (165, 100), (200, 74),
              (230, 42), (265, 76), (295, 63), (325, 110), (360, 94), (395, 138),
              (430, 156), (462, 165)]
    pad = " ".join(f"{x},{yy}" for x, yy in punten)
    berg = f"{pad} 462,{basis} {links},{basis}"
    knipsel = _id("berg")
    d = [f'<clipPath id="{knipsel}"><polygon points="{berg}"/></clipPath>']
    boomgrens, sneeuwgrens = y(2000), y(2900)
    lagen = [(top_y - 6, sneeuwgrens, SNEEUW), (sneeuwgrens, boomgrens, "#cfd6c6"),
             (boomgrens, basis, "#4f7c48")]
    for y1, y2, kleur in lagen:
        d.append(f'<rect x="{links}" y="{y1:.1f}" width="{462-links}" height="{y2-y1:.1f}" '
                 f'fill="{kleur}" clip-path="url(#{knipsel})"/>')
    d.append(f'<polygon points="{berg}" fill="none" stroke="{DARK}" stroke-width="1.8" stroke-linejoin="round"/>')
    for grens, naam in [(sneeuwgrens, "sneeuwgrens, \u00b1 2900 m"), (boomgrens, "boomgrens, \u00b1 2000 m")]:
        d.append(f'<line x1="{links}" y1="{grens:.1f}" x2="462" y2="{grens:.1f}" '
                 f'stroke="{DARK}" stroke-width="1.3" stroke-dasharray="5 4"/>')
        d.append(_kussen(458, grens - 6, naam, 9.5, DARK, "end"))
    d.append(f'<line x1="{links}" y1="{top_y}" x2="{links}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    for m in (0, 1000, 2000, 3000, 4000):
        d.append(f'<line x1="{links-4}" y1="{y(m):.1f}" x2="{links}" y2="{y(m):.1f}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(links - 7, y(m) + 3.5, f"{m}", 9, DIM, "end"))
    d.append(_tekst(links - 7, 14, "meter", 9.5, DIM, "end"))
    legenda = [("eeuwige sneeuw", SNEEUW), ("alpenweide", "#cfd6c6"), ("naaldbos en weiden", "#4f7c48")]
    x = 40
    for naam, kleur in legenda:
        d.append(f'<rect x="{x}" y="{h-24}" width="13" height="13" rx="3" fill="{kleur}" stroke="{DIM}" stroke-width="1"/>')
        d.append(_tekst(x + 18, h - 14, naam, 10, INK, "start"))
        x += 22 + len(naam) * 6.1
    return _svg(breedte, h, "".join(d))


def woestijnduinen(breedte=470):
    """Zandduinen, een felle zon en een oase met palmen."""
    h = 186
    d = [f'<rect x="0" y="0" width="{breedte}" height="{h-26}" fill="#f6efdd"/>',
         f'<circle cx="392" cy="40" r="24" fill="{AMBER}" opacity="0.85"/>']
    for a in range(0, 360, 45):
        import math
        r = math.radians(a)
        d.append(f'<line x1="{392+29*math.cos(r):.1f}" y1="{40+29*math.sin(r):.1f}" '
                 f'x2="{392+38*math.cos(r):.1f}" y2="{40+38*math.sin(r):.1f}" '
                 f'stroke="{AMBER}" stroke-width="2.2" stroke-linecap="round" opacity="0.7"/>')
    lagen = [("M0 104 q70 -30 150 -8 q90 24 170 -12 q90 -40 150 -6 V160 H0 Z", ZAND_DONKER),
             ("M0 124 q80 -24 156 -2 q86 24 164 -8 q80 -32 150 4 V160 H0 Z", ZAND),
             ("M0 144 q90 -18 170 2 q80 20 150 -4 q70 -22 150 6 V160 H0 Z", "#efe0b6")]
    for pad, kleur in lagen:
        d.append(f'<path d="{pad}" fill="{kleur}"/>')
    # de oase
    d.append(f'<ellipse cx="96" cy="146" rx="42" ry="11" fill="{ZEE}" opacity="0.7"/>')
    for px, ph in [(66, 40), (88, 52), (112, 44)]:
        d.append(f'<path d="M{px} 142 q4 -{ph//2} 1 -{ph}" fill="none" stroke="#6b4f2a" stroke-width="3"/>')
        # de bladeren buigen aan het uiteinde naar beneden, zoals bij een palm
        for dx, dy, ex, ey in [(-19, -13, -25, -2), (-12, -17, -17, -8), (0, -19, 0, -12),
                               (12, -17, 17, -8), (19, -13, 25, -2)]:
            d.append(f'<path d="M{px+1} {142-ph} q{dx} {dy} {ex} {ey}" fill="none" '
                     f'stroke="{LOOF}" stroke-width="2.6" stroke-linecap="round"/>')
    d.append(_tekst(96, 176, "oase", 11, AMBER, "middle", True))
    d.append(_tekst(320, 176, "zandduinen", 11, AMBER, "middle", True))
    return _svg(breedte, h, "".join(d))


def regenwoudlagen(breedte=470):
    """De lagen van het tropisch regenwoud, met de hoogte in meter ernaast."""
    h = 254
    links, basis, top_y, top_m = 36, 208, 24, 50

    def y(m):
        return basis - m / top_m * (basis - top_y)

    d = []
    banden = [(50, 35, "#eef4e8"), (35, 15, "#dcebd6"), (15, 3, "#cfe3c8"), (3, 0, "#b9d4b2")]
    for hoog, laag, kleur in banden:
        d.append(f'<rect x="{links}" y="{y(hoog):.1f}" width="{breedte-links-8}" '
                 f'height="{y(laag)-y(hoog):.1f}" fill="{kleur}"/>')
    # de bomen staan links, de namen rechts, zodat ze elkaar niet raken
    for tx, kruin, br in [(64, 34, 30), (112, 22, 34), (158, 30, 28), (206, 20, 32),
                          (252, 33, 26), (296, 24, 30)]:
        d.append(f'<rect x="{tx-4}" y="{y(kruin):.1f}" width="8" height="{basis-y(kruin):.1f}" fill="#6b4f2a"/>')
        d.append(f'<ellipse cx="{tx}" cy="{y(kruin):.1f}" rx="{br}" ry="{br*0.55:.1f}" '
                 f'fill="{LOOF}" opacity="0.85"/>')
    for tx in (138, 274):
        d.append(f'<rect x="{tx-4}" y="{y(46):.1f}" width="8" height="{basis-y(46):.1f}" fill="#6b4f2a"/>')
        d.append(f'<ellipse cx="{tx}" cy="{y(46):.1f}" rx="26" ry="15" fill="{LOOF_DONKER}"/>')
    for tx in (86, 180, 232, 316):
        d.append(f'<path d="M{tx} {basis} q-4 -22 4 -34 q6 -10 0 -16" fill="none" stroke="{LOOF_DONKER}" stroke-width="2.4"/>')
    d.append(f'<line x1="{links}" y1="{basis}" x2="{breedte-8}" y2="{basis}" stroke="#6b4f2a" stroke-width="3"/>')
    d.append(f'<line x1="{links}" y1="{top_y}" x2="{links}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    for m in (0, 10, 20, 30, 40, 50):
        d.append(f'<line x1="{links-4}" y1="{y(m):.1f}" x2="{links}" y2="{y(m):.1f}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(links - 7, y(m) + 3.5, f"{m}", 9, DIM, "end"))
    d.append(_tekst(links - 7, 16, "meter", 9.5, DIM, "end"))
    for m, naam in [(43, "uitstekende bomen"), (25, "kroonlaag"), (9, "struiklaag")]:
        d.append(_tekst(346, y(m) + 4, naam, 10.5, DARK, "start", True))
    d.append(_tekst(346, basis + 14, "bodemlaag", 10.5, DARK, "start", True))
    d.append(_tekst(346, basis + 27, "donker, want het licht komt", 9, DIM, "start"))
    d.append(_tekst(346, basis + 37, "er bijna niet door", 9, DIM, "start"))
    return _svg(breedte, h, "".join(d))


def vulkaan(breedte=470):
    """Een vulkaan in doorsnede: magmakamer, pijp, krater en lavastroom."""
    h = 286
    grond = 212
    d = [f'<rect x="0" y="{grond}" width="{breedte}" height="{h-grond}" fill="#e4dbc8"/>']
    # de kegel, met laagjes as en lava zoals bij een echte stratovulkaan
    kegel = "M104 212 L228 66 L242 66 L366 212 Z"
    knip = _id("kegel")
    d.append(f'<clipPath id="{knip}"><path d="{kegel}"/></clipPath>')
    d.append(f'<path d="{kegel}" fill="{ROTS}"/>')
    for i in range(6):
        d.append(f'<path d="M104 {200-i*26} L366 {200-i*26}" stroke="{STEEN}" stroke-width="7" '
                 f'opacity="0.5" clip-path="url(#{knip})"/>')
    d.append(f'<path d="{kegel}" fill="none" stroke="{DARK}" stroke-width="1.8" stroke-linejoin="round"/>')
    # pijp en magmakamer
    d.append(f'<path d="M228 66 L228 240 L242 240 L242 66 Z" fill="{LAVA}" clip-path="url(#{knip})"/>')
    d.append(f'<rect x="228" y="212" width="14" height="30" fill="{LAVA}"/>')
    d.append(f'<ellipse cx="235" cy="250" rx="62" ry="24" fill="{LAVA}"/>')
    d.append(f'<ellipse cx="235" cy="250" rx="62" ry="24" fill="none" stroke="{ROOD}" stroke-width="1.6"/>')
    # lavastroom over de rechterflank
    d.append(f'<path d="M240 70 q26 34 34 64 q10 32 34 78" fill="none" stroke="{LAVA}" '
             f'stroke-width="7" stroke-linecap="round"/>')
    # askolom
    for cxx, cyy, rr in [(232, 46, 20), (208, 30, 17), (252, 26, 16), (226, 12, 14), (268, 44, 13)]:
        d.append(f'<circle cx="{cxx}" cy="{cyy}" r="{rr}" fill="{DIM}" opacity="0.38"/>')
    merken = [(120, 24, 208, 34, "askolom"), (330, 62, 250, 66, "krater"),
              (412, 150, 292, 150, "lavastroom"), (86, 140, 224, 140, "pijp"),
              (106, 264, 174, 252, "magmakamer")]
    for tx, ty, lx, ly, naam in merken:
        anker = "end" if tx < lx else "start"
        d.append(f'<line x1="{tx + (4 if anker == "start" else -4)}" y1="{ty}" x2="{lx}" y2="{ly}" '
                 f'stroke="{DIM}" stroke-width="1.1"/>')
        d.append(_tekst(tx, ty + 3.5, naam, 10.5, DARK, anker, True))
    return _svg(breedte, h, "".join(d))


def gewesten(breedte=470):
    """De drie gewesten en de tien provincies, met hun hoofdplaats."""
    rijen = [
        ("Vlaanderen", FOREST, 10, 168, [("Antwerpen", "Antwerpen"), ("Limburg", "Hasselt"),
                                         ("Oost-Vlaanderen", "Gent"), ("Vlaams-Brabant", "Leuven"),
                                         ("West-Vlaanderen", "Brugge")]),
        ("Wallonië", AMBER, 186, 168, [("Henegouwen", "Bergen"), ("Luik", "Luik"),
                                            ("Luxemburg", "Aarlen"), ("Namen", "Namen"),
                                            ("Waals-Brabant", "Waver")]),
    ]
    h = 178
    d = []
    for naam, kleur, x, bb, provincies in rijen:
        d.append(f'<rect x="{x}" y="10" width="{bb}" height="{h-20}" rx="9" fill="#ffffff" '
                 f'stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(f'<path d="M{x} 19 a9 9 0 0 1 9 -9 h{bb-18} a9 9 0 0 1 9 9 v17 h{-bb} Z" fill="{kleur}"/>')
        d.append(_tekst(x + bb / 2, 31, naam, 11.5, "#ffffff", "middle", True))
        for i, (prov, stad) in enumerate(provincies):
            y = 56 + i * 22
            d.append(_tekst(x + 10, y, prov, 10.5, INK, "start"))
            d.append(_tekst(x + bb - 10, y, stad, 9, DIM, "end"))
            if i < 4:
                d.append(f'<line x1="{x+10}" y1="{y+7}" x2="{x+bb-10}" y2="{y+7}" stroke="{BORDER}" stroke-width="1"/>')
    x, bb = 362, 98
    d.append(f'<rect x="{x}" y="10" width="{bb}" height="{h-20}" rx="9" fill="#ffffff" '
             f'stroke="{BORDER}" stroke-width="1.4"/>')
    d.append(f'<path d="M{x} 19 a9 9 0 0 1 9 -9 h{bb-18} a9 9 0 0 1 9 9 v17 h{-bb} Z" fill="{DIM}"/>')
    d.append(_tekst(x + bb / 2, 31, "Brussel", 11.5, "#ffffff", "middle", True))
    for i, regel in enumerate(["Hoofdstad van", "België en van", "Europa.", "",
                               "19 gemeenten,", "geen provincie."]):
        d.append(_tekst(x + bb / 2, 58 + i * 16, regel, 9.5, INK if i < 3 else DIM))
    d.append(_tekst(x + bb / 2, 31, "Brussel", 11.5, "#ffffff", "middle", True))
    return _svg(breedte, h, "".join(d))


# ---------------------------------------------------------------------------
# Tekeningen bij spelling.
# ---------------------------------------------------------------------------

def _vakje(x, y, b, hh, tekst, kleur=None, grootte=12, vet=True, vul=None):
    """Een afgerond kadertje met een woord erin."""
    kleur = kleur or DARK
    vul = vul or "#ffffff"
    return (f'<rect x="{x}" y="{y}" width="{b}" height="{hh}" rx="8" fill="{vul}" '
            f'stroke="{kleur}" stroke-width="1.6"/>'
            + _tekst(x + b/2, y + hh/2 + grootte*0.36, tekst, grootte, kleur, "middle", vet))


def _pijl(x1, y, x2, kleur=None):
    """Een pijltje naar rechts."""
    kleur = kleur or DIM
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-6}" y2="{y}" stroke="{kleur}" stroke-width="1.8"/>'
            f'<polygon points="{x2},{y} {x2-8},{y-4.5} {x2-8},{y+4.5}" fill="{kleur}"/>')


def kofschip(breedte=470):
    """'t Kofschip: eindigt de stam op t, k, f, s, ch of p, dan -te en -t."""
    h = 276
    d = [f'<path d="M0 122 q39 -7 78 0 q39 7 78 0 q39 -7 78 0 q39 7 78 0 q39 -7 78 0 q39 7 78 0" '
         f'fill="none" stroke="{WATER}" stroke-width="3.4"/>']
    # het schip
    d.append(f'<path d="M168 122 L302 122 L286 146 L184 146 Z" fill="{DARK}"/>')
    d.append(f'<line x1="212" y1="30" x2="212" y2="122" stroke="#6b4f2a" stroke-width="4"/>')
    d.append(f'<path d="M217 34 L217 116 L297 116 Z" fill="{AMBER}" opacity="0.85"/>')
    d.append(f'<path d="M207 40 L207 116 L158 116 Z" fill="{AMBER}" opacity="0.45"/>')
    d.append(f'<circle cx="212" cy="26" r="4" fill="{DARK}"/>')
    d.append(_tekst(235, 168, "Eindigt de stam op een van deze letters?", 11, INK))

    letters = ["t", "k", "f", "s", "ch", "p"]
    bb, gat = 54, 8
    x0 = (breedte - (len(letters)*bb + (len(letters)-1)*gat)) / 2
    for i, letter in enumerate(letters):
        x = x0 + i*(bb+gat)
        d.append(f'<rect x="{x:.1f}" y="180" width="{bb}" height="32" rx="8" fill="{AMBER}" opacity="0.16"/>')
        d.append(f'<rect x="{x:.1f}" y="180" width="{bb}" height="32" rx="8" fill="none" '
                 f'stroke="{AMBER}" stroke-width="1.6"/>')
        d.append(_tekst(x + bb/2, 202, letter, 15, AMBER, "middle", True))

    for x, kop, regel, voorbeeld, kleur in [
            (16, "ja", "-te en -t", "werken → werkte, gewerkt", AMBER),
            (244, "nee", "-de en -d", "leren → leerde, geleerd", FOREST)]:
        d.append(f'<rect x="{x}" y="228" width="210" height="42" rx="10" fill="#ffffff" '
                 f'stroke="{kleur}" stroke-width="1.6"/>')
        d.append(_tekst(x + 16, 247, f"{kop}: {regel}", 11.5, kleur, "start", True))
        d.append(_tekst(x + 16, 262, voorbeeld, 10, DIM, "start"))
    return _svg(breedte, h, "".join(d))


def lettergrepen(breedte=470):
    """Open en gesloten lettergrepen, en wanneer je een letter verdubbelt."""
    h = 214
    kaart_b = 222
    d = []
    kaarten = [
        (10, "open lettergreep", "eindigt op een klinker", FOREST,
         [("ra", "men", "ramen"), ("bo", "men", "bomen")],
         "één medeklinker, lange klank"),
        (238, "gesloten lettergreep", "eindigt op een medeklinker", AMBER,
         [("ram", "men", "rammen"), ("bom", "men", "bommen")],
         "twee medeklinkers, korte klank"),
    ]
    for x, kop, onder, kleur, paren, slot in kaarten:
        d.append(f'<rect x="{x}" y="10" width="{kaart_b}" height="{h-24}" rx="12" fill="#ffffff" '
                 f'stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(f'<path d="M{x} 19 a9 9 0 0 1 9 -9 h{kaart_b-18} a9 9 0 0 1 9 9 v19 h{-kaart_b} Z" fill="{kleur}"/>')
        d.append(_tekst(x + kaart_b/2, 33, kop, 11.5, "#ffffff", "middle", True))
        d.append(_tekst(x + kaart_b/2, 56, onder, 9.5, DIM))
        for i, (eerste, tweede, heel) in enumerate(paren):
            y = 68 + i*60
            d.append(_vakje(x + 14, y, 50, 30, eerste, kleur, 12.5))
            d.append(_vakje(x + 68, y, 50, 30, tweede, DIM, 12.5, vet=False))
            d.append(_pijl(x + 124, y + 15, x + 140, kleur))
            d.append(_tekst(x + kaart_b - 12, y + 20, heel, 12.5, DARK, "end", True))
        d.append(_tekst(x + kaart_b/2, h - 24, slot, 9.5, kleur))
    return _svg(breedte, h, "".join(d))


def werkwoord_nu(breedte=470):
    """De -t in de tegenwoordige tijd, per persoon."""
    rijen = [("ik", "stam", "ik word"),
             ("jij, hij, zij, u", "stam + t", "jij wordt"),
             ("jij ná het werkwoord", "stam", "word jij?"),
             ("wij, jullie, zij", "hele werkwoord", "wij worden")]
    h = 34 + len(rijen)*46 + 10
    d = [_tekst(14, 22, "wie doet het?", 9.5, DIM, "start"),
         _tekst(190, 22, "wat schrijf je?", 9.5, DIM, "start"),
         _tekst(348, 22, "voorbeeld", 9.5, DIM, "start")]
    for i, (wie, wat, vb) in enumerate(rijen):
        y = 34 + i*46
        kleur = AMBER if "+ t" in wat else FOREST
        d.append(_vakje(14, y, 160, 34, wie, DIM, 10.5, vet=False))
        d.append(_pijl(178, y + 17, 192, kleur))
        d.append(_vakje(196, y, 142, 34, wat, kleur, 11))
        d.append(_pijl(342, y + 17, 356, DIM))
        d.append(_tekst(362, y + 22, vb, 12, DARK, "start", True))
    return _svg(breedte, h, "".join(d))


def verkleinwoorden(breedte=470):
    """De vijf uitgangen van het verkleinwoord, met een voorbeeld."""
    h = 146
    paren = [("-je", "boek", "boek", "je"), ("-tje", "stoel", "stoel", "tje"),
             ("-pje", "boom", "boom", "pje"), ("-etje", "bal", "bal", "letje"),
             ("-kje", "koning", "konin", "kje")]
    vak = (breedte - 20) / len(paren)
    d = []
    for i, (uitgang, grondwoord, romp, staart) in enumerate(paren):
        cx = 10 + vak*(i + 0.5)
        d.append(f'<rect x="{cx-38:.1f}" y="20" width="76" height="38" rx="10" fill="{FOREST}" opacity="0.10"/>')
        d.append(f'<rect x="{cx-38:.1f}" y="20" width="76" height="38" rx="10" fill="none" '
                 f'stroke="{FOREST}" stroke-width="1.6"/>')
        d.append(_tekst(cx, 46, uitgang, 15, FOREST, "middle", True))
        d.append(_tekst(cx, 82, grondwoord, 11, DIM))
        d.append(f'<text x="{cx:.1f}" y="104" text-anchor="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="12.5" font-weight="600">'
                 f'<tspan fill="{INK}">{romp}</tspan><tspan fill="{AMBER}">{staart}</tspan></text>')
        d.append(f'<path d="M{cx:.1f} 88 v8" stroke="{BORDER}" stroke-width="1.4"/>')
    d.append(_tekst(breedte/2, 132, "Welke uitgang het wordt, hoor je aan de klank ervoor. "
                                    "Bij koning verdwijnt de g.", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


# ---------------------------------------------------------------------------
# Geschiedenis voor ✨ Spark: het historisch referentiekader en de prehistorie
# ---------------------------------------------------------------------------

def jaartellijn(breedte=470):
    """De jaartelling rond het nulpunt: links v.C., rechts n.C.

    Het lastige voor een leerling is dat de getallen links gróter worden
    naarmate je verder teruggaat. Daarom staan de pijlen er expliciet bij.
    """
    h = 118
    y = 58
    m = 30
    merken = [(-3000, "3000 v.C."), (-2000, "2000 v.C."), (-1000, "1000 v.C."),
              (0, "0"), (1000, "1000 n.C."), (2000, "2000 n.C.")]
    links, rechts = -3400, 2400
    def x(v):
        return m + (v - links) / (rechts - links) * (breedte - 2 * m)

    d = [f'<line x1="{m}" y1="{y}" x2="{breedte-m}" y2="{y}" stroke="{INK}" stroke-width="2"/>',
         f'<path d="M{breedte-m} {y} l-9 -5 v10 z" fill="{INK}"/>']
    for waarde, label in merken:
        px = x(waarde)
        nul = waarde == 0
        hoog = 14 if nul else 9
        d.append(f'<line x1="{px:.1f}" y1="{y-hoog}" x2="{px:.1f}" y2="{y+hoog}" '
                 f'stroke="{DARK if nul else DIM}" stroke-width="{3 if nul else 1.6}"/>')
        # Vaste regel voor élk jaartal: anders hangt de dikkere nul lager
        # dan de rest en lijkt de lijn scheef.
        d.append(f'<text x="{px:.1f}" y="{y+28:.0f}" text-anchor="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="10" '
                 f'font-weight="{600 if nul else 400}" fill="{DARK if nul else DIM}">{label}</text>')

    # De twee helften benoemen, met een pijl die de telrichting toont.
    for x0, x1, tekst, kleur in [(x(-3200), x(-300), "voor Christus", AMBER),
                                 (x(300), x(2200), "na Christus", FOREST)]:
        d.append(f'<line x1="{x0:.1f}" y1="{y-32}" x2="{x1:.1f}" y2="{y-32}" '
                 f'stroke="{kleur}" stroke-width="1.6"/>')
        punt = x0 if kleur == AMBER else x1
        richting = 1 if kleur == AMBER else -1
        d.append(f'<path d="M{punt:.1f} {y-32} l{7*richting} -4.5 v9 z" fill="{kleur}"/>')
        d.append(f'<text x="{(x0+x1)/2:.1f}" y="{y-40}" text-anchor="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="10.5" font-weight="600" '
                 f'fill="{kleur}">{tekst}</text>')
    d.append(f'<text x="{x(-1800):.1f}" y="{y+48}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{AMBER}">'
             f'hoe groter het getal, hoe langer geleden</text>')
    return _svg(breedte, h, "".join(d))


def domeinen(breedte=470):
    """De vier maatschappelijke domeinen, met bij elk waar het over gaat."""
    vakken = [("politiek", "macht, bestuur,|wetten, oorlog", FOREST),
              ("sociaal", "bevolkingsgroepen,|rechten, ongelijkheid", "#5b7f9c"),
              ("economisch", "landbouw, ambacht,|handel, geld", AMBER),
              ("cultureel", "religie, kunst,|wetenschap, taal", "#7a5b8f")]
    kolom = (breedte - 3 * 10) / 4
    h = 92
    d = []
    for i, (naam, onder, kleur) in enumerate(vakken):
        x = i * (kolom + 10)
        d.append(f'<rect x="{x:.1f}" y="6" width="{kolom:.1f}" height="{h-12}" rx="9" '
                 f'fill="#ffffff" stroke="{kleur}" stroke-width="1.8"/>')
        d.append(f'<rect x="{x:.1f}" y="6" width="{kolom:.1f}" height="22" rx="9" fill="{kleur}"/>')
        d.append(f'<rect x="{x:.1f}" y="19" width="{kolom:.1f}" height="9" fill="{kleur}"/>')
        d.append(f'<text x="{x+kolom/2:.1f}" y="21" text-anchor="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="11" font-weight="600" '
                 f'fill="#ffffff">{naam}</text>')
        for j, regel in enumerate(onder.split("|")):
            d.append(f'<text x="{x+kolom/2:.1f}" y="{47+j*14}" text-anchor="middle" '
                     f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{regel}</text>')
    return _svg(breedte, h, "".join(d))


def nomadisch_sedentair(breedte=470):
    """Links: rondtrekken achter het voedsel aan. Rechts: blijven en boeren."""
    h = 168
    half = breedte / 2 - 8
    d = []

    def kader(x0, titel, kleur):
        d.append(f'<rect x="{x0:.1f}" y="6" width="{half:.1f}" height="{h-14}" rx="10" '
                 f'fill="{PAPER}" stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(f'<text x="{x0+half/2:.1f}" y="26" text-anchor="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="11.5" font-weight="600" '
                 f'fill="{kleur}">{titel}</text>')

    kader(0, "nomadisch", AMBER)
    kader(breedte - half, "sedentair", FOREST)

    # Links: drie kampplaatsen met pijlen ertussen, want de groep verhuist mee.
    gy = 92
    for i, x0 in enumerate([34, half / 2 + 4, half - 44]):
        flauw = 1 if i == 1 else 0.45
        d.append(f'<path d="M{x0-13} {gy} l13 -26 l13 26 z" fill="{AMBER}" opacity="{flauw}"/>')
        d.append(f'<line x1="{x0-13}" y1="{gy}" x2="{x0+13}" y2="{gy}" stroke="{DARK}" '
                 f'stroke-width="1.4" opacity="{flauw}"/>')
    for x0 in [48, half / 2 + 20]:
        d.append(f'<path d="M{x0} {gy-12} h20 m0 0 l-6 -4.5 m6 4.5 l-6 4.5" stroke="{DIM}" '
                 f'stroke-width="1.5" fill="none" stroke-linecap="round"/>')
    d.append(f'<text x="{half/2:.1f}" y="{gy+32}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">'
             f'de groep trekt mee met het voedsel</text>')
    d.append(f'<text x="{half/2:.1f}" y="{gy+48}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">'
             f'jagen en verzamelen</text>')

    # Rechts: twee huizen op een akker, want het voedsel komt naar de mens toe.
    bx = breedte - half
    akker_y = gy + 4
    d.append(f'<rect x="{bx+22:.1f}" y="{akker_y}" width="{half-44:.1f}" height="20" rx="3" fill="{GRAS_LICHT}"/>')
    for i in range(7):
        lx = bx + 32 + i * (half - 64) / 6
        d.append(f'<line x1="{lx:.1f}" y1="{akker_y+4}" x2="{lx:.1f}" y2="{akker_y+16}" '
                 f'stroke="{GRAS}" stroke-width="1.6"/>')
    for x0 in [bx + 44, bx + half - 62]:
        d.append(f'<rect x="{x0:.1f}" y="{gy-24}" width="30" height="24" fill="#ffffff" '
                 f'stroke="{DARK}" stroke-width="1.5"/>')
        d.append(f'<path d="M{x0-4} {gy-24} l19 -15 l19 15 z" fill="{FOREST}"/>')
    d.append(f'<text x="{bx+half/2:.1f}" y="{gy+32}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">'
             f'het voedsel groeit waar men woont</text>')
    d.append(f'<text x="{bx+half/2:.1f}" y="{gy+48}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">'
             f'landbouw en veeteelt</text>')
    return _svg(breedte, h, "".join(d))


def irrigatie(breedte=470):
    """Waarom bevloeiing om samenwerking vraagt: één rivier, veel akkers."""
    h = 176
    d = []
    # De rivier loopt bovenaan dwars over het beeld.
    d.append(f'<rect x="0" y="16" width="{breedte}" height="26" fill="{ZEE}" opacity="0.75"/>')
    d.append(f'<text x="12" y="33" font-family="IBM Plex Sans,sans-serif" font-size="10.5" '
             f'font-weight="600" fill="#ffffff">de rivier</text>')

    kanaal_y = 92
    d.append(f'<rect x="40" y="{kanaal_y}" width="{breedte-80}" height="9" fill="{ZEE}" opacity="0.6"/>')
    # Tussen twee zijtakken in, anders schrijft het label over een tak heen.
    d.append(f'<text x="{breedte*0.31:.1f}" y="{kanaal_y-6}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">hoofdkanaal</text>')

    # Aftakkingen van de rivier naar het kanaal, en van het kanaal naar de akkers.
    for x0 in [78, breedte / 2, breedte - 78]:
        d.append(f'<rect x="{x0-4:.1f}" y="42" width="8" height="{kanaal_y-42}" fill="{ZEE}" opacity="0.6"/>')

    for i in range(4):
        ax = 40 + i * (breedte - 80) / 4 + 8
        ab = (breedte - 80) / 4 - 16
        d.append(f'<rect x="{ax:.1f}" y="{kanaal_y+22}" width="{ab:.1f}" height="34" rx="3" fill="{GRAS_LICHT}" stroke="{GRAS}" stroke-width="1.2"/>')
        d.append(f'<rect x="{ax+ab/2-3:.1f}" y="{kanaal_y+9}" width="6" height="13" fill="{ZEE}" opacity="0.6"/>')
        for j in range(4):
            lx = ax + 7 + j * (ab - 14) / 3
            d.append(f'<line x1="{lx:.1f}" y1="{kanaal_y+29}" x2="{lx:.1f}" y2="{kanaal_y+49}" stroke="{GRAS}" stroke-width="1.5"/>')

    d.append(f'<text x="{breedte/2:.1f}" y="{h-12}" text-anchor="middle" '
             f'font-family="IBM Plex Sans,sans-serif" font-size="10" fill="{DIM}">'
             f'graven, onderhouden en het water eerlijk verdelen: dat lukt alleen samen</text>')
    return _svg(breedte, h, "".join(d))


def standenpiramide(lagen, breedte=470):
    """Een standenmaatschappij als piramide.

    lagen = [(naam, toelichting), ...] van boven naar onder. De onderste laag
    is het breedst, want dat is meteen het punt: bovenaan staan er weinig.
    """
    n = len(lagen)
    laag_h = 40
    h = n * laag_h + 16
    top = 96
    onder = breedte - 150
    d = []
    for i, (naam, toelichting) in enumerate(lagen):
        b0 = top + (onder - top) * i / n
        b1 = top + (onder - top) * (i + 1) / n
        y0 = 8 + i * laag_h
        mid = 120
        kleur = [FOREST, "#3f6f5f", "#5b8878", "#84a99b", "#b4c9bf"][min(i, 4)]
        tekst = "#ffffff" if i < 3 else DARK
        d.append(f'<path d="M{mid-b0/2:.1f} {y0} H{mid+b0/2:.1f} L{mid+b1/2:.1f} {y0+laag_h-3} '
                 f'H{mid-b1/2:.1f} Z" fill="{kleur}" stroke="#ffffff" stroke-width="1.5"/>')
        d.append(f'<text x="{mid:.1f}" y="{y0+laag_h/2:.1f}" text-anchor="middle" dominant-baseline="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="10.5" font-weight="600" fill="{tekst}">{naam}</text>')
        streep_start = max(mid + b0 / 2, mid + b1 / 2) + 10
        d.append(f'<line x1="{streep_start:.1f}" y1="{y0+laag_h/2:.1f}" x2="{mid+onder/2+22:.1f}" y2="{y0+laag_h/2:.1f}" '
                 f'stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(f'<text x="{mid+onder/2+30:.1f}" y="{y0+laag_h/2:.1f}" dominant-baseline="middle" '
                 f'font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{toelichting}</text>')
    return _svg(breedte, h, "".join(d))


def ziggurat(breedte=470):
    """De tempeltoren midden in een Mesopotamische stad."""
    h = 168
    mid = breedte / 2
    grond = h - 40
    d = [f'<rect x="0" y="{grond}" width="{breedte}" height="14" fill="{ZAND}" opacity="0.55"/>']
    treden = [(150, 30), (116, 26), (84, 24)]
    y = grond
    for b, hoogte in treden:
        y -= hoogte
        d.append(f'<rect x="{mid-b/2:.1f}" y="{y}" width="{b}" height="{hoogte}" fill="{ZAND_DONKER}" stroke="{DARK}" stroke-width="1.3"/>')
    d.append(f'<rect x="{mid-26:.1f}" y="{y-26}" width="52" height="26" fill="{AMBER}" stroke="{DARK}" stroke-width="1.3"/>')
    # De trap die tegen de voorkant omhoogloopt.
    d.append(f'<path d="M{mid-9:.1f} {grond} L{mid-9:.1f} {y} h18 L{mid+9:.1f} {grond} Z" '
             f'fill="{ZAND}" stroke="{DARK}" stroke-width="1.1"/>')
    for i in range(7):
        ty = grond - 4 - i * (grond - 4 - y) / 7
        d.append(f'<line x1="{mid-9:.1f}" y1="{ty:.1f}" x2="{mid+9:.1f}" y2="{ty:.1f}" stroke="{DARK}" stroke-width="0.7" opacity="0.5"/>')
    d.append(f'<text x="{mid+40:.1f}" y="{y-12}" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">de tempel bovenaan</text>')
    d.append(f'<text x="{mid:.1f}" y="{h-8}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="9.5" fill="{DIM}">gebouwd uit in de zon gedroogde kleitegels</text>')
    return _svg(breedte, h, "".join(d))


def zuilstijlen(breedte=470):
    """De drie Griekse zuilstijlen naast elkaar, herkenbaar aan hun kapiteel.

    Het verschil zit bovenaan de zuil, in het kapiteel: Dorisch is een sober
    kussen, Ionisch heeft twee krullen opzij, Korintisch een kelk vol bladeren.
    Daarom staat dat stuk hier groot: dat is wat je moet kunnen herkennen.
    """
    h = 250
    steen = "#d8d2c4"
    ABACUS_Y, ABACUS_H = 46, 9      # de vierkante dekplaat, bij alle drie gelijk
    KAP_TOP = ABACUS_Y + ABACUS_H   # waar het kapiteel begint
    KAP_ONDER = 92                  # waar de schacht begint
    kolommen = [
        ("Dorisch", "een sober kussen", 84),
        ("Ionisch", "twee krullen opzij", 235),
        ("Korintisch", "een kelk vol bladeren", 386),
    ]
    schacht_b = 30
    voet = h - 34
    d = [f'<rect x="20" y="{voet}" width="{breedte-40}" height="9" fill="{BORDER}"/>']

    for naam, onder, cx in kolommen:
        # de schacht, met groeven
        d.append(f'<rect x="{cx-schacht_b/2}" y="{KAP_ONDER}" width="{schacht_b}" '
                 f'height="{voet-KAP_ONDER}" fill="{steen}" stroke="{FOREST}" stroke-width="1.4"/>')
        for i in range(1, 4):
            gx = cx - schacht_b / 2 + i * schacht_b / 4
            d.append(f'<line x1="{gx:.1f}" y1="{KAP_ONDER+4}" x2="{gx:.1f}" y2="{voet-4}" '
                     f'stroke="{FOREST}" stroke-width="0.7" opacity="0.5"/>')

        if naam == "Dorisch":
            # een breed kussen dat van de schacht naar de dekplaat uitloopt
            d.append(f'<path d="M{cx-15} {KAP_ONDER} Q{cx-16} {KAP_TOP+4} {cx-26} {KAP_TOP} '
                     f'H{cx+26} Q{cx+16} {KAP_TOP+4} {cx+15} {KAP_ONDER} Z" '
                     f'fill="{steen}" stroke="{FOREST}" stroke-width="1.4"/>')
            d.append(f'<line x1="{cx-20}" y1="{KAP_TOP+9}" x2="{cx+20}" y2="{KAP_TOP+9}" '
                     f'stroke="{FOREST}" stroke-width="0.8" opacity="0.5"/>')
            # geen voetstuk: een Dorische zuil staat rechtstreeks op de vloer
        elif naam == "Ionisch":
            d.append(f'<rect x="{cx-15}" y="{KAP_ONDER-8}" width="30" height="8" fill="{steen}" '
                     f'stroke="{FOREST}" stroke-width="1.2"/>')
            for kant in (-1, 1):
                kx = cx + kant * 17
                ky = KAP_TOP + 13
                d.append(f'<circle cx="{kx}" cy="{ky}" r="11" fill="{steen}" '
                         f'stroke="{FOREST}" stroke-width="1.4"/>')
                d.append(f'<circle cx="{kx}" cy="{ky}" r="5.5" fill="none" '
                         f'stroke="{FOREST}" stroke-width="1.1"/>')
                d.append(f'<circle cx="{kx}" cy="{ky}" r="1.8" fill="{FOREST}"/>')
            d.append(f'<rect x="{cx-7}" y="{KAP_TOP+6}" width="14" height="{KAP_ONDER-KAP_TOP-6}" '
                     f'fill="{steen}" stroke="{FOREST}" stroke-width="1.1"/>')
            d.append(f'<rect x="{cx-20}" y="{voet-7}" width="40" height="7" fill="{steen}" '
                     f'stroke="{FOREST}" stroke-width="1.4"/>')
        else:
            # een kelk: smal onderaan, wijd bovenaan, met bladeren erin
            d.append(f'<path d="M{cx-14} {KAP_ONDER} C{cx-15} {KAP_TOP+12} {cx-24} {KAP_TOP+8} '
                     f'{cx-25} {KAP_TOP} H{cx+25} C{cx+24} {KAP_TOP+8} {cx+15} {KAP_TOP+12} '
                     f'{cx+14} {KAP_ONDER} Z" fill="{steen}" stroke="{FOREST}" stroke-width="1.4"/>')
            # onderste krans bladeren, en een tweede rij die erboven uitsteekt
            for bx, bh in ((-8, 13), (0, 16), (8, 13)):
                bo = KAP_ONDER - 2
                d.append(f'<path d="M{cx+bx} {bo} Q{cx+bx-4.5} {bo-bh/2} {cx+bx} {bo-bh} '
                         f'Q{cx+bx+4.5} {bo-bh/2} {cx+bx} {bo} Z" fill="{FOREST}" opacity="0.5"/>')
            for bx in (-16, -5.5, 5.5, 16):
                bo = KAP_TOP + 14
                d.append(f'<path d="M{cx+bx} {bo} Q{cx+bx-4} {bo-7} {cx+bx} {bo-13} '
                         f'Q{cx+bx+4} {bo-7} {cx+bx} {bo} Z" fill="{FOREST}" opacity="0.32"/>')
            d.append(f'<rect x="{cx-20}" y="{voet-7}" width="40" height="7" fill="{steen}" '
                     f'stroke="{FOREST}" stroke-width="1.4"/>')

        # de dekplaat komt bovenop, zodat ze het kapiteel netjes afsluit
        d.append(f'<rect x="{cx-29}" y="{ABACUS_Y}" width="58" height="{ABACUS_H}" '
                 f'fill="{steen}" stroke="{FOREST}" stroke-width="1.4"/>')
        d.append(_tekst(cx, 32, naam, 11, DARK, vet=True))
        d.append(_tekst(cx, h - 12, onder, 9, DIM))

    return _svg(breedte, h, "".join(d))


def primair_secundair(breedte=470):
    """Waarom een bron primair of secundair heet: het gaat om de tijd.

    Links de gebeurtenis, daarnaast wat er toen gemaakt werd (primair), en
    rechts wat er later uit gemaakt werd (secundair).
    """
    h = 214
    lijn_y = 150
    d = [f'<line x1="26" y1="{lijn_y}" x2="{breedte-26}" y2="{lijn_y}" '
         f'stroke="{DIM}" stroke-width="1.6"/>',
         f'<path d="M{breedte-30} {lijn_y-5} L{breedte-20} {lijn_y} L{breedte-30} {lijn_y+5} Z" fill="{DIM}"/>',
         _tekst(breedte - 40, lijn_y + 20, "later", 9.5, DIM)]

    blokken = [
        (108, "de gebeurtenis", "het voorval zelf", AMBER, "toen"),
        (250, "primaire bron", "toen gemaakt", FOREST, "toen"),
        (396, "secundaire bron", "later gemaakt|uit die bronnen", DARK, "later"),
    ]
    for cx, kop, onder, kleur, _ in blokken:
        bb, bh = 118, 60
        d.append(f'<rect x="{cx-bb/2}" y="{lijn_y-bh-22}" width="{bb}" height="{bh}" rx="9" '
                 f'fill="{PAPER}" stroke="{kleur}" stroke-width="1.6"/>')
        d.append(_tekst(cx, lijn_y - bh - 22 + 24, kop, 10.5, kleur, vet=True))
        for i, regel in enumerate(onder.split("|")):
            d.append(_tekst(cx, lijn_y - bh - 22 + 40 + i * 12, regel, 9, DIM))
        d.append(f'<line x1="{cx}" y1="{lijn_y-22}" x2="{cx}" y2="{lijn_y-5}" '
                 f'stroke="{kleur}" stroke-width="1.3" stroke-dasharray="3 2.5"/>')
        d.append(f'<circle cx="{cx}" cy="{lijn_y}" r="4.5" fill="{kleur}"/>')

    # een boog over de vakjes heen: de secundaire bron komt uit de primaire voort
    boog_y = lijn_y - 82
    d.append(f'<path d="M250 {boog_y} Q323 {boog_y-30} 396 {boog_y-6}" fill="none" '
             f'stroke="{DIM}" stroke-width="1.3"/>')
    d.append(f'<path d="M396 {boog_y-6} l-8.5 -4.5 l1.5 8 Z" fill="{DIM}" '
             f'transform="rotate(150 396 {boog_y-6})"/>')
    d.append(_tekst(323, boog_y - 26, "wordt gemaakt uit", 9, DIM))

    d.append(_tekst(breedte / 2, h - 10,
                    "Primair of secundair gaat over wanneer de bron gemaakt is, niet over hoe goed ze is.",
                    9.5, DIM))
    return _svg(breedte, h, "".join(d))


def getallensoorten(breedte=470):
    """De getallenverzamelingen als dozen in elkaar: ℕ zit in ℤ, ℤ zit in ℚ.

    Dat "in elkaar" is precies het punt van de uitbreiding: er komt telkens
    iets bij, en alles wat je al had blijft gelden.
    """
    h = 232
    lagen = [
        ("ℚ  rationale getallen", "breuken en kommagetallen", "−3/4 · 0,25 · 2,5", "#7a5b8f", 0),
        ("ℤ  gehele getallen", "de negatieve erbij", "−7 · −1", "#5b7f9c", 1),
        ("ℕ  natuurlijke getallen", "om te tellen", "0 · 1 · 2 · 3", FOREST, 2),
    ]
    d = []
    for kop, onder, voorbeeld, kleur, i in lagen:
        pad = 24 + i * 46
        y0 = 12 + i * 34
        y1 = h - 14 - i * 34
        d.append(f'<rect x="{pad}" y="{y0}" width="{breedte-2*pad}" height="{y1-y0}" rx="12" '
                 f'fill="none" stroke="{kleur}" stroke-width="1.8"/>')
        d.append(_tekst(pad + 14, y0 + 20, kop, 11.5, kleur, anker="start", vet=True))
        d.append(_tekst(breedte - pad - 14, y0 + 20, onder, 9, DIM, anker="end"))
        # de voorbeelden van deze laag staan onderin haar eigen strook
        d.append(_tekst(breedte / 2, y1 - 11, voorbeeld, 10.5, kleur))

    return _svg(breedte, h, "".join(d))


def verhoudingstabel(paren, breedte=470, koppen=("aantal", "prijs")):
    """Een verhoudingstabel: twee rijen die in dezelfde verhouding meegroeien.

    paren = [(links, rechts), ...] als tekst, van links naar rechts.
    """
    n = len(paren)
    kolom = min(96, (breedte - 120) / n)
    x0 = 100
    h = 150
    rij_y = [54, 92]
    d = [f'<rect x="{x0}" y="{rij_y[0]-22}" width="{kolom*n}" height="{88}" fill="{PAPER}" '
         f'stroke="{BORDER}" stroke-width="1.2"/>']
    for r, kop in enumerate(koppen):
        d.append(_tekst(x0 - 12, rij_y[r] + 4, kop, 10.5, DIM, anker="end"))
    for i, (links, rechts) in enumerate(paren):
        cx = x0 + kolom * i + kolom / 2
        if i:
            d.append(f'<line x1="{x0+kolom*i}" y1="{rij_y[0]-22}" x2="{x0+kolom*i}" '
                     f'y2="{rij_y[0]-22+88}" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(cx, rij_y[0] + 4, links, 12, DARK, vet=True))
        d.append(_tekst(cx, rij_y[1] + 4, rechts, 12, FOREST, vet=True))
    d.append(f'<line x1="{x0}" y1="{rij_y[0]+20}" x2="{x0+kolom*n}" y2="{rij_y[0]+20}" '
             f'stroke="{BORDER}" stroke-width="1.2"/>')
    return _svg(breedte, h - 26, "".join(d))


def tekenregels(breedte=470):
    """Het vierkantje met de tekenregels voor × en : bij negatieve getallen.

    Vier vakjes: gelijke tekens geven plus, verschillende tekens geven min.
    Bewust zonder getallen erin, zodat het voor maal én voor delen geldt.
    """
    vak = 84
    x0 = (breedte - 2 * vak) / 2 + 16
    y0 = 46
    rijen = [("+", "+", "+"), ("+", "−", "−"),
             ("−", "+", "−"), ("−", "−", "+")]
    d = []
    # koppen langs de rand: welk teken heeft het eerste, welk het tweede getal
    d.append(_tekst(x0 + vak / 2, y0 - 12, "tweede getal +", 10.5, DIM))
    d.append(_tekst(x0 + vak * 1.5, y0 - 12, "tweede getal −", 10.5, DIM))
    for i, kop in enumerate(("eerste getal +", "eerste getal −")):
        d.append(_tekst(x0 - 12, y0 + vak * i + vak / 2 + 4, kop, 10.5, DIM, anker="end"))
    for i, (eerste, tweede, uit) in enumerate(rijen):
        rij, kol = i // 2, i % 2
        x, y = x0 + vak * kol, y0 + vak * rij
        positief = uit == "+"
        d.append(f'<rect x="{x}" y="{y}" width="{vak}" height="{vak}" rx="10" '
                 f'fill="{PAPER if positief else "#f6efe4"}" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(x + vak / 2, y + 30, f"{eerste} × {tweede}", 11, DIM))
        d.append(_tekst(x + vak / 2, y + 58, uit, 26, FOREST if positief else AMBER, vet=True))
    return _svg(breedte, y0 + vak * 2 + 14, "".join(d))


def mogelijkhedenboom(eerste, tweede, breedte=470):
    """Een boompje dat alle combinaties van twee keuzes laat zien.

    eerste = de takken bovenaan, tweede = wat er bij elke tak nog bij kan.
    Zo wordt zichtbaar waarom je het aantal keuzes vermenigvuldigt.
    """
    n, m = len(eerste), len(tweede)
    top_y, blad_y = 54, 132
    vakb, vakh = 88, 30
    stam_x = breedte / 2
    tak_x = [(i + 0.5) * breedte / n for i in range(n)]
    d = [f'<circle cx="{stam_x}" cy="20" r="5" fill="{FOREST}"/>']
    for i, naam in enumerate(eerste):
        d.append(f'<line x1="{stam_x}" y1="25" x2="{tak_x[i]:.1f}" y2="{top_y - vakh/2}" '
                 f'stroke="{BORDER}" stroke-width="1.6"/>')
        d.append(f'<rect x="{tak_x[i]-vakb/2:.1f}" y="{top_y-vakh/2}" width="{vakb}" height="{vakh}" '
                 f'rx="8" fill="{PAPER}" stroke="{FOREST}" stroke-width="1.4"/>')
        d.append(_tekst(tak_x[i], top_y + 4, naam, 11, DARK, vet=True))
        for j, blad in enumerate(tweede):
            bx = tak_x[i] + (j - (m - 1) / 2) * (vakb / m + 6)
            d.append(f'<line x1="{tak_x[i]:.1f}" y1="{top_y + vakh/2}" x2="{bx:.1f}" '
                     f'y2="{blad_y - vakh/2}" stroke="{BORDER}" stroke-width="1.4"/>')
            d.append(f'<rect x="{bx - vakb/m/2 - 2:.1f}" y="{blad_y-vakh/2}" '
                     f'width="{vakb/m + 4:.1f}" height="{vakh}" rx="8" fill="#ffffff" '
                     f'stroke="{AMBER}" stroke-width="1.4"/>')
            d.append(_tekst(bx, blad_y + 4, blad, 10, DARK))
    return _svg(breedte, blad_y + vakh / 2 + 12, "".join(d))


def pijlrichting(links, rechts, omkeerbaar, breedte=470):
    """Twee uitspraken met een pijl ertussen: geldt het \u00e9\u00e9n kant op, of allebei.

    Bewust zonder bijschrift bij de pijlen: tussen de twee vakjes is maar een
    goede negentig punten plaats, en tekst die daar niet in past, loopt over de
    vakjes heen. Wat de richtingen betekenen, hoort in het onderschrift.
    """
    vakb, vakh = 168, 54
    y = 46
    x1, x2 = 6, breedte - vakb - 6
    d = []
    for x, tekst in ((x1, links), (x2, rechts)):
        d.append(f'<rect x="{x}" y="{y}" width="{vakb}" height="{vakh}" rx="10" '
                 f'fill="{PAPER}" stroke="{FOREST}" stroke-width="1.6"/>')
        regels = tekst.split("|")
        start = y + vakh / 2 + 4 - (len(regels) - 1) * 7
        for j, regel in enumerate(regels):
            d.append(_tekst(x + vakb / 2, start + j * 15, regel, 11, DARK, vet=(j == 0)))
    mx1, mx2 = x1 + vakb + 14, x2 - 14
    mid = y + vakh / 2
    d.append(f'<path d="M{mx1} {mid-8} H{mx2} l-7 -5 m7 5 l-7 5" stroke="{FOREST}" '
             f'stroke-width="2" fill="none" stroke-linecap="round"/>')
    if omkeerbaar:
        d.append(f'<path d="M{mx2} {mid+8} H{mx1} l7 -5 m-7 5 l7 5" stroke="{FOREST}" '
                 f'stroke-width="2" fill="none" stroke-linecap="round"/>')
    else:
        # de terugweg gestippeld en doorstreept: die geldt niet
        d.append(f'<path d="M{mx2} {mid+8} H{mx1} l7 -5 m-7 5 l7 5" stroke="#c9c2b4" '
                 f'stroke-width="2" fill="none" stroke-linecap="round" stroke-dasharray="4 4"/>')
        m = (mx1 + mx2) / 2
        d.append(f'<line x1="{m-7}" y1="{mid+1}" x2="{m+7}" y2="{mid+15}" '
                 f'stroke="{AMBER}" stroke-width="2.4" stroke-linecap="round"/>')
        d.append(f'<line x1="{m+7}" y1="{mid+1}" x2="{m-7}" y2="{mid+15}" '
                 f'stroke="{AMBER}" stroke-width="2.4" stroke-linecap="round"/>')
    return _svg(breedte, y + vakh + 16, "".join(d))


def insluiting(buiten, binnen, voorbeeld_buiten, voorbeeld_binnen, breedte=470):
    """Eén groep helemaal binnen een andere: elk vierkant is een rechthoek.

    Zo wordt zichtbaar waarom de als-dan maar één kant op werkt.
    """
    h = 172
    d = [f'<rect x="20" y="14" width="{breedte-40}" height="{h-28}" rx="14" fill="none" '
         f'stroke="#5b7f9c" stroke-width="1.8"/>']
    d.append(_tekst(34, 36, buiten, 11.5, "#5b7f9c", anker="start", vet=True))
    d.append(_tekst(breedte - 34, 36, voorbeeld_buiten, 9.5, DIM, anker="end"))
    d.append(f'<rect x="{breedte/2-108}" y="62" width="216" height="{h-96}" rx="12" fill="none" '
             f'stroke="{FOREST}" stroke-width="1.8"/>')
    d.append(_tekst(breedte / 2, 84, binnen, 11.5, FOREST, vet=True))
    d.append(_tekst(breedte / 2, h - 48, voorbeeld_binnen, 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def evenwijdige_hoeken(breedte=470):
    """Twee evenwijdige rechten met een snijlijn, en de acht hoeken genummerd.

    De nummertjes staan op de deellijn van hun eigen hoek, op vaste afstand van
    het snijpunt. Zet je ze gewoon schuin naast het snijpunt, dan komen twee
    van de vier op de snijlijn zelf te liggen, want die staat schuin.

    Welke hoeken gelijk zijn, hoort in het onderschrift: in de tekening zelf is
    daar geen plaats voor zonder dat het een kluwen wordt.
    """
    import math
    y1, y2 = 46, 130
    x0, x1 = 22, breedte - 22
    sx1, sx2 = 190, 282
    h = 182
    d = []
    for y in (y1, y2):
        d.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{FOREST}" stroke-width="2.2"/>')
    rico = (sx2 - sx1) / (y2 - y1)
    top = (sx1 - rico * (y1 - 14), 14)
    bot = (sx2 + rico * (h - 12 - y2), h - 12)
    d.append(f'<line x1="{top[0]:.1f}" y1="{top[1]}" x2="{bot[0]:.1f}" y2="{bot[1]}" '
             f'stroke="{DARK}" stroke-width="2.2"/>')
    for y in (y1, y2):
        d.append(f'<path d="M{x1-58} {y-6} l8 6 l-8 6" fill="none" stroke="{FOREST}" '
                 f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')

    # richting van de snijlijn, op lengte 1 gebracht
    lang = math.hypot(sx2 - sx1, y2 - y1)
    vx, vy = (sx2 - sx1) / lang, (y2 - y1) / lang
    # Hoe smaller de hoek, hoe verder het nummertje van het snijpunt moet staan,
    # anders raakt het bolletje een van de twee benen. Bij een halve hoek van a
    # ligt een bolletje op afstand R op R·sin(a) van elk been; 17 geeft een
    # bolletje van 10 nog een paar punten lucht.
    def afstand(halve_hoek):
        return max(27.0, 17.0 / max(math.sin(halve_hoek), 0.05))

    for sx, sy, eerste in ((sx1, y1, 1), (sx2, y2, 5)):
        # de vier hoeken, elk tussen een tak van de evenwijdige en een tak van
        # de snijlijn; het nummertje komt op de deellijn ertussen
        takken = [((-1, 0), (-vx, -vy)), ((1, 0), (-vx, -vy)),
                  ((-1, 0), (vx, vy)), ((1, 0), (vx, vy))]
        for j, ((ux, uy), (wx, wy)) in enumerate(takken):
            bx, by = ux + wx, uy + wy
            norm = math.hypot(bx, by) or 1
            halve = math.acos(max(-1.0, min(1.0, ux * wx + uy * wy))) / 2
            straal = afstand(halve)
            cx, cy = sx + bx / norm * straal, sy + by / norm * straal
            d.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="10" fill="{PAPER}" '
                     f'stroke="{BORDER}" stroke-width="1"/>')
            d.append(_tekst(cx, cy + 4, str(eerste + j), 10.5, DIM))
    return _svg(breedte, h, "".join(d))


def merkwaardige_lijnen(breedte=470):
    """De vier merkwaardige lijnen, elk in een eigen driehoekje.

    De driehoek staat bewust scheef. In een driehoek die bijna gelijkbenig is,
    vallen de hoogtelijn, de middelloodlijn en de zwaartelijn haast samen, en
    dan lijken alle vier de tekeningen op elkaar — net het omgekeerde van wat
    ze moeten laten zien. De lijnen worden echt berekend, niet geschat.
    """
    import math
    vak = breedte / 4
    h = 136
    top = (0.30, 0.08)
    linksonder = (0.06, 0.78)
    rechtsonder = (0.96, 0.78)
    namen = ["bissectrice", "hoogtelijn", "middelloodlijn", "zwaartelijn"]
    d = []
    for i, naam in enumerate(namen):
        ox, oy = i * vak + 9, 12
        b, hh = vak - 18, 82

        def P(f):
            return ox + f[0] * b, oy + f[1] * hh

        A, B, C = P(top), P(linksonder), P(rechtsonder)
        d.append(f'<polygon points="{A[0]:.1f},{A[1]:.1f} {B[0]:.1f},{B[1]:.1f} {C[0]:.1f},{C[1]:.1f}" '
                 f'fill="#ffffff" stroke="{DARK}" stroke-width="1.8"/>')
        M = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
        voet = (A[0], C[1])           # BC loopt horizontaal, dus loodrecht is verticaal
        if naam == "bissectrice":
            # de echte deellijn: de som van de twee eenheidsvectoren uit A
            eenheden = []
            for hoekpunt in (B, C):
                dx, dy = hoekpunt[0] - A[0], hoekpunt[1] - A[1]
                lang = math.hypot(dx, dy)
                eenheden.append((dx / lang, dy / lang))
            rx, ry = eenheden[0][0] + eenheden[1][0], eenheden[0][1] + eenheden[1][1]
            t = (C[1] - A[1]) / ry
            doel = (A[0] + rx * t, C[1])
            d.append(f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{doel[0]:.1f}" y2="{doel[1]:.1f}" '
                     f'stroke="{AMBER}" stroke-width="2"/>')
            # twee boogjes: de tophoek is in twee gelijke stukken verdeeld
            for hoekpunt in (B, doel):
                dx, dy = hoekpunt[0] - A[0], hoekpunt[1] - A[1]
                lang = math.hypot(dx, dy)
                d.append(f'<circle cx="{A[0]+dx/lang*17:.1f}" cy="{A[1]+dy/lang*17:.1f}" r="1.9" fill="{AMBER}"/>')
        elif naam == "hoogtelijn":
            d.append(f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{voet[0]:.1f}" y2="{voet[1]:.1f}" '
                     f'stroke="{AMBER}" stroke-width="2"/>')
            d.append(f'<path d="M{voet[0]+8:.1f} {voet[1]} v-8 h-8" fill="none" stroke="{AMBER}" stroke-width="1.4"/>')
        elif naam == "middelloodlijn":
            d.append(f'<line x1="{M[0]:.1f}" y1="{M[1]-40:.1f}" x2="{M[0]:.1f}" y2="{M[1]+9:.1f}" '
                     f'stroke="{AMBER}" stroke-width="2"/>')
            d.append(f'<path d="M{M[0]+8:.1f} {M[1]} v-8 h-8" fill="none" stroke="{AMBER}" stroke-width="1.4"/>')
            for teken in (-1, 1):
                d.append(f'<line x1="{M[0]+teken*14:.1f}" y1="{M[1]-4}" x2="{M[0]+teken*14:.1f}" '
                         f'y2="{M[1]+4}" stroke="{DIM}" stroke-width="1.4"/>')
        else:
            d.append(f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{M[0]:.1f}" y2="{M[1]:.1f}" '
                     f'stroke="{AMBER}" stroke-width="2"/>')
            for teken in (-1, 1):
                d.append(f'<line x1="{M[0]+teken*14:.1f}" y1="{M[1]-4}" x2="{M[0]+teken*14:.1f}" '
                         f'y2="{M[1]+4}" stroke="{DIM}" stroke-width="1.4"/>')
        d.append(_tekst(ox + b / 2, h - 12, naam, 10, DIM))
    return _svg(breedte, h, "".join(d))


def vierkante_stap(breedte=470):
    """Waarom een stap bij oppervlakte maal honderd is en niet maal tien.

    Eén vierkante decimeter, verdeeld in vierkante centimeters: tien rijen van
    tien. Dat je de lengte én de breedte omzet, is precies wat je hier ziet.
    """
    zijde = 158
    x0, y0 = (breedte - zijde) / 2, 30
    vak = zijde / 10
    d = [f'<rect x="{x0}" y="{y0}" width="{zijde}" height="{zijde}" '
         f'fill="rgba(47,93,80,.06)" stroke="{DARK}" stroke-width="2"/>']
    for k in range(1, 10):
        d.append(f'<line x1="{x0+k*vak:.1f}" y1="{y0}" x2="{x0+k*vak:.1f}" y2="{y0+zijde}" '
                 f'stroke="{BORDER}" stroke-width="1"/>')
        d.append(f'<line x1="{x0}" y1="{y0+k*vak:.1f}" x2="{x0+zijde}" y2="{y0+k*vak:.1f}" '
                 f'stroke="{BORDER}" stroke-width="1"/>')
    # het eerste vakje opvullen, zodat je ziet hoe klein één cm² is
    d.append(f'<rect x="{x0}" y="{y0}" width="{vak:.1f}" height="{vak:.1f}" fill="{AMBER}" opacity="0.8"/>')
    d.append(_tekst(x0 + zijde / 2, y0 - 11, "1 dm", 11, DARK, vet=True))
    d.append(_tekst(x0 - 10, y0 + zijde / 2 + 4, "1 dm", 11, DARK, anker="end", vet=True))
    d.append(_tekst(x0 + zijde / 2, y0 + zijde + 20, "10 rijen van 10 = 100 cm²", 11, AMBER))
    return _svg(breedte, y0 + zijde + 32, "".join(d))


def assenstelsel(punten, tot=6, breedte=300):
    """Een assenstelsel met een paar punten erin.

    punten = [(x, y, naam), ...] met waarden tussen 0 en `tot`.
    """
    rand = 30
    # rechts wat meer lucht, anders plakt de letter x tegen het laatste cijfer
    vlak = breedte - rand - 30
    h = vlak + rand + 20
    stap = vlak / tot
    ox, oy = rand, rand + vlak - stap * 0  # oorsprong linksonder
    oy = rand + vlak
    d = []
    for k in range(tot + 1):
        d.append(f'<line x1="{ox+k*stap:.1f}" y1="{rand}" x2="{ox+k*stap:.1f}" y2="{oy}" '
                 f'stroke="{BORDER}" stroke-width="1"/>')
        d.append(f'<line x1="{ox}" y1="{oy-k*stap:.1f}" x2="{ox+vlak:.1f}" y2="{oy-k*stap:.1f}" '
                 f'stroke="{BORDER}" stroke-width="1"/>')
    d.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+vlak+8:.1f}" y2="{oy}" stroke="{DARK}" stroke-width="1.8"/>')
    d.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{rand-8}" stroke="{DARK}" stroke-width="1.8"/>')
    d.append(_tekst(ox + vlak + 16, oy + 5, "x", 11, DARK, vet=True))
    d.append(_tekst(ox - 14, rand - 4, "y", 11, DARK, vet=True))
    d.append(_tekst(ox - 9, oy + 15, "0", 10, DIM))
    for k in range(1, tot + 1):
        d.append(_tekst(ox + k * stap, oy + 15, str(k), 9.5, DIM))
        d.append(_tekst(ox - 10, oy - k * stap + 4, str(k), 9.5, DIM))
    for x, y, naam in punten:
        px, py = ox + x * stap, oy - y * stap
        d.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{px:.1f}" y2="{oy}" stroke="{AMBER}" '
                 f'stroke-width="1.2" stroke-dasharray="3 3"/>')
        d.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{ox}" y2="{py:.1f}" stroke="{AMBER}" '
                 f'stroke-width="1.2" stroke-dasharray="3 3"/>')
        d.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{FOREST}"/>')
        d.append(_tekst(px + 20, py - 6, naam, 10.5, FOREST, vet=True))
    return _svg(breedte, h, "".join(d))


def evenredig_grafieken(breedte=470):
    """Recht evenredig naast omgekeerd evenredig, zodat het verschil opvalt."""
    vak = breedte / 2
    rand, vlak = 30, 128
    h = vlak + rand + 34
    d = []
    for i, soort in enumerate(("recht", "omgekeerd")):
        ox = i * vak + rand
        oy = rand + vlak
        d.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+vak-rand-12:.1f}" y2="{oy}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{rand-6}" stroke="{DARK}" stroke-width="1.6"/>')
        punten = []
        if soort == "recht":
            for k in range(0, 61):
                x = k / 60
                punten.append((ox + x * (vak - rand - 20), oy - x * vlak * 0.92))
            bijschrift = "y = 3x"
        else:
            for k in range(0, 61):
                x = 0.18 + k / 60 * 0.82
                y = 0.18 / x
                punten.append((ox + x * (vak - rand - 20), oy - min(y, 1.0) * vlak * 0.92))
            bijschrift = "y = 24 : x"
        pad = " ".join(f"{px:.1f},{py:.1f}" for px, py in punten)
        d.append(f'<polyline points="{pad}" fill="none" stroke="{FOREST}" stroke-width="2.2"/>')
        d.append(_tekst(ox + (vak - rand) / 2, h - 22, bijschrift, 11, FOREST, vet=True))
        d.append(_tekst(ox + (vak - rand) / 2, h - 8,
                        "rechte door de oorsprong" if soort == "recht" else "kromme, raakt de assen niet",
                        9.5, DIM))
    return _svg(breedte, h, "".join(d))


def venndiagram(naam_a, naam_b, enkel_a, samen, enkel_b, buiten=None, breedte=470):
    """Twee overlappende cirkels met wat in elk deel zit.

    De drie gebieden staan elk op hun eigen plek: links wat enkel in A zit,
    in het midden de doorsnede, rechts wat enkel in B zit.
    """
    r = 92
    cy = 112
    kader_h = 196                      # de doos rond de cirkels
    h = kader_h + (30 if buiten else 14)   # plus een strook voor het onderschrift
    cxa, cxb = breedte / 2 - 52, breedte / 2 + 52
    d = [f'<rect x="14" y="14" width="{breedte-28}" height="{kader_h}" rx="12" fill="{PAPER}" '
         f'stroke="{BORDER}" stroke-width="1.2"/>']
    d.append(f'<circle cx="{cxa}" cy="{cy}" r="{r}" fill="{FOREST}" fill-opacity="0.10" '
             f'stroke="{FOREST}" stroke-width="1.8"/>')
    d.append(f'<circle cx="{cxb}" cy="{cy}" r="{r}" fill="{AMBER}" fill-opacity="0.10" '
             f'stroke="{AMBER}" stroke-width="1.8"/>')
    d.append(_tekst(cxa - r + 26, cy - r + 2, naam_a, 12, FOREST, vet=True))
    d.append(_tekst(cxb + r - 26, cy - r + 2, naam_b, 12, AMBER, vet=True))
    # de drie gebieden; het middelste ligt precies tussen de twee middelpunten
    for tekst, x, kleur in ((enkel_a, cxa - 48, DARK),
                            (samen, (cxa + cxb) / 2, INK),
                            (enkel_b, cxb + 48, DARK)):
        for i, regel in enumerate(str(tekst).split("\n")):
            d.append(_tekst(x, cy + 4 + i * 15, regel, 11.5, kleur))
    if buiten:
        d.append(_tekst(breedte / 2, h - 8, buiten, 10, DIM))
    return _svg(breedte, h, "".join(d))


def frequentietabel(paren, breedte=470, koppen=("waarde", "hoe vaak")):
    """Een frequentietabel: elke waarde met het aantal keer dat ze voorkomt."""
    n = len(paren)
    kolom = min(84, (breedte - 130) / n)
    x0 = 110
    rij_y = [56, 94]
    d = [f'<rect x="{x0}" y="{rij_y[0]-22}" width="{kolom*n}" height="88" fill="{PAPER}" '
         f'stroke="{BORDER}" stroke-width="1.2"/>']
    for r, kop in enumerate(koppen):
        d.append(_tekst(x0 - 12, rij_y[r] + 4, kop, 10.5, DIM, anker="end"))
    for i, (links, rechts) in enumerate(paren):
        cx = x0 + kolom * i + kolom / 2
        if i:
            d.append(f'<line x1="{x0+kolom*i}" y1="{rij_y[0]-22}" x2="{x0+kolom*i}" '
                     f'y2="{rij_y[0]+66}" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(cx, rij_y[0] + 4, str(links), 12, DARK, vet=True))
        d.append(_tekst(cx, rij_y[1] + 4, str(rechts), 12, FOREST, vet=True))
    d.append(f'<line x1="{x0}" y1="{rij_y[0]+20}" x2="{x0+kolom*n}" y2="{rij_y[0]+20}" '
             f'stroke="{BORDER}" stroke-width="1.2"/>')
    totaal = sum(int(r) for _, r in paren)
    d.append(_tekst(x0 + kolom * n / 2, rij_y[1] + 46, f"samen {totaal} metingen", 10, DIM))
    return _svg(breedte, 152, "".join(d))


def middelmaten(getallen, breedte=470):
    """De getallen op een rij, met de mediaan en het gemiddelde aangeduid."""
    gesorteerd = sorted(getallen)
    n = len(gesorteerd)
    gem = sum(gesorteerd) / n
    if n % 2:
        med = gesorteerd[n // 2]
    else:
        med = (gesorteerd[n // 2 - 1] + gesorteerd[n // 2]) / 2
    laag, hoog = gesorteerd[0], gesorteerd[-1]
    marge = 56
    span = max(hoog - laag, 1)
    h = 150

    def px(waarde):
        return marge + (waarde - laag) / span * (breedte - 2 * marge)

    d = [f'<line x1="{marge-14}" y1="86" x2="{breedte-marge+14}" y2="86" '
         f'stroke="{BORDER}" stroke-width="2"/>']
    for g in gesorteerd:
        d.append(f'<circle cx="{px(g)}" cy="86" r="5.5" fill="{FOREST}"/>')
        d.append(_tekst(px(g), 108, str(g), 10.5, DIM))
    for waarde, naam, kleur, y in ((med, "mediaan", AMBER, 52), (gem, "gemiddelde", "#5b7f9c", 32)):
        d.append(f'<line x1="{px(waarde)}" y1="{y+6}" x2="{px(waarde)}" y2="80" '
                 f'stroke="{kleur}" stroke-width="1.6" stroke-dasharray="4 3"/>')
        tekst = f"{naam} {str(waarde).replace('.', ',').removesuffix(',0')}"
        anker = "start" if px(waarde) < breedte / 2 else "end"
        schuif = 7 if anker == "start" else -7
        d.append(_tekst(px(waarde) + schuif, y + 4, tekst, 10.5, kleur, anker=anker, vet=True))
    d.append(_tekst(breedte / 2, h - 12,
                    f"variatiebreedte: {hoog} − {laag} = {hoog - laag}", 10, DIM))
    return _svg(breedte, h, "".join(d))


# ---------------------------------------------------------------------------
# 🧱 Basis — de bouwstenen van wiskunde
# ---------------------------------------------------------------------------

def cijfertabel(koppen, rijen, breedte=470, accent=None, labelbreedte=130):
    """Een tabel met één cijfer per vakje: de plaatswaardetabel (D H T E t h d)
    of de herleidingstabel voor maten (km hm dam m …).

    rijen: lijst van dicts met
      cijfers    — één tekst per kolom ("" voor een leeg vakje)
      komma      — na welke kolom (index) de komma staat, of None
      label      — tekst rechts van de rij, bv. "= 3,5 km"
      bijgezet   — indices van nullen die je zelf moest bijzetten (amber)
    accent: index van de kolom waarvan de kop in het groen staat (E, m, g, l).
    """
    n = len(koppen)
    cel = min(44, (breedte - labelbreedte) / n)
    x0 = 4
    kop_h, rij_h, gap = 26, 34, 10
    d = []
    for i, k in enumerate(koppen):
        x = x0 + i * cel
        vul = FOREST if i == accent else "#ffffff"
        kl = "#ffffff" if i == accent else DARK
        d.append(f'<rect x="{x+2:.1f}" y="4" width="{cel-4:.1f}" height="{kop_h}" rx="6" '
                 f'fill="{vul}" stroke="{DARK}" stroke-width="1.2"/>')
        d.append(_tekst(x + cel / 2, 4 + kop_h / 2 + 4, k, 11, kl, vet=True))
    for r, rij in enumerate(rijen):
        y = 4 + kop_h + gap + r * (rij_h + gap)
        bijgezet = set(rij.get("bijgezet", ()))
        for i, c in enumerate(rij["cijfers"]):
            x = x0 + i * cel
            extra = i in bijgezet
            rand = AMBER if extra else BORDER
            streep = ' stroke-dasharray="4 3"' if extra else ""
            d.append(f'<rect x="{x+2:.1f}" y="{y}" width="{cel-4:.1f}" height="{rij_h}" rx="6" '
                     f'fill="#ffffff" stroke="{rand}" stroke-width="1.4"{streep}/>')
            if c:
                d.append(_tekst(x + cel / 2, y + rij_h / 2 + 6, c, 16, AMBER if extra else INK, vet=True))
        if rij.get("komma") is not None:
            kx = x0 + (rij["komma"] + 1) * cel
            d.append(f'<circle cx="{kx:.1f}" cy="{y+rij_h-5}" r="4.2" fill="{AMBER}"/>')
        if rij.get("label"):
            d.append(_tekst(x0 + n * cel + 12, y + rij_h / 2 + 5, rij["label"], 12.5, DARK, anker="start", vet=True))
    h = 4 + kop_h + gap + len(rijen) * (rij_h + gap)
    return _svg(breedte, h, "".join(d))


def kommasprong(getal, sprongen, som, breedte=470):
    """De komma springt: bij × 10 één plaats naar rechts, bij : 10 één naar links.

    getal    — zoals je het schrijft, bv. "3,45" of "45"
    sprongen — +2 is twee plaatsen naar rechts (× 100), -3 drie naar links
    som      — de tekst erboven, bv. "3,45 × 100 = 345"
    Nullen die je moet bijzetten, staan in een amberkleurig stippelvakje.
    """
    heel, _, deel = getal.partition(",")
    cijfers = heel + deel
    oud = len(heel)
    nieuw = oud + sprongen
    links = max(0, 1 - nieuw)
    rechts = max(0, nieuw - len(cijfers))
    cijfers = "0" * links + cijfers + "0" * rechts
    oud += links
    nieuw += links
    extra = set(range(links)) | set(range(len(cijfers) - rechts, len(cijfers)))

    cel = 40
    b = len(cijfers) * cel
    x0 = (breedte - b) / 2
    y = 70
    hh = 40
    d = [_tekst(breedte / 2, 22, som, 15, DARK, vet=True)]
    for i, c in enumerate(cijfers):
        x = x0 + i * cel
        rand = AMBER if i in extra else BORDER
        streep = ' stroke-dasharray="4 3"' if i in extra else ""
        d.append(f'<rect x="{x+3:.1f}" y="{y}" width="{cel-6}" height="{hh}" rx="7" '
                 f'fill="#ffffff" stroke="{rand}" stroke-width="1.5"{streep}/>')
        d.append(_tekst(x + cel / 2, y + hh / 2 + 7, c, 19, AMBER if i in extra else INK, vet=True))
    # de oude komma, grijs en open
    ox = x0 + oud * cel
    d.append(f'<circle cx="{ox:.1f}" cy="{y+hh-4}" r="4.6" fill="#ffffff" stroke="{DIM}" stroke-width="1.5"/>')
    # de sprongen, één boogje per plaats
    stap = 1 if sprongen > 0 else -1
    for k in range(abs(sprongen)):
        a = ox + k * stap * cel
        z = a + stap * cel
        d.append(f'<path d="M{a:.1f} {y-4} Q{(a+z)/2:.1f} {y-26} {z:.1f} {y-4}" fill="none" '
                 f'stroke="{AMBER}" stroke-width="1.8"/>')
        d.append(f'<polygon points="{z:.1f},{y-3} {z-stap*7:.1f},{y-8} {z-stap*2:.1f},{y-11}" fill="{AMBER}"/>')
    # de nieuwe komma, vol amber — tenzij ze achteraan staat: dan is het een geheel getal
    nx = x0 + nieuw * cel
    if nieuw < len(cijfers):
        d.append(f'<circle cx="{nx:.1f}" cy="{y+hh-4}" r="5.2" fill="{AMBER}"/>')
    else:
        d.append(f'<circle cx="{nx:.1f}" cy="{y+hh-4}" r="5.2" fill="none" stroke="{AMBER}" stroke-width="1.6" stroke-dasharray="2 2"/>')
    return _svg(breedte, y + hh + 12, "".join(d))


def benoemde_som(delen, breedte=470, grootte=26):
    """Een bewerking in groot, met onder elk deel zijn naam.

    delen: lijst van (tekst, naam) — naam None voor tekens als + of =.
    Bv. [("20", "deeltal"), (":", None), ("3", "deler"), ("=", None),
         ("6", "quotiënt"), ("rest 2", "rest")]
    """
    breedtes = [max(len(t) * grootte * 0.62, 30 if n is None else 70) + 14 for t, n in delen]
    totaal = sum(breedtes)
    x = (breedte - totaal) / 2
    d = []
    for (tekst, naam), bw in zip(delen, breedtes):
        cx = x + bw / 2
        kleur = DIM if naam is None else INK
        d.append(_tekst(cx, 44, tekst, grootte, kleur, vet=naam is not None))
        if naam:
            d.append(f'<line x1="{cx:.1f}" y1="54" x2="{cx:.1f}" y2="66" stroke="{AMBER}" stroke-width="1.5"/>')
            d.append(_tekst(cx, 82, naam, 11.5, FOREST, vet=True))
        x += bw
    return _svg(breedte, 92, "".join(d))


def breuk_namen(teller=3, noemer=4, breedte=470):
    """Een grote breuk met pijltjes naar teller, breukstreep en noemer, en
    rechts een strook in `noemer` stukken waarvan er `teller` gekleurd zijn."""
    d = []
    bx = 70
    d.append(_tekst(bx, 60, str(teller), 40, INK, vet=True))
    d.append(f'<line x1="{bx-26}" y1="78" x2="{bx+26}" y2="78" stroke="{INK}" stroke-width="3.2"/>')
    d.append(_tekst(bx, 126, str(noemer), 40, INK, vet=True))
    uitleg = [
        (36, "teller", "hoeveel stukken je neemt"),
        (78, "breukstreep", "betekent 'gedeeld door'"),
        (120, "noemer", "in hoeveel gelijke stukken"),
    ]
    for y, naam, wat in uitleg:
        d.append(f'<line x1="{bx+32}" y1="{y}" x2="{bx+62}" y2="{y}" stroke="{AMBER}" stroke-width="1.5"/>')
        d.append(_tekst(bx + 68, y + 4, naam, 12, FOREST, anker="start", vet=True))
        d.append(_tekst(bx + 68, y + 18, wat, 9.5, DIM, anker="start"))
    sx, sb, sh = 300, breedte - 306, 40
    for k in range(noemer):
        x = sx + k * sb / noemer
        vul = FOREST if k < teller else "#ffffff"
        d.append(f'<rect x="{x:.1f}" y="58" width="{sb/noemer:.1f}" height="{sh}" fill="{vul}" '
                 f'stroke="{DARK}" stroke-width="1.4"/>')
    d.append(_tekst(sx + sb / 2, 118, f"{teller} van de {noemer} gelijke stukken", 10, DIM))
    return _svg(breedte, 142, "".join(d))


def groepjes(totaal, per, breedte=470):
    """Stippen verdeeld in groepjes van `per`, met wat overblijft in amber.
    Toont een deling met rest: 20 : 3 = 6, rest 2."""
    aantal, rest = divmod(totaal, per)
    r = 7
    stap = 2 * r + 5
    groep_b = per * stap + 14
    gap = 10
    per_rij = max(1, int((breedte + gap) // (groep_b + gap)))
    d = []
    blokken = [(per, FOREST)] * aantal + ([(rest, AMBER)] if rest else [])
    for i, (n, kleur) in enumerate(blokken):
        rij, kol = divmod(i, per_rij)
        x = kol * (groep_b + gap)
        y = rij * 44
        rest_blok = kleur == AMBER
        d.append(f'<rect x="{x+1}" y="{y+4}" width="{groep_b-2 if not rest_blok else n*stap+12}" height="30" rx="15" '
                 f'fill="none" stroke="{kleur}" stroke-width="1.4"'
                 + (' stroke-dasharray="4 3"' if rest_blok else "") + '/>')
        for k in range(n):
            d.append(f'<circle cx="{x + 8 + r + k*stap:.1f}" cy="{y+19}" r="{r}" fill="{kleur}"/>')
    rijen = (len(blokken) + per_rij - 1) // per_rij
    return _svg(breedte, rijen * 44 + 2, "".join(d))


def rijtjes(rijen, breedte=470, labelbreedte=118):
    """Rijtjes getallen als bolletjes: delers of veelvouden van twee getallen.

    rijen: lijst van (label, getallen, gemeenschappelijk, omcirkeld)
      gemeenschappelijk — getallen die in beide rijen staan (groen gevuld)
      omcirkeld         — het ene getal waar het om draait (amber ring)
    Een getal None tekent "…" (de rij gaat verder).
    """
    d = []
    for r, (label, getallen, samen, rond) in enumerate(rijen):
        y = 8 + r * 46
        d.append(_tekst(0, y + 22, label, 10.5, DARK, anker="start", vet=True))
        stap = min(42, (breedte - labelbreedte) / max(1, len(getallen)))
        for i, g in enumerate(getallen):
            cx = labelbreedte + i * stap + stap / 2
            if g is None:
                d.append(_tekst(cx, y + 22, "…", 13, DIM))
                continue
            gevuld = g in samen
            vul = FOREST if gevuld else "#ffffff"
            kl = "#ffffff" if gevuld else INK
            d.append(f'<circle cx="{cx:.1f}" cy="{y+18}" r="15" fill="{vul}" stroke="{FOREST if gevuld else BORDER}" stroke-width="1.4"/>')
            if g == rond:
                d.append(f'<circle cx="{cx:.1f}" cy="{y+18}" r="19.5" fill="none" stroke="{AMBER}" stroke-width="2.4"/>')
            d.append(_tekst(cx, y + 22.5, str(g), 11.5, kl, vet=True))
    return _svg(breedte, 8 + len(rijen) * 46, "".join(d))


def dubbele_getallenlijn(links, rechts, merken, breedte=470):
    """Een getallenlijn met boven elk streepje de breuk en eronder het kommagetal:
    hetzelfde punt, twee namen.  merken = lijst van (waarde, boven, onder)."""
    m = 64
    y = 50
    def x(v):
        return m + (v - links) / (rechts - links) * (breedte - 2 * m)
    d = [f'<line x1="{m}" y1="{y}" x2="{breedte-m}" y2="{y}" stroke="{INK}" stroke-width="2"/>',
         f'<path d="M{breedte-m+8} {y} l-9 -5 v10 z" fill="{INK}"/>']
    for waarde, boven, onder in merken:
        px = x(waarde)
        geheel = float(waarde).is_integer()
        d.append(f'<line x1="{px:.1f}" y1="{y-10}" x2="{px:.1f}" y2="{y+10}" stroke="{DARK if geheel else FOREST}" stroke-width="{2.6 if geheel else 2}"/>')
        if boven:
            d.append(_tekst(px, y - 18, boven, 12, FOREST, vet=True))
        if onder:
            d.append(_tekst(px, y + 28, onder, 12, AMBER, vet=True))
    d.append(_tekst(4, y - 18, "breuk", 9, DIM, anker="start"))
    d.append(_tekst(4, y + 28, "komma", 9, DIM, anker="start"))
    return _svg(breedte, y + 40, "".join(d))
