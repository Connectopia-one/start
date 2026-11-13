"""Statistiek: voorstellingen, centrum en spreiding — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, vak_zone, pix_zone, s_tekst, s_lijn, s_vak, DONKER, GROEN

BOX = "statistiek-boxplot-toets"
HIST = venster("statistiek-histogram-lengte", 145, 175, 0, 12, 5, 2)
STAVEN = [(150, 5, 3), (155, 5, 7), (160, 5, 10), (165, 5, 6), (170, 5, 4)]

# boxplot van toetsresultaten op 100: min 30, Q1 55, mediaan 65, Q3 78, max 95
X0, X1, A, B = 80, 920, 20, 100


def _x(w):
    return X0 + (w - A) / (B - A) * (X1 - X0)


def _box():
    y = 300
    d = [s_lijn(X0, 470, X1, 470, kleur=DONKER, dikte=3)]
    for w in range(20, 101, 10):
        d.append(s_lijn(_x(w), 462, _x(w), 478, kleur=DONKER, dikte=2))
        d.append(s_tekst(_x(w), 510, w, 20))
    d.append(s_tekst(500, 560, "punten op 100", 20, kleur="#6b6b5a"))
    d.append(s_lijn(_x(30), y, _x(55), y, kleur=DONKER, dikte=3))
    d.append(s_lijn(_x(78), y, _x(95), y, kleur=DONKER, dikte=3))
    d.append(s_lijn(_x(30), y - 40, _x(30), y + 40, kleur=DONKER, dikte=3))
    d.append(s_lijn(_x(95), y - 40, _x(95), y + 40, kleur=DONKER, dikte=3))
    d.append(s_vak(_x(55), y - 80, _x(78) - _x(55), 160, vul="#cfe0c3", rand=GROEN, dikte=4))
    d.append(s_lijn(_x(65), y - 80, _x(65), y + 80, kleur=GROEN, dikte=5))
    return d


def _bz(w, breed=40):
    return pix_zone(_x(w) - breed / 2, 200, breed, 200)


GRAFIEKEN = [
    dict(naam=BOX, titel="Boxplot van de toets wiskunde (120 leerlingen)", eigen=_box),
    dict(naam=HIST, titel="Lengte van 30 leerlingen (in cm)", staven=STAVEN, xlabel="cm", ylabel="aantal", ijk_x=5, ijk_y=2),
]
PRENTEN = [dict(bestand=f"{BOX}.svg", zelf=True, wat="boxplot van toetsresultaten", vragen="klikvragen en aflezen"),
           dict(bestand=f"{HIST}.svg", zelf=True, wat="histogram van lengtes", vragen="klikvragen en aflezen")]

VRAGEN = [
    klik(
        "Klik op de mediaan in de boxplot.",
        f"{BOX}.svg",
        [_bz(65, 36)],
        "De mediaan is de lijn binnen de doos: hier 65 punten. De randen van de doos zijn Q1 en Q3.",
    ),
    klik(
        "Klik op de waarde waaronder een kwart van de leerlingen scoorde.",
        f"{BOX}.svg",
        [_bz(55, 36)],
        "Dat is het eerste kwartiel Q1: de linkerrand van de doos, bij 55 punten.",
    ),
    met_prent(f"{BOX}.svg", tabel(
        "Juist of fout volgens de boxplot?",
        [
            ("De interkwartielafstand is 23 punten.", J),
            ("De variatiebreedte is 65 punten.", J),
            ("Ongeveer 60 leerlingen haalden minstens 65 punten.", J),
            ("Het gemiddelde is zeker 65 punten.", F),
            ("Ongeveer 30 leerlingen haalden tussen 78 en 95 punten.", J),
        ],
        "IKA = 78 − 55 = 23. Variatiebreedte = 95 − 30 = 65. De helft van 120 ligt boven de mediaan, een kwart boven Q3. Het gemiddelde lees je niet af uit een boxplot.",
    )),
    met_prent(f"{BOX}.svg", mk(
        "Waarom is de linkersnor langer dan de rechtersnor?",
        [
            "de laagste kwart scores liggen verder uit elkaar dan de hoogste kwart",
            "er zijn meer leerlingen met een lage score dan met een hoge",
            "de mediaan ligt links van het midden van de doos",
            "de toets was te moeilijk",
        ],
        0,
        "Elke snor bevat een kwart van de leerlingen. Een langere snor betekent dat dat kwart meer gespreid ligt, niet dat het meer leerlingen zijn.",
    )),
    klik(
        "Klik op de modale klasse in het histogram.",
        f"{HIST}.svg",
        [vak_zone(HIST, 160, 165, 0, 10)],
        "De modale klasse is de klasse met de grootste frequentie: [160, 165[ met 10 leerlingen.",
    ),
    met_prent(f"{HIST}.svg", inv(
        "Hoeveel procent van de leerlingen is minstens 165 cm?",
        ["33,3", "33,3%", "33,3 %", "33", "33%", "33,33"],
        r"\(6 + 4 = 10\) van de \(30\): \(\tfrac{10}{30} \approx 33{,}3\%\).",
    )),
    met_prent(f"{HIST}.svg", mk(
        "In welke klasse ligt de mediaan?",
        [r"\(\left[155, 160\right[\)", r"\(\left[160, 165\right[\)", r"\(\left[165, 170\right[\)", r"\(\left[150, 155\right[\)"],
        1,
        r"De mediaan van \(30\) lengtes ligt tussen de \(15\)de en de \(16\)de. Tot \(160\) cm tel je \(3 + 7 = 10\), tot \(165\) cm \(20\): de mediaan valt in \(\left[160, 165\right[\).",
    )),
    met_prent(f"{HIST}.svg", inv(
        "Bereken het gemiddelde met de klassenmiddens. Rond af op een tiende, in cm.",
        ["162,7", "162,7 cm", "162.7"],
        r"\(\tfrac{3 \cdot 152{,}5 + 7 \cdot 157{,}5 + 10 \cdot 162{,}5 + 6 \cdot 167{,}5 + 4 \cdot 172{,}5}{30} = \tfrac{4880}{30} \approx 162{,}7\) cm.",
    )),
    koppel(
        "Koppel elke vraag aan de voorstelling die er het best bij past.",
        [
            ["Hoe veranderde de temperatuur elk uur van de dag?", "lijndiagram"],
            ["Welk deel van het budget gaat naar huur, eten en vrije tijd?", "cirkeldiagram"],
            ["Hoe zijn de lengtes van 200 leerlingen verdeeld over klassen van 5 cm?", "histogram"],
            ["Hoe verschillen de toetsscores van drie klassen in spreiding?", "drie boxplots naast elkaar"],
        ],
        ["dotplot met één punt"],
        "Een verloop in de tijd: lijndiagram. Delen van een geheel: cirkeldiagram. Klassen: histogram. Spreiding vergelijken: boxplots.",
    ),
    mk(
        r"De getallen \(4, 7, 7, 9, x\) hebben als gemiddelde \(8\). Hoeveel is \(x\)?",
        [r"\(8\)", r"\(13\)", r"\(11\)", r"\(15\)"],
        1,
        r"Vijf getallen met gemiddelde \(8\) hebben als som \(40\). \(4 + 7 + 7 + 9 = 27\), dus \(x = 13\).",
    ),
    casus(
        r"Zes vrienden lopen de \(5\) km. Hun tijden in minuten: \(24,\ 26,\ 27,\ 29,\ 30,\ 52\).",
        [
            inv(
                "Wat is het gemiddelde? Rond af op een tiende, in minuten.",
                ["31,3", "31,3 minuten", "31.3"],
                r"\(24 + 26 + 27 + 29 + 30 + 52 = 188\), en \(188 : 6 \approx 31{,}3\).",
            ),
            inv(
                "Wat is de mediaan, in minuten?",
                ["28", "28 minuten"],
                r"Zes tijden: het gemiddelde van de derde en de vierde, \(\tfrac{27 + 29}{2} = 28\).",
            ),
            mk(
                "Welke maat beschrijft het best hoe snel de groep meestal loopt?",
                [
                    "de mediaan, want de ene trage tijd trekt het gemiddelde omhoog",
                    "het gemiddelde, want daarin telt elke loper even zwaar mee",
                    "de variatiebreedte, want die toont het verschil tussen snelste en traagste",
                    "de modus, want die komt het vaakst voor",
                ],
                0,
                r"Vijf van de zes lopers zitten onder het gemiddelde. De tijd van \(52\) minuten is een uitschieter. Een modus is er hier niet: elke tijd komt één keer voor.",
            ),
        ],
    ),
    tabel(
        "Welke centrummaat verandert als je de grootste waarde nog veel groter maakt?",
        [
            ("het rekenkundig gemiddelde", "verandert"),
            ("de mediaan", "verandert niet"),
            ("de modus, als de grootste waarde maar één keer voorkomt", "verandert niet"),
            ("de variatiebreedte", "verandert"),
        ],
        "Het gemiddelde en de variatiebreedte rekenen met elke waarde. De mediaan en de modus hangen enkel af van de middelste of de vaakst voorkomende waarde.",
        kolommen=["verandert", "verandert niet"],
    ),
    keuze(
        "Bij een rechtsscheve verdeling ligt het gemiddelde meestal [[*rechts van|links van|op]] de mediaan, want de lange staart trekt het gemiddelde naar [[*de grote waarden|de kleine waarden]].",
        "Een paar heel grote waarden duwen het gemiddelde omhoog, de mediaan blijft in het midden van de rij.",
    ),
    sorteer(
        "Numeriek, categorisch geordend of categorisch niet geordend?",
        ["numeriek", "categorisch, geordend", "categorisch, niet geordend"],
        [
            ["het aantal broers en zussen", "numeriek"],
            ["de lievelingskleur", "categorisch, niet geordend"],
            ["de kledingmaat S, M, L of XL", "categorisch, geordend"],
            ["de reistijd naar school in minuten", "numeriek"],
            ["de woonplaats", "categorisch, niet geordend"],
            ["de beoordeling: nooit, soms, vaak, altijd", "categorisch, geordend"],
        ],
        "Numerieke gegevens zijn getallen waarmee je kan rekenen. Categorische gegevens zijn klassen, met of zonder volgorde.",
    ),
    mk(
        r"Klas A heeft als punten \(6, 7, 7, 8, 8, 9\). Klas B heeft \(2, 5, 8, 9, 10, 11\). Beide hebben gemiddelde \(7{,}5\). Wat klopt?",
        [
            "de standaardafwijking van klas B is groter",
            "de standaardafwijking van klas A is groter",
            "ze hebben dezelfde standaardafwijking, want het gemiddelde is gelijk",
            "de mediaan van klas B is kleiner",
        ],
        0,
        r"In klas B liggen de punten veel verder van \(7{,}5\) af. De mediaan van B is \(8{,}5\), die van A \(7{,}5\).",
    ),
    inv(
        r"Wat is de mediaan van \(12, 3, 8, 15, 6, 10\)?",
        ["9"],
        r"Eerst ordenen: \(3, 6, 8, 10, 12, 15\). Bij een even aantal neem je het gemiddelde van de twee middelste: \(\tfrac{8 + 10}{2} = 9\).",
    ),
    volgorde(
        r"Je stelt een boxplot op van \(11\) gemeten waarden. Zet de stappen in volgorde.",
        [
            "de waarden van klein naar groot ordenen",
            "de mediaan zoeken: de 6de waarde",
            "Q1 en Q3 zoeken: de mediaan van de onderste en de bovenste helft",
            "minimum en maximum aflezen",
            "de doos van Q1 tot Q3 en de snorren tot minimum en maximum tekenen",
        ],
        "Zonder ordenen kan je geen mediaan of kwartiel vinden. Daarna werk je van binnen naar buiten.",
    ),
    mk(
        r"Bij een enquête antwoorden \(40\) leerlingen. \(14\) komen met de fiets. Hoe groot is de hoek van die sector in een cirkeldiagram?",
        [r"\(14^{\circ}\)", r"\(35^{\circ}\)", r"\(126^{\circ}\)", r"\(140^{\circ}\)"],
        2,
        r"\(\tfrac{14}{40} = 0{,}35\), en \(0{,}35 \cdot 360^{\circ} = 126^{\circ}\).",
    ),
    tabel(
        "Juist of fout over spreidingsmaten?",
        [
            ("De interkwartielafstand bevat de middelste helft van de gegevens.", J),
            ("Een standaardafwijking van 0 betekent dat alle waarden gelijk zijn.", J),
            ("De variatiebreedte is ongevoelig voor uitschieters.", F),
            ("Een grote standaardafwijking betekent dat de waarden groot zijn.", F),
        ],
        "De standaardafwijking meet de spreiding rond het gemiddelde, niet de grootte van de waarden. De variatiebreedte hangt net af van de uiterste waarden.",
    ),
    mk(
        r"Elke leerling krijgt \(2\) bonuspunten op een toets. Wat gebeurt er met het gemiddelde en met de standaardafwijking?",
        [
            r"het gemiddelde stijgt met \(2\), de standaardafwijking blijft gelijk",
            r"beide stijgen met \(2\)",
            r"het gemiddelde blijft gelijk, de standaardafwijking stijgt",
            r"beide blijven gelijk",
        ],
        0,
        "Alles schuift 2 op: het centrum verschuift mee, maar de afstanden tussen de punten en het gemiddelde veranderen niet.",
    ),
    sleep(
        "De waarde die het vaakst voorkomt, is de [[modus]]. De middelste waarde van een geordende rij is de [[mediaan]]. Het verschil tussen Q3 en Q1 is de [[interkwartielafstand]].",
        ["variatiebreedte", "frequentie"],
        "Modus en mediaan zijn centrummaten, de interkwartielafstand is een spreidingsmaat.",
    ),
    inv(
        r"Een speler scoorde in \(4\) wedstrijden gemiddeld \(15\) punten. Hoeveel moet hij scoren in de vijfde wedstrijd om gemiddeld \(17\) te halen?",
        ["25", "25 punten"],
        r"Na \(5\) wedstrijden is de som \(5 \cdot 17 = 85\). Na \(4\) was ze \(4 \cdot 15 = 60\). Dus \(85 - 60 = 25\).",
    ),
    open_(
        r"In een klas haalt iedereen tussen \(10\) en \(14\) op \(20\), behalve één leerling met \(1\). Welke centrummaat geeft het best weer hoe de klas het deed? Leg uit.",
        r"De mediaan. De ene lage score trekt het gemiddelde naar beneden, terwijl de mediaan enkel naar het midden van de geordende rij kijkt en zo de typische score van de klas toont.",
    ),
    mk(
        r"In een dotplot liggen \(15\) punten tussen \(3\) en \(6\) en \(12\) punten tussen \(14\) en \(17\), met niets ertussen. Wat besluit je?",
        [
            "de gegevens vormen twee clusters: er zitten wellicht twee groepen in",
            "de verdeling is symmetrisch, dus het gemiddelde is een goede samenvatting",
            "er zijn 27 uitschieters",
            "de mediaan ligt rond 10",
        ],
        0,
        "Twee duidelijke groepjes wijzen op twee soorten metingen, bijvoorbeeld twee leeftijdsgroepen. Een gemiddelde rond 10 beschrijft niemand. De mediaan (de 14de waarde) ligt nog in de eerste groep.",
    ),
    inv(
        r"Het gemiddelde van vijf getallen is \(12\). Je laat het getal \(20\) weg. Wat is het gemiddelde van de vier getallen die overblijven?",
        ["10"],
        r"De som van de vijf is \(5 \cdot 12 = 60\). Zonder \(20\): \(40\), en \(40 : 4 = 10\).",
    ),
    keuze(
        "Tussen Q1 en de mediaan ligt [[*25 %|50 %|75 %]] van de gegevens. Boven Q1 ligt [[*75 %|25 %|50 %]] van de gegevens.",
        "De drie kwartielen verdelen de geordende gegevens in vier even grote stukken.",
    ),
    met_prent(f"{HIST}.svg", tabel(
        "Juist of fout volgens het histogram?",
        [
            ("Er zijn 7 leerlingen van minstens 155 en minder dan 160 cm.", J),
            ("Er is minstens één leerling van precies 175 cm.", F),
            ("De kleinste leerling is precies 150 cm.", F),
            ("Er zijn samen 30 leerlingen.", J),
        ],
        "Bij klassen ken je de waarden niet meer precies: je weet enkel in welke klasse ze vallen. 175 hoort niet bij [170, 175[.",
    )),
    mk(
        "Waarom raken de staven van een histogram elkaar, en die van een staafdiagram niet?",
        [
            "een histogram toont aaneensluitende klassen van een numerieke grootheid",
            "een histogram heeft altijd meer gegevens dan een staafdiagram",
            "bij een staafdiagram zijn de staven altijd even hoog",
            "dat is enkel een kwestie van smaak van wie de grafiek tekent, er is geen echte reden voor",
        ],
        0,
        "De klassen van een histogram sluiten op elkaar aan: waar de ene stopt, begint de volgende. Bij een staafdiagram staan losse categorieën naast elkaar.",
    ),
]
