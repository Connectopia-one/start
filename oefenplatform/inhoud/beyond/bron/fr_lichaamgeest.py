# -*- coding: utf-8 -*-
"""Lichaam en geest: monisme en dualisme.

Het vierde van twaalf thema's over filosofie, en het eerste van vier over
wijsgerige antropologie: de filosofie van de mens.

De lijstjes staan letterlijk in de fiche:

    de basisideeën van filosofen die bijdroegen aan het debat over lichaam en
        geest: Plato, Aristoteles, René Descartes, Parmenides, Benedictus de
        Spinoza
    de monistische en de dualistische mensvisie uitleggen
    die twee vergelijken en de gelijkenissen en verschillen benoemen
    westerse visies over lichaam en geest vergelijken met niet-westerse visies

Bij de niet-westerse visies noemt de fiche geen tradities bij naam. De vragen
hieronder blijven daarom bij wat algemeen vaststaat: dat de scheiding tussen
lichaam en geest in veel niet-westerse tradities minder scherp is of ontbreekt,
en dat het boeddhisme geen vast, blijvend zelf kent. Er is geen school, tekst
of leraar genoemd die de fiche niet noemt.

Deel 1 zijn de begrippen monisme en dualisme, met Parmenides, Plato en
Aristoteles.
Deel 2 zijn Descartes en Spinoza, de vergelijking, en de niet-westerse visies.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Wat houdt een dualistische mensvisie in?",
         opties=["de mens bestaat uit twee werkelijkheden: een lichaam en een geest",
                 "de mens bestaat uit één werkelijkheid, waarvan geest een kant is",
                 "de mens bestaat enkel uit materie en verder niets",
                 "de mens bestaat uit drie delen: lichaam, geest en ziel"],
         antwoord=0,
         uitleg="Dualisme komt van duo: twee. Lichaam en geest zijn er twee soorten "
                "werkelijkheid, en de ene is niet tot de andere terug te brengen."),
    dict(type="meerkeuze",
         vraag="Wat houdt een monistische mensvisie in?",
         opties=["er is maar één werkelijkheid, en lichaam en geest horen er beide bij",
                 "er zijn twee gescheiden werkelijkheden die op elkaar inwerken",
                 "de geest bestaat wel en het lichaam is een illusie",
                 "elke mens heeft één eigen werkelijkheid, verschillend van die van anderen"],
         antwoord=0,
         uitleg="Monisme komt van monos: één. Er is één werkelijkheid; lichaam en geest zijn geen "
                "twee aparte soorten zijn."),
    dict(type="meerkeuze",
         vraag="Wat is de kern van het denken van Parmenides?",
         opties=["het zijnde is één en onveranderlijk; verandering is schijn",
                 "alles stroomt voortdurend, en niets blijft ooit hetzelfde",
                 "de ziel is onsterfelijk en het lichaam vergankelijk",
                 "kennis komt uitsluitend uit de zintuigen"],
         antwoord=0,
         uitleg="Parmenides staat in deze fiche voor het monisme in zijn strengste vorm: er is "
                "één zijn, en wat op verandering lijkt, misleidt ons."),
    dict(type="meerkeuze",
         vraag="Waarom hoort Parmenides in dit thema thuis?",
         opties=["hij is het vroege voorbeeld van een monistische visie",
                 "hij scheidde als eerste het lichaam van de geest",
                 "hij toonde aan dat de ziel sterfelijk is",
                 "hij bedacht het woord dualisme"],
         antwoord=0,
         uitleg="De fiche zet hem in de rij van filosofen over lichaam en geest omdat hij de "
                "eenheid van het zijnde verdedigt."),
    dict(type="meerkeuze",
         vraag="Hoe ziet Plato de verhouding tussen lichaam en ziel?",
         opties=["de ziel staat los van het lichaam en is onsterfelijk",
                 "de ziel is de vorm van het lichaam en gaat er niet van los",
                 "de ziel en het lichaam zijn twee kanten van één werkelijkheid",
                 "de ziel bestaat niet; er is enkel een lichaam"],
         antwoord=0,
         uitleg="Plato is een dualist: de ziel is van een andere orde dan het lichaam en blijft "
                "bestaan als het lichaam vergaat."),
    dict(type="meerkeuze",
         vraag="Welke vergelijking past bij de visie van Plato op het lichaam?",
         opties=["het lichaam als een gevangenis waarin de ziel verblijft",
                 "het lichaam als de vorm die de ziel in zich aanneemt",
                 "het lichaam als de enige werkelijkheid die er is",
                 "het lichaam als een machine zonder bestuurder"],
         antwoord=0,
         uitleg="Bij Plato hoort de ziel bij een hogere werkelijkheid en zit ze in het lichaam "
                "vast. Dat past bij de grotallegorie uit de kennisleer."),
    dict(type="meerkeuze",
         vraag="Hoe ziet Aristoteles de verhouding tussen lichaam en ziel?",
         opties=["de ziel is de vorm van het lichaam en bestaat er niet los van",
                 "de ziel is een aparte stof die in het lichaam gevangen zit",
                 "de ziel bestaat niet; alles is beweging van materie",
                 "de ziel is onsterfelijk en reist van lichaam naar lichaam"],
         antwoord=0,
         uitleg="Bij Aristoteles horen de twee samen zoals de vorm bij de stof: je kan ze "
                "onderscheiden maar niet scheiden."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over Plato en Aristoteles kloppen?",
         opties=["Plato houdt de ziel los van het lichaam, Aristoteles niet",
                 "beiden spreken over een ziel, maar met een ander verband met het lichaam",
                 "beiden vinden dat de ziel het lichaam overleeft",
                 "Aristoteles ontkent dat er zoiets als een ziel is"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Aristoteles ontkent de ziel niet, hij maakt haar onlosmakelijk "
                "met het lichaam verbonden."),
    dict(type="meerkeuze",
         vraag="Een vriend zegt: mijn lichaam is gewoon het voertuig waarin ik rondrijd. Welke "
               "visie hoor je?",
         opties=["een dualistische visie", "een monistische visie",
                 "de visie van Aristoteles", "de visie van Spinoza"],
         antwoord=0,
         uitleg="Wie zichzelf van zijn lichaam onderscheidt als bestuurder van een voertuig, "
                "spreekt dualistisch."),
    dict(type="meerkeuze",
         vraag="Een arts zegt: je sombere stemming komt van een tekort in je schildklier. Welke "
               "visie hoor je?",
         opties=["een monistische visie: het geestelijke is niet los van het lichamelijke",
                 "een dualistische visie: lichaam en geest staan volledig los van elkaar",
                 "de visie van Plato over de onsterfelijke ziel",
                 "een visie waarin de geest het lichaam bestuurt"],
         antwoord=0,
         uitleg="Hier wordt iets geestelijks verklaard uit iets lichamelijks. Dat kan alleen als "
                "de twee niet van elkaar gescheiden zijn."),
    dict(type="meerkeuze",
         vraag="Wat hebben een monist en een dualist met elkaar gemeen?",
         opties=["beiden willen verklaren hoe denken en lichaam met elkaar samenhangen",
                 "beiden geloven in een onsterfelijke ziel",
                 "beiden vinden dat de geest belangrijker is dan het sterfelijke lichaam",
                 "beiden ontkennen dat de mens een lichaam heeft"],
         antwoord=0,
         uitleg="De vraag is dezelfde. Ze geven er een ander antwoord op: één werkelijkheid of "
                "twee."),
    dict(type="meerkeuze",
         vraag="Waarom is de vraag naar lichaam en geest een filosofische vraag en geen medische?",
         opties=["geen enkele meting kan beslissen of geest en lichaam één of twee zijn",
                 "artsen hebben er nog nooit onderzoek naar gedaan",
                 "de hersenen zijn veel te ingewikkeld om ooit volledig te onderzoeken",
                 "de vraag gaat over de toekomst en niet over het heden"],
         antwoord=0,
         uitleg="Hersenonderzoek laat zien dát er samenhang is; of geest daarmee hetzelfde is als "
                "brein, is een vraag over begrippen."),
    dict(type="waarofniet",
         vraag="Monisme komt van het woord voor één, dualisme van het woord voor twee.",
         antwoord=True,
         uitleg="Waar. Monos is één en duo is twee: dat is meteen het verschil tussen de twee "
                "mensvisies."),
    dict(type="waarofniet",
         vraag="Volgens Plato gaat de ziel verloren zodra het lichaam sterft.",
         antwoord=False,
         uitleg="Niet waar. Bij Plato is de ziel juist onsterfelijk; ze staat los van het "
                "vergankelijke lichaam."),
    dict(type="waarofniet",
         vraag="Volgens Aristoteles kan de ziel los van het lichaam bestaan.",
         antwoord=False,
         uitleg="Niet waar. Bij hem is de ziel de vorm van het lichaam: je kan ze onderscheiden, "
                "maar niet scheiden."),
    dict(type="waarofniet",
         vraag="Parmenides verdedigt dat het zijnde één en onveranderlijk is.",
         antwoord=True,
         uitleg="Waar. Daarom staat hij in deze fiche als het vroege voorbeeld van het monisme."),
    dict(type="invultekst",
         vraag="Hoe heet de mensvisie die lichaam en geest als twee werkelijkheden ziet?",
         antwoord=["dualisme", "het dualisme"],
         uitleg="Dualisme komt van duo: twee."),
    dict(type="invultekst",
         vraag="Hoe heet de mensvisie die maar één werkelijkheid aanneemt?",
         antwoord=["monisme", "het monisme"],
         uitleg="Monisme komt van monos: één."),
    dict(type="invultekst",
         vraag="Welke filosoof noemt de ziel de vorm van het lichaam?",
         antwoord=["Aristoteles"],
         uitleg="Bij Aristoteles horen vorm en stof samen; de ziel bestaat niet los van het "
                "lichaam."),
    dict(type="invultekst",
         vraag="Welke filosoof uit de oudheid ziet de ziel als onsterfelijk en het lichaam als "
               "haar gevangenis?",
         antwoord=["Plato"],
         uitleg="Plato is in dit thema het voorbeeld van het dualisme."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Wat is de kern van het dualisme van René Descartes?",
         opties=["denken en uitgebreidheid zijn twee verschillende soorten werkelijkheid",
                 "denken en uitgebreidheid zijn twee kanten van dezelfde werkelijkheid",
                 "er bestaat alleen denken, en materie is een illusie",
                 "er bestaat alleen materie, en denken is een illusie"],
         antwoord=0,
         uitleg="Bij Descartes is er een denkende werkelijkheid en een uitgebreide, stoffelijke "
                "werkelijkheid. Dat is het bekendste dualisme uit de filosofie."),
    dict(type="meerkeuze",
         vraag="Welk probleem levert het dualisme van Descartes op?",
         opties=["als denken en lichaam zo verschillend zijn, hoe kunnen ze dan op elkaar "
                 "inwerken?",
                 "als denken en lichaam één zijn, waarom voelen die twee dan toch verschillend?",
                 "als er maar één werkelijkheid is, wie neemt die dan waar?",
                 "als de ziel onsterfelijk is, waarom sterft het lichaam dan?"],
         antwoord=0,
         uitleg="Dat heet het interactieprobleem. Je beslist om op te staan en je benen bewegen: "
                "hoe raakt een gedachte aan een spier?"),
    dict(type="meerkeuze",
         vraag="Hoe sluit het dualisme van Descartes aan bij zijn methodische twijfel?",
         opties=["hij kan aan zijn lichaam twijfelen maar niet aan zijn denken",
                 "hij kan aan zijn denken twijfelen maar niet aan zijn lichaam",
                 "hij kan aan beide twijfelen en besluit dat niets bestaat",
                 "hij kan aan geen van beide twijfelen en besluit dat alles bestaat"],
         antwoord=0,
         uitleg="Dat zijn denken bestaat, staat voor hem vast; over zijn lichaam en de buitenwereld "
                "kan hij zich vergissen. Zo komen de twee werkelijkheden uit elkaar te liggen."),
    dict(type="meerkeuze",
         vraag="Wat is de kern van de visie van Benedictus de Spinoza?",
         opties=["er is één werkelijkheid, en denken en uitgebreidheid zijn er twee kanten van",
                 "er zijn twee aparte werkelijkheden die elkaar op geen enkele manier raken",
                 "de geest bestuurt het lichaam als een stuurman zijn schip",
                 "het lichaam is een gevangenis waarin de ziel wacht"],
         antwoord=0,
         uitleg="Spinoza is een monist: wat Descartes in twee knipt, is bij hem één werkelijkheid "
                "die je op twee manieren kan bekijken."),
    dict(type="meerkeuze",
         vraag="Welk probleem van Descartes lost Spinoza daarmee op?",
         opties=["het interactieprobleem, want er is niets meer dat op elkaar moet inwerken",
                 "het demarcatieprobleem, want hij geeft een maatstaf voor echte wetenschap",
                 "het is-ought probleem, want hij leidt een norm uit een feit af",
                 "het probleem van de inductie, want hij vertrekt van de rede"],
         antwoord=0,
         uitleg="Als denken en lichaam twee kanten van hetzelfde zijn, hoeft er geen brug meer "
                "tussen twee werelden gebouwd te worden."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over Descartes en Spinoza kloppen?",
         opties=["Descartes is een dualist en Spinoza een monist",
                 "beiden spreken over denken en over uitgebreidheid",
                 "beiden nemen twee gescheiden werkelijkheden aan",
                 "Spinoza ontkent dat mensen kunnen denken"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Ze gebruiken dezelfde twee begrippen en verschillen over de "
                "vraag of die twee werkelijkheden zijn of twee kanten van één."),
    dict(type="meerkeuze",
         vraag="Zet de vier filosofen op de juiste kant. Wie zijn de monisten?",
         opties=["Parmenides en Spinoza", "Plato en Descartes",
                 "Plato en Spinoza", "Parmenides en Descartes"],
         antwoord=0,
         uitleg="Parmenides en Spinoza nemen één werkelijkheid aan; Plato en Descartes nemen er "
                "twee. Aristoteles leunt met zijn vorm-en-stof dicht bij de monistische kant aan."),
    dict(type="meerkeuze",
         vraag="Wat is kenmerkend voor veel niet-westerse visies op lichaam en geest?",
         opties=["de scheiding tussen lichaam en geest is er minder scherp of ontbreekt",
                 "de scheiding tussen lichaam en geest is er juist veel scherper",
                 "er wordt enkel over het lichaam gesproken en nooit over de geest",
                 "er wordt enkel over de geest gesproken en nooit over het lichaam"],
         antwoord=0,
         uitleg="Waar het westerse denken de twee graag uit elkaar legt, zien veel andere "
                "tradities mens, lichaam en omgeving als één samenhangend geheel."),
    dict(type="meerkeuze",
         vraag="Wat zegt het boeddhisme over het zelf?",
         opties=["er is geen vast, blijvend zelf; wat jij bent, is voortdurend in verandering",
                 "het zelf is een onveranderlijke ziel die het lichaam overleeft",
                 "het zelf is hetzelfde als het lichaam en niets meer",
                 "het zelf is een illusie die niemand ooit ervaart"],
         antwoord=0,
         uitleg="Dat is een van de scherpste verschillen met de westerse zielsopvatting: geen "
                "vaste kern, wel een voortdurend veranderend geheel."),
    dict(type="meerkeuze",
         vraag="Waarom is het nuttig om westerse en niet-westerse visies naast elkaar te leggen?",
         opties=["je ziet dan dat de westerse indeling zelf een keuze is en niet vanzelfsprekend",
                 "je kan dan beslissen welke traditie de juiste is",
                 "je hoeft de westerse visies dan niet meer te kennen",
                 "je kan dan meten welke visie het dichtst bij de hersenen staat"],
         antwoord=0,
         uitleg="Precies dat is de winst van de vergelijking: wat vanzelfsprekend leek, blijkt één "
                "mogelijke manier om de mens te bekijken."),
    dict(type="meerkeuze",
         vraag="Een therapeut zegt: je rugpijn en je spanning op het werk kan je niet los van "
               "elkaar behandelen. Welke visie past daarbij?",
         opties=["een monistische visie", "een dualistische visie",
                 "de visie van Plato", "de visie van Descartes"],
         antwoord=0,
         uitleg="Wie het lichamelijke en het geestelijke als één geheel behandelt, denkt "
                "monistisch."),
    dict(type="meerkeuze",
         vraag="Waarom blijft het debat over lichaam en geest ook vandaag open?",
         opties=["hersenonderzoek toont samenhang, maar niet of geest hetzelfde ís als brein",
                 "er is nog te weinig hersenonderzoek gedaan om iets te kunnen zeggen",
                 "filosofen weigeren de uitkomsten van hersenonderzoek te lezen",
                 "het debat is al beslecht, maar niemand wil dat toegeven"],
         antwoord=0,
         uitleg="Samenhang aantonen is iets anders dan identiteit aantonen. Die stap is een "
                "filosofische stap, geen meting."),
    dict(type="waarofniet",
         vraag="Het interactieprobleem is het bezwaar dat twee zo verschillende werkelijkheden "
               "moeilijk op elkaar kunnen inwerken.",
         antwoord=True,
         uitleg="Waar. Het is het klassieke bezwaar tegen het dualisme van Descartes."),
    dict(type="waarofniet",
         vraag="Spinoza neemt net als Descartes twee gescheiden werkelijkheden aan.",
         antwoord=False,
         uitleg="Niet waar. Bij Spinoza is er één werkelijkheid; denken en uitgebreidheid zijn er "
                "twee kanten van."),
    dict(type="waarofniet",
         vraag="In veel niet-westerse tradities is de scheiding tussen lichaam en geest minder "
               "scherp dan in het westerse denken.",
         antwoord=True,
         uitleg="Waar. Mens, lichaam en omgeving worden er vaker als één samenhangend geheel "
                "gezien."),
    dict(type="waarofniet",
         vraag="Het boeddhisme kent een vast, onveranderlijk zelf dat het lichaam overleeft.",
         antwoord=False,
         uitleg="Niet waar. Juist niet: er is geen vaste kern, wel een voortdurend veranderend "
                "geheel."),
    dict(type="invultekst",
         vraag="Welke filosoof uit dit thema is de bekendste dualist?",
         antwoord=["Descartes", "René Descartes"],
         uitleg="Descartes scheidt het denken van de uitgebreide, stoffelijke werkelijkheid."),
    dict(type="invultekst",
         vraag="Welke filosoof maakt van denken en uitgebreidheid twee kanten van één "
               "werkelijkheid?",
         antwoord=["Spinoza", "Benedictus de Spinoza"],
         uitleg="Spinoza is in dit thema het voorbeeld van het monisme in de nieuwe tijd."),
    dict(type="invultekst",
         vraag="Hoe heet het bezwaar dat twee gescheiden werkelijkheden elkaar moeilijk kunnen "
               "raken? Het ...",
         antwoord=["interactieprobleem"],
         uitleg="Het klassieke bezwaar tegen het dualisme."),
    dict(type="invultekst",
         vraag="Welke traditie kent geen vast, blijvend zelf?",
         antwoord=["het boeddhisme", "boeddhisme"],
         uitleg="Dat is een van de scherpste verschillen met de westerse zielsopvatting."),
]
