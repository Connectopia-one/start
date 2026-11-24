"""Telproblemen en het binomium — pittig (🌍 Beyond doorstroom)."""
from math import comb
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst

PASCAL = "tellen-pascal-bey"


def _plek(n, k):
    return 500 + (k - n / 2) * 120, 80 + n * 82


def _pascal():
    d = []
    for n in range(7):
        x0, y = _plek(n, 0)
        d.append(s_tekst(60, y + 7, f"n = {n}", grootte=20, anker="start", kleur="#7a7a6a"))
        for k in range(n + 1):
            x, y = _plek(n, k)
            d.append(s_tekst(x, y + 9, str(comb(n, k)), grootte=28, vet=True))
    return d


def _zone(n, k):
    x, y = _plek(n, k)
    return pix_zone(x - 40, y - 30, 80, 60)


GRAFIEKEN = [dict(naam=PASCAL, titel="De driehoek van Pascal, rij 0 tot rij 6", eigen=_pascal)]
PRENTEN = [dict(bestand=f"{PASCAL}.svg", zelf=True, wat="driehoek van Pascal tot rij 6", vragen="klikvragen over binomiaalcoëfficiënten")]

VRAGEN = [
    klik(
        r"Klik op de coëfficiënt van \(a^{3}b^{3}\) in \((a + b)^{6}\).",
        f"{PASCAL}.svg",
        [_zone(6, 3)],
        r"\(\binom{6}{3} = 20\), het middelste getal van rij 6.",
    ),
    klik(
        r"Klik op een getal dat gelijk is aan \(\binom{5}{2}\).",
        f"{PASCAL}.svg",
        [_zone(5, 2), _zone(5, 3)],
        r"\(\binom{5}{2} = \binom{5}{3} = 10\): de rij is symmetrisch.",
    ),
    klik(
        r"Klik op het getal dat telt op hoeveel manieren je 2 personen kiest uit 4.",
        f"{PASCAL}.svg",
        [_zone(4, 2)],
        r"\(\binom{4}{2} = 6\), in rij 4.",
    ),
    met_prent(f"{PASCAL}.svg", tabel(
        "Kijk naar de driehoek van Pascal. Juist of fout?",
        [(r"De getallen van rij 6 tellen samen op tot 64.", J), (r"Elk getal binnen in de driehoek is de som van de twee getallen schuin erboven.", J), (r"In rij 5 staat het getal 5 maar één keer.", F), (r"Rij 4 geeft de coëfficiënten van \((a + b)^{3}\).", F)],
        r"Rij \(n\) hoort bij \((a + b)^{n}\) en telt op tot \(2^{n}\).",
        kolommen=["Juist", "Fout"],
    )),
    sorteer(
        "Welk telprobleem is het?",
        ["Variatie", "Combinatie", "Herhalingsvariatie"],
        [("Een voorzitter, een secretaris en een penningmeester kiezen uit 12 leden", "Variatie"), ("Een jury van 3 kiezen uit 12 kandidaten", "Combinatie"), ("Een pincode van 4 cijfers", "Herhalingsvariatie"),
         ("Goud, zilver en brons verdelen onder 8 lopers", "Variatie"), ("5 kaarten trekken uit een spel van 52", "Combinatie"), ("Een wachtwoord van 3 letters, herhaling toegelaten", "Herhalingsvariatie")],
        "Telt de volgorde? Dan variatie. Mag herhalen? Dan herhalingsvariatie.",
    ),
    tabel(
        "Hoeveel mogelijkheden?",
        [("voorzitter, secretaris en penningmeester uit 12 leden", "1320"), ("een jury van 3 uit 12 kandidaten", "220"), ("een code van 4 verschillende cijfers", "5040"), ("woorden met de letters van BANAAN", "60")],
        r"\(12 \cdot 11 \cdot 10\), \(\binom{12}{3}\), \(10 \cdot 9 \cdot 8 \cdot 7\) en \(\tfrac{6!}{3!\,2!}\).",
        kolommen=["1320", "220", "5040", "60"],
    ),
    inv(
        "Een werkgroep heeft 2 jongens uit 5 en 2 meisjes uit 4. Hoeveel verschillende werkgroepen zijn er?",
        ["60", "zestig"],
        r"Productregel: \(\binom{5}{2} \cdot \binom{4}{2} = 10 \cdot 6\).",
    ),
    casus(
        "Je kiest 3 leerlingen uit een groep van 5 jongens en 4 meisjes.",
        [
            inv("Hoeveel groepjes zijn er in totaal?", ["84"], r"\(\binom{9}{3}\)."),
            inv("Hoeveel groepjes hebben geen enkel meisje?", ["10", "tien"], r"\(\binom{5}{3}\)."),
            inv("Hoeveel groepjes hebben minstens één meisje?", ["74"], "Complementregel: alle groepjes min die zonder meisje."),
        ],
    ),
    mk(
        r"Wat is de coëfficiënt van \(x^{3}\) in \((2x - 1)^{5}\)?",
        ["80", "−80", "10", "40"],
        0,
        r"\(\binom{5}{3}(2x)^{3}(-1)^{2} = 10 \cdot 8\,x^{3}\).",
    ),
    inv(
        r"Wat is de term zonder \(x\) in \(\left(x + \tfrac{1}{x}\right)^{6}\)? Schrijf het getal.",
        ["20", "twintig"],
        r"De algemene term is \(\binom{6}{k}x^{6 - 2k}\); \(6 - 2k = 0\) geeft \(k = 3\).",
    ),
    mk(
        r"Wat is de coëfficiënt van \(x^{2}\) in \((1 - 3x)^{4}\)?",
        ["54", "−54", "18", "6"],
        0,
        r"\(\binom{4}{2}(-3)^{2} = 6 \cdot 9\). Het minteken valt weg door het kwadraat.",
    ),
    inv(
        "Hoeveel diagonalen heeft een regelmatige achthoek?",
        ["20", "twintig"],
        r"Elk paar hoekpunten geeft een lijnstuk: \(\binom{8}{2} = 28\). Daarvan zijn 8 zijden.",
    ),
    mk(
        "Op een rooster wandel je van linksonder naar rechtsboven: 4 stappen naar rechts en 3 naar boven. Hoeveel kortste wegen zijn er?",
        ["35", "12", "7", "70"],
        0,
        r"Kies welke 3 van de 7 stappen naar boven gaan: \(\binom{7}{3}\).",
    ),
    tabel(
        "Over binomiaalcoëfficiënten: juist of fout?",
        [(r"\(\binom{6}{2} + \binom{6}{3} = \binom{7}{3}\)", J), (r"\(\binom{10}{7} = \binom{10}{3}\)", J), (r"\(\binom{n}{2} = \dfrac{n(n - 1)}{2}\)", J), (r"\((a - b)^{4}\) heeft 5 termen die allemaal positief zijn.", F), (r"\(\binom{8}{4} = 2 \cdot \binom{4}{2}\)", F)],
        r"Bij \((a - b)^{n}\) wisselen de tekens. \(\binom{8}{4} = 70\).",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Bereken \(\sum_{k=1}^{4} k^{2}\).",
        ["30", "dertig"],
        r"\(1 + 4 + 9 + 16\).",
    ),
    mk(
        r"Welke som is gelijk aan \(\sum_{k=0}^{5}\binom{5}{k}\)?",
        [r"\(2^{5}\)", r"\(5!\)", r"\(5^{2}\)", r"\(\binom{10}{5}\)"],
        0,
        r"Vul \(a = b = 1\) in \((a + b)^{5}\) in.",
    ),
    volgorde(
        r"Zet de stappen om de coëfficiënt van \(x^{4}\) in \((x + 2)^{7}\) te vinden in volgorde.",
        [r"schrijf de algemene term \(\binom{7}{k}x^{7 - k}2^{k}\)", r"stel \(7 - k = 4\), dus \(k = 3\)", r"bereken \(\binom{7}{3} = 35\) en \(2^{3} = 8\)", r"vermenigvuldig: 280"],
        "Zo hoef je niet de hele macht uit te werken.",
    ),
    koppel(
        "Verbind de vraag met de juiste formule.",
        [("rangschik 6 verschillende boeken", r"\(6!\)"), ("kies 2 uit 6 zonder volgorde", r"\(\binom{6}{2}\)"), ("kies 2 uit 6 met volgorde", r"\(6 \cdot 5\)"), ("een code van 2 tekens uit 6, herhaling mag", r"\(6^{2}\)")],
        [r"\(2^{6}\)"],
        "Volgorde en herhaling bepalen de formule.",
    ),
    mk(
        "Een restaurant biedt 3 soepen of 4 salades als voorgerecht, en 5 hoofdgerechten. Hoeveel menu's met één voorgerecht en één hoofdgerecht zijn er?",
        ["35", "60", "12", "20"],
        0,
        "Somregel voor het voorgerecht (3 + 4), productregel daarna (7 · 5).",
    ),
    keuze(
        r"Bij een combinatie telt de volgorde [[*niet|wel]] mee. Daarom is het aantal combinaties [[*kleiner dan of gelijk aan|groter dan]] het aantal variaties.",
        r"Elke combinatie van \(p\) elementen geeft \(p!\) variaties.",
    ),
    inv(
        "Tien vrienden geven elkaar allemaal één keer een hand. Hoeveel handdrukken zijn dat?",
        ["45"],
        r"\(\binom{10}{2} = \tfrac{10 \cdot 9}{2}\).",
    ),
    sleep(
        r"De algemene term van \((a + b)^{n}\) is [[\(\binom{n}{k}a^{n-k}b^{k}\)]]. De exponenten tellen samen op tot [[n]].",
        [r"\(\binom{n}{k}a^{k}b^{k}\)", "k", "2n"],
        "Elke term heeft graad n.",
    ),
    mk(
        "Op hoeveel manieren kan je 4 verschillende prijzen verdelen onder 3 kinderen, als een kind meer dan één prijs mag krijgen?",
        [r"\(3^{4} = 81\)", r"\(4^{3} = 64\)", r"\(\binom{4}{3} = 4\)", r"\(4 \cdot 3 = 12\)"],
        0,
        "Elke prijs heeft 3 mogelijke kinderen: herhalingsvariatie.",
    ),
    inv(
        "Hoeveel woorden van 5 letters kan je maken met de letters van KAJAK? Ze hoeven niets te betekenen.",
        ["30", "dertig"],
        r"Herhalingspermutatie: \(\tfrac{5!}{2!\,2!} = \tfrac{120}{4}\).",
    ),
    tabel(
        r"Welk teken heeft de term in de uitwerking van \((x - 1)^{5}\)?",
        [(r"de term met \(x^{5}\)", "+"), (r"de term met \(x^{4}\)", "−"), (r"de term met \(x^{2}\)", "+"), (r"de term zonder \(x\)", "−")],
        r"Het teken is dat van \((-1)^{k}\), met \(k = 5 - \) de exponent van \(x\).",
        kolommen=["+", "−"],
    ),
    mk(
        "Hoeveel getallen van 100 tot en met 999 hebben drie verschillende cijfers?",
        ["648", "720", "504", "729"],
        0,
        "Het eerste cijfer mag geen 0 zijn: 9 keuzes, dan 9 en dan 8.",
    ),
    inv(
        r"Bereken \(\dfrac{7!}{5!}\).",
        ["42", "tweeënveertig"],
        r"\(\tfrac{7 \cdot 6 \cdot 5!}{5!} = 7 \cdot 6\).",
    ),
    mk(
        "Vier mensen gaan op een rij staan. Twee van hen willen naast elkaar staan. Hoeveel rijen zijn er mogelijk?",
        ["12", "6", "24", "18"],
        0,
        r"Zie het duo als één blok: \(3!\) rijen, en het duo kan op 2 manieren staan.",
    ),
]
