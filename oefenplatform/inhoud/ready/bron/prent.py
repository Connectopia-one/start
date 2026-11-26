# -*- coding: utf-8 -*-
"""Eenvoudige, zelfgetekende prenten (svg) voor de Ready-vragen (3de en 4de leerjaar).
Elke prent komt in public/examenvormen/ready/ en de vraag verwijst ernaar met
afbeelding_pad "/examenvormen/ready/<naam>.svg". Kim, 26/11: "moeten we niet ook
meer prenten erbij hebben?" Duidelijke lijnen, grote cijfers, witte achtergrond."""
import math, pathlib

MAP = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "ready"
DARK, ORANJE, PAARS, GROEN, BLAUW, GEEL, ROOD, GRIJS = "#2f4a22", "#c4622d", "#7a5aa6", "#6f9a4a", "#3d7fb8", "#f2c94c", "#d0453a", "#888"
FONT = "Nunito, Arial, sans-serif"
GEMAAKT = {}


def svg(b, h, inhoud):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {b} {h}" width="{b * 2}" height="{h * 2}" '
            f'font-family="{FONT}"><rect width="{b}" height="{h}" fill="#fff"/>{inhoud}</svg>')


def bewaar(naam, s):
    GEMAAKT[naam] = s
    MAP.mkdir(parents=True, exist_ok=True)
    (MAP / f"{naam}.svg").write_text(s, encoding="utf-8")
    return f"/examenvormen/ready/{naam}.svg"


def T(x, y, s, m=14, k=DARK, a="middle", w="400"):
    return f'<text x="{x}" y="{y}" font-size="{m}" fill="{k}" text-anchor="{a}" font-weight="{w}">{s}</text>'


def letters(*ls, y=None):
    return ""


# ------------------------------------------------------------------ wiskunde
def klok(uur, minuut, cx=90, cy=90, r=80, digitaal=None):
    d = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{DARK}" stroke-width="4"/>']
    for i in range(1, 13):
        a = math.radians(i * 30 - 90)
        d.append(T(f"{cx + (r - 17) * math.cos(a):.1f}", f"{cy + (r - 17) * math.sin(a) + 6:.1f}", i, 17))
    for i in range(60):
        a = math.radians(i * 6 - 90); l = 7 if i % 5 == 0 else 3
        d.append(f'<line x1="{cx + r * math.cos(a):.1f}" y1="{cy + r * math.sin(a):.1f}" x2="{cx + (r - l) * math.cos(a):.1f}" y2="{cy + (r - l) * math.sin(a):.1f}" stroke="{DARK}" stroke-width="1.5"/>')
    au = math.radians((uur % 12 + minuut / 60) * 30 - 90); am = math.radians(minuut * 6 - 90)
    d.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r * .5 * math.cos(au):.1f}" y2="{cy + r * .5 * math.sin(au):.1f}" stroke="{ORANJE}" stroke-width="8" stroke-linecap="round"/>')
    d.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r * .78 * math.cos(am):.1f}" y2="{cy + r * .78 * math.sin(am):.1f}" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>')
    d.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{DARK}"/>')
    return "".join(d)


def p_klok(naam, uur, minuut):
    return bewaar(naam, svg(180, 180, klok(uur, minuut)))


def p_digitaal(naam, tekst):
    return bewaar(naam, svg(220, 100, f'<rect x="10" y="10" width="200" height="80" rx="14" fill="#1f2a1a"/>' + T(110, 70, tekst, 48, "#9be07a", w="700")))


def p_taart(naam, n, k, kleur=PAARS):
    c, r, d = 90, 80, []
    for i in range(n):
        a1 = math.radians(i * 360 / n - 90); a2 = math.radians((i + 1) * 360 / n - 90)
        d.append(f'<path d="M{c},{c} L{c + r * math.cos(a1):.1f},{c + r * math.sin(a1):.1f} A{r},{r} 0 0 1 {c + r * math.cos(a2):.1f},{c + r * math.sin(a2):.1f} Z" fill="{kleur if i < k else "#fff"}" stroke="{DARK}" stroke-width="3"/>')
    return bewaar(naam, svg(180, 180, "".join(d)))


def p_balk(naam, n, k, kleur=ORANJE):
    w = 300 / n
    return bewaar(naam, svg(320, 70, "".join(f'<rect x="{10 + i * w:.1f}" y="10" width="{w:.1f}" height="50" fill="{kleur if i < k else "#fff"}" stroke="{DARK}" stroke-width="3"/>' for i in range(n))))


def p_blokken(naam, d_, h, t, e):
    """MAB-blokken: duizend = grote kubus, honderd = plaat, tien = staaf, eenheid = blokje."""
    o, x = [], 10
    for _ in range(d_):
        o.append(f'<rect x="{x}" y="20" width="60" height="60" fill="#f3c9a8" stroke="{DARK}" stroke-width="2"/><polygon points="{x},20 {x + 14},6 {x + 74},6 {x + 60},20" fill="#f8dcc6" stroke="{DARK}" stroke-width="2"/><polygon points="{x + 60},20 {x + 74},6 {x + 74},66 {x + 60},80" fill="#e0a77e" stroke="{DARK}" stroke-width="2"/>'); x += 84
    for _ in range(h):
        o.append(f'<rect x="{x}" y="20" width="44" height="60" fill="#cfe3b8" stroke="{DARK}" stroke-width="2"/>' + "".join(f'<line x1="{x}" y1="{20 + j * 6}" x2="{x + 44}" y2="{20 + j * 6}" stroke="{DARK}" stroke-width=".6"/>' for j in range(1, 10))); x += 52
    for _ in range(t):
        o.append(f'<rect x="{x}" y="20" width="10" height="60" fill="{GEEL}" stroke="{DARK}" stroke-width="2"/>'); x += 16
    for i in range(e):
        o.append(f'<rect x="{x}" y="{70 - (i % 2) * 14}" width="10" height="10" fill="{BLAUW}" stroke="{DARK}" stroke-width="1.5"/>'); x += 8 if i % 2 == 0 else 8
    return bewaar(naam, svg(max(x + 20, 200), 100, "".join(o)))


def p_getallenlijn(naam, van, tot, stap, pijl_bij, labels=None):
    n = (tot - van) // stap; w = 340 / n; d = [f'<line x1="20" y1="50" x2="370" y2="50" stroke="{DARK}" stroke-width="3"/>']
    for i in range(n + 1):
        x = 20 + i * w; v = van + i * stap
        d.append(f'<line x1="{x:.1f}" y1="40" x2="{x:.1f}" y2="60" stroke="{DARK}" stroke-width="2"/>')
        if labels is None or v in labels: d.append(T(f"{x:.1f}", 82, f"{v:,}".replace(",", " "), 13))
    x = 20 + (pijl_bij - van) / stap * w
    d.append(f'<polygon points="{x:.1f},36 {x - 9:.1f},16 {x + 9:.1f},16" fill="{ORANJE}"/>' + T(f"{x:.1f}", 12, "?", 14, ORANJE, w="700"))
    return bewaar(naam, svg(390, 95, "".join(d)))


def p_munten(naam, bedragen):
    """bedragen in cent; munten < 500 als cirkel, briefjes als rechthoek."""
    d, x = [], 10
    for b in bedragen:
        if b >= 500:
            d.append(f'<rect x="{x}" y="20" width="110" height="60" rx="6" fill="#d9ecf7" stroke="{BLAUW}" stroke-width="3"/>' + T(x + 55, 60, f"{b // 100} €", 22, BLAUW, w="700")); x += 120
        else:
            r = 26 if b >= 100 else 22
            kl = "#e9c46a" if b >= 100 or b in (10, 20, 50) else "#d08a5a"
            s = f"{b // 100} €" if b >= 100 else f"{b} c"
            d.append(f'<circle cx="{x + r}" cy="50" r="{r}" fill="{kl}" stroke="{DARK}" stroke-width="2"/>' + T(x + r, 56, s, 15, DARK, w="700")); x += 2 * r + 10
    return bewaar(naam, svg(x + 10, 100, "".join(d)))


def p_figuur(naam, soort):
    s = f'stroke="{DARK}" stroke-width="4" fill="#f8dcc6"'
    f = {"vierkant": f'<rect x="50" y="20" width="120" height="120" {s}/>',
         "rechthoek": f'<rect x="20" y="40" width="180" height="90" {s}/>',
         "driehoek": f'<polygon points="30,140 190,140 110,20" {s}/>',
         "cirkel": f'<circle cx="110" cy="80" r="62" {s}/>',
         "zeshoek": "<polygon points=\"" + " ".join(f"{110 + 65 * math.cos(math.radians(60 * i)):.1f},{80 + 65 * math.sin(math.radians(60 * i)):.1f}" for i in range(6)) + f'" {s}/>',
         "vijfhoek": "<polygon points=\"" + " ".join(f"{110 + 65 * math.cos(math.radians(72 * i - 90)):.1f},{85 + 65 * math.sin(math.radians(72 * i - 90)):.1f}" for i in range(5)) + f'" {s}/>',
         "ruit": f'<polygon points="110,8 158,80 110,152 62,80" {s}/>'}[soort]
    return bewaar(naam, svg(220, 160, f))


