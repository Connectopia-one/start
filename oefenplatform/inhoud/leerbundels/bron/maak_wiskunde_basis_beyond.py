# -*- coding: utf-8 -*-
r"""De leerbundels voor wiskunde basis op 🌍 Beyond doorstroom.

Gebaseerd op de vakfiche wiskunde basis voor de derde graad doorstroom, de
vragen staan in beyond/wiskunde-basis.json (gemaakt door
beyond/bron/bouw_wiskunde_basis.py). Twaalf gewone thema's en zeven thema's
die enkel voor de richtingen met bedrijfswetenschappen gelden; die laatste
dragen "Bedrijfswetenschappen:" in hun titel, net zoals de hoofdstukken.

Eén bundel per thema: deel 1 en deel 2 behandelen dezelfde stof met andere
vragen, dus Kim laadt de bundel twee keer op. Elke bundel dekt elke vraag
van zijn twee hoofdstukken. Wiskunde staat in echte notatie tussen \( en \),
net zoals in de vragen.

De sleutels eindigen op "-beyond-doorstroom", omdat 🚀 Boost doorstroom een
vak met dezelfde naam heeft (zie maak_wiskunde_basis.py) en enkele titels
daar bijna gelijk zijn.

Kim, 9 en 11 november 2026: bundels voor elk vak dat er nog geen had, op een
witte achtergrond.
"""
import math
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Wiskunde basis"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[slug + "-beyond-doorstroom"] = b


KLEUR = {"v": svg.FOREST, "a": svg.AMBER, "g": svg.DIM, "b": svg.INFO if hasattr(svg, "INFO") else "#3b6ea5"}


def plot(functies, xmin, xmax, ymin, ymax, breedte=320, hoogte=220, punten=(), vertikaal=(),
         horizontaal=(), stap_x=1, stap_y=1, xlabel="x", ylabel="y", vlak=None, rechthoeken=(), toon_een=True):
    r"""Een assenstelsel met een of meer grafieken.

    functies:   (f, kleur, label) met f een gewone Python-functie; kleur "v", "a", "g" of "b"
    punten:     (x, y, label)
    vertikaal:  x-waarden waar een stippellijn komt (asymptoot, symmetrieas)
    horizontaal: y-waarden met een stippellijn
    vlak:       (f, a, b): de oppervlakte onder f tussen a en b inkleuren
    """
    L, R, T, B = 26, 16, 14, 24
    w, h = breedte - L - R, hoogte - T - B
    X = lambda x: L + (x - xmin) / (xmax - xmin) * w
    Y = lambda y: T + (ymax - y) / (ymax - ymin) * h
    d = []
    # raster
    x = math.ceil(xmin / stap_x) * stap_x
    while x <= xmax + 1e-9:
        d.append(f'<line x1="{X(x):.1f}" y1="{T}" x2="{X(x):.1f}" y2="{T+h}" stroke="#ece7db" stroke-width="1"/>')
        x += stap_x
    y = math.ceil(ymin / stap_y) * stap_y
    while y <= ymax + 1e-9:
        d.append(f'<line x1="{L}" y1="{Y(y):.1f}" x2="{L+w}" y2="{Y(y):.1f}" stroke="#ece7db" stroke-width="1"/>')
        y += stap_y
    if vlak:
        # (f, a, b) kleurt tot de x-as, (f, a, b, g) tussen f en g
        f, a, b = vlak[:3]
        g = vlak[3] if len(vlak) > 3 else None
        boven = [(X(a + (b - a) * i / 80), Y(f(a + (b - a) * i / 80))) for i in range(81)]
        if g:
            pts = boven + [(X(b - (b - a) * i / 80), Y(g(b - (b - a) * i / 80))) for i in range(81)]
        else:
            pts = [(X(a), Y(0))] + boven + [(X(b), Y(0))]
        d.append('<polygon points="' + " ".join(f"{p:.1f},{q:.1f}" for p, q in pts)
                 + f'" fill="{svg.AMBER}" fill-opacity=".22" stroke="none"/>')
    for x0, x1, hh in rechthoeken:
        d.append(f'<rect x="{X(x0):.1f}" y="{min(Y(hh), Y(0)):.1f}" width="{X(x1) - X(x0):.1f}" height="{abs(Y(0) - Y(hh)):.1f}" '
                 f'fill="{svg.FOREST}" fill-opacity=".14" stroke="{svg.FOREST}" stroke-width="1.2"/>')
    # assen
    if ymin <= 0 <= ymax:
        d.append(f'<line x1="{L}" y1="{Y(0):.1f}" x2="{L+w+6}" y2="{Y(0):.1f}" stroke="{svg.INK}" stroke-width="1.5"/>')
        d.append(svg._tekst(L + w + 8, Y(0) + 4, xlabel, 10.5, svg.INK, "start", True))
    if xmin <= 0 <= xmax:
        d.append(f'<line x1="{X(0):.1f}" y1="{T-6}" x2="{X(0):.1f}" y2="{T+h}" stroke="{svg.INK}" stroke-width="1.5"/>')
        d.append(svg._tekst(X(0) + 5, T - 2, ylabel, 10.5, svg.INK, "start", True))
    # getallen bij de assen: enkel 1 op elke as, om niet te overladen
    if toon_een and xmin < 1 < xmax and ymin <= 0 <= ymax:
        d.append(svg._tekst(X(1), Y(0) + 12, "1", 9, svg.DIM))
    if toon_een and ymin < 1 < ymax and xmin <= 0 <= xmax:
        d.append(svg._tekst(X(0) - 5, Y(1) + 3, "1", 9, svg.DIM, "end"))
    for xv in vertikaal:
        d.append(f'<line x1="{X(xv):.1f}" y1="{T}" x2="{X(xv):.1f}" y2="{T+h}" stroke="{svg.DIM}" stroke-width="1.3" stroke-dasharray="5 4"/>')
    for yv in horizontaal:
        d.append(f'<line x1="{L}" y1="{Y(yv):.1f}" x2="{L+w}" y2="{Y(yv):.1f}" stroke="{svg.DIM}" stroke-width="1.3" stroke-dasharray="5 4"/>')
    d.append(f'<clipPath id="c{id(functies)}"><rect x="{L}" y="{T}" width="{w}" height="{h}"/></clipPath>')
    for f, k, label in functies:
        stukken, huidig = [], []
        n = 300
        for i in range(n + 1):
            xv = xmin + (xmax - xmin) * i / n
            try:
                yv = f(xv)
            except (ZeroDivisionError, ValueError):
                yv = None
            if yv is None or not (ymin - 50 * (ymax - ymin) < yv < ymax + 50 * (ymax - ymin)) or isinstance(yv, complex):
                if huidig: stukken.append(huidig); huidig = []
                continue
            if huidig and abs(yv - huidig[-1][2]) > 3 * (ymax - ymin):
                stukken.append(huidig); huidig = []
            huidig.append((X(xv), Y(yv), yv))
        if huidig: stukken.append(huidig)
        for s in stukken:
            d.append(f'<polyline clip-path="url(#c{id(functies)})" points="' + " ".join(f"{p:.1f},{q:.1f}" for p, q, _ in s)
                     + f'" fill="none" stroke="{KLEUR[k]}" stroke-width="2.3"/>')
        if label:
            # label bij het laatste zichtbare punt
            zicht = [(p, q) for s in stukken for p, q, _ in s if T <= q <= T + h]
            if zicht:
                p, q = zicht[-1]
                d.append(svg._tekst(min(p, L + w - 2) - 2, max(q - 6, T + 10), label, 10.5, KLEUR[k], "end", True))
    for xv, yv, label in punten:
        d.append(f'<circle cx="{X(xv):.1f}" cy="{Y(yv):.1f}" r="3.6" fill="{svg.INK}"/>')
        if label:
            d.append(svg._tekst(X(xv) + 6, Y(yv) - 6, label, 10, svg.INK, "start", True))
    return svg._svg(breedte, hoogte, "".join(d))


# ───────────────────────── 1. Machtswortels, machten en logaritmen
zet("machtswortels-machten-en-logaritmen",
    titel="Machtswortels, machten en logaritmen",
    onder="Wortels als machten schrijven, rekenen met rationale exponenten, en de logaritme als de exponent die je zoekt.",
    secties=[
        dict(kop="Machtswortels", blokken=[
            ("p", r"De \(n\)-de machtswortel van \(a\) is het getal dat tot de \(n\)-de macht \(a\) geeft. "
                  r"\(\sqrt[3]{64}=4\) want \(4^{3}=64\), en \(\sqrt[4]{81}=3\) want \(3^{4}=81\). Een kubus met inhoud "
                  r"\(343\ \text{cm}^{3}\) heeft een ribbe van \(\sqrt[3]{343}=7\) cm."),
            ("kader", tabel(["", r"oneven \(n\)", r"even \(n\)"],
                            [[r"positief getal", r"\(\sqrt[3]{8}=2\)", r"\(\sqrt[4]{16}=2\)"],
                             [r"negatief getal", r"bestaat: \(\sqrt[3]{-125}=-5\)", r"bestaat <strong>niet</strong> in \(\mathbb{R}\): \(\sqrt[4]{-16}\)"]])),
            ("p", r"Met je rekentoestel: \(\sqrt[5]{200}\approx 2{,}89\). Let op: een wortel van een som is <strong>niet</strong> "
                  r"de som van de wortels. \(\sqrt{9+16}=\sqrt{25}=5\), maar \(\sqrt{9}+\sqrt{16}=7\). Een product mag je wel samen "
                  r"nemen: \(\sqrt[3]{2}\cdot\sqrt[3]{4}=\sqrt[3]{8}=2\). En \(\left(\sqrt[3]{5}\right)^{3}=5\)."),
        ]),
        dict(kop="Machten met een rationale exponent", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(a^{\frac{m}{n}}=\sqrt[n]{a^{m}}\)</strong> en "
                      r"<strong>\(a^{-n}=\dfrac{1}{a^{n}}\)</strong> (met \(a>0\))</p>"),
            ("kader", tabel(["schrijfwijze", "is gelijk aan"],
                            [[r"\(\sqrt[5]{x^{3}}\)", r"\(x^{\frac{3}{5}}\)"],
                             [r"\(7^{\frac{2}{3}}\)", r"\(\sqrt[3]{7^{2}}\)"],
                             [r"\(8^{\frac{2}{3}}\)", r"\(\left(\sqrt[3]{8}\right)^{2}=2^{2}=4\)"],
                             [r"\(16^{-\frac{1}{2}}\)", r"\(\dfrac{1}{\sqrt{16}}=\dfrac{1}{4}\)"],
                             [r"\(\dfrac{1}{\sqrt[4]{x^{3}}}\)", r"\(x^{-\frac{3}{4}}\)"],
                             [r"\(2^{\frac{1}{2}}\)", r"\(\sqrt{2}\), en dus <strong>niet</strong> \(\dfrac{1}{2^{2}}\)"]])),
            ("p", r"Een negatieve exponent betekent <strong>omkeren</strong>. Een breuk als exponent betekent <strong>een wortel</strong>."),
        ]),
        dict(kop="Rekenregels", blokken=[
            ("kader", tabel(["regel", "voorbeeld"],
                            [[r"\(a^{m}\cdot a^{n}=a^{m+n}\)", r"\(a^{\frac{1}{2}}\cdot a^{\frac{1}{3}}=a^{\frac{5}{6}}\)"],
                             [r"\(\dfrac{a^{m}}{a^{n}}=a^{m-n}\)", r"\(\dfrac{b^{\frac{5}{2}}}{b^{\frac{1}{2}}}=b^{2}\)"],
                             [r"\(\left(a^{m}\right)^{n}=a^{m\cdot n}\)", r"\(\left(x^{\frac{3}{4}}\right)^{2}=x^{\frac{3}{2}}\)"]])),
            ("p", r"Zo kan je ook wortels met verschillende wortelexponenten samen nemen: "
                  r"\(\sqrt{a}\cdot\sqrt[3]{a}=a^{\frac{1}{2}}\cdot a^{\frac{1}{3}}=a^{\frac{5}{6}}=\sqrt[6]{a^{5}}\)."),
            ("p", r"Welk getal is het grootst? Reken ze om: \(27^{\frac{2}{3}}=\left(\sqrt[3]{27}\right)^{2}=9\) is groter dan "
                  r"bijvoorbeeld \(16^{\frac{1}{2}}=4\) of \(32^{\frac{1}{5}}=2\)."),
        ]),
        dict(kop="De logaritme", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(\log_{a}x=y\iff a^{y}=x\)</strong></p>"
                      r"<p>De logaritme is <strong>de exponent die je zoekt</strong>. Het grondtal \(a\) is positief en niet \(1\), en \(x\) is positief.</p>"),
            ("kader", tabel(["opgave", "denk", "antwoord"],
                            [[r"\(\log_{2}32\)", r"\(2^{?}=32\)", r"\(5\)"],
                             [r"\(\log 1000\)", r"\(10^{?}=1000\) (\(\log\) zonder grondtal = grondtal \(10\))", r"\(3\)"],
                             [r"\(\log_{3}\dfrac{1}{9}\)", r"\(3^{?}=\dfrac{1}{9}=3^{-2}\)", r"\(-2\)"],
                             [r"\(\log_{5}1\)", r"\(5^{?}=1\)", r"\(0\)"],
                             [r"\(\log_{4}2\)", r"\(4^{?}=2\)", r"\(\tfrac{1}{2}\), dus niet \(2\)"],
                             [r"\(\log_{2}(-8)\)", r"\(2^{?}\) is nooit negatief", r"bestaat niet in \(\mathbb{R}\)"]])),
            ("p", r"Het getal <strong>\(e\approx 2{,}718\)</strong> is het grondtal van de <strong>natuurlijke logaritme</strong> "
                  r"\(\ln\). Zo is \(\ln e^{4}=4\)."),
        ]),
        dict(kop="Rekenregels voor logaritmen", blokken=[
            ("kader", tabel(["regel", "voorbeeld"],
                            [[r"\(\log_{a}(x\cdot y)=\log_{a}x+\log_{a}y\)", r"\(\log_{6}4+\log_{6}9=\log_{6}36=2\); \(\log 2+\log 5=\log 10=1\)"],
                             [r"\(\log_{a}\dfrac{x}{y}=\log_{a}x-\log_{a}y\)", r"\(\log_{2}48-\log_{2}3=\log_{2}16=4\)"],
                             [r"\(\log_{a}x^{r}=r\log_{a}x\)", r"\(\log_{a}x^{5}=5\log_{a}x\); \(\ln x^{2}=2\ln x\)"],
                             [r"\(\log_{a}x=\dfrac{\log x}{\log a}\)", r"\(\log_{3}20=\dfrac{\log 20}{\log 3}\approx 2{,}73\)"]])),
            ("p", r"Die laatste regel heb je nodig op een rekentoestel dat enkel \(\log\) en \(\ln\) kent. Opgelet: "
                  r"\(\dfrac{\log 8}{\log 2}=\log_{2}8=3\), en dat is <strong>niet</strong> \(\log 4\)."),
            ("p", r"Een exponentiële vergelijking los je zo op: uit \(2^{x}=10\) volgt \(x=\log_{2}10=\dfrac{\log 10}{\log 2}\approx 3{,}32\)."),
        ]),
    ],
    onthoud=[
        r"\(\sqrt[n]{a}\) met even \(n\) bestaat niet voor negatieve \(a\); met oneven \(n\) wel.",
        r"\(a^{\frac{m}{n}}=\sqrt[n]{a^{m}}\) en \(a^{-n}=\dfrac{1}{a^{n}}\).",
        r"Exponenten: optellen bij vermenigvuldigen, aftrekken bij delen, vermenigvuldigen bij een macht van een macht.",
        r"\(\log_{a}x=y\) betekent \(a^{y}=x\); \(\log\) heeft grondtal \(10\), \(\ln\) grondtal \(e\).",
        r"\(\log(xy)=\log x+\log y\), \(\log\frac{x}{y}=\log x-\log y\), \(\log x^{r}=r\log x\).",
        r"\(\log_{a}x=\dfrac{\log x}{\log a}\).",
    ])


