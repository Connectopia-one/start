# -*- coding: utf-8 -*-
"""Herstelt de scheikundige notatie die naar_notatie.py uit elkaar trekt.

    python3 -I chemnot.py --toon <bestand.py> ...
    python3 -I chemnot.py [--strings] <bestand.py> ...

Scheikunde schrijft haar formules met echte boven- en onderschriften
(SO4(2-), 1s2 2s2, Mg(2+)). naar_notatie.py kent enkel de wiskunde: het maakt
daar ^{2-} van en laat dat buiten de formule staan, en het hakt 6,02 maal
tien tot de drieentwintigste in twee stukken. Dit script zet de echte
wetenschappelijke notatie wel in een formule, en geeft al de rest zijn
bovengeschreven teken terug. Draai het meteen na naar_notatie.py.
"""
import re, sys, os

HOOG = {"-": "⁻", "+": "⁺", "n": "ⁿ",
        "0": "⁰", "1": "¹", "2": "²", "3": "³",
        "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷",
        "8": "⁸", "9": "⁹"}
KOP = re.compile(r'\A(?:#[^\n]*\n)*"""(?:.|\n)*?"""', re.S)
AAN, UIT = "", ""



# ── vooraf: een molecuulformule zonder onderschriften ─────────────────────
# Enkel deze lijst, want F1, G2, LD50 en H314 zijn geen moleculen.
# F2 en I2 staan er NIET bij: F1 en F2 zijn de generaties uit de genetica.
MOLECULEN = """CO2 H2O O2 N2 H2 Cl2 Br2 C6H12O6 CH2 CH3 CH4 C2H6 C3H8
C4H10 C2H6O H2SO4 H2SO3 H2O2 H3O H2CO3 HNO3 HCO3 CO3 SO4 SO3 NO3 NO2 NH4 NH3
NH2 PO4 ClO3 N2O NaCl Na2 Fe2O3 CaCO3 CaCl2 MgCl2 CuSO4 AgNO3 BaSO4 CH3OH
CH3COOH CH3COCH3 CH3CH2OH CHCl3 CCl4 HO2 Al2O3 SO2 P2O5 K2O Li2O MgO""".split()
LAAG = str.maketrans("0123456789", "\u2080\u2081\u2082\u2083\u2084"
                     "\u2085\u2086\u2087\u2088\u2089")


def vooraf(t):
    """Zet de moleculen uit de lijst in echte onderschriften. Draai dit
    vóór naar_notatie.py, anders leest dat H2 + O2 als een optelling."""
    n = 0
    for naam in sorted(MOLECULEN, key=len, reverse=True):
        if not any(c.isdigit() for c in naam):
            continue
        t, k = re.subn(r"\b" + naam + r"\b", naam.translate(LAAG), t)
        n += k
    return t, n


def regels(t):
    tel = {}

    def zet(naam, patroon, vervang):
        nonlocal t
        t, n = re.subn(patroon, vervang, t)
        if n:
            tel[naam] = tel.get(naam, 0) + n

    # 0. in een reactievergelijking is een getal een coefficient, geen formule
    def plat(regel):
        reactie = "\u2192" in regel or (
            " geeft " in regel
            and re.search(r"[A-Z][A-Za-z]*[\u2080-\u2089]", regel))
        if not reactie:
            return regel
        return re.sub(r"\\\((\d+)\\\)", lambda m: m.group(1), regel)
    regels_ = t.split("\n")
    nieuw_ = [plat(r) for r in regels_]
    if nieuw_ != regels_:
        tel["coefficient"] = sum(1 for a, b in zip(regels_, nieuw_) if a != b)
    t = "\n".join(nieuw_)

    # 0b. een getal voor een molecuul is een coefficient, geen formule
    zet("coefficient voor molecuul",
        r"\\\((\d+)\\\)(\s+)(?=[A-Z][A-Za-z₀-₉]*[₀-₉⁺⁻])",
        lambda m: m.group(1) + m.group(2))

    # 1. \(6\),02.\(10^{23}\)  ->  \(6{,}02 \cdot 10^{23}\)
    zet("wetenschappelijk",
        r"\\\((\d+)\\\),(\d+)\s*[.·]\s*\\\(10\^\{(-?\d+)\}\\\)",
        lambda m: r"\(%s{,}%s \cdot 10^{%s}\)"
        % (m.group(1), m.group(2), m.group(3)))
    zet("wetenschappelijk zonder komma",
        r"\\\((\d+)\\\)\s*[.·]\s*\\\(10\^\{(-?\d+)\}\\\)",
        lambda m: r"\(%s \cdot 10^{%s}\)" % (m.group(1), m.group(2)))

    # 2. wat al in een formule staat, blijft met rust
    bewaar = []

    def weg(m):
        bewaar.append(m.group(0))
        return "%s%d%s" % (AAN, len(bewaar) - 1, UIT)
    t = re.sub(r"\\\(.*?\\\)", weg, t, flags=re.S)

    # 3. elk ander ^{...} krijgt zijn bovengeschreven teken terug
    def terug(m):
        binnen = m.group(1)
        if any(c not in HOOG for c in binnen):
            return m.group(0)
        return "".join(HOOG[c] for c in binnen)
    t, n = re.subn(r"\^\{([^{}]*)\}", terug, t)
    if n:
        tel["bovengeschreven terug"] = n

    t = re.sub(AAN + r"(\d+)" + UIT, lambda m: bewaar[int(m.group(1))], t)
    return t, tel


paden = [a for a in sys.argv[1:] if not a.startswith("--")]
for pad in paden:
    tekst = open(pad, encoding="utf-8").read()
    alles = {}

    def doe(s, alles=alles):
        k = KOP.match(s)
        if "--vooraf" in sys.argv:
            kk = KOP.match(s)
            kop, rest = (s[:kk.end()], s[kk.end():]) if kk else ("", s)
            rest, n = vooraf(rest)
            if n:
                alles["molecuul"] = alles.get("molecuul", 0) + n
            return kop + rest
        kop, rest = (s[:k.end()], s[k.end():]) if k else ("", s)
        rest, tel = regels(rest)
        for a, b in tel.items():
            alles[a] = alles.get(a, 0) + b
        return kop + rest

    if "--velden" in sys.argv:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from op_strings import pas_toe, VELDEN
        nieuw = pas_toe(tekst, doe, VELDEN)
    elif "--strings" in sys.argv:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from op_strings import pas_toe
        nieuw = pas_toe(tekst, doe)
    else:
        nieuw = doe(tekst)
    if "--toon" in sys.argv:
        import difflib
        for r in difflib.unified_diff(tekst.split("\n"), nieuw.split("\n"),
                                      lineterm="", n=0):
            if r[:1] in "+-" and r[:3] not in ("+++", "---"):
                print(r)
    else:
        open(pad, "w", encoding="utf-8").write(nieuw)
        print(pad, alles)
