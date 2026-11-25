"""Gegevens weergeven en samenvatten — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_statistiek: soorten gegevens, frequentietabel, diagrammen,
centrummaten, spreidingsmaten, boxplot en misleidende grafieken. Met twee
zelfgetekende prenten: twee boxplots en twee staafdiagrammen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import s_tekst, s_lijn, s_vak, pix_zone

BP = "twee-boxplots-klassen"
X0, X1 = 140, 920
KLAS = {"A": (20, 45, 60, 70, 95, 210), "B": (35, 50, 55, 60, 80, 400)}


def _x(w):
    return X0 + w / 100 * (X1 - X0)


def _boxplots():
    d = [s_lijn(X0, 540, X1, 540, kleur="#24331b", dikte=2)]
    for w in range(0, 101, 10):
        d.append(s_lijn(_x(w), 534, _x(w), 546, kleur="#24331b", dikte=2))
        d.append(s_tekst(_x(w), 572, str(w), 18))
    d.append(s_tekst(530, 610, "punten op 100", 18))
    for naam, (mn, q1, me, q3, mx, y) in KLAS.items():
        d.append(s_tekst(70, y + 8, f"klas {naam}", 22, vet=True))
        d.append(s_lijn(_x(mn), y, _x(q1), y, kleur="#24331b", dikte=3))
        d.append(s_lijn(_x(q3), y, _x(mx), y, kleur="#24331b", dikte=3))
        d.append(s_lijn(_x(mn), y - 20, _x(mn), y + 20, kleur="#24331b", dikte=3))
        d.append(s_lijn(_x(mx), y - 20, _x(mx), y + 20, kleur="#24331b", dikte=3))
        d.append(s_vak(_x(q1), y - 45, _x(q3) - _x(q1), 90, vul="#e6efdc", rand="#2f4a22", dikte=3))
        d.append(s_lijn(_x(me), y - 45, _x(me), y + 45, kleur="#b5651d", dikte=5))
    return d


def _lz(w, y, b=36, h=110):
    return [pix_zone(_x(w) - b / 2, y - h / 2, b, h)]


MS = "staven-eerlijk-misleidend"
MERK = [("A", 92), ("B", 96)]


def _staven():
    d = []
    for (x0, vanaf, kop) in [(60, 0, "Grafiek 1"), (530, 90, "Grafiek 2")]:
        d.append(s_vak(x0, 60, 410, 560, vul="#ffffff", rand="#b9b29c", dikte=2, rond=10))
        d.append(s_tekst(x0 + 205, 95, kop, 22, vet=True))
        d.append(s_tekst(x0 + 205, 122, "tevreden klanten (%)", 17))
        ax, ay, top = x0 + 70, 560, 150
        d.append(s_lijn(ax, ay, x0 + 380, ay, kleur="#24331b", dikte=2))
        d.append(s_lijn(ax, ay, ax, top - 10, kleur="#24331b", dikte=2))
        hoog = 100 - vanaf
        for k in range(5):
            w = vanaf + k * hoog / 4
            yy = ay - (w - vanaf) / hoog * (ay - top)
            d.append(s_lijn(ax - 6, yy, ax, yy, kleur="#24331b", dikte=2))
            d.append(s_tekst(ax - 10, yy + 6, f"{w:g}".replace(".", ","), 16, "end"))
        for i, (m, v) in enumerate(MERK):
            bx = ax + 50 + i * 140
            yy = ay - (v - vanaf) / hoog * (ay - top)
            d.append(s_vak(bx, yy, 90, ay - yy, vul="#3b6fa0" if m == "A" else "#b5651d", rand="#24331b", dikte=2))
            d.append(s_tekst(bx + 45, ay + 26, f"merk {m}", 18))
    return d


GRAFIEKEN = [dict(naam=BP, titel="De punten van twee klassen op dezelfde toets", eigen=_boxplots),
             dict(naam=MS, titel="Twee grafieken met dezelfde cijfers", eigen=_staven)]
UB, UM = f"{BP}.svg", f"{MS}.svg"

VRAGEN = [
    klik("Klik op de mediaan van klas A.", UB, _lz(60, 210), "De streep in de doos: 60 punten."),
    klik("Klik op het maximum van klas B.", UB, _lz(80, 400, 40, 60), "Het rechtse uiteinde van de snor: 80 punten."),
    klik("Klik op de doos van de klas met de grootste interkwartielafstand.", UB, [pix_zone(_x(45), 165, _x(70) - _x(45), 90)],
         r"Klas A: \(70 - 45 = 25\). Klas B: \(60 - 50 = 10\)."),
    klik("Klik op de grafiek die een klein verschil groot doet lijken.", UM, [pix_zone(530, 60, 410, 560)],
         "In grafiek 2 begint de as bij 90. Daardoor lijkt merk B veel beter, terwijl het verschil maar 4 procentpunten is."),
    klik("Klik op de grafiek die de twee merken eerlijk vergelijkt.", UM, [pix_zone(60, 60, 410, 560)], "Een as die bij 0 begint, toont de echte verhouding."),
    met_prent(UB, inv("Wat is de interkwartielafstand van klas B?", ["10", "tien"], r"\(Q_{3} - Q_{1} = 60 - 50 = 10\).")),
    met_prent(UB, inv("Wat is de variatiebreedte van klas A?", ["75", "vijfenzeventig"], r"\(95 - 20 = 75\).")),
    met_prent(UB, inv("Welk percentage van klas A haalt tussen 45 en 70 punten?", ["50", "50%", "50 %"], "Tussen Q1 en Q3 ligt de helft van de gegevens.")),
    mk(r"Wat is de mediaan van \(2, 3, 3, 8, 9, 15\)?",
       [r"\(5{,}5\)", r"\(3\)", r"\(6{,}67\)", r"\(8\)"], 0, r"Zes getallen: het gemiddelde van de twee middelste, \(\frac{3 + 8}{2} = 5{,}5\)."),
    inv("Na vier toetsen heeft Mo gemiddeld 12 op 20. Wat moet hij op de vijfde halen om gemiddeld 13 te hebben?", ["17", "zeventien"],
        r"Nodig: \(5 \cdot 13 = 65\). Hij heeft \(4 \cdot 12 = 48\). \(65 - 48 = 17\)."),
    inv(r"Schoenmaten in een groep: \(38, 39, 39, 40, 41, 39, 42\). Wat is de modus?", ["39"], r"\(39\) komt drie keer voor."),
    tabel("Categorisch of numeriek?",
          [("je favoriete sport", "categorisch"), ("het aantal berichten dat je per dag stuurt", "numeriek"), ("je postcode", "categorisch"),
           ("je lichaamstemperatuur", "numeriek"), ("de kleur van je fiets", "categorisch")],
          "Een postcode bestaat uit cijfers, maar rekenen ermee heeft geen zin: het is een naam voor een gemeente.",
          kolommen=["categorisch", "numeriek"]),
    tabel("Welk diagram past het best?",
          [("hoe de temperatuur verloopt over een week", "lijndiagram"), ("hoe een budget verdeeld is over vier posten", "cirkeldiagram"),
           ("de lengtes van 200 leerlingen, in klassen", "histogram"), ("het aantal leerlingen per favoriete sport", "staafdiagram")],
          "Tijd: lijn. Delen van een geheel: cirkel. Numeriek in klassen: histogram. Categorieën: staven.",
          kolommen=["staafdiagram", "cirkeldiagram", "lijndiagram", "histogram"]),
    casus("Twintig leerlingen tellen hun broers en zussen. Geen: \\(4\\) leerlingen. Eén: \\(8\\). Twee: \\(5\\). Drie: \\(3\\).", [
        inv("Wat is de modus van het aantal broers en zussen?", ["1", "een", "één"], "De meeste leerlingen (8) hebben één broer of zus."),
        inv("Wat is het gemiddelde? Een kommagetal.", ["1,35", "1.35"], r"\(\frac{0 \cdot 4 + 1 \cdot 8 + 2 \cdot 5 + 3 \cdot 3}{20} = \frac{27}{20} = 1{,}35\)."),
        inv("Wat is de mediaan van het aantal broers en zussen?", ["1", "een", "één"], "Het 10de en 11de gegeven zijn allebei 1."),
        inv("Wat is de relatieve frequentie van twee broers of zussen, in procent?", ["25", "25%", "25 %"], r"\(5 : 20 = 0{,}25\)."),
    ]),
    mk(r"Bij de getallen \(4, 5, 6\) komt een uitschieter \(100\). Welke maat verandert het meest?",
       ["het gemiddelde", "de mediaan", "de modus", "geen van de drie maten"], 0, r"Het gemiddelde springt van \(5\) naar \(28{,}75\), de mediaan van \(5\) naar \(5{,}5\)."),
    keuze("In een bedrijf verdient één directeur heel veel. Over het loon van een gewone werknemer zegt [[*de mediaan|het gemiddelde]] het meest.",
          "De mediaan trekt zich niets aan van één uitschieter."),
    mk("Twee klassen halen gemiddeld 14 op 20. In klas A is de standaardafwijking 1, in klas B 4. Wat klopt?",
       ["in B liggen de punten verder uiteen", "klas B heeft betere punten dan A", "in A liggen de punten verder uiteen", "de twee klassen zijn in alles precies gelijk"], 0,
       "Een grotere standaardafwijking: de punten liggen verder van het gemiddelde."),
    inv("Van 25 leerlingen komt 36 % met de fiets. Hoeveel leerlingen zijn dat?", ["9", "negen"], r"\(0{,}36 \cdot 25 = 9\)."),
    tabel("Klopt dit over centrum- en spreidingsmaten?",
          [("De mediaan is altijd een van de gegevens.", F), ("Het gemiddelde kan een waarde zijn die niemand heeft.", J),
           ("Bij een symmetrische verdeling liggen gemiddelde en mediaan dicht bij elkaar.", J), ("Een boxplot toont elk afzonderlijk gegeven.", F)],
          "Bij een even aantal gegevens is de mediaan het gemiddelde van twee middelste. Een boxplot vat samen in vijf getallen.",
          kolommen=["Juist", "Fout"]),
    sleep("In een boxplot ligt [[50]] % van de gegevens in de doos. De streep in de doos is de [[mediaan]].",
          ["25", "modus"], "De doos loopt van Q1 tot Q3."),
    mk("Een krant kopt: 'Aantal diefstallen verdubbeld!' Het ging van 2 naar 4. Wat is het probleem met die kop?",
       ["het gaat om heel kleine aantallen", "verdubbelen is wiskundig fout hier", "de krant had procenten moeten weglaten", "4 is niet het dubbele van 2"], 0,
       "Bij kleine aantallen lijkt een verandering groot. Kijk altijd hoeveel gegevens erachter zitten."),
    inv("Het gemiddelde van vijf getallen is 8. Vier ervan zijn 6, 7, 9 en 10. Wat is het vijfde?", ["8", "acht"], r"\(5 \cdot 8 = 40\) en \(40 - 32 = 8\)."),
    open_("Leg uit waarom je bij een kleine groep met een uitschieter beter de mediaan gebruikt dan het gemiddelde. Geef een voorbeeld.",
          r"Een uitschieter trekt het gemiddelde mee, de mediaan niet. Zakgeld \(5, 5, 6, 7, 100\) euro: het gemiddelde is \(24{,}60\) euro, maar vier van de vijf krijgen veel minder. De mediaan, \(6\) euro, toont beter wat gewoon is."),
    met_prent(UM, inv("Hoeveel procentpunten meer tevreden klanten heeft merk B dan merk A?", ["4", "4%", "4 %"],
                      r"\(96 - 92 = 4\) procentpunten.")),
    keuze("In grafiek 2 lijkt merk B [[*veel|een beetje]] beter, omdat de verticale as begint bij [[*90|0]].", "Een afgeknotte as vergroot kleine verschillen."),
    mk("Welke maat past het best bij de favoriete kleur van de leerlingen in een klas?",
       ["de modus", "het gemiddelde", "de mediaan", "de standaardafwijking"], 0, "Bij categorische gegevens kan je niet rekenen of ordenen: enkel tellen."),
    inv(r"Wat is de variatiebreedte van \(-3, 5, 12, 7\)?", ["15", "vijftien"], r"\(12 - (-3) = 15\)."),
]
