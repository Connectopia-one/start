"""De rechthoekige driehoek oplossen en toepassen — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, DONKER, GROEN, LICHT

DRIEHOEK = "gonio-driehoek"
C, A, B = (200, 540), (820, 540), (200, 210)


def _driehoek():
    d = [f'<polygon points="{C[0]},{C[1]} {A[0]},{A[1]} {B[0]},{B[1]}" fill="{LICHT}" stroke="{DONKER}" stroke-width="4"/>',
         f'<polyline points="{C[0]},{C[1]-34} {C[0]+34},{C[1]-34} {C[0]+34},{C[1]}" fill="none" stroke="{DONKER}" stroke-width="3"/>',
         f'<path d="M {A[0]-70} {A[1]} A 70 70 0 0 0 {A[0]-62} {A[1]-33}" fill="none" stroke="#7a4b8c" stroke-width="4"/>']
    d += [s_tekst(C[0] - 26, C[1] + 30, "C", 28, vet=True), s_tekst(A[0] + 26, A[1] + 30, "A", 28, vet=True),
          s_tekst(B[0] - 26, B[1] - 8, "B", 28, vet=True), s_tekst(A[0] - 98, A[1] - 14, "α", 26, kleur="#7a4b8c", vet=True)]
    d += [s_tekst((A[0] + C[0]) / 2, C[1] + 40, "15 cm", 24, kleur=GROEN, vet=True),
          s_tekst(C[0] - 60, (B[1] + C[1]) / 2 + 8, "8 cm", 24, kleur=GROEN, vet=True),
          s_tekst((A[0] + B[0]) / 2 + 40, (A[1] + B[1]) / 2 - 16, "17 cm", 24, kleur=GROEN, vet=True)]
    return d


def _zijde(p, q):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    return pix_zone(mx - 60, my - 50, 120, 100)


GRAFIEKEN = [dict(naam=DRIEHOEK, titel="Rechthoekige driehoek ABC met de rechte hoek in C", eigen=_driehoek)]
PRENTEN = [dict(bestand=f"{DRIEHOEK}.svg", zelf=True, wat="rechthoekige driehoek met zijden 8, 15 en 17", vragen="klikvragen over overstaande en aanliggende zijde")]

VRAGEN = [
    klik(
        "Klik op de overstaande zijde van hoek α.",
        f"{DRIEHOEK}.svg",
        [_zijde(B, C)],
        "De overstaande zijde ligt tegenover de hoek en raakt hem niet: dat is BC.",
    ),
    klik(
        "Klik op de aanliggende rechthoekszijde van hoek B.",
        f"{DRIEHOEK}.svg",
        [_zijde(B, C)],
        "Bij hoek B liggen twee zijden: BC en BA. BA is de schuine zijde, dus de aanliggende rechthoekszijde is BC. Voor hoek A is diezelfde zijde net de overstaande.",
    ),
    met_prent(f"{DRIEHOEK}.svg", koppel(
        "Koppel elk goniometrisch getal aan zijn waarde in deze driehoek.",
        [
            [r"\(\sin\alpha\)", r"\(\tfrac{8}{17}\)"],
            [r"\(\cos\alpha\)", r"\(\tfrac{15}{17}\)"],
            [r"\(\tan\alpha\)", r"\(\tfrac{8}{15}\)"],
            [r"\(\tan \hat{B}\)", r"\(\tfrac{15}{8}\)"],
        ],
        [r"\(\tfrac{17}{8}\)"],
        r"Sinus: overstaande op schuine zijde. Cosinus: aanliggende op schuine zijde. Tangens: overstaande op aanliggende. Voor hoek B wisselen overstaand en aanliggend van plaats.",
    )),
    met_prent(f"{DRIEHOEK}.svg", mk(
        "Hoe groot is α, afgerond op een graad?",
        [r"\(28^{\circ}\)", r"\(62^{\circ}\)", r"\(32^{\circ}\)", r"\(25^{\circ}\)"],
        0,
        r"\(\tan\alpha = \tfrac{8}{15}\), dus \(\alpha = \tan^{-1}\tfrac{8}{15} \approx 28{,}07^{\circ}\). \(62^{\circ}\) is hoek B.",
    )),
    met_prent(f"{DRIEHOEK}.svg", tabel(
        "Juist of fout over deze driehoek?",
        [
            (r"\(\sin\alpha = \cos \hat{B}\)", J),
            (r"\(\sin^{2}\alpha + \cos^{2}\alpha = 1\)", J),
            (r"\(\tan\alpha \cdot \tan \hat{B} = 1\)", J),
            (r"\(\sin\alpha + \cos\alpha = 1\)", F),
        ],
        r"\(\tfrac{8}{17}\) is zowel \(\sin\alpha\) als \(\cos \hat{B}\). \(\tfrac{64 + 225}{289} = 1\). \(\tfrac{8}{15} \cdot \tfrac{15}{8} = 1\). Maar \(\tfrac{8}{17} + \tfrac{15}{17} = \tfrac{23}{17}\).",
    )),
    casus(
        r"Je staat \(20\) m van de voet van een gebouw. Je kijkt naar de top onder een kijkhoek van \(35^{\circ}\). Je ogen zitten op \(1{,}6\) m hoogte.",
        [
            mk(
                "Welke berekening geeft de hoogte van het gebouw boven je ooghoogte?",
                [r"\(20 \cdot \sin 35^{\circ}\)", r"\(\dfrac{20}{\tan 35^{\circ}}\)", r"\(20 \cdot \tan 35^{\circ}\)", r"\(\dfrac{20}{\cos 35^{\circ}}\)"],
                2,
                r"Je kent de aanliggende zijde (\(20\) m) en zoekt de overstaande: \(\tan 35^{\circ} = \tfrac{h}{20}\).",
            ),
            inv(
                "Hoe hoog is het gebouw in totaal? Rond af op een decimaal, in meter.",
                ["15,6", "15,6 m", "15.6"],
                r"\(20 \cdot \tan 35^{\circ} \approx 14{,}00\) m, plus \(1{,}6\) m ooghoogte: \(15{,}6\) m.",
            ),
        ],
    ),
    mk(
        r"Een ladder van \(4\) m staat tegen een muur en maakt een hoek van \(75^{\circ}\) met de grond. Hoe ver staat de voet van de muur, afgerond op een cm?",
        [r"\(3{,}86\) m", r"\(1{,}04\) m", r"\(1{,}07\) m", r"\(14{,}93\) m"],
        1,
        r"De afstand tot de muur is de aanliggende zijde: \(4 \cdot \cos 75^{\circ} \approx 1{,}04\) m. \(3{,}86\) m is de hoogte tegen de muur.",
    ),
    koppel(
        "Je kent twee gegevens in een rechthoekige driehoek en zoekt een derde. Koppel aan wat je moet gebruiken.",
        [
            ["hoek en schuine zijde gekend, overstaande zijde gezocht", "sinus"],
            ["hoek en schuine zijde gekend, aanliggende zijde gezocht", "cosinus"],
            ["hoek en aanliggende zijde gekend, overstaande zijde gezocht", "tangens"],
            ["twee rechthoekszijden gekend, schuine zijde gezocht", "stelling van Pythagoras"],
        ],
        ["som van de hoeken"],
        "Kies het verband dat de twee gekende stukken en het gezochte stuk samen bevat.",
    ),
    mk(
        r"Een oprit moet \(30\) cm hoogte overbruggen en mag hoogstens \(6\%\) hellen. Hoe lang moet de oprit horizontaal minstens zijn?",
        [r"\(1{,}8\) m", r"\(5\) m", r"\(18\) m", r"\(50\) cm"],
        1,
        r"\(6\%\) betekent \(6\) cm stijgen per \(100\) cm horizontaal: \(\tfrac{30}{0{,}06} = 500\) cm \(= 5\) m.",
    ),
    tabel(
        "Juist of fout over hellingen?",
        [
            (r"Een helling van \(12\%\) heeft een hellingshoek van ongeveer \(6{,}8^{\circ}\).", J),
            (r"Een helling van \(50\%\) heeft een hellingshoek van \(45^{\circ}\).", F),
            ("Het hellingspercentage is de tangens van de hellingshoek, maal 100.", J),
            (r"Een helling van \(200\%\) bestaat niet.", F),
        ],
        r"\(\tan^{-1} 0{,}12 \approx 6{,}8^{\circ}\). Bij \(45^{\circ}\) hoort \(100\%\). Een helling van \(200\%\) stijgt \(2\) m per meter: steil, maar het bestaat (ongeveer \(63^{\circ}\)).",
    ),
    inv(
        r"Een fietser rijdt \(250\) m langs een weg die onder \(4^{\circ}\) stijgt. Hoeveel meter hoogte wint hij? Rond af op een meter.",
        ["17", "17 m"],
        r"De afgelegde weg is de schuine zijde, de hoogte de overstaande: \(250 \cdot \sin 4^{\circ} \approx 17{,}4\) m.",
    ),
    volgorde(
        r"Je lost een rechthoekige driehoek op met \(\hat{C} = 90^{\circ}\), \(\hat{A} = 40^{\circ}\) en \(BC = 5\). Zet de stappen in een logische volgorde.",
        [
            "een schets maken en aanduiden wat gegeven is",
            r"\(\hat{B} = 90^{\circ} - 40^{\circ} = 50^{\circ}\) berekenen",
            r"\(AB = \dfrac{5}{\sin 40^{\circ}} \approx 7{,}78\) berekenen",
            r"\(AC = \dfrac{5}{\tan 40^{\circ}} \approx 5{,}96\) berekenen",
            r"controleren met Pythagoras: \(5^{2} + 5{,}96^{2} \approx 7{,}78^{2}\)",
        ],
        "Eerst de schets, dan de hoeken, dan de zijden, en tot slot een controle met een ander verband.",
    ),
    mk(
        r"\(\cos\alpha = 0{,}6\) en \(\alpha\) is scherp. Hoeveel is \(\tan\alpha\)?",
        [r"\(0{,}75\)", r"\(\tfrac{4}{3}\)", r"\(0{,}8\)", r"\(\tfrac{3}{5}\)"],
        1,
        r"Met de grondformule: \(\sin\alpha = \sqrt{1 - 0{,}36} = 0{,}8\). Dan \(\tan\alpha = \tfrac{0{,}8}{0{,}6} = \tfrac{4}{3}\).",
    ),
    sorteer(
        "Kan dit getal de sinus of cosinus van een scherpe hoek zijn?",
        ["Kan", "Kan niet"],
        [
            [r"\(0{,}99\)", "Kan"],
            [r"\(1{,}2\)", "Kan niet"],
            [r"\(\tfrac{\sqrt{3}}{2}\)", "Kan"],
            [r"\(-0{,}3\)", "Kan niet"],
            [r"\(\tfrac{5}{4}\)", "Kan niet"],
            [r"\(0{,}01\)", "Kan"],
        ],
        "Sinus en cosinus van een scherpe hoek liggen strikt tussen 0 en 1: de rechthoekszijde is altijd korter dan de schuine zijde, en lengtes zijn positief.",
    ),
    keuze(
        r"Hoe groter een scherpe hoek, hoe [[*groter|kleiner]] zijn sinus, hoe [[*kleiner|groter]] zijn cosinus en hoe [[*groter|kleiner]] zijn tangens.",
        r"Bij een steilere hoek groeit de overstaande zijde en krimpt de aanliggende zijde, bij een vaste schuine zijde.",
    ),
    mk(
        r"Een dak is \(6\) m breed en de nok ligt \(2\) m boven de dakgoot, precies in het midden. Hoe groot is de dakhelling, afgerond op een graad?",
        [r"\(18^{\circ}\)", r"\(34^{\circ}\)", r"\(42^{\circ}\)", r"\(19^{\circ}\)"],
        1,
        r"Halve breedte \(3\) m, hoogte \(2\) m: \(\tan^{-1}\tfrac{2}{3} \approx 33{,}7^{\circ}\). Wie de hele breedte neemt, vindt \(\tan^{-1}\tfrac{2}{6} \approx 18^{\circ}\).",
    ),
    casus(
        r"Vanaf een punt op de grond kijk je naar de voet en de top van een vlaggenmast op het dak van een gebouw. Je staat \(30\) m van het gebouw. De voet van de mast zie je onder \(28^{\circ}\), de top onder \(41^{\circ}\). Laat je ooghoogte weg.",
        [
            mk(
                "Hoe hoog is het gebouw, afgerond op een decimeter?",
                [r"\(14{,}1\) m", r"\(16{,}0\) m", r"\(26{,}1\) m", r"\(15{,}0\) m"],
                1,
                r"\(30 \cdot \tan 28^{\circ} \approx 15{,}95\) m.",
            ),
            inv(
                "Hoe lang is de vlaggenmast? Rond af op een meter.",
                ["10", "10 m"],
                r"De top: \(30 \cdot \tan 41^{\circ} \approx 26{,}08\) m. De mast: \(26{,}08 - 15{,}95 \approx 10{,}1\) m. Het verschil van de hoeken (\(13^{\circ}\)) mag je niet zomaar gebruiken.",
            ),
        ],
    ),
    tabel(
        "Juist of fout over de rechthoekige driehoek?",
        [
            ("Met één zijde en één scherpe hoek kan je de hele driehoek oplossen.", J),
            ("Met enkel de drie hoeken kan je de zijden berekenen.", F),
            ("De twee scherpe hoeken zijn samen 90°.", J),
            ("Je kan een scherpe hoek van 95° uitkomen als je juist rekent.", F),
        ],
        "Uit de hoeken alleen ken je de vorm, niet de grootte: er zijn oneindig veel gelijkvormige driehoeken. Een scherpe hoek is kleiner dan 90°.",
    ),
    mk(
        r"Een vlieger hangt aan \(60\) m touw. Het touw maakt een hoek van \(50^{\circ}\) met de grond. Hoe hoog hangt de vlieger boven je hand?",
        [r"\(38{,}6\) m", r"\(46\) m", r"\(71{,}5\) m", r"\(50\) m"],
        1,
        r"\(60 \cdot \sin 50^{\circ} \approx 45{,}96\) m. \(38{,}6\) m is \(60 \cdot \cos 50^{\circ}\): de horizontale afstand.",
    ),
    inv(
        r"Een loopband in een luchthaven is \(12\) m lang horizontaal gemeten en loopt onder \(25^{\circ}\) omhoog. Hoe lang is de band zelf? Rond af op een decimaal, in meter.",
        ["13,2", "13,2 m", "13.2"],
        r"De horizontale lengte is de aanliggende zijde: \(\dfrac{12}{\cos 25^{\circ}} \approx 13{,}24\) m.",
    ),
    sleep(
        r"Als je \(\sin\alpha\) kent en \(\alpha\) zoekt, gebruik je de [[inverse sinus]] op je rekentoestel. Voor je begint, kijk je na of het toestel op [[graden]] staat.",
        ["radialen", "inverse tangens"],
        r"De inverse sinus (\(\sin^{-1}\)) geeft de hoek bij een gegeven sinus. Staat het toestel op radialen, dan krijg je een ander getal.",
    ),
    mk(
        r"Een gelijkbenige driehoek heeft een basis van \(10\) cm en basishoeken van \(70^{\circ}\). Hoe hoog is hij, afgerond op een mm?",
        [r"\(13{,}7\) cm", r"\(27{,}5\) cm", r"\(4{,}7\) cm", r"\(1{,}8\) cm"],
        0,
        r"De hoogte deelt de driehoek in twee rechthoekige driehoeken met aanliggende zijde \(5\) cm: \(5 \cdot \tan 70^{\circ} \approx 13{,}7\) cm.",
    ),
    open_(
        r"Leg uit waarom \(\sin 30^{\circ} = 0{,}5\) geldt in elke rechthoekige driehoek met een hoek van \(30^{\circ}\), groot of klein.",
        r"Alle rechthoekige driehoeken met een hoek van \(30^{\circ}\) hebben dezelfde hoeken (\(90^{\circ}\), \(30^{\circ}\), \(60^{\circ}\)) en zijn dus gelijkvormig. Dan zijn de verhoudingen van de zijden overal gelijk, ook de verhouding van overstaande zijde op schuine zijde.",
    ),
    mk(
        r"Welke berekening geeft de schuine zijde als je een hoek van \(32^{\circ}\) en de aanliggende rechthoekszijde \(9\) kent?",
        [r"\(9 \cdot \cos 32^{\circ}\)", r"\(\dfrac{9}{\cos 32^{\circ}}\)", r"\(\dfrac{9}{\sin 32^{\circ}}\)", r"\(9 \cdot \tan 32^{\circ}\)"],
        1,
        r"\(\cos 32^{\circ} = \tfrac{9}{\text{schuine zijde}}\), dus schuine zijde \(= \tfrac{9}{\cos 32^{\circ}} \approx 10{,}6\).",
    ),
    inv(
        r"Een boom werpt een schaduw van \(18\) m als de zon \(30^{\circ}\) boven de horizon staat. Hoe hoog is de boom? Rond af op een decimaal, in meter.",
        ["10,4", "10,4 m", "10.4"],
        r"\(18 \cdot \tan 30^{\circ} \approx 10{,}39\) m.",
    ),
    inv(
        r"In een rechthoekige driehoek is de schuine zijde \(26\) cm en geldt \(\sin\alpha = \tfrac{5}{13}\). Hoe lang is de zijde tegenover \(\alpha\), in cm?",
        ["10", "10 cm"],
        r"\(\sin\alpha = \tfrac{\text{overstaande}}{26} = \tfrac{5}{13}\), dus de overstaande zijde is \(26 \cdot \tfrac{5}{13} = 10\) cm.",
    ),
    keuze(
        r"In een rechthoekige driehoek met scherpe hoeken van \(30^{\circ}\) en \(60^{\circ}\) is \(\sin 30^{\circ}\) gelijk aan [[*\(\cos 60^{\circ}\)|\(\cos 30^{\circ}\)|\(\tan 60^{\circ}\)]], want de overstaande zijde van de ene hoek is de [[*aanliggende|schuine|overstaande]] zijde van de andere.",
        r"Twee complementaire hoeken wisselen overstaand en aanliggend: \(\sin\alpha = \cos(90^{\circ} - \alpha)\).",
    ),
    mk(
        r"Een weg stijgt onder een hoek van \(5^{\circ}\). Welk hellingspercentage hoort daarbij?",
        [r"\(5\%\)", r"\(8{,}7\%\)", r"\(0{,}09\%\)", r"\(11{,}1\%\)"],
        1,
        r"Het hellingspercentage is \(\tan 5^{\circ} \cdot 100 \approx 8{,}7\%\). Hoek en percentage zijn niet hetzelfde getal.",
    ),
]
