"""Pythagoras en de rechthoekige driehoek — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

ROOSTER = venster("pythagoras-rooster", -3, 8, -1, 7)
PUNTEN = {"A": (1, 1), "B": (4, 5), "C": (5, 5), "D": (6, 3), "E": (-1, 5)}

GRAFIEKEN = [
    dict(naam=ROOSTER, titel="Vijf punten in een assenstelsel",
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()]),
]
PRENTEN = [dict(bestand=f"{ROOSTER}.svg", zelf=True, wat="assenstelsel met vijf punten", vragen="klikvragen over afstanden")]

VRAGEN = [
    klik(
        "Klik op het punt dat precies op afstand 5 van A ligt.",
        f"{ROOSTER}.svg",
        [punt_zone(ROOSTER, 4, 5)],
        r"Van A naar B: \(3\) naar rechts en \(4\) omhoog, dus \(\sqrt{9 + 16} = 5\). C ligt op \(\sqrt{32}\), D op \(\sqrt{29}\), E op \(\sqrt{20}\).",
    ),
    klik(
        "Klik op het punt dat het verst van A ligt.",
        f"{ROOSTER}.svg",
        [punt_zone(ROOSTER, 5, 5)],
        r"Vergelijk de kwadraten van de afstanden: B \(25\), C \(16 + 16 = 32\), D \(25 + 4 = 29\), E \(4 + 16 = 20\). C wint.",
    ),
    met_prent(f"{ROOSTER}.svg", inv(
        "Hoe groot is de afstand tussen D en E? Typ bijvoorbeeld 3√5.",
        ["√53", "wortel 53", "√ 53"],
        r"\(\Delta x = 7\) en \(\Delta y = 2\): \(\sqrt{49 + 4} = \sqrt{53} \approx 7{,}28\).",
    )),
    met_prent(f"{ROOSTER}.svg", mk(
        "Is driehoek ABD rechthoekig?",
        [
            r"ja, met de rechte hoek in B, want \(25 + 8 = 33\)",
            r"nee, want \(AB^{2} + BD^{2}\) is \(33\) en \(AD^{2}\) is \(29\)",
            r"ja, met de rechte hoek in A, want \(AB = 5\)",
            r"dat kan je niet weten zonder hoeken te meten",
        ],
        1,
        r"\(AB^{2} = 25\), \(BD^{2} = 4 + 4 = 8\), \(AD^{2} = 29\). De langste zijde in het kwadraat moet gelijk zijn aan de som van de andere twee: \(25 + 8 = 33 \neq 29\).",
    )),
    tabel(
        "Is een driehoek met deze zijden rechthoekig?",
        [
            (r"\(7\), \(24\) en \(25\)", J),
            (r"\(6\), \(7\) en \(9\)", F),
            (r"\(1\), \(1\) en \(\sqrt{2}\)", J),
            (r"\(8\), \(15\) en \(16\)", F),
            (r"\(0{,}9\), \(1{,}2\) en \(1{,}5\)", J),
        ],
        r"\(49 + 576 = 625\). \(36 + 49 = 85 \neq 81\). \(1 + 1 = 2\). \(64 + 225 = 289 \neq 256\). \(0{,}81 + 1{,}44 = 2{,}25\).",
    ),
    mk(
        r"Een rechthoekig scherm is \(48\) cm breed en \(36\) cm hoog. Hoe lang is de diagonaal?",
        [r"\(84\) cm", r"\(42\) cm", r"\(60\) cm", r"\(72\) cm"],
        2,
        r"\(\sqrt{48^{2} + 36^{2}} = \sqrt{2304 + 1296} = \sqrt{3600} = 60\) cm.",
    ),
    casus(
        r"Een ladder van \(6{,}5\) m staat tegen een muur. De voet staat \(2{,}5\) m van de muur.",
        [
            inv(
                "Hoe hoog reikt de ladder tegen de muur, in meter?",
                ["6", "6 m", "6 meter"],
                r"\(\sqrt{6{,}5^{2} - 2{,}5^{2}} = \sqrt{42{,}25 - 6{,}25} = \sqrt{36} = 6\) m.",
            ),
            mk(
                r"De voet schuift \(1{,}4\) m verder van de muur weg. Hoeveel zakt de top?",
                [r"\(1{,}4\) m", r"\(0{,}8\) m", r"\(2{,}1\) m", r"\(0{,}6\) m"],
                1,
                r"Nu staat de voet op \(3{,}9\) m: \(\sqrt{42{,}25 - 15{,}21} = \sqrt{27{,}04} = 5{,}2\) m. De top zakt van \(6\) naar \(5{,}2\) m. De top zakt dus minder dan de voet opschuift.",
            ),
        ],
    ),
    mk(
        r"Een balk is \(2\) m lang, \(1\) m breed en \(2\) m hoog. Past een stok van \(3\) m er schuin in?",
        [
            r"nee, want de langste ribbe is maar \(2\) m",
            r"ja, precies: de ruimtediagonaal is \(3\) m",
            r"nee, de ruimtediagonaal is \(\sqrt{5}\) m",
            r"ja, want \(2 + 1 = 3\)",
        ],
        1,
        r"\(\sqrt{2^{2} + 1^{2} + 2^{2}} = \sqrt{9} = 3\) m. Eerst de diagonaal van het grondvlak (\(\sqrt{5}\)), dan met de hoogte erbij.",
    ),
    volgorde(
        r"Je zoekt de ruimtediagonaal van een kubus met ribbe \(4\) cm. Zet de stappen in volgorde.",
        [
            "een schets maken met de grondvlakdiagonaal en de ruimtediagonaal",
            r"de diagonaal van het grondvlak berekenen: \(\sqrt{16 + 16} = \sqrt{32}\)",
            r"Pythagoras opnieuw toepassen met de hoogte: \(\sqrt{32 + 16} = \sqrt{48}\)",
            r"vereenvoudigen tot \(4\sqrt{3} \approx 6{,}93\) cm",
        ],
        "De ruimtediagonaal is de schuine zijde van een rechthoekige driehoek met de grondvlakdiagonaal en een opstaande ribbe als rechthoekszijden.",
    ),
    keuze(
        r"In driehoek \(KLM\) is de hoek in \(L\) recht. Dan is [[*\(KM\)|\(KL\)|\(LM\)]] de schuine zijde, en geldt [[*\(KL^{2} + LM^{2} = KM^{2}\)|\(KM^{2} + KL^{2} = LM^{2}\)|\(KL + LM = KM\)]].",
        "De schuine zijde ligt tegenover de rechte hoek. Pythagoras werkt met de kwadraten van de zijden, niet met de zijden zelf.",
    ),
    inv(
        r"Een gelijkzijdige driehoek heeft zijden van \(10\) cm. Hoe hoog is hij? Typ bijvoorbeeld 3√2.",
        ["5√3", "5 √3", "5 wortel 3"],
        r"De hoogte deelt de basis in twee stukken van \(5\): \(\sqrt{100 - 25} = \sqrt{75} = 5\sqrt{3} \approx 8{,}66\) cm.",
    ),
    mk(
        r"Een vierkant heeft een diagonaal van \(10\) cm. Hoe groot is de oppervlakte?",
        [r"\(100\) cm²", r"\(25\) cm²", r"\(50\) cm²", r"\(10\sqrt{2}\) cm²"],
        2,
        r"Met zijde \(z\): \(z^{2} + z^{2} = 100\), dus \(z^{2} = 50\). En \(z^{2}\) is net de oppervlakte.",
    ),
    sorteer(
        "Is de hoek tegenover de langste zijde recht, scherp of stomp?",
        ["recht", "scherp", "stomp"],
        [
            [r"zijden \(5\), \(12\), \(13\)", "recht"],
            [r"zijden \(5\), \(6\), \(7\)", "scherp"],
            [r"zijden \(4\), \(5\), \(8\)", "stomp"],
            [r"zijden \(9\), \(40\), \(41\)", "recht"],
            [r"zijden \(3\), \(4\), \(6\)", "stomp"],
        ],
        r"Vergelijk \(a^{2} + b^{2}\) met \(c^{2}\): gelijk geeft recht, groter geeft scherp, kleiner geeft stomp. \(25 + 36 = 61 > 49\); \(16 + 25 = 41 < 64\); \(9 + 16 = 25 < 36\).",
    ),
    mk(
        r"Een voetbalveld is \(105\) m lang en \(68\) m breed. Hoeveel meter win je ongeveer als je diagonaal oversteekt in plaats van langs twee zijden?",
        [r"\(48\) m", r"\(125\) m", r"\(173\) m", r"\(37\) m"],
        0,
        r"De diagonaal is \(\sqrt{105^{2} + 68^{2}} = \sqrt{15\,649} \approx 125\) m. Langs de zijden is het \(173\) m. Je wint \(173 - 125 = 48\) m.",
    ),
    casus(
        r"Een tent heeft een doorsnede in de vorm van een gelijkbenige driehoek. De bodem is \(2{,}4\) m breed en de twee schuine zijden zijn elk \(2\) m.",
        [
            inv(
                "Hoe hoog is de tent in het midden, in meter? Typ een kommagetal.",
                ["1,6", "1,6 m", "1.6"],
                r"De hoogte valt in het midden van de bodem: \(\sqrt{2^{2} - 1{,}2^{2}} = \sqrt{4 - 1{,}44} = \sqrt{2{,}56} = 1{,}6\) m.",
            ),
            mk(
                r"Hoe groot is de oppervlakte van die driehoekige doorsnede?",
                [r"\(3{,}84\) m²", r"\(1{,}92\) m²", r"\(2{,}4\) m²", r"\(4{,}8\) m²"],
                1,
                r"\(\tfrac{\text{basis} \cdot \text{hoogte}}{2} = \tfrac{2{,}4 \cdot 1{,}6}{2} = 1{,}92\) m².",
            ),
        ],
    ),
    tabel(
        "Juist of fout over de stelling van Pythagoras?",
        [
            ("Ze geldt enkel in een rechthoekige driehoek.", J),
            ("Met de omgekeerde stelling toon je aan dat een driehoek rechthoekig is.", J),
            ("Als je alle zijden verdubbelt, blijft een rechthoekige driehoek rechthoekig.", J),
            ("De schuine zijde kan korter zijn dan een rechthoekszijde.", F),
        ],
        "Vergroten met een factor geeft een gelijkvormige driehoek met dezelfde hoeken. De schuine zijde ligt tegenover de grootste hoek en is de langste.",
    ),
    mk(
        r"De afstand tussen \(P(2, -1)\) en \(Q(x, 3)\) is \(5\), en \(x\) is positief. Hoeveel is \(x\)?",
        [r"\(3\)", r"\(5\)", r"\(7\)", r"\(1\)"],
        1,
        r"\(\Delta y = 4\), dus \(\Delta x = 3\): \(x = 2 + 3 = 5\). Ook \(x = -1\) geeft afstand \(5\), maar dat is negatief.",
    ),
    sleep(
        "In een rechthoekige driehoek heten de twee zijden die de rechte hoek vormen de [[rechthoekszijden]]. De zijde tegenover de rechte hoek is de [[schuine zijde]], en die is altijd de [[langste]] zijde.",
        ["kortste", "hoogtelijn"],
        "De grootste hoek ligt tegenover de grootste zijde, en in een rechthoekige driehoek is de rechte hoek de grootste.",
    ),
    mk(
        r"Een televisiescherm in de verhouding \(16 : 9\) is \(80\) cm breed. Hoe lang is de diagonaal ongeveer?",
        [r"\(92\) cm", r"\(125\) cm", r"\(89\) cm", r"\(100\) cm"],
        0,
        r"De hoogte is \(80 \cdot \tfrac{9}{16} = 45\) cm. De diagonaal: \(\sqrt{6400 + 2025} = \sqrt{8425} \approx 91{,}8\) cm.",
    ),
    inv(
        r"Een rechthoek heeft een diagonaal van \(17\) cm en een zijde van \(8\) cm. Hoe groot is de omtrek, in cm?",
        ["46", "46 cm"],
        r"De andere zijde is \(\sqrt{289 - 64} = \sqrt{225} = 15\). Omtrek: \(2 \cdot (8 + 15) = 46\) cm.",
    ),
    koppel(
        "Koppel elke situatie aan de berekening die het antwoord geeft.",
        [
            ["ladder van 5 m, voet 3 m van de muur: hoogte", r"\(\sqrt{5^{2} - 3^{2}}\)"],
            ["rechthoekige tuin van 5 m op 3 m: diagonaal", r"\(\sqrt{5^{2} + 3^{2}}\)"],
            ["balk van 5 op 3 op 3: ruimtediagonaal", r"\(\sqrt{5^{2} + 3^{2} + 3^{2}}\)"],
            ["vierkant met zijde 5: diagonaal", r"\(5\sqrt{2}\)"],
        ],
        [r"\(5 + 3\)"],
        "Zoek je de schuine zijde, dan tel je de kwadraten op. Zoek je een rechthoekszijde, dan trek je af.",
    ),
    mk(
        r"Een vlieger hangt aan een touw van \(50\) m. Hij hangt recht boven een punt dat \(30\) m van jou ligt. Je houdt het touw op \(1{,}5\) m hoogte. Hoe hoog hangt de vlieger boven de grond?",
        [r"\(40\) m", r"\(41{,}5\) m", r"\(38{,}5\) m", r"\(58{,}3\) m"],
        1,
        r"\(\sqrt{50^{2} - 30^{2}} = 40\) m boven je hand, en je hand zit op \(1{,}5\) m: \(41{,}5\) m.",
    ),
    open_(
        r"Een driehoek heeft zijden \(10\), \(24\) en \(26\). Toon aan dat hij rechthoekig is en zeg waar de rechte hoek ligt.",
        r"\(10^{2} + 24^{2} = 100 + 576 = 676 = 26^{2}\). Volgens de omgekeerde stelling van Pythagoras is de driehoek rechthoekig. De rechte hoek ligt tegenover de langste zijde \(26\), dus tussen de zijden \(10\) en \(24\).",
    ),
    mk(
        r"Een cilindervormig blik is \(12\) cm hoog en heeft een diameter van \(5\) cm. Hoe lang mag een rietje hoogstens zijn om er helemaal in te passen?",
        [r"\(13\) cm", r"\(17\) cm", r"\(12{,}5\) cm", r"\(14\) cm"],
        0,
        r"Het langste rietje loopt schuin van onderaan de ene kant naar bovenaan de overkant: \(\sqrt{12^{2} + 5^{2}} = 13\) cm.",
    ),
    mk(
        r"In een rechthoekige driehoek zijn de rechthoekszijden \(x\) en \(2x\), en de schuine zijde is \(10\). Hoeveel is \(x\)?",
        [r"\(2\sqrt{5}\)", r"\(\sqrt{10}\)", r"\(\tfrac{10}{3}\)", r"\(5\)"],
        0,
        r"\(x^{2} + 4x^{2} = 100\), dus \(5x^{2} = 100\), \(x^{2} = 20\) en \(x = \sqrt{20} = 2\sqrt{5}\).",
    ),
    inv(
        r"Een fietser rijdt \(9\) km naar het noorden en daarna \(12\) km naar het oosten. Hoe ver is hij in vogelvlucht van zijn vertrekpunt, in km?",
        ["15", "15 km"],
        r"Noord en oost staan loodrecht op elkaar: \(\sqrt{81 + 144} = 15\) km.",
    ),
    mk(
        r"Hoe groot is de afstand tussen \(R(-3, 2)\) en \(S(3, -6)\)?",
        [r"\(2\)", r"\(10\)", r"\(14\)", r"\(\sqrt{20}\)"],
        1,
        r"\(\Delta x = 6\) en \(\Delta y = -8\). In het kwadraat valt het minteken weg: \(\sqrt{36 + 64} = 10\).",
    ),
    keuze(
        r"Een rechthoekige driehoek heeft rechthoekszijden \(1\) en \(2\). Zijn schuine zijde is [[*\(\sqrt{5}\)|\(3\)|\(\sqrt{3}\)]], en dat is ongeveer [[*\(2{,}24\)|\(1{,}73\)|\(2{,}5\)]].",
        r"\(1 + 4 = 5\), en \(\sqrt{5} \approx 2{,}236\). De schuine zijde is korter dan de som \(1 + 2 = 3\) van de andere twee.",
    ),
]
