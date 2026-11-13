"""Telproblemen met boom- en venndiagram — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, kansboom, DONKER, GROEN

VENN = "tellen-venndiagram-klas"
BOOM = "tellen-boomdiagram-ijsje"


def _venn():
    d = [s_vak(60, 70, 880, 520, vul="#fffdf7", rand=DONKER, dikte=3, rond=20),
         s_tekst(110, 110, "Klas van 30", 22, anker="start", vet=True),
         '<circle cx="390" cy="340" r="190" fill="#3b6fa0" fill-opacity="0.18" stroke="#3b6fa0" stroke-width="4"/>',
         '<circle cx="610" cy="340" r="190" fill="#b5651d" fill-opacity="0.18" stroke="#b5651d" stroke-width="4"/>',
         s_tekst(300, 140, "Sport", 26, kleur="#3b6fa0", vet=True),
         s_tekst(700, 140, "Muziek", 26, kleur="#b5651d", vet=True),
         s_tekst(300, 350, "12", 34, vet=True), s_tekst(500, 350, "5", 34, vet=True),
         s_tekst(700, 350, "8", 34, vet=True), s_tekst(870, 550, "5", 34, vet=True)]
    return d


_B, _M, _K = kansboom(
    (90, 340),
    [("hoorntje", "", (420, 185)), ("potje", "", (420, 495))],
    {
        "hoorntje": [("vanille", "", (800, 85)), ("chocolade", "", (800, 185)), ("aardbei", "", (800, 285))],
        "potje": [("vanille", "", (800, 395)), ("chocolade", "", (800, 495)), ("aardbei", "", (800, 595))],
    },
)

GRAFIEKEN = [
    dict(naam=VENN, titel="Wie doet aan sport en wie aan muziek?", eigen=_venn),
    dict(naam=BOOM, titel="Een ijsje kiezen", eigen=lambda: _B),
]
PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over venn- en boomdiagram") for g in GRAFIEKEN]


def _knoop(k):
    x, y = _K[k]
    return pix_zone(x - 65, y - 30, 130, 60)


VRAGEN = [
    klik(
        "Klik op het gebied van de leerlingen die wel muziek doen, maar geen sport.",
        f"{VENN}.svg",
        [pix_zone(640, 200, 150, 280)],
        "Enkel muziek: het stuk van de rechterkring dat niet overlapt met de linkerkring. Daar staan 8 leerlingen.",
    ),
    klik(
        "Klik op het gebied van de leerlingen die geen van beide doen.",
        f"{VENN}.svg",
        [pix_zone(800, 500, 130, 85), pix_zone(70, 480, 130, 105), pix_zone(800, 75, 135, 90)],
        "Wie aan geen enkele voorwaarde voldoet, staat buiten beide kringen, binnen de rechthoek van de hele klas.",
    ),
    met_prent(f"{VENN}.svg", tabel(
        "Juist of fout volgens het venndiagram?",
        [
            ("17 leerlingen doen aan sport.", J),
            ("13 leerlingen doen aan muziek.", J),
            ("25 leerlingen doen minstens één van de twee.", J),
            ("20 leerlingen doen precies één van de twee.", J),
            ("10 leerlingen doen geen sport.", F),
        ],
        r"Sport: \(12 + 5 = 17\). Muziek: \(5 + 8 = 13\). Minstens één: \(12 + 5 + 8 = 25\). Precies één: \(12 + 8 = 20\). Geen sport: \(8 + 5 = 13\).",
    )),
    met_prent(f"{VENN}.svg", mk(
        "Hoeveel leerlingen doen niet aan muziek?",
        [r"\(12\)", r"\(17\)", r"\(22\)", r"\(5\)"],
        1,
        r"Complementregel: \(30 - 13 = 17\). Of zo: \(12\) enkel sport plus \(5\) die niets doen.",
    )),
    klik(
        "Klik op het einde van het pad 'potje met aardbei'.",
        f"{BOOM}.svg",
        [_knoop(("potje", "aardbei"))],
        "Een pad loopt van het beginpunt over 'potje' naar 'aardbei'. Elk eindpunt is één uitkomst.",
    ),
    met_prent(f"{BOOM}.svg", inv(
        "Hoeveel verschillende ijsjes met één bol kan je kiezen?",
        ["6", "zes"],
        r"Productregel: \(2\) keuzes voor de houder maal \(3\) smaken \(= 6\) paden.",
    )),
    met_prent(f"{BOOM}.svg", mk(
        "Er komt een vierde smaak bij, en je mag ook een wafeltje als houder kiezen. Hoeveel ijsjes met één bol zijn er dan?",
        [r"\(7\)", r"\(9\)", r"\(12\)", r"\(24\)"],
        2,
        r"\(3\) houders maal \(4\) smaken \(= 12\). Je telt niet op maar vermenigvuldigt.",
    )),
    mk(
        r"Een code bestaat uit \(2\) letters (A tot Z) gevolgd door \(3\) cijfers. Hoeveel codes zijn er?",
        [r"\(676\,000\)", r"\(26\,000\)", r"\(52\,000\)", r"\(1\,757\,600\)"],
        0,
        r"\(26 \cdot 26 \cdot 10 \cdot 10 \cdot 10 = 676\,000\).",
    ),
    mk(
        r"Acht lopers doen mee aan een finale. Hoeveel verschillende podia (goud, zilver, brons) zijn mogelijk?",
        [r"\(24\)", r"\(56\)", r"\(336\)", r"\(512\)"],
        2,
        r"Zonder terugleggen: \(8\) kandidaten voor goud, dan \(7\), dan \(6\): \(8 \cdot 7 \cdot 6 = 336\). \(512 = 8^{3}\) zou betekenen dat iemand twee medailles kan winnen.",
    ),
    sorteer(
        "Met of zonder herhaling?",
        ["met herhaling: telkens evenveel keuzes", "zonder herhaling: telkens één keuze minder"],
        [
            ["een pincode van 4 cijfers", "met herhaling: telkens evenveel keuzes"],
            ["een klassenvoorzitter en een secretaris kiezen", "zonder herhaling: telkens één keuze minder"],
            ["drie keer gooien met een dobbelsteen", "met herhaling: telkens evenveel keuzes"],
            ["5 boeken naast elkaar op een plank zetten", "zonder herhaling: telkens één keuze minder"],
            ["een kaart trekken, ze niet terugleggen en nog een trekken", "zonder herhaling: telkens één keuze minder"],
        ],
        "Kan dezelfde keuze opnieuw, dan blijft het aantal keuzes gelijk. Wie al gekozen is, of wat al op de plank staat, valt weg.",
    ),
    inv(
        r"Op hoeveel manieren kan je \(5\) boeken naast elkaar op een plank zetten?",
        ["120"],
        r"\(5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120\).",
    ),
    casus(
        r"Van \(120\) leerlingen gaan er \(70\) met de fiets naar school, \(45\) met de bus en \(15\) soms met de fiets en soms met de bus.",
        [
            inv(
                "Hoeveel leerlingen gebruiken minstens één van de twee?",
                ["100"],
                r"Somregel: \(70 + 45 - 15 = 100\). Wie allebei doet, tel je anders twee keer.",
            ),
            mk(
                "Hoeveel leerlingen nemen enkel de bus?",
                [r"\(45\)", r"\(30\)", r"\(55\)", r"\(15\)"],
                1,
                r"Van de \(45\) busleerlingen nemen er \(15\) ook de fiets: \(45 - 15 = 30\).",
            ),
            inv(
                "Hoeveel leerlingen gebruiken geen van beide?",
                ["20"],
                r"Complementregel: \(120 - 100 = 20\).",
            ),
        ],
    ),
    mk(
        r"Hoeveel getallen van \(1\) tot en met \(60\) zijn deelbaar door \(4\) of door \(6\)?",
        [r"\(25\)", r"\(20\)", r"\(15\)", r"\(30\)"],
        1,
        r"Door \(4\): \(15\). Door \(6\): \(10\). Door allebei, dus door \(12\): \(5\). Somregel: \(15 + 10 - 5 = 20\).",
    ),
    keuze(
        "Bij opeenvolgende keuzes gebruik je de [[*productregel|somregel|complementregel]]. Bij twee groepen die overlappen, gebruik je de [[*somregel|productregel]] en trek je de [[*doorsnede|unie|rest]] één keer af.",
        "Opeenvolgende stappen vermenigvuldigen; groepen samennemen optellen, zonder dubbel te tellen.",
    ),
    casus(
        r"Je bekijkt alle getallen van drie cijfers, van \(100\) tot en met \(999\).",
        [
            mk(
                r"Hoeveel ervan hebben geen enkel cijfer \(7\)?",
                [r"\(729\)", r"\(648\)", r"\(900\)", r"\(504\)"],
                1,
                r"Eerste cijfer: \(1\) tot \(9\) zonder \(7\), dus \(8\) keuzes. Tweede en derde: \(0\) tot \(9\) zonder \(7\), elk \(9\). \(8 \cdot 9 \cdot 9 = 648\).",
            ),
            inv(
                r"Hoeveel ervan hebben minstens één cijfer \(7\)?",
                ["252"],
                r"Er zijn \(900\) getallen van drie cijfers. Complement: \(900 - 648 = 252\).",
            ),
        ],
    ),
    tabel(
        "Juist of fout over telproblemen?",
        [
            ("Bij een boomdiagram tel je de eindpunten van de paden.", J),
            ("Twee disjuncte groepen mag je gewoon optellen.", J),
            ("Een venndiagram toont het best keuzes die na elkaar komen.", F),
            ("De complementregel helpt als 'minstens één' moeilijk rechtstreeks te tellen is.", J),
        ],
        "Een venndiagram toont groepen en hun overlap; voor stappen na elkaar is een boomdiagram of de productregel geschikter.",
    ),
    mk(
        r"Je gooit drie keer met een munt. In hoeveel van de uitkomsten valt er minstens één keer kop?",
        [r"\(3\)", r"\(4\)", r"\(6\)", r"\(7\)"],
        3,
        r"Er zijn \(2^{3} = 8\) uitkomsten. Enkel 'munt, munt, munt' heeft geen kop: \(8 - 1 = 7\).",
    ),
    volgorde(
        r"Van \(32\) leerlingen spelen er \(15\) een instrument, \(20\) sporten er en \(6\) doen geen van beide. Je zoekt hoeveel er allebei doen. Zet de stappen in volgorde.",
        [
            r"wie minstens één doet: \(32 - 6 = 26\)",
            r"de twee groepen optellen: \(15 + 20 = 35\)",
            r"het verschil is de doorsnede: \(35 - 26 = 9\)",
            r"invullen in een venndiagram: \(6\), \(9\), \(11\) en \(6\)",
        ],
        "Wie in beide groepen zit, tel je bij het optellen twee keer: het overschot boven de echte vereniging is de doorsnede.",
    ),
    mk(
        r"Een restaurant heeft \(4\) voorgerechten, \(5\) hoofdgerechten en \(3\) desserts. Een menu heeft een hoofdgerecht en daarnaast een voorgerecht of een dessert, niet allebei. Hoeveel menu's zijn er?",
        [r"\(60\)", r"\(35\)", r"\(12\)", r"\(27\)"],
        1,
        r"Hoofdgerecht met voorgerecht: \(5 \cdot 4 = 20\). Hoofdgerecht met dessert: \(5 \cdot 3 = 15\). Die twee groepen zijn disjunct: \(20 + 15 = 35\).",
    ),
    sleep(
        "Twee groepen die niets gemeen hebben, noem je [[disjunct]]. Hun [[doorsnede]] is leeg, en het aantal in de [[unie]] is de som van beide groepen.",
        ["complement", "deelverzameling"],
        "Is de doorsnede leeg, dan tel je niemand dubbel.",
    ),
    open_(
        r"Een leerling zegt: 'In een klas van \(25\) doen \(14\) aan voetbal en \(16\) aan zwemmen, dus \(30\) leerlingen sporten.' Leg uit wat er mis is en wat je minstens kan besluiten.",
        r"Er zijn maar \(25\) leerlingen, dus minstens \(14 + 16 - 25 = 5\) leerlingen doen allebei. Die tel je bij het optellen twee keer. Het juiste aantal sporters is \(30\) min de doorsnede, en dat is hoogstens \(25\).",
    ),
    mk(
        r"Een wachtwoord bestaat uit \(4\) tekens, elk een cijfer of een kleine letter (a tot z). Hoeveel wachtwoorden zijn er?",
        [r"\(36^{4}\)", r"\(4^{36}\)", r"\(10^{4} + 26^{4}\)", r"\(36 \cdot 4\)"],
        0,
        r"Per teken \(10 + 26 = 36\) keuzes, en dat vier keer na elkaar: \(36^{4} = 1\,679\,616\).",
    ),
    inv(
        r"Op een feest geeft elk van de \(8\) gasten elke andere gast één keer een hand. Hoeveel handdrukken zijn er?",
        ["28"],
        r"Elke gast geeft \(7\) handen: \(8 \cdot 7 = 56\). Zo tel je elke handdruk twee keer, dus \(56 : 2 = 28\).",
    ),
    met_prent(f"{VENN}.svg", mk(
        "Hoeveel procent van de klas doet zowel sport als muziek, afgerond op een tiende?",
        [r"\(5\%\)", r"\(16{,}7\%\)", r"\(38{,}5\%\)", r"\(29{,}4\%\)"],
        1,
        r"\(\tfrac{5}{30} \approx 0{,}167\). Wie deelt door \(13\) of \(17\), neemt een deelgroep in plaats van de hele klas.",
    )),
    inv(
        r"Een fietsslot heeft drie ringen met de cijfers \(0\) tot \(9\). Je weet dat het eerste cijfer even is en dat de code geen twee dezelfde cijfers heeft. Hoeveel codes moet je hoogstens proberen?",
        ["360"],
        r"Eerste cijfer: \(0, 2, 4, 6\) of \(8\), dus \(5\) keuzes. Dan \(9\) en \(8\) keuzes voor de andere: \(5 \cdot 9 \cdot 8 = 360\).",
    ),
    keuze(
        r"Je gooit vier keer met een munt. Een boomdiagram heeft dan [[*\(16\)|\(8\)|\(4\)]] paden. Bij één worp met een dobbelsteen en één met een munt zijn het er [[*\(12\)|\(8\)|\(36\)]].",
        r"\(2^{4} = 16\) en \(6 \cdot 2 = 12\).",
    ),
    mk(
        r"Een klas van \(20\) leerlingen kiest een voorzitter en een secretaris, twee verschillende leerlingen. Op hoeveel manieren kan dat?",
        [r"\(190\)", r"\(380\)", r"\(400\)", r"\(39\)"],
        1,
        r"\(20\) keuzes voor voorzitter, daarna \(19\) voor secretaris: \(380\). De volgorde telt, want de functies verschillen. \(190\) zou kloppen voor twee gelijke functies.",
    ),
]
