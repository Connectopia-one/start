# -*- coding: utf-8 -*-
"""Hulpjes om de vragen van 🧱 Basis na te rekenen.

Elke rekenvraag in de themabestanden krijgt een veld `reken`: wat er volgens
Python uit moet komen. `bouw_basis.py` kijkt dan of de aangeduide optie (of het
invulantwoord) daarmee overeenkomt, en of geen enkele andere optie dat ook doet.
Het veld gaat niet mee naar de JSON.

`reken` kan zijn:
  - een getal (int, Fraction): de aangeduide optie moet die waarde hebben.
    "0,75", "3/4", "2 1/4", "€ 4,50" en "2500 m" worden allemaal gelezen.
  - een tekst: de aangeduide optie moet letterlijk die tekst zijn.
  - True of False: bij een waar/niet-vraag.
"""
import re
from fractions import Fraction as F

_MENG = re.compile(r"(\d+) (\d+)/(\d+)")
_BREUK = re.compile(r"(\d+)/(\d+)")
_KOMMA = re.compile(r"\d{1,3}(?: \d{3})+(?:,\d+)?|\d+(?:,\d+)?")


def g(tekst: str) -> F:
    """Een getal zoals we het in het Nederlands schrijven: "3,45" → 69/20."""
    tekst = tekst.replace(" ", "")
    heel, _, deel = tekst.partition(",")
    return F(int(heel or 0)) + (F(int(deel), 10 ** len(deel)) if deel else 0)


def getal(tekst: str):
    """Het eerste getal in een tekst, als breuk. None als er geen is."""
    for patroon, maak in (
        (_MENG, lambda m: int(m[1]) + F(int(m[2]), int(m[3]))),
        (_BREUK, lambda m: F(int(m[1]), int(m[2]))),
        (_KOMMA, lambda m: g(m[0])),
    ):
        m = patroon.search(tekst)
        if m:
            # Een breuk of gemengd getal wint alleen als het vooraan staat.
            eerder = _KOMMA.search(tekst)
            if patroon is not _KOMMA and eerder and eerder.start() < m.start():
                continue
            return maak(m)
    return None


def nl(waarde) -> str:
    """Een getal terug als tekst, met komma: 69/20 → "3,45", 2500 → "2500"."""
    waarde = F(waarde)
    if waarde.denominator == 1:
        n = waarde.numerator
        return f"{n:,}".replace(",", " ") if n >= 10000 else str(n)
    for decimalen in range(1, 7):
        if (waarde * 10 ** decimalen).denominator == 1:
            heel = int(waarde)
            rest = int((waarde - heel) * 10 ** decimalen)
            return f"{heel},{rest:0{decimalen}d}"
    raise ValueError(f"{waarde} is geen eindig kommagetal")


# --- maten ------------------------------------------------------------------

_VOOR = {"k": 1000, "h": 100, "da": 10, "": 1, "d": F(1, 10), "c": F(1, 100), "m": F(1, 1000)}
_GROND = {"m": "lengte", "g": "gewicht", "l": "inhoud"}
_MAAT = re.compile(r"^\s*([\d ,/]+?)\s*(da|k|h|d|c|m)?(m|g|l)\s*$")


def maat(tekst: str):
    """"1,2 m" → ("lengte", 6/5). Zo kan je maten van soorten vergelijken."""
    m = _MAAT.match(tekst)
    if not m:
        raise ValueError(f"geen maat: {tekst!r}")
    return _GROND[m[3]], getal(m[1]) * _VOOR[m[2] or ""]


def grootste(opties):
    soort = {maat(o)[0] for o in opties}
    assert len(soort) == 1, opties
    return max(opties, key=lambda o: maat(o)[1])


def kleinste(opties):
    soort = {maat(o)[0] for o in opties}
    assert len(soort) == 1, opties
    return min(opties, key=lambda o: maat(o)[1])


def enige(opties, klopt):
    """De enige optie waarvoor klopt(optie) waar is. Faalt als het er niet precies één is."""
    goed = [o for o in opties if klopt(o)]
    if len(goed) != 1:
        raise SystemExit(f"verwacht precies één passende optie, kreeg {goed} uit {opties}")
    return goed[0]


def omzetting_klopt(tekst: str) -> bool:
    """"3,2 kg = 3200 g" → True."""
    links, rechts = tekst.split("=")
    return maat(links) == maat(rechts)