# ───────────────────────── 2. Grafisch onderzoek van een functie
zet("grafisch-onderzoek-van-een-functie",
    titel="Grafisch onderzoek van een functie",
    onder="Uit een grafiek, tabel of voorschrift aflezen wat een functie doet, en wat dat betekent in een situatie.",
    secties=[
        dict(kop="Domein, bereik en snijpunten", blokken=[
            ("kader", tabel(["begrip", "betekenis", "voorbeeld"],
                            [[r"domein \(\text{dom} f\)", r"alle \(x\)-waarden waarvoor \(f(x)\) bestaat", r"\(f(x)=\dfrac{1}{x-2}\): \(\mathbb{R}\setminus\{2\}\)"],
                             [r"bereik \(\text{ber} f\)", r"alle \(y\)-waarden die \(f\) aanneemt", r"\(f(x)=x^{2}\): \([0,+\infty[\), dus niet \(\mathbb{R}\)"],
                             [r"nulwaarde", r"de \(x\)-waarde van een snijpunt met de \(x\)-as", r"\(f(x)=3x-6\): \(x=2\)"],
                             [r"nulpunt", r"de coördinaat van dat snijpunt", r"\((2,0)\)"],
                             [r"snijpunt met de \(y\)-as", r"\((0,f(0))\)", r"\(f(x)=3x-6\): \((0,-6)\)"]])),
            ("p", r"Een functie heeft <strong>hoogstens één</strong> snijpunt met de \(y\)-as (anders hoorden er twee \(y\)-waarden bij \(x=0\)). "
                  r"Niet elke functie heeft een nulwaarde: \(f(x)=x^{2}+1\) raakt de \(x\)-as nooit."),
            ("p", r"Daalt de grafiek tot \(x=1\), bereikt ze in \((1,-4)\) haar laagste punt en stijgt ze daarna, dan is het bereik \([-4,+\infty[\)."),
        ]),
        dict(kop="Tekenverloop", blokken=[
            ("p", r"Een tekenverloop toont <strong>waar de grafiek boven of onder de \(x\)-as ligt en waar ze de \(x\)-as snijdt</strong>: "
                  r"\(+\) erboven, \(-\) eronder, \(0\) in een nulwaarde."),
            ("fig", plot([(lambda x: 0.5 * (x + 1) * (x - 3), "v", "f")], -3, 5, -3, 4, punten=[(-1, 0, ""), (3, 0, "")]),
             r"\(f(x)<0\) op \(]-1,3[\) en \(f(x)>0\) voor \(x<-1\) en \(x>3\)."),
            ("kader", tabel([r"\(x\)", "", r"\(-1\)", "", r"\(3\)", ""],
                            [[r"\(f(x)\)", r"\(+\)", r"\(0\)", r"\(-\)", r"\(0\)", r"\(+\)"]])),
        ]),
        dict(kop="Stijgen, dalen en extrema", blokken=[
            ("p", r"Op elk interval van het domein kijk je hoe de functie verloopt:"),
            ("kader", tabel(["verloop", "wat zie je", "voorbeeld"],
                            [["toenemende stijging", "stijgt en wordt steeds steiler", r"\(x^{2}\) op \([0,+\infty[\)"],
                             ["afnemende stijging", "stijgt, maar steeds trager", r"\(10, 16, 20, 22, 23\): de stappen \(6, 4, 2, 1\) worden kleiner"],
                             ["constante stijging", "stijgt telkens evenveel", r"\(2, 5, 8, 11\): telkens \(+3\)"],
                             ["afnemende daling", "daalt, maar steeds minder hard", "de waarde van een auto"],
                             ["constant", r"de grafiek loopt evenwijdig met de \(x\)-as", ""]])),
            ("p", r"Stijgt \(f\) tot \(x=2\) met \(f(2)=7\) en daalt ze daarna, dan bereikt \(f\) een <strong>maximum \(7\) in \(x=2\)</strong>. "
                  r"Een functie die eerst stijgt en dan daalt, heeft dus een maximum, geen minimum. Net voor een maximum zie je vaak een afnemende stijging."),
        ]),
        dict(kop="Symmetrie, asymptoten en periode", blokken=[
            ("kader", tabel(["kenmerk", "betekenis"],
                            [["even functie", r"symmetrisch ten opzichte van de \(y\)-as, bv. \(x^{2}\)"],
                             ["oneven functie", r"symmetrisch ten opzichte van de <strong>oorsprong</strong> (niet de \(x\)-as), bv. \(x^{3}\)"],
                             [r"horizontale asymptoot \(y=3\)", r"voor heel grote of heel kleine \(x\) komt \(f(x)\) steeds dichter bij \(3\)"],
                             [r"verticale asymptoot \(x=-4\)", r"bij \(f(x)=\dfrac{5}{x+4}\): \(-4\) ligt niet in het domein"],
                             [r"periode \(p\)", r"de grafiek herhaalt zich: met periode \(5\) is \(f(2)=f(7)=f(12)\)"]])),
            ("fig", plot([(lambda x: 1 / x if x != 0 else None, "v", "1/x")], -5, 5, -4, 4),
             r"Als \(x\to+\infty\), dan \(f(x)\to 0\): de \(x\)-as is een horizontale asymptoot."),
        ]),
        dict(kop="Functies in situaties", blokken=[
            ("p", r"Het <strong>praktisch domein</strong> bevat enkel de \(x\)-waarden die in de situatie zin hebben; het is dus niet altijd "
                  r"hetzelfde als het domein. Het <strong>praktisch bereik</strong> zijn de \(y\)-waarden die dan voorkomen."),
            ("kader", r"<p><strong>Een bal:</strong> \(h(t)=30t-5t^{2}\), hoogte in meter na \(t\) seconden.</p><ul>"
                      r"<li>\(h(t)=0\) bij \(t=0\) en \(t=6\): praktisch domein \([0,6]\).</li>"
                      r"<li>Hoogste punt bij \(t=3\): \(h(3)=45\). Praktisch bereik \([0,45]\).</li>"
                      r"<li>\(h(2)=60-20=40\) m.</li></ul>"),
            ("kader", tabel(["situatie", "kenmerk", "betekenis"],
                            [[r"temperatuur \(T(u)\)", "minimum", "de laagste temperatuur, rond 5 uur 's morgens"],
                             [r"winst \(W(q)\): \(-\) voor \(q<200\), \(+\) voor \(q>200\)", r"nulwaarde \(200\)", "geen winst en geen verlies; pas boven 200 stuks winst"],
                             [r"medicijn \(M(t)\) dat steeds dichter bij \(0\) komt", r"horizontale asymptoot \(M=0\)", ""],
                             [r"waterhoogte die elke \(12{,}5\) uur op en neer gaat", "periode", ""],
                             [r"kapitaal \(K(t)\)", r"snijpunt met de \(y\)-as", r"het beginkapitaal op \(t=0\)"],
                             [r"taxi: \(4\) euro + \(2\) euro per km", r"\(P(k)=2k+4\)", r"voor \(30\) euro: \(2k+4=30\), \(k=13\) km"]])),
        ]),
    ],
    onthoud=[
        r"Domein: waar \(f(x)\) bestaat; bereik: welke \(y\)-waarden er voorkomen.",
        "Nulwaarde = x-waarde, nulpunt = punt; hoogstens één snijpunt met de y-as.",
        r"Tekenverloop: \(+\) boven, \(-\) onder de \(x\)-as.",
        "Even: symmetrisch t.o.v. de y-as. Oneven: t.o.v. de oorsprong.",
        "Toenemend/afnemend stijgen of dalen: kijk of de stappen groter of kleiner worden.",
        "Praktisch domein en bereik: enkel wat in de situatie zin heeft.",
    ])


# ───────────────────────── 3. Tweedegraadsfuncties
zet("tweedegraadsfuncties",
    titel="Tweedegraadsfuncties",
    onder="De parabool: top, symmetrieas, nulwaarden, transformaties en toepassingen.",
    secties=[
        dict(kop="Dal- of bergparabool", blokken=[
            ("p", r"De grafiek van \(f(x)=ax^{2}+bx+c\) is een parabool. Is \(a>0\), dan is het een <strong>dalparabool</strong> met een "
                  r"<strong>minimum</strong> in de top. Is \(a<0\), dan is het een <strong>bergparabool</strong> met een maximum. "
                  r"\(f(x)=-2x^{2}+3x+1\) is dus een bergparabool."),
            ("p", r"Hoe groter \(|a|\), hoe <strong>steiler</strong> (smaller) de parabool. \(0{,}1x^{2}\) is breder dan \(x^{2}\); "
                  r"\(-3x^{2}\) is een bergparabool die steiler is dan \(-x^{2}\)."),
            ("fig", plot([(lambda x: x * x, "g", "x²"), (lambda x: 3 * (x - 2) ** 2 + 1, "v", ""), (lambda x: -(x - 1) ** 2 + 4, "a", "")],
                         -3, 5, -2, 8, punten=[(2, 1, "(2, 1)"), (1, 4, "(1, 4)")]),
             r"Grijs \(x^{2}\), groen een dalparabool met top \((2,1)\), oranje een bergparabool met top \((1,4)\)."),
        ]),
        dict(kop="De top vinden", blokken=[
            ("kader", tabel(["vorm", "top", "voorbeeld"],
                            [[r"\(f(x)=a(x-p)^{2}+q\)", r"\((p,q)\), symmetrieas \(x=p\)", r"\(3(x-2)^{2}+5\): top \((2,5)\); \((x+4)^{2}-1\): as \(x=-4\)"],
                             [r"\(f(x)=ax^{2}+bx+c\)", r"\(x=-\dfrac{b}{2a}\), dan \(y=f(x)\) invullen", r"\(x^{2}-6x+2\): \(x=3\), \(y=9-18+2=-7\)"],
                             [r"\(f(x)=a(x-x_1)(x-x_2)\)", r"midden tussen de nulwaarden", r"nulwaarden \(-2\) en \(6\): top bij \(x=2\)"]])),
            ("p", r"Ook uit een tabel lees je de top af, dankzij de symmetrie: \(f(0)=5\), \(f(1)=2\), \(f(2)=1\), \(f(3)=2\), \(f(4)=5\) geeft top \((2,1)\)."),
            ("p", r"Van topvorm naar gewone vorm: \((x-2)^{2}-9=x^{2}-4x+4-9=x^{2}-4x-5\)."),
        ]),
        dict(kop="Nulwaarden, snijpunt met de y-as en bereik", blokken=[
            ("kader", r"<ul><li>\(f(x)=2(x-1)(x+5)\) heeft nulwaarden \(1\) en \(-5\).</li>"
                      r"<li>\((x-4)(x-4)\) heeft twee <strong>samenvallende</strong> nulwaarden: de parabool raakt de \(x\)-as, net zoals "
                      r"\(x^{2}+2x+1=(x+1)^{2}\).</li>"
                      r"<li>\((x-1)^{2}+2\) heeft <strong>geen</strong> nulwaarden: de top ligt boven de \(x\)-as en het is een dalparabool. "
                      r"Niet elke tweedegraadsfunctie heeft dus twee nulwaarden.</li>"
                      r"<li>Het snijpunt met de \(y\)-as is \(c\): \(4x^{2}-x+7\) snijdt de \(y\)-as in \(7\).</li></ul>"),
            ("p", r"Het bereik volgt uit de top: \(-(x-1)^{2}+4\) heeft bereik \(]-\infty,4]\). \((x-3)^{2}\) daalt tot \(3\) en stijgt op "
                  r"\([3,+\infty[\). Op \([0,+\infty[\) stijgt \(x^{2}\) toenemend."),
            ("p", r"Het tekenverloop van \((x-1)(x-5)\): \(+\) voor \(x<1\), \(-\) tussen \(1\) en \(5\), \(+\) voor \(x>5\)."),
        ]),
        dict(kop="Transformaties", blokken=[
            ("kader", tabel([r"van \(x^{2}\) naar", "transformatie"],
                            [[r"\(x^{2}+3\)", r"verschuiving \(3\) naar <strong>boven</strong>"],
                             [r"\((x-3)^{2}\)", r"verschuiving \(3\) naar <strong>rechts</strong>"],
                             [r"\((x+2)^{2}\)", r"verschuiving \(2\) naar <strong>links</strong>"],
                             [r"\(-x^{2}\)", r"spiegeling rond de \(x\)-as"],
                             [r"\(4x^{2}\)", r"verticale uitrekking met factor \(4\): de \(x\)-coördinaat van de top verandert niet"]])),
            ("p", r"\(2(x+1)^{2}-5\): verschuiving \(1\) naar links, verticale uitrekking met factor \(2\), verschuiving \(5\) naar beneden. "
                  r"Spiegelen rond de \(x\)-as en dan \(6\) naar boven geeft \(-x^{2}+6\). \((x-5)^{2}+2\) heeft haar top \(5\) rechts en \(2\) boven die van \(x^{2}\)."),
        ]),
        dict(kop="Een voorschrift opstellen", blokken=[
            ("kader", r"<ul><li>Top \((-1,3)\), door \((0,5)\): \(f(x)=a(x+1)^{2}+3\). Invullen: \(5=a+3\), dus \(a=2\): "
                      r"\(f(x)=2(x+1)^{2}+3\).</li>"
                      r"<li>Nulwaarden \(0\) en \(8\), door \((4,32)\): \(f(x)=ax(x-8)\). Invullen: \(32=a\cdot 4\cdot(-4)\), dus \(a=-2\): "
                      r"\(f(x)=-2x(x-8)\).</li></ul>"),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("kader", r"<p><strong>Een bal:</strong> \(h(x)=-0{,}05x^{2}+x+2\).</p><ul>"
                      r"<li>Top bij \(x=-\dfrac{1}{2\cdot(-0{,}05)}=10\) m; hoogte \(h(10)=-5+10+2=7\) m.</li>"
                      r"<li>Vertrekhoogte: \(h(0)=2\) m.</li></ul>"),
            ("kader", r"<p><strong>Een weide:</strong> \(40\) m draad, \(A(x)=x(20-x)\).</p><ul>"
                      r"<li>Praktisch domein \([0,20]\).</li><li>Top bij \(x=10\): \(A(10)=100\ \text{m}^{2}\). De grootste weide is een "
                      r"<strong>vierkant</strong> van \(10\) bij \(10\).</li></ul>"),
            ("p", r"<strong>Omzet:</strong> \(O(p)=-4p^{2}+160p\) is het grootst bij \(p=-\dfrac{160}{2\cdot(-4)}=20\) euro."),
        ]),
    ],
    onthoud=[
        r"\(a>0\): dalparabool met minimum; \(a<0\): bergparabool met maximum; grotere \(|a|\) = steiler.",
        r"Top van \(a(x-p)^{2}+q\) is \((p,q)\); bij \(ax^{2}+bx+c\) is \(x_{top}=-\dfrac{b}{2a}\).",
        "De top ligt midden tussen de nulwaarden; het snijpunt met de y-as is c.",
        r"\((x-3)^{2}\): 3 naar rechts. \(x^{2}+3\): 3 naar boven. \(-x^{2}\): spiegeling. \(4x^{2}\): uitrekking.",
        "Een parabool heeft 0, 1 of 2 nulwaarden.",
        "Optimaliseren: de top geeft het grootste of kleinste resultaat.",
    ])


# ───────────────────────── 4. Tweedegraadsvergelijkingen algebraïsch oplossen
zet("tweedegraadsvergelijkingen-algebraisch-oplossen",
    titel="Tweedegraadsvergelijkingen algebraïsch oplossen",
    onder="Vierkantsvergelijkingen oplossen met de discriminant of door te ontbinden, en ze gebruiken in vraagstukken.",
    secties=[
        dict(kop="Onvolledige vierkantsvergelijkingen", blokken=[
            ("p", r"Een vierkantsvergelijking heeft de vorm \(ax^{2}+bx+c=0\) met \(a\neq 0\). Is \(b=0\) of \(c=0\), dan is ze "
                  r"<strong>onvolledig</strong>, zoals \(3x^{2}-12=0\). Die los je snel op:"),
            ("kader", tabel(["vorm", "aanpak", "voorbeeld"],
                            [[r"\(ax^{2}+c=0\)", r"\(x^{2}\) alleen zetten, dan worteltrekken (twee tekens!)",
                              r"\(x^{2}=49\): \(V=\{-7,7\}\); \(4x^{2}=100\): \(x=\pm 5\); \(-x^{2}+4=0\): \(x=\pm 2\)"],
                             ["", r"is \(x^{2}\) negatief, dan is er geen oplossing", r"\(x^{2}+9=0\): \(V=\varnothing\)"],
                             [r"\(ax^{2}+bx=0\)", r"\(x\) buiten haakjes: \(x(ax+b)=0\)", r"\(x^{2}-5x=0\): \(x(x-5)=0\), \(V=\{0,5\}\); \(3x^{2}-6x=0\): \(V=\{0,2\}\)"]])),
            ("p", r"Deel <strong>nooit</strong> beide leden door \(x\): dan verlies je de oplossing \(0\). Zo heeft \(x^{2}=3x\) de oplossingen "
                  r"\(0\) en \(3\), niet alleen \(3\)."),
        ]),
        dict(kop="De discriminant", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(D=b^{2}-4ac\)</strong> &nbsp;&nbsp; "
                      r"<strong>\(x=\dfrac{-b\pm\sqrt{D}}{2a}\)</strong></p>"),
            ("kader", tabel([r"\(D\)", "aantal oplossingen", "parabool"],
                            [[r"\(D>0\)", "twee", r"snijdt de \(x\)-as twee keer"],
                             [r"\(D=0\)", r"één: \(x=-\dfrac{b}{2a}\)", r"raakt de \(x\)-as in haar top"],
                             [r"\(D<0\)", "geen", r"raakt de \(x\)-as niet"]])),
            ("fig", svg.discriminant(), r"Twee, één of geen snijpunten met de \(x\)-as."),
            ("kader", r"<ul><li>\(2x^{2}+3x-2=0\): \(D=9+16=25\), \(x=\dfrac{-3\pm 5}{4}\), dus \(V=\left\{-2,\tfrac{1}{2}\right\}\).</li>"
                      r"<li>\(x^{2}-2x-15=0\): \(D=4+60=64\), \(x=\dfrac{2\pm 8}{2}\), dus \(V=\{-3,5\}\).</li>"
                      r"<li>\(x^{2}-6x+9=0\): \(D=0\), één oplossing \(x=3\).</li>"
                      r"<li>\(x^{2}+x+1=0\): \(D=1-4=-3<0\), geen oplossing.</li>"
                      r"<li>\(x^{2}+4x-1=0\): \(D=20\), \(x=\dfrac{-4\pm\sqrt{20}}{2}\approx 0{,}24\) of \(-4{,}24\).</li>"
                      r"<li>\(x^{2}+4x+c=0\) met \(D=0\): \(16-4c=0\), dus \(c=4\).</li></ul>"),
            ("p", r"Een vierkantsvergelijking heeft dus nooit meer dan twee oplossingen."),
        ]),
        dict(kop="Ontbinden in factoren", blokken=[
            ("p", r"Een product is nul als een van de factoren nul is. \((x-2)(x+7)=0\) geeft \(x=2\) of \(x=-7\). Maar "
                  r"\((x-2)(x+7)=8\) mag je zo <strong>niet</strong> oplossen: werk eerst uit tot \(\ldots=0\)."),
            ("kader", tabel(["ontbinding", "voorbeeld"],
                            [[r"verschil van twee kwadraten: \(a^{2}-b^{2}=(a-b)(a+b)\)", r"\(x^{2}-16=(x-4)(x+4)\)"],
                             [r"som-productmethode: zoek twee getallen met som \(b\) en product \(c\)", r"\(x^{2}+5x+6=(x+2)(x+3)\)"],
                             ["", r"\(x^{2}-7x+10=(x-2)(x-5)\): nulwaarden \(2\) en \(5\)"],
                             ["", r"\(x^{2}+2x-24=(x+6)(x-4)\): positieve oplossing \(4\)"]])),
            ("p", r"\((x-1)^{2}=16\) los je op door worteltrekken: \(x-1=\pm 4\), dus \(V=\{-3,5\}\)."),
        ]),
        dict(kop="Snijpunten van twee grafieken", blokken=[
            ("p", r"Je lost \(f(x)=g(x)\) op en berekent bij elke oplossing de functiewaarde. \(x^{2}=x+6\) geeft \(x^{2}-x-6=0\), "
                  r"\((x-3)(x+2)=0\): \(x=-2\) of \(x=3\)."),
            ("p", r"\(x^{2}+1=0\) heeft geen oplossing, dus de parabool \(y=x^{2}+1\) en de rechte \(y=0\) hebben geen snijpunt. "
                  r"\(x^{2}+1=2x\) geeft \((x-1)^{2}=0\): de rechte \(y=2x\) <strong>raakt</strong> de parabool in één punt."),
        ]),
        dict(kop="Vraagstukken", blokken=[
            ("kader", tabel(["vraagstuk", "vergelijking", "antwoord"],
                            [[r"rechthoek \(3\) cm langer dan breed, oppervlakte \(40\ \text{cm}^{2}\)", r"\(x(x+3)=40\), \(x^{2}+3x-40=0\)", r"\(x=5\) (\(-8\) valt weg)"],
                             [r"steen valt \(5t^{2}\) meter; wanneer \(45\) m?", r"\(5t^{2}=45\)", r"\(t=3\) s"],
                             [r"som van een positief getal en zijn kwadraat is \(30\)", r"\(x^{2}+x-30=0\)", r"\(5\)"],
                             [r"vierkant tuintje met pad van \(1\) m, samen \(49\ \text{m}^{2}\)", r"\((x+2)^{2}=49\)", r"\(x=5\) m"],
                             [r"bal \(h(t)=-5t^{2}+20t\) op \(15\) m", r"\(-5t^{2}+20t=15\), \(t^{2}-4t+3=0\)", r"na \(1\) s en na \(3\) s"],
                             [r"wanneer terug op de grond?", r"\(-5t^{2}+20t=0\)", r"na \(4\) s"],
                             [r"winst \(W(q)=-q^{2}+50q-400\) nul", r"\(q^{2}-50q+400=0\)", r"\(q=10\) en \(q=40\)"]])),
            ("p", r"Controleer altijd of een oplossing in de situatie past. Een lengte kan niet negatief zijn: een negatieve oplossing "
                  r"van de vergelijking is dan geen antwoord."),
        ]),
    ],
    onthoud=[
        r"\(ax^{2}+c=0\): worteltrekken, met \(\pm\). \(ax^{2}+bx=0\): \(x\) buiten haakjes.",
        r"Nooit delen door \(x\): je verliest de oplossing \(0\).",
        r"\(D=b^{2}-4ac\); \(x=\dfrac{-b\pm\sqrt{D}}{2a}\). \(D>0\): twee, \(D=0\): één, \(D<0\): geen.",
        r"Een product is nul als een factor nul is; eerst alles naar één lid.",
        r"Snijpunten: los \(f(x)=g(x)\) op.",
        "Controleer of de oplossing in de situatie zin heeft.",
    ])


