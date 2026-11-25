"""Pythagoras en de goniometrische verhoudingen — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_pythagoras: de stelling van Pythagoras in het vlak en in de
ruimte, de afstand tussen twee punten, en sinus, cosinus en tangens van een
scherpe hoek met de grondformule. Met twee zelfgetekende prenten: een
rechthoekige driehoek met genummerde zijden en een assenstelsel met punten."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_tekst, pix_zone, venster, punt_zone

RD = "rechthoekige-driehoek-zijden"
PA, PC, PB = (170, 540), (800, 540), (800, 140)
MIDDEN = {"1": ((PA[0] + PB[0]) / 2 - 30, (PA[1] + PB[1]) / 2 - 30), "2": ((PC[0] + PB[0]) / 2 + 36, (PC[1] + PB[1]) / 2),
          "3": ((PA[0] + PC[0]) / 2, PA[1] + 36)}


def _driehoek():
    pts = " ".join(f"{x},{y}" for x, y in (PA, PC, PB))
    d = [f'<polygon points="{pts}" fill="#e6efdc" stroke="#24331b" stroke-width="4"/>',
         f'<rect x="{PC[0]-36}" y="{PC[1]-36}" width="36" height="36" fill="none" stroke="#24331b" stroke-width="3"/>',
         f'<path d="M {PA[0]+80} {PA[1]} A 80 80 0 0 0 {PA[0]+80*0.8437:.1f} {PA[1]-80*0.5368:.1f}" fill="none" stroke="#b5651d" stroke-width="4"/>',
         s_tekst(PA[0] + 110, PA[1] - 18, "α", 30, kleur="#b5651d", vet=True),
         f'<path d="M {PB[0]} {PB[1]+80} A 80 80 0 0 1 {PB[0]-80*0.8437:.1f} {PB[1]+80*0.5368:.1f}" fill="none" stroke="#7a4b8c" stroke-width="4"/>',
         s_tekst(PB[0] - 40, PB[1] + 120, "β", 30, kleur="#7a4b8c", vet=True)]
    for t, (x, y) in [("A", (PA[0] - 30, PA[1] + 10)), ("C", (PC[0] + 30, PC[1] + 10)), ("B", (PB[0] + 30, PB[1] - 10))]:
        d.append(s_tekst(x, y, t, 26, vet=True))
    for n, (x, y) in MIDDEN.items():
        d.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="#3b6fa0"/>')
        d.append(s_tekst(x, y + 8, n, 22, kleur="#ffffff", vet=True))
    return d


def _zz(n):
    x, y = MIDDEN[n]
    return [pix_zone(x - 40, y - 40, 80, 80)]


AS = venster("punten-afstand", -4, 6, -4, 6)
GRAFIEKEN = [dict(naam=RD, titel="Rechthoekige driehoek ABC met drie genummerde zijden", eigen=_driehoek),
             dict(naam=AS, titel="Vijf punten in een assenstelsel",
                  punten=[(1, 1, "A"), (4, 5, "B"), (-2, 3, "C"), (-3, -1, "D"), (5, -2, "E")])]
UD, UA = f"{RD}.svg", f"{AS}.svg"

VRAGEN = [
    klik(r"Klik op de overstaande zijde van \(\alpha\).", UD, _zz("2"), r"De overstaande zijde ligt tegenover de hoek: \(BC\)."),
    klik("Klik op de schuine zijde.", UD, _zz("1"), r"De schuine zijde ligt tegenover de rechte hoek: \(AB\)."),
    klik(r"Klik op de aanliggende rechthoekszijde van \(\alpha\).", UD, _zz("3"), r"\(AC\) vormt samen met de schuine zijde de hoek \(\alpha\)."),
    klik(r"Klik op de overstaande zijde van \(\beta\).", UD, _zz("3"), r"Voor \(\beta\) wisselen de rollen: \(AC\) ligt tegenover \(\beta\)."),
    klik("Klik op een punt dat op afstand 5 van A ligt.", UA, [punt_zone(AS, 4, 5), punt_zone(AS, 5, -2)],
         r"\(AB = \sqrt{3^{2} + 4^{2}} = 5\) en \(AE = \sqrt{4^{2} + 3^{2}} = 5\)."),
    klik("Klik op het punt dat het dichtst bij de oorsprong ligt.", UA, [punt_zone(AS, 1, 1)],
         r"\(OA = \sqrt{2} \approx 1{,}4\). \(D\) ligt op \(\sqrt{10}\), \(C\) op \(\sqrt{13}\)."),
    inv(r"De schuine zijde is \(17\), de overstaande zijde van \(\alpha\) is \(8\). Wat is \(\cos \alpha\)? Schrijf als breuk, bv. 3/4.", ["15/17"],
        r"De aanliggende zijde is \(\sqrt{17^{2} - 8^{2}} = \sqrt{225} = 15\). \(\cos \alpha = \frac{15}{17}\)."),
    inv(r"De rechthoekszijden zijn \(7\) en \(24\). Hoe lang is de schuine zijde? Een getal.", ["25", "vijfentwintig"],
        r"\(\sqrt{49 + 576} = \sqrt{625} = 25\)."),
    inv(r"De schuine zijde is \(10\) en een rechthoekszijde \(6\). Hoe lang is de andere? Een getal.", ["8", "acht"],
        r"\(\sqrt{100 - 36} = \sqrt{64} = 8\)."),
    tabel("Is een driehoek met deze zijden rechthoekig?",
          [(r"\(8\), \(15\), \(17\)", "ja"), (r"\(6\), \(7\), \(9\)", "nee"), (r"\(20\), \(21\), \(29\)", "ja"), (r"\(1\), \(1\), \(\sqrt{2}\)", "ja"), (r"\(4\), \(5\), \(6\)", "nee")],
          r"Controleer of de twee kleinste kwadraten samen het grootste geven: \(400 + 441 = 841 = 29^{2}\), maar \(36 + 49 = 85 \neq 81\).",
          kolommen=["ja", "nee"]),
    mk(r"Een balk is \(3\) bij \(4\) bij \(12\) cm. Hoe lang is de ruimtediagonaal?",
       [r"\(13\) cm", r"\(19\) cm", r"\(5\) cm", r"\(\sqrt{153}\) cm"], 0,
       r"Eerst de diagonaal van het grondvlak: \(5\). Dan \(\sqrt{5^{2} + 12^{2}} = 13\)."),
    inv(r"Wat is de afstand tussen \(P(-2, 3)\) en \(Q(4, -5)\)? Een getal.", ["10", "tien"],
        r"\(\sqrt{6^{2} + 8^{2}} = \sqrt{100} = 10\). Let op de tekens bij het aftrekken."),
    mk(r"Hoe lang is de ruimtediagonaal van een kubus met ribbe \(2\)?",
       [r"\(2\sqrt{3}\)", r"\(2\sqrt{2}\)", r"\(\sqrt{6}\)", r"\(\sqrt{12} + 1\)"], 0,
       r"\(\sqrt{2^{2} + 2^{2} + 2^{2}} = \sqrt{12} = 2\sqrt{3}\)."),
    casus("Een computerscherm is \\(48\\) cm breed en \\(36\\) cm hoog.", [
        inv("Hoe lang is de diagonaal, in cm? Een getal.", ["60", "zestig"], r"\(\sqrt{48^{2} + 36^{2}} = \sqrt{3600} = 60\)."),
        inv("Hoeveel procent langer is de diagonaal dan de breedte? Een getal.", ["25", "25%"], r"\(60 : 48 = 1{,}25\): \(25\,\%\) langer."),
        keuze("Een scherm van 96 bij 72 cm heeft een diagonaal van [[*120|84|168]] cm.", "Alle maten keer 2, dus de diagonaal ook."),
    ]),
    mk(r"Een vlieger hangt aan een strak touw van \(50\) m dat een hoek van \(40^{\circ}\) maakt met de grond. Welke berekening geeft de hoogte?",
       [r"\(50 \cdot \sin 40^{\circ}\)", r"\(50 \cdot \cos 40^{\circ}\)", r"\(50 \cdot \tan 40^{\circ}\)", r"\(\frac{50}{\sin 40^{\circ}}\)"], 0,
       "De hoogte is de overstaande zijde, het touw de schuine zijde."),
    inv("Hoe hoog hangt die vlieger, afgerond op 0,1 m?", ["32,1", "32.1"], r"\(50 \cdot \sin 40^{\circ} \approx 32{,}14\)."),
    mk(r"Een weg stijgt \(12\) m over een horizontale afstand van \(100\) m. Wat is \(\tan \alpha\)?",
       [r"\(0{,}12\)", r"\(0{,}88\)", r"\(1{,}2\)", r"\(\frac{100}{12}\)"], 0, r"Overstaande gedeeld door aanliggende: \(12 : 100\)."),
    inv(r"\(\cos \alpha = 0{,}28\) en \(\alpha\) is scherp. Wat is \(\sin \alpha\)?", ["0,96", "0.96"],
        r"\(\sin^{2}\alpha = 1 - 0{,}0784 = 0{,}9216\), dus \(\sin \alpha = 0{,}96\)."),
    tabel("Klopt dit over de goniometrische getallen van een scherpe hoek?",
          [(r"\(\sin 30^{\circ} = 0{,}5\)", J), (r"\(\tan \alpha\) kan groter zijn dan \(1\).", J),
           (r"Met \(\alpha\) en \(\beta\) de twee scherpe hoeken is \(\sin \alpha = \cos \beta\).", J), (r"Als \(\alpha\) groter wordt, wordt \(\cos \alpha\) groter.", F)],
          r"De overstaande zijde van \(\alpha\) is de aanliggende van \(\beta\). Bij een grotere hoek wordt de aanliggende zijde relatief korter.",
          kolommen=["Juist", "Fout"]),
    sorteer("Welk goniometrisch getal gebruik je?", [r"\(\sin\)", r"\(\cos\)", r"\(\tan\)"],
            [(r"\(\alpha\) en de schuine zijde gekend, de aanliggende gezocht", r"\(\cos\)"),
             (r"overstaande en aanliggende gekend, \(\alpha\) gezocht", r"\(\tan\)"),
             (r"overstaande en schuine gekend, \(\alpha\) gezocht", r"\(\sin\)"),
             (r"\(\alpha\) en de overstaande gekend, de schuine gezocht", r"\(\sin\)")],
            "Kijk welke twee zijden meedoen: die bepalen het getal."),
    mk(r"De overstaande zijde is \(5\) en de schuine zijde \(10\). Hoe groot is \(\alpha\)?",
       [r"\(30^{\circ}\)", r"\(60^{\circ}\)", r"\(45^{\circ}\)", r"\(26{,}6^{\circ}\)"], 0,
       r"\(\sin \alpha = 0{,}5\), dus \(\alpha = 30^{\circ}\)."),
    inv(r"\(\tan \alpha = 1\). Hoeveel graden is \(\alpha\)?", ["45"], r"Overstaande en aanliggende zijn even lang: \(45^{\circ}\)."),
    keuze("In een rechthoekige driehoek ligt de schuine zijde altijd [[*tegenover de rechte hoek|naast de rechte hoek|tegenover de kleinste hoek]].",
          "Daarom is ze ook de langste zijde."),
    koppel("Verbind de formule met haar naam.",
           [(r"\(\sin^{2}\alpha + \cos^{2}\alpha = 1\)", "de grondformule"), (r"\(a^{2} + b^{2} = c^{2}\)", "de stelling van Pythagoras"),
            (r"\(\sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}\)", "de afstand tussen twee punten")],
           ["de tangensregel"], "De grondformule is Pythagoras, gedeeld door het kwadraat van de schuine zijde."),
    inv(r"Een rechthoek is \(9\) cm lang en zijn diagonaal is \(15\) cm. Hoe breed is hij, in cm?", ["12", "twaalf"],
        r"\(\sqrt{15^{2} - 9^{2}} = \sqrt{144} = 12\)."),
    mk(r"Waarom mag je in een driehoek met zijden \(5\), \(6\) en \(8\) niet zomaar \(\sin \alpha = \frac{\text{overstaande}}{\text{schuine}}\) gebruiken?",
       ["hij is niet rechthoekig", "omdat de zijden te klein zijn", "omdat 8 geen kwadraat is", "omdat je eerst de omtrek moet kennen"], 0,
       r"\(25 + 36 = 61 \neq 64\). Die definities gelden enkel in een rechthoekige driehoek."),
    sleep(r"In een rechthoekige driehoek met \(\alpha = 30^{\circ}\) en een schuine zijde van \(8\) is de overstaande zijde van \(\alpha\) gelijk aan [[4]], want \(\sin 30^{\circ} =\) [[\(0{,}5\)]].",
          ["8", r"\(2\)"], r"\(8 \cdot 0{,}5 = 4\)."),
    open_("Leg uit hoe de grondformule van de goniometrie volgt uit de stelling van Pythagoras.",
          r"Noem de zijden \(a\) (overstaande), \(b\) (aanliggende) en \(c\) (schuine). Pythagoras: \(a^{2} + b^{2} = c^{2}\). Deel alles door \(c^{2}\): \(\left(\frac{a}{c}\right)^{2} + \left(\frac{b}{c}\right)^{2} = 1\), en dat is \(\sin^{2}\alpha + \cos^{2}\alpha = 1\)."),
]
