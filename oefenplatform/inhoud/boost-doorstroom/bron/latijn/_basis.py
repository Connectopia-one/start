# -*- coding: utf-8 -*-
"""Gedeelde hulpjes voor de hoofdstukken Latijn (Boost doorstroom, fiche 2027 2DO).

teksten.json bevat de Latijnse teksten, letterlijk overgenomen uit:
Perseus Digital Library (Caesar ed. Rice Holmes, Ovidius ed. Magnus, Plinius,
Gellius ed. Rolfe, Ammianus ed. Rolfe, Petronius ed. Heseltine), de Clementijnse
Vulgata (project BibleGet), Erasmus via The Latin Library (CLTK) en Galileo,
Sidereus Nuncius (1610). FOUTEN hieronder zet tikfouten van de digitale
versies recht; woorden die de uitgever tussen [haken] schrapt, vallen weg.
Verander nooit zelf iets aan de Latijnse tekst.
"""
import sys, json, re
import pathlib
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER.parents[2]))
from uitdaging.bron._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_
T = json.load(open(HIER / 'teksten.json'))
FOUTEN = {'A the nis': 'Athenis', 'eiusmodihuiusmodi': 'huiusmodi', 'differenten': 'differentem', 'tunc tune (ut opinari dabatur), sus- picerent': 'tunc (ut opinari dabatur) suspicerent', 'magnitudo magnitude': 'magnitudo', 'deforis.\\': 'deforis.', 'nune Gavillae': 'nunc Gavillae', 'Me lissam': 'Melissam'}
def schoon(s):
    for a, b in FOUTEN.items(): s = s.replace(a, b)
    s = re.sub(r'\s*\[[^\]]*\]', '', s)
    return re.sub(r'\s+', ' ', s).strip()
def proza(key, refs=None):
    """Caesar-achtige tekst: per hoofdstuk één alinea, met hoofdstuknummer."""
    out = []
    for h in T[key]:
        out.append(f"({h['ref'].split('.')[-1]}) " + ' '.join(f"{schoon(t)}" for n, t in h['secties']))
    return out
def secties(key, a=None, z=None):
    return [(n, schoon(t)) for n, t in T[key] if a is None or (n.isdigit() and a <= int(n) <= z)]
def verzen(key, per=5, a=None, z=None):
    v = [x for x in T[key] if a is None or a <= x[0] <= z]; out = []
    for i in range(0, len(v), per):
        blok = v[i:i+per]
        out.append(f"({blok[0][0]}) " + " / ".join(schoon(t) for n, t in blok))
    return out
def ster(alineas, woorden):
    """Zet *...* rond de eerste keer dat elk woord uit de woordenlijst voorkomt."""
    tekst = "\n\n".join(alineas)
    for w in woorden:
        pat = r'(?<![\w*])' + re.escape(w["woord"]) + r'(?![\w*])'
        tekst, n = re.subn(pat, '*' + w["woord"] + '*', tekst, count=1)
        if n == 0:
            raise SystemExit("woord niet gevonden: " + w["woord"])
    return tekst
def W(**kw): return [{"woord": k.replace('_', ' '), "uitleg": v} for k, v in kw.items()]
def Wl(*paren): return [{"woord": a, "uitleg": b} for a, b in paren]