# ───────────────────────── 5. Exponentiële functies en groeimodellen
zet("exponentiele-functies-en-groeimodellen",
    titel="Exponentiële functies en groeimodellen",
    onder="De grafiek van a tot de x, groeifactoren, en rekenen met groei en verval.",
    secties=[
        dict(kop="De functie a tot de x", blokken=[
            ("fig", plot([(lambda x: 2 ** x, "v", "2^x"), (lambda x: 0.5 ** x, "a", "(1/2)^x")], -4, 4, -1, 8,
                         punten=[(0, 1, "(0, 1)")]),
             r"\(2^{x}\) stijgt, \(\left(\tfrac{1}{2}\right)^{x}\) daalt. Ze snijden elkaar in \((0,1)\)."),
            ("kader", tabel(["kenmerk", r"\(f(x)=a^{x}\) met \(a>0\), \(a\neq 1\)"],
                            [["vast punt", r"\((0,1)\), want \(a^{0}=1\)"],
                             ["domein", r"\(\mathbb{R}\)"],
                             ["bereik", r"\(]0,+\infty[\): de grafiek snijdt de \(x\)-as nooit"],
                             ["asymptoot", r"horizontaal: \(y=0\)"],
                             ["stijgend", r"als \(a>1\): toenemende stijging"],
                             ["dalend", r"als \(0<a<1\): afnemende daling"]])),
            ("p", r"Bij \(3\cdot 2^{x}\) gaat \(f(x)\to 0\) als \(x\to-\infty\). Gaat de grafiek van \(a^{x}\) door \((1,6)\), dan is \(a^{1}=6\), dus \(a=6\)."),
        ]),
        dict(kop="Transformaties", blokken=[
            ("kader", tabel(["voorschrift", "wat gebeurt er", "asymptoot en bereik"],
                            [[r"\(2^{x}+4\)", r"\(4\) naar boven", r"\(y=4\); bereik \(]4,+\infty[\)"],
                             [r"\(5\cdot 2^{x}-3\)", r"uitrekking met factor \(5\), \(3\) naar beneden", r"\(y=-3\)"],
                             [r"\(-3^{x}\)", r"spiegeling rond de \(x\)-as", r"\(y=0\); bereik \(]-\infty,0[\)"],
                             [r"\(3\cdot 2^{x}-1\)", r"verticale uitrekking met factor \(3\), \(1\) naar beneden", r"\(y=-1\)"]])),
            ("p", r"\(-2\cdot 3^{x}\) is <strong>dalend</strong>: de spiegeling draait het stijgen om. \(4\cdot 3^{x}+2\) snijdt de "
                  r"\(y\)-as in \(4\cdot 1+2=6\)."),
            ("p", r"\(2^{x}+c\) heeft enkel een nulwaarde als \(c\) negatief is: \(2^{x}+(-8)=0\) geeft \(2^{x}=8\), \(x=3\)."),
            ("weetje", r"\(2\cdot 5^{x}\) is niet hetzelfde als \(10^{x}\): bij \(x=2\) is het eerste \(50\), het tweede \(100\)."),
        ]),
        dict(kop="Groeifactor", blokken=[
            ("kader", tabel(["procent per periode", "groeifactor"],
                            [[r"\(+4\%\)", r"\(1{,}04\)"], [r"\(+7\%\)", r"\(1{,}07\)"], [r"\(-15\%\)", r"\(0{,}85\)"], [r"\(-10\%\)", r"\(0{,}9\)"]])),
            ("p", r"Een exponentieel groeimodel heeft de vorm <strong>\(N(t)=b\cdot g^{t}\)</strong>: \(b\) is de <strong>beginwaarde</strong>, "
                  r"\(g\) de groeifactor. \(K(t)=1500\cdot 1{,}02^{t}\) start bij \(1500\) euro. In \(N(t)=300\cdot 0{,}9^{t}\) neemt \(N\) "
                  r"elke tijdseenheid met \(10\%\) af."),
            ("p", r"<strong>Samengestelde intrest</strong>: \(2000\) euro aan \(3\%\) geeft \(B(t)=2000\cdot 1{,}03^{t}\). Bij "
                  r"<strong>enkelvoudige intrest</strong> komt er elk jaar hetzelfde bedrag bij: dat is <strong>lineaire</strong> groei."),
        ]),
        dict(kop="Welke groei?", blokken=[
            ("kader", tabel(["tabel", "kijk naar", "groei"],
                            [[r"\(3, 7, 11, 15\)", r"de <strong>verschillen</strong> zijn gelijk (\(+4\))", "lineair"],
                             [r"\(500, 550, 605, 665{,}5\)", r"de <strong>quotiënten</strong> zijn gelijk (\(\times 1{,}1\))", r"exponentieel met \(g=1{,}1\)"],
                             [r"\(5, 15, 45, 135\)", r"\(\times 3\), start \(5\)", r"\(f(x)=5\cdot 3^{x}\)"],
                             [r"\(1, 2, 5, 10\)", "verschillen en quotiënten wisselen", "niet lineair en niet exponentieel"]])),
            ("p", r"Een lineair model \(ax+b\) heeft een gelijk <strong>verschil</strong> per tijdseenheid, geen gelijke groeifactor."),
        ]),
        dict(kop="Groeifactor over een andere periode", blokken=[
            ("kader", r"<ul><li>\(21\%\) per twee jaar: \(g^{2}=1{,}21\), dus per jaar \(g=\sqrt{1{,}21}=1{,}1\).</li>"
                      r"<li>\(1{,}02\) per maand: per jaar \(1{,}02^{12}\approx 1{,}268\).</li>"
                      r"<li>\(10\%\) per jaar is na twee jaar \(1{,}1^{2}=1{,}21\): \(21\%\), dus <strong>niet</strong> \(20\%\).</li></ul>"),
        ]),
        dict(kop="Halveringstijd en verdubbelingstijd", blokken=[
            ("p", r"De <strong>halveringstijd</strong> is de tijd waarna nog de helft over is. \(80\) mg met een halveringstijd van \(8\) dagen: "
                  r"na \(24\) dagen (drie keer halveren) blijft \(80\to 40\to 20\to 10\) mg over."),
            ("p", r"De <strong>verdubbelingstijd</strong> bij \(5\%\) per jaar: \(1{,}05^{t}=2\), dus \(t=\log_{1{,}05}2=\dfrac{\log 2}{\log 1{,}05}\approx 14{,}2\) jaar. "
                  r"Die tijd hangt <strong>niet</strong> af van de beginwaarde."),
            ("p", r"Een stad van \(80\,000\) inwoners krimpt \(2\%\) per jaar: na \(5\) jaar \(80\,000\cdot 0{,}98^{5}\approx 72\,314\)."),
        ]),
    ],
    onthoud=[
        r"\(a^{x}\) gaat door \((0,1)\), bereik \(]0,+\infty[\), asymptoot \(y=0\).",
        r"\(a>1\): stijgend; \(0<a<1\): dalend.",
        r"\(+p\%\) geeft groeifactor \(1+\frac{p}{100}\); \(-p\%\) geeft \(1-\frac{p}{100}\).",
        r"\(N(t)=b\cdot g^{t}\): \(b\) is de beginwaarde.",
        "Gelijke verschillen: lineair. Gelijke quotiënten: exponentieel.",
        r"Verdubbelingstijd: \(g^{t}=2\), dus \(t=\log_{g}2\).",
    ])


# ───────────────────────── 6. De sinusfunctie en de goniometrische cirkel
zet("de-sinusfunctie-en-de-goniometrische-cirkel",
    titel="De sinusfunctie en de goniometrische cirkel",
    onder="Hoeken in radialen, de sinus op de cirkel, en sinusfuncties die periodieke verschijnselen beschrijven.",
    secties=[
        dict(kop="Radialen", blokken=[
            ("p", r"Een <strong>radiaal</strong> is de hoek waarbij <strong>de boog op de cirkel even lang is als de straal</strong>. "
                  r"Een halve cirkel is \(\pi\) radialen: <strong>\(180°=\pi\) rad</strong>. Dus \(1\) rad \(=\dfrac{180°}{\pi}\approx 57°\)."),
            ("kader", tabel(["graden", r"\(30°\)", r"\(45°\)", r"\(60°\)", r"\(90°\)", r"\(135°\)", r"\(180°\)", r"\(270°\)", r"\(360°\)"],
                            [["radialen", r"\(\frac{\pi}{6}\)", r"\(\frac{\pi}{4}\)", r"\(\frac{\pi}{3}\)", r"\(\frac{\pi}{2}\)", r"\(\frac{3\pi}{4}\)", r"\(\pi\)", r"\(\frac{3\pi}{2}\)", r"\(2\pi\)"]])),
        ]),
        dict(kop="De goniometrische cirkel", blokken=[
            ("fig", svg.goniocirkel(), r"Het beeldpunt van \(\alpha\) heeft coördinaat \((\cos\alpha,\sin\alpha)\)."),
            ("p", r"De goniometrische cirkel heeft straal \(1\). Het <strong>beeldpunt</strong> van een hoek \(\alpha\) heeft als coördinaat "
                  r"<strong>\((\cos\alpha,\sin\alpha)\)</strong>: de sinus is de hoogte van dat punt."),
            ("kader", tabel(["kwadrant", "hoeken", r"teken van \(\sin\)"],
                            [["eerste", r"\(0\) tot \(\frac{\pi}{2}\)", r"\(+\)"], ["tweede", r"\(\frac{\pi}{2}\) tot \(\pi\)", r"\(+\)"],
                             ["derde", r"\(\pi\) tot \(\frac{3\pi}{2}\), bv. \(\frac{5\pi}{4}\)", r"\(-\)"], ["vierde", r"\(\frac{3\pi}{2}\) tot \(2\pi\)", r"\(-\)"]])),
            ("p", r"\(\sin\frac{\pi}{2}=1\), \(\sin\frac{\pi}{6}=\frac{1}{2}\), \(\sin\pi=0\). Hoeken die even hoog liggen, hebben dezelfde sinus: "
                  r"\(\sin\frac{\pi}{6}=\sin\frac{5\pi}{6}\). Met je rekentoestel in radialen: \(\sin 2\approx 0{,}91\)."),
        ]),
        dict(kop="De grafiek van sin x", blokken=[
            ("fig", plot([(math.sin, "v", "sin x")], -0.3, 6.6, -1.5, 1.5, breedte=380, hoogte=170, stap_x=math.pi / 2, stap_y=0.5,
                         punten=[(math.pi / 2, 1, "π/2"), (3 * math.pi / 2, -1, "3π/2")]),
             r"Eén periode van \(\sin x\), van \(0\) tot \(2\pi\)."),
            ("kader", tabel(["kenmerk", r"\(\sin x\)"],
                            [["bereik", r"\([-1,1]\)"], ["periode", r"\(2\pi\): \(\sin(x+2\pi)=\sin x\) (en niet \(\sin x+2\pi\))"],
                             [r"nulwaarden op \([0,2\pi]\)", r"\(0\), \(\pi\) en \(2\pi\)"],
                             ["maximum en minimum", r"max \(1\) in \(\frac{\pi}{2}\), min \(-1\) in \(\frac{3\pi}{2}\)"],
                             ["dalend", r"op \(\left[\frac{\pi}{2},\frac{3\pi}{2}\right]\)"],
                             ["symmetrie", "oneven: symmetrisch ten opzichte van de oorsprong"]])),
        ]),
        dict(kop="De algemene sinusfunctie", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(f(x)=a\sin b(x-c)+d\)</strong></p>"),
            ("kader", tabel(["parameter", "betekenis", "voorbeeld"],
                            [[r"\(a\)", r"<strong>amplitude</strong> \(|a|\): de helft van max \(-\) min; \(a<0\) spiegelt rond de \(x\)-as", r"\(3\sin x+1\): amplitude \(3\)"],
                             [r"\(b\)", r"periode \(\dfrac{2\pi}{b}\); horizontale uitrekking met factor \(\dfrac{1}{b}\)", r"\(\sin 4x\): periode \(\frac{\pi}{2}\)"],
                             [r"\(c\)", r"<strong>faseverschuiving</strong>: \(c\) naar rechts", r"\(2\sin\left(x-\frac{\pi}{3}\right)\): \(\frac{\pi}{3}\) naar rechts"],
                             [r"\(d\)", r"<strong>evenwichtslijn</strong> \(y=d\); verandert de periode niet", r"\(3\sin x+1\): \(y=1\), bereik \([-2,4]\)"]])),
            ("p", r"\(4\sin x\) en \(\sin 4x\) hebben dus <strong>niet</strong> dezelfde periode: het eerste heeft periode \(2\pi\), het tweede \(\frac{\pi}{2}\). "
                  r"\(\sin x\) verticaal uitrekken met factor \(5\) en \(2\) omhoog geeft \(5\sin x+2\). Het maximum van \(2\sin 3(x-1)+5\) is \(5+2=7\)."),
            ("p", r"De <strong>frequentie</strong> is \(\dfrac{1}{p}\): het aantal golven per tijdseenheid. Eén golf in \(4\) s geeft \(0{,}25\) per seconde."),
        ]),
        dict(kop="Periodieke verschijnselen", blokken=[
            ("kader", tabel(["gegeven", "berekening"],
                            [[r"max \(10\), min \(2\)", r"evenwichtslijn \(\frac{10+2}{2}=6\), amplitude \(\frac{10-2}{2}=4\)"],
                             [r"haven: hoogst \(5\) m, laagst \(1\) m, periode \(12\) uur", r"amplitude \(2\), evenwichtslijn \(3\), \(b=\dfrac{2\pi}{12}=\dfrac{\pi}{6}\)"],
                             [r"reuzenrad: diameter \(40\) m, as op \(22\) m, \(10\) min per toer", r"amplitude \(20\), evenwichtslijn \(22\), periode \(10\); laagste punt \(22-20=2\) m"]])),
            ("p", r"Ook de ademhaling, de seizoenen of de daglengte kan je met een sinusfunctie beschrijven, omdat ze zich steeds na dezelfde tijd herhalen."),
        ]),
    ],
    onthoud=[
        r"\(180°=\pi\) rad; \(1\) rad \(\approx 57°\).",
        r"Beeldpunt \((\cos\alpha,\sin\alpha)\); sinus positief in kwadrant 1 en 2.",
        r"\(\sin x\): bereik \([-1,1]\), periode \(2\pi\), nulwaarden \(0,\pi,2\pi\).",
        r"\(a\sin b(x-c)+d\): amplitude \(|a|\), periode \(\frac{2\pi}{b}\), faseverschuiving \(c\), evenwichtslijn \(y=d\).",
        r"Amplitude \(=\frac{\max-\min}{2}\), evenwichtslijn \(=\frac{\max+\min}{2}\); frequentie \(=\frac{1}{p}\).",
    ])


