# -*- coding: utf-8 -*-
"""Hulp voor Launchpad-vragen (1ste en 2de leerjaar). Zelfde vorm als Ready (vr.py),
maar met een paar extra's: K() zet het juiste antwoord op een plaats die telkens
verschuift, zodat het niet altijd vooraan of het langste staat."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "ready" / "bron"))
from vr import mk, inv, wn  # noqa: E402

_plaats = [0]


def K(vraag, juist, fout, uitleg, reken=None, prent=None):
    """Meerkeuze: juist antwoord + foute opties, plaats schuift telkens op."""
    opties = list(fout)
    p = _plaats[0] % (len(fout) + 1); _plaats[0] += 1
    opties.insert(p, juist)
    return mk(vraag, [str(o) for o in opties], p, uitleg, reken, prent)


def I(vraag, antwoord, uitleg, reken=None, prent=None):
    a = antwoord if isinstance(antwoord, list) else [str(antwoord)]
    return inv(vraag, a if len(a) > 1 else a[0], uitleg, reken, prent)


def W(zin, waar, uitleg, prent=None):
    return wn(zin, waar, uitleg, prent)


def buren(r, n, lo, hi):
    """Drie foute getallen dicht bij n, binnen [lo, hi]."""
    s = set()
    while len(s) < 3:
        x = n + r.choice([-3, -2, -1, 1, 2, 3, 10, -10])
        if lo <= x <= hi and x != n: s.add(x)
    return sorted(s)
