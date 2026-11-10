"""Kansrekenen met kansbomen en kruistabellen — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, kansboom, s_tekst, s_vak, LICHT

BOOM = "kansen-kansboom-bus"
KRUIS = "kansen-kruistabel-ontbijt"

_BOOM, _MIDDEN, _KNOPEN = kansboom(
    (90, 340),
    [("bus", "0,3", (420, 185)), ("geen bus", "0,7", (420, 495))],
    {
        "bus": [("te laat", "0,1", (800, 105)), ("op tijd", "0,9", (800, 265))],
        "geen bus": [("te laat", "0,05", (800, 415)), ("op tijd", "0,95", (800, 575))],
    },
)


def _boom():
    return _BOOM


def _knoop_zone(sleutel):
    x, y = _KNOPEN[sleutel]
    return pix_zone(x - 60, y - 26, 120, 52)


def _tak_zone(sleutel):
    x, y = _MIDDEN[sleutel]
    return pix_zone(x - 55, y - 40, 110, 80)


# Kruistabel: 250 leerlingen
KOP = ["", "Moe in de les", "Niet moe", "Totaal"]
RIJEN = [
    ["Ontbijt elke dag", "30", "120", "150"],
    ["Ontbijt niet elke dag", "45", "55", "100"],
    ["Totaal", "75", "175", "250"],
]
KX = [60, 340, 560, 760, 940]  # kolomgrenzen
KY = [150, 230, 320, 410, 500]  # rijgrenzen


def _kruis():
    d = []
    for r in range(4):
        for k in range(4):
            x0, x1, y0, y1 = KX[k], KX[k + 1], KY[r], KY[r + 1]
            vul = LICHT if r == 0 or k == 0 else "#fffdf7"
            d.append(s_vak(x0, y0, x1 - x0, y1 - y0, vul=vul, rand="#2f4a22"))
            t = KOP[k] if r == 0 else RIJEN[r - 1][k]
            d.append(s_tekst((x0 + x1) / 2, (y0 + y1) / 2 + 8, t, 21 if r and k else 20, vet=(r == 0 or k == 0)))
    d.append(s_tekst(500, 590, "Bevraging bij 250 leerlingen", 18, kleur="#6b6b5a"))
    return d


def _cel_zone(r, k):
    """r en k tellen vanaf 1 voor de getallen (0 is de kop)."""
    return pix_zone(KX[k], KY[r], KX[k + 1] - KX[k], KY[r + 1] - KY[r])


GRAFIEKEN = [
    dict(naam=BOOM, titel="Bus nemen en te laat komen", eigen=_boom),
    dict(naam=KRUIS, titel="Ontbijt en moe zijn in de les", eigen=_kruis),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen bij een kansboom en een kruistabel") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        "Klik op de kans dat een leerling die de bus neemt, te laat komt.",
        f"{BOOM}.svg",
        [_tak_zone(("bus", "te laat"))],
        r"Die voorwaardelijke kans \(P(\text{te laat} \mid \text{bus}) = 0{,}1\) staat op de tak van 'bus' naar 'te laat'.",
    ),
    klik(
        "Klik op het einde van het pad 'neemt de bus niet en komt te laat'.",
        f"{BOOM}.svg",
        [_knoop_zone(("geen bus", "te laat"))],
        "Eerst de tak 'geen bus', daarna vanuit die knoop de tak 'te laat'.",
    ),
    met_prent(f"{BOOM}.svg", mk(
        "Hoe groot is de kans dat een willekeurige leerling de bus niet neemt en op tijd komt?",
        [r"\(0{,}95\)", r"\(0{,}665\)", r"\(0{,}7\)", r"\(1{,}65\)"],
        1,
        r"Productregel langs het pad: \(0{,}7 \cdot 0{,}95 = 0{,}665\).",
    )),
    met_prent(f"{BOOM}.svg", mk(
        "Hoe groot is de kans dat een willekeurige leerling te laat komt?",
        [r"\(0{,}15\)", r"\(0{,}075\)", r"\(0{,}065\)", r"\(0{,}035\)"],
        2,
        r"Twee paden eindigen op 'te laat'. Productregel en somregel: \(0{,}3 \cdot 0{,}1 + 0{,}7 \cdot 0{,}05\).",
    )),
    met_prent(f"{BOOM}.svg", tabel(
        "Juist of fout over deze kansboom?",
        [
            ("Wie de bus neemt, komt vaker te laat dan wie de bus niet neemt.", J),
            ("De kansen op de takken die uit één knoop vertrekken, tellen samen op tot 1.", J),
            ("Meer dan de helft van de laatkomers neemt de bus.", F),
            ("Te laat komen hangt hier niet af van de bus nemen.", F),
        ],
        r"\(0{,}1 > 0{,}05\): de kans hangt dus wel af van de bus. Van de laatkomers komt \(0{,}03\) van de bus en \(0{,}035\) niet: minder dan de helft neemt de bus.",
    )),
    klik(
        "Klik op het getal dat je als noemer nodig hebt voor de kans dat een leerling die niet elke dag ontbijt, moe is in de les.",
        f"{KRUIS}.svg",
        [_cel_zone(2, 3)],
        "Bij een voorwaardelijke kans kijk je enkel naar de groep waarover het gaat: de 100 leerlingen die niet elke dag ontbijten.",
    ),
    met_prent(f"{KRUIS}.svg", inv(
        "Je kiest willekeurig een leerling. Hoe groot is de kans dat die elke dag ontbijt en niet moe is? Geef een kommagetal.",
        "0,48",
        r"\(\frac{120}{250} = 0{,}48\).",
    )),
    met_prent(f"{KRUIS}.svg", mk(
        "Een leerling is moe in de les. Hoe groot is de kans dat die elke dag ontbijt?",
        [r"\(0{,}2\)", r"\(0{,}12\)", r"\(0{,}4\)", r"\(0{,}3\)"],
        2,
        r"Je kijkt enkel naar de 75 vermoeide leerlingen: \(\frac{30}{75} = 0{,}4\).",
    )),
    met_prent(f"{KRUIS}.svg", tabel(
        "Juist of fout volgens deze kruistabel?",
        [
            (r"\(P(\text{moe} \mid \text{ontbijt elke dag}) = 0{,}2\)", J),
            ("Wie niet elke dag ontbijt, is minder vaak moe dan wie elke dag ontbijt.", F),
            (r"\(P(\text{moe}) = 0{,}3\)", J),
            (r"\(P(\text{ontbijt elke dag}) = 0{,}4\)", F),
        ],
        r"\(\frac{30}{150} = 0{,}2\) tegenover \(\frac{45}{100} = 0{,}45\). \(\frac{75}{250} = 0{,}3\) en \(\frac{150}{250} = 0{,}6\).",
    )),
    mk(
        "Je gooit met twee eerlijke dobbelstenen. Hoe groot is de kans dat de som 7 is?",
        [r"\(\dfrac{7}{36}\)", r"\(\dfrac{1}{12}\)", r"\(\dfrac{1}{11}\)", r"\(\dfrac{1}{6}\)"],
        3,
        r"Er zijn \(36\) even waarschijnlijke uitkomsten. Zes geven som 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).",
    ),
    mk(
        "Een zak bevat 4 rode, 5 blauwe en 3 groene knikkers. Je trekt er blind één. Hoe groot is de kans dat ze niet blauw is?",
        [r"\(\dfrac{5}{12}\)", r"\(\dfrac{7}{12}\)", r"\(\dfrac{1}{3}\)", r"\(\dfrac{7}{5}\)"],
        1,
        r"Complementregel: \(1 - \frac{5}{12} = \frac{7}{12}\). Of rechtstreeks: \(4 + 3 = 7\) gunstige knikkers op \(12\).",
    ),
    keuze(
        "Je gooit een punaise 1000 keer: 620 keer ligt de punt omhoog. Hoe vaker je gooit, hoe [[*dichter bij|verder van|exact gelijk aan]] de kans 620/1000 komt te liggen. Zo'n geschatte kans heet een [[*empirische|voorwaardelijke|Laplace-]]kans.",
        "Bij veel herhalingen stabiliseert het aandeel rond de echte kans. Laplace kan hier niet: punt omhoog en punt opzij zijn niet even waarschijnlijk.",
    ),
    sorteer(
        "Mag je hier de wet van Laplace gebruiken?",
        ["Laplace mag", "Laplace mag niet"],
        [
            ["Een eerlijke dobbelsteen gooien", "Laplace mag"],
            ["Een punaise die op de punt of op de kop valt", "Laplace mag niet"],
            ["Een kaart trekken uit een goed geschud spel", "Laplace mag"],
            ["Morgen regent het of het regent niet", "Laplace mag niet"],
            ["Een naam trekken uit een hoed met 30 briefjes", "Laplace mag"],
            ["Een voetbalmatch winnen, verliezen of gelijkspelen", "Laplace mag niet"],
        ],
        "Laplace werkt enkel als alle uitkomsten even waarschijnlijk zijn.",
    ),
    mk(
        "Je gooit drie keer met een eerlijke munt. Hoe groot is de kans dat je minstens één keer kop gooit?",
        [r"\(\dfrac{3}{8}\)", r"\(\dfrac{1}{2}\)", r"\(\dfrac{7}{8}\)", r"\(\dfrac{3}{4}\)"],
        2,
        r"Het tegengestelde is 'drie keer munt': \(\left(\frac{1}{2}\right)^3 = \frac{1}{8}\). Dus \(1 - \frac{1}{8}\).",
    ),
    mk(
        "Een test geeft in 95 % van de gevallen het juiste resultaat. Je doet hem twee keer, onafhankelijk van elkaar. Hoe groot is de kans dat hij beide keren juist is?",
        [r"\(0{,}95\)", r"\(0{,}9025\)", r"\(0{,}0975\)", r"\(1{,}9\)"],
        1,
        r"\(0{,}95 \cdot 0{,}95 = 0{,}9025\).",
    ),
    tabel(
        "Juist of fout over kansen?",
        [
            ("Een kans van 0 betekent dat de gebeurtenis onmogelijk is.", J),
            ("Een kans kan groter zijn dan 1 als iets heel vaak gebeurt.", F),
            ("Twee gebeurtenissen die elkaar uitsluiten, kunnen samen gebeuren.", F),
            (r"Bij een eerlijke munt is de kans op kop bij de zesde worp \(\frac{1}{2}\), ook na vijf keer kop.", J),
        ],
        "Een kans ligt altijd tussen 0 en 1. Een munt heeft geen geheugen.",
    ),
    volgorde(
        "Zet de stappen om met een kansboom P(A) te berekenen in de goede volgorde.",
        [
            "Teken de eerste vertakking, met kansen die samen 1 zijn",
            "Teken bij elke knoop de tweede vertakking met de voorwaardelijke kansen",
            "Vermenigvuldig de kansen langs elk pad dat bij A hoort",
            "Tel de kansen van die paden op",
        ],
        "Eerst de boom opbouwen, dan productregel per pad, dan somregel over de paden.",
    ),
    koppel(
        "Koppel de regel aan wat je doet.",
        [
            ["Productregel", "Kansen langs één pad vermenigvuldigen"],
            ["Somregel", "Kansen van verschillende paden optellen"],
            ["Complementregel", "De kans op het tegengestelde van 1 aftrekken"],
            ["Wet van Laplace", "Gunstige uitkomsten delen door alle even waarschijnlijke uitkomsten"],
        ],
        ["Kansen van takken uit één knoop vermenigvuldigen"],
        "Langs een pad: maal. Tussen paden: plus. Het tegendeel: 1 min.",
    ),
    sleep(
        "Bij een dobbelsteen is {1, 2, 3, 4, 5, 6} de [[uitkomstenverzameling]]. 'Een even getal gooien' is een [[gebeurtenis]] met drie gunstige [[uitkomsten]].",
        ["kans", "frequentie", "kruistabel"],
        "Een gebeurtenis is een deel van de uitkomstenverzameling.",
    ),
    mk(
        "In een klas van 24 hebben 6 leerlingen een huisdier en 10 een broer of zus. 4 leerlingen hebben allebei. Hoe groot is de kans dat een willekeurige leerling een huisdier of een broer of zus heeft?",
        [r"\(\dfrac{16}{24}\)", r"\(\dfrac{4}{24}\)", r"\(\dfrac{10}{24}\)", r"\(\dfrac{12}{24}\)"],
        3,
        r"Wie beide heeft, mag je maar één keer tellen: \(6 + 10 - 4 = 12\) leerlingen.",
    ),
    mk(
        "Van 80 sporters in een club spelen er 20 tennis. 15 van die tennissers zijn meisjes. Hoe groot is de kans dat een willekeurige tennisser een meisje is?",
        [r"\(0{,}1875\)", r"\(0{,}25\)", r"\(0{,}75\)", r"\(0{,}2\)"],
        2,
        r"Je kijkt enkel naar de 20 tennissers: \(\frac{15}{20}\).",
    ),
    open_(
        r"Leg met een voorbeeld uit dat \(P(A \mid B)\) en \(P(B \mid A)\) niet hetzelfde zijn.",
        r"Bijvoorbeeld A = 'is profvoetballer' en B = 'is een man'. \(P(\text{man} \mid \text{profvoetballer})\) is bijna 1, maar \(P(\text{profvoetballer} \mid \text{man})\) is heel klein. De groep waarbinnen je kijkt (de noemer) is telkens anders.",
        "De voorwaarde bepaalt de groep waarin je telt.",
    ),
    inv(
        "In een vaas staan 3 rode en 2 witte tulpen. Je neemt er blind 2, zonder terugleggen. Hoe groot is de kans op 2 rode tulpen? Geef een kommagetal.",
        "0,3",
        r"\(\frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20} = 0{,}3\).",
    ),
    mk(
        "Dezelfde vaas (3 rode, 2 witte tulpen), maar nu zet je de eerste tulp terug voor je de tweede neemt. Hoe groot is de kans op 2 rode?",
        [r"\(0{,}6\)", r"\(0{,}36\)", r"\(0{,}09\)", r"\(0{,}5\)"],
        1,
        r"Met terugleggen blijft de kans telkens \(\frac{3}{5}\): \(0{,}6 \cdot 0{,}6\).",
    ),
    mk(
        "Een quiz heeft 4 meerkeuzevragen met elk 4 opties. Je gokt bij elke vraag. Hoe groot is de kans dat alles fout is?",
        [r"Ongeveer \(0{,}75\)", r"Ongeveer \(0{,}25\)", r"Ongeveer \(0{,}68\)", r"Ongeveer \(0{,}32\)"],
        3,
        r"Per vraag is de kans op fout \(\frac{3}{4}\). Vier keer: \(\left(\frac{3}{4}\right)^4 \approx 0{,}316\).",
    ),
    mk(
        "Het weerbericht zegt: 'kans op regen 70 %'. Wat betekent dat?",
        [
            "Op dagen met zo'n voorspelling regent het in ongeveer 70 % van de gevallen",
            "Het zal morgen 70 % van de dag regenen",
            "Het regent morgen op 70 % van de plaatsen in het land",
            "Het regent morgen zeker, maar minder hard",
        ],
        0,
        "Een kans zegt hoe vaak iets gebeurt op lange termijn, bij vergelijkbare omstandigheden.",
    ),
    mk(
        "Bij 50 worpen met een dobbelsteen kwam 13 keer een zes. Wat kan je besluiten?",
        [
            "De dobbelsteen is zeker vals",
            "De kans op een zes is bij deze dobbelsteen 13/50",
            "Dat kan toeval zijn: 50 worpen is te weinig om te besluiten",
            "Bij de volgende worpen zal zes minder vaak vallen",
        ],
        2,
        r"Verwacht is ongeveer \(\frac{50}{6} \approx 8\). Bij weinig worpen schommelt de relatieve frequentie nog sterk rond de kans.",
    ),
    casus(
        "Een sneltest voor griep. Van de mensen met klachten heeft 10 % griep. Bij wie griep heeft, is de test in 90 % van de gevallen positief. Bij wie geen griep heeft, is hij toch in 20 % van de gevallen positief.",
        [
            mk(
                "Hoe groot is de kans dat iemand met klachten positief test?",
                [r"\(0{,}09\)", r"\(0{,}27\)", r"\(0{,}2\)", r"\(1{,}1\)"],
                1,
                r"Teken een kansboom: \(0{,}1 \cdot 0{,}9 + 0{,}9 \cdot 0{,}2 = 0{,}09 + 0{,}18\).",
            ),
            mk(
                "Iemand test positief. Hoe groot is de kans dat die persoon echt griep heeft?",
                [r"Ongeveer \(0{,}9\)", r"Ongeveer \(0{,}33\)", r"Ongeveer \(0{,}1\)", r"Ongeveer \(0{,}5\)"],
                1,
                r"Van alle positieve tests komt maar \(0{,}09\) van mensen met griep: \(\frac{0{,}09}{0{,}27} = \frac{1}{3}\).",
            ),
            mk(
                "Waarom is die kans zo klein, terwijl de test griep meestal wel opspoort?",
                [
                    "Omdat de test bij griep vaak negatief is",
                    "Omdat de meeste geteste mensen geen griep hebben, zodat er veel vals positieve tests zijn",
                    "Omdat je kansen bij een kansboom nooit mag delen",
                    "Omdat 10 % en 20 % samen 30 % geven",
                ],
                1,
                "Een klein deel van een grote groep (20 % van 90 %) is meer dan een groot deel van een kleine groep (90 % van 10 %).",
            ),
        ],
    ),
]