def p_hoek(naam, soort):
    s = f'stroke="{DARK}" stroke-width="5" fill="none" stroke-linecap="round"'
    pts = {"recht": "40,20 40,140 190,140", "scherp": "170,30 40,140 200,140", "stomp": "10,60 70,140 210,140"}[soort]
    extra = f'<rect x="40" y="116" width="24" height="24" fill="none" stroke="{ORANJE}" stroke-width="3"/>' if soort == "recht" else ""
    return bewaar(naam, svg(220, 160, f'<polyline points="{pts}" {s}/>' + extra))


def p_rechthoek_maten(naam, l, b, eenheid="cm", rooster=False):
    W, H = 40 * l if l <= 7 else 280, 40 * b if b <= 4 else 160
    d = [f'<rect x="40" y="20" width="{W}" height="{H}" fill="#f8dcc6" stroke="{DARK}" stroke-width="4"/>']
    if rooster:
        d += [f'<line x1="{40 + i * W / l:.1f}" y1="20" x2="{40 + i * W / l:.1f}" y2="{20 + H}" stroke="{DARK}" stroke-width="1"/>' for i in range(1, l)]
        d += [f'<line x1="40" y1="{20 + j * H / b:.1f}" x2="{40 + W}" y2="{20 + j * H / b:.1f}" stroke="{DARK}" stroke-width="1"/>' for j in range(1, b)]
    else:
        d += [T(40 + W / 2, 20 + H + 26, f"{l} {eenheid}", 18, ORANJE, w="700"), T(40 + W + 30, 20 + H / 2 + 6, f"{b} {eenheid}", 18, ORANJE, w="700")]
    return bewaar(naam, svg(40 + W + 80, H + 60, "".join(d)))


def p_kubussen(naam, l, b, h):
    z, d = 26, []
    for laag in range(h):
        for r in range(b - 1, -1, -1):
            for k in range(l):
                x = 20 + k * z + r * 13; y = 30 + (h) * z + b * 13 - laag * z - r * 13
                d.append(f'<polygon points="{x},{y} {x + z},{y} {x + z},{y - z} {x},{y - z}" fill="#f3c9a8" stroke="{DARK}" stroke-width="1.5"/>'
                         f'<polygon points="{x},{y - z} {x + 13},{y - z - 13} {x + z + 13},{y - z - 13} {x + z},{y - z}" fill="#f8dcc6" stroke="{DARK}" stroke-width="1.5"/>'
                         f'<polygon points="{x + z},{y} {x + z + 13},{y - 13} {x + z + 13},{y - z - 13} {x + z},{y - z}" fill="#e0a77e" stroke="{DARK}" stroke-width="1.5"/>')
    return bewaar(naam, svg(40 + l * z + b * 13 + 20, 50 + h * z + b * 13, "".join(d)))


def p_thermometer(naam, graden, lo=-10, hi=40):
    y = lambda g: 230 - (g - lo) / (hi - lo) * 200
    d = [f'<rect x="60" y="20" width="24" height="220" rx="12" fill="#fff" stroke="{DARK}" stroke-width="3"/>',
         f'<rect x="66" y="{y(graden):.1f}" width="12" height="{238 - y(graden):.1f}" fill="{ROOD}"/>',
         f'<circle cx="72" cy="250" r="20" fill="{ROOD}" stroke="{DARK}" stroke-width="3"/>']
    for g in range(lo, hi + 1, 5):
        d.append(f'<line x1="84" y1="{y(g):.1f}" x2="{98 if g % 10 == 0 else 92}" y2="{y(g):.1f}" stroke="{DARK}" stroke-width="2"/>')
        if g % 10 == 0: d.append(T(102, f"{y(g) + 5:.1f}", f"{g} °C".replace("-", "−"), 14, a="start"))
    return bewaar(naam, svg(170, 280, "".join(d)))


def p_staaf(naam, titel, data, kleur=GROEN):
    m = max(v for _, v in data); w = 260 / len(data)
    d = [T(160, 20, titel, 15, w="700"), f'<line x1="40" y1="200" x2="300" y2="200" stroke="{DARK}" stroke-width="2"/>', f'<line x1="40" y1="200" x2="40" y2="35" stroke="{DARK}" stroke-width="2"/>']
    for g in range(0, m + 1, 2 if m <= 12 else 5):
        yy = 200 - g / m * 150
        d.append(f'<line x1="36" y1="{yy:.1f}" x2="300" y2="{yy:.1f}" stroke="#ddd"/>' + T(30, f"{yy + 4:.1f}", g, 12, a="end"))
    for i, (lab, v) in enumerate(data):
        x = 40 + i * w + w * .2; hh = v / m * 150
        d.append(f'<rect x="{x:.1f}" y="{200 - hh:.1f}" width="{w * .6:.1f}" height="{hh:.1f}" fill="{kleur}"/>' + T(f"{x + w * .3:.1f}", 218, lab, 13))
    return bewaar(naam, svg(320, 230, "".join(d)))


def p_rooster(naam, kolommen, rijen, markeer):
    z, d = 40, []
    for i, k in enumerate(kolommen): d.append(T(50 + i * z + z / 2, 22, k, 16, w="700"))
    for j in range(rijen): d.append(T(20, 30 + j * z + z / 2 + 6, j + 1, 16, w="700"))
    for i in range(len(kolommen)):
        for j in range(rijen):
            d.append(f'<rect x="{50 + i * z}" y="{30 + j * z}" width="{z}" height="{z}" fill="#fff" stroke="{DARK}" stroke-width="1.5"/>')
    for (k, r, teken) in markeer:
        i = kolommen.index(k); d.append(T(50 + i * z + z / 2, 30 + (r - 1) * z + z / 2 + 9, teken, 26))
    return bewaar(naam, svg(60 + len(kolommen) * z, 40 + rijen * z, "".join(d)))


def p_symmetrie(naam, letter):
    return bewaar(naam, svg(160, 160, T(80, 130, letter, 140, DARK, w="700") + f'<line x1="80" y1="5" x2="80" y2="155" stroke="{ORANJE}" stroke-width="3" stroke-dasharray="8 6"/>'))


def p_ruimte(naam, soort):
    s = f'stroke="{DARK}" stroke-width="3"'
    f = {"kubus": f'<rect x="40" y="60" width="100" height="100" fill="#f3c9a8" {s}/><polygon points="40,60 80,20 180,20 140,60" fill="#f8dcc6" {s}/><polygon points="140,60 180,20 180,120 140,160" fill="#e0a77e" {s}/>',
         "cilinder": f'<rect x="50" y="40" width="100" height="110" fill="#cfe3b8" stroke="none"/><line x1="50" y1="40" x2="50" y2="150" {s}/><line x1="150" y1="40" x2="150" y2="150" {s}/><ellipse cx="100" cy="150" rx="50" ry="16" fill="#cfe3b8" {s}/><ellipse cx="100" cy="40" rx="50" ry="16" fill="#e4f0d6" {s}/>',
         "bol": f'<circle cx="100" cy="90" r="70" fill="#d9ecf7" {s}/><ellipse cx="100" cy="90" rx="70" ry="20" fill="none" stroke="{DARK}" stroke-width="1.5" stroke-dasharray="6 5"/>',
         "kegel": f'<polygon points="100,15 45,150 155,150" fill="#f8dcc6" {s}/><ellipse cx="100" cy="150" rx="55" ry="16" fill="#f3c9a8" {s}/>',
         "piramide": f'<polygon points="100,15 30,140 120,165" fill="#f8dcc6" {s}/><polygon points="100,15 120,165 175,125" fill="#e0a77e" {s}/>',
         "balk": f'<rect x="20" y="70" width="140" height="80" fill="#f3c9a8" {s}/><polygon points="20,70 55,40 195,40 160,70" fill="#f8dcc6" {s}/><polygon points="160,70 195,40 195,120 160,150" fill="#e0a77e" {s}/>'}[soort]
    return bewaar(naam, svg(200, 180, f))


