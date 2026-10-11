# -*- coding: utf-8 -*-
"""Zet de natuurkundige formules die nog gewone tekst zijn om naar notatie.

    python3 -I fysnot.py --toon <bestand.py> ...      toont wat het zou doen
    python3 -I fysnot.py [--strings] <bestand.py> ... past het toe

Werkt na naar_notatie.py, dus op tekst waar de getallen al in notatie staan.
Het zoekt een hele vergelijking (Q = c . m . DeltaT, p.V = n.R.T) en maakt
daar een formule van, met \\cdot tussen twee symbolen en \\times tussen twee
getallen. Een span telt enkel mee als er een bekend natuurkundig symbool of
een isgelijkteken in staat; zo blijft gewone tekst gewone tekst. Bestaande
formules worden eerst weggemaskeerd, zodat er nooit een formule in een
formule belandt.
"""
import re, sys, os

GRIEKS = {"ρ": r"\rho", "μ": r"\mu", "α": r"\alpha",
          "β": r"\beta", "θ": r"\theta", "λ": r"\lambda",
          "π": r"\pi", "Ω": r"\Omega", "σ": r"\sigma",
          "ω": r"\omega", "φ": r"\varphi", "ε": r"\varepsilon"}
ONDER = str.maketrans("₀₁₂₃₄₅₆₇"
                      "₈₉", "0123456789")

GROOT = set((
    "Fz Fn Fw Fv FA Fr Fm Fe Fg Fres Ek Ep Ez Em Et Eel Ekin Epot "
    "Q U I R P W M "
    "ΔT Δl Δx Δt Δp ΔV ΔE Δv Δs "
    "x₀ t₀ v₀ p₀ V₀ T₀ s₀ "
    "Vond Vv ls lv Rs Rp Us Up Is Ip "
    "ρ μ α θ λ Ω φ ω").split())
LETTER = set("ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghiklmnpqrstuvwxyz")
EENHEIDLETTER = set("NJWAVCKTLsmghF")
EENHEID = {"kg", "mol", "Hz", "Pa", "Nm", "km", "cm", "mm", "ms", "kJ", "MJ",
           "kW", "mA", "kN", "Wb", "rad", "min", "uur", "kWh", "ton", "dm",
           "mL", "kPa", "hPa", "MPa", "Ah", "nm", "GHz", "kHz"}

AAN, UIT = "", ""
NOT = AAN + r"\d+" + UIT
SYM = (r"(?:Δ?[A-Za-zρμαβθλπΩ"
       r"σωφε]"
       r"(?:[₀-₉]|,?[a-z]{1,4}(?![a-zéëèï]))?)")
GETAL = r"\d+(?:[.,]\d+)?"
TERM = "(?:%s|%s|%s)" % (NOT, SYM, GETAL)
TERMP = r"(?:\(\s*)*" + TERM + r"(?:\s*\))*"
OP = r"(?:\s*(?:\.(?!\s*[A-Z])|[·×/+=^]|−|-(?=[\s(]))\s*)"
SPAN = re.compile(r"(?<![\w\\{éë" + AAN + r"])(%s(?:%s%s)+)"
                  % (TERMP, OP, TERMP))
WOORD = re.compile(r"^[a-zéëèïáäöüA-Z]{2,}$")


def sym(s):
    s = s.strip()
    kop = ""
    if s.startswith("Δ"):
        kop, s = r"\Delta ", s[1:]
    if not s:
        return r"\Delta"
    letter, rest = s[0], s[1:]
    letter = GRIEKS.get(letter, letter)
    rest = rest.translate(ONDER).lstrip(",")
    if rest:
        rest = r"\text{%s}" % rest if len(rest) > 1 else rest
        return "%s%s_{%s}" % (kop, letter, rest)
    return kop + letter


_not, _getal, _sym_, _op = (re.compile(NOT), re.compile(GETAL),
                            re.compile(SYM), re.compile(OP))


def deel(span):
    """hak de span in termen en operatoren; None als er iets vreemds in staat"""
    uit, i = [], 0
    while i < len(span):
        for soort, rx in (("t", _not), ("t", _getal), ("t", _sym_)):
            m = rx.match(span, i)
            if m and m.end() > i:
                uit.append((soort, m.group(0)))
                i = m.end()
                break
        else:
            if span[i] in "()":
                uit.append(("h", span[i]))
                i += 1
                continue
            m = _op.match(span, i)
            if m and m.end() > i:
                uit.append(("o", m.group(0).strip()))
                i = m.end()
                continue
            return None
    return uit