# ───────────────────────── 7. Vergelijkingen grafisch oplossen
zet("vergelijkingen-grafisch-oplossen",
    titel="Vergelijkingen grafisch oplossen",
    onder="Een vergelijking oplossen door grafieken te snijden, met de hand of met een rekenapp, en het antwoord in de situatie formuleren.",
    secties=[
        dict(kop="Het idee", blokken=[
            ("kader", r"<ul><li>De oplossingen van <strong>\(f(x)=0\)</strong> zijn de \(x\)-coördinaten van de <strong>snijpunten met de \(x\)-as</strong>.</li>"
                      r"<li>De oplossingen van <strong>\(f(x)=g(x)\)</strong> vind je door beide grafieken te tekenen en de <strong>\(x\)-coördinaten van hun "
                      r"snijpunten</strong> af te lezen.</li>"
                      r"<li>\(f(x)=5\) los je op met de rechte \(y=5\).</li></ul>"),
            ("fig", plot([(lambda x: 0.5 * x * x + 0.5 * x + 2, "v", "f"), (lambda x: x + 3, "a", "g")], -3, 4, -1, 8,
                         punten=[(-1, 2, "(−1, 2)"), (2, 5, "(2, 5)")]),
             r"\(f\) en \(g\) snijden elkaar in \(x=-1\) en \(x=2\): \(V=\{-1,2\}\)."),
            ("p", r"De oplossingenverzameling noteer je met <strong>\(V\)</strong>. Snijden de grafieken in \((-1,3)\) en \((2,6)\), dan is "
                  r"\(V=\{-1,2\}\): enkel de \(x\)-waarden. Snijden ze niet, dan is \(V=\varnothing\). Een grafiek die de rechte \(y=4\) "
                  r"<strong>raakt</strong>, levert ook een oplossing op."),
        ]),
        dict(kop="Herschrijven", blokken=[
            ("p", r"\(x^{3}-2x=1\) kan je oplossen met de grafieken \(y=x^{3}-2x\) en \(y=1\), of met de nulwaarden van "
                  r"\(h(x)=x^{3}-2x-1\): dat geeft dezelfde oplossingen."),
            ("p", r"Snijdt \(x^{2}-4x+3\) de rechte \(y=3\) in \(x=0\) en \(x=4\), dan is \(V=\{0,4\}\) voor \(x^{2}-4x+3=3\), dus voor \(x^{2}-4x=0\)."),
            ("p", r"\(x^{3}-4x=0\) heeft \(V=\{-2,0,2\}\). Een derdegraadsvergelijking heeft <strong>niet altijd</strong> drie oplossingen: "
                  r"\(x^{3}=8\) heeft er maar één."),
        ]),
        dict(kop="Hoeveel oplossingen?", blokken=[
            ("kader", tabel(["vergelijking", "aantal", "waarom"],
                            [[r"\(2^{x}=-3\)", "geen", r"\(2^{x}\) is altijd positief"],
                             [r"\(5\cdot 3^{x}+2=0\)", "geen", r"\(5\cdot 3^{x}=-2\) kan niet"],
                             [r"\(3\cdot 2^{x}=24\)", "één", r"\(2^{x}=8\), \(x=3\); vorm \(b\cdot a^{x}+c=0\)"],
                             [r"\(2^{x}=3^{x}\)", "één", r"ze snijden enkel in \((0,1)\)"],
                             [r"\(\sin x=2\)", "geen", r"\(\sin x\) ligt tussen \(-1\) en \(1\)"],
                             [r"\(\sin x=\frac{1}{2}\) op \([0,2\pi]\)", "twee", r"\(\frac{\pi}{6}\) en \(\frac{5\pi}{6}\)"],
                             [r"\(2\sin x+1=0\) op \([0,2\pi]\)", "twee", r"\(\sin x=-\frac{1}{2}\)"],
                             [r"\(\sin x=0{,}3\) op \(\mathbb{R}\)", "oneindig veel", "de sinus is periodiek"]])),
        ]),
        dict(kop="Met een rekenapp", blokken=[
            ("p", r"Grafisch oplossen geeft soms een <strong>benadering</strong> in plaats van een exacte waarde. Geeft de app "
                  r"\(x\approx 1{,}7320508\), dan rond je af zoals de opgave vraagt, bv. \(1{,}73\)."),
        ]),
        dict(kop="Vraagstukken", blokken=[
            ("kader", tabel(["situatie", "vergelijking", "antwoord"],
                            [[r"\(1000\) euro aan \(4\%\); wanneer \(1500\)?", r"\(1000\cdot 1{,}04^{t}=1500\)", r"\(t\approx 10{,}34\): na \(11\) jaar voor het eerst meer dan \(1500\) euro"],
                             [r"plant \(h(t)=2\cdot 1{,}5^{t}\); wanneer \(13{,}5\) cm?", r"\(2\cdot 1{,}5^{t}=13{,}5\)", r"\(t=3\) weken"],
                             [r"medicijn \(M(t)=400\cdot 0{,}5^{t}\); wanneer \(50\) mg?", r"\(400\cdot 0{,}5^{t}=50\)", r"\(t=3\) uur"],
                             [r"algen \(A(t)=5\cdot 1{,}2^{t}\); vijver van \(60\ \text{m}^{2}\)", r"\(5\cdot 1{,}2^{t}=60\)", r"na ongeveer \(13{,}6\) dagen"],
                             [r"vissen \(N(t)=2000\cdot 0{,}9^{t}\) onder \(1000\)", r"snijpunt bij \(t\approx 6{,}58\)", "in het zevende jaar"],
                             [r"gsm A: \(10+0{,}05x\), B: \(4+0{,}10x\)", r"\(10+0{,}05x=4+0{,}10x\)", r"\(x=120\) minuten; daarboven is A goedkoper"],
                             [r"kosten \(0{,}5q^{2}+400\), opbrengst \(30q\)", r"snijpunten van \(K\) en \(O\)", r"\(q=20\) en \(q=40\)"]])),
            ("p", r"Niet elke oplossing van de vergelijking hoort bij het antwoord. Een doos uit karton van \(20\) bij \(20\) cm: "
                  r"\(I(x)=x(20-2x)^{2}=500\) geeft \(1{,}91\), \(5\) en \(13{,}09\). Maar \(x\) moet kleiner zijn dan \(10\), dus enkel \(1{,}91\) en \(5\) passen."),
            ("p", r"<strong>Periodieke situaties.</strong> \(T(m)=8\sin\left(\frac{\pi}{6}(m-4)\right)+12\): de hoogste temperatuur is \(12+8=20\) graden; "
                  r"de maanden met \(16\) graden vind je met de rechte \(y=16\). Een bakje met \(h(t)=15\sin\left(\frac{\pi}{4}t\right)+17\): één toer duurt "
                  r"\(\frac{2\pi}{\pi/4}=8\) minuten, en het bakje is per toer twee keer op \(17\) m (de evenwichtslijn)."),
        ]),
    ],
    onthoud=[
        r"\(f(x)=0\): snijpunten met de \(x\)-as. \(f(x)=g(x)\): snijpunten van de twee grafieken.",
        r"Schrijf enkel de \(x\)-waarden in \(V\); geen snijpunt: \(V=\varnothing\).",
        r"\(a^{x}\) is altijd positief; \(\sin x\) ligt tussen \(-1\) en \(1\).",
        "Een rekenapp geeft vaak een benadering: rond af zoals gevraagd.",
        "Controleer of elke oplossing in de situatie past, en formuleer het antwoord in woorden.",
    ])


# ───────────────────────── 8. Afgeleiden: helling en raaklijn
zet("afgeleiden-helling-en-raaklijn",
    titel="Afgeleiden: helling en raaklijn",
    onder="Gemiddelde verandering, ogenblikkelijke verandering, de raaklijn, en wat de hellinggrafiek zegt over een functie.",
    secties=[
        dict(kop="Het differentiequotiënt", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(\dfrac{\Delta y}{\Delta x}=\dfrac{f(b)-f(a)}{b-a}\)</strong></p>"
                      r"<p>Dat is de <strong>gemiddelde verandering</strong> over \([a,b]\): de richtingscoëfficiënt van de rechte door "
                      r"\((a,f(a))\) en \((b,f(b))\).</p>"),
            ("kader", r"<ul><li>\(f(x)=x^{2}\) over \([1,4]\): \(\dfrac{16-1}{4-1}=5\).</li>"
                      r"<li>Een auto op \(150\) km na \(2\) uur en op \(390\) km na \(5\) uur: \(\dfrac{390-150}{5-2}=80\) km/h gemiddeld.</li>"
                      r"<li>\(f(x)=2^{x}\) over \([0,3]\): \(\dfrac{8-1}{3}\approx 2{,}33\).</li></ul>"),
        ]),
        dict(kop="De afgeleide in een punt", blokken=[
            ("fig", svg.koordeenraaklijn(), r"Als \(h\) naar \(0\) gaat, wordt de koorde de raaklijn."),
            ("p", r"De <strong>afgeleide \(f'(a)\)</strong> is <strong>de limiet van het differentiequotiënt over \([a,a+h]\) als \(h\) naar \(0\) gaat</strong>. "
                  r"Het is de richtingscoëfficiënt van de <strong>raaklijn</strong> in dat punt: de helling, de ogenblikkelijke verandering."),
            ("p", r"Uit een tabel: over \([2,2+h]\) geeft \(h=0{,}1\): \(4{,}1\); \(h=0{,}01\): \(4{,}01\); \(h=0{,}001\): \(4{,}001\). Dus \(f'(2)=4\)."),
            ("kader", r"<ul><li>\(f'(3)<0\): de grafiek <strong>daalt</strong> in de buurt van \(x=3\).</li>"
                      r"<li>Een grotere afgeleide zegt iets over de <strong>helling</strong>, niet over de functiewaarde: uit \(f'(3)=10\) en \(g'(3)=2\) "
                      r"volgt niet dat \(f(3)>g(3)\).</li>"
                      r"<li>De gemiddelde verandering over \([a,b]\) is niet altijd gelijk aan de afgeleide in het midden.</li>"
                      r"<li>Voor een rechte \(mx+q\) is de afgeleide overal \(m\): \(y=-0{,}5x+3\) heeft helling \(-0{,}5\).</li>"
                      r"<li>In de top van een parabool is de raaklijn <strong>horizontaal</strong>, niet verticaal: \(f'=0\).</li></ul>"),
        ]),
        dict(kop="De vergelijking van de raaklijn", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(y-y_{1}=m(x-x_{1})\)</strong> met \(m=f'(x_{1})\) en \(y_{1}=f(x_{1})\)</p>"),
            ("kader", r"<ul><li>\(f(2)=5\), \(f'(2)=3\): \(y-5=3(x-2)\), dus \(y=3x-1\).</li>"
                      r"<li>\(f(-1)=4\), \(f'(-1)=-2\): \(y-4=-2(x+1)\), dus \(y=-2x+2\).</li>"
                      r"<li>De raaklijn in \(x=1\) gaat door \((1,3)\) en \((3,7)\): \(f'(1)=\dfrac{7-3}{3-1}=2\).</li>"
                      r"<li>Een rekenapp geeft voor \(x^{3}-3x\) dat \(f'(2)=9\): de raaklijn in \(x=2\) heeft richtingscoëfficiënt \(9\).</li></ul>"),
        ]),
        dict(kop="De afgeleide in situaties", blokken=[
            ("kader", tabel(["functie", "afgeleide", "voorbeeld"],
                            [[r"afgelegde weg \(s(t)\)", r"snelheid \(v(t)=s'(t)\)", r"\(s'(10)=6\): op \(10\) s rijdt de fietser \(6\) m/s"],
                             [r"snelheid \(v(t)\)", "versnelling", r"\(v(t)=0\): het voorwerp staat even stil"],
                             [r"totale kost \(K(q)\)", r"<strong>marginale kost</strong> \(K'(q)\)", "de kost van één stuk extra"]])),
        ]),
        dict(kop="De hellinggrafiek", blokken=[
            ("p", r"De <strong>hellinggrafiek</strong> is de grafiek van de afgeleide functie \(f'\). Uit het <strong>tekenverloop</strong> van \(f'\) lees je af hoe \(f\) op elk interval verloopt."),
            ("fig", svg.naast_elkaar([
                plot([(lambda x: (x - 3) ** 2 - 2, "v", "f")], -1, 7, -3, 6, breedte=230, hoogte=180),
                plot([(lambda x: 2 * (x - 3), "a", "f′")], -1, 7, -4, 6, breedte=230, hoogte=180, punten=[(3, 0, "3")])]),
             r"Een dalparabool met top in \(x=3\) heeft als hellinggrafiek een stijgende rechte die de \(x\)-as snijdt in \(3\)."),
            ("kader", tabel([r"hellinggrafiek \(f'\)", r"functie \(f\)"],
                            [[r"\(f'>0\) (boven de \(x\)-as)", "stijgend"],
                             [r"\(f'<0\) overal", "overal dalend"],
                             [r"van \(+\) naar \(-\)", "maximum"],
                             [r"van \(-\) naar \(+\)", "minimum"],
                             [r"\(f'\) positief en stijgend", "toenemende stijging"],
                             [r"\(f'\) positief en dalend", "afnemende stijging"],
                             [r"horizontale rechte \(y=2\)", r"stijgende rechte met richtingscoëfficiënt \(2\)"]])),
            ("kader", r"<ul><li>\(f'\): \(+\) voor \(x<-2\), \(-\) tussen \(-2\) en \(4\), \(+\) voor \(x>4\): maximum in \(-2\), minimum in \(4\).</li>"
                      r"<li>\(f\) daalt tot \(1\), stijgt tot \(5\), daalt dan: \(f'\) is \(-\), \(+\), \(-\).</li>"
                      r"<li>\(f'(x)=0\) geeft <strong>niet zeker</strong> een extremum: \(f'\) moet ook van teken wisselen (denk aan \(x^{3}\) in \(0\)).</li>"
                      r"<li>Een nulwaarde van \(f\) is geen nulwaarde van \(f'\).</li>"
                      r"<li>Twee functies die enkel verschillen door een verticale verschuiving, hebben dezelfde hellinggrafiek.</li>"
                      r"<li>Stijgt de totale kost eerst steeds trager en dan steeds sneller, dan daalt de marginale kost eerst en stijgt hij daarna.</li></ul>"),
        ]),
    ],
    onthoud=[
        r"Differentiequotiënt \(\frac{f(b)-f(a)}{b-a}\) = gemiddelde verandering.",
        r"\(f'(a)\) = limiet voor \(h\to 0\) = richtingscoëfficiënt van de raaklijn.",
        r"Raaklijn: \(y-f(a)=f'(a)(x-a)\).",
        r"\(s'=v\), \(v'=\) versnelling, \(K'=\) marginale kost.",
        r"\(f'>0\): stijgend; \(f'<0\): dalend; tekenwissel van \(f'\): extremum.",
    ])


# ───────────────────────── 9. Rekenkundige en meetkundige rijen
zet("rekenkundige-en-meetkundige-rijen",
    titel="Rekenkundige en meetkundige rijen",
    onder="Rijen waarin je telkens hetzelfde optelt of met hetzelfde vermenigvuldigt, en hoe je hun termen en sommen berekent.",
    secties=[
        dict(kop="Twee soorten rijen", blokken=[
            ("kader", tabel(["", "rekenkundige rij", "meetkundige rij"],
                            [["idee", r"telkens hetzelfde getal \(v\) <strong>optellen</strong>", r"telkens met hetzelfde getal \(q\) <strong>vermenigvuldigen</strong>"],
                             ["naam", r"verschil \(v\)", r"reden \(q\)"],
                             ["recursief", r"\(u_{n+1}=u_{n}+v\)", r"\(u_{n+1}=q\cdot u_{n}\)"],
                             ["expliciet", r"\(u_{n}=u_{1}+(n-1)\cdot v\)", r"\(u_{n}=u_{1}\cdot q^{n-1}\)"],
                             ["som", r"\(s_{n}=n\cdot\dfrac{u_{1}+u_{n}}{2}\)", r"\(s_{n}=u_{1}\cdot\dfrac{1-q^{n}}{1-q}\) (\(q\neq 1\))"],
                             ["groei", "lineair: losse punten op een rechte", r"exponentieel (bij \(q>1\))"],
                             ["kenmerk", "elke term is het gemiddelde van de term ervoor en erna", "het quotiënt van twee opeenvolgende termen is altijd hetzelfde"]])),
            ("fig", svg.tweerijen(), "Links een rekenkundige rij (punten op een rechte), rechts een meetkundige rij."),
        ]),
        dict(kop="Rekenkundige rijen", blokken=[
            ("kader", r"<p><strong>De rij \(5, 8, 11, 14,\dots\)</strong></p><ul>"
                      r"<li>Verschil \(v=3\). Recursief: \(u_{1}=5\) en \(u_{n+1}=u_{n}+3\).</li>"
                      r"<li>Expliciet: \(u_{n}=5+(n-1)\cdot 3\), dus \(u_{20}=5+19\cdot 3=62\).</li>"
                      r"<li>Som van de eerste \(10\) termen: \(u_{10}=32\), \(s_{10}=10\cdot\dfrac{5+32}{2}=185\).</li></ul>"),
            ("kader", r"<ul><li>\(12, 9, 6, 3\): verschil \(-3\). Een negatief verschil geeft een <strong>dalende</strong> rij; \(u_{n}=7-2n\) daalt dus.</li>"
                      r"<li>\(v=0\): alle termen zijn gelijk.</li>"
                      r"<li>\(2{,}5;\ 4;\ 5{,}5;\ 7\) is rekenkundig met \(v=1{,}5\).</li>"
                      r"<li>\(u_{1}=4\) en \(u_{6}=29\): \(4+5v=29\), dus \(v=5\).</li>"
                      r"<li>\(1+2+\dots+100=100\cdot\dfrac{1+100}{2}=5050\).</li>"
                      r"<li>\(u_{1}=100\), \(v=-7\): \(u_{n}=107-7n<0\) voor het eerst bij \(n=16\): \(u_{16}=-5\).</li></ul>"),
            ("p", r"<strong>Een zaal:</strong> \(15\) stoelen op rij \(1\), telkens \(2\) meer. Rij \(12\): \(15+11\cdot 2=37\). Samen: \(12\cdot\dfrac{15+37}{2}=312\). "
                  r"<strong>Enkelvoudige intrest:</strong> \(1000\) euro aan \(2\%\) geeft elk jaar \(20\) euro erbij: een rekenkundige rij met verschil \(20\)."),
        ]),
        dict(kop="Meetkundige rijen", blokken=[
            ("kader", r"<p><strong>De rij \(3, 6, 12, 24,\dots\)</strong></p><ul>"
                      r"<li>Reden \(q=2\). \(u_{8}=3\cdot 2^{7}=384\).</li>"
                      r"<li>\(1+2+4+\dots+512\) (tien termen): \(1\cdot\dfrac{1-2^{10}}{1-2}=1023\).</li></ul>"),
            ("kader", r"<ul><li>\(80, 40, 20, 10\): \(u_{1}=80\) en \(u_{n+1}=\tfrac{1}{2}u_{n}\).</li>"
                      r"<li>\(u_{1}=5\), \(q=0{,}8\): dalend, met een <strong>afnemende daling</strong>.</li>"
                      r"<li>\(q=1\): alle termen zijn gelijk.</li>"
                      r"<li>\(81;\ 27;\ 9;\ 3\) is meetkundig met \(q=\frac{1}{3}\). \(2, 6, 18, 54\) is meetkundig, niet rekenkundig.</li>"
                      r"<li>\(u_{1}=2\), \(u_{4}=54\): \(2q^{3}=54\), \(q^{3}=27\), \(q=3\).</li></ul>"),
            ("kader", tabel(["situatie", "rij", "uitkomst"],
                            [[r"\(1000\) euro aan \(2\%\) samengestelde intrest", r"meetkundig, \(q=1{,}02\)", r"na \(5\) jaar \(1000\cdot 1{,}02^{5}\approx 1104{,}08\) euro"],
                             [r"bal van \(4\) m, botst terug tot \(75\%\)", r"meetkundig, \(q=0{,}75\)", r"na de derde bots \(4\cdot 0{,}75^{3}=1{,}6875\) m"],
                             [r"bericht naar \(3\) nieuwe mensen per ronde", r"\(3, 9, 27, 81, 243\)", r"ronde \(5\): \(243\); samen \(363\)"]])),
            ("weetje", r"Op lange termijn wint een meetkundige rij met \(q>1\) altijd van een rekenkundige rij, hoe groot het verschil ook is: "
                       r"exponentiële groei haalt lineaire groei altijd in."),
        ]),
    ],
    onthoud=[
        r"Rekenkundig: \(+v\); \(u_{n}=u_{1}+(n-1)v\); \(s_{n}=n\cdot\frac{u_{1}+u_{n}}{2}\).",
        r"Meetkundig: \(\times q\); \(u_{n}=u_{1}q^{n-1}\); \(s_{n}=u_{1}\frac{1-q^{n}}{1-q}\).",
        "Rekenkundig = lineaire groei; meetkundig = exponentiële groei.",
        "Enkelvoudige intrest: rekenkundig. Samengestelde intrest: meetkundig.",
    ])


