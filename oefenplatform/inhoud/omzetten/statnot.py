# -*- coding: utf-8 -*-
"""Statistiek in notatie: H0, mu, sigma, alfa, P(X ≤ 4), X ~ B(20; 0,3).

    python3 -I statnot.py [--letters] [--strings] <bestand.py> …

Met --strings gaat enkel de tekst in de string-literalen mee; dat is wat je
nodig hebt in een bundelbestand, waar ook echte python staat.

Met --letters gaan ook de losse n, p en k in notatie; doe dat alleen in een
bestand waar die letters altijd een variabele zijn.

Werkt met merktekens: elke bestaande \\( ... \\) gaat eerst opzij, zodat geen
enkele regel binnen een formule kan toeslaan.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OPEN, SLUIT = "", ""
TEKEN = {"≤": r"\leq", "≥": r"\geq", "≠": r"\neq", "~": r"\sim",
         "<": "<", ">": ">", "=": "="}
SYMBOOL = [(r"H0", "H_{0}"), (r"H1", "H_{1}"), (r"mu", r"\mu"),
           (r"sigma", r"\sigma"), (r"alfa", r"\alpha"),
           (r"Q1", "Q_{1}"), (r"Q2", "Q_{2}"), (r"Q3", "Q_{3}")]
# met --letters: de losse letters die in statistiek altijd een variabele zijn
LETTERS = [(r"n", "n"), (r"p", "p"), (r"k", "k")]


def omzet(t):
    bak, tel = [], {}

    def mt(inhoud):
        bak.append(inhoud)
        return f"{OPEN}{len(bak) - 1}{SLUIT}"

    def tl(naam, k=1):
        if k:
            tel[naam] = tel.get(naam, 0) + k

    t = re.sub(r"\\\((.*?)\\\)", lambda m: mt(m.group(1)), t, flags=re.S)
    t = re.sub(r"<[^<>]*>", lambda m: mt(m.group(0)), t)   # html-tags blijven html
    M = re.escape(OPEN) + r"\d+" + re.escape(SLUIT)
    NR = re.compile(re.escape(OPEN) + r"(\d+)" + re.escape(SLUIT))

    def inh(stuk):
        m = NR.fullmatch(stuk)
        return bak[int(m.group(1))] if m else stuk

    # P(X ≤ 4), P(Z < 1,96), P(X = k)
    def kans(m):
        tl("kans")
        return mt("P(%s %s %s)" % (m.group(1), TEKEN.get(m.group(2), m.group(2)),
                                   inh(m.group(3))))
    t = re.sub(r"\bP\(([XZYK])\s*([=<>≤≥≠])\s*(" + M + r"|[a-zA-Z])\)", kans, t)

    # B(20; 0,3) en N(100; 15)
    def verdeling(m):
        tl("verdeling")
        return mt("%s(%s; %s)" % (m.group(1), inh(m.group(2)), inh(m.group(3))))
    t = re.sub(r"\b([BN])\((" + M + r"); (" + M + r")\)", verdeling, t)

    # X is B(...)  ->  X ~ B(...)
    def verdeeld(m):
        inhoud = inh(m.group(1))
        if not re.match(r"[BN]\(", inhoud):
            return m.group(0)
        tl("verdeeld als")
        return mt(r"X \sim " + inhoud)
    t = re.sub(r"\bX (?:is|~) (" + M + r")", verdeeld, t)

    for woord, latex in SYMBOOL + (LETTERS if "--letters" in sys.argv else []):
        t, k = re.subn(r"(?<![\w\\])" + woord + r"(?![\w])",
                       lambda m, l=latex: mt(l), t)
        tl(woord, k)
    t, k = re.subn(r"\bx met een streepje\b", lambda m: mt(r"\bar{x}"), t)
    tl("x-streep", k)
    t, k = re.subn(r"\bp met een dakje\b", lambda m: mt(r"\hat{p}"), t)
    tl("p-dakje", k)

    def terug(m):
        inhoud = inh(m.group(0))
        return inhoud if inhoud.startswith("<") else r"\(" + inhoud + r"\)"

    t = re.sub(M, terug, t)
    return t, tel



for pad in [a for a in sys.argv[1:] if not a.startswith("--")]:
    tekst = open(pad, encoding="utf-8").read()
    if "--strings" in sys.argv:          # bundelbestand: enkel de tekst
        from op_strings import pas_toe
        alles = {}
        def doe(s, alles=alles):
            s, tel = omzet(s)
            for k, v in tel.items():
                alles[k] = alles.get(k, 0) + v
            return s
        open(pad, "w", encoding="utf-8").write(pas_toe(tekst, doe))
        print(pad, alles)
        continue
    kop = re.match(r'\A(?:#[^\n]*\n)*"""(?:.|\n)*?"""', tekst, re.S)
    k, rest = (kop.group(0), tekst[kop.end():]) if kop else ("", tekst)
    rest, tel = omzet(rest)
    open(pad, "w", encoding="utf-8").write(k + rest)
    print(pad, tel)
