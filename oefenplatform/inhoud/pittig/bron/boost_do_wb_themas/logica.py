"""Logica: bewerkingen en waarheidstabellen — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_logica: waarheidswaarde, negatie, conjunctie, disjunctie,
implicatie, equivalentie, tautologie en contradictie, nodig en voldoende,
kwantoren, waarheidstabellen en logische poorten. Met een zelfgetekende
waarheidstabel voor drie uitspraken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, s_lijn, pix_zone

WT = "waarheidstabel-drie"
RIJEN = [(1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0), (0, 1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
_X = [330, 500, 670]
_Y0, _DY = 120, 58


def _tabel():
    d = [s_vak(240, 70, 520, 50, vul="#e6efdc", rand="#2f4a22", dikte=2)]
    for x, t in zip(_X, "pqr"):
        d.append(s_tekst(x, 104, t, 26, vet=True))
    for i, rij in enumerate(RIJEN):
        y = _Y0 + i * _DY
        d.append(s_vak(240, y, 520, _DY, vul="#ffffff" if i % 2 else "#faf8f1", rand="#b9b29c", dikte=1))
        for x, w in zip(_X, rij):
            d.append(s_tekst(x, y + 38, str(w), 24))
    d.append(s_lijn(415, 70, 415, _Y0 + 8 * _DY, kleur="#b9b29c", dikte=1))
    d.append(s_lijn(585, 70, 585, _Y0 + 8 * _DY, kleur="#b9b29c", dikte=1))
    d.append(s_tekst(500, _Y0 + 8 * _DY + 40, "1 = waar, 0 = vals", 18))
    return d


def _rij(*rijen):
    return [pix_zone(240, _Y0 + RIJEN.index(r) * _DY, 520, _DY) for r in rijen]


GRAFIEKEN = [dict(naam=WT, titel="Waarheidstabel voor p, q en r", eigen=_tabel)]
U = f"{WT}.svg"

VRAGEN = [
    klik(r"Klik op de enige rij waar \((p \wedge q) \Rightarrow r\) vals is.", U, _rij((1, 1, 0)),
         r"Een implicatie is enkel vals als het eerste deel waar is en het tweede vals: \(p \wedge q\) waar, \(r\) vals."),
    klik(r"Klik op de rij waar \(p \wedge q \wedge r\) waar is.", U, _rij((1, 1, 1)),
         "Een conjunctie vraagt dat alle delen waar zijn."),
    klik(r"Klik op een rij waar \(\neg p \wedge (q \vee r)\) waar is.", U, _rij((0, 1, 1), (0, 1, 0), (0, 0, 1)),
         r"\(p\) moet vals zijn en minstens één van \(q\) en \(r\) waar. Dat lukt in drie rijen."),
    klik(r"Klik op de rij waar \(p \vee q \vee r\) vals is.", U, _rij((0, 0, 0)),
         "Een disjunctie is enkel vals als alle delen vals zijn."),
    tabel(r"\(p\) is waar en \(q\) is vals. Is de uitspraak waar of vals?",
          [(r"\(p \wedge q\)", "vals"), (r"\(p \vee q\)", "waar"), (r"\(p \Rightarrow q\)", "vals"), (r"\(q \Rightarrow p\)", "waar"),
           (r"\(p \Leftrightarrow q\)", "vals"), (r"\(\neg p \vee q\)", "vals")],
          r"\(q \Rightarrow p\) heeft een vals eerste deel, dus is waar. \(\neg p \vee q\): allebei vals.",
          kolommen=["waar", "vals"]),
    mk("Welke uitspraak is de negatie van 'Het regent en het waait'?",
       ["het regent niet of het waait niet", "het regent niet en het waait niet", "het regent niet, maar het waait wel", "als het regent, dan waait het niet"], 0,
       r"\(\neg(p \wedge q)\) is waar zodra minstens één deel vals is. Dat is \(\neg p \vee \neg q\)."),
    mk(r"Wat is \(p \wedge \neg p\)?",
       ["een contradictie", "een tautologie", "een implicatie", "soms waar, soms vals"], 0,
       r"\(p\) en \(\neg p\) kunnen nooit samen waar zijn: altijd vals."),
    sorteer("Tautologie, contradictie of geen van beide?", ["tautologie", "contradictie", "geen van beide"],
            [(r"\(p \Rightarrow (p \vee q)\)", "tautologie"), (r"\(\neg(p \vee \neg p)\)", "contradictie"), (r"\(p \Rightarrow q\)", "geen van beide"),
             (r"\((p \wedge \neg q) \wedge q\)", "contradictie"), (r"\(p \vee q\)", "geen van beide")],
            "Een tautologie heeft in elke rij waar, een contradictie in elke rij vals."),
    inv("Hoeveel rijen heeft een waarheidstabel met vijf uitspraken? Een getal.", ["32", "tweeëndertig"],
        r"Elke uitspraak verdubbelt het aantal rijen: \(2^{5} = 32\)."),
    mk("'Als je 18 bent, mag je stemmen.' Welk geval spreekt die regel tegen?",
       ["iemand van 18 mag niet stemmen", "iemand van 16 mag niet stemmen", "iemand van 16 mag toch al gaan stemmen", "iemand van 18 gaat stemmen"], 0,
       "Enkel een waar eerste deel met een vals tweede deel maakt de implicatie vals. Over wie jonger is, zegt de regel niets."),
    keuze(r"Op een menu staat 'soep of dessert'. Daar bedoelt men meestal niet allebei. Bij \(p \vee q\) in de logica mag je [[*allebei|maar één van de twee]] nemen.",
          r"Het logische of is ook waar als beide delen waar zijn."),
    koppel("Welke soort voorwaarde is het eerste voor het tweede?",
           [("deelbaar zijn door 2, om deelbaar te zijn door 6", "nodig, niet voldoende"),
            ("deelbaar zijn door 6, om deelbaar te zijn door 2", "voldoende, niet nodig"),
            (r"\(x + 1 = 5\), om \(x = 4\) te hebben", "nodig en voldoende")],
           ["geen van beide"],
           r"\(10\) is deelbaar door \(2\), maar niet door \(6\). \(x + 1 = 5\) en \(x = 4\) zijn equivalent."),
    mk(r"Wat is de negatie van \(\exists x: x^{2} < 0\)?",
       [r"\(\forall x: x^{2} \geq 0\)", r"\(\exists x: x^{2} \geq 0\)", r"\(\forall x: x^{2} < 0\)", r"\(\neg \forall x: x^{2} < 0\)"], 0,
       r"Het bestaat-er-een wordt voor-elke, en \(<\) wordt \(\geq\)."),
    tabel("Is deze uitspraak met een kwantor waar of vals?",
          [(r"\(\forall x \in \mathbb{R}: x^{2} \geq 0\)", "waar"), (r"\(\exists x \in \mathbb{N}: x < 0\)", "vals"),
           (r"\(\exists x \in \mathbb{Z}: x^{2} = 4\)", "waar"), (r"\(\forall x \in \mathbb{Z}: 2x > x\)", "vals")],
          r"Eén tegenvoorbeeld volstaat om een voor-elke vals te maken: bij \(x = 0\) is \(2x = x\).",
          kolommen=["waar", "vals"]),
    casus("Een alarm gaat af als de deur open is (\\(p\\)) en het alarm ingeschakeld is (\\(q\\)), of als iemand op de paniekknop drukt (\\(r\\)).", [
        mk("Welke uitdrukking hoort bij het alarm?",
           [r"\((p \wedge q) \vee r\)", r"\(p \wedge (q \vee r)\)", r"\(\neg(p \wedge q) \vee r\)", r"\(p \vee q \vee r\)"], 0,
           "De paniekknop werkt altijd, de deur enkel samen met het ingeschakelde alarm."),
        inv("Hoeveel rijen telt de waarheidstabel van dit alarm? Een getal.", ["8", "acht"], r"Drie uitspraken: \(2^{3} = 8\)."),
        inv("In hoeveel van die rijen gaat het alarm af? Een getal.", ["5", "vijf"],
            r"In de vier rijen met \(r\) waar, plus de rij met \(p\) en \(q\) waar en \(r\) vals."),
        keuze("De paniekknop zit met de rest verbonden via een [[*of-poort|en-poort|niet-poort]].", "Eén van de twee ingangen volstaat."),
    ]),
    mk(r"Wanneer is \(p \Leftrightarrow \neg q\) waar?",
       [r"als \(p\) en \(q\) verschillen", r"als \(p\) en \(q\) gelijk zijn", r"als \(p\) en \(q\) allebei vals zijn", r"enkel als \(p\) en \(q\) allebei waar zijn"], 0,
       r"\(p\) moet dezelfde waarde hebben als \(\neg q\), dus net de andere waarde dan \(q\)."),
    inv(r"\(p\) is waar, \(q\) is vals en \(r\) is waar. Is \((p \Rightarrow q) \vee \neg r\) waar of vals? Eén woord.", ["vals"],
        r"\(p \Rightarrow q\) is vals en \(\neg r\) is vals. Een disjunctie van twee valse delen is vals."),
    inv(r"In hoeveel rijen van een tabel met drie uitspraken is \(p \vee q \vee r\) waar? Een getal.", ["7", "zeven"],
        "In alle acht rijen behalve de rij met drie keer vals."),
    tabel(r"Vul de kolom \(\neg p \vee q\) aan.",
          [(r"\(p = 1\), \(q = 1\)", "1"), (r"\(p = 1\), \(q = 0\)", "0"), (r"\(p = 0\), \(q = 1\)", "1"), (r"\(p = 0\), \(q = 0\)", "1")],
          r"Enkel als \(p\) waar is en \(q\) vals, zijn beide delen vals. Dezelfde kolom als \(p \Rightarrow q\).",
          kolommen=["1", "0"]),
    keuze(r"De kolommen van \(p \Rightarrow q\) en \(\neg p \vee q\) zijn [[*gelijk|elkaars omgekeerde]]. Daarom is \((p \Rightarrow q) \Leftrightarrow (\neg p \vee q)\) een [[*tautologie|contradictie]].",
          "Twee gelijke kolommen geven bij een equivalentie in elke rij waar."),
    mk("'Als het regent, is de straat nat.' De straat is nat. Wat weet je nu zeker over de regen?",
       ["niets", "dat het zeker regent", "dat het zeker niet regent", "dat het daarnet regende"], 0,
       "Een implicatie werkt maar in één richting. De straat kan ook nat zijn door een sproeier."),
    sleep("Bij een en-poort is de uitgang [[1]] als alle ingangen 1 zijn. Zet je er een niet-poort achter, dan wordt de uitgang [[0]].",
          ["2"], "Een niet-poort keert het signaal om."),
    tabel("Welke poort hoort bij deze schakeling?",
          [("Een lamp brandt als de ene of de andere knop ingedrukt is, of allebei.", "of-poort"),
           ("Een machine start enkel als twee sleutels tegelijk gedraaid zijn.", "en-poort"),
           ("Een nachtlampje gaat aan als de sensor geen licht meet.", "niet-poort")],
          "Of: minstens één. En: allemaal. Niet: omkeren.",
          kolommen=["en-poort", "of-poort", "niet-poort"]),
    mk(r"Waarom is \(p \Rightarrow q\) waar als \(p\) vals is?",
       ["de belofte wordt niet gebroken", r"omdat \(q\) dan ook altijd vals is", "omdat een implicatie altijd waar is", "omdat een vals deel nooit meetelt"], 0,
       "Wie belooft 'als het mooi weer is, gaan we zwemmen', liegt niet als het regent."),
    inv(r"\(p \Rightarrow q\) is vals. Wat is dan de waarheidswaarde van \(q\)? Eén woord.", ["vals"],
        r"Een implicatie is enkel vals bij \(p\) waar en \(q\) vals."),
    mk(r"Hoe schrijf je in symbolen: niet allebei, \(p\) en \(q\)?",
       [r"\(\neg(p \wedge q)\)", r"\(\neg p \wedge \neg q\)", r"\(\neg p \wedge q\)", r"\(\neg(p \vee q)\)"], 0,
       r"De negatie staat voor de hele conjunctie. \(\neg p \wedge \neg q\) betekent: geen van beide."),
    open_("Leg met een voorbeeld uit waarom 'als p, dan q' niet hetzelfde is als 'als q, dan p'.",
          "'Als een getal deelbaar is door 4, dan is het even' is waar. 'Als een getal even is, dan is het deelbaar door 4' is vals: 6 is even, maar niet deelbaar door 4. De richting van de implicatie doet er dus toe."),
]