# ───────────────────────── 10. Kansrekenen met kansbomen en kruistabellen
zet("kansrekenen-met-kansbomen-en-kruistabellen",
    titel="Kansrekenen met kansbomen en kruistabellen",
    onder="Kansen berekenen met Laplace, met kruistabellen en met kansbomen, ook voorwaardelijke kansen.",
    secties=[
        dict(kop="Basisbegrippen", blokken=[
            ("kader", tabel(["begrip", "betekenis", "voorbeeld"],
                            [["uitkomstenverzameling", "alle mogelijke uitkomsten", r"één dobbelsteenworp: \(\{1,2,3,4,5,6\}\)"],
                             ["gebeurtenis", "een deel van de uitkomstenverzameling", r"een even getal: \(\{2,4,6\}\)"],
                             ["wet van Laplace", "bij gelijk mogelijke uitkomsten: gunstig / mogelijk", r"\(P(\text{even})=\frac{3}{6}=\frac{1}{2}\)"],
                             ["complementregel", r"\(P(\text{niet }A)=1-P(A)\)", r"trein op tijd \(0{,}85\): niet op tijd \(0{,}15\)"]])),
            ("p", r"Een vaas met \(5\) rode, \(3\) blauwe en \(2\) groene knikkers: \(P(\text{blauw})=\frac{3}{10}=0{,}3\). Een aas uit \(52\) kaarten: \(\frac{4}{52}=\frac{1}{13}\). "
                  r"Een kans ligt altijd tussen \(0\) en \(1\), nooit erboven."),
        ]),
        dict(kop="Relatieve frequentie", blokken=[
            ("p", r"Een munt valt \(94\) keer op kop bij \(200\) worpen: relatieve frequentie \(\frac{94}{200}=0{,}47\). Herhaal je een experiment "
                  r"<strong>heel vaak</strong>, dan komt de relatieve frequentie dicht bij de kans."),
            ("p", r"Een munt heeft geen geheugen: na vijf keer kop is de kans op kop bij de zesde worp nog altijd \(\frac{1}{2}\)."),
            ("p", r"<strong>Verwachte frequentie</strong> = kans \(\times\) aantal. Kans op winst \(0{,}2\), \(150\) keer draaien: \(30\) keer winst. "
                  r"\(120\) van \(500\) mensen hebben een hond: in een groep van \(2000\) verwacht je \(2000\cdot\frac{120}{500}=480\)."),
        ]),
        dict(kop="Kruistabellen en voorwaardelijke kans", blokken=[
            ("kader", tabel(["", "sport", "sport niet", "totaal"],
                            [["jongen", "60", "40", "100"], ["meisje", "70", "30", "100"], ["totaal", "130", "70", "200"]])),
            ("p", r"Alle cellen samen tellen op tot het totaal, hier \(200\)."),
            ("kader", r"<ul><li>\(P(\text{sport})=\frac{130}{200}=0{,}65\).</li>"
                      r"<li>\(P(\text{sport}\mid\text{meisje})=\frac{70}{100}=0{,}7\): de kans op sport, <strong>als je weet</strong> dat het een meisje is. "
                      r"Je kijkt enkel naar de rij 'meisje'.</li>"
                      r"<li>\(P(\text{meisje}\mid\text{sport})=\frac{70}{130}\approx 0{,}54\): nu kijk je enkel naar de kolom 'sport'.</li></ul>"),
            ("p", r"\(P(A\mid B)\) en \(P(B\mid A)\) zijn dus <strong>niet</strong> altijd gelijk."),
        ]),
        dict(kop="Kansbomen", blokken=[
            ("fig", svg.kansboom(), "Twee knikkers uit een zak van drie groene en twee oranje, zonder terugleggen."),
            ("kader", r"<ul><li><strong>Productregel:</strong> de kans op een pad is het <strong>product</strong> van de kansen op de takken.</li>"
                      r"<li><strong>Somregel:</strong> de kans dat een van verschillende paden zich voordoet, is de <strong>som</strong> van hun kansen.</li>"
                      r"<li>De takken uit hetzelfde knooppunt tellen op tot \(1\); alle paden samen ook.</li></ul>"),
            ("kader", tabel(["opgave", "berekening"],
                            [[r"twee keer kop met een munt", r"\(0{,}5\cdot 0{,}5=0{,}25\)"],
                             [r"precies één keer kop", r"\(0{,}25+0{,}25=0{,}5\) (KM of MK)"],
                             [r"\(3\) rood, \(2\) wit, twee rode <strong>zonder</strong> terugleggen", r"\(\frac{3}{5}\cdot\frac{2}{4}=\frac{3}{10}\): de kansen van de tweede stap veranderen"],
                             [r"twee rode <strong>met</strong> terugleggen", r"\(\frac{3}{5}\cdot\frac{3}{5}=\frac{9}{25}\)"],
                             [r"schutter met kans \(0{,}7\): twee keer mis", r"\(0{,}3\cdot 0{,}3=0{,}09\); minstens één raak: \(1-0{,}09=0{,}91\)"],
                             [r"minstens één zes bij drie worpen", r"\(1-\left(\frac{5}{6}\right)^{3}\approx 0{,}42\), en dus niet \(\frac{1}{6}+\frac{1}{6}+\frac{1}{6}\)"],
                             [r"bus gehaald \(0{,}8\) (dan op tijd \(0{,}95\)), gemist (dan op tijd \(0{,}3\))", r"\(0{,}8\cdot 0{,}95+0{,}2\cdot 0{,}3=0{,}82\)"],
                             [r"\(60\%\) Frans (\(90\%\) slaagt), \(40\%\) Duits (\(75\%\) slaagt)", r"\(0{,}6\cdot 0{,}9+0{,}4\cdot 0{,}75=0{,}84\)"]])),
        ]),
        dict(kop="Een medische test", blokken=[
            ("p", r"\(2\%\) is ziek. De test is positief bij \(95\%\) van de zieken en bij \(10\%\) van de gezonden."),
            ("kader", r"<ul><li>Ziek én positief: \(0{,}02\cdot 0{,}95=0{,}019\).</li>"
                      r"<li>Gezond én positief: \(0{,}98\cdot 0{,}10=0{,}098\).</li>"
                      r"<li>Positief: \(0{,}019+0{,}098=0{,}117\).</li>"
                      r"<li>\(P(\text{ziek}\mid\text{positief})=\dfrac{0{,}019}{0{,}117}\approx 0{,}16\).</li></ul>"),
            ("weetje", r"Dus maar \(16\%\), niet \(95\%\)! Omdat er zoveel meer gezonde mensen zijn, zijn de meeste positieve tests vals alarm."),
        ]),
    ],
    onthoud=[
        "Laplace: gunstig / mogelijk, bij gelijk mogelijke uitkomsten.",
        r"\(P(\text{niet }A)=1-P(A)\); een kans ligt tussen \(0\) en \(1\).",
        "Relatieve frequentie nadert de kans bij heel veel herhalingen.",
        r"\(P(A\mid B)\): kijk enkel naar de rij of kolom van \(B\).",
        "Kansboom: vermenigvuldigen langs een pad, optellen over paden.",
        "Minstens één: reken via het complement.",
    ])


# ───────────────────────── 11. Steekproeven, samenhang en causaliteit
zet("steekproeven-samenhang-en-causaliteit",
    titel="Steekproeven, samenhang en causaliteit",
    onder="Hoe je een eerlijke steekproef trekt, welke fouten erin kunnen sluipen, en waarom samenhang nog geen oorzaak is.",
    secties=[
        dict(kop="Populatie, steekproef en variabele", blokken=[
            ("p", r"Een onderzoeker wil weten hoeveel uur Vlaamse jongeren van \(16\) jaar slapen en bevraagt er \(800\)."),
            ("kader", tabel(["begrip", "in dat voorbeeld"],
                            [["populatie: de hele groep waarover je iets wil weten", r"alle Vlaamse jongeren van \(16\) jaar"],
                             ["steekproef: het deel dat je bevraagt", r"de \(800\) bevraagde jongeren"],
                             ["variabele: wat je meet", "het aantal uren slaap"]])),
            ("p", r"Een steekproef is <strong>representatief</strong> als ze de populatie goed weerspiegelt, zodat je besluiten mag doortrekken."),
        ]),
        dict(kop="Soorten steekproeven", blokken=[
            ("kader", tabel(["soort", "wat", "voorbeeld"],
                            [["enkelvoudig aselecte steekproef (EAS)", "elke groep van die grootte heeft evenveel kans om gekozen te worden",
                              r"alle \(1000\) leerlingen nummeren en met een toevalsgenerator \(50\) verschillende nummers trekken"],
                             ["vrijwillige respons", "wie wil, doet mee", "een online stemming in een krant over een nieuw zwembad"],
                             ["opportunistische steekproef", "wie toevallig makkelijk bereikbaar is", "mensen die in de bibliotheek zitten"]])),
            ("p", r"<strong>Randomisatie</strong>: het toeval bepaalt wie in de steekproef komt. Dat is de beste bescherming tegen vertekening."),
            ("kader", r"<p><strong>Vertekende steekproeven</strong></p><ul>"
                      r"<li>Mensen in een bibliotheek zeggen niets over hoeveel <em>alle</em> Vlamingen lezen.</li>"
                      r"<li>Voetbalsupporters aan een stadion zeggen niets over hoeveel Belgen voetbal kijken.</li>"
                      r"<li>Enkel overdag naar vaste nummers bellen: werkende mensen en jongeren bereik je amper.</li>"
                      r"<li>Te veel mensen met een hoog inkomen: het besluit <strong>overschat</strong> het gemiddeld inkomen.</li></ul>"),
        ]),
        dict(kop="Fouten", blokken=[
            ("kader", tabel(["", "steekproeffout", "niet-steekproeffout"],
                            [["wat", "het toevallige verschil tussen steekproef en populatie, omdat je maar een deel bevraagt",
                              "een fout in de manier van werken"],
                             ["voorbeelden", "deze steekproef heeft toevallig iets meer langslapers",
                              "mensen antwoorden niet eerlijk over hun inkomen; een sturende vraag zoals 'Bent u het ermee eens dat de gevaarlijke snelweg eindelijk veiliger moet?'; vrijwillige respons"],
                             ["grotere steekproef helpt?", "<strong>ja</strong>, bij een aselecte steekproef", "<strong>nee</strong>"]])),
            ("p", r"<strong>Variabiliteit van steekproeven</strong>: verschillende steekproeven uit dezelfde populatie geven telkens een iets ander resultaat. "
                  r"Twee goede aselecte steekproeven geven dus bijna nooit exact hetzelfde."),
        ]),
        dict(kop="Samenhang of causaliteit?", blokken=[
            ("p", r"Bij <strong>samenhang</strong> gaan twee variabelen samen op of af. Bij <strong>causaliteit</strong> <strong>veroorzaakt</strong> de ene de andere. "
                  r"Een sterke samenhang bewijst nog geen oorzaak, en er is ook niet altijd een duidelijke oorzaak en gevolg."),
            ("kader", tabel(["verklaring", "voorbeeld"],
                            [["een <strong>derde verborgen variabele</strong> beïnvloedt allebei", "ijsjes en verdrinkingen (warm weer); ooievaars en baby's (hoe landelijk); brandweerlieden en schade (grootte van de brand); schoenmaat en leesvaardigheid bij kinderen (leeftijd); chocolade en Nobelprijzen (rijkdom)"],
                             ["<strong>omwisseling van oorzaak en gevolg</strong>", "wie ziek is, gaat naar de dokter (niet omgekeerd); misschien maakt geluk dat je meer sport"],
                             ["<strong>toeval</strong>", "films met een acteur en verdrinkingen in een zwembad; verdwijnt vaak bij nieuwe gegevens"],
                             ["<strong>causaliteit</strong>", "harder op het gaspedaal, sneller rijden; roken veroorzaakt longkanker (met veel onderzoek aangetoond)"]])),
            ("p", r"Causaliteit toon je het best aan met een <strong>experiment waarbij het toeval beslist wie de behandeling krijgt</strong>. Zie je enkel "
                  r"dat leerlingen met meer boeken thuis betere punten halen, of dat kinderen die ontbijten beter scoren, vraag je je af of er een derde "
                  r"variabele achter zit, zoals een regelmatig gezinsleven."),
        ]),
    ],
    onthoud=[
        "Populatie = alle; steekproef = een deel; variabele = wat je meet.",
        "EAS: elke groep heeft evenveel kans. Vrijwillige respons en opportunistische steekproeven zijn vertekend.",
        "Steekproeffout: toeval, kleiner bij een grotere steekproef. Niet-steekproeffout: fout in de aanpak, groter maken helpt niet.",
        "Samenhang is geen causaliteit: denk aan een derde variabele, omgekeerde richting of toeval.",
        "Causaliteit toon je aan met een gerandomiseerd experiment.",
    ])


# ───────────────────────── 12. De normale verdeling
zet("de-normale-verdeling",
    titel="De normale verdeling",
    onder="De Gausskromme, de vuistregels 68-95, en kansen berekenen met een rekenapp.",
    secties=[
        dict(kop="De Gausskromme", blokken=[
            ("fig", svg.normaalkromme(100, 15, 85, 115, xlabel="", toon_kans=True),
             r"\(N(100,15)\): ongeveer \(68\%\) ligt tussen \(85\) en \(115\)."),
            ("p", r"In <strong>\(N(\mu,\sigma)\)</strong> is \(\mu\) het <strong>gemiddelde</strong> en \(\sigma\) de <strong>standaardafwijking</strong> van de populatie. "
                  r"De Gausskromme is de <strong>dichtheidsfunctie</strong>: een klok, symmetrisch rond \(\mu\). De top ligt boven het gemiddelde, "
                  r"dus bij \(N(170,8)\) boven \(170\). De helft van de waarden ligt onder het gemiddelde."),
            ("kader", r"<ul><li>De oppervlakte onder de kromme is altijd \(1\).</li>"
                      r"<li>Grotere \(\sigma\): de kromme wordt <strong>breder en lager</strong>. \(N(50,2)\) is hoger dan \(N(50,4)\).</li>"
                      r"<li>Ander \(\mu\), zelfde \(\sigma\): zelfde vorm, maar verschoven.</li>"
                      r"<li>Zelfde gemiddelde is dus niet genoeg voor dezelfde kromme. Klas A \(N(65,5)\) en klas B \(N(65,15)\): zelfde gemiddelde, maar in B liggen de punten veel verder uit elkaar.</li>"
                      r"<li>Een standaardafwijking is nooit negatief.</li></ul>"),
        ]),
        dict(kop="Wanneer past het model?", blokken=[
            ("p", r"Als het <strong>histogram ongeveer klokvormig en symmetrisch</strong> is. Niet bij inkomens (lange staart naar rechts), en niet bij "
                  r"een histogram met twee toppen."),
            ("p", r"Een steekproef heeft gemiddelde \(\bar{x}\) en standaardafwijking \(s\). Geeft een app \(\bar{x}=172{,}4\) cm en \(s=6{,}9\) cm bij een "
                  r"klokvormig histogram, dan kies je het model \(N(172{,}4;\ 6{,}9)\)."),
        ]),
        dict(kop="De vuistregels", blokken=[
            ("kader", tabel(["interval", "deel van de waarden", r"bij \(N(100,15)\)"],
                            [[r"\(\mu-\sigma\) tot \(\mu+\sigma\)", r"ongeveer \(68\%\)", r"\(85\) tot \(115\)"],
                             [r"\(\mu-2\sigma\) tot \(\mu+2\sigma\)", r"ongeveer \(95\%\)", r"\(70\) tot \(130\)"]])),
            ("kader", r"<p>Met de symmetrie vind je ook de staarten:</p><ul>"
                      r"<li>\(P(X>100)=50\%\).</li>"
                      r"<li>\(P(X<85)\approx\frac{1-0{,}68}{2}=0{,}16\).</li>"
                      r"<li>\(P(X>130)\approx\frac{1-0{,}95}{2}=0{,}025\).</li>"
                      r"<li>Toets \(N(60,10)\) en Lotte haalt \(80=\mu+2\sigma\): ze zit bij ongeveer de beste \(2{,}5\%\).</li></ul>"),
        ]),
        dict(kop="Kansen met een rekenapp", blokken=[
            ("p", r"\(P(X<a)\) is de <strong>oppervlakte onder de kromme links van \(a\)</strong>. Je geeft in: de grens \(a\), het gemiddelde \(\mu\) en de standaardafwijking \(\sigma\). "
                  r"De oppervlakte tussen \(a\) en \(b\) is ongeveer de relatieve frequentie van waarden tussen \(a\) en \(b\)."),
            ("kader", tabel(["opgave", "uitkomst"],
                            [[r"koffie \(N(500,4)\): \(P(X<492)\)", r"\(\approx 0{,}0228\): ongeveer \(2{,}3\%\) weegt minder dan \(492\) g; bij \(10\,000\) pakken zo'n \(228\)"],
                             [r"\(P(X>492)\)", r"\(1-0{,}0228=0{,}9772\), want \(P(X>a)=1-P(X<a)\)"],
                             [r"flessen \(N(1000,5)\): \(P(990<X<1010)\)", r"\(1-2\cdot 0{,}0228=0{,}9544\); \(P(X>1010)\) is even groot als \(P(X<990)\)"],
                             [r"mannen \(N(180,7)\), deur \(201\) cm", r"\(201=\mu+3\sigma\): ongeveer \(0{,}15\%\) is groter"],
                             [r"\(P(173<X<194)\)", r"van \(\mu-\sigma\) tot \(\mu+2\sigma\): \(0{,}34+0{,}475\approx 0{,}815\)"]])),
            ("p", r"Omgekeerd: het gewicht waaronder \(10\%\) van de pakken ligt, is de waarde \(a\) met \(P(X<a)=0{,}10\). De app geeft \(a\approx 494{,}9\): "
                  r"\(10\%\) weegt minder dan ongeveer \(494{,}9\) g."),
            ("weetje", r"De kans op precies één waarde, zoals \(P(X=500)\), is \(0\): een kans is een oppervlakte, en een lijn heeft geen oppervlakte. "
                       r"De hoogte van de kromme is dus geen kans."),
        ]),
    ],
    onthoud=[
        r"\(N(\mu,\sigma)\): klok rond het gemiddelde \(\mu\); grotere \(\sigma\) = breder en lager.",
        "Oppervlakte onder de kromme = 1; de helft ligt onder het gemiddelde.",
        r"\(68\%\) binnen \(\mu\pm\sigma\), \(95\%\) binnen \(\mu\pm 2\sigma\).",
        r"\(P(X<a)\) = oppervlakte links van \(a\); \(P(X>a)=1-P(X<a)\).",
        "Enkel geschikt bij een klokvormig, symmetrisch histogram.",
    ])


