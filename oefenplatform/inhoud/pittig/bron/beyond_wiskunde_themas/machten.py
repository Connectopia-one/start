"""Machtswortels, machten en logaritmen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent

GRAFIEKEN = []
PRENTEN = []

VRAGEN = [
    tabel(
        r"Vereenvoudig. Welke uitkomst hoort erbij?",
        [(r"\(\sqrt[3]{-125}\)", r"\(-5\)"), (r"\(27^{2/3}\)", r"\(9\)"), (r"\(\left(\tfrac{1}{4}\right)^{-3/2}\)", r"\(8\)"), (r"\(\sqrt[4]{81^{3}}\)", r"\(27\)")],
        r"\(27^{2/3} = (\sqrt[3]{27})^{2} = 9\). \(\left(\tfrac{1}{4}\right)^{-3/2} = 4^{3/2} = 8\). \(\sqrt[4]{81^{3}} = 3^{3} = 27\).",
        kolommen=[r"\(-5\)", r"\(9\)", r"\(8\)", r"\(27\)"],
    ),
    tabel(
        r"Juist of fout, voor alle \(a, b > 0\)?",
        [(r"\(\sqrt[n]{ab} = \sqrt[n]{a}\cdot\sqrt[n]{b}\)", J),
         (r"\(\sqrt{a^{2} + b^{2}} = a + b\)", F),
         (r"\(a^{1/2}\cdot a^{1/3} = a^{5/6}\)", J),
         (r"\(\left(a^{2}\right)^{3} = a^{5}\)", F),
         (r"\(\log(ab) = \log a + \log b\)", J),
         (r"\(\dfrac{\log a}{\log b} = \log(a - b)\)", F)],
        r"Een wortel verdeelt over een product, niet over een som. \((a^{2})^{3} = a^{6}\). Een quotiënt van logaritmen is \(\log_{b}a\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Vereenvoudig \(\sqrt{12} + \sqrt{75} - \sqrt{27}\).",
        [r"\(4\sqrt{3}\)", r"\(\sqrt{60}\)", r"\(10\sqrt{3}\)", r"\(2\sqrt{3}\)"],
        0,
        r"\(2\sqrt{3} + 5\sqrt{3} - 3\sqrt{3} = 4\sqrt{3}\).",
    ),
    mk(
        r"Maak de noemer rationaal: \(\dfrac{4}{\sqrt{7} + \sqrt{3}}\).",
        [r"\(\sqrt{7} - \sqrt{3}\)", r"\(\sqrt{7} + \sqrt{3}\)", r"\(\tfrac{4}{10}(\sqrt{7} - \sqrt{3})\)", r"\(4(\sqrt{7} - \sqrt{3})\)"],
        0,
        r"Vermenigvuldig met \(\sqrt{7} - \sqrt{3}\): de noemer wordt \(7 - 3 = 4\), dus \(\tfrac{4(\sqrt{7} - \sqrt{3})}{4}\).",
    ),
    inv(
        r"Los op voor \(x > 0\): \(x^{2/3} = 16\).",
        ["64"],
        r"Verhef beide leden tot de macht \(\tfrac{3}{2}\): \(x = 16^{3/2} = 4^{3} = 64\).",
    ),
    volgorde(
        "Zet van klein naar groot.",
        [r"\(2^{1/2}\)", r"\(3^{1/3}\)", r"\(\log_{2}3\)", r"\(\sqrt[4]{8}\)"],
        r"\(\sqrt{2} \approx 1{,}414\), \(\sqrt[3]{3} \approx 1{,}442\), \(\log_{2}3 \approx 1{,}585\), \(\sqrt[4]{8} = 2^{3/4} \approx 1{,}682\).",
    ),
    koppel(
        "Verbind elke logaritme met haar waarde.",
        [(r"\(\log_{4}8\)", r"\(\tfrac{3}{2}\)"), (r"\(\log_{9}\tfrac{1}{3}\)", r"\(-\tfrac{1}{2}\)"), (r"\(\log_{1/2}16\)", r"\(-4\)"), (r"\(\ln\sqrt{e}\)", r"\(\tfrac{1}{2}\)")],
        [r"\(2\)"],
        r"Schrijf beide als macht van hetzelfde grondtal: \(8 = 4^{3/2}\), \(\tfrac{1}{3} = 9^{-1/2}\), \(16 = \left(\tfrac{1}{2}\right)^{-4}\).",
    ),
    mk(
        r"Los op: \(\log_{3}(x + 1) + \log_{3}(x - 1) = 1\).",
        [r"\(x = 2\)", r"\(x = -2\) of \(x = 2\)", r"\(x = \sqrt{3}\)", r"\(x = 4\)"],
        0,
        r"\(\log_{3}(x^{2} - 1) = 1\) geeft \(x^{2} = 4\). \(x = -2\) valt weg: \(\log_{3}(-1)\) bestaat niet.",
    ),
    inv(
        r"Los op: \(4^{x} - 3\cdot 2^{x} - 4 = 0\). Typ \(x\).",
        ["2", "x = 2", "x=2"],
        r"Stel \(t = 2^{x}\): \(t^{2} - 3t - 4 = 0\) geeft \(t = 4\) of \(t = -1\). \(2^{x} = -1\) kan niet, dus \(x = 2\).",
    ),
    sorteer(
        "Bestaat de uitdrukking in de reële getallen?",
        ["Bestaat", "Bestaat niet"],
        [(r"\(\sqrt[3]{-27}\)", "Bestaat"), (r"\(\sqrt[4]{-16}\)", "Bestaat niet"), (r"\(\log_{2}0\)", "Bestaat niet"),
         (r"\(\ln 1\)", "Bestaat"), (r"\(\log_{1}5\)", "Bestaat niet"), (r"\(\left(-8\right)^{2}\)", "Bestaat")],
        "Een even wortel van een negatief getal en een logaritme van 0 bestaan niet. Grondtal 1 is niet toegelaten.",
    ),
    casus(
        r"Een radioactieve stof halveert elke 8 dagen. Er is nu 200 mg. Na \(t\) dagen is er \(m(t) = 200\cdot\left(\tfrac{1}{2}\right)^{t/8}\) mg.",
        [
            inv("Hoeveel mg is er na 24 dagen?", ["25", "25 mg"], r"\(200 \cdot \left(\tfrac{1}{2}\right)^{3} = 25\) mg."),
            mk("Welke uitdrukking geeft het aantal dagen tot er 10 mg over is?",
               [r"\(8\cdot\log_{2}20\)", r"\(\log_{2}20\)", r"\(\tfrac{8}{\log_{2}20}\)", r"\(20 \cdot 8\)"], 0,
               r"\(\left(\tfrac{1}{2}\right)^{t/8} = \tfrac{1}{20}\) geeft \(\tfrac{t}{8} = \log_{2}20\)."),
            mk("Afgerond op een dag?", ["35 dagen", "43 dagen", "4 dagen", "160 dagen"], 0, r"\(8 \cdot 4{,}32 \approx 34{,}6\)."),
        ],
    ),
    keuze(
        r"\(\log_{a}x\) bestaat enkel als \(x\) [[*strikt positief|positief of nul|verschillend van 1]] is en het grondtal \(a\) positief en verschillend van [[*1|0|e]] is.",
        "Een macht van een positief grondtal is altijd strikt positief, dus de logaritme van 0 of van een negatief getal bestaat niet.",
    ),
    mk(
        r"Schrijf \(\dfrac{\sqrt[3]{a^{2}}\cdot a^{-1}}{\sqrt{a}}\) als één macht van \(a\), met \(a > 0\).",
        [r"\(a^{-5/6}\)", r"\(a^{1/6}\)", r"\(a^{-1/6}\)", r"\(a^{7/6}\)"],
        0,
        r"\(\tfrac{2}{3} - 1 - \tfrac{1}{2} = -\tfrac{5}{6}\).",
    ),
    inv(
        r"Hoeveel is \(\log_{2}12 - \log_{2}3\)?",
        ["2"],
        r"\(\log_{2}\tfrac{12}{3} = \log_{2}4 = 2\).",
    ),

    mk(
        r"Een spaarbedrag groeit 3 % per jaar. Na hoeveel volle jaren is het voor het eerst minstens anderhalf keer zo groot?",
        ["14 jaar", "17 jaar", "13 jaar", "50 jaar"],
        0,
        r"\(1{,}03^{n} \geq 1{,}5\) geeft \(n \geq \dfrac{\ln 1{,}5}{\ln 1{,}03} \approx 13{,}7\), dus \(14\) jaar.",
    ),
    sleep(
        r"Voor \(a > 0\) is \(a^{m/n}\) gelijk aan de [[\(n\)-de]] machtswortel uit \(a^{m}\). Een negatieve exponent betekent het [[omgekeerde]].",
        [r"\(m\)-de", "tegengestelde"],
        r"\(a^{-p} = \tfrac{1}{a^{p}}\), niet \(-a^{p}\).",
    ),
    inv(
        r"Los op: \(\log(x) + \log(x + 15) = 2\). Typ \(x\).",
        ["5", "x = 5", "x=5"],
        r"\(x(x + 15) = 100\) geeft \(x^{2} + 15x - 100 = 0\): \(x = 5\) of \(x = -20\). Enkel \(5\) ligt in het domein.",
    ),
    tabel(
        r"Juist of fout?",
        [(r"\(\ln(e^{3}) = 3\)", J), (r"\(e^{\ln 5} = 5\)", J), (r"\(\ln(-e) = -1\)", F), (r"\(\ln e^{2} = (\ln e)^{2}\)", F), (r"\(\log_{10}0{,}001 = -3\)", J)],
        r"\(\ln\) en \(e^{x}\) heffen elkaar op. \(\ln(-e)\) bestaat niet. \(\ln e^{2} = 2\), \((\ln e)^{2} = 1\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Welke uitdrukking is gelijk aan \(2\log_{a}x - \tfrac{1}{2}\log_{a}y + \log_{a}z\)?",
        [r"\(\log_{a}\dfrac{x^{2}z}{\sqrt{y}}\)", r"\(\log_{a}\dfrac{x^{2}\sqrt{y}}{z}\)", r"\(\log_{a}(x^{2} - \sqrt{y} + z)\)", r"\(\log_{a}\dfrac{2xz}{y/2}\)"],
        0,
        "Een factor wordt een exponent, een som wordt een product, een verschil een quotiënt.",
    ),
    inv(
        r"Hoeveel cijfers heeft \(2^{100}\)? Gebruik \(\log 2 \approx 0{,}30103\).",
        ["31"],
        r"\(\log 2^{100} = 30{,}103\). Een getal met logaritme tussen \(30\) en \(31\) heeft \(31\) cijfers.",
    ),
    casus(
        r"Het geluidsniveau is \(L = 10\log\dfrac{I}{I_{0}}\) dB. Een stofzuiger geeft 70 dB.",
        [
            inv("Twee stofzuigers staan aan. Hoeveel dB is dat, afgerond op een geheel getal?", ["73", "73 dB"], r"\(10\log 2 \approx 3\) dB erbij."),
            mk("Hoeveel keer zo intens is 90 dB als 70 dB?", ["100 keer", "20 keer", "2 keer", "1000 keer"], 0, r"\(20\) dB meer is \(10^{2}\) keer de intensiteit."),
        ],
    ),
    mk(
        r"Los op: \(5^{2x - 1} = 125^{x + 1}\).",
        [r"\(x = -4\)", r"\(x = 4\)", r"\(x = -\tfrac{2}{5}\)", r"\(x = 2\)"],
        0,
        r"\(125 = 5^{3}\): \(2x - 1 = 3x + 3\), dus \(x = -4\).",
    ),
    sorteer(
        "Is de vereenvoudiging juist?",
        ["Juist", "Fout"],
        [(r"\(\sqrt[6]{a^{4}} = \sqrt[3]{a^{2}}\) voor \(a > 0\)", "Juist"),
         (r"\(\sqrt{a^{2}} = a\) voor elke reële \(a\)", "Fout"),
         (r"\(\sqrt{a^{2}} = |a|\) voor elke reële \(a\)", "Juist"),
         (r"\(\sqrt[3]{a^{3}} = a\) voor elke reële \(a\)", "Juist"),
         (r"\(\sqrt[4]{a^{4}} = a\) voor elke reële \(a\)", "Fout")],
        r"Een even wortel is nooit negatief: bij negatieve \(a\) krijg je \(|a|\). Een oneven wortel behoudt het teken.",
    ),
    mk(
        r"Voor welke \(x\) bestaat \(\log_{2}\dfrac{x - 1}{3 - x}\)?",
        [r"\(\left]1, 3\right[\)", r"\(\left]-\infty, 1\right[ \cup \left]3, +\infty\right[\)", r"\(\left]1, +\infty\right[\)", r"\(\left[1, 3\right]\)"],
        0,
        r"De breuk moet strikt positief zijn: teller en noemer hebben hetzelfde teken, dus \(1 < x < 3\).",
    ),
    inv(
        r"Bereken \(\log_{3}5\cdot\log_{5}7\cdot\log_{7}81\).",
        ["4"],
        r"Met grondtalverandering valt alles weg tot \(\log_{3}81 = 4\).",
    ),
    keuze(
        r"Omdat \(\ln\) een [[*stijgende|dalende]] functie is, blijft bij \(\ln a < \ln b\) het ongelijkheidsteken behouden: \(a\) [[*<|>]] \(b\). Bij \(\log_{1/2}\) draait het teken [[*wel|niet]] om.",
        r"Een logaritme met grondtal tussen \(0\) en \(1\) is dalend.",
    ),
    inv(
        r"Los op: \(\log_{1/2}(x - 3) \geq -2\). Wat is de grootste \(x\) die voldoet?",
        ["7"],
        r"\(\log_{1/2}\) daalt: \(x - 3 \leq \left(\tfrac{1}{2}\right)^{-2} = 4\), samen met \(x > 3\): \(\left]3, 7\right]\).",
    ),

]
