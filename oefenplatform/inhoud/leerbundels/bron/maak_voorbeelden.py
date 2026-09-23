# -*- coding: utf-8 -*-
"""Voorbeeldbundels voor aardrijkskunde en geschiedenis."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

BUNDELS = {}

BUNDELS["kaartlezen-en-orientatie"] = dict(
    vak="Aardrijkskunde", titel="Kaartlezen en oriëntatie",
    onder="Een kaart lezen: richting, legende, schaal en coördinaten.",
    secties=[
        dict(kop="De windroos", blokken=[
            ("p", "Op bijna elke kaart wijst het noorden naar boven. Met de vier hoofdrichtingen en de vier tussenrichtingen kan je elke plaats beschrijven."),
            ("fig", svg.windroos(78), "Met de klok mee: noord, noordoost, oost, zuidoost, zuid, zuidwest, west, noordwest."),
            ("p", "Een geheugensteuntje om ze in de juiste volgorde te houden: <strong>N</strong>ooit <strong>O</strong>oit <strong>Z</strong>al ik <strong>W</strong>eggaan."),
            ("weetje", "De zon komt op in het oosten en gaat onder in het westen. Weet je hoe laat het is, dan weet je dus ook ongeveer waar het noorden ligt, zonder kompas."),
        ]),
        dict(kop="De legende", blokken=[
            ("p", "Een kaart kan niet alles tekenen zoals het er echt uitziet. Daarom gebruikt ze <strong>symbolen</strong>, en in de legende staat wat elk symbool betekent."),
            ("fig", tabel(["Vaak gebruikte kleur", "Wat het meestal betekent"], [
                ["blauw", "water: rivieren, meren, de zee"],
                ["groen", "laag land, bossen, weiden"],
                ["geel en bruin", "hoger land, heuvels en bergen"],
                ["rood of grijs", "wegen en bebouwing"],
                ["zwarte lijnen", "grenzen"],
            ]), "Wie zonder legende leest, raadt maar wat. Kijk er dus altijd eerst naar."),
        ]),
        dict(kop="De schaal", blokken=[
            ("p", "Een kaart is altijd kleiner dan de werkelijkheid. De schaal zegt hoeveel kleiner."),
            ("fig", svg.schaalbalk(340), "Meet je 3 cm op deze kaart, dan is dat 3 km in het echt."),
            ("p", "Hoe <em>kleiner</em> het gebied dat je toont, hoe <em>meer</em> detail er op past. Op een kaart van je gemeente zie je de straten; op een kaart van Europa alleen nog de grote steden."),
        ]),
        dict(kop="Coördinaten", blokken=[
            ("p", "Een raster met letters en cijfers helpt je iets snel terugvinden. Je zegt eerst de letter, dan het cijfer."),
            ("fig", svg.rasterkaart(400), "De kerk staat in vak C3, het station in D4 en de rivier loopt door A2 en B2."),
            ("p", "Op een wereldkaart doen <strong>lengte- en breedtegraden</strong> hetzelfde werk, maar dan voor de hele aarde. De evenaar is breedtegraad 0."),
        ]),
        dict(kop="Soorten kaarten", blokken=[
            ("fig", tabel(["Soort kaart", "Waarvoor je ze gebruikt"], [
                ["wegenkaart", "van A naar B geraken"],
                ["reliëfkaart", "zien waar het hoog en laag ligt"],
                ["politieke kaart", "landen, provincies en grenzen"],
                ["weerkaart", "zien wat voor weer er komt"],
                ["plattegrond", "één gebouw of één stad van heel dichtbij"],
            ]), None),
            ("p", "Welke kaart je nodig hebt, hangt dus af van je vraag. Met een weerkaart vind je de weg niet."),
        ]),
    ],
    onthoud=[
        "Het noorden staat op een kaart bijna altijd bovenaan.",
        "Nooit Ooit Zal ik Weggaan: N, O, Z, W.",
        "Lees altijd eerst de legende.",
        "De schaal zegt hoeveel kleiner de kaart is dan het echt.",
        "Coördinaten: eerst de letter, dan het cijfer.",
        "Blauw is water, groen is laag land, bruin is hoog land.",
    ])

BUNDELS["tijd-en-tijdlijn"] = dict(
    vak="Geschiedenis", titel="Tijd en tijdlijn",
    onder="Hoe we de tijd indelen, hoe je een tijdlijn leest en hoe je een bron beoordeelt.",
    secties=[
        dict(kop="De grote lijn", blokken=[
            ("p", "Historici delen het verleden op in periodes. Die grenzen zijn door mensen gekozen, dus ze liggen niet overal precies gelijk — maar de volgorde staat vast."),
            ("fig", svg.tijdlijn(
                [("prehistorie", -3000, -800, "#8d8d8d"),
                 ("oudheid", -800, 500, "#2f5d50"),
                 ("middeleeuwen", 500, 1500, "#c17f2b"),
                 ("nieuwe tijd", 1500, 1800, "#3b6ea5"),
                 ("nieuwste tijd", 1800, 2030, "#7a5230")],
                [(0, "jaar 1", "boven"), (476, "val van Rome", "onder"),
                 (1492, "Columbus", "boven"), (1830, "België", "onder")],
                470),
                "De prehistorie duurde vele duizenden jaren langer dan hier past; alles links van de oudheid is dus sterk ingekort."),
            ("p", "De grens tussen prehistorie en geschiedenis is het <strong>schrift</strong>. Vanaf het moment dat mensen dingen opschreven, hebben we geschreven bronnen."),
            ("p", "Zo'n periode heet ook een <strong>tijdvak</strong>: een stuk tijd met eigen kenmerken, niet een vast aantal jaren. Het ene tijdvak duurt duizenden jaren, het andere een paar eeuwen. De <strong>oudheid</strong> bijvoorbeeld is het tijdvak van beschavingen zoals Egypte, Griekenland en Rome."),
        ]),
        dict(kop="Eeuwen tellen", blokken=[
            ("p", "Een eeuw is 100 jaar, een millennium 1 000 jaar en een decennium 10 jaar. Het lastige zit in het tellen van de eeuwen."),
            ("fig", svg.eeuwenbalk(470), "Je telt de eeuw altijd één hoger dan de eerste twee cijfers: 1302 ligt in de 14de eeuw, niet in de 13de."),
            ("weetje", "Er bestaat geen jaar 0: na 1 v.Chr. komt meteen 1 na Chr. Daarom moet je bij een berekening over het begin van de jaartelling altijd één jaar aftrekken."),
        ]),
        dict(kop="Woorden voor een stuk tijd", blokken=[
            ("p", "Voor een stuk tijd bestaan er vaste woorden. Ze zeggen alle vijf iets anders, dus het loont om ze uit elkaar te houden."),
            ("fig", tabel(["Woord", "Hoe lang", "Handig om te weten"], [
                ["decennium", "10 jaar", "tien decennia maken een eeuw"],
                ["generatie", "ongeveer 25 tot 30 jaar", "de tijd tussen ouders en hun kinderen"],
                ["halve eeuw", "50 jaar", "de helft van honderd"],
                ["eeuw", "100 jaar", "tien eeuwen maken een millennium"],
                ["millennium", "1 000 jaar", "duizend jaar, dus tien eeuwen"],
            ]), "Een kwart eeuw is 25 jaar, een kwart van honderd."),
            ("p", "Een <strong>generatie</strong> is geen afgesproken getal maar een schatting: de tijd die er gemiddeld tussen ouders en hun kinderen zit. Reken met 25 tot 30 jaar. In één eeuw passen er dus ongeveer drie à vier."),
        ]),
        dict(kop="Voor en na Christus", blokken=[
            ("p", "Onze jaartelling begint bij het jaar 1. Alles daarvoor krijgt <strong>v.Chr.</strong>, en die jaartallen tellen <em>af</em>: 500 v.Chr. ligt later dan 1000 v.Chr."),
            ("fig", svg.getallenlijn(470, -1000, 1000, [
                (-1000, "1000 v.Chr.", svg.INK, False),
                (-500, "500 v.Chr.", svg.DIM, False),
                (0, "begin", svg.AMBER, True),
                (500, "500", svg.DIM, False),
                (1000, "1000", svg.INK, False)]),
                "Hoe verder naar links, hoe langer geleden."),
        ]),
        dict(kop="Bronnen", blokken=[
            ("p", "Alles wat we over vroeger weten, komt uit bronnen. Niet elke bron is even betrouwbaar."),
            ("fig", tabel(["Soort bron", "Wat het is", "Voorbeeld"], [
                ["primair", "gemaakt in de tijd zelf", "een dagboek, een munt, een gebouw"],
                ["secundair", "later gemaakt, over die tijd", "een geschiedenisboek, een documentaire"],
                ["geschreven", "met woorden", "een brief, een kroniek"],
                ["ongeschreven", "zonder woorden", "een pot, een wapen, een schilderij"],
                ["mondeling", "doorverteld", "een verhaal van je overgrootmoeder"],
            ]), "Een primaire bron staat het dichtst bij wat er gebeurde, maar is daarom nog niet eerlijk."),
        ]),
        dict(kop="Een bron beoordelen", blokken=[
            ("p", "Historici stellen bij elke bron dezelfde vragen. Doe dat ook zelf, ook bij wat je vandaag online leest."),
            ("fig", svg.stappen(["Wie|maakte deze bron?", "Wanneer|was dat?", "Waarom|maakte die het?", "Klopt het|met andere bronnen?"]),
             "Wie er belang bij had, vertelt het verhaal zelden helemaal neutraal."),
            ("p", "Spreken twee bronnen elkaar tegen, dan is de vraag niet welke je het liefst gelooft, maar wie er wat bij te winnen had."),
            ("weetje", "Let ook op <strong>anachronismen</strong>: iets dat in een verhaal of een film opduikt terwijl het in die tijd nog niet bestond. Een ridder die op zijn horloge kijkt, of een Romein die een aardappel eet. Het is meteen een teken dat de maker het niet zo nauw nam."),
        ]),
        dict(kop="Wat historici en archeologen doen", blokken=[
            ("p", "Een <strong>historicus</strong> onderzoekt bronnen, vooral geschreven. Een <strong>archeoloog</strong> graaft op en onderzoekt wat er in de grond zit: potten, botten, muren, gereedschap."),
            ("p", "Voor de prehistorie is de archeoloog de enige getuige die we hebben, want geschreven bronnen zijn er niet."),
        ]),
    ],
    onthoud=[
        "Prehistorie, oudheid, middeleeuwen, nieuwe tijd, nieuwste tijd.",
        "De grens tussen prehistorie en geschiedenis is het schrift.",
        "Tel de eeuw één hoger dan de eerste twee cijfers: 1302 is de 14de eeuw.",
        "Er bestaat geen jaar 0.",
        "Voor Christus tellen de jaartallen af.",
        "Decennium 10 jaar, generatie ongeveer 25 tot 30 jaar, eeuw 100 jaar, millennium 1 000 jaar.",
        "Een tijdvak is een periode met eigen kenmerken, geen vast aantal jaren.",
        "Vraag bij elke bron: wie, wanneer en waarom?",
        "Een anachronisme is iets dat in die tijd nog niet bestond.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
