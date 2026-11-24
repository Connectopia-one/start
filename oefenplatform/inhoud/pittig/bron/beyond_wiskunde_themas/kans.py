"""Kansrekenen en kansverdelingen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import kansboom, pix_zone, s_tekst

BOOM = "kans-machines-bey"
_STUK, _MIDDEN, _KNOPEN = kansboom(
    (90, 320),
    [("A", "0,6", (330, 170)), ("B", "0,4", (330, 470))],
    {"A": [("fout", "0,05", (720, 90)), ("goed", "0,95", (720, 250))],
     "B": [("fout", "0,10", (720, 390)), ("goed", "0,90", (720, 550))]},
)


def _boom():
    return _STUK + [s_tekst(90, 290, "start", 18, kleur="#7a7a6a")]


def _knoop(k):
    x, y = _KNOPEN[k]
    return pix_zone(x - 60, y - 26, 120, 52)


def _tak(k):
    x, y = _MIDDEN[k]
    return pix_zone(x - 70, y - 40, 140, 80)


GRAFIEKEN = [dict(naam=BOOM, titel="Kansboom: machine A of B, stuk goed of fout", eigen=_boom)]
PRENTEN = [dict(bestand=f"{BOOM}.svg", zelf=True, wat="kansboom met twee machines en goede of foute stukken", vragen="klikvragen over paden en voorwaardelijke kansen")]

VRAGEN = [
    klik(
        "Een fabriek heeft twee machines. Klik op het eindpunt van het pad met kans 0,04.",
        f"{BOOM}.svg",
        [_knoop(("B", "fout"))],
        "Vermenigvuldig langs het pad: machine B en daarna een fout stuk.",
    ),
    klik(
        r"Klik op de tak waarop de voorwaardelijke kans \(P(\text{goed} \mid A)\) staat.",
        f"{BOOM}.svg",
        [_tak(("A", "goed"))],
        "Op de tweede takken staan kansen onder voorwaarde van de eerste keuze.",
    ),
    met_prent(f"{BOOM}.svg", inv(
        r"Bereken met de kansboom \(P(\text{fout})\). Geef een decimaal getal.",
        ["0,07", "0.07"],
        r"Tel de twee paden naar een fout stuk op: \(0{,}6 \cdot 0{,}05 + 0{,}4 \cdot 0{,}10\).",
    )),
    met_prent(f"{BOOM}.svg", mk(
        r"Een stuk is fout. Hoe groot is de kans dat het van machine A komt?",
        [r"\(\tfrac{3}{7}\)", r"\(\tfrac{4}{7}\)", r"\(0{,}03\)", r"\(0{,}6\)"],
        0,
        r"\(P(A \mid \text{fout}) = \dfrac{P(A \cap \text{fout})}{P(\text{fout})}\): deel het pad A-fout door de kans op een fout stuk.",
    )),
    met_prent(f"{BOOM}.svg", tabel(
        "Kijk naar de kansboom. Juist of fout?",
        [(r"\(P(A \cap \text{goed}) = 0{,}57\)", J), (r"De kansen op de vier eindpunten tellen op tot 1.", J), (r"\(P(\text{fout} \mid B) = 0{,}04\)", F), (r"Machine en kwaliteit zijn onafhankelijk.", F)],
        r"\(P(\text{fout} \mid B)\) staat op de tak: 0,10. De foutkans hangt af van de machine, dus niet onafhankelijk.",
        kolommen=["Juist", "Fout"],
    )),
    casus(
        "Op een school zijn 120 meisjes en 80 jongens. 90 meisjes en 40 jongens doen aan sport.",
        [
            inv(r"Hoe groot is \(P(\text{sport})\)? Geef een decimaal getal.", ["0,65", "0.65"], r"\(\tfrac{130}{200}\)."),
            mk(r"Hoe groot is \(P(\text{meisje} \mid \text{sport})\)?", [r"\(\tfrac{9}{13}\)", r"\(\tfrac{3}{4}\)", r"\(\tfrac{9}{20}\)", r"\(\tfrac{3}{5}\)"], 0, r"Van de 130 sporters zijn er 90 meisjes."),
            mk("Zijn 'meisje' en 'sport' onafhankelijk?", ["nee, want P(sport | meisje) is 0,75", "ja, want beide kansen zijn groter dan 0,5", "ja, want het zijn twee verschillende kenmerken", "dat kan je niet nagaan in een kruistabel"], 0,
               "Bij onafhankelijkheid verandert de voorwaarde de kans niet, en 0,75 is niet 0,65."),
        ],
    ),
    tabel(
        r"\(P(A) = 0{,}5\), \(P(B) = 0{,}4\) en \(P(A \cap B) = 0{,}2\). Juist of fout?",
        [(r"\(P(A \cup B) = 0{,}7\)", J), (r"\(A\) en \(B\) zijn onafhankelijk.", J), (r"\(A\) en \(B\) sluiten elkaar uit.", F), (r"\(P(A \mid B) = 0{,}8\)", F)],
        r"\(0{,}5 \cdot 0{,}4 = 0{,}2\): onafhankelijk. \(P(A \mid B) = \tfrac{0{,}2}{0{,}4} = 0{,}5\).",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        "Een vaas bevat 3 rode en 2 blauwe knikkers. Je trekt er twee zonder terugleggen. Hoe groot is de kans op twee rode? Schrijf ze als breuk.",
        ["3/10"],
        r"\(\tfrac{3}{5} \cdot \tfrac{2}{4}\).",
    ),
    mk(
        "Je gooit met twee eerlijke dobbelstenen. Hoe groot is de kans op minstens één zes?",
        [r"\(\tfrac{11}{36}\)", r"\(\tfrac{1}{3}\)", r"\(\tfrac{1}{6}\)", r"\(\tfrac{10}{36}\)"],
        0,
        r"Complement: \(1 - \left(\tfrac{5}{6}\right)^{2} = 1 - \tfrac{25}{36}\).",
    ),
    tabel(
        "Twee eerlijke dobbelstenen. Wat is de kans?",
        [("de som is 7", r"\(\tfrac{1}{6}\)"), ("de som is 2", r"\(\tfrac{1}{36}\)"), ("twee dezelfde ogen", r"\(\tfrac{1}{6}\)"), ("de som is 4", r"\(\tfrac{1}{12}\)")],
        r"Er zijn 36 even waarschijnlijke uitkomsten. Som 4: (1,3), (2,2), (3,1).",
        kolommen=[r"\(\tfrac{1}{6}\)", r"\(\tfrac{1}{36}\)", r"\(\tfrac{1}{12}\)"],
    ),
    inv(
        r"\(X\) neemt de waarden 0, 1 en 2 aan met kansen 0,5, 0,3 en 0,2. Bereken \(E(X)\). Geef een decimaal getal.",
        ["0,7", "0.7"],
        r"\(0 \cdot 0{,}5 + 1 \cdot 0{,}3 + 2 \cdot 0{,}2\).",
    ),
    mk(
        "Bij een spel win je 10 euro met kans 0,1. Anders verlies je 2 euro. Wat is je verwachte winst per spel?",
        ["−0,80 euro", "1 euro", "0,80 euro", "−2 euro"],
        0,
        r"\(10 \cdot 0{,}1 - 2 \cdot 0{,}9 = 1 - 1{,}8\).",
    ),
    sorteer(
        "Is de kansvariabele binomiaal verdeeld?",
        ["Binomiaal", "Niet binomiaal"],
        [("het aantal keer kop bij 20 worpen met een munt", "Binomiaal"), ("het aantal zessen bij 12 worpen met een dobbelsteen", "Binomiaal"), ("het aantal juiste antwoorden als je 10 meerkeuzevragen met 4 opties gokt", "Binomiaal"),
         ("het aantal azen als je 5 kaarten trekt zonder terugleggen", "Niet binomiaal"), ("de lengte van een willekeurige leerling", "Niet binomiaal"), ("het aantal worpen tot je een eerste zes gooit", "Niet binomiaal")],
        "Binomiaal vraagt een vast aantal onafhankelijke pogingen met telkens dezelfde slaagkans.",
    ),
    casus(
        r"\(X \sim \text{Bin}(5;\ 0{,}2)\).",
        [
            inv(r"Bereken \(E(X)\).", ["1", "een", "één"], r"\(5 \cdot 0{,}2\)."),
            mk(r"Hoe groot is \(P(X = 0)\)?", [r"\(0{,}8^{5}\)", r"\(0{,}2^{5}\)", r"\(1 - 0{,}2^{5}\)", r"\(5 \cdot 0{,}8\)"], 0, "Vijf keer na elkaar geen succes."),
            mk(r"Hoe bereken je \(P(X \geq 1)\) het snelst?", [r"\(1 - 0{,}8^{5}\)", r"\(P(X = 1) \cdot 5\)", r"\(0{,}2 \cdot 5\)", r"\(1 - 0{,}2^{5}\)"], 0, "Met de complementregel."),
        ],
    ),
    mk(
        r"Wat is de standaardafwijking van \(X \sim \text{Bin}(100;\ 0{,}5)\)?",
        ["5", "25", "50", "10"],
        0,
        r"\(\sqrt{100 \cdot 0{,}5 \cdot 0{,}5} = \sqrt{25}\).",
    ),
    inv(
        r"\(X \sim \text{Bin}(4;\ \tfrac{1}{2})\). Bereken \(P(X = 2)\). Schrijf het antwoord als vereenvoudigde breuk.",
        ["3/8"],
        r"\(\binom{4}{2} \cdot \left(\tfrac{1}{2}\right)^{4} = \tfrac{6}{16}\).",
    ),
    koppel(
        "Verbind de situatie met de regel die je gebruikt.",
        [("de kans op 'minstens één'", "complementregel"), ("de kans op A of B, die elkaar niet uitsluiten", "algemene somregel"), ("de kans op een pad in een kansboom", "productregel"), ("de kans op A als je weet dat B gebeurd is", "voorwaardelijke kans")],
        ["wet van de grote aantallen"],
        "Elke vraagvorm heeft zijn eigen rekenregel.",
    ),
    keuze(
        r"Twee gebeurtenissen die elkaar uitsluiten hebben \(P(A \cap B) =\) [[*0|1|P(A) · P(B)]]. Als ze allebei een kans groter dan 0 hebben, zijn ze [[*afhankelijk|onafhankelijk]].",
        r"Uitsluitend betekent: als A gebeurt, kan B niet meer. Dan verandert B wel degelijk.",
    ),
    tabel(
        "Juist of fout?",
        [(r"\(P(A \mid B) = P(B \mid A)\) geldt altijd.", F), (r"Als \(A\) en \(B\) onafhankelijk zijn, dan is \(P(A \mid B) = P(A)\).", J), (r"\(E(X)\) kan een getal zijn dat \(X\) nooit aanneemt.", J), (r"\(P(\overline{A} \cap \overline{B}) = 1 - P(A \cup B)\)", J)],
        r"Bij een eerlijke dobbelsteen is \(E(X) = 3{,}5\), en dat gooi je nooit.",
        kolommen=["Juist", "Fout"],
    ),
    volgorde(
        "Zet de stappen om een voorwaardelijke kans uit een kansboom te halen in volgorde.",
        ["teken de boom met de kansen op de takken", "vermenigvuldig langs elk pad", "tel de paden op die bij de voorwaarde horen", "deel het gevraagde pad door die som"],
        "Zo vind je bijvoorbeeld uit welke machine een fout stuk komt.",
    ),
    mk(
        "Je gooit 4 keer met een eerlijke dobbelsteen. Hoe groot is de kans op minstens één zes, afgerond?",
        ["0,52", "0,67", "0,48", "0,17"],
        0,
        r"\(1 - \left(\tfrac{5}{6}\right)^{4} \approx 1 - 0{,}482\).",
    ),
    sleep(
        r"Bij \(\text{Bin}(n, p)\) is de verwachtingswaarde [[\(np\)]] en de standaardafwijking [[\(\sqrt{np(1 - p)}\)]].",
        [r"\(n + p\)", r"\(np(1 - p)\)"],
        "Vergeet de wortel niet bij de standaardafwijking.",
    ),
    mk(
        "Je meet bij een loket verschillende dingen. Welke kansvariabele is continu?",
        ["de wachttijd aan een loket", "het aantal klanten aan een loket", "het aantal fouten in een tekst", "het aantal kinderen in een gezin"],
        0,
        "Een tijd kan elke waarde in een interval aannemen.",
    ),
    inv(
        "Een toets heeft 5 meerkeuzevragen met elk 4 opties. Je gokt alles. Hoeveel juiste antwoorden verwacht je? Geef een decimaal getal.",
        ["1,25", "1.25"],
        r"\(X \sim \text{Bin}(5;\ 0{,}25)\) en \(E(X) = 5 \cdot 0{,}25\).",
    ),
    mk(
        r"\(A\) en \(B\) sluiten elkaar uit, met \(P(A) = 0{,}3\) en \(P(B) = 0{,}25\). Hoe groot is \(P(A \cup B)\)?",
        ["0,55", "0,075", "0,475", "0,45"],
        0,
        r"De doorsnede is leeg, dus je telt gewoon op.",
    ),
    inv(
        r"\(X \sim \text{Bin}(4;\ 0{,}3)\). Hoeveel is \(P(X \leq 4)\)? Schrijf het getal.",
        ["1", "een", "één"],
        "Met 4 pogingen kan je nooit meer dan 4 successen hebben: alle kansen samen.",
    ),
]
