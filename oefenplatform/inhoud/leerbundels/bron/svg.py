# -*- coding: utf-8 -*-
"""Kleine tekenhulpjes voor de illustraties in de leerbundels."""

FOREST = "#2f5d50"
DARK = "#234539"
AMBER = "#c17f2b"
INK = "#23291f"
DIM = "#6b7260"
BORDER = "#e4ded0"
PAPER = "#ffffff"   # dezelfde kleur als --paper in stijl.css: het blad zelf

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


def staafdiagram(paren, breedte=330, hoogte=180, kleur=None, stap=None,
                 waarden=False):
    """paren = [(label, waarde), ...]

    stap bepaalt om de hoeveel de streepjes op de zij-as staan. Laat je hem
    weg, dan kiest de tekening er zelf vier, wat niet altijd ronde getallen
    geeft — bij grote waarden zet je hem dus beter zelf.

    waarden=True zet de waarde boven elke staaf. Doe dat zodra er één grote
    uitschieter tussen staat: de kleine staven worden dan zo laag dat je ze
    van de as niet meer kan aflezen, en dan valt de tekst eronder niet meer
    na te rekenen.
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
        if waarden:
            d.append(f'<text x="{x+bb/2:.1f}" y="{hoogte-onder-h-4:.1f}" text-anchor="middle" '
                     f'font-family="IBM Plex Sans,sans-serif" font-size="10" font-weight="600" '
                     f'fill="{INK}">{w}</text>')
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


def lijngrafiek(punten, breedte=330, hoogte=180, labels=None, stap=None):
    """punten = [waarde, ...], labels = wat er onder elk punt staat.

    stap bepaalt om de hoeveel de streepjes met getallen op de zij-as staan.
    Laat je hem weg, dan staat er geen enkel getal op die as, en dan valt er
    uit de lijn niets af te lezen. Zet hem dus zodra de hoogte zelf iets
    betekent.
    """
    links, onder, boven = 30, 28, 14
    top = max(punten)
    n = len(punten)
    vlak = hoogte - onder - boven
    breed = (breedte - links - 10) / (n - 1)
    d = [f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte}" y2="{hoogte-onder}" stroke="{DIM}" stroke-width="1.4"/>']
    if stap:
        for s in range(0, int(top) + 1, stap):
            y = hoogte - onder - s / top * vlak
            d.append(f'<line x1="{links-4}" y1="{y:.1f}" x2="{links}" y2="{y:.1f}" stroke="{DIM}" stroke-width="1.2"/>')
            d.append(f'<text x="{links-7}" y="{y+3.5:.1f}" text-anchor="end" font-family="IBM Plex Sans,sans-serif" font-size="9.5" fill="{DIM}">{s}</text>')
    pts = []
    for i, w in enumerate(punten):
        x = links + i * breed
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
    # 14 px lucht bovenaan: anders steekt het woord "hoogtepunt" boven de
    # viewBox uit, en dat wordt niet afgeknipt maar half getoond.
    h = 192
    top = 14
    basis = 128 + top
    d = [f'<path d="M30 {basis} C 150 {basis-10}, 210 {40+top}, 300 {34+top} C 360 {30+top}, 400 {70+top}, {breedte-30} {basis}" '
         f'fill="none" stroke="{FOREST}" stroke-width="2.6"/>']
    # de labels staan bewust aan de kant waar de lijn niet loopt,
    # anders snijdt de boog dwars door de tekst
    punten = [(30, basis, "begin", "wie, waar, wanneer", "onder"),
              (170, basis - 46, "probleem", "er loopt iets mis", "boven"),
              (300, 34 + top, "hoogtepunt", "het spannendst", "boven"),
              (breedte - 30, basis, "einde", "het loopt af", "onder")]
    for x, y, naam, onder, kant in punten:
        d.append(f'<circle cx="{x}" cy="{y:.0f}" r="5" fill="{AMBER}"/>')
        anker = "start" if x < 100 else ("end" if x > breedte - 100 else "middle")
        if kant == "boven":
            yn, yo = y - 36, y - 22
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


def _lampje(cx, cy, r, aan=True):
    kleur = AMBER if aan else DIM
    vul = "#fff8e6" if aan else "#eeece7"
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{vul}" stroke="{kleur}" stroke-width="2.2"/>'
            f'<path d="M{cx-r*0.5:.1f} {cy-r*0.5:.1f} l{r:.1f} {r:.1f} '
            f'M{cx+r*0.5:.1f} {cy-r*0.5:.1f} l{-r:.1f} {r:.1f}" stroke="{kleur}" stroke-width="1.8"/>')


def stroomkring(breedte=380, dicht=False):
    """Een stroomkring met batterij, lampje en schakelaar.

    Staat de schakelaar open, dan brandt het lampje niet. Anders zegt de
    tekening het omgekeerde van het bijschrift.
    """
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
    d.append(_lampje(mx, y0, 14, dicht))
    d.append(f'<text x="{mx}" y="{y0-24}" text-anchor="middle" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">lampje</text>')
    # schakelaar, rechts
    d.append(f'<rect x="{x1-9}" y="{(y0+y1)/2-18}" width="18" height="36" fill="{PAPER}" stroke="none"/>')
    d.append(f'<circle cx="{x1}" cy="{(y0+y1)/2-16}" r="3" fill="{DARK}"/>')
    d.append(f'<circle cx="{x1}" cy="{(y0+y1)/2+16}" r="3" fill="{DARK}"/>')
    mid = (y0 + y1) / 2
    eind = (x1, mid - 16) if dicht else (x1 + 13, mid - 12)
    d.append(f'<line x1="{x1}" y1="{mid+16}" x2="{eind[0]}" y2="{eind[1]}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>')
    # het label binnen de kring: rechts is er geen plaats en onder de schakelaar
    # zou het dwars over de draad vallen
    d.append(f'<text x="{x1-16}" y="{mid+4}" text-anchor="end" font-family="IBM Plex Sans,sans-serif" font-size="10.5" fill="{DIM}">schakelaar</text>')
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
    # 162 en niet 150: bij 150 stak de top van het fronton boven de viewBox uit.
    vloer = 162

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


# ---------------------------------------------------------------------------
# Wetenschap en techniek. Alles hieronder is zelf getekend: schema's, geen
# afbeeldingen van iemand anders.
# ---------------------------------------------------------------------------

BLOED_ARM = "#5b93b8"     # zuurstofarm bloed, naar de longen toe
BLOED_RIJK = "#c0392b"    # zuurstofrijk bloed, van de longen weg
SPIER = "#c0705f"
BOT = "#efe7d6"


def bloedsomloop(breedte=470):
    """De kleine en de grote bloedsomloop als één schema.

    Links gaat het zuurstofarme bloed omhoog, rechts komt het zuurstofrijke
    terug naar beneden. Dat is het hele punt: het bloed passeert twee keer
    langs het hart voor het één volledig rondje gemaakt heeft.
    """
    h = 236
    mid = breedte / 2
    kader_b, kader_h = 168, 40
    rijen = [(26, "de longen", "hier komt zuurstof bij"),
             (105, "het hart", "pompt alles rond"),
             (184, "de rest van je lichaam", "hier wordt zuurstof verbruikt")]
    d = []
    for y, naam, onder in rijen:
        vul = "#ffffff" if naam != "het hart" else "#fdeceb"
        d.append(f'<rect x="{mid-kader_b/2:.1f}" y="{y}" width="{kader_b}" height="{kader_h}" rx="9" '
                 f'fill="{vul}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(_tekst(mid, y + 17, naam, 11, DARK, "middle", True))
        d.append(_tekst(mid, y + 31, onder, 9, DIM))

    def pijl(x, y_van, y_naar, kleur, label, kant):
        """Een verticale pijl naast de kaders, met haar naam ernaast."""
        punt = -1 if y_naar < y_van else 1
        eind = y_naar - punt * 7
        d.append(f'<line x1="{x}" y1="{y_van}" x2="{x}" y2="{eind}" stroke="{kleur}" '
                 f'stroke-width="4" stroke-linecap="round"/>')
        d.append(f'<path d="M{x-6} {eind} L{x} {y_naar} L{x+6} {eind} Z" fill="{kleur}"/>')
        anker = "end" if kant == "links" else "start"
        lx = x - 11 if kant == "links" else x + 11
        d.append(_tekst(lx, (y_van + y_naar) / 2 + 3, label, 9, kleur, anker))

    links = mid - kader_b / 2 - 22
    rechts = mid + kader_b / 2 + 22
    pijl(links, 105, 66, BLOED_ARM, "zuurstofarm", "links")
    pijl(links, 184, 145, BLOED_ARM, "zuurstofarm", "links")
    pijl(rechts, 66, 105, BLOED_RIJK, "zuurstofrijk", "rechts")
    pijl(rechts, 145, 184, BLOED_RIJK, "zuurstofrijk", "rechts")

    return _svg(breedte, h, "".join(d))


def spierpaar(breedte=470):
    """Waarom spieren in paren zitten: een spier kan alleen trekken.

    Links de arm geplooid, rechts gestrekt. Telkens is de spier die samentrekt
    kort en dik getekend, en de andere lang en dun. Het bot staat bovenop de
    spieren getekend, want anders verdwijnt het achter het vlees.
    """
    h = 208
    half = breedte / 2 - 8
    d = []

    def bot(x1, y1, x2, y2):
        d.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{DARK}" stroke-width="13" stroke-linecap="round"/>')
        d.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{BOT}" stroke-width="11" stroke-linecap="round"/>')

    def arm(x0, titel, geplooid):
        d.append(f'<rect x="{x0:.1f}" y="6" width="{half:.1f}" height="{h-16}" rx="10" '
                 f'fill="{PAPER}" stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(_tekst(x0 + half / 2, 26, titel, 11.5, FOREST, "middle", True))

        as_x = x0 + 96
        schouder, elleboog = (as_x, 58), (as_x, 136)
        hand = (as_x + 48, 182) if geplooid else (as_x, 196)

        # Eerst de spieren, dan de botten eroverheen.
        for kant, naam, werkt in [(-1, "buigspier", geplooid), (1, "strekspier", not geplooid)]:
            dik = 11 if werkt else 6
            hoog = 29 if werkt else 39
            cy = 93 if werkt else 97
            cx = as_x + kant * 20
            d.append(f'<line x1="{cx}" y1="{cy-hoog}" x2="{as_x}" y2="58" stroke="{SPIER}" '
                     f'stroke-width="2.4" opacity="0.8"/>')
            d.append(f'<line x1="{cx}" y1="{cy+hoog}" x2="{as_x+kant*4}" y2="140" stroke="{SPIER}" '
                     f'stroke-width="2.4" opacity="0.8"/>')
            d.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{dik}" ry="{hoog}" fill="{SPIER}" '
                     f'opacity="{0.95 if werkt else 0.38}" stroke="{DARK}" stroke-width="1.1"/>')
            anker = "end" if kant < 0 else "start"
            lx = cx - dik - 7 if kant < 0 else cx + dik + 7
            d.append(_tekst(lx, cy - 2, naam, 9.5, DARK if werkt else DIM, anker, werkt))
            d.append(_tekst(lx, cy + 11, "trekt samen" if werkt else "ontspant", 9,
                            DARK if werkt else DIM, anker))

        bot(*schouder, *elleboog)
        bot(*elleboog, *hand)
        d.append(f'<circle cx="{elleboog[0]}" cy="{elleboog[1]}" r="6" fill="#ffffff" '
                 f'stroke="{DARK}" stroke-width="1.5"/>')
        d.append(_tekst(elleboog[0] - 14, elleboog[1] + 4, "elleboog", 9, DIM, "end"))

    arm(0, "arm geplooid", True)
    arm(breedte - half, "arm gestrekt", False)
    return _svg(breedte, h, "".join(d))


def schaduw(breedte=470):
    """Waarom een schaduw ontstaat: licht gaat in rechte lijnen."""
    h = 226
    lamp = (56, 112)
    voor_x1, voor_x2, voor_y1, voor_y2 = 178, 196, 96, 128
    scherm = 404
    d = [f'<rect x="{scherm}" y="24" width="14" height="168" rx="3" fill="{STEEN}" '
         f'stroke="{DARK}" stroke-width="1.4"/>']

    def straal(py, kleur, dik, streep=""):
        helling = (py - lamp[1]) / (voor_x2 - lamp[0])
        y_eind = lamp[1] + (scherm - lamp[0]) * helling
        d.append(f'<line x1="{lamp[0]}" y1="{lamp[1]}" x2="{scherm}" y2="{y_eind:.1f}" '
                 f'stroke="{kleur}" stroke-width="{dik}"{streep}/>')
        return y_eind

    boven = straal(voor_y1, AMBER, 1.4)
    onder = straal(voor_y2, AMBER, 1.4)
    for py in (voor_y1 - 10, voor_y2 + 10):
        straal(py, AMBER, 1.2, ' opacity="0.45"')

    # De schaduw zelf, als een donkere band op het scherm.
    d.append(f'<rect x="{scherm}" y="{boven:.1f}" width="14" height="{onder-boven:.1f}" '
             f'fill="{DARK}"/>')

    d.append(f'<rect x="{voor_x1}" y="{voor_y1}" width="{voor_x2-voor_x1}" '
             f'height="{voor_y2-voor_y1}" rx="3" fill="{FOREST}" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<circle cx="{lamp[0]}" cy="{lamp[1]}" r="13" fill="{AMBER}"/>')
    for hoek in range(0, 360, 45):
        import math
        r = math.radians(hoek)
        d.append(f'<line x1="{lamp[0]+16*math.cos(r):.1f}" y1="{lamp[1]+16*math.sin(r):.1f}" '
                 f'x2="{lamp[0]+22*math.cos(r):.1f}" y2="{lamp[1]+22*math.sin(r):.1f}" '
                 f'stroke="{AMBER}" stroke-width="2" stroke-linecap="round"/>')

    d.append(_tekst(lamp[0], h - 24, "lichtbron", 9.5, DIM))
    d.append(_tekst((voor_x1 + voor_x2) / 2, h - 24, "voorwerp", 9.5, DIM))
    d.append(_tekst(scherm + 7, h - 24, "scherm", 9.5, DIM))
    d.append(_kussen(scherm - 12, (boven + onder) / 2 + 3, "schaduw", 9.5, DARK, "end", True))
    return _svg(breedte, h, "".join(d))


def spiegel_weerkaatsing(breedte=470):
    """Licht kaatst van een spiegel terug onder dezelfde hoek."""
    import math
    h = 192
    top = (235, 150)
    d = []
    # De spiegel, met arcering eronder zodat je ziet welke kant de achterkant is.
    d.append(f'<line x1="86" y1="150" x2="384" y2="150" stroke="{DARK}" stroke-width="3"/>')
    for x in range(90, 381, 14):
        d.append(f'<line x1="{x}" y1="150" x2="{x-8}" y2="162" stroke="{DIM}" stroke-width="1.1"/>')
    d.append(_tekst(384, 176, "de spiegel", 9.5, DIM, "end"))

    d.append(f'<line x1="{top[0]}" y1="{top[1]}" x2="{top[0]}" y2="46" stroke="{DIM}" '
             f'stroke-width="1.3" stroke-dasharray="5 4"/>')
    d.append(_tekst(top[0] + 6, 52, "loodlijn", 9, DIM, "start"))

    for van, naar, label, lx in [((115, 60), top, "invallende straal", 115),
                                 (top, (355, 60), "teruggekaatste straal", 355)]:
        d.append(f'<line x1="{van[0]}" y1="{van[1]}" x2="{naar[0]}" y2="{naar[1]}" '
                 f'stroke="{AMBER}" stroke-width="2.6"/>')
    # Pijlpunten die de looprichting aangeven.
    for (x, y, dx, dy) in [(178, 106, 4, 3), (296, 104, 4, -3)]:
        hoek = math.degrees(math.atan2(dy, dx))
        d.append(f'<polygon points="0,-5 11,0 0,5" fill="{AMBER}" '
                 f'transform="translate({x},{y}) rotate({hoek:.1f})"/>')
    d.append(_tekst(112, 48, "invallende straal", 9.5, DARK, "middle"))
    d.append(_tekst(358, 48, "teruggekaatste straal", 9.5, DARK, "middle"))

    r = 34
    for kant in (-1, 1):
        px = top[0] + kant * r * math.sin(math.radians(53))
        py = top[1] - r * math.cos(math.radians(53))
        boog = f'M{px:.1f} {py:.1f} A {r} {r} 0 0 {1 if kant < 0 else 0} {top[0]} {top[1]-r}'
        d.append(f'<path d="{boog}" fill="none" stroke="{FOREST}" stroke-width="1.6"/>')
        mx = top[0] + kant * (r + 12) * math.sin(math.radians(26.5))
        my = top[1] - (r + 12) * math.cos(math.radians(26.5)) + 3
        d.append(_tekst(mx, my, "hoek", 9, FOREST, "middle"))
    return _svg(breedte, h, "".join(d))


def breking(breedte=470):
    """Waarom een rietje in een glas water geknikt lijkt."""
    h = 212
    gx1, gx2, gy1, gy2 = 156, 316, 46, 200
    water_y = 100
    d = [f'<rect x="{gx1}" y="{gy1}" width="{gx2-gx1}" height="{gy2-gy1}" rx="6" '
         f'fill="#ffffff" stroke="{DARK}" stroke-width="1.8"/>',
         f'<rect x="{gx1+2}" y="{water_y}" width="{gx2-gx1-4}" height="{gy2-water_y-2}" '
         f'rx="4" fill="{ZEE}" opacity="0.32"/>',
         f'<line x1="{gx1+2}" y1="{water_y}" x2="{gx2-2}" y2="{water_y}" stroke="{ZEE}" stroke-width="2"/>']
    d.append(_tekst(gx2 + 10, water_y + 4, "wateroppervlak", 9.5, DIM, "start"))

    knik = (252, water_y)
    for (x1, y1), (x2, y2) in [((306, 26), knik), (knik, (230, 192))]:
        d.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{AMBER}" '
                 f'stroke-width="9" stroke-linecap="round"/>')
    d.append(f'<circle cx="{knik[0]}" cy="{knik[1]}" r="4" fill="{DARK}"/>')
    d.append(f'<line x1="{gx1-6}" y1="{water_y-26}" x2="{knik[0]-10}" y2="{water_y-4}" '
             f'stroke="{DIM}" stroke-width="1.1"/>')
    d.append(_tekst(gx1 - 10, water_y - 24, "hier lijkt het geknikt", 9.5, DARK, "end"))
    return _svg(breedte, h, "".join(d))


def _golf(x0, x1, y, amplitude, golven, kleur, dik=2.2):
    import math
    punten = []
    n = 160
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        hoek = 2 * math.pi * golven * i / n
        punten.append(f"{x:.1f},{y - amplitude * math.sin(hoek):.1f}")
    return (f'<polyline points="{" ".join(punten)}" fill="none" stroke="{kleur}" '
            f'stroke-width="{dik}" stroke-linejoin="round"/>')


def geluidsgolf(breedte=470):
    """Hoog tegenover laag, en luid tegenover zacht, als golven getekend."""
    h = 238
    half = breedte / 2 - 8
    d = []

    def kader(x0, titel):
        d.append(f'<rect x="{x0:.1f}" y="6" width="{half:.1f}" height="{h-18}" rx="10" '
                 f'fill="{PAPER}" stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(_tekst(x0 + half / 2, 26, titel, 11.5, FOREST, "middle", True))

    kader(0, "hoog of laag")
    kader(breedte - half, "luid of zacht")

    for (x0, paren) in [(0, [("lage toon", 2, 17, 76), ("hoge toon", 6, 17, 158)]),
                        (breedte - half, [("zacht geluid", 4, 8, 76), ("luid geluid", 4, 24, 158)])]:
        for naam, golven, amp, y in paren:
            d.append(f'<line x1="{x0+18}" y1="{y}" x2="{x0+half-18}" y2="{y}" stroke="{BORDER}" '
                     f'stroke-width="1.2"/>')
            d.append(_golf(x0 + 18, x0 + half - 18, y, amp, golven, AMBER))
            d.append(_tekst(x0 + half / 2, y + 42, naam, 10, DARK, "middle", True))

    d.append(_tekst(half / 2, h - 26, "sneller trillen klinkt hoger", 9.5, DIM))
    d.append(_tekst(breedte - half / 2, h - 26, "groter trillen klinkt luider", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def _batterij(mx, y, achtergrond=PAPER):
    uit = [f'<rect x="{mx-28:.1f}" y="{y-9}" width="56" height="18" fill="{achtergrond}" stroke="none"/>']
    for dx, hh, dik in [(-12, 20, 2.6), (-2, 11, 4.5), (8, 20, 2.6), (18, 11, 4.5)]:
        uit.append(f'<line x1="{mx+dx:.1f}" y1="{y-hh/2}" x2="{mx+dx:.1f}" y2="{y+hh/2}" '
                   f'stroke="{DARK}" stroke-width="{dik}"/>')
    return "".join(uit)


def serie_parallel(breedte=470):
    """Twee lampjes na elkaar tegenover twee lampjes elk op hun eigen tak.

    Het verschil dat telt: gaat er één lampje stuk, dan is in serie de hele
    kring onderbroken, en bij een parallelschakeling alleen die ene tak.
    """
    h = 248
    half = breedte / 2 - 8
    ly0, ly1 = 58, 150
    d = []

    def kader(x0, titel):
        d.append(f'<rect x="{x0:.1f}" y="6" width="{half:.1f}" height="{h-18}" rx="10" '
                 f'fill="{PAPER}" stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(_tekst(x0 + half / 2, 28, titel, 11.5, FOREST, "middle", True))

    def lus(x0):
        a, b = x0 + 34, x0 + half - 34
        d.append(f'<rect x="{a}" y="{ly0}" width="{b-a}" height="{ly1-ly0}" rx="12" '
                 f'fill="none" stroke="{DARK}" stroke-width="2.4"/>')
        d.append(_batterij((a + b) / 2, ly1))
        d.append(_tekst((a + b) / 2, ly1 + 24, "batterij", 9.5, DIM))
        return a, b

    def lamp_op_draad(cx, cy):
        d.append(f'<rect x="{cx-15:.1f}" y="{cy-16}" width="30" height="32" fill="{PAPER}" stroke="none"/>')
        d.append(_lampje(cx, cy, 13))

    def slot(x0, boven, onder, kleur):
        d.append(_tekst(x0 + half / 2, h - 50, boven, 10, DARK, "middle", True))
        d.append(_tekst(x0 + half / 2, h - 34, onder, 10, kleur, "middle", True))

    kader(0, "in serie")
    a, b = lus(0)
    for cx in (a + (b - a) / 3, a + 2 * (b - a) / 3):
        lamp_op_draad(cx, ly0)
    slot(0, "één lampje stuk", "= allebei uit", BLOED_RIJK)

    x0 = breedte - half
    kader(x0, "parallel")
    a, b = lus(x0)
    tak = (a + b) / 2
    d.append(f'<line x1="{tak}" y1="{ly0}" x2="{tak}" y2="{ly1-14}" stroke="{DARK}" stroke-width="2.4"/>')
    for cx in ((a + tak) / 2, (tak + b) / 2):
        lamp_op_draad(cx, ly0)
    slot(x0, "één lampje stuk", "= het andere brandt door", FOREST)

    return _svg(breedte, h, "".join(d))


def staafmagneet(breedte=470):
    """Gelijke polen stoten af, verschillende trekken aan."""
    h = 212
    half = breedte / 2 - 8
    magneet_b, magneet_h = 64, 26
    y = 78
    d = []

    def magneet(x, polen):
        for i, naam in enumerate(polen):
            kleur = BLOED_RIJK if naam == "N" else "#3b6ea5"
            d.append(f'<rect x="{x+i*magneet_b/2:.1f}" y="{y}" width="{magneet_b/2}" '
                     f'height="{magneet_h}" fill="{kleur}" stroke="{DARK}" stroke-width="1.3"/>')
            d.append(_tekst(x + i * magneet_b / 2 + magneet_b / 4, y + magneet_h / 2 + 4,
                            naam, 12, "#ffffff", "middle", True))

    def paneel(x0, titel, rechtse_polen, naar_buiten, uitkomst, kleur):
        d.append(f'<rect x="{x0:.1f}" y="6" width="{half:.1f}" height="{h-16}" rx="10" '
                 f'fill="{PAPER}" stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(_tekst(x0 + half / 2, 28, titel, 11.5, FOREST, "middle", True))
        magneet(x0 + 34, ("Z", "N"))
        magneet(x0 + 129, rechtse_polen)
        # De pijlen staan náást het paar, niet ertussen: naar buiten is afstoten,
        # naar binnen is aantrekken. Tussen de magneten is er te weinig plaats.
        my = y + magneet_h / 2
        for binnen, buiten in [(x0 + 28, x0 + 6), (x0 + 199, x0 + 221)]:
            van, naar = (binnen, buiten) if naar_buiten else (buiten, binnen)
            d.append(f'<line x1="{van}" y1="{my}" x2="{naar}" y2="{my}" stroke="{kleur}" '
                     f'stroke-width="3.2" stroke-linecap="round"/>')
            richting = 1 if naar > van else -1
            d.append(f'<path d="M{naar+richting*7} {my} l{-8*richting} -5.5 l0 11 Z" fill="{kleur}"/>')
        d.append(_tekst(x0 + half / 2, y + 66, uitkomst, 10.5, kleur, "middle", True))

    paneel(0, "N tegenover N", ("N", "Z"), True, "ze duwen elkaar weg", BLOED_RIJK)
    paneel(breedte - half, "N tegenover Z", ("Z", "N"), False, "ze trekken elkaar aan", FOREST)
    d.append(_tekst(breedte / 2, h - 8,
                    "N is de noordpool, Z de zuidpool. Gelijke polen stoten af, verschillende trekken aan.",
                    9.5, DIM))
    return _svg(breedte, h, "".join(d))


def dag_en_nacht(breedte=470):
    """De aarde draait om haar as; de kant naar de zon heeft dag."""
    import math
    h = 212
    zon = (58, 116)
    aarde = (306, 116)
    r = 62
    knip = _id("dagnacht")
    d = [f'<clipPath id="{knip}"><circle cx="{aarde[0]}" cy="{aarde[1]}" r="{r}"/></clipPath>']

    # Zonnestralen, evenwijdig, want de zon staat onvoorstelbaar ver.
    for dy in range(-66, 67, 22):
        d.append(f'<line x1="{zon[0]+34}" y1="{aarde[1]+dy}" x2="{aarde[0]-r-12}" y2="{aarde[1]+dy}" '
                 f'stroke="{AMBER}" stroke-width="1.6"/>')
        d.append(f'<path d="M{aarde[0]-r-6} {aarde[1]+dy} l-9 -4.5 l0 9 Z" fill="{AMBER}"/>')

    d.append(f'<circle cx="{zon[0]}" cy="{zon[1]}" r="30" fill="{AMBER}"/>')
    for hoek in range(0, 360, 30):
        rr = math.radians(hoek)
        d.append(f'<line x1="{zon[0]+33*math.cos(rr):.1f}" y1="{zon[1]+33*math.sin(rr):.1f}" '
                 f'x2="{zon[0]+41*math.cos(rr):.1f}" y2="{zon[1]+41*math.sin(rr):.1f}" '
                 f'stroke="{AMBER}" stroke-width="2.4" stroke-linecap="round"/>')
    d.append(_tekst(zon[0], zon[1] + 4, "zon", 11, "#ffffff", "middle", True))

    # De aarde: linkerhelft verlicht, rechterhelft in het donker.
    d.append(f'<rect x="{aarde[0]-r}" y="{aarde[1]-r}" width="{r}" height="{2*r}" '
             f'fill="{ZEE}" opacity="0.45" clip-path="url(#{knip})"/>')
    d.append(f'<rect x="{aarde[0]}" y="{aarde[1]-r}" width="{r}" height="{2*r}" '
             f'fill="{DARK}" clip-path="url(#{knip})"/>')
    d.append(f'<circle cx="{aarde[0]}" cy="{aarde[1]}" r="{r}" fill="none" stroke="{DARK}" stroke-width="1.8"/>')

    # De scheve as, met de noordpool erop.
    scheef = math.radians(23.5)
    ax, ay = (r + 16) * math.sin(scheef), (r + 16) * math.cos(scheef)
    d.append(f'<line x1="{aarde[0]-ax:.1f}" y1="{aarde[1]+ay:.1f}" x2="{aarde[0]+ax:.1f}" '
             f'y2="{aarde[1]-ay:.1f}" stroke="{DARK}" stroke-width="2.2"/>')
    d.append(f'<circle cx="{aarde[0]+ax:.1f}" cy="{aarde[1]-ay:.1f}" r="3.5" fill="{DARK}"/>')
    d.append(_tekst(aarde[0] + ax + 8, aarde[1] - ay + 4, "noordpool", 9, DIM, "start"))

    d.append(_tekst(aarde[0] - 31, aarde[1] + 4, "dag", 12, DARK, "middle", True))
    d.append(_tekst(aarde[0] + 31, aarde[1] + 4, "nacht", 12, "#ffffff", "middle", True))
    d.append(_tekst(aarde[0], aarde[1] + r + 24, "de aarde draait in 24 uur één keer rond", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def _maanvorm(cx, cy, r, fase):
    """Het verlichte deel van de maan bij een fase tussen 0 en 1.

    0 is nieuwe maan, 0,5 is volle maan. De rand tussen licht en donker is
    een halve ellips; hoe platter die is, hoe dichter je bij kwartier zit.
    """
    import math
    k = math.cos(2 * math.pi * fase)
    rx = abs(k) * r
    wassend = fase < 0.5
    buiten_sweep = 1 if wassend else 0
    binnen_sweep = (1 if k < 0 else 0) if wassend else (0 if k < 0 else 1)
    return (f'M{cx} {cy-r} A {r} {r} 0 0 {buiten_sweep} {cx} {cy+r} '
            f'A {rx:.2f} {r} 0 0 {binnen_sweep} {cx} {cy-r} Z')


def maanfasen(breedte=470):
    """De acht standen van de maan, van nieuw naar vol en terug."""
    h = 186
    namen = ["nieuwe maan", "wassende sikkel", "eerste kwartier", "wassende maan",
             "volle maan", "afnemende maan", "laatste kwartier", "afnemende sikkel"]
    r = 21
    kolom = breedte / 4
    d = []
    for i, naam in enumerate(namen):
        rij, kol = divmod(i, 4)
        cx = kolom * kol + kolom / 2
        cy = 34 + rij * 86
        d.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="{r}" fill="{DARK}" stroke="{DARK}" stroke-width="1.2"/>')
        fase = i / 8
        if i:
            d.append(f'<path d="{_maanvorm(cx, cy, r, fase)}" fill="#f2efe4"/>')
        for j, regel in enumerate(naam.split(" ")):
            d.append(_tekst(cx, cy + r + 15 + j * 12, regel, 9.5, DARK))
    d.append(_tekst(breedte / 2, h - 6,
                    "De zon verlicht altijd de helft van de maan. Je kijkt er alleen elke avond anders tegenaan.",
                    9.5, DIM))
    return _svg(breedte, h, "".join(d))


def zonnestelsel(breedte=470):
    """De zon en de acht planeten op een rij, in de juiste volgorde."""
    h = 174
    planeten = [("Mercurius", 5.7, "#9a948a"), ("Venus", 6.6, "#d8b36a"),
                ("aarde", 6.8, "#4f86b0"), ("Mars", 5.9, "#a2521f"),
                ("Jupiter", 13.0, "#c9a173"), ("Saturnus", 12.3, "#dcc48d"),
                ("Uranus", 9.4, "#8fc4c9"), ("Neptunus", 9.3, "#4a6fae")]
    y = 74
    x0, x1 = 104, breedte - 24
    d = [f'<line x1="82" y1="{y}" x2="{x1}" y2="{y}" stroke="{BORDER}" stroke-width="1.4" '
         f'stroke-dasharray="5 5"/>']
    # De zon staat links, maar past niet heel: er is maar een rand van te zien.
    d.append(f'<path d="M20 {y-58} A 58 58 0 0 1 20 {y+58} Z" fill="{AMBER}"/>')
    d.append(_tekst(24, y + 4, "zon", 11, "#ffffff", "start", True))

    stap = (x1 - x0) / (len(planeten) - 1)
    for i, (naam, r, kleur) in enumerate(planeten):
        cx = x0 + i * stap
        if naam == "Saturnus":
            d.append(f'<ellipse cx="{cx:.1f}" cy="{y}" rx="{r*1.9:.1f}" ry="{r*0.5:.1f}" '
                     f'fill="none" stroke="{ZAND_DONKER}" stroke-width="2.4"/>')
        d.append(f'<circle cx="{cx:.1f}" cy="{y}" r="{r}" fill="{kleur}" stroke="{DARK}" stroke-width="1.2"/>')
        vet = naam == "aarde"
        d.append(_tekst(cx, y + 34 + (i % 2) * 14, naam, 9.5, DARK if vet else DIM, "middle", vet))
    d.append(_tekst(breedte / 2, h - 26, "Niet op schaal: in het echt staan de planeten "
                                         "duizenden keren verder uit elkaar,", 9.5, DIM))
    d.append(_tekst(breedte / 2, h - 12, "en past de aarde meer dan duizend keer in Jupiter.", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


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


def oude_graven(breedte=470):
    """Twee soorten graven uit de prehistorie naast elkaar.

    Links een hunebed of megalietgraf: zware staande stenen met daarop een
    platte deksteen. Rechts een grafheuvel, in doorsnede getekend, want het
    punt is juist dat het graf ónder de heuvel zit.
    """
    h = 186
    half = breedte / 2 - 8
    grond = 132
    d = []

    def kader(x0, titel):
        d.append(f'<rect x="{x0:.1f}" y="6" width="{half:.1f}" height="{h-16}" rx="10" '
                 f'fill="{PAPER}" stroke="{BORDER}" stroke-width="1.4"/>')
        d.append(_tekst(x0 + half / 2, 26, titel, 11.5, FOREST, "middle", True))

    kader(0, "hunebed")
    kader(breedte - half, "grafheuvel")

    # Links: vier staande stenen met twee dekstenen erop.
    d.append(f'<rect x="18" y="{grond}" width="{half-36:.1f}" height="11" rx="3" '
             f'fill="{ZAND}" opacity="0.55"/>')
    staand_top = grond - 46
    for x0 in [30, 72, 116, 158]:
        d.append(f'<rect x="{x0}" y="{staand_top}" width="21" height="46" rx="4" '
                 f'fill="{STEEN}" stroke="{DARK}" stroke-width="1.4"/>')
    for x0, br in [(20, 92), (116, 74)]:
        d.append(f'<rect x="{x0}" y="{staand_top-22}" width="{br}" height="22" rx="6" '
                 f'fill="{ROTS}" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(_tekst(half / 2, staand_top - 32, "dekstenen", 9.5, DIM))
    d.append(_tekst(half / 2, grond + 28, "staande stenen met een platte steen erop", 9.5, DIM))
    d.append(_tekst(half / 2, grond + 43, "de grafkamer ligt eronder", 9.5, DIM))

    # Rechts: de heuvel in doorsnede, met het graf op het oude loopvlak.
    bx = breedte - half
    mid = bx + half / 2
    d.append(f'<path d="M{bx+24:.1f} {grond} Q{mid:.1f} {grond-96} {bx+half-24:.1f} {grond} Z" '
             f'fill="{ZAND}" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<path d="M{bx+24:.1f} {grond} Q{mid:.1f} {grond-96} {bx+half-24:.1f} {grond}" '
             f'fill="none" stroke="{GRAS}" stroke-width="3"/>')
    d.append(f'<line x1="{bx+16:.1f}" y1="{grond}" x2="{bx+half-16:.1f}" y2="{grond}" '
             f'stroke="{DARK}" stroke-width="1.2" stroke-dasharray="5 4"/>')
    d.append(f'<rect x="{mid-26:.1f}" y="{grond-6}" width="52" height="22" rx="3" '
             f'fill="{PAPER}" stroke="{DARK}" stroke-width="1.3"/>')
    d.append(f'<circle cx="{mid:.1f}" cy="{grond+5}" r="6" fill="{OKER}" stroke="{DARK}" stroke-width="1"/>')
    d.append(f'<line x1="{mid-44:.1f}" y1="{grond-18}" x2="{mid-28:.1f}" y2="{grond+2}" '
             f'stroke="{DIM}" stroke-width="1.1"/>')
    d.append(_kussen(mid - 42, grond - 16, "het graf", 9.5, DIM, "end"))
    d.append(_tekst(mid, grond + 28, "een heuvel van aarde over het graf", 9.5, DIM))
    d.append(_tekst(mid, grond + 43, "hier in doorsnede getekend", 9.5, DIM))
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
    # Komt een waarde twee keer voor, dan stapelen we de bolletjes op elkaar.
    # Anders liggen ze precies over elkaar en lijkt de reeks korter dan ze is,
    # terwijl net dát zichtbaar moet zijn: hoeveel keer een waarde voorkomt.
    hoevaak = {}
    for g in gesorteerd:
        keer = hoevaak.get(g, 0)
        hoevaak[g] = keer + 1
        d.append(f'<circle cx="{px(g)}" cy="{86 - keer * 12}" r="5.5" fill="{FOREST}"/>')
        if keer == 0:
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


# ---------------------------------------------------------------------------
# Natuurwetenschappen ✨ Spark. Zelf getekende schema's bij de vakfiche
# natuurwetenschappen eerste graad A-stroom.
# ---------------------------------------------------------------------------

CELWAND = "#6f8f4a"
KERN = "#7a5b8f"


def twee_cellen(breedte=470):
    """Een plantaardige en een dierlijke cel naast elkaar, met labels.

    Het verschil moet je in één oogopslag zien: links de hoekige cel met
    celwand, bladgroenkorrels en één grote vacuole, rechts de ronde cel
    zonder die drie.
    """
    h = 228
    vak = breedte / 2
    d = []
    for i, soort in enumerate(("plantaardig", "dierlijk")):
        ox = i * vak
        cx, cy = ox + vak / 2, 108
        if soort == "plantaardig":
            d.append(f'<rect x="{ox+24}" y="36" width="{vak-48:.1f}" height="146" rx="10" '
                     f'fill="rgba(111,143,74,.10)" stroke="{CELWAND}" stroke-width="4.5"/>')
            d.append(f'<rect x="{ox+30}" y="42" width="{vak-60:.1f}" height="134" rx="8" '
                     f'fill="none" stroke="{FOREST}" stroke-width="1.8"/>')
            d.append(f'<rect x="{ox+46}" y="58" width="{vak-92:.1f}" height="66" rx="8" '
                     f'fill="rgba(91,147,184,.18)" stroke="#5b93b8" stroke-width="1.6"/>')
            d.append(_tekst(cx, 96, "vacuole", 9.5, "#3d6e8c"))
            for k, (bx, by) in enumerate(((0.30, 150), (0.52, 158), (0.72, 146))):
                d.append(f'<ellipse cx="{ox + vak*bx:.1f}" cy="{by}" rx="10" ry="6.5" '
                         f'fill="rgba(47,93,80,.35)" stroke="{FOREST}" stroke-width="1.4"/>')
            d.append(f'<circle cx="{ox + vak*0.34:.1f}" cy="134" r="12" fill="rgba(122,91,143,.28)" '
                     f'stroke="{KERN}" stroke-width="1.8"/>')
            d.append(f'<ellipse cx="{ox + vak*0.66:.1f}" cy="132" rx="11" ry="6" '
                     f'fill="rgba(193,127,43,.25)" stroke="{AMBER}" stroke-width="1.5"/>')
        else:
            d.append(f'<ellipse cx="{cx:.1f}" cy="{cy}" rx="{vak/2-30:.1f}" ry="70" '
                     f'fill="rgba(193,127,43,.08)" stroke="{FOREST}" stroke-width="2.4"/>')
            d.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="18" fill="rgba(122,91,143,.28)" '
                     f'stroke="{KERN}" stroke-width="1.8"/>')
            for bx, by in ((0.34, 84), (0.66, 86), (0.40, 140), (0.64, 138)):
                d.append(f'<ellipse cx="{ox + vak*bx:.1f}" cy="{by}" rx="11" ry="6" '
                         f'fill="rgba(193,127,43,.25)" stroke="{AMBER}" stroke-width="1.5"/>')
        d.append(_tekst(cx, 24, f"{soort}e cel", 11.5, DARK, vet=True))
    legende = [("celwand", CELWAND), ("celkern", KERN), ("mitochondrion", AMBER),
               ("bladgroenkorrel", FOREST)]
    x = 14
    for naam, kleur in legende:
        d.append(f'<rect x="{x}" y="206" width="13" height="13" rx="3" fill="{kleur}" opacity="0.55" '
                 f'stroke="{kleur}" stroke-width="1.4"/>')
        d.append(_tekst(x + 19, 217, naam, 9.5, DIM, anker="start"))
        x += len(naam) * 5.6 + 42
    return _svg(breedte, h, "".join(d))


def fotosynthese(breedte=470):
    """Wat er bij fotosynthese in en uit een blad gaat, met de omzetting erbij."""
    h = 226
    mx = breedte / 2
    d = [f'<path d="M{mx-96} 132 q40 -60 96 -44 q56 -16 96 44 q-96 40 -192 0 Z" '
         f'fill="rgba(47,93,80,.18)" stroke="{FOREST}" stroke-width="2.2"/>',
         f'<path d="M{mx-96} 132 h192" stroke="{FOREST}" stroke-width="1.4" opacity="0.5"/>']
    for k in range(-3, 4):
        d.append(f'<path d="M{mx + k*24} 132 q6 -22 0 -38" stroke="{FOREST}" stroke-width="1" '
                 f'fill="none" opacity="0.45"/>')
    # zon
    d.append(f'<circle cx="46" cy="38" r="17" fill="#f0c33c" stroke="{AMBER}" stroke-width="1.8"/>')
    for hoek in range(0, 360, 45):
        import math
        a = math.radians(hoek)
        d.append(f'<line x1="{46+22*math.cos(a):.1f}" y1="{38+22*math.sin(a):.1f}" '
                 f'x2="{46+29*math.cos(a):.1f}" y2="{38+29*math.sin(a):.1f}" '
                 f'stroke="{AMBER}" stroke-width="1.8" stroke-linecap="round"/>')
    d.append(_tekst(46, 76, "lichtenergie", 9.5, AMBER, vet=True))
    # naar_binnen: de pijl wijst naar het blad. naar_buiten: hij wijst ervandaan.
    pijlen = [(112, 66, mx - 60, 96, "CO₂ in", "#5b7f9c", True),
              (112, 150, mx - 60, 124, "H₂O in", "#5b93b8", True),
              (breedte - 112, 66, mx + 60, 96, "O₂ uit", FOREST, False),
              (breedte - 112, 150, mx + 60, 124, "glucose uit", AMBER, False)]
    for xb, yb, xblad, yblad, naam, kleur, naar_binnen in pijlen:
        if naar_binnen:
            begin, eind = (xb, yb), (xblad, yblad)
        else:
            begin, eind = (xblad, yblad), (xb, yb)
        d.append(f'<path d="M{begin[0]:.0f} {begin[1]:.0f} L{eind[0]:.0f} {eind[1]:.0f}" '
                 f'stroke="{kleur}" stroke-width="2.2" '
                 f'marker-end="url(#{_pijlpunt(kleur)})" fill="none"/>')
        d.append(_tekst(xb + (-8 if naar_binnen else 8), yb - 8, naam, 10, kleur,
                        anker="end" if naar_binnen else "start", vet=True))
    d.append(f'<rect x="{mx-168:.0f}" y="176" width="336" height="36" rx="9" fill="{PAPER}" '
             f'stroke="{BORDER}" stroke-width="1.4"/>')
    d.append(_tekst(mx, 199, "koolstofdioxide + water → glucose + zuurstofgas", 11.5, DARK, vet=True))
    return _svg(breedte, h, _pijlpunten() + "".join(d))


_PIJLKLEUREN = {}


def _pijlpunt(kleur):
    """Registreert een pijlpunt in die kleur en geeft het id terug."""
    if kleur not in _PIJLKLEUREN:
        _PIJLKLEUREN[kleur] = _id("punt")
    return _PIJLKLEUREN[kleur]


def _pijlpunten():
    """De <defs> met alle pijlpunten die tot hiertoe gevraagd zijn."""
    marks = "".join(
        f'<marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{kleur}"/></marker>'
        for kleur, mid in _PIJLKLEUREN.items())
    return f"<defs>{marks}</defs>"


def voedselpiramide(breedte=470):
    """De voedselpiramide: veel producenten onderaan, weinig toppredatoren boven."""
    h = 190
    lagen = [("producenten — planten", FOREST, 1.0),
             ("consumenten 1ste orde — planteneters", "#6f8f4a", 0.74),
             ("consumenten 2de orde — vleeseters", AMBER, 0.48),
             ("toppredator", "#a2521f", 0.24)]
    laag_h = 40
    d = []
    for i, (naam, kleur, deel) in enumerate(reversed(lagen)):
        y = 16 + i * laag_h
        volgende = list(reversed(lagen))[i + 1][2] if i + 1 < len(lagen) else deel
        b1 = (breedte - 150) * deel
        b2 = (breedte - 150) * volgende
        mx = (breedte - 60) / 2
        d.append(f'<path d="M{mx-b1/2:.1f} {y} H{mx+b1/2:.1f} L{mx+b2/2:.1f} {y+laag_h} '
                 f'H{mx-b2/2:.1f} Z" fill="{kleur}" opacity="0.30" stroke="{kleur}" stroke-width="1.8"/>')
        d.append(_tekst(mx, y + laag_h / 2 + 4, naam.split(" — ")[0], 10.5, DARK, vet=True))
        if " — " in naam:
            d.append(_tekst(breedte - 8, y + laag_h / 2 + 4, naam.split(" — ")[1], 9.5, DIM, anker="end"))
    d.append(f'<path d="M14 {16+len(lagen)*laag_h} V20 m0 0 l-5 6 m5 -6 l5 6" stroke="{DIM}" '
             f'stroke-width="1.6" fill="none"/>')
    d.append(_tekst(24, 100, "energie", 9.5, DIM, anker="start"))
    return _svg(breedte, h, "".join(d))


def bloemdoorsnede(breedte=470):
    """Een bloem in doorsnede, met de meeldraad links en de stamper in het midden."""
    h = 224
    mx = breedte / 2
    d = [f'<path d="M{mx} 196 V96" stroke="{FOREST}" stroke-width="4" stroke-linecap="round"/>']
    # kroonbladen
    d.append(f'<path d="M{mx-24} 150 q-70 -26 -86 -74 q54 6 86 44 Z" fill="rgba(240,195,60,.35)" '
             f'stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(f'<path d="M{mx+24} 150 q70 -26 86 -74 q-54 6 -86 44 Z" fill="rgba(240,195,60,.35)" '
             f'stroke="{AMBER}" stroke-width="1.6"/>')
    # stamper
    d.append(f'<path d="M{mx} 150 V66" stroke="{KERN}" stroke-width="3.2"/>')
    d.append(f'<ellipse cx="{mx}" cy="60" rx="17" ry="8" fill="rgba(122,91,143,.35)" '
             f'stroke="{KERN}" stroke-width="1.8"/>')
    d.append(f'<ellipse cx="{mx}" cy="158" rx="24" ry="18" fill="rgba(122,91,143,.20)" '
             f'stroke="{KERN}" stroke-width="1.8"/>')
    for dx in (-8, 8):
        d.append(f'<circle cx="{mx+dx}" cy="158" r="4.2" fill="{KERN}" opacity="0.75"/>')
    # meeldraden
    for zijde in (-1, 1):
        x = mx + zijde * 46
        d.append(f'<path d="M{mx + zijde*10} 150 Q{x} 120 {x} 84" stroke="{AMBER}" '
                 f'stroke-width="2.6" fill="none"/>')
        d.append(f'<ellipse cx="{x}" cy="78" rx="11" ry="7" fill="rgba(193,127,43,.45)" '
                 f'stroke="{AMBER}" stroke-width="1.6"/>')
    labels = [(mx + 24, 56, "stempel", "start", KERN), (mx + 14, 106, "stijl", "start", KERN),
              (mx + 30, 176, "vruchtbeginsel met zaadbeginsels", "start", KERN),
              (mx - 60, 70, "helmknop", "end", AMBER), (mx - 58, 122, "helmdraad", "end", AMBER),
              (mx + 14, 208, "stengel", "start", FOREST)]
    for x, y, naam, anker, kleur in labels:
        d.append(_kussen(x, y, naam, 9.5, kleur, anker=anker, vet=True))
    return _svg(breedte, h, "".join(d))


def menstruatiecyclus(breedte=470):
    """De cyclus van 28 dagen als een balk, met de vier gebeurtenissen erop."""
    h = 168
    links, rechts = 30, breedte - 20
    y = 78
    breed = rechts - links
    d = [f'<rect x="{links}" y="{y}" width="{breed:.1f}" height="30" rx="8" fill="{PAPER}" '
         f'stroke="{BORDER}" stroke-width="1.4"/>']

    def plek(dag):
        return links + breed * dag / 28

    d.append(f'<rect x="{links}" y="{y}" width="{plek(5)-links:.1f}" height="30" rx="8" '
             f'fill="rgba(192,57,43,.28)" stroke="#c0392b" stroke-width="1.4"/>')
    d.append(f'<rect x="{plek(11):.1f}" y="{y}" width="{plek(16)-plek(11):.1f}" height="30" '
             f'fill="rgba(240,195,60,.35)" stroke="{AMBER}" stroke-width="1.4"/>')
    d.append(f'<line x1="{plek(14):.1f}" y1="{y-16}" x2="{plek(14):.1f}" y2="{y+38}" '
             f'stroke="{FOREST}" stroke-width="2.2"/>')
    for dag in (1, 7, 14, 21, 28):
        d.append(f'<line x1="{plek(dag):.1f}" y1="{y+30}" x2="{plek(dag):.1f}" y2="{y+36}" '
                 f'stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(plek(dag), y + 50, f"dag {dag}", 9.5, DIM))
    d.append(_kussen(plek(2.5), y - 24, "menstruatie", 9.5, "#c0392b", anker="middle", vet=True))
    d.append(_kussen(plek(14), y - 26, "eisprong", 9.5, FOREST, anker="middle", vet=True))
    d.append(_kussen(plek(13.5), y + 26, "vruchtbare periode", 9.5, AMBER, anker="middle", vet=True))
    d.append(_kussen(plek(23), y - 24, "slijmvlies verdikt", 9.5, KERN, anker="middle", vet=True))
    d.append(_tekst(breedte / 2, 150,
                    "Gemiddeld 28 dagen, maar 21 tot 35 dagen is normaal. Dag 1 is de eerste dag "
                    "van de menstruatie.", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def krachtpijl(breedte=470):
    """De vier kenmerken van een kracht: aangrijpingspunt, grootte, richting, zin."""
    h = 172
    y = 96
    x0, x1 = 120, 330
    d = [f'<rect x="60" y="{y-26}" width="60" height="52" rx="8" fill="rgba(193,127,43,.18)" '
         f'stroke="{AMBER}" stroke-width="1.8"/>',
         f'<line x1="40" y1="{y}" x2="{breedte-30}" y2="{y}" stroke="{DIM}" stroke-width="1" '
         f'stroke-dasharray="5 5"/>',
         f'<path d="M{x0} {y} H{x1}" stroke="{FOREST}" stroke-width="3.4" '
         f'marker-end="url(#{_pijlpunt(FOREST)})"/>',
         f'<circle cx="{x0}" cy="{y}" r="5" fill="{FOREST}"/>']
    d.append(_tekst(x0, y + 26, "aangrijpingspunt", 9.5, FOREST, vet=True))
    d.append(_tekst((x0 + x1) / 2, y - 14, "grootte", 9.5, DARK, vet=True))
    d.append(_tekst(breedte - 34, y - 12, "zin", 9.5, FOREST, anker="end", vet=True))
    d.append(_tekst(40, y - 12, "richting", 9.5, DIM, anker="start"))
    d.append(f'<path d="M{x0} {y+58} H{x0-70}" stroke="#5b7f9c" stroke-width="3" '
             f'marker-end="url(#{_pijlpunt("#5b7f9c")})"/>')
    d.append(_tekst(x0 + 8, y + 62, "zelfde richting, andere zin", 9.5, "#5b7f9c", anker="start"))
    return _svg(breedte, h, _pijlpunten() + "".join(d))


def onderdompeling(breedte=470):
    """Twee maatcilinders: het volume van een steen uit het verschil in waterpeil."""
    h = 220
    d = []
    for i, (peil, met_steen, bijschrift) in enumerate(((50, False, "vóór: 50 mL"),
                                                       (65, True, "na: 65 mL"))):
        ox = 70 + i * 200
        bodem, top = 176, 46
        hoog = bodem - top
        d.append(f'<rect x="{ox}" y="{top}" width="70" height="{hoog}" rx="6" fill="#ffffff" '
                 f'stroke="{DIM}" stroke-width="1.8"/>')
        waterhoogte = hoog * peil / 80
        d.append(f'<rect x="{ox+2}" y="{bodem-waterhoogte:.1f}" width="66" height="{waterhoogte-2:.1f}" '
                 f'rx="4" fill="rgba(91,147,184,.35)"/>')
        for merk in range(10, 81, 10):
            my = bodem - hoog * merk / 80
            d.append(f'<line x1="{ox}" y1="{my:.1f}" x2="{ox+12}" y2="{my:.1f}" stroke="{DIM}" stroke-width="1"/>')
            if merk % 20 == 0:
                d.append(_tekst(ox - 6, my + 3.5, str(merk), 8.5, DIM, anker="end"))
        if met_steen:
            d.append(f'<path d="M{ox+22} 158 q-10 -20 6 -26 q22 -12 30 6 q10 18 -8 22 Z" '
                     f'fill="rgba(122,91,143,.45)" stroke="{KERN}" stroke-width="1.6"/>')
        d.append(_tekst(ox + 35, 198, bijschrift, 10.5, DARK, vet=True))
    d.append(f'<path d="M160 110 H{268}" stroke="{FOREST}" stroke-width="2.4" '
             f'marker-end="url(#{_pijlpunt(FOREST)})"/>')
    d.append(_kussen(214, 102, "steen erin", 9.5, FOREST, anker="middle", vet=True))
    d.append(_tekst(breedte / 2, 214,
                    "65 mL − 50 mL = 15 mL, en 1 mL is 1 cm³. Het volume van de steen is dus 15 cm³.",
                    10, DARK))
    return _svg(breedte, h, _pijlpunten() + "".join(d))


def faseovergangen(breedte=470):
    """De drie toestanden in een driehoek, met de zes faseovergangen ertussen."""
    h = 224
    mx = breedte / 2
    punten = {"vast": (mx - 150, 188), "vloeibaar": (mx + 150, 188), "gasvormig": (mx, 52)}
    d = []
    for naam, (x, y) in punten.items():
        d.append(f'<rect x="{x-62:.0f}" y="{y-20:.0f}" width="124" height="40" rx="10" '
                 f'fill="rgba(47,93,80,.10)" stroke="{FOREST}" stroke-width="2"/>')
        d.append(_tekst(x, y + 5, naam, 11.5, DARK, vet=True))
    paren = [("vast", "vloeibaar", "smelten", -13, AMBER),
             ("vloeibaar", "vast", "stollen", 13, "#5b7f9c"),
             ("vloeibaar", "gasvormig", "verdampen", -13, AMBER),
             ("gasvormig", "vloeibaar", "condenseren", 13, "#5b7f9c"),
             ("vast", "gasvormig", "sublimeren", -13, AMBER),
             ("gasvormig", "vast", "rijpen", 13, "#5b7f9c")]
    import math
    for van, naar, naam, verschuiving, kleur in paren:
        x0, y0 = punten[van]
        x1, y1 = punten[naar]
        hoek = math.atan2(y1 - y0, x1 - x0)
        # De loodrechte wordt uit de vaste volgorde van de drie vakjes gehaald,
        # niet uit de richting van deze pijl. Anders vallen de heen- en de
        # terugpijl van hetzelfde paar op elkaar.
        namen = list(punten)
        vast0, vast1 = punten[min(van, naar, key=namen.index)], punten[max(van, naar, key=namen.index)]
        basis = math.atan2(vast1[1] - vast0[1], vast1[0] - vast0[0])
        nx, ny = -math.sin(basis) * verschuiving, math.cos(basis) * verschuiving
        ax0, ay0 = x0 + math.cos(hoek) * 66 + nx, y0 + math.sin(hoek) * 30 + ny
        ax1, ay1 = x1 - math.cos(hoek) * 66 + nx, y1 - math.sin(hoek) * 30 + ny
        d.append(f'<path d="M{ax0:.1f} {ay0:.1f} L{ax1:.1f} {ay1:.1f}" stroke="{kleur}" '
                 f'stroke-width="2" fill="none" marker-end="url(#{_pijlpunt(kleur)})"/>')
        # Elk label staat op een kwart van zijn éigen beginpunt. Omdat de twee
        # pijlen van een paar tegengesteld lopen, komen hun witte vlakjes zo aan
        # weerszijden te liggen in plaats van over elkaar.
        deel = 0.28
        d.append(_kussen(ax0 + (ax1 - ax0) * deel, ay0 + (ay1 - ay0) * deel - 2, naam, 9.5, kleur,
                         anker="middle", vet=True))
    return _svg(breedte, h, _pijlpunten() + "".join(d))


# ---------------------------------------------------------------------------
# Nederlands ✨ Spark: communicatie, register en de opbouw van een tekst
# ---------------------------------------------------------------------------

def communicatiemodel(breedte=470):
    """Zender, boodschap en ontvanger, met kanaal, context en doel erbij."""
    h = 186
    d = [f'<rect x="6" y="6" width="{breedte-12}" height="140" rx="14" fill="none" '
         f'stroke="{BORDER}" stroke-width="1.6" stroke-dasharray="6 5"/>',
         _tekst(20, 26, "context: de situatie waarin je communiceert", 9.5, DIM, "start")]
    vakken = [(26, "zender", "wie stuurt", FOREST),
              (180, "boodschap", "wat je zegt", AMBER),
              (334, "ontvanger", "voor wie", FOREST)]
    for x, naam, onder, kleur in vakken:
        d.append(f'<rect x="{x}" y="52" width="110" height="46" rx="10" fill="{kleur}18" '
                 f'stroke="{kleur}" stroke-width="1.7"/>')
        d.append(_tekst(x + 55, 74, naam, 12.5, DARK, "middle", True))
        d.append(_tekst(x + 55, 90, onder, 9.5, DIM))
    for x1, x2 in ((140, 176), (294, 330)):
        d.append(_pijl(x1, 75, x2, DIM))
        d.append(_tekst((x1 + x2) / 2, 64, "kanaal", 9, DIM))
    d.append(_tekst(235, 120, "kanaal: mail, app, blog, telefoon, gesprek", 10, DIM))
    d.append(f'<rect x="120" y="152" width="230" height="28" rx="9" fill="#ffffff" '
             f'stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(_tekst(235, 171, "doel: waarom stuur je die boodschap?", 10.5, AMBER, "middle", True))
    return _svg(breedte, h, "".join(d))


def registerschaal(breedte=470, zinnen=None):
    """Van informeel naar formeel, met een voorbeeldzin per stap.

    Met `zinnen` geef je drie andere voorbeeldzinnen mee, bijvoorbeeld Franse.
    De schaal zelf blijft dezelfde: informeel, neutraal, formeel.
    """
    h = 160
    a, b, c = zinnen or ("Hey, kom je straks?", "Kom je straks ook?", "Komt u straks ook?")
    d = [f'<line x1="30" y1="46" x2="{breedte-30}" y2="46" stroke="{BORDER}" stroke-width="8" '
         f'stroke-linecap="round"/>']
    punten = [(78, "informeel", "je beste vriend", a, FOREST),
              (235, "neutraal", "je trainer", b, DIM),
              (breedte - 78, "formeel", "een onbekende", c, AMBER)]
    for x, naam, wie, zin, kleur in punten:
        d.append(f'<circle cx="{x}" cy="46" r="9" fill="{kleur}"/>')
        d.append(_tekst(x, 28, naam, 11.5, DARK, "middle", True))
        d.append(_tekst(x, 76, wie, 9.5, DIM))
        d.append(f'<rect x="{x-72}" y="88" width="144" height="30" rx="9" fill="#ffffff" '
                 f'stroke="{kleur}" stroke-width="1.5"/>')
        d.append(_tekst(x, 107, zin, 10.5, kleur, "middle", True))
    d.append(_tekst(breedte/2, 142, "Niet één vorm is juist: de situatie en de ontvanger bepalen je keuze.",
                    9.5, DIM))
    return _svg(breedte, h, "".join(d))


def kernpiramide(breedte=470):
    """Van onderwerp naar hoofdgedachte naar hoofdpunten en details."""
    h = 196
    rijen = [("onderwerp", "één of enkele woorden", FOREST, 150),
             ("hoofdgedachte", "de belangrijkste boodschap, in één zin", AMBER, 250),
             ("hoofdpunten", "wat die boodschap ondersteunt", FOREST, 340),
             ("details", "voorbeelden, cijfers, namen", DIM, 430)]
    for i, (naam, onder, kleur, b) in enumerate(rijen):
        y = 8 + i * 46
        x = (breedte - b) / 2
        d = f'<rect x="{x:.0f}" y="{y}" width="{b}" height="38" rx="9" fill="{kleur}18" ' \
            f'stroke="{kleur}" stroke-width="1.6"/>'
        rijen[i] = d + _tekst(breedte/2, y + 18, naam, 12, DARK, "middle", True) \
                     + _tekst(breedte/2, y + 31, onder, 9.5, DIM)
    return _svg(breedte, h, "".join(rijen))


# ---------------------------------------------------------------------------
# Frans ✨ Spark
# ---------------------------------------------------------------------------

def fotokader(breedte=470):
    """Een fotokader met de plaatsaanduidingen die je nodig hebt om het te beschrijven."""
    h = 214
    x0, y0 = 34, 14
    br, hg = breedte - 2 * x0, 148
    d = [f'<rect x="{x0}" y="{y0}" width="{br}" height="{hg}" rx="10" fill="#ffffff" '
         f'stroke="{DARK}" stroke-width="2"/>']
    # de band van de achtergrond, bovenaan
    d.append(f'<rect x="{x0}" y="{y0}" width="{br}" height="52" fill="{FOREST}12"/>')
    d.append(f'<line x1="{x0}" y1="{y0+52}" x2="{x0+br}" y2="{y0+52}" stroke="{FOREST}" '
             f'stroke-width="1.3" stroke-dasharray="5 4"/>')
    d.append(_tekst(x0 + br / 2, y0 + 30, "à l&#39;arrière-plan — op de achtergrond", 11, FOREST, "middle", True))
    # de drie kolommen
    for i, naam in enumerate(("à gauche", "au milieu", "à droite")):
        cx = x0 + br * (i + 0.5) / 3
        if i:
            lx = x0 + br * i / 3
            d.append(f'<line x1="{lx:.1f}" y1="{y0+52}" x2="{lx:.1f}" y2="{y0+hg}" '
                     f'stroke="{BORDER}" stroke-width="1.3" stroke-dasharray="4 4"/>')
        d.append(_tekst(cx, y0 + 96, naam, 12.5, DARK, "middle", True))
    d.append(f'<rect x="{x0}" y="{y0+hg-34}" width="{br}" height="34" fill="{AMBER}14"/>')
    d.append(f'<line x1="{x0}" y1="{y0+hg-34}" x2="{x0+br}" y2="{y0+hg-34}" stroke="{AMBER}" '
             f'stroke-width="1.3" stroke-dasharray="5 4"/>')
    d.append(_tekst(x0 + br / 2, y0 + hg - 13, "au premier plan — op de voorgrond", 11, AMBER, "middle", True))
    d.append(_tekst(breedte / 2, h - 12,
                    "Sur la photo, il y a… — begin met wat je ziet, en zeg er meteen bij wáár.",
                    10, DIM))
    return _svg(breedte, h, "".join(d))


def franse_tijden(breedte=470):
    """De tijden van de vakfiche op één lijn: verleden, nu en toekomst."""
    h = 204
    y = 104
    d = [f'<line x1="18" y1="{y}" x2="{breedte-18}" y2="{y}" stroke="{BORDER}" stroke-width="7" '
         f'stroke-linecap="round"/>']
    d.append(f'<circle cx="{breedte/2}" cy="{y}" r="8" fill="{AMBER}"/>')
    d.append(_tekst(breedte / 2, y - 16, "maintenant", 11, AMBER, "middle", True))
    blokken = [(62, "imparfait", "je mangeais", "wat gewoonlijk zo was", FOREST, True),
               (172, "passé composé", "j&#39;ai mangé", "één keer, afgelopen", DARK, True),
               (breedte - 172, "passé récent", "je viens de manger", "net gebeurd", DARK, False),
               (breedte - 62, "futur proche", "je vais manger", "straks", FOREST, False)]
    for x, naam, vorm, onder, kleur, boven in blokken:
        ty = y - 88 if boven else y + 18
        d.append(f'<rect x="{x-52:.0f}" y="{ty}" width="104" height="54" rx="9" fill="{kleur}12" '
                 f'stroke="{kleur}" stroke-width="1.6"/>')
        d.append(_tekst(x, ty + 16, naam, 10, DIM))
        # de vormen verschillen sterk in lengte; laat de letter krimpen zodat
        # "je viens de manger" niet buiten zijn vakje loopt
        maat = min(11.5, 98 / (len(vorm.replace("&#39;", "'")) * 0.58))
        d.append(_tekst(x, ty + 32, vorm, round(maat, 1), kleur, "middle", True))
        d.append(_tekst(x, ty + 46, onder, 8.5, DIM))
        lijn = (ty + 54, y - 4) if boven else (ty, y + 4)
        d.append(f'<line x1="{x}" y1="{lijn[0]}" x2="{x}" y2="{lijn[1]}" stroke="{kleur}" '
                 f'stroke-width="1.4" stroke-dasharray="3 3"/>')
    d.append(_tekst(breedte / 2, h - 10, "Het présent staat in het midden: je mange.", 10, DIM))
    return _svg(breedte, h, "".join(d))


def voornaamwoordplaats(breedte=470):
    """Waar het persoonlijk voornaamwoord staat: in het Frans vóór het werkwoord."""
    h = 168
    d = []
    for rij, (taal, delen, kleur) in enumerate((
            ("Nederlands", [("ik", DIM), ("zie", DARK), ("haar", AMBER)], DIM),
            ("Frans", [("je", DIM), ("la", AMBER), ("vois", DARK)], FOREST))):
        y = 26 + rij * 74
        d.append(_tekst(24, y + 24, taal, 11, kleur, "start", True))
        for i, (woord, wk) in enumerate(delen):
            x = 128 + i * 112
            d.append(f'<rect x="{x}" y="{y}" width="100" height="40" rx="9" fill="{wk}18" '
                     f'stroke="{wk}" stroke-width="1.6"/>')
            d.append(_tekst(x + 50, y + 26, woord, 14, DARK, "middle", True))
    d.append(_tekst(breedte / 2, h - 10,
                    "Het voorwerp staat in het Frans vóór het werkwoord, in het Nederlands erachter.",
                    10, DIM))
    return _svg(breedte, h, "".join(d))


def breukfiguur(vorm, teller, noemer, breedte=None):
    """Een cirkel, strook of raster in gelijke stukken, met er een aantal gekleurd.

    Dezelfde drie vormen als in de vragen op het scherm (components/Figuren.tsx),
    zodat een kind op papier niet iets anders ziet dan online. Zet teller op 0
    voor een lege figuur: dan kleurt het kind zelf in.
    """
    if vorm == "cirkel":
        r, c = 66, 76
        import math
        d = []
        if noemer == 1:
            d.append(f'<circle cx="{c}" cy="{c}" r="{r}" fill="{FOREST if teller else "#ffffff"}" '
                     f'stroke="{DARK}" stroke-width="1.8"/>')
        else:
            for i in range(noemer):
                a0 = -math.pi / 2 + i * 2 * math.pi / noemer
                a1 = -math.pi / 2 + (i + 1) * 2 * math.pi / noemer
                x0, y0 = c + r * math.cos(a0), c + r * math.sin(a0)
                x1, y1 = c + r * math.cos(a1), c + r * math.sin(a1)
                groot = 1 if (a1 - a0) > math.pi else 0
                vul = FOREST if i < teller else "#ffffff"
                d.append(f'<path d="M {c} {c} L {x0:.1f} {y0:.1f} A {r} {r} 0 {groot} 1 {x1:.1f} {y1:.1f} Z" '
                         f'fill="{vul}" stroke="{DARK}" stroke-width="1.8"/>')
        return _svg(152, 152, "".join(d))

    if vorm == "strook":
        b = breedte or min(330, noemer * 56)
        w = b / noemer
        d = []
        for i in range(noemer):
            vul = FOREST if i < teller else "#ffffff"
            d.append(f'<rect x="{2 + i*w:.1f}" y="2" width="{w:.1f}" height="44" '
                     f'fill="{vul}" stroke="{DARK}" stroke-width="1.6"/>')
        return _svg(b + 4, 48, "".join(d))

    # raster: honderd vakjes in tien rijen, of minder vakjes op één rij
    kolommen = 10 if noemer == 100 else noemer
    rijen = -(-noemer // kolommen)
    cel = 18 if noemer == 100 else 26
    d = []
    for i in range(noemer):
        vul = AMBER if i < teller else "#ffffff"
        d.append(f'<rect x="{2 + (i % kolommen)*cel}" y="{2 + (i // kolommen)*cel}" '
                 f'width="{cel}" height="{cel}" fill="{vul}" stroke="{BORDER}" stroke-width="1"/>')
    d.append(f'<rect x="2" y="2" width="{kolommen*cel}" height="{rijen*cel}" fill="none" '
             f'stroke="{DARK}" stroke-width="1.6"/>')
    return _svg(kolommen * cel + 4, rijen * cel + 4, "".join(d))


def hoek(graden, breedte=120):
    """Eén hoek, zonder naam en zonder gradental erbij.

    hoekenrij() schrijft de naam en het aantal graden onder elke hoek en hoort
    dus in een leerbundel. In een oefenbundel is dat net de vraag, dus hier
    staat er niets bij — ook geen haakje bij 90 graden, want dat verklapt het.
    """
    import math
    cx, cy, arm = breedte / 2 - 20, 62, 46
    a = math.radians(-graden)
    r = 17
    x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
    groot = 1 if graden > 180 else 0
    d = [
        f'<line x1="{cx}" y1="{cy}" x2="{cx+arm}" y2="{cy}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{cx+arm*math.cos(a):.1f}" y2="{cy+arm*math.sin(a):.1f}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>',
        f'<path d="M{cx+r} {cy} A{r} {r} 0 {groot} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{AMBER}" stroke-width="1.8"/>',
    ]
    return _svg(breedte, 86, "".join(d))


_VORMEN = {
    "vierkant": '<rect x="{cx0}" y="14" width="46" height="46" fill="#ffffff" stroke="{k}" stroke-width="2" rx="2"/>',
    "rechthoek": '<rect x="{cx1}" y="20" width="58" height="36" fill="#ffffff" stroke="{k}" stroke-width="2" rx="2"/>',
    "driehoek": '<polygon points="{cx},14 {xr},60 {xl},60" fill="#ffffff" stroke="{k}" stroke-width="2"/>',
    "cirkel": '<circle cx="{cx}" cy="37" r="24" fill="#ffffff" stroke="{k}" stroke-width="2"/>',
    "ruit": '<polygon points="{cx},12 {xr},37 {cx},62 {xl},37" fill="#ffffff" stroke="{k}" stroke-width="2"/>',
    "trapezium": '<polygon points="{xa},16 {xb},16 {xr},60 {xl},60" fill="#ffffff" stroke="{k}" stroke-width="2"/>',
    "vijfhoek": '<polygon points="{cx},12 {xr},31 {p1},62 {p2},62 {xl},31" fill="#ffffff" stroke="{k}" stroke-width="2"/>',
    "zeshoek": '<polygon points="{xa},12 {xb},12 {xr},37 {xb},62 {xa},62 {xl},37" fill="#ffffff" stroke="{k}" stroke-width="2"/>',
}


def vorm(naam, breedte=110):
    """Eén vlakke figuur, zonder naam eronder. Zie vormenrij() voor de versie
    mét naam, die in een leerbundel hoort."""
    cx = breedte / 2
    inhoud = _VORMEN[naam].format(
        k=DARK, cx=cx, cx0=cx - 23, cx1=cx - 29, xl=cx - 26, xr=cx + 26,
        xa=cx - 14, xb=cx + 14, p1=cx + 16, p2=cx - 16)
    return _svg(breedte, 74, inhoud)


def ruimtefiguur(naam, breedte=110):
    """Eén ruimtefiguur, zonder naam eronder. Zie ruimtefiguren() voor de
    versie mét naam."""
    cx = breedte / 2

    def blok(b, hh, diep):
        x, y = cx - b / 2 - diep / 2, 62 - hh
        return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{b}" height="{hh}" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                f'<path d="M{x:.1f} {y:.1f} l{diep} -{diep} h{b} l-{diep} {diep}" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                f'<path d="M{x+b:.1f} {y:.1f} l{diep} -{diep} v{hh} l-{diep} {diep}" fill="#f2efe7" stroke="{DARK}" stroke-width="1.9"/>')

    if naam == "kubus":
        inhoud = blok(40, 40, 13)
    elif naam == "balk":
        inhoud = blok(54, 30, 12)
    elif naam == "cilinder":
        inhoud = (f'<path d="M{cx-22} 28 v30 a22 8 0 0 0 44 0 v-30" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                  f'<ellipse cx="{cx}" cy="28" rx="22" ry="8" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>')
    elif naam == "kegel":
        inhoud = (f'<path d="M{cx} 22 L{cx-22} 58 A22 8 0 0 0 {cx+22} 58 Z" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                  f'<path d="M{cx-22} 58 A22 8 0 0 1 {cx+22} 58" fill="none" stroke="{DARK}" stroke-width="1.9"/>')
    else:
        inhoud = (f'<circle cx="{cx}" cy="44" r="23" fill="#ffffff" stroke="{DARK}" stroke-width="1.9"/>'
                  f'<ellipse cx="{cx}" cy="44" rx="23" ry="8" fill="none" stroke="{BORDER}" stroke-width="1.5"/>')
    return _svg(breedte, 74, inhoud)


# ---------------------------------------------------------------------------
# Tekeningen bij samenleving en economie.
# ---------------------------------------------------------------------------

def kringloop(breedte=470):
    """De eenvoudige economische kringloop: gezinnen, bedrijven en de overheid.

    Boven de vier stromen tussen gezinnen en bedrijven, met de richting in de
    pijl zelf. Onder de overheid, die aan beide kanten belastingen ontvangt en
    er voorzieningen voor teruggeeft.
    """
    h = 258
    gb, gh = 140, 100
    lx, rx, by = 14, breedte - 14 - gb, 24
    d = []
    for x, naam in ((lx, "de gezinnen"), (rx, "de bedrijven")):
        d.append(f'<rect x="{x}" y="{by}" width="{gb}" height="{gh}" rx="11" fill="{PAPER}" '
                 f'stroke="{FOREST}" stroke-width="1.8"/>')
        d.append(_tekst(x + gb / 2, by + 26, naam, 12, DARK, vet=True))

    # De vier stromen tussen gezinnen en bedrijven.
    x1, x2 = lx + gb + 12, rx - 12
    stromen = [
        ("arbeid", True), ("loon", False),
        ("goederen en diensten", False), ("je betaling", True),
    ]
    for i, (label, naar_rechts) in enumerate(stromen):
        y = by + 16 + i * 22
        d.append(_tekst((x1 + x2) / 2, y - 5, label, 9, DIM))
        if naar_rechts:
            d.append(f'<path d="M{x1} {y} H{x2} l-7 -4 m7 4 l-7 4" stroke="{FOREST}" '
                     f'stroke-width="1.8" fill="none" stroke-linecap="round"/>')
        else:
            d.append(f'<path d="M{x2} {y} H{x1} l7 -4 m-7 4 l7 4" stroke="{AMBER}" '
                     f'stroke-width="1.8" fill="none" stroke-linecap="round"/>')

    # De overheid, met aan elke kant een stroom heen en een stroom terug.
    ox, oy, ob, oh = 60, 186, breedte - 120, 56
    d.append(f'<rect x="{ox}" y="{oy}" width="{ob}" height="{oh}" rx="11" fill="{PAPER}" '
             f'stroke="{DARK}" stroke-width="1.8"/>')
    d.append(_tekst(breedte / 2, oy + 24, "de overheid", 12, DARK, vet=True))
    d.append(_tekst(breedte / 2, oy + 42, "int belastingen en geeft voorzieningen terug", 9, DIM))
    boven, onder = by + gh + 4, oy - 4
    for x, label, omhoog, anker in ((72, "belastingen", False, "start"),
                                    (150, "uitkeringen", True, "start"),
                                    (breedte - 72, "belastingen", False, "end"),
                                    (breedte - 150, "wegen en scholen", True, "end")):
        if omhoog:
            d.append(f'<path d="M{x} {onder} V{boven} l-4 7 m4 -7 l4 7" stroke="{DARK}" '
                     f'stroke-width="1.6" fill="none" stroke-linecap="round"/>')
            ty, tx = onder - 8, x + (10 if anker == "start" else -10)
        else:
            d.append(f'<path d="M{x} {boven} V{onder} l-4 -7 m4 7 l4 -7" stroke="{FOREST}" '
                     f'stroke-width="1.6" fill="none" stroke-linecap="round"/>')
            ty, tx = boven + 14, x + (10 if anker == "start" else -10)
        d.append(_tekst(tx, ty, label, 9, DIM, anker))
    return _svg(breedte, h, "".join(d))


def bestuurslagen(breedte=470):
    """De vier bestuursniveaus van België als kaders in elkaar.

    Ze zitten in elkaar omdat je gemeente in je provincie ligt en je provincie
    in je gewest. Binnen zijn eigen bevoegdheden is elk niveau wel zelf baas:
    dat zegt het onderschrift, want de tekening kan dat niet.
    """
    h = 228
    lagen = [
        (12, 10, 198, "de federale overheid", "justitie, defensie, pensioenen", DARK),
        (40, 36, 172, "de gemeenschappen en de gewesten", "onderwijs, milieu, wonen", FOREST),
        (68, 62, 146, "de provincie", "provinciale wegen en domeinen", AMBER),
        (96, 88, 122, "de gemeente of stad", "huisvuil, identiteitskaart", "#5b7f9c"),
    ]
    d = []
    for x, y, onder, naam, voorbeeld, kleur in lagen:
        bb, hh = breedte - 2 * x, onder - y
        d.append(f'<rect x="{x}" y="{y}" width="{bb}" height="{hh}" rx="12" fill="none" '
                 f'stroke="{kleur}" stroke-width="1.8"/>')
        d.append(_tekst(x + 12, y + 21, naam, 10.5, kleur, "start", True))
        d.append(_tekst(x + bb - 12, y + 21, voorbeeld, 8.5, DIM, "end"))
    d.append(_tekst(breedte / 2, h - 8,
                    "Ze liggen in elkaar op de kaart, niet in macht: binnen zijn eigen lijst beslist elk niveau zelf.",
                    9, DIM))
    return _svg(breedte, h, "".join(d))


def relieftrappen(breedte=470):
    """De drie trappen van het Belgische reliëf, van de Noordzee naar het zuidoosten.

    Geen kaart maar een doorsnede: België klimt van het noordwesten naar het
    zuidoosten, en de dertien reliëfeenheden van de vakfiche vallen in drie
    trappen uiteen. Een kaart met die dertien namen erop hebben we niet — de
    kaarten die in omloop zijn dragen de namen van de landstreken, en dat zijn
    andere namen. Een schema kan hier ook niet scheef staan, want er komt geen
    enkele grens aan te pas.
    """
    h = 250
    basis, links, rechts = 190, 52, 458
    zee = 208

    def y(m):
        return basis - m / 760 * (basis - 26)

    # Per trap: van waar tot waar op de horizontale as, de bovengrens in meter,
    # de naam, het hoogtebereik en de kleur.
    trappen = [
        (links, 180, 100, "laagvlaktes", "0 tot 100 m", "#dfe7d5"),
        (180, 300, 200, "laagplateaus", "100 tot 200 m", "#c2cfb2"),
        (300, rechts, 694, "plateaus", "200 tot 694 m", "#9fb08c"),
    ]
    d = [f'<rect x="0" y="0" width="{breedte}" height="{zee}" fill="#eef4f8"/>']
    # De Noordzee links: het nulpunt van alle hoogtes, dus die hoort erbij.
    d.append(f'<rect x="0" y="{basis}" width="{links}" height="{zee-basis}" fill="{WATER}"/>')
    d.append(_tekst(links / 2, basis + 15, "Noordzee", 9, DARK))
    for x0, x1, top, naam, bereik, kleur in trappen:
        yt = y(top)
        d.append(f'<rect x="{x0}" y="{yt:.1f}" width="{x1-x0}" height="{basis-yt:.1f}" '
                 f'fill="{kleur}" stroke="{DARK}" stroke-width="1.6"/>')
        # De naam staat bóven de trap, in de vrije ruimte: op de onderste twee
        # treden is binnenin te weinig plaats en dan zou de tekst eruit lopen.
        midden = (x0 + x1) / 2
        d.append(_tekst(midden, yt - 19, naam, 11.5, INK, vet=True))
        d.append(_tekst(midden, yt - 6, bereik, 9.5, DIM))
    # De hoogteas links van de tekening.
    d.append(f'<line x1="{links-12}" y1="{y(760):.1f}" x2="{links-12}" y2="{basis}" stroke="{DIM}" stroke-width="1.4"/>')
    for m in (0, 200, 400, 600):
        d.append(f'<line x1="{links-16}" y1="{y(m):.1f}" x2="{links-12}" y2="{y(m):.1f}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(links - 20, y(m) + 3.5, f"{m}", 9, DIM, "end"))
    d.append(_tekst(links - 20, 14, "meter", 9, DIM, "end"))
    # Het hoogste punt van het land, boven op de bovenste trap.
    d.append(f'<circle cx="{rechts-28}" cy="{y(694):.1f}" r="3.4" fill="{AMBER}"/>')
    d.append(_tekst(rechts - 14, y(694) + 22, "Signaal van Botrange, 694 m", 9, DARK, "end"))
    # De windstreken onderaan, want dat is wat de trappen verklaart.
    d.append(_tekst(links, h - 6, "noordwesten", 9.5, DIM, "start"))
    d.append(_tekst(rechts, h - 6, "zuidoosten", 9.5, DIM, "end"))
    d.append(f'<line x1="{links}" y1="{h-20}" x2="{rechts}" y2="{h-20}" stroke="{BORDER}" stroke-width="1.2"/>')
    return _svg(breedte, h, "".join(d))


def hoogtelijnen(breedte=470):
    """Een heuvel met hoogtelijnen, van bovenaf en van opzij.

    De twee tekeningen staan naast elkaar omdat dat het hele punt is: waar de
    lijnen bovenaan dicht bij elkaar liggen, staat de helling eronder steil.
    """
    h = 232
    d = []
    # ── links: de heuvel van bovenaf, met de lijnen rechts dicht bijeen.
    cx, cy = 116, 118
    ringen = [(96, 58, "#eef3ea"), (76, 46, "#dfe7d5"), (58, 34, "#c9d6ba"),
              (42, 23, "#b2c4a0"), (26, 13, "#9fb08c")]
    for i, (rx, ry, kleur) in enumerate(ringen):
        # De middelpunten schuiven naar rechts, zodat de rechterflank steil wordt.
        mx = cx + i * 9
        d.append(f'<ellipse cx="{mx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{kleur}" '
                 f'stroke="{DARK}" stroke-width="1.3"/>')
        if i % 2 == 0:
            d.append(_kussen(mx - rx + 15, cy + ry - 3, f"{100 + i*20}", 8, DIM, "middle"))
    d.append(_tekst(cx, 24, "van bovenaf", 10, INK, vet=True))
    d.append(_tekst(24, 208, "flauw", 9, DIM, "start"))
    d.append(_tekst(214, 208, "steil", 9, AMBER, "end", vet=True))
    # ── rechts: dezelfde heuvel van opzij.
    lx, basis, top = 252, 190, 74
    punten = [(lx, basis), (lx + 40, basis - 20), (lx + 86, basis - 62),
              (lx + 128, top + 4), (lx + 150, top), (lx + 176, basis - 44),
              (lx + 192, basis)]
    pad = " ".join(f"{x},{y}" for x, y in punten)
    d.append(f'<polygon points="{pad}" fill="#c9d6ba" stroke="{DARK}" stroke-width="1.6"/>')
    for m, y in [(100, basis - 24), (140, basis - 58), (180, basis - 92)]:
        d.append(f'<line x1="{lx-14}" y1="{y}" x2="{lx+200}" y2="{y}" stroke="{DIM}" '
                 f'stroke-width="1" stroke-dasharray="4 4"/>')
        d.append(_tekst(lx - 18, y + 3.5, f"{m}", 8.5, DIM, "end"))
    d.append(_tekst(lx + 96, 24, "van opzij", 10, INK, vet=True))
    d.append(_tekst(lx + 40, 208, "flauw", 9, DIM))
    d.append(_tekst(lx + 178, 208, "steil", 9, AMBER, vet=True))
    return _svg(breedte, h, "".join(d))


def reliefvormen(breedte=470):
    """De vier reliëfvormen van de fiche naast elkaar: vlakte, plateau, heuvel, berg."""
    h = 176
    basis = 130
    vak = breedte / 4
    vormen = [
        ("vlakte", "laag en vlak", [(6, 14), (14, 14), (30, 14), (100, 14), (116, 14)]),
        ("plateau", "hoog en vlak", [(6, 14), (26, 62), (40, 66), (86, 66), (100, 62), (116, 14)]),
        ("heuvel", "rond en niet zo hoog", [(6, 14), (30, 30), (56, 58), (82, 30), (116, 14)]),
        ("berg", "hoog en steil", [(6, 14), (36, 40), (58, 104), (80, 40), (116, 14)]),
    ]
    d = []
    for i, (naam, onder, vorm) in enumerate(vormen):
        x0 = i * vak + (vak - 122) / 2
        punten = [(x0 + dx, basis - dy) for dx, dy in vorm]
        pad = " ".join(f"{x:.1f},{y:.1f}" for x, y in punten)
        d.append(f'<polygon points="{x0},{basis} {pad} {x0+122},{basis}" fill="#c9d6ba" '
                 f'stroke="{DARK}" stroke-width="1.5"/>')
        if naam == "berg":
            d.append(f'<polygon points="{x0+48},{basis-78} {x0+58},{basis-104} {x0+68},{basis-78}" fill="{SNEEUW}" stroke="{DARK}" stroke-width="1.1"/>')
        d.append(_tekst(x0 + 61, basis + 22, naam, 11, INK, vet=True))
        d.append(_tekst(x0 + 61, basis + 36, onder, 8.5, DIM))
    d.append(f'<line x1="0" y1="{basis}" x2="{breedte}" y2="{basis}" stroke="{DARK}" stroke-width="1.6"/>')
    return _svg(breedte, h, "".join(d))


def gradennet(breedte=470):
    """De aardbol met het gradennet: evenaar, keerkringen, poolcirkels, meridianen."""
    import math
    h = 276
    cx, cy, r = 148, 142, 108
    knip = _id("net")
    d = [f'<defs><clipPath id="{knip}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#eaf1f6" stroke="{DARK}" stroke-width="1.8"/>']
    g = [f'<g clip-path="url(#{knip})">']
    # De breedtecirkels: als ellipsen, want we kijken schuin op de bol.
    for graden, naam, kleur, dik in [(0, "evenaar, 0°", DARK, 2.0),
                                     (23.5, "keerkring, 23,5° N", AMBER, 1.3),
                                     (-23.5, "keerkring, 23,5° Z", AMBER, 1.3),
                                     (66.5, "poolcirkel, 66,5° N", "#5b7f9c", 1.3),
                                     (-66.5, "poolcirkel, 66,5° Z", "#5b7f9c", 1.3)]:
        y = cy - math.sin(math.radians(graden)) * r
        rx = math.cos(math.radians(graden)) * r
        g.append(f'<ellipse cx="{cx}" cy="{y:.1f}" rx="{rx:.1f}" ry="{rx*0.20:.1f}" fill="none" '
                 f'stroke="{kleur}" stroke-width="{dik}"/>')
    # De meridianen: halve ellipsen van pool tot pool.
    for f in (-1.0, -0.6, -0.2, 0.2, 0.6, 1.0):
        rx = abs(f) * r
        richting = "1" if f > 0 else "0"
        if rx < 1:
            g.append(f'<line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" stroke="{DIM}" stroke-width="1"/>')
        else:
            g.append(f'<path d="M {cx} {cy-r} A {rx:.1f} {r} 0 0 {richting} {cx} {cy+r}" '
                     f'fill="none" stroke="{DIM}" stroke-width="1"/>')
    # De nulmeridiaan valt in deze stand samen met de voorste middellijn.
    g.append(f'<line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" stroke="{FOREST}" stroke-width="2"/>')
    g.append("</g>")
    d += g
    d.append(f'<circle cx="{cx}" cy="{cy-r}" r="3" fill="{DARK}"/>')
    d.append(f'<circle cx="{cx}" cy="{cy+r}" r="3" fill="{DARK}"/>')
    d.append(_tekst(cx - 42, cy - r - 4, "noordpool", 9, DARK, "end"))
    d.append(_tekst(cx, cy + r + 17, "zuidpool", 9, DARK))
    # De namen rechts, elk met een streepje naar zijn lijn.
    namen = [(cy - math.sin(math.radians(66.5)) * r, "poolcirkel 66,5° N", "#5b7f9c"),
             (cy - math.sin(math.radians(23.5)) * r, "keerkring 23,5° N", AMBER),
             (cy, "evenaar 0°", DARK),
             (cy + math.sin(math.radians(23.5)) * r, "keerkring 23,5° Z", AMBER),
             (cy + math.sin(math.radians(66.5)) * r, "poolcirkel 66,5° Z", "#5b7f9c")]
    for y, naam, kleur in namen:
        x = cx + math.cos(math.asin((cy - y) / r)) * r
        d.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="272" y2="{y:.1f}" stroke="{kleur}" '
                 f'stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(_tekst(278, y + 3.5, naam, 9, kleur, "start"))
    d.append(f'<line x1="{cx}" y1="{cy-r-4}" x2="{cx}" y2="{cy-r-16}" stroke="{FOREST}" stroke-width="1.6"/>')
    d.append(_tekst(cx + 6, cy - r - 20, "nulmeridiaan, 0° lengte", 9, FOREST, "start"))
    return _svg(breedte, h, "".join(d))


def landschapslagen(breedte=470):
    """De lagen waaruit een landschap is opgebouwd, van de ondergrond naar boven.

    Links de natuurlijke lagen, rechts wat de mens erbovenop legt. Dat is de
    indeling die de vakfiche maakt, en het is meteen de reden waarom twee
    streken er anders uitzien.
    """
    h = 262
    x0, bb = 24, 210
    lagen = [
        ("ondergrond", "zand, leem, klei of vast gesteente", "#b9a98c"),
        ("bodem", "de losse laag waarin wortels zitten", "#8d7a5a"),
        ("water", "beken, grondwater, de zee", "#8fb4cc"),
        ("reliëf", "de hoogteverschillen", "#9fb08c"),
        ("klimaat", "warm, gematigd of koud", "#cfe0ea"),
        ("vegetatie", "loofbos, naaldbos, gras, mos", "#7ba368"),
    ]
    menselijk = [
        ("landgebruik", "landbouw, wonen, industrie, recreatie"),
        ("bebouwing", "waar en hoe dicht de huizen staan"),
        ("infrastructuur", "wegen, spoor, kanalen, leidingen"),
        ("ontginning", "groeves, mijnen, grondstoffen"),
    ]
    hoog = 30
    d = [_tekst(x0, 16, "natuurlijke lagen", 10.5, FOREST, "start", vet=True)]
    for i, (naam, uitleg, kleur) in enumerate(reversed(lagen)):
        y = 26 + i * hoog
        d.append(f'<rect x="{x0}" y="{y}" width="{bb}" height="{hoog-5}" rx="4" fill="{kleur}" '
                 f'stroke="{DARK}" stroke-width="1.2"/>')
        d.append(_tekst(x0 + 10, y + 13, naam, 10, INK, "start", vet=True))
        d.append(_tekst(x0 + 10, y + 23, uitleg, 8, INK, "start"))
    x1 = x0 + bb + 26
    d.append(_tekst(x1, 16, "wat de mens erbovenop legt", 10.5, AMBER, "start", vet=True))
    for i, (naam, uitleg) in enumerate(menselijk):
        y = 26 + i * hoog
        d.append(f'<rect x="{x1}" y="{y}" width="{bb - 24}" height="{hoog-5}" rx="4" fill="#f6ecdc" '
                 f'stroke="{AMBER}" stroke-width="1.2"/>')
        d.append(_tekst(x1 + 10, y + 13, naam, 10, INK, "start", vet=True))
        d.append(_tekst(x1 + 10, y + 23, uitleg, 8, INK, "start"))
    d.append(_tekst(x1, 26 + 4 * hoog + 16, "Deze lagen kunnen op enkele", 9, DIM, "start"))
    d.append(_tekst(x1, 26 + 4 * hoog + 28, "jaren tijd sterk veranderen.", 9, DIM, "start"))
    d.append(_tekst(x0, h - 8, "Onderaan de ondergrond, bovenaan wat groeit. Elke laag werkt op de andere in.", 9, DIM, "start"))
    return _svg(breedte, h, "".join(d))


def vijfp(breedte=470):
    """De vijf P's van het duurzaamheidsmodel, met van elk een voorbeeld."""
    h = 210
    ps = [
        ("People", "mensen", "een eerlijk loon, veilig werk, onderwijs voor iedereen", "#c17f2b"),
        ("Planet", "de aarde", "een beekvallei beschermen, een bos aanleggen", "#3f7a46"),
        ("Prosperity", "welvaart", "werk dat genoeg opbrengt, betaalbare energie", "#5b7f9c"),
        ("Peace", "vrede", "zonder vrede wordt er niets opgebouwd of beschermd", "#7a5b8f"),
        ("Partnership", "samenwerking", "landen, bedrijven en burgers die samen aanpakken", "#a2521f"),
    ]
    kolom = (breedte - 16) / 5
    d = []
    for i, (p, nl, vb, kleur) in enumerate(ps):
        x = 8 + i * kolom
        d.append(f'<rect x="{x:.1f}" y="10" width="{kolom-8:.1f}" height="150" rx="6" fill="#fff" '
                 f'stroke="{kleur}" stroke-width="1.6"/>')
        d.append(f'<rect x="{x:.1f}" y="10" width="{kolom-8:.1f}" height="30" rx="6" fill="{kleur}"/>')
        d.append(f'<rect x="{x:.1f}" y="30" width="{kolom-8:.1f}" height="10" fill="{kleur}"/>')
        mid = x + (kolom - 8) / 2
        d.append(_tekst(mid, 30, p, 10.5, "#ffffff", vet=True))
        d.append(_tekst(mid, 56, nl, 9.5, DIM))
        # Het voorbeeld in regels van hoogstens 18 tekens, zodat niets uitloopt.
        regels, regel = [], ""
        for woord in vb.split():
            if len(regel) + len(woord) + 1 > 17:
                regels.append(regel); regel = woord
            else:
                regel = (regel + " " + woord).strip()
        regels.append(regel)
        for j, r in enumerate(regels[:7]):
            d.append(_tekst(mid, 76 + j * 11, r, 8, INK))
    d.append(_tekst(breedte / 2, 180, "De vijf hangen samen: wat de ene vooruithelpt, kan de andere tegelijk schaden.", 9.5, DIM))
    d.append(_tekst(breedte / 2, 196, "Daarom is duurzaamheid altijd een afweging en nooit één knop.", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def aardbeving(breedte=470):
    """Een aardbeving: de haard in de diepte, het epicentrum erboven, de golven."""
    import math
    h = 214
    grond = 78
    cx, hy = 196, 156
    d = [f'<rect x="0" y="0" width="{breedte}" height="{grond}" fill="#eaf1f6"/>',
         f'<rect x="0" y="{grond}" width="{breedte}" height="{h-grond}" fill="#e2d7c0"/>',
         f'<line x1="0" y1="{grond}" x2="{breedte}" y2="{grond}" stroke="{DARK}" stroke-width="1.8"/>']
    # De breuklijn waarlangs de twee stukken korst bewegen.
    d.append(f'<path d="M {cx-52} {h} L {cx} {hy} L {cx+46} {grond}" fill="none" stroke="{DARK}" '
             f'stroke-width="1.8" stroke-dasharray="7 4"/>')
    d.append(_tekst(cx - 86, hy + 30, "breuklijn", 9, DARK, "start"))
    # De golven van de haard naar het oppervlak.
    for r in (34, 56, 78):
        d.append(f'<circle cx="{cx}" cy="{hy}" r="{r}" fill="none" stroke="{AMBER}" '
                 f'stroke-width="1.3" opacity="0.75"/>')
    d.append(f'<circle cx="{cx}" cy="{hy}" r="6" fill="{ROOD}"/>')
    d.append(_tekst(cx + 14, hy + 4, "de haard", 9.5, ROOD, "start", vet=True))
    d.append(_tekst(cx + 14, hy + 16, "hier begint de beweging", 8.5, ROOD, "start"))
    d.append(f'<line x1="{cx}" y1="{hy}" x2="{cx}" y2="{grond}" stroke="{ROOD}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    d.append(f'<circle cx="{cx}" cy="{grond}" r="5" fill="{ROOD}"/>')
    d.append(_tekst(cx + 14, grond - 18, "het epicentrum", 9.5, ROOD, "start", vet=True))
    d.append(_tekst(cx + 14, grond - 6, "het punt recht boven de haard", 8.5, ROOD, "start"))
    # Een huisje links en rechts, want de schade is het gevolg dat men ziet.
    for x in (62, 118):
        d.append(f'<polygon points="{x-16},{grond} {x-16},{grond-20} {x},{grond-32} {x+16},{grond-20} {x+16},{grond}" '
                 f'fill="#f3ece0" stroke="{DARK}" stroke-width="1.3"/>')
    # De seismograaf rechtsboven: een lijn die uitslaat.
    sx, sy = 352, 34
    d.append(f'<rect x="{sx}" y="{sy-18}" width="104" height="40" rx="4" fill="#fff" stroke="{DIM}" stroke-width="1.2"/>')
    punten = []
    for i in range(53):
        x = sx + 4 + i * 1.85
        amp = 0 if i < 18 or i > 40 else 13 * math.sin(i * 1.7) * (1 - abs(i - 29) / 13)
        punten.append(f"{x:.1f},{sy + 2 - amp:.1f}")
    d.append(f'<polyline points="{" ".join(punten)}" fill="none" stroke="{ROOD}" stroke-width="1.3"/>')
    d.append(_tekst(sx + 52, sy + 34, "seismograaf", 9, DIM))
    return _svg(breedte, h, "".join(d))


def dalvormen(breedte=470):
    """Het V-dal van een rivier naast het U-dal van een gletsjer."""
    h = 190
    d = []
    vakken = [
        (16, "V-dal", "smalle bodem, een rivier snijdt zich in", "#9fb08c",
         "M 0 20 L 34 24 L 92 128 L 150 24 L 184 20"),
        (256, "U-dal", "brede bodem, een gletsjer schuurt uit", "#cfd6c6",
         "M 0 20 L 24 24 L 46 112 Q 92 142 138 112 L 160 24 L 184 20"),
    ]
    for x0, naam, onder, kleur, pad in vakken:
        verschoven = []
        for stuk in pad.split():
            verschoven.append(stuk)
        p = pad
        d.append(f'<g transform="translate({x0},14)">')
        d.append(f'<path d="{p} L 184 150 L 0 150 Z" fill="{kleur}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append('</g>')
        d.append(_tekst(x0 + 92, 176, naam, 11, INK, vet=True))
        d.append(_tekst(x0 + 92, 188 - 4, onder, 9, DIM))
    # Een streepje water op de bodem van het V-dal, en ijs in het U-dal.
    d.append(f'<ellipse cx="108" cy="140" rx="9" ry="3" fill="{WATER}"/>')
    d.append(f'<path d="M 302 126 Q 348 156 394 126 L 394 140 Q 348 170 302 140 Z" fill="{SNEEUW}" stroke="{DIM}" stroke-width="1"/>')

    return _svg(breedte, 196, "".join(d))


def slijtage(breedte=470):
    """Verwering, erosie en sedimentatie in drie stappen naast elkaar."""
    h = 186
    vak = breedte / 3
    d = []
    titels = [
        ("verwering", "de steen valt ter plaatse uiteen", "vorst, water, wortels"),
        ("erosie", "het losse materiaal wordt weggevoerd", "water, wind, ijs"),
        ("sedimentatie", "het wordt elders weer afgezet", "een delta, een zandbank, een duin"),
    ]
    for i, (naam, wat, door) in enumerate(titels):
        x = i * vak
        mid = x + vak / 2
        d.append(f'<rect x="{x+8:.1f}" y="8" width="{vak-16:.1f}" height="108" rx="6" fill="#faf8f3" stroke="{BORDER}" stroke-width="1.2"/>')
        if i == 0:
            d.append(f'<path d="M {mid-34} 96 L {mid-18} 48 L {mid+4} 44 L {mid+22} 96 Z" fill="#b9a98c" stroke="{DARK}" stroke-width="1.3"/>')
            d.append(f'<line x1="{mid-16}" y1="52" x2="{mid-4}" y2="94" stroke="{DARK}" stroke-width="1.2"/>')
            d.append(f'<line x1="{mid+2}" y1="46" x2="{mid+8}" y2="94" stroke="{DARK}" stroke-width="1.2"/>')
            d.append(f'<circle cx="{mid+28}" cy="92" r="3" fill="#b9a98c" stroke="{DARK}" stroke-width="0.9"/>')
        elif i == 1:
            d.append(f'<path d="M {mid-40} 52 Q {mid} 72 {mid+40} 96" fill="none" stroke="{WATER}" stroke-width="7" stroke-linecap="round"/>')
            for dx, dy in ((-16, 62), (4, 74), (22, 86)):
                d.append(f'<circle cx="{mid+dx}" cy="{dy}" r="3" fill="#b9a98c" stroke="{DARK}" stroke-width="0.9"/>')
            d.append(f'<path d="M {mid+28} 40 l 16 0 l -5 -5 m 5 5 l -5 5" fill="none" stroke="{DIM}" stroke-width="1.2"/>')
        else:
            d.append(f'<path d="M {mid-44} 96 Q {mid} 62 {mid+44} 96 Z" fill="{ZAND}" stroke="{DARK}" stroke-width="1.3"/>')
            for dx, dy in ((-20, 88), (0, 80), (18, 88)):
                d.append(f'<circle cx="{mid+dx}" cy="{dy}" r="2.6" fill="#b9a98c" stroke="{DARK}" stroke-width="0.8"/>')
        d.append(f'<line x1="{mid-46}" y1="96" x2="{mid+46}" y2="96" stroke="{DARK}" stroke-width="1.4"/>')
        d.append(_tekst(mid, 132, naam, 11, INK, vet=True))
        d.append(_tekst(mid, 148, wat, 8.5, INK))
        d.append(_tekst(mid, 162, door, 8.5, DIM))
        if i < 2:
            d.append(_tekst(x + vak, 66, "→", 16, AMBER))
    return _svg(breedte, h, "".join(d))


def broeikas(breedte=470):
    """Het broeikaseffect, en wat er verandert als er meer broeikasgassen bij komen."""
    h = 240
    d = []
    for i, (x0, kop, dikte, weg, onder) in enumerate([
            (10, "gewoon broeikaseffect", 5, 3, "een deel van de warmte gaat weg, de rest houdt de aarde leefbaar"),
            (242, "versterkt broeikaseffect", 11, 1, "er zitten meer broeikasgassen in de lucht, dus er ontsnapt minder"),
    ]):
        b = 218
        grond = 152
        d.append(f'<rect x="{x0}" y="16" width="{b}" height="{grond-16}" fill="#eaf1f6" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(f'<rect x="{x0}" y="{grond}" width="{b}" height="26" fill="{GRAS}" stroke="{DARK}" stroke-width="1.2"/>')
        # De laag broeikasgassen: hoe dikker, hoe meer warmte er blijft hangen.
        d.append(f'<rect x="{x0}" y="{52-dikte}" width="{b}" height="{dikte*2}" fill="{DIM}" opacity="0.35"/>')
        d.append(_tekst(x0 + b - 6, 50, "broeikasgassen", 8, DIM, "end"))
        # De zon links, met een straal naar de grond.
        d.append(f'<circle cx="{x0+28}" cy="34" r="11" fill="{AMBER}"/>')
        d.append(f'<path d="M {x0+38} 42 L {x0+96} {grond-6}" stroke="{AMBER}" stroke-width="2"/>')
        d.append(f'<path d="M {x0+90} {grond-20} l 8 16 l -14 -4" fill="{AMBER}"/>')
        # De warmte die terugkaatst: een paar pijlen omhoog, en een paar terug omlaag.
        for j in range(weg):
            x = x0 + 118 + j * 26
            d.append(f'<path d="M {x} {grond-6} L {x} 62" stroke="{ROOD}" stroke-width="1.6"/>')
            d.append(f'<path d="M {x-4} 68 L {x} 58 L {x+4} 68 Z" fill="{ROOD}"/>')
        for j in range(4 - weg + 1):
            x = x0 + 118 + (weg + j) * 26
            if x > x0 + b - 16:
                break
            d.append(f'<path d="M {x} {grond-6} L {x} 62" stroke="{ROOD}" stroke-width="1.6" opacity="0.5"/>')
            d.append(f'<path d="M {x} 56 L {x} {grond-14}" stroke="{ROOD}" stroke-width="1.6"/>')
            d.append(f'<path d="M {x-4} {grond-20} L {x} {grond-10} L {x+4} {grond-20} Z" fill="{ROOD}"/>')
        d.append(_tekst(x0 + b / 2, 10, kop, 10.5, INK, vet=True))
        regels = []
        regel = ""
        for woord in onder.split():
            if len(regel) + len(woord) + 1 > 44:
                regels.append(regel); regel = woord
            else:
                regel = (regel + " " + woord).strip()
        regels.append(regel)
        for j, r in enumerate(regels):
            d.append(_tekst(x0 + b / 2, 196 + j * 12, r, 8.5, DIM))
    d.append(_tekst(breedte / 2, h - 8, "Een rode pijl omhoog is warmte die weggaat; een pijl die terugbuigt is warmte die blijft hangen.", 9, DIM))
    return _svg(breedte, h, "".join(d))


def drukgebieden(breedte=470):
    """Een hogedrukgebied naast een lagedrukgebied, met het weer dat erbij hoort."""
    h = 208
    d = []
    for x0, letter, naam, kleur, weer in [
            (16, "H", "hogedrukgebied", "#5b93b8", ["lucht zakt naar beneden", "weinig wolken", "rustig en meestal droog"]),
            (256, "L", "lagedrukgebied of depressie", ROOD, ["lucht stijgt op", "wolken vormen zich", "wind en kans op regen"]),
    ]:
        b = 198
        d.append(f'<rect x="{x0}" y="10" width="{b}" height="118" rx="6" fill="#f7f9fb" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(f'<circle cx="{x0+46}" cy="64" r="26" fill="{kleur}" opacity="0.16"/>')
        d.append(_tekst(x0 + 46, 74, letter, 30, kleur, vet=True))
        # De pijl: omlaag bij hoge druk, omhoog bij lage druk.
        px = x0 + 100
        if letter == "H":
            d.append(f'<path d="M {px} 28 L {px} 96" stroke="{kleur}" stroke-width="2.4"/>')
            d.append(f'<path d="M {px-6} 88 L {px} 102 L {px+6} 88 Z" fill="{kleur}"/>')
            d.append(f'<ellipse cx="{px+52}" cy="44" rx="20" ry="9" fill="#ffffff" stroke="{BORDER}" stroke-width="1"/>')
        else:
            d.append(f'<path d="M {px} 102 L {px} 34" stroke="{kleur}" stroke-width="2.4"/>')
            d.append(f'<path d="M {px-6} 42 L {px} 28 L {px+6} 42 Z" fill="{kleur}"/>')
            for dx, dy, r in ((36, 40, 12), (52, 36, 15), (68, 42, 11)):
                d.append(f'<circle cx="{px+dx}" cy="{dy}" r="{r}" fill="#c8cfd6"/>')
            for j in range(4):
                xx = px + 34 + j * 12
                d.append(f'<line x1="{xx}" y1="56" x2="{xx-4}" y2="72" stroke="{WATER}" stroke-width="1.6"/>')
        d.append(_tekst(x0 + b / 2, 146, naam, 10.5, INK, vet=True))
        for j, r in enumerate(weer):
            d.append(_tekst(x0 + b / 2, 162 + j * 13, r, 9, DIM))
    return _svg(breedte, h, "".join(d))


def kaartlagen(breedte=470):
    """Kaartlagen die je in een viewer over elkaar legt, elk met wat ze toont."""
    h = 276
    d = []
    lagen = [
        ("luchtfoto", "hoe het gebied er echt uitziet", "#cfd6c6"),
        ("bodemkaart", "zand, leem of klei", "#d9c8a6"),
        ("hoogtelaag", "hoe hoog het ligt", "#c2d2df"),
        ("waterlopen", "beken, grachten, rivieren", "#a8cfe0"),
        ("bebouwing", "waar de huizen staan", "#e8d7c4"),
    ]
    bb, hh, schuin = 188, 52, 44
    for i, (naam, wat, kleur) in enumerate(lagen):
        y = 16 + i * 44
        x = 28 + (len(lagen) - 1 - i) * 6
        punten = f"{x},{y+hh} {x+schuin},{y} {x+schuin+bb},{y} {x+bb},{y+hh}"
        d.append(f'<polygon points="{punten}" fill="{kleur}" stroke="{DARK}" stroke-width="1.2" opacity="0.93"/>')
        d.append(_tekst(x + schuin + bb + 12, y + 24, naam, 10, INK, "start", vet=True))
        d.append(_tekst(x + schuin + bb + 12, y + 36, wat, 8.5, DIM, "start"))
    d.append(_tekst(24, h - 8, "In een viewer zet je elke laag apart aan of uit. Wat samenvalt, valt meteen op.", 9, DIM, "start"))
    return _svg(breedte, h, "".join(d))


def bodemprofiel(breedte=470):
    """Een kuiltje in de bodem, met de lagen die je erin ziet zitten."""
    h = 230
    x0, bb = 30, 250
    lagen = [
        (0, 34, "#4a3f2e", "strooisel en humus", "donker, veel plantenresten"),
        (34, 96, "#6b563a", "bovenste bodemlaag", "waarin de wortels zitten"),
        (96, 150, "#a08a63", "onderste bodemlaag", "lichter, minder humus"),
        (150, 190, "#b9a98c", "ondergrond", "zand, leem, klei of gesteente"),
    ]
    d = [f'<rect x="{x0}" y="20" width="{bb}" height="190" fill="#ffffff"/>']
    for y0, y1, kleur, naam, uitleg in lagen:
        d.append(f'<rect x="{x0}" y="{20+y0}" width="{bb}" height="{y1-y0}" fill="{kleur}"/>')
        d.append(f'<line x1="{x0+bb}" y1="{20+(y0+y1)/2}" x2="{x0+bb+16}" y2="{20+(y0+y1)/2}" stroke="{DIM}" stroke-width="1"/>')
        d.append(_tekst(x0 + bb + 22, 20 + (y0 + y1) / 2 - 2, naam, 9.5, INK, "start", vet=True))
        d.append(_tekst(x0 + bb + 22, 20 + (y0 + y1) / 2 + 10, uitleg, 8, DIM, "start"))
    d.append(f'<rect x="{x0}" y="20" width="{bb}" height="190" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
    # Een graspol en een paar worteltjes bovenaan, zodat het een echte kuil lijkt.
    for i in range(9):
        gx = x0 + 14 + i * 27
        d.append(f'<path d="M {gx} 20 q 3 -10 7 -12" fill="none" stroke="{GRAS}" stroke-width="2"/>')
        d.append(f'<path d="M {gx+4} 20 q -3 -9 -7 -11" fill="none" stroke="{GRAS}" stroke-width="2"/>')
    for i in range(4):
        wx = x0 + 34 + i * 58
        d.append(f'<path d="M {wx} 22 q 6 34 -4 68" fill="none" stroke="#d8c9a8" stroke-width="1.2" opacity="0.7"/>')
    d.append(_tekst(x0, h - 8, "Graaf een klein kuiltje: de lagen liggen onder elkaar en verschillen in kleur en textuur.", 9, DIM, "start"))
    return _svg(breedte, h, "".join(d))


def transect(breedte=470):
    """Een transect: het landschap zoals je het van opzij zou zien, met wat erop staat."""
    h = 226
    basis = 168
    # Het terrein: laag bij de beek links, klimmend naar een bos rechts.
    punten = [(0, 150), (54, 148), (96, 140), (150, 126), (214, 104),
              (286, 78), (360, 58), (430, 46), (470, 42)]
    pad = " ".join(f"{x},{basis - (150 - y)}" if False else f"{x},{y}" for x, y in punten)
    d = [f'<polygon points="{pad} 470,{basis} 0,{basis}" fill="#dfe7d5" stroke="{DARK}" stroke-width="1.6"/>']

    def hoogte(x):
        for (x1, y1), (x2, y2) in zip(punten, punten[1:]):
            if x1 <= x <= x2:
                return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        return punten[-1][1]

    # De beek in de laagte, dan weide, dorp, akker en bos hogerop.
    d.append(f'<ellipse cx="26" cy="150" rx="22" ry="5" fill="{WATER}" stroke="{DIM}" stroke-width="1"/>')
    for x in (80, 112):
        y = hoogte(x)
        d.append(f'<path d="M {x} {y} q 3 -9 7 -11 M {x+4} {y} q -3 -8 -7 -10" fill="none" stroke="{GRAS}" stroke-width="1.8"/>')
    for x in (168, 196, 224):
        y = hoogte(x)
        d.append(f'<polygon points="{x-11},{y} {x-11},{y-13} {x},{y-22} {x+11},{y-13} {x+11},{y}" '
                 f'fill="#f3ece0" stroke="{DARK}" stroke-width="1.2"/>')
    for i in range(7):
        x = 276 + i * 11
        y = hoogte(x)
        d.append(f'<line x1="{x}" y1="{y}" x2="{x-5}" y2="{y-10}" stroke="{ZAND_DONKER}" stroke-width="1.6"/>')
    for x in (382, 406, 430, 452):
        y = hoogte(x)
        d.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-12}" stroke="#7a5b3a" stroke-width="2"/>')
        d.append(f'<circle cx="{x}" cy="{y-20}" r="10" fill="{LOOF}"/>')
    etiketten = [(26, "beek"), (96, "weide"), (196, "dorp"), (304, "akker"), (416, "bos")]
    for x, naam in etiketten:
        d.append(_tekst(x, basis + 15, naam, 9.5, INK, vet=True))
    d.append(f'<line x1="0" y1="{basis}" x2="{breedte}" y2="{basis}" stroke="{DARK}" stroke-width="1.6"/>')
    d.append(f'<path d="M 12 {basis+30} L 458 {basis+30}" stroke="{DIM}" stroke-width="1.2"/>')
    d.append(_tekst(12, basis + 44, "laag, nat", 9, DIM, "start"))
    d.append(_tekst(458, basis + 44, "hoog, droog", 9, DIM, "end"))
    d.append(_tekst(breedte / 2, basis + 44, "je tekent wat je ziet, van links naar rechts", 9, DIM))
    return _svg(breedte, h, "".join(d))


def schemasymbolen(breedte=470):
    """De symbolen van een elektrisch schema, met hun naam eronder."""
    h = 200
    namen = [
        ("spanningsbron", "batterij"),
        ("lamp", "lampje"),
        ("schakelaar", "open of dicht"),
        ("weerstand", "remt de stroom"),
        ("zoemer", "maakt geluid"),
        ("LED", "één richting"),
        ("motor", "draait"),
        ("meter", "meet"),
    ]
    kol, rij = 4, 2
    bv, bh = breedte / kol, 92
    d = []
    for i, (naam, onder) in enumerate(namen):
        cx = (i % kol) * bv + bv / 2
        cy = (i // kol) * bh + 34
        d.append(f'<line x1="{cx-30}" y1="{cy}" x2="{cx-16}" y2="{cy}" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(f'<line x1="{cx+16}" y1="{cy}" x2="{cx+30}" y2="{cy}" stroke="{DARK}" stroke-width="1.6"/>')
        if naam == "spanningsbron":
            for dx, hh, dik in [(-7, 18, 2.2), (1, 9, 4.2), (9, 18, 2.2)]:
                d.append(f'<line x1="{cx+dx}" y1="{cy-hh/2}" x2="{cx+dx}" y2="{cy+hh/2}" stroke="{DARK}" stroke-width="{dik}"/>')
            d.append(f'<line x1="{cx-16}" y1="{cy}" x2="{cx-9}" y2="{cy}" stroke="{DARK}" stroke-width="1.6"/>')
            d.append(f'<line x1="{cx+11}" y1="{cy}" x2="{cx+16}" y2="{cy}" stroke="{DARK}" stroke-width="1.6"/>')
        elif naam == "lamp":
            d.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
            d.append(f'<path d="M{cx-8.5} {cy-8.5} l17 17 M{cx+8.5} {cy-8.5} l-17 17" stroke="{DARK}" stroke-width="1.5"/>')
        elif naam == "schakelaar":
            d.append(f'<circle cx="{cx-14}" cy="{cy}" r="2.4" fill="{DARK}"/>')
            d.append(f'<circle cx="{cx+14}" cy="{cy}" r="2.4" fill="{DARK}"/>')
            d.append(f'<line x1="{cx-14}" y1="{cy}" x2="{cx+11}" y2="{cy-13}" stroke="{DARK}" stroke-width="1.8"/>')
        elif naam == "weerstand":
            d.append(f'<rect x="{cx-16}" y="{cy-7}" width="32" height="14" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
        elif naam == "zoemer":
            d.append(f'<path d="M{cx-14} {cy+8} L{cx-14} {cy-8} A 14 14 0 0 1 {cx+14} {cy-8} L{cx+14} {cy+8} Z" '
                     f'fill="none" stroke="{DARK}" stroke-width="1.6"/>')
        elif naam == "LED":
            d.append(f'<polygon points="{cx-10},{cy-10} {cx-10},{cy+10} {cx+8},{cy}" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
            d.append(f'<line x1="{cx+8}" y1="{cy-10}" x2="{cx+8}" y2="{cy+10}" stroke="{DARK}" stroke-width="1.8"/>')
            for dx, dy in ((2, -14), (9, -12)):
                d.append(f'<path d="M{cx+dx} {cy+dy} l7 -7 l-2.5 0 m2.5 0 l0 2.5" fill="none" stroke="{AMBER}" stroke-width="1.3"/>')
        elif naam == "motor":
            d.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
            d.append(_tekst(cx, cy + 4, "M", 12, DARK, vet=True))
        else:
            d.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
            d.append(_tekst(cx, cy + 4, "A", 11, DARK, vet=True))
        d.append(_tekst(cx, cy + 32, naam, 9.5, INK, vet=True))
        d.append(_tekst(cx, cy + 44, onder, 8.5, DIM))
    d.append(_tekst(breedte / 2, h - 6, "In een schema teken je het symbool, nooit een afbeelding van het onderdeel zelf.", 9, DIM))
    return _svg(breedte, h, "".join(d))


def poorten(breedte=470):
    """De EN-, OF- en NIET-poort, elk met haar waarheidstabel eronder."""
    h = 236
    vak = breedte / 3
    soorten = [
        ("EN", "alleen 1 als ALLE ingangen 1 zijn", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)], 2),
        ("OF", "al 1 zodra ÉÉN ingang 1 is", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)], 2),
        ("NIET", "draait de ingang om", [(0, 1), (1, 0)], 1),
    ]
    d = []
    for i, (naam, uitleg, tabel_, ingangen) in enumerate(soorten):
        x = i * vak + vak / 2
        cy = 46
        # De poort zelf, als eenvoudige doos met haar naam erin.
        d.append(f'<rect x="{x-30}" y="{cy-22}" width="60" height="44" rx="5" fill="#f2f5f0" stroke="{DARK}" stroke-width="1.6"/>')
        d.append(_tekst(x, cy + 5, naam, 14, FOREST, vet=True))
        if ingangen == 2:
            d.append(f'<line x1="{x-52}" y1="{cy-10}" x2="{x-30}" y2="{cy-10}" stroke="{DARK}" stroke-width="1.5"/>')
            d.append(f'<line x1="{x-52}" y1="{cy+10}" x2="{x-30}" y2="{cy+10}" stroke="{DARK}" stroke-width="1.5"/>')
            d.append(_tekst(x - 56, cy - 6, "A", 9, DIM, "end"))
            d.append(_tekst(x - 56, cy + 14, "B", 9, DIM, "end"))
        else:
            d.append(f'<line x1="{x-52}" y1="{cy}" x2="{x-30}" y2="{cy}" stroke="{DARK}" stroke-width="1.5"/>')
            d.append(_tekst(x - 56, cy + 4, "A", 9, DIM, "end"))
        d.append(f'<line x1="{x+30}" y1="{cy}" x2="{x+50}" y2="{cy}" stroke="{DARK}" stroke-width="1.5"/>')
        d.append(_tekst(x + 54, cy + 4, "U", 9, DIM, "start"))
        d.append(_tekst(x, 96, uitleg, 8.5, DIM))
        # De waarheidstabel eronder.
        kop = ["A", "B", "U"] if ingangen == 2 else ["A", "U"]
        cel = 30
        bb = cel * len(kop)
        tx = x - bb / 2
        ty = 110
        for j, k in enumerate(kop):
            d.append(f'<rect x="{tx+j*cel}" y="{ty}" width="{cel}" height="20" fill="{FOREST}"/>')
            d.append(_tekst(tx + j * cel + cel / 2, ty + 14, k, 9.5, "#ffffff", vet=True))
        for r, regel in enumerate(tabel_):
            for j, w in enumerate(regel):
                vy = ty + 20 + r * 20
                vul = "#ffffff" if r % 2 == 0 else "#f6f8f5"
                d.append(f'<rect x="{tx+j*cel}" y="{vy}" width="{cel}" height="20" fill="{vul}" stroke="{BORDER}" stroke-width="0.8"/>')
                laatste = j == len(regel) - 1
                d.append(_tekst(tx + j * cel + cel / 2, vy + 14, str(w), 9.5,
                                AMBER if laatste and w == 1 else INK, vet=laatste))
    d.append(_tekst(breedte / 2, h - 6, "1 is aan of waar, 0 is uit of niet waar. De kolom U is de uitgang.", 9, DIM))
    return _svg(breedte, h, "".join(d))


def ipo(breedte=470):
    """Het IPO-model: invoer, verwerking, uitvoer, met een voorbeeld eronder."""
    h = 176
    vakb, tussen = 124, 42
    start = (breedte - 3 * vakb - 2 * tussen) / 2
    stukken = [
        ("invoer", "de sensor meet iets", "een temperatuursensor", "#e8eef4"),
        ("verwerking", "de sturing beslist", "de regelaar vergelijkt met 20 °C", "#eef1e9"),
        ("uitvoer", "de actuator doet iets", "de ketel slaat aan", "#f6ecdc"),
    ]
    d = []
    for i, (naam, wat, vb, kleur) in enumerate(stukken):
        x = start + i * (vakb + tussen)
        d.append(f'<rect x="{x:.1f}" y="18" width="{vakb}" height="76" rx="6" fill="{kleur}" stroke="{DARK}" stroke-width="1.4"/>')
        mid = x + vakb / 2
        d.append(_tekst(mid, 44, naam, 12, INK, vet=True))
        d.append(_tekst(mid, 62, wat, 8.5, DIM))
        for j, regel in enumerate(_regels(vb, 22)):
            d.append(_tekst(mid, 112 + j * 12, regel, 8.5, INK))
        if i < 2:
            px = x + vakb + 6
            d.append(f'<line x1="{px}" y1="56" x2="{px+tussen-12}" y2="56" stroke="{AMBER}" stroke-width="2.2"/>')
            d.append(f'<path d="M{px+tussen-18} 50 l8 6 l-8 6 Z" fill="{AMBER}"/>')
    d.append(_tekst(breedte / 2, h - 6, "Een sensor meet, een actuator doet. Daartussen zit de verwerking.", 9, DIM))
    return _svg(breedte, h, "".join(d))


def _regels(tekst, breed):
    """Breek een zin af in regels van hoogstens `breed` tekens."""
    uit, regel = [], ""
    for woord in tekst.split():
        if len(regel) + len(woord) + 1 > breed:
            uit.append(regel)
            regel = woord
        else:
            regel = (regel + " " + woord).strip()
    uit.append(regel)
    return uit


def technischproces(breedte=470):
    """De vijf fasen van het technisch proces, met de terugkeer naar fase 2 of 3."""
    h = 200
    fasen = [
        ("1", "probleemstelling", "wat heeft de gebruiker nodig? criteria vastleggen"),
        ("2", "ontwerpen", "schets, materiaal, gereedschap, verbindingen"),
        ("3", "maken", "volgens het stappenplan, en veilig"),
        ("4", "in gebruik nemen", "gebruiken en testen"),
        ("5", "evalueren", "voldoet het aan de criteria?"),
    ]
    vak = (breedte - 8) / 5
    d = []
    for i, (nr, naam, wat) in enumerate(fasen):
        x = 4 + i * vak
        d.append(f'<rect x="{x+3:.1f}" y="14" width="{vak-6:.1f}" height="104" rx="6" fill="#f2f5f0" '
                 f'stroke="{FOREST}" stroke-width="1.4"/>')
        mid = x + vak / 2
        d.append(f'<circle cx="{mid:.1f}" cy="32" r="11" fill="{FOREST}"/>')
        d.append(_tekst(mid, 36, nr, 11, "#ffffff", vet=True))
        for j, r in enumerate(_regels(naam, 12)):
            d.append(_tekst(mid, 58 + j * 11, r, 8.5, INK, vet=True))
        for j, r in enumerate(_regels(wat, 17)):
            d.append(_tekst(mid, 82 + j * 10, r, 7.5, DIM))
        if i < 4:
            px = x + vak - 2
            d.append(f'<path d="M{px-3} 58 l9 8 l-9 8 Z" fill="{AMBER}"/>')
    # De terugkeerpijl: bij een fout ga je naar fase 2 of 3, niet naar fase 1.
    x2 = 4 + 1.5 * vak
    x3 = 4 + 2.5 * vak
    x5 = 4 + 4.5 * vak
    d.append(f'<path d="M{x5:.1f} 122 L{x5:.1f} 150 L{x2:.1f} 150 L{x2:.1f} 126" fill="none" '
             f'stroke="{ROOD}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    d.append(f'<path d="M{x2-5:.1f} 132 L{x2:.1f} 120 L{x2+5:.1f} 132 Z" fill="{ROOD}"/>')
    d.append(f'<path d="M{x3:.1f} 150 L{x3:.1f} 126" fill="none" stroke="{ROOD}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    d.append(f'<path d="M{x3-5:.1f} 132 L{x3:.1f} 120 L{x3+5:.1f} 132 Z" fill="{ROOD}"/>')
    d.append(_tekst(breedte / 2, 166, "Voldoet het niet aan de criteria, dan keer je terug naar fase 2 of fase 3.", 9.5, ROOD))
    d.append(_tekst(breedte / 2, 182, "Niet naar fase 1: het probleem en de criteria staan al vast.", 9.5, DIM))
    return _svg(breedte, h, "".join(d))


def overbrengingen(breedte=470):
    """Vier overbrengingen naast elkaar: tandwielen, ketting, riem en wrijvingswielen."""
    import math
    h = 220
    vak = breedte / 2
    d = []

    def tandwiel(cx, cy, r, tanden, kleur="#cfd6c6"):
        uit = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{kleur}" stroke="{DARK}" stroke-width="1.4"/>']
        for k in range(tanden):
            a = 2 * math.pi * k / tanden
            uit.append(f'<line x1="{cx+math.cos(a)*r:.1f}" y1="{cy+math.sin(a)*r:.1f}" '
                       f'x2="{cx+math.cos(a)*(r+4):.1f}" y2="{cy+math.sin(a)*(r+4):.1f}" '
                       f'stroke="{DARK}" stroke-width="2.4"/>')
        uit.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{DARK}"/>')
        return "".join(uit)

    # 1. Twee tandwielen die in elkaar grijpen: rechtstreeks, en ze draaien tegengesteld.
    d.append(tandwiel(66, 54, 24, 12))
    d.append(tandwiel(122, 54, 24, 12))
    d.append(_tekst(94, 96, "tandwielen", 10, INK, vet=True))
    d.append(_tekst(94, 108, "rechtstreeks, tegengestelde zin", 8, DIM))
    d.append(f'<path d="M 50 34 a 22 22 0 0 1 20 -8" fill="none" stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(f'<path d="M 70 26 l -7 -1 l 4 6 Z" fill="{AMBER}"/>')
    d.append(f'<path d="M 138 34 a 22 22 0 0 0 -20 -8" fill="none" stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(f'<path d="M 118 26 l 7 -1 l -4 6 Z" fill="{AMBER}"/>')
    # 2. Ketting over twee tandwielen: onrechtstreeks, zelfde zin.
    d.append(tandwiel(300, 54, 22, 11))
    d.append(tandwiel(392, 54, 14, 8))
    d.append(f'<path d="M 300 32 L 392 40 M 300 76 L 392 68" stroke="{DARK}" stroke-width="2.6"/>')
    d.append(_tekst(346, 96, "ketting over twee tandwielen", 10, INK, vet=True))
    d.append(_tekst(346, 108, "onrechtstreeks, zelfde zin, slipt niet", 8, DIM))
    # 3. Riem: onrechtstreeks, en gekruist draait de volger om.
    for cx, r in ((66, 22), (150, 14)):
        d.append(f'<circle cx="{cx}" cy="158" r="{r}" fill="#dfe7d5" stroke="{DARK}" stroke-width="1.4"/>')
        d.append(f'<circle cx="{cx}" cy="158" r="3" fill="{DARK}"/>')
    d.append(f'<path d="M 66 136 L 150 144 M 66 180 L 150 172" stroke="{AMBER}" stroke-width="2.2"/>')
    d.append(_tekst(108, 198, "riemoverbrenging", 10, INK, vet=True))
    d.append(_tekst(108, 210, "riem, niet gekruist: zelfde zin", 8, DIM))
    # 4. Wrijvingswielen: ze raken elkaar en kunnen slippen.
    d.append(f'<circle cx="318" cy="158" r="21" fill="#e4dccd" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<circle cx="366" cy="158" r="27" fill="#e4dccd" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<circle cx="318" cy="158" r="3" fill="{DARK}"/>')
    d.append(f'<circle cx="366" cy="158" r="3" fill="{DARK}"/>')
    d.append(_tekst(346, 198, "wrijvingswielen", 10, INK, vet=True))
    d.append(_tekst(346, 210, "raken elkaar, kunnen slippen", 8, DIM))
    return _svg(breedte, h, "".join(d))


def krachtsoorten(breedte=470):
    """De vier krachten op een constructie: druk, trek, torsie en buiging."""
    h = 168
    vak = breedte / 4
    soorten = [
        ("druk", "van twee kanten samengeduwd"),
        ("trek", "van twee kanten uit elkaar getrokken"),
        ("torsie", "gewrongen om zijn as"),
        ("buiging", "doorgebogen in het midden"),
    ]
    d = []
    for i, (naam, wat) in enumerate(soorten):
        x0 = i * vak
        mid = x0 + vak / 2
        cy = 56
        if naam == "buiging":
            d.append(f'<path d="M {mid-40} {cy-8} Q {mid} {cy+22} {mid+40} {cy-8} L {mid+40} {cy+4} '
                     f'Q {mid} {cy+34} {mid-40} {cy+4} Z" fill="#cfd6c6" stroke="{DARK}" stroke-width="1.4"/>')
            d.append(f'<path d="M {mid} {cy-30} L {mid} {cy-2}" stroke="{ROOD}" stroke-width="2"/>')
            d.append(f'<path d="M {mid-5} {cy-8} L {mid} {cy+2} L {mid+5} {cy-8} Z" fill="{ROOD}"/>')
        elif naam == "torsie":
            d.append(f'<rect x="{mid-40}" y="{cy-9}" width="80" height="18" fill="#cfd6c6" stroke="{DARK}" stroke-width="1.4"/>')
            d.append(f'<path d="M {mid-46} {cy-16} a 16 16 0 0 1 0 32" fill="none" stroke="{ROOD}" stroke-width="2"/>')
            d.append(f'<path d="M {mid-46} {cy+10} l -4 8 l 9 -2 Z" fill="{ROOD}"/>')
            d.append(f'<path d="M {mid+46} {cy+16} a 16 16 0 0 1 0 -32" fill="none" stroke="{ROOD}" stroke-width="2"/>')
            d.append(f'<path d="M {mid+46} {cy-10} l 4 -8 l -9 2 Z" fill="{ROOD}"/>')
        else:
            d.append(f'<rect x="{mid-30}" y="{cy-10}" width="60" height="20" fill="#cfd6c6" stroke="{DARK}" stroke-width="1.4"/>')
            if naam == "druk":
                d.append(f'<path d="M {mid-52} {cy} L {mid-34} {cy}" stroke="{ROOD}" stroke-width="2.2"/>')
                d.append(f'<path d="M {mid-34} {cy-5} l 8 5 l -8 5 Z" fill="{ROOD}"/>')
                d.append(f'<path d="M {mid+52} {cy} L {mid+34} {cy}" stroke="{ROOD}" stroke-width="2.2"/>')
                d.append(f'<path d="M {mid+34} {cy-5} l -8 5 l 8 5 Z" fill="{ROOD}"/>')
            else:
                d.append(f'<path d="M {mid-34} {cy} L {mid-52} {cy}" stroke="{ROOD}" stroke-width="2.2"/>')
                d.append(f'<path d="M {mid-52} {cy-5} l -8 5 l 8 5 Z" fill="{ROOD}"/>')
                d.append(f'<path d="M {mid+34} {cy} L {mid+52} {cy}" stroke="{ROOD}" stroke-width="2.2"/>')
                d.append(f'<path d="M {mid+52} {cy-5} l 8 5 l -8 5 Z" fill="{ROOD}"/>')
        d.append(_tekst(mid, 112, naam, 11, INK, vet=True))
        for j, r in enumerate(_regels(wat, 18)):
            d.append(_tekst(mid, 128 + j * 11, r, 8.5, DIM))
    return _svg(breedte, h, "".join(d))


def aanzichten(breedte=470):
    """Een blokje in perspectief, met zijn drie aanzichten ernaast."""
    h = 218
    d = []
    # Links het voorwerp schuin getekend: een liggend blok met een uitsparing.
    ox, oy = 40, 70
    b, hh, dp = 96, 46, 26
    d.append(f'<polygon points="{ox},{oy} {ox+b},{oy} {ox+b},{oy+hh} {ox},{oy+hh}" fill="#dfe7d5" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(f'<polygon points="{ox},{oy} {ox+dp},{oy-dp} {ox+b+dp},{oy-dp} {ox+b},{oy}" fill="#cfd6c6" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(f'<polygon points="{ox+b},{oy} {ox+b+dp},{oy-dp} {ox+b+dp},{oy+hh-dp} {ox+b},{oy+hh}" fill="#b9c8a8" stroke="{DARK}" stroke-width="1.5"/>')
    d.append(_tekst(ox + b / 2, oy + hh + 22, "het voorwerp", 10, INK, vet=True))
    d.append(_tekst(ox + b / 2, oy + hh + 34, "isometrisch getekend", 8.5, DIM))
    # Rechts de drie aanzichten, elk in zijn eigen kadertje.
    vakken = [("vooraanzicht", "wat je ziet als je er recht voor staat", 96, 46),
              ("bovenaanzicht", "wat je ziet als je erop neerkijkt", 96, 26),
              ("zijaanzicht", "wat je ziet als je opzij gaat staan", 26, 46)]
    x = 232
    for i, (naam, wat, bb, hhh) in enumerate(vakken):
        y = 16 + i * 66
        d.append(f'<rect x="{x}" y="{y}" width="{bb}" height="{hhh}" fill="#f2f5f0" stroke="{DARK}" stroke-width="1.5"/>')
        d.append(_tekst(x + 112, y + hhh / 2 - 2, naam, 9.5, INK, "start", vet=True))
        d.append(_tekst(x + 112, y + hhh / 2 + 10, wat, 8, DIM, "start"))
    d.append(_tekst(breedte / 2, h - 6, "Een aanzicht is altijd plat: je tekent geen diepte, alleen wat je vanuit die ene kant ziet.", 9, DIM))
    return _svg(breedte, h, "".join(d))


def leeftijdshistogram(breedte=470):
    """Drie leeftijdshistogrammen naast elkaar: piramide, klok en urn.

    De cijfers zijn geen echte landencijfers maar de drie schoolvormen van het
    model, zodat een kind aan de vórm leert aflezen en niet aan een landnaam.
    Links de mannen, rechts de vrouwen, van jong onderaan naar oud bovenaan,
    zoals op elk leeftijdshistogram.
    """
    h = 230
    vormen = [
        ("piramide", "veel kinderen, weinig ouderen",
         [1.00, 0.88, 0.76, 0.64, 0.53, 0.42, 0.32, 0.22, 0.13, 0.06]),
        ("klok", "de groepen liggen dicht bij elkaar",
         [0.72, 0.78, 0.84, 0.88, 0.86, 0.78, 0.64, 0.46, 0.27, 0.11]),
        ("urn", "weinig kinderen, veel ouderen",
         [0.46, 0.52, 0.60, 0.70, 0.82, 0.90, 0.86, 0.72, 0.48, 0.20]),
    ]
    kolom = breedte / 3
    balk_h = 13
    onder = 186
    d = []
    for i, (naam, onderschrift, waarden) in enumerate(vormen):
        mid = kolom * i + kolom / 2
        half = kolom / 2 - 16
        for j, w in enumerate(waarden):
            y = onder - (j + 1) * balk_h
            b = w * half
            d.append(f'<rect x="{mid-b:.1f}" y="{y}" width="{b:.1f}" height="{balk_h-2}" '
                     f'fill="#9fb7c8" stroke="{DARK}" stroke-width="0.7"/>')
            d.append(f'<rect x="{mid:.1f}" y="{y}" width="{b:.1f}" height="{balk_h-2}" '
                     f'fill="#d8bfa6" stroke="{DARK}" stroke-width="0.7"/>')
        d.append(f'<line x1="{mid:.1f}" y1="{onder-len(waarden)*balk_h}" x2="{mid:.1f}" '
                 f'y2="{onder}" stroke="{DARK}" stroke-width="1.2"/>')
        d.append(f'<line x1="{mid-half:.1f}" y1="{onder}" x2="{mid+half:.1f}" y2="{onder}" '
                 f'stroke="{INK}" stroke-width="1.6"/>')
        d.append(_tekst(mid, onder + 16, naam, 11, AMBER, vet=True))
        for regel_i, regel in enumerate(_regels(onderschrift, 22)):
            d.append(_tekst(mid, onder + 30 + regel_i * 12, regel, 9, DIM))
    d.append(_tekst(kolom / 2 - 34, 20, "mannen", 9, DIM, "end"))
    d.append(_tekst(kolom / 2 + 34, 20, "vrouwen", 9, DIM, "start"))
    d.append(_tekst(breedte - 8, 20, "onderaan de jongste groep, bovenaan de oudste",
                    9, DIM, "end"))
    return _svg(breedte, h, "".join(d))


def demografische_transitie(breedte=470):
    """De vier fasen van de demografische transitie, met beide cijfers.

    De bruine lijn is het geboortecijfer, de blauwe het sterftecijfer. Het
    gekleurde vlak ertussen is de natuurlijke aangroei: hoe wijder het gat,
    hoe sneller de bevolking groeit.
    """
    links, rechts = 42, breedte - 10
    boven, onder = 24, 156
    h = 212
    span = rechts - links

    def x(f):
        return links + f * span

    def y(waarde):                      # waarde in ‰, van 0 tot 45
        return onder - waarde / 45 * (onder - boven)

    fracties = [0.00, 0.12, 0.25, 0.38, 0.50, 0.62, 0.75, 0.88, 1.00]
    geboorte = [40, 40, 39, 37, 32, 24, 17, 13, 11]
    sterfte = [38, 34, 26, 18, 13, 11, 10, 10, 11]
    gb = " ".join(f"{x(f):.1f},{y(v):.1f}" for f, v in zip(fracties, geboorte))
    st = " ".join(f"{x(f):.1f},{y(v):.1f}" for f, v in zip(fracties, sterfte))
    vlak = gb + " " + " ".join(
        f"{x(f):.1f},{y(v):.1f}" for f, v in zip(reversed(fracties), reversed(sterfte)))
    d = [f'<polygon points="{vlak}" fill="#cfe0d4" opacity="0.75"/>']
    d.append(f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{onder}" stroke="{DIM}" stroke-width="1.4"/>')
    d.append(f'<line x1="{links}" y1="{onder}" x2="{rechts}" y2="{onder}" stroke="{DIM}" stroke-width="1.4"/>')
    for waarde in (0, 20, 40):
        d.append(f'<line x1="{links-4}" y1="{y(waarde):.1f}" x2="{links}" y2="{y(waarde):.1f}" '
                 f'stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(links - 7, y(waarde) + 3.5, f"{waarde}", 9, DIM, "end"))
    d.append(_tekst(links - 7, 14, "per 1000", 9, DIM, "end"))
    for i in (1, 2, 3):
        gx = x(i / 4)
        d.append(f'<line x1="{gx:.1f}" y1="{boven}" x2="{gx:.1f}" y2="{onder}" stroke="{DIM}" '
                 f'stroke-width="1.1" stroke-dasharray="4 4" opacity="0.6"/>')
    d.append(f'<polyline points="{gb}" fill="none" stroke="{AMBER}" stroke-width="2.4"/>')
    d.append(f'<polyline points="{st}" fill="none" stroke="#5b7f9c" stroke-width="2.4"/>')
    for i, (naam, bij) in enumerate([
            ("fase 1", "beide hoog"),
            ("fase 2", "sterfte daalt"),
            ("fase 3", "geboorte daalt"),
            ("fase 4", "beide laag")]):
        mx = x((i + 0.5) / 4)
        d.append(_tekst(mx, onder + 16, naam, 10, DARK, vet=True))
        d.append(_tekst(mx, onder + 29, bij, 9, DIM))
    d.append(_tekst(x(0.5), 14, "geboortecijfer", 9.5, AMBER, "end"))
    d.append(_tekst(x(0.54), 14, "sterftecijfer", 9.5, "#5b7f9c", "start"))
    return _svg(breedte, h + 16, "".join(d))


def stralingsbalans(breedte=470):
    """Wat er met het zonlicht gebeurt: terugkaatsen of opnemen, en albedo."""
    h = 232
    d = []
    for i, (x0, kop, albedo, kleur, terug, op) in enumerate([
            (10, "sneeuw en ijs", "hoog albedo", "#e8eef3", 4, 1),
            (242, "water en donker bos", "laag albedo", "#3d5a6c", 1, 4)]):
        b, grond = 218, 150
        d.append(f'<rect x="{x0}" y="16" width="{b}" height="{grond-16}" fill="#eaf1f6" '
                 f'stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(f'<rect x="{x0}" y="{grond}" width="{b}" height="30" fill="{kleur}" '
                 f'stroke="{DARK}" stroke-width="1.2"/>')
        d.append(f'<circle cx="{x0+26}" cy="34" r="11" fill="{AMBER}"/>')
        d.append(f'<path d="M {x0+36} 42 L {x0+96} {grond-4}" stroke="{AMBER}" stroke-width="2.2"/>')
        d.append(f'<path d="M {x0+90} {grond-18} l 8 14 l -13 -3" fill="{AMBER}"/>')
        for j in range(terug):                      # teruggekaatst zonlicht
            sx = x0 + 104 + j * 16
            d.append(f'<path d="M {sx} {grond-4} L {sx+14} 30" stroke="{AMBER}" stroke-width="1.8"/>')
            d.append(f'<path d="M {sx+10} 42 l 5 -13 l -11 4" fill="{AMBER}"/>')
        for j in range(op):                         # opgenomen als warmte
            sx = x0 + 40 + j * 15
            d.append(f'<path d="M {sx} {grond+6} v 18" stroke="#b9472e" stroke-width="1.8"/>')
            d.append(f'<path d="M {sx-4} {grond+20} l 4 8 l 4 -8" fill="#b9472e"/>')
        d.append(_tekst(x0 + b / 2, 190, kop, 11, DARK, vet=True))
        d.append(_tekst(x0 + b / 2, 204, albedo, 10, AMBER))
        d.append(_tekst(x0 + b / 2, 220,
                        "kaatst veel terug" if terug > op else "neemt veel warmte op", 9, DIM))
    return _svg(breedte, h, "".join(d))


# ──────────────────────────────────── economie

def _as_vlak(breedte, hoogte, xlabel, ylabel, links=44, onder=36, boven=18, rechts=16):
    """Twee assen met een label eraan. Geeft (lijst, x(), y()) terug.

    De labels staan buiten het vlak: dat van de zij-as bovenaan, dat van de
    onderas rechts, zodat ze nooit over een curve komen.
    """
    b, h = breedte - links - rechts, hoogte - onder - boven
    def x(v):
        return links + v / 10 * b
    def y(v):
        return hoogte - onder - v / 10 * h
    d = [f'<line x1="{links}" y1="{boven-4}" x2="{links}" y2="{hoogte-onder}" stroke="{INK}" stroke-width="1.8"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte-rechts+4}" y2="{hoogte-onder}" stroke="{INK}" stroke-width="1.8"/>',
         _tekst(links - 2, boven - 6, ylabel, 10.5, DIM, "start", True),
         _tekst(breedte - rechts + 4, hoogte - onder + 16, xlabel, 10.5, DIM, "end", True)]
    return d, x, y


def marktevenwicht(breedte=430, verschuiving=None, xlabel="hoeveelheid", ylabel="prijs"):
    """De vraag- en de aanbodcurve met hun snijpunt.

    verschuiving kan "vraag rechts", "vraag links", "aanbod rechts" of
    "aanbod links" zijn. De verschoven curve komt er in stippellijn bij, met
    het nieuwe snijpunt erbij getekend.
    """
    hoogte = 250
    d, x, y = _as_vlak(breedte, hoogte, xlabel, ylabel)

    def lijn(p1, p2, kleur, stip=False, dik=2.2):
        s = ' stroke-dasharray="6 4"' if stip else ""
        d.append(f'<line x1="{x(p1[0]):.1f}" y1="{y(p1[1]):.1f}" x2="{x(p2[0]):.1f}" '
                 f'y2="{y(p2[1]):.1f}" stroke="{kleur}" stroke-width="{dik}"{s}/>')

    def punt(q, p, label):
        d.append(f'<line x1="{x(0):.1f}" y1="{y(p):.1f}" x2="{x(q):.1f}" y2="{y(p):.1f}" '
                 f'stroke="{DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(f'<line x1="{x(q):.1f}" y1="{y(0):.1f}" x2="{x(q):.1f}" y2="{y(p):.1f}" '
                 f'stroke="{DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(f'<circle cx="{x(q):.1f}" cy="{y(p):.1f}" r="4" fill="{INK}"/>')
        d.append(_tekst(x(q) + 7, y(p) - 7, label, 11, INK, "start", True))

    # vraag: p = 10 - q, aanbod: p = q, snijpunt in (5, 5)
    lijn((1, 9), (9, 1), FOREST)
    lijn((1, 1), (9, 9), AMBER)
    d.append(_tekst(x(9) + 6, y(1), "V", 12, FOREST, "start", True))
    d.append(_tekst(x(9) + 6, y(9), "A", 12, AMBER, "start", True))
    punt(5, 5, "E")

    if verschuiving == "vraag rechts":
        lijn((3, 9), (9, 3), FOREST, True)          # p = 12 - q
        punt(6, 6, "E′")
    elif verschuiving == "vraag links":
        lijn((1, 7), (7, 1), FOREST, True)          # p = 8 - q
        punt(4, 4, "E′")
    elif verschuiving == "aanbod rechts":
        lijn((3, 1), (9, 7), AMBER, True)           # p = q - 2
        punt(6, 4, "E′")
    elif verschuiving == "aanbod links":
        lijn((1, 3), (7, 9), AMBER, True)           # p = q + 2
        punt(4, 6, "E′")
    return _svg(breedte, hoogte, "".join(d))


def kostencurven(breedte=430):
    """De gemiddelde totale kost, de gemiddelde variabele kost en de
    marginale kost, met het snijpunt in het laagste punt van de GTK."""
    hoogte = 250
    d, x, y = _as_vlak(breedte, hoogte, "hoeveelheid", "kost per stuk")
    # TK = 18 + 2q + 0,5q²  →  GTK = 18/q + 2 + 0,5q, GVK = 2 + 0,5q, MK = 2 + q
    # GTK is het laagst bij q = 6, en MK snijdt ze daar: beide 8.
    def reeks(f, van, tot):
        pts = []
        q = van
        while q <= tot + 1e-9:
            pts.append(f"{x(q):.1f},{y(f(q)):.1f}")
            q += 0.25
        return " ".join(pts)

    gtk = lambda q: 18 / q + 2 + 0.5 * q
    gvk = lambda q: 2 + 0.5 * q
    mk = lambda q: 2 + q
    # de y-as loopt tot 10, dus GTK start pas waar ze daaronder zakt (q ≈ 2,6)
    d.append(f'<polyline points="{reeks(gtk, 2.75, 9.5)}" fill="none" stroke="{FOREST}" stroke-width="2.2"/>')
    d.append(f'<polyline points="{reeks(gvk, 1, 9.5)}" fill="none" stroke="{DIM}" stroke-width="1.8" stroke-dasharray="6 4"/>')
    d.append(f'<polyline points="{reeks(mk, 1, 8)}" fill="none" stroke="{AMBER}" stroke-width="2.2"/>')
    d.append(_tekst(x(9.5) + 4, y(gtk(9.5)), "GTK", 10.5, FOREST, "start", True))
    d.append(_tekst(x(9.5) + 4, y(gvk(9.5)), "GVK", 10.5, DIM, "start", True))
    d.append(_tekst(x(8) + 4, y(mk(8)) - 8, "MK", 10.5, AMBER, "start", True))
    d.append(f'<circle cx="{x(6):.1f}" cy="{y(8):.1f}" r="4" fill="{INK}"/>')
    d.append(f'<line x1="{x(6):.1f}" y1="{y(0):.1f}" x2="{x(6):.1f}" y2="{y(8):.1f}" '
             f'stroke="{DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
    return _svg(breedte, hoogte, "".join(d))


def budgetlijn(breedte=430):
    """Een budgetlijn met één indifferentiecurve die ze net raakt."""
    hoogte = 250
    d, x, y = _as_vlak(breedte, hoogte, "goed B", "goed A")
    # budgetlijn: A + B = 8, indifferentiecurve: A·B = 16, raakpunt in (4, 4)
    d.append(f'<line x1="{x(0):.1f}" y1="{y(8):.1f}" x2="{x(8):.1f}" y2="{y(0):.1f}" '
             f'stroke="{FOREST}" stroke-width="2.2"/>')
    pts = []
    b = 2.0
    while b <= 8.0 + 1e-9:
        pts.append(f"{x(b):.1f},{y(16 / b):.1f}")
        b += 0.2
    d.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{AMBER}" stroke-width="2.2"/>')
    d.append(f'<circle cx="{x(4):.1f}" cy="{y(4):.1f}" r="4" fill="{INK}"/>')
    d.append(_tekst(x(4) + 8, y(4) - 8, "raakpunt", 10.5, INK, "start", True))
    d.append(_tekst(x(8) + 6, y(0) + 2, "budgetlijn", 10, FOREST, "start", True))
    d.append(_tekst(x(8) + 6, y(2), "IC", 10.5, AMBER, "start", True))
    return _svg(breedte, hoogte, "".join(d))


def balansschema(actief, passief, breedte=470):
    """Een balans in T-vorm. actief en passief zijn lijsten van regels;
    een regel die met - begint, wordt als onderverdeling gezet."""
    kolom = (breedte - 10) / 2
    regels = max(len(actief), len(passief))
    h = 40 + regels * 19 + 10
    d = [f'<rect x="0" y="0" width="{kolom:.1f}" height="{h}" rx="8" fill="#ffffff" stroke="{DARK}" stroke-width="1.6"/>',
         f'<rect x="{kolom+10:.1f}" y="0" width="{kolom:.1f}" height="{h}" rx="8" fill="#ffffff" stroke="{DARK}" stroke-width="1.6"/>',
         f'<rect x="0" y="0" width="{kolom:.1f}" height="26" rx="8" fill="{FOREST}"/>',
         f'<rect x="{kolom+10:.1f}" y="0" width="{kolom:.1f}" height="26" rx="8" fill="{AMBER}"/>',
         _tekst(kolom / 2, 17, "ACTIEF", 11, "#ffffff", "middle", True),
         _tekst(kolom + 10 + kolom / 2, 17, "PASSIEF", 11, "#ffffff", "middle", True)]
    for i, r in enumerate(actief):
        onder = r.startswith("-")
        d.append(_tekst(14 + (12 if onder else 0), 46 + i * 19, r.lstrip("- "),
                        10.5 if onder else 11, DIM if onder else DARK, "start", not onder))
    for i, r in enumerate(passief):
        onder = r.startswith("-")
        d.append(_tekst(kolom + 24 + (12 if onder else 0), 46 + i * 19, r.lstrip("- "),
                        10.5 if onder else 11, DIM if onder else DARK, "start", not onder))
    return _svg(breedte, h, "".join(d))


def levenscyclus(breedte=470):
    """De productlevenscyclus: de verkoop van de ontwikkeling tot de neergang."""
    hoogte = 230
    links, onder, boven = 44, 46, 18
    b, h = breedte - links - 16, hoogte - onder - boven
    def x(v):
        return links + v / 10 * b
    def y(v):
        return hoogte - onder - v / 10 * h
    d = [f'<line x1="{links}" y1="{boven-4}" x2="{links}" y2="{hoogte-onder}" stroke="{INK}" stroke-width="1.8"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte-12}" y2="{hoogte-onder}" stroke="{INK}" stroke-width="1.8"/>',
         _tekst(links - 2, boven - 6, "verkoop", 10.5, DIM, "start", True),
         _tekst(breedte - 12, hoogte - onder + 16, "tijd", 10.5, DIM, "end", True)]
    punten = [(0, 0), (1.4, 0), (2.4, 1.2), (3.6, 4.2), (5, 7.6), (6.4, 8.6),
              (7.6, 8.4), (8.6, 6.2), (9.6, 3.4)]
    pts = " ".join(f"{x(q):.1f},{y(p):.1f}" for q, p in punten)
    d.append(f'<polyline points="{pts}" fill="none" stroke="{FOREST}" stroke-width="2.4"/>')
    fases = [(0.7, "ontwikkeling"), (2.4, "introductie"), (4.4, "groei"),
             (7.0, "volwassen"), (9.1, "neergang")]
    for q, naam in fases:
        d.append(f'<line x1="{x(q)+ (0 if q==0.7 else 0):.1f}" y1="{y(0):.1f}" '
                 f'x2="{x(q):.1f}" y2="{y(9.4):.1f}" stroke="{BORDER}" stroke-width="1"/>')
        d.append(_tekst(x(q), hoogte - onder + 18, naam, 9.5, DIM, "middle", False))
    return _svg(breedte, hoogte, "".join(d))


def swotvakken(sterk, zwak, kansen, bedreigingen, breedte=470):
    """De vier vakken van een SWOT, met per vak enkele voorbeelden."""
    kolom = (breedte - 10) / 2
    regels = max(len(sterk), len(zwak), len(kansen), len(bedreigingen))
    vh = 34 + regels * 17 + 8
    h = vh * 2 + 10
    d = []
    vakken = [(0, 0, "Sterktes", sterk, FOREST), (kolom + 10, 0, "Zwaktes", zwak, AMBER),
              (0, vh + 10, "Kansen", kansen, FOREST), (kolom + 10, vh + 10, "Bedreigingen", bedreigingen, AMBER)]
    for vx, vy, kop, regels_, kleur in vakken:
        d.append(f'<rect x="{vx:.1f}" y="{vy}" width="{kolom:.1f}" height="{vh}" rx="8" '
                 f'fill="#ffffff" stroke="{kleur}" stroke-width="1.6"/>')
        d.append(_tekst(vx + 12, vy + 19, kop, 11.5, kleur, "start", True))
        for i, r in enumerate(regels_):
            d.append(_tekst(vx + 12, vy + 38 + i * 17, "· " + r, 10.5, DIM, "start", False))
    d.append(_tekst(kolom / 2, h - 2, "binnen het bedrijf", 9.5, DIM, "middle", False))
    d.append(_tekst(kolom + 10 + kolom / 2, h - 2, "buiten het bedrijf", 9.5, DIM, "middle", False))
    return _svg(breedte, h + 6, "".join(d))


def indifferentiemap(breedte=430, aantal=3):
    """Enkele indifferentiecurven van één consument, bol naar de oorsprong."""
    hoogte = 250
    d, x, y = _as_vlak(breedte, hoogte, "goed B", "goed A")
    for i in range(aantal):
        k = 9.0 + i * 12.0            # A·B = k, dus hoe groter k, hoe verder weg
        pts = []
        b = 1.2
        while b <= 9.4 + 1e-9:
            a = k / b
            if 0.6 <= a <= 9.4:
                pts.append(f"{x(b):.1f},{y(a):.1f}")
            b += 0.2
        kleur = [AMBER, FOREST, DARK][i % 3]
        d.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{kleur}" stroke-width="2.1"/>')
        d.append(_tekst(x(9.4) + 5, y(k / 9.4), f"IC{i+1}", 10, kleur, "start", True))
    return _svg(breedte, hoogte, "".join(d))


# ---------------------------------------------------------------------------
# 🚀 Boost — gegevens en verbanden
# ---------------------------------------------------------------------------

def _kwartielen(getallen):
    """De vijf kengetallen van een reeks: min, Q1, mediaan, Q3, max.

    De kwartielen zijn de medianen van de onderste en de bovenste helft, de
    mediaan zelf niet meegerekend. Zo staat het in de vakfiche, en zo rekent
    ook een rekenmachine het.
    """
    g = sorted(getallen)
    n = len(g)

    def mediaan(reeks):
        m = len(reeks)
        return reeks[m // 2] if m % 2 else (reeks[m // 2 - 1] + reeks[m // 2]) / 2

    return g[0], mediaan(g[: n // 2]), mediaan(g), mediaan(g[(n + 1) // 2:]), g[-1]


def _getal(waarde):
    """Een getal zoals wij het schrijven: komma, en geen nullen achteraan."""
    tekst = f"{waarde:.2f}".rstrip("0").rstrip(".")
    return tekst.replace(".", ",")


def boxplot(getallen, breedte=470, stap=2, vanaf=0):
    """Een boxplot van de reeks, met de vijf kengetallen erbij.

    Alles wordt uit de reeks zelf gerekend, zodat de tekening nooit iets
    anders kan zeggen dan de getallen eronder.
    """
    laag, q1, med, q3, hoog = _kwartielen(getallen)
    marge_l, marge_r = 34, 26
    hoogte = 176
    as_y = 136
    bovengrens = stap * int(-(-(hoog + stap) // stap))
    span = max(bovengrens - vanaf, 1)

    def px(waarde):
        return marge_l + (waarde - vanaf) / span * (breedte - marge_l - marge_r)

    d = []
    # de as met haar streepjes en getallen: zonder getallen valt een boxplot
    # niet te lezen
    d.append(f'<line x1="{marge_l}" y1="{as_y}" x2="{breedte-marge_r+6}" y2="{as_y}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    tik = vanaf
    while tik <= bovengrens + 1e-9:
        d.append(f'<line x1="{px(tik):.1f}" y1="{as_y}" x2="{px(tik):.1f}" y2="{as_y+5}" '
                 f'stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(px(tik), as_y + 18, _getal(tik), 9.5, DIM))
        tik += stap
    # de snor van minimum tot maximum, met een streepje aan elk uiteinde
    midden = 84
    d.append(f'<line x1="{px(laag):.1f}" y1="{midden}" x2="{px(hoog):.1f}" y2="{midden}" '
             f'stroke="{DIM}" stroke-width="1.6"/>')
    for waarde in (laag, hoog):
        d.append(f'<line x1="{px(waarde):.1f}" y1="{midden-13}" x2="{px(waarde):.1f}" '
                 f'y2="{midden+13}" stroke="{DIM}" stroke-width="1.8"/>')
    # de doos: de middelste helft van de gegevens
    d.append(f'<rect x="{px(q1):.1f}" y="{midden-23}" width="{px(q3)-px(q1):.1f}" height="46" '
             f'fill="{FOREST}" fill-opacity="0.16" stroke="{FOREST}" stroke-width="1.8" rx="3"/>')
    d.append(f'<line x1="{px(med):.1f}" y1="{midden-23}" x2="{px(med):.1f}" y2="{midden+23}" '
             f'stroke="{AMBER}" stroke-width="2.6"/>')
    # de namen erboven, in twee rijen zodat ze elkaar niet raken
    d.append(_tekst(px(med), 32, f"mediaan {_getal(med)}", 10.5, AMBER, "middle", True))
    d.append(f'<line x1="{px(med):.1f}" y1="38" x2="{px(med):.1f}" y2="{midden-27}" '
             f'stroke="{AMBER}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    d.append(_tekst(px(q1), 56, f"Q1 {_getal(q1)}", 10.5, FOREST, "middle", True))
    d.append(_tekst(px(q3), 56, f"Q3 {_getal(q3)}", 10.5, FOREST, "middle", True))
    d.append(_tekst(px(laag), 118, _getal(laag), 10, DIM, "middle", True))
    d.append(_tekst(px(hoog), 118, _getal(hoog), 10, DIM, "middle", True))
    return _svg(breedte, hoogte, "".join(d))


def puntenwolk(punten, breedte=400, hoogte=250, xlabel="", ylabel="",
               xstap=5, ystap=2, trend=True):
    """Een spreidingsdiagram: één punt per meetpaar, met de trendlijn erbij.

    De trendlijn wordt gerekend uit de punten (de kleinste-kwadratenrechte) en
    loopt enkel over de gemeten x-waarden: buiten dat bereik weet je niet of
    ze nog klopt, en dan hoort ze er ook niet te staan.
    """
    xs = [p[0] for p in punten]
    ys = [p[1] for p in punten]
    xmin = xstap * int(min(xs) // xstap)
    xmax = xstap * int(-(-max(xs) // xstap))
    ymin = ystap * int(min(ys) // ystap) - ystap
    ymax = ystap * int(-(-max(ys) // ystap)) + ystap
    links, onder, boven, rechts = 44, 40, 20, 14
    vlak_b = breedte - links - rechts
    vlak_h = hoogte - onder - boven

    def px(v):
        return links + (v - xmin) / max(xmax - xmin, 1) * vlak_b

    def py(v):
        return hoogte - onder - (v - ymin) / max(ymax - ymin, 1) * vlak_h

    d = [f'<line x1="{links}" y1="{boven-6}" x2="{links}" y2="{hoogte-onder}" '
         f'stroke="{INK}" stroke-width="1.8"/>',
         f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte-rechts+6}" y2="{hoogte-onder}" '
         f'stroke="{INK}" stroke-width="1.8"/>']
    tik = ymin
    while tik <= ymax + 1e-9:
        d.append(f'<line x1="{links-5}" y1="{py(tik):.1f}" x2="{links}" y2="{py(tik):.1f}" '
                 f'stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(links - 8, py(tik) + 3.5, _getal(tik), 9.5, DIM, "end"))
        tik += ystap
    tik = xmin
    while tik <= xmax + 1e-9:
        d.append(f'<line x1="{px(tik):.1f}" y1="{hoogte-onder}" x2="{px(tik):.1f}" '
                 f'y2="{hoogte-onder+5}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(px(tik), hoogte - onder + 17, _getal(tik), 9.5, DIM))
        tik += xstap
    if trend and len(punten) > 1:
        n = len(punten)
        gx, gy = sum(xs) / n, sum(ys) / n
        noemer = sum((x - gx) ** 2 for x in xs)
        if noemer:
            a = sum((x - gx) * (y - gy) for x, y in zip(xs, ys)) / noemer
            b = gy - a * gx
            uiteinden = []
            for xq in (min(xs), max(xs)):
                yq = a * xq + b
                if yq < ymin and a:
                    xq = (ymin - b) / a
                elif yq > ymax and a:
                    xq = (ymax - b) / a
                uiteinden.append(xq)
            x1, x2 = uiteinden
            d.append(f'<line x1="{px(x1):.1f}" y1="{py(a*x1+b):.1f}" x2="{px(x2):.1f}" '
                     f'y2="{py(a*x2+b):.1f}" stroke="{AMBER}" stroke-width="2.2"/>')
            d.append(_tekst(px(x2) - 4, py(a * x2 + b) - 9, "trendlijn", 10, AMBER, "end", True))
    for x, y in punten:
        d.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="4.2" fill="{FOREST}"/>')
    d.append(_tekst(links - 2, boven - 8, ylabel, 10.5, DIM, "start", True))
    d.append(_tekst(breedte - rechts + 6, hoogte - onder + 31, xlabel, 10.5, DIM, "end", True))
    return _svg(breedte, hoogte, "".join(d))


def productiecurven(marginaal, breedte=470, xlabel="aantal werkers"):
    """De totale en de marginale productie onder elkaar, uit dezelfde reeks.

    `marginaal` is wat elke extra werker erbij brengt. De totale productie is
    de som daarvan, dus de twee tekeningen kunnen elkaar niet tegenspreken:
    waar het marginale door nul gaat, ligt het hoogste punt van het totaal.
    """
    totaal = []
    som = 0
    for m in marginaal:
        som += m
        totaal.append(som)
    n = len(marginaal)
    links, rechts = 42, 22
    breed = breedte - links - rechts

    def px(i):
        return links + (i - 1) / max(n - 1, 1) * breed

    d = []

    def paneel(boven, onder, waarden, kleur, naam, nullijn=False):
        hoog = max(max(waarden), 1)
        laag = min(min(waarden), 0)
        span = hoog - laag
        def py(v):
            return onder - (v - laag) / span * (onder - boven)
        # de as met een getal bij de uiterste waarden
        d.append(f'<line x1="{links}" y1="{boven-6}" x2="{links}" y2="{onder+2}" '
                 f'stroke="{INK}" stroke-width="1.6"/>')
        d.append(f'<line x1="{links}" y1="{py(laag):.1f}" x2="{breedte-rechts+4}" '
                 f'y2="{py(laag):.1f}" stroke="{INK}" stroke-width="1.6"/>')
        if nullijn and laag < 0:
            d.append(f'<line x1="{links}" y1="{py(0):.1f}" x2="{breedte-rechts+4}" '
                     f'y2="{py(0):.1f}" stroke="{DIM}" stroke-width="1.2" stroke-dasharray="5 4"/>')
            d.append(_tekst(links - 6, py(0) + 4, "0", 9.5, DIM, "end"))
        d.append(_tekst(links - 6, py(hoog) + 4, _getal(hoog), 9.5, DIM, "end"))
        d.append(_tekst(links - 2, boven - 10, naam, 10.5, kleur, "start", True))
        punten = " ".join(f"{px(i+1):.1f},{py(v):.1f}" for i, v in enumerate(waarden))
        d.append(f'<polyline points="{punten}" fill="none" stroke="{kleur}" stroke-width="2.2"/>')
        for i, v in enumerate(waarden):
            d.append(f'<circle cx="{px(i+1):.1f}" cy="{py(v):.1f}" r="3" fill="{kleur}"/>')
        return py

    paneel(30, 150, totaal, FOREST, "totale productie")
    py2 = paneel(196, 300, marginaal, AMBER, "marginale productie", nullijn=True)
    # het keerpunt: de laatste werker die meer bijbrengt dan de vorige
    top = max(range(n), key=lambda i: marginaal[i])
    d.append(f'<line x1="{px(top+1):.1f}" y1="190" x2="{px(top+1):.1f}" y2="306" '
             f'stroke="{DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
    d.append(_tekst(px(top + 1), 186, "keerpunt", 9.5, DIM, "middle", True))
    # de nummers van de werkers onder de onderste tekening
    for i in range(1, n + 1):
        d.append(_tekst(px(i), 322, str(i), 9.5, DIM))
    d.append(_tekst(breedte - rechts + 4, 338, xlabel, 10.5, DIM, "end", True))
    return _svg(breedte, 344, "".join(d))


def organogram(afdelingen, breedte=470, staf=None):
    """Een organogram met drie niveaus: de leiding boven, de afdelingen onder.

    De verticale lijnen zijn gezagslijnen. Geef `staf` mee en die komt er met
    een stippellijn naast te hangen: hij adviseert, hij beslist niet.
    """
    hoogte = 206
    d = []
    midden = breedte / 2

    def vak(x, y, b, h, tekst, kleur=FOREST, stip=False):
        s = ' stroke-dasharray="5 4"' if stip else ""
        d.append(f'<rect x="{x:.1f}" y="{y}" width="{b:.1f}" height="{h}" fill="{PAPER}" '
                 f'stroke="{kleur}" stroke-width="1.8" rx="5"{s}/>')
        for i, regel in enumerate(tekst.split("|")):
            d.append(_tekst(x + b / 2, y + h / 2 + 4 + (i - (len(tekst.split("|")) - 1) / 2) * 12,
                            regel.strip(), 10, INK if not stip else DIM, "middle", i == 0))

    # de leiding
    top_b, top_h = 150, 34
    vak(midden - top_b / 2, 14, top_b, top_h, "directie")
    # de staf ernaast, met een stippellijn
    if staf:
        staf_b = 108
        staf_x = midden + top_b / 2 + 40
        vak(staf_x, 20, staf_b, 24, staf, DIM, True)
        d.append(f'<line x1="{midden + top_b/2:.1f}" y1="32" x2="{staf_x:.1f}" y2="32" '
                 f'stroke="{DIM}" stroke-width="1.4" stroke-dasharray="5 4"/>')
        d.append(_tekst(midden + top_b / 2 + 20, 26, "advies", 9, DIM, "middle"))
    # de balk waar de gezagslijnen aan hangen
    marge = 14
    n = len(afdelingen)
    vak_b = (breedte - 2 * marge - (n - 1) * 10) / n
    balk_y = 86
    d.append(f'<line x1="{midden:.1f}" y1="{14 + top_h}" x2="{midden:.1f}" y2="{balk_y}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    eerste = marge + vak_b / 2
    laatste = marge + (n - 1) * (vak_b + 10) + vak_b / 2
    d.append(f'<line x1="{eerste:.1f}" y1="{balk_y}" x2="{laatste:.1f}" y2="{balk_y}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    for i, naam in enumerate(afdelingen):
        x = marge + i * (vak_b + 10)
        d.append(f'<line x1="{x + vak_b/2:.1f}" y1="{balk_y}" x2="{x + vak_b/2:.1f}" y2="112" '
                 f'stroke="{INK}" stroke-width="1.6"/>')
        vak(x, 112, vak_b, 48, naam)
    d.append(_tekst(marge, 184, "de volle lijn is een gezagslijn, de stippellijn een adviesrelatie",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


# ---------------------------------------------------------------------------
# 🚀 Boost dubbele finaliteit — gezondheid, zorg en welzijn
# ---------------------------------------------------------------------------

def oogdoorsnede(breedte=470):
    """Een doorsnede van het oog, van het hoornvlies vooraan tot de oogzenuw
    achteraan. Het licht komt van links binnen."""
    hoogte = 250
    cx, cy, r = 232, 118, 88
    d = []
    # de oogbol
    d.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAPER}" stroke="{INK}" stroke-width="1.8"/>')
    # het netvlies: de binnenste laag achteraan
    d.append(f'<path d="M{cx} {cy-r+6} A {r-6} {r-6} 0 0 0 {cx} {cy+r-6}" fill="none" '
             f'stroke="{FOREST}" stroke-width="4"/>')
    # het hoornvlies vooraan, als een bolling naar links
    d.append(f'<path d="M{cx-r+14} {cy-34} A 40 40 0 0 0 {cx-r+14} {cy+34}" fill="none" '
             f'stroke="{AMBER}" stroke-width="3.4"/>')
    # de iris met de pupil ertussen
    for teken in (-1, 1):
        d.append(f'<line x1="{cx-r+16}" y1="{cy+teken*34}" x2="{cx-r+22}" y2="{cy+teken*13}" '
                 f'stroke="{INK}" stroke-width="4"/>')
    # de lens
    d.append(f'<ellipse cx="{cx-r+34}" cy="{cy}" rx="11" ry="26" fill="{FOREST}" '
             f'fill-opacity="0.18" stroke="{FOREST}" stroke-width="1.8"/>')
    # het licht dat binnenvalt
    for y in (cy - 16, cy, cy + 16):
        d.append(f'<line x1="14" y1="{y}" x2="{cx-r+10}" y2="{cy}" stroke="{AMBER}" '
                 f'stroke-width="1.2" stroke-dasharray="5 4"/>')
    d.append(_tekst(16, cy - 26, "licht", 10, AMBER, "start", True))
    # de oogzenuw achteraan
    d.append(f'<path d="M{cx+r-4} {cy} q 30 0 46 18" fill="none" stroke="{DIM}" stroke-width="7"/>')
    # de labels, elk met een streepje naar zijn plaats
    def wijs(tx, ty, px, py, naam, anker="start"):
        d.append(f'<line x1="{tx if anker=="start" else tx}" y1="{ty+3}" x2="{px}" y2="{py}" '
                 f'stroke="{DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(_tekst(tx, ty, naam, 10, INK, anker, True))
    wijs(cx - r - 46, cy - 60, cx - r + 16, cy - 30, "hoornvlies")
    wijs(cx - r - 30, cy + 74, cx - r + 18, cy + 24, "iris")
    wijs(cx - 46, cy + 92, cx - r + 34, cy + 26, "lens")
    wijs(cx + 18, cy - 100, cx + r - 12, cy - 44, "netvlies")
    wijs(cx + r + 6, cy + 62, cx + r + 30, cy + 14, "oogzenuw")
    wijs(cx - r - 54, cy + 10, cx - r + 18, cy + 2, "pupil")
    d.append(_tekst(16, hoogte - 10,
                    "het beeld valt omgekeerd op het netvlies; de hersenen zetten het recht",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def oordoorsnede(breedte=470):
    """Het oor in zijn drie delen, met de weg van het geluid erdoor."""
    hoogte = 218
    d = []
    for x, b, naam in ((10, 150, "buitenoor"), (160, 120, "middenoor"),
                       (280, 180, "binnenoor")):
        d.append(f'<rect x="{x}" y="28" width="{b}" height="130" fill="{PAPER}" '
                 f'stroke="{BORDER}" stroke-width="1.4" rx="6"/>')
        d.append(_tekst(x + b / 2, 20, naam, 10.5, FOREST, "middle", True))
    # de oorschelp en de gehoorgang
    d.append('<path d="M30 76 q 34 -34 54 0 q 10 22 -14 32 q -18 6 -22 -6" fill="none" '
             f'stroke="{INK}" stroke-width="2"/>')
    d.append(f'<line x1="84" y1="98" x2="160" y2="98" stroke="{INK}" stroke-width="2"/>')
    d.append(f'<line x1="84" y1="78" x2="160" y2="78" stroke="{INK}" stroke-width="2"/>')
    d.append(_tekst(28, 140, "oorschelp en gehoorgang", 9, DIM, "start"))
    # het trommelvel tussen buiten- en middenoor
    d.append(f'<line x1="161" y1="68" x2="161" y2="108" stroke="{AMBER}" stroke-width="3.4"/>')
    d.append(_tekst(161, 60, "trommelvel", 9, AMBER, "middle", True))
    # de drie gehoorbeentjes, met hun namen onder elkaar
    for i, naam in enumerate(("hamer", "aambeeld", "stijgbeugel")):
        x = 180 + i * 30
        d.append(f'<rect x="{x}" y="76" width="21" height="16" rx="4" fill="{FOREST}" '
                 f'fill-opacity="0.22" stroke="{FOREST}" stroke-width="1.4"/>')
        d.append(_tekst(168, 116 + i * 13, f"\u2022 {naam}", 9, DIM, "start"))
    # het slakkenhuis en de gehoorzenuw
    d.append(f'<path d="M332 92 a 28 28 0 1 1 -2 -13 a 19 19 0 1 0 -6 9 a 10 10 0 1 0 8 -4" '
             f'fill="none" stroke="{FOREST}" stroke-width="3"/>')
    d.append(_tekst(322, 140, "slakkenhuis en evenwichtsorgaan", 9, FOREST, "middle", True))
    d.append(f'<path d="M360 100 q 28 10 40 24" fill="none" stroke="{DIM}" stroke-width="5"/>')
    d.append(_tekst(412, 142, "gehoorzenuw", 9, DIM, "middle"))
    # de buis van Eustachius naar de keel
    d.append(f'<path d="M198 100 q 8 46 -46 62" fill="none" stroke="{DIM}" stroke-width="2" '
             f'stroke-dasharray="5 4"/>')
    d.append(_tekst(150, 180, "buis van Eustachius, naar de keel", 9, DIM, "middle"))
    d.append(_tekst(10, hoogte - 8,
                    "het geluid gaat van links naar rechts: trilling, versterking, impuls",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def huidlagen(breedte=470):
    """De drie lagen van de huid, met wat er in elke laag thuishoort."""
    hoogte = 214
    lagen = [("opperhuid", 20, 40, "de buitenste laag, zonder bloedvaten"),
             ("lederhuid", 60, 76, "receptoren, bloedvaten en klieren"),
             ("onderhuids vetweefsel", 136, 54, "isoleert en vangt stoten op")]
    d = []
    for naam, y, h, uitleg in lagen:
        d.append(f'<rect x="12" y="{y}" width="260" height="{h}" fill="{FOREST}" '
                 f'fill-opacity="{0.08 if naam == "opperhuid" else 0.16}" stroke="{FOREST}" '
                 f'stroke-width="1.6"/>')
        d.append(_tekst(280, y + 16, naam, 10.5, INK, "start", True))
        for i, regel in enumerate(_regels(uitleg, 36)):
            d.append(_tekst(280, y + 30 + i * 12, regel, 9, DIM, "start"))
    # een zweetklier met haar kanaal naar buiten
    d.append(f'<circle cx="80" cy="118" r="10" fill="{PAPER}" stroke="{AMBER}" stroke-width="1.8"/>')
    d.append(f'<path d="M80 108 q 4 -36 -6 -48" fill="none" stroke="{AMBER}" stroke-width="1.8"/>')
    d.append(_tekst(96, 122, "zweetklier", 8.5, AMBER, "start"))
    # een bloedvat
    d.append(f'<path d="M150 70 q 20 30 0 60" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    d.append(_tekst(160, 100, "bloedvat", 8.5, DIM, "start"))
    # een receptor met zijn zenuw
    d.append(f'<circle cx="222" cy="96" r="7" fill="{FOREST}"/>')
    d.append(f'<line x1="222" y1="103" x2="222" y2="130" stroke="{FOREST}" stroke-width="1.8"/>')
    d.append(_tekst(236, 100, "receptor", 8.5, FOREST, "start"))
    d.append(_tekst(12, hoogte - 8, "van buiten naar binnen: opperhuid, lederhuid, vetweefsel",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def neuron(breedte=470):
    """Een zenuwcel: dendrieten, cellichaam, axon met myelineschede en de
    eindknoppen die aan de synaps komen."""
    hoogte = 176
    y = 84
    d = []
    # de dendrieten links
    for hoek in (-34, -12, 12, 34):
        import math
        dx, dy = 44 * math.cos(math.radians(180 + hoek)), 44 * math.sin(math.radians(180 + hoek))
        d.append(f'<line x1="86" y1="{y}" x2="{86+dx:.1f}" y2="{y+dy:.1f}" stroke="{FOREST}" '
                 f'stroke-width="2.4" stroke-linecap="round"/>')
    # het cellichaam met zijn kern
    d.append(f'<circle cx="94" cy="{y}" r="24" fill="{FOREST}" fill-opacity="0.18" '
             f'stroke="{FOREST}" stroke-width="2"/>')
    d.append(f'<circle cx="94" cy="{y}" r="8" fill="{FOREST}"/>')
    # het axon met de myelineschede in stukken, met knopen ertussen
    d.append(f'<line x1="118" y1="{y}" x2="382" y2="{y}" stroke="{INK}" stroke-width="3"/>')
    for i in range(5):
        x = 130 + i * 50
        d.append(f'<rect x="{x}" y="{y-11}" width="38" height="22" rx="11" fill="{AMBER}" '
                 f'fill-opacity="0.26" stroke="{AMBER}" stroke-width="1.6"/>')
    # de eindknoppen rechts
    for dy in (-20, 0, 20):
        d.append(f'<line x1="382" y1="{y}" x2="410" y2="{y+dy}" stroke="{INK}" stroke-width="2.2"/>')
        d.append(f'<circle cx="414" cy="{y+dy}" r="6" fill="{INK}"/>')
    # de labels
    for tx, ty, px, py, naam, anker in (
            (36, 28, 60, y - 26, "dendrieten", "start"),
            (94, 150, 94, y + 26, "cellichaam", "middle"),
            (232, 150, 232, y + 13, "axon", "middle"),
            (300, 28, 300, y - 13, "myelineschede", "middle"),
            (174, 36, 174, y - 6, "knoop van Ranvier", "middle"),
            (420, 150, 414, y + 26, "eindknoppen", "end")):
        d.append(f'<line x1="{tx if anker != "end" else tx - 50}" y1="{ty + (4 if ty < y else -10)}" '
                 f'x2="{px}" y2="{py}" stroke="{DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(_tekst(tx, ty, naam, 10, INK, anker, True))
    d.append(_tekst(10, hoogte - 6,
                    "de impuls loopt van links naar rechts en springt van knoop naar knoop",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def icfschema(breedte=470):
    """Het ICF-schema: de gezondheidstoestand in drie delen, met het ik en de
    omgeving eronder. De pijlen lopen in twee richtingen, want de drie
    beïnvloeden elkaar."""
    hoogte = 232
    d = []
    marge = 14
    d.append(_tekst(breedte / 2, 18, "gezondheidstoestand", 11, FOREST, "middle", True))
    delen = [("lichaam", "hoe werkt het lichaam?"),
             ("doen", "wat doet iemand zelf?"),
             ("samen", "doet iemand mee?")]
    b = (breedte - 2 * marge - 2 * 10) / 3
    for i, (naam, vraag) in enumerate(delen):
        x = marge + i * (b + 10)
        d.append(f'<rect x="{x:.1f}" y="28" width="{b:.1f}" height="54" fill="{FOREST}" '
                 f'fill-opacity="0.12" stroke="{FOREST}" stroke-width="1.8" rx="6"/>')
        d.append(_tekst(x + b / 2, 50, naam, 11, INK, "middle", True))
        for j, regel in enumerate(_regels(vraag, int((b - 12) / 4.8))):
            d.append(_tekst(x + b / 2, 66 + j * 11, regel, 9, DIM))
    # het ik en de omgeving eronder
    onder = [("het ik", "persoonlijke factoren: leeftijd, geslacht, karakter, achtergrond"),
             ("de omgeving", "externe factoren: de woning, het gezin, de school, de buurt")]
    b2 = (breedte - 2 * marge - 14) / 2
    for i, (naam, uitleg) in enumerate(onder):
        x = marge + i * (b2 + 14)
        d.append(f'<rect x="{x:.1f}" y="140" width="{b2:.1f}" height="62" fill="{PAPER}" '
                 f'stroke="{AMBER}" stroke-width="1.8" rx="6"/>')
        d.append(_tekst(x + b2 / 2, 160, naam, 11, INK, "middle", True))
        for j, regel in enumerate(_regels(uitleg, int((b2 - 14) / 4.8))):
            d.append(_tekst(x + b2 / 2, 176 + j * 11, regel, 9, DIM))
        # een pijl in twee richtingen naar de gezondheidstoestand
        px = x + b2 / 2
        d.append(f'<line x1="{px:.1f}" y1="92" x2="{px:.1f}" y2="130" stroke="{DIM}" stroke-width="1.6"/>')
        d.append(f'<path d="M{px:.1f} 86 l-5 9 h10 z" fill="{DIM}"/>')
        d.append(f'<path d="M{px:.1f} 136 l-5 -9 h10 z" fill="{DIM}"/>')
    d.append(_tekst(breedte / 2, 118, "ze beïnvloeden elkaar in twee richtingen", 9.5, DIM))
    d.append(_tekst(marge, hoogte - 6,
                    "de omgeving kan helpen of hinderen: een lift helpt, een trap hindert",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def voedingsdriehoek(breedte=470):
    """De voedingsdriehoek: op zijn kop, met het breedste deel bovenaan, en de
    restgroep eronder, buiten de driehoek."""
    hoogte = 248
    top_y, punt_y = 24, 184
    links, rechts = 16, 200
    d = []
    banden = [("water, groenten, fruit, granen, noten en peulvruchten", FOREST, 0.0, 0.40),
              ("vis, eieren, melkproducten en kaas", "#6f8f4a", 0.40, 0.72),
              ("rood vlees, bewerkt vlees en boter", AMBER, 0.72, 1.0)]
    h = punt_y - top_y
    mx = (links + rechts) / 2
    for naam, kleur, van, tot in banden:
        y1, y2 = top_y + van * h, top_y + tot * h
        b1 = (rechts - links) * (1 - van) / 2
        b2 = (rechts - links) * (1 - tot) / 2
        d.append(f'<polygon points="{mx-b1:.1f},{y1:.1f} {mx+b1:.1f},{y1:.1f} '
                 f'{mx+b2:.1f},{y2:.1f} {mx-b2:.1f},{y2:.1f}" fill="{kleur}" fill-opacity="0.22" '
                 f'stroke="{kleur}" stroke-width="1.6"/>')
        # het etiket staat naast de driehoek, want onderin is er geen plaats
        ym = (y1 + y2) / 2
        d.append(f'<rect x="216" y="{ym-9:.1f}" width="11" height="11" fill="{kleur}" '
                 f'fill-opacity="0.5" stroke="{kleur}" stroke-width="1.2"/>')
        for i, regel in enumerate(_regels(naam, 42)):
            d.append(_tekst(234, ym + i * 12, regel, 9.5, INK, "start"))
    # de pijl langs de driehoek: hoe lager, hoe minder
    d.append(f'<line x1="{links-8}" y1="{top_y+4}" x2="{links-8}" y2="{punt_y}" stroke="{DIM}" '
             f'stroke-width="1.4"/>')
    d.append(f'<path d="M{links-8} {punt_y+6} l-5 -9 h10 z" fill="{DIM}"/>')
    d.append(_tekst(links - 14, top_y - 6, "hoe lager, hoe minder", 9.5, DIM, "start", True))
    # de restgroep, buiten de driehoek
    d.append(f'<rect x="16" y="196" width="{breedte-32}" height="34" fill="{DIM}" '
             f'fill-opacity="0.10" stroke="{DIM}" stroke-width="1.4" stroke-dasharray="6 4" rx="6"/>')
    d.append(_tekst(28, 218, "restgroep", 10.5, INK, "start", True))
    d.append(_tekst(100, 218, "snoep, frisdrank, alcohol, chips \u2014 staat buiten de driehoek: "
                              "hoe minder, hoe beter", 9.5, DIM, "start"))
    d.append(_tekst(16, hoogte - 6,
                    "meer plantaardig dan dierlijk, en zo weinig mogelijk lege calorie\u00ebn",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def ladder(sporten, breedte=470, bovenaan="het best", onderaan="het slechtst"):
    """Een rangorde als ladder: de beste keuze bovenaan, de slechtste onder.

    `sporten` is de lijst van boven naar onder, elk (naam, uitleg).
    """
    rij_h = 36
    hoogte = len(sporten) * rij_h + 44
    d = []
    for i, (naam, uitleg) in enumerate(sporten):
        y = 26 + i * rij_h
        d.append(f'<rect x="58" y="{y}" width="{breedte-74}" height="{rij_h-6}" fill="{FOREST}" '
                 f'fill-opacity="{0.22 - i * 0.03:.2f}" stroke="{FOREST}" stroke-width="1.4" rx="5"/>')
        d.append(_tekst(70, y + 20, naam, 10.5, INK, "start", True))
        d.append(_tekst(70 + 9 * len(naam), y + 20, uitleg, 9, DIM, "start"))
    # de pijl met het oordeel ernaast
    d.append(f'<line x1="32" y1="30" x2="32" y2="{26 + len(sporten) * rij_h - 6}" stroke="{DIM}" '
             f'stroke-width="1.6"/>')
    d.append(f'<path d="M32 24 l-5 9 h10 z" fill="{DIM}"/>')
    d.append(_tekst(44, 18, bovenaan, 9.5, DIM, "start", True))
    d.append(_tekst(44, 26 + len(sporten) * rij_h + 8, onderaan, 9.5, DIM, "start", True))
    return _svg(breedte, hoogte, "".join(d))


def koelkastzones(breedte=470):
    """De zones van een koelkast: onderaan het koudst, in de deur het minst
    koud. De pijl links loopt mee met de koude lucht die zakt."""
    hoogte = 250
    d = []
    kast_x, kast_b = 52, 236
    zones = [("bovenaan", "bereide gerechten, restjes in een doos", 26, 48),
             ("midden", "melkproducten, patisserie, open bokalen", 74, 48),
             ("onderaan, boven de lade", "het koudst: rauw vlees, gehakt, vis, schaaldieren", 122, 48),
             ("de groentelade", "groenten en fruit, iets minder koud", 170, 44)]
    for naam, wat, y, h in zones:
        kleur = FOREST if "koudst" in wat else DIM
        d.append(f'<rect x="{kast_x}" y="{y}" width="{kast_b}" height="{h}" fill="{kleur}" '
                 f'fill-opacity="0.12" stroke="{kleur}" stroke-width="1.4"/>')
        d.append(_tekst(kast_x + 10, y + 18, naam, 9.5, INK, "start", True))
        for i, regel in enumerate(_regels(wat, 46)):
            d.append(_tekst(kast_x + 10, y + 32 + i * 11, regel, 9, DIM, "start"))
    # de deur, als een smalle strook ernaast
    d.append(f'<rect x="{kast_x+kast_b+10}" y="26" width="118" height="188" fill="{AMBER}" '
             f'fill-opacity="0.12" stroke="{AMBER}" stroke-width="1.4"/>')
    d.append(_tekst(kast_x + kast_b + 20, 44, "de deur", 9.5, INK, "start", True))
    for i, regel in enumerate(_regels("de minst koude plaats: dranken, sauzen, boter, eieren", 20)):
        d.append(_tekst(kast_x + kast_b + 20, 60 + i * 11, regel, 9, DIM, "start"))
    # de pijl: koude lucht zakt
    d.append(f'<line x1="36" y1="30" x2="36" y2="206" stroke="{FOREST}" stroke-width="1.6"/>')
    d.append(f'<path d="M36 212 l-5 -9 h10 z" fill="{FOREST}"/>')
    d.append(_tekst(30, 226, "koude lucht zakt", 9.5, FOREST, "start", True))
    d.append(_tekst(30, hoogte - 6, "hoe lager, hoe kouder; in de deur is het het minst koud",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def gedektetafel(breedte=470):
    """Een gedekt couvert voor een warme maaltijd, van boven gezien."""
    hoogte = 218
    cx, cy = 210, 118
    d = []
    # het bord
    d.append(f'<circle cx="{cx}" cy="{cy}" r="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.8"/>')
    d.append(f'<circle cx="{cx}" cy="{cy}" r="42" fill="none" stroke="{BORDER}" stroke-width="1.4"/>')
    # de vork links
    d.append(f'<line x1="{cx-74}" y1="{cy-26}" x2="{cx-74}" y2="{cy+30}" stroke="{FOREST}" '
             f'stroke-width="5" stroke-linecap="round"/>')
    for k in (-5, 0, 5):
        d.append(f'<line x1="{cx-74+k}" y1="{cy-26}" x2="{cx-74+k}" y2="{cy-10}" stroke="{FOREST}" '
                 f'stroke-width="1.6"/>')
    d.append(_tekst(cx - 74, cy + 50, "vork", 10, INK, "middle", True))
    d.append(_tekst(cx - 74, cy + 64, "links", 9, DIM))
    # het mes rechts, met de snijkant naar het bord
    d.append(f'<line x1="{cx+74}" y1="{cy-26}" x2="{cx+74}" y2="{cy+30}" stroke="{AMBER}" '
             f'stroke-width="5" stroke-linecap="round"/>')
    d.append(f'<path d="M{cx+71} {cy-26} l0 24" stroke="{INK}" stroke-width="1.6" fill="none"/>')
    d.append(_tekst(cx + 74, cy + 50, "mes", 10, INK, "middle", True))
    d.append(_tekst(cx + 74, cy + 64, "rechts, snijkant naar het bord", 9, DIM))
    # het glas rechtsboven
    d.append(f'<path d="M{cx+62} {cy-74} h26 l-4 24 h-18 z" fill="{PAPER}" stroke="{INK}" '
             f'stroke-width="1.6"/>')
    d.append(f'<line x1="{cx+75}" y1="{cy-50}" x2="{cx+75}" y2="{cy-42}" stroke="{INK}" stroke-width="1.6"/>')
    d.append(_tekst(cx + 88, cy - 82, "glas, rechtsboven", 9.5, INK, "end", True))
    # het dessertbestek boven het bord
    d.append(f'<line x1="{cx-26}" y1="{cy-70}" x2="{cx+26}" y2="{cy-70}" stroke="{DIM}" '
             f'stroke-width="4" stroke-linecap="round"/>')
    d.append(_tekst(cx - 36, cy - 80, "dessertbestek, boven het bord", 9.5, DIM, "end"))
    # het servet links van de vork
    d.append(f'<rect x="{cx-128}" y="{cy-22}" width="34" height="46" fill="{FOREST}" '
             f'fill-opacity="0.14" stroke="{FOREST}" stroke-width="1.4" rx="3"/>')
    d.append(_tekst(cx - 111, cy + 40, "servet", 9.5, INK, "middle", True))
    d.append(_tekst(16, hoogte - 6, "mes rechts, vork links, glas rechtsboven, dessertbestek boven",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def sinnercirkel(breedte=470, delen=None):
    """De Sinner-cirkel: vier factoren die samen het schoonmaakresultaat
    bepalen. Geef `delen` mee als vier (naam, aandeel) om te tonen dat een
    kleiner deel van de ene door een groter deel van de andere opgevuld wordt.
    """
    import math
    delen = delen or [("tijd", 25), ("chemie", 25), ("temperatuur", 25),
                      ("mechanische handeling", 25)]
    hoogte = 250
    cx, cy, r = 150, 120, 92
    kleuren = [FOREST, AMBER, "#6f8f4a", DIM]
    d = []
    totaal = sum(a for _, a in delen) or 1
    hoek = -90.0
    for i, (naam, aandeel) in enumerate(delen):
        span = aandeel / totaal * 360
        x1 = cx + r * math.cos(math.radians(hoek))
        y1 = cy + r * math.sin(math.radians(hoek))
        x2 = cx + r * math.cos(math.radians(hoek + span))
        y2 = cy + r * math.sin(math.radians(hoek + span))
        groot = 1 if span > 180 else 0
        d.append(f'<path d="M{cx} {cy} L{x1:.1f} {y1:.1f} A {r} {r} 0 {groot} 1 {x2:.1f} {y2:.1f} Z" '
                 f'fill="{kleuren[i]}" fill-opacity="0.22" stroke="{kleuren[i]}" stroke-width="1.8"/>')
        # het etiket in de legende ernaast, want in een sector past weinig
        ly = 52 + i * 34
        d.append(f'<rect x="276" y="{ly-10}" width="12" height="12" fill="{kleuren[i]}" '
                 f'fill-opacity="0.5" stroke="{kleuren[i]}" stroke-width="1.2"/>')
        d.append(_tekst(296, ly, naam, 10.5, INK, "start", True))
        d.append(_tekst(296, ly + 13, f"{aandeel} %", 9.5, DIM, "start"))
        hoek += span
    d.append(_tekst(16, hoogte - 6,
                    "de vier samen zijn altijd het geheel: minder van de ene vraagt meer van een andere",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


def wassymbolen(breedte=470):
    """De vijf groepen van het onderhoudsetiket, met een doorstreept symbool
    erbij om te tonen wat een kruis betekent."""
    hoogte = 206
    d = []
    x0, stap = 34, 86

    def kruis(cx, cy):
        for teken in (1, -1):
            d.append(f'<line x1="{cx-22}" y1="{cy-22*teken}" x2="{cx+22}" y2="{cy+22*teken}" '
                     f'stroke="#b03a2e" stroke-width="2.6"/>')

    def onder(cx, naam, uitleg):
        d.append(_tekst(cx, 112, naam, 10, INK, "middle", True))
        for i, regel in enumerate(_regels(uitleg, 16)):
            d.append(_tekst(cx, 126 + i * 11, regel, 8.5, DIM))

    # 1 wassen: een kuipje met een getal erin
    cx = x0
    d.append(f'<path d="M{cx-22} 48 l6 -14 h32 l6 14 a 22 16 0 1 1 -44 0 z" fill="{PAPER}" '
             f'stroke="{INK}" stroke-width="2"/>')
    d.append(_tekst(cx, 58, "40", 12, INK, "middle", True))
    onder(cx, "wassen", "het getal is de hoogste temperatuur")
    # 2 bleken: een driehoek
    cx = x0 + stap
    d.append(f'<polygon points="{cx},30 {cx-24},70 {cx+24},70" fill="{PAPER}" stroke="{INK}" '
             f'stroke-width="2"/>')
    onder(cx, "bleken", "met of zonder chloor")
    # 3 drogen: een vierkant met een cirkel erin
    cx = x0 + 2 * stap
    d.append(f'<rect x="{cx-24}" y="26" width="48" height="48" fill="{PAPER}" stroke="{INK}" '
             f'stroke-width="2"/>')
    d.append(f'<circle cx="{cx}" cy="50" r="14" fill="none" stroke="{INK}" stroke-width="2"/>')
    onder(cx, "drogen", "in de droogtrommel of niet")
    # 4 strijken: een strijkijzer met puntjes
    cx = x0 + 3 * stap
    d.append(f'<path d="M{cx-24} 66 h48 l-8 -24 q -4 -10 -14 -10 h-10 q -10 0 -16 10 z" '
             f'fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    for k in (-8, 0, 8):
        d.append(f'<circle cx="{cx+k}" cy="56" r="2.4" fill="{INK}"/>')
    onder(cx, "strijken", "de puntjes geven de hitte")
    # 5 professionele reiniging: een cirkel, hier doorstreept
    cx = x0 + 4 * stap
    d.append(f'<circle cx="{cx}" cy="50" r="24" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
    kruis(cx, 50)
    onder(cx, "reiniging", "doorstreept: het mag niet")
    d.append(_tekst(16, hoogte - 6,
                    "een kruis door een symbool betekent altijd: deze behandeling is verboden",
                    9.5, DIM, "start"))
    return _svg(breedte, hoogte, "".join(d))


# 🚀 Boost dubbele finaliteit — ontwikkeling en pedagogisch handelen

def driehoekmodel(hoeken, midden="", breedte=470):
    """Een driehoek met bij elke hoek een naam en een regel uitleg, en in het
    midden waar het model over gaat. `hoeken` is [(naam, uitleg), ...] met drie
    hoeken: boven, linksonder, rechtsonder."""
    hoogte = 262
    cx, top, basis_y = 235, 42, 208
    half = 150
    d = [f'<polygon points="{cx},{top} {cx-half},{basis_y} {cx+half},{basis_y}" fill="{FOREST}" '
         f'fill-opacity="0.10" stroke="{FOREST}" stroke-width="2"/>']
    if midden:
        d.append(_tekst(cx, 162, midden, 11, FOREST, "middle", True))
    plekken = [(cx, top - 26, "middle", top - 13),
               (cx - half, basis_y + 18, "start", basis_y + 31),
               (cx + half, basis_y + 18, "end", basis_y + 31)]
    for (naam, uitleg), (x, y, anker, y2) in zip(hoeken, plekken):
        d.append(_tekst(x, y, naam, 11, INK, anker, True))
        d.append(_tekst(x, y2, uitleg, 9.5, DIM, anker))
    for px, py in ((cx, top), (cx - half, basis_y), (cx + half, basis_y)):
        d.append(f'<circle cx="{px}" cy="{py}" r="5" fill="{FOREST}"/>')
    return _svg(breedte, hoogte, "".join(d))


def kwadranten(vakken, breedte=470, onder=None):
    """Vier vakken naast en onder elkaar. `vakken` is [(kop, [regels]), ...],
    vier stuks. `onder` is een slotzin onder de vier."""
    kolom = (breedte - 10) / 2
    regels = max(len(r) for _, r in vakken)
    vh = 34 + regels * 17 + 8
    h = vh * 2 + 10
    kleuren = [FOREST, AMBER, "#6f8f4a", DIM]
    for i, (kop, rs) in enumerate(vakken):
        vx = 0 if i % 2 == 0 else kolom + 10
        vy = 0 if i < 2 else vh + 10
        kleur = kleuren[i]
        yield_ = None
    d = []
    for i, (kop, rs) in enumerate(vakken):
        vx = 0 if i % 2 == 0 else kolom + 10
        vy = 0 if i < 2 else vh + 10
        kleur = kleuren[i]
        d.append(f'<rect x="{vx:.1f}" y="{vy}" width="{kolom:.1f}" height="{vh}" rx="8" '
                 f'fill="#ffffff" stroke="{kleur}" stroke-width="1.6"/>')
        d.append(_tekst(vx + 12, vy + 19, kop, 11.5, kleur, "start", True))
        for j, r in enumerate(rs):
            d.append(_tekst(vx + 12, vy + 38 + j * 17, "· " + r, 10.5, DIM, "start"))
    extra = 0
    if onder:
        d.append(_tekst(breedte / 2, h + 12, onder, 9.5, DIM, "middle"))
        extra = 18
    return _svg(breedte, h + 6 + extra, "".join(d))


def groeicurveschets(breedte=470):
    """Een groeicurve zonder cijfers: de band waarin de meeste kinderen van een
    leeftijd zitten, met de lijn van één kind erdoor. De assen dragen namen,
    geen getallen, want dit is geen echte referentiecurve."""
    hoogte = 250
    links, onder, boven, rechts = 52, 44, 16, 24
    bx, by = breedte - links - rechts, hoogte - onder - boven
    d = [f'<line x1="{links}" y1="{boven}" x2="{links}" y2="{boven+by}" stroke="{INK}" stroke-width="1.6"/>',
         f'<line x1="{links}" y1="{boven+by}" x2="{links+bx}" y2="{boven+by}" stroke="{INK}" stroke-width="1.6"/>']

    def punt(t, f):
        """t van 0 tot 1 over de leeftijd, f van 0 tot 1 over de lengte."""
        return links + t * bx, boven + by - f * by

    # de band: een onder- en een bovengrens die allebei afvlakken
    def lijn(hoog):
        ps = []
        for i in range(41):
            t = i / 40
            f = hoog * (1 - (1 - t) ** 1.7)
            ps.append("%.1f %.1f" % punt(t, f))
        return ps
    laag, hoogg = lijn(0.60), lijn(0.95)
    d.append(f'<path d="M{" L".join(laag)} L{" L".join(reversed(hoogg))} Z" fill="{FOREST}" '
             f'fill-opacity="0.14" stroke="none"/>')
    for ps, kleur in ((laag, FOREST), (hoogg, FOREST)):
        d.append(f'<path d="M{" L".join(ps)}" fill="none" stroke="{kleur}" stroke-width="1.4" '
                 f'stroke-dasharray="4 3"/>')
    # het kind zelf: netjes in de band, met een knik waar de groeispurt zit
    kind = []
    for i in range(41):
        t = i / 40
        f = 0.78 * (1 - (1 - t) ** 1.7)
        if t > 0.62:
            f += 0.10 * min(1.0, (t - 0.62) / 0.18)
        kind.append("%.1f %.1f" % punt(t, f))
    d.append(f'<path d="M{" L".join(kind)}" fill="none" stroke="{AMBER}" stroke-width="2.4"/>')
    px, py = punt(0.72, 0.78 * (1 - 0.28 ** 1.7) + 0.10 * min(1.0, 0.10 / 0.18))
    d.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{AMBER}"/>')
    d.append(_tekst(px - 12, py - 16, "de groeispurt", 9.5, AMBER, "end", True))
    d.append(f'<rect x="{links+bx-204:.1f}" y="{boven+by-46}" width="200" height="38" rx="6" '
             f'fill="#ffffff" fill-opacity="0.92" stroke="{BORDER}" stroke-width="1"/>')
    d.append(f'<line x1="{links+bx-194:.1f}" y1="{boven+by-33}" x2="{links+bx-172:.1f}" y2="{boven+by-33}" '
             f'stroke="{AMBER}" stroke-width="2.4"/>')
    d.append(_tekst(links + bx - 166, boven + by - 30, "dit kind", 9.5, INK, "start", True))
    d.append(f'<line x1="{links+bx-194:.1f}" y1="{boven+by-17}" x2="{links+bx-172:.1f}" y2="{boven+by-17}" '
             f'stroke="{FOREST}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    d.append(_tekst(links + bx - 166, boven + by - 14, "de band van zijn leeftijdsgenoten", 9.5, DIM, "start"))
    d.append(_tekst(links + bx / 2, hoogte - 10, "de leeftijd", 10, INK, "middle", True))
    d.append(f'<text x="16" y="{boven + by/2:.1f}" text-anchor="middle" '
             f'transform="rotate(-90 16 {boven + by/2:.1f})" font-family="IBM Plex Sans,sans-serif" '
             f'font-size="10" font-weight="600" fill="{INK}">de lengte</text>')
    return _svg(breedte, hoogte, "".join(d))


def watercyclus(breedte=470):
    """De hydrologische cyclus boven een kust: verdampen, condenseren, neerslaan,
    afstromen en infiltreren.

    De vijf stappen staan elk één keer, met de pijl in de richting waarin het
    water echt gaat. Links de zee waaruit het grootste deel verdampt, rechts
    het land waar de neerslag valt en terugstroomt.
    """
    h = 250
    punt = _pijlpunt(DARK)
    blauw = _pijlpunt(ZEE)
    d = [f'<rect x="0" y="0" width="{breedte}" height="236" fill="{LUCHT}"/>']

    # De zon links boven.
    d.append(f'<circle cx="44" cy="36" r="17" fill="{AMBER}"/>')
    for i in range(8):
        import math
        a = i * math.pi / 4
        d.append(f'<line x1="{44 + 22 * math.cos(a):.1f}" y1="{36 + 22 * math.sin(a):.1f}" '
                 f'x2="{44 + 28 * math.cos(a):.1f}" y2="{36 + 28 * math.sin(a):.1f}" '
                 f'stroke="{AMBER}" stroke-width="2" stroke-linecap="round"/>')

    # De zee links, het land rechts.
    d.append(f'<rect x="0" y="150" width="215" height="86" fill="{ZEE}"/>')
    d.append(f'<path d="M 215 150 L 272 150 L 330 104 L 372 118 L 430 78 L 470 92 L 470 236 L 215 236 Z" '
             f'fill="{GRAS}" stroke="{DARK}" stroke-width="1.4"/>')
    d.append(f'<path d="M 215 206 L 272 206 L 330 180 L 400 188 L 470 168 L 470 236 L 215 236 Z" '
             f'fill="{ZAND_DONKER}" opacity="0.85"/>')

    # De wolk.
    for cx, cy, rx, ry in [(192, 52, 21, 14), (215, 44, 27, 18), (240, 53, 21, 13)]:
        d.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#ffffff" '
                 f'stroke="{DIM}" stroke-width="1"/>')

    # Verdamping, condensatie, neerslag, afstroming, infiltratie.
    d.append(f'<path d="M 104 146 Q 112 100 148 74" fill="none" stroke="{ZEE}" stroke-width="2.2" '
             f'marker-end="url(#{blauw})"/>')
    d.append(f'<line x1="162" y1="70" x2="184" y2="56" stroke="{DARK}" stroke-width="2" '
             f'marker-end="url(#{punt})"/>')
    for x0, x1, y1 in [(250, 253, 104), (268, 271, 110), (286, 289, 100)]:
        d.append(f'<line x1="{x0}" y1="68" x2="{x1}" y2="{y1}" stroke="{ZEE}" stroke-width="2.2" '
                 f'marker-end="url(#{blauw})"/>')
    d.append(f'<path d="M 424 86 Q 360 122 300 134 Q 252 144 222 150" fill="none" stroke="{ZEE}" '
             f'stroke-width="2.6" marker-end="url(#{blauw})"/>')
    d.append(f'<line x1="336" y1="132" x2="340" y2="176" stroke="{ZEE}" stroke-width="2.2" '
             f'marker-end="url(#{blauw})"/>')

    d.append(_kussen(126, 114, "verdamping", 9.5, DARK, "start", vet=True))
    d.append(_kussen(215, 22, "condensatie", 9.5, DARK, "middle", vet=True))
    d.append(_kussen(300, 92, "neerslag", 9.5, DARK, "start", vet=True))
    d.append(_kussen(276, 158, "afstroming", 9.5, DARK, "middle", vet=True))
    d.append(_kussen(348, 184, "infiltratie", 9.5, DARK, "start", vet=True))
    d.append(_kussen(228, 226, "grondwater", 9.5, DARK, "start"))

    return _svg(breedte, h, _pijlpunten() + "".join(d))


def gesteentecyclus(breedte=470):
    """De gesteentecyclus: magma, magmatisch, sedimentair en metamorf gesteente.

    De buitenste pijlen lopen de hele kring rond. De pijl binnenin is er
    omdat een metamorf gesteente dat aan de oppervlakte komt, net zo goed
    verweert als elk ander gesteente: de kring heeft geen vaste orde.
    """
    h = 272
    punt = _pijlpunt(DARK)
    d = []
    vakken = [
        (160, 10, 150, 44, ["magmatisch", "gesteente"], "#dcd3e8"),
        (320, 110, 146, 44, ["sediment en", "sedimentair gesteente"], ZAND),
        (160, 212, 150, 44, ["metamorf", "gesteente"], "#cfd6c6"),
        (4, 110, 146, 44, ["magma"], "#f0c9b4"),
    ]
    for x, y, w, hh, regels, kleur in vakken:
        d.append(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="9" fill="{kleur}" '
                 f'stroke="{DARK}" stroke-width="1.6"/>')
        start = y + hh / 2 + (4 if len(regels) == 1 else -3)
        for i, r in enumerate(regels):
            d.append(_tekst(x + w / 2, start + i * 13, r, 10, INK, vet=(i == 0)))

    for x1, y1, x2, y2 in [(124, 110, 182, 56), (316, 46, 384, 106),
                           (386, 158, 318, 212), (154, 220, 92, 158),
                           (268, 212, 330, 160)]:
        d.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DARK}" stroke-width="2" '
                 f'marker-end="url(#{punt})"/>')

    d.append(_kussen(114, 76, "afkoelen", 9.5, DARK, "middle", vet=True))
    d.append(_kussen(378, 70, "verwering en erosie", 9.5, DARK, "middle", vet=True))
    d.append(_kussen(374, 200, "druk en hitte", 9.5, DARK, "middle", vet=True))
    d.append(_kussen(100, 196, "smelten", 9.5, DARK, "middle", vet=True))
    d.append(_kussen(266, 178, "verwering", 9.5, DARK, "middle"))

    return _svg(breedte, h, _pijlpunten() + "".join(d))


def normaalkromme(mu, sigma, van=None, tot=None, breedte=470, xlabel="",
                  hoogte=228, toon_kans=True):
    """De klok van een normale verdeling, met een gearceerd stuk eronder.

    Alles wordt gerekend, niets getekend op het gevoel: de klok is de echte
    dichtheidsfunctie, de streepjes staan op mu en op mu plus of min één en
    twee keer sigma, en de kans in het gearceerde stuk komt uit de
    foutfunctie. Zo kan de tekening nooit iets anders zeggen dan de tekst.

    van en tot mogen None zijn: dat is een staart die doorloopt.
    """
    import math

    links, onder, boven, rechts = 30, 44, 26, 22
    vlak_b = breedte - links - rechts
    vlak_h = hoogte - onder - boven
    x0, x1 = mu - 4 * sigma, mu + 4 * sigma

    def px(v):
        return links + (v - x0) / (x1 - x0) * vlak_b

    def dichtheid(v):
        return math.exp(-0.5 * ((v - mu) / sigma) ** 2)

    def py(v):
        return hoogte - onder - dichtheid(v) * vlak_h

    stappen_n = 240
    punten = [(x0 + i * (x1 - x0) / stappen_n) for i in range(stappen_n + 1)]
    d = []

    # het gearceerde stuk, als een gevulde vorm onder de kromme
    a = x0 if van is None else max(van, x0)
    b = x1 if tot is None else min(tot, x1)
    if a < b:
        rand = [(a + i * (b - a) / stappen_n) for i in range(stappen_n + 1)]
        pad = [f"M {px(a):.1f} {hoogte-onder:.1f}"]
        pad += [f"L {px(v):.1f} {py(v):.1f}" for v in rand]
        pad.append(f"L {px(b):.1f} {hoogte-onder:.1f} Z")
        d.append(f'<path d="{" ".join(pad)}" fill="{FOREST}" fill-opacity="0.22"/>')

    # de kromme zelf
    lijn = " ".join(f"{'M' if i == 0 else 'L'} {px(v):.1f} {py(v):.1f}"
                    for i, v in enumerate(punten))
    d.append(f'<path d="{lijn}" fill="none" stroke="{FOREST}" stroke-width="2.2"/>')

    # de as, met een streepje op mu en op elke sigma ernaast
    as_y = hoogte - onder
    d.append(f'<line x1="{links-6}" y1="{as_y}" x2="{breedte-rechts+6}" y2="{as_y}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    for k in (-2, -1, 0, 1, 2):
        v = mu + k * sigma
        d.append(f'<line x1="{px(v):.1f}" y1="{as_y}" x2="{px(v):.1f}" y2="{as_y+5}" '
                 f'stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(px(v), as_y + 18, _getal(v), 9.5, DIM))
        naam = "μ" if k == 0 else ("μ" + ("+" if k > 0 else "−")
                                   + ("σ" if abs(k) == 1 else f"{abs(k)}σ"))
        d.append(_tekst(px(v), as_y + 31, naam, 9, DIM))
    d.append(f'<line x1="{px(mu):.1f}" y1="{py(mu):.1f}" x2="{px(mu):.1f}" y2="{as_y}" '
             f'stroke="{AMBER}" stroke-width="1.6" stroke-dasharray="4 3"/>')

    # de grenzen van het gearceerde stuk, met hun waarde erboven
    for grens in (van, tot):
        if grens is None or not x0 < grens < x1:
            continue
        d.append(f'<line x1="{px(grens):.1f}" y1="{py(grens):.1f}" x2="{px(grens):.1f}" '
                 f'y2="{as_y}" stroke="{DARK}" stroke-width="1.8"/>')
        # het getal naast de grenslijn, aan de kant van de staart, zodat het
        # niet op de kromme zelf komt te liggen
        kant = 5 if grens >= mu else -5
        d.append(_tekst(px(grens) + kant, py(grens) - 5, _getal(grens), 10, DARK,
                        "start" if kant > 0 else "end", True))

    if toon_kans and a < b:
        def phi(v):
            return 0.5 * (1 + math.erf((v - mu) / (sigma * math.sqrt(2))))
        kans = phi(b) - phi(a)
        midden_x = px((a + b) / 2)
        d.append(_tekst(midden_x, as_y - 14, f"{kans * 100:.1f}".replace(".", ",") + " %",
                        11, DARK, "middle", True))
    if xlabel:
        d.append(_tekst(breedte - rechts + 6, boven - 10, xlabel, 10.5, DIM, "end", True))
    return _svg(breedte, hoogte, "".join(d))


def dotplot(getallen, breedte=470, stap=1, hoogte=None):
    """Een dotplot: één bolletje per meting, gestapeld boven zijn waarde.

    Voor een kleine dataset met weinig verschillende waarden. Het aantal
    bolletjes is het aantal metingen, dus de tekening telt zichzelf na.
    """
    g = sorted(getallen)
    laag = stap * int(min(g) // stap) - stap
    hoog = stap * int(-(-max(g) // stap)) + stap
    hoogste_stapel = max(g.count(w) for w in set(g))
    r = 6.0
    hoogte = hoogte or int(44 + hoogste_stapel * (2 * r + 2.5))
    links, rechts = 24, 22
    as_y = hoogte - 32

    def px(v):
        return links + (v - laag) / max(hoog - laag, 1) * (breedte - links - rechts)

    d = [f'<line x1="{links-6}" y1="{as_y}" x2="{breedte-rechts+6}" y2="{as_y}" '
         f'stroke="{INK}" stroke-width="1.6"/>']
    tik = laag
    while tik <= hoog + 1e-9:
        d.append(f'<line x1="{px(tik):.1f}" y1="{as_y}" x2="{px(tik):.1f}" y2="{as_y+5}" '
                 f'stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(px(tik), as_y + 18, _getal(tik), 9.5, DIM))
        tik += stap
    for waarde in sorted(set(g)):
        for i in range(g.count(waarde)):
            cy = as_y - r - 2 - i * (2 * r + 2.5)
            d.append(f'<circle cx="{px(waarde):.1f}" cy="{cy:.1f}" r="{r}" '
                     f'fill="{FOREST}" fill-opacity="0.75" stroke="{FOREST}" stroke-width="1.2"/>')
    return _svg(breedte, hoogte, "".join(d))


def histogram(klassen, breedte=470, hoogte=224, xlabel="", ylabel="aantal"):
    """Een histogram: staven die elkaar raken, want de klassen sluiten aan.

    klassen is een lijst (ondergrens, bovengrens, frequentie). De breedte van
    een staaf volgt de breedte van haar klasse, zodat een bredere klasse ook
    een bredere staaf krijgt; dat is net het verschil met een staafdiagram.
    """
    links, onder, boven, rechts = 40, 44, 22, 18
    vlak_b = breedte - links - rechts
    vlak_h = hoogte - onder - boven
    laag = min(k[0] for k in klassen)
    hoog = max(k[1] for k in klassen)
    top = max(k[2] for k in klassen)
    stap_y = 1 if top <= 6 else (2 if top <= 14 else 5 if top <= 35 else 10)
    bovengrens = stap_y * int(-(-top // stap_y))

    def px(v):
        return links + (v - laag) / max(hoog - laag, 1) * vlak_b

    def py(v):
        return hoogte - onder - v / max(bovengrens, 1) * vlak_h

    d = []
    tik = 0
    while tik <= bovengrens:
        d.append(f'<line x1="{links}" y1="{py(tik):.1f}" x2="{breedte-rechts}" '
                 f'y2="{py(tik):.1f}" stroke="{BORDER}" stroke-width="1"/>')
        d.append(_tekst(links - 8, py(tik) + 3.5, str(tik), 9.5, DIM, "end"))
        tik += stap_y
    for onder_g, boven_g, freq in klassen:
        x, b = px(onder_g), px(boven_g) - px(onder_g)
        d.append(f'<rect x="{x:.1f}" y="{py(freq):.1f}" width="{b:.1f}" '
                 f'height="{hoogte-onder-py(freq):.1f}" fill="{FOREST}" fill-opacity="0.3" '
                 f'stroke="{FOREST}" stroke-width="1.6"/>')
        if freq:
            d.append(_tekst(x + b / 2, py(freq) - 6, str(freq), 10, DARK, "middle", True))
    d.append(f'<line x1="{links}" y1="{boven-6}" x2="{links}" y2="{hoogte-onder}" '
             f'stroke="{INK}" stroke-width="1.8"/>')
    d.append(f'<line x1="{links}" y1="{hoogte-onder}" x2="{breedte-rechts+6}" '
             f'y2="{hoogte-onder}" stroke="{INK}" stroke-width="1.8"/>')
    for grens in sorted({k[0] for k in klassen} | {k[1] for k in klassen}):
        d.append(f'<line x1="{px(grens):.1f}" y1="{hoogte-onder}" x2="{px(grens):.1f}" '
                 f'y2="{hoogte-onder+5}" stroke="{DIM}" stroke-width="1.2"/>')
        d.append(_tekst(px(grens), hoogte - onder + 18, _getal(grens), 9.5, DIM))
    d.append(_tekst(links - 2, boven - 8, ylabel, 10.5, DIM, "start", True))
    if xlabel:
        d.append(_tekst(breedte - rechts + 6, hoogte - onder + 32, xlabel, 10.5, DIM, "end", True))
    return _svg(breedte, hoogte, "".join(d))


# ---------------------------------------------------------------------------
# Elektrostatica. Enya Vermeyen, leerkracht wiskunde en fysica, schreef op
# 10 oktober 2026 dat er bij de theorie van fysica geen enkele afbeelding
# stond, terwijl fysica net bij uitstek via afbeeldingen werkt, en noemde de
# elektroscoop als voorbeeld van iets waar leerlingen zelfs mét een tekening
# nog moeite mee hebben. Ze had gelijk: in de drieëntwintig fysicabundels van
# 🌍 Beyond stond geen enkele figuur. Deze drie zijn de eerste.
# ---------------------------------------------------------------------------

LADING_MIN = "#2f6d9e"    # negatief, koel
LADING_PLUS = "#b4452c"   # positief, warm
GLAS = "#eef4f6"
METAAL = "#cdd4d8"


def _teken(x, y, soort, r=7.2):
    """Een plus- of minteken in een bolletje, zoals in een schoolboek."""
    kleur = LADING_PLUS if soort == "+" else LADING_MIN
    streep = (f'<line x1="{x-3.4:.1f}" y1="{y:.1f}" x2="{x+3.4:.1f}" y2="{y:.1f}" '
              f'stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>')
    if soort == "+":
        streep += (f'<line x1="{x:.1f}" y1="{y-3.4:.1f}" x2="{x:.1f}" y2="{y+3.4:.1f}" '
                   f'stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>')
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{kleur}"/>' + streep


def _staaf(x, y, breed, soort, label):
    """Een geladen staaf, liggend, met haar tekens erop."""
    kleur = LADING_PLUS if soort == "+" else LADING_MIN
    d = [f'<rect x="{x:.1f}" y="{y:.1f}" width="{breed:.1f}" height="19" rx="9.5" '
         f'fill="#ffffff" stroke="{kleur}" stroke-width="1.8"/>']
    aantal = max(3, int(breed // 26))
    for i in range(aantal):
        cx = x + breed * (i + 0.5) / aantal
        d.append(_teken(cx, y + 9.5, soort, 6.4))
    d.append(_tekst(x + breed / 2, y + 36, label, 9.5, kleur, "middle", True))
    return "".join(d)


def _elektroscoop(cx, geladen):
    """Eén elektroscoop. De bladen hangen samen of wijken uit."""
    import math
    d = []
    # de glazen stolp met de voet
    d.append(f'<path d="M{cx-58} 88 h116 v104 h-116 z" fill="{GLAS}" stroke="{DIM}" stroke-width="1.4"/>')
    d.append(f'<rect x="{cx-70}" y="192" width="140" height="11" rx="3" fill="{METAAL}" stroke="{DIM}" stroke-width="1.2"/>')
    # de stop bovenaan, isolerend, en de metalen staaf erdoor
    d.append(f'<rect x="{cx-26}" y="78" width="52" height="14" rx="4" fill="{AMBER}" opacity="0.65"/>')
    d.append(f'<line x1="{cx}" y1="42" x2="{cx}" y2="146" stroke="{DIM}" stroke-width="4" stroke-linecap="round"/>')
    d.append(f'<circle cx="{cx}" cy="34" r="15" fill="{METAAL}" stroke="{DIM}" stroke-width="1.4"/>')
    # de twee blaadjes: samen als er geen lading op staat, uitgeweken als wel
    schuin = 23.0 if geladen else 2.0
    dx = 44 * math.tan(math.radians(schuin))
    for kant in (-1, 1):
        top1, top2 = cx + kant * 1.5, cx + kant * 4.5
        d.append(f'<path d="M{top1:.1f} 146 L{top2:.1f} 146 L{top2 + kant*dx:.1f} 190 '
                 f'L{top1 + kant*dx:.1f} 190 Z" fill="{METAAL}" stroke="{DIM}" stroke-width="1.2"/>')
    if geladen:
        for tx, ty in [(cx, 34), (cx - 12, 104), (cx + 12, 126)]:
            d.append(_teken(tx, ty, "-", 6.6))
        for kant in (-1, 1):
            d.append(_teken(cx + kant * (3 + dx), 174, "-", 6.6))
        # twee pijltjes die zeggen welke kant de bladen op gaan
        for kant in (-1, 1):
            van, tot = cx + kant * 31, cx + kant * 50
            d.append(f'<path d="M{van:.1f} 186 H{tot:.1f}" stroke="{LADING_MIN}" stroke-width="1.6"/>')
            d.append(f'<path d="M{tot:.1f} 186 l{-kant*6} -4 v8 z" fill="{LADING_MIN}"/>')
    return "".join(d)


def elektroscoop(breedte=470):
    """Twee elektroscopen naast elkaar: ongeladen en negatief geladen.

    Het punt van de tekening is het verschil tussen de twee bladen. Links
    hangen ze samen omdat er niets op staat; rechts dragen ze allebei dezelfde
    negatieve lading, dus stoten ze elkaar af en wijken ze uit.
    """
    h = 240
    d = [_elektroscoop(148, False), _elektroscoop(352, True)]
    # de onderdelen staan één keer benoemd, bij de linkse. De aanwijslijn
    # loopt gerust over het glas heen: het glas is doorzichtig.
    for ly, naam, tot in [(38, "knop", 130), (112, "staaf", 144), (170, "blaadjes", 144)]:
        d.append(f'<path d="M72 {ly-3.5} H{tot}" stroke="{DIM}" '
                 f'stroke-width="0.9" stroke-dasharray="3 3"/>')
        d.append(f'<circle cx="{tot}" cy="{ly-3.5}" r="1.8" fill="{DIM}"/>')
        d.append(_tekst(68, ly, naam, 9.5, DIM, "end"))
    d.append(_tekst(148, 224, "ongeladen", 10.5, DIM, "middle", True))
    d.append(_tekst(352, 224, "negatief geladen", 10.5, LADING_MIN, "middle", True))
    return _svg(breedte, h, "".join(d))


def influentie(breedte=470):
    """Een negatief geladen staaf bij een metalen bol, zonder aanraking.

    De vrije elektronen vluchten naar de verste kant, dus de dichtste kant
    blijft positief achter. In totaal verandert de lading van de bol niet.
    """
    h = 214
    cx, cy, r = 330, 98, 58
    d = [_staaf(20, 88, 138, "-", "negatief geladen staaf")]
    # de bol op een isolerende voet
    d.append(f'<rect x="{cx-9}" y="{cy+r-4}" width="18" height="24" fill="{AMBER}" opacity="0.65"/>')
    d.append(f'<rect x="{cx-40}" y="{cy+r+20}" width="80" height="9" rx="3" fill="{AMBER}" opacity="0.65"/>')
    d.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{METAAL}" stroke="{DIM}" stroke-width="1.6"/>')
    # links de positieve kant, rechts de elektronen die weggeduwd zijn
    for ty in (-26, 0, 26):
        d.append(_teken(cx - 38, cy + ty, "+", 6.6))
    for ty in (-30, -10, 10, 30):
        d.append(_teken(cx + 39, cy + ty, "-", 6.6))
    # de pijl die zegt waar de elektronen naartoe gaan
    d.append(f'<path d="M{cx-14} {cy} H{cx+14}" stroke="{LADING_MIN}" stroke-width="2"/>')
    d.append(f'<path d="M{cx+16} {cy} l-7 -4.5 v9 z" fill="{LADING_MIN}"/>')
    d.append(_tekst(cx, cy - 14, "elektronen", 9, LADING_MIN, "middle", True))
    # de tussenruimte, want de staaf raakt de bol niet aan
    d.append(f'<path d="M162 56 H268" stroke="{DIM}" stroke-width="1.2" stroke-dasharray="4 4"/>')
    d.append(f'<path d="M162 56 l7 -4 v8 z" fill="{DIM}"/>')
    d.append(f'<path d="M268 56 l-7 -4 v8 z" fill="{DIM}"/>')
    d.append(_tekst(215, 48, "geen contact", 9.5, DIM))
    d.append(_tekst(cx - 48, 196, "dichtste kant: positief", 9.5, LADING_PLUS, "middle"))
    d.append(_tekst(cx + 70, 196, "verste kant: negatief", 9.5, LADING_MIN, "middle"))
    return _svg(breedte, h, "".join(d))


def polarisatie(breedte=470):
    """Dezelfde isolator zonder en met een geladen staaf ernaast.

    In een isolator kunnen de elektronen hun atoom niet verlaten. De moleculen
    worden dipolen en draaien zich alleen maar een beetje, met hun positieve
    kant naar de negatieve staaf toe.
    """
    import math
    h = 206

    def dipool(x, y, graden):
        """Eén molecule als een ovaaltje met een plus- en een mintekenkant.

        Bij 0 graden staat de pluskant links. Let daarop: de pluskant moet
        naar de negatieve staaf wijzen, anders spreekt de tekening haar eigen
        bijschrift tegen.
        """
        hoek = math.radians(graden)
        dx, dy = 10.5 * math.cos(hoek), 10.5 * math.sin(hoek)
        return (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="15" ry="8.5" fill="#ffffff" '
                f'stroke="{DIM}" stroke-width="1.1" '
                f'transform="rotate({graden:.0f} {x:.1f} {y:.1f})"/>'
                + _teken(x - dx, y - dy, "+", 5.6) + _teken(x + dx, y + dy, "-", 5.6))

    d = []
    # links: door elkaar, want er staat niets in de buurt
    kris = [18, 142, 73, 205, 101, 160]
    d.append(f'<rect x="22" y="56" width="166" height="104" rx="8" fill="{GLAS}" stroke="{DIM}" stroke-width="1.4"/>')
    for i, graden in enumerate(kris):
        d.append(dipool(56 + (i % 3) * 49, 84 + (i // 3) * 46, graden))
    d.append(_tekst(105, 180, "zonder staaf: door elkaar", 10, DIM))

    # rechts: allemaal met hun pluskant naar de staaf, die links ernaast staat
    d.append(f'<rect x="282" y="56" width="166" height="104" rx="8" fill="{GLAS}" stroke="{DIM}" stroke-width="1.4"/>')
    for i in range(6):
        d.append(dipool(316 + (i % 3) * 49, 84 + (i // 3) * 46, 0))
    d.append(f'<rect x="246" y="60" width="18" height="96" rx="9" fill="#ffffff" stroke="{LADING_MIN}" stroke-width="1.8"/>')
    for ty in (80, 108, 136):
        d.append(_teken(255, ty, "-", 6.2))
    d.append(_tekst(255, 46, "staaf", 9, LADING_MIN))
    d.append(_tekst(365, 180, "met staaf: de pluskant naar de staaf", 10, LADING_MIN, "middle", True))
    d.append(_tekst(235, 199, "de moleculen verhuizen niet, ze draaien alleen", 9.5, DIM, "middle"))
    return _svg(breedte, h, "".join(d))


def _pijlkop(x, y, hoek, kleur, maat=5.0):
    """Een driehoekje op (x, y), met de punt in de richting hoek (radialen)."""
    import math
    c, s = math.cos(hoek), math.sin(hoek)
    punten = []
    for px, py in ((maat, 0.0), (-maat * 0.8, maat * 0.62), (-maat * 0.8, -maat * 0.62)):
        punten.append(f"{x + px*c - py*s:.1f},{y + px*s + py*c:.1f}")
    return f'<polygon points="{" ".join(punten)}" fill="{kleur}"/>'


def veldpatronen(breedte=470):
    r"""De vier veldlijnenpatronen die de vakfiche noemt, in één figuur.

    Radiaal rond een positieve en rond een negatieve puntlading, het dipool-
    veld tussen twee ongelijknamige ladingen, en het homogene veld tussen twee
    platen. De afspraak over de zin staat in elk vak: weg van positief, naar
    negatief toe.

    De fiche vraagt om veldlijnen te kunnen tekenen. In een meerkeuzevraag kan
    dat niet, dus staan ze hier.
    """
    import math
    cel_b, cel_h = 234, 186
    VELD = FOREST
    d = []

    def kader(kx, ky, titel):
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{cel_b-12}" height="{cel_h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, ky + cel_h - 8, titel, 10, DIM, "middle", True))

    def radiaal(kx, ky, soort):
        cx, cy = kx + cel_b / 2, ky + 82
        for i in range(8):
            hoek = math.radians(i * 45)
            c, s = math.cos(hoek), math.sin(hoek)
            r0, r1 = 15, 60
            d.append(f'<line x1="{cx + r0*c:.1f}" y1="{cy + r0*s:.1f}" '
                     f'x2="{cx + r1*c:.1f}" y2="{cy + r1*s:.1f}" stroke="{VELD}" stroke-width="1.3"/>')
            # de punt staat halfweg, zodat ze niet tegen de rand aanloopt
            rp = 44 if soort == "+" else 30
            d.append(_pijlkop(cx + rp * c, cy + rp * s, hoek if soort == "+" else hoek + math.pi, VELD))
        d.append(_teken(cx, cy, soort, 13))

    def dipool(kx, ky):
        cy = ky + 82
        xl, xr = kx + 56, kx + cel_b - 56
        for boog in (-54, -26, 0, 26, 54):
            mx, my = (xl + xr) / 2, cy + boog
            pad = f"M{xl+14} {cy} Q{mx:.0f} {my + boog:.0f} {xr-14} {cy}"
            d.append(f'<path d="{pad}" fill="none" stroke="{VELD}" stroke-width="1.3"/>')
            # halverwege een bezier: het punt en de raaklijn
            px = ((xl + 14) + 2 * mx + (xr - 14)) / 4
            py = (cy + 2 * (my + boog) + cy) / 4
            d.append(_pijlkop(px, py, 0.0, VELD))
        d.append(_teken(xl, cy, "+", 13))
        d.append(_teken(xr, cy, "-", 13))

    def homogeen(kx, ky):
        cy = ky + 82
        xl, xr = kx + 40, kx + cel_b - 40
        d.append(f'<rect x="{xl-9}" y="{cy-56}" width="9" height="112" fill="{LADING_PLUS}" opacity="0.8"/>')
        d.append(f'<rect x="{xr}" y="{cy-56}" width="9" height="112" fill="{LADING_MIN}" opacity="0.8"/>')
        for dy in (-40, -20, 0, 20, 40):
            d.append(f'<line x1="{xl+2}" y1="{cy+dy}" x2="{xr-2}" y2="{cy+dy}" stroke="{VELD}" stroke-width="1.3"/>')
            d.append(_pijlkop((xl + xr) / 2, cy + dy, 0.0, VELD))
        d.append(_tekst(xl - 5, cy - 62, "+", 12, LADING_PLUS))
        d.append(_tekst(xr + 5, cy - 62, "–", 13, LADING_MIN))

    kader(0, 0, "radiaal: weg van een positieve lading")
    radiaal(0, 0, "+")
    kader(cel_b, 0, "radiaal: naar een negatieve lading toe")
    radiaal(cel_b, 0, "-")
    kader(0, cel_h, "dipool: van plus naar min")
    dipool(0, cel_h)
    kader(cel_b, cel_h, "homogeen: overal even sterk")
    homogeen(cel_b, cel_h)
    return _svg(breedte, cel_h * 2, "".join(d))


def equipotentiaal(breedte=470):
    r"""Equipotentiaallijnen naast de veldlijnen, in twee gevallen.

    Links rond een puntlading: de veldlijnen lopen stervormig naar buiten, de
    equipotentiaallijnen zijn cirkels eromheen. Rechts tussen twee platen: de
    veldlijnen lopen recht van plus naar min, de equipotentiaallijnen staan er
    als evenwijdige rechten dwars op.

    Wat je op de tekening moet zien, en wat met woorden alleen niet lukt: de
    twee soorten lijnen staan overal loodrecht op elkaar. Daarom kost het geen
    arbeid om een lading langs zo'n stippellijn te verplaatsen.
    """
    import math
    cel_b, cel_h = 234, 196
    VELD = FOREST
    EQUI = AMBER
    d = []

    def kader(kx, titel):
        d.append(f'<rect x="{kx+6}" y="4" width="{cel_b-12}" height="{cel_h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, cel_h - 8, titel, 10, DIM, "middle", True))

    kader(0, "rond een puntlading: cirkels")
    kader(cel_b, "tussen twee platen: rechten")

    # links: puntlading met cirkels eromheen
    cx, cy = cel_b / 2, 86
    for straal in (30, 48, 66):
        d.append(f'<circle cx="{cx}" cy="{cy}" r="{straal}" fill="none" stroke="{EQUI}" '
                 f'stroke-width="1.2" stroke-dasharray="4 3"/>')
    for i in range(8):
        hoek = math.radians(i * 45)
        c, s = math.cos(hoek), math.sin(hoek)
        d.append(f'<line x1="{cx + 14*c:.1f}" y1="{cy + 14*s:.1f}" '
                 f'x2="{cx + 74*c:.1f}" y2="{cy + 74*s:.1f}" stroke="{VELD}" stroke-width="1.3"/>')
        d.append(_pijlkop(cx + 56 * c, cy + 56 * s, hoek, VELD))
    d.append(_teken(cx, cy, "+", 12))

    # rechts: twee platen met rechten ertussen
    kx = cel_b
    xl, xr = kx + 44, kx + cel_b - 44
    d.append(f'<rect x="{xl-9}" y="{cy-58}" width="9" height="116" fill="{LADING_PLUS}" opacity="0.8"/>')
    d.append(f'<rect x="{xr}" y="{cy-58}" width="9" height="116" fill="{LADING_MIN}" opacity="0.8"/>')
    for deel in (1, 2, 3):
        x = xl + (xr - xl) * deel / 4
        d.append(f'<line x1="{x:.1f}" y1="{cy-52}" x2="{x:.1f}" y2="{cy+52}" stroke="{EQUI}" '
                 f'stroke-width="1.2" stroke-dasharray="4 3"/>')
    for dy in (-34, 0, 34):
        d.append(f'<line x1="{xl+2}" y1="{cy+dy}" x2="{xr-2}" y2="{cy+dy}" stroke="{VELD}" stroke-width="1.3"/>')
        d.append(_pijlkop(xl + (xr - xl) * 0.62, cy + dy, 0.0, VELD))
    d.append(_tekst(xl - 5, cy - 64, "+", 12, LADING_PLUS))
    d.append(_tekst(xr + 5, cy - 64, "–", 13, LADING_MIN))

    return _svg(breedte, cel_h, "".join(d))


# ───────────────────────── stroomkringen
DRAAD = "#2f5d50"


def _draad(punten):
    """Een draad langs een rij punten, met rechte hoeken zoals in een schema."""
    d = " ".join(("M" if i == 0 else "L") + f"{x:.1f} {y:.1f}" for i, (x, y) in enumerate(punten))
    return f'<path d="{d}" fill="none" stroke="{DRAAD}" stroke-width="1.6" stroke-linejoin="round"/>'


def _weerstand(cx, cy, label, breed=44, hoog=17, staand=False, kant="rechts"):
    """Het rechthoekje van een weerstand, met zijn waarde ernaast.

    Bij een staande weerstand zegt `kant` aan welke zijde het opschrift komt.
    Dat moet je kiezen: staat de weerstand in de rechterdraad van de kring,
    dan valt een opschrift rechts buiten het kader.
    """
    b, h = (hoog, breed) if staand else (breed, hoog)
    uit = [f'<rect x="{cx-b/2:.1f}" y="{cy-h/2:.1f}" width="{b}" height="{h}" rx="2" '
           f'fill="#ffffff" stroke="{DRAAD}" stroke-width="1.6"/>']
    if label:
        if staand and kant == "links":
            uit.append(_tekst(cx - b / 2 - 6, cy + 4, label, 10, INK, "end"))
        elif staand:
            uit.append(_tekst(cx + b / 2 + 6, cy + 4, label, 10, INK, "start"))
        else:
            uit.append(_tekst(cx, cy - h / 2 - 6, label, 10, INK))
    return "".join(uit)


def _bron(cx, cy, label=None, staand=True):
    """Het symbool van een spanningsbron: een lange dunne en een korte dikke streep."""
    uit = []
    if staand:
        uit.append(f'<line x1="{cx-11}" y1="{cy-4}" x2="{cx+11}" y2="{cy-4}" stroke="{DRAAD}" stroke-width="1.6"/>')
        uit.append(f'<line x1="{cx-6}" y1="{cy+4}" x2="{cx+6}" y2="{cy+4}" stroke="{DRAAD}" stroke-width="3.4"/>')
        if label:
            # rechts van het symbool, binnen de kring: links ervan is er
            # geen plaats meer tot aan de rand van het kader
            uit.append(_tekst(cx + 16, cy + 4, label, 10, INK, "start"))
    else:
        uit.append(f'<line x1="{cx-4}" y1="{cy-11}" x2="{cx-4}" y2="{cy+11}" stroke="{DRAAD}" stroke-width="1.6"/>')
        uit.append(f'<line x1="{cx+4}" y1="{cy-6}" x2="{cx+4}" y2="{cy+6}" stroke="{DRAAD}" stroke-width="3.4"/>')
        if label:
            uit.append(_tekst(cx, cy - 16, label, 10, INK))
    return "".join(uit)


def kringsymbolen(breedte=470):
    r"""De symbolen die in een elektrisch schema terugkomen.

    Een schema toont welke onderdelen met elkaar verbonden zijn, niet hoe lang
    of hoe dik de draden zijn. Wie de symbolen niet kent, kan een schema niet
    lezen, en met woorden alleen leer je ze niet.
    """
    d = []
    vak_b, vak_h = 78, 74
    namen = ["spanningsbron", "weerstand", "lamp", "schakelaar", "ampèremeter", "voltmeter"]
    for i, naam in enumerate(namen):
        kx = (i % 6) * vak_b
        cx, cy = kx + vak_b / 2, 30
        d.append(f'<line x1="{kx+8}" y1="{cy}" x2="{cx-17:.1f}" y2="{cy}" stroke="{DRAAD}" stroke-width="1.6"/>')
        d.append(f'<line x1="{cx+17:.1f}" y1="{cy}" x2="{kx+vak_b-8}" y2="{cy}" stroke="{DRAAD}" stroke-width="1.6"/>')
        if naam == "spanningsbron":
            d.append(_bron(cx, cy, None, staand=False))
        elif naam == "weerstand":
            d.append(_weerstand(cx, cy, None, 34, 15))
        elif naam == "lamp":
            d.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="#ffffff" stroke="{DRAAD}" stroke-width="1.6"/>')
            d.append(f'<line x1="{cx-7.8:.1f}" y1="{cy-7.8:.1f}" x2="{cx+7.8:.1f}" y2="{cy+7.8:.1f}" stroke="{DRAAD}" stroke-width="1.4"/>')
            d.append(f'<line x1="{cx-7.8:.1f}" y1="{cy+7.8:.1f}" x2="{cx+7.8:.1f}" y2="{cy-7.8:.1f}" stroke="{DRAAD}" stroke-width="1.4"/>')
        elif naam == "schakelaar":
            d.append(f'<circle cx="{cx-11}" cy="{cy}" r="2.2" fill="{DRAAD}"/>')
            d.append(f'<circle cx="{cx+11}" cy="{cy}" r="2.2" fill="{DRAAD}"/>')
            d.append(f'<line x1="{cx-11}" y1="{cy}" x2="{cx+9}" y2="{cy-12}" stroke="{DRAAD}" stroke-width="1.6"/>')
        else:
            d.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="#ffffff" stroke="{DRAAD}" stroke-width="1.6"/>')
            d.append(_tekst(cx, cy + 4, "A" if naam == "ampèremeter" else "V", 11, DARK, "middle", True))
        d.append(_tekst(cx, 58, naam, 9.5, DIM))
    return _svg(breedte, 68, "".join(d))


def schakelingen(breedte=470):
    r"""Serie, parallel en de gemengde schakeling van de fiche, als schema.

    De getallen zijn die van de rekenvoorbeelden in de bundel, zodat de
    tekening en de berekening over dezelfde kring gaan.
    """
    cel_b, cel_h = 234, 168
    d = []

    def kader(kx, ky, titel, breed=None):
        breed = breed or cel_b
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{breed-12}" height="{cel_h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + breed / 2, ky + cel_h - 8, titel, 10, DIM, "middle", True))

    def serie(kx, ky):
        l, r = kx + 36, kx + cel_b - 36
        b, o = ky + 32, ky + 108
        d.append(_draad([(l, b), (r, b), (r, o), (l, o), (l, b)]))
        d.append(f'<rect x="{l+28}" y="{b-9}" width="44" height="18" fill="#ffffff"/>')
        d.append(_weerstand(l + 50, b, "4,0 Ω"))
        d.append(f'<rect x="{r-72}" y="{b-9}" width="44" height="18" fill="#ffffff"/>')
        d.append(_weerstand(r - 50, b, "6,0 Ω"))
        d.append(f'<rect x="{l-12}" y="{(b+o)/2-12}" width="24" height="24" fill="#ffffff"/>')
        d.append(_bron(l, (b + o) / 2, "20 V"))

    def parallel(kx, ky):
        # de rechterdraad blijft van de rand: daar staat het opschrift van
        # de rechtse tak
        l, r = kx + 30, kx + cel_b - 58
        b, o = ky + 30, ky + 110
        m = (l + r) / 2 + 20
        d.append(_draad([(l, b), (r, b), (r, o), (l, o), (l, b)]))
        d.append(_draad([(m, b), (m, o)]))
        d.append(f'<rect x="{m-9}" y="{(b+o)/2-22}" width="18" height="44" fill="#ffffff"/>')
        d.append(_weerstand(m, (b + o) / 2, "6,0 Ω", staand=True))
        d.append(f'<rect x="{r-9}" y="{(b+o)/2-22}" width="18" height="44" fill="#ffffff"/>')
        d.append(_weerstand(r, (b + o) / 2, "12 Ω", staand=True))
        d.append(f'<rect x="{l-12}" y="{(b+o)/2-12}" width="24" height="24" fill="#ffffff"/>')
        d.append(_bron(l, (b + o) / 2, "24 V"))

    def gemengd(kx, ky):
        # dit vakje is twee keer zo breed, dus de kring mag ruimer staan
        l, r = kx + 120, kx + cel_b * 2 - 150
        b, o = ky + 30, ky + 110
        m = (l + r) / 2 + 30
        d.append(_draad([(l, b), (r, b), (r, o), (l, o), (l, b)]))
        d.append(_draad([(m, b), (m, o)]))
        # de weerstand in serie staat vóór de splitsing, in de bovenste draad
        d.append(f'<rect x="{l+16}" y="{b-9}" width="44" height="18" fill="#ffffff"/>')
        d.append(_weerstand(l + 38, b, "10 Ω"))
        d.append(f'<rect x="{m-9}" y="{(b+o)/2-22}" width="18" height="44" fill="#ffffff"/>')
        d.append(_weerstand(m, (b + o) / 2, "20 Ω", staand=True))
        d.append(f'<rect x="{r-9}" y="{(b+o)/2-22}" width="18" height="44" fill="#ffffff"/>')
        d.append(_weerstand(r, (b + o) / 2, "20 Ω", staand=True))
        d.append(f'<rect x="{l-12}" y="{(b+o)/2-12}" width="24" height="24" fill="#ffffff"/>')
        d.append(_bron(l, (b + o) / 2, "40 V"))

    kader(0, 0, "serie: één weg")
    serie(0, 0)
    kader(cel_b, 0, "parallel: twee wegen")
    parallel(cel_b, 0)
    kader(0, cel_h, "gemengd: de twee van 20 Ω staan parallel", cel_b * 2)
    gemengd(0, cel_h)
    return _svg(breedte, cel_h * 2, "".join(d))


# ───────────────────────── magnetische velden
NOORD = "#b4452c"   # dezelfde warme kleur als een positieve lading
ZUID = "#2f6d9e"


def magneetvelden(breedte=470):
    r"""De vier veldpatronen die bij magnetisme horen.

    Een staafmagneet, een rechte stroomvoerende draad, een spoel en een
    hoefijzermagneet. Buiten een magneet lopen de veldlijnen van noord naar
    zuid; binnenin lopen ze door, want een magnetische veldlijn is een
    gesloten lus en heeft geen begin of einde.
    """
    import math
    cel_b, cel_h = 234, 186
    VELD = FOREST
    d = []

    def kader(kx, ky, titel):
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{cel_b-12}" height="{cel_h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, ky + cel_h - 8, titel, 10, DIM, "middle", True))

    def staaf(kx, ky):
        cy = ky + 80
        x0, x1 = kx + 78, kx + cel_b - 78
        for boog, kant in ((34, -1), (56, -1), (34, 1), (56, 1)):
            # een lus van de noordpool naar de zuidpool, langs boven of onder
            mx = (x0 + x1) / 2
            pad = (f"M{x1} {cy} C{x1+boog} {cy + kant*boog*0.5:.0f} "
                   f"{mx+boog*0.9:.0f} {cy + kant*boog:.0f} {mx:.0f} {cy + kant*boog:.0f} "
                   f"C{mx-boog*0.9:.0f} {cy + kant*boog:.0f} {x0-boog} {cy + kant*boog*0.5:.0f} "
                   f"{x0} {cy}")
            d.append(f'<path d="{pad}" fill="none" stroke="{VELD}" stroke-width="1.3"/>')
            d.append(_pijlkop(mx, cy + kant * boog, math.pi, VELD))
        d.append(f'<rect x="{x0}" y="{cy-13}" width="{(x1-x0)/2}" height="26" fill="{ZUID}" opacity="0.85"/>')
        d.append(f'<rect x="{(x0+x1)/2}" y="{cy-13}" width="{(x1-x0)/2}" height="26" fill="{NOORD}" opacity="0.85"/>')
        d.append(_tekst(x0 + (x1 - x0) / 4, cy + 4, "Z", 11, "#ffffff", "middle", True))
        d.append(_tekst(x1 - (x1 - x0) / 4, cy + 4, "N", 11, "#ffffff", "middle", True))

    def draad(kx, ky):
        cx, cy = kx + cel_b / 2, ky + 80
        for straal in (22, 38, 54):
            d.append(f'<circle cx="{cx}" cy="{cy}" r="{straal}" fill="none" stroke="{VELD}" stroke-width="1.3"/>')
            # de pijl bovenaan wijst naar links: tegen de klok in, bij een
            # stroom die uit het blad komt
            d.append(_pijlkop(cx, cy - straal, math.pi, VELD))
        d.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#ffffff" stroke="{INK}" stroke-width="1.4"/>')
        d.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="{INK}"/>')
        d.append(_tekst(cx, cy + 74, "stroom uit het blad", 9.5, DIM))

    def spoel(kx, ky):
        cy = ky + 78
        x0, x1 = kx + 56, kx + cel_b - 56
        n = 6
        stap = (x1 - x0) / n
        for i in range(n):
            x = x0 + i * stap
            d.append(f'<ellipse cx="{x+stap/2:.1f}" cy="{cy}" rx="{stap/2.6:.1f}" ry="30" '
                     f'fill="none" stroke="{INK}" stroke-width="1.5"/>')
        for dy in (-13, 0, 13):
            d.append(f'<line x1="{x0+6}" y1="{cy+dy}" x2="{x1-6}" y2="{cy+dy}" stroke="{VELD}" stroke-width="1.3"/>')
            d.append(_pijlkop((x0 + x1) / 2, cy + dy, 0.0, VELD))
        d.append(_tekst(x0 - 14, cy + 4, "Z", 11, ZUID, "middle", True))
        d.append(_tekst(x1 + 14, cy + 4, "N", 11, NOORD, "middle", True))

    def hoefijzer(kx, ky):
        cx, cy = kx + cel_b / 2, ky + 74
        # een U op zijn kop: twee benen met de polen naar elkaar toe
        d.append(f'<path d="M{cx-46} {cy-34} L{cx-46} {cy+22} A46 46 0 0 0 {cx+46} {cy+22} '
                 f'L{cx+46} {cy-34}" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="butt"/>')
        d.append(f'<rect x="{cx-52}" y="{cy-40}" width="13" height="16" fill="{NOORD}"/>')
        d.append(f'<rect x="{cx+39}" y="{cy-40}" width="13" height="16" fill="{ZUID}"/>')
        d.append(_tekst(cx - 46, cy - 48, "N", 10.5, NOORD, "middle", True))
        d.append(_tekst(cx + 46, cy - 48, "Z", 10.5, ZUID, "middle", True))
        # de lijnen lopen door de opening tussen de twee poolvlakken, dus
        # binnen de hoogte van die vlakken (cy-40 tot cy-24)
        for dy in (-37, -32, -27):
            d.append(f'<line x1="{cx-39}" y1="{cy+dy}" x2="{cx+39}" y2="{cy+dy}" stroke="{VELD}" stroke-width="1.3"/>')
            d.append(_pijlkop(cx, cy + dy, 0.0, VELD))

    kader(0, 0, "staafmagneet: van noord naar zuid")
    staaf(0, 0)
    kader(cel_b, 0, "rechte draad: cirkels rond de draad")
    draad(cel_b, 0)
    kader(0, cel_h, "spoel: binnenin nagenoeg homogeen")
    spoel(0, cel_h)
    kader(cel_b, cel_h, "hoefijzer: homogeen tussen de benen")
    hoefijzer(cel_b, cel_h)
    return _svg(breedte, cel_h * 2, "".join(d))


def magneetkracht(breedte=470):
    r"""Drie tekeningen bij de kracht van een magnetisch veld.

    Links de laplacekracht op een draad: het veld het blad in, de stroom naar
    rechts, de kracht naar boven. Rechts twee evenwijdige draden, een keer met
    gelijke en een keer met tegengestelde stroomzin. Onderaan de cirkelbaan van
    een positieve lading in een veld dat uit het blad komt.
    """
    import math
    cel_b, cel_h = 234, 178
    KRACHT = AMBER
    d = []

    def kader(kx, ky, titel, breed=None):
        b = breed or cel_b
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{b-12}" height="{cel_h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + b / 2, ky + cel_h - 8, titel, 10, DIM, "middle", True))

    def kruisje(x, y, r=4.0):
        """Het veld dat het blad in gaat: de pluimen van een wegvliegende pijl."""
        return (f'<line x1="{x-r}" y1="{y-r}" x2="{x+r}" y2="{y+r}" stroke="{DIM}" '
                f'stroke-width="1.2"/>'
                f'<line x1="{x-r}" y1="{y+r}" x2="{x+r}" y2="{y-r}" stroke="{DIM}" '
                f'stroke-width="1.2"/>')

    def stip(x, y):
        """Het veld dat uit het blad komt: de punt van een pijl die naar je toe wijst."""
        return (f'<circle cx="{x}" cy="{y}" r="5" fill="none" stroke="{DIM}" '
                f'stroke-width="1.1"/>'
                f'<circle cx="{x}" cy="{y}" r="1.6" fill="{DIM}"/>')

    # ── 1. de kracht op een draad
    kader(0, 0, "draad in een veld: F staat loodrecht op allebei")
    cy = 104
    # de kruisjes blijven weg waar de draad en de krachtpijl staan
    for ay in (42, 62, 82, 124):
        for ax in range(30, 210, 30):
            if ax == 120 and ay != 124:
                continue
            d.append(kruisje(ax, ay))
    d.append(f'<line x1="22" y1="{cy}" x2="206" y2="{cy}" stroke="{DRAAD}" stroke-width="2.4"/>')
    d.append(_pijlkop(204, cy, 0.0, DRAAD, 6.0))
    d.append(_tekst(196, cy - 9, "I", 11.5, DRAAD, "middle", True))
    d.append(f'<line x1="120" y1="{cy-3}" x2="120" y2="{cy-56}" stroke="{KRACHT}" '
             f'stroke-width="2.2"/>')
    d.append(_pijlkop(120, cy - 56, -math.pi / 2, KRACHT, 6.0))
    d.append(_tekst(132, cy - 50, "F", 11.5, KRACHT, "middle", True))
    d.append(_tekst(117, 28, "B het blad in", 9.5, DIM, "middle"))

    # ── 2. twee evenwijdige draden
    kx = cel_b
    kader(kx, 0, "gelijke zin trekt aan, tegengestelde stoot af")
    for i, (zin, tekst) in enumerate(((1, "aantrekken"), (-1, "afstoten"))):
        bx = kx + 32 + i * 104
        boven, onder = 38, 116
        for dx in (0, 48):
            d.append(f'<line x1="{bx+dx}" y1="{boven}" x2="{bx+dx}" y2="{onder}" '
                     f'stroke="{DRAAD}" stroke-width="2.2"/>')
        d.append(_pijlkop(bx, boven + 4, -math.pi / 2, DRAAD, 5.0))
        if zin == 1:
            d.append(_pijlkop(bx + 48, boven + 4, -math.pi / 2, DRAAD, 5.0))
        else:
            d.append(_pijlkop(bx + 48, onder - 4, math.pi / 2, DRAAD, 5.0))
        my = (boven + onder) / 2
        for kant, x0 in ((1, bx), (-1, bx + 48)):
            richting = kant * zin
            begin = x0 + kant * 5
            eind = begin + richting * 12
            d.append(f'<line x1="{begin}" y1="{my}" x2="{eind}" y2="{my}" '
                     f'stroke="{KRACHT}" stroke-width="2.0"/>')
            d.append(_pijlkop(eind, my, 0.0 if richting > 0 else math.pi, KRACHT, 5.0))
        d.append(_tekst(bx + 24, onder + 18, tekst, 9.5, DIM, "middle", True))

    # ── 3. de cirkelbaan van een lading
    ky = cel_h
    kader(0, ky, "een lading loodrecht in het veld draait rond", cel_b * 2)
    mx, my = 150, ky + 82
    straal = 46
    for ax in range(34, 374, 40):
        for ay in (ky + 34, ky + 72, ky + 110):
            if (ax - mx) ** 2 + (ay - my) ** 2 > (straal + 22) ** 2:
                d.append(stip(ax, ay))
    d.append(f'<circle cx="{mx}" cy="{my}" r="{straal}" fill="none" stroke="{FOREST}" '
             f'stroke-width="1.6"/>')
    # Met B uit het blad draait een positieve lading mét de wijzers mee:
    # F = q v x B wijst dan naar het middelpunt. Draait ze de andere kant op,
    # dan wijst de kracht naar buiten en is er geen cirkel.
    d.append(_pijlkop(mx, my - straal, 0.0, FOREST, 5.5))
    d.append(_pijlkop(mx, my + straal, math.pi, FOREST, 5.5))
    px, py = mx + straal, my
    d.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{LADING_PLUS}"/>')
    d.append(_tekst(px, py + 3.6, "+", 11, "#ffffff", "middle", True))
    d.append(f'<line x1="{px}" y1="{py+10}" x2="{px}" y2="{py+44}" stroke="{DRAAD}" '
             f'stroke-width="2.0"/>')
    d.append(_pijlkop(px, py + 44, math.pi / 2, DRAAD, 5.5))
    d.append(_tekst(px + 11, py + 40, "v", 11.5, DRAAD, "middle", True))
    d.append(f'<line x1="{px-10}" y1="{py}" x2="{px-36}" y2="{py}" stroke="{KRACHT}" '
             f'stroke-width="2.0"/>')
    d.append(_pijlkop(px - 36, py, math.pi, KRACHT, 5.5))
    d.append(_tekst(px - 23, py - 9, "F", 11.5, KRACHT, "middle", True))
    d.append(_tekst(412, ky + 76, "B uit het blad", 9.5, DIM, "middle"))

    return _svg(cel_b * 2, cel_h * 2, "\n".join(d))


def inductie(breedte=470):
    r"""Drie tekeningen bij elektromagnetische inductie.

    Links een magneet die in een spoel geduwd wordt, met de inductiestroom
    die volgens de wet van Lenz een noordpool naar de magneet toe keert.
    Rechts een transformator met zijn twee spoelen op één kern. Onderaan de
    flux en de inductiespanning onder elkaar, zodat je ziet dat de spanning
    de helling van de fluxgrafiek volgt en niet de flux zelf.
    """
    import math
    cel_b, cel_h = 234, 186
    d = []

    def kader(kx, ky, titel, breed=None, hoog=None):
        b = breed or cel_b
        h = hoog or cel_h
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{b-12}" height="{h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + b / 2, ky + h - 8, titel, 10, DIM, "middle", True))

    # ── 1. een magneet in een spoel
    kader(0, 0, "duwen geeft stroom; de spoel duwt terug")
    cy = 92
    # de spoel: zes lussen op een rij
    for i in range(6):
        x = 78 + i * 20
        d.append(f'<ellipse cx="{x}" cy="{cy}" rx="7" ry="30" fill="none" '
                 f'stroke="{DRAAD}" stroke-width="1.6"/>')
    # de aansluitdraden met de stroomzin erin
    d.append(_draad([(78, cy + 30), (72, cy + 46), (186, cy + 46), (186, cy + 30)]))
    d.append(_pijlkop(130, cy + 46, 0.0, DRAAD, 5.0))
    d.append(_tekst(130, cy + 60, "inductiestroom", 9.5, DIM, "middle"))
    # de magneet links ervan, noordpool naar de spoel toe
    mx, my = 26, cy
    d.append(f'<rect x="{mx}" y="{my-11}" width="20" height="22" fill="{ZUID}" opacity="0.85"/>')
    d.append(f'<rect x="{mx+20}" y="{my-11}" width="20" height="22" fill="{NOORD}" opacity="0.85"/>')
    d.append(_tekst(mx + 10, my + 4, "Z", 10, "#ffffff", "middle", True))
    d.append(_tekst(mx + 30, my + 4, "N", 10, "#ffffff", "middle", True))
    d.append(f'<line x1="{mx+44}" y1="{my}" x2="{mx+62}" y2="{my}" stroke="{AMBER}" '
             f'stroke-width="2.0"/>')
    d.append(_pijlkop(mx + 62, my, 0.0, AMBER, 5.5))
    d.append(_tekst(mx + 54, my - 9, "v", 11, AMBER, "middle", True))
    # de pool die de spoel zelf maakt staat naar de magneet toe: dat is de
    # wet van Lenz, de spoel werkt zijn eigen oorzaak tegen
    d.append(_tekst(78, my - 38, "N", 11, NOORD, "middle", True))
    d.append(f'<line x1="78" y1="{my-34}" x2="78" y2="{my-26}" stroke="{NOORD}" '
             f'stroke-width="1.4"/>')

    # ── 2. de transformator
    kx = cel_b
    kader(kx, 0, "transformator: de verhouding van de windingen")
    lx, rx = kx + 62, kx + 160
    boven, onder = 44, 136
    # de gesloten kern
    d.append(f'<rect x="{lx}" y="{boven}" width="{rx-lx}" height="{onder-boven}" rx="4" '
             f'fill="none" stroke="{DIM}" stroke-width="9" opacity="0.35"/>')
    for i in range(4):
        y = boven + 16 + i * 18
        d.append(f'<ellipse cx="{lx}" cy="{y}" rx="16" ry="6" fill="none" stroke="{DRAAD}" '
                 f'stroke-width="1.6"/>')
    for i in range(8):
        y = boven + 10 + i * 10
        d.append(f'<ellipse cx="{rx}" cy="{y}" rx="16" ry="3.5" fill="none" stroke="{DRAAD}" '
                 f'stroke-width="1.4"/>')
    d.append(_tekst(lx - 28, boven + 50, "N₁", 11.5, DRAAD, "middle", True))
    d.append(_tekst(lx - 28, boven + 66, "U₁", 10.5, DIM, "middle"))
    d.append(_tekst(rx + 28, boven + 50, "N₂", 11.5, DRAAD, "middle", True))
    d.append(_tekst(rx + 28, boven + 66, "U₂", 10.5, DIM, "middle"))
    d.append(_tekst(kx + cel_b / 2, 30, "meer windingen is meer spanning", 9.5, DIM, "middle"))

    # ── 3. de flux en de spanning onder elkaar
    ky = cel_h
    hoog = 196
    kader(0, ky, "de spanning volgt de helling, niet de flux zelf", cel_b * 2, hoog)
    x0, x1 = 54, 430

    def as_stelsel(by, naam, eenheid):
        d.append(f'<line x1="{x0}" y1="{by}" x2="{x1}" y2="{by}" stroke="{DIM}" '
                 f'stroke-width="1.1"/>')
        d.append(f'<line x1="{x0}" y1="{by-34}" x2="{x0}" y2="{by+16}" stroke="{DIM}" '
                 f'stroke-width="1.1"/>')
        d.append(_pijlkop(x1, by, 0.0, DIM, 4.0))
        d.append(_tekst(x1 - 4, by + 13, "t", 9.5, DIM, "middle"))
        d.append(_tekst(x0 - 20, by - 28, naam, 10.5, INK, "middle", True))
        d.append(_tekst(x0 - 20, by - 16, eenheid, 8.5, DIM, "middle"))

    # de flux: omhoog, vlak, omlaag
    fy = ky + 60
    as_stelsel(fy, "Φ", "(Wb)")
    p1, p2, p3 = 160, 270, 390
    d.append(f'<path d="M{x0+6} {fy} L{p1} {fy-30} L{p2} {fy-30} L{p3} {fy}" fill="none" '
             f'stroke="{FOREST}" stroke-width="2.0"/>')
    for x, naam in ((110, "stijgt"), (215, "vlak"), (330, "daalt")):
        d.append(_tekst(x, fy + 13, naam, 9, DIM, "middle"))
    # de spanning: constant, nul, tegengesteld
    uy = ky + 138
    as_stelsel(uy, "U", "(V)")
    d.append(f'<path d="M{x0+6} {uy+22} L{p1} {uy+22} L{p1} {uy} L{p2} {uy} L{p2} {uy-22} '
             f'L{p3} {uy-22} L{p3} {uy}" fill="none" stroke="{AMBER}" stroke-width="2.0"/>')
    for x, y, naam in ((110, uy - 9, "een vaste waarde"), (215, uy - 9, "nul"),
                       (330, uy + 15, "andere zin")):
        d.append(_tekst(x, y, naam, 9, DIM, "middle"))
    for x in (p1, p2, p3):
        d.append(f'<line x1="{x}" y1="{fy-38}" x2="{x}" y2="{uy+26}" stroke="{BORDER}" '
                 f'stroke-width="1" stroke-dasharray="3 3"/>')

    return _svg(cel_b * 2, cel_h + hoog, "\n".join(d))


def krachtenbeeld(breedte=470):
    r"""Drie tekeningen bij statica.

    Een blok op een helling met de zwaartekracht ontbonden, twee krachten
    die loodrecht op elkaar staan met hun resultante, en het moment van een
    kracht met zijn krachtarm.
    """
    import math
    cel_b, cel_h = 234, 186
    KRACHT = AMBER
    ONTBIND = FOREST
    d = []

    def kader(kx, ky, titel, breed=None, hoog=None):
        b = breed or cel_b
        h = hoog or cel_h
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{b-12}" height="{h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + b / 2, ky + h - 8, titel, 10, DIM, "middle", True))

    def pijl(x0, y0, x1, y1, kleur, breed=2.0, stippel=False):
        extra = ' stroke-dasharray="5 3"' if stippel else ""
        d.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                 f'stroke="{kleur}" stroke-width="{breed}"{extra}/>')
        d.append(_pijlkop(x1, y1, math.atan2(y1 - y0, x1 - x0), kleur, 5.5))

    # ── 1. een blok op een helling
    kader(0, 0, "op een helling splits je de zwaartekracht")
    ax, ay, bx = 24, 134, 206
    hoogte = 62
    d.append(f'<path d="M{ax} {ay} L{bx} {ay} L{bx} {ay-hoogte} Z" fill="{BORDER}" '
             f'opacity="0.45" stroke="{DIM}" stroke-width="1.2"/>')
    hoek = math.atan2(hoogte, bx - ax)
    c, s = math.cos(hoek), math.sin(hoek)
    # het blokje staat op de schuine zijde: langs de helling is (c, -s),
    # de buitennormaal is (-s, -c)
    t = 0.46
    px, py = ax + (bx - ax) * t, ay - hoogte * t
    halfb, hoog = 15, 20
    punten = []
    for u, v in ((-halfb, 0), (halfb, 0), (halfb, hoog), (-halfb, hoog)):
        punten.append(f"{px + u*c - v*s:.1f},{py - u*s - v*c:.1f}")
    d.append(f'<polygon points="{" ".join(punten)}" fill="{PAPER}" stroke="{INK}" '
             f'stroke-width="1.3"/>')
    gx, gy = px - (hoog / 2) * s, py - (hoog / 2) * c
    # de zwaartekracht, recht omlaag
    pijl(gx, gy, gx, gy + 42, KRACHT)
    d.append(_tekst(gx + 2, gy + 56, "Fz", 10.5, KRACHT, "middle", True))
    # haar twee componenten, gestippeld
    pijl(gx, gy, gx - 30 * c, gy + 30 * s, ONTBIND, 1.6, True)
    d.append(_tekst(gx - 30 * c - 2, gy + 30 * s + 14, "langs", 9, ONTBIND, "middle"))
    pijl(gx, gy, gx + 26 * s, gy + 26 * c, ONTBIND, 1.6, True)
    d.append(_tekst(gx + 26 * s + 30, gy + 26 * c + 4, "loodrecht", 9, ONTBIND, "middle"))
    # de normaalkracht heft die loodrechte component op
    pijl(gx, gy, gx - 26 * s, gy - 26 * c, DRAAD)
    d.append(_tekst(gx - 26 * s - 14, gy - 26 * c - 2, "FN", 10.5, DRAAD, "middle", True))
    d.append(_tekst(ax + 24, ay - 6, "α", 11, DIM, "middle", True))

    # ── 2. twee krachten samenstellen
    kx = cel_b
    kader(kx, 0, "loodrecht op elkaar: Pythagoras")
    ox, oy = kx + 58, 126
    f1, f2 = 92, 69           # 8 N en 6 N, op schaal
    pijl(ox, oy, ox + f1, oy, KRACHT)
    d.append(_tekst(ox + f1 / 2, oy + 16, "8 N", 10.5, KRACHT, "middle", True))
    pijl(ox, oy, ox, oy - f2, KRACHT)
    d.append(_tekst(ox - 17, oy - f2 / 2, "6 N", 10.5, KRACHT, "middle", True))
    d.append(f'<path d="M{ox+f1} {oy} L{ox+f1} {oy-f2} L{ox} {oy-f2}" fill="none" '
             f'stroke="{BORDER}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    pijl(ox, oy, ox + f1, oy - f2, ONTBIND, 2.4)
    d.append(_tekst(ox + f1 + 2, oy - f2 - 10, "10 N", 10.5, ONTBIND, "middle", True))
    d.append(_tekst(kx + cel_b / 2, 36, "de diagonaal van de rechthoek", 9.5, DIM, "middle"))

    # ── 3. het moment van een kracht
    ky = cel_h
    kader(0, ky, "moment: kracht maal de loodrechte afstand", cel_b * 2)
    dx0, dy0 = 100, ky + 118
    arm_d = 150
    ex, ey = dx0 + arm_d, dy0
    d.append(f'<line x1="{dx0}" y1="{dy0}" x2="{ex}" y2="{ey}" stroke="{INK}" '
             f'stroke-width="3"/>')
    d.append(f'<circle cx="{dx0}" cy="{dy0}" r="5" fill="{INK}"/>')
    d.append(_tekst(dx0 - 4, dy0 + 20, "draaipunt", 9.5, DIM, "middle"))
    a = math.radians(25)
    ca, sa = math.cos(a), math.sin(a)
    # de kracht grijpt aan op het uiteinde en wijst schuin naar beneden
    pijl(ex, ey, ex + 58 * ca, ey + 58 * sa, KRACHT, 2.2)
    d.append(_tekst(ex + 58 * ca + 14, ey + 58 * sa, "F", 11.5, KRACHT, "middle", True))
    # haar werklijn, doorgetrokken naar de andere kant
    d.append(f'<line x1="{ex}" y1="{ey}" x2="{ex-140*ca:.1f}" y2="{ey-140*sa:.1f}" '
             f'stroke="{KRACHT}" stroke-width="1" stroke-dasharray="4 3" opacity="0.7"/>')
    # de loodlijn uit het draaipunt op die werklijn: dat is de krachtarm
    fx, fy = ex - arm_d * ca * ca, ey - arm_d * ca * sa
    d.append(f'<line x1="{dx0}" y1="{dy0}" x2="{fx:.1f}" y2="{fy:.1f}" stroke="{ONTBIND}" '
             f'stroke-width="2" stroke-dasharray="5 3"/>')
    d.append(_tekst((dx0 + fx) / 2 - 16, (dy0 + fy) / 2 + 2, "arm", 10, ONTBIND, "middle", True))
    # de afstand d langs de stang
    d.append(f'<line x1="{dx0}" y1="{dy0+9}" x2="{ex}" y2="{ey+9}" stroke="{DIM}" '
             f'stroke-width="1" stroke-dasharray="3 3"/>')
    d.append(_tekst((dx0 + ex) / 2, dy0 + 22, "d", 10.5, DIM, "middle", True))
    d.append(_tekst(ex + 20, ey + 13, "α", 11, DIM, "middle", True))
    d.append(_tekst(352, ky + 60, "M = F · d · sin α", 11.5, INK, "middle", True))
    d.append(_tekst(352, ky + 78, "de arm is d · sin α", 9.5, DIM, "middle"))
    d.append(_tekst(352, ky + 100, "gaat de werklijn door het", 9.5, DIM, "middle"))
    d.append(_tekst(352, ky + 113, "draaipunt, dan is de arm nul", 9.5, DIM, "middle"))
    d.append(_tekst(352, ky + 126, "en het moment ook", 9.5, DIM, "middle"))

    return _svg(cel_b * 2, cel_h * 2, "\n".join(d))


def newtonkrachten(breedte=470):
    r"""Twee tekeningen bij de wetten van Newton.

    Links een vrijlichaamsschema van een kist die geduwd wordt, met de
    resulterende kracht eronder. Rechts een actie-reactiepaar, waarbij de
    twee krachten op verschillende lichamen aangrijpen en elkaar dus niet
    opheffen.
    """
    import math
    cel_b, cel_h = 234, 196
    KRACHT = AMBER
    d = []

    def kader(kx, ky, titel):
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{cel_b-12}" height="{cel_h-28}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, ky + cel_h - 8, titel, 10, DIM, "middle", True))

    def pijl(x0, y0, x1, y1, kleur, breed=2.0):
        d.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                 f'stroke="{kleur}" stroke-width="{breed}"/>')
        d.append(_pijlkop(x1, y1, math.atan2(y1 - y0, x1 - x0), kleur, 5.5))

    # ── 1. het vrijlichaamsschema van een geduwde kist
    kader(0, 0, "alle krachten op één lichaam: tel ze op")
    vloer = 108
    d.append(f'<line x1="18" y1="{vloer}" x2="216" y2="{vloer}" stroke="{DIM}" '
             f'stroke-width="1.6"/>')
    kb, kh = 38, 30
    kxl, kxr = 98, 98 + kb
    d.append(f'<rect x="{kxl}" y="{vloer-kh}" width="{kb}" height="{kh}" rx="2" '
             f'fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/>')
    mx, my = kxl + kb / 2, vloer - kh / 2
    # elke pijl vertrekt aan de rand van de kist, met haar opschrift erbuiten
    pijl(kxr, my, kxr + 44, my, KRACHT)
    d.append(_tekst(kxr + 50, my + 4, "20 N", 9.5, KRACHT, "start", True))
    pijl(kxl, my, kxl - 30, my, FOREST)
    d.append(_tekst(kxl - 36, my + 4, "5 N", 9.5, FOREST, "end", True))
    pijl(mx, vloer, mx, vloer + 28, KRACHT)
    d.append(_tekst(mx + 8, vloer + 26, "Fz", 9.5, KRACHT, "start", True))
    pijl(mx, vloer - kh, mx, vloer - kh - 28, DRAAD)
    d.append(_tekst(mx + 8, vloer - kh - 24, "FN", 9.5, DRAAD, "start", True))
    d.append(_tekst(kxr + 50, my - 8, "duwen", 8.5, DIM, "start"))
    d.append(_tekst(kxl - 36, my - 8, "wrijving", 8.5, DIM, "end"))
    d.append(_tekst(117, 152, "omhoog en omlaag heffen elkaar op", 9, DIM, "middle"))
    pijl(62, 166, 102, 166, FOREST, 2.6)
    d.append(_tekst(110, 170, "Fres = 15 N", 10, FOREST, "start", True))

    # ── 2. actie en reactie
    kx = cel_b
    kader(kx, 0, "actie en reactie: twee lichamen, geen evenwicht")
    grond = 112
    d.append(f'<line x1="{kx+18}" y1="{grond}" x2="{kx+216}" y2="{grond}" stroke="{DIM}" '
             f'stroke-width="1.6"/>')
    d.append(f'<rect x="{kx+180}" y="{grond-70}" width="22" height="70" fill="{BORDER}" '
             f'stroke="{DIM}" stroke-width="1.2"/>')
    d.append(_tekst(kx + 191, grond + 14, "muur", 9, DIM, "middle"))
    d.append(f'<rect x="{kx+40}" y="{grond-48}" width="32" height="48" rx="3" '
             f'fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/>')
    d.append(_tekst(kx + 56, grond + 14, "jij", 9, DIM, "middle"))
    # jouw kracht grijpt aan op de muur, de hare op jou; de opschriften staan
    # elk aan de kant waar hun eigen pijl naartoe wijst
    pijl(kx + 158, grond - 46, kx + 180, grond - 46, KRACHT, 2.2)
    d.append(_tekst(kx + 152, grond - 50, "jij op de muur", 8.5, KRACHT, "end"))
    d.append(_tekst(kx + 152, grond - 39, "200 N", 9, KRACHT, "end", True))
    pijl(kx + 94, grond - 16, kx + 72, grond - 16, DRAAD, 2.2)
    d.append(_tekst(kx + 124, grond - 24, "de muur op jou", 8.5, DRAAD, "middle"))
    d.append(_tekst(kx + 124, grond - 13, "200 N", 9, DRAAD, "middle", True))
    d.append(_tekst(kx + cel_b / 2, grond + 36, "even groot en tegengesteld,", 9.5, DIM, "middle"))
    d.append(_tekst(kx + cel_b / 2, grond + 48, "maar elk op een ánder lichaam", 9.5, DIM, "middle"))

    return _svg(cel_b * 2, cel_h, "\n".join(d))


def bewegingsgrafieken(breedte=470):
    r"""De zes bewegingsgrafieken van een ERB en van een EVRB.

    Bovenaan de drie grafieken van een eenparig rechtlijnige beweging, onderaan
    dezelfde drie voor een eenparig veranderlijke beweging. Onder elke
    v(t)-grafiek staat de oppervlakte ingekleurd, want dat is de verplaatsing;
    dat verband is net wat je op een grafiek moet kunnen zien.
    """
    import math
    cel_b, cel_h = 156, 150
    d = []

    def paneel(px, py, tag, as_naam, onder):
        d.append(f'<rect x="{px+5}" y="{py+4}" width="{cel_b-10}" height="{cel_h-30}" rx="7" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        ox, oy, top = px + 28, py + 92, py + 20
        rechts = px + cel_b - 18
        d.append(f'<line x1="{ox}" y1="{top}" x2="{ox}" y2="{oy+6}" stroke="{DIM}" '
                 f'stroke-width="1.3"/>')
        d.append(f'<line x1="{ox-6}" y1="{oy}" x2="{rechts}" y2="{oy}" stroke="{DIM}" '
                 f'stroke-width="1.3"/>')
        d.append(_pijlkop(rechts, oy, 0.0, DIM, 4.0))
        d.append(_pijlkop(ox, top, -math.pi / 2, DIM, 4.0))
        d.append(_tekst(rechts - 2, oy + 13, "t", 9.5, DIM, "middle"))
        d.append(_tekst(ox - 10, top + 4, as_naam, 9.5, DIM, "middle"))
        d.append(_tekst(px + 14, py + 16, tag, 8.5, DARK, "start", True))
        d.append(_tekst(px + cel_b / 2, py + cel_h - 10, onder, 9, DIM, "middle"))
        return ox, oy, top, rechts

    # ── bovenste rij: de eenparig rechtlijnige beweging
    ox, oy, top, rechts = paneel(0, 0, "ERB", "x", "rechte: de helling is v")
    d.append(f'<line x1="{ox+4}" y1="{oy-12}" x2="{rechts-10}" y2="{top+12}" '
             f'stroke="{FOREST}" stroke-width="2.2"/>')

    ox, oy, top, rechts = paneel(cel_b, 0, "ERB", "v", "vlak: de opp. is de weg")
    vy = oy - 42
    d.append(f'<rect x="{ox+1}" y="{vy}" width="{rechts-10-ox}" height="{oy-vy}" '
             f'fill="{AMBER}" fill-opacity="0.16"/>')
    d.append(f'<line x1="{ox+1}" y1="{vy}" x2="{rechts-10}" y2="{vy}" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')
    d.append(_tekst((ox + rechts - 10) / 2, oy - 16, "v maal t", 9, AMBER, "middle", True))

    ox, oy, top, rechts = paneel(cel_b * 2, 0, "ERB", "a", "op de as: a blijft nul")
    d.append(f'<line x1="{ox+1}" y1="{oy-1.5}" x2="{rechts-10}" y2="{oy-1.5}" '
             f'stroke="{FOREST}" stroke-width="2.4"/>')
    d.append(_tekst((ox + rechts - 10) / 2, oy - 10, "a is 0", 9, FOREST, "middle", True))

    # ── onderste rij: de eenparig veranderlijke rechtlijnige beweging
    ry = cel_h
    ox, oy, top, rechts = paneel(0, ry, "EVRB", "x", "parabool: steeds steiler")
    punten = []
    for i in range(25):
        f = i / 24
        punten.append(f"{ox + 2 + f * (rechts - 12 - ox):.1f},"
                      f"{oy - 8 - (oy - 8 - (top + 10)) * f * f:.1f}")
    d.append(f'<polyline points="{" ".join(punten)}" fill="none" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')

    ox, oy, top, rechts = paneel(cel_b, ry, "EVRB", "v", "schuin: de helling is a")
    ex, ey = rechts - 10, top + 14
    d.append(f'<path d="M{ox+1} {oy} L{ex} {ey} L{ex} {oy} Z" fill="{AMBER}" '
             f'fill-opacity="0.16"/>')
    d.append(f'<line x1="{ox+1}" y1="{oy}" x2="{ex}" y2="{ey}" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')
    d.append(_tekst(ox + 92, oy - 13, "halve opp.", 9, AMBER, "middle", True))

    ox, oy, top, rechts = paneel(cel_b * 2, ry, "EVRB", "a", "vlak: a blijft gelijk")
    ay = oy - 40
    d.append(f'<line x1="{ox+1}" y1="{ay}" x2="{rechts-10}" y2="{ay}" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')
    d.append(_tekst((ox + rechts - 10) / 2, ay - 8, "a is constant", 9, FOREST, "middle", True))

    return _svg(cel_b * 3, cel_h * 2, "\n".join(d))


def worpbaan(breedte=470):
    r"""Twee tekeningen bij de horizontale worp.

    Links de baan zelf, met op twee plaatsen de snelheid ontbonden: vx blijft
    even lang, vy wordt langer, en samen staan ze raaklijnig aan de baan.
    Rechts de klassieke proef: een bal die je gewoon laat vallen en een bal
    die je horizontaal wegschiet staan op elk ogenblik even hoog.
    """
    import math
    cel_b, cel_h = 234, 206
    d = []

    def kader(kx, ky, titel):
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{cel_b-12}" height="{cel_h-30}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, ky + cel_h - 9, titel, 10, DIM, "middle", True))

    def pijl(x0, y0, x1, y1, kleur, breed=1.8, maat=4.6):
        d.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                 f'stroke="{kleur}" stroke-width="{breed}"/>')
        d.append(_pijlkop(x1, y1, math.atan2(y1 - y0, x1 - x0), kleur, maat))

    # ── 1. de baan, met de snelheid ontbonden
    kader(0, 0, "vx blijft, vy groeit, samen raaklijnig")
    x0, y0 = 40, 40
    xe, ye = 206, 142
    k = (ye - y0) / (xe - x0) ** 2
    d.append(f'<rect x="14" y="{y0}" width="{x0-14}" height="9" fill="{BORDER}" '
             f'stroke="{DIM}" stroke-width="1.1"/>')
    d.append(f'<line x1="14" y1="{ye+9}" x2="218" y2="{ye+9}" stroke="{DIM}" '
             f'stroke-width="1.5"/>')
    punten = [f"{x0 + i / 40 * (xe - x0):.1f},{y0 + k * (i / 40 * (xe - x0)) ** 2:.1f}"
              for i in range(41)]
    d.append(f'<polyline points="{" ".join(punten)}" fill="none" stroke="{FOREST}" '
             f'stroke-width="2.0" stroke-dasharray="1 0"/>')
    # de snelheid op twee plaatsen: horizontaal even lang, verticaal steeds langer
    for f, vy_lang, naam in ((0.42, 20, False), (0.78, 38, True)):
        px = x0 + f * (xe - x0)
        py = y0 + k * (px - x0) ** 2
        d.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.4" fill="{DARK}"/>')
        pijl(px, py, px + 30, py, FOREST)
        pijl(px, py, px, py + vy_lang, AMBER)
        pijl(px, py, px + 30, py + vy_lang, DARK, 2.2, 5.2)
        if naam:
            d.append(_tekst(px + 16, py - 5, "vx", 9, FOREST, "middle", True))
            d.append(_tekst(px - 9, py + vy_lang / 2, "vy", 9, AMBER, "middle", True))
            d.append(_tekst(px + 36, py + vy_lang - 4, "v", 9.5, DARK, "start", True))
    d.append(_tekst(x0 + 2, y0 - 8, "v0", 9, FOREST, "start", True))
    pijl(x0, y0 - 4, x0 + 26, y0 - 4, FOREST)

    # ── 2. vallen en wegschieten: altijd even hoog
    kx = cel_b
    kader(kx, 0, "even hoog op elk ogenblik")
    bx, by = kx + 46, 36
    d.append(f'<line x1="{kx+16}" y1="{by-12}" x2="{kx+16}" y2="{by+120}" stroke="{DIM}" '
             f'stroke-width="1.5"/>')
    d.append(f'<line x1="{kx+16}" y1="{by+120}" x2="{kx+218}" y2="{by+120}" stroke="{DIM}" '
             f'stroke-width="1.5"/>')
    hoogtes = [0, 13, 52, 117]
    schuif = [0, 38, 76, 114]
    for i, (h, s) in enumerate(zip(hoogtes, schuif)):
        y = by + h
        if not i:
            # op t = 0 liggen de twee ballen op elkaar; één bolletje volstaat
            d.append(f'<circle cx="{bx}" cy="{y}" r="4.2" fill="{PAPER}" stroke="{DARK}" '
                     f'stroke-width="1.6"/>')
            continue
        d.append(f'<line x1="{bx}" y1="{y}" x2="{bx+s}" y2="{y}" stroke="{DIM}" '
                 f'stroke-width="0.9" stroke-dasharray="3 3"/>')
        d.append(f'<circle cx="{bx}" cy="{y}" r="4.2" fill="{PAPER}" stroke="{LADING_MIN}" '
                 f'stroke-width="1.6"/>')
        d.append(f'<circle cx="{bx+s}" cy="{y}" r="4.2" fill="{PAPER}" stroke="{AMBER}" '
                 f'stroke-width="1.6"/>')
    d.append(_tekst(bx - 8, by - 10, "valt", 9, LADING_MIN, "middle", True))
    d.append(_tekst(bx + 40, by - 10, "weggeschoten", 9, AMBER, "start", True))
    d.append(_tekst(kx + cel_b / 2, by + 140, "dezelfde valtijd, een andere dracht",
                    9.5, DIM, "middle"))

    return _svg(cel_b * 2, cel_h, "\n".join(d))


def cirkelbeweging(breedte=470):
    r"""Twee tekeningen bij de cirkelbeweging en de gravitatie.

    Links een eenparig cirkelvormige beweging: de snelheid raakt aan de
    cirkel, de versnelling wijst naar het middelpunt, en die twee staan
    loodrecht op elkaar. Rechts een satelliet, waar de gravitatiekracht
    precies de rol van middelpuntzoekende kracht speelt.
    """
    import math
    cel_b, cel_h = 234, 212
    d = []

    def kader(kx, ky, titel):
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{cel_b-12}" height="{cel_h-30}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, ky + cel_h - 9, titel, 10, DIM, "middle", True))

    def pijl(x0, y0, x1, y1, kleur, breed=2.0, maat=5.0):
        d.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                 f'stroke="{kleur}" stroke-width="{breed}"/>')
        d.append(_pijlkop(x1, y1, math.atan2(y1 - y0, x1 - x0), kleur, maat))

    # ── 1. de eenparig cirkelvormige beweging
    kader(0, 0, "v raakt aan de cirkel, a wijst naar binnen")
    mx, my, straal = 112, 98, 58
    d.append(f'<circle cx="{mx}" cy="{my}" r="{straal}" fill="none" stroke="{DIM}" '
             f'stroke-width="1.2" stroke-dasharray="4 4"/>')
    d.append(f'<circle cx="{mx}" cy="{my}" r="2.6" fill="{DIM}"/>')
    hoek = -math.radians(45)
    bx, by = mx + straal * math.cos(hoek), my + straal * math.sin(hoek)
    # de straal, met haar naam halverwege
    d.append(f'<line x1="{mx}" y1="{my}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{DIM}" '
             f'stroke-width="1.1"/>')
    d.append(_tekst((mx + bx) / 2 + 9, (my + by) / 2 + 10, "r", 9.5, DIM, "middle", True))
    d.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="5" fill="{DARK}"/>')
    # v staat loodrecht op de straal, a wijst naar het middelpunt
    vx, vy = -math.sin(hoek), math.cos(hoek)
    pijl(bx, by, bx + vx * 46, by + vy * 46, FOREST)
    d.append(_tekst(bx + vx * 54, by + vy * 54 + 4, "v", 10, FOREST, "middle", True))
    ax, ay = (mx - bx) / straal, (my - by) / straal
    pijl(bx, by, bx + ax * 34, by + ay * 34, AMBER)
    d.append(_tekst(bx + ax * 30 - 2, by + ay * 30 - 7, "a", 10, AMBER, "middle", True))
    # de omloopzin
    d.append(f'<path d="M{mx-20} {my-straal-6} A 24 24 0 0 1 {mx+20} {my-straal-6}" '
             f'fill="none" stroke="{DIM}" stroke-width="1.3"/>')
    d.append(_pijlkop(mx + 20, my - straal - 6, 0.9, DIM, 4.4))
    d.append(_tekst(mx, my - straal - 20, "één ronde duurt T", 9, DIM, "middle"))
    # het hoekje tussen v en a: die twee staan loodrecht op elkaar
    h1x, h1y = bx + vx * 9, by + vy * 9
    h2x, h2y = h1x + ax * 9, h1y + ay * 9
    h3x, h3y = bx + ax * 9, by + ay * 9
    d.append(f'<polyline points="{h1x:.1f},{h1y:.1f} {h2x:.1f},{h2y:.1f} {h3x:.1f},{h3y:.1f}" '
             f'fill="none" stroke="{DIM}" stroke-width="1.0"/>')
    d.append(_tekst(mx, my + straal + 20, "v en a staan loodrecht op elkaar", 9.5, DIM, "middle"))

    # ── 2. de satelliet
    kx = cel_b
    kader(kx, 0, "bij een satelliet is Fg de kracht naar binnen")
    ax0, ay0, aarde = kx + 112, 100, 23
    baan = 64
    d.append(f'<circle cx="{ax0}" cy="{ay0}" r="{baan}" fill="none" stroke="{DIM}" '
             f'stroke-width="1.1" stroke-dasharray="4 4"/>')
    # het radiale veld: korte pijlen die naar de planeet wijzen
    for i in range(8):
        h = i * math.pi / 4 + math.pi / 8
        c, s = math.cos(h), math.sin(h)
        pijl(ax0 + c * (aarde + 24), ay0 + s * (aarde + 24),
             ax0 + c * (aarde + 6), ay0 + s * (aarde + 6), DRAAD, 1.2, 3.6)
    d.append(f'<circle cx="{ax0}" cy="{ay0}" r="{aarde}" fill="{BORDER}" stroke="{DARK}" '
             f'stroke-width="1.4"/>')
    d.append(_tekst(ax0, ay0 + 4, "M", 10.5, DARK, "middle", True))
    hoek2 = -math.radians(50)
    sx, sy = ax0 + baan * math.cos(hoek2), ay0 + baan * math.sin(hoek2)
    d.append(f'<rect x="{sx-5:.1f}" y="{sy-5:.1f}" width="10" height="10" rx="1.5" '
             f'fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/>')
    vx2, vy2 = -math.sin(hoek2), math.cos(hoek2)
    pijl(sx, sy, sx + vx2 * 40, sy + vy2 * 40, FOREST)
    d.append(_tekst(sx + vx2 * 48, sy + vy2 * 48 + 4, "v", 10, FOREST, "middle", True))
    ax2, ay2 = (ax0 - sx) / baan, (ay0 - sy) / baan
    pijl(sx, sy, sx + ax2 * 30, sy + ay2 * 30, AMBER)
    d.append(_tekst(sx + ax2 * 15 - ay2 * 14, sy + ay2 * 15 + ax2 * 14 + 3, "Fg", 10,
                    AMBER, "middle", True))
    d.append(_tekst(kx + cel_b / 2, 176, "Fg is hier de middelpuntzoekende kracht",
                    9.5, DIM, "middle"))

    return _svg(cel_b * 2, cel_h, "\n".join(d))


def arbeid_energie(breedte=470):
    r"""Twee tekeningen bij arbeid, energie en vermogen.

    Links een F(x)-grafiek waarvan de oppervlakte de arbeid is, ook bij een
    kracht die onderweg verandert. Rechts een kar die van een helling rolt,
    met balkjes die laten zien hoe Ep in Ek overgaat.
    """
    import math
    cel_b, cel_h = 234, 210
    d = []

    def kader(kx, ky, titel):
        d.append(f'<rect x="{kx+6}" y="{ky+4}" width="{cel_b-12}" height="{cel_h-30}" rx="8" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        d.append(_tekst(kx + cel_b / 2, ky + cel_h - 9, titel, 10, DIM, "middle", True))

    # ── 1. de oppervlakte onder F(x) is de arbeid
    kader(0, 0, "de oppervlakte onder F(x) is W")
    ox, oy, top, rechts = 34, 134, 28, 210
    d.append(f'<line x1="{ox}" y1="{top}" x2="{ox}" y2="{oy+6}" stroke="{DIM}" '
             f'stroke-width="1.3"/>')
    d.append(f'<line x1="{ox-6}" y1="{oy}" x2="{rechts}" y2="{oy}" stroke="{DIM}" '
             f'stroke-width="1.3"/>')
    d.append(_pijlkop(rechts, oy, 0.0, DIM, 4.2))
    d.append(_pijlkop(ox, top, -math.pi / 2, DIM, 4.2))
    d.append(_tekst(rechts - 4, oy + 14, "x", 10, DIM, "middle"))
    d.append(_tekst(ox - 12, top + 5, "F", 10, DIM, "middle"))
    # een kracht die eerst vast is en daarna lineair groeit
    x1, x2, x3 = ox + 10, ox + 80, ox + 150
    f1, f2 = oy - 38, oy - 86
    d.append(f'<path d="M{x1} {oy} L{x1} {f1} L{x2} {f1} L{x3} {f2} L{x3} {oy} Z" '
             f'fill="{AMBER}" fill-opacity="0.18" stroke="none"/>')
    d.append(f'<polyline points="{x1},{f1} {x2},{f1} {x3},{f2}" fill="none" '
             f'stroke="{FOREST}" stroke-width="2.2"/>')
    d.append(_tekst((x1 + x3) / 2, oy - 22, "W", 12, AMBER, "middle", True))
    d.append(_tekst(117, 160, "vaste kracht: W = F x", 9.5, DIM, "middle"))
    d.append(_tekst(117, 173, "veranderlijke kracht: de oppervlakte", 9.5, DIM, "middle"))

    # ── 2. van Ep naar Ek
    kx = cel_b
    kader(kx, 0, "Ep gaat over in Ek, samen blijft het gelijk")
    hx0, hy0 = kx + 32, 42
    hx1, hy1 = kx + 150, 118
    d.append(f'<path d="M{hx0} {hy0} Q {hx0+56} {hy0+58} {hx1} {hy1} L{kx+206} {hy1}" '
             f'fill="none" stroke="{DIM}" stroke-width="1.8"/>')
    d.append(f'<line x1="{hx0}" y1="{hy1}" x2="{hx0}" y2="{hy0}" stroke="{DIM}" '
             f'stroke-width="0.9" stroke-dasharray="3 3"/>')
    d.append(_tekst(hx0 - 10, (hy0 + hy1) / 2, "h", 9.5, DIM, "middle", True))
    # drie balkjes: boven, halverwege en beneden
    def meter(bx, by, deel, naam):
        br, bh = 15, 34
        d.append(f'<rect x="{bx}" y="{by-bh}" width="{br}" height="{bh}" fill="{PAPER}" '
                 f'stroke="{BORDER}" stroke-width="1"/>')
        hoog = bh * deel
        d.append(f'<rect x="{bx}" y="{by-bh}" width="{br}" height="{hoog:.1f}" '
                 f'fill="{DRAAD}" fill-opacity="0.5"/>')
        d.append(f'<rect x="{bx}" y="{by-bh+hoog:.1f}" width="{br}" height="{bh-hoog:.1f}" '
                 f'fill="{AMBER}" fill-opacity="0.5"/>')
        d.append(_tekst(bx + br / 2, by + 11, naam, 8.5, DIM, "middle"))
    d.append(f'<circle cx="{hx0}" cy="{hy0-6}" r="5" fill="{DARK}"/>')
    d.append(f'<circle cx="{hx1}" cy="{hy1-6}" r="5" fill="{DARK}"/>')
    # de drie balkjes staan op één rij onder de helling, zodat ze de baan niet raken
    meter(kx + 44, 158, 1.0, "boven")
    meter(kx + 104, 158, 0.5, "halfweg")
    meter(kx + 164, 158, 0.0, "beneden")
    d.append(f'<rect x="{kx+178}" y="36" width="11" height="9" fill="{DRAAD}" '
             f'fill-opacity="0.5"/>')
    d.append(_tekst(kx + 194, 44, "Ep", 9.5, DRAAD, "start", True))
    d.append(f'<rect x="{kx+178}" y="52" width="11" height="9" fill="{AMBER}" '
             f'fill-opacity="0.5"/>')
    d.append(_tekst(kx + 194, 60, "Ek", 9.5, AMBER, "start", True))

    return _svg(cel_b * 2, cel_h, "\n".join(d))


def gaswetten(breedte=470):
    r"""De drie gaswetten, elk in hun eigen grafiek.

    Links een isotherm proces: p tegenover V geeft een hyperbool. In het
    midden een isobaar proces: V tegenover T geeft een rechte door de
    oorsprong. Rechts een isochoor proces: p tegenover T geeft er ook een.
    Dat die twee rechten door de oorsprong gaan, geldt alleen met T in
    kelvin; daarom staat de eenheid bij de as.
    """
    import math
    cel_b, cel_h = 156, 158
    d = []

    def paneel(px, tag, y_naam, x_naam, onder):
        d.append(f'<rect x="{px+5}" y="4" width="{cel_b-10}" height="{cel_h-30}" rx="7" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        ox, oy, top = px + 30, 102, 24
        rechts = px + cel_b - 18
        d.append(f'<line x1="{ox}" y1="{top}" x2="{ox}" y2="{oy+6}" stroke="{DIM}" '
                 f'stroke-width="1.3"/>')
        d.append(f'<line x1="{ox-6}" y1="{oy}" x2="{rechts}" y2="{oy}" stroke="{DIM}" '
                 f'stroke-width="1.3"/>')
        d.append(_pijlkop(rechts, oy, 0.0, DIM, 4.0))
        d.append(_pijlkop(ox, top, -math.pi / 2, DIM, 4.0))
        d.append(_tekst(rechts - 4, oy + 13, x_naam, 9.5, DIM, "middle"))
        d.append(_tekst(ox - 11, top + 4, y_naam, 9.5, DIM, "middle"))
        d.append(_tekst(px + cel_b - 16, 20, tag, 8.5, DARK, "end", True))
        d.append(_tekst(px + cel_b / 2, cel_h - 10, onder, 9, DIM, "middle"))
        return ox, oy, top, rechts

    # ── isotherm: p(V) is een hyperbool
    ox, oy, top, rechts = paneel(0, "isotherm", "p", "V", "p maal V blijft gelijk")
    x0, x1 = ox + 14, rechts - 10
    k = (oy - top - 12) * (x0 - ox)
    punten = []
    for i in range(29):
        x = x0 + (x1 - x0) * i / 28
        punten.append(f"{x:.1f},{oy - k / (x - ox):.1f}")
    d.append(f'<polyline points="{" ".join(punten)}" fill="none" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')
    d.append(_tekst(ox + 88, oy - 44, "hyperbool", 9, FOREST, "middle", True))

    # ── isobaar: V(T) is een rechte door de oorsprong
    ox, oy, top, rechts = paneel(cel_b, "isobaar", "V", "T (K)", "V stijgt recht met T")
    ex, ey = rechts - 12, top + 10
    d.append(f'<line x1="{ox}" y1="{oy}" x2="{ex}" y2="{ey}" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')
    d.append(f'<circle cx="{ox}" cy="{oy}" r="3" fill="{DARK}"/>')
    d.append(_tekst(ox + 40, oy - 8, "door 0 K", 8.5, AMBER, "start", True))

    # ── isochoor: p(T) is er ook een
    ox, oy, top, rechts = paneel(cel_b * 2, "isochoor", "p", "T (K)", "p stijgt recht met T")
    ex, ey = rechts - 12, top + 22
    d.append(f'<line x1="{ox}" y1="{oy}" x2="{ex}" y2="{ey}" stroke="{FOREST}" '
             f'stroke-width="2.2"/>')
    d.append(f'<circle cx="{ox}" cy="{oy}" r="3" fill="{DARK}"/>')
    d.append(_tekst(ox + 56, oy - 8, "door 0 K", 8.5, AMBER, "start", True))

    return _svg(cel_b * 3, cel_h, "\n".join(d))


def verwarmingscurve(breedte=470):
    r"""De verwarmingscurve van water, van ijs tot stoom.

    Op de horizontale as de warmte die je toevoert, op de verticale as de
    temperatuur. De twee vlakke stukken zijn het smelten en het koken: daar
    gaat alle warmte naar de faseovergang en beweegt de thermometer niet.
    Dat is net het stuk dat bij een smelt- of stolcurve het vaakst verkeerd
    gelezen wordt.
    """
    import math
    h = 206
    d = []
    ox, oy, top, rechts = 54, 180, 22, 450
    y0, y100 = 132, 70

    d.append(f'<rect x="4" y="4" width="{breedte-8}" height="{h-34}" rx="8" '
             f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
    d.append(f'<line x1="{ox}" y1="{top}" x2="{ox}" y2="{oy+6}" stroke="{DIM}" '
             f'stroke-width="1.3"/>')
    d.append(f'<line x1="{ox-6}" y1="{oy}" x2="{rechts}" y2="{oy}" stroke="{DIM}" '
             f'stroke-width="1.3"/>')
    d.append(_pijlkop(rechts, oy, 0.0, DIM, 4.5))
    d.append(_pijlkop(ox, top, -math.pi / 2, DIM, 4.5))
    d.append(_tekst(ox - 10, top + 4, "T", 10, DIM, "end"))
    d.append(_tekst(rechts - 8, oy + 15, "warmte Q", 10, DIM, "end"))

    # ── de twee hulplijnen met hun temperatuur
    for y, naam in ((y0, "0 °C"), (y100, "100 °C")):
        d.append(f'<line x1="{ox}" y1="{y}" x2="{rechts-14}" y2="{y}" stroke="{BORDER}" '
                 f'stroke-width="1.1" stroke-dasharray="4 4"/>')
        d.append(_tekst(ox - 7, y + 4, naam, 9, DIM, "end"))

    # ── de curve zelf
    xs = [58, 104, 158, 228, 372, 436]
    ys = [150, y0, y0, y100, y100, 44]
    punten = " ".join(f"{x},{y}" for x, y in zip(xs, ys))
    d.append(f'<polyline points="{punten}" fill="none" stroke="{FOREST}" stroke-width="2.4" '
             f'stroke-linejoin="round"/>')

    # ── de vlakke stukken dikker, want daar zit de faseovergang
    d.append(f'<line x1="{xs[1]}" y1="{y0}" x2="{xs[2]}" y2="{y0}" stroke="{AMBER}" '
             f'stroke-width="3.4"/>')
    d.append(f'<line x1="{xs[3]}" y1="{y100}" x2="{xs[4]}" y2="{y100}" stroke="{AMBER}" '
             f'stroke-width="3.4"/>')

    d.append(_tekst(78, 166, "ijs", 9.5, DIM, "middle"))
    d.append(_tekst(131, y0 - 8, "smelten", 9.5, AMBER, "middle", True))
    d.append(_tekst(203, 124, "water", 9.5, DIM, "middle"))
    d.append(_tekst(300, y100 - 8, "koken", 9.5, AMBER, "middle", True))
    d.append(_tekst(420, 90, "stoom", 9.5, DIM, "middle"))

    d.append(_tekst(breedte / 2, h - 10,
                    "op een vlak stuk verandert de temperatuur niet", 9, DIM, "middle"))
    return _svg(breedte, h, "\n".join(d))


def trillingsgrafiek(breedte=470):
    r"""Een harmonische trilling en een gedempte trilling naast elkaar.

    Links staat de amplitude A als pijl vanaf de evenwichtslijn en de periode
    T tussen twee gelijke standen. Rechts dezelfde trilling, maar met twee
    krimpende grenzen eromheen: de frequentie blijft, de amplitude niet.
    """
    import math
    cel_b, cel_h = 234, 196
    d = []

    def paneel(px, tag, onder):
        d.append(f'<rect x="{px+5}" y="4" width="{cel_b-10}" height="{cel_h-30}" rx="7" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        mid = 96
        ox, rechts = px + 26, px + cel_b - 16
        d.append(f'<line x1="{ox}" y1="{mid}" x2="{rechts}" y2="{mid}" stroke="{BORDER}" '
                 f'stroke-width="1.1" stroke-dasharray="4 4"/>')
        d.append(f'<line x1="{ox}" y1="36" x2="{ox}" y2="{mid+52}" stroke="{DIM}" '
                 f'stroke-width="1.3"/>')
        d.append(_pijlkop(ox, 36, -math.pi / 2, DIM, 4.0))
        d.append(_tekst(ox - 10, 40, "y", 9.5, DIM, "middle"))
        d.append(_tekst(rechts, mid + 15, "t", 9.5, DIM, "middle"))
        d.append(_tekst(px + cel_b - 16, 20, tag, 8.5, DARK, "end", True))
        d.append(_tekst(px + cel_b / 2, cel_h - 10, onder, 9, DIM, "middle"))
        return ox, mid, rechts

    # ── links: de gewone harmonische trilling
    ox, mid, rechts = paneel(0, "harmonisch", "A en T lees je er zo af")
    amp = 40
    d.append(_golf(ox, rechts - 4, mid, amp, 2, FOREST))
    top1 = ox + (rechts - 4 - ox) / 8
    top2 = ox + 5 * (rechts - 4 - ox) / 8
    # amplitude
    d.append(f'<line x1="{top1}" y1="{mid}" x2="{top1}" y2="{mid-amp}" stroke="{AMBER}" '
             f'stroke-width="1.6"/>')
    d.append(_pijlkop(top1, mid - amp, -math.pi / 2, AMBER, 4.0))
    d.append(_tekst(top1 + 12, mid - amp / 2 + 4, "A", 10, AMBER, "middle", True))
    # periode
    d.append(f'<line x1="{top1}" y1="{mid-amp-14}" x2="{top2}" y2="{mid-amp-14}" '
             f'stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(_pijlkop(top1, mid - amp - 14, math.pi, AMBER, 4.0))
    d.append(_pijlkop(top2, mid - amp - 14, 0.0, AMBER, 4.0))
    d.append(_tekst((top1 + top2) / 2, mid - amp - 19, "T", 10, AMBER, "middle", True))

    # ── rechts: dezelfde trilling, gedempt
    ox, mid, rechts = paneel(cel_b, "gedempt", "de amplitude krimpt, T niet")
    x1 = rechts - 4
    n = 160
    punten, boven, onder_rand = [], [], []
    for i in range(n + 1):
        x = ox + (x1 - ox) * i / n
        env = amp * math.exp(-2.1 * i / n)
        punten.append(f"{x:.1f},{mid - env * math.sin(2 * math.pi * 2 * i / n):.1f}")
        boven.append(f"{x:.1f},{mid - env:.1f}")
        onder_rand.append(f"{x:.1f},{mid + env:.1f}")
    for rand in (boven, onder_rand):
        d.append(f'<polyline points="{" ".join(rand)}" fill="none" stroke="{AMBER}" '
                 f'stroke-width="1.3" stroke-dasharray="4 3"/>')
    d.append(f'<polyline points="{" ".join(punten)}" fill="none" stroke="{FOREST}" '
             f'stroke-width="2.2" stroke-linejoin="round"/>')

    return _svg(cel_b * 2, cel_h, "\n".join(d))


def golfbeeld(breedte=470):
    r"""Een lopende golf en een staande golf naast elkaar.

    Links staat de golflengte als pijl tussen twee toppen en de amplitude
    als pijl vanaf de rustlijn. Rechts de staande golf: de twee uiterste
    standen getekend, met de knopen als stip en de buiken ertussen.
    """
    import math
    cel_b, cel_h = 234, 190
    d = []

    def paneel(px, tag, onder):
        d.append(f'<rect x="{px+5}" y="4" width="{cel_b-10}" height="{cel_h-30}" rx="7" '
                 f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
        mid = 94
        ox, rechts = px + 20, px + cel_b - 16
        d.append(f'<line x1="{ox}" y1="{mid}" x2="{rechts}" y2="{mid}" stroke="{BORDER}" '
                 f'stroke-width="1.1" stroke-dasharray="4 4"/>')
        d.append(_tekst(px + cel_b - 16, 20, tag, 8.5, DARK, "end", True))
        d.append(_tekst(px + cel_b / 2, cel_h - 10, onder, 9, DIM, "middle"))
        return ox, mid, rechts

    # ── links: de lopende golf
    ox, mid, rechts = paneel(0, "lopende golf", "λ tussen twee toppen")
    amp = 34
    d.append(_golf(ox, rechts, mid, amp, 2, FOREST))
    span = rechts - ox
    top1 = ox + span / 8
    top2 = ox + 5 * span / 8
    d.append(f'<line x1="{top1}" y1="{mid-amp-12}" x2="{top2}" y2="{mid-amp-12}" '
             f'stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(_pijlkop(top1, mid - amp - 12, math.pi, AMBER, 4.0))
    d.append(_pijlkop(top2, mid - amp - 12, 0.0, AMBER, 4.0))
    d.append(_tekst((top1 + top2) / 2, mid - amp - 17, "λ", 10.5, AMBER, "middle", True))
    dal = ox + 3 * span / 8
    d.append(f'<line x1="{dal}" y1="{mid}" x2="{dal}" y2="{mid+amp}" stroke="{AMBER}" '
             f'stroke-width="1.6"/>')
    d.append(_pijlkop(dal, mid + amp, math.pi / 2, AMBER, 4.0))
    d.append(_tekst(dal + 13, mid + amp / 2 + 4, "A", 10, AMBER, "middle", True))
    d.append(_pijlkop(rechts - 2, mid + amp + 22, 0.0, FOREST, 5.0))
    d.append(f'<line x1="{rechts-44}" y1="{mid+amp+22}" x2="{rechts-4}" y2="{mid+amp+22}" '
             f'stroke="{FOREST}" stroke-width="1.6"/>')
    d.append(_tekst(rechts - 58, mid + amp + 26, "v", 10, FOREST, "end", True))

    # ── rechts: de staande golf
    ox, mid, rechts = paneel(cel_b, "staande golf", "knopen blijven op hun plaats")
    span = rechts - ox
    for teken, stijl in ((1, ""), (-1, ' stroke-dasharray="5 4"')):
        punten = []
        for i in range(121):
            x = ox + span * i / 120
            punten.append(f"{x:.1f},{mid - teken * amp * math.sin(3 * math.pi * i / 120):.1f}")
        d.append(f'<polyline points="{" ".join(punten)}" fill="none" stroke="{FOREST}" '
                 f'stroke-width="2.2"{stijl}/>')
    for i in range(4):
        x = ox + span * i / 3
        d.append(f'<circle cx="{x:.1f}" cy="{mid}" r="3.4" fill="{DARK}"/>')
    d.append(_tekst(ox + span / 6, mid - amp - 10, "buik", 9, AMBER, "middle", True))
    d.append(_tekst(rechts, mid + amp + 16, "knoop", 9, AMBER, "end", True))
    return _svg(cel_b * 2, cel_h, "\n".join(d))


def lensbeeld(breedte=470):
    r"""De stralengang door een bolle lens.

    Het voorwerp staat verder dan \(2f\); de twee hulpstralen snijden elkaar
    rechts van de lens en geven daar een omgekeerd, kleiner beeld.
    """
    import math
    h = 206
    d = []
    d.append(f'<rect x="5" y="4" width="{breedte-10}" height="{h-28}" rx="7" '
             f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
    as_y = 108
    lens_x = 250
    f = 70
    d.append(f'<line x1="30" y1="{as_y}" x2="440" y2="{as_y}" stroke="{BORDER}" '
             f'stroke-width="1.1" stroke-dasharray="4 4"/>')
    d.append(f'<ellipse cx="{lens_x}" cy="{as_y}" rx="9" ry="64" fill="{FOREST}" '
             f'fill-opacity="0.12" stroke="{FOREST}" stroke-width="1.6"/>')

    for x, naam in ((lens_x - f, "F"), (lens_x + f, "F"),
                    (lens_x - 2 * f, "2F"), (lens_x + 2 * f, "2F")):
        d.append(f'<circle cx="{x}" cy="{as_y}" r="2.8" fill="{DARK}"/>')
        d.append(_tekst(x, as_y + 16, naam, 9, DIM, "middle"))

    vx, vh = 80, 56
    d.append(f'<line x1="{vx}" y1="{as_y}" x2="{vx}" y2="{as_y-vh}" stroke="{FOREST}" '
             f'stroke-width="2.4"/>')
    d.append(_pijlkop(vx, as_y - vh, -math.pi / 2, FOREST, 5.0))
    d.append(_tekst(vx, as_y - vh - 10, "voorwerp", 9, FOREST, "middle", True))

    do = lens_x - vx
    di = 1 / (1 / f - 1 / do)
    bx = lens_x + di
    bh = vh * di / do

    straal = f'stroke="{AMBER}" stroke-width="1.5"'
    d.append(f'<line x1="{vx}" y1="{as_y-vh}" x2="{lens_x}" y2="{as_y-vh}" {straal}/>')
    d.append(f'<line x1="{lens_x}" y1="{as_y-vh}" x2="{bx:.1f}" y2="{as_y+bh:.1f}" {straal}/>')
    d.append(f'<line x1="{vx}" y1="{as_y-vh}" x2="{bx:.1f}" y2="{as_y+bh:.1f}" {straal}/>')

    d.append(f'<line x1="{bx:.1f}" y1="{as_y}" x2="{bx:.1f}" y2="{as_y+bh:.1f}" '
             f'stroke="{DARK}" stroke-width="2.4"/>')
    d.append(_pijlkop(bx, as_y + bh, math.pi / 2, DARK, 5.0))
    d.append(_tekst(bx + 4, as_y + bh + 16, "beeld", 9, DARK, "start", True))
    d.append(_tekst(breedte / 2, h - 8,
                    "voorwerp links van 2F, beeld tussen F en 2F", 9, DIM, "middle"))
    return _svg(breedte, h, "\n".join(d))


def emspectrum(breedte=470):
    r"""Het elektromagnetisch spectrum als één balk van radiogolf tot gamma."""
    import math
    h = 160
    namen = ["radio", "micro", "infrarood", "licht", "uv", "röntgen", "gamma"]
    d = []
    d.append(f'<rect x="5" y="4" width="{breedte-10}" height="{h-28}" rx="7" '
             f'fill="#ffffff" stroke="{BORDER}" stroke-width="1.2"/>')
    links, rechts = 30, 440
    top, hoog = 56, 34
    stap = (rechts - links) / len(namen)

    d.append(_tekst(links, 32, "grote λ", 9, DIM, "start"))
    d.append(_tekst(rechts, 32, "hoge f", 9, DIM, "end"))
    d.append(f'<line x1="{links+46}" y1="28" x2="{rechts-42}" y2="28" stroke="{BORDER}" '
             f'stroke-width="1.2"/>')
    d.append(_pijlkop(rechts - 42, 28, 0.0, BORDER, 4.5))

    for i, naam in enumerate(namen):
        x = links + i * stap
        dek = 0.10 + i * 0.075
        d.append(f'<rect x="{x:.1f}" y="{top}" width="{stap:.1f}" height="{hoog}" '
                 f'fill="{FOREST}" fill-opacity="{dek:.2f}" stroke="{BORDER}" '
                 f'stroke-width="1"/>')
        d.append(_tekst(x + stap / 2, top + hoog + 16, naam, 8.5, INK, "middle"))

    lx = links + 3 * stap
    d.append(f'<line x1="{lx:.1f}" y1="{top+hoog+24}" x2="{lx+stap:.1f}" '
             f'y2="{top+hoog+24}" stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(f'<line x1="{lx:.1f}" y1="{top+hoog+24}" x2="{lx:.1f}" y2="{top+hoog+19}" '
             f'stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(f'<line x1="{lx+stap:.1f}" y1="{top+hoog+24}" x2="{lx+stap:.1f}" '
             f'y2="{top+hoog+19}" stroke="{AMBER}" stroke-width="1.6"/>')
    d.append(_tekst(lx + stap / 2, top + hoog + 38, "400 tot 700 nm", 8.5, AMBER,
                    "middle", True))
    return _svg(breedte, h, "\n".join(d))