# ------------------------------------------------------------------ voorwerpen en dieren (eenvoudig getekend)
def voorwerp(soort, x=0, y=0, s=1):
    g = lambda inner: f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'
    k = f'stroke="{DARK}" stroke-width="3"'
    v = {
        "trein": f'<line x1="0" y1="120" x2="160" y2="120" stroke="#777" stroke-width="5"/>' + "".join(f'<rect x="{6 + i * 22}" y="117" width="8" height="12" fill="#8a5a2b"/>' for i in range(7)) + f'<rect x="10" y="40" width="140" height="60" rx="8" fill="{ROOD}" {k}/><rect x="25" y="52" width="30" height="24" fill="#d9ecf7" {k}/><rect x="70" y="52" width="30" height="24" fill="#d9ecf7" {k}/><rect x="115" y="20" width="30" height="22" fill="{DARK}"/><circle cx="40" cy="105" r="13" fill="{DARK}"/><circle cx="120" cy="105" r="13" fill="{DARK}"/>',
        "ijs": f'<polygon points="60,70 100,70 80,150" fill="#e9c46a" {k}/><circle cx="68" cy="58" r="22" fill="#f3b3c8" {k}/><circle cx="94" cy="58" r="22" fill="#cfe3b8" {k}/><circle cx="80" cy="38" r="22" fill="#f8dcc6" {k}/>',
        "huis": f'<rect x="30" y="70" width="100" height="80" fill="#f8dcc6" {k}/><polygon points="20,72 80,20 140,72" fill="{ROOD}" {k}/><rect x="68" y="105" width="24" height="45" fill="#8a5a2b" {k}/><rect x="40" y="85" width="20" height="20" fill="#d9ecf7" {k}/><rect x="100" y="85" width="20" height="20" fill="#d9ecf7" {k}/>',
        "boom": f'<rect x="70" y="90" width="20" height="60" fill="#8a5a2b" {k}/><circle cx="80" cy="60" r="45" fill="{GROEN}" {k}/>',
        "vis": f'<ellipse cx="75" cy="80" rx="55" ry="30" fill="{BLAUW}" {k}/><polygon points="125,80 155,55 155,105" fill="{BLAUW}" {k}/><circle cx="45" cy="72" r="5" fill="{DARK}"/>',
        "koe": f'<rect x="30" y="60" width="100" height="50" rx="15" fill="#fff" {k}/><circle cx="60" cy="80" r="10" fill="{DARK}"/><circle cx="100" cy="90" r="8" fill="{DARK}"/><rect x="40" y="108" width="10" height="35" fill="#fff" {k}/><rect x="110" y="108" width="10" height="35" fill="#fff" {k}/><ellipse cx="22" cy="60" rx="18" ry="22" fill="#fff" {k}/><ellipse cx="14" cy="72" rx="9" ry="7" fill="#f3b3c8" {k}/>',
        "vogel": f'<ellipse cx="80" cy="85" rx="45" ry="30" fill="{GEEL}" {k}/><circle cx="125" cy="60" r="20" fill="{GEEL}" {k}/><polygon points="143,58 162,64 143,68" fill="{ORANJE}" {k}/><circle cx="130" cy="55" r="4" fill="{DARK}"/><path d="M55 80 Q80 50 105 80" fill="#e9c46a" {k}/><line x1="70" y1="113" x2="65" y2="140" {k}/><line x1="90" y1="113" x2="95" y2="140" {k}/>',
        "ster": f'<polygon points="80,10 98,60 150,60 108,92 124,145 80,112 36,145 52,92 10,60 62,60" fill="{GEEL}" {k}/>',
        "zon": f'<circle cx="80" cy="80" r="35" fill="{GEEL}" {k}/>' + "".join(f'<line x1="{80 + 45 * math.cos(math.radians(a))}" y1="{80 + 45 * math.sin(math.radians(a))}" x2="{80 + 65 * math.cos(math.radians(a))}" y2="{80 + 65 * math.sin(math.radians(a))}" stroke="{ORANJE}" stroke-width="5" stroke-linecap="round"/>' for a in range(0, 360, 45)),
        "bal": f'<circle cx="80" cy="80" r="60" fill="#fff" {k}/><polygon points="80,55 100,70 92,94 68,94 60,70" fill="{DARK}"/>',
        "koning": f'<polygon points="30,90 30,30 55,60 80,20 105,60 130,30 130,90" fill="{GEEL}" {k}/><rect x="30" y="90" width="100" height="20" fill="{GEEL}" {k}/><circle cx="80" cy="70" r="7" fill="{ROOD}"/>',
        "ring": f'<circle cx="80" cy="90" r="45" fill="none" stroke="{GEEL}" stroke-width="14"/><polygon points="80,20 100,40 80,55 60,40" fill="#d9ecf7" {k}/>',
        "bank": f'<rect x="10" y="60" width="140" height="18" rx="4" fill="#8a5a2b" {k}/><rect x="10" y="30" width="140" height="14" rx="4" fill="#8a5a2b" {k}/><rect x="20" y="78" width="10" height="50" fill="{DARK}"/><rect x="130" y="78" width="10" height="50" fill="{DARK}"/>',
        "hond": f'<ellipse cx="85" cy="90" rx="50" ry="25" fill="#c9965a" {k}/><circle cx="35" cy="65" r="24" fill="#c9965a" {k}/><ellipse cx="22" cy="50" rx="8" ry="18" fill="#8a5a2b"/><circle cx="28" cy="62" r="4" fill="{DARK}"/><circle cx="12" cy="72" r="5" fill="{DARK}"/><rect x="50" y="108" width="10" height="35" fill="#c9965a" {k}/><rect x="110" y="108" width="10" height="35" fill="#c9965a" {k}/><path d="M133 85 Q155 60 150 50" fill="none" {k}/>',
    }[soort]
    return g(v)


def p_voorwerp(naam, soort):
    return bewaar(naam, svg(170, 160, voorwerp(soort)))


def p_voorwerpen(naam, soorten):
    return bewaar(naam, svg(170 * len(soorten), 160, "".join(voorwerp(s, i * 170) for i, s in enumerate(soorten))))


def p_insect(naam, poten, kleur=DARK):
    """Lijfje met een aantal poten om te tellen: 6 voor een insect, 8 voor een spin."""
    d = [f'<ellipse cx="110" cy="90" rx="{50 if poten == 6 else 36}" ry="26" fill="{kleur}"/>', f'<circle cx="{50 if poten == 6 else 62}" cy="90" r="18" fill="{kleur}"/>']
    per = poten // 2
    for i in range(per):
        x = 80 + i * (60 / (per - 1))
        d.append(f'<path d="M{x:.0f} 80 L{x - 10:.0f} 45 L{x - 25:.0f} 35" fill="none" stroke="{kleur}" stroke-width="4"/>')
        d.append(f'<path d="M{x:.0f} 100 L{x - 10:.0f} 135 L{x - 25:.0f} 145" fill="none" stroke="{kleur}" stroke-width="4"/>')
    if poten == 6:
        d.append(f'<path d="M40 78 L25 55 M44 76 L36 50" stroke="{kleur}" stroke-width="3" fill="none"/>')
    return bewaar(naam, svg(200, 170, "".join(d)))


def p_plant(naam, pijl_naar):
    """Plant met een oranje pijl naar één deel: wortel, stengel, blad of bloem."""
    d = [f'<rect x="0" y="170" width="240" height="70" fill="#e9d8bf"/>',
         f'<path d="M100 170 L75 210 M100 170 L100 228 M100 170 L125 215 M88 192 L64 200" stroke="#8a5a2b" stroke-width="4" fill="none"/>',
         f'<line x1="100" y1="170" x2="100" y2="60" stroke="{GROEN}" stroke-width="7"/>',
         f'<ellipse cx="72" cy="125" rx="30" ry="12" fill="{GROEN}" transform="rotate(-25 72 125)"/>',
         f'<ellipse cx="128" cy="108" rx="30" ry="12" fill="{GROEN}" transform="rotate(25 128 108)"/>']
    for i in range(6):
        a = math.radians(i * 60); d.append(f'<circle cx="{100 + 16 * math.cos(a):.1f}" cy="{48 + 16 * math.sin(a):.1f}" r="13" fill="#f3b3c8"/>')
    d.append(f'<circle cx="100" cy="48" r="10" fill="{GEEL}"/>')
    doel = {"bloem": (118, 48), "blad": (150, 106), "stengel": (104, 150), "wortel": (126, 214)}[pijl_naar]
    d.append(f'<line x1="215" y1="{doel[1]}" x2="{doel[0] + 14}" y2="{doel[1]}" stroke="{ORANJE}" stroke-width="5"/><polygon points="{doel[0] + 4},{doel[1]} {doel[0] + 20},{doel[1] - 9} {doel[0] + 20},{doel[1] + 9}" fill="{ORANJE}"/>')
    return bewaar(naam, svg(240, 240, "".join(d)))


def p_kompas(naam, vraag_op):
    """Kompasroos met N; één punt heeft een oranje vraagteken."""
    c = 110; d = [f'<circle cx="{c}" cy="{c}" r="80" fill="#fff" stroke="{DARK}" stroke-width="3"/>',
                  f'<polygon points="{c},{c - 75} {c + 14},{c} {c},{c + 75} {c - 14},{c}" fill="{DARK}"/>',
                  f'<polygon points="{c - 75},{c} {c},{c - 14} {c + 75},{c} {c},{c + 14}" fill="{GRIJS}"/>', T(c, 20, "N", 20, w="700")]
    pos = {"O": (c + 97, c + 7), "Z": (c, c + 104), "W": (c - 97, c + 7)}
    for k, (x, y) in pos.items():
        d.append(T(x, y, "?" if k == vraag_op else "", 24, ORANJE, w="700"))
    return bewaar(naam, svg(220, 225, "".join(d)))


def p_vlag(naam, kleuren, horizontaal=False):
    if horizontaal:
        d = "".join(f'<rect x="10" y="{10 + i * 40}" width="180" height="40" fill="{k}" stroke="{DARK}" stroke-width="1"/>' for i, k in enumerate(kleuren))
    else:
        d = "".join(f'<rect x="{10 + i * 60}" y="10" width="60" height="120" fill="{k}" stroke="{DARK}" stroke-width="1"/>' for i, k in enumerate(kleuren))
    return bewaar(naam, svg(200, 140, d))


