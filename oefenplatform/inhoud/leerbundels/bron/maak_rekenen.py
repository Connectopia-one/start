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
            ("fig", svg.breukstroken(470), "Hoe groter de noemer, hoe kleiner elk stukje. 1/5 is dus kleiner dan 1/3."),
            ("p", "Staat boven en onder hetzelfde getal, dan heb je alle stukken samen: 4/4 is 1 geheel. "
                  "En wordt er iets weggenomen, dan is wat overblijft ook een breuk: eet je 3 van de "
                  "8 stukken van een pizza, dan blijft er <strong>5/8</strong> over."),
        ]),
        dict(kop="Breuken die evenveel waard zijn", blokken=[
            ("p", "Twee breuken die er anders uitzien, kunnen precies evenveel waard zijn. "
                  "2/4 is hetzelfde als 1/2: je hebt het geheel alleen in kleinere stukjes gesneden."),
            ("fig", tabel(["Deze breuk", "is evenveel als"], [
                ["2/4", "1/2"],
                ["4/8", "1/2"],
                ["2/6", "1/3"],
                ["10/15", "2/3"],
                ["6/8", "3/4"],
            ], "60%"), "Teller en noemer allebei door hetzelfde getal delen: dat heet vereenvoudigen."),
            ("p", "<strong>Vereenvoudigen</strong> doe je door de teller en de noemer allebei door "
                  "hetzelfde getal te delen. 6/8 : 2 geeft 3/4. Lukt dat niet meer, dan is de breuk "
                  "zo eenvoudig als ze kan zijn."),
            ("weetje", "Om te vergelijken welke breuk het grootst is, zet je ze om in kommagetallen. "
                       "2/3 is ongeveer 0,67 en 3/8 is 0,375, dus 2/3 is groter."),
        ]),
        dict(kop="Rekenen met breuken", blokken=[
            ("p", "Hebben twee breuken dezelfde noemer, dan tel je gewoon de tellers op of trek je "
                  "ze af. De noemer blijft staan."),
            ("kader", "<p style='margin:0 0 4px'><strong>1/4 + 2/4 = 3/4</strong> — de stukken zijn even groot, dus je telt ze gewoon.</p>"
                      "<p style='margin:0'><strong>5/8 − 2/8 = 3/8</strong> — hetzelfde, maar dan aftrekken.</p>"),
            ("p", "Een breuk <em>van</em> een getal nemen doe je in twee stappen: eerst delen door de "
                  "noemer, dan vermenigvuldigen met de teller."),
            ("fig", svg.stappen(["Deel|door de noemer", "Maal|met de teller", "Klaar|lees je antwoord"]),
             "3/8 van 64: eerst 64 : 8 = 8, dan 3 × 8 = 24."),
            ("p", "Zo gaat het altijd: 1/5 van 45 is 45 : 5 = 9, en 2/3 van 27 is 27 : 3 = 9, dan 2 × 9 = 18."),
        ]),
        dict(kop="Breuk, kommagetal en procent", blokken=[
            ("p", "Dezelfde hoeveelheid kan er op drie manieren uitzien. Van een breuk naar een "
                  "kommagetal deel je de teller door de noemer: 3 : 4 = 0,75. Van een kommagetal naar "
                  "procent vermenigvuldig je met 100."),
            ("fig", tabel(["Breuk", "Kommagetal", "Procent"], [
                ["1/10", "0,1", "10%"],
                ["1/5", "0,2", "20%"],
                ["1/4", "0,25", "25%"],
                ["1/2", "0,5", "50%"],
                ["3/4", "0,75", "75%"],
            ], "80%"), "Deze vijf ken je het best uit het hoofd."),
            ("p", "Daarmee vergelijk je ook vlot: is 0,6 meer of minder dan 1/2? 1/2 is 0,5, dus 0,6 is meer."),
        ]),
        dict(kop="Procent rekenen", blokken=[
            ("p", "Procent betekent <em>per honderd</em>. 25% is dus 25 van de 100, of een vierde van het geheel."),
            ("fig", svg.procentraster(25, 215), "25 van de 100 vakjes gekleurd: dat is 25%, of 1/4."),
            ("fig", tabel(["Zoek je", "Dan doe je", "Voorbeeld"], [
                ["10%", "delen door 10", "10% van 240 = 24"],
                ["25%", "delen door 4", "25% van 60 = 15"],
                ["50%", "de helft nemen", "50% van 86 = 43"],
                ["20%", "10% nemen en verdubbelen", "20% van 250 = 50"],
            ]), "Bijna elke procentvraag los je op via 10%."),
            ("p", "Bij <strong>korting</strong> reken je eerst hoeveel de korting waard is en trek je "
                  "die af. Een trui van 40 euro met 25% korting: 25% van 40 is 10 euro, dus je betaalt 30 euro."),
        ]),
        dict(kop="Handig hoofdrekenen", blokken=[
            ("p", "Een grote som wordt klein als je ze in stukken hakt of een omweg neemt."),
            ("fig", tabel(["Som", "Handige omweg", "Uitkomst"], [
                ["348 + 156", "300 + 100 = 400, 48 + 56 = 104", "504"],
                ["1 000 − 365", "1 000 − 300 = 700, dan − 65", "635"],
                ["25 × 4", "vier kwartjes maken een euro", "100"],
                ["144 : 12", "12 × 12 = 144", "12"],
                ["0,5 × 24", "de helft van 24", "12"],
            ]), "Niet elke som vraagt om cijferen; vaak is omdenken sneller."),
            ("p", "<strong>Afronden</strong> is een getal vervangen door een rond getal dat er dicht "
                  "bij ligt. Je kijkt naar het cijfer rechts van de plaats waarop je afrondt: 5 of "
                  "meer gaat naar boven. 2 468 afgerond op honderdtallen wordt dus 2 500."),
        ]),
        dict(kop="De volgorde van de bewerkingen", blokken=[
            ("p", "Staan er in één som verschillende bewerkingen, dan mag je niet zomaar van links "
                  "naar rechts werken. Er is een vaste volgorde."),
            ("fig", svg.stappen(["Haakjes|eerst ( ) uitrekenen", "Maal en delen|× en :", "Plus en min|+ en −"]),
             "Bij 12 + 3 × 4 reken je dus eerst 3 × 4 = 12, en pas daarna 12 + 12 = 24."),
            ("p", "Haakjes zijn de baas: <strong>(7 + 3) × 5 = 50</strong>. Zonder haakjes zou 7 + 3 × 5 "
                  "iets helemaal anders geven, namelijk 22."),
        ]),
        dict(kop="Kommagetallen en verdelen", blokken=[
            ("p", "Bij optellen en aftrekken zet je de komma's netjes onder elkaar, en vul je aan met "
                  "nullen tot er evenveel cijfers achter de komma staan: 2,50 + 3,75 = 6,25."),
            ("p", "Bij delen reken je eerst zonder komma en zet je ze achteraf terug: 42 : 2 = 21, "
                  "dus <strong>4,2 : 2 = 2,1</strong>."),
            ("p", "Gaat het over verdelen met maten, zet dan eerst alles in dezelfde eenheid. Een fles "
                  "van 2 liter over glazen van 250 ml: 2 liter is 2 000 ml, en 2 000 : 250 = 8 glazen."),
            ("weetje", "Een rekenmachine schrijft 1.2 met een punt. Op je blad schrijf je 1,2 met een komma. Hetzelfde getal."),
        ]),
    ],
    onthoud=[
        "De noemer zegt in hoeveel stukken, de teller hoeveel je er neemt.",
        "Hoe groter de noemer, hoe kleiner het stukje.",
        "Gelijke noemers? Dan tel je gewoon de tellers op.",
        "Een breuk van een getal: eerst delen door de noemer, dan maal de teller.",
        "3/4, 0,75 en 75% zijn drie namen voor hetzelfde.",
        "Procent: zoek eerst 10% en reken van daaruit verder.",
        "Eerst haakjes, dan maal en delen, dan plus en min.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
