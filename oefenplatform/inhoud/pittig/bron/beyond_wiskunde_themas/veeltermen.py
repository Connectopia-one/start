"""Veeltermen, deelbaarheid en Horner — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent

GRAFIEKEN = []
PRENTEN = []

VRAGEN = [
    casus(
        r"Je deelt \(P(x) = 2x^{3} - 5x^{2} + x + 6\) met het schema van Horner door \(x - 2\).",
        [
            mk("Welke getallen zet je bovenaan in het schema?", [r"\(2,\ -5,\ 1,\ 6\)", r"\(2,\ 5,\ 1,\ 6\)", r"\(-5,\ 1,\ 6\)", r"\(6,\ 1,\ -5,\ 2\)"], 0,
               "Alle coëfficiënten, van de hoogste macht naar de constante term."),
            mk("Welke onderste rij krijg je?", [r"\(2,\ -1,\ -1,\ 4\)", r"\(2,\ -1,\ -1,\ 8\)", r"\(2,\ -9,\ 19,\ -32\)", r"\(2,\ -3,\ -5,\ -4\)"], 0,
               r"\(2\); \(-5 + 4 = -1\); \(1 - 2 = -1\); \(6 - 2 = 4\)."),
            mk("Wat is het quotiënt?", [r"\(2x^{2} - x - 1\)", r"\(2x^{3} - x^{2} - x\)", r"\(2x^{2} - x - 1 + 4\)", r"\(x^{2} - x - 1\)"], 0,
               "Het quotiënt is één graad lager. De laatste 4 is de rest."),
            inv(r"Hoeveel is \(P(2)\)?", ["4"], "Volgens de reststelling is de rest gelijk aan P(2)."),
        ],
    ),
    tabel(
        r"Wat is de rest van de deling?",
        [(r"\((x^{4} - 3x + 2) : (x - 1)\)", r"\(0\)"), (r"\((x^{3} + 2x^{2} - 5) : (x + 2)\)", r"\(-5\)"), (r"\((2x^{3} - x + 1) : (x + 1)\)", r"\(0\)"), (r"\((x^{5} + 1) : (x - 2)\)", r"\(33\)")],
        r"Reststelling: vul \(a\) in voor deling door \(x - a\). \(1 - 3 + 2 = 0\); \(-8 + 8 - 5 = -5\); \(-2 + 1 + 1 = 0\); \(32 + 1 = 33\).",
        kolommen=[r"\(0\)", r"\(-5\)", r"\(33\)"],
    ),
    mk(
        r"Voor welke \(k\) is \(x^{3} - kx^{2} + 2x + 3\) deelbaar door \(x + 1\)?",
        [r"\(k = 0\)", r"\(k = 2\)", r"\(k = -2\)", r"\(k = 6\)"],
        0,
        r"\(P(-1) = -1 - k - 2 + 3 = -k\). Dat is \(0\) voor \(k = 0\).",
    ),
    inv(
        r"\(P(x)\) gedeeld door \(x - 3\) geeft rest \(5\). Welke rest geeft \(P(x) + 2x\) gedeeld door \(x - 3\)?",
        ["11"],
        r"De nieuwe rest is \(P(3) + 2 \cdot 3 = 5 + 6 = 11\).",
    ),
    sorteer(
        r"Is \(x - 2\) een deler van de veelterm?",
        ["Deler", "Geen deler"],
        [(r"\(x^{3} - 8\)", "Deler"), (r"\(x^{2} + 4\)", "Geen deler"), (r"\(x^{3} - 2x^{2} + x - 2\)", "Deler"), (r"\(x^{4} - 16\)", "Deler"), (r"\(x^{3} + 8\)", "Geen deler"), (r"\(2x^{2} - 3x - 2\)", "Deler")],
        r"\(x - 2\) is een deler als \(P(2) = 0\). Reken telkens \(P(2)\) uit.",
    ),
    mk(
        r"Wat is de volledige ontbinding van \(x^{3} - 2x^{2} - 5x + 6\) in \(\mathbb{R}\)?",
        [r"\((x - 1)(x + 2)(x - 3)\)", r"\((x + 1)(x - 2)(x + 3)\)", r"\((x - 1)(x^{2} - x - 6)\)", r"\((x - 1)(x - 2)(x + 3)\)"],
        0,
        r"\(P(1) = 0\). Horner geeft \(x^{2} - x - 6 = (x + 2)(x - 3)\). Ontbind volledig, dus ook de tweedegraadsfactor.",
    ),
    koppel(
        "Verbind de veelterm met haar ontbinding.",
        [(r"\(x^{3} + 27\)", r"\((x + 3)(x^{2} - 3x + 9)\)"), (r"\(x^{4} - 1\)", r"\((x - 1)(x + 1)(x^{2} + 1)\)"), (r"\(9x^{2} - 6x + 1\)", r"\((3x - 1)^{2}\)"), (r"\(x^{3} - 4x\)", r"\(x(x - 2)(x + 2)\)")],
        [r"\((x + 3)^{3}\)"],
        r"Som van derdemachten: \(a^{3} + b^{3} = (a + b)(a^{2} - ab + b^{2})\). \(x^{2} + 1\) ontbindt niet in \(\mathbb{R}\).",
    ),
    tabel(
        "Over veeltermen: juist of fout?",
        [("Een veelterm van graad 4 heeft altijd 4 reële nulwaarden.", F),
         ("Een veelterm van graad 3 heeft minstens één reële nulwaarde.", J),
         (r"Als \(P(1) = P(-1) = 0\), dan is \(x^{2} - 1\) een deler van \(P\).", J),
         (r"Bij deling door \(x^{2} + 1\) is de rest hoogstens van graad 1.", J),
         (r"Horner werkt ook bij deling door \(2x - 1\) zonder aanpassing.", F)],
        r"Bij \(2x - 1\) deel je door \(x - \tfrac{1}{2}\) en daarna het quotiënt nog door 2. Een vierdegraadsveelterm als \(x^{4} + 1\) heeft geen reële nulwaarden.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"\(P(x) = x^{3} + ax^{2} + bx - 6\) is deelbaar door \(x - 1\) en door \(x - 2\). Hoeveel is \(a\)?",
        ["-6", "−6"],
        r"\(P(1) = 0\) geeft \(a + b = 5\). \(P(2) = 0\) geeft \(4a + 2b = -2\), dus \(2a + b = -1\). Dan is \(a = -6\) en \(b = 11\): \(P(x) = (x - 1)(x - 2)(x - 3)\).",
    ),
    mk(
        r"Welke gehele getallen komen in aanmerking als nulwaarde van \(x^{3} + 4x^{2} - 7x - 10\)?",
        [r"de delers van \(-10\): \(\pm 1, \pm 2, \pm 5, \pm 10\)", r"enkel \(1\) en \(-1\)", r"de delers van \(4\)", r"alle getallen tussen \(-10\) en \(10\)"],
        0,
        "Een gehele nulwaarde van een veelterm met gehele coëfficiënten en hoogste coëfficiënt 1 deelt de constante term.",
    ),
    inv(
        r"Hoeveel reële nulwaarden heeft \(x^{4} - 5x^{2} + 4\)?",
        ["4", "vier"],
        r"Stel \(t = x^{2}\): \(t^{2} - 5t + 4 = 0\), \(t = 1\) of \(t = 4\). Dat geeft \(x = \pm 1\) en \(x = \pm 2\).",
    ),
    keuze(
        r"Bij de deling van \(A(x)\) door \(B(x)\) geldt \(A = B \cdot Q + R\) met graad van \(R\) [[*kleiner dan|gelijk aan|groter dan]] de graad van \(B\). De graad van \(Q\) is graad \(A\) [[*min|plus|maal]] graad \(B\).",
        "Je deelt verder zolang de rest nog een graad heeft die even groot is als die van de deler.",
    ),
    mk(
        r"Wat is het quotiënt bij \((x^{4} - 1) : (x^{2} + 1)\)?",
        [r"\(x^{2} - 1\)", r"\(x^{2} + 1\)", r"\(x^{2}\)", r"\(x - 1\)"],
        0,
        r"\(x^{4} - 1 = (x^{2} - 1)(x^{2} + 1)\): de deling gaat op met rest \(0\).",
    ),
    tabel(
        r"De tekentabel van \(P(x) = (x + 1)(x - 2)^{2}\). Wat is het teken?",
        [(r"\(x < -1\)", "negatief"), (r"\(x = -1\)", "nul"), (r"\(-1 < x < 2\)", "positief"), (r"\(x = 2\)", "nul"), (r"\(x > 2\)", "positief")],
        r"Een kwadraat is nooit negatief: rond \(x = 2\) verandert het teken niet. Enkel bij \(x = -1\) wisselt het.",
        kolommen=["negatief", "nul", "positief"],
    ),
    inv(
        r"Los op: \(x^{3} - 6x^{2} + 11x - 6 = 0\). Typ de grootste oplossing.",
        ["3"],
        r"\(x = 1\) is een nulwaarde. Horner: \(x^{2} - 5x + 6 = (x - 2)(x - 3)\). Oplossingen \(1, 2, 3\).",
    ),
    sleep(
        r"De reststelling zegt: de rest bij de deling van \(P(x)\) door \(x - a\) is [[\(P(a)\)]]. Is die rest nul, dan is \(a\) een [[nulwaarde]] en \(x - a\) een [[deler]] van \(P(x)\).",
        [r"\(P(-a)\)", "asymptoot"],
        "Daarom zoek je bij ontbinden eerst een getal waarvoor de veelterm nul wordt.",
    ),
    mk(
        r"Een veelterm van graad 3 heeft nulwaarden \(-1\), \(2\) en \(4\) en \(P(0) = 16\). Wat is \(P(x)\)?",
        [r"\(2(x + 1)(x - 2)(x - 4)\)", r"\((x + 1)(x - 2)(x - 4)\)", r"\(-2(x + 1)(x - 2)(x - 4)\)", r"\(2(x - 1)(x + 2)(x + 4)\)"],
        0,
        r"\(P(x) = a(x + 1)(x - 2)(x - 4)\). \(P(0) = a \cdot 8 = 16\), dus \(a = 2\).",
    ),
    sorteer(
        r"Ontbindt de veelterm verder in \(\mathbb{R}\)?",
        ["Ontbindt verder", "Ontbindt niet verder"],
        [(r"\(x^{2} + x + 1\)", "Ontbindt niet verder"), (r"\(x^{2} - 2\)", "Ontbindt verder"), (r"\(x^{2} + 9\)", "Ontbindt niet verder"), (r"\(x^{2} - 6x + 9\)", "Ontbindt verder"), (r"\(x^{2} + 2x - 1\)", "Ontbindt verder")],
        r"Een tweedegraadsveelterm ontbindt in \(\mathbb{R}\) als \(D \geq 0\). \(x^{2} - 2 = (x - \sqrt{2})(x + \sqrt{2})\).",
    ),
    inv(
        r"De som van de nulwaarden van \(2x^{2} - 7x + 3\) is?",
        ["3,5", "3.5", "7/2"],
        r"Som \(= -\tfrac{b}{a} = \tfrac{7}{2}\). De nulwaarden zijn \(3\) en \(\tfrac{1}{2}\).",
    ),
    mk(
        r"Los op: \(x^{3} - x^{2} - 4x + 4 \geq 0\).",
        [r"\(\left[-2, 1\right] \cup \left[2, +\infty\right[\)", r"\(\left]-\infty, -2\right] \cup \left[1, 2\right]\)", r"\(\left[2, +\infty\right[\)", r"\(\left[-2, 2\right]\)"],
        0,
        r"\(x^{2}(x - 1) - 4(x - 1) = (x - 1)(x - 2)(x + 2)\). Tekentabel: positief tussen \(-2\) en \(1\) en vanaf \(2\).",
    ),
    tabel(
        "Welke graad heeft het quotiënt?",
        [(r"graad 7 gedeeld door graad 3", "4"), (r"graad 5 gedeeld door graad 1", "4"), (r"graad 4 gedeeld door graad 2", "2"), (r"graad 6 gedeeld door graad 3", "3")],
        "De graad van het quotiënt is het verschil van de graden.",
        kolommen=["2", "3", "4"],
    ),
    keuze(
        r"Bij Horner voor \(x^{4} + 3x - 1\) zet je bovenaan [[*1, 0, 0, 3, −1|1, 3, −1|1, 0, 3, −1]]: elke ontbrekende macht krijgt een [[*0|1|weglating]].",
        "Elke macht van de hoogste tot de constante krijgt een plaats, ook als ze ontbreekt.",
    ),
    mk(
        r"De rest bij \(P(x) : (x - 1)\) is \(3\) en bij \(P(x) : (x + 1)\) is \(-1\). Wat is de rest bij \(P(x) : (x^{2} - 1)\)?",
        [r"\(2x + 1\)", r"\(2\)", r"\(x + 2\)", r"\(-3\)"],
        0,
        r"De rest is \(ax + b\) met \(a + b = 3\) en \(-a + b = -1\): \(a = 2\), \(b = 1\).",
    ),
    inv(
        r"Vul aan: \(x^{3} - 64 = (x - 4)(x^{2} + 4x + \ldots)\).",
        ["16"],
        r"\(a^{3} - b^{3} = (a - b)(a^{2} + ab + b^{2})\) met \(b = 4\): \(b^{2} = 16\).",
    ),
    tabel(
        r"Is het getal een nulwaarde van \(2x^{3} - 3x^{2} - 11x + 6\)?",
        [(r"\(3\)", J), (r"\(-2\)", J), (r"\(\tfrac{1}{2}\)", J), (r"\(1\)", F)],
        r"\(54 - 27 - 33 + 6 = 0\); \(-16 - 12 + 22 + 6 = 0\); \(\tfrac{1}{4} - \tfrac{3}{4} - \tfrac{11}{2} + 6 = 0\); \(2 - 3 - 11 + 6 = -6\).",
        kolommen=["Juist", "Fout"],
    ),
    volgorde(
        r"Zet de stappen om \(x^{3} + 2x^{2} - x - 2\) volledig te ontbinden in volgorde.",
        [r"een nulwaarde zoeken onder de delers van \(-2\)", r"vaststellen dat \(P(1) = 0\)", r"met Horner delen door \(x - 1\)", r"\(x^{2} + 3x + 2\) ontbinden", r"\((x - 1)(x + 1)(x + 2)\) noteren"],
        "Eerst één nulwaarde, dan delen, dan verder ontbinden.",
    ),
    mk(
        r"Welke uitspraak over \(P(x) = x^{4} + x^{2} + 1\) klopt?",
        [r"ze heeft geen reële nulwaarden", r"ze heeft vier reële nulwaarden", r"\(x = -1\) is een nulwaarde", r"ze is deelbaar door \(x - 1\)"],
        0,
        r"Voor elke reële \(x\) is \(x^{4} + x^{2} + 1 \geq 1\).",
    ),
]