# ───────────────────────── 13. Bedrijfswetenschappen: ongelijkheden oplossen
zet("bedrijfswetenschappen-ongelijkheden-oplossen",
    titel="Bedrijfswetenschappen: ongelijkheden oplossen",
    onder="Ongelijkheden grafisch en met een tekenverloop oplossen, en de oplossing als interval schrijven.",
    secties=[
        dict(kop="Intervallen", blokken=[
            ("fig", svg.intervallen(), "Een vol bolletje: de grens doet mee. Een open bolletje: de grens doet niet mee."),
            ("kader", tabel(["notatie", "betekenis"],
                            [[r"\([4,+\infty[\)", r"alle getallen \(\geq 4\)"],
                             [r"\(]1,5]\)", r"\(1<x\leq 5\)"],
                             [r"\([2,7[\)", r"\(2\leq x<7\): \(7\) hoort er <strong>niet</strong> bij"],
                             [r"\(]-\infty,-3[\cup]1,+\infty[\)", r"kleiner dan \(-3\) <strong>of</strong> groter dan \(1\)"]])),
        ]),
        dict(kop="Grafisch oplossen", blokken=[
            ("kader", tabel(["ongelijkheid", r"je neemt de \(x\)-waarden waar"],
                            [[r"\(f(x)>0\)", r"de grafiek <strong>boven</strong> de \(x\)-as ligt"],
                             [r"\(f(x)\leq g(x)\)", r"de grafiek van \(f\) <strong>onder of op</strong> die van \(g\) ligt"],
                             [r"\(f(x)>3\)", r"de grafiek boven de rechte \(y=3\) ligt"]])),
            ("p", r"De oplossingen zijn reële getallen; je schrijft ze als interval of unie van intervallen. Bij een <strong>strikte</strong> ongelijkheid (\(<\), \(>\)) horen de nulwaarden of snijpunten <strong>niet</strong> bij de oplossingen; bij \(\leq\) en \(\geq\) wel."),
            ("kader", r"<ul><li>\(f\) heeft nulwaarden \(-3\) en \(1\), positief ertussen: \(f(x)\geq 0\) geeft \([-3,1]\); \(f(x)<0\) geeft \(]-\infty,-3[\cup]1,+\infty[\).</li>"
                      r"<li>\(f\) onder \(g\) voor \(x<2\), erboven voor \(x>2\): \(f(x)>g(x)\) geeft \(]2,+\infty[\).</li>"
                      r"<li>Dalende \(f\), stijgende \(g\), snijpunt in \(4\): \(f(x)\geq g(x)\) geeft \(]-\infty,4]\).</li>"
                      r"<li>Nulwaarden \(-2\), \(0\), \(3\) met tekenverloop \(-,+,-,+\): \(f(x)>0\) geeft \(]-2,0[\cup]3,+\infty[\).</li>"
                      r"<li>\(3\cdot 1{,}2^{x}\) en \(10\) snijden bij \(x\approx 6{,}60\); de exponentiële functie stijgt, dus \(3\cdot 1{,}2^{x}<10\) geeft \(]-\infty;\ 6{,}60[\).</li></ul>"),
            ("kader", tabel(["ongelijkheid", "oplossing", "waarom"],
                            [[r"\(2^{x}>0\)", r"\(\mathbb{R}\)", r"\(2^{x}\) is altijd positief"],
                             [r"\(\sin x>1\)", r"\(\varnothing\)", r"\(\sin x\leq 1\)"],
                             [r"\(\sin x\geq 0\) op \([0,2\pi]\)", r"\([0,\pi]\cup\{2\pi\}\)", "de sinus is niet negatief in kwadrant 1 en 2"],
                             [r"\(x^{2}<0\)", r"\(\varnothing\)", "een kwadraat is nooit negatief"],
                             [r"\(x^{2}\leq 0\)", r"\(\{0\}\)", r"\(x=0\) voldoet wel"]])),
        ]),
        dict(kop="Eerstegraadsongelijkheden", blokken=[
            ("p", r"Vermenigvuldig of deel je beide leden door een <strong>negatief</strong> getal, dan <strong>keert het ongelijkheidsteken om</strong>. "
                  r"\(-3x+6>0\) geeft \(-3x>-6\), dus \(x<2\): \(V=]-\infty,2[\)."),
        ]),
        dict(kop="Tweedegraadsongelijkheden", blokken=[
            ("p", r"Werkwijze: <strong>nulwaarden zoeken, een tekenverloop maken en de juiste intervallen nemen</strong>. "
                  r"Een dalparabool (\(a>0\)) is <strong>negatief</strong> tussen haar nulwaarden, een bergparabool (\(a<0\)) <strong>positief</strong>."),
            ("fig", svg.paraboolteken(), "Het teken van een parabool tussen en buiten haar nulwaarden."),
            ("kader", tabel(["ongelijkheid", "nulwaarden", "oplossing"],
                            [[r"\(x^{2}-5x+4<0\)", r"\(1\) en \(4\)", r"\(]1,4[\)"],
                             [r"\(x^{2}-9\geq 0\)", r"\(-3\) en \(3\)", r"\(]-\infty,-3]\cup[3,+\infty[\)"],
                             [r"\(-x^{2}+2x+3>0\)", r"\(-1\) en \(3\)", r"\(]-1,3[\)"],
                             [r"\(-2x^{2}+8\leq 0\)", r"\(-2\) en \(2\)", r"\(]-\infty,-2]\cup[2,+\infty[\)"],
                             [r"\(x^{2}+4>0\)", "geen", r"\(\mathbb{R}\)"],
                             [r"\(x^{2}-6x+9>0\)", r"\(3\) (dubbel)", r"\(\mathbb{R}\setminus\{3\}\); bij \(\leq 0\): \(\{3\}\)"],
                             [r"\(2x^{2}\leq 8x\)", r"\(2x^{2}-8x=2x(x-4)\): \(0\) en \(4\)", r"\([0,4]\)"]])),
            ("p", r"Deel bij \(2x^{2}\leq 8x\) <strong>niet</strong> door \(2x\): je weet niet of \(x\) positief of negatief is, en je verliest oplossingen. "
                  r"Een tweedegraadsongelijkheid heeft ook niet altijd een begrensd interval als oplossing. Dezelfde werkwijze werkt voor elke veeltermfunctie."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("kader", tabel(["situatie", "ongelijkheid", "oplossing"],
                            [[r"winst \(W(q)=-q^{2}+60q-500\)", r"\(W(q)>0\), nulwaarden \(10\) en \(50\)", r"\(10<q<50\); grootste winst bij \(q=30\)"],
                             [r"bal \(h(t)=-5t^{2}+20t\) hoger dan \(15\) m", r"\(-5t^{2}+20t-15>0\)", r"\(1<t<3\)"],
                             [r"\(x^{2}\) onder \(x+2\)", r"\(x^{2}-x-2<0\)", r"\(]-1,2[\)"],
                             [r"rechthoek \(x(12-x)\geq 32\)", r"\(x^{2}-12x+32\leq 0\)", r"\(4\leq x\leq 8\)"],
                             [r"kost \(K(u)=u^{2}-8u+30<18\)", r"\(u^{2}-8u+12<0\)", r"\(2<u<6\)"]])),
        ]),
    ],
    onthoud=[
        "Strikt (< of >): grenzen doen niet mee. Met gelijkheid: wel.",
        "Grafisch: kijk waar de grafiek boven of onder de as of de andere grafiek ligt.",
        "Vermenigvuldigen met een negatief getal keert het teken om.",
        "Tweedegraads: nulwaarden, tekenverloop, juiste intervallen.",
        "Dalparabool negatief tussen de nulwaarden, bergparabool positief.",
        "Nooit delen door een uitdrukking met x.",
    ])


# ───────────────────────── 14. Bedrijfswetenschappen: exponentiële en goniometrische vergelijkingen
zet("bedrijfswetenschappen-exponentiele-en-goniometrische-vergelijkingen",
    titel="Bedrijfswetenschappen: exponentiële en goniometrische vergelijkingen",
    onder="Vergelijkingen met een onbekende in de exponent of in een sinus algebraïsch oplossen.",
    secties=[
        dict(kop="Exponentiële vergelijkingen met hetzelfde grondtal", blokken=[
            ("p", r"Schrijf beide leden als macht van hetzelfde getal."),
            ("kader", tabel(["vergelijking", "oplossing"],
                            [[r"\(2^{x}=64\)", r"\(2^{x}=2^{6}\), dus \(x=6\)"],
                             [r"\(3^{x}=\frac{1}{27}\)", r"\(3^{x}=3^{-3}\), dus \(x=-3\)"],
                             [r"\(10^{x}=0{,}001\)", r"\(x=-3\)"],
                             [r"\(9^{x}=3\)", r"\(3^{2x}=3^{1}\), dus \(x=\frac{1}{2}\)"],
                             [r"\(5\cdot 2^{x}-40=0\)", r"\(2^{x}=8\), \(V=\{3\}\)"]])),
        ]),
        dict(kop="Exponentiële vergelijkingen met een logaritme", blokken=[
            ("p", r"Lukt dat niet, zet dan de macht alleen en neem de logaritme met dat grondtal. \(a^{x}=k\) (met \(k>0\)) geeft \(x=\log_{a}k\)."),
            ("kader", tabel(["vergelijking", "exact", "benaderd"],
                            [[r"\(2^{x}=7\)", r"\(x=\log_{2}7\)", r"\(2{,}81\)"],
                             [r"\(e^{x}=5\)", r"\(x=\ln 5\)", r"\(1{,}61\)"],
                             [r"\(1{,}2^{x}-2=0\)", r"\(x=\log_{1{,}2}2\)", r"\(3{,}80\)"],
                             [r"\(2000\cdot 1{,}03^{t}=3000\)", r"\(t=\log_{1{,}03}1{,}5\)", r"\(13{,}7\)"]])),
            ("p", r"Opgelet: \(3\cdot 2^{x}\) is <strong>niet</strong> \(6^{x}\). Deel eerst door \(3\): \(3\cdot 2^{x}=24\) geeft \(2^{x}=8\). Zo ook "
                  r"\(2\cdot 3^{x}=18\): \(3^{x}=9\), \(x=2\), en niet hetzelfde als \(6^{x}=18\)."),
            ("p", r"Is \(b>0\) en \(c>0\), dan heeft \(b\cdot a^{x}+c=0\) <strong>geen</strong> oplossing: \(4\cdot 1{,}5^{x}+3=0\) geeft \(V=\varnothing\). "
                  r"Bij \(a>1\) en \(k>1\) is \(\log_{a}k\) positief."),
            ("p", "<strong>Groei en verval</strong>"),
            ("kader", r"<ul><li>Verdubbelingstijd: los \(a^{t}=2\) op.</li>"
                      r"<li>Een stof halveert elke \(5\) jaar: \(80\cdot 0{,}5^{t/5}=10\) geeft \(0{,}5^{t/5}=\frac{1}{8}\), \(\frac{t}{5}=3\), dus \(t=15\) jaar.</li>"
                      r"<li>\(50\,000\) inwoners, \(-4\%\) per jaar: \(50\,000\cdot 0{,}96^{t}<40\,000\) geeft \(t>\log_{0{,}96}0{,}8\approx 5{,}47\): na \(6\) jaar.</li></ul>"),
        ]),
        dict(kop="Goniometrische vergelijkingen", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(\sin x=\sin\alpha\iff x=\alpha+k\cdot 2\pi\) of \(x=\pi-\alpha+k\cdot 2\pi\)</strong>, met \(k\in\mathbb{Z}\)</p>"),
            ("fig", svg.goniocirkel(), r"Twee punten op de cirkel liggen even hoog: \(\alpha\) en \(\pi-\alpha\)."),
            ("kader", tabel(["vergelijking", r"oplossingen in \([0,2\pi]\)"],
                            [[r"\(\sin x=\frac{1}{2}\) of \(2\sin x-1=0\)", r"\(\frac{\pi}{6}\) en \(\frac{5\pi}{6}\)"],
                             [r"\(\sin x=-1\)", r"enkel \(\frac{3\pi}{2}\)"],
                             [r"\(2\sin x+\sqrt{3}=0\), dus \(\sin x=-\frac{\sqrt{3}}{2}\)", r"\(\frac{4\pi}{3}\) en \(\frac{5\pi}{3}\)"],
                             [r"\(\sin x=-0{,}5\)", r"\(\frac{7\pi}{6}\) en \(\frac{11\pi}{6}\)"],
                             [r"\(\sin x+1=1\), dus \(\sin x=0\)", r"\(0\), \(\pi\) en \(2\pi\)"],
                             [r"\(\sin x=0{,}3\)", r"\(\approx 0{,}30\) en \(\pi-0{,}30\approx 2{,}84\) (geen in het derde kwadrant)"],
                             [r"\(3\sin x=4\)", r"geen: \(\sin x=\frac{4}{3}>1\)"]])),
            ("p", r"Zet je rekentoestel in <strong>radialen</strong> als je de oplossing in radialen wil."),
            ("kader", r"<ul><li>\(\sin x=\frac{\sqrt{2}}{2}\): \(x=\frac{\pi}{4}+k\cdot 2\pi\) of \(x=\frac{3\pi}{4}+k\cdot 2\pi\).</li>"
                      r"<li>\(\sin 2x=1\): \(2x=\frac{\pi}{2}+k\cdot 2\pi\), dus \(x=\frac{\pi}{4}+k\pi\). De oplossingen liggen \(\pi\) uit elkaar; in \([0,\pi]\) enkel \(\frac{\pi}{4}\).</li>"
                      r"<li>\(\sin\left(x-\frac{\pi}{4}\right)=0\): \(x-\frac{\pi}{4}=k\pi\), dus \(x=\frac{\pi}{4}+k\pi\).</li></ul>"),
            ("p", r"Een goniometrische vergelijking met een oplossing heeft op \(\mathbb{R}\) <strong>oneindig veel</strong> oplossingen. "
                  r"De algemene vorm is \(a\sin b(x-c)+d=0\), zoals \(4\sin 3(x-1)+2=0\)."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("kader", r"<p><strong>Getij:</strong> \(h(t)=2\sin\left(\frac{\pi}{6}t\right)+3\).</p><ul>"
                      r"<li>\(h=4\): \(\sin\left(\frac{\pi}{6}t\right)=\frac{1}{2}\), \(\frac{\pi}{6}t=\frac{\pi}{6}\): voor het eerst na \(1\) uur.</li>"
                      r"<li>\(h=5\): \(\sin\left(\frac{\pi}{6}t\right)=1\), \(\frac{\pi}{6}t=\frac{\pi}{2}\): na \(3\) uur.</li></ul>"
                      r"<p><strong>Reuzenrad:</strong> \(h(t)=10\sin\left(\frac{\pi}{5}(t-2{,}5)\right)+12\). Op \(12\) m als de sinus \(0\) is: voor het eerst bij \(t=2{,}5\) min.</p>"),
        ]),
    ],
    onthoud=[
        r"Zelfde grondtal: exponenten gelijkstellen. Anders: \(a^{x}=k\Rightarrow x=\log_{a}k\).",
        r"Eerst de macht alleen zetten; \(b\cdot a^{x}\) is niet \((ba)^{x}\).",
        r"\(a^{x}\) is altijd positief: \(a^{x}=\) negatief getal heeft geen oplossing.",
        r"\(\sin x=\sin\alpha\): \(x=\alpha+k2\pi\) of \(x=\pi-\alpha+k2\pi\).",
        r"\(\sin x\) ligt tussen \(-1\) en \(1\); rekentoestel in radialen.",
    ])


# ───────────────────────── 15. Bedrijfswetenschappen: afgeleiden berekenen met rekenregels
zet("bedrijfswetenschappen-afgeleiden-berekenen-met-rekenregels",
    titel="Bedrijfswetenschappen: afgeleiden berekenen met rekenregels",
    onder="Afgeleiden berekenen zonder limiet: de basisafgeleiden, de rekenregels en de kettingregel.",
    secties=[
        dict(kop="Notatie en basisafgeleiden", blokken=[
            ("p", r"De afgeleide van \(y=f(x)\) noteer je \(f^{\prime}(x)\) of, met de notatie van Leibniz, \(\dfrac{dy}{dx}\)."),
            ("kader", tabel([r"\(f(x)\)", r"\(f^{\prime}(x)\)", "voorbeeld"],
                            [[r"\(c\) (constante)", r"\(0\)", r"\((5)^{\prime}=0\)"],
                             [r"\(x^{n}\)", r"\(n\cdot x^{n-1}\)", r"\((x^{5})^{\prime}=5x^{4}\)"],
                             [r"\(\dfrac{1}{x}\)", r"\(-\dfrac{1}{x^{2}}\)", r"\(\left(\dfrac{4}{x^{2}}\right)^{\prime}=(4x^{-2})^{\prime}=-\dfrac{8}{x^{3}}\)"],
                             [r"\(\sqrt{x}\)", r"\(\dfrac{1}{2\sqrt{x}}\)", ""],
                             [r"\(e^{x}\)", r"\(e^{x}\)", ""],
                             [r"\(a^{x}\)", r"\(a^{x}\ln a\)", r"\((2^{x})^{\prime}=2^{x}\ln 2\)"],
                             [r"\(\ln x\)", r"\(\dfrac{1}{x}\)", ""],
                             [r"\(\log_{a}x\)", r"\(\dfrac{1}{x\ln a}\)", r"\((\log x)^{\prime}=\dfrac{1}{x\ln 10}\)"]])),
            ("p", r"Let op: \(x^{2}\) (veranderlijke in het grondtal) en \(2^{x}\) (veranderlijke in de exponent) volgen <strong>niet</strong> dezelfde regel."),
        ]),
        dict(kop="Som, veelvoud, product en quotiënt", blokken=[
            ("kader", tabel(["regel", "formule"],
                            [["som", r"\((f+g)^{\prime}=f^{\prime}+g^{\prime}\)"],
                             ["veelvoud", r"\((c\cdot f)^{\prime}=c\cdot f^{\prime}\)"],
                             ["productregel", r"\((f\cdot g)^{\prime}=f^{\prime}\cdot g+f\cdot g^{\prime}\)"],
                             ["quotiëntregel", r"\(\left(\dfrac{f}{g}\right)^{\prime}=\dfrac{f^{\prime}g-fg^{\prime}}{g^{2}}\)"]])),
            ("p", r"De afgeleide van een product is dus <strong>niet</strong> \(f^{\prime}\cdot g^{\prime}\). Bij de quotiëntregel is de volgorde in de teller belangrijk: eerst \(f^{\prime}g\), dan min \(fg^{\prime}\)."),
            ("kader", r"<ul><li>\((3x^{4}-2x^{2}+7x-1)^{\prime}=12x^{3}-4x+7\); \((x^{2}+x^{3})^{\prime}=2x+3x^{2}\)</li>"
                      r"<li>\(f(x)=x^{3}-4x\): \(f^{\prime}(x)=3x^{2}-4\), dus \(f^{\prime}(2)=8\)</li>"
                      r"<li>\(\big((2x+1)(x^{2}-3)\big)^{\prime}=2(x^{2}-3)+(2x+1)\cdot 2x=6x^{2}+2x-6\)</li>"
                      r"<li>\((x\cdot e^{x})^{\prime}=e^{x}+xe^{x}=(x+1)e^{x}\)</li>"
                      r"<li>\(\left(\dfrac{x}{x+1}\right)^{\prime}=\dfrac{1\cdot(x+1)-x\cdot 1}{(x+1)^{2}}=\dfrac{1}{(x+1)^{2}}\)</li>"
                      r"<li>\(\left(\dfrac{2x-1}{x}\right)^{\prime}=\dfrac{2x-(2x-1)}{x^{2}}=\dfrac{1}{x^{2}}\), dus \(f^{\prime}(1)=1\)</li>"
                      r"<li>\(\left(\dfrac{e^{x}}{x}\right)^{\prime}=\dfrac{e^{x}x-e^{x}}{x^{2}}=\dfrac{(x-1)e^{x}}{x^{2}}\)</li></ul>"),
        ]),
        dict(kop="De kettingregel", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(\big(f(g(x))\big)^{\prime}=f^{\prime}(g(x))\cdot g^{\prime}(x)\)</strong></p>"
                      r"<p style='text-align:center'>buitenste functie afleiden, binnenste laten staan, en vermenigvuldigen met de afgeleide van de binnenste</p>"),
            ("kader", tabel([r"\(f(x)\)", r"\(f^{\prime}(x)\)"],
                            [[r"\((3x-2)^{4}\)", r"\(4(3x-2)^{3}\cdot 3=12(3x-2)^{3}\)"],
                             [r"\((x^{2}+1)^{3}\)", r"\(3(x^{2}+1)^{2}\cdot 2x=6x(x^{2}+1)^{2}\), niet enkel \(3(x^{2}+1)^{2}\)"],
                             [r"\(e^{3x}\)", r"\(3e^{3x}\)"],
                             [r"\(e^{2x}\)", r"\(2e^{2x}\), dus \(f^{\prime}(0)=2\)"],
                             [r"\(\ln(x^{2}+4)\)", r"\(\dfrac{2x}{x^{2}+4}\)"],
                             [r"\(\ln(3x)\)", r"\(\dfrac{3}{3x}=\dfrac{1}{x}\), dus \(f^{\prime}(2)=\frac{1}{2}\)"],
                             [r"\(\sqrt{2x+5}\)", r"\(\dfrac{1}{2\sqrt{2x+5}}\cdot 2=\dfrac{1}{\sqrt{2x+5}}\)"]])),
        ]),
        dict(kop="Raaklijn en betekenis", blokken=[
            ("p", r"De raaklijn in \((a,f(a))\): <strong>\(y-f(a)=f^{\prime}(a)(x-a)\)</strong>. Voor \(y=x^{2}\) in \((3,9)\): \(f^{\prime}(3)=6\), dus \(y-9=6(x-3)\) of \(y=6x-9\)."),
            ("fig", plot([(lambda x: x * x, "v", "y = x²"), (lambda x: 6 * x - 9, "a", "raaklijn")], -1, 5, -2, 16,
                         punten=[(3, 9, "(3, 9)")], stap_y=2), "De raaklijn raakt de parabool in \\((3,9)\\) en heeft helling \\(6\\)."),
            ("p", r"Een <strong>positieve</strong> afgeleide betekent dat de functie daar stijgt, een <strong>negatieve</strong> dat ze daalt."),
            ("kader", r"<ul><li><strong>Marginale kost:</strong> \(K(q)=0{,}5q^{2}+20q+300\) geeft \(K^{\prime}(q)=q+20\). Bij \(q=40\) is de marginale kost \(60\) euro: één stuk extra kost ongeveer \(60\) euro.</li>"
                      r"<li><strong>Groeisnelheid:</strong> \(B(t)=1000\cdot e^{0{,}05t}\) geeft \(B^{\prime}(t)=50\cdot e^{0{,}05t}\). \(B^{\prime}(10)\) is hoe <strong>snel</strong> het bedrag op tijdstip \(10\) groeit (euro per jaar), niet hoeveel er op de rekening staat.</li></ul>"),
        ]),
    ],
    onthoud=[
        r"\((x^{n})^{\prime}=nx^{n-1}\), \((e^{x})^{\prime}=e^{x}\), \((\ln x)^{\prime}=\frac{1}{x}\), \((a^{x})^{\prime}=a^{x}\ln a\).",
        r"Product: \(f^{\prime}g+fg^{\prime}\). Quotiënt: \(\frac{f^{\prime}g-fg^{\prime}}{g^{2}}\).",
        "Kettingregel: buitenste afleiden, maal de afgeleide van de binnenste.",
        r"Raaklijn: \(y-f(a)=f^{\prime}(a)(x-a)\).",
        "Afgeleide = snelheid van verandering (marginale kost, groeisnelheid).",
    ])


