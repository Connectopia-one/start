"""Getallen ordenen, afronden en intervallen — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_ordenen: vergelijken met de symbolen, de getallenas,
afronden en de intervalnotatie (open, halfopen, gesloten). Met twee
zelfgetekende prenten: vier intervallen en een getallenas met punten."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import getallenas, s_lijn, s_tekst, pix_zone, DONKER

VI = "vier-intervallen"
_A, _B = -4, 5
_X0, _X1 = 160, 900


def _x(w):
    return _X0 + (w - _A) / (_B - _A) * (_X1 - _X0)


RIJEN = [("A", -2, 3, True, False), ("B", -2, 3, False, True), ("C", -2, 3, True, True), ("D", -2, None, False, None)]
RIJ_Y = [130, 260, 390, 520]


def _intervallen():
    d = []
    for (letter, a, b, va, vb), y in zip(RIJEN, RIJ_Y):
        d.append(s_lijn(_X0 - 30, y, _X1 + 40, y, kleur=DONKER, dikte=2))
        d.append(f'<polygon points="{_X1+50},{y} {_X1+36},{y-7} {_X1+36},{y+7}" fill="{DONKER}"/>')
        for w in range(_A, _B + 1):
            d.append(s_lijn(_x(w), y - 8, _x(w), y + 8, kleur=DONKER, dikte=2))
            d.append(s_tekst(_x(w), y + 34, str(w).replace("-", "−"), 18))
        eind = _x(b) if b is not None else _X1 + 30
        d.append(s_lijn(_x(a), y, eind, y, kleur="#3b6fa0", dikte=8))
        for w, vol in [(a, va), (b, vb)]:
            if w is None:
                continue
            vul = "#3b6fa0" if vol else "#ffffff"
            d.append(f'<circle cx="{_x(w):.1f}" cy="{y}" r="11" fill="{vul}" stroke="#3b6fa0" stroke-width="4"/>')
        d.append(f'<circle cx="80" cy="{y}" r="22" fill="#ffffff" stroke="{DONKER}" stroke-width="2"/>')
        d.append(s_tekst(80, y + 8, letter, 22, vet=True))
    return d


ZI = {l: [pix_zone(40, y - 55, 940, 110)] for (l, *_), y in zip(RIJEN, RIJ_Y)}

AS = "punten-op-de-as"
_AS, _Z = getallenas(-2, 3, 0.25, [("P", -1.5), ("Q", -0.25), ("R", 0.6), ("S", 2 ** 0.5), ("T", 2.7)], ijk=[-2, -1, 0, 1, 2, 3])

GRAFIEKEN = [dict(naam=VI, titel="Vier intervallen op de getallenas", eigen=_intervallen),
             dict(naam=AS, titel="Vijf punten op de getallenas", eigen=lambda: _AS)]
U, UA = f"{VI}.svg", f"{AS}.svg"

VRAGEN = [
    klik(r"Klik op de voorstelling van \(\left]-2, 3\right]\).", U, ZI["B"],
         r"Bij \(-2\) een leeg bolletje (de grens hoort er niet bij), bij \(3\) een vol bolletje."),
    klik(r"Klik op de voorstelling van de oplossingen van \(x > -2\).", U, ZI["D"],
         r"Leeg bolletje bij \(-2\) en een lijn die naar rechts blijft doorlopen."),
    klik(r"Klik op de voorstelling van alle \(x\) met \(-2 \leq x < 3\).", U, ZI["A"],
         r"Vol bij \(-2\), leeg bij \(3\): het interval \(\left[-2, 3\right[\)."),
    klik(r"Klik op het enige begrensde interval waarin zowel \(-2\) als \(3\) liggen.", U, ZI["C"],
         r"Twee volle bolletjes: \(\left[-2, 3\right]\) is gesloten."),
    klik(r"Klik op het punt bij \(-\frac{1}{4}\).", UA, [_Z["Q"]], r"\(-\frac{1}{4} = -0{,}25\): net links van \(0\)."),
    klik(r"Klik op het punt dat in \(\left]\frac{3}{2}, 3\right[\) ligt.", UA, [_Z["T"]],
         r"\(\frac{3}{2} = 1{,}5\). Enkel T ligt tussen \(1{,}5\) en \(3\). S ligt op \(\sqrt{2} \approx 1{,}41\)."),
    klik(r"Klik op het punt bij \(\sqrt{2}\).", UA, [_Z["S"]], r"\(\sqrt{2} \approx 1{,}41\): tussen \(1{,}25\) en \(1{,}5\)."),
    volgorde("Rangschik deze getallen van klein naar groot.",
             [r"\(-\frac{5}{3}\)", r"\(-1{,}6\)", r"\(-\frac{3}{2}\)", r"\(-1{,}05\)", r"\(-1\)"],
             r"\(-1{,}666\ldots < -1{,}6 < -1{,}5 < -1{,}05 < -1\). Hoe verder van nul aan de negatieve kant, hoe kleiner."),
    tabel("Klopt deze ongelijkheid?",
          [(r"\(-\frac{1}{3} < -0{,}3\)", J), (r"\(0{,}7 > \frac{5}{7}\)", F), (r"\(\sqrt{10} < 3{,}2\)", J), (r"\(-4{,}01 \geq -4{,}1\)", J)],
          r"\(-\frac{1}{3} = -0{,}333\ldots\), \(\frac{5}{7} \approx 0{,}714\) en \(\sqrt{10} \approx 3{,}16\).",
          kolommen=["Juist", "Fout"]),
    mk(r"Rond \(0{,}0496\) af op twee cijfers na de komma.",
       [r"\(0{,}05\)", r"\(0{,}04\)", r"\(0{,}5\)", r"\(0{,}049\)"], 0,
       r"Het eerste cijfer dat wegvalt is een \(9\): de \(4\) wordt een \(5\)."),
    inv(r"Rond \(2{,}995\) af op twee cijfers na de komma.", ["3,00", "3.00", "3", "3,0"],
        r"De \(5\) laat de \(9\) naar boven gaan, en dat schuift door: \(2{,}995 \to 3{,}00\)."),
    inv(r"Rond \(48\,501\) af op duizendtallen. Een getal.", ["49000", "49 000", "49.000"],
        r"Het eerste cijfer dat wegvalt is een \(5\), dus naar boven: \(49\,000\)."),
    casus("Een kassa rondt het totaal af op het dichtste veelvoud van \\(5\\) cent.", [
        inv(r"Hoeveel betaal je bij een totaal van \(8{,}42\) euro? Een getal.", ["8,40", "8.40", "8,4"],
            r"\(8{,}42\) ligt dichter bij \(8{,}40\) dan bij \(8{,}45\)."),
        inv(r"Hoeveel betaal je bij \(8{,}43\) euro? Een getal.", ["8,45", "8.45"], r"\(8{,}43\) ligt dichter bij \(8{,}45\)."),
        mk("Waarom rondt de kassa het totaal af en niet elk artikel apart?",
           ["anders tellen de afrondingen op", "het totaal is altijd een rond getal", "per artikel afronden is niet toegelaten", "zo betaal je altijd minder dan je kocht"], 0,
           "Elke afronding is een kleine fout. Rond je pas op het einde af, dan is er maar één."),
    ]),
    koppel("Verbind elke ongelijkheid met haar interval.",
           [(r"\(-1 < x \leq 4\)", r"\(\left]-1, 4\right]\)"), (r"\(x \geq -1\)", r"\(\left[-1, +\infty\right[\)"),
            (r"\(x < 4\)", r"\(\left]-\infty, 4\right[\)"), (r"\(-1 \leq x \leq 4\)", r"\(\left[-1, 4\right]\)")],
           [r"\(\left[-1, 4\right[\)"],
           "Kleiner dan of gelijk aan geeft een gesloten haakje, strikt kleiner een open haakje."),
    inv(r"Wat is het grootste gehele getal in \(\left]-6, -2\right[\)?", ["-3", "min 3", "min drie"],
        r"\(-2\) hoort er niet bij (open haakje). Het grootste gehele getal ervoor is \(-3\)."),
    tabel(r"Hoort het getal bij \(\left[-\frac{1}{2}, \sqrt{3}\right[\)?",
          [(r"\(-0{,}5\)", "ja"), (r"\(1{,}73\)", "ja"), (r"\(\sqrt{3}\)", "nee"), (r"\(-0{,}51\)", "nee"), (r"\(0\)", "ja")],
          r"\(-\frac{1}{2}\) hoort erbij (gesloten), \(\sqrt{3} \approx 1{,}732\) niet (open). \(1{,}73\) ligt er net onder.",
          kolommen=["ja", "nee"]),
    mk(r"Welk interval hoort bij: \(x\) is hoogstens \(2\) en meer dan \(-3\)?",
       [r"\(\left]-3, 2\right]\)", r"\(\left[-3, 2\right[\)", r"\(\left]-\infty, 2\right]\)", r"\(\left[-3, +\infty\right[\)"], 0,
       r"'Hoogstens 2': \(2\) doet mee. 'Meer dan \(-3\)': \(-3\) doet niet mee."),
    sleep(r"De oplossingen van \(x \geq 7\) schrijf je als [[\(\left[7, +\infty\right[\)]]. Op de getallenas teken je bij \(7\) een [[vol]] bolletje.",
          [r"\(\left]7, +\infty\right[\)", "leeg"], r"Het teken \(\geq\) laat \(7\) zelf toe."),
    keuze("Een lift mag hoogstens 630 kg dragen. De grens 630 kg hoort [[*er wel bij|er niet bij]], dus het haakje bij 630 is gesloten.",
          "'Hoogstens' laat de grens zelf nog toe."),
    mk(r"Wat is het verschil tussen \(\left[1, 4\right]\) en \(\left]1, 4\right[\)?",
       [r"enkel de getallen \(1\) en \(4\)", r"alle getallen tussen \(1\) en \(4\)", "er is helemaal geen enkel verschil", r"het getal \(2{,}5\) zit er niet in"], 0,
       "Het gesloten interval bevat de twee grenzen, het open niet. De rest is hetzelfde."),
    tabel("Klopt dit over intervallen?",
          [(r"In \(\left]0, 1\right[\) ligt een grootste getal.", F), (r"Tussen \(0{,}1\) en \(0{,}11\) liggen nog getallen.", J),
           (r"\(\left[3, 5\right]\) bevat oneindig veel getallen.", J), (r"Bij \(-\infty\) kan een gesloten haakje staan.", F)],
          r"Hoe dicht je ook bij \(1\) komt, er ligt altijd nog een getal tussen. \(\infty\) is geen getal, dus daar staat het haakje open.",
          kolommen=["Juist", "Fout"]),
    mk(r"Je rondt \(2{,}45\) eerst af op \(2{,}5\) en daarna op een geheel getal: \(3\). Wat geeft rechtstreeks afronden op een geheel getal?",
       [r"\(2\)", r"\(3\)", r"\(2{,}4\)", r"\(2{,}5\)"], 0,
       r"Rechtstreeks kijk je enkel naar de \(4\): naar beneden. Twee keer afronden kan het resultaat vervalsen."),
    mk(r"Welk getal ligt precies midden tussen \(-\frac{1}{2}\) en \(\frac{3}{4}\)?",
       [r"\(0{,}125\)", r"\(\frac{1}{4}\)", r"\(0{,}625\)", r"\(\frac{1}{2}\)"], 0,
       r"\((-0{,}5 + 0{,}75) : 2 = 0{,}25 : 2 = 0{,}125\)."),
    inv(r"Hoeveel gehele getallen kan \(x\) zijn als \(x \in \left[-3, 1\right[\)?", ["4", "vier"],
        r"\(-3, -2, -1\) en \(0\). \(1\) hoort er niet bij."),
    sorteer(r"Ligt het getal links of rechts van \(-\frac{2}{3}\) op de getallenas?", ["links", "rechts"],
            [(r"\(-0{,}7\)", "links"), (r"\(-0{,}6\)", "rechts"), (r"\(-1\)", "links"), (r"\(-0{,}66\)", "rechts"), (r"\(-\frac{3}{4}\)", "links")],
            r"\(-\frac{2}{3} = -0{,}666\ldots\). Links ligt alles wat kleiner is."),
    mk(r"Hoe schrijf je: \(x\) ligt niet onder \(-2\)?",
       [r"\(x \geq -2\)", r"\(x > -2\)", r"\(x \leq -2\)", r"\(-2 < x < +\infty\)"], 0,
       r"Niet onder \(-2\): gelijk aan \(-2\) mag ook."),
    keuze("Bij oneindig staat het haakje altijd open, want oneindig is [[*geen getal|het grootste getal|een gesloten grens]].",
          "Je kan oneindig nooit bereiken, dus het kan er ook niet bij horen."),
    open_(r"Schrijf de oplossingen van \(-1 < x \leq 4\) als interval. Leg ook uit hoe je ze op de getallenas tekent.",
          r"\(\left]-1, 4\right]\). Op de getallenas een leeg bolletje bij \(-1\), een vol bolletje bij \(4\), en een dikke lijn ertussen."),
]
