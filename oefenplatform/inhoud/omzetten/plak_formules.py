# -*- coding: utf-8 -*-
"""Twee formules die naast elkaar staan tot een plakken.

Na het omzetten blijft er soms een rekenteken buiten de formules staan:

    \\(14\\) x \\(4 = 56\\)

Dat is "14" in wiskundeletters, dan een gewone x in gewone letters, en dan
weer wiskundeletters. Op het scherm zie je dat verschil. Dit script maakt er

    \\(14 \\times 4 = 56\\)

van: een formule.

Het teken tussen de twee formules moet er een zijn dat enkel in een berekening
voorkomt, met een spatie langs beide kanten. Een puntkomma, een dubbelepunt of
een koppelteken blijven dus staan, want die horen bij de zin.

Een middelste punt (·) staat er bewust niet bij. Die gebruiken we in de
bundels ook als scheidingsteken in een opsomming: "\\(0{,}2\\) · \\(0{,}7\\)" is
een rijtje, geen maalbewerking, en dat verschil kan dit script niet zien.

Een schuine streep kan ook een rijtje scheiden ("kansen \\(0{,}1\\) / \\(0{,}3\\)").
Dat is zeldzaam, maar kijk de uitvoer van --toon dus altijd na.

Werkt op een bestand met gewone r-strings (\\(...\\)) en op een bestand waar de
backslash verdubbeld staat ("\\\\(...\\\\)"), maar niet op een bestand waar
beide door elkaar staan.

    python3 -I omzetten/plak_formules.py --toon bestand.py
    python3 -I omzetten/plak_formules.py bestand.py
"""
import re
import sys

# het teken buiten de formules, en wat er in de formule van wordt
TEKENS = {
    "x": None,          # maal: \times tussen getallen, \cdot tussen symbolen
    "×": None,
    "=": "=",
    "/": "/",
    "+": "+",
    "−": "-",
}


def _maal(links, rechts):
    """Maal tussen twee getallen is x, tussen symbolen een punt."""
    staart = links.rstrip()[-1:]
    kop = rechts.lstrip()[:1]
    getal = (staart.isdigit() or staart in "})") and (kop.isdigit() or kop in "(")
    return "\\times" if getal else "\\cdot"


def _patroon(bs):
    """De regex voor een paar formules, met bs als backslash in de tekst."""
    aan = re.escape(bs + "(")
    uit = re.escape(bs + ")")
    # de inhoud mag het sluitteken niet bevatten
    inhoud = "(?:(?!%s).)+?" % uit
    tekens = "|".join(re.escape(t) for t in TEKENS)
    return re.compile("%s(%s)%s (%s) %s(%s)%s"
                      % (aan, inhoud, uit, tekens, aan, inhoud, uit))


def plak(bron: str, bs: str = "\\") -> tuple:
    """Plakt paren aan elkaar tot er niets meer te plakken valt."""
    pat = _patroon(bs)
    aantal = 0

    def een(m):
        nonlocal aantal
        links, teken, rechts = m.group(1), m.group(2), m.group(3)
        nieuw = TEKENS[teken] or _maal(links, rechts)
        aantal += 1
        return "%s(%s %s %s%s)" % (bs, links, nieuw, rechts, bs)

    vorig = None
    while vorig != bron:
        vorig = bron
        bron = pat.sub(een, bron)
    return bron, aantal


def doe(pad: str, toon: bool) -> int:
    bron = open(pad, encoding="utf-8").read()
    # een bestand met verdubbelde backslashes herken je aan \\( in de tekst
    bs = "\\\\" if "\\\\(" in bron else "\\"
    nieuw, aantal = plak(bron, bs)
    if toon:
        for oud, nu in zip(bron.splitlines(), nieuw.splitlines()):
            if oud != nu:
                print("- " + oud.strip())
                print("+ " + nu.strip())
    elif aantal:
        open(pad, "w", encoding="utf-8").write(nieuw)
    return aantal


def main(argv):
    toon = "--toon" in argv
    paden = [a for a in argv if not a.startswith("--")]
    totaal = 0
    for pad in paden:
        n = doe(pad, toon)
        if n:
            print("%s: %d geplakt" % (pad, n), file=sys.stderr)
        totaal += n
    print("%d formules geplakt." % totaal, file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:])
