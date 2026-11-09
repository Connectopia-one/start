"""Tekent de prenten voor de pittige vragen bedrijfswetenschappen en recht 🌍 Beyond.

    python3 inhoud/pittig/bron/maak_prenten_bedrijfswetenschappen_beyond.py

Schrijft naar public/examenvormen/bedrijfswetenschappen-beyond/. Alles is eigen
tekenwerk (documenten, schema's en grafieken met verzonnen cijfers), dus Kim
hoeft niets te zoeken. De klikvakken staan in
beyond_bedrijfswetenschappen_themas/prentmaat.py, zodat vraag en prent nooit
uit elkaar lopen.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from beyond_bedrijfswetenschappen_themas import prentmaat as pm  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "bedrijfswetenschappen-beyond"
GROEN, DONKER, ACHTER, LIJN, ZACHT = "#2f4a22", "#24331b", "#fffdf7", "#b9b29c", "#eef3e6"
FONT = 'font-family="Arial, sans-serif"'


def svg(B, H, inhoud):
    return "\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" {FONT}>',
                      f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>', *inhoud, "</svg>"]) + "\n"


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tekst(x, y, t, grootte=22, anker="start", vet=False, kleur=DONKER):
    w = ' font-weight="bold"' if vet else ""
    return f'<text x="{x}" y="{y}" font-size="{grootte}" text-anchor="{anker}" fill="{kleur}"{w}>{esc(t)}</text>'


def kaart(bestand, titel, rijen):
    """rijen: (label, bedrag, vet) — een document met regels onder elkaar."""
    n = len(rijen)
    B, H = pm.KAART_B, pm.kaart_hoogte(n)
    d = [f'<rect x="10" y="10" width="{B-20}" height="{H-20}" rx="16" fill="#fff" stroke="{LIJN}" stroke-width="2"/>',
         tekst(B / 2, 58, titel, 28, "middle", True)]
    for i, (label, bedrag, vet) in enumerate(rijen):
        y = pm.KAART_TOP + i * pm.KAART_RIJ
        if i % 2 == 0:
            d.append(f'<rect x="24" y="{y}" width="{B-48}" height="{pm.KAART_RIJ}" fill="{ZACHT}"/>')
        d.append(tekst(40, y + 32, label, 22, vet=vet))
        d.append(tekst(B - 40, y + 32, bedrag, 22, "end", vet=vet))
    (UIT / bestand).write_text(svg(B, H, d), encoding="utf-8")


def regels(t, breed):
    """Knipt een tekst in regels van ongeveer breed tekens."""
    woorden, uit, nu = [w for w in str(t).split(" ") if w], [], ""
    for w in woorden:
        if len(nu) + len(w) + 1 > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = (nu + " " + w).strip()
    if nu:
        uit.append(nu)
    return uit


def raster(bestand, titel, kolomkoppen, rijkoppen, cellen, grootte=21):
    """cellen[r][k]: tekst. rijkoppen mag None zijn."""
    n_r, n_k = len(cellen), len(cellen[0])
    links, B, H = pm.raster_maat(n_r, bool(rijkoppen))
    w = (B - 20 - links) / n_k
    d = [tekst(B / 2, 44, titel, 26, "middle", True)]
    for k, kop in enumerate(kolomkoppen):
        x = links + k * w
        d.append(f'<rect x="{x+4:.1f}" y="{pm.RASTER_TOP}" width="{w-8:.1f}" height="{pm.RASTER_KOP-8}" rx="10" fill="{GROEN}"/>')
        d.append(tekst(x + w / 2, pm.RASTER_TOP + 34, kop, 21, "middle", True, "#fff"))
    for r in range(n_r):
        y = pm.RASTER_TOP + pm.RASTER_KOP + r * pm.RASTER_CEL
        if rijkoppen:
            d.append(f'<rect x="20" y="{y+4}" width="{links-28}" height="{pm.RASTER_CEL-8}" rx="10" fill="{ZACHT}"/>')
            rr = regels(rijkoppen[r], 22)
            for i, t in enumerate(rr):
                d.append(tekst(34, y + pm.RASTER_CEL / 2 - (len(rr) - 1) * 13 + i * 26 + 7, t, 19, vet=True))
        for k in range(n_k):
            x = links + k * w
            d.append(f'<rect x="{x+4:.1f}" y="{y+4}" width="{w-8:.1f}" height="{pm.RASTER_CEL-8}" rx="10" fill="#fff" stroke="{LIJN}" stroke-width="2"/>')
            rr = regels(cellen[r][k], int(w / (grootte * 0.52)))
            for i, t in enumerate(rr):
                d.append(tekst(x + w / 2, y + pm.RASTER_CEL / 2 - (len(rr) - 1) * 13 + i * 26 + 7, t, grootte, "middle"))
    (UIT / bestand).write_text(svg(B, H, d), encoding="utf-8")


TEKENINGEN = []


def tekening(f):
    TEKENINGEN.append(f)
    return f


@tekening
def aanslagbiljet():
    from beyond_bedrijfswetenschappen_themas.personenbelasting import BILJET
    kaart("aanslagbiljet.svg", "Aanslagbiljet personenbelasting (vereenvoudigd)", BILJET)


@tekening
def voorafbetalingen():
    B, H = pm.JAAR_B, pm.JAAR_H
    d = [tekst(B / 2, 40, "Boekjaar 2026 (= kalenderjaar): de vier voorafbetalingen", 24, "middle", True),
         f'<line x1="{pm.JAAR_X0}" y1="130" x2="{pm.JAAR_X1}" y2="130" stroke="{GROEN}" stroke-width="5"/>']
    maanden = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
    begin = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    for m, b in zip(maanden, begin):
        x = pm.x_dag(b)
        d.append(f'<line x1="{x:.1f}" y1="120" x2="{x:.1f}" y2="140" stroke="{GROEN}" stroke-width="2"/>')
        d.append(tekst(x + 36, 165, m, 17, "middle", kleur="#5b6b4f"))
    for naam, datum, dag in pm.VA_DAGEN:
        x = pm.x_dag(dag)
        d.append(f'<circle cx="{x:.1f}" cy="130" r="11" fill="#b5651d"/>')
        d.append(tekst(x, 92, naam, 22, "middle", True))
        d.append(tekst(x, 210, datum, 19, "middle"))
    (UIT / "voorafbetalingen.svg").write_text(svg(B, H, d), encoding="utf-8")


@tekening
def aankoopfactuur():
    from beyond_bedrijfswetenschappen_themas.aankopen import FACTUUR
    kaart("aankoopfactuur.svg", "Factuur van Groothandel Noord aan Winkel Zuid", FACTUUR)


@tekening
def kasblad():
    from beyond_bedrijfswetenschappen_themas.verkopen import KASBLAD
    kaart("kasblad.svg", "Kasblad Kledingwinkel Mie, dinsdag 14 maart", KASBLAD)


@tekening
def loonsynthese():
    from beyond_bedrijfswetenschappen_themas.lonen import SYNTHESE
    kaart("loonsynthese.svg", "Loonsynthese maart, Schrijnwerkerij Hout bv", SYNTHESE)


@tekening
def overlopende():
    raster("overlopende-rekeningen.svg", "Kosten en opbrengsten op het einde van het boekjaar",
           ["Kost", "Opbrengst"],
           ["Al betaald of ontvangen, hoort bij volgend jaar", "Hoort bij dit jaar, nog te betalen of te ontvangen"],
           [["Over te dragen kosten", "Over te dragen opbrengsten"],
            ["Toe te rekenen kosten", "Verkregen opbrengsten"]])


@tekening
def balans():
    B, H = pm.BALANS_B, pm.BALANS_H
    d = [tekst(B / 2, 40, "Balans voor financiële analyse, Velo nv, 31 december 2026 (in euro)", 23, "middle", True),
         tekst(255, 100, "ACTIVA", 22, "middle", True), tekst(745, 100, "PASSIVA", 22, "middle", True)]
    for naam, (x, y, w, h, label, bedrag) in pm.BALANS_VAKKEN.items():
        kleur = "#fff" if naam in ("voorraad", "vorderingen", "liquide") else ZACHT
        d.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{kleur}" stroke="{GROEN}" stroke-width="2"/>')
        d.append(tekst(x + 16, y + h / 2 + 8, label, 20, vet=naam not in ("voorraad", "vorderingen", "liquide")))
        d.append(tekst(x + w - 16, y + h / 2 + 8, bedrag, 20, "end"))
    d.append(tekst(30, 548, "Courante activa: 400 000", 19, kleur="#5b6b4f"))
    d.append(tekst(255, 548, "", 19))
    d.append(tekst(970, 548, "Balanstotaal: 1 000 000", 19, "end", kleur="#5b6b4f"))
    (UIT / "balans-velo.svg").write_text(svg(B, H, d), encoding="utf-8")


@tekening
def cyclus():
    B, H = pm.CYCLUS_B, pm.CYCLUS_H
    x0, s = pm.CYCLUS_X0, pm.CYCLUS_DAG
    d = [tekst(B / 2, 40, "De bedrijfscyclus van een groothandel, in dagen", 24, "middle", True),
         f'<line x1="{x0}" y1="90" x2="{x0 + 85 * s}" y2="90" stroke="{GROEN}" stroke-width="3"/>']
    for dag in range(0, 81, 10):
        x = x0 + dag * s
        d.append(f'<line x1="{x}" y1="82" x2="{x}" y2="98" stroke="{GROEN}" stroke-width="2"/>')
        d.append(tekst(x, 75, str(dag), 17, "middle"))
    for dag, wat in ((0, "aankoop goederen"), (50, "verkoop"), (80, "klant betaalt")):
        x = x0 + dag * s
        d.append(f'<line x1="{x}" y1="98" x2="{x}" y2="{H-20}" stroke="{LIJN}" stroke-width="2" stroke-dasharray="6 5"/>')
    d.append(tekst(x0 + 40 * s, H - 8, "leverancier wordt betaald op dag 40", 16, "middle", kleur="#5b6b4f"))
    kleuren = {"voorraad": "#c9d9b8", "klant": "#e8cfa6", "leverancier": "#d7d1e8", "ntfp": "#f2b8a0"}
    for naam, (van, tot, y, label) in pm.CYCLUS_BALKEN.items():
        x = x0 + van * s
        d.append(f'<rect x="{x}" y="{y}" width="{(tot-van)*s}" height="36" rx="8" fill="{kleuren[naam]}" stroke="{GROEN}" stroke-width="1.5"/>')
        d.append(tekst(x + (tot - van) * s / 2, y + 25, label, 18, "middle", True))
    (UIT / "bedrijfscyclus.svg").write_text(svg(B, H, d), encoding="utf-8")


@tekening
def hefboom():
    from beyond_bedrijfswetenschappen_themas.solvabiliteit import HEFBOOM_KOPPEN, HEFBOOM_RIJEN, HEFBOOM
    raster("hefboom.svg", "Drie manieren om 1 000 000 euro te financieren (zonder belasting)",
           HEFBOOM_KOPPEN, HEFBOOM_RIJEN, HEFBOOM, grootte=22)


@tekening
def financieringsvormen():
    raster("financieringsvormen.svg", "Financieringsvormen: wie geeft het geld en voor hoe lang?",
           ["Korte termijn (tot een jaar)", "Lange termijn (meer dan een jaar)"],
           ["Eigen vermogen", "Vreemd vermogen"],
           [["Bestaat niet: eigen vermogen blijft in de onderneming", "?"],
            ["?", "?"]], grootte=20)


@tekening
def cashflowtabel():
    from beyond_bedrijfswetenschappen_themas.investeringen import CF_KOPPEN, CF_RIJEN, CF
    raster("cashflowtabel.svg", "Cashflowtabel: nieuwe machine van Plaat bv (in euro)", CF_KOPPEN, CF_RIJEN, CF, grootte=20)


@tekening
def swot():
    raster("swot.svg", "SWOT-analyse", ["Helpt de onderneming", "Hindert de onderneming"],
           ["Intern: in de onderneming", "Extern: in de omgeving"],
           [["S: sterktes", "W: zwaktes"], ["O: kansen", "T: bedreigingen"]], grootte=24)


@tekening
def bmc():
    B, H = pm.BMC_B, pm.BMC_H
    d = [tekst(B / 2, 44, "Business Model Canvas", 26, "middle", True)]
    for naam, (x, y, w, h, label) in pm.BMC_VAKKEN.items():
        d.append(f'<rect x="{x+3:.1f}" y="{y+3}" width="{w-6:.1f}" height="{h-6}" rx="10" fill="#fff" stroke="{GROEN}" stroke-width="2"/>')
        d.append(tekst(x + 14, y + 32, label, 19, vet=True))
    (UIT / "bmc.svg").write_text(svg(B, H, d), encoding="utf-8")


@tekening
def bcg():
    raster("bcg.svg", "BCG-matrix", ["Groot marktaandeel", "Klein marktaandeel"],
           ["Hoge marktgroei", "Lage marktgroei"], [["?", "?"], ["?", "?"]], grootte=30)


@tekening
def plc():
    import math
    B, H = pm.PLC_B, pm.PLC_H
    x0, x1, top, onder = pm.PLC_X0, pm.PLC_X1, pm.PLC_TOP, pm.PLC_ONDER
    w = (x1 - x0) / 5
    d = [tekst(B / 2, 36, "De productlevenscyclus: omzet in de tijd", 24, "middle", True),
         f'<line x1="{x0}" y1="{onder}" x2="{x1+10}" y2="{onder}" stroke="{DONKER}" stroke-width="3"/>',
         f'<line x1="{x0}" y1="{onder}" x2="{x0}" y2="{top-30}" stroke="{DONKER}" stroke-width="3"/>',
         tekst(x1, onder + 40, "tijd", 19, "end"), tekst(x0 - 12, top - 10, "omzet", 19, "end")]
    for i in range(5):
        x = x0 + i * w
        if i:
            d.append(f'<line x1="{x:.1f}" y1="{top-30}" x2="{x:.1f}" y2="{onder}" stroke="{LIJN}" stroke-width="2" stroke-dasharray="7 6"/>')
        d.append(tekst(x + w / 2, top - 8, f"Fase {i+1}", 20, "middle", True))
    # omzetcurve: 0 in fase 1, traag in 2, snel in 3, vlak in 4, dalend in 5
    pts = []
    for k in range(0, 501):
        t = k / 500 * 5
        def stijg(u):
            return 0.95 / (1 + math.exp(-3.4 * (u - 2.5)))
        y = max(0.0, stijg(t) - stijg(1.0)) if t >= 1 else 0.0
        if t > 3.7:
            y *= math.exp(-0.75 * (t - 3.7) ** 2)
        pts.append(f"{x0 + t * w:.1f},{onder - y * (onder - top):.1f}")
    d.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GROEN}" stroke-width="5"/>')
    (UIT / "productlevenscyclus.svg").write_text(svg(B, H, d), encoding="utf-8")


@tekening
def opzegtermijnen():
    B, H = pm.OPZEG_B, pm.OPZEG_H
    d = [tekst(B / 2, 42, "Opzegtermijnen voor wie na 1 januari 2014 begon (wettelijke tabel, deel)", 23, "middle", True)]
    koppen = ["Anciënniteit", "De werkgever zegt op", "De werknemer zegt op"]
    for (x0, x1), kop in zip(pm.OPZEG_KOL, koppen):
        d.append(f'<rect x="{x0+3}" y="{pm.OPZEG_TOP-62}" width="{x1-x0-6}" height="54" rx="10" fill="{GROEN}"/>')
        d.append(tekst((x0 + x1) / 2, pm.OPZEG_TOP - 27, kop, 21, "middle", True, "#fff"))
    for r, rij in enumerate(pm.OPZEG):
        y = pm.OPZEG_TOP + r * pm.OPZEG_RIJ
        if r % 2 == 0:
            d.append(f'<rect x="20" y="{y}" width="960" height="{pm.OPZEG_RIJ}" fill="{ZACHT}"/>')
        for (x0, x1), t in zip(pm.OPZEG_KOL, rij):
            d.append(tekst((x0 + x1) / 2, y + 27, t, 20, "middle"))
    d.append(tekst(B / 2, H - 22, "Bron: FOD Werkgelegenheid, Arbeid en Sociaal Overleg (wet eenheidsstatuut).", 16, "middle", kleur="#5b6b4f"))
    (UIT / "opzegtermijnen.svg").write_text(svg(B, H, d), encoding="utf-8")


def assen(d, xlabel, ylabel, titel):
    x0, x1, top, onder = pm.GRAF_X0, pm.GRAF_X1, pm.GRAF_TOP, pm.GRAF_ONDER
    d += [tekst(pm.GRAF_B / 2, 38, titel, 24, "middle", True),
          f'<line x1="{x0}" y1="{onder}" x2="{x1+20}" y2="{onder}" stroke="{DONKER}" stroke-width="3"/>',
          f'<line x1="{x0}" y1="{onder}" x2="{x0}" y2="{top-20}" stroke="{DONKER}" stroke-width="3"/>',
          tekst(x1 + 20, onder + 62, xlabel, 19, "end"), tekst(x0 + 10, top - 26, ylabel, 19)]


def lijn(pts, kleur, dikte=5, streep=None):
    s = f' stroke-dasharray="{streep}"' if streep else ""
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polyline points="{p}" fill="none" stroke="{kleur}" stroke-width="{dikte}"{s}/>'


@tekening
def voorraadverloop():
    gx, gy = pm.gx, pm.gy
    T, V = pm.VV_DAGEN, pm.VV_VMAX
    d = []
    assen(d, "dagen", "stuks in voorraad", "Voorraad van fietsbanden bij Velo nv")
    for v in (0, 100, 200, 300, 400, 500, 600):
        d.append(tekst(pm.GRAF_X0 - 12, gy(v, V) + 7, v, 17, "end"))
    for t in (0, 30, 60, 90):
        d.append(tekst(gx(t, T), pm.GRAF_ONDER + 28, t, 17, "middle"))
    for v, naam in ((pm.VV_MAX, "maximum"), (pm.VV_MIN, "minimum")):
        d.append(lijn([(pm.GRAF_X0, gy(v, V)), (pm.GRAF_X1 + 10, gy(v, V))], "#b5651d", 3, "10 7"))
        d.append(tekst(pm.GRAF_X1 + 10, gy(v, V) - 12, naam, 18, "end", kleur="#b5651d", vet=True))
    pts = []
    for c in range(3):
        a = c * pm.VV_CYCLUS
        pts += [(gx(a, T), gy(pm.VV_MAX, V)), (gx(a + pm.VV_CYCLUS, T), gy(pm.VV_MIN, V))]
    d.append(lijn(pts, GROEN))
    (UIT / "voorraadverloop.svg").write_text(svg(pm.GRAF_B, pm.GRAF_H, d), encoding="utf-8")


@tekening
def voorraadkosten():
    gx, gy = pm.gx, pm.gy
    Q, V = pm.VK_QMAX, pm.VK_VMAX
    d = []
    assen(d, "grootte van een bestelling (stuks)", "kosten per jaar", "De voorraadkosten en de bestelgrootte")
    qs = [q for q in range(140, 1001, 5)]
    krommen = [("A", pm.vk_bewaar, "#b5651d"), ("B", pm.vk_bestel, "#3b6fa0"),
               ("C", lambda q: pm.vk_bewaar(q) + pm.vk_bestel(q), GROEN)]
    for letter, f, kleur in krommen:
        pts = [(gx(q, Q), gy(f(q), V)) for q in qs if f(q) <= V]
        d.append(lijn(pts, kleur))
        x, y = pts[-1] if letter != "B" else pts[-1]
        d.append(f'<circle cx="{x+30:.1f}" cy="{y:.1f}" r="20" fill="{kleur}"/>')
        d.append(tekst(x + 30, y + 8, letter, 22, "middle", True, "#fff"))
    (UIT / "voorraadkosten.svg").write_text(svg(pm.GRAF_B, pm.GRAF_H, d), encoding="utf-8")


@tekening
def breakeven():
    gx, gy = pm.gx, pm.gy
    Q, V = pm.BE_QMAX, pm.BE_VMAX
    d = []
    assen(d, "afzet (stuks)", "euro", "Kosten en opbrengsten van Plaat bv")
    for v in range(0, 100001, 20000):
        d.append(tekst(pm.GRAF_X0 - 12, gy(v, V) + 7, f"{v:,}".replace(",", " "), 17, "end"))
    for q in range(0, 2001, 500):
        d.append(tekst(gx(q, Q), pm.GRAF_ONDER + 28, f"{q:,}".replace(",", " "), 17, "middle"))
    krommen = [("A", lambda q: pm.BE_VAST, "#b5651d"), ("B", lambda q: pm.BE_VAST + pm.BE_VAR * q, "#3b6fa0"),
               ("C", lambda q: pm.BE_PRIJS * q, GROEN)]
    for letter, f, kleur in krommen:
        d.append(lijn([(gx(0, Q), gy(f(0), V)), (gx(Q, Q), gy(f(Q), V))], kleur))
        x, y = gx(Q, Q), gy(f(Q), V)
        d.append(f'<circle cx="{x+32:.1f}" cy="{y:.1f}" r="20" fill="{kleur}"/>')
        d.append(tekst(x + 32, y + 8, letter, 22, "middle", True, "#fff"))
    (UIT / "breakeven.svg").write_text(svg(pm.GRAF_B, pm.GRAF_H, d), encoding="utf-8")


@tekening
def databank():
    B, H = pm.DB_B, pm.DB_H
    d = [tekst(B / 2, 44, "Twee tabellen in een databank van een webwinkel", 24, "middle", True)]
    for naam, t in pm.DB_TABELLEN.items():
        d.append(f'<rect x="{t["x"]}" y="{pm.DB_KOP_Y}" width="{t["w"]}" height="{pm.DB_RIJ}" rx="8" fill="{GROEN}"/>')
        d.append(tekst(t["x"] + 14, pm.DB_KOP_Y + 30, naam, 21, vet=True, kleur="#fff"))
        for k, veld in enumerate(t["velden"]):
            x, w = pm.db_kol(naam, k)
            d.append(f'<rect x="{x:.1f}" y="{pm.DB_VELD_Y}" width="{w:.1f}" height="{pm.DB_RIJ}" fill="{ZACHT}" stroke="{LIJN}" stroke-width="1.5"/>')
            label = ("🔑 " if k == t["sleutel"] else "") + veld
            d.append(tekst(x + w / 2, pm.DB_VELD_Y + 29, label, 18, "middle", True))
            for r, rec in enumerate(t["records"]):
                y = pm.DB_VELD_Y + (r + 1) * pm.DB_RIJ
                d.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{pm.DB_RIJ}" fill="#fff" stroke="{LIJN}" stroke-width="1.5"/>')
                d.append(tekst(x + w / 2, y + 29, rec[k], 18, "middle"))
    # relatielijn onder de tabellen: Klanten.Klantnr (1) naar Bestellingen.Klantnr (veel)
    xa = pm.db_kol("Klanten", 0)[0] + pm.db_kol("Klanten", 0)[1] / 2
    xb = pm.db_kol("Bestellingen", 1)[0] + pm.db_kol("Bestellingen", 1)[1] / 2
    ya = pm.DB_VELD_Y + (len(pm.DB_TABELLEN["Klanten"]["records"]) + 1) * pm.DB_RIJ
    yb = pm.DB_VELD_Y + (len(pm.DB_TABELLEN["Bestellingen"]["records"]) + 1) * pm.DB_RIJ
    y = pm.DB_RELATIE_Y
    d.append(lijn([(xa, ya), (xa, y), (xb, y), (xb, yb)], DONKER, 3))
    d.append(tekst(xa + 14, ya + 30, "1", 24, vet=True))
    d.append(tekst(xb + 14, yb + 34, "∞", 30, vet=True))
    (UIT / "databank.svg").write_text(svg(B, H, d), encoding="utf-8")


@tekening
def hr_gegevens():
    from beyond_bedrijfswetenschappen_themas.hrm import HR_GEGEVENS
    kaart("hr-gegevens.svg", "Personeelsgegevens van drukkerij Inkt nv", HR_GEGEVENS)


@tekening
def hr_stromen():
    raster("hr-stromen.svg", "De loopbaan van een werknemer in de onderneming",
           ["Instroom", "Doorstroom", "Uitstroom"], None, [["binnenkomen", "groeien", "vertrekken"]], grootte=24)


def main():
    UIT.mkdir(parents=True, exist_ok=True)
    for f in TEKENINGEN:
        f()
    print(f"{len(TEKENINGEN)} prenten in {UIT}")


if __name__ == "__main__":
    main()