def p_stroomkring(naam, gesloten=True, met_lepel=False):
    d = [f'<rect x="30" y="110" width="90" height="40" rx="6" fill="{GEEL}" stroke="{DARK}" stroke-width="3"/>', T(75, 136, "batterij", 14),
         f'<circle cx="250" cy="60" r="22" fill="{"#fff6a8" if gesloten else "#fff"}" stroke="{DARK}" stroke-width="3"/>',
         f'<polyline points="120,125 180,125 180,60 228,60" fill="none" stroke="{ORANJE}" stroke-width="4"/>']
    if gesloten:
        d.append(f'<polyline points="272,60 300,60 300,190 30,190 30,150" fill="none" stroke="{ORANJE}" stroke-width="4"/>')
        if gesloten: d += [f'<line x1="250" y1="{30 - i}" x2="250" y2="{20 - i}" stroke="{GEEL}" stroke-width="3"/>' for i in (0,)]
    else:
        d.append(f'<polyline points="272,60 300,60 300,190 190,190" fill="none" stroke="{ORANJE}" stroke-width="4"/><polyline points="140,190 30,190 30,150" fill="none" stroke="{ORANJE}" stroke-width="4"/>')
    return bewaar(naam, svg(330, 210, "".join(d)))


def p_tijdsbalk(naam, punten, vraag=None):
    d = [f'<line x1="15" y1="70" x2="470" y2="70" stroke="{DARK}" stroke-width="4"/><polygon points="470,60 490,70 470,80" fill="{DARK}"/>']
    for x, boven, onder in punten:
        d.append(f'<line x1="{x}" y1="58" x2="{x}" y2="82" stroke="{ORANJE}" stroke-width="4"/>' + T(x, 46, boven, 19, w="700") + T(x, 110, onder, 22, ORANJE if onder == "?" else DARK, w="700"))
    return bewaar(naam, svg(500, 125, "".join(d)))


def p_kasteel(naam, pijl=None):
    k = f'stroke="{DARK}" stroke-width="3"'
    d = [f'<rect x="0" y="190" width="400" height="35" fill="{BLAUW}"/>',
         f'<rect x="60" y="90" width="240" height="100" fill="#cfc6b3" {k}/>',
         f'<rect x="30" y="50" width="60" height="140" fill="#bdb3a0" {k}/><rect x="270" y="50" width="60" height="140" fill="#bdb3a0" {k}/>'] + \
        [f'<rect x="{x}" y="38" width="12" height="14" fill="#bdb3a0" {k}/>' for x in (30, 54, 78, 270, 294, 318)] + \
        [f'<path d="M155 190 L155 140 Q180 115 205 140 L205 190 Z" fill="#5a3b1d" {k}/>',
         f'<polygon points="150,190 210,190 230,215 130,215" fill="#8a5a2b" {k}/>',
         f'<line x1="155" y1="140" x2="135" y2="200" stroke="{DARK}" stroke-width="2"/><line x1="205" y1="140" x2="225" y2="200" stroke="{DARK}" stroke-width="2"/>',
         f'<polygon points="60,50 60,15 85,25 60,35" fill="{ROOD}"/>']
    if pijl:
        y = {"gracht": 212, "ophaalbrug": 203, "toren": 100}[pijl]; x = {"gracht": 300, "ophaalbrug": 222, "toren": 330}[pijl]
        d.append(f'<line x1="{x + 60}" y1="{y}" x2="{x + 8}" y2="{y}" stroke="{ORANJE}" stroke-width="5"/><polygon points="{x},{y} {x + 16},{y - 9} {x + 16},{y + 9}" fill="{ORANJE}"/>')
    return bewaar(naam, svg(400, 225, "".join(d)))


def p_afvalbak(naam, soort):
    kl = {"pmd": BLAUW, "gft": GROEN, "papier": "#c9a227", "glas": "#9fb3a6", "rest": GRIJS}[soort]
    if soort == "pmd":  # de blauwe zak
        return bewaar(naam, svg(160, 180, f'<path d="M45 45 Q30 110 38 165 L122 165 Q130 110 115 45 Z" fill="{BLAUW}" stroke="{DARK}" stroke-width="3"/><path d="M55 45 Q80 20 105 45 M68 30 L60 12 M92 30 L100 12" fill="none" stroke="{DARK}" stroke-width="3"/>' + T(80, 115, "PMD", 24, "#fff", w="700")))
    return bewaar(naam, svg(160, 180, f'<rect x="30" y="40" width="100" height="130" rx="8" fill="{kl}" stroke="{DARK}" stroke-width="3"/><rect x="22" y="25" width="116" height="20" rx="6" fill="{kl}" stroke="{DARK}" stroke-width="3"/>'))


