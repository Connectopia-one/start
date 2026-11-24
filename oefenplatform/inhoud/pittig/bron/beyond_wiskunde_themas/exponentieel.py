"""Exponentiële en logaritmische functies — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("exponentieel-verval-bey", 0, 15, 0, 900, 1, 100)


def _n(t):
    return 800 * 0.5 ** (t / 3)


GRAFIEKEN = [
    dict(naam=GRAF, titel="Een geneesmiddel in het bloed", krommen=[(_n, "groen", "N", (0, 15))], labelplek={"N": (1.5, 760)},
         xlabel="uren", ylabel="mg"),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="exponentieel verval 800 · (1/2)^(t/3)", vragen="klikvragen over halveringstijd en aflezen")]

VRAGEN = [
    klik(
        "Klik op het punt van de grafiek dat de halveringstijd toont.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3, 400)],
        "Na 3 uur is de hoeveelheid gehalveerd van 800 naar 400 mg.",
    ),
    klik(
        "Klik op het punt waar nog een achtste van de beginhoeveelheid over is.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 9, 100)],
        r"Een achtste is drie keer halveren: \(3 \cdot 3 = 9\) uur, \(100\) mg.",
    ),
    klik(
        "Klik in de strook van de tijd waarin er meer dan 200 mg in het bloed is.",
        f"{GRAF}.svg",
        [strook_zone(GRAF, 0.2, 5.8)],
        "200 mg is een kwart van 800: na twee halveringen, dus na 6 uur. Daarvoor is er meer.",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafiek van de exponentiële functie. Juist of fout?",
        [("Elk uur verdwijnt evenveel mg.", F), ("De grafiek heeft de horizontale asymptoot y = 0.", J), ("Na 15 uur is er 25 mg over.", J), ("De groeifactor per uur is 0,5.", F)],
        r"Per 3 uur is de factor \(0{,}5\), per uur \(0{,}5^{1/3} \approx 0{,}79\). Na 15 uur: \(800 \cdot 0{,}5^{5} = 25\).",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{GRAF}.svg", mk(
        "Kijk naar de grafiek. Welk voorschrift past?",
        [r"\(N(t) = 800 \cdot 0{,}5^{t/3}\)", r"\(N(t) = 800 \cdot 0{,}5^{3t}\)", r"\(N(t) = 800 - 133t\)", r"\(N(t) = 800 \cdot 3^{-t}\)"],
        0,
        "Beginwaarde 800 en halveren om de 3 uur.",
    )),
    tabel(
        "Lineair of exponentieel?",
        [("1, 4, 7, 10, 13", "lineair"), ("5, 10, 20, 40, 80", "exponentieel"), ("1000, 900, 810, 729", "exponentieel"), ("50, 45, 40, 35", "lineair"), ("2, 6, 18, 54", "exponentieel")],
        "Lineair: telkens hetzelfde verschil. Exponentieel: telkens dezelfde factor.",
        kolommen=["lineair", "exponentieel"],
    ),
    mk(
        r"Een bedrag groeit met 2 % per maand. Met hoeveel procent groeit het per jaar?",
        [r"ongeveer \(26{,}8\,\%\)", r"\(24\,\%\)", r"ongeveer \(12{,}7\,\%\)", r"\(2\,\%\)"],
        0,
        r"\(1{,}02^{12} \approx 1{,}268\). Samengestelde groei is meer dan \(12 \cdot 2\,\%\).",
    ),
    inv(
        r"Een stad groeit 4 % per jaar. Na hoeveel volle jaren is de bevolking voor het eerst verdubbeld?",
        ["18"],
        r"\(t = \dfrac{\ln 2}{\ln 1{,}04} \approx 17{,}7\), dus na \(18\) jaar.",
    ),
    koppel(
        "Verbind de functie met haar asymptoot.",
        [(r"\(y = 2^{x} - 3\)", r"\(y = -3\)"), (r"\(y = \log_{2}(x - 3)\)", r"\(x = 3\)"), (r"\(y = 5 \cdot 0{,}5^{x}\)", r"\(y = 0\)"), (r"\(y = \ln x + 3\)", r"\(x = 0\)")],
        [r"\(y = 3\)"],
        "Een exponentiële functie heeft een horizontale, een logaritmische een verticale asymptoot.",
    ),
    tabel(
        "Over exponentiële en logaritmische functies: juist of fout?",
        [(r"De grafiek van \(\left(\tfrac{1}{3}\right)^{x}\) is het spiegelbeeld van \(3^{x}\) om de y-as.", J),
         (r"\(\log_{1/2}x\) is stijgend.", F),
         (r"\(e^{x}\) en \(\ln x\) snijden elkaar.", F),
         (r"\(2^{x} > x\) voor elke reële \(x\).", J),
         (r"\(\ln x < 0\) voor \(0 < x < 1\).", J)],
        r"\(\left(\tfrac{1}{3}\right)^{x} = 3^{-x}\). Een logaritme met grondtal tussen 0 en 1 daalt. \(e^{x}\) ligt boven \(y = x\), \(\ln x\) eronder.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        r"Een auto van 30 000 euro verliest elk jaar 15 % van zijn waarde.",
        [
            mk("Welk model past?", [r"\(W(t) = 30\,000 \cdot 0{,}85^{t}\)", r"\(W(t) = 30\,000 \cdot 1{,}15^{t}\)", r"\(W(t) = 30\,000 - 4500t\)", r"\(W(t) = 30\,000 \cdot 0{,}15^{t}\)"], 0, "15 % eraf: groeifactor 0,85."),
            mk("Wat is de waarde na 4 jaar, afgerond?", ["15 660 euro", "12 000 euro", "18 000 euro", "25 500 euro"], 0, r"\(30\,000 \cdot 0{,}85^{4} \approx 15\,660\)."),
            inv("Na hoeveel volle jaren is de auto voor het eerst minder dan de helft waard?", ["5"], r"\(0{,}85^{t} < 0{,}5\) geeft \(t > \tfrac{\ln 0{,}5}{\ln 0{,}85} \approx 4{,}27\)."),
        ],
    ),
    mk(
        r"Wat is het domein van \(f(x) = \log_{3}(4 - x^{2})\)?",
        [r"\(\left]-2, 2\right[\)", r"\(\left[-2, 2\right]\)", r"\(\left]-\infty, -2\right[ \cup \left]2, +\infty\right[\)", r"\(\left]0, +\infty\right[\)"],
        0,
        r"\(4 - x^{2} > 0\) geeft \(-2 < x < 2\).",
    ),
    sorteer(
        "Stijgend of dalend?",
        ["Stijgend", "Dalend"],
        [(r"\(y = 0{,}7^{x}\)", "Dalend"), (r"\(y = e^{-x}\)", "Dalend"), (r"\(y = \log_{5}x\)", "Stijgend"), (r"\(y = -\ln x\)", "Dalend"), (r"\(y = 1{,}01^{x}\)", "Stijgend"), (r"\(y = \log_{0{,}2}x\)", "Dalend")],
        r"Grondtal groter dan 1: stijgend. Tussen 0 en 1: dalend. Een minteken ervoor keert om.",
    ),
    inv(
        r"De grafiek van \(f(x) = a \cdot b^{x}\) gaat door \((0, 3)\) en \((2, 48)\). Hoeveel is \(b\)?",
        ["4"],
        r"\(a = 3\) en \(3b^{2} = 48\), dus \(b^{2} = 16\) en \(b = 4\) (een grondtal is positief).",
    ),
    keuze(
        r"Bij exponentiële groei komt er per tijdseenheid [[*een vast percentage|een vast aantal]] bij. De grafiek is dan [[*hol|bol]] en stijgt steeds sneller.",
        "Een vast percentage van een steeds groter getal geeft steeds grotere sprongen.",
    ),
    mk(
        r"Een bacteriekolonie verdrievoudigt elke 4 uur. Hoe groot is de groeifactor per uur?",
        [r"\(3^{1/4} \approx 1{,}32\)", r"\(\tfrac{3}{4}\)", r"\(3^{4} = 81\)", r"\(1{,}75\)"],
        0,
        r"\(g^{4} = 3\), dus \(g = \sqrt[4]{3}\).",
    ),
    tabel(
        "Welke transformatie brengt de grafiek van y = 2ˣ naar de gegeven grafiek?",
        [(r"\(y = 2^{x + 1}\)", "1 naar links"), (r"\(y = 2^{x} + 1\)", "1 naar boven"), (r"\(y = -2^{x}\)", "spiegelen om de x-as"), (r"\(y = 2^{-x}\)", "spiegelen om de y-as")],
        r"\(2^{x + 1} = 2 \cdot 2^{x}\): dat is ook verticaal uitrekken met 2.",
        kolommen=["1 naar links", "1 naar boven", "spiegelen om de x-as", "spiegelen om de y-as"],
    ),
    inv(
        r"Los op: \(\ln(x - 2) = 1\). Rond af op twee cijfers na de komma.",
        ["4,72", "4.72"],
        r"\(x - 2 = e\), dus \(x = e + 2 \approx 4{,}72\).",
    ),
    mk(
        r"De pH is \(-\log[H^{+}]\). Hoe verandert \([H^{+}]\) als de pH daalt van 6 naar 4?",
        ["ze wordt 100 keer zo groot", "ze wordt 2 keer zo groot", "ze wordt 100 keer zo klein", "ze daalt met 2"],
        0,
        r"\([H^{+}] = 10^{-pH}\): van \(10^{-6}\) naar \(10^{-4}\).",
    ),
    sleep(
        r"De grafieken van \(a^{x}\) en \(\log_{a}x\) zijn elkaars spiegelbeeld om [[\(y = x\)]]. Het punt \((0, 1)\) van de ene wordt [[\((1, 0)\)]] op de andere.",
        [r"de \(y\)-as", r"\((0, -1)\)"],
        "Inverse functies wisselen x en y.",
    ),
    volgorde(
        "Zet van traag naar snel groeiend voor grote x.",
        [r"\(\ln x\)", r"\(\sqrt{x}\)", r"\(x^{3}\)", r"\(2^{x}\)"],
        "Een logaritme groeit het traagst, een exponentiële functie wint uiteindelijk van elke macht.",
    ),
    mk(
        r"In 2020 waren er 120 dieren, in 2025 waren er 180. Bij exponentiële groei: hoeveel in 2030?",
        ["270", "240", "225", "360"],
        0,
        r"In 5 jaar factor \(1{,}5\). Nog eens 5 jaar: \(180 \cdot 1{,}5 = 270\).",
    ),
    tabel(
        r"Bereken met het rekentoestel. Welke waarde klopt, afgerond?",
        [(r"\(e^{2}\)", "7,39"), (r"\(\ln 10\)", "2,30"), (r"\(\log_{2}10\)", "3,32")],
        r"\(\log_{2}10 = \tfrac{\ln 10}{\ln 2}\).",
        kolommen=["7,39", "2,30", "3,32"],
    ),
    inv(
        r"Een kopje koffie koelt af: \(T(t) = 20 + 60 \cdot 0{,}9^{t}\) (°C, t in minuten). Welke temperatuur nadert de koffie op lange termijn?",
        ["20", "20 °C", "20°C"],
        r"\(0{,}9^{t} \to 0\), dus \(T \to 20\): de kamertemperatuur is de horizontale asymptoot.",
    ),
    mk(
        r"Welke functie heeft de grafiek die door \((1, 0)\) en \((4, 2)\) gaat?",
        [r"\(\log_{2}x\)", r"\(\log_{4}x\)", r"\(2^{x} - 2\)", r"\(\ln x\)"],
        0,
        r"\(\log_{2}1 = 0\) en \(\log_{2}4 = 2\).",
    ),
    sorteer(
        "Hoort de uitspraak bij de grafiek van a^x of bij die van log_a x?",
        ["a^x", "log_a x"],
        [("domein ℝ", "a^x"), ("bereik ℝ", "log_a x"), ("gaat door (0, 1)", "a^x"), ("verticale asymptoot", "log_a x"), ("altijd positief", "a^x")],
        "De rollen van domein en bereik wisselen bij inverse functies.",
    ),
    inv(
        r"Een lening van 5000 euro groeit met 6 % per jaar samengestelde intrest. Hoeveel euro is ze na 3 jaar, afgerond op een euro?",
        ["5955", "5 955"],
        r"\(5000 \cdot 1{,}06^{3} = 5955{,}08\).",
    ),
    tabel(
        r"Over \(f(x) = 3 - 2^{x}\). Juist of fout?",
        [(r"Het bereik is \(\left]-\infty, 3\right[\)", J), (r"f is dalend.", J), (r"f heeft nulwaarde \(\log_{2}3\).", J), (r"De horizontale asymptoot is \(y = 0\).", F)],
        r"\(2^{x}\) gespiegeld om de x-as en 3 omhoog: asymptoot \(y = 3\).",
        kolommen=["Juist", "Fout"],
    ),
]
