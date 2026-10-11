# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij wiskunde ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof, alleen met moeilijkere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere getallen en andere situaties dan die van
het hoofdstuk op het scherm. Wie hier iets bijschrijft, legt het eerst naast
`../../spark/wiskunde.json` en `../../spark/wiskunde-meetkunde-metend.json`.

Breuken schrijf je met `bundel.breuk(teller, noemer)`, nooit met een schuine
streep. Een los kleiner-dan teken schrijf je als `&lt;`, want in een antwoord
wordt html niet ontsnapt.

De bestandsnaam eindigt op `-spark`, zodat Beheer → Leerstof enkel in de
hoofdstukken van ✨ Spark zoekt: anders belandt "Meetkunde" bij het
gelijknamige hoofdstuk van 🌱 Start.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel, oefenbundel

SPARK = "✨ Spark — 1ste en 2de middelbaar"

W = "80px"
WW = "150px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Zet je berekening ernaast of eronder: bij een fout antwoord zie je dan waar het misliep.",
    "Reken zonder rekenmachine, tenzij er bij de opdracht iets anders staat.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-negatieve-getallen-en-procenten-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Negatieve getallen en procenten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Optellen en aftrekken",
             opdracht="Let op het verschil tussen het minteken van de bewerking en dat van het getal.",
             oefeningen=[
                 ("rij", [(r"\(-8 + 3\)", r"\(-5\)"), (r"\(6 - 11\)", r"\(-5\)"),
                          (r"\(-7 - 5\)", r"\(-12\)"), (r"\(-9 + 9\)", r"\(0\)")],
                  "Bereken."),
                 ("rij", [(r"\(-5 - (-8)\)", r"\(3\)"), (r"\(7 - (-4)\)", r"\(11\)"),
                          (r"\(-3 + (-6)\)", r"\(-9\)"), (r"\(2 - (-2)\)", r"\(4\)")],
                  "Werk eerst de haakjes weg."),
                 ("kort", r"Het is 's nachts \(-6^{\circ}\text{C}\). Overdag stijgt het \(11\) graden. Hoe warm is het dan?",
                  r"\(5^{\circ}\text{C}\)", W),
                 ("kort", r"Een duiker zit op \(-18\) m en daalt nog \(7\) m. Waar zit hij nu?",
                  r"\(-25\) m", W),
             ]),

        dict(kop="Vermenigvuldigen, delen en machten",
             opdracht="Tel eerst de mintekens, bepaal dan het teken van je antwoord.",
             oefeningen=[
                 ("rij", [(r"\(-4 \cdot 5\)", r"\(-20\)"), (r"\(-9 \cdot -3\)", r"\(27\)"),
                          (r"\(-36 : 4\)", r"\(-9\)"), (r"\(-36 : (-4)\)", r"\(9\)")],
                  "Bereken."),
                 ("rij", [(r"\((-3)^{2}\)", r"\(9\)"), (r"\((-3)^{3}\)", r"\(-27\)"),
                          (r"\((-1)^{5}\)", r"\(-1\)"), (r"\((-2)^{4}\)", r"\(16\)")],
                  "Bereken."),
                 ("kort", r"Bereken \(-2 \cdot (5 - 9)\).", r"\(8\)", W),
                 ("waar", "Twee negatieve getallen vermenigvuldigen geeft altijd een negatief getal.",
                  False),
                 ("open", "Leg uit hoe je aan het teken van een macht ziet of het antwoord "
                          "positief of negatief wordt.",
                  "Bij een negatief grondtal beslist de exponent: is die even, dan vallen de "
                  "mintekens twee aan twee weg en is het antwoord positief. Is de exponent "
                  "oneven, dan blijft er één minteken over.", 4),
             ]),

        dict(kop="Rekenen met procenten",
             opdracht="Denk eraan: 'van' betekent vermenigvuldigen.",
             oefeningen=[
                 ("rij", [(r"\(15\,\%\) van \(60\)", r"\(9\)"), (r"\(40\,\%\) van \(250\)", r"\(100\)"),
                          (r"\(12{,}5\,\%\) van \(80\)", r"\(10\)"), (r"\(75\,\%\) van \(48\)", r"\(36\)")],
                  "Bereken."),
                 ("tabel", ["breuk", "kommagetal", "procent"],
                  [[bundel.breuk(1, 4), None, None], [bundel.breuk(5, 8), None, None],
                   [bundel.breuk(3, 5), None, None]],
                  bundel.breuk(1, 4) + r" \(= 0{,}25 = 25\,\%\) · " + bundel.breuk(5, 8) +
                  r" \(= 0{,}625 = 62{,}5\,\%\) · " + bundel.breuk(3, 5) + r" \(= 0{,}6 = 60\,\%\)"),
                 ("kort", r"In een klas van \(40\) leerlingen dragen er \(14\) een bril. Hoeveel procent?",
                  r"\(35\,\%\)", W),
                 ("waar", r"\(30\,\%\) van \(50\) geeft hetzelfde als \(50\,\%\) van \(30\).", True),
             ]),

        dict(kop="Korting en stijging",
             opdracht="Reken een percentage altijd op de prijs vóór de verandering.",
             oefeningen=[
                 ("kort", r"Een jas van € \(80\) krijgt \(15\,\%\) korting. Wat betaal je?", r"€ \(68\)", W),
                 ("kort", r"Een fiets kost € \(180\). De prijs zakt met \(35\,\%\). Wat betaal je?",
                  r"€ \(117\)", W),
                 ("kort", r"Een spel kost € \(90\) na \(25\,\%\) korting. Wat was de oude prijs?",
                  r"€ \(120\)", W),
                 ("kort", r"Van \(60\) naar \(75\) gaan: hoeveel procent stijging is dat?", r"\(25\,\%\)", W),
                 ("kort", r"\(45\,\%\) van een klas zijn meisjes, dat zijn er \(18\). Hoeveel leerlingen "
                          "telt de klas?", r"\(40\)", W),
                 ("open", r"Een trui van € \(50\) gaat eerst \(20\,\%\) omhoog en daarna weer \(20\,\%\) omlaag. "
                          r"Bereken de eindprijs en leg uit waarom dat geen € \(50\) is.",
                  r"€ \(48\). De stijging rekent op \(50\) (+ € \(10\) → € \(60\)), de daling op \(60\) (&minus; € \(12\) → "
                  r"€ \(48\)). Een percentage rekent altijd op het bedrag van dat moment, en dat is "
                  "de tweede keer groter.", 5),
                 ("waar", r"Een korting van \(25\,\%\) geeft hetzelfde als vermenigvuldigen met \(0{,}75\).",
                  True),
                 ("open", r"De ene winkel geeft \(30\,\%\) korting op een jas van € \(90\), de andere geeft "
                          r"€ \(25\) korting op dezelfde jas. Waar betaal je het minst, en hoeveel?",
                  r"\(30\,\%\) van \(90\) is € \(27\), dus daar betaal je € \(63\). Bij de andere betaal je € \(65\). "
                  r"De eerste winkel is € \(2\) goedkoper.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-getallenleer-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Getallenleer",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Soorten getallen",
             opdracht=r"Natuurlijk \((\mathbb{N})\), geheel \((\mathbb{Z})\) of rationaal \((\mathbb{Q})\)? Geef de kleinste die past.",
             oefeningen=[
                 ("rij", [(r"\(12\)", "ℕ"), (r"\(-7\)", "ℤ"), (bundel.breuk(2, 5), "ℚ"),
                          (r"\(0\)", "ℕ")],
                  "In welke getallenverzameling hoort dit het eerst thuis?", WW),
                 ("waar", "Elk geheel getal is ook een rationaal getal.", True),
                 ("open", "Wat voegen de gehele getallen toe aan de natuurlijke getallen, en wat "
                          "voegen de rationale daar nog aan toe?",
                  "De gehele getallen voegen de negatieve getallen toe. De rationale getallen "
                  "voegen daar alle breuken aan toe, dus alles wat je als een deling van twee "
                  "gehele getallen kan schrijven.", 4),
             ]),

        dict(kop="Breuken benoemen",
             opdracht="Gebruik de juiste naam, niet 'het bovenste getal'.",
             oefeningen=[
                 ("rij", [("het onderste getal", "de noemer"), ("het bovenste getal", "de teller"),
                          (r"een breuk met teller \(1\)", "een stambreuk")],
                  "Hoe heet dit?", WW),
                 ("rij", [(r"het tegengestelde van \(-9\)", r"\(9\)"),
                          ("het omgekeerde van " + bundel.breuk(3, 5), bundel.breuk(5, 3)),
                          (r"de absolute waarde van \(-11\)", r"\(11\)")],
                  "Geef het gevraagde getal.", WW),
                 ("open", "Wanneer noem je twee breuken gelijknamig, en waarom wil je dat?",
                  "Als ze dezelfde noemer hebben. Pas dan tellen de tellers over hetzelfde soort "
                  "stukken en kan je optellen of aftrekken.", 3),
                 ("open", "Wanneer noem je een breuk onvereenvoudigbaar?",
                  r"Als teller en noemer geen gemeenschappelijke deler meer hebben behalve \(1\). "
                  "Je kan er dus niets meer uit wegdelen.", 3),
             ]),

        dict(kop="Delers, veelvouden en priemgetallen",
             opdracht="Schrijf je ontbinding ernaast als dat helpt.",
             oefeningen=[
                 ("rij", [(r"ggd van \(18\) en \(24\)", r"\(6\)"), (r"kgv van \(6\) en \(8\)", r"\(24\)"),
                          (r"ggd van \(30\) en \(45\)", r"\(15\)"), (r"kgv van \(9\) en \(12\)", r"\(36\)")],
                  "Bereken."),
                 ("rij", [(r"\(21\)", "geen"), (r"\(29\)", "priem"), (r"\(51\)", "geen"), (r"\(37\)", "priem")],
                  "Priemgetal of niet? Schrijf 'priem' of 'geen'.", WW),
                 ("open", "Waarvoor gebruik je het kgv als je met breuken werkt?",
                  "Om twee breuken gelijknamig te maken: het kgv van de noemers is de kleinste "
                  "gemeenschappelijke noemer, dus daarmee blijven de getallen het kleinst.", 3),
                 ("waar", r"\(2\) is het enige even priemgetal.", True),
             ]),

        dict(kop="Machten, wortels en volgorde",
             opdracht="Denk aan de rekenvolgorde: eerst haakjes, dan machten, dan · en :, dan + en &minus;.",
             oefeningen=[
                 ("rij", [(r"\(3^{2} \cdot 3^{3}\)", r"\(3^{5} = 243\)"), (r"\((5^{2})^{3}\)", r"\(5^{6}\)"),
                          (r"\(3^{-2}\)", bundel.breuk(1, 9)), (r"\(2^{0}\)", r"\(1\)")],
                  "Bereken of vereenvoudig.", WW),
                 ("rij", [(r"\(\sqrt{81}\)", r"\(9\)"), (r"\(\sqrt{144}\)", r"\(12\)"), (r"\(\sqrt{1}\)", r"\(1\)")], "Bereken."),
                 ("rij", [(r"\(5 + 2 \cdot 6\)", r"\(17\)"), (r"\((5 + 2) \cdot 6\)", r"\(42\)"),
                          (r"\(20 - 3^{2}\)", r"\(11\)"), (r"\(2 \cdot 3 + 4 \cdot 5\)", r"\(26\)")],
                  "Bereken."),
                 ("kort", r"Wat is de rest bij de deling \(29 : 4\)?", r"\(1\)", W),
             ]),

        dict(kop="Afronden, schaal en evenredigheid",
             opdracht="Schrijf je tussenstap op.",
             oefeningen=[
                 ("rij", [(r"\(5{,}6749\) op twee decimalen", r"\(5{,}67\)"), (r"\(12{,}395\) op twee decimalen", r"\(12{,}40\)"),
                          (r"\(0{,}0648\) op drie decimalen", r"\(0{,}065\)")],
                  "Rond af.", WW),
                 ("kort", r"Op een plan met schaal \(1 : 100\) meet een muur \(4{,}5\) cm. Hoe lang is die "
                          "muur in het echt?", r"\(4{,}5\) m", W),
                 ("kort", r"Drie broden kosten € \(4{,}50\). Wat kosten er zeven?", r"€ \(10{,}50\)", W),
                 ("kort", "Hoeveel procent is " + bundel.breuk(7, 8) + "?", r"\(87{,}5\,\%\)", W),
                 ("waar", r"\(-3\) is groter dan \(-5\).", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-probleemoplossend-denken-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Probleemoplossend denken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eerst begrijpen, dan rekenen",
             opdracht="Lees elke opgave twee keer voor je begint te rekenen.",
             oefeningen=[
                 ("open", "Je leest een vraagstuk en je snapt niet wat er gevraagd wordt. "
                          "Noem twee dingen die je dan het best eerst doet.",
                  "De vraag nog eens lezen en onderstrepen wat er precies gevraagd wordt, de "
                  "gegevens in een tabel of een tekening zetten, en schatten wat een redelijk "
                  "antwoord zou zijn.", 4),
                 ("open", r"Je rekent uit dat een schoolbus \(4{,}3\) kinderen vervoert. Wat doe je?",
                  "Je controleert je berekening: een aantal kinderen kan geen kommagetal zijn. "
                  "Klopt de berekening toch, dan rond je af naar wat in de situatie past en zeg "
                  "je erbij waarom.", 4),
                 ("waar", "Schatten voor je rekent, is tijdverlies.", False),
                 ("open", "Wat is de laatste stap bij het oplossen van een vraagstuk?",
                  "Terugkijken: klopt het antwoord met de vraag die gesteld werd, en is het een "
                  "redelijk getal in deze situatie? Pas dan schrijf je je zin.", 3),
             ]),

        dict(kop="Vraagstukken met één stap te veel",
             opdracht="Zet je tussenstappen eronder.",
             oefeningen=[
                 ("kort", r"Een fles water kost € \(1{,}35\). Wat kosten er negen?", r"€ \(12{,}15\)", W),
                 ("kort", r"In een klas van \(28\) is een vierde afwezig. Hoeveel zijn er aanwezig?",
                  r"\(21\)", W),
                 ("kort", r"Een tuin is \(15\) m op \(9\) m. Hoeveel meter hek heb je nodig?", r"\(48\) m", W),
                 ("kort", r"Een trein vertrekt om \(8\).\(50\) u en rijdt \(3\) u \(25\) min. Hoe laat komt hij aan?",
                  r"\(12\).\(15\) u", W),
                 ("kort", r"Een pak van \(400\) g koekjes kost € \(2{,}60\). Wat kost een kilo?", r"€ \(6{,}50\)", W),
                 ("kort", r"Je koopt vijf broodjes van € \(2{,}80\) en betaalt met € \(20\). Hoeveel krijg "
                          "je terug?", r"€ \(6\)", W),
                 ("kort", r"Een fietser rijdt \(18\) km per uur. Hoe lang doet hij over \(45\) km?",
                  r"\(2\) u \(30\) min", W),
                 ("kort", r"Een recept voor \(4\) personen vraagt \(320\) g rijst. Hoeveel voor \(6\) personen?",
                  r"\(480\) g", W),
             ]),

        dict(kop="Terugrekenen en tellen",
             opdracht="Werk van achter naar voor, of maak een tekening.",
             oefeningen=[
                 ("open", r"Ik denk aan een getal, trek er \(5\) van af en vermenigvuldig het "
                          r"resultaat met \(4\). Ik krijg \(28\). Aan welk getal dacht ik?",
                  r"\(12\). Terugrekenen: \(28 : 4 = 7\), en \(7 + 5 = 12\).", 3),
                 ("open", r"Een kaars van \(24\) cm brandt \(3\) cm per uur op. Na hoeveel uur is ze nog "
                          r"\(6\) cm lang?",
                  r"\(6\) uur. Er moet \(24 - 6 = 18\) cm opbranden, en \(18 : 3 = 6\).", 3),
                 ("open", "Vier vrienden zitten aan een tafel. Ieder geeft ieder ander één keer "
                          "een hand. Hoeveel handdrukken zijn er?",
                  r"\(6\). Elk van de \(4\) geeft \(3\) handen, dat is \(12\), maar elke handdruk telde je twee "
                  r"keer: \(12 : 2 = 6\).", 4),
                 ("open", r"Een tuin van \(24\) m lang krijgt om de \(4\) meter een paal, ook aan het "
                          "begin en aan het einde. Hoeveel palen zijn er?",
                  r"\(7\). Er zijn \(24 : 4 = 6\) tussenstukken, en bij een rij met twee uiteinden staat "
                  "er altijd één paal meer dan er tussenstukken zijn.", 4),
                 ("open", r"Op een parking staan auto's en motors: samen \(18\) voertuigen en "
                          r"\(62\) wielen. Hoeveel motors staan er?",
                  r"\(5\) motors (en \(13\) auto's). Stel dat het allemaal auto's waren: \(18 \cdot 4 = 72\) "
                  r"wielen, dat zijn er \(10\) te veel. Elke motor scheelt \(2\) wielen, dus \(10 : 2 = 5\).", 5),
             ]),

        dict(kop="Rijen en patronen",
             opdracht="Zoek eerst de regel, schrijf die op, en gebruik ze dan.",
             oefeningen=[
                 ("rij", [(r"\(3\), \(6\), \(12\), \(24\), …", r"\(48\)"), (r"\(1\), \(4\), \(9\), \(16\), …", r"\(25\)"),
                          (r"\(2\), \(5\), \(10\), \(17\), …", r"\(26\)"), (r"\(100\), \(91\), \(82\), \(73\), …", r"\(64\)")],
                  "Welk getal komt er daarna?", WW),
                 ("open", r"Een som van drie opeenvolgende getallen is \(57\). Wat is het kleinste?",
                  r"\(18\). Het middelste getal is \(57 : 3 = 19\), dus de drie zijn \(18\), \(19\) en \(20\).", 3),
                 ("open", r"Het is nu \(15\).\(00\) u. Hoe laat is het over \(100\) uur?",
                  r"\(19\).\(00\) u. \(100 : 24 = 4\) dagen en \(4\) uur over, dus \(15\).\(00\) u \(+ 4\) uur.", 3),
                 ("open", r"Je verdeelt \(100\) snoepjes eerlijk over een aantal kinderen en er "
                          r"blijven er \(4\) over. Hoeveel kinderen kunnen er zijn?",
                  r"Een deler van \(96\) die groter is dan \(4\): \(6\), \(8\), \(12\), \(16\), \(24\), \(32\), \(48\) of \(96\). "
                  r"(Groter dan \(4\), anders zou je de rest nog kunnen uitdelen.)", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-redeneringen-en-uitspraken-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Wiskundige redeneringen en uitspraken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Weerleggen met één geval",
             opdracht="Eén tegenvoorbeeld volstaat. Schrijf het getal of de figuur op.",
             oefeningen=[
                 ("rij", [("alle priemgetallen zijn oneven", r"\(2\)"),
                          ("het kwadraat van een getal is groter dan het getal zelf", r"\(1\) (of \(0\))"),
                          (r"elk getal deelbaar door \(3\) is deelbaar door \(6\)", r"\(9\)"),
                          ("elke vierhoek met vier gelijke zijden is een vierkant", "een ruit")],
                  "Geef één tegenvoorbeeld.", WW),
                 ("kort", "Hoe noem je één geval waarmee je een uitspraak onderuithaalt?",
                  "een tegenvoorbeeld", WW),
                 ("waar", "Als je tien voorbeelden vindt waarin een uitspraak klopt, is ze "
                          "bewezen.", False),
                 ("open", "Leg het verschil uit tussen een voorbeeld en een bewijs.",
                  "Een voorbeeld toont dat het in één geval klopt. Een bewijs toont dat het in "
                  "álle gevallen klopt, door met letters te redeneren in plaats van met getallen.", 4),
             ]),

        dict(kop="Pijlen: ⇒ of ⇔",
             opdracht="Vraag je bij elke uitspraak ook af of de omgekeerde klopt.",
             oefeningen=[
                 ("rij", [(r"een getal is deelbaar door \(6\) … het is deelbaar door \(3\)", "⇒"),
                          ("een vierhoek is een vierkant … hij heeft vier rechte hoeken", "⇒"),
                          (r"een getal is even … het eindigt op \(0\), \(2\), \(4\), \(6\) of \(8\)", "⇔"),
                          (r"een getal is groter dan \(10\) … het is groter dan \(5\)", "⇒")],
                  "Welke pijl hoort hier: ⇒ of ⇔?", WW),
                 ("open", r"Waarom staat er bij 'deelbaar door \(6\) ⇒ deelbaar door \(3\)' geen dubbele "
                          "pijl?",
                  r"Omdat de omgekeerde uitspraak niet klopt: \(9\) is deelbaar door \(3\) maar niet door "
                  r"\(6\). Een dubbele pijl mag pas als het in allebei de richtingen geldt.", 4),
                 ("waar", "Een vierkant is altijd een rechthoek.", True),
                 ("waar", "Een rechthoek is altijd een vierkant.", False),
             ]),

        dict(kop="Waar zit de fout?",
             opdracht="Schrijf niet enkel 'fout', maar zeg in welke stap het misging.",
             oefeningen=[
                 ("open", r"Iemand redeneert: „\(7 > 4\), dus \(-7 > -4\).” Waar zit de fout?",
                  r"Bij het vermenigvuldigen met \(-1\) draait een ongelijkheid om. Het moet "
                  r"\(-7 < -4\) zijn.", 3),
                 ("open", r"Iemand schrijft: „\(24 : 6 : 2 = 24 : 3 = 8\)”. Wat ging er mis?",
                  r"Delingen werk je van links naar rechts af: \(24 : 6 = 4\), en \(4 : 2 = 2\). De "
                  "tweede deling zomaar eerst doen mag niet.", 3),
                 ("open", r"Iemand schrijft: „\(\sqrt{16 + 9} = \sqrt{16} + \sqrt{9} = 4 + 3 = 7\)”. Klopt dat?",
                  r"Nee. \(\sqrt{25} = 5\), niet \(7\). Een wortel mag je niet over een som verdelen.", 3),
                 ("open", r"Iemand zegt: „\(20\,\%\) korting en daarna nog eens \(20\,\%\) korting is samen "
                          r"\(40\,\%\) korting.” Wat is er mis?",
                  r"De tweede korting rekent op de al verlaagde prijs. \(0{,}8 \cdot 0{,}8 = 0{,}64\), dus je "
                  r"betaalt \(64\,\%\) en de korting is samen \(36\,\%\), niet \(40\,\%\).", 4),
                 ("open", "Een redenering klopt in elke stap, maar de laatste zin beantwoordt "
                          "een andere vraag dan er gesteld werd. Wat is je oordeel?",
                  "De oefening is fout opgelost. Rekenen dat klopt maar niet de gestelde vraag "
                  "beantwoordt, levert geen antwoord.", 3),
             ]),

        dict(kop="Algemeen redeneren",
             opdracht="Redeneer met letters, niet met voorbeelden.",
             oefeningen=[
                 ("open", "Toon aan dat de som van twee even getallen altijd even is.",
                  r"Elk even getal kan je schrijven als 2a en 2b. Hun som is \(2a + 2b = 2(a + b)\), "
                  r"en dat is een veelvoud van \(2\), dus even.", 4),
                 ("waar", "Het product van twee oneven getallen is altijd even.", False),
                 ("rij", [(r"uit \(a = b\) volgt \(a^{2} = b^{2}\)", "juist"),
                          (r"uit \(a^{2} = b^{2}\) volgt \(a = b\)", "fout"),
                          (r"uit \(a \cdot b = 0\) volgt \(a = 0\)", "fout")],
                  "Juist of fout?", WW),
                 ("open", "Geef bij elk van de twee foute uitspraken hierboven een "
                          "tegenvoorbeeld.",
                  r"\(a^{2} = b^{2}\): neem \(a = 3\) en \(b = -3\). \(a \cdot b = 0\): neem \(a = 5\) en \(b = 0\), dan is "
                  r"het product \(0\) terwijl a niet \(0\) is.", 4),
                 ("open", "Waarom schrijf je tussenstappen op in een berekening?",
                  "Zo kan je (en kan een ander) nakijken waar een fout zit, en hoef je bij een "
                  "vergissing niet alles opnieuw te doen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-meetkunde-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Meetkunde",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoeken herkennen",
             opdracht="Schrijf onder elke hoek of hij scherp, recht, stomp of gestrekt is.",
             oefeningen=[
                 ("fig", [(svg.hoek(35), "scherp"), (svg.hoek(90), "recht"),
                          (svg.hoek(145), "stomp"), (svg.hoek(180), "gestrekt")],
                  "Welke soort hoek is dit?"),
                 ("rij", [(r"de nevenhoek van \(55^{\circ}\)", r"\(125^{\circ}\)"), (r"de overstaande hoek van \(55^{\circ}\)", r"\(55^{\circ}\)"),
                          (r"de complementaire hoek van \(55^{\circ}\)", r"\(35^{\circ}\)")],
                  r"Twee rechten snijden elkaar onder \(55^{\circ}\). Bereken.", WW),
                 ("kort", "Twee evenwijdige rechten worden gesneden door een derde rechte. Eén "
                          r"overeenkomstige hoek is \(72^{\circ}\). Hoe groot is de andere?", r"\(72^{\circ}\)", W),
                 ("waar", "Twee evenwijdige rechten snijden elkaar ver genoeg verderop toch.",
                  False),
             ]),

        dict(kop="Rekenen met hoeken in figuren",
             opdracht=r"De som van de hoeken van een driehoek is \(180^{\circ}\), van een vierhoek \(360^{\circ}\).",
             oefeningen=[
                 ("rij", [(r"een driehoek met \(40^{\circ}\) en \(75^{\circ}\)", r"\(65^{\circ}\)"),
                          (r"een driehoek met \(90^{\circ}\) en \(32^{\circ}\)", r"\(58^{\circ}\)"),
                          (r"een vierhoek met \(100^{\circ}\), \(85^{\circ}\) en \(95^{\circ}\)", r"\(80^{\circ}\)")],
                  "Hoe groot is de ontbrekende hoek?", WW),
                 ("kort", r"In een gelijkbenige driehoek is de tophoek \(50^{\circ}\). Hoe groot is elke "
                          "basishoek?", r"\(65^{\circ}\)", W),
                 ("kort", r"In een gelijkbenige driehoek is een basishoek \(70^{\circ}\). Hoe groot is de "
                          "tophoek?", r"\(40^{\circ}\)", W),
                 ("kort", r"In een parallellogram is één hoek \(115^{\circ}\). Hoe groot is de hoek ernaast?",
                  r"\(65^{\circ}\)", W),
                 ("open", r"Een driehoek heeft hoeken van \(90^{\circ}\) en \(45^{\circ}\). Wat weet je allemaal over "
                          "die driehoek?",
                  r"De derde hoek is ook \(45^{\circ}\), dus de driehoek is rechthoekig én gelijkbenig. De "
                  "twee rechthoekszijden zijn even lang.", 4),
             ]),

        dict(kop="Vormen benoemen",
             opdracht="Schrijf onder elke figuur zijn naam.",
             oefeningen=[
                 ("fig", [(svg.vorm("ruit"), "ruit"), (svg.vorm("trapezium"), "trapezium"),
                          (svg.vorm("zeshoek"), "zeshoek")],
                  "Hoe heet deze figuur?"),
                 ("rij", [("beide paren overstaande zijden evenwijdig", "parallellogram"),
                          ("vier even lange zijden", "ruit"),
                          ("juist één paar evenwijdige zijden", "trapezium"),
                          ("vier gelijke zijden én vier rechte hoeken", "vierkant")],
                  "Welke vierhoek is dit?", WW),
                 ("rij", [("een vierkant", r"\(4\)"), ("een gewone rechthoek", r"\(2\)"),
                          ("een gelijkzijdige driehoek", r"\(3\)"), ("een gewoon parallellogram", r"\(0\)")],
                  "Hoeveel symmetrieassen heeft dit?", WW),
                 ("waar", "De diagonalen van een ruit staan loodrecht op elkaar.", True),
             ]),

        dict(kop="Lijnen in een driehoek",
             opdracht="Gebruik de namen uit de bundel.",
             oefeningen=[
                 ("rij", [("verdeelt een hoek in twee gelijke stukken", "bissectrice"),
                          ("staat loodrecht op een zijde, door het midden ervan", "middelloodlijn"),
                          ("van een hoekpunt loodrecht op de overstaande zijde", "hoogtelijn"),
                          ("van een hoekpunt naar het midden van de overstaande zijde", "zwaartelijn")],
                  "Welke merkwaardige lijn is dit?", WW),
                 ("kort", "Hoe noem je de langste zijde van een rechthoekige driehoek?",
                  "de schuine zijde (hypotenusa)", WW),
                 ("teken", "Teken een driehoek en construeer met je geodriehoek de hoogtelijn "
                           "uit één hoekpunt.",
                  "De lijn vertrekt uit het hoekpunt en staat loodrecht op de overstaande zijde "
                  "(of op het verlengde ervan bij een stompe hoek).", 45),
             ]),

        dict(kop="Congruentie en transformaties",
             opdracht="Let goed op het verschil tussen dezelfde vorm en dezelfde grootte.",
             oefeningen=[
                 ("rij", [("drie paar even lange zijden", "ZZZ"),
                          ("twee zijden en de ingesloten hoek", "ZHZ"),
                          ("een zijde en de twee aanliggende hoeken", "HZH")],
                  "Welk congruentiekenmerk is dit?", WW),
                 ("waar", "Twee driehoeken met drie gelijke hoeken zijn altijd congruent.", False),
                 ("rij", [("schuift opzij zonder te draaien", "translatie"),
                          ("draait een kwartslag rond een punt", "rotatie"),
                          ("klapt om rond een rechte", "spiegeling")],
                  "Welke transformatie is dit?", WW),
                 ("open", "Wat mag je besluiten zodra je aantoont dat twee driehoeken congruent "
                          "zijn?",
                  "Dat al hun overeenkomstige zijden even lang zijn en al hun overeenkomstige "
                  "hoeken even groot. Je hoeft die dus niet één voor één meer te meten.", 4),
                 ("open", "Welke eigenschap blijft bij een spiegeling om een rechte niet "
                          "noodzakelijk behouden?",
                  "De draaizin: wat met de klok mee stond, staat erna tegen de klok in. Lengtes, "
                  "hoeken en oppervlakte blijven wel gelijk.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-metend-rekenen-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Metend rekenen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eenheden omzetten",
             opdracht=r"Zet de maatladder eronder als dat helpt. Let op: bij \(\text{m}^{2}\) spring je per twee, bij \(\text{m}^{3}\) per drie.",
             oefeningen=[
                 ("rij", [(r"\(4{,}2\) km in m", r"\(4\,200\) m"), (r"\(75\) cm in m", r"\(0{,}75\) m"),
                          (r"\(3{,}4\) kg in g", r"\(3\,400\) g"), (r"\(250\) ml in l", r"\(0{,}25\) l")],
                  "Zet om."),
                 ("rij", [(r"\(4\,\text{m}^{2}\) in \(\text{dm}^{2}\)", r"\(400\,\text{dm}^{2}\)"), (r"\(3\,\text{m}^{2}\) in \(\text{cm}^{2}\)", r"\(30\,000\,\text{cm}^{2}\)"),
                          (r"\(2\,\text{m}^{3}\) in l", r"\(2\,000\) l"), (r"\(5\,000\,\text{cm}^{3}\) in \(\text{dm}^{3}\)", r"\(5\,\text{dm}^{3}\)")],
                  "Zet om.", WW),
                 ("rij", [(r"\(3{,}5\) uur in minuten", r"\(210\) min"), ("een half uur in seconden", r"\(1\,800\) s"),
                          (r"\(135\) minuten in uren en minuten", r"\(2\) u \(15\) min")],
                  "Zet om.", WW),
                 ("waar", r"\(1\) liter is hetzelfde als \(1\,\text{dm}^{3}\).", True),
             ]),

        dict(kop="Omtrek en oppervlakte",
             opdracht="Schrijf eerst de formule op, vul dan de getallen in.",
             oefeningen=[
                 ("rij", [(r"rechthoek \(9\) cm op \(4\) cm", r"\(26\) cm"), (r"vierkant met zijde \(7\) cm", r"\(28\) cm"),
                          (r"gelijkzijdige driehoek met zijde \(6\) cm", r"\(18\) cm")],
                  "Bereken de omtrek.", WW),
                 ("rij", [(r"rechthoek \(9\) cm op \(4\) cm", r"\(36\,\text{cm}^{2}\)"),
                          (r"driehoek met basis \(10\) cm en hoogte \(6\) cm", r"\(30\,\text{cm}^{2}\)"),
                          (r"parallellogram met basis \(8\) cm en hoogte \(5\) cm", r"\(40\,\text{cm}^{2}\)"),
                          (r"ruit met diagonalen \(10\) cm en \(6\) cm", r"\(30\,\text{cm}^{2}\)")],
                  "Bereken de oppervlakte.", WW),
                 ("kort", r"Een trapezium heeft evenwijdige zijden van \(5\) cm en \(11\) cm en een "
                          r"hoogte van \(6\) cm. Wat is de oppervlakte?", r"\(48\,\text{cm}^{2}\)", W),
                 ("kort", r"Een vierkant heeft een oppervlakte van \(64\,\text{cm}^{2}\). Hoe lang is een zijde?",
                  r"\(8\) cm", W),
                 ("kort", r"Een rechthoek heeft een oppervlakte van \(54\,\text{cm}^{2}\) en een lengte van "
                          r"\(9\) cm. Hoe breed is hij?", r"\(6\) cm", W),
             ]),

        dict(kop="De cirkel",
             opdracht=r"Neem \(\pi = 3{,}14\). Schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"Een cirkel heeft een straal van \(4\) cm. Hoe lang is de omtrek?",
                  r"\(25{,}12\) cm", W),
                 ("kort", "Dezelfde cirkel: hoe groot is de oppervlakte?", r"\(50{,}24\,\text{cm}^{2}\)", W),
                 ("kort", r"Een cirkel heeft een diameter van \(12\) cm. Hoe lang is de omtrek?",
                  r"\(37{,}68\) cm", W),
                 ("open", r"Een figuur bestaat uit een vierkant met zijde \(8\) cm, met daarop een "
                          r"halve cirkel met diameter \(8\) cm. Bereken de totale oppervlakte.",
                  r"Het vierkant is \(64\,\text{cm}^{2}\). De halve cirkel heeft straal \(4\), dus "
                  r"\((3{,}14 \cdot 4 \cdot 4) : 2 = 25{,}12\,\text{cm}^{2}\). Samen \(89{,}12\,\text{cm}^{2}\).", 5),
             ]),

        dict(kop="Ruimtefiguren",
             opdracht=r"Let op het verschil tussen oppervlakte (\(\text{cm}^{2}\)) en volume (\(\text{cm}^{3}\)).",
             oefeningen=[
                 ("fig", [(svg.ruimtefiguur("kubus"), "kubus"), (svg.ruimtefiguur("cilinder"), "cilinder"),
                          (svg.ruimtefiguur("kegel"), "kegel")],
                  "Hoe heet deze ruimtefiguur?"),
                 ("rij", [(r"kubus met ribbe \(5\) cm", r"\(125\,\text{cm}^{3}\)"),
                          (r"balk \(6\) cm op \(4\) cm op \(3\) cm", r"\(72\,\text{cm}^{3}\)"),
                          (r"kubus met ribbe \(2\) dm, in liter", r"\(8\) l")],
                  "Bereken het volume.", WW),
                 ("kort", r"Wat is de totale oppervlakte van een kubus met ribbe \(5\) cm?",
                  r"\(150\,\text{cm}^{2}\)", W),
                 ("kort", r"Een cilinder heeft straal \(2\) cm en hoogte \(10\) cm. Wat is het volume? "
                          r"Neem \(\pi = 3{,}14\).", r"\(125{,}6\,\text{cm}^{3}\)", W),
                 ("kort", r"Een zwembad van \(12\) m op \(5\) m staat \(1{,}5\) m vol. Hoeveel liter is dat?",
                  r"\(90\,000\) l", W),
             ]),

        dict(kop="Denken over maten",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("waar", "Twee rechthoeken met dezelfde omtrek hebben ook dezelfde oppervlakte.",
                  False),
                 ("open", "Je verdubbelt de zijde van een vierkant. Wat gebeurt er met de "
                          "oppervlakte, en waarom?",
                  "Ze wordt vier keer zo groot. De oppervlakte is zijde · zijde, dus je "
                  r"vermenigvuldigt twee keer met \(2\).", 4),
                 ("kort", r"Een tuin is \(25\) m op \(16\) m. Hoeveel are is dat?", r"\(4\) are", W),
                 ("kort", r"Een pad van \(1{,}8\) km leg je af in \(20\) minuten. Hoeveel meter per minuut?",
                  r"\(90\) m/min", W),
                 ("kort", r"Een plan heeft schaal \(1 : 200\). Een muur is \(6\) cm op het plan. Hoe lang "
                          "is hij echt?", r"\(12\) m", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-relaties-en-verandering-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Relaties en verandering",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het assenstelsel",
             opdracht="De eerste coördinaat hoort bij de x-as.",
             oefeningen=[
                 ("kort", "Welke coördinaten heeft de oorsprong?", r"\((0, 0)\)", W),
                 ("kort", "Een punt ligt op de x-as. Wat weet je over zijn y-coördinaat?",
                  r"die is \(0\)", W),
                 ("teken", r"Teken een assenstelsel en zet deze punten erop: \(A(2, 3)\), \(B(-1, 4)\), "
                           r"\(C(0, -2)\) en \(D(3, 0)\).",
                  r"\(A\) rechtsboven, \(B\) linksboven, \(C\) op de y-as onder de oorsprong, \(D\) op de x-as "
                  "rechts van de oorsprong.", 55),
             ]),

        dict(kop="Rekenen met letters",
             opdracht="Gelijksoortige termen mag je samennemen, andere niet.",
             oefeningen=[
                 ("rij", [(r"3x als \(x = 7\)", r"\(21\)"), (r"\(2a + 5\) als \(a = 9\)", r"\(23\)"),
                          (r"\(x^{2} - 3x\) als \(x = 6\)", r"\(18\)"), (r"\(2a - b\) als \(a = 4\) en \(b = -5\)", r"\(13\)")],
                  "Bereken de getalwaarde.", WW),
                 ("rij", [(r"\(5a + 2a - 3a\)", "4a"), (r"\(4(x + 3)\)", r"\(4x + 12\)"),
                          (r"\(2(3x - 4) + 5x\)", r"\(11x - 8\)"), (r"\(7b - b\)", "6b")],
                  "Herleid of werk de haakjes weg.", WW),
                 ("rij", [(r"\((a + b)^{2}\)", r"\(a^{2} + 2ab + b^{2}\)"), (r"\((a - b)^{2}\)", r"\(a^{2} - 2ab + b^{2}\)"),
                          (r"\((a + b)(a - b)\)", r"\(a^{2} - b^{2}\)"), (r"\((x + 5)^{2}\)", r"\(x^{2} + 10x + 25\)")],
                  "Werk uit.", "230px"),
                 ("kort", r"Wat is de graad van de veelterm \(4x^{3} + 2x - 9\)?", r"\(3\)", W),
                 ("kort", "In de eenterm 7x^{4}, welk getal is de coëfficiënt?", r"\(7\)", W),
             ]),

        dict(kop="Vergelijkingen oplossen",
             opdracht="Doe links en rechts altijd hetzelfde. Schrijf elke stap op.",
             oefeningen=[
                 ("rij", [(r"\(x + 9 = 15\)", r"\(x = 6\)"), (r"\(4x = 28\)", r"\(x = 7\)"),
                          (r"\(3x + 4 = 19\)", r"\(x = 5\)"), (r"\(x - 6 = -11\)", r"\(x = -5\)")],
                  "Los op.", WW),
                 ("rij", [(r"\(6x - 5 = 3x + 7\)", r"\(x = 4\)"), (r"\(2(x - 3) = 14\)", r"\(x = 10\)"),
                          (r"\(x : 5 = 4\)", r"\(x = 20\)"), (r"\(5 - x = 12\)", r"\(x = -7\)")],
                  "Los op.", WW),
                 ("open", r"Bij \(6x = 30\) deelt iemand enkel links door \(6\) en schrijft \(x = 30\). "
                          "Wat is er mis?",
                  "Wat je links doet, moet je ook rechts doen. Anders klopt de gelijkheid niet "
                  r"meer. Het juiste antwoord is \(x = 5\).", 3),
             ]),

        dict(kop="Vraagstukken met een vergelijking",
             opdracht="Zeg eerst wat x is, stel dan de vergelijking op, los dan op.",
             oefeningen=[
                 ("open", r"Ik denk aan een getal. Het drievoud ervan min \(4\) is \(26\). Schrijf de "
                          "vergelijking en los ze op.",
                  r"\(3x - 4 = 26\), dus \(3x = 30\) en \(x = 10\).", 4),
                 ("open", r"Een taxi vraagt € \(4\) opstapgeld en € \(1{,}50\) per kilometer. Je betaalt "
                          r"€ \(25\). Hoeveel kilometer reed je?",
                  r"\(4 + 1{,}5k = 25\), dus \(1{,}5k = 21\) en \(k = 14\) km.", 4),
                 ("open", r"De omtrek van een rechthoek is \(34\) cm en de lengte is \(11\) cm. Welke "
                          "vergelijking gebruik je voor de breedte b, en wat is b?",
                  r"\(2 \cdot (11 + b) = 34\), dus \(11 + b = 17\) en \(b = 6\) cm.", 4),
             ]),

        dict(kop="Evenredigheid en rijen",
             opdracht="Recht evenredig: keer zoveel. Omgekeerd evenredig: het product blijft gelijk.",
             oefeningen=[
                 ("tabel", ["aantal broden", "prijs in €"],
                  [[r"\(3\)", r"\(4{,}50\)"], [r"\(5\)", None], [r"\(8\)", None]],
                  r"\(5\) broden kosten € \(7{,}50 \cdot 8\) broden kosten € \(12\)"),
                 ("open", r"Zes werklui doen een klus in \(8\) dagen. Hoe lang doen twaalf werklui "
                          "erover? Leg uit welk soort verband dat is.",
                  r"\(4\) dagen. Dit is omgekeerd evenredig: het product blijft \(48\) manddagen, dus "
                  "dubbel zoveel werklui betekent de helft van de tijd.", 4),
                 ("waar", "De grafiek van een recht evenredig verband is een rechte lijn door "
                          "de oorsprong.", True),
                 ("rij", [(r"\(4\), \(9\), \(14\), \(19\), …", r"\(24\)"), (r"\(3\), \(6\), \(12\), \(24\), …", r"\(48\)"),
                          (r"\(1\), \(3\), \(6\), \(10\), …", r"\(15\)")],
                  "Welk getal komt er daarna?", WW),
                 ("open", r"Met lucifers leg je driehoekjes op een rij: \(1\) driehoek kost \(3\) "
                          r"lucifers, \(2\) kosten er \(5\), \(3\) kosten er \(7\). Hoeveel voor n driehoekjes?",
                  r"\(2n + 1\). De eerste kost \(3\), en elke volgende komt er met \(2\) lucifers bij.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-data-en-onzekerheid-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Data en onzekerheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Soorten gegevens",
             opdracht="Kan je ermee rekenen, of alleen maar tellen?",
             oefeningen=[
                 ("rij", [("het aantal broers en zussen", "numeriek"),
                          ("de lievelingskleur", "categorisch"),
                          ("de lengte in cm", "numeriek"),
                          ("de manier waarop je naar school komt", "categorisch")],
                  "Numeriek of categorisch?", WW),
                 ("kort", "Welke centrummaat kan je gebruiken bij een categorische variabele?",
                  "de modus", W),
                 ("waar", "In een frequentietabel is de som van alle frequenties gelijk aan het "
                          "aantal metingen.", True),
             ]),

        dict(kop="Gemiddelde, modus, mediaan",
             opdracht="Zet de getallen eerst op volgorde als je de mediaan zoekt.",
             oefeningen=[
                 ("rij", [(r"\(3\), \(7\), \(8\)", r"\(6\)"), (r"\(4\), \(6\), \(6\), \(12\)", r"\(7\)"),
                          (r"\(10\), \(10\), \(10\), \(10\)", r"\(10\)")],
                  "Bereken het gemiddelde.", WW),
                 ("rij", [(r"\(2\), \(9\), \(9\), \(11\), \(14\)", r"\(9\)"), (r"\(5\), \(3\), \(9\), \(1\), \(7\)", r"\(5\)"),
                          (r"\(3\), \(5\), \(8\), \(12\)", r"\(6{,}5\)")],
                  "Bereken de mediaan.", WW),
                 ("rij", [(r"\(4\), \(8\), \(8\), \(9\), \(15\)", r"\(8\)"), (r"\(6\), \(6\), \(9\), \(9\), \(13\)", r"\(6\) en \(9\)")],
                  "Wat is de modus?", WW),
                 ("kort", r"Wat is de variatiebreedte van \(5\), \(8\), \(13\) en \(21\)?", r"\(16\)", W),
                 ("waar", "Het gemiddelde moet altijd één van de gegeven waarden zijn.", False),
             ]),

        dict(kop="Terugrekenen met gemiddelden",
             opdracht="Denk aan het totaal: gemiddelde · aantal.",
             oefeningen=[
                 ("kort", r"Het gemiddelde van vijf toetsen is \(13\). Wat is het totaal van de "
                          "punten?", r"\(65\)", W),
                 ("open", r"Je hebt \(11\), \(14\) en \(15\) op drie toetsen. Wat moet je op de vierde halen "
                          r"voor een gemiddelde van \(14\)?",
                  r"\(16\). Voor gemiddelde \(14\) over vier toetsen heb je \(56\) punten nodig; je hebt er "
                  r"al \(40\).", 4),
                 ("open", r"In een frequentietabel staat: waarde \(3\) komt \(5\) keer voor, waarde \(4\) "
                          r"komt \(3\) keer voor. Hoeveel metingen zijn er, en wat is het gemiddelde?",
                  r"\(8\) metingen. Het totaal is \(5 \cdot 3 + 3 \cdot 4 = 27\), dus het gemiddelde is "
                  r"\(27 : 8 = 3{,}375\).", 4),
                 ("kort", r"Een reeks heeft gemiddelde \(20\) en variatiebreedte \(0\). Wat weet je?",
                  r"alle waarden zijn \(20\)", WW),
             ]),

        dict(kop="Diagrammen",
             opdracht=r"Een hele cirkel is \(360^{\circ}\).",
             oefeningen=[
                 ("rij", [("de temperatuur per uur", "lijndiagram"),
                          ("welk deel van de klas met de fiets komt", "cirkeldiagram"),
                          ("hoeveel leerlingen elke sport doen", "staafdiagram")],
                  "Welk diagram past het best?", WW),
                 ("rij", [(r"\(25\,\%\) van het geheel", r"\(90^{\circ}\)"), (r"een sector van \(90^{\circ}\)",
                          bundel.breuk(1, 4)), (r"\(15\) van de \(40\) leerlingen", r"\(135^{\circ}\)")],
                  "Reken om naar graden, of naar een deel.", WW),
                 ("open", r"Een staafdiagram begint zijn verticale as niet bij \(0\) maar bij \(90\). "
                          "Wat is daar het gevaar van?",
                  "Kleine verschillen lijken enorm, want de staven vergelijken alleen het stukje "
                  r"boven \(90\). Wie snel kijkt, leest een verschil dat er nauwelijks is.", 4),
             ]),

        dict(kop="Cijfers lezen met een kritische blik",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Vier mensen verdienen € \(11\), € \(13\), € \(15\) en € \(600\) per week. Welke "
                          "centrummaat geeft het eerlijkste beeld, en waarom?",
                  r"De mediaan (€ \(14\)). Het gemiddelde van € \(159{,}75\) wordt volledig opgetrokken "
                  "door die ene uitschieter en beschrijft niemand uit de groep.", 5),
                 ("waar", "De mediaan verandert nauwelijks als je er één heel grote waarde bij "
                          "doet.", True),
                 ("open", r"Je leest: „de gemiddelde Belg heeft \(1{,}7\) kinderen”. Hoe kan dat, "
                          r"terwijl niemand \(1{,}7\) kinderen heeft?",
                  "Een gemiddelde is een rekenresultaat, geen bestaand geval. Je deelt het "
                  "totale aantal kinderen door het aantal mensen; daar hoeft geen geheel getal "
                  "uit te komen.", 4),
                 ("open", r"Twee klassen hebben allebei gemiddelde \(14\), maar klas \(A\) heeft "
                          r"variatiebreedte \(4\) en klas \(B\) \(16\). Wat besluit je?",
                  r"In klas \(A\) liggen de punten dicht bij elkaar, in klas \(B\) ver uit elkaar. "
                  "Hetzelfde gemiddelde zegt dus niets over hoe de groep eruitziet.", 4),
                 ("open", "Je wil twee klassen van verschillende grootte vergelijken. Wat "
                          "gebruik je het best, en waarom?",
                  "Percentages of relatieve frequenties in plaats van aantallen, want anders "
                  "lijkt de grootste klas altijd de hoogste cijfers te hebben.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-verzamelingen-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Verzamelingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Notatie",
             opdracht="Gebruik accolades en de juiste tekens.",
             oefeningen=[
                 ("rij", [("∈", "is een element van"), ("⊂", "is een deelverzameling van"),
                          ("∩", "doorsnede"), ("∪", "unie")],
                  "Wat betekent dit teken?", "210px"),
                 ("kort", r"Hoe schrijf je de verzameling met \(2\), \(4\) en \(6\) erin?", r"\(\{2, 4, 6\}\)", W),
                 ("kort", r"Hoe schrijf je wiskundig dat \(7\) niet in \(A\) zit?", r"\(7 \notin A\)", W),
                 ("kort", "Hoe noem je een verzameling zonder elementen?",
                  r"de lege verzameling \((\emptyset)\)", WW),
                 ("waar", "De volgorde waarin je de elementen opschrijft, maakt uit.", False),
             ]),

        dict(kop="Bewerkingen",
             opdracht=r"\(A = \{1, 2, 3, 4, 5, 6\}\) en \(B = \{4, 5, 6, 7\}\). Gebruik die twee.",
             oefeningen=[
                 ("rij", [(r"\(A \cap B\)", r"\(\{4, 5, 6\}\)"), (r"\(A \cup B\)", r"\(\{1, 2, 3, 4, 5, 6, 7\}\)"),
                          (r"\(A \setminus B\)", r"\(\{1, 2, 3\}\)"), (r"\(B \setminus A\)", r"\(\{7\}\)")],
                  "Bereken.", "210px"),
                 ("waar", r"\(A \setminus B\) is altijd hetzelfde als \(B \setminus A\).", False),
                 ("rij", [(r"\(\{1, 3, 5\} \cap \{2, 4, 6\}\)", "∅"), (r"\(\{1, 2, 3\} \cap \{1, 2, 3\}\)", r"\(\{1, 2, 3\}\)"),
                          (r"\(\{1, 2\} \cup \emptyset\)", r"\(\{1, 2\}\)")],
                  "Bereken.", "210px"),
                 ("kort", r"Hoeveel elementen heeft \(\{3, 5, 5, 7\}\)?", r"\(3\)", W),
                 ("kort", "Hoeveel deelverzamelingen heeft {a, b, c}?", r"\(8\)", W),
             ]),

        dict(kop="Verzamelingen die je al kent",
             opdracht="Denk aan de meetkunde en aan de getallen.",
             oefeningen=[
                 ("rij", [("de priemgetallen en de even getallen", r"\(\{2\}\)"),
                          ("de vierkanten en de rechthoeken", "de vierkanten"),
                          ("de ruiten en de rechthoeken", "de vierkanten"),
                          (r"de delers van \(12\) en de veelvouden van \(12\)", r"\(\{12\}\)")],
                  "Wat zit er in de doorsnede?", "210px"),
                 ("open", r"\(V\) is de verzameling vierkanten en \(R\) die van de rechthoeken. Welke "
                          "van de twee is een deelverzameling van de andere, en waarom?",
                  r"\(V \subset R\). Elk vierkant heeft vier rechte hoeken en is dus een rechthoek, maar "
                  "niet elke rechthoek heeft vier gelijke zijden.", 4),
                 ("waar", r"Als \(A \subset B\), dan is \(A \cap B\) gelijk aan \(A\).", True),
                 ("open", r"Wat is het verschil tussen \(\{0\}\) en ∅?",
                  r"\(\{0\}\) is een verzameling met één element, namelijk het getal \(0\). ∅ heeft er "
                  "geen enkel. Een lege doos is niet hetzelfde als een doos met een nul erin.", 4),
             ]),

        dict(kop="Venndiagrammen",
             opdracht="Teken het diagram eerst, vul dan de aantallen in, van binnen naar buiten.",
             oefeningen=[
                 ("teken", r"Van \(30\) leerlingen volgen er \(18\) Frans, \(14\) Duits en \(5\) allebei. Teken "
                           "het venndiagram met de vier aantallen erin.",
                  r"Allebei \(5\), alleen Frans \(13\), alleen Duits \(9\), geen van beide \(3\). (\(13 + 5 + 9 = 27\), "
                  r"dus \(3\) buiten de cirkels.)", 55),
                 ("kort", r"\(A\) heeft \(9\) elementen, \(B\) heeft \(6\), en hun doorsnede heeft er \(4\). Hoeveel "
                          "elementen heeft de unie?", r"\(11\)", W),
                 ("open", "In een venndiagram is de linkercirkel volledig ingekleurd behalve het "
                          "overlappende deel. Welke bewerking is dat?",
                  r"\(A \setminus B\): alles wat in \(A\) zit maar niet in \(B\).", 3),
                 ("open", "Waarom is een venndiagram handig bij een vraagstuk met twee groepen?",
                  "Je ziet meteen dat wie in allebei de groepen zit, anders twee keer geteld "
                  "wordt. Door van de doorsnede naar buiten te werken, tel je iedereen precies "
                  "één keer.", 4),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        print("  ", naam)
