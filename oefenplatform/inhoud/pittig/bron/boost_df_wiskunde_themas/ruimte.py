"""Rechten, vlakken en gelijkvormigheid — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_lijn, DONKER

BALK = "ruimte-balk"
P = {
    "A": (220, 520), "B": (620, 520), "C": (800, 390), "D": (400, 390),
    "E": (220, 270), "F": (620, 270), "G": (800, 140), "H": (400, 140),
}
VERBORGEN = {"AD", "DC", "DH"}
RIBBEN = ["AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"]


def _balk():
    d = []
    for r in RIBBEN:
        (x1, y1), (x2, y2) = P[r[0]], P[r[1]]
        stip = ' stroke-dasharray="10 8"' if r in VERBORGEN or r[::-1] in VERBORGEN else ""
        d.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DONKER}" stroke-width="4"{stip}/>')
    plaats = {"A": (-24, 28), "B": (20, 28), "C": (26, 10), "D": (-26, 28), "E": (-26, -8), "F": (14, -14), "G": (22, -10), "H": (-22, -14)}
    for k, (x, y) in P.items():
        dx, dy = plaats[k]
        d.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{DONKER}"/>')
        d.append(s_tekst(x + dx, y + dy, k, 26, vet=True))
    return d


def ribbe(r):
    (x1, y1), (x2, y2) = P[r[0]], P[r[1]]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return pix_zone(mx - 40, my - 40, 80, 80)


GRAFIEKEN = [dict(naam=BALK, titel="Balk ABCD.EFGH in cavalièreperspectief", eigen=_balk)]
PRENTEN = [dict(bestand=f"{BALK}.svg", zelf=True, wat="balk in cavalièreperspectief", vragen="klikvragen over de onderlinge ligging van ribben")]

VRAGEN = [
    klik(
        "Klik op een ribbe die kruisend is met AB.",
        f"{BALK}.svg",
        [ribbe("CG"), ribbe("DH"), ribbe("EH"), ribbe("FG")],
        "Kruisend: niet evenwijdig en geen snijpunt. Dat geldt voor CG, DH, EH en FG. DC, EF en HG zijn evenwijdig met AB; AD, AE, BC en BF snijden AB.",
    ),
    klik(
        "Klik op een ribbe die evenwijdig is met het grondvlak ABCD, maar er niet in ligt.",
        f"{BALK}.svg",
        [ribbe("EF"), ribbe("FG"), ribbe("GH"), ribbe("HE")],
        "De ribben van het bovenvlak EFGH liggen in een vlak dat evenwijdig is met het grondvlak.",
    ),
    met_prent(f"{BALK}.svg", tabel(
        "Wat is de onderlinge ligging van deze twee rechten?",
        [
            ("AB en GH", "evenwijdig"),
            ("AB en CG", "kruisend"),
            ("AE en EH", "snijdend"),
            ("BF en DH", "evenwijdig"),
            ("EF en DC", "evenwijdig"),
            ("BC en EH", "evenwijdig"),
            ("AE en BC", "kruisend"),
        ],
        "Evenwijdige rechten liggen in één vlak zonder snijpunt. Kruisende rechten liggen niet in één vlak. EF en DC liggen samen in het schuine vlak EFCD, BC en EH in het vlak BCHE.",
        kolommen=["evenwijdig", "snijdend", "kruisend"],
    )),
    met_prent(f"{BALK}.svg", mk(
        "Wat is de doorsnede van het vlak ABFE en het vlak BCGF?",
        ["de rechte BF", "het punt B", "de rechte FG", "die vlakken snijden elkaar niet"],
        0,
        "Twee snijdende vlakken hebben een rechte gemeen. Zowel B als F ligt in beide vlakken.",
    )),
    met_prent(f"{BALK}.svg", mk(
        "Waarom zijn de ribben AD, DC en DH in stippellijn getekend?",
        [
            "ze zijn korter dan de andere ribben",
            "ze liggen achter de balk en zijn niet zichtbaar",
            "ze staan loodrecht op het vlak van het blad",
            "bij cavalièreperspectief teken je schuine ribben altijd zo",
        ],
        1,
        "Onzichtbare ribben teken je in stippellijn. De schuine ribben BC, FG en EH zie je wel, en die zijn vol getekend.",
    )),
    sorteer(
        "Kan dit bij twee rechten in één vlak, of enkel in de ruimte?",
        ["Kan in één vlak", "Enkel in de ruimte"],
        [
            ["Ze snijden elkaar in één punt.", "Kan in één vlak"],
            ["Ze zijn kruisend.", "Enkel in de ruimte"],
            ["Ze zijn evenwijdig en vallen niet samen.", "Kan in één vlak"],
            ["Ze snijden niet en zijn niet evenwijdig.", "Enkel in de ruimte"],
            ["Ze staan loodrecht op elkaar en snijden elkaar.", "Kan in één vlak"],
        ],
        "In één vlak snijden twee rechten elkaar of zijn ze evenwijdig. Wie niet snijdt en niet evenwijdig is, is kruisend: dat kan pas in de ruimte.",
    ),
    tabel(
        "Juist of fout over rechten en vlakken in de ruimte?",
        [
            ("Twee vlakken die elkaar snijden, hebben juist één punt gemeen.", F),
            ("Een rechte die evenwijdig is met een vlak, kan dat vlak niet snijden.", J),
            ("Door twee kruisende rechten gaat geen enkel vlak.", J),
            ("Twee rechten die allebei loodrecht op hetzelfde vlak staan, zijn evenwijdig.", J),
        ],
        "Snijdende vlakken hebben een rechte gemeen. Kruisende rechten liggen per definitie niet in één vlak. Denk aan twee verticale ribben van een balk: allebei loodrecht op het grondvlak, en evenwijdig.",
    ),
    koppel(
        "Koppel elk lichaam aan zijn bovenaanzicht als het rechtop op tafel staat.",
        [
            ["een cilinder", "een cirkel"],
            ["een vierzijdige piramide met vierkant grondvlak", "een vierkant met zijn twee diagonalen"],
            ["een kubus", "een vierkant"],
            ["een kegel", "een cirkel met een stip in het midden"],
        ],
        ["een driehoek"],
        "Van boven zie je bij een piramide de vier opstaande ribben naar de top lopen: de diagonalen. Een kegel toont zijn top als stip midden in de cirkel.",
    ),
    mk(
        "Welk lichaam heeft als vooraanzicht een driehoek en als bovenaanzicht een cirkel?",
        ["een kegel", "een cilinder", "een piramide", "een prisma met driehoekig grondvlak"],
        0,
        "Een rechtopstaande kegel ziet er van voor uit als een driehoek en van boven als een cirkel.",
    ),
    casus(
        r"\(A\) is de verzameling van de positieve delers van \(12\), \(B\) die van de positieve delers van \(18\).",
        [
            mk(
                r"Wat is \(A \cap B\)?",
                [r"\(\{1, 2, 3, 6\}\)", r"\(\{1, 2, 3, 4, 6, 9, 12, 18\}\)", r"\(\{4, 12\}\)", r"\(\{6\}\)"],
                0,
                r"\(A = \{1, 2, 3, 4, 6, 12\}\) en \(B = \{1, 2, 3, 6, 9, 18\}\). De doorsnede bevat wat in allebei zit.",
            ),
            inv(
                r"Hoeveel elementen heeft \(A \cup B\)?",
                ["8", "acht"],
                r"\(6 + 6 - 4 = 8\): de gemeenschappelijke elementen tel je maar één keer.",
            ),
            mk(
                r"Wat is \(A \setminus B\)?",
                [r"\(\{9, 18\}\)", r"\(\{4, 12\}\)", r"\(\{1, 2, 3, 6\}\)", r"\(\{4, 9, 12, 18\}\)"],
                1,
                r"\(A\) zonder \(B\): de delers van \(12\) die geen deler van \(18\) zijn.",
            ),
        ],
    ),
    tabel(
        r"Juist of fout? \(C = \{2, 4, 6, 8\}\) en \(D = \{4, 8\}\).",
        [
            (r"\(D \subset C\)", J),
            (r"\(C \cap D = D\)", J),
            (r"\(C \cup D = D\)", F),
            (r"\(D \setminus C = \{2, 6\}\)", F),
        ],
        r"Elk element van \(D\) zit in \(C\). Dan is de doorsnede \(D\) en de unie \(C\). \(D \setminus C\) is leeg; \(\{2, 6\}\) is \(C \setminus D\).",
    ),
    mk(
        r"Een stok van \(1{,}5\) m werpt een schaduw van \(2\) m. Op hetzelfde moment werpt een boom een schaduw van \(12\) m. Hoe hoog is de boom?",
        [r"\(16\) m", r"\(9\) m", r"\(11{,}5\) m", r"\(8\) m"],
        1,
        r"Stok en schaduw vormen met de zonnestralen gelijkvormige driehoeken. De factor is \(12 : 2 = 6\), dus \(1{,}5 \cdot 6 = 9\) m.",
    ),
    casus(
        r"Een maquette van een sporthal is gemaakt op schaal \(1 : 200\).",
        [
            inv(
                r"Op de maquette is de hal \(25\) cm lang. Hoeveel meter is dat in het echt?",
                ["50", "50 m", "50 meter"],
                r"\(25 \cdot 200 = 5000\) cm \(= 50\) m.",
            ),
            mk(
                r"Het dak van de maquette heeft een oppervlakte van \(300\) cm². Hoe groot is het echte dak?",
                [r"\(60\,000\) cm²", r"\(1200\) m²", r"\(600\) m²", r"\(12\,000\) m²"],
                1,
                r"Oppervlakte gaat met het kwadraat van de factor: \(300 \cdot 200^{2} = 12\,000\,000\) cm² \(= 1200\) m².",
            ),
        ],
    ),
    keuze(
        r"Twee gelijkvormige vazen: de grote is \(1{,}5\) keer zo hoog als de kleine. Dan is haar omtrek [[*\(1{,}5\)|\(2{,}25\)|\(3{,}375\)]] keer zo groot, haar buitenoppervlak [[*\(2{,}25\)|\(1{,}5\)|\(3{,}375\)]] keer zo groot en haar inhoud [[*\(3{,}375\)|\(2{,}25\)|\(1{,}5\)]] keer zo groot.",
        r"Lengtes met factor \(k\), oppervlaktes met \(k^{2} = 2{,}25\), inhoud met \(k^{3} = 3{,}375\).",
    ),
    mk(
        r"Een kubus heeft een inhoud van \(8\) liter. Een gelijkvormige kubus heeft een inhoud van \(27\) liter. Wat is de gelijkvormigheidsfactor?",
        [r"\(\tfrac{27}{8}\)", r"\(\tfrac{3}{2}\)", r"\(\tfrac{9}{4}\)", r"\(19\)"],
        1,
        r"De inhoud gaat met \(k^{3}\): \(k^{3} = \tfrac{27}{8}\), dus \(k = \tfrac{3}{2}\). Ribben van \(2\) dm en \(3\) dm.",
    ),
    koppel(
        "Koppel elk gegeven bij twee driehoeken aan het kenmerk waarmee je besluit dat ze gelijkvormig zijn.",
        [
            [r"zijden \(4, 6, 8\) en \(6, 9, 12\)", "ZZZ"],
            [r"twee zijden \(3\) en \(5\) met ingesloten hoek \(40^{\circ}\), en twee zijden \(6\) en \(10\) met ingesloten hoek \(40^{\circ}\)", "ZHZ"],
            [r"hoeken \(50^{\circ}\) en \(70^{\circ}\) in de ene, hoeken \(70^{\circ}\) en \(60^{\circ}\) in de andere", "HH"],
        ],
        ["ZZH"],
        r"\(6 : 4 = 9 : 6 = 12 : 8 = 1{,}5\). Bij ZHZ zijn twee zijden evenredig en is de ingesloten hoek gelijk. Bij HH: de derde hoek van de eerste driehoek is \(60^{\circ}\).",
    ),
    mk(
        r"Driehoek \(PQR\) heeft zijden \(PQ = 6\), \(QR = 8\) en \(PR = 10\). Een gelijkvormige driehoek heeft als langste zijde \(15\). Hoe lang is zijn kortste zijde?",
        [r"\(11\)", r"\(9\)", r"\(12\)", r"\(7{,}5\)"],
        1,
        r"De factor is \(15 : 10 = 1{,}5\), en de kortste zijde wordt \(6 \cdot 1{,}5 = 9\). Wie \(5\) optelt in plaats van te vermenigvuldigen, komt op \(11\).",
    ),
    tabel(
        "Zijn deze figuren altijd gelijkvormig?",
        [
            ("twee vierkanten", J),
            ("twee rechthoeken", F),
            ("twee gelijkzijdige driehoeken", J),
            ("twee cirkels", J),
            ("twee ruiten", F),
        ],
        r"Vierkanten, gelijkzijdige driehoeken en cirkels hebben altijd dezelfde vorm. Een rechthoek van \(1\) op \(4\) heeft niet de vorm van een rechthoek van \(2\) op \(3\); ruiten kunnen verschillende hoeken hebben.",
    ),
    sleep(
        "In het cavalièreperspectief teken je het vooraanzicht op ware grootte. Ribben die naar achter lopen, teken je [[schuin]] en [[verkort]]. Evenwijdige ribben blijven [[evenwijdig]].",
        ["loodrecht", "verlengd"],
        "Zo krijg je diepte in de tekening zonder dat evenwijdige lijnen samenkomen.",
    ),
    inv(
        r"Op een kaart met schaal \(1 : 50\,000\) ligt een wandelroute van \(7{,}5\) km. Hoeveel cm is die route op de kaart?",
        ["15", "15 cm"],
        r"\(7{,}5\) km \(= 750\,000\) cm, en \(750\,000 : 50\,000 = 15\) cm.",
    ),
    mk(
        r"Een kubus wordt opengevouwen tot een ontwikkeling. Hoeveel ribben moet je minstens doorknippen?",
        [r"\(5\)", r"\(7\)", r"\(6\)", r"\(12\)"],
        1,
        r"De zes vierkanten blijven aan elkaar hangen langs \(5\) ribben. Van de \(12\) ribben knip je er dus \(12 - 5 = 7\) door.",
    ),
    mk(
        r"Een reuzenpizza heeft een dubbel zo grote diameter als een gewone pizza, en is even dik. Hoeveel gewone pizza's eet je evenveel als één reuzenpizza?",
        [r"\(2\)", r"\(4\)", r"\(8\)", r"\(6\)"],
        1,
        r"De oppervlakte gaat met het kwadraat van de factor: \(2^{2} = 4\). Omdat de dikte gelijk blijft, telt enkel de oppervlakte.",
    ),
    open_(
        "Leg uit waarom een mens die drie keer zo groot zou worden, door zijn eigen botten zou zakken. Gebruik de woorden volume en oppervlakte.",
        "Zijn gewicht hangt af van zijn volume, en dat wordt 3³ = 27 keer zo groot. De kracht die een bot kan dragen, hangt af van de oppervlakte van de botdoorsnede, en die wordt maar 3² = 9 keer zo groot. Elk stukje bot moet dus 3 keer zoveel dragen.",
    ),
    met_prent(f"{BALK}.svg", mk(
        "Wat is de onderlinge ligging van de diagonaal AC van het grondvlak en de ribbe FG?",
        ["evenwijdig", "snijdend", "kruisend", "ze vallen samen"],
        2,
        "AC ligt in het grondvlak, FG in het bovenvlak, en ze lopen in een andere richting. Ze snijden niet en zijn niet evenwijdig.",
    )),
    met_prent(f"{BALK}.svg", mk(
        "Welke rechte ligt in het vlak door A, C, G en E?",
        ["de rechte BH", "de rechte AG", "de rechte CD", "de rechte EF"],
        1,
        "A en G liggen allebei in dat schuine vlak, dus de hele rechte AG ook. BH snijdt het vlak enkel in het midden van de balk.",
    )),
    inv(
        r"Een auto van \(4{,}2\) m is op een bouwtekening \(2{,}1\) cm lang. Op welke schaal is de tekening gemaakt? Typ bijvoorbeeld 1:50.",
        ["1:200", "1 : 200", "1/200"],
        r"\(4{,}2\) m \(= 420\) cm, en \(420 : 2{,}1 = 200\).",
    ),
    keuze(
        r"Een element van \(A \cap B\) zit [[*altijd|nooit|soms]] in \(A \cup B\). Een element van \(A \setminus B\) zit [[*nooit|altijd|soms]] in \(B\). Een element van \(A \cup B\) zit [[*soms|altijd|nooit]] in \(A \cap B\).",
        r"Wat in beide zit, zit zeker in de unie. Wat in \(A\) zonder \(B\) zit, zit per definitie niet in \(B\). Een element van de unie kan in maar één van beide zitten.",
    ),
]