# ───────────────────────── 16. Bedrijfswetenschappen: verloop van een functie en optimaliseren
TABEL_X3_3X = tabel(
    [r"\(x\)", "", r"\(-1\)", "", r"\(0\)", "", r"\(1\)", ""],
    [[r"\(f^{\prime}(x)=3x^{2}-3\)", r"\(+\)", r"\(0\)", r"\(-\)", r"\(-\)", r"\(-\)", r"\(0\)", r"\(+\)"],
     [r"\(f^{\prime\prime}(x)=6x\)", r"\(-\)", r"\(-\)", r"\(-\)", r"\(0\)", r"\(+\)", r"\(+\)", r"\(+\)"],
     [r"\(f(x)=x^{3}-3x\)", "stijgt, bol", r"max \(2\)", "daalt, bol", r"buigpunt \((0,0)\)", "daalt, hol", r"min \(-2\)", "stijgt, hol"]])

zet("bedrijfswetenschappen-verloop-van-een-functie-en-optimaliseren",
    titel="Bedrijfswetenschappen: verloop van een functie en optimaliseren",
    onder="Met de eerste en tweede afgeleide het verloop van een functie onderzoeken, en extremumproblemen oplossen.",
    secties=[
        dict(kop="Stijgen, dalen en extrema", blokken=[
            ("p", r"Als \(f^{\prime}(x)>0\) op een interval, dan <strong>stijgt</strong> \(f\) daar; als \(f^{\prime}(x)<0\), dan <strong>daalt</strong> \(f\). "
                  r"In de tabel van het waardenverloop zie je het teken van \(f^{\prime}\). Gaat het teken van \(f^{\prime}\) in \(a\) van \(+\) naar \(-\), dan heeft \(f\) een <strong>relatief maximum</strong>; van \(-\) naar \(+\) een <strong>relatief minimum</strong>."),
            ("fig", plot([(lambda x: x ** 3 - 3 * x, "v", "f")], -2.5, 2.5, -3, 3,
                         punten=[(-1, 2, "max"), (1, -2, "min"), (0, 0, "buigpunt")]), r"\(f(x)=x^{3}-3x\): maximum \(2\) in \(x=-1\), minimum \(-2\) in \(x=1\)."),
            ("p", r"Opgelet: \(f^{\prime}(a)=0\) betekent alleen dat de raaklijn <strong>horizontaal</strong> is. Er is niet altijd een extremum: bij \(x^{3}\) is \(f^{\prime}(0)=0\), maar \(f\) stijgt gewoon door."),
        ]),
        dict(kop="Hol, bol, buigpunten en de samenvattende tabel", blokken=[
            ("kader", tabel(["teken", "betekenis"],
                            [[r"\(f^{\prime\prime}>0\)", "de grafiek is <strong>hol</strong> (dalparabool-vorm)"],
                             [r"\(f^{\prime\prime}<0\)", "de grafiek is <strong>bol</strong> (bergparabool-vorm)"],
                             [r"\(f^{\prime}>0\) en \(f^{\prime\prime}<0\)", "<strong>afnemende stijging</strong>: stijgt, maar steeds trager"],
                             [r"\(f^{\prime}>0\) en \(f^{\prime\prime}>0\)", "toenemende stijging"]])),
            ("p", r"Een <strong>buigpunt</strong> is een punt waar de grafiek van hol naar bol gaat of omgekeerd: \(f^{\prime\prime}\) wisselt van teken. "
                  r"\(f^{\prime\prime}(a)=0\) alleen is niet genoeg. Een buigpunt van \(f\) is een top van de grafiek van \(f^{\prime}\). Een tweedegraadsfunctie heeft nooit een buigpunt. "
                  r"Een functie kan stijgen en tegelijk bol zijn."),
            ("kader", r"<p>\(f(x)=x^{3}-6x^{2}+5\): \(f^{\prime\prime}(x)=6x-12\) is nul in \(x=2\) en wisselt daar van teken. Buigpunt bij \(x=2\); bol voor \(x<2\), hol voor \(x>2\).</p>"),
            ("p", r"<strong>De samenvattende tabel.</strong> In een samenvattende tabel zet je het teken van \(f^{\prime}\) en \(f^{\prime\prime}\), stijgen of dalen, hol of bol, extrema en buigpunten."),
            ("kader", TABEL_X3_3X),
            ("kader", tabel(["functie", "afgeleide", "besluit"],
                            [[r"\(x^{4}-2x^{2}\)", r"\(4x^{3}-4x=4x(x-1)(x+1)\)", r"kandidaat-extrema \(-1\), \(0\), \(1\); in \(0\) een <strong>maximum</strong> (\(f^{\prime\prime}(0)=-4\)), in \(\pm 1\) een minimum"],
                             [r"\(2x^{3}-3x^{2}-12x\)", r"\(6x^{2}-6x-12=6(x-2)(x+1)\)", r"maximum in \(-1\), minimum in \(2\)"],
                             [r"\(x^{2}-4x+1\)", r"\(2x-4\)", r"minimum \(-3\) in \(x=2\), bereik \([-3,+\infty[\)"]])),
            ("p", r"Op de grafiek van \(f^{\prime}\): een nulpunt met \(f^{\prime}\) positief links en negatief rechts geeft een maximum van \(f\)."),
        ]),
        dict(kop="Extremumproblemen", blokken=[
            ("kader", r"<p><strong>Stappenplan</strong></p><ol><li>Een veranderlijke kiezen en het voorschrift opstellen.</li><li>Het praktisch domein bepalen.</li>"
                      r"<li>Afleiden en \(f^{\prime}(x)=0\) oplossen.</li><li>Controleren of het een maximum of minimum is (ook de grenspunten).</li><li>Antwoorden in een zin, met eenheid.</li></ol>"),
            ("p", r"Hangt het voorschrift van twee grootheden af, druk dan de ene uit in de andere met het gegeven. Bij een blikje met \(\pi r^{2}h=500\) schrijf je \(h=\frac{500}{\pi r^{2}}\), "
                  r"zodat de oppervlakte maar van één veranderlijke afhangt. Controleer met de tweede afgeleide: \(f^{\prime}(a)=0\) en \(f^{\prime\prime}(a)<0\) geeft een <strong>maximum</strong>, "
                  r"\(f^{\prime\prime}(a)>0\) een <strong>minimum</strong>. Bij een praktisch domein \([a,b]\) kan het grootste resultaat ook in een grenspunt liggen."),
            ("kader", tabel(["probleem", "functie", "oplossing"],
                            [[r"weide met \(40\) m hekwerk", r"\(A(x)=x(20-x)\), domein \(]0,20[\)", r"\(x=10\) m: een vierkant"],
                             ["winstfunctie", r"\(W(q)=-2q^{2}+160q-1200\)", r"\(W^{\prime}=0\) bij \(q=40\); winst \(2000\) euro"],
                             [r"open doos uit karton van \(12\) cm", r"\(V(x)=x(12-2x)^{2}\), domein \(]0,6[\)", r"\(x=2\) cm (\(x=6\) valt buiten het domein)"],
                             ["gemiddelde kost", r"\(G(q)=q+\dfrac{400}{q}\)", r"\(G^{\prime}=1-\dfrac{400}{q^{2}}=0\): \(q=20\), kost \(40\) euro"],
                             [r"som \(30\), product maximaal", r"\(P(x)=x(30-x)\)", r"\(15\) en \(15\)"],
                             [r"\(x\cdot e^{-x}\), \(x\geq 0\)", r"\(f^{\prime}=(1-x)e^{-x}\)", r"maximum bij \(x=1\)"],
                             ["opbrengst", r"\(O(p)=p(100-2p)\)", r"\(100-4p=0\): prijs \(25\) euro"]])),
        ]),
    ],
    onthoud=[
        r"\(f^{\prime}>0\): stijgen; \(f^{\prime}<0\): dalen. Tekenwissel van \(f^{\prime}\) = extremum.",
        r"\(f^{\prime\prime}>0\): hol; \(f^{\prime\prime}<0\): bol. Tekenwissel van \(f^{\prime\prime}\) = buigpunt.",
        r"\(f^{\prime}(a)=0\) of \(f^{\prime\prime}(a)=0\) alleen is niet genoeg.",
        "Extremumprobleem: voorschrift, domein, afleiden, controleren, antwoord in een zin.",
    ])


