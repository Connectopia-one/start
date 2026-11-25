"""Telproblemen en problemen oplossen — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_telproblemen: boomdiagram, venndiagram, som-, product- en
complementregel, en probleemoplossend denken (heuristieken, terugwerken,
schatten, controleren). Met twee zelfgetekende prenten: een venndiagram en
een boomdiagram."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, pix_zone, kansboom

VD = "venn-voetbal-muziek"
GETAL = {"V": (330, 340, "10"), "VM": (500, 340, "5"), "M": (670, 340, "8"), "G": (130, 560, "5")}


def _venn():
    d = [s_vak(60, 70, 880, 540, vul="#ffffff", rand="#24331b", dikte=3, rond=14),
         s_tekst(90, 105, "Klas van 28 leerlingen", 22, "start", vet=True),
         '<circle cx="410" cy="340" r="190" fill="#3b6fa0" fill-opacity="0.18" stroke="#3b6fa0" stroke-width="4"/>',
         '<circle cx="590" cy="340" r="190" fill="#b5651d" fill-opacity="0.18" stroke="#b5651d" stroke-width="4"/>',
         s_tekst(250, 150, "voetbal", 24, kleur="#3b6fa0", vet=True), s_tekst(750, 150, "muziek", 24, kleur="#b5651d", vet=True)]
    for x, y, t in GETAL.values():
        d.append(s_tekst(x, y + 12, t, 36, vet=True))
    return d


def _gz(*sleutels):
    return [pix_zone(GETAL[s][0] - 45, GETAL[s][1] - 40, 90, 80) for s in sleutels]


BD = "boom-menu"
_BOOM, _MID, _KNOPEN = kansboom((90, 330),
                                [("soep", "", (330, 180)), ("salade", "", (330, 480))],
                                {"soep": [("vis", "", (700, 90)), ("vlees", "", (700, 180)), ("veggie", "", (700, 270))],
                                 "salade": [("vis", "", (700, 390)), ("vlees", "", (700, 480)), ("veggie", "", (700, 570))]})


def _bz(*paden):
    return [pix_zone(_KNOPEN[p][0] - 60, _KNOPEN[p][1] - 26, 120, 52) for p in paden]


GRAFIEKEN = [dict(naam=VD, titel="Wie voetbalt, wie speelt muziek?", eigen=_venn),
             dict(naam=BD, titel="Een menu: eerst een voorgerecht, dan een hoofdgerecht", eigen=lambda: _BOOM)]
UV, UB = f"{VD}.svg", f"{BD}.svg"

VRAGEN = [
    klik("Klik op het getal van de leerlingen die voetballen maar geen muziek spelen.", UV, _gz("V"), "Het deel van de blauwe cirkel buiten de overlap."),
    klik("Klik op het getal van de leerlingen die geen van beide doen.", UV, _gz("G"), "Buiten beide cirkels, maar binnen de klas."),
    klik("Klik op een getal dat meetelt bij alle leerlingen die muziek spelen.", UV, _gz("VM", "M"), "Muziek: enkel muziek plus de overlap."),
    klik("Klik op het eindpunt voor soep met vis.", UB, _bz(("soep", "vis")), "Volg eerst de tak naar soep, dan naar vis."),
    klik("Klik op een eindpunt van een menu met veggie.", UB, _bz(("soep", "veggie"), ("salade", "veggie")), "Veggie kan na soep en na salade."),
    inv("Kijk naar het venndiagram. Hoeveel leerlingen spelen muziek?", ["13", "dertien"], r"\(8 + 5 = 13\)."),
    inv(r"Kijk naar het venndiagram. Hoeveel leerlingen zitten in \(V \cup M\)?", ["23", "drieëntwintig"],
        r"\(10 + 5 + 8 = 23\), of \(28 - 5\). Ook: \(15 + 13 - 5 = 23\)."),
    inv("Een restaurant heeft 3 voorgerechten, 4 hoofdgerechten en 2 desserts. Hoeveel menu's van drie gangen zijn er?", ["24", "vierentwintig"],
        r"Keuzes na elkaar: \(3 \cdot 4 \cdot 2 = 24\)."),
    inv("Een code bestaat uit twee letters (26 mogelijke) gevolgd door één cijfer. Hoeveel codes zijn er?", ["6760", "6 760", "6.760"],
        r"\(26 \cdot 26 \cdot 10 = 6\,760\)."),
    inv("Hoeveel pincodes van 4 cijfers bevatten minstens één 7?", ["3439", "3 439", "3.439"],
        r"Complement: zonder 7 zijn er \(9^{4} = 6\,561\). Dus \(10\,000 - 6\,561 = 3\,439\)."),
    mk("Je kiest één voertuig: een van 5 fietsen of een van 3 steps. Welke regel en hoeveel keuzes?",
       [r"de somregel: \(8\)", r"de productregel: \(15\)", r"de complementregel: \(2\)", r"de productregel: \(8\) keuzes"], 0,
       "Je kiest het een of het ander, niet allebei: optellen."),
    tabel("Som- of productregel?",
          [("een broek én een trui kiezen", "productregel"), ("met de trein of met de bus gaan", "somregel"),
           ("drie keer na elkaar een munt opgooien", "productregel"), ("een prijs kiezen uit vak A of uit vak B", "somregel")],
          "Keuzes na elkaar: vermenigvuldigen. Keuzes die elkaar uitsluiten: optellen.",
          kolommen=["somregel", "productregel"]),
    inv("Je gooit twee dobbelstenen. Op hoeveel manieren is de som 7?", ["6", "zes"], r"\((1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\)."),
    inv("Je gooit twee dobbelstenen. Bij hoeveel uitkomsten is er minstens één zes?", ["11", "elf"], r"Zonder zes: \(5 \cdot 5 = 25\). \(36 - 25 = 11\)."),
    casus("Een slak zit onderaan een put van \\(10\\) m. Overdag klimt ze \\(3\\) m omhoog, 's nachts glijdt ze \\(2\\) m terug.", [
        mk("Welke heuristiek helpt hier het best?",
           ["een tabel per dag maken", "het antwoord gewoon gokken", "de getallen optellen", "van achteren naar voren werken met breuken"], 0,
           "Per dag bijhouden waar de slak 's avonds en 's ochtends zit."),
        inv("Op welke hoogte zit ze na de eerste nacht, in m?", ["1", "een", "één"], r"\(3 - 2 = 1\)."),
        inv("Op welke dag komt ze boven?", ["8", "acht"], r"Na 7 nachten zit ze op \(7\) m. Op dag 8 klimt ze tot \(10\) m."),
        keuze("Het antwoord '10 dagen' (10 m gedeeld door 1 m per dag) is [[*fout, want de laatste dag zakt ze niet meer terug|juist]].",
              "Controleer altijd of je redenering klopt met het verhaal."),
    ]),
    mk("Ik deel een getal door 3, trek er 4 van af en krijg 5. Welk getal was het?",
       [r"\(27\)", r"\(3\)", r"\(17\)", r"\(\frac{1}{3}\)"], 0, r"Terugwerken: \(5 + 4 = 9\) en \(9 \cdot 3 = 27\)."),
    inv("Een jas kost na 30 % korting 56 euro. Wat was de oude prijs, in euro?", ["80", "tachtig"], r"\(56\) is \(70\,\%\): \(56 : 0{,}7 = 80\)."),
    mk("Een klas van 24 leerlingen gaat op uitstap. Het kost 18,50 euro per persoon. Wat is een goede schatting van het totaal?",
       ["ongeveer 450 euro", "ongeveer 45 euro", "ongeveer 4 500 euro", "ongeveer 250 euro"], 0, r"\(25 \cdot 18 = 450\). Precies: \(444\) euro."),
    sorteer("Welke heuristiek past het best?", ["terugwerken", "tabel maken", "tekening maken"],
            [("Je kent het resultaat na een reeks bewerkingen.", "terugwerken"), ("Je zoekt een patroon in het aantal blokjes per stap.", "tabel maken"),
             ("Rond een tuin komt een pad: hoeveel tegels heb je nodig?", "tekening maken"), ("Op het einde had ze nog 12 euro. Hoeveel had ze eerst?", "terugwerken")],
            "Meer dan één heuristiek kan werken, maar deze zijn het snelst."),
    tabel("Is dit antwoord redelijk?",
          [("Een leerling van 15 jaar weegt 520 kg.", "nee"), ("Een auto rijdt 120 km per uur op de autosnelweg.", "ja"),
           ("Een klaslokaal heeft een oppervlakte van 6 m².", "nee"), ("Een liter melk kost 1,20 euro.", "ja")],
          "Een onrealistische grootteorde wijst op een rekenfout of een verkeerde eenheid.",
          kolommen=["ja", "nee"]),
    keuze(r"In \(|A \cup B| = |A| + |B| - |A \cap B|\) trek je de overlap af, omdat je ze anders [[*twee keer|nul keer]] telt.", "De overlap zit in A én in B."),
    inv("Van 40 jongeren hebben er 25 een fiets, 18 een step en 8 geen van beide. Hoeveel hebben er beide?", ["11", "elf"],
        r"Minstens één: \(40 - 8 = 32\). \(25 + 18 - 32 = 11\)."),
    mk("Zes personen geven elkaar elk één keer een hand. Hoeveel handdrukken zijn er?",
       [r"\(15\)", r"\(30\)", r"\(36\)", r"\(6 \cdot 5\)"], 0,
       r"Eenvoudiger beginnen: 2 personen geven 1, 3 geven 3, 4 geven 6. Elke nieuwe persoon geeft iedereen een hand: \(5 + 4 + 3 + 2 + 1 = 15\)."),
    sleep("Met 2 soorten brood, 3 soorten beleg en 2 drankjes maak je [[12]] lunchpakketten. Dat is de [[productregel]].",
          ["7", "somregel"], r"\(2 \cdot 3 \cdot 2 = 12\)."),
    open_("Leg uit waarom je bij 'minstens één' vaak beter het complement telt. Gebruik een voorbeeld.",
          r"Het tegendeel van 'minstens één' is 'geen enkele', en dat is één geval dat je makkelijk telt. Bij drie keer een munt: minstens één keer kop is alles behalve drie keer munt, dus \(8 - 1 = 7\)."),
    inv("Hoeveel getallen van drie verschillende cijfers kan je maken met de cijfers 1, 2, 3 en 4?", ["24", "vierentwintig"],
        r"\(4\) keuzes voor het eerste cijfer, dan \(3\), dan \(2\): \(24\)."),
    keuze("Drie keer een dobbelsteen gooien geeft [[*216|18|36]] uitkomsten.", r"\(6 \cdot 6 \cdot 6 = 216\)."),
]
