"""Statistiek: voorstellingen, centrum en spreiding — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import s_lijn, s_tekst, pix_zone, DONKER, GROEN

BOX = "statistiek-boxplot-do"
WAARDEN = {"min": 22, "Q1": 42, "med": 58, "Q3": 70, "max": 92}
Y0, Y1 = 220, 360


def X(v):
    return 100 + 8 * v


def _box():
    w = WAARDEN
    d = [s_lijn(X(0), 470, X(100), 470, kleur=DONKER, dikte=3)]
    for v in range(0, 101, 10):
        d.append(s_lijn(X(v), 462, X(v), 478, kleur=DONKER, dikte=2))
        d.append(s_tekst(X(v), 510, str(v), 20))
    d.append(s_tekst(X(50), 560, "punten op 100 voor een toets (120 leerlingen)", 22))
    mid = (Y0 + Y1) / 2
    d.append(s_lijn(X(w["min"]), mid, X(w["Q1"]), mid, kleur=GROEN, dikte=3))
    d.append(s_lijn(X(w["Q3"]), mid, X(w["max"]), mid, kleur=GROEN, dikte=3))
    for k in ("min", "max"):
        d.append(s_lijn(X(w[k]), mid - 35, X(w[k]), mid + 35, kleur=GROEN, dikte=4))
    d.append(f'<rect x="{X(w["Q1"])}" y="{Y0}" width="{X(w["Q3"]) - X(w["Q1"])}" height="{Y1 - Y0}" fill="#eef5e6" stroke="{GROEN}" stroke-width="4"/>')
    d.append(s_lijn(X(w["med"]), Y0, X(w["med"]), Y1, kleur="#7a4b8c", dikte=5))
    return d


def _zone(k):
    return pix_zone(X(WAARDEN[k]) - 20, Y0 - 10, 40, Y1 - Y0 + 20)


GRAFIEKEN = [dict(naam=BOX, titel="Boxplot van de toetsresultaten", eigen=_box)]
PRENTEN = [dict(bestand=f"{BOX}.svg", zelf=True, wat="boxplot met minimum 22, Q1 42, mediaan 58, Q3 70, maximum 92", vragen="klikvragen en aflezen van kwartielen en spreiding")]

VRAGEN = [
    klik(
        "Klik op de lijn die de mediaan toont.",
        f"{BOX}.svg",
        [_zone("med")],
        "De mediaan is de lijn binnenin de doos, hier bij 58 punten.",
    ),
    klik(
        "Klik op de lijn waaronder drie kwart van de leerlingen ligt.",
        f"{BOX}.svg",
        [_zone("Q3")],
        "Dat is het derde kwartiel: de rechterrand van de doos, bij 70 punten.",
    ),
    klik(
        "Klik op de lijn die de laagste score toont.",
        f"{BOX}.svg",
        [_zone("min")],
        "Het minimum is het uiteinde van de linkse snor: 22 punten.",
    ),
    met_prent(f"{BOX}.svg", tabel(
        "Kijk naar de boxplot. Welk getal lees je af?",
        [("de mediaan", "58"), ("de interkwartielafstand", "28"), ("de variatiebreedte", "70"), ("het eerste kwartiel", "42")],
        r"Interkwartielafstand \(70 - 42 = 28\). Variatiebreedte \(92 - 22 = 70\).",
        kolommen=["58", "28", "70", "42"],
    )),
    met_prent(f"{BOX}.svg", tabel(
        "Kijk naar de boxplot. Juist of fout?",
        [("Ongeveer 60 leerlingen haalden 58 of meer.", J),
         ("Ongeveer 30 leerlingen haalden minder dan 42.", J),
         ("De helft van de leerlingen haalde tussen 42 en 70.", J),
         ("Het gemiddelde is zeker 58.", F),
         ("Tussen 70 en 92 zitten meer leerlingen dan tussen 42 en 58.", F)],
        "Elk stuk van de boxplot bevat een kwart van de leerlingen, ongeacht hoe lang het stuk is. Het gemiddelde lees je niet af op een boxplot.",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{BOX}.svg", mk(
        "Kijk naar de boxplot. In welk deel liggen de scores het dichtst bij elkaar?",
        ["tussen de mediaan en Q3", "tussen Q1 en de mediaan", "in de linkse snor", "in de rechtse snor"],
        0,
        "Elk deel bevat een kwart. Het kortste deel (58 tot 70, breedte 12) heeft de scores het dichtst opeen.",
    )),
    mk(
        r"Wat is de mediaan van \(12,\ 3,\ 9,\ 15,\ 6,\ 10\)?",
        [r"\(9{,}5\)", r"\(9\)", r"\(10\)", r"\(9{,}17\)"],
        0,
        r"Eerst rangschikken: \(3, 6, 9, 10, 12, 15\). Het midden ligt tussen \(9\) en \(10\): \(9{,}5\).",
    ),
    casus(
        "In een klein bedrijf verdienen vijf werknemers per maand 2200, 2300, 2400, 2500 en 2600 euro. De zaakvoerder verdient 12 000 euro.",
        [
            inv("Wat is het gemiddelde maandloon van de zes, in euro?", ["4000", "4 000"], r"\(\dfrac{12\,000 + 12\,000}{6} = 4000\) euro."),
            inv("Wat is de mediaan, in euro?", ["2450", "2 450"], r"Tussen \(2400\) en \(2500\): \(2450\) euro."),
            mk("Welk getal geeft het beste beeld van een gewoon loon?", ["de mediaan", "het gemiddelde", "de variatiebreedte", "het maximum"], 0,
               "Het hoge loon van de zaakvoerder trekt het gemiddelde ver omhoog. De mediaan heeft daar geen last van."),
        ],
    ),
    sorteer(
        "Welke diagram past het best?",
        ["Lijndiagram", "Cirkeldiagram", "Histogram"],
        [("de temperatuur elke dag van een maand", "Lijndiagram"),
         ("de verdeling van het gezinsbudget over wonen, eten en vrije tijd", "Cirkeldiagram"),
         ("de lengtes van 200 leerlingen in klassen van 5 cm", "Histogram"),
         ("het aantal inwoners van België sinds 1900", "Lijndiagram"),
         ("welk deel van de stemmen naar elke partij ging", "Cirkeldiagram"),
         ("de reactietijden van 80 proefpersonen gegroepeerd per 50 ms", "Histogram")],
        "Een verloop in de tijd: lijndiagram. Delen van één geheel: cirkeldiagram. Numerieke gegevens in klassen: histogram.",
    ),
    tabel(
        "Wat gebeurt er met de waarde als je bij de reeks 4, 6, 7, 9, 14 de 14 vervangt door 64?",
        [("het gemiddelde", "verandert"), ("de mediaan", "blijft gelijk"), ("de variatiebreedte", "verandert"), ("de interkwartielafstand", "blijft gelijk"), ("de modus (er is er geen)", "blijft gelijk")],
        "Enkel de grootste waarde verandert. Maten die enkel naar het midden kijken, merken dat niet.",
        kolommen=["verandert", "blijft gelijk"],
    ),
    inv(
        "Het gemiddelde van vier toetsen is 13. Welke score heb je op de vijfde toets nodig voor een gemiddelde van 14?",
        ["18"],
        r"Nu heb je \(4 \cdot 13 = 52\) punten. Voor \(5 \cdot 14 = 70\) heb je \(70 - 52 = 18\) nodig.",
    ),
    mk(
        "Klas A en klas B hebben allebei 12 op 20 als gemiddelde. De standaardafwijking is 1,5 in A en 4 in B. Wat besluit je?",
        ["in B liggen de scores verder uit elkaar", "in B zitten de betere leerlingen van de twee", "in A zijn er zeker meer leerlingen gebuisd", "met dezelfde gemiddelden is er geen verschil"],
        0,
        "De standaardafwijking meet de spreiding rond het gemiddelde. Ze zegt niets over wie beter is.",
    ),
    koppel(
        "Verbind het soort gegevens met een voorbeeld.",
        [("numeriek, discreet", "het aantal broers en zussen"),
         ("numeriek, continu", "de lengte in cm"),
         ("categorisch, geordend", "de kledingmaat S, M, L"),
         ("categorisch, niet geordend", "de favoriete kleur")],
        ["het gemiddelde"],
        "Discreet: je telt. Continu: je meet. Geordend categorisch: er is een volgorde, maar je rekent er niet mee.",
    ),
    mk(
        r"Van 80 leerlingen kwamen er 28 met de bus. Hoeveel graden krijgt de bus in een cirkeldiagram?",
        [r"\(126^\circ\)", r"\(28^\circ\)", r"\(35^\circ\)", r"\(100^\circ\)"],
        0,
        r"\(\tfrac{28}{80} = 35\,\%\) en \(0{,}35 \cdot 360^\circ = 126^\circ\).",
    ),
    tabel(
        "Een histogram heeft klassen van 150 tot 155 cm, van 155 tot 160, enzovoort. Juist of fout?",
        [("Een leerling van 155 cm hoort in de klasse van 155 tot 160.", J),
         ("Het klassenmidden van de klasse van 160 tot 165 is 162,5.", J),
         ("De staven van een histogram staan los van elkaar.", F),
         ("Je kunt uit het histogram de exacte lengte van elke leerling aflezen.", F)],
        r"Klassen als \(\left[155, 160\right[\) nemen de linkergrens mee. Door te groeperen verlies je de exacte waarden.",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        "Een verdeling met een lange staart naar rechts noem je [[*rechtsscheef|linksscheef|symmetrisch]]. Het gemiddelde ligt dan meestal [[*rechts|links]] van de mediaan.",
        "De grote waarden in de staart trekken het gemiddelde mee naar rechts.",
    ),
    inv(
        r"Wat is de modus van \(5,\ 8,\ 8,\ 3,\ 5,\ 8,\ 2\)?",
        ["8"],
        r"\(8\) komt drie keer voor, vaker dan elke andere waarde.",
    ),
    volgorde(
        r"Zet voor de reeks \(1,\ 1,\ 3,\ 4,\ 11\) van klein naar groot.",
        ["de modus", "de mediaan", "het gemiddelde", "de variatiebreedte"],
        r"Modus \(1\), mediaan \(3\), gemiddelde \(\tfrac{20}{5} = 4\), variatiebreedte \(11 - 1 = 10\).",
    ),
    casus(
        "Een frequentietabel geeft het aantal doelpunten per wedstrijd van een ploeg: 0 doelpunten in 4 wedstrijden, 1 in 7, 2 in 6, 3 in 3.",
        [
            inv("Hoeveel wedstrijden zijn er gespeeld?", ["20"], r"\(4 + 7 + 6 + 3 = 20\)."),
            inv("Hoeveel doelpunten werden er in totaal gescoord?", ["28"], r"\(0 \cdot 4 + 1 \cdot 7 + 2 \cdot 6 + 3 \cdot 3 = 28\)."),
            mk("Wat is het gemiddelde aantal doelpunten per wedstrijd?", ["1,4", "1,5", "7", "2"], 0, r"\(\tfrac{28}{20} = 1{,}4\)."),
        ],
    ),
    sleep(
        "De doos van een boxplot loopt van [[Q1]] tot [[Q3]] en bevat de middelste [[helft]] van de gegevens.",
        ["het minimum", "kwart"],
        "Elk van de vier stukken bevat een kwart, dus de doos samen de helft.",
    ),
    inv(
        "Van 40 leerlingen komen er 14 te voet. Wat is de relatieve frequentie, in procent?",
        ["35", "35%", "35 %", "35 procent"],
        r"\(\tfrac{14}{40} = 0{,}35 = 35\,\%\).",
    ),
    tabel(
        "Juist of fout over centrummaten?",
        [("De mediaan van een reeks is altijd een waarde uit die reeks.", F),
         ("Een reeks kan twee modi hebben.", J),
         ("Als je bij elke waarde 5 optelt, stijgt het gemiddelde met 5.", J),
         ("Als je bij elke waarde 5 optelt, verandert de standaardafwijking.", F),
         ("Bij een symmetrische verdeling liggen gemiddelde en mediaan dicht bij elkaar.", J)],
        "Bij een even aantal waarden ligt de mediaan vaak tussen twee waarden. Alles verschuiven verandert het centrum, niet de spreiding.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Een reeks van zeven getallen heeft gemiddelde \(10\). Je voegt het getal \(18\) toe. Wat is het nieuwe gemiddelde?",
        ["11", "14", "10,5", "12"],
        0,
        r"De som was \(70\), nu \(88\) voor acht getallen: \(88 : 8 = 11\).",
    ),
    inv(
        r"Wat is de variatiebreedte van \(-4,\ 7,\ 2,\ 15,\ 0\)?",
        ["19"],
        r"\(15 - (-4) = 19\).",
    ),
    sorteer(
        "Is dit numeriek of categorisch?",
        ["Numeriek", "Categorisch"],
        [("de postcode van je gemeente", "Categorisch"), ("je reistijd naar school in minuten", "Numeriek"), ("je lievelingsvak", "Categorisch"), ("het aantal sms'jes per dag", "Numeriek"), ("je rugnummer bij de voetbal", "Categorisch")],
        "Een postcode of rugnummer is een getal, maar rekenen ermee heeft geen zin: het is een naam.",
    ),
    keuze(
        "Een waarde die ver van de rest ligt, heet een [[*uitschieter|modus|kwartiel]]. Die heeft het meeste invloed op [[*het gemiddelde|de mediaan]].",
        "De mediaan kijkt enkel naar de middelste waarde. Het gemiddelde telt elke waarde mee.",
    ),
]