def som_klopt(tekst: str) -> bool:
    """"3,2 × 10 = 32", "45 : 100 = 0,45" of "1,6 + 0,45 = 2,05" → klopt het?"""
    m = re.match(r"^\s*([\d ,]+?)\s*([×:+−-])\s*([\d ,]+?)\s*=\s*([\d ,]+?)\s*$", tekst)
    if not m:
        raise ValueError(f"geen som: {tekst!r}")
    a, b, c = g(m[1]), g(m[3]), g(m[4])
    uitkomst = {"×": a * b, ":": a / b, "+": a + b, "−": a - b, "-": a - b}[m[2]]
    return uitkomst == c


def stijgend(tekst: str) -> bool:
    """"0,2 · 1/2 · 0,7" → staan ze van klein naar groot?"""
    waarden = [getal(d) for d in tekst.split("·")]
    return all(x < y for x, y in zip(waarden, waarden[1:]))


def delers(n: int) -> list:
    return [d for d in range(1, n + 1) if n % d == 0]


def priem(n: int) -> bool:
    return n > 1 and delers(n) == [1, n]


# --- vragen schrijven ---------------------------------------------------------
# Kort, zodat een themabestand leest als een lijst vragen en niet als code.
# Bij meerkeuze staat het juiste antwoord vooraan; het platform schudt de
# opties bij het tonen (lib/optievolgorde.ts).

WOORD = object()   # voor vragen zonder getal om na te rekenen (definities)


def mk(vraag, opties, uitleg, reken):
    return dict(type="meerkeuze", vraag=vraag, opties=list(opties), antwoord=0,
                uitleg=uitleg, reken=reken)


def invul(vraag, antwoord, uitleg, reken):
    return dict(type="invultekst", vraag=vraag, antwoord=antwoord, uitleg=uitleg, reken=reken)


def won(vraag, antwoord, uitleg, reken):
    return dict(type="waarofniet", vraag=vraag, antwoord=antwoord, uitleg=uitleg, reken=reken)


# --- tekeningen en doe-oefeningen (zie components/Figuren.tsx) -----------------

_FIGUUR = re.compile(r"\{\{\s*figuur\s+(cirkel|strook|raster)\s+(\d+)/(\d+)\s*\}\}")


def figuur(vorm: str, teller: int, noemer: int) -> str:
    """De markering voor een tekening in de vraag: figuur("cirkel", 3, 8)."""
    return "{{figuur %s %d/%d}}" % (vorm, teller, noemer)


def gekleurd(vraag: str) -> F:
    """Hoeveel er gekleurd is in de (enige) tekening van een vraag."""
    treffers = _FIGUUR.findall(vraag)
    if len(treffers) != 1:
        raise SystemExit(f"verwacht één tekening in {vraag!r}, vond er {len(treffers)}")
    return F(int(treffers[0][1]), int(treffers[0][2]))


def kleur(vraag, vorm, delen, deel, uitleg):
    """Een kleuroefening: het kind kleurt `deel` van een tekening in `delen` stukken.
    Het antwoord is hoeveel stukken gekleurd moeten zijn."""
    stukken = F(deel) * delen
    if stukken.denominator != 1:
        raise SystemExit(f"{vraag!r}: {deel} van {delen} stukken is geen geheel aantal")
    return dict(type="invultekst", vraag=f"{vraag} {{{{kleur {vorm} {delen}}}}}",
                antwoord=str(stukken.numerator), uitleg=uitleg, reken=stukken)


SCHEIDING = " · "


def sleep(vraag, items, richting, uitleg):
    """Een sleepoefening: getallen in volgorde op een lijn zetten. Schrijf de
    items in de juiste volgorde; `reken` zet ze zelf in volgorde om na te kijken."""
    waarden = [getal(i) for i in items]
    if len(set(waarden)) != len(waarden):
        raise SystemExit(f"{vraag!r}: twee getallen zijn even groot")
    juist = sorted(items, key=getal, reverse=(richting == "groot-klein"))
    return dict(type="invultekst", vraag=f"{vraag} {{{{sleep {richting}}}}}",
                opties=list(items), antwoord=SCHEIDING.join(items), uitleg=uitleg,
                reken=SCHEIDING.join(juist))
