"""De eigenheid van de filosofie — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_eigenheid: dagdagelijkse en wetenschappelijke
kennis, natuur- en menswetenschappen (gedrags- en cultuurwetenschappen), de
plaats van de filosofie en de filosofische verwondering. Met een zelfgetekend
schema van de wetenschappen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, GEEL

WS = Prent("schema-wetenschappen", "De wetenschappen", "een boomschema met vijf vakken, letters A tot E; D en E dragen een naam")
VAKKEN = {"A": (400, 80, 200, 70), "B": (130, 230, 220, 70), "C": (650, 230, 220, 70), "D": (440, 400, 260, 70), "E": (720, 400, 260, 70)}
KL = {"A": GEEL, "B": LICHTGROEN, "C": "#9ec7e6", "D": "#ffffff", "E": "#ffffff"}
WS.lijn(500, 150, 240, 230, DONKER, 3); WS.lijn(500, 150, 760, 230, DONKER, 3)
WS.lijn(760, 300, 570, 400, DONKER, 3); WS.lijn(760, 300, 850, 400, DONKER, 3)
for t, (x, y, b, h) in VAKKEN.items():
    WS.rect(x, y, b, h, KL[t], DONKER, 10, 3)
    if t in "DE":
        WS.letter(x + 30, y + h / 2, t)
        WS.tekst(x + 152, y + h / 2 + 6, "gedragswetenschappen" if t == "D" else "cultuurwetenschappen", 17, vet=True)
    else:
        WS.letter(x + b / 2, y + h / 2, t)
WS.tekst(500, 590, "Elk vak is een groep wetenschappen. A, B en C zijn leeg gelaten.", 20)
U = "schema-wetenschappen.svg"
Z = {t: [Prent.zone(x, y, b, h)] for t, (x, y, b, h) in VAKKEN.items()}

ONDERZOEK = ("Lees de situatie.\n\n"
             "Lotte hoort van haar buurman dat jongeren tegenwoordig minder lezen dan vroeger. Een onderzoeksbureau bevraagt "
             "daarna 3 000 jongeren met dezelfde vragenlijst als twintig jaar geleden. Een filosoof vraagt zich af: wat is "
             "eigenlijk 'lezen'? Telt een lang bericht op je gsm ook?")

VRAGEN = [
    klik("Bekijk het schema. Klik op het vak waar de psychologie hoort.", U, Z["D"], "Psychologie is een gedragswetenschap, binnen de menswetenschappen."),
    klik("Klik op het vak waar de fysica, de chemie en de biologie horen.", U, Z["B"], "De natuurwetenschappen."),
    klik("Klik op het vak waar de geschiedenis en de antropologie horen.", U, Z["E"], "Cultuurwetenschappen, binnen de menswetenschappen."),
    klik("Klik op het vak van de groep waar de filosofie bij hoort, met haar eigen vragen en methode.", U, Z["C"], "Filosofie hoort bij de menswetenschappen, net als de gedrags- en cultuurwetenschappen."),
    casus(ONDERZOEK, [
        sorteer("Welke soort kennis?", ["dagdagelijkse kennis", "wetenschappelijke kennis"],
                [("wat de buurman zegt", "dagdagelijkse kennis"), ("de bevraging van 3 000 jongeren", "wetenschappelijke kennis")],
                "Wetenschappelijke kennis volgt een methode die anderen kunnen nagaan."),
        mk("Waarom gebruikt het bureau dezelfde vragenlijst als twintig jaar geleden?",
           ["zo kan je de resultaten eerlijk vergelijken", "omdat een nieuwe vragenlijst te duur zou zijn", "omdat jongeren de oude vragen al kennen", "omdat de buurman dat zo gevraagd had"],
           0, "Een methode die anderen kunnen nagaan en herhalen."),
        keuze("De vraag 'wat is eigenlijk lezen?' is een [[*filosofische|natuurwetenschappelijke|dagdagelijkse]] vraag.", "De filosoof zoekt het begrip zelf; het bureau meet hoe vaak het voorkomt."),
        mk("Waarom is dit onderzoek bij mensen moeilijker dan bij stenen?",
           ["mensen reageren op het onderzoek zelf", "mensen zijn veel zwaarder en groter dan stenen om te meten", "stenen kan je in geen geval meten met een vragenlijst", "mensen veranderen eigenlijk nooit van mening"],
           0, "Wie weet dat hij bekeken wordt, gedraagt zich anders."),
    ]),
    tabel("Klopt dit over de eigenheid van de filosofie?",
          [("Dagdagelijkse kennis is altijd fout.", F), ("Wetenschappelijke kennis kan bijgesteld worden.", J), ("Psychologie is een natuurwetenschap.", F), ("Filosofie werkt met argumenten in plaats van metingen.", J)],
          "Dagdagelijkse kennis is vaak nuttig, maar niet systematisch gecontroleerd."),
    sorteer("Natuurwetenschap, gedragswetenschap of cultuurwetenschap?", ["natuurwetenschap", "gedragswetenschap", "cultuurwetenschap"],
            [("sterrenkunde", "natuurwetenschap"), ("psychologie", "gedragswetenschap"), ("geschiedenis", "cultuurwetenschap"), ("chemie", "natuurwetenschap"), ("antropologie", "cultuurwetenschap")],
            "Menswetenschappen splits je in gedrags- en cultuurwetenschappen."),
    keuze("Filosofie begint met [[*verwondering|een experiment|een meting]].", "Je verbazen over wat iedereen gewoon vindt."),
    mk("Waarover verwondert een filosoof zich het eerst?",
       ["over het gewone, zoals de tijd", "over een zeldzame komeet die voorbijvliegt", "over de uitslag van een spannende voetbalmatch", "over het weerbericht van morgen in de krant"],
       0, "Niet de komeet maar de stoel verbaast de filosoof."),
    keuze("Een vraag als 'is het rechtvaardig dat rijke landen meer uitstoten?' los je op met [[*argumenten|een meettoestel|een vragenlijst]].", "Haar vragen zijn niet meetbaar."),
    mk("Waarom noemt men filosofie de moeder van de wetenschappen?",
       ["veel vakken begonnen als filosofische vraag", "filosofie is ouder dan de mens zelf", "filosofen bouwden de eerste laboratoria", "elke wetenschapper moet eerst filosofie studeren"],
       0, "Fysica, psychologie en biologie werden pas later eigen vakken."),
    sorteer("Hoort de houding bij filosoferen?", ["ja", "nee"],
            [("doorvragen", "ja"), ("twijfelen aan het vanzelfsprekende", "ja"), ("je mening laten tegenspreken", "ja"), ("alles aannemen wat je hoort", "nee"), ("snel een antwoord kiezen en stoppen", "nee")],
            "Elk antwoord roept nieuwe vragen op."),
    keuze("Een socioloog meet hoeveel mensen eerlijk zijn. De filosoof vraagt [[*wat eerlijkheid is|hoeveel mensen liegen|waar eerlijke mensen wonen]].", "De filosoof zoekt het begrip."),
    keuze("De wetenschap beschrijft vooral [[*hoe iets is|wat zou moeten]], de filosofie vraagt ook naar wat zou moeten.", "Dat iets kan, zegt niet dat het mag."),
    inv("Hoe heet de filosofische vraag hoe betrouwbaar je kennis is? Eén woord.", ["kennisleer", "de kennisleer", "kennistheorie"], "De kennisleer."),
    mk("Een kind vraagt: 'Waarom moet ik delen?' Wat is dat?",
       ["het begin van een filosofische vraag", "een vraag die je met een experiment kan beantwoorden", "een natuurwetenschappelijke vraag over het lichaam", "een vraag zonder enige waarde voor het denken"],
       0, "Kinderen filosoferen uit zichzelf."),
    tabel("Is het dagdagelijkse kennis?",
          [("'Mijn oma zegt dat het gaat regenen.'", J), ("'Uit metingen van 30 jaar blijkt dat de zomers warmer worden.'", F), ("'Iedereen weet dat katten eigenwijs zijn.'", J), ("'Een proef die door drie labo's herhaald werd.'", F)],
          "Wetenschap is controleerbaar en herhaalbaar."),
    sleep("Wetenschappelijke kennis volgt een [[methode]], is [[controleerbaar]] en kan door nieuw onderzoek [[bijgesteld]] worden.",
          ["geheim", "eeuwig"], "Dat is de kracht van wetenschap."),
    mk("Waarom blijft filosofie nodig naast de wetenschap?",
       ["wetenschap zegt niet wat goed is", "wetenschap is in de meeste gevallen gewoon fout", "filosofie meet veel nauwkeuriger dan de wetenschap", "zonder filosofie zouden er geen getallen bestaan"],
       0, "Dat iets kan, zegt niet dat het mag."),
    keuze("Dagdagelijkse kennis kan fout zijn zonder dat je het merkt, omdat je [[*vooral voorbeelden ziet die je verwachting bevestigen|nooit iets meemaakt|alles meet]].", "Wetenschap zoekt juist de tegenvoorbeelden."),
    inv("Hoe heet de groep wetenschappen waartoe de sociologie en de psychologie samen horen? Eén woord.", ["menswetenschappen", "de menswetenschappen", "menswetenschap"], "De menswetenschappen."),
    open_("Bedenk een filosofische vraag over iets heel gewoons uit je dag. Leg uit waarom je die vraag niet met een meting kan beantwoorden.",
          "Wat is vriendschap eigenlijk? Je kan meten hoeveel vrienden iemand heeft, maar geen toestel zegt je wat vriendschap is. Daarvoor moet je redeneren en argumenten afwegen."),
    keuze("Filosofie hoort bij de menswetenschappen, maar [[*heeft eigen vragen en een eigen methode|gebruikt dezelfde metingen als de psychologie|is eigenlijk een natuurwetenschap]].", "Ze onderzoekt door te denken en te argumenteren."),
    tabel("Is het een natuurwetenschap?",
          [("biologie", J), ("sociologie", F), ("fysica", J), ("psychologie", F)],
          "Sociologie en psychologie zijn menswetenschappen."),
    keuze("Een filosofische vraag kan je [[*niet|wel]] met een experiment beslechten.", "Je komt er met redeneren."),
    mk("Een onderzoek naar plantengroei in de woestijn. Welke soort wetenschap?",
       ["een natuurwetenschap", "een cultuurwetenschap over volkeren", "een gedragswetenschap over mensen", "de filosofie van de natuur"],
       0, "Plantengroei is biologie."),
    keuze("Wie niets vreemd vindt, [[*stelt geen vragen|is een goede filosoof|weet alles]].", "Zonder verwondering komt het denken niet in beweging."),
]
