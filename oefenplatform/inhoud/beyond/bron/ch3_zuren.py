# -*- coding: utf-8 -*-
"""Zuren en basen volgens Brønsted-Lowry — 🌍 Beyond, chemie.

Deel 1 gaat over de begrippen: een zuur dat een proton afstaat en een base die
er een opneemt, het geconjugeerde paar, de amfolyt, de protolysereactie en de
waardigheid van een meerwaardig zuur of base. Deel 2 gaat over de sterkte: de
zuurconstante en de baseconstante, pKz en pKb, het verschil tussen een sterk en
een zwak zuur, de ionisatiegraad, en het zure, basische of neutrale karakter van
een oplossing van een zout.

Het rekenen met pH zit in een eigen thema. Hier gaat het om wat sterk en zwak
betekenen, en om wat je uit een constante kan afleiden zonder te rekenen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een zuur volgens Brønsted-Lowry?",
        opties=[
            "een stof die een proton kan afstaan",
            "een stof die een proton kan opnemen",
            "een stof die een elektronenpaar kan afstaan",
            "een stof die in water hydroxide-ionen vormt",
        ],
        antwoord=0,
        uitleg="Een proton is hier een H⁺-ion. Een base is net het omgekeerde: ze neemt "
        "dat proton op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een protolysereactie?",
        opties=[
            "een proton gaat van het zuur naar de base",
            "een elektron gaat van het zuur naar de base",
            "twee zuren wisselen hun zuurresten uit",
            "een zout valt uiteen in zijn twee ionen",
        ],
        antwoord=0,
        uitleg="Daarom heeft een protolyse altijd een zuur én een base nodig. Zonder "
        "iemand die het proton opneemt, gebeurt er niets.",
    ),
    dict(
        type="invultekst",
        vraag="Welk ion ontstaat er als water een proton opneemt?",
        antwoord=["hydroxoniumion", "H3O+", "hydroxonium"],
        uitleg="H₂O plus H⁺ geeft H₃O⁺. Daarom schrijft men de ionisatie van een zuur in "
        "water met het hydroxoniumion en niet met een los H⁺.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de geconjugeerde base van waterstofchloride, HCl?",
        opties=[
            "het chloride-ion",
            "het hydroxide-ion",
            "het hydroxoniumion",
            "het chloraation",
        ],
        antwoord=0,
        uitleg="Wat overblijft als het zuur zijn proton afstaat, is zijn geconjugeerde "
        "base. HCl wordt dus Cl⁻.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuur en zijn geconjugeerde base verschillen precies één proton van elkaar.",
        antwoord=True,
        uitleg="Azijnzuur CH₃COOH en het acetaation CH₃COO⁻ vormen zo'n paar. Meer "
        "verschil is er niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het geconjugeerde zuur van ammoniak, NH₃?",
        opties=[
            "het ammoniumion",
            "het nitraation",
            "het hydroxide-ion",
            "het nitrietion",
        ],
        antwoord=0,
        uitleg="Ammoniak neemt een proton op en wordt NH₄⁺. Dat ion kan het proton weer "
        "afstaan, en is dus een zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn amfolyten? Kruis alles aan wat juist is.",
        opties=[
            "water",
            "het waterstofcarbonaation",
            "het chloride-ion",
            "het ammoniumion",
        ],
        antwoord=[0, 1],
        uitleg="Een amfolyt kan een proton afstaan én opnemen. HCO₃⁻ kan naar CO₃²⁻ of "
        "naar H₂CO₃.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof die zowel als zuur als als base kan werken?",
        antwoord=["amfolyt", "een amfolyt", "amfoteer"],
        uitleg="Water is het bekendste voorbeeld: tegenover HCl is het een base, tegenover "
        "ammoniak een zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men zwavelzuur een tweewaardig zuur?",
        opties=[
            "het kan twee protonen afstaan, in twee stappen",
            "het bevat twee zuurstofatomen in zijn zuurrest",
            "het lost op in water met twee moleculen water",
            "het vormt met een base altijd twee verschillende zouten",
        ],
        antwoord=0,
        uitleg="Eerst H₂SO₄ naar HSO₄⁻, dan naar SO₄²⁻. De eerste stap is veel sterker dan "
        "de tweede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Water reageert met ammoniak. Welke rol speelt het water?",
        opties=[
            "het is het zuur en staat een proton af",
            "het is de base en neemt een proton op",
            "het is enkel het oplosmiddel en doet niet mee",
            "het is de katalysator van de reactie",
        ],
        antwoord=0,
        uitleg="NH₃ plus H₂O geeft NH₄⁺ plus OH⁻. Tegenover een sterkere base gedraagt "
        "water zich als een zuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof kan alleen zuur zijn als er een base aanwezig is die het proton opneemt.",
        antwoord=True,
        uitleg="Zuiver zwavelzuur zonder water ioniseert niet. Pas met water erbij komt "
        "de protolyse op gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke paren zijn een zuur met zijn geconjugeerde base? Kruis alles aan wat juist is.",
        opties=[
            "H₂CO₃ en HCO₃⁻",
            "NH₄⁺ en NH₃",
            "HCl en HClO",
            "H₂O en H₃O⁺",
        ],
        antwoord=[0, 1],
        uitleg="Een paar verschilt precies één proton, met het zuur als het deeltje dat "
        "er één meer heeft. H₂O en H₃O⁺ is dus een paar met water als base.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel protonen kan fosforzuur H₃PO₄ in totaal afstaan?",
        antwoord=["drie", "3"],
        uitleg="Het is een driewaardig zuur: H₃PO₄, H₂PO₄⁻ en HPO₄²⁻ staan elk één proton "
        "af. De laatste stap is de zwakste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een meerwaardige base?",
        opties=[
            "ze kan meer dan één proton opnemen",
            "ze bevat meer dan één metaalatoom",
            "ze lost in water altijd volledig op",
            "ze vormt met elk zuur hetzelfde zout",
        ],
        antwoord=0,
        uitleg="Het carbonaation CO₃²⁻ kan er twee opnemen: eerst naar HCO₃⁻, dan naar "
        "H₂CO₃.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het hydroxide-ion zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het neemt een proton op en wordt water",
            "het is de geconjugeerde base van water",
            "het staat een proton af en wordt zuurstof",
            "het is het geconjugeerde zuur van water",
        ],
        antwoord=[0, 1],
        uitleg="Water kan een proton afstaan en wordt dan OH⁻. Omgekeerd neemt OH⁻ een "
        "proton op en wordt het weer water.",
    ),
    dict(
        type="waarofniet",
        vraag="In de reactie van azijnzuur met water is het water het zuur.",
        antwoord=False,
        uitleg="Azijnzuur staat het proton af, dus is dat het zuur. Water neemt het op en "
        "is hier de base.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een amfolyt komt in water terecht. Hoe weet je welke reactie het meest waarschijnlijk is?",
        opties=[
            "je vergelijkt zijn zuurconstante met zijn baseconstante",
            "je kijkt welke reactie het snelste op gang komt",
            "je kijkt hoeveel protonen het deeltje in totaal heeft",
            "je vergelijkt zijn molaire massa met die van water",
        ],
        antwoord=0,
        uitleg="Is Kz groter dan Kb, dan gedraagt het deeltje zich vooral als zuur. Bij "
        "HCO₃⁻ is het omgekeerd, en daarom is bakpoeder in water lichtbasisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof kan geen base zijn volgens Brønsted-Lowry?",
        opties=[
            "het hydroxoniumion",
            "het ammoniakmolecule",
            "het carbonaation",
            "het hydroxide-ion",
        ],
        antwoord=0,
        uitleg="H₃O⁺ heeft al een proton te veel en staat het liever af. Het is dus het "
        "sterkste zuur dat in water kan bestaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een base moet altijd een hydroxidegroep bevatten.",
        antwoord=False,
        uitleg="Volgens Brønsted-Lowry niet: ammoniak heeft geen OH en is toch een base, "
        "want ze neemt een proton op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de twee deeltjes die precies één proton van elkaar verschillen?",
        antwoord=["geconjugeerd paar", "een geconjugeerd paar", "zuurbasekoppel"],
        uitleg="Het deeltje met het extra proton is het zuur, het andere de base. Elke "
        "protolyse heeft twee zulke paren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een sterk zuur in water?",
        opties=[
            "het staat zijn proton zo goed als volledig af",
            "het staat maar een klein deel van zijn protonen af",
            "het heeft altijd meer dan één proton af te staan",
            "het reageert heel snel met elke andere stof",
        ],
        antwoord=0,
        uitleg="Zoutzuur is in water bijna volledig geïoniseerd. Azijnzuur maar voor een "
        "paar procent, en dat is dus een zwak zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je de zuurconstante van een zuur HA in water?",
        opties=[
            "Kz is [H₃O⁺] maal [A⁻] gedeeld door [HA]",
            "Kz is [HA] gedeeld door [H₃O⁺] maal [A⁻]",
            "Kz is [H₃O⁺] gedeeld door [A⁻] maal [HA]",
            "Kz is [A⁻] gedeeld door [HA] maal [H₃O⁺]",
        ],
        antwoord=0,
        uitleg="Het is gewoon de evenwichtsconstante van de protolyse met water. Het "
        "water zelf staat er niet in, want het is in overmaat.",
    ),
    dict(
        type="invultekst",
        vraag="Wat betekent een kleine pKz-waarde voor een zuur?",
        antwoord=["sterk zuur", "sterk", "het is sterk"],
        uitleg="pKz is de negatieve logaritme van Kz. Een grote Kz hoort dus bij een "
        "kleine pKz, en dat is een sterk zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je over de geconjugeerde base van een sterk zuur?",
        opties=[
            "ze is een heel zwakke base",
            "ze is zelf ook een sterke base",
            "ze reageert niet met water of met een zuur",
            "ze heeft dezelfde constante als het zuur",
        ],
        antwoord=0,
        uitleg="Het chloride-ion neemt bijna nooit een proton terug op. Daarom is een "
        "oplossing van keukenzout neutraal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sterk zuur en een geconcentreerd zuur betekenen hetzelfde.",
        antwoord=False,
        uitleg="Sterk gaat over hoe goed het ioniseert, geconcentreerd over hoeveel mol "
        "er per liter in zit. Verdund zoutzuur blijft een sterk zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de ionisatiegraad van een zuur?",
        opties=[
            "het deel van de moleculen dat zijn proton heeft afgestaan",
            "het aantal protonen dat één molecule kan afstaan",
            "de hoeveelheid zuur die je per liter water kan oplossen",
            "het verschil tussen de pH en de pKz van het zuur",
        ],
        antwoord=0,
        uitleg="Bij een sterk zuur ligt die graad bij honderd procent, bij een zwak zuur "
        "veel lager. Verdunnen maakt de ionisatiegraad groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zuren zijn sterke zuren? Kruis alles aan wat juist is.",
        opties=[
            "zoutzuur",
            "salpeterzuur",
            "azijnzuur",
            "koolzuur",
        ],
        antwoord=[0, 1],
        uitleg="HCl en HNO₃ ioniseren zo goed als volledig. Azijnzuur en koolzuur zijn "
        "zwakke zuren en blijven grotendeels als molecule in de oplossing.",
    ),
    dict(
        type="invultekst",
        vraag="Welk toestel meet de pH van een oplossing nauwkeurig?",
        antwoord=["pH-meter", "een pH-meter", "pHmeter"],
        uitleg="Een indicator geeft maar een gebied, een pH-meter een getal. Je ijkt ze "
        "eerst met bufferoplossingen van bekende pH.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een zuurbase-indicator?",
        opties=[
            "het is zelf een zwak zuur waarvan de twee vormen anders gekleurd zijn",
            "het is een sterk zuur dat van kleur verandert bij verdunnen",
            "het meet de elektrische geleidbaarheid van de oplossing",
            "het reageert met het zout dat bij de neutralisatie ontstaat",
        ],
        antwoord=0,
        uitleg="Het geconjugeerde paar van de indicator heeft twee kleuren. Welke je "
        "ziet, hangt af van de pH rond het omslaggebied.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het omslaggebied van een indicator zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het ligt rond de pKz van de indicator",
            "het beslaat ongeveer twee pH-eenheden",
            "het ligt altijd precies bij pH 7",
            "het is voor elke indicator hetzelfde",
        ],
        antwoord=[0, 1],
        uitleg="Fenolftaleïen slaat om rond pH 9, methyloranje rond pH 4. Daarom kies je "
        "je indicator bij de titratie die je doet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oplossing van keukenzout in water is neutraal.",
        antwoord=True,
        uitleg="Na⁺ en Cl⁻ komen van een sterke base en een sterk zuur. Geen van de twee "
        "reageert nog met water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een oplossing van natriumacetaat basisch?",
        opties=[
            "het acetaation is de geconjugeerde base van een zwak zuur",
            "het natriumion neemt protonen op uit het water",
            "het acetaation staat protonen af aan het water",
            "het zout reageert met water tot natriumhydroxide",
        ],
        antwoord=0,
        uitleg="Omdat azijnzuur zwak is, is zijn geconjugeerde base sterk genoeg om een "
        "proton van water af te pakken. Daarbij ontstaat OH⁻.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een oplossing van ammoniumchloride zuur?",
        opties=[
            "het ammoniumion staat een proton af aan het water",
            "het chloride-ion neemt een proton op uit het water",
            "het zout vormt met water zoutzuur en ammoniak",
            "het ammoniumion neemt hydroxide-ionen weg uit het water",
        ],
        antwoord=0,
        uitleg="NH₄⁺ is het geconjugeerde zuur van de zwakke base ammoniak. Daardoor "
        "ontstaat er wat H₃O⁺ in de oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oplossingen van een zout zijn neutraal? Kruis alles aan wat juist is.",
        opties=[
            "natriumchloride in water",
            "kaliumnitraat in water",
            "natriumcarbonaat in water",
            "ammoniumchloride in water",
        ],
        antwoord=[0, 1],
        uitleg="Beide ionen komen van een sterk zuur en een sterke base. Soda is basisch "
        "en ammoniumchloride zuur.",
    ),
    dict(
        type="invultekst",
        vraag="Welke constante hoort bij een base in water?",
        antwoord=["baseconstante", "Kb", "de baseconstante"],
        uitleg="Kb heeft dezelfde vorm als Kz, met het hydroxide-ion in de teller. Voor "
        "een geconjugeerd paar geldt Kz maal Kb is de constante van water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee zuren hebben pKz 3 en pKz 5. Wat weet je?",
        opties=[
            "het zuur met pKz 3 is het sterkste van de twee",
            "het zuur met pKz 5 is het sterkste van de twee",
            "de twee zuren zijn even sterk in water",
            "het zuur met pKz 5 ioniseert volledig in water",
        ],
        antwoord=0,
        uitleg="Hoe kleiner pKz, hoe groter Kz en hoe sterker het zuur. Twee eenheden "
        "verschil in pKz is een factor honderd in Kz.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee zuren met dezelfde concentratie, één sterk en één zwak. Wat verschilt?",
        opties=[
            "de pH van de twee oplossingen",
            "het aantal mol zuur per liter",
            "de waardigheid van de twee zuren",
            "de massa zuur die je afgewogen hebt",
        ],
        antwoord=0,
        uitleg="Het sterke zuur geeft veel meer hydroxoniumionen, dus een lagere pH. De "
        "concentratie van het zuur zelf is gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor een geconjugeerd paar geldt: hoe sterker het zuur, hoe zwakker zijn base.",
        antwoord=True,
        uitleg="Het product van Kz en Kb is altijd de ionisatieconstante van water. Wordt "
        "de ene groter, dan moet de andere kleiner worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwak zuur kan nooit een lage pH geven, hoe geconcentreerd het ook is.",
        antwoord=False,
        uitleg="Bij een hoge concentratie geeft ook een zwak zuur genoeg "
        "hydroxoniumionen voor een lage pH. Azijn is daarvan een voorbeeld.",
    ),
    dict(
        type="invultekst",
        vraag="Welke indicator is kleurloos in zuur en roze in basisch midden?",
        antwoord=["fenolftaleïen", "fenolftaleine", "fenolftaleïne"],
        uitleg="Haar omslag ligt rond pH 9. Daarom past ze goed bij de titratie van een "
        "zwak zuur met een sterke base.",
    ),
]
