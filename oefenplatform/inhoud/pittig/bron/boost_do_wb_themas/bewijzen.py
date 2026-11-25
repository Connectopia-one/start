"""Redeneren, bewijzen en tegenvoorbeelden — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_bewijzen: uitspraken controleren, illustreren met
voorbeelden, weerleggen met een tegenvoorbeeld, correct noteren en
redeneerstappen in een bewijs aanvullen. Met twee zelfgetekende prenten:
een kladblad met fouten en een uitgeschreven bewijs."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, s_lijn, pix_zone

KB = "kladblad-met-fouten"
KL = [("A", "= 2x − 6 − (x − 5)"), ("B", "= 2x − 6 − x − 5"), ("C", "= x − 11")]
KR = [("D", "3x + x = 12"), ("E", "4x = 12"), ("F", "x = 12 − 4 = 8")]


def _kladblad():
    d = []
    for x0, kop, opg, lijnen in [(40, "Oefening 1", "Werk uit: 2(x − 3) − (x − 5)", KL), (520, "Oefening 2", "Los op: 3x = 12 − x", KR)]:
        d.append(s_vak(x0, 60, 440, 540, vul="#ffffff", rand="#b9b29c", dikte=2, rond=12))
        d.append(s_tekst(x0 + 220, 100, kop, 22, vet=True))
        d.append(s_tekst(x0 + 220, 150, opg, 21))
        for i, (letter, t) in enumerate(lijnen):
            y = 250 + i * 110
            d.append(s_lijn(x0 + 20, y + 25, x0 + 420, y + 25, kleur="#e7e2d2", dikte=1))
            d.append(f'<circle cx="{x0+50}" cy="{y}" r="20" fill="#ffffff" stroke="#24331b" stroke-width="2"/>')
            d.append(s_tekst(x0 + 50, y + 7, letter, 20, vet=True))
            d.append(s_tekst(x0 + 95, y + 8, t, 24, "start"))
    return d


def _kz(kolom, i):
    return [pix_zone(40 + kolom * 480, 250 + i * 110 - 45, 440, 90)]


BW = "bewijs-som-even"
STAPPEN = [("A", "Gegeven: a en b zijn even gehele getallen."),
           ("B", "Dan is a = 2m en b = 2n, met m en n geheel."),
           ("C", "a + b = 2m + 2n = 2(m + n)"),
           ("D", "m + n is geheel, dus a + b is even.")]


def _bewijs():
    d = [s_tekst(500, 80, "Te bewijzen: de som van twee even getallen is even.", 22)]
    for i, (letter, t) in enumerate(STAPPEN):
        y = 130 + i * 115
        d.append(s_vak(80, y, 840, 90, vul="#ffffff" if i % 2 else "#f6f3ea", rand="#b9b29c", dikte=2, rond=14))
        d.append(f'<circle cx="130" cy="{y+45}" r="22" fill="#ffffff" stroke="#24331b" stroke-width="2"/>')
        d.append(s_tekst(130, y + 53, letter, 22, vet=True))
        d.append(s_tekst(180, y + 54, t, 24, "start"))
    return d


BZ = {l: [pix_zone(80, 130 + i * 115, 840, 90)] for i, (l, _) in enumerate(STAPPEN)}

GRAFIEKEN = [dict(naam=KB, titel="Twee oefeningen op een kladblad", eigen=_kladblad),
             dict(naam=BW, titel="Een bewijs in vier stappen", eigen=_bewijs)]
UK, UB = f"{KB}.svg", f"{BW}.svg"

VRAGEN = [
    klik("Klik op de regel met de fout in oefening 1.", UK, _kz(0, 1),
         r"Een min voor de haakjes verandert elk teken erbinnen: \(-(x - 5) = -x + 5\). De uitkomst is \(x - 1\)."),
    klik("Klik op de regel met de fout in oefening 2.", UK, _kz(1, 2),
         r"Uit \(4x = 12\) volgt \(x = 12 : 4 = 3\). Je deelt door 4, je trekt niet af."),
    klik("Klik op de stap die zegt wat 'even' betekent.", UB, BZ["B"], "Een even getal is het dubbel van een geheel getal."),
    klik("Klik op de stap waar de distributiviteit gebruikt wordt.", UB, BZ["C"], r"\(2m + 2n = 2(m + n)\): de factor 2 wordt buiten haakjes gebracht."),
    klik("Klik op het besluit van het bewijs.", UB, BZ["D"], "Het besluit zegt wat bewezen moest worden."),
    tabel("Uitspraak: elk priemgetal is oneven. Is dit getal een tegenvoorbeeld?",
          [(r"\(2\)", "ja"), (r"\(9\)", "nee"), (r"\(3\)", "nee"), (r"\(15\)", "nee")],
          r"Enkel \(2\) is priem én even. \(9\) en \(15\) zijn geen priemgetallen, dus ze zeggen niets over de uitspraak.",
          kolommen=["ja", "nee"]),
    mk(r"Welk getal weerlegt: als \(x^{2} > 4\), dan is \(x > 2\)?",
       [r"\(x = -3\)", r"\(x = 3\)", r"\(x = 2{,}5\)", r"\(x = 0\)"], 0,
       r"\((-3)^{2} = 9 > 4\), maar \(-3\) is niet groter dan \(2\). Bij \(0\) is het eerste deel al vals."),
    sorteer(r"Altijd waar, of vals met een tegenvoorbeeld? (\(a\) is een reëel getal, niet nul.)", ["altijd waar", "vals"],
            [(r"\((-a)^{2} = a^{2}\)", "altijd waar"), (r"\(\frac{1}{a} < a\)", "vals"), (r"\(a + a = 2a\)", "altijd waar"),
             (r"\(a^{3} \geq a\)", "vals"), (r"\(2a > a\)", "vals")],
            r"Tegenvoorbeelden: \(a = 0{,}5\) geeft \(\frac{1}{a} = 2\) en \(a^{3} = 0{,}125\). Bij \(a = -1\) is \(2a = -2 < -1\)."),
    mk(r"Welk koppel is een tegenvoorbeeld voor \((a + b)^{2} = a^{2} + b^{2}\)?",
       [r"\(a = 1\) en \(b = 1\)", r"\(a = 0\) en \(b = 5\)", r"\(a = 3\) en \(b = 0\)", r"\(a = 0\) en \(b = -5\)"], 0,
       r"\((1 + 1)^{2} = 4\), maar \(1^{2} + 1^{2} = 2\). Met een nul erin klopt de gelijkheid toevallig wel."),
    mk(r"Een leerling ziet dat \(n^{2} + n + 41\) een priemgetal is voor \(n = 0\) tot \(5\). Ze besluit: altijd priem. Wat klopt?",
       ["het besluit is niet bewezen", "zes voorbeelden zijn genoeg", r"het is bewezen voor elke \(n\)", "met letters erbij klopt het wel"], 0,
       r"Voorbeelden maken iets geloofwaardig, maar bewijzen het niet. Bij \(n = 40\) krijg je \(1681 = 41 \cdot 41\)."),
    keuze("Om te bewijzen dat er een even priemgetal bestaat, volstaat [[*één voorbeeld|een bewijs met letters|een tegenvoorbeeld]].",
          "Bij 'er bestaat' is één geval genoeg: 2."),
    tabel("Is het eerste een nodige of een voldoende voorwaarde voor het tweede?",
          [("een vierkant zijn, om een rechthoek te zijn", "voldoende"), ("vier gelijke zijden hebben, om een vierkant te zijn", "nodig"),
           ("even zijn, om deelbaar door 10 te zijn", "nodig"), ("deelbaar zijn door 10, om even te zijn", "voldoende")],
          "Een ruit heeft vier gelijke zijden, maar is niet altijd een vierkant. 4 is even, maar niet deelbaar door 10.",
          kolommen=["nodig", "voldoende"]),
    volgorde("Zet de stappen van het bewijs 'het product van twee oneven getallen is oneven' in de juiste volgorde.",
             [r"Neem \(a = 2m + 1\) en \(b = 2n + 1\), met \(m\) en \(n\) geheel.", r"\(a \cdot b = 4mn + 2m + 2n + 1\)",
              r"\(a \cdot b = 2(2mn + m + n) + 1\)", r"\(2mn + m + n\) is geheel, dus \(a \cdot b\) is oneven."],
             "Gegevens, uitwerken, schrijven in de vorm 2 keer iets plus 1, besluit."),
    sleep(r"Neem drie opeenvolgende gehele getallen \(n\), \(n + 1\) en \(n + 2\). Hun som is [[\(3n + 3\)]] \(= 3(n + 1)\). Die som is dus altijd deelbaar door [[\(3\)]].",
          [r"\(3n\)", r"\(2\)"], "Met letters geldt de redenering voor elke drie opeenvolgende getallen."),
    casus("Jonas zegt: 'Als je een getal kwadrateert, wordt het altijd groter.'", [
        mk("Welk getal is een tegenvoorbeeld?", [r"\(0{,}5\)", r"\(2\)", r"\(\sqrt{5}\)", r"\(-3\)"], 0,
           r"\(0{,}5^{2} = 0{,}25\): kleiner dan \(0{,}5\)."),
        tabel("Is dit getal ook een tegenvoorbeeld voor Jonas?",
              [(r"\(1\)", "ja"), (r"\(0\)", "ja"), (r"\(-2\)", "nee"), (r"\(3\)", "nee")],
              r"\(1^{2} = 1\) en \(0^{2} = 0\): niet groter. \((-2)^{2} = 4\) is wel groter dan \(-2\).",
              kolommen=["ja", "nee"]),
        keuze("Jonas toont twintig voorbeelden waarbij het klopt. Zijn bewering is dan [[*nog altijd niet bewezen|wel bewezen]].",
              "Eén tegenvoorbeeld weegt zwaarder dan twintig voorbeelden."),
        mk("Hoe maakt Jonas zijn bewering juist?",
           [r"voor elk getal groter dan \(1\)", r"voor elk getal kleiner dan \(1\)", "voor elk getal dat niet nul is", "voor elk positief getal"], 0,
           r"Tussen \(0\) en \(1\) wordt een kwadraat kleiner. Vanaf \(1\) (zonder \(1\) zelf) wordt het groter."),
    ]),
    mk(r"Wat is er fout aan: \(x^{2} = 9 \Rightarrow x = 3\)?",
       [r"\(x = -3\) is ook een oplossing", "er is helemaal niets fout aan deze stap", r"het moet \(x = 4{,}5\) zijn", r"het moet \(x = 81\) zijn"], 0,
       r"\((-3)^{2} = 9\). Het besluit vergeet een geval."),
    tabel("Is deze redeneerstap correct?",
          [(r"\(2x = 10 \Leftrightarrow x = 5\)", "correct"), (r"\(x + 4 = 9 \Leftrightarrow x = 13\)", "fout"),
           (r"\(-x = 6 \Leftrightarrow x = -6\)", "correct"), (r"\(\frac{x}{3} = 2 \Leftrightarrow x = \frac{2}{3}\)", "fout")],
          r"Bij \(x + 4 = 9\) trek je \(4\) af: \(x = 5\). Bij \(\frac{x}{3} = 2\) vermenigvuldig je met \(3\): \(x = 6\).",
          kolommen=["correct", "fout"]),
    inv(r"Iemand schrijft \(-2^{2} = 4\). Wat is de juiste uitkomst? Een getal.", ["-4", "min 4", "min vier"],
        r"De macht werkt enkel op de \(2\): \(-2^{2} = -(2^{2}) = -4\)."),
    mk(r"Welke notatie voor de oplossingen van \(x^{2} = 9\) is correct?",
       [r"\(x = 3 \vee x = -3\)", r"\(x = 3 \wedge x = -3\)", r"\(x = \pm 3 = 9\)", r"\(x = 3 = -3\)"], 0,
       r"Of de ene, of de andere oplossing: dat is \(\vee\). Een getal kan niet tegelijk \(3\) en \(-3\) zijn."),
    koppel("Verbind elke foute berekening met wat er misging.",
           [(r"\(10 - 2 \cdot 3 = 24\)", "volgorde van de bewerkingen"), (r"\((2x)^{3} = 2x^{3}\)", "de macht niet op elke factor"),
            (r"\(\sqrt{16 + 9} = 4 + 3\)", "de wortel van een som gesplitst"), ("lengte keer 3, dus oppervlakte keer 3", "schaalverandering")],
           ["een tegenvoorbeeld gebruikt"],
           r"\(10 - 6 = 4\), \((2x)^{3} = 8x^{3}\), \(\sqrt{25} = 5\) en de oppervlakte wordt keer 9."),
    keuze("Een bewering met 'er bestaat' weerleg je [[*door aan te tonen dat het in geen enkel geval lukt|met één tegenvoorbeeld]].",
          "Eén geval waar het niet lukt, zegt niets: misschien lukt het bij een ander geval wel."),
    mk(r"Hoe bewijs je dat \(n^{2} - n\) voor elk geheel getal \(n\) even is?",
       [r"\(n(n - 1)\): een van twee opeenvolgende getallen is even",
        r"het klopt voor \(n = 1\) tot \(n = 10\), dus voor elke \(n\)",
        r"\(n^{2}\) en \(n\) zijn altijd allebei even getallen",
        r"\(n^{2} - n\) is altijd \(0\), en \(0\) is een even getal"], 0,
       r"\(n^{2} - n = n(n - 1)\). Van twee opeenvolgende getallen is er altijd één even, dus het product ook."),
    inv(r"Vul de redeneerstap aan: \(3(x - 2) = 12 \Leftrightarrow x - 2 = \ldots\) Een getal.", ["4", "vier"],
        r"Beide leden delen door \(3\): \(12 : 3 = 4\)."),
    keuze("Bij een kubus worden alle ribben 2 keer zo lang. Het volume wordt [[*8|2|4|6]] keer zo groot.",
          r"Elke van de drie afmetingen keer 2: \(2 \cdot 2 \cdot 2 = 8\)."),
    tabel("Klopt dit over bewijzen?",
          [("Een bewijs met letters geldt voor elk getal dat je invult.", J), ("Een tegenvoorbeeld moet aan de voorwaarden van de uitspraak voldoen.", J),
           ("Als je geen tegenvoorbeeld vindt, is de uitspraak bewezen.", F), ("Een tekening kan een bewijs ondersteunen, maar vervangt het niet.", J)],
          "Niet vinden is iets anders dan bewijzen dat het niet bestaat.",
          kolommen=["Juist", "Fout"]),
    inv(r"Geef een getal \(x\), verschillend van \(0\), waarvoor \(x^{2} = x\).", ["1", "een", "één"],
        r"\(1^{2} = 1\). Zo toon je dat 'er bestaat een \(x \neq 0\) met \(x^{2} = x\)' waar is."),
    open_("Bewijs dat de som van twee oneven getallen even is.",
          r"Neem \(a = 2m + 1\) en \(b = 2n + 1\), met \(m\) en \(n\) geheel. Dan is \(a + b = 2m + 2n + 2 = 2(m + n + 1)\). Omdat \(m + n + 1\) geheel is, is \(a + b\) even."),
]
