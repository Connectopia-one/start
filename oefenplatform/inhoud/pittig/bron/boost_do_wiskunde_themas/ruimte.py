"""Rechten, vlakken en gelijkvormigheid — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import s_lijn, s_tekst, pix_zone, DONKER, GROEN

BALK = "ruimte-balk-do"
P = {"A": (200, 540), "B": (620, 540), "F": (620, 310), "E": (200, 310)}
DX, DY = 200, -140
for o, n in (("A", "D"), ("B", "C"), ("F", "G"), ("E", "H")):
    P[n] = (P[o][0] + DX, P[o][1] + DY)
RIBBEN = ["AB", "BF", "FE", "EA", "DC", "CG", "GH", "HD", "AD", "BC", "FG", "EH"]
VERBORGEN = {"AD", "DC", "DH", "HD"}


def _midden(r):
    (x1, y1), (x2, y2) = P[r[0]], P[r[1]]
    return (x1 + x2) / 2, (y1 + y2) / 2


def _ribzone(r):
    x, y = _midden(r)
    return pix_zone(x - 34, y - 34, 68, 68)


def _balk():
    d = []
    for r in RIBBEN:
        (x1, y1), (x2, y2) = P[r[0]], P[r[1]]
        if r in VERBORGEN:
            d.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GROEN}" stroke-width="3" stroke-dasharray="10 8"/>')
        else:
            d.append(s_lijn(x1, y1, x2, y2, kleur=GROEN, dikte=4))
    plaats = {"A": (-22, 30), "B": (18, 30), "C": (22, 22), "D": (-26, 26), "E": (-24, -8), "F": (18, -10), "G": (22, -10), "H": (-24, -12)}
    for k, (x, y) in P.items():
        d.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{DONKER}"/>')
        d.append(s_tekst(x + plaats[k][0], y + plaats[k][1], k, 26, vet=True))
    return d


def _hoekzone(k):
    x, y = P[k]
    return pix_zone(x - 32, y - 32, 64, 64)


GRAFIEKEN = [dict(naam=BALK, titel="Balk ABCD EFGH in cavalièreperspectief", eigen=_balk)]
PRENTEN = [dict(bestand=f"{BALK}.svg", zelf=True, wat="balk met hoekpunten A tot H, verborgen ribben in stippellijn", vragen="klikvragen over ligging van rechten en vlakken")]

VRAGEN = [
    klik(
        "Klik op een ribbe die kruisend is met de ribbe AB.",
        f"{BALK}.svg",
        [_ribzone(r) for r in ("CG", "HD", "EH", "FG")],
        "AB is niet evenwijdig met CG, DH, EH en FG, en raakt ze ook niet. Ze liggen niet in één vlak met AB: dat is kruisend.",
    ),
    klik(
        "Klik op het hoekpunt waar de vlakken ABFE, BCGF en EFGH samenkomen.",
        f"{BALK}.svg",
        [_hoekzone("F")],
        "Het voorvlak, het rechterzijvlak en het bovenvlak hebben enkel F gemeen.",
    ),
    klik(
        "Klik op een ribbe die evenwijdig is met het vlak ABCD, maar er niet in ligt.",
        f"{BALK}.svg",
        [_ribzone(r) for r in ("EH", "FG", "FE", "GH")],
        "De ribben van het bovenvlak EFGH lopen evenwijdig met het grondvlak ABCD.",
    ),
    klik(
        "Klik op de ribbe die de doorsnede is van de vlakken ABCD en BCGF.",
        f"{BALK}.svg",
        [_ribzone("BC")],
        "Twee snijdende vlakken hebben een rechte gemeen. Hier is dat de ribbe BC.",
    ),
    met_prent(f"{BALK}.svg", tabel(
        "Kijk naar de balk. Welke ligging hebben de twee rechten?",
        [("AB en HG", "evenwijdig"), ("AB en BF", "snijdend"), ("AB en CG", "kruisend"), ("EH en BC", "evenwijdig"), ("AE en DC", "kruisend")],
        "Evenwijdig: in één vlak en nooit samen. Snijdend: één punt gemeen. Kruisend: niet in één vlak.",
        kolommen=["evenwijdig", "snijdend", "kruisend"],
    )),
    tabel(
        "Juist of fout over rechten en vlakken in de ruimte?",
        [
            ("Twee rechten die elkaar niet snijden, zijn altijd evenwijdig.", F),
            ("Twee verschillende vlakken die elkaar snijden, hebben een rechte gemeen.", J),
            ("Een rechte kan een vlak in precies twee punten snijden.", F),
            ("Door twee snijdende rechten gaat precies één vlak.", J),
            ("Twee kruisende rechten kunnen loodrecht op elkaar staan.", J),
            ("Een vlak en een rechte die er niet in ligt, hebben altijd een punt gemeen.", F),
        ],
        "In de ruimte kunnen rechten ook kruisen. Een rechte die een vlak snijdt, doet dat in één punt; een rechte kan ook evenwijdig lopen met een vlak.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        "Hoeveel paren evenwijdige ribben heeft een balk?",
        ["6", "12", "18", "24"],
        2,
        "Er zijn drie richtingen met elk vier evenwijdige ribben. Vier ribben vormen \\(6\\) paren, dus \\(3 \\cdot 6 = 18\\).",
    ),
    koppel(
        "Verbind elke rechtopstaande figuur met haar bovenaanzicht.",
        [("kegel", "een cirkel met een punt in het midden"), ("cilinder", "een cirkel zonder punt"), ("vierzijdige piramide", "een vierkant met de twee diagonalen"), ("balk", "een rechthoek")],
        ["een driehoek"],
        "Van boven zie je het grondvlak. Bij een kegel en een piramide zie je ook de top en de ribben ernaartoe.",
    ),

    mk(
        "Welke figuur heeft als vooraanzicht, zijaanzicht en bovenaanzicht drie even grote cirkels?",
        ["een cilinder", "een bol", "een kegel", "een kubus"],
        1,
        "Een bol ziet er langs elke kant hetzelfde uit. Een cilinder heeft van voor een rechthoek.",
    ),
    sorteer(
        "Kun je dit patroon opvouwen tot een kubus?",
        ["Ja", "Nee"],
        [("een kruisvorm: vier vierkanten op een rij met één erboven en één eronder in het tweede vak", "Ja"),
         ("zes vierkanten op één rij", "Nee"),
         ("vier vierkanten op een rij met boven en onder het eerste vak er één bij", "Ja"),
         ("een blok van twee op drie vierkanten", "Nee"),
         ("vier vierkanten rond één hoekpunt met twee vierkanten eraan", "Nee")],
        "Een ontwikkeling van een kubus heeft zes vierkanten waarvan er nooit vier rond één hoekpunt liggen en nooit vijf op een rij.",
    ),
    tabel(
        r"Neem \(A = \{1, 2, 3, 4, 6\}\) en \(B = \{2, 4, 5, 8\}\). Klopt het?",
        [
            (r"\(A \cap B = \{2, 4\}\)", J),
            (r"\(A \cup B\) heeft \(9\) elementen", F),
            (r"\(A \setminus B = \{1, 3, 6\}\)", J),
            (r"\(B \setminus A = \{5, 8\}\)", J),
            (r"\(\{2, 4\} \subset B\)", J),
            (r"\(\{2, 5\} \subset A\)", F),
        ],
        r"\(A \cup B = \{1, 2, 3, 4, 5, 6, 8\}\): zeven elementen, want \(2\) en \(4\) tel je maar één keer. \(5\) zit niet in \(A\).",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        "In een klas van 26 leerlingen spelen er 15 voetbal en 12 tennis. Vijf leerlingen doen geen van beide. Hoeveel leerlingen doen allebei?",
        ["6", "zes"],
        r"\(26 - 5 = 21\) leerlingen doen minstens één sport. \(15 + 12 - 21 = 6\) tel je dubbel: die doen beide.",
    ),
    keuze(
        r"Als \(A \subset B\), dan is \(A \cap B\) gelijk aan [[*\(A\)|\(B\)|de lege verzameling]] en \(A \cup B\) gelijk aan [[*\(B\)|\(A\)|de lege verzameling]].",
        "Alles van A zit al in B. De gemeenschappelijke elementen zijn dus die van A, en samen krijg je B.",
    ),
    mk(
        "Twee driehoeken zijn gelijkvormig. De zijden van de kleine zijn 4, 6 en 8 cm. De kleinste zijde van de grote is 10 cm. Wat is de omtrek van de grote driehoek?",
        ["24 cm", "45 cm", "60 cm", "34 cm"],
        1,
        r"De factor is \(10 : 4 = 2{,}5\). De omtrek wordt ook \(2{,}5\) keer zo groot: \(18 \cdot 2{,}5 = 45\) cm.",
    ),
    mk(
        "Een driehoek wordt vergroot zodat zijn oppervlakte 9 keer zo groot wordt. Hoeveel keer zo lang worden de zijden?",
        ["3 keer", "9 keer", "4,5 keer", "81 keer"],
        0,
        r"De oppervlakte wordt \(k^{2}\) keer zo groot. \(k^{2} = 9\), dus \(k = 3\).",
    ),
    mk(
        "Een kubus van 2 cm ribbe weegt 20 g. Hoeveel weegt een kubus van hetzelfde materiaal met ribbe 6 cm?",
        ["60 g", "180 g", "540 g", "120 g"],
        2,
        r"De factor is \(3\), het volume en dus het gewicht worden \(3^{3} = 27\) keer zo groot: \(540\) g.",
    ),
    tabel(
        r"Bij een gelijkvormigheidsfactor \(k\): hoeveel keer zo groot wordt het?",
        [("de omtrek", r"\(k\)"), ("de oppervlakte", r"\(k^{2}\)"), ("het volume", r"\(k^{3}\)"), ("een hoek", "blijft gelijk"), ("de lengte van een diagonaal", r"\(k\)")],
        "Alles wat een lengte is, gaat maal k. Oppervlakte twee keer maal k, volume drie keer. Hoeken veranderen niet.",
        kolommen=[r"\(k\)", r"\(k^{2}\)", r"\(k^{3}\)", "blijft gelijk"],
    ),
    casus(
        "Een tuinarchitect maakt een plan op schaal 1 : 200. Een rechthoekig grasveld is op het plan 6 cm lang en 4 cm breed.",
        [
            mk("Hoe lang is het grasveld in het echt?", ["1,2 m", "12 m", "120 m", "30 m"], 1, r"\(6 \cdot 200 = 1200\) cm \(= 12\) m."),
            mk("Hoe groot is de oppervlakte in het echt?", [r"\(96\) m\(^{2}\)", r"\(48\) m\(^{2}\)", r"\(9{,}6\) m\(^{2}\)", r"\(960\) m\(^{2}\)"], 0, r"\(12 \cdot 8 = 96\) m\(^{2}\)."),
            mk("Hoeveel keer is de echte oppervlakte groter dan op het plan?", ["200", "400", "40 000", "8 000 000"], 2, r"Bij schaal \(1 : 200\) is de oppervlakte \(200^{2} = 40\,000\) keer zo groot."),
        ],
    ),
    sorteer(
        "Zijn de twee driehoeken zeker gelijkvormig?",
        ["Zeker gelijkvormig", "Niet zeker"],
        [("Beide hebben hoeken van 40° en 75°.", "Zeker gelijkvormig"),
         ("Zijden 3, 4, 5 en zijden 6, 8, 10.", "Zeker gelijkvormig"),
         ("Beide zijn gelijkbenig.", "Niet zeker"),
         ("Beide hebben een hoek van 50°.", "Niet zeker"),
         ("Twee zijden 2 en 3 met ingesloten hoek 60°, en twee zijden 4 en 6 met ingesloten hoek 60°.", "Zeker gelijkvormig"),
         ("Beide zijn rechthoekig.", "Niet zeker")],
        "HH, ZZZ en ZHZ zijn de kenmerken. Eén gelijke hoek of 'gelijkbenig' is niet genoeg.",
    ),
    inv(
        "Een boom werpt een schaduw van 12 m. Op hetzelfde moment werpt een paal van 1,5 m een schaduw van 2 m. Hoe hoog is de boom, in meter?",
        ["9", "9 m", "9 meter", "9,0"],
        r"De zonnestralen maken dezelfde hoek, dus de driehoeken zijn gelijkvormig (HH). \(\dfrac{h}{12} = \dfrac{1{,}5}{2}\), dus \(h = 9\) m.",
    ),


    mk(
        "Twee gelijkvormige flessen hebben een hoogte van 15 cm en 30 cm. De kleine bevat 25 cl. Hoeveel bevat de grote?",
        ["50 cl", "100 cl", "200 cl", "75 cl"],
        2,
        r"De factor is \(2\), de inhoud gaat maal \(2^{3} = 8\): \(200\) cl.",
    ),
    tabel(
        "Juist of fout over schaal?",
        [
            ("Op schaal 1 : 50 is 1 cm op de tekening 50 cm in het echt.", J),
            ("Een schaal 5 : 1 is een vergroting.", J),
            ("Op een kaart van 1 : 100 000 is 1 cm gelijk aan 10 km.", F),
            ("Een kaart op schaal 1 : 10 000 toont meer details dan een kaart op 1 : 100 000 van hetzelfde gebied.", J),
            ("Op schaal 1 : 20 is een oppervlakte op de tekening 20 keer kleiner.", F),
        ],
        r"\(100\,000\) cm is \(1\) km. Bij schaal \(1 : 20\) is de oppervlakte \(400\) keer kleiner.",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        "Bij cavalièreperspectief teken je het voorvlak [[op ware grootte]] en de ribben naar achter [[schuin]] en korter. Ribben die evenwijdig zijn, blijven [[evenwijdig]]. Verborgen ribben teken je [[in stippellijn]].",
        ["loodrecht", "gebogen", "niet"],
        "Zo krijg je een ruimtelijk beeld op papier waarin je toch nog lengtes kunt aflezen.",
    ),
    volgorde(
        "Een kubus heeft ribbe 1. Je maakt gelijkvormige kubussen met factor 2, 3 en 4. Zet deze getallen van klein naar groot.",
        ["volume bij factor 2", "oppervlakte van één zijvlak bij factor 3", "totale oppervlakte bij factor 2", "volume bij factor 4"],
        r"Volume bij factor 2: \(2^{3} = 8\). Zijvlak bij factor 3: \(3^{2} = 9\). Totale oppervlakte bij factor 2: \(6 \cdot 4 = 24\). Volume bij factor 4: \(64\).",
    ),
    inv(
        "Een balk heeft hoekpunten ABCD EFGH. Hoeveel ribben zijn kruisend met één gegeven ribbe?",
        ["4", "vier"],
        "Van de elf andere ribben zijn er drie evenwijdig en vier snijdend. De overige vier zijn kruisend.",
    ),
    mk(
        "Welke ruimtefiguur heeft als ontwikkeling een rechthoek met twee cirkels eraan?",
        ["een kegel", "een cilinder", "een prisma", "een piramide"],
        1,
        "De mantel van een cilinder rolt open tot een rechthoek. Boven en onder zit een cirkel.",
    ),
    tabel(
        "Juist of fout over gelijkvormigheid?",
        [
            ("Twee vierkanten zijn altijd gelijkvormig.", J),
            ("Twee rechthoeken zijn altijd gelijkvormig.", F),
            ("Twee cirkels zijn altijd gelijkvormig.", J),
            ("Twee gelijkvormige figuren zijn ook altijd even groot.", F),
        ],
        "Een rechthoek van 1 op 2 en een van 1 op 3 hebben niet dezelfde vorm. Vierkanten en cirkels hebben maar één maat die verandert.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        "De oppervlakte van een figuur op een plan is 25 keer kleiner dan in het echt. Op welke schaal is het plan getekend? Typ zoals 1 : 10.",
        ["1 : 5", "1:5", "1 op 5"],
        r"De oppervlakte wordt \(k^{2}\) keer kleiner. \(k^{2} = 25\) geeft \(k = 5\).",
    ),
]
