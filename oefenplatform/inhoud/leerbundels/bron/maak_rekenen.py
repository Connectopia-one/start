# -*- coding: utf-8 -*-
"""De leerbundel bij het gratis proefhoofdstuk Rekenen en breuken van Wiskunde.

Net als bij spelling is dit het hoofdstuk dat iemand zonder account mag
proberen. Het is dus ook het enige stuk leerstof dat een ouder ziet voor die
beslist, en daarom staat er meer in dan in een gewone bundel: bij elke regel
een voorbeeld dat je meteen zelf kan narekenen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

BUNDELS = {}

BUNDELS["rekenen-en-breuken"] = dict(
    vak="Wiskunde", titel="Rekenen en breuken",
    onder="Breuken, procenten en handig hoofdrekenen — met bij elke regel een voorbeeld.",
    secties=[
        dict(kop="Wat een breuk is", blokken=[
            ("p", "Een breuk is een geheel dat in gelijke stukken verdeeld is. Het onderste getal, "
                  "de <strong>noemer</strong>, zegt in hoeveel stukken. Het bovenste getal, de "
                  "<strong>teller</strong>, zegt hoeveel van die stukken je neemt."),
            ("fig", svg.breukstroken(470), r"Hoe groter de noemer, hoe kleiner elk stukje. \(\tfrac{1}{5}\) is dus kleiner dan \(\tfrac{1}{3}\)."),
            ("p", r"Staat boven en onder hetzelfde getal, dan heb je alle stukken samen: \(\tfrac{4}{4}\) is \(1\) geheel. "
                  r"En wordt er iets weggenomen, dan is wat overblijft ook een breuk: eet je \(3\) van de "
                  r"\(8\) stukken van een pizza, dan blijft er <strong>\(\tfrac{5}{8}\)</strong> over."),
        ]),
        dict(kop="Breuken die evenveel waard zijn", blokken=[
            ("p", "Twee breuken die er anders uitzien, kunnen precies evenveel waard zijn. "
                  r"\(\tfrac{2}{4}\) is hetzelfde als \(\tfrac{1}{2}\): je hebt het geheel alleen in kleinere stukjes gesneden."),
            ("fig", tabel(["Deze breuk", "is evenveel als"], [
                [r"\(\tfrac{2}{4}\)", r"\(\tfrac{1}{2}\)"],
                [r"\(\tfrac{4}{8}\)", r"\(\tfrac{1}{2}\)"],
                [r"\(\tfrac{2}{6}\)", r"\(\tfrac{1}{3}\)"],
                [r"\(\tfrac{10}{15}\)", r"\(\tfrac{2}{3}\)"],
                [r"\(\tfrac{6}{8}\)", r"\(\tfrac{3}{4}\)"],
            ], "60%"), "Teller en noemer allebei door hetzelfde getal delen: dat heet vereenvoudigen."),
            ("p", "<strong>Vereenvoudigen</strong> doe je door de teller en de noemer allebei door "
                  r"hetzelfde getal te delen. \(\tfrac{6}{8} : 2\) geeft \(\tfrac{3}{4}\). Lukt dat niet meer, dan is de breuk "
                  "zo eenvoudig als ze kan zijn."),
            ("weetje", "Om te vergelijken welke breuk het grootst is, zet je ze om in kommagetallen. "
                       r"\(\tfrac{2}{3}\) is ongeveer \(0{,}67\) en \(\tfrac{3}{8}\) is \(0{,}375\), dus \(\tfrac{2}{3}\) is groter."),
        ]),
        dict(kop="Rekenen met breuken", blokken=[
            ("p", "Hebben twee breuken dezelfde noemer, dan tel je gewoon de tellers op of trek je "
                  "ze af. De noemer blijft staan."),
            ("kader", r"<p style='margin:0 0 4px'><strong>\(\tfrac{1}{4} + \tfrac{2}{4} = \tfrac{3}{4}\)</strong> — de stukken zijn even groot, dus je telt ze gewoon.</p>"
                      r"<p style='margin:0'><strong>\(\tfrac{5}{8} - \tfrac{2}{8} = \tfrac{3}{8}\)</strong> — hetzelfde, maar dan aftrekken.</p>"),
            ("p", "Een breuk <em>van</em> een getal nemen doe je in twee stappen: eerst delen door de "
                  "noemer, dan vermenigvuldigen met de teller."),
            ("fig", svg.stappen(["Deel|door de noemer", "Maal|met de teller", "Klaar|lees je antwoord"]),
             r"\(\tfrac{3}{8}\) van \(64\): eerst \(64 : 8 = 8\), dan \(3 \cdot 8 = 24\)."),
            ("p", r"Zo gaat het altijd: \(\tfrac{1}{5}\) van \(45\) is \(45 : 5 = 9\), en \(\tfrac{2}{3}\) van \(27\) is \(27 : 3 = 9\), dan \(2 \cdot 9 = 18\)."),
        ]),
        dict(kop="Breuk, kommagetal en procent", blokken=[
            ("p", "Dezelfde hoeveelheid kan er op drie manieren uitzien. Van een breuk naar een "
                  r"kommagetal deel je de teller door de noemer: \(3 : 4 = 0{,}75\). Van een kommagetal naar "
                  r"procent vermenigvuldig je met \(100\)."),
            ("fig", tabel(["Breuk", "Kommagetal", "Procent"], [
                [r"\(\tfrac{1}{10}\)", r"\(0{,}1\)", "10%"],
                [r"\(\tfrac{1}{5}\)", r"\(0{,}2\)", "20%"],
                [r"\(\tfrac{1}{4}\)", r"\(0{,}25\)", "25%"],
                [r"\(\tfrac{1}{2}\)", r"\(0{,}5\)", "50%"],
                [r"\(\tfrac{3}{4}\)", r"\(0{,}75\)", "75%"],
            ], "80%"), "Deze vijf ken je het best uit het hoofd."),
            ("p", r"Daarmee vergelijk je ook vlot: is \(0{,}6\) meer of minder dan \(\tfrac{1}{2}\)? \(\tfrac{1}{2}\) is \(0{,}5\), dus \(0{,}6\) is meer."),
        ]),
        dict(kop="Procent rekenen", blokken=[
            ("p", r"Procent betekent <em>per honderd</em>. \(25\,\%\) is dus \(25\) van de \(100\), of een vierde van het geheel."),
            ("fig", svg.procentraster(25, 215), r"\(25\) van de \(100\) vakjes gekleurd: dat is \(25\,\%\), of \(\tfrac{1}{4}\)."),
            ("fig", tabel(["Zoek je", "Dan doe je", "Voorbeeld"], [
                ["10%", r"delen door \(10\)", r"\(10\,\%\) van \(240 = 24\)"],
                ["25%", r"delen door \(4\)", r"\(25\,\%\) van \(60 = 15\)"],
                ["50%", "de helft nemen", r"\(50\,\%\) van \(86 = 43\)"],
                ["20%", r"\(10\,\%\) nemen en verdubbelen", r"\(20\,\%\) van \(250 = 50\)"],
            ]), r"Bijna elke procentvraag los je op via \(10\,\%\)."),
            ("p", "Bij <strong>korting</strong> reken je eerst hoeveel de korting waard is en trek je "
                  r"die af. Een trui van \(40\) euro met \(25\,\%\) korting: \(25\,\%\) van \(40\) is \(10\) euro, dus je betaalt \(30\) euro."),
        ]),
        dict(kop="Handig hoofdrekenen", blokken=[
            ("p", "Een grote som wordt klein als je ze in stukken hakt of een omweg neemt."),
            ("fig", tabel(["Som", "Handige omweg", "Uitkomst"], [
                [r"\(348 + 156\)", r"\(300 + 100 = 400\), \(48 + 56 = 104\)", r"\(504\)"],
                [r"\(1\,000 - 365\)", r"\(1\,000 - 300 = 700\), dan \(- 65\)", r"\(635\)"],
                [r"\(25 \cdot 4\)", "vier kwartjes maken een euro", r"\(100\)"],
                [r"\(144 : 12\)", r"\(12 \cdot 12 = 144\)", r"\(12\)"],
                [r"\(0{,}5 \cdot 24\)", r"de helft van \(24\)", r"\(12\)"],
            ]), "Niet elke som vraagt om cijferen; vaak is omdenken sneller."),
            ("p", "<strong>Afronden</strong> is een getal vervangen door een rond getal dat er dicht "
                  r"bij ligt. Je kijkt naar het cijfer rechts van de plaats waarop je afrondt: \(5\) of "
                  r"meer gaat naar boven. \(2\,468\) afgerond op honderdtallen wordt dus \(2\,500\)."),
        ]),
        dict(kop="De volgorde van de bewerkingen", blokken=[
            ("p", "Staan er in één som verschillende bewerkingen, dan mag je niet zomaar van links "
                  "naar rechts werken. Er is een vaste volgorde."),
            ("fig", svg.stappen(["Haakjes|eerst ( ) uitrekenen", "Maal en delen|× en :", "Plus en min|+ en −"]),
             r"Bij \(12 + 3 \cdot 4\) reken je dus eerst \(3 \cdot 4 = 12\), en pas daarna \(12 + 12 = 24\)."),
            ("p", r"Haakjes zijn de baas: <strong>\((7 + 3) \cdot 5 = 50\)</strong>. Zonder haakjes zou \(7 + 3 \cdot 5\) "
                  r"iets helemaal anders geven, namelijk \(22\)."),
        ]),
        dict(kop="Kommagetallen en verdelen", blokken=[
            ("p", "Bij optellen en aftrekken zet je de komma's netjes onder elkaar, en vul je aan met "
                  r"nullen tot er evenveel cijfers achter de komma staan: \(2{,}50 + 3{,}75 = 6{,}25\)."),
            ("p", r"Bij delen reken je eerst zonder komma en zet je ze achteraf terug: \(42 : 2 = 21\), "
                  r"dus <strong>\(4{,}2 : 2 = 2{,}1\)</strong>."),
            ("p", "Gaat het over verdelen met maten, zet dan eerst alles in dezelfde eenheid. Een fles "
                  r"van \(2\) liter over glazen van \(250\) ml: \(2\) liter is \(2\,000\) ml, en \(2\,000 : 250 = 8\) glazen."),
            ("weetje", r"Een rekenmachine schrijft 1.2 met een punt. Op je blad schrijf je \(1{,}2\) met een komma. Hetzelfde getal."),
        ]),
    ],
    onthoud=[
        "De noemer zegt in hoeveel stukken, de teller hoeveel je er neemt.",
        "Hoe groter de noemer, hoe kleiner het stukje.",
        "Gelijke noemers? Dan tel je gewoon de tellers op.",
        "Een breuk van een getal: eerst delen door de noemer, dan maal de teller.",
        r"\(\tfrac{3}{4}\), \(0{,}75\) en \(75\,\%\) zijn drie namen voor hetzelfde.",
        r"Procent: zoek eerst \(10\,\%\) en reken van daaruit verder.",
        "Eerst haakjes, dan maal en delen, dan plus en min.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