def bruikbaar(stukken, ruw):
    if stukken is None:
        return False
    termen = [s for k, s in stukken if k == "t"]
    if len(termen) < 2:
        return False
    alles_getal = all(t.startswith(AAN) or re.fullmatch(GETAL, t)
                      for t in termen)
    if "=" not in ruw and not alles_getal \
            and not any(t in GROOT for t in termen):
        return False
    # "N / m" is een eenheid, geen formule
    if "=" not in ruw and all(len(t) == 1 and t in EENHEIDLETTER
                              for t in termen):
        return False
    for t in termen:
        if t.startswith(AAN):
            continue
        if t in EENHEID:
            return False
        if WOORD.match(t) and t not in GROOT:
            return False
        if len(t) == 1 and t.isalpha() and t not in LETTER and t not in GRIEKS:
            return False
    return True


def bouw(stukken, bewaar):
    uit, vorig = [], None
    for k, s in stukken:
        if k == "t":
            if s.startswith(AAN):
                binnen = bewaar[int(s[1:-1])]
                uit.append(binnen.strip())
                vorig = "n" if re.fullmatch(r"[\d{},.\\\s-]+", binnen) else "s"
            elif re.fullmatch(GETAL, s):
                uit.append(s.replace(",", "{,}"))
                vorig = "n"
            else:
                uit.append(sym(s))
                vorig = "s"
        elif k == "h":
            uit.append(r"\left(" if s == "(" else r"\right)")
        else:
            if s in (".", "·"):
                uit.append(r"\times" if vorig == "n" else r"\cdot")
            elif s == "×":
                uit.append(r"\times")
            elif s == "−":
                uit.append("-")
            else:
                uit.append(s)
    los = " ".join(uit).replace(r"\left( ", r"\left(").replace(r" \right)", r"\right)")
    return r"\(" + los + r"\)"



# ── exponenten die buiten de formule bleven staan ─────────────────────────
MACHT_NA = re.compile(r"\\\((?P<b>(?:[^\\]|\\(?![()]))*?)\\\)\^\{(?P<n>\d)\}")
EENH = re.compile(r"(?<![\w}])([A-Za-z\u03a9]+(?:/[A-Za-z\u03a9]+)+)\^\{(\d)\}")


def exponenten(t):
    # \(F = m \cdot g\)^{2}  ->  \(F = m \cdot g^{2}\)
    t = MACHT_NA.sub(lambda m: r"\(%s^{%s}\)" % (m.group("b"), m.group("n")), t)
    # m/s^{2}  ->  \(\text{m/s}^{2}\), en aan een getal ervoor vastgeplakt
    t = EENH.sub(lambda m: r"\(\text{%s}^{%s}\)" % (m.group(1), m.group(2)), t)
    t = re.sub(r"\\\((?P<a>(?:[^\\]|\\(?![()]))*?)\\\)\s+\\\(\\text\{(?P<e>[^{}]*)\}\^\{(?P<n>\d)\}\\\)",
               lambda m: r"\(%s\ \text{%s}^{%s}\)" % (m.group("a"), m.group("e"), m.group("n")), t)
    return t

FORM = re.compile(r"\\\((.*?)\\\)", re.S)
KOP = re.compile(r'\A(?:#[^\n]*\n)*"""(?:.|\n)*?"""', re.S)


def regels(t):
    bewaar = []

    def weg(m):
        bewaar.append(m.group(1))
        return "%s%d%s" % (AAN, len(bewaar) - 1, UIT)
    k = KOP.match(t)
    kop, t = (t[:k.end()], t[k.end():]) if k else ("", t)
    t = exponenten(t)
    t = FORM.sub(weg, t)
    n = [0]

    def vervang(m):
        ruw = m.group(1).rstrip(" .")
        voor = t[:m.start()].rstrip()
        eerste = re.match(SYM, ruw)
        if (eerste and len(eerste.group(0)) == 1
                and eerste.group(0) in EENHEIDLETTER
                and m.start() > 0 and t[m.start() - 1] in " \u00a0"
                and (voor.endswith(")") or voor.endswith(UIT)
                     or (voor and voor[-1].isdigit()))):
            return m.group(0)
        while ruw.count("(") < ruw.count(")") and ruw.endswith(")"):
            ruw = ruw[:-1].rstrip(" .")
        while ruw.count("(") > ruw.count(")") and ruw.startswith("("):
            ruw = ruw[1:].lstrip()
        if ruw.count("(") != ruw.count(")"):
            return m.group(0)
        stukken = deel(ruw)
        if not bruikbaar(stukken, ruw):
            return m.group(0)
        n[0] += 1
        return bouw(stukken, bewaar) + m.group(0)[len(ruw):]
    t = SPAN.sub(vervang, t)
    t = re.sub(AAN + r"(\d+)" + UIT,
               lambda m: r"\(" + bewaar[int(m.group(1))] + r"\)", t)
    return kop + t, n[0]


paden = [a for a in sys.argv[1:] if not a.startswith("--")]
for pad in paden:
    tekst = open(pad, encoding="utf-8").read()

    def doe(s):
        return regels(regels(s)[0])[0]

    if "--strings" in sys.argv:
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
        print(pad, "omgezet")
