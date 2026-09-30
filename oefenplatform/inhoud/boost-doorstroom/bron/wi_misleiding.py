# -*- coding: utf-8 -*-
"""De vragen voor "Misleiding met cijfers, en verbanden in een puntenwolk".

Uit de bouwsteen Data en onzekerheid: kritisch kijken naar statistische
informatie. Procent tegenover procentpunt, assen die ongepast geschaald of
foutief geijkt zijn, vervorming door een tekening in drie dimensies, gegevens
die weggelaten worden, en de keuze tussen mediaan en gemiddelde.

Daarnaast het verband tussen twee variabelen: het spreidingsdiagram, de
trendlijn, de correlatiecoëfficiënt, en het onderscheid tussen een sterke
correlatie en een oorzaak-gevolgrelatie.

Deel 1 is de misleiding. Deel 2 is de puntenwolk.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Een partij gaat van 20 naar 25 procent van de stemmen. Met hoeveel procentpunt is ze gegroeid?",
        opties=["5 procentpunt", "25 procentpunt", "5 procent", "20 procentpunt"],
        antwoord=0,
        uitleg="Procentpunt is het gewone verschil tussen twee percentages: 25 min 20.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde partij gaat van 20 naar 25 procent. Met hoeveel procent is ze gegroeid?",
        opties=["25 procent", "5 procent", "20 procent", "125 procent"],
        antwoord=0,
        uitleg="De groei van 5 gedeeld door de beginwaarde 20 geeft een kwart erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijft een krant liever dat een partij met 25 procent groeide dan met 5 procentpunt?",
        opties=[
            "het getal klinkt veel indrukwekkender terwijl de groei dezelfde is",
            "procentpunt is een verouderde term die vandaag niemand nog gebruikt",
            "het is de enige juiste manier om groei uit te drukken",
            "procenten zijn altijd nauwkeuriger dan procentpunten",
        ],
        antwoord=0,
        uitleg="Allebei de getallen kloppen, maar ze zeggen iets anders. Lees altijd welk van de twee er staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je met de verticale as een klein verschil groot laten lijken?",
        opties=[
            "de as niet bij nul laten beginnen maar vlak onder de laagste waarde",
            "de as bij nul laten beginnen en hem daarna ruim laten doorlopen",
            "de staven smaller tekenen dan gewoonlijk",
            "de waarden op de as in een andere kleur zetten",
        ],
        antwoord=0,
        uitleg="Een staafje van 98 lijkt dan dubbel zo hoog als een staafje van 97.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er mis met een as waar de stappen 0, 10, 20, 50 en 100 zijn?",
        opties=[
            "de as is foutief geijkt, want gelijke afstanden tonen ongelijke sprongen",
            "de as loopt niet ver genoeg door naar boven toe",
            "er staan veel te weinig waarden op de as om er nog iets op te lezen",
            "de as moet altijd bij één beginnen en niet bij nul",
        ],
        antwoord=0,
        uitleg="Zo kan een grafiek een kromme recht laten lijken of omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom misleidt een staafdiagram dat als blokken in drie dimensies getekend is?",
        opties=[
            "het oog vergelijkt volumes in plaats van hoogtes",
            "de staven staan te ver uit elkaar om te vergelijken",
            "de kleuren zijn dan altijd slechter te onderscheiden",
            "je kan de waarden op de as niet meer aflezen",
        ],
        antwoord=0,
        uitleg="Een blok dat twee keer zo hoog is, lijkt veel meer dan twee keer zo groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grafiek toont de verkoop van 2022 tot 2024 en laat 2023 weg. Waarom is dat misleidend?",
        opties=[
            "net dat jaar kan de stijging tegenspreken die de grafiek toont",
            "een grafiek moet altijd minstens vijf jaren tonen",
            "zonder dat jaar kan je het gemiddelde niet meer berekenen",
            "de as loopt dan niet meer gelijkmatig door",
        ],
        antwoord=0,
        uitleg="Ga altijd na of er jaren of groepen ontbreken, en vraag je af waarom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer geeft de mediaan een eerlijker beeld dan het gemiddelde?",
        opties=[
            "als enkele heel grote waarden het gemiddelde omhoog trekken",
            "als alle waarden dicht bij elkaar liggen",
            "als je met categorische gegevens werkt",
            "als er precies evenveel waarden boven als onder liggen",
        ],
        antwoord=0,
        uitleg="Bij lonen of huizenprijzen zegt de mediaan meer over wat gewoon is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reclame zegt: negen op de tien tandartsen raden dit aan. Welke vraag stel je eerst?",
        opties=[
            "hoeveel tandartsen zijn er bevraagd en door wie",
            "in welk lettertype de zin gedrukt staat",
            "of het getal negen wel deelbaar is door drie",
            "of tandartsen wel een mening mogen geven",
        ],
        antwoord=0,
        uitleg="Tien tandartsen die de fabrikant zelf koos, zeggen iets anders dan duizend willekeurige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vertelt een percentage zonder het aantal maar het halve verhaal?",
        opties=[
            "vijftig procent kan twee mensen op vier zijn of duizend op tweeduizend",
            "percentages worden altijd afgerond en zijn dus eigenlijk nooit juist",
            "een percentage kan niet boven de honderd uitkomen",
            "een percentage verandert mee met de gekozen as",
        ],
        antwoord=0,
        uitleg="Bij kleine aantallen schommelt een percentage enorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel verhoogt de prijs met 20 procent en geeft daarna 20 procent korting. Wat is het gevolg?",
        opties=[
            "de prijs ligt lager dan in het begin, de korting geldt op een hoger bedrag",
            "de prijs is na die twee stappen weer precies dezelfde als in het begin",
            "de prijs ligt hoger dan in het begin",
            "dat hangt volledig af van de beginprijs",
        ],
        antwoord=0,
        uitleg="Neem 100 euro: 120 euro min 20 procent is 96 euro. Procenten van verschillende bedragen tellen niet gewoon op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat bij een grafiek altijd best de bron vermeld?",
        opties=[
            "zo kan de lezer de cijfers zelf nagaan en zien wie ze verzamelde",
            "zo staat de grafiek meteen een stuk mooier in de bladspiegel",
            "zo hoeft de as niet meer bij nul te beginnen",
            "zo weet je meteen of de verdeling scheef is",
        ],
        antwoord=0,
        uitleg="Wie de cijfers verzamelde, heeft vaak ook belang bij de uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cirkeldiagram toont percentages die samen 118 procent geven. Wat is er aan de hand?",
        opties=[
            "de delen overlappen elkaar of het diagram klopt niet",
            "dat is normaal bij een cirkeldiagram met veel sectoren",
            "de cirkel is gewoon te klein getekend",
            "er is afgerond naar boven bij elk deel",
        ],
        antwoord=0,
        uitleg="Een cirkeldiagram verdeelt één geheel, dus alles samen is honderd procent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale as die niet bij nul begint, kan een klein verschil groot doen lijken.",
        antwoord=True,
        uitleg="Kijk bij elke grafiek eerst waar de as begint.",
    ),
    dict(
        type="waarofniet",
        vraag="Procent en procentpunt betekenen hetzelfde.",
        antwoord=False,
        uitleg="Van 20 naar 25 is 5 procentpunt, maar 25 procent groei.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek kan kloppen en toch een verkeerde indruk geven.",
        antwoord=True,
        uitleg="Met de keuze van de as, het tijdvak of de tekening stuur je wat de lezer ziet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gemiddelde is altijd de beste centrummaat om een groep te beschrijven.",
        antwoord=False,
        uitleg="Bij uitschieters of een scheve verdeling zegt de mediaan meer.",
    ),
    dict(
        type="invultekst",
        vraag="Een partij gaat van 12 naar 18 procent. Met hoeveel procentpunt is dat?",
        antwoord=["6"],
        uitleg="Gewoon het verschil.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen twee percentages, in één woord?",
        antwoord=["procentpunt", "procentpunten"],
        uitleg="Niet te verwarren met de groei in procent.",
    ),
    dict(
        type="invultekst",
        vraag="Een prijs van 100 euro stijgt 20 procent en krijgt dan 20 procent korting. Hoeveel euro kost ze dan?",
        antwoord=["96", "96 euro"],
        uitleg="20 procent van 120 is 24.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zet je uit in een spreidingsdiagram?",
        opties=[
            "twee variabelen tegen elkaar, één punt per waarneming",
            "één variabele in klassen, met aansluitende staven",
            "het verloop van één variabele door de tijd",
            "het aandeel van elk deel in één geheel",
        ],
        antwoord=0,
        uitleg="Zo zie je meteen of er een verband is tussen de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een trendlijn in een puntenwolk?",
        opties=[
            "de rechte die de vorm van de wolk het best samenvat",
            "de rechte die door alle punten van de wolk gaat",
            "de lijn die de hoogste en de laagste waarde verbindt",
            "de rand van de wolk aan de bovenkant",
        ],
        antwoord=0,
        uitleg="Ze gaat meestal door geen enkel punt precies, maar ligt er zo dicht mogelijk bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een positieve correlatie?",
        opties=[
            "als de ene variabele stijgt, stijgt de andere meestal ook",
            "als de ene variabele stijgt, daalt de andere meestal",
            "de ene variabele veroorzaakt de andere",
            "de punten liggen willekeurig verspreid over de grafiek",
        ],
        antwoord=0,
        uitleg="De wolk loopt dan van linksonder naar rechtsboven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tussen welke waarden ligt de correlatiecoëfficiënt?",
        opties=["tussen min 1 en 1", "tussen 0 en 1", "tussen min 100 en 100", "tussen 0 en 100"],
        antwoord=0,
        uitleg="Bij min 1 en 1 liggen alle punten precies op een rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een correlatiecoëfficiënt dicht bij nul?",
        opties=[
            "er is nauwelijks een rechtlijnig verband tussen de twee",
            "de twee variabelen zijn perfect aan elkaar gekoppeld",
            "de ene variabele veroorzaakt zeker de andere niet",
            "alle punten liggen precies op één rechte",
        ],
        antwoord=0,
        uitleg="Er kan wel nog een ander soort verband zijn, bijvoorbeeld een gebogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een correlatiecoëfficiënt van min 0,9?",
        opties=[
            "een sterk verband waarbij de ene daalt als de andere stijgt",
            "een tamelijk zwak verband waarbij allebei samen stijgen",
            "helemaal geen verband tussen de twee variabelen",
            "een verband dat door negen punten wordt getoond",
        ],
        antwoord=0,
        uitleg="Het teken geeft de richting, het getal de sterkte.",
    ),
    dict(
        type="meerkeuze",
        vraag="In gemeenten met meer ooievaars worden meer baby's geboren. Wat is de beste verklaring?",
        opties=[
            "grotere landelijke gemeenten hebben meer van allebei",
            "ooievaars brengen inderdaad de baby's rond",
            "het is zuiver toeval en er is geen verband",
            "baby's trekken de ooievaars naar een gemeente toe",
        ],
        antwoord=0,
        uitleg="Een derde factor verklaart de twee. Correlatie is geen oorzakelijk verband.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat correlatie geen oorzakelijk verband is?",
        opties=[
            "twee zaken kunnen samen bewegen zonder dat de ene de andere veroorzaakt",
            "twee zaken die samen bewegen hebben nooit iets met elkaar te maken",
            "een oorzaak geeft altijd een correlatie van precies één",
            "een correlatie kan enkel bij numerieke gegevens fout zijn",
        ],
        antwoord=0,
        uitleg="Er kan een derde factor zijn, of het verband kan omgekeerd lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="IJsverkoop en verdrinkingen stijgen samen. Welke derde factor verklaart dat?",
        opties=[
            "warm weer, want dan eet en zwemt iedereen meer",
            "de prijs van het ijs in de zomermaanden zelf",
            "het aantal zwembaden in een gemeente",
            "de leeftijd van de mensen die ijs kopen",
        ],
        antwoord=0,
        uitleg="Het ene veroorzaakt het andere niet; allebei hangen ze aan de temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het riskant om met een trendlijn ver buiten de gemeten waarden te voorspellen?",
        opties=[
            "buiten het gemeten gebied kan het verband er heel anders uitzien",
            "een trendlijn kan je enkel naar links doortrekken",
            "de correlatiecoëfficiënt wordt dan groter dan één",
            "de punten vallen dan vanzelf buiten de rand van de grafiek weg",
        ],
        antwoord=0,
        uitleg="Een groei die tien jaar rechtlijnig was, hoeft dat de volgende tien jaar niet te blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet één uitschieter ver van de wolk met de trendlijn?",
        opties=[
            "hij kan de lijn flink naar zich toe trekken",
            "hij verandert niets aan de ligging van de lijn",
            "hij maakt de correlatiecoëfficiënt altijd nul",
            "hij zorgt dat er geen trendlijn meer bestaat",
        ],
        antwoord=0,
        uitleg="Ga daarom altijd na of zo'n punt een meetfout is of een echte waarneming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet een puntenwolk zonder verband eruit?",
        opties=[
            "de punten liggen verspreid zonder duidelijke richting",
            "de punten liggen netjes op één rechte lijn",
            "de punten liggen allemaal in één hoek samen",
            "de punten liggen op een mooi gebogen lijn omhoog",
        ],
        antwoord=0,
        uitleg="De correlatiecoëfficiënt ligt dan dicht bij nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak past bij een sterke correlatie tussen studietijd en punten?",
        opties=[
            "wie meer studeert, haalt in deze groep meestal hogere punten",
            "meer studeren zorgt bij iedereen voor hogere punten",
            "wie hoge punten haalt, doet dat zonder te studeren",
            "studietijd en punten hebben duidelijk niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg="Je beschrijft wat je ziet in deze groep, zonder een oorzaak te beweren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een correlatiecoëfficiënt van 1 betekent dat alle punten precies op een stijgende rechte liggen.",
        antwoord=True,
        uitleg="Bij min 1 liggen ze op een dalende rechte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sterke correlatie bewijst dat de ene variabele de andere veroorzaakt.",
        antwoord=False,
        uitleg="Er kan een derde factor achter zitten, of het verband kan omgekeerd lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een negatieve correlatie loopt de puntenwolk van linksboven naar rechtsonder.",
        antwoord=True,
        uitleg="Als de ene stijgt, daalt de andere.",
    ),
    dict(
        type="waarofniet",
        vraag="Een trendlijn gaat altijd door alle punten van de wolk.",
        antwoord=False,
        uitleg="Ze vat de wolk samen en gaat vaak door geen enkel punt precies.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grafiek waarin je twee variabelen tegen elkaar uitzet met één punt per waarneming?",
        antwoord=["spreidingsdiagram", "puntenwolk"],
        uitleg="Ook puntenwolk is een gangbare naam.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de grootste waarde die een correlatiecoëfficiënt kan aannemen?",
        antwoord=["1", "één"],
        uitleg="De kleinste is min 1.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de rechte die de vorm van een puntenwolk samenvat?",
        antwoord=["trendlijn", "de trendlijn"],
        uitleg="Ze gaat meestal door geen enkel punt precies.",
    ),
]
