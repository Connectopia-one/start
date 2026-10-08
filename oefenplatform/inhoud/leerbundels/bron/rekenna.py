# -*- coding: utf-8 -*-
"""Rekent elke som na die in een antwoord van een oefenbundel uitgeschreven staat.

    python3 -I rekenna.py                 alle oefenbundels
    python3 -I rekenna.py maak_oefeningen_aardrijkskunde_beyond

Een scheve tekening zie je meteen, een fout rekenvoorbeeld niet. Daarom zoekt
dit script in de antwoorden naar een uitgeschreven som ("3 200 - 850 - 450 =
1 900 euro", "1200 / 100 x 0,65 = 7,8") en kijkt of de uitkomst klopt. Een
hele keten wordt in één keer gelezen, met maal en gedeeld door vóór plus en
min, zodat een tussenstap niet als een fout gemeld wordt. Een antwoord is vaak
afgerond, dus een afwijking van één procent is goed.

Wat dit script **niet** kan, en dus overslaat: een vergelijking met een
onbekende, een wortelvorm, een percentage en een omzetting van eenheden. Daar
staat links en rechts van het = iets anders dan een getal, en dat herkent
`echte_som` aan het teken dat er tegenaan staat. Een melding is dus niet
automatisch een fout: reken ze met de hand na voor je iets wijzigt.
"""
import importlib, pathlib, re, sys

HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))

GETAL = r"[-−]?\d[\d  ]*(?:[.,]\d+)?"
TEKEN = r"[×÷·+−*/-]"
MAAL, DEEL, PLUS = "×·*", "÷/", "+"
SOM = re.compile(rf"({GETAL}(?:\s*{TEKEN}\s*{GETAL})+)\s*=\s*({GETAL})")
# Een teken dat vlak tegen de som aan staat: dan hangt de som aan iets vast
# (x/4 + 2 = 5, 6/√3 = 2√3, 3x, 27/63) en kunnen we ze niet lezen. Achteraan mag
# wel een punt of een eenheid volgen ("= 1 900 euro"), maar geen letter of
# breukstreep die tegen het getal aan kleeft, en geen teken dat de som verder
# zet ("= 45 + 32 = 77").
VOOR = re.compile(r"[\w√×÷·+−*/^,.=]")
NA = re.compile(r"[\w√^/]")


def echte_som(t, m):
    """Is dit een losstaande som, of hangt ze aan iets vast?"""
    voor, na = t[:m.start()], t[m.end():]
    if voor and VOOR.match(voor[-1]):
        return False
    if na and NA.match(na[0]):
        return False
    rest = na.lstrip()
    # Gaat de som verder ("= 45 + 32 = 77") of staat er een tweede lid naast
    # ("6 · 9 = 9 · 6"), dan is dit nog niet de uitkomst.
    if rest and rest[0] in "×÷·+−*/-=":
        return False
    return "%" not in rest[:1] and "√" not in m.group(0)


def nummer(s):
    s = s.replace(" ", "").replace(" ", "").replace("−", "-")
    return float(s.replace(",", ".") if "," in s else s)


def reken(keten):
    """Rekent de keten uit, met maal en gedeeld door vóór plus en min."""
    stukken = re.split(rf"\s*({TEKEN})\s*", keten)
    rij = [nummer(stukken[0])]
    for i in range(1, len(stukken) - 1, 2):
        teken, getal = stukken[i], nummer(stukken[i + 1])
        if teken in MAAL:
            rij[-1] *= getal
        elif teken in DEEL:
            if getal == 0:
                return None
            rij[-1] /= getal
        else:
            rij += [teken, getal]
    uit = rij[0]
    for i in range(1, len(rij) - 1, 2):
        uit = uit + rij[i + 1] if rij[i] == PLUS else uit - rij[i + 1]
    return uit


def teksten(oefening):
    """Alle tekst van één oefening, hoe diep ze ook genest staat."""
    uit = []

    def loop(d):
        if isinstance(d, str):
            uit.append(d)
        elif isinstance(d, (list, tuple)):
            for x in d:
                loop(x)

    loop(oefening[1:])
    return uit


def main(namen):
    goed = fout = 0
    for naam in namen or sorted(f.stem for f in HIER.glob("maak_oefeningen_*.py")):
        m = importlib.import_module(naam)
        for sleutel, b in getattr(m, "OEFENBUNDELS", {}).items():
            for r in b["reeksen"]:
                for o in r["oefeningen"]:
                    for t in teksten(o):
                        for tref in SOM.finditer(t):
                            if not echte_som(t, tref):
                                continue
                            try:
                                w, z = reken(tref.group(1)), nummer(tref.group(2))
                            except ValueError:
                                continue
                            if w is None:
                                continue
                            if abs(w - z) <= max(abs(z) * 0.01, 0.051):
                                goed += 1
                            else:
                                fout += 1
                                print(f"{sleutel} / {r['kop']}: {tref.group(0)} "
                                      f"maar het is {w:g}")
    print(f"{goed} sommen kloppen, {fout} niet")
    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