def p_seizoenboom(naam, seizoen):
    d = [f'<rect x="0" y="180" width="200" height="40" fill="{"#fff" if seizoen == "winter" else "#cfe3b8"}" stroke="#ddd"/>', f'<rect x="90" y="100" width="20" height="85" fill="#8a5a2b"/>',
         f'<path d="M100 110 L60 70 M100 120 L145 75 M100 100 L100 55" stroke="#8a5a2b" stroke-width="6"/>']
    if seizoen == "zomer": d.append(f'<circle cx="100" cy="75" r="62" fill="{GROEN}"/>')
    if seizoen == "lente": d += [f'<circle cx="{x}" cy="{y}" r="7" fill="#f3b3c8"/>' for x, y in ((60, 70), (80, 50), (100, 55), (120, 45), (145, 75), (130, 60), (70, 85), (115, 80))]
    if seizoen == "herfst":
        d += [f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" fill="{ORANJE}"/>' for x, y in ((60, 70), (100, 55), (145, 75), (50, 190), (130, 195), (160, 185), (40, 200))]
    if seizoen == "winter":
        d += [f'<circle cx="{x}" cy="{y}" r="4" fill="#d9ecf7" stroke="{GRIJS}"/>' for x, y in ((30, 30), (70, 20), (150, 30), (180, 60), (20, 90), (160, 120), (40, 140))]
    return bewaar(naam, svg(200, 220, "".join(d)))


def p_tekst(naam, regels, groot=40, kleur=DARK):
    h = 30 + len(regels) * (groot + 12)
    return bewaar(naam, svg(360, h, "".join(T(180, 20 + (i + 1) * (groot + 6), r, groot, kleur, w="700") for i, r in enumerate(regels))))


# ------------------------------------------------------------------ prenten van Wikimedia Commons (met bron)
SCRATCH_COMMONS = pathlib.Path("/tmp/claude-0/-home-user/dee4549b-f215-519f-b3dc-1256f89e6465/scratchpad")
BRONNEN = {}


def pijl_svg(x, y, van="links", lengte=70):
    """Oranje pijl die met zijn punt op (x, y) wijst."""
    dx = -1 if van == "links" else 1
    x0 = x + dx * lengte
    return (f'<line x1="{x0}" y1="{y}" x2="{x + dx * 14}" y2="{y}" stroke="{ORANJE}" stroke-width="6" stroke-linecap="round"/>'
            f'<polygon points="{x},{y} {x + dx * 20},{y - 11} {x + dx * 20},{y + 11}" fill="{ORANJE}"/>')


def p_commons(naam, bronbestand, B, H, overlay, bronregel):
    """Tekent een vrije prent van Wikimedia Commons met een pijl erop, als webp."""
    import subprocess
    from PIL import Image
    png = SCRATCH_COMMONS / "lich" / f"{naam}.png"
    subprocess.run(["node", str(SCRATCH_COMMONS / "comp.js"), str(SCRATCH_COMMONS / "wmdl" / bronbestand), str(png), str(B), str(H), overlay], check=True)
    MAP.mkdir(parents=True, exist_ok=True)
    Image.open(png).convert("RGB").save(MAP / f"{naam}.webp", "WEBP", quality=82)
    bron(f"{naam}.webp", bronregel)
    return f"/examenvormen/ready/{naam}.webp"


def bron(bestand, regel):
    """Houdt BRONNEN.txt bij: elke prent die niet helemaal zelf getekend is, met haar bron."""
    f = MAP / "BRONNEN.txt"
    if f.exists():
        for lijn in f.read_text(encoding="utf-8").splitlines()[1:]:
            if ": " in lijn: k, v = lijn.split(": ", 1); BRONNEN.setdefault(k, v)
    BRONNEN[bestand] = regel
    f.write_text("Prenten Ready die niet zelf getekend zijn:\n" + "".join(f"{k}: {v}\n" for k, v in sorted(BRONNEN.items())), encoding="utf-8")


SKELET = "Human skeleton front - no labels.svg, Mikael Häggström naar LadyofHats, publiek domein, https://commons.wikimedia.org/wiki/File:Human_skeleton_front_-_no_labels.svg"
VERTERING = "Digestive system without labels.svg, LadyofHats (Mariana Ruiz Villarreal), publiek domein, https://commons.wikimedia.org/wiki/File:Digestive_system_without_labels.svg"


def p_skelet(naam, deel):
    x, y = {"schedel": (100, 40), "ribben": (88, 150), "knie": (105, 340), "bekken": (85, 205), "dijbeen": (92, 290)}[deel]
    return p_commons(naam, "Human_skeleton_front_-_no_labels.svg", 260, 500, pijl_svg(x, y, "links", 75), SKELET)


def p_vertering(naam, deel):
    x, y = {"maag": (165, 280), "slokdarm": (112, 200), "darmen": (100, 390)}[deel]
    return p_commons(naam, "dig.svg", 220, 500, pijl_svg(x, y, "rechts" if deel == "maag" else "links", 60), VERTERING)


# ------------------------------------------------------------------ zelf getekend: lichaam en eten
def p_oog(naam):
    return bewaar(naam, svg(240, 140, f'<path d="M20 70 Q120 -10 220 70 Q120 150 20 70 Z" fill="#fff" stroke="{DARK}" stroke-width="4"/>'
                                     f'<circle cx="120" cy="70" r="34" fill="{BLAUW}"/><circle cx="120" cy="70" r="15" fill="{DARK}"/><circle cx="110" cy="60" r="6" fill="#fff"/>'
                                     + "".join(f'<line x1="{60 + i * 24}" y1="{30 - abs(i - 2) * 4}" x2="{56 + i * 24}" y2="{14 - abs(i - 2) * 4}" stroke="{DARK}" stroke-width="3"/>' for i in range(5))))


def p_oor(naam):
    return bewaar(naam, svg(160, 200, f'<path d="M50 40 Q60 5 105 15 Q150 30 135 90 Q125 120 105 140 Q95 165 70 175 Q45 180 48 155" fill="#f8dcc6" stroke="{DARK}" stroke-width="4"/>'
                                     f'<path d="M75 60 Q100 40 115 70 Q115 95 95 105 Q85 115 90 130" fill="none" stroke="{DARK}" stroke-width="3"/>'))


def p_romp(naam, pijl_naar):
    """Bovenlichaam met twee longen en het hart, pijl naar long of hart."""
    d = [f'<path d="M70 20 Q70 5 110 5 Q150 5 150 20 L150 40 Q220 45 225 90 L215 260 L5 260 L-5 90 Q0 45 70 40 Z" fill="#fbeee2" stroke="{DARK}" stroke-width="3"/>',
         f'<path d="M100 75 Q55 70 50 140 Q48 200 95 200 Q105 160 105 90 Z" fill="#f3b3c8" stroke="{DARK}" stroke-width="3"/>',
         f'<path d="M120 75 Q165 70 170 140 Q172 200 125 200 Q115 160 115 90 Z" fill="#f3b3c8" stroke="{DARK}" stroke-width="3"/>',
         f'<line x1="110" y1="45" x2="110" y2="80" stroke="{DARK}" stroke-width="6"/>',
         f'<path d="M120 150 Q120 130 135 132 Q150 134 147 150 Q143 168 125 185 Q108 168 106 152 Q105 134 118 135 Z" fill="{ROOD}" stroke="{DARK}" stroke-width="3"/>']
    if pijl_naar == "hart": d.append(pijl_svg(140, 160, "rechts", 70))
    else: d.append(pijl_svg(58, 140, "links", 55))
    return bewaar(naam, svg(240, 270, "".join(d)))


def eten(soort, x):
    k = f'stroke="{DARK}" stroke-width="3"'
    v = {"appel": f'<circle cx="60" cy="80" r="40" fill="{ROOD}" {k}/><line x1="60" y1="40" x2="65" y2="20" {k}/><ellipse cx="80" cy="28" rx="14" ry="7" fill="{GROEN}"/>',
         "wortel": f'<polygon points="40,40 80,40 60,140" fill="{ORANJE}" {k}/><path d="M50 40 L40 10 M60 40 L60 5 M70 40 L82 10" stroke="{GROEN}" stroke-width="5"/>',
         "lolly": f'<line x1="60" y1="80" x2="60" y2="145" stroke="#bbb" stroke-width="6"/><circle cx="60" cy="60" r="38" fill="#f3b3c8" {k}/><path d="M60 60 m-25 0 a25 25 0 1 1 25 25" fill="none" stroke="{ROOD}" stroke-width="5"/>',
         "blikje": f'<rect x="30" y="25" width="60" height="115" rx="8" fill="{ROOD}" {k}/><rect x="30" y="65" width="60" height="30" fill="#fff"/><text x="60" y="87" font-size="16" text-anchor="middle" fill="{ROOD}" font-weight="700">FRIS</text>',
         "chips": f'<path d="M25 30 L95 30 L105 140 L15 140 Z" fill="{GEEL}" {k}/><text x="60" y="95" font-size="18" text-anchor="middle" fill="{ROOD}" font-weight="700">CHIPS</text>',
         "banaan": f'<path d="M20 50 Q30 140 110 120 Q50 115 35 45 Z" fill="{GEEL}" {k}/>'}[soort]
    return f'<g transform="translate({x},0)">{v}</g>'


def p_eten(naam, soorten, letters=True):
    d = "".join(eten(s, i * 125) for i, s in enumerate(soorten))
    if letters: d += "".join(T(60 + i * 125, 175, "ABCD"[i], 22, ORANJE, w="700") for i in range(len(soorten)))
    return bewaar(naam, svg(125 * len(soorten), 185, d))


# ------------------------------------------------------------------ meer wiskunde
def p_stippen(naam, rijen, per_rij, kleur=BLAUW):
    return bewaar(naam, svg(30 + per_rij * 34, 30 + rijen * 34, "".join(
        f'<circle cx="{32 + k * 34}" cy="{32 + r * 34}" r="12" fill="{kleur}" stroke="{DARK}" stroke-width="2"/>' for r in range(rijen) for k in range(per_rij))))


def p_borden(naam, borden, per_bord, rest=0):
    d, B = [], 130
    for b in range(borden):
        cx = 70 + b * B
        d.append(f'<ellipse cx="{cx}" cy="70" rx="58" ry="48" fill="#fff" stroke="{DARK}" stroke-width="3"/><ellipse cx="{cx}" cy="70" rx="42" ry="33" fill="none" stroke="#ccc" stroke-width="2"/>')
        for i in range(per_bord):
            d.append(f'<circle cx="{cx - 24 + (i % 3) * 24}" cy="{56 + (i // 3) * 24}" r="9" fill="{ROOD}" stroke="{DARK}" stroke-width="1.5"/>')
    for i in range(rest):
        d.append(f'<circle cx="{40 + i * 26}" cy="150" r="9" fill="{ROOD}" stroke="{DARK}" stroke-width="1.5"/>')
    if rest: d.append(T(40 + rest * 26, 156, "over", 15, a="start"))
    return bewaar(naam, svg(max(borden * B + 20, 200), 175 if rest else 135, "".join(d)))


def p_sprongen(naam, stap, aantal, tot):
    w = 360 / tot; d = [f'<line x1="20" y1="90" x2="380" y2="90" stroke="{DARK}" stroke-width="3"/>']
    for v in range(tot + 1):
        x = 20 + v * w
        d.append(f'<line x1="{x:.1f}" y1="{82 if v % stap else 76}" x2="{x:.1f}" y2="{98 if v % stap else 104}" stroke="{DARK}" stroke-width="{1.5 if v % stap else 2.5}"/>')
        if v == 0: d.append(T(f"{x:.1f}", 124, 0, 15, w="700"))
    for i in range(aantal):
        x1 = 20 + i * stap * w; x2 = 20 + (i + 1) * stap * w
        d.append(f'<path d="M{x1:.1f} 86 Q{(x1 + x2) / 2:.1f} 30 {x2:.1f} 86" fill="none" stroke="{ORANJE}" stroke-width="3"/><polygon points="{x2:.1f},88 {x2 - 9:.1f},76 {x2 + 2:.1f},74" fill="{ORANJE}"/>')
    return bewaar(naam, svg(400, 135, "".join(d)))


def p_cijfer(naam, a, b, teken, uitkomst=None):
    """Een cijferoefening onder elkaar, met lege vakjes of met een (mogelijk foute) uitkomst."""
    sa, sb = str(a), str(b); n = max(len(sa), len(sb)) + 1; z = 40; x0 = 60
    def rij(s, y, k=DARK):
        return "".join(T(x0 + (n - len(s) + i) * z + z / 2, y, c, 30, k, w="700") for i, c in enumerate(s))
    d = [rij(sa, 50), T(x0 - 20, 100, teken, 30, ORANJE, w="700"), rij(sb, 100),
         f'<line x1="{x0 - 30}" y1="118" x2="{x0 + n * z}" y2="118" stroke="{DARK}" stroke-width="3"/>']
    if uitkomst is None:
        d += [f'<rect x="{x0 + i * z + 4}" y="128" width="{z - 8}" height="{z}" rx="4" fill="#fff" stroke="{GRIJS}" stroke-width="2"/>' for i in range(n)]
    else:
        d.append(rij(str(uitkomst), 160, BLAUW))
    return bewaar(naam, svg(x0 + n * z + 30, 180, "".join(d)))


def p_liniaal(naam, cm):
    d = [f'<rect x="20" y="70" width="{20 + 15 * 30}" height="44" fill="#fff6c8" stroke="{DARK}" stroke-width="2"/>']
    for i in range(0, 151):
        x = 30 + i * 3; l = 18 if i % 10 == 0 else (11 if i % 5 == 0 else 6)
        d.append(f'<line x1="{x}" y1="70" x2="{x}" y2="{70 + l}" stroke="{DARK}" stroke-width="{1.4 if i % 10 == 0 else .7}"/>')
        if i % 10 == 0: d.append(T(x, 106, i // 10, 12))
    L = cm * 30
    d.append(f'<rect x="30" y="34" width="{L - 22}" height="22" fill="{GEEL}" stroke="{DARK}" stroke-width="2"/><polygon points="{30 + L - 22},34 {30 + L},45 {30 + L - 22},56" fill="#f8dcc6" stroke="{DARK}" stroke-width="2"/><rect x="30" y="34" width="14" height="22" fill="#f3b3c8" stroke="{DARK}" stroke-width="2"/>')
    d.append(f'<line x1="30" y1="34" x2="30" y2="70" stroke="{GRIJS}" stroke-dasharray="4 3"/><line x1="{30 + L}" y1="45" x2="{30 + L}" y2="70" stroke="{GRIJS}" stroke-dasharray="4 3"/>')
    return bewaar(naam, svg(500, 125, "".join(d)))


def p_maatbeker(naam, ml, max_ml=500, stap=100):
    y = lambda v: 220 - v / max_ml * 180
    d = [f'<rect x="61" y="{y(ml):.1f}" width="98" height="{220 - y(ml):.1f}" fill="#bfe0f5"/>',
         f'<path d="M60 30 L60 220 Q60 230 70 230 L150 230 Q160 230 160 220 L160 30" fill="none" stroke="{DARK}" stroke-width="4"/>']
    for v in range(0, max_ml + 1, stap // 2):
        d.append(f'<line x1="60" y1="{y(v):.1f}" x2="{80 if v % stap == 0 else 72}" y2="{y(v):.1f}" stroke="{DARK}" stroke-width="2"/>')
        if v % stap == 0 and v: d.append(T(84, f"{y(v) + 5:.1f}", f"{v} ml", 13, a="start"))
    return bewaar(naam, svg(220, 245, "".join(d)))


def p_twee_klokken(naam, u1, m1, u2, m2, l1="begin", l2="einde"):
    return bewaar(naam, svg(400, 215, f'<g>{klok(u1, m1, 100, 95, 80)}</g><g>{klok(u2, m2, 300, 95, 80)}</g>' + T(100, 205, l1, 16, w="700") + T(300, 205, l2, 16, w="700")))


def p_prijzen(naam, items):
    """items: lijst (soort, prijs als tekst)."""
    d = "".join(eten(s, i * 125) + T(60 + i * 125, 178, p, 18, BLAUW, w="700") for i, (s, p) in enumerate(items))
    return bewaar(naam, svg(125 * len(items), 190, d))


def p_figuren_letters(naam, soorten):
    s = f'stroke="{DARK}" stroke-width="3" fill="#f8dcc6"'
    vorm = {"cirkel": '<circle cx="50" cy="50" r="38" {s}/>', "vierkant": '<rect x="14" y="14" width="72" height="72" {s}/>',
            "driehoek": '<polygon points="10,88 90,88 50,12" {s}/>', "rechthoek": '<rect x="4" y="28" width="92" height="46" {s}/>'}
    d = "".join(f'<g transform="translate({10 + i * 110},5)">' + vorm[k].format(s=s) + "</g>" + T(60 + i * 110, 125, "ABCD"[i], 22, ORANJE, w="700") for i, k in enumerate(soorten))
    return bewaar(naam, svg(110 * len(soorten) + 10, 135, d))


def p_bord(naam, regels, breed=360, kleur="#fff6c8"):
    h = 40 + len(regels) * 34
    d = [f'<rect x="8" y="8" width="{breed - 16}" height="{h - 16}" rx="12" fill="{kleur}" stroke="{DARK}" stroke-width="4"/>']
    for i, r in enumerate(regels):
        groot = 26 if i == 0 else 20
        d.append(T(breed / 2, 46 + i * 34, r, groot, DARK, w="700" if i == 0 else "400"))
    return bewaar(naam, svg(breed, h, "".join(d)))


# ------------------------------------------------------------------ strips (verhaal in prentjes)
def paneel(soort):
    k = f'stroke="{DARK}" stroke-width="3"'
    grond = f'<rect x="0" y="110" width="140" height="40" fill="#e9d8bf"/>'
    return {
        "zaad": grond + f'<ellipse cx="70" cy="125" rx="9" ry="6" fill="#8a5a2b" {k}/>',
        "kiem": grond + f'<line x1="70" y1="110" x2="70" y2="80" stroke="{GROEN}" stroke-width="5"/><ellipse cx="58" cy="78" rx="12" ry="6" fill="{GROEN}"/><ellipse cx="82" cy="78" rx="12" ry="6" fill="{GROEN}"/>',
        "bloem": grond + f'<line x1="70" y1="110" x2="70" y2="45" stroke="{GROEN}" stroke-width="5"/><ellipse cx="55" cy="85" rx="14" ry="6" fill="{GROEN}"/>' + "".join(f'<circle cx="{70 + 13 * math.cos(math.radians(a)):.1f}" cy="{38 + 13 * math.sin(math.radians(a)):.1f}" r="10" fill="#f3b3c8"/>' for a in range(0, 360, 60)) + f'<circle cx="70" cy="38" r="8" fill="{GEEL}"/>',
        "ijs3": f'<polygon points="50,80 90,80 70,145" fill="#e9c46a" {k}/><circle cx="58" cy="70" r="16" fill="#f3b3c8" {k}/><circle cx="82" cy="70" r="16" fill="#cfe3b8" {k}/><circle cx="70" cy="50" r="16" fill="#f8dcc6" {k}/>',
        "ijs1": f'<polygon points="50,80 90,80 70,145" fill="#e9c46a" {k}/><circle cx="70" cy="72" r="17" fill="#f3b3c8" {k}/>',
        "ijs0": f'<polygon points="50,80 90,80 70,145" fill="#e9c46a" {k}/><path d="M55 80 Q70 70 85 80" fill="none" stroke="#f3b3c8" stroke-width="4"/>',
    }[soort]


def p_strip(naam, panelen):
    d = "".join(f'<g transform="translate({10 + i * 155},10)"><rect x="0" y="0" width="140" height="150" rx="10" fill="#fff" stroke="{DARK}" stroke-width="3"/>{paneel(s)}</g>'
                + T(80 + i * 155, 185, "ABCD"[i], 22, ORANJE, w="700") for i, s in enumerate(panelen))
    return bewaar(naam, svg(155 * len(panelen) + 10, 195, d))


# ------------------------------------------------------------------ kaarten (Natural Earth, publiek domein, via world-atlas)
NE = "Kaartdata: Natural Earth (publiek domein), via world-atlas 2.0.2 (Mike Bostock, ISC-licentie)"


def _landen(res):
    import json
    return json.loads((SCRATCH_COMMONS / "kaartdata" / f"landen-{res}.json").read_text())


def _ringen(geo):
    polys = geo["coordinates"] if geo["type"] == "MultiPolygon" else [geo["coordinates"]]
    for p in polys:
        for r in p:
            lons = [c[0] for c in r]
            if max(lons) > 150 and min(lons) < -150:
                r = [[c[0] + 360 if c[0] < 0 else c[0], c[1]] for c in r]
            yield r


def werelddeel(land):
    pts = [c for r in _ringen(land["geo"]) for c in r]
    lon = sum(c[0] for c in pts) / len(pts); lat = sum(c[1] for c in pts) / len(pts)
    n = land["naam"]
    if n in ("Russia",): return "rusland"
    if n in ("Turkey", "Kazakhstan", "Cyprus", "N. Cyprus", "Georgia", "Azerbaijan", "Armenia"): return "azie"
    if n == "Greenland": return "noord-amerika"
    if lat < -60: return "antarctica"
    if lon < -30: return "noord-amerika" if (lat >= 12 or (lon < -77 and lat >= 7)) else "zuid-amerika"
    if lat >= 35 and lon <= 40: return "europa"
    if lat < 37.5 and -20 <= lon <= 52 and not (lon >= 34 and lat >= 12): return "afrika"
    if (lon >= 130 and lat < 0) or (lon > 110 and lat < -10): return "oceanie"
    return "azie"


def p_wereld(naam, oranje=(), pijl=None):
    """Wereldkaart; de werelddelen in 'oranje' kleuren oranje, de rest lichtgroen. pijl = (lon, lat, van)."""
    X = lambda lon: (lon + 170) * 2; Y = lambda lat: (84 - lat) * 2
    d = [f'<rect width="720" height="290" fill="#d9ecf7"/>']
    for l in _landen("110m"):
        w = werelddeel(l)
        kl = ORANJE if w in oranje else ("#eeeeee" if w in ("antarctica",) else "#cfe3b8")
        for r in _ringen(l["geo"]):
            d.append('<path d="M' + " L".join(f"{X(c[0]):.1f},{Y(c[1]):.1f}" for c in r) + f'Z" fill="{kl}" stroke="#7a8f6a" stroke-width=".4"/>')
    if pijl: d.append(pijl_svg(X(pijl[0]), Y(pijl[1]), pijl[2], 60))
    bron(f"{naam}.svg", NE)
    return bewaar(naam, svg(720, 290, "".join(d)))


def p_benelux(naam, pijl=None, groen="Belgium", hoofdstad=False):
    lo0, lo1, la0, la1 = 1.0, 9.6, 48.6, 54.0
    S = 70; X = lambda lon: (lon - lo0) * S * 0.64; Y = lambda lat: (la1 - lat) * S
    B, H = X(lo1), Y(la0)
    d = [f'<rect width="{B:.0f}" height="{H:.0f}" fill="#d9ecf7"/>']
    for l in _landen("50m"):
        rs = list(_ringen(l["geo"]))
        if not any(lo0 - 3 < c[0] < lo1 + 3 and la0 - 3 < c[1] < la1 + 3 for r in rs for c in r): continue
        kl = GROEN if l["naam"] == groen else {"Netherlands": "#fde3cf", "Germany": "#e6dcf2", "France": "#fbf0c4", "Luxembourg": "#f7c9d6"}.get(l["naam"], "#eeeeee")
        for r in rs:
            d.append('<path d="M' + " L".join(f"{X(c[0]):.1f},{Y(c[1]):.1f}" for c in r) + f'Z" fill="{kl}" stroke="{DARK}" stroke-width="2"/>')
    if hoofdstad: d.append(f'<circle cx="{X(4.35):.1f}" cy="{Y(50.85):.1f}" r="7" fill="{ROOD}" stroke="#fff" stroke-width="2"/>')
    if pijl: d.append(pijl_svg(X(pijl[0]), Y(pijl[1]), pijl[2], 70))
    bron(f"{naam}.svg", NE)
    return bewaar(naam, svg(int(B), int(H), "".join(d)))


# ------------------------------------------------------------------ wereldoriëntatie: dingen en landschappen
K3 = f'stroke="{DARK}" stroke-width="3"'


def ding(soort):
    k = K3
    return {
        "ijsblokjes": f'<rect x="30" y="60" width="50" height="50" rx="6" fill="#d9f0fb" {k}/><rect x="85" y="75" width="45" height="45" rx="6" fill="#d9f0fb" {k}/><rect x="55" y="20" width="45" height="45" rx="6" fill="#d9f0fb" {k}/><path d="M40 70 L50 70 M95 85 L105 85" stroke="#fff" stroke-width="4"/>',
        "glas": f'<path d="M40 20 L50 140 L110 140 L120 20 Z" fill="#fff" {k}/><path d="M44 60 L50 138 L110 138 L116 60 Z" fill="#bfe0f5"/>',
        "pot": f'<rect x="30" y="80" width="100" height="60" rx="6" fill="{GRIJS}" {k}/><rect x="20" y="72" width="120" height="12" rx="4" fill="#aaa" {k}/>' + "".join(f'<path d="M{50 + i * 28} 64 Q{40 + i * 28} 48 {50 + i * 28} 34 Q{60 + i * 28} 20 {50 + i * 28} 6" fill="none" stroke="#9ab" stroke-width="4"/>' for i in range(3)),
        "magneet": f'<path d="M30 20 L30 90 Q30 140 80 140 Q130 140 130 90 L130 20 L100 20 L100 90 Q100 110 80 110 Q60 110 60 90 L60 20 Z" fill="{ROOD}" {k}/><rect x="30" y="20" width="30" height="22" fill="#ccc" {k}/><rect x="100" y="20" width="30" height="22" fill="#ccc" {k}/>',
        "stopcontact": f'<rect x="20" y="20" width="120" height="120" rx="16" fill="#fff" {k}/><circle cx="80" cy="80" r="42" fill="#f4f4f4" {k}/><circle cx="62" cy="80" r="7" fill="{DARK}"/><circle cx="98" cy="80" r="7" fill="{DARK}"/>',
        "kaars": f'<rect x="60" y="60" width="40" height="85" fill="#fff6c8" {k}/><line x1="80" y1="60" x2="80" y2="48" {k}/><path d="M80 15 Q95 35 80 48 Q65 35 80 15" fill="{GEEL}" stroke="{ORANJE}" stroke-width="2"/>',
        "lamp": f'<path d="M55 95 Q30 70 40 45 Q55 15 80 15 Q105 15 120 45 Q130 70 105 95 Z" fill="#fff6a8" {k}/><rect x="60" y="95" width="40" height="30" fill="#aaa" {k}/><path d="M62 105 L98 105 M62 115 L98 115" stroke="{DARK}" stroke-width="2"/>',
        "oude-telefoon": f'<rect x="25" y="70" width="110" height="70" rx="12" fill="#222" {k}/><circle cx="80" cy="105" r="24" fill="#eee" {k}/>' + "".join(f'<circle cx="{80 + 15 * math.cos(math.radians(a)):.1f}" cy="{105 + 15 * math.sin(math.radians(a)):.1f}" r="3" fill="#222"/>' for a in range(0, 360, 36)) + f'<path d="M20 60 Q20 35 40 35 L120 35 Q140 35 140 60 L120 60 L115 48 L45 48 L40 60 Z" fill="#222" {k}/>',
        "gsm": f'<rect x="50" y="10" width="60" height="130" rx="12" fill="#333" {k}/><rect x="56" y="22" width="48" height="100" rx="4" fill="#9ed0f0"/><circle cx="80" cy="131" r="4" fill="#ccc"/>',
        "vuistbijl": f'<path d="M80 10 Q125 60 115 110 Q100 145 80 145 Q60 145 45 110 Q35 60 80 10 Z" fill="#b9a88f" {k}/><path d="M80 30 L70 60 L85 80 L72 110 M95 55 L100 90" stroke="#7d6b55" stroke-width="2" fill="none"/>',
        "schild": f'<path d="M30 20 L130 20 L130 70 Q130 125 80 145 Q30 125 30 70 Z" fill="{BLAUW}" {k}/><path d="M80 20 L80 145 M30 70 L130 70" stroke="{GEEL}" stroke-width="10"/>',
        "kerstboom": f'<polygon points="80,10 30,70 55,70 20,120 140,120 105,70 130,70" fill="{GROEN}" {k}/><rect x="70" y="120" width="20" height="25" fill="#8a5a2b" {k}/><circle cx="65" cy="60" r="6" fill="{ROOD}"/><circle cx="95" cy="90" r="6" fill="{GEEL}"/><circle cx="60" cy="105" r="6" fill="{BLAUW}"/><polygon points="80,0 85,12 78,12" fill="{GEEL}"/>',
        "paaseieren": f'<ellipse cx="50" cy="95" rx="30" ry="40" fill="#f3b3c8" {k}/><path d="M22 90 Q50 75 78 90" stroke="{GEEL}" stroke-width="6" fill="none"/><ellipse cx="110" cy="100" rx="28" ry="37" fill="#cfe3b8" {k}/><circle cx="100" cy="95" r="5" fill="{ORANJE}"/><circle cx="118" cy="108" r="5" fill="{ORANJE}"/><circle cx="112" cy="82" r="5" fill="{ORANJE}"/>',
        "gemeentehuis": f'<rect x="20" y="60" width="120" height="85" fill="#f3ecd9" {k}/><polygon points="10,62 80,20 150,62" fill="#c9965a" {k}/><rect x="68" y="105" width="24" height="40" fill="#8a5a2b" {k}/>' + "".join(f'<rect x="{32 + i * 26}" y="75" width="16" height="22" fill="#d9ecf7" {k}/>' for i in range(4)) + f'<line x1="80" y1="20" x2="80" y2="0" {k}/><rect x="80" y="0" width="22" height="12" fill="{DARK}"/><rect x="80" y="0" width="22" height="4" fill="{DARK}"/>',
        "kruiwagen": f'<path d="M20 50 L120 50 L105 95 L35 95 Z" fill="{GROEN}" {k}/><circle cx="130" cy="110" r="20" fill="#555" {k}/><circle cx="130" cy="110" r="5" fill="#ccc"/><line x1="105" y1="95" x2="130" y2="110" {k}/><line x1="20" y1="50" x2="0" y2="40" stroke="#8a5a2b" stroke-width="6"/><line x1="40" y1="95" x2="40" y2="130" {k}/>',
    }[soort]


def p_ding(naam, soort):
    return bewaar(naam, svg(160, 155, ding(soort)))


def p_dingen(naam, soorten, letters=True):
    d = "".join(f'<g transform="translate({i * 165},0)">{ding(s)}</g>' + (T(80 + i * 165, 180, "ABCD"[i], 22, ORANJE, w="700") if letters else "") for i, s in enumerate(soorten))
    return bewaar(naam, svg(165 * len(soorten), 190 if letters else 155, d))


def p_waterbak(naam, items):
    """items: lijst (letter, soort, drijft). soort: kurk, steen, eend, sleutel."""
    d = [f'<rect x="10" y="60" width="380" height="140" fill="#bfe0f5"/><path d="M10 20 L10 200 L390 200 L390 20" fill="none" stroke="{DARK}" stroke-width="4"/>']
    for i, (letter, soort, drijft) in enumerate(items):
        x = 70 + i * 120; y = 52 if drijft else 178
        vorm = {"kurk": f'<rect x="{x - 15}" y="{y - 12}" width="30" height="24" rx="5" fill="#c9965a" {K3}/>',
                "steen": f'<ellipse cx="{x}" cy="{y}" rx="24" ry="16" fill="#999" {K3}/>',
                "eend": f'<ellipse cx="{x}" cy="{y}" rx="24" ry="13" fill="{GEEL}" {K3}/><circle cx="{x + 16}" cy="{y - 16}" r="10" fill="{GEEL}" {K3}/><polygon points="{x + 25},{y - 17} {x + 36},{y - 14} {x + 25},{y - 11}" fill="{ORANJE}"/>',
                "sleutel": f'<circle cx="{x - 14}" cy="{y}" r="10" fill="none" stroke="#b08a2e" stroke-width="5"/><line x1="{x - 4}" y1="{y}" x2="{x + 24}" y2="{y}" stroke="#b08a2e" stroke-width="5"/><line x1="{x + 18}" y1="{y}" x2="{x + 18}" y2="{y + 9}" stroke="#b08a2e" stroke-width="4"/>'}[soort]
        d.append(vorm + T(x, 230, letter, 22, ORANJE, w="700"))
    return bewaar(naam, svg(400, 240, "".join(d)))


def p_wip(naam):
    return bewaar(naam, svg(320, 170, f'<polygon points="160,150 130,150 145,110 175,110 190,150" fill="#8a5a2b" {K3}/><line x1="20" y1="130" x2="300" y2="90" stroke="{ORANJE}" stroke-width="10" stroke-linecap="round"/>'
                                        f'<polygon points="160,110 140,150 180,150" fill="{GRIJS}" {K3}/><rect x="25" y="88" width="40" height="38" fill="#c9965a" {K3}/><circle cx="275" cy="60" r="14" fill="#f8dcc6" {K3}/><line x1="275" y1="74" x2="275" y2="92" {K3}/>'))


def p_katrol(naam):
    return bewaar(naam, svg(220, 240, f'<line x1="20" y1="15" x2="200" y2="15" stroke="#8a5a2b" stroke-width="10"/><line x1="110" y1="15" x2="110" y2="40" {K3}/>'
                                        f'<circle cx="110" cy="65" r="28" fill="#ccc" {K3}/><circle cx="110" cy="65" r="6" fill="{DARK}"/><line x1="82" y1="65" x2="82" y2="180" stroke="#8a5a2b" stroke-width="4"/><line x1="138" y1="65" x2="138" y2="200" stroke="#8a5a2b" stroke-width="4"/>'
                                        f'<rect x="57" y="180" width="50" height="45" fill="#c9965a" {K3}/><path d="M130 200 L146 200 L146 225 L130 225 Z" fill="#f8dcc6" {K3}/>'))


def p_weer(naam, soort):
    wolk = f'<path d="M40 90 Q20 90 22 70 Q25 50 48 55 Q55 30 85 35 Q110 25 120 55 Q145 55 142 75 Q140 92 120 92 Z" fill="#dfe6ea" {K3}/>'
    extra = {"regen": "".join(f'<line x1="{45 + i * 22}" y1="{105 + (i % 2) * 8}" x2="{38 + i * 22}" y2="{125 + (i % 2) * 8}" stroke="{BLAUW}" stroke-width="4" stroke-linecap="round"/>' for i in range(4)),
             "sneeuw": "".join(T(45 + i * 24, 125 + (i % 2) * 10, "*", 30, BLAUW, w="700") for i in range(4)),
             "onweer": f'<polygon points="80,92 65,125 80,125 70,150 100,112 84,112 92,92" fill="{GEEL}" {K3}/>'}[soort]
    return bewaar(naam, svg(160, 155, wolk + extra))


def p_landschap(naam, soort):
    if soort == "woestijn":
        d = f'<rect width="300" height="200" fill="#fbe3a8"/><circle cx="240" cy="45" r="25" fill="{GEEL}"/><path d="M0 140 Q70 100 150 140 T300 130 L300 200 L0 200 Z" fill="#e9c46a"/><rect x="70" y="80" width="14" height="70" rx="7" fill="{GROEN}"/><path d="M70 110 L55 110 L55 90 M84 100 L98 100 L98 85" stroke="{GROEN}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    elif soort == "pool":
        d = f'<rect width="300" height="200" fill="#dbe9f4"/><path d="M0 130 L60 90 L110 125 L170 80 L230 120 L300 100 L300 200 L0 200 Z" fill="#fff" stroke="#9ab" stroke-width="2"/><ellipse cx="150" cy="160" rx="34" ry="20" fill="#fff" {K3}/><circle cx="185" cy="140" r="14" fill="#fff" {K3}/><circle cx="190" cy="137" r="2.5" fill="{DARK}"/>'
    elif soort == "regenwoud":
        d = f'<rect width="300" height="200" fill="#d9ecf7"/>' + "".join(f'<rect x="{x}" y="90" width="12" height="110" fill="#6b4a2b"/><circle cx="{x + 6}" cy="{70 + (x % 3) * 10}" r="{45 - (x % 2) * 8}" fill="{["#3e7a32", "#4f8f3c", "#2f6a2a"][x % 3]}"/>' for x in (20, 80, 140, 200, 260)) + "".join(f'<line x1="{40 + i * 50}" y1="{10 + (i % 2) * 15}" x2="{34 + i * 50}" y2="{30 + (i % 2) * 15}" stroke="{BLAUW}" stroke-width="3"/>' for i in range(6))
    elif soort == "kust":
        d = f'<rect width="300" height="200" fill="#d9ecf7"/><rect y="90" width="300" height="60" fill="{BLAUW}"/><path d="M0 90 Q20 82 40 90 T80 90 T120 90 T160 90 T200 90 T240 90 T280 90 T320 90" fill="none" stroke="#fff" stroke-width="3"/><rect y="140" width="300" height="60" fill="#f5e0a8"/><path d="M220 140 L250 140 L235 110 Z" fill="{ROOD}"/><line x1="235" y1="110" x2="235" y2="175" stroke="{DARK}" stroke-width="3"/>'
    else:  # ardennen
        d = f'<rect width="300" height="200" fill="#d9ecf7"/><path d="M0 120 Q60 40 130 110 Q190 50 300 115 L300 200 L0 200 Z" fill="#7aa35a"/>' + "".join(f'<polygon points="{x},{y} {x - 12},{y + 30} {x + 12},{y + 30}" fill="#2f6a2a"/>' for x, y in ((40, 95), (60, 85), (150, 100), (175, 90), (230, 95), (260, 100), (100, 130), (200, 135))) + f'<path d="M0 185 Q100 160 150 180 T300 170" fill="none" stroke="{BLAUW}" stroke-width="8"/>'
    return bewaar(naam, svg(300, 200, d))


def p_verkeersbord(naam, soort):
    if soort == "geen-fietsers":
        d = f'<circle cx="80" cy="80" r="70" fill="#fff" stroke="{ROOD}" stroke-width="14"/><circle cx="55" cy="95" r="16" fill="none" stroke="{DARK}" stroke-width="4"/><circle cx="105" cy="95" r="16" fill="none" stroke="{DARK}" stroke-width="4"/><path d="M55 95 L72 70 L95 70 L105 95 M72 70 L82 95 L55 95 M90 62 L100 62" fill="none" stroke="{DARK}" stroke-width="4"/>'
    elif soort == "stop":
        d = "<polygon points=\"" + " ".join(f"{80 + 72 * math.cos(math.radians(22.5 + 45 * i)):.1f},{80 + 72 * math.sin(math.radians(22.5 + 45 * i)):.1f}" for i in range(8)) + f'" fill="{ROOD}" stroke="#fff" stroke-width="5"/>' + T(80, 93, "STOP", 34, "#fff", w="700")
    else:  # zebrapad
        d = f'<rect width="160" height="160" fill="#777"/>' + "".join(f'<rect x="{12 + i * 30}" y="20" width="18" height="120" fill="#fff"/>' for i in range(5))
    return bewaar(naam, svg(160, 160, d))


def p_stamboom(naam, vraag_bij="oma"):
    vak = lambda x, y, t: f'<rect x="{x}" y="{y}" width="110" height="44" rx="10" fill="{"#fde3cf" if t == "?" else "#fff"}" {K3}/>' + T(x + 55, y + 29, t, 18, ORANJE if t == "?" else DARK, w="700")
    d = [f'<path d="M115 66 L115 90 L175 90 M235 66 L235 90 L175 90 L175 116 M175 160 L175 184" stroke="{DARK}" stroke-width="3" fill="none"/>',
         vak(60, 22, "opa"), vak(180, 22, "?" if vraag_bij == "oma" else "oma"), vak(120, 116, "mama"), vak(120, 184, "ik")]
    return bewaar(naam, svg(350, 240, "".join(d)))


def p_grot(naam):
    d = f'<rect width="300" height="190" fill="#c9a77a"/><path d="M0 0 L300 0 L300 25 Q150 55 0 25 Z" fill="#8f6f48"/>'
    dier = lambda x, y, s: f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="50" cy="40" rx="45" ry="24" fill="#5a2f1a"/><circle cx="100" cy="30" r="14" fill="#5a2f1a"/><path d="M95 18 L88 4 M105 18 L112 4" stroke="#5a2f1a" stroke-width="4"/><path d="M20 58 L15 90 M40 60 L40 92 M65 60 L68 92 M85 55 L92 88" stroke="#5a2f1a" stroke-width="7"/></g>'
    hand = f'<g transform="translate(230,120)"><path d="M0 40 L0 10 M10 40 L10 0 M20 40 L20 2 M30 40 L30 8 M40 45 L50 25" stroke="#b5422e" stroke-width="7" stroke-linecap="round"/><ellipse cx="18" cy="48" rx="22" ry="16" fill="#b5422e"/></g>'
    return bewaar(naam, svg(300, 190, d + dier(30, 60, 1.1) + dier(150, 100, .6) + hand))
