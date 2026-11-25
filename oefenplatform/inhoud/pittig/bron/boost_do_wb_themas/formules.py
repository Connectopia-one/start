"""Formules omvormen — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_formules: eigenschappen van gelijkheden, een letter
vrijmaken in wiskundige formules en in formules uit de natuurwetenschappen.
Met een zelfgetekend kladblad met twee omvormingen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, s_lijn, pix_zone

KB = "omvormingen-kladblad"
L1 = [("A", "2·Eₖ = m·v²"), ("B", "v² = 2·Eₖ − m"), ("C", "v = √(2·Eₖ − m)")]
L2 = [("D", "P − 2l = 2b"), ("E", "(P − 2l) : 2 = b"), ("F", "b = P − l")]


def _kladblad():
    d = []
    for x0, kop, opg, lijnen in [(40, "Oefening 1", "Maak v vrij in Eₖ = ½·m·v²", L1), (520, "Oefening 2", "Maak b vrij in P = 2l + 2b", L2)]:
        d.append(s_vak(x0, 60, 440, 540, vul="#ffffff", rand="#b9b29c", dikte=2, rond=12))
        d.append(s_tekst(x0 + 220, 100, kop, 22, vet=True))
        d.append(s_tekst(x0 + 220, 150, opg, 21))
        for i, (letter, t) in enumerate(lijnen):
            y = 250 + i * 110
            d.append(s_lijn(x0 + 20, y + 25, x0 + 420, y + 25, kleur="#e7e2d2", dikte=1))
            d.append(f'<circle cx="{x0+50}" cy="{y}" r="20" fill="#ffffff" stroke="#24331b" stroke-width="2"/>')
            d.append(s_tekst(x0 + 50, y + 7, letter, 20, vet=True))
            d.append(s_tekst(x0 + 95, y + 8, t, 25, "start"))
    return d


def _kz(kolom, i):
    return [pix_zone(40 + kolom * 480, 250 + i * 110 - 45, 440, 90)]


GRAFIEKEN = [dict(naam=KB, titel="Twee leerlingen maken een letter vrij", eigen=_kladblad)]
U = f"{KB}.svg"

VRAGEN = [
    klik("Klik op de eerste regel met een fout in oefening 1.", U, _kz(0, 1),
         r"Uit \(2E_{k} = m v^{2}\) volgt \(v^{2} = \frac{2E_{k}}{m}\): je deelt door \(m\), je trekt het niet af."),
    klik("Klik op de foute omvorming in oefening 2.", U, _kz(1, 2),
         r"\(\frac{P - 2l}{2} = \frac{P}{2} - l\). Je moet ook \(P\) door \(2\) delen."),
    mk(r"Het elektrisch vermogen is \(P = U \cdot I\). Hoe druk je \(I\) uit?",
       [r"\(I = \frac{P}{U}\)", r"\(I = P \cdot U\)", r"\(I = \frac{U}{P}\)", r"\(I = \frac{P}{U^{2}}\)"], 0,
       r"Beide leden delen door \(U\)."),
    inv(r"Er geldt \(s = v \cdot t\). Een trein rijdt \(600\) m aan \(15\) m/s. Hoeveel seconden duurt dat? Een getal.", ["40", "veertig"],
        r"\(t = \frac{s}{v} = \frac{600}{15} = 40\)."),
    mk(r"Maak \(r\) vrij in \(A = \pi r^{2}\), met \(r > 0\).",
       [r"\(r = \sqrt{\frac{A}{\pi}}\)", r"\(r = \frac{A}{\pi}\)", r"\(r = \sqrt{A} - \pi\)", r"\(r = \frac{\sqrt{A}}{2\pi}\)"], 0,
       r"Eerst delen door \(\pi\), dan de wortel. Omgekeerd aan de volgorde waarin de formule rekent."),
    inv(r"Een cirkel heeft een oppervlakte van \(50{,}27\) cm². Wat is de straal, afgerond op een cm?", ["4", "vier"],
        r"\(r = \sqrt{\frac{50{,}27}{\pi}} \approx \sqrt{16} = 4\)."),
    mk(r"Maak \(x\) vrij in \(y = \frac{x - 4}{5}\).",
       [r"\(x = 5y + 4\)", r"\(x = 5y - 4\)", r"\(x = \frac{y}{5} + 4\)", r"\(x = 5(y + 4)\)"], 0,
       r"Eerst maal \(5\): \(5y = x - 4\). Dan \(4\) erbij."),
    tabel("Is deze omvorming correct?",
          [(r"\(A = l \cdot b \Leftrightarrow l = \frac{A}{b}\)", "correct"), (r"\(P = 2l + 2b \Leftrightarrow l = P - b\)", "fout"),
           (r"\(F = k \cdot x \Leftrightarrow k = \frac{F}{x}\)", "correct"), (r"\(y = 3x + 6 \Leftrightarrow x = \frac{y}{3} - 6\)", "fout"),
           (r"\(c = \frac{n}{V} \Leftrightarrow V = \frac{n}{c}\)", "correct")],
          r"Bij de foute: \(l = \frac{P}{2} - b\) en \(x = \frac{y}{3} - 2\). De \(6\) moet ook gedeeld worden.",
          kolommen=["correct", "fout"]),
    volgorde(r"Zet de stappen om \(h\) vrij te maken in \(V = \frac{1}{3} \pi r^{2} h\) in de juiste volgorde.",
             [r"bepaal welke letter je zoekt: \(h\)", r"beide leden maal \(3\): \(3V = \pi r^{2} h\)", r"beide leden delen door \(\pi r^{2}\)", r"\(h = \frac{3V}{\pi r^{2}}\)"],
             "Eerst de breuk weg, dan de factoren voor h."),
    casus("Een gouden ring heeft een massa van \\(9{,}65\\) g. Goud heeft een massadichtheid \\(\\rho = 19{,}3\\) g/cm³.", [
        inv("Wat is het volume van de ring, in cm³?", ["0,5", "0.5"], r"\(V = \frac{m}{\rho} = \frac{9{,}65}{19{,}3} = 0{,}5\)."),
        keuze("Een even grote ring in zilver (10,5 g/cm³) is [[*lichter|zwaarder|even zwaar]].", "Hetzelfde volume met een kleinere dichtheid geeft minder massa."),
        inv("Hoeveel gram weegt die zilveren ring? Een getal.", ["5,25", "5.25"], r"\(m = \rho \cdot V = 10{,}5 \cdot 0{,}5 = 5{,}25\)."),
    ]),
    mk(r"Een fietser rijdt drie keer zo snel. Wat gebeurt er met \(E_{k} = \frac{1}{2} m v^{2}\)?",
       [r"\(\times 9\)", r"\(\times 3\)", r"\(\times 6\)", r"\(\times 27\)"], 0, r"De snelheid staat in het kwadraat: \(3^{2} = 9\)."),
    inv(r"In \(E_{k} = \frac{1}{2} m v^{2}\) is \(m = 2\) kg en \(E_{k} = 25\) J. Wat is \(v\) in m/s?", ["5", "vijf"],
        r"\(v^{2} = \frac{2E_{k}}{m} = 25\), dus \(v = 5\) (een snelheid hier positief)."),
    mk(r"Een kracht van \(600\) N drukt op \(0{,}02\) m². Wat is de druk?",
       [r"\(30\,000\) Pa", r"\(12\) Pa", r"\(3\,000\) Pa", r"\(300\,000\) Pa"], 0, r"\(p = \frac{F}{A} = \frac{600}{0{,}02} = 30\,000\)."),
    keuze("Een scherp mes snijdt beter: de oppervlakte wordt [[*kleiner|groter]] en de druk dus [[*groter|kleiner]].",
          r"In \(p = \frac{F}{A}\) staat \(A\) in de noemer."),
    tabel("De andere grootheden blijven gelijk. Wordt de gevraagde grootheid groter of kleiner?",
          [(r"\(R\) wordt groter. Wat doet \(I\) in \(I = \frac{U}{R}\)?", "kleiner"), (r"\(V\) wordt groter. Wat doet \(\rho\) in \(\rho = \frac{m}{V}\)?", "kleiner"),
           (r"\(t\) wordt groter. Wat doet \(E\) in \(E = P \cdot t\)?", "groter"), (r"\(h\) wordt groter. Wat doet \(E_{p}\) in \(E_{p} = m g h\)?", "groter")],
          "Een letter in de teller werkt mee, een letter in de noemer werkt tegen.",
          kolommen=["groter", "kleiner"]),
    mk(r"Waarom mag je \(x(x - 2) = 3(x - 2)\) niet zomaar door \(x - 2\) delen?",
       [r"\(x - 2\) kan nul zijn", "delen mag nooit bij een gelijkheid", r"\(x - 2\) is altijd negatief", "dan wordt de formule te lang"], 0,
       r"Als \(x = 2\), deel je door nul. Zo verlies je de oplossing \(x = 2\)."),
    inv(r"Een balk heeft \(V = l \cdot b \cdot h\). \(V = 120\), \(l = 6\) en \(b = 4\). Wat is \(h\)?", ["5", "vijf"], r"\(h = \frac{V}{l \cdot b} = \frac{120}{24} = 5\)."),
    sleep(r"Om \(b\) vrij te maken in \(A = \frac{b \cdot h}{2}\), vermenigvuldig je beide leden eerst met [[\(2\)]] en deel je daarna door [[\(h\)]].",
          [r"\(b\)", r"\(A\)"], r"Zo krijg je \(b = \frac{2A}{h}\)."),
    mk(r"Er geldt \(F_{z} = m \cdot g\) met \(g = 9{,}81\) N/kg. Een voorwerp heeft \(F_{z} = 490{,}5\) N. Wat is \(m\)?",
       [r"\(50\) kg", r"\(4\,812\) kg", r"\(500\) kg", r"\(5\) kg"], 0, r"\(m = \frac{490{,}5}{9{,}81} = 50\)."),
    koppel("Verbind elke vrij te maken letter met de uitdrukking.",
           [(r"\(v\) uit \(s = v \cdot t\)", r"\(\frac{s}{t}\)"), (r"\(t\) uit \(s = v \cdot t\)", r"\(\frac{s}{v}\)"), (r"\(s\) uit \(v = \frac{s}{t}\)", r"\(v \cdot t\)")],
           [r"\(s \cdot t\)"], "Dezelfde drie grootheden, telkens een andere vrijgemaakt."),
    inv(r"Een vierkant heeft omtrek \(P = 36\) cm. Wat is de oppervlakte in cm²?", ["81"], r"\(z = \frac{P}{4} = 9\) en \(A = z^{2} = 81\)."),
    keuze(r"Uit \(x^{2} = 36\) volgt \(x = 6\) [[*of|en]] \(x = -6\).", "Twee mogelijke oplossingen, maar niet tegelijk."),
    inv(r"Een veer met \(k = 50\) N/m wordt \(0{,}04\) m uitgerekt. Hoeveel newton is de veerkracht?", ["2", "twee"], r"\(F = k \cdot x = 50 \cdot 0{,}04 = 2\)."),
    mk(r"Maak \(b\) vrij in \(y = ax + b\).",
       [r"\(b = y - ax\)", r"\(b = ax - y\)", r"\(b = \frac{y}{ax}\)", r"\(b = y + ax\)"], 0, r"Trek \(ax\) af van beide leden."),
    mk(r"Maak \(a\) vrij in \(y = ax + b\), met \(x \neq 0\).",
       [r"\(a = \frac{y - b}{x}\)", r"\(a = y - b - x\)", r"\(a = \frac{x}{y - b}\)", r"\(a = \frac{y}{x} - b\cdot x\)"], 0,
       r"Eerst \(b\) aftrekken, dan delen door \(x\)."),
    tabel("Mag je deze stap altijd zetten bij een gelijkheid?",
          [("beide leden vermenigvuldigen met 5", "altijd"), (r"beide leden delen door \(x\)", "niet altijd"), ("bij beide leden 3 optellen", "altijd"),
           (r"van \(x^{2} = 9\) naar \(x = 3\) gaan", "niet altijd")],
          r"\(x\) kan nul zijn, en bij een kwadraat vergeet je zo \(x = -3\).",
          kolommen=["altijd", "niet altijd"]),
    inv(r"Een oplossing heeft \(c = 0{,}5\) mol/l en bevat \(n = 2\) mol. Hoeveel liter is \(V\)?", ["4", "vier"], r"\(V = \frac{n}{c} = \frac{2}{0{,}5} = 4\)."),
    open_(r"Maak \(r\) vrij in \(P = 2\pi r\) en bereken de straal van een cirkel met een omtrek van \(31{,}4\) cm. Leg elke stap uit.",
          r"Beide leden delen door \(2\pi\): \(r = \frac{P}{2\pi}\). Invullen: \(r = \frac{31{,}4}{2\pi} \approx 5\) cm."),
]
