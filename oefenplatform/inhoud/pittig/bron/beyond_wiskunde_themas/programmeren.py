"""Programmeren: algoritmen en structuren — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_vak, DONKER, RAND

CODE = "programmeren-code-bey"
_REGELS = [
    "def faculteit(n):",
    "    if n == 0:",
    "        return 1",
    "    return n * faculteit(n - 1)",
    "",
    "def som_lijst(getallen):",
    "    totaal = 0",
    "    for g in getallen:",
    "        totaal = g",
    "    return totaal",
]
X0, Y0, RH = 150, 62, 54


def _code():
    d = [s_vak(60, 30, 880, len(_REGELS) * RH + 30, vul="#fffdf7", rand=RAND, rond=14)]
    for i, t in enumerate(_REGELS):
        y = Y0 + i * RH + 30
        d.append(f'<text x="{X0 - 30}" y="{y}" font-family="DejaVu Sans Mono, Consolas, monospace" font-size="24" fill="#9a9a8a" text-anchor="end">{i + 1}</text>')
        t = t.replace(" ", " ")
        d.append(f'<text x="{X0}" y="{y}" font-family="DejaVu Sans Mono, Consolas, monospace" font-size="27" fill="{DONKER}">{t}</text>')
    return d


def _regel(nr):
    y = Y0 + (nr - 1) * RH
    return pix_zone(X0 - 60, y, 780, RH)


GRAFIEKEN = [dict(naam=CODE, titel="Twee functies in Python, met regelnummers", eigen=_code)]
PRENTEN = [dict(bestand=f"{CODE}.svg", zelf=True, wat="Python-code met een recursieve faculteit en een foute som van een lijst", vragen="klikvragen over stopgeval en debuggen")]

VRAGEN = [
    klik(
        "Klik op een regel van het stopgeval van de recursieve functie.",
        f"{CODE}.svg",
        [_regel(2), _regel(3)],
        "Voor n = 0 roept de functie zichzelf niet meer op.",
    ),
    klik(
        "De functie som_lijst geeft een verkeerd resultaat. Klik op de regel met de fout.",
        f"{CODE}.svg",
        [_regel(9)],
        "Er moet totaal = totaal + g staan: nu onthoudt de lus enkel het laatste getal.",
    ),
    met_prent(f"{CODE}.svg", inv(
        "Wat geeft faculteit(4) terug?",
        ["24", "vierentwintig"],
        r"\(4 \cdot 3 \cdot 2 \cdot 1 \cdot 1\).",
    )),
    met_prent(f"{CODE}.svg", inv(
        "Wat geeft de foute versie van som_lijst([2, 5, 7]) terug?",
        ["7", "zeven"],
        "Bij elke stap wordt totaal overschreven; na de lus is het het laatste element.",
    )),
    met_prent(f"{CODE}.svg", tabel(
        "Kijk naar de code. Juist of fout?",
        [("faculteit(n) roept zichzelf op met een kleinere waarde.", J), ("Zonder regel 2 en 3 zou faculteit nooit stoppen.", J), ("De variabele totaal wordt in regel 7 aangemaakt.", J), ("som_lijst([]) geeft een foutmelding.", F)],
        "Bij een lege lijst loopt de lus niet en geeft de functie 0 terug.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        "Wat drukt Python af?",
        [(r"\(\texttt{print(len('wiskunde'))}\)", "8"), (r"\(\texttt{print(17 \% 5)}\)", "2"), (r"\(\texttt{print([4, 7, 9][-1])}\)", "9"), (r"\(\texttt{print(sum(range(2, 10, 3)))}\)", "15")],
        r"\(\texttt{range(2, 10, 3)}\) geeft 2, 5 en 8. Index \(-1\) is het laatste element.",
        kolommen=["8", "2", "9", "15"],
    ),
    casus(
        r"Bekijk deze code: \(\texttt{n = 10}\), \(\texttt{teller = 0}\), en dan \(\texttt{while n > 1:}\) met daarin \(\texttt{n = n // 2}\) en \(\texttt{teller = teller + 1}\).",
        [
            inv("Welke waarden krijgt n na elkaar? Schrijf de laatste.", ["1", "een", "één"], "10, 5, 2 en 1: dan is de voorwaarde niet meer waar."),
            inv("Wat is teller op het einde?", ["3", "drie"], "Drie keer door de lus."),
            mk("Waarom stopt deze lus zeker?", ["n wordt elke keer kleiner en blijft geheel", "teller wordt elke keer groter en stopt de lus", "een while-lus stopt altijd na tien stappen", "10 is een even getal en deelt dus netjes door 2"], 0,
               "Een geheel getal dat elke stap daalt, komt na eindig veel stappen onder 2."),
        ],
    ),
    sorteer(
        "Welke datastructuur kies je?",
        ["list", "tuple", "set", "dictionary"],
        [("een rij toetsresultaten die je nog aanvult", "list"), ("de coördinaten van een vast punt", "tuple"), ("alle verschillende woorden in een tekst", "set"),
         ("bij elke leerling zijn punt opzoeken", "dictionary"), ("een wachtrij waarvan je de volgorde bijhoudt en wijzigt", "list"), ("het aantal keer dat elke letter voorkomt", "dictionary")],
        "Moet je opzoeken met een sleutel? Dictionary. Alleen verschillende waarden? Set. Niet wijzigen? Tuple.",
    ),
    mk(
        r"Wat gebeurt er bij \(\texttt{t = (1, 2, 3)}\) gevolgd door \(\texttt{t[0] = 5}\)?",
        ["je krijgt een foutmelding", "t wordt dan (5, 2, 3)", "t wordt dan (5, 1, 2, 3)", "er gebeurt helemaal niets"],
        0,
        "Een tuple kan je achteraf niet wijzigen.",
    ),
    inv(
        r"Na \(\texttt{d = \{'a': 1, 'b': 2\}}\) en \(\texttt{d['c'] = 3}\): hoeveel is \(\texttt{len(d)}\)?",
        ["3", "drie"],
        "Er komt een nieuwe sleutel bij.",
    ),
    mk(
        "Je zoekt een getal in een gesorteerde lijst van een miljoen getallen door telkens de helft te schrappen. Hoeveel stappen heb je hoogstens nodig?",
        ["20", "1000", "500 000", "6"],
        0,
        r"\(2^{20} \approx 1\,000\,000\): na 20 halveringen blijft er één getal over.",
    ),
    mk(
        "Een algoritme met twee geneste lussen over n elementen doet ongeveer n² stappen. Hoeveel keer langer duurt het als n tien keer groter wordt?",
        ["100 keer", "10 keer", "20 keer", "1000 keer"],
        0,
        r"\((10n)^{2} = 100n^{2}\).",
    ),
    koppel(
        "Verbind de techniek met de uitleg.",
        [("recursie", "een functie die zichzelf oproept"), ("verdeel-en-heers", "opsplitsen in deelproblemen en de oplossingen samenvoegen"), ("dynamisch programmeren", "tussenresultaten bewaren om ze niet opnieuw te berekenen"), ("numerieke methode", "een antwoord benaderen met rekenstappen")],
        ["een programma zonder lussen"],
        "Dynamisch programmeren ruilt geheugen voor tijd.",
    ),
    mk(
        "Een recursieve functie berekent het n-de Fibonaccigetal en roept zichzelf telkens twee keer op. Waarom wordt ze zo traag voor grote n?",
        ["tussenwaarden worden steeds opnieuw berekend", "Python kan geen heel grote getallen optellen", "de functie heeft dan geen stopgeval meer nodig", "elke oproep maakt eerst een nieuwe lijst aan"],
        0,
        "Bewaar je de tussenresultaten, dan wordt het veel sneller: dynamisch programmeren.",
    ),
    inv(
        r"Een programma benadert \(\int_{0}^{1} x\,dx\) met \(n = 4\) en \(\sum f(x_{i})\,\Delta x\), met \(x_{i}\) de rechtergrens van elk deelinterval. Wat geeft het? Geef een decimaal getal.",
        ["0,625", "0.625"],
        r"\(\Delta x = 0{,}25\) en \((0{,}25 + 0{,}5 + 0{,}75 + 1) \cdot 0{,}25\).",
    ),
    volgorde(
        "Zet de stappen om een probleem met een programma op te lossen in volgorde.",
        ["het probleem analyseren", "een algoritme ontwerpen", "het programma schrijven", "testen en debuggen"],
        "Eerst denken, dan typen.",
    ),
    tabel(
        "Over Python: juist of fout?",
        [(r"\(\texttt{3 > 2 and 1 > 2}\) is \(\texttt{True}\).", F), (r"\(\texttt{range(5)}\) loopt van 0 tot en met 4.", J), (r"\(\texttt{x = x + 1}\) is in Python een vergelijking zonder oplossing.", F), (r"Een functie zonder \(\texttt{return}\) geeft \(\texttt{None}\) terug.", J)],
        r"\(\texttt{=}\) is een toekenning, geen gelijkheid. \(\texttt{and}\) vraagt dat beide delen waar zijn.",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        r"Een algoritme is [[*correct|eindig]] als het voor elke toegelaten invoer het juiste antwoord geeft. Het is [[*eindig|correct]] als het altijd stopt.",
        "Je moet allebei kunnen beargumenteren.",
    ),
    sleep(
        r"Grafieken teken je met [[matplotlib]], toevalsgetallen haal je uit [[random]] en met grote rijen getallen reken je vlot in [[numpy]].",
        ["pandas", "math"],
        "Dat zijn de drie bibliotheken die je mag gebruiken.",
    ),
    mk(
        r"Wat drukt dit af: \(\texttt{lijst = [3, 1, 2]}\), \(\texttt{lijst.append(5)}\), \(\texttt{print(lijst)}\)?",
        [r"\(\texttt{[3, 1, 2, 5]}\)", r"\(\texttt{[5, 3, 1, 2]}\)", r"\(\texttt{[1, 2, 3, 5]}\)", r"\(\texttt{[3, 1, 2]}\)"],
        0,
        r"\(\texttt{append}\) zet het nieuwe element achteraan.",
    ),
    inv(
        r"Hoeveel keer drukt \(\texttt{for i in range(3):}\) met daarin \(\texttt{for j in range(4):}\) en \(\texttt{print(i, j)}\) iets af?",
        ["12", "twaalf"],
        r"De binnenste lus loopt 4 keer voor elk van de 3 waarden van \(i\).",
    ),
    sorteer(
        "Welk soort fout is het?",
        ["Syntaxfout", "Logische fout"],
        [(r"een vergeten dubbelpunt na \(\texttt{if}\)", "Syntaxfout"), ("de som van een lijst start bij 1 in plaats van 0", "Logische fout"), ("een haakje dat nooit gesloten wordt", "Syntaxfout"),
         (r"\(\texttt{range(1, n)}\) waar \(\texttt{range(1, n + 1)}\) moest staan", "Logische fout"), ("een verkeerd ingesprongen regel na for", "Syntaxfout"), ("een gemiddelde dat door het verkeerde aantal deelt", "Logische fout")],
        "Een syntaxfout stopt het programma meteen. Een logische fout loopt wel, maar geeft een verkeerd resultaat.",
    ),
    mk(
        r"Waarom test je \(\texttt{gemiddelde(lijst)}\) ook met een lege lijst?",
        ["omdat je dan door nul deelt", "omdat een lege lijst het snelst door de lus gaat", "omdat Python lege lijsten niet kan aanmaken", "omdat het gemiddelde dan altijd netjes 0 is"],
        0,
        "Randgevallen verstoppen de meeste fouten.",
    ),
    inv(
        r"Wat drukt \(\texttt{print(len(set('banaan')))}\) af?",
        ["3", "drie"],
        "De verschillende letters zijn b, a en n.",
    ),
    mk(
        r"Welke code telt hoeveel getallen in \(\texttt{lijst}\) groter zijn dan 10?",
        [r"\(\texttt{sum(1 for g in lijst if g > 10)}\)", r"\(\texttt{len(g for g in lijst) > 10}\)", r"\(\texttt{sum(g for g in lijst) > 10}\)", r"\(\texttt{max(lijst) - min(lijst) > 10}\)"],
        0,
        "Voor elk getal dat aan de voorwaarde voldoet, tel je 1 op.",
    ),
    tabel(
        "Hoeveel stappen doet het algoritme ongeveer voor een lijst met n elementen?",
        [("het grootste element zoeken door alles één keer te bekijken", "n"), ("elk paar elementen met elkaar vergelijken", "n²"), ("binair zoeken in een gesorteerde lijst", r"\(\log_{2} n\)")],
        "Hoe trager de groei, hoe beter het algoritme schaalt.",
        kolommen=["n", "n²", r"\(\log_{2} n\)"],
    ),
    inv(
        r"Wat drukt \(\texttt{print(7 // 2)}\) af?",
        ["3", "drie"],
        r"\(\texttt{//}\) is de gehele deling: de rest valt weg.",
    ),
    mk(
        "Een functie moet het kleinste getal uit een lijst teruggeven. Welke start voor de variabele kleinste is veilig?",
        ["het eerste element", "het getal 0 als begin", "het getal 1000 als begin", "het laatste getal min 1"],
        0,
        "Met 0 of 1000 als start gaat het mis bij een lijst met enkel grote of enkel negatieve getallen.",
    ),
]
