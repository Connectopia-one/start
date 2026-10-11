# -*- coding: utf-8 -*-
"""De vragen voor "Wiskundige redeneringen en uitspraken" (✨ Spark, wiskunde).

De vakfiche vraagt hier drie dingen: je beoordeelt of een uitspraak klopt, je
geeft een voorbeeld bij een juiste uitspraak en een tegenvoorbeeld bij een
foute, en je schrijft een redenering correct op met ⇒ en ⇔.

De fiche zegt er uitdrukkelijk bij dat dit geen los onderdeel is: het komt in
alle andere onderdelen terug. Daarom leunen de vragen hier op leerstof die de
andere hoofdstukken ook gebruiken — getallen, breuken, meetkunde — en gaat het
telkens om de redenering eromheen, niet om het rekenwerk zelf.

Deel 1 blijft bij één uitspraak per keer. Deel 2 vraagt om de richting van een
als-dan te bewaken en om zelf een tegenvoorbeeld te kiezen.

De wiskundige notatie staat in de vragen zelf: \\(a \\Rightarrow b\\),
\\(a \\Leftrightarrow b\\) en \\(x \\leq 5\\).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: „alle vogels kunnen vliegen”. Wat is genoeg om aan te tonen dat dat niet klopt?",
        opties=[
            "Eén vogel aanwijzen die niet kan vliegen",
            "Tien vogels aanwijzen die wel kunnen vliegen",
            "Zeggen dat je het niet gelooft",
        ],
        antwoord=0,
        uitleg="Eén geval dat de uitspraak onderuithaalt, is genoeg. Zo'n geval heet een "
               "tegenvoorbeeld. Een pinguïn volstaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je één geval waarmee je aantoont dat een uitspraak niet klopt?",
        opties=["Een tegenvoorbeeld", "Een bewijs", "Een eigenschap"],
        antwoord=0,
        uitleg="Een tegenvoorbeeld. Eén stuks is genoeg: een uitspraak die voor álle gevallen zou "
               "moeten gelden, valt door één uitzondering.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je tien voorbeelden vindt waarin een uitspraak klopt, dan is de uitspraak bewezen.",
        antwoord=False,
        uitleg="Nee. Voorbeelden kunnen een uitspraak illustreren, maar niet bewijzen. Er kan altijd "
               "nog een geval bestaan dat je niet bekeek. Eén tegenvoorbeeld kan haar wél omverwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Als een getal deelbaar is door \(4\), dan is het deelbaar door \(2\).” Klopt dat?",
        opties=["Ja, altijd", "Nee, nooit", r"Alleen bij even getallen boven \(100\)"],
        antwoord=0,
        uitleg=r"Wie door \(4\) deelbaar is, is een veelvoud van \(4\), en elk veelvoud van \(4\) is "
               r"ook een veelvoud van \(2\). Bijvoorbeeld \(12\): \(12 : 4 = 3\) en \(12 : 2 = 6\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Als een getal deelbaar is door \(2\), dan is het deelbaar door \(4\).” Welk getal "
              r"toont aan dat dit niet klopt?",
        opties=[r"\(6\)", r"\(8\)", r"\(12\)"],
        antwoord=0,
        uitleg=r"\(6\) is deelbaar door \(2\) maar niet door \(4\). Dat ene getal volstaat als "
               r"tegenvoorbeeld. \(8\) en \(12\) zijn door allebei deelbaar en weerleggen dus niets.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent het pijltje \(\Rightarrow\) in \(a \Rightarrow b\)?",
        opties=[r"Als \(a\) waar is, dan is \(b\) waar", r"\(a\) en \(b\) zijn hetzelfde",
                r"\(a\) is groter dan \(b\)"],
        antwoord=0,
        uitleg=r"\(\Rightarrow\) is de als-dan-pijl, de implicatie. \(a \Rightarrow b\) lees je als: "
               r"als \(a\), dan \(b\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent de dubbele pijl \(\Leftrightarrow\)?",
        opties=[
            "Het een geldt precies wanneer het ander geldt",
            "Het een volgt uit het ander, maar niet omgekeerd",
            "De twee kanten zijn even groot",
        ],
        antwoord=0,
        uitleg=r"\(\Leftrightarrow\) is de als-en-slechts-als-pijl, de equivalentie: het geldt in "
               r"allebei de richtingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vierkant is altijd een rechthoek.",
        antwoord=True,
        uitleg="Juist. Een rechthoek is een vierhoek met vier rechte hoeken, en dat heeft een vierkant "
               "ook. Een vierkant heeft daarbovenop vier gelijke zijden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechthoek is altijd een vierkant.",
        antwoord=False,
        uitleg=r"Nee. Een rechthoek van \(3\) bij \(5\) heeft vier rechte hoeken maar geen vier "
               r"gelijke zijden. Dat is meteen het tegenvoorbeeld. Let op de richting: de ene "
               r"uitspraak klopt, de omgekeerde niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="„Alle priemgetallen zijn oneven.” Welk getal weerlegt dat?",
        opties=[r"\(2\)", r"\(9\)", r"\(15\)"],
        antwoord=0,
        uitleg=r"\(2\) is een priemgetal en even. \(9\) en \(15\) zijn wel oneven, maar geen "
               r"priemgetallen, dus die zeggen niets over deze uitspraak.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe schrijf je „\(x\) is kleiner dan of gelijk aan \(5\)”?",
        opties=[r"\(x \leq 5\)", r"\(x < 5\)", r"\(x \geq 5\)"],
        antwoord=0,
        uitleg=r"Het streepje onder het teken betekent „of gelijk aan”. \(x \leq 5\) laat \(5\) zelf "
               r"ook toe, \(x < 5\) niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Haakjes kunnen de uitkomst van een berekening veranderen.",
        antwoord=True,
        uitleg=r"Juist. \(2 + 3 \cdot 4 = 14\), maar \((2 + 3) \cdot 4 = 20\). Haakjes horen bij de "
               r"redenering en mag je niet zomaar weglaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="„Als het regent, is de straat nat.” Het regent niet. Wat weet je over de straat?",
        opties=[
            "Niets met zekerheid, ze kan nat zijn of droog",
            "Ze is zeker droog",
            "Ze is zeker nat",
        ],
        antwoord=0,
        uitleg="De als-dan zegt enkel iets over wat er gebeurt als het wél regent. De straat kan ook "
               "nat zijn door een sproeier. Zo'n omgekeerde redenering is een van de vaakst gemaakte "
               "fouten.",
    ),
    dict(
        type="meerkeuze",
        vraag="„Als een vierhoek vier gelijke zijden heeft, dan is het een vierkant.” Wat is hier het tegenvoorbeeld?",
        opties=["Een ruit die scheef staat", "Een rechthoek", "Een gelijkzijdige driehoek"],
        antwoord=0,
        uitleg="Een ruit heeft vier gelijke zijden maar geen rechte hoeken. Een driehoek is geen "
               "vierhoek en kan dus geen tegenvoorbeeld zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Vul aan: een uitspraak weerleg je met één … (één woord)",
        antwoord="tegenvoorbeeld",
        uitleg="Eén tegenvoorbeeld volstaat om een uitspraak die voor alle gevallen zou gelden, "
               "onderuit te halen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het product van twee even getallen is altijd even.",
        antwoord=True,
        uitleg=r"Juist. Elk even getal is een veelvoud van \(2\), dus hun product is zeker een "
               r"veelvoud van \(2\). Bijvoorbeeld \(4 \cdot 6 = 24\).",
    ),
    dict(
        type="waarofniet",
        vraag="Het product van twee oneven getallen is altijd even.",
        antwoord=False,
        uitleg=r"Nee. \(3 \cdot 5 = 15\), en dat is oneven. Dat ene geval weerlegt de uitspraak al.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke uitspraak geldt in allebei de richtingen, en verdient dus \(\Leftrightarrow\)?",
        opties=[
            r"Een getal eindigt op \(0\) \(\Leftrightarrow\) het is deelbaar door \(10\)",
            r"Een getal is deelbaar door \(2\) \(\Leftrightarrow\) het is deelbaar door \(6\)",
            r"Een vierhoek is een ruit \(\Leftrightarrow\) het is een vierkant",
        ],
        antwoord=0,
        uitleg=r"Eindigt een getal op \(0\), dan is het deelbaar door \(10\), en omgekeerd. Bij de "
               r"andere twee klopt maar één richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je tussenstappen op in een berekening?",
        opties=[
            "Zodat iemand anders kan nagaan waar een fout zit",
            "Omdat het netter oogt",
            "Omdat de uitkomst anders fout is",
        ],
        antwoord=0,
        uitleg="Een redenering moet te volgen zijn. Met tussenstappen kan je zelf en kan een ander "
               "zien welke stap klopt en welke niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Alle veelvouden van \(6\) zijn even.” Wat doe je om dit te illustreren?",
        opties=[
            r"Enkele veelvouden opschrijven: \(6,\ 12,\ 18,\ 24\)",
            "Een tegenvoorbeeld zoeken",
            "Zeggen dat het niet klopt",
        ],
        antwoord=0,
        uitleg=r"Bij een uitspraak die klopt, geef je ter illustratie een voorbeeld. Een "
               r"tegenvoorbeeld bestaat hier niet, want \(6\) is even en een veelvoud van een even "
               r"getal blijft even.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"„Als een getal deelbaar is door \(6\), dan is het deelbaar door \(3\).” En de omgekeerde uitspraak?",
        opties=[
            "De eerste klopt, de omgekeerde niet",
            r"Allebei kloppen, dus \(\Leftrightarrow\)",
            "Geen van beide klopt",
        ],
        antwoord=0,
        uitleg=r"Elk veelvoud van \(6\) is ook een veelvoud van \(3\). Omgekeerd niet: \(9\) is "
               r"deelbaar door \(3\) maar niet door \(6\). Dus wel \(\Rightarrow\), geen "
               r"\(\Leftrightarrow\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Iemand redeneert: „\(5 > 3\), dus \(-5 > -3\).” Waar zit de fout?",
        opties=[
            r"Bij negatieve getallen draait de volgorde om: \(-5 < -3\)",
            "Er is geen fout",
            "Je mag geen minteken voor een getal zetten",
        ],
        antwoord=0,
        uitleg=r"Het tegengestelde nemen keert de ongelijkheid om. \(-5\) ligt verder naar links dan "
               r"\(-3\), dus \(-5 < -3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Als \(a \cdot b = 0\), dan is \(a = 0\).” Wat is het tegenvoorbeeld?",
        opties=[r"\(a = 3\) en \(b = 0\)", r"\(a = 0\) en \(b = 0\)", r"\(a = 1\) en \(b = 1\)"],
        antwoord=0,
        uitleg=r"\(3 \cdot 0 = 0\), terwijl \(a\) niet nul is. Wat wél klopt: als \(a \cdot b = 0\), "
               r"dan is \(a = 0\) óf \(b = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag="Als je aan beide kanten van een ongelijkheid hetzelfde getal optelt, blijft ze kloppen.",
        antwoord=True,
        uitleg=r"Juist. Uit \(5 > 3\) volgt \(5 + 2 > 3 + 2\), dus \(7 > 5\). Optellen verschuift "
               r"allebei de kanten evenveel.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je beide kanten van een ongelijkheid met hetzelfde getal vermenigvuldigt, blijft ze kloppen.",
        antwoord=False,
        uitleg=r"Niet altijd. Uit \(5 > 3\) volgt bij maal \(-1\): \(-5\) en \(-3\), en \(-5 < -3\). "
               r"Bij een negatief getal draait het teken om. Dat is het tegenvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="„Als een vierhoek een vierkant is, dan heeft hij vier rechte hoeken.” Welke pijl hoort hier?",
        opties=[r"\(\Rightarrow\)", r"\(\Leftrightarrow\)", "Geen van beide"],
        antwoord=0,
        uitleg=r"Enkel \(\Rightarrow\). Omgekeerd geldt het niet: een rechthoek van \(3\) bij \(5\) "
               r"heeft vier rechte hoeken en is geen vierkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="„Het kwadraat van een getal is altijd groter dan het getal zelf.” Welk getal weerlegt dat?",
        opties=[r"\(0{,}5\)", r"\(2\)", r"\(10\)"],
        antwoord=0,
        uitleg=r"\(0{,}5 \cdot 0{,}5 = 0{,}25\), en dat is kleiner dan \(0{,}5\). Bij getallen tussen "
               r"\(0\) en \(1\) wordt het kwadraat juist kleiner. Ook \(0\) en \(1\) zijn "
               r"tegenvoorbeelden, want daar is het even groot.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Iemand schrijft: „\(12 : 4 : 2 = 12 : 2 = 6\)”. Wat ging er mis?",
        opties=[
            r"Delen gaat van links naar rechts: \(12 : 4 = 3\), dan \(3 : 2 = 1{,}5\)",
            "Niets, het klopt",
            "Je mag niet twee keer na elkaar delen",
        ],
        antwoord=0,
        uitleg=r"Delen is niet associatief. Wie eerst \(4 : 2\) doet, verandert de opgave. Binnen "
               r"dezelfde stap reken je van links naar rechts.",
    ),
    dict(
        type="waarofniet",
        vraag="Als twee driehoeken dezelfde oppervlakte hebben, zijn ze gelijk van vorm.",
        antwoord=False,
        uitleg=r"Nee. Een driehoek met basis \(6\) en hoogte \(2\) en een met basis \(3\) en hoogte "
               r"\(4\) hebben allebei oppervlakte \(6\), maar zien er heel anders uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="„Als twee getallen even zijn, is hun som even.” Hoe toon je dat aan voor álle even getallen?",
        opties=[r"Schrijf ze als \(2a\) en \(2b\): hun som is \(2(a + b)\), dus een veelvoud van \(2\)",
                r"Reken het na voor \(2 + 4\), \(6 + 8\) en \(10 + 12\): drie voorbeelden volstaan als bewijs",
                "Zeg dat het voor de hand ligt"],
        antwoord=0,
        uitleg="Met letters dek je alle gevallen in één keer. Voorbeelden illustreren wel, maar "
               "bewijzen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Een getal is deelbaar door \(3\) \(\Leftrightarrow\) de som van zijn cijfers is "
              r"deelbaar door \(3\).” Klopt de dubbele pijl?",
        opties=[
            "Ja, het geldt in allebei de richtingen",
            "Nee, enkel van links naar rechts",
            "Nee, enkel van rechts naar links",
        ],
        antwoord=0,
        uitleg=r"Dat is precies wat de deelbaarheidsregel zegt, en ze werkt beide kanten op. Bij "
               r"\(123\): \(1 + 2 + 3 = 6\), deelbaar door \(3\), en \(123 : 3 = 41\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Iemand redeneert: „\(10\,\%\) korting en dan nog eens \(10\,\%\) korting is samen "
              r"\(20\,\%\) korting.” Wat is er mis?",
        opties=[r"De tweede korting wordt van een kleiner bedrag genomen: samen is het \(19\,\%\)",
                "Niets, het klopt",
                "Je mag geen twee kortingen na elkaar geven, want een winkel rekent altijd één korting"],
        antwoord=0,
        uitleg=r"Van € \(100\) blijft na de eerste korting € \(90\) over, en \(10\,\%\) daarvan is "
               r"€ \(9\). Je betaalt € \(81\), dus de korting is \(19\,\%\). Percentages tel je niet "
               r"zomaar op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Uit \(a = b\) volgt \(a^{2} = b^{2}\).",
        antwoord=True,
        uitleg="Juist. Zijn twee getallen gelijk, dan zijn hun kwadraten dat ook.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Uit \(a^{2} = b^{2}\) volgt \(a = b\).",
        antwoord=False,
        uitleg=r"Nee. Neem \(a = 3\) en \(b = -3\): allebei in het kwadraat geeft \(9\), maar \(3\) "
               r"is niet \(-3\). De pijl werkt hier dus maar in één richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een voorbeeld en een bewijs?",
        opties=[
            "Een voorbeeld toont één geval, een bewijs dekt alle gevallen",
            "Een bewijs is een voorbeeld met meer cijfers",
            "Er is geen verschil",
        ],
        antwoord=0,
        uitleg="Daarom kan je met voorbeelden nooit bewijzen dat iets áltijd geldt, terwijl één "
               "tegenvoorbeeld wel genoeg is om het te weerleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Alle getallen die op \(5\) eindigen zijn deelbaar door \(5\).” En: „alle getallen "
              r"die deelbaar zijn door \(5\) eindigen op \(5\).”",
        opties=[
            "De eerste klopt, de tweede niet",
            "Allebei kloppen",
            "De tweede klopt, de eerste niet",
        ],
        antwoord=0,
        uitleg=r"\(10\) is deelbaar door \(5\) maar eindigt op \(0\). Dat is het tegenvoorbeeld bij "
               r"de tweede uitspraak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool gebruik je als iets in allebei de richtingen geldt?",
        opties=[r"\(\Leftrightarrow\)", r"\(\Rightarrow\)", r"\(=\)"],
        antwoord=0,
        uitleg=r"De dubbele pijl \(\Leftrightarrow\) staat voor als en slechts als: het geldt heen én "
               r"terug. De enkele pijl \(\Rightarrow\) geldt maar in één richting.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Iemand schrijft: „\(\sqrt{9 + 16} = \sqrt{9} + \sqrt{16} = 3 + 4 = 7\)”. Klopt dat?",
        opties=[r"Nee, \(\sqrt{25} = 5\). Een wortel mag je niet zo splitsen bij een som",
                "Ja, dat is de gewone rekenregel: een wortel mag je over een som verdelen",
                "Ja, maar enkel bij kwadraten"],
        antwoord=0,
        uitleg=r"Eerst het haakje: \(9 + 16 = 25\), en \(\sqrt{25} = 5\). Deze fout hoort bij het "
               r"soort redeneerstap dat je moet kunnen betrappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een redenering klopt in elke stap, maar de laatste zin beantwoordt een andere vraag dan er gesteld werd. Wat is je oordeel?",
        opties=["De redenering is niet af: het antwoord past niet bij de vraag",
                "Ze is juist, want elke stap klopt en dat is wat telt bij een redenering",
                "Ze is fout vanaf de eerste stap"],
        antwoord=0,
        uitleg="Een redenering beoordelen is meer dan de stappen nakijken. Ze moet ook uitkomen bij "
               "wat er gevraagd werd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"„Als een getal groter is dan \(10\), dan is het groter dan \(5\).” Welke pijl hoort hier, en waarom?",
        opties=[
            r"\(\Rightarrow\), want omgekeerd geldt het niet: \(7\) is groter dan \(5\) maar niet dan \(10\)",
            r"\(\Leftrightarrow\), want allebei gaan over grote getallen",
            "Geen pijl, want het zijn geen wiskundige uitspraken",
        ],
        antwoord=0,
        uitleg=r"Zoek bij elke als-dan altijd één getal dat de omgekeerde richting onderuithaalt. "
               r"Vind je er een, dan is het \(\Rightarrow\) en geen \(\Leftrightarrow\).",
    ),
]