# ───────────────────────── 17. Bedrijfswetenschappen: integralen en oppervlakte
zet("bedrijfswetenschappen-integralen-en-oppervlakte",
    titel="Bedrijfswetenschappen: integralen en oppervlakte",
    onder="Oppervlakte benaderen met rechthoekjes, primitieve functies zoeken en bepaalde integralen berekenen.",
    secties=[
        dict(kop="Oppervlakte benaderen", blokken=[
            ("p", r"Je verdeelt \([a,b]\) in deelintervallen met breedte \(\Delta x\) en zet op elk een rechthoekje. De som \(\sum f(x_{i})\cdot\Delta x\) heet een <strong>Riemannsom</strong>. "
                  r"Bij een <strong>stijgende</strong> functie neem je voor de <strong>ondersom</strong> als hoogte de functiewaarde in het <strong>linkereindpunt</strong>, voor de <strong>bovensom</strong> die in het rechtereindpunt."),
            ("fig", svg.naast_elkaar([
                plot([(lambda x: x, "v", "")], 0, 4.4, 0, 4.4, breedte=220, hoogte=200, rechthoeken=[(i, i + 1, i) for i in range(4)], xlabel="x", ylabel="y"),
                plot([(lambda x: x, "v", "")], 0, 4.4, 0, 4.4, breedte=220, hoogte=200, rechthoeken=[(i, i + 1, i + 1) for i in range(4)], xlabel="x", ylabel="y")]),
             r"\(f(x)=x\) op \([0,4]\): ondersom \(0+1+2+3=6\) (links), bovensom \(1+2+3+4=10\) (rechts). De echte oppervlakte \(8\) ligt ertussen."),
            ("p", r"Hoe meer deelintervallen, hoe beter de benadering. Als het aantal deelintervallen naar oneindig gaat, worden onder- en bovensom gelijk: de limiet van de ondersommen en bovensommen is de "
                  r"<strong>bepaalde integraal</strong> \(\displaystyle\int_{a}^{b}f(x)\,dx\). Daarin is \(f(x)\) de <strong>integrand</strong> en komt \(dx\) overeen met \(\Delta x\), de breedte van de rechthoekjes."),
            ("kader", r"<ul><li>Is \(f(x)\geq 0\) op \([a,b]\), dan is \(\int_{a}^{b}f(x)\,dx\) de <strong>oppervlakte</strong> tussen de grafiek en de \(x\)-as.</li>"
                      r"<li>Ligt de grafiek <strong>onder</strong> de \(x\)-as, dan is de integraal over dat stuk <strong>negatief</strong>.</li>"
                      r"<li>\(\int_{a}^{a}f(x)\,dx=0\) en \(\int_{0}^{4}f\,dx=\int_{0}^{1}f\,dx+\int_{1}^{4}f\,dx\).</li>"
                      r"<li>Bij een dalende functie is de ondersom nog altijd de kleinste: dan neem je de rechterkant.</li></ul>"),
        ]),
        dict(kop="Primitieve functies", blokken=[
            ("p", r"\(F\) is een <strong>primitieve functie</strong> van \(f\) als \(F^{\prime}(x)=f(x)\). Een functie heeft er oneindig veel: \(x^{3}\), \(x^{3}+5\) en \(x^{3}-2\) zijn allemaal primitieven van \(3x^{2}\). "
                  r"Je schrijft \(\int f(x)\,dx=F(x)+c\)."),
            ("kader", tabel([r"\(f(x)\)", r"\(\int f(x)\,dx\)"],
                            [[r"\(k\) (constante)", r"\(kx+c\), bv. \(\int 7\,dx=7x+c\)"],
                             [r"\(x^{n}\) (\(n\neq -1\))", r"\(\dfrac{x^{n+1}}{n+1}+c\), bv. \(\int x^{4}\,dx=\dfrac{x^{5}}{5}+c\)"],
                             [r"\(k\cdot f(x)\)", r"\(k\int f(x)\,dx\)"],
                             [r"\(f(x)+g(x)\)", r"\(\int f(x)\,dx+\int g(x)\,dx\) (een som, geen product)"]])),
            ("p", r"Voorbeeld: \(\int(6x^{2}-4x+3)\,dx=2x^{3}-2x^{2}+3x+c\)."),
        ]),
        dict(kop="Bepaalde integralen berekenen", blokken=[
            ("kader", r"<p style='text-align:center'><strong>\(\displaystyle\int_{a}^{b}f(x)\,dx=\big[F(x)\big]_{a}^{b}=F(b)-F(a)\)</strong></p>"),
            ("kader", tabel(["integraal", "berekening", "resultaat"],
                            [[r"\(\int_{0}^{3}x^{2}\,dx\)", r"\(\left[\frac{x^{3}}{3}\right]_{0}^{3}=9-0\)", r"\(9\)"],
                             [r"\(\int_{1}^{2}(4x^{3}-2x)\,dx\)", r"\(\left[x^{4}-x^{2}\right]_{1}^{2}=12-0\)", r"\(12\)"],
                             [r"\(\int_{0}^{1}(3x^{2}+2x+1)\,dx\)", r"\(\left[x^{3}+x^{2}+x\right]_{0}^{1}\)", r"\(3\)"],
                             [r"\(\int_{1}^{3}x\,dx\)", r"\(\left[\frac{x^{2}}{2}\right]_{1}^{3}=\frac{9}{2}-\frac{1}{2}\)", r"\(4\) (niet \(3-1\))"],
                             [r"\(\int_{0}^{2}(x^{2}-4)\,dx\)", r"\(\frac{8}{3}-8\)", r"\(-\frac{16}{3}\): de grafiek ligt onder de as"]])),
        ]),
        dict(kop="Werkelijke oppervlakte", blokken=[
            ("p", r"Wisselt de functie van teken, dan <strong>splits</strong> je de integraal bij de nulwaarden en neem je de stukken onder de as met een minteken. "
                  r"\(\int_{-1}^{1}x^{3}\,dx=0\), maar de werkelijke oppervlakte is \(\frac{1}{4}+\frac{1}{4}=\frac{1}{2}\)."),
            ("p", r"Zo is de oppervlakte tussen \(y=x^{2}-1\) en de \(x\)-as op \([0,2]\) gelijk aan \(-\int_{0}^{1}(x^{2}-1)\,dx+\int_{1}^{2}(x^{2}-1)\,dx\)."),
            ("p", r"<strong>Tussen twee krommen</strong>, met \(f(x)\geq g(x)\) op \([a,b]\): \(\displaystyle\int_{a}^{b}\big(f(x)-g(x)\big)\,dx\). De bovenste functie komt eerst. "
                  r"De grenzen van het ingesloten stuk zijn de \(x\)-waarden van de snijpunten."),
            ("fig", plot([(lambda x: 2 * x, "a", "y = 2x"), (lambda x: x * x, "v", "y = x²")], -0.5, 2.6, -0.5, 5.5,
                         vlak=(lambda x: 2 * x, 0, 2, lambda x: x * x), punten=[(0, 0, ""), (2, 4, "(2, 4)")]),
             r"\(x^{2}=2x\) geeft \(x=0\) of \(x=2\). Oppervlakte: \(\int_{0}^{2}(2x-x^{2})\,dx=4-\frac{8}{3}=\frac{4}{3}\)."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("kader", tabel(["gegeven", "de integraal geeft", "voorbeeld"],
                            [[r"snelheid \(v(t)\)", "de afgelegde weg", r"\(v=2t\) m/s: \(\int_{0}^{5}2t\,dt=25\) m; \(v=3t^{2}\): \(\int_{1}^{2}3t^{2}\,dt=7\) m"],
                             [r"marginale kost \(K^{\prime}(q)\)", "de extra kost (primitiveren geeft de kostfunctie)", r"\(\int_{10}^{20}(2q+10)\,dq=600-200=400\) euro"],
                             [r"debiet \(d(t)\)", "de hoeveelheid die erin stroomt", r"\(\int_{0}^{6}(6-t)\,dt=18\) liter"]])),
        ]),
    ],
    onthoud=[
        "Riemannsom: rechthoekjes; meer deelintervallen geeft een betere benadering.",
        r"Primitieve: \(F^{\prime}=f\); \(\int x^{n}\,dx=\frac{x^{n+1}}{n+1}+c\).",
        r"\(\int_{a}^{b}f(x)\,dx=F(b)-F(a)\).",
        "Onder de x-as is de integraal negatief: splits bij de nulwaarden.",
        r"Tussen twee krommen: \(\int_{a}^{b}(\text{boven}-\text{onder})\,dx\).",
    ])


# ───────────────────────── 18. Bedrijfswetenschappen: matrices, grafen en stelsels
zet("bedrijfswetenschappen-matrices-grafen-en-stelsels",
    titel="Bedrijfswetenschappen: matrices, grafen en stelsels",
    onder="Rekenen met matrices, overgangsmatrices en grafen, en stelsels oplossen met Gauss-Jordan.",
    secties=[
        dict(kop="Matrices", blokken=[
            ("p", r"Een matrix met \(m\) rijen en \(n\) kolommen heeft <strong>dimensie</strong> \(m\times n\). Het element \(a_{ij}\) staat op rij \(i\), kolom \(j\): in "
                  r"\(A=\begin{bmatrix}4&7&1\\2&5&9\end{bmatrix}\) (dimensie \(2\times 3\)) is \(a_{23}=9\). Twee matrices zijn <strong>gelijk</strong> als ze dezelfde dimensie hebben en alle overeenkomstige elementen gelijk zijn."),
            ("kader", tabel(["soort", "voorbeeld"],
                            [["eenheidsmatrix van orde 2", r"\(I=\begin{bmatrix}1&0\\0&1\end{bmatrix}\)"],
                             ["diagonaalmatrix", r"\(\begin{bmatrix}3&0\\0&-2\end{bmatrix}\)"],
                             [r"symmetrische matrix (\(A^{T}=A\)), niet altijd diagonaal", r"\(\begin{bmatrix}1&5\\5&2\end{bmatrix}\)"],
                             ["getransponeerde: rijen worden kolommen", r"\(\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}^{T}=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}\)"]])),
        ]),
        dict(kop="Rekenen met matrices", blokken=[
            ("kader", tabel(["bewerking", "regel", "voorbeeld"],
                            [["optellen", "enkel bij dezelfde dimensie, element per element", r"\(\begin{bmatrix}1&2\\3&4\end{bmatrix}+\begin{bmatrix}5&0\\-1&2\end{bmatrix}=\begin{bmatrix}6&2\\2&6\end{bmatrix}\)"],
                             ["met een getal", "elk element", r"\(3\begin{bmatrix}2&-1\\0&4\end{bmatrix}=\begin{bmatrix}6&-3\\0&12\end{bmatrix}\)"],
                             ["tegengestelde", r"symmetrisch element voor de optelling", r"\(-A\)"],
                             ["vermenigvuldigen", r"rij maal kolom; \((m\times n)\cdot(n\times p)\) geeft \(m\times p\)", r"\(\begin{bmatrix}1&2\\0&3\end{bmatrix}\begin{bmatrix}4\\5\end{bmatrix}=\begin{bmatrix}14\\15\end{bmatrix}\)"]])),
            ("kader", r"<ul><li>\(A\cdot B\) bestaat enkel als het aantal kolommen van \(A\) gelijk is aan het aantal rijen van \(B\). Een \(2\times 3\)-matrix kan je dus niet met zichzelf vermenigvuldigen.</li>"
                      r"<li>Meestal is \(A\cdot B\neq B\cdot A\), ook bij vierkante matrices.</li>"
                      r"<li>\(A\cdot B\) kan de nulmatrix zijn terwijl \(A\) en \(B\) dat niet zijn.</li>"
                      r"<li>\(A(B+C)=AB+AC\) en \((AB)^{T}=B^{T}A^{T}\).</li>"
                      r"<li>\(A=\begin{bmatrix}2&0\\1&1\end{bmatrix}\): \(A^{2}=\begin{bmatrix}4&0\\3&1\end{bmatrix}\), want rij \(2\) maal kolom \(1\) is \(1\cdot 2+1\cdot 1=3\).</li>"
                      r"<li>Omzet van \(10\) broden aan \(3\) euro en \(4\) taarten aan \(12\) euro: \(\begin{bmatrix}10&4\end{bmatrix}\cdot\begin{bmatrix}3\\12\end{bmatrix}=78\) euro.</li></ul>"),
        ]),
        dict(kop="Overgangsmatrices en grafen", blokken=[
            ("p", r"Een <strong>overgangsmatrix</strong> (Markov-matrix) \(T\) geeft de kansen om van een toestand (kolom) naar een andere (rij) te gaan: elke <strong>kolom</strong> telt op tot \(1\). "
                  r"De toestand na \(n\) stappen is \(T^{n}\cdot X_{0}\). Een <strong>evenwichtstoestand</strong> \(X\) verandert niet meer: \(T\cdot X=X\). Ook bij een migratiematrix verhuist er dan nog wel iemand: er verhuizen evenveel mensen, maar evenveel in beide richtingen."),
            ("kader", r"<p>\(T=\begin{bmatrix}0{,}8&0{,}3\\0{,}2&0{,}7\end{bmatrix}\), \(X_{0}=\begin{bmatrix}100\\100\end{bmatrix}\): \(T\cdot X_{0}=\begin{bmatrix}80+30\\20+70\end{bmatrix}=\begin{bmatrix}110\\90\end{bmatrix}\).</p>"),
            ("p", r"In een <strong>Lesliematrix</strong> staan op de eerste rij de vruchtbaarheidscijfers van elke leeftijdsklasse, en daaronder de overlevingskansen."),
            ("p", r"In de <strong>verbindingsmatrix</strong> \(M\) van een graaf staat een \(1\) op plaats \((i,j)\) als er een rechtstreekse verbinding (pijl) is tussen de knopen, van knoop \(i\) naar knoop \(j\). "
                  r"\(M^{2}\) telt de wegen van lengte \(2\). De graaf met \(A\to B\), \(B\to C\), \(C\to A\) heeft \(M=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}\): drie enen."),
        ]),
        dict(kop="Stelsels met Gauss-Jordan", blokken=[
            ("p", r"Je schrijft een stelsel als <strong>uitgebreide coëfficiëntenmatrix</strong>: "
                  r"\(\begin{cases}2x+y=5\\x-3y=1\end{cases}\) wordt \(\left[\begin{array}{cc|c}2&1&5\\1&-3&1\end{array}\right]\)."),
            ("kader", r"<p><strong>Elementaire rijoperaties</strong> (twee elementen binnen een rij wisselen hoort er niet bij):</p><ul>"
                      r"<li>twee rijen van plaats wisselen;</li><li>een rij vermenigvuldigen met een getal dat niet \(0\) is;</li><li>bij een rij een veelvoud van een andere rij optellen.</li></ul>"),
            ("p", r"Je werkt tot de <strong>rijcanonieke vorm</strong>: elke leidende coëfficiënt is \(1\), met nullen erboven en eronder, en de leidende enen schuiven naar rechts op."),
            ("kader", r"<p>\(\begin{cases}x+y=7\\x-y=1\end{cases}\): \(\left[\begin{array}{cc|c}1&1&7\\1&-1&1\end{array}\right]\xrightarrow{R_{2}-R_{1}}\left[\begin{array}{cc|c}1&1&7\\0&-2&-6\end{array}\right]"
                      r"\xrightarrow{R_{2}:(-2)}\left[\begin{array}{cc|c}1&1&7\\0&1&3\end{array}\right]\xrightarrow{R_{1}-R_{2}}\left[\begin{array}{cc|c}1&0&4\\0&1&3\end{array}\right]\): \(x=4\), \(y=3\).</p>"),
            ("kader", tabel(["eindmatrix", "soort stelsel", "oplossing"],
                            [[r"\(\left[\begin{array}{cc|c}1&0&2\\0&1&-1\end{array}\right]\)", "bepaald: precies één oplossing", r"\(V=\{(2,-1)\}\)"],
                             [r"rij \(\left[\begin{array}{ccc|c}0&0&0&4\end{array}\right]\)", r"<strong>strijdig</strong> (\(0=4\))", r"\(V=\varnothing\)"],
                             [r"\(\left[\begin{array}{ccc|c}1&0&2&3\\0&1&-1&1\\0&0&0&0\end{array}\right]\)", "onbepaald met één vrijheidsgraad", r"\(z=r\): \(V=\{(3-2r,\ 1+r,\ r)\mid r\in\mathbb{R}\}\)"]])),
            ("p", r"Een nulrij \(\left[\begin{array}{ccc|c}0&0&0&0\end{array}\right]\) (\(0=0\)) maakt een stelsel dus <strong>niet</strong> strijdig."),
            ("p", r"Toepassing: een bakker met \(30\) kg bloem en \(10\) uur maakt broden \(x\) (\(0{,}5\) kg, \(0{,}1\) uur) en taarten \(y\) (\(1\) kg, \(0{,}5\) uur). Als hij alles opgebruikt: "
                  r"\(\begin{cases}0{,}5x+y=30\\0{,}1x+0{,}5y=10\end{cases}\)."),
        ]),
    ],
    onthoud=[
        r"Dimensie \(m\times n\); \(a_{ij}\) op rij \(i\), kolom \(j\).",
        r"Product: rij maal kolom; \((m\times n)(n\times p)=m\times p\); meestal \(AB\neq BA\).",
        r"Overgangsmatrix: kolommen tellen op tot \(1\); \(X_{n}=T^{n}X_{0}\); evenwicht \(TX=X\).",
        r"Verbindingsmatrix: \(M^{2}\) telt wegen van lengte \(2\).",
        "Gauss-Jordan: bepaald, strijdig (0 = getal) of onbepaald (nulrij, vrije parameter).",
    ])


# ───────────────────────── 19. Bedrijfswetenschappen: hypothesetoetsen en correlatie
def _wolk(helling, ruis, n=14, zaad=3):
    """Vaste puntenwolk (geen toeval bij elke render), voor een spreidingsdiagram."""
    pts, s = [], zaad
    for i in range(n):
        s = (s * 1103515245 + 12345) % 2 ** 31
        e = (s / 2 ** 31 - 0.5) * 2 * ruis
        x = 0.4 + i * 4.2 / (n - 1)
        pts.append((x, 2.5 + helling * (x - 2.5) + e, ""))
    return pts


SPREIDING = svg.naast_elkaar([
    plot([(lambda x: 2.5 + 0.9 * (x - 2.5), "a", "")], 0, 5, 0, 5, breedte=150, hoogte=140, punten=_wolk(0.9, 0.5), xlabel="", ylabel=""),
    plot([(lambda x: 2.5 - 0.9 * (x - 2.5), "a", "")], 0, 5, 0, 5, breedte=150, hoogte=140, punten=_wolk(-0.9, 0.5, zaad=7), xlabel="", ylabel=""),
    plot([], 0, 5, 0, 5, breedte=150, hoogte=140, punten=_wolk(0, 2.2, zaad=11), xlabel="", ylabel="")])

zet("bedrijfswetenschappen-hypothesetoetsen-en-correlatie",
    titel="Bedrijfswetenschappen: hypothesetoetsen en correlatie",
    onder="Met een steekproef een bewering toetsen, en het verband tussen twee grootheden beschrijven.",
    secties=[
        dict(kop="Hypothesen opstellen", blokken=[
            ("p", r"De <strong>nulhypothese</strong> \(H_{0}\) is de bewering die je toetst; ze bevat altijd een gelijkheidsteken. De <strong>alternatieve hypothese</strong> \(H_{1}\) is wat je vermoedt."),
            ("kader", tabel(["situatie", r"\(H_{0}\)", r"\(H_{1}\)", "toets"],
                            [[r"pakken van \(500\) g, je denkt dat ze minder wegen", r"\(\mu=500\)", r"\(\mu<500\)", "eenzijdig (links)"],
                             [r"leerlingen scoren hoger dan \(65\)", r"\(\mu=65\)", r"\(\mu>65\)", "eenzijdig (rechts)"],
                             [r"machine van \(1\) liter ontregeld, te veel of te weinig", r"\(\mu=1\)", r"\(\mu\neq 1\)", "tweezijdig"],
                             [r"partij zegt \(40\%\) van de kiezers", r"\(p=0{,}40\)", r"\(p<0{,}40\)", "eenzijdig"]])),
            ("p", r"\(\mu\) is het populatiegemiddelde, \(p\) de <strong>populatieproportie</strong>. De <strong>steekproefproportie</strong> verschilt van steekproef tot steekproef: "
                  r"\(180\) van \(500\) kiezers geeft \(\hat{p}=\frac{180}{500}=0{,}36\). Bij grote steekproeven heeft het steekproefgemiddelde bij benadering een <strong>normale verdeling</strong>."),
        ]),
        dict(kop="p-waarde en besluit", blokken=[
            ("p", r"De <strong>p-waarde</strong> is de kans op een steekproefresultaat dat minstens zo extreem is, <strong>als \(H_{0}\) waar is</strong>. Het is dus <strong>niet</strong> de kans dat \(H_{0}\) waar is."),
            ("fig", svg.normaalkromme(500, 4, None, 492, xlabel="gemiddeld gewicht in g", toon_kans=True),
             r"Als \(H_{0}\) waar is: een steekproefgemiddelde van \(492\) g of minder is erg onwaarschijnlijk (kleine p-waarde)."),
            ("kader", r"<p style='text-align:center'>\(p\leq\alpha\): <strong>\(H_{0}\) verwerpen</strong> &nbsp;&nbsp;|&nbsp;&nbsp; \(p>\alpha\): <strong>\(H_{0}\) niet verwerpen</strong></p>"),
            ("kader", tabel([r"\(\alpha\)", "p-waarde", "besluit"],
                            [[r"\(0{,}05\)", r"\(0{,}02\)", r"\(H_{0}\) verwerpen"],
                             [r"\(0{,}01\)", r"\(0{,}03\)", r"\(H_{0}\) niet verwerpen"],
                             [r"\(0{,}05\)", r"\(0{,}05\)", r"\(H_{0}\) verwerpen (\(p\leq\alpha\))"],
                             [r"\(0{,}05\)", r"\(0{,}30\)", "het resultaat is goed te verklaren als \\(H_{0}\\) waar is"]])),
            ("p", r"Het <strong>significantieniveau</strong> \(\alpha\) kies je <strong>vooraf</strong>, voor je de gegevens bekijkt. Bij \(\alpha=5\%\) aanvaard je \(5\%\) kans om \(H_{0}\) ten onrechte te verwerpen. "
                  r"Hoe kleiner de p-waarde, hoe sterker het bewijs tegen \(H_{0}\). Bij een grotere \(\alpha\) (bv. \(0{,}10\)) verwerp je sneller dan bij \(0{,}01\). "
                  r"Verwerp je \(H_{0}\) niet, dan heb je <strong>niet bewezen</strong> dat \(H_{0}\) waar is: je hebt alleen te weinig bewijs ertegen."),
        ]),
        dict(kop="Spreidingsdiagram en correlatie", blokken=[
            ("p", r"Een <strong>spreidingsdiagram</strong> heeft een punt per waarneming: de onafhankelijke variabele (wat je zelf verandert, zoals het aantal uren studie) horizontaal, "
                  r"de afhankelijke (de punten op de toets) verticaal."),
            ("fig", SPREIDING, r"Links \(r\approx 0{,}9\) (stijgend), midden \(r\approx -0{,}9\) (dalend), rechts \(r\approx 0\): geen patroon."),
            ("p", r"De <strong>correlatiecoëfficiënt</strong> \(r\) meet hoe sterk de puntenwolk op een rechte lijkt. Een positieve correlatie: bij grotere \(x\) meestal grotere \(y\)."),
            ("kader", tabel([r"\(r\)", "betekenis"],
                            [[r"tussen \(-1\) en \(1\)", "altijd"],
                             [r"dicht bij \(1\)", "sterk stijgend lineair verband: grotere \\(x\\), meestal grotere \\(y\\)"],
                             [r"dicht bij \(-1\)", r"sterk dalend lineair verband; \(-0{,}95\) is sterker dan \(0{,}8\)"],
                             [r"\(0{,}35\)", "zwak en positief"],
                             [r"dicht bij \(0\)", "geen <strong>lineair</strong> verband (bij een perfect kwadratisch verband, een parabool met de top in het midden, is \\(r\\approx 0\\))"]])),
            ("p", r"Recht evenredige grootheden liggen op een rechte door de oorsprong; omgekeerd evenredige volgen \(y=\dfrac{a}{x}\). "
                  r"Bij een lineair verband liggen de punten ongeveer op een rechte."),
        ]),
        dict(kop="Trendlijn en causaliteit", blokken=[
            ("p", r"De trendlijn en \(r\) bepaal je met ICT, zoals een rekenapp of rekenblad. Trendlijn \(y=2{,}5x+40\) (\(x\): reclame in duizend euro, \(y\): verkoop in duizend stuks): "
                  r"per duizend euro reclame extra stijgt de verkoop met ongeveer \(2500\) stuks. Bij \(x=10\) verwacht je \(2{,}5\cdot 10+40=65\) duizend stuks."),
            ("p", r"Voorspel niet ver <strong>buiten</strong> het bereik van de gemeten gegevens: daar weet je niet of het verband nog geldt."),
            ("weetje", r"<strong>Samenhang is geen oorzaak.</strong> De ijsverkoop en het aantal zonnebrandgevallen hangen sterk samen, maar de echte verklaring is een derde, verborgen variabele: het warme, zonnige weer. "
                       r"\(r=-0{,}85\) tussen prijs en verkochte stuks betekent een sterk dalend verband: bij hogere prijzen worden minder stuks verkocht."),
        ]),
    ],
    onthoud=[
        r"\(H_{0}\) met \(=\); \(H_{1}\) met \(<\), \(>\) (eenzijdig) of \(\neq\) (tweezijdig).",
        r"p-waarde: kans op zo'n resultaat als \(H_{0}\) waar is. \(p\leq\alpha\): verwerpen.",
        r"Niet verwerpen is niet bewijzen.",
        r"\(r\) tussen \(-1\) en \(1\); dicht bij \(\pm 1\) sterk lineair, dicht bij \(0\) geen lineair verband.",
        "Correlatie is geen causaliteit; niet ver buiten de gegevens voorspellen.",
    ])
