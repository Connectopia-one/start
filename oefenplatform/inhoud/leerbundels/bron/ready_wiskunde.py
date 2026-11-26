# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de Ready-hoofdstukken wiskunde (3de en 4de leerjaar),
behalve Tafels en delen (zie ready_tafels.py). De vragen op het scherm staan in
../../ready/bron/wiskunde_*.py; de oefenbundels vragen andere getallen.

    python3 ready_wiskunde.py            # alles
    python3 ready_wiskunde.py breuken    # één hoofdstuk
"""
import math, sys
from ready_gemeen import maak, tabel, svg, READY, DARK, ORANJE, PAARS, GROEN

HOE = ["Schrijf met potlood, dan kan je gerust iets uitgommen.",
       "Schrijf altijd je tussenstappen op, ook als je het antwoord al in je hoofd weet.",
       "Het antwoordblad zit achteraan. Scheur het eraf voor je begint."]
W = "90px"


def klok(uur, minuut, maat=120):
    r = maat / 2 - 6; c = maat / 2
    d = [f'<circle cx="{c}" cy="{c}" r="{r}" fill="#fff" stroke="{DARK}" stroke-width="3"/>']
    for i in range(1, 13):
        a = math.radians(i * 30 - 90)
        d.append(f'<text x="{c + (r - 13) * math.cos(a):.1f}" y="{c + (r - 13) * math.sin(a) + 4:.1f}" font-size="11" text-anchor="middle" fill="{DARK}">{i}</text>')
    for i in range(60):
        a = math.radians(i * 6 - 90); l = 5 if i % 5 == 0 else 2
        d.append(f'<line x1="{c + r * math.cos(a):.1f}" y1="{c + r * math.sin(a):.1f}" x2="{c + (r - l) * math.cos(a):.1f}" y2="{c + (r - l) * math.sin(a):.1f}" stroke="{DARK}" stroke-width="1"/>')
    if uur is not None:
        au = math.radians((uur % 12 + minuut / 60) * 30 - 90); am = math.radians(minuut * 6 - 90)
        d.append(f'<line x1="{c}" y1="{c}" x2="{c + r * .5 * math.cos(au):.1f}" y2="{c + r * .5 * math.sin(au):.1f}" stroke="{ORANJE}" stroke-width="5" stroke-linecap="round"/>')
        d.append(f'<line x1="{c}" y1="{c}" x2="{c + r * .8 * math.cos(am):.1f}" y2="{c + r * .8 * math.sin(am):.1f}" stroke="{DARK}" stroke-width="3" stroke-linecap="round"/>')
    d.append(f'<circle cx="{c}" cy="{c}" r="4" fill="{DARK}"/>')
    return svg(maat, maat, "".join(d))


def breukbalk(n, k, kleur=ORANJE, b=220):
    w = b / n
    return svg(b + 4, 40, "".join(
        f'<rect x="{2 + i * w:.1f}" y="4" width="{w:.1f}" height="30" fill="{kleur if i < k else "#fff"}" stroke="{DARK}" stroke-width="1.5"/>' for i in range(n)))


def taart(n, k, kleur=PAARS, m=90):
    c = m / 2; r = m / 2 - 4; d = []
    for i in range(n):
        a1 = math.radians(i * 360 / n - 90); a2 = math.radians((i + 1) * 360 / n - 90)
        d.append(f'<path d="M{c},{c} L{c + r * math.cos(a1):.1f},{c + r * math.sin(a1):.1f} A{r},{r} 0 0 1 {c + r * math.cos(a2):.1f},{c + r * math.sin(a2):.1f} Z" '
                 f'fill="{kleur if i < k else "#fff"}" stroke="{DARK}" stroke-width="1.5"/>')
    return svg(m, m, "".join(d))


def figuren():
    s = f'stroke="{DARK}" stroke-width="2.5" fill="none"'
    d = [f'<rect x="10" y="20" width="60" height="60" {s}/>', f'<text x="40" y="100" font-size="12" text-anchor="middle">vierkant</text>',
         f'<rect x="90" y="30" width="100" height="50" {s}/>', f'<text x="140" y="100" font-size="12" text-anchor="middle">rechthoek</text>',
         f'<polygon points="210,80 280,80 245,20" {s}/>', f'<text x="245" y="100" font-size="12" text-anchor="middle">driehoek</text>',
         f'<circle cx="335" cy="50" r="32" {s}/>', f'<text x="335" y="100" font-size="12" text-anchor="middle">cirkel</text>',
         f'<polygon points="420,50 450,15 480,50 450,85" {s}/>', f'<text x="450" y="100" font-size="12" text-anchor="middle">ruit</text>']
    return svg(500, 108, "".join(d))


def hoeken():
    s = f'stroke="{DARK}" stroke-width="3" fill="none" stroke-linecap="round"'
    d = [f'<polyline points="20,20 20,90 100,90" {s}/><rect x="20" y="76" width="14" height="14" fill="none" stroke="{ORANJE}" stroke-width="2"/>',
         f'<text x="60" y="112" font-size="12" text-anchor="middle">recht</text>',
         f'<polyline points="200,25 140,90 230,90" {s}/><text x="185" y="112" font-size="12" text-anchor="middle">scherp</text>',
         f'<polyline points="250,40 290,90 380,90" {s}/><text x="320" y="112" font-size="12" text-anchor="middle">stomp</text>']
    return svg(400, 120, "".join(d))


def lijnen():
    s = f'stroke="{DARK}" stroke-width="3" stroke-linecap="round"'
    d = [f'<line x1="20" y1="30" x2="160" y2="30" {s}/><line x1="20" y1="60" x2="160" y2="60" {s}/>',
         f'<text x="90" y="90" font-size="12" text-anchor="middle">evenwijdig</text>',
         f'<line x1="200" y1="60" x2="320" y2="60" {s}/><line x1="260" y1="10" x2="260" y2="60" {s}/>',
         f'<rect x="260" y="46" width="14" height="14" fill="none" stroke="{ORANJE}" stroke-width="2"/>',
         f'<text x="260" y="90" font-size="12" text-anchor="middle">loodrecht</text>']
    return svg(340, 100, "".join(d))


def kubusblok():
    """3 bij 2 kubusjes, 2 lagen, in eenvoudig perspectief."""
    d, z = [], 22
    for laag in range(2):
        for rij in range(1, -1, -1):
            for k in range(3):
                x = 20 + k * z + rij * 11; y = 80 - laag * z - rij * 11
                d.append(f'<polygon points="{x},{y} {x + z},{y} {x + z},{y - z} {x},{y - z}" fill="#f3c9a8" stroke="{DARK}"/>'
                         f'<polygon points="{x},{y - z} {x + 11},{y - z - 11} {x + z + 11},{y - z - 11} {x + z},{y - z}" fill="#f8dcc6" stroke="{DARK}"/>'
                         f'<polygon points="{x + z},{y} {x + z + 11},{y - 11} {x + z + 11},{y - z - 11} {x + z},{y - z}" fill="#e0a77e" stroke="{DARK}"/>')
    return svg(130, 100, "".join(d), 210)


def hoek(soort):
    s = f'stroke="{DARK}" stroke-width="3" fill="none" stroke-linecap="round"'
    p = {"recht": "20,10 20,80 100,80", "scherp": "90,15 20,80 110,80", "stomp": "0,30 40,80 120,80"}[soort]
    extra = f'<rect x="20" y="66" width="14" height="14" fill="none" stroke="{ORANJE}" stroke-width="2"/>' if soort == "recht" else ""
    return svg(125, 90, f'<polyline points="{p}" {s}/>' + extra, 125)


def rooster(k, r, z=26):
    d = [f'<rect x="{2 + i * z}" y="{2 + j * z}" width="{z}" height="{z}" fill="#f3c9a8" stroke="{DARK}" stroke-width="1.2"/>' for i in range(k) for j in range(r)]
    return svg(k * z + 4, r * z + 4, "".join(d))


H = {}

# ---------------------------------------------------------------- getallen
H["getallen"] = ("getallen-tot-10000-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Getallen tot 10 000",
    onder="Duizendtallen, honderdtallen, tientallen en eenheden, getallen vergelijken, ordenen en afronden.",
    secties=[
        dict(kop="De plaats van een cijfer", blokken=[
            ("p", "In <strong>4 638</strong> staat elk cijfer op een eigen plaats. Die plaats bepaalt hoeveel het cijfer waard is."),
            ("fig", tabel(["D (duizendtal)", "H (honderdtal)", "T (tiental)", "E (eenheid)"], [["4", "6", "3", "8"], ["4 000", "600", "30", "8"]], "100%")),
            ("p", "4 638 = 4 000 + 600 + 30 + 8. Tien eenheden zijn 1 tiental, tien tientallen 1 honderdtal, tien honderdtallen 1 duizendtal."),
            ("weetje", "Grote getallen schrijf je met een spatie na het duizendtal: 4 638, niet 4638. Zo lees je ze makkelijker."),
        ]),
        dict(kop="Getallen vergelijken en ordenen", blokken=[
            ("p", "Vergelijk eerst de <strong>duizendtallen</strong>. Zijn die gelijk, kijk dan naar de honderdtallen, en zo verder."),
            ("p", "3 520 <strong>&lt;</strong> 3 610, want 5 honderdtallen is minder dan 6. Het open stuk van het teken wijst naar het grootste getal."),
        ]),
        dict(kop="Afronden", blokken=[
            ("p", "Afronden op een tiental: kijk naar de eenheden. Is het 5 of meer, dan ga je naar boven. Is het minder dan 5, dan ga je naar beneden."),
            ("fig", tabel(["Getal", "Op een tiental", "Op een honderdtal", "Op een duizendtal"], [["3 847", "3 850", "3 800", "4 000"], ["6 215", "6 220", "6 200", "6 000"]], "100%")),
        ]),
        dict(kop="Getallen op de getallenlijn", blokken=[
            ("p", "Op een getallenlijn staan de getallen op gelijke afstand. Tussen 2 000 en 3 000 ligt 2 500 precies in het midden."),
        ]),
    ],
    onthoud=["D H T E: duizendtal, honderdtal, tiental, eenheid.", "Vergelijken: begin bij het cijfer helemaal links.",
             "Afronden: 5 of meer gaat naar boven.", "Grote getallen schrijf je met een spatie: 7 250."]),
    dict(vak="Wiskunde", niveau=READY, titel="Getallen tot 10 000", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Splitsen", opdracht="Schrijf hoeveel elk cijfer waard is.", oefeningen=[
            ("tabel", ["Getal", "D", "H", "T", "E"], [["5 274", None, None, None, None], ["8 019", None, None, None, None], ["3 600", None, None, None, None]],
             "5 274: 5 000, 200, 70, 4 · 8 019: 8 000, 0, 10, 9 · 3 600: 3 000, 600, 0, 0", "80px"),
            ("rij", [("4 000 + 300 + 20 + 1 =", "4 321"), ("7 000 + 50 + 6 =", "7 056"), ("9 000 + 900 + 9 =", "9 909")], "", "110px"),
        ]),
        dict(kop="Vergelijken", opdracht="Schrijf &lt;, &gt; of = op de lijn.", oefeningen=[
            ("rij", [("2 415 ... 2 451", "&lt;"), ("6 300 ... 6 030", "&gt;"), ("4 999 ... 5 000", "&lt;"), ("7 000 ... 6 000 + 1 000", "=")], "", W),
            ("open", "Zet van klein naar groot: 3 850 – 3 508 – 3 580 – 3 805.", "3 508 – 3 580 – 3 805 – 3 850", 1),
        ]),
        dict(kop="Tellen en verder tellen", oefeningen=[
            ("rij", [("1 meer dan 4 997", "4 998"), ("10 meer dan 3 495", "3 505"), ("100 meer dan 6 950", "7 050"), ("1 000 minder dan 9 200", "8 200")], "Schrijf het getal.", "110px"),
            ("open", "Tel verder per 250: 1 000 – 1 250 – ... tot 2 500.", "1 000 – 1 250 – 1 500 – 1 750 – 2 000 – 2 250 – 2 500", 1),
        ]),
        dict(kop="Afronden", oefeningen=[
            ("rij", [("2 463", "2 460"), ("5 718", "5 720"), ("8 095", "8 100")], "Rond af op een tiental.", W),
            ("rij", [("2 463", "2 500"), ("5 718", "5 700"), ("8 095", "8 100")], "Rond af op een honderdtal.", W),
            ("rij", [("2 463", "2 000"), ("5 718", "6 000"), ("8 095", "8 000")], "Rond af op een duizendtal.", W),
        ]),
        dict(kop="Puzzelen met getallen", oefeningen=[
            ("open", "Maak met de cijfers 3, 7, 0 en 5 het grootste en het kleinste getal van vier cijfers (een getal begint niet met 0).", "grootste 7 530, kleinste 3 057", 2),
            ("waar", "In 6 482 is de 4 meer waard dan de 8.", True),
            ("waar", "Het getal na 6 999 is 6 1000.", False),
            ("open", "Ik ben een getal tussen 4 000 en 5 000. Mijn honderdtal is 7, mijn tiental 0 en mijn eenheid 2. Wie ben ik?", "4 702", 1),
        ]),
    ]))

# ---------------------------------------------------------------- rekenen
H["rekenen"] = ("rekenen-en-cijferen-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Rekenen en cijferen",
    onder="Optellen en aftrekken tot 10 000, onder elkaar rekenen, vermenigvuldigen en delen met grotere getallen, rekenvolgorde.",
    secties=[
        dict(kop="Onder elkaar optellen", blokken=[
            ("p", "Zet de getallen netjes <strong>onder elkaar</strong>: eenheden onder eenheden, tientallen onder tientallen. Begin <strong>rechts</strong>."),
            ("fig", tabel(["", "D", "H", "T", "E"], [["", "", "1", "1", ""], ["", "4", "5", "6", "8"], ["+", "1", "2", "7", "5"], ["=", "5", "8", "4", "3"]], "60%"),
             "8 + 5 = 13: schrijf 3, de 1 gaat mee naar de tientallen."),
        ]),
        dict(kop="Onder elkaar aftrekken", blokken=[
            ("p", "Lukt het niet, dan <strong>leen</strong> je een tiental van links. 7 352 − 2 128: 2 − 8 lukt niet, dus 12 − 8 = 4 en er blijven 4 tientallen over."),
            ("weetje", "Kijk een aftrekking na met een optelling: 5 224 + 2 128 moet weer 7 352 geven."),
        ]),
        dict(kop="Vermenigvuldigen met grotere getallen", blokken=[
            ("p", "Splits het grote getal: 23 × 4 = (20 × 4) + (3 × 4) = 80 + 12 = <strong>92</strong>."),
            ("p", "Met een getal van twee cijfers: 24 × 12 = (24 × 10) + (24 × 2) = 240 + 48 = <strong>288</strong>."),
        ]),
        dict(kop="Delen met grotere getallen", blokken=[
            ("p", "Splits in stukken die je makkelijk kan delen: 96 : 4 = (80 : 4) + (16 : 4) = 20 + 4 = <strong>24</strong>."),
        ]),
        dict(kop="Rekenvolgorde", blokken=[
            ("kader", "<strong>1.</strong> Eerst wat tussen <strong>haakjes</strong> staat.<br><strong>2.</strong> Dan <strong>×</strong> en <strong>:</strong> van links naar rechts.<br>"
                      "<strong>3.</strong> Dan <strong>+</strong> en <strong>−</strong> van links naar rechts."),
            ("p", "3 + 4 × 2 = 3 + 8 = 11, maar (3 + 4) × 2 = 7 × 2 = 14."),
        ]),
    ],
    onthoud=["Onder elkaar: eenheden onder eenheden, begin rechts.", "Meer dan 9? Schrijf de eenheid, de 1 gaat mee.",
             "Kijk na met de omgekeerde bewerking.", "Splits om te vermenigvuldigen of te delen.", "Haakjes, dan × en :, dan + en −."]),
    dict(vak="Wiskunde", niveau=READY, titel="Rekenen en cijferen", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Onder elkaar optellen", opdracht="Reken onder elkaar uit in de ruitjes.", oefeningen=[
            ("teken", "3 457 + 2 386 =", "5 843", 40), ("teken", "1 908 + 4 595 =", "6 503", 40),
        ]),
        dict(kop="Onder elkaar aftrekken", opdracht="Reken onder elkaar uit in de ruitjes en kijk na met een optelling.", oefeningen=[
            ("teken", "6 524 − 3 172 =", "3 352", 40), ("teken", "8 000 − 2 645 =", "5 355", 40),
        ]),
        dict(kop="Uit het hoofd", opdracht="Reken uit.", oefeningen=[
            ("rij", [("2 500 + 1 500 =", "4 000"), ("6 000 − 1 200 =", "4 800"), ("4 990 + 10 =", "5 000"), ("7 300 − 400 =", "6 900")], "", "110px"),
        ]),
        dict(kop="Vermenigvuldigen", opdracht="Splits het getal en schrijf je tussenstappen.", oefeningen=[
            ("open", "34 × 3 =", "30 × 3 = 90; 4 × 3 = 12; 90 + 12 = 102", 2),
            ("open", "126 × 4 =", "100 × 4 = 400; 20 × 4 = 80; 6 × 4 = 24; samen 504", 2),
            ("open", "23 × 12 =", "23 × 10 = 230; 23 × 2 = 46; 230 + 46 = 276", 2),
        ]),
        dict(kop="Delen", opdracht="Splits het getal en schrijf je tussenstappen.", oefeningen=[
            ("open", "84 : 4 =", "80 : 4 = 20; 4 : 4 = 1; samen 21", 2),
            ("open", "105 : 5 =", "100 : 5 = 20; 5 : 5 = 1; samen 21", 2),
            ("open", "144 : 12 =", "120 : 12 = 10; 24 : 12 = 2; samen 12", 2),
        ]),
        dict(kop="Rekenvolgorde", opdracht="Reken uit. Let op de volgorde.", oefeningen=[
            ("rij", [("5 + 3 × 4 =", "17"), ("(5 + 3) × 4 =", "32"), ("20 − 8 : 2 =", "16"), ("(20 − 8) : 2 =", "6")], "", W),
            ("waar", "6 + 2 × 5 = 40", False),
        ]),
        dict(kop="Vraagstukken", opdracht="Schrijf je tussenstappen op en zet de eenheid erbij.", oefeningen=[
            ("open", "Een bakker bakt 1 250 broodjes op zaterdag en 980 op zondag. Hoeveel broodjes bakt hij in het weekend?", "1 250 + 980 = 2 230 broodjes", 2),
            ("open", "Een school krijgt 36 dozen met elk 12 schriften. Hoeveel schriften zijn dat?", "36 × 10 = 360; 36 × 2 = 72; samen 432 schriften", 2),
            ("open", "Een uitstap kost 8 euro per kind. De klas betaalt samen 184 euro. Hoeveel kinderen gaan mee?", "184 : 8 = 23 kinderen", 2),
        ]),
    ]))

# ---------------------------------------------------------------- breuken
H["breuken"] = ("breuken-en-kommagetallen-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Breuken en kommagetallen",
    onder="Teller en noemer, breuken vergelijken, gelijknamige breuken optellen en aftrekken, een breuk van een getal, kommagetallen.",
    secties=[
        dict(kop="Wat is een breuk?", blokken=[
            ("fig", taart(8, 3), "3/8: de taart is in 8 gelijke stukken verdeeld, er zijn er 3 gekleurd"),
            ("p", "De <strong>noemer</strong> (onder) zegt in hoeveel gelijke stukken je verdeelt. De <strong>teller</strong> (boven) zegt hoeveel stukken je neemt."),
        ]),
        dict(kop="Breuken vergelijken", blokken=[
            ("fig", breukbalk(2, 1), "1/2"), ("fig", breukbalk(4, 1), "1/4"), ("fig", breukbalk(8, 1), "1/8"),
            ("p", "Hoe <strong>groter de noemer</strong>, hoe <strong>kleiner</strong> elk stuk. Bij dezelfde noemer is de breuk met de grootste teller het grootst: 5/7 &gt; 3/7."),
            ("weetje", "2/4 en 1/2 zijn even groot. Kijk maar op de balken."),
        ]),
        dict(kop="Optellen en aftrekken met dezelfde noemer", blokken=[
            ("p", "De noemer blijft, je rekent enkel met de tellers: 1/4 + 2/4 = <strong>3/4</strong> en 5/6 − 2/6 = <strong>3/6</strong>."),
        ]),
        dict(kop="Een breuk van een getal", blokken=[
            ("kader", "3/4 van 20<br>Stap 1: deel door de noemer: 20 : 4 = 5<br>Stap 2: vermenigvuldig met de teller: 5 × 3 = <strong>15</strong>"),
        ]),
        dict(kop="Kommagetallen", blokken=[
            ("fig", tabel(["E", ",", "t (tiende)", "h (honderdste)"], [["2", ",", "3", "5"]], "60%"), "2,35 = 2 eenheden, 3 tienden en 5 honderdsten"),
            ("p", "0,1 = 1/10 en 0,01 = 1/100. Met geld: 2,35 euro is 2 euro en 35 cent."),
            ("p", "Vergelijken: kijk eerst naar de eenheden, dan naar de tienden, dan naar de honderdsten. 2,5 &gt; 2,45."),
        ]),
    ],
    onthoud=["Teller boven, noemer onder.", "Grotere noemer = kleinere stukken.", "Zelfde noemer: reken enkel met de tellers.",
             "Breuk van een getal: delen door de noemer, maal de teller.", "Eerste cijfer na de komma: tienden. Tweede: honderdsten."]),
    dict(vak="Wiskunde", niveau=READY, titel="Breuken en kommagetallen", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Welke breuk zie je?", opdracht="Schrijf de breuk van het gekleurde deel.", oefeningen=[
            ("fig", [(taart(4, 1), "1/4"), (taart(6, 5), "5/6"), (breukbalk(5, 2, b=150), "2/5")], ""),
        ]),
        dict(kop="Kleuren", oefeningen=[
            ("kleur", [(breukbalk(8, 0, b=180), "Kleur 3/8.", "3 vakjes gekleurd"), (breukbalk(10, 0, b=180), "Kleur 7/10.", "7 vakjes gekleurd")]),
        ]),
        dict(kop="Vergelijken", opdracht="Schrijf &lt;, &gt; of = op de lijn.", oefeningen=[
            ("rij", [("1/3 ... 1/5", "&gt;"), ("4/9 ... 7/9", "&lt;"), ("2/4 ... 1/2", "="), ("1/10 ... 1/2", "&lt;")], "", W),
        ]),
        dict(kop="Optellen en aftrekken", opdracht="Reken uit.", oefeningen=[
            ("rij", [("2/7 + 3/7 =", "5/7"), ("1/5 + 3/5 =", "4/5"), ("8/9 − 5/9 =", "3/9"), ("6/10 − 1/10 =", "5/10")], "", W),
        ]),
        dict(kop="Een breuk van een getal", opdracht="Schrijf je twee stappen op.", oefeningen=[
            ("open", "1/5 van 35 =", "35 : 5 = 7", 1), ("open", "3/4 van 28 =", "28 : 4 = 7; 7 × 3 = 21", 2), ("open", "2/3 van 18 =", "18 : 3 = 6; 6 × 2 = 12", 2),
        ]),
        dict(kop="Kommagetallen", oefeningen=[
            ("rij", [("drie tienden", "0,3"), ("zeven honderdsten", "0,07"), ("2 en 5 tienden", "2,5")], "Schrijf als kommagetal.", W),
            ("open", "Zet van klein naar groot: 1,5 – 1,05 – 1,45 – 1,4.", "1,05 – 1,4 – 1,45 – 1,5", 1),
            ("rij", [("2,40 + 1,35 =", "3,75"), ("5,80 − 2,50 =", "3,30"), ("0,75 + 0,25 =", "1,00")], "Reken uit.", W),
            ("waar", "0,50 is evenveel als 0,5.", True),
        ]),
        dict(kop="Vraagstukken", opdracht="Schrijf je tussenstappen op en zet de eenheid erbij.", oefeningen=[
            ("open", "Een klas van 28 kinderen. 1/4 draagt een bril. Hoeveel kinderen dragen een bril?", "28 : 4 = 7 kinderen", 2),
            ("open", "Een lat kost 1,25 euro en een gom 0,60 euro. Hoeveel betaal je voor beide?", "1,25 + 0,60 = 1,85 euro", 2),
        ]),
    ]))

# ---------------------------------------------------------------- meten
H["meten"] = ("meten-en-geld-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Meten en geld",
    onder="Lengte, gewicht en inhoud, omtrek en oppervlakte, volume met kubusjes, rekenen met euro en cent.",
    secties=[
        dict(kop="Maten om te onthouden", blokken=[
            ("fig", tabel(["Wat meet je?", "Maten", "Om te onthouden"], [
                ["lengte", "km, m, dm, cm, mm", "1 km = 1 000 m · 1 m = 100 cm · 1 cm = 10 mm"],
                ["gewicht", "kg, g", "1 kg = 1 000 g"], ["inhoud", "l, dl, cl, ml", "1 l = 1 000 ml"], ["geld", "euro, cent", "1 euro = 100 cent"]], "100%")),
            ("weetje", "Kilo betekent duizend, centi honderdste en milli duizendste. Zo weet je meteen hoeveel er in gaan."),
        ]),
        dict(kop="Omtrek", blokken=[
            ("p", "De <strong>omtrek</strong> is de lengte van de rand. Tel alle zijden op. Een rechthoek van 6 cm bij 4 cm: 6 + 4 + 6 + 4 = <strong>20 cm</strong>."),
        ]),
        dict(kop="Oppervlakte", blokken=[
            ("fig", rooster(6, 4), "6 vakjes lang en 4 vakjes breed: 6 × 4 = 24 vakjes"),
            ("p", "De <strong>oppervlakte</strong> is hoeveel vierkantjes erin passen: <strong>lengte × breedte</strong>. Je schrijft cm² of m²."),
            ("p", "1 dm² = 100 cm² (10 cm bij 10 cm). 1 m² is een vierkant van 1 m bij 1 m."),
        ]),
        dict(kop="Volume", blokken=[
            ("fig", kubusblok(), "3 × 2 = 6 kubusjes per laag, 2 lagen: 12 kubusjes"),
            ("p", "Het <strong>volume</strong> is hoeveel ruimte iets inneemt. Tel de kubusjes: per laag, en dan maal het aantal lagen."),
        ]),
        dict(kop="Rekenen met geld", blokken=[
            ("p", "Tel eerst de euro's, dan de centen. 7,50 + 1,80: 7 + 1 = 8 euro, 50 + 80 = 130 cent = 1,30 euro. Samen <strong>9,30 euro</strong>."),
            ("p", "Teruggeven: tel aan tot het bedrag dat je gaf. Van 3,40 tot 4 is 0,60, van 4 tot 5 is 1. Je krijgt <strong>1,60 euro</strong> terug."),
        ]),
    ],
    onthoud=["1 km = 1 000 m, 1 m = 100 cm, 1 cm = 10 mm.", "1 kg = 1 000 g, 1 l = 1 000 ml, 1 euro = 100 cent.",
             "Omtrek: alle zijden samen.", "Oppervlakte: lengte × breedte, in cm² of m².", "Volume: tel de kubusjes."]),
    dict(vak="Wiskunde", niveau=READY, titel="Meten en geld", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Omzetten", opdracht="Vul in.", oefeningen=[
            ("rij", [("4 m = ... cm", "400"), ("50 mm = ... cm", "5"), ("3 km = ... m", "3 000"), ("1 m 20 cm = ... cm", "120")], "", W),
            ("rij", [("5 kg = ... g", "5 000"), ("2 l = ... ml", "2 000"), ("half kg = ... g", "500"), ("4 euro = ... cent", "400")], "", W),
        ]),
        dict(kop="Welke maat past?", oefeningen=[
            ("rij", [("een potlood: 15 ...", "cm"), ("een appel: 150 ...", "g"), ("een emmer: 10 ...", "l"), ("Gent – Brussel: 55 ...", "km")], "Schrijf de maat.", W),
        ]),
        dict(kop="Omtrek en oppervlakte", opdracht="Schrijf je berekening op.", oefeningen=[
            ("open", "Een rechthoek is 7 cm lang en 3 cm breed. Bereken de omtrek.", "7 + 3 + 7 + 3 = 20 cm", 2),
            ("open", "Bereken de oppervlakte van dezelfde rechthoek.", "7 × 3 = 21 cm²", 1),
            ("open", "Een vierkant heeft zijden van 6 m. Bereken de omtrek en de oppervlakte.", "omtrek 4 × 6 = 24 m; oppervlakte 6 × 6 = 36 m²", 2),
            ("teken", "Teken in de ruitjes een rechthoek met een oppervlakte van 12 vakjes. Hoe lang en hoe breed is hij?", "bv. 4 bij 3, 6 bij 2 of 12 bij 1", 40),
        ]),
        dict(kop="Volume", oefeningen=[
            ("fig", [(kubusblok(), "12 kubusjes")], "Hoeveel kubusjes zijn het?"),
            ("open", "Een doos is 4 kubusjes lang, 3 breed en 2 hoog. Hoeveel kubusjes passen erin?", "4 × 3 = 12 per laag; 12 × 2 = 24 kubusjes", 2),
        ]),
        dict(kop="Rekenen met geld", opdracht="Schrijf je tussenstappen op.", oefeningen=[
            ("open", "Een boek kost 6,40 euro en een strip 3,90 euro. Hoeveel betaal je samen?", "6 + 3 = 9 euro; 40 + 90 = 130 cent = 1,30; samen 10,30 euro", 2),
            ("open", "Je betaalt met 10 euro voor een spel van 7,25 euro. Hoeveel krijg je terug?", "van 7,25 tot 8 is 0,75; van 8 tot 10 is 2; samen 2,75 euro", 2),
            ("open", "4 ijsjes van 1,50 euro. Hoeveel kost dat?", "4 × 1,50 = 6,00 euro", 1),
        ]),
    ]))

# ---------------------------------------------------------------- tijd
H["tijd"] = ("tijd-en-temperatuur-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Tijd en temperatuur",
    onder="Klok lezen tot op de minuut, analoog en digitaal, kalender, tijdsduur en temperatuur.",
    secties=[
        dict(kop="De klok", blokken=[
            ("fig", klok(3, 0) + " " + klok(5, 30) + " " + klok(8, 15) + " " + klok(10, 45), "drie uur · half zes · kwart over acht · kwart voor elf"),
            ("p", "De <strong>kleine wijzer</strong> (oranje) wijst het uur aan. De <strong>grote wijzer</strong> de minuten: elk cijfer is 5 minuten verder."),
            ("fig", tabel(["Grote wijzer op", "12", "3", "6", "9"], [["Minuten na het uur", "0 (vol uur)", "15 (kwart over)", "30 (half)", "45 (kwart voor)"]], "100%")),
        ]),
        dict(kop="Digitale klok", blokken=[
            ("p", "Een digitale klok telt de uren van 0 tot 23. Na de middag tel je 12 bij het uur: 3 uur 's middags = <strong>15.00</strong>, kwart voor acht 's avonds = <strong>19.45</strong>."),
        ]),
        dict(kop="Kalender", blokken=[
            ("fig", tabel(["31 dagen", "30 dagen", "28 of 29 dagen"], [["januari, maart, mei, juli, augustus, oktober, december", "april, juni, september, november", "februari"]], "100%")),
            ("weetje", "Tel op je knokkels: een knokkel is een maand met 31 dagen, een putje een maand met 30 (of februari)."),
            ("p", "1 jaar = 12 maanden = 52 weken = 365 dagen. 1 week = 7 dagen. 1 dag = 24 uur. 1 uur = 60 minuten."),
        ]),
        dict(kop="Tijdsduur", blokken=[
            ("kader", "Van 14.15 tot 15.45<br>Stap 1: tel volle uren: 14.15 → 15.15 = 1 uur<br>Stap 2: tel de minuten: 15.15 → 15.45 = 30 minuten<br>Samen: <strong>1 uur en 30 minuten</strong>"),
        ]),
        dict(kop="Temperatuur", blokken=[
            ("p", "Temperatuur meet je met een thermometer in <strong>graden Celsius (°C)</strong>. Water bevriest bij 0 °C en kookt bij 100 °C. Je lichaam is ongeveer 37 °C."),
            ("p", "Onder nul schrijf je een minteken: −3 °C is 3 graden onder nul, kouder dan 0 °C."),
        ]),
    ],
    onthoud=["Kleine wijzer: uur. Grote wijzer: minuten.", "Na de middag: +12 op de digitale klok.",
             "Tijdsduur: eerst volle uren, dan minuten.", "0 °C: water bevriest. 100 °C: water kookt."]),
    dict(vak="Wiskunde", niveau=READY, titel="Tijd en temperatuur", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Hoe laat is het?", opdracht="Schrijf het uur onder de klok.", oefeningen=[
            ("fig", [(klok(7, 0, 100), "7.00 (zeven uur)"), (klok(2, 30, 100), "2.30 (half drie)"), (klok(9, 15, 100), "9.15 (kwart over negen)"), (klok(4, 45, 100), "4.45 (kwart voor vijf)")], ""),
            ("fig", [(klok(1, 10, 100), "1.10 (tien over een)"), (klok(6, 25, 100), "6.25 (vijf voor half zeven)"), (klok(11, 50, 100), "11.50 (tien voor twaalf)")], ""),
        ]),
        dict(kop="Teken de wijzers", oefeningen=[
            ("kleur", [(klok(None, 0, 110), "Teken: half vier.", "kleine wijzer tussen 3 en 4, grote op 6"),
                       (klok(None, 0, 110), "Teken: kwart over tien.", "kleine wijzer net na 10, grote op 3"),
                       (klok(None, 0, 110), "Teken: 20 over 8.", "kleine wijzer tussen 8 en 9, grote op 4")]),
        ]),
        dict(kop="Digitale klok", oefeningen=[
            ("rij", [("4 uur 's middags", "16.00"), ("half negen 's avonds", "20.30"), ("kwart voor zeven 's morgens", "6.45")], "Schrijf zoals een digitale klok.", W),
        ]),
        dict(kop="Kalender", oefeningen=[
            ("rij", [("dagen in een week", "7"), ("maanden in een jaar", "12"), ("dagen in april", "30"), ("dagen in 2 weken", "14")], "Hoeveel?", W),
            ("open", "Vandaag is het woensdag 10 maart. Welke dag en datum is het over een week?", "woensdag 17 maart", 1),
        ]),
        dict(kop="Tijdsduur", opdracht="Schrijf je tussenstappen op.", oefeningen=[
            ("open", "De zwemles begint om 16.30 en eindigt om 17.15. Hoe lang duurt de les?", "16.30 → 17.00 = 30 min; 17.00 → 17.15 = 15 min; samen 45 minuten", 2),
            ("open", "De trein vertrekt om 9.45 en de rit duurt 1 uur en 20 minuten. Hoe laat komt hij aan?", "9.45 + 1 uur = 10.45; + 20 min = 11.05", 2),
        ]),
        dict(kop="Temperatuur", oefeningen=[
            ("rij", [("4 °C, 7 graden warmer", "11 °C"), ("2 °C, 5 graden kouder", "−3 °C"), ("−1 °C, 6 graden warmer", "5 °C")], "Hoe warm is het nu?", W),
            ("waar", "Bij −5 °C kan er ijs op een vijver liggen.", True),
            ("waar", "Een kopje thee is ongeveer 10 °C.", False),
        ]),
    ]))

# ---------------------------------------------------------------- meetkunde
H["meetkunde"] = ("meetkunde-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Meetkunde",
    onder="Hoeken, vlakke figuren, evenwijdig en loodrecht, ruimtefiguren, symmetrie, aanzichten en een rooster.",
    secties=[
        dict(kop="Hoeken", blokken=[
            ("fig", hoeken()),
            ("p", "Een <strong>rechte hoek</strong> is zoals de hoek van een blad papier. Een <strong>scherpe</strong> hoek is kleiner, een <strong>stompe</strong> hoek groter."),
            ("weetje", "Met de hoek van een blad papier kan je elke hoek testen: past hij erin, dan is hij scherp."),
        ]),
        dict(kop="Vlakke figuren", blokken=[
            ("fig", figuren()),
            ("fig", tabel(["Figuur", "Zijden", "Hoeken", "Let op"], [["vierkant", "4 even lang", "4 rechte", ""], ["rechthoek", "overstaande even lang", "4 rechte", "een vierkant is ook een rechthoek"],
                ["driehoek", "3", "3", "hoogstens één rechte hoek"], ["ruit", "4 even lang", "niet altijd recht", ""], ["cirkel", "geen", "geen", "rond"]], "100%")),
        ]),
        dict(kop="Evenwijdig en loodrecht", blokken=[
            ("fig", lijnen()),
            ("p", "<strong>Evenwijdige</strong> lijnen raken elkaar nooit, zoals de rails van een trein. <strong>Loodrechte</strong> lijnen maken een rechte hoek."),
        ]),
        dict(kop="Ruimtefiguren", blokken=[
            ("fig", tabel(["Ruimtefiguur", "Zoals", "Vlakken"], [["kubus", "een dobbelsteen", "6 vierkanten"], ["balk", "een schoenendoos", "6 rechthoeken"],
                ["bol", "een bal", "geen plat vlak"], ["cilinder", "een blikje", "2 cirkels en een gebogen vlak"], ["kegel", "een ijshoorntje", "1 cirkel en een punt"], ["piramide", "de piramides in Egypte", "een grondvlak en driehoeken"]], "100%")),
        ]),
        dict(kop="Symmetrie en spiegelen", blokken=[
            ("p", "Een <strong>symmetrieas</strong> verdeelt een figuur in twee spiegelbeelden. Plooi je de figuur op de as, dan vallen de helften precies op elkaar. Een vierkant heeft 4 assen, een rechthoek 2."),
            ("p", "Bij spiegelen blijft de figuur even groot, maar links en rechts wisselen."),
        ]),
        dict(kop="Aanzichten en rooster", blokken=[
            ("p", "Van boven zie je een staande cilinder als een cirkel, van voren als een rechthoek."),
            ("p", "In een rooster noem je eerst de <strong>letter</strong> (kolom) en dan het <strong>cijfer</strong> (rij): C4 is kolom C, rij 4."),
        ]),
    ],
    onthoud=["Recht, scherp (kleiner), stomp (groter).", "Evenwijdig raakt nooit, loodrecht maakt een rechte hoek.",
             "Vlakke figuren zijn plat, ruimtefiguren kan je vastnemen.", "Een symmetrieas maakt twee spiegelbeelden.", "Rooster: eerst letter, dan cijfer."]),
    dict(vak="Wiskunde", niveau=READY, titel="Meetkunde", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Hoeken", oefeningen=[
            ("fig", [(hoek("stomp"), "stomp"), (hoek("recht"), "recht"), (hoek("scherp"), "scherp")], "Schrijf onder elke hoek of hij recht, scherp of stomp is."),
            ("teken", "Teken in de ruitjes een rechte hoek, een scherpe hoek en een stompe hoek.", "eigen tekening", 40),
        ]),
        dict(kop="Figuren", oefeningen=[
            ("rij", [("vierkant: hoeken", "4"), ("driehoek: zijden", "3"), ("zeshoek: hoeken", "6"), ("cirkel: hoeken", "0")], "Hoeveel?", W),
            ("teken", "Teken in de ruitjes een rechthoek van 5 bij 3 vakjes en een vierkant van 3 bij 3 vakjes.", "eigen tekening", 45),
            ("waar", "Elk vierkant is ook een rechthoek.", True),
            ("waar", "Een driehoek kan vier hoeken hebben.", False),
        ]),
        dict(kop="Evenwijdig en loodrecht", oefeningen=[
            ("teken", "Teken twee evenwijdige lijnen en twee loodrechte lijnen. Gebruik je lat.", "eigen tekening", 40),
            ("open", "Zoek in de klas of thuis twee dingen met evenwijdige randen en schrijf ze op.", "bv. de randen van een deur, van een boek, de lijnen op je blad", 2),
        ]),
        dict(kop="Ruimtefiguren", oefeningen=[
            ("rij", [("een dobbelsteen", "kubus"), ("een tennisbal", "bol"), ("een rol koekjes", "cilinder"), ("een feesthoedje", "kegel")], "Welke ruimtefiguur?", "120px"),
        ]),
        dict(kop="Symmetrie", oefeningen=[
            ("rij", [("A", "ja"), ("F", "nee"), ("H", "ja"), ("L", "nee"), ("M", "ja"), ("O", "ja")], "Heeft de hoofdletter een symmetrieas? Schrijf ja of nee.", W),
            ("teken", "Teken links in de ruitjes een halve boom of een half huisje tegen een lijn. Spiegel het aan de andere kant.", "eigen tekening, beide helften gelijk", 45),
        ]),
        dict(kop="Rooster", oefeningen=[
            ("open", "Teken in de ruitjes van de vorige oefening letters A tot E bovenaan en cijfers 1 tot 5 links. Zet een kruisje op B3 en een bolletje op D5.", "kruisje: kolom B, rij 3; bolletje: kolom D, rij 5", 1),
            ("rij", [("B2, 2 naar rechts", "D2"), ("C4, 1 naar boven", "C3"), ("E1, 3 naar links", "B1")], "Waar kom je uit? (rij 1 staat bovenaan)", W),
        ]),
    ]))

# ---------------------------------------------------------------- vraagstukken
H["vraagstukken"] = ("vraagstukken-en-tabellen-ready", dict(
    vak="Wiskunde", niveau=READY, titel="Vraagstukken en tabellen",
    onder="Stappenplan voor vraagstukken, verhoudingstabel, tabellen en diagrammen, Venndiagram.",
    secties=[
        dict(kop="Het stappenplan", blokken=[
            ("kader", "<strong>1. Lees</strong> de vraag twee keer.<br><strong>2. Wat weet ik?</strong> Onderlijn de getallen.<br>"
                      "<strong>3. Wat moet ik vinden?</strong> Omcirkel de vraag.<br><strong>4. Reken</strong> en schrijf je tussenstappen.<br>"
                      "<strong>5. Kan het kloppen?</strong> Een klas van 500 kinderen bestaat niet."),
            ("fig", tabel(["Woorden in de vraag", "Vaak deze bewerking"], [["samen, erbij, in totaal", "+"], ["over, verschil, hoeveel meer", "−"],
                ["keer, elk, per", "×"], ["verdelen, eerlijk, hoeveel per", ":"]], "100%")),
            ("weetje", "Een tekening of schema helpt bijna altijd."),
        ]),
        dict(kop="De verhoudingstabel", blokken=[
            ("fig", tabel(["appels", "2", "4", "8"], [["euro", "1", "2", "4"]], "60%"), "wat je boven × 2 doet, doe je onder ook × 2"),
            ("p", "Wat je in de ene rij doet, doe je in de andere rij ook. Zo vind je snel de prijs van 8 appels."),
        ]),
        dict(kop="Tabellen en diagrammen", blokken=[
            ("fig", tabel(["Dag", "ma", "di", "wo", "do"], [["Bezoekers", "12", "18", "9", "15"]], "80%")),
            ("p", "Kijk eerst naar de <strong>titel</strong> en wat er in de rijen en kolommen staat. In een <strong>staafdiagram</strong> is de hoogste staaf het grootste getal. In een <strong>pictogram</strong> staat een tekentje voor een aantal."),
        ]),
        dict(kop="Venndiagram", blokken=[
            ("fig", svg(300, 150, f'<circle cx="110" cy="75" r="62" fill="#f3c9a855" stroke="{ORANJE}" stroke-width="2.5"/><circle cx="190" cy="75" r="62" fill="#7a5aa622" stroke="{PAARS}" stroke-width="2.5"/>'
                         f'<text x="80" y="22" font-size="12">even</text><text x="190" y="22" font-size="12">groter dan 5</text>'
                         f'<text x="80" y="80" font-size="15">2 4</text><text x="140" y="80" font-size="15">6 8</text><text x="205" y="80" font-size="15">7 9</text><text x="12" y="140" font-size="15">1 3</text>'),
             "6 en 8 zijn even én groter dan 5: ze staan in het midden"),
            ("p", "Wat bij beide groepen hoort, staat in het stuk waar de cirkels <strong>overlappen</strong>. Wat bij geen van beide hoort, staat erbuiten."),
        ]),
    ],
    onthoud=["Lees, zoek wat je weet, zoek wat je moet vinden, reken, kijk na.", "Verhoudingstabel: wat je boven doet, doe je onder ook.",
             "Tabel of diagram: eerst de titel lezen.", "Venndiagram: het midden hoort bij beide."]),
    dict(vak="Wiskunde", niveau=READY, titel="Vraagstukken en tabellen", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Welke bewerking?", oefeningen=[
            ("rij", [("5 rijen van 8 stoelen", "×"), ("30 snoepjes eerlijk over 6 kinderen", ":"), ("12 kinderen en er komen er 5 bij", "+"), ("hoeveel meer is 20 dan 13", "−")], "Schrijf +, −, × of :.", W),
        ]),
        dict(kop="Vraagstukken", opdracht="Volg het stappenplan. Schrijf je tussenstappen en de eenheid.", oefeningen=[
            ("open", "Een doos bevat 8 kleurpotloden. Juf koopt 7 dozen. Hoeveel potloden zijn dat?", "7 × 8 = 56 potloden", 2),
            ("open", "Lena heeft 85 euro gespaard. Ze koopt schoenen van 49 euro. Hoeveel heeft ze nog?", "85 − 49 = 36 euro", 2),
            ("open", "In een bus zitten 32 mensen. Er stappen er 11 uit en 7 in. Hoeveel zitten er nu?", "32 − 11 = 21; 21 + 7 = 28 mensen", 3),
            ("open", "Opa verdeelt 60 euro eerlijk over zijn 4 kleinkinderen. Hoeveel krijgt elk?", "60 : 4 = 15 euro", 2),
        ]),
        dict(kop="Verhoudingstabel", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["tickets", "1", "2", "5", "10"], [["euro", "4", None, None, None]], "8 · 20 · 40", "70px"),
            ("tabel", ["pakken", "1", "3", "6"], [["flessen", "6", None, None]], "18 · 36", "70px"),
        ]),
        dict(kop="Tabel lezen", oefeningen=[
            ("tekst", tabel(["Hoe kom je naar school?", "te voet", "fiets", "auto", "bus"], [["Aantal kinderen", "7", "12", "5", "4"]], "100%")),
            ("rij", [("Hoeveel kinderen met de fiets?", "12"), ("Hoeveel kinderen in totaal?", "28"), ("Hoeveel meer met de fiets dan met de auto?", "7")], "", W),
            ("teken", "Maak in de ruitjes een staafdiagram van de tabel: één vakje per kind.", "staven van 7, 12, 5 en 4 vakjes hoog", 55),
        ]),
        dict(kop="Venndiagram", oefeningen=[
            ("open", "Zet de getallen 3, 4, 10, 12, 15, 20 in een Venndiagram met de cirkels 'even' en 'groter dan 10'. Welke staan in het midden?", "12 en 20 (even én groter dan 10); 4 en 10 enkel even; 15 enkel groter dan 10; 3 erbuiten", 3),
            ("waar", "Een getal dat buiten beide cirkels staat, hoort bij geen van beide groepen.", True),
        ]),
    ]))


if __name__ == "__main__":
    kies = sys.argv[1:] or list(H)
    for k in kies:
        naam, leer, oefen = H[k]
        maak(naam, "wiskunde", leer, oefen, ruitjes=True)
