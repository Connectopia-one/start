"""Telproblemen met boom- en venndiagram — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import s_tekst, s_vak, pix_zone, DONKER

VENN = "tellen-venn-do"
GETAL = {"enkel S": (300, 340, "9"), "S en M": (500, 340, "6"), "enkel M": (700, 340, "8"), "geen": (880, 560, "7")}


def _venn():
    d = [s_vak(80, 70, 860, 530, vul="#fffdf7", rond=16),
         s_tekst(130, 110, "klas: 30", 22, anker="start", vet=True),
         '<circle cx="390" cy="340" r="200" fill="#2f4a22" fill-opacity="0.12" stroke="#2f4a22" stroke-width="4"/>',
         '<circle cx="610" cy="340" r="200" fill="#7a4b8c" fill-opacity="0.12" stroke="#7a4b8c" stroke-width="4"/>',
         s_tekst(260, 165, "sportclub (S)", 24, kleur="#2f4a22", vet=True),
         s_tekst(740, 165, "muziekschool (M)", 24, kleur="#7a4b8c", vet=True)]
    for x, y, t in GETAL.values():
        d.append(s_tekst(x, y + 14, t, 44, kleur=DONKER, vet=True))
    return d


def _zone(k):
    x, y, _ = GETAL[k]
    return pix_zone(x - 50, y - 40, 100, 80)


GRAFIEKEN = [dict(naam=VENN, titel="Wie zit in de sportclub, wie in de muziekschool?", eigen=_venn)]
PRENTEN = [dict(bestand=f"{VENN}.svg", zelf=True, wat="venndiagram van een klas van 30 met sportclub en muziekschool", vragen="klikvragen en rekenvragen met de somregel")]

VRAGEN = [
    klik(
        "Klik op het getal dat zegt hoeveel leerlingen in de sportclub én in de muziekschool zitten.",
        f"{VENN}.svg",
        [_zone("S en M")],
        "Wie in allebei zit, staat in de doorsnede: het stuk waar de cirkels overlappen.",
    ),
    klik(
        "Klik op het getal van de leerlingen die in geen van beide zitten.",
        f"{VENN}.svg",
        [_zone("geen")],
        "Buiten de twee cirkels, maar binnen de rechthoek van de klas.",
    ),
    klik(
        "Klik op het getal van de leerlingen die wel muziekschool volgen maar niet sporten.",
        f"{VENN}.svg",
        [_zone("enkel M")],
        "Enkel M: in de rechtercirkel, buiten de overlapping.",
    ),
    met_prent(f"{VENN}.svg", tabel(
        "Kijk naar het venndiagram. Hoeveel leerlingen?",
        [("in de sportclub", "15"), ("in de muziekschool", "14"), ("in minstens één van beide", "23"), ("in precies één van beide", "17")],
        r"Sportclub \(9 + 6 = 15\), muziekschool \(6 + 8 = 14\). Minstens één: \(15 + 14 - 6 = 23\). Precies één: \(9 + 8 = 17\).",
        kolommen=["15", "14", "23", "17"],
    )),
    met_prent(f"{VENN}.svg", tabel(
        "Kijk naar het venndiagram. Juist of fout?",
        [("Er zitten 29 leerlingen in de sportclub of de muziekschool.", F),
         ("Meer dan de helft van de klas sport.", F),
         ("Zeven leerlingen volgen geen van beide.", J),
         ("Van wie muziekschool volgt, sport minder dan de helft.", J)],
        r"\(15 + 14 = 29\) telt de \(6\) dubbel. \(15\) van \(30\) is precies de helft, niet meer. Van de \(14\) muzikanten sporten er \(6\).",
        kolommen=["Juist", "Fout"],
    )),
    mk(
        "Een code bestaat uit twee letters (A tot Z) gevolgd door drie cijfers. Hoeveel codes zijn er?",
        ["676 000", "26 000", "67 600", "17 576 000"],
        0,
        r"\(26 \cdot 26 \cdot 10 \cdot 10 \cdot 10 = 676\,000\).",
    ),
    mk(
        "Acht lopers doen mee aan een finale. Hoeveel verschillende podiums (goud, zilver, brons) zijn er?",
        ["336", "512", "24", "56"],
        0,
        r"\(8 \cdot 7 \cdot 6 = 336\). Wie goud heeft, kan geen zilver meer winnen.",
    ),
    inv(
        "Hoeveel codes van vier cijfers (0 tot 9) bestaan er waarin geen enkel cijfer twee keer voorkomt?",
        ["5040", "5 040"],
        r"\(10 \cdot 9 \cdot 8 \cdot 7 = 5040\).",
    ),
    casus(
        "Een pizzeria biedt 3 soorten deeg, 5 sauzen en je kiest wel of geen extra kaas.",
        [
            inv("Hoeveel verschillende pizza's kun je samenstellen?", ["30"], r"\(3 \cdot 5 \cdot 2 = 30\)."),
            mk("Hoeveel paden heeft het boomdiagram?", ["10", "30", "15", "60"], 1, "Elk pad is één pizza."),
            mk("Hoeveel takken vertrekken uit het beginpunt?", ["3", "5", "2", "30"], 0, "De eerste keuze is het deeg: drie soorten."),
        ],
    ),
    sorteer(
        "Met of zonder terugleggen?",
        ["Met terugleggen", "Zonder terugleggen"],
        [("een pincode waarin cijfers mogen herhalen", "Met terugleggen"),
         ("een voorzitter en een secretaris kiezen uit een klas", "Zonder terugleggen"),
         ("drie keer met een dobbelsteen gooien", "Met terugleggen"),
         ("vijf kaarten na elkaar uit een spel trekken en ze houden", "Zonder terugleggen"),
         ("de volgorde van aankomst van zes lopers", "Zonder terugleggen")],
        "Zonder terugleggen: wat gekozen is, kan niet nog eens. Dan daalt het aantal keuzes per stap.",
    ),
    inv(
        "Hoeveel getallen van 1 tot en met 100 zijn deelbaar door 3 of door 5?",
        ["47"],
        r"\(33\) veelvouden van \(3\), \(20\) van \(5\), \(6\) van \(15\). \(33 + 20 - 6 = 47\).",
    ),
    mk(
        "Hoeveel getallen van 1 tot en met 50 zijn niet deelbaar door 4?",
        ["38", "12", "46", "37"],
        0,
        r"Er zijn \(12\) veelvouden van \(4\) tot \(50\). Complementregel: \(50 - 12 = 38\).",
    ),
    tabel(
        "Juist of fout over tellen?",
        [("Je gooit vier keer met een munt: er zijn 16 uitkomsten.", J),
         ("Uit 5 truien en 5 broeken kun je 10 combinaties maken.", F),
         ("Een fietsslot met 3 schijven van 0 tot 9 heeft 999 codes.", F),
         ("Bij twee dobbelstenen geeft som 12 maar één uitkomst.", J),
         ("Bij twee dobbelstenen komt som 2 even vaak voor als som 7.", F)],
        r"\(5 \cdot 5 = 25\) combinaties. Het slot heeft \(1000\) codes, \(000\) telt mee. Som 7 kan op zes manieren, som 2 enkel met (1, 1).",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "Van 50 jongeren hebben er 32 een smartphone en 21 een tablet. Zes jongeren hebben geen van beide.",
        [
            inv("Hoeveel jongeren hebben minstens één van de twee?", ["44"], r"\(50 - 6 = 44\)."),
            inv("Hoeveel hebben er allebei?", ["9"], r"\(32 + 21 - 44 = 9\)."),
            inv("Hoeveel hebben enkel een tablet?", ["12"], r"\(21 - 9 = 12\)."),
        ],
    ),
    koppel(
        "Welke regel gebruik je?",
        [("je kiest na elkaar een jas, een sjaal en een muts", "productregel"),
         ("je telt twee groepen die overlappen samen", "somregel met de doorsnede eraf"),
         ("je telt wat niet aan de voorwaarde voldoet", "complementregel")],
        ["delingsregel"],
        "Na elkaar: vermenigvuldigen. Samen: optellen min de dubbel getelde. Het omgekeerde: geheel min de rest.",
    ),
    mk(
        "Je gooit drie keer met een munt. In hoeveel uitkomsten heb je minstens één keer kop?",
        ["7", "3", "4", "6"],
        0,
        r"Er zijn \(8\) uitkomsten en maar één zonder kop (MMM). \(8 - 1 = 7\).",
    ),
    keuze(
        "Twee groepen die niets gemeen hebben, noem je [[*disjunct|gelijk|onbepaald]]. Hun doorsnede is dan [[*leeg|alles|één element]].",
        "Bij disjuncte groepen mag je de aantallen gewoon optellen.",
    ),
    volgorde(
        "Je vult een venndiagram in. Wat doe je eerst?",
        ["het aantal in de doorsnede invullen", "elke groep aanvullen tot haar totaal", "de som van alles in de kringen berekenen", "het aantal buiten de kringen bepalen"],
        "Begin in het midden. Anders tel je wie in beide zit dubbel.",
    ),
    inv(
        "Op hoeveel manieren kunnen vier vrienden naast elkaar op een bank gaan zitten?",
        ["24"],
        r"\(4 \cdot 3 \cdot 2 \cdot 1 = 24\).",
    ),
    mk(
        "Een klas kiest een klasvertegenwoordiger en een plaatsvervanger uit 20 leerlingen. Op hoeveel manieren kan dat?",
        ["380", "400", "190", "39"],
        0,
        r"\(20 \cdot 19 = 380\): de rollen verschillen, dus de volgorde telt.",
    ),
    sleep(
        "Bij een boomdiagram is één [[pad]] van het begin tot het einde één uitkomst. Het aantal uitkomsten vind je met de [[productregel]].",
        ["tak", "somregel"],
        "Elke tak is een keuze in één stap. Een pad combineert alle keuzes.",
    ),
    mk(
        "Hoeveel even getallen van drie cijfers kun je maken met de cijfers 1, 2, 3, 4 en 5 als elk cijfer hoogstens één keer mag?",
        ["24", "60", "48", "12"],
        0,
        r"Het laatste cijfer is \(2\) of \(4\): \(2\) keuzes. Dan nog \(4\) en \(3\) voor de andere plaatsen: \(2 \cdot 4 \cdot 3 = 24\).",
    ),
    inv(
        "Een restaurant heeft 4 voorgerechten en 6 hoofdgerechten. Je neemt een hoofdgerecht, met of zonder voorgerecht. Hoeveel keuzes heb je?",
        ["30"],
        r"Voor het voorgerecht heb je \(5\) mogelijkheden (vier of geen). \(5 \cdot 6 = 30\).",
    ),
    met_prent(f"{VENN}.svg", inv(
        "Kijk naar het venndiagram. Hoeveel leerlingen zitten niet in de muziekschool?",
        ["16"],
        r"Complementregel: \(30 - 14 = 16\). Of: \(9 + 7 = 16\).",
    )),
    tabel(
        "Hoeveel uitkomsten?",
        [("twee keer met een dobbelsteen gooien", "36"), ("vijf keer met een munt gooien", "32"), ("drie letters uit A, B, C met herhaling", "27"), ("de volgorde van vier boeken op een plank", "24")],
        r"\(6^{2} = 36\), \(2^{5} = 32\), \(3^{3} = 27\), \(4 \cdot 3 \cdot 2 \cdot 1 = 24\).",
        kolommen=["36", "32", "27", "24"],
    ),
    mk(
        "Een wachtwoord bestaat uit 3 tekens. Elk teken is een cijfer of een kleine letter. Hoeveel wachtwoorden zijn er?",
        ["46 656", "17 576", "1000", "108"],
        0,
        r"Er zijn \(10 + 26 = 36\) tekens per plaats: \(36^{3} = 46\,656\).",
    ),
]
