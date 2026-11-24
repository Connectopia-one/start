"""Algebraïsche structuren en groepen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, LICHT, RAND

CAY = "groepen-cayley-bey"
_EL = ["e", "a", "b", "c"]
_T = {"e": "eabc", "a": "abce", "b": "bcea", "c": "ceab"}
X0, Y0, BW, BH = 260, 80, 120, 92


def _cel(rij, kol):
    """rij/kol 0 = kop, 1..4 = elementen."""
    return X0 + kol * BW, Y0 + rij * BH


def _tabel():
    d = []
    for r in range(5):
        for k in range(5):
            x, y = _cel(r, k)
            vul = LICHT if (r == 0 or k == 0) else "#fffdf7"
            d.append(s_vak(x, y, BW, BH, vul=vul, rand=RAND))
            if r == 0 and k == 0:
                t = "∗"
            elif r == 0:
                t = _EL[k - 1]
            elif k == 0:
                t = _EL[r - 1]
            else:
                t = _T[_EL[r - 1]][k - 1]
            d.append(s_tekst(x + BW / 2, y + BH / 2 + 12, t, 34, vet=(r == 0 or k == 0)))
    return d


def _zone(rij, kol):
    x, y = _cel(rij, kol)
    return pix_zone(x + 4, y + 4, BW - 8, BH - 8)


def _r(el):
    return _EL.index(el) + 1


GRAFIEKEN = [dict(naam=CAY, titel="De Cayley-tabel van een groep met vier elementen", eigen=_tabel)]
PRENTEN = [dict(bestand=f"{CAY}.svg", zelf=True, wat="Cayley-tabel van een groep {e, a, b, c}", vragen="klikvragen over neutraal en invers element")]

VRAGEN = [
    klik(
        r"Klik in de rij van \(c\) op het vakje dat toont welk element het invers van \(c\) is.",
        f"{CAY}.svg",
        [_zone(_r("c"), _r("a"))],
        r"Zoek in de rij van \(c\) waar \(e\) staat: in de kolom van \(a\). Dus \(c^{-1} = a\).",
    ),
    klik(
        r"Klik in de kopregel op het element \(x\) waarvoor \(a \ast x = c\).",
        f"{CAY}.svg",
        [_zone(0, _r("b"))],
        r"In de rij van \(a\) staat \(c\) in de kolom van \(b\).",
    ),
    met_prent(f"{CAY}.svg", tabel(
        "Kijk naar de Cayley-tabel. Juist of fout?",
        [("De groep is commutatief.", J), (r"\(b\) is zijn eigen invers.", J), (r"\(a \ast a = e\)", F), (r"In elke kolom staat elk element precies één keer.", J), (r"Het neutraal element is \(a\).", F)],
        r"De tabel is symmetrisch om de diagonaal. De rij van \(e\) herhaalt de kopregel, dus \(e\) is neutraal.",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{CAY}.svg", inv(
        r"Bereken met de tabel \((a \ast a) \ast a\). Schrijf de letter.",
        ["c"],
        r"Eerst het product tussen haakjes, dan nog eens met \(a\).",
    )),
    met_prent(f"{CAY}.svg", mk(
        r"Los op met de tabel: \(b \ast x = a\).",
        [r"\(x = c\)", r"\(x = a\)", r"\(x = b\)", r"\(x = e\)"],
        0,
        r"In de rij van \(b\) staat \(a\) in de kolom van \(c\).",
    )),
    met_prent(f"{CAY}.svg", inv(
        r"Bereken met de tabel \(c \ast c \ast c \ast c\). Schrijf de letter.",
        ["e"],
        r"\(c \ast c = b\), \(b \ast c = a\), \(a \ast c = e\).",
    )),
    sorteer(
        "Is het een groep?",
        ["Groep", "Geen groep"],
        [(r"\((\mathbb{Q}_{0}, \cdot)\)", "Groep"), (r"\((\{-1, 1\}, \cdot)\)", "Groep"), (r"de even gehele getallen met \(+\)", "Groep"),
         (r"\((\{0, 1\}, \cdot)\)", "Geen groep"), (r"de oneven gehele getallen met \(+\)", "Geen groep"), (r"\((\mathbb{Z}, -)\)", "Geen groep")],
        "Twee oneven getallen geven een even som: niet intern. Aftrekken is niet associatief. 0 heeft geen invers.",
    ),
    casus(
        r"Op \(\mathbb{Z}\) definieer je \(a \ast b = a + b + 1\).",
        [
            mk(r"Is \(\ast\) intern in \(\mathbb{Z}\)?", ["ja, want een som van gehele getallen plus 1 is geheel", "nee, want je telt er telkens 1 bij op en dat mag niet", "enkel voor positieve gehele getallen a en b samen", "enkel als a en b twee verschillende getallen zijn"], 0, "Optellen van gehele getallen geeft altijd een geheel getal."),
            inv("Wat is het neutraal element?", ["-1", "−1", "min 1"], r"\(a + e + 1 = a\) geeft \(e = -1\)."),
            mk(r"Wat is het invers van \(a\)?", [r"\(-a - 2\)", r"\(-a\)", r"\(-a - 1\)", r"\(\tfrac{1}{a}\)"], 0, r"\(a + a' + 1 = -1\) geeft \(a' = -a - 2\)."),
        ],
    ),
    tabel(
        r"In elke groep \((G, \ast)\): juist of fout?",
        [(r"\((a \ast b)^{-1} = b^{-1} \ast a^{-1}\)", J), (r"\(e^{-1} = e\)", J), (r"Uit \(x \ast a = y \ast a\) volgt \(x = y\).", J), (r"\(a \ast b = b \ast a\)", F), (r"Er kan een element zijn met twee inversen.", F)],
        "Het invers is uniek, en de schrappingswet geldt links en rechts.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Je lost \(a \ast x = b\) op in een niet-commutatieve groep. Wat is \(x\)?",
        [r"\(a^{-1} \ast b\)", r"\(b \ast a^{-1}\)", r"\(b \ast a\)", r"\(a \ast b^{-1}\)"],
        0,
        r"Bewerk links met \(a^{-1}\): \(a^{-1} \ast a \ast x = a^{-1} \ast b\).",
    ),
    volgorde(
        r"Zet de stappen van het bewijs dat het neutraal element uniek is in volgorde.",
        [r"stel dat \(e\) en \(e'\) allebei neutraal zijn", r"omdat \(e'\) neutraal is, geldt \(e \ast e' = e\)", r"omdat \(e\) neutraal is, geldt \(e \ast e' = e'\)", r"dus \(e = e'\)"],
        "Je berekent hetzelfde product op twee manieren.",
    ),
    koppel(
        "Verbind de structuur met haar neutraal element.",
        [(r"\((\mathbb{Z}, +)\)", r"\(0\)"), (r"\((\mathbb{R}_{0}, \cdot)\)", r"\(1\)"), ("matrices van orde 2 met de optelling", "de nulmatrix"), ("inverteerbare matrices van orde 2 met de vermenigvuldiging", "de eenheidsmatrix")],
        [r"\(-1\)"],
        "Het neutraal element verandert niets aan wat je ermee bewerkt.",
    ),
    tabel(
        "Welke eigenschap ontbreekt?",
        [(r"\((\mathbb{N}, +)\)", "invers element"), (r"de oneven gehele getallen met \(+\) en het getal 1 erbij", "intern"), (r"\((\mathbb{Z}, -)\)", "associatief"), (r"\((\mathbb{Z}, \cdot)\)", "invers element")],
        r"\((5 - 3) - 1 \neq 5 - (3 - 1)\). Een som van twee oneven getallen ligt niet meer in de verzameling.",
        kolommen=["intern", "associatief", "invers element"],
    ),
    mk(
        "De draaiingen van een vierkant over 0°, 90°, 180° en 270° vormen een groep met 'na elkaar uitvoeren'. Wat is het invers van de draaiing over 90°?",
        ["de draaiing over 270°", "de draaiing over 90°", "de draaiing over 180°", "de draaiing over 0°"],
        0,
        "90° + 270° = 360°, en dat is hetzelfde als niet draaien.",
    ),
    inv(
        "Bij dezelfde draaiingen van het vierkant: hoeveel graden is de draaiing over 180° gevolgd door die over 270°? Geef een getal van 0 tot 359.",
        ["90", "negentig"],
        "450° is een volle toer plus 90°.",
    ),
    keuze(
        r"De inverteerbare matrices van orde 2 vormen met de vermenigvuldiging een groep die [[*niet commutatief|commutatief]] is. Alle matrices van orde 2 vormen met de vermenigvuldiging [[*geen groep|een groep]].",
        r"Een matrix met determinant 0 heeft geen inverse, en \(AB\) is niet altijd \(BA\).",
    ),
    sleep(
        r"Een groep vraagt een [[interne]] bewerking die [[associatief]] is, met een [[neutraal]] element en voor elk element een [[invers]] element.",
        ["commutatieve", "eindig"],
        "Commutatief hoeft niet: dat maakt de groep extra.",
    ),
    tabel(
        "Juist of fout over getallenverzamelingen?",
        [(r"\((\mathbb{R}, \cdot)\) is een groep.", F), (r"\((\mathbb{C}, +)\) is een commutatieve groep.", J), (r"In \((\mathbb{Q}_{0}, \cdot)\) is het invers van \(\tfrac{2}{3}\) gelijk aan \(\tfrac{3}{2}\).", J), (r"In \((\mathbb{Z}, +)\) is het invers van \(-4\) gelijk aan \(\tfrac{1}{4}\).", F)],
        r"Bij \(+\) is het invers het tegengestelde, bij \(\cdot\) het omgekeerde. In \(\mathbb{R}\) heeft 0 geen omgekeerde.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"In een groep geldt \(a \ast a = e\) voor elk element. Wat weet je over \(a^{-1}\)?",
        [r"\(a^{-1} = a\)", r"\(a^{-1} = e\)", r"\(a^{-1}\) bestaat niet", r"\(a^{-1} = a \ast a\)"],
        0,
        r"\(a \ast a = e\) betekent precies dat \(a\) zijn eigen invers is.",
    ),
    inv(
        "Een eindige groep heeft 7 elementen. Hoeveel vakjes heeft haar Cayley-tabel, zonder kopregel en kopkolom?",
        ["49", "negenenveertig"],
        r"\(7 \cdot 7\).",
    ),
    mk(
        "Waarom kan in een rij van de Cayley-tabel van een groep geen element twee keer staan?",
        ["anders is a ∗ x = a ∗ y met x ≠ y, wat de schrappingswet verbiedt", "omdat de tabel anders niet meer symmetrisch om de diagonaal is", "omdat elke groep commutatief is en elke rij dus anders is", "omdat het neutraal element dan nergens in de tabel staat"],
        0,
        r"Bewerk \(a \ast x = a \ast y\) links met \(a^{-1}\): dan is \(x = y\).",
    ),
    tabel(
        r"Op \(\mathbb{R}\) definieer je \(a \ast b = \tfrac{a + b}{2}\), het gemiddelde. Juist of fout?",
        [(r"\(\ast\) is intern in \(\mathbb{R}\).", J), (r"\(\ast\) is commutatief.", J), (r"\(\ast\) is associatief.", F)],
        r"\((0 \ast 0) \ast 4 = 2\), maar \(0 \ast (0 \ast 4) = 1\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Welk getal is in \((\mathbb{R}_{0}, \cdot)\) zijn eigen invers, naast 1?",
        [r"\(-1\)", r"\(0\)", r"\(\tfrac{1}{2}\)", r"\(2\)"],
        0,
        r"\((-1) \cdot (-1) = 1\).",
    ),
    tabel(
        r"Op \(\mathbb{R}\) definieer je \(a \circ b = \max(a, b)\), het grootste van de twee. Juist of fout?",
        [(r"\(\circ\) is associatief.", J), (r"\(\circ\) is commutatief.", J), (r"\((\mathbb{R}, \circ)\) heeft een neutraal element.", F)],
        r"Een neutraal element zou kleiner moeten zijn dan elk reëel getal, en dat bestaat niet.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Wat is in \((\mathbb{Q}_{0}, \cdot)\) het invers van \(-0{,}25\)?",
        ["-4", "−4", "min 4"],
        r"\(-0{,}25 \cdot (-4) = 1\).",
    ),
    mk(
        "Welke structuur is een eindige groep?",
        [r"\((\{1, -1, i, -i\}, \cdot)\)", r"\((\mathbb{N}, +)\)", r"\((\mathbb{Z}, +)\)", r"\((\{0, 1, 2\}, +)\)"],
        0,
        r"Elk product van twee van die vier getallen ligt er weer in, en elk heeft een invers. Bij \(\{0, 1, 2\}\) is \(2 + 2 = 4\) niet intern.",
    ),
    inv(
        r"Op \(\mathbb{Z}\) is \(a \circ b = a + b - 3\). Wat is het neutraal element?",
        ["3", "drie"],
        r"\(a + e - 3 = a\).",
    ),
    mk(
        r"Waarom is \((\{-1, 0, 1\}, +)\) geen groep?",
        [r"omdat \(1 + 1\) niet in de verzameling ligt", "omdat 0 geen invers heeft voor de optelling", "omdat de optelling niet associatief is", "omdat er geen neutraal element in zit"],
        0,
        "De bewerking is niet intern.",
    ),
]
