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
                 ("rij", [("&minus;8 + 3", "&minus;5"), ("6 &minus; 11", "&minus;5"),
                          ("&minus;7 &minus; 5", "&minus;12"), ("&minus;9 + 9", "0")],
                  "Bereken."),
                 ("rij", [("&minus;5 &minus; (&minus;8)", "3"), ("7 &minus; (&minus;4)", "11"),
                          ("&minus;3 + (&minus;6)", "&minus;9"), ("2 &minus; (&minus;2)", "4")],
                  "Werk eerst de haakjes weg."),
                 ("kort", "Het is 's nachts &minus;6 °C. Overdag stijgt het 11 graden. Hoe warm is het dan?",
                  "5 °C", W),
                 ("kort", "Een duiker zit op &minus;18 m en daalt nog 7 m. Waar zit hij nu?",
                  "&minus;25 m", W),
             ]),

        dict(kop="Vermenigvuldigen, delen en machten",
             opdracht="Tel eerst de mintekens, bepaal dan het teken van je antwoord.",
             oefeningen=[
                 ("rij", [("&minus;4 × 5", "&minus;20"), ("&minus;9 × &minus;3", "27"),
                          ("&minus;36 : 4", "&minus;9"), ("&minus;36 : (&minus;4)", "9")],
                  "Bereken."),
                 ("rij", [("(&minus;3)²", "9"), ("(&minus;3)³", "&minus;27"),
                          ("(&minus;1)⁵", "&minus;1"), ("(&minus;2)⁴", "16")],
                  "Bereken."),
                 ("kort", "Bereken &minus;2 × (5 &minus; 9).", "8", W),
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
                 ("rij", [("15 % van 60", "9"), ("40 % van 250", "100"),
                          ("12,5 % van 80", "10"), ("75 % van 48", "36")],
                  "Bereken."),
                 ("tabel", ["breuk", "kommagetal", "procent"],
                  [[bundel.breuk(1, 4), None, None], [bundel.breuk(5, 8), None, None],
                   [bundel.breuk(3, 5), None, None]],
                  bundel.breuk(1, 4) + " = 0,25 = 25 % · " + bundel.breuk(5, 8) +
                  " = 0,625 = 62,5 % · " + bundel.breuk(3, 5) + " = 0,6 = 60 %"),
                 ("kort", "In een klas van 40 leerlingen dragen er 14 een bril. Hoeveel procent?",
                  "35 %", W),
                 ("waar", "30 % van 50 geeft hetzelfde als 50 % van 30.", True),
             ]),

        dict(kop="Korting en stijging",
             opdracht="Reken een percentage altijd op de prijs vóór de verandering.",
             oefeningen=[
                 ("kort", "Een jas van € 80 krijgt 15 % korting. Wat betaal je?", "€ 68", W),
                 ("kort", "Een fiets kost € 180. De prijs zakt met 35 %. Wat betaal je?",
                  "€ 117", W),
                 ("kort", "Een spel kost € 90 na 25 % korting. Wat was de oude prijs?",
                  "€ 120", W),
                 ("kort", "Van 60 naar 75 gaan: hoeveel procent stijging is dat?", "25 %", W),
                 ("kort", "45 % van een klas zijn meisjes, dat zijn er 18. Hoeveel leerlingen "
                          "telt de klas?", "40", W),
                 ("open", "Een trui van € 50 gaat eerst 20 % omhoog en daarna weer 20 % omlaag. "
                          "Bereken de eindprijs en leg uit waarom dat geen € 50 is.",
                  "€ 48. De stijging rekent op 50 (+ € 10 → € 60), de daling op 60 (&minus; € 12 → "
                  "€ 48). Een percentage rekent altijd op het bedrag van dat moment, en dat is "
                  "de tweede keer groter.", 5),
                 ("waar", "Een korting van 25 % geeft hetzelfde als vermenigvuldigen met 0,75.",
                  True),
                 ("open", "De ene winkel geeft 30 % korting op een jas van € 90, de andere geeft "
                          "€ 25 korting op dezelfde jas. Waar betaal je het minst, en hoeveel?",
                  "30 % van 90 is € 27, dus daar betaal je € 63. Bij de andere betaal je € 65. "
                  "De eerste winkel is € 2 goedkoper.", 4),
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
             opdracht="Natuurlijk (ℕ), geheel (ℤ) of rationaal (ℚ)? Geef de kleinste die past.",
             oefeningen=[
                 ("rij", [("12", "ℕ"), ("&minus;7", "ℤ"), (bundel.breuk(2, 5), "ℚ"),
                          ("0", "ℕ")],
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
                          ("een breuk met teller 1", "een stambreuk")],
                  "Hoe heet dit?", WW),
                 ("rij", [("het tegengestelde van &minus;9", "9"),
                          ("het omgekeerde van " + bundel.breuk(3, 5), bundel.breuk(5, 3)),
                          ("de absolute waarde van &minus;11", "11")],
                  "Geef het gevraagde getal.", WW),
                 ("open", "Wanneer noem je twee breuken gelijknamig, en waarom wil je dat?",
                  "Als ze dezelfde noemer hebben. Pas dan tellen de tellers over hetzelfde soort "
                  "stukken en kan je optellen of aftrekken.", 3),
                 ("open", "Wanneer noem je een breuk onvereenvoudigbaar?",
                  "Als teller en noemer geen gemeenschappelijke deler meer hebben behalve 1. "
                  "Je kan er dus niets meer uit wegdelen.", 3),
             ]),

        dict(kop="Delers, veelvouden en priemgetallen",
             opdracht="Schrijf je ontbinding ernaast als dat helpt.",
             oefeningen=[
                 ("rij", [("ggd van 18 en 24", "6"), ("kgv van 6 en 8", "24"),
                          ("ggd van 30 en 45", "15"), ("kgv van 9 en 12", "36")],
                  "Bereken."),
                 ("rij", [("21", "geen"), ("29", "priem"), ("51", "geen"), ("37", "priem")],
                  "Priemgetal of niet? Schrijf 'priem' of 'geen'.", WW),
                 ("open", "Waarvoor gebruik je het kgv als je met breuken werkt?",
                  "Om twee breuken gelijknamig te maken: het kgv van de noemers is de kleinste "
                  "gemeenschappelijke noemer, dus daarmee blijven de getallen het kleinst.", 3),
                 ("waar", "2 is het enige even priemgetal.", True),
             ]),

        dict(kop="Machten, wortels en volgorde",
             opdracht="Denk aan de rekenvolgorde: eerst haakjes, dan machten, dan × en :, dan + en &minus;.",
             oefeningen=[
                 ("rij", [("3² × 3³", "3⁵ = 243"), ("(5²)³", "5⁶"),
                          ("3⁻²", bundel.breuk(1, 9)), ("2⁰", "1")],
                  "Bereken of vereenvoudig.", WW),
                 ("rij", [("√81", "9"), ("√144", "12"), ("√1", "1")], "Bereken."),
                 ("rij", [("5 + 2 × 6", "17"), ("(5 + 2) × 6", "42"),
                          ("20 &minus; 3²", "11"), ("2 × 3 + 4 × 5", "26")],
                  "Bereken."),
                 ("kort", "Wat is de rest bij de deling 29 : 4?", "1", W),
             ]),

        dict(kop="Afronden, schaal en evenredigheid",
             opdracht="Schrijf je tussenstap op.",
             oefeningen=[
                 ("rij", [("5,6749 op twee decimalen", "5,67"), ("12,395 op twee decimalen", "12,40"),
                          ("0,0648 op drie decimalen", "0,065")],
                  "Rond af.", WW),
                 ("kort", "Op een plan met schaal 1 : 100 meet een muur 4,5 cm. Hoe lang is die "
                          "muur in het echt?", "4,5 m", W),
                 ("kort", "Drie broden kosten € 4,50. Wat kosten er zeven?", "€ 10,50", W),
                 ("kort", "Hoeveel procent is " + bundel.breuk(7, 8) + "?", "87,5 %", W),
                 ("waar", "&minus;3 is groter dan &minus;5.", True),
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
                 ("open", "Je rekent uit dat een schoolbus 4,3 kinderen vervoert. Wat doe je?",
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
                 ("kort", "Een fles water kost € 1,35. Wat kosten er negen?", "€ 12,15", W),
                 ("kort", "In een klas van 28 is een vierde afwezig. Hoeveel zijn er aanwezig?",
                  "21", W),
                 ("kort", "Een tuin is 15 m op 9 m. Hoeveel meter hek heb je nodig?", "48 m", W),
                 ("kort", "Een trein vertrekt om 8.50 u en rijdt 3 u 25 min. Hoe laat komt hij aan?",
                  "12.15 u", W),
                 ("kort", "Een pak van 400 g koekjes kost € 2,60. Wat kost een kilo?", "€ 6,50", W),
                 ("kort", "Je koopt vijf broodjes van € 2,80 en betaalt met € 20. Hoeveel krijg "
                          "je terug?", "€ 6", W),
                 ("kort", "Een fietser rijdt 18 km per uur. Hoe lang doet hij over 45 km?",
                  "2 u 30 min", W),
                 ("kort", "Een recept voor 4 personen vraagt 320 g rijst. Hoeveel voor 6 personen?",
                  "480 g", W),
             ]),

        dict(kop="Terugrekenen en tellen",
             opdracht="Werk van achter naar voor, of maak een tekening.",
             oefeningen=[
                 ("open", "Ik denk aan een getal, trek er 5 van af en vermenigvuldig het "
                          "resultaat met 4. Ik krijg 28. Aan welk getal dacht ik?",
                  "12. Terugrekenen: 28 : 4 = 7, en 7 + 5 = 12.", 3),
                 ("open", "Een kaars van 24 cm brandt 3 cm per uur op. Na hoeveel uur is ze nog "
                          "6 cm lang?",
                  "6 uur. Er moet 24 &minus; 6 = 18 cm opbranden, en 18 : 3 = 6.", 3),
                 ("open", "Vier vrienden zitten aan een tafel. Ieder geeft ieder ander één keer "
                          "een hand. Hoeveel handdrukken zijn er?",
                  "6. Elk van de 4 geeft 3 handen, dat is 12, maar elke handdruk telde je twee "
                  "keer: 12 : 2 = 6.", 4),
                 ("open", "Een tuin van 24 m lang krijgt om de 4 meter een paal, ook aan het "
                          "begin en aan het einde. Hoeveel palen zijn er?",
                  "7. Er zijn 24 : 4 = 6 tussenstukken, en bij een rij met twee uiteinden staat "
                  "er altijd één paal meer dan er tussenstukken zijn.", 4),
                 ("open", "Op een parking staan auto's en motors: samen 18 voertuigen en "
                          "62 wielen. Hoeveel motors staan er?",
                  "5 motors (en 13 auto's). Stel dat het allemaal auto's waren: 18 × 4 = 72 "
                  "wielen, dat zijn er 10 te veel. Elke motor scheelt 2 wielen, dus 10 : 2 = 5.", 5),
             ]),

        dict(kop="Rijen en patronen",
             opdracht="Zoek eerst de regel, schrijf die op, en gebruik ze dan.",
             oefeningen=[
                 ("rij", [("3, 6, 12, 24, …", "48"), ("1, 4, 9, 16, …", "25"),
                          ("2, 5, 10, 17, …", "26"), ("100, 91, 82, 73, …", "64")],
                  "Welk getal komt er daarna?", WW),
                 ("open", "Een som van drie opeenvolgende getallen is 57. Wat is het kleinste?",
                  "18. Het middelste getal is 57 : 3 = 19, dus de drie zijn 18, 19 en 20.", 3),
                 ("open", "Het is nu 15.00 u. Hoe laat is het over 100 uur?",
                  "19.00 u. 100 : 24 = 4 dagen en 4 uur over, dus 15.00 u + 4 uur.", 3),
                 ("open", "Je verdeelt 100 snoepjes eerlijk over een aantal kinderen en er "
                          "blijven er 4 over. Hoeveel kinderen kunnen er zijn?",
                  "Een deler van 96 die groter is dan 4: 6, 8, 12, 16, 24, 32, 48 of 96. "
                  "(Groter dan 4, anders zou je de rest nog kunnen uitdelen.)", 4),
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
                 ("rij", [("alle priemgetallen zijn oneven", "2"),
                          ("het kwadraat van een getal is groter dan het getal zelf", "1 (of 0)"),
                          ("elk getal deelbaar door 3 is deelbaar door 6", "9"),
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
                 ("rij", [("een getal is deelbaar door 6 … het is deelbaar door 3", "⇒"),
                          ("een vierhoek is een vierkant … hij heeft vier rechte hoeken", "⇒"),
                          ("een getal is even … het eindigt op 0, 2, 4, 6 of 8", "⇔"),
                          ("een getal is groter dan 10 … het is groter dan 5", "⇒")],
                  "Welke pijl hoort hier: ⇒ of ⇔?", WW),
                 ("open", "Waarom staat er bij 'deelbaar door 6 ⇒ deelbaar door 3' geen dubbele "
                          "pijl?",
                  "Omdat de omgekeerde uitspraak niet klopt: 9 is deelbaar door 3 maar niet door "
                  "6. Een dubbele pijl mag pas als het in allebei de richtingen geldt.", 4),
                 ("waar", "Een vierkant is altijd een rechthoek.", True),
                 ("waar", "Een rechthoek is altijd een vierkant.", False),
             ]),

        dict(kop="Waar zit de fout?",
             opdracht="Schrijf niet enkel 'fout', maar zeg in welke stap het misging.",
             oefeningen=[
                 ("open", "Iemand redeneert: „7 &gt; 4, dus &minus;7 &gt; &minus;4.” Waar zit de fout?",
                  "Bij het vermenigvuldigen met &minus;1 draait een ongelijkheid om. Het moet "
                  "&minus;7 &lt; &minus;4 zijn.", 3),
                 ("open", "Iemand schrijft: „24 : 6 : 2 = 24 : 3 = 8”. Wat ging er mis?",
                  "Delingen werk je van links naar rechts af: 24 : 6 = 4, en 4 : 2 = 2. De "
                  "tweede deling zomaar eerst doen mag niet.", 3),
                 ("open", "Iemand schrijft: „√(16 + 9) = √16 + √9 = 4 + 3 = 7”. Klopt dat?",
                  "Nee. √25 = 5, niet 7. Een wortel mag je niet over een som verdelen.", 3),
                 ("open", "Iemand zegt: „20 % korting en daarna nog eens 20 % korting is samen "
                          "40 % korting.” Wat is er mis?",
                  "De tweede korting rekent op de al verlaagde prijs. 0,8 × 0,8 = 0,64, dus je "
                  "betaalt 64 % en de korting is samen 36 %, niet 40 %.", 4),
                 ("open", "Een redenering klopt in elke stap, maar de laatste zin beantwoordt "
                          "een andere vraag dan er gesteld werd. Wat is je oordeel?",
                  "De oefening is fout opgelost. Rekenen dat klopt maar niet de gestelde vraag "
                  "beantwoordt, levert geen antwoord.", 3),
             ]),

        dict(kop="Algemeen redeneren",
             opdracht="Redeneer met letters, niet met voorbeelden.",
             oefeningen=[
                 ("open", "Toon aan dat de som van twee even getallen altijd even is.",
                  "Elk even getal kan je schrijven als 2a en 2b. Hun som is 2a + 2b = 2(a + b), "
                  "en dat is een veelvoud van 2, dus even.", 4),
                 ("waar", "Het product van twee oneven getallen is altijd even.", False),
                 ("rij", [("uit a = b volgt a² = b²", "juist"),
                          ("uit a² = b² volgt a = b", "fout"),
                          ("uit a × b = 0 volgt a = 0", "fout")],
                  "Juist of fout?", WW),
                 ("open", "Geef bij elk van de twee foute uitspraken hierboven een "
                          "tegenvoorbeeld.",
                  "a² = b²: neem a = 3 en b = &minus;3. a × b = 0: neem a = 5 en b = 0, dan is "
                  "het product 0 terwijl a niet 0 is.", 4),
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
                 ("rij", [("de nevenhoek van 55°", "125°"), ("de overstaande hoek van 55°", "55°"),
                          ("de complementaire hoek van 55°", "35°")],
                  "Twee rechten snijden elkaar onder 55°. Bereken.", WW),
                 ("kort", "Twee evenwijdige rechten worden gesneden door een derde rechte. Eén "
                          "overeenkomstige hoek is 72°. Hoe groot is de andere?", "72°", W),
                 ("waar", "Twee evenwijdige rechten snijden elkaar ver genoeg verderop toch.",
                  False),
             ]),

        dict(kop="Rekenen met hoeken in figuren",
             opdracht="De som van de hoeken van een driehoek is 180°, van een vierhoek 360°.",
             oefeningen=[
                 ("rij", [("een driehoek met 40° en 75°", "65°"),
                          ("een driehoek met 90° en 32°", "58°"),
                          ("een vierhoek met 100°, 85° en 95°", "80°")],
                  "Hoe groot is de ontbrekende hoek?", WW),
                 ("kort", "In een gelijkbenige driehoek is de tophoek 50°. Hoe groot is elke "
                          "basishoek?", "65°", W),
                 ("kort", "In een gelijkbenige driehoek is een basishoek 70°. Hoe groot is de "
                          "tophoek?", "40°", W),
                 ("kort", "In een parallellogram is één hoek 115°. Hoe groot is de hoek ernaast?",
                  "65°", W),
                 ("open", "Een driehoek heeft hoeken van 90° en 45°. Wat weet je allemaal over "
                          "die driehoek?",
                  "De derde hoek is ook 45°, dus de driehoek is rechthoekig én gelijkbenig. De "
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
                 ("rij", [("een vierkant", "4"), ("een gewone rechthoek", "2"),
                          ("een gelijkzijdige driehoek", "3"), ("een gewoon parallellogram", "0")],
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
             opdracht="Zet de maatladder eronder als dat helpt. Let op: bij m² spring je per twee, bij m³ per drie.",
             oefeningen=[
                 ("rij", [("4,2 km in m", "4 200 m"), ("75 cm in m", "0,75 m"),
                          ("3,4 kg in g", "3 400 g"), ("250 ml in l", "0,25 l")],
                  "Zet om."),
                 ("rij", [("4 m² in dm²", "400 dm²"), ("3 m² in cm²", "30 000 cm²"),
                          ("2 m³ in l", "2 000 l"), ("5 000 cm³ in dm³", "5 dm³")],
                  "Zet om.", WW),
                 ("rij", [("3,5 uur in minuten", "210 min"), ("een half uur in seconden", "1 800 s"),
                          ("135 minuten in uren en minuten", "2 u 15 min")],
                  "Zet om.", WW),
                 ("waar", "1 liter is hetzelfde als 1 dm³.", True),
             ]),

        dict(kop="Omtrek en oppervlakte",
             opdracht="Schrijf eerst de formule op, vul dan de getallen in.",
             oefeningen=[
                 ("rij", [("rechthoek 9 cm op 4 cm", "26 cm"), ("vierkant met zijde 7 cm", "28 cm"),
                          ("gelijkzijdige driehoek met zijde 6 cm", "18 cm")],
                  "Bereken de omtrek.", WW),
                 ("rij", [("rechthoek 9 cm op 4 cm", "36 cm²"),
                          ("driehoek met basis 10 cm en hoogte 6 cm", "30 cm²"),
                          ("parallellogram met basis 8 cm en hoogte 5 cm", "40 cm²"),
                          ("ruit met diagonalen 10 cm en 6 cm", "30 cm²")],
                  "Bereken de oppervlakte.", WW),
                 ("kort", "Een trapezium heeft evenwijdige zijden van 5 cm en 11 cm en een "
                          "hoogte van 6 cm. Wat is de oppervlakte?", "48 cm²", W),
                 ("kort", "Een vierkant heeft een oppervlakte van 64 cm². Hoe lang is een zijde?",
                  "8 cm", W),
                 ("kort", "Een rechthoek heeft een oppervlakte van 54 cm² en een lengte van "
                          "9 cm. Hoe breed is hij?", "6 cm", W),
             ]),

        dict(kop="De cirkel",
             opdracht="Neem π = 3,14. Schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", "Een cirkel heeft een straal van 4 cm. Hoe lang is de omtrek?",
                  "25,12 cm", W),
                 ("kort", "Dezelfde cirkel: hoe groot is de oppervlakte?", "50,24 cm²", W),
                 ("kort", "Een cirkel heeft een diameter van 12 cm. Hoe lang is de omtrek?",
                  "37,68 cm", W),
                 ("open", "Een figuur bestaat uit een vierkant met zijde 8 cm, met daarop een "
                          "halve cirkel met diameter 8 cm. Bereken de totale oppervlakte.",
                  "Het vierkant is 64 cm². De halve cirkel heeft straal 4, dus "
                  "(3,14 × 4 × 4) : 2 = 25,12 cm². Samen 89,12 cm².", 5),
             ]),

        dict(kop="Ruimtefiguren",
             opdracht="Let op het verschil tussen oppervlakte (cm²) en volume (cm³).",
             oefeningen=[
                 ("fig", [(svg.ruimtefiguur("kubus"), "kubus"), (svg.ruimtefiguur("cilinder"), "cilinder"),
                          (svg.ruimtefiguur("kegel"), "kegel")],
                  "Hoe heet deze ruimtefiguur?"),
                 ("rij", [("kubus met ribbe 5 cm", "125 cm³"),
                          ("balk 6 cm op 4 cm op 3 cm", "72 cm³"),
                          ("kubus met ribbe 2 dm, in liter", "8 l")],
                  "Bereken het volume.", WW),
                 ("kort", "Wat is de totale oppervlakte van een kubus met ribbe 5 cm?",
                  "150 cm²", W),
                 ("kort", "Een cilinder heeft straal 2 cm en hoogte 10 cm. Wat is het volume? "
                          "Neem π = 3,14.", "125,6 cm³", W),
                 ("kort", "Een zwembad van 12 m op 5 m staat 1,5 m vol. Hoeveel liter is dat?",
                  "90 000 l", W),
             ]),

        dict(kop="Denken over maten",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("waar", "Twee rechthoeken met dezelfde omtrek hebben ook dezelfde oppervlakte.",
                  False),
                 ("open", "Je verdubbelt de zijde van een vierkant. Wat gebeurt er met de "
                          "oppervlakte, en waarom?",
                  "Ze wordt vier keer zo groot. De oppervlakte is zijde × zijde, dus je "
                  "vermenigvuldigt twee keer met 2.", 4),
                 ("kort", "Een tuin is 25 m op 16 m. Hoeveel are is dat?", "4 are", W),
                 ("kort", "Een pad van 1,8 km leg je af in 20 minuten. Hoeveel meter per minuut?",
                  "90 m/min", W),
                 ("kort", "Een plan heeft schaal 1 : 200. Een muur is 6 cm op het plan. Hoe lang "
                          "is hij echt?", "12 m", W),
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
                 ("kort", "Welke coördinaten heeft de oorsprong?", "(0, 0)", W),
                 ("kort", "Een punt ligt op de x-as. Wat weet je over zijn y-coördinaat?",
                  "die is 0", W),
                 ("teken", "Teken een assenstelsel en zet deze punten erop: A(2, 3), B(&minus;1, 4), "
                           "C(0, &minus;2) en D(3, 0).",
                  "A rechtsboven, B linksboven, C op de y-as onder de oorsprong, D op de x-as "
                  "rechts van de oorsprong.", 55),
             ]),

        dict(kop="Rekenen met letters",
             opdracht="Gelijksoortige termen mag je samennemen, andere niet.",
             oefeningen=[
                 ("rij", [("3x als x = 7", "21"), ("2a + 5 als a = 9", "23"),
                          ("x² &minus; 3x als x = 6", "18"), ("2a &minus; b als a = 4 en b = &minus;5", "13")],
                  "Bereken de getalwaarde.", WW),
                 ("rij", [("5a + 2a &minus; 3a", "4a"), ("4(x + 3)", "4x + 12"),
                          ("2(3x &minus; 4) + 5x", "11x &minus; 8"), ("7b &minus; b", "6b")],
                  "Herleid of werk de haakjes weg.", WW),
                 ("rij", [("(a + b)²", "a² + 2ab + b²"), ("(a &minus; b)²", "a² &minus; 2ab + b²"),
                          ("(a + b)(a &minus; b)", "a² &minus; b²"), ("(x + 5)²", "x² + 10x + 25")],
                  "Werk uit.", "230px"),
                 ("kort", "Wat is de graad van de veelterm 4x³ + 2x &minus; 9?", "3", W),
                 ("kort", "In de eenterm 7x⁴, welk getal is de coëfficiënt?", "7", W),
             ]),

        dict(kop="Vergelijkingen oplossen",
             opdracht="Doe links en rechts altijd hetzelfde. Schrijf elke stap op.",
             oefeningen=[
                 ("rij", [("x + 9 = 15", "x = 6"), ("4x = 28", "x = 7"),
                          ("3x + 4 = 19", "x = 5"), ("x &minus; 6 = &minus;11", "x = &minus;5")],
                  "Los op.", WW),
                 ("rij", [("6x &minus; 5 = 3x + 7", "x = 4"), ("2(x &minus; 3) = 14", "x = 10"),
                          ("x : 5 = 4", "x = 20"), ("5 &minus; x = 12", "x = &minus;7")],
                  "Los op.", WW),
                 ("open", "Bij 6x = 30 deelt iemand enkel links door 6 en schrijft x = 30. "
                          "Wat is er mis?",
                  "Wat je links doet, moet je ook rechts doen. Anders klopt de gelijkheid niet "
                  "meer. Het juiste antwoord is x = 5.", 3),
             ]),

        dict(kop="Vraagstukken met een vergelijking",
             opdracht="Zeg eerst wat x is, stel dan de vergelijking op, los dan op.",
             oefeningen=[
                 ("open", "Ik denk aan een getal. Het drievoud ervan min 4 is 26. Schrijf de "
                          "vergelijking en los ze op.",
                  "3x &minus; 4 = 26, dus 3x = 30 en x = 10.", 4),
                 ("open", "Een taxi vraagt € 4 opstapgeld en € 1,50 per kilometer. Je betaalt "
                          "€ 25. Hoeveel kilometer reed je?",
                  "4 + 1,5k = 25, dus 1,5k = 21 en k = 14 km.", 4),
                 ("open", "De omtrek van een rechthoek is 34 cm en de lengte is 11 cm. Welke "
                          "vergelijking gebruik je voor de breedte b, en wat is b?",
                  "2 × (11 + b) = 34, dus 11 + b = 17 en b = 6 cm.", 4),
             ]),

        dict(kop="Evenredigheid en rijen",
             opdracht="Recht evenredig: keer zoveel. Omgekeerd evenredig: het product blijft gelijk.",
             oefeningen=[
                 ("tabel", ["aantal broden", "prijs in €"],
                  [["3", "4,50"], ["5", None], ["8", None]],
                  "5 broden kosten € 7,50 · 8 broden kosten € 12"),
                 ("open", "Zes werklui doen een klus in 8 dagen. Hoe lang doen twaalf werklui "
                          "erover? Leg uit welk soort verband dat is.",
                  "4 dagen. Dit is omgekeerd evenredig: het product blijft 48 manddagen, dus "
                  "dubbel zoveel werklui betekent de helft van de tijd.", 4),
                 ("waar", "De grafiek van een recht evenredig verband is een rechte lijn door "
                          "de oorsprong.", True),
                 ("rij", [("4, 9, 14, 19, …", "24"), ("3, 6, 12, 24, …", "48"),
                          ("1, 3, 6, 10, …", "15")],
                  "Welk getal komt er daarna?", WW),
                 ("open", "Met lucifers leg je driehoekjes op een rij: 1 driehoek kost 3 "
                          "lucifers, 2 kosten er 5, 3 kosten er 7. Hoeveel voor n driehoekjes?",
                  "2n + 1. De eerste kost 3, en elke volgende komt er met 2 lucifers bij.", 4),
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
                 ("rij", [("3, 7, 8", "6"), ("4, 6, 6, 12", "7"),
                          ("10, 10, 10, 10", "10")],
                  "Bereken het gemiddelde.", WW),
                 ("rij", [("2, 9, 9, 11, 14", "9"), ("5, 3, 9, 1, 7", "5"),
                          ("3, 5, 8, 12", "6,5")],
                  "Bereken de mediaan.", WW),
                 ("rij", [("4, 8, 8, 9, 15", "8"), ("6, 6, 9, 9, 13", "6 en 9")],
                  "Wat is de modus?", WW),
                 ("kort", "Wat is de variatiebreedte van 5, 8, 13 en 21?", "16", W),
                 ("waar", "Het gemiddelde moet altijd één van de gegeven waarden zijn.", False),
             ]),

        dict(kop="Terugrekenen met gemiddelden",
             opdracht="Denk aan het totaal: gemiddelde × aantal.",
             oefeningen=[
                 ("kort", "Het gemiddelde van vijf toetsen is 13. Wat is het totaal van de "
                          "punten?", "65", W),
                 ("open", "Je hebt 11, 14 en 15 op drie toetsen. Wat moet je op de vierde halen "
                          "voor een gemiddelde van 14?",
                  "16. Voor gemiddelde 14 over vier toetsen heb je 56 punten nodig; je hebt er "
                  "al 40.", 4),
                 ("open", "In een frequentietabel staat: waarde 3 komt 5 keer voor, waarde 4 "
                          "komt 3 keer voor. Hoeveel metingen zijn er, en wat is het gemiddelde?",
                  "8 metingen. Het totaal is 5 × 3 + 3 × 4 = 27, dus het gemiddelde is "
                  "27 : 8 = 3,375.", 4),
                 ("kort", "Een reeks heeft gemiddelde 20 en variatiebreedte 0. Wat weet je?",
                  "alle waarden zijn 20", WW),
             ]),

        dict(kop="Diagrammen",
             opdracht="Een hele cirkel is 360°.",
             oefeningen=[
                 ("rij", [("de temperatuur per uur", "lijndiagram"),
                          ("welk deel van de klas met de fiets komt", "cirkeldiagram"),
                          ("hoeveel leerlingen elke sport doen", "staafdiagram")],
                  "Welk diagram past het best?", WW),
                 ("rij", [("25 % van het geheel", "90°"), ("een sector van 90°",
                          bundel.breuk(1, 4)), ("15 van de 40 leerlingen", "135°")],
                  "Reken om naar graden, of naar een deel.", WW),
                 ("open", "Een staafdiagram begint zijn verticale as niet bij 0 maar bij 90. "
                          "Wat is daar het gevaar van?",
                  "Kleine verschillen lijken enorm, want de staven vergelijken alleen het stukje "
                  "boven 90. Wie snel kijkt, leest een verschil dat er nauwelijks is.", 4),
             ]),

        dict(kop="Cijfers lezen met een kritische blik",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Vier mensen verdienen € 11, € 13, € 15 en € 600 per week. Welke "
                          "centrummaat geeft het eerlijkste beeld, en waarom?",
                  "De mediaan (€ 14). Het gemiddelde van € 159,75 wordt volledig opgetrokken "
                  "door die ene uitschieter en beschrijft niemand uit de groep.", 5),
                 ("waar", "De mediaan verandert nauwelijks als je er één heel grote waarde bij "
                          "doet.", True),
                 ("open", "Je leest: „de gemiddelde Belg heeft 1,7 kinderen”. Hoe kan dat, "
                          "terwijl niemand 1,7 kinderen heeft?",
                  "Een gemiddelde is een rekenresultaat, geen bestaand geval. Je deelt het "
                  "totale aantal kinderen door het aantal mensen; daar hoeft geen geheel getal "
                  "uit te komen.", 4),
                 ("open", "Twee klassen hebben allebei gemiddelde 14, maar klas A heeft "
                          "variatiebreedte 4 en klas B 16. Wat besluit je?",
                  "In klas A liggen de punten dicht bij elkaar, in klas B ver uit elkaar. "
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
                 ("kort", "Hoe schrijf je de verzameling met 2, 4 en 6 erin?", "{2, 4, 6}", W),
                 ("kort", "Hoe schrijf je wiskundig dat 7 niet in A zit?", "7 ∉ A", W),
                 ("kort", "Hoe noem je een verzameling zonder elementen?",
                  "de lege verzameling (∅)", WW),
                 ("waar", "De volgorde waarin je de elementen opschrijft, maakt uit.", False),
             ]),

        dict(kop="Bewerkingen",
             opdracht="A = {1, 2, 3, 4, 5, 6} en B = {4, 5, 6, 7}. Gebruik die twee.",
             oefeningen=[
                 ("rij", [("A ∩ B", "{4, 5, 6}"), ("A ∪ B", "{1, 2, 3, 4, 5, 6, 7}"),
                          ("A \\ B", "{1, 2, 3}"), ("B \\ A", "{7}")],
                  "Bereken.", "210px"),
                 ("waar", "A \\ B is altijd hetzelfde als B \\ A.", False),
                 ("rij", [("{1, 3, 5} ∩ {2, 4, 6}", "∅"), ("{1, 2, 3} ∩ {1, 2, 3}", "{1, 2, 3}"),
                          ("{1, 2} ∪ ∅", "{1, 2}")],
                  "Bereken.", "210px"),
                 ("kort", "Hoeveel elementen heeft {3, 5, 5, 7}?", "3", W),
                 ("kort", "Hoeveel deelverzamelingen heeft {a, b, c}?", "8", W),
             ]),

        dict(kop="Verzamelingen die je al kent",
             opdracht="Denk aan de meetkunde en aan de getallen.",
             oefeningen=[
                 ("rij", [("de priemgetallen en de even getallen", "{2}"),
                          ("de vierkanten en de rechthoeken", "de vierkanten"),
                          ("de ruiten en de rechthoeken", "de vierkanten"),
                          ("de delers van 12 en de veelvouden van 12", "{12}")],
                  "Wat zit er in de doorsnede?", "210px"),
                 ("open", "V is de verzameling vierkanten en R die van de rechthoeken. Welke "
                          "van de twee is een deelverzameling van de andere, en waarom?",
                  "V ⊂ R. Elk vierkant heeft vier rechte hoeken en is dus een rechthoek, maar "
                  "niet elke rechthoek heeft vier gelijke zijden.", 4),
                 ("waar", "Als A ⊂ B, dan is A ∩ B gelijk aan A.", True),
                 ("open", "Wat is het verschil tussen {0} en ∅?",
                  "{0} is een verzameling met één element, namelijk het getal 0. ∅ heeft er "
                  "geen enkel. Een lege doos is niet hetzelfde als een doos met een nul erin.", 4),
             ]),

        dict(kop="Venndiagrammen",
             opdracht="Teken het diagram eerst, vul dan de aantallen in, van binnen naar buiten.",
             oefeningen=[
                 ("teken", "Van 30 leerlingen volgen er 18 Frans, 14 Duits en 5 allebei. Teken "
                           "het venndiagram met de vier aantallen erin.",
                  "Allebei 5, alleen Frans 13, alleen Duits 9, geen van beide 3. (13 + 5 + 9 = 27, "
                  "dus 3 buiten de cirkels.)", 55),
                 ("kort", "A heeft 9 elementen, B heeft 6, en hun doorsnede heeft er 4. Hoeveel "
                          "elementen heeft de unie?", "11", W),
                 ("open", "In een venndiagram is de linkercirkel volledig ingekleurd behalve het "
                          "overlappende deel. Welke bewerking is dat?",
                  "A \\ B: alles wat in A zit maar niet in B.", 3),
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
