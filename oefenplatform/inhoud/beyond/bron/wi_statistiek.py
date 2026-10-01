# -*- coding: utf-8 -*-
"""Statistiek: de normale verdeling, steekproeven en de hypothesetoets.

Het derde stuk van het onderdeel "Telproblemen, kansrekenen en statistiek"
van fiche G2. Alles staat hier in opgaven met context, en het rekenwerk mag
met ICT: wat je zelf moet kunnen, is beoordelen of een model past en wat een
uitkomst betekent.

Deel 1 is de normale verdeling met de Gausskromme en de z-score.
Deel 2 zijn de steekproeven, het verschil tussen samenhang en oorzaak, en de
hypothesetoets.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de grafiek van een normale verdeling eruit?",
        opties=[
            "klokvormig en symmetrisch rond het gemiddelde",
            "klokvormig maar met een lange staart naar rechts",
            "een rechte die gelijkmatig stijgt tot aan het gemiddelde",
            "een trapjeslijn met één stap per waarde",
        ],
        antwoord=0,
        uitleg="Die kromme heet de Gausskromme. Is een histogram duidelijk scheef, dan past het normale model niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bepaalt waar de top van de Gausskromme ligt?",
        opties=[
            "het gemiddelde",
            "de standaardafwijking",
            "het aantal metingen",
            "de grootste meetwaarde",
        ],
        antwoord=0,
        uitleg="Het gemiddelde schuift de kromme naar links of naar rechts. De standaardafwijking maakt haar breder of smaller.",
    ),
    dict(
        type="invultekst",
        vraag="Een meting is precies gelijk aan het gemiddelde. Welke z-score heeft ze? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="De z-score meet hoeveel standaardafwijkingen je van het gemiddelde af zit. Op het gemiddelde zelf is dat nul.",
    ),
    dict(
        type="waarofniet",
        vraag="De standaardafwijking bepaalt hoe breed de Gausskromme is.",
        antwoord=True,
        uitleg="Een kleine standaardafwijking geeft een smalle, hoge klok; een grote geeft een brede, platte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de z-score van een meting?",
        opties=[
            "het verschil met het gemiddelde, gedeeld door de standaardafwijking",
            "het verschil met het gemiddelde, maal de standaardafwijking ervan",
            "de meting gedeeld door het gemiddelde van alle metingen",
            "de meting min de standaardafwijking van de verdeling",
        ],
        antwoord=0,
        uitleg="Zo wordt elke verdeling omgezet naar de standaardnormale, en kan je metingen uit verschillende groepen vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de totale oppervlakte onder een Gausskromme?",
        opties=["één", "honderd", "nul", "gelijk aan het gemiddelde"],
        antwoord=0,
        uitleg="Alle kans samen is één. Een kans is dus een stuk van die oppervlakte.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een continue verdeling is de kans op precies één welbepaalde waarde gelijk aan nul.",
        antwoord=True,
        uitleg="Een enkele waarde heeft geen breedte, dus ook geen oppervlakte. Daarom reken je altijd met intervallen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk gemiddelde heeft de standaardnormale verdeling? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Ze is de normale verdeling na omzetting naar z-scores.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke standaardafwijking heeft de standaardnormale verdeling?",
        opties=["één", "nul", "honderd", "dezelfde als de oorspronkelijke"],
        antwoord=0,
        uitleg="Gemiddelde nul en standaardafwijking één, zodat één eenheid op de as precies één standaardafwijking is.",
    ),
    dict(
        type="waarofniet",
        vraag="Ongeveer vijfennegentig procent van de metingen ligt binnen één standaardafwijking van het gemiddelde.",
        antwoord=False,
        uitleg="Binnen één standaardafwijking ligt ongeveer achtenzestig procent. Vijfennegentig procent hoort bij twee standaardafwijkingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel procent van de metingen ligt ongeveer binnen twee standaardafwijkingen van het gemiddelde?",
        opties=["vijfennegentig", "achtenzestig", "negenennegentig", "vijftig"],
        antwoord=0,
        uitleg="Dat is de bekende vuistregel: ongeveer achtenzestig, vijfennegentig en negenennegentig komma zeven procent bij één, twee en drie standaardafwijkingen.",
    ),
    dict(
        type="invultekst",
        vraag="Het gemiddelde is zeventig en de standaardafwijking vijf. Welke z-score heeft een meting van tachtig? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="Tien verschil gedeeld door vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beoordeel je of de normale verdeling een geschikt model is voor je gegevens?",
        opties=[
            "je kijkt of het histogram ongeveer klokvormig is",
            "je kijkt of alle waarden positief zijn",
            "je kijkt of er precies honderd metingen zijn",
            "je kijkt of het gemiddelde groter is dan nul",
        ],
        antwoord=0,
        uitleg="Je kan er ook de dichtheidsfunctie met de geschatte parameters over tekenen en vergelijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een z-score kan negatief zijn.",
        antwoord=True,
        uitleg="Dan ligt de meting onder het gemiddelde. Het teken zegt aan welke kant ze zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een z-score van min anderhalf?",
        opties=[
            "de meting ligt anderhalve standaardafwijking onder het gemiddelde",
            "de meting ligt anderhalve standaardafwijking boven het gemiddelde",
            "de meting is anderhalve eenheid kleiner dan het gemiddelde",
            "de kans op die meting is anderhalf procent",
        ],
        antwoord=0,
        uitleg="De z-score telt in standaardafwijkingen, niet in de eenheid van de meting zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee komt een kans bij een normale verdeling overeen?",
        opties=[
            "met de oppervlakte onder de Gausskromme",
            "met de hoogte van de Gausskromme in dat punt",
            "met de z-score van de bijbehorende waarde",
            "met de breedte van het interval op de x-as",
        ],
        antwoord=0,
        uitleg="De hoogte alleen zegt niets: pas een stuk oppervlakte geeft een kans.",
    ),
    dict(
        type="waarofniet",
        vraag="De Gausskromme raakt links en rechts de horizontale as.",
        antwoord=False,
        uitleg="Ze nadert de as wel, maar bereikt haar nooit. Elke waarde blijft dus in principe mogelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel procent van de metingen ligt links van het gemiddelde bij een normale verdeling? Schrijf het getal.",
        antwoord=["50", "vijftig"],
        uitleg="De kromme is symmetrisch om het gemiddelde, dus de oppervlakte valt in twee gelijke helften uiteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee Gausskrommen hebben hetzelfde gemiddelde, maar de ene is smaller. Wat betekent dat?",
        opties=[
            "bij de smalle liggen de metingen dichter bij het gemiddelde",
            "bij de smalle liggen de metingen verder van het gemiddelde",
            "de smalle hoort bij een grotere groep metingen",
            "de smalle heeft een kleinere totale oppervlakte",
        ],
        antwoord=0,
        uitleg="Smaller betekent een kleinere standaardafwijking, dus minder spreiding. De oppervlakte blijft bij allebei één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen het gemiddelde van een populatie en dat van een steekproef?",
        opties=[
            "het eerste is de echte waarde, het tweede een schatting ervan",
            "het eerste is een schatting, het tweede de echte waarde",
            "het eerste gebruikt meer cijfers na de komma dan het tweede",
            "er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Daarom krijgen ze ook een ander symbool. Je kent het populatiegemiddelde meestal niet en schat het uit je steekproef.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een steekproef representatief?",
        opties=[
            "als ze op de belangrijke kenmerken op de populatie lijkt",
            "als ze uit minstens honderd personen bestaat",
            "als iedereen die meedeed dat vrijwillig deed",
            "als ze op één plaats en in één keer verzameld is geweest",
        ],
        antwoord=0,
        uitleg="Grootte alleen helpt niet: een heel grote maar scheve steekproef blijft scheef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is randomisatie bij een steekproef?",
        opties=[
            "iedereen uit de populatie evenveel kans geven om gekozen te worden",
            "de deelnemers zelf laten beslissen of ze meedoen",
            "de gegevens achteraf in willekeurige volgorde zetten",
            "een groep kiezen die het gemakkelijkst te bereiken valt, zonder loting",
        ],
        antwoord=0,
        uitleg="Dat is net wat een enkelvoudig aselecte steekproef doet, en het is de beste bescherming tegen vertekening.",
    ),
    dict(
        type="invultekst",
        vraag="Een significantieniveau alfa van nul komma nul vijf. Hoeveel procent is dat? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="Dat is de kans die je aanvaardt om de nulhypothese onterecht te verwerpen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere aselecte steekproef geeft doorgaans een betrouwbaarder resultaat.",
        antwoord=True,
        uitleg="De steekproeffout wordt kleiner. Een niet-steekproeffout, zoals een slechte vraagstelling, wordt er niet kleiner van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een steekproeffout en een niet-steekproeffout?",
        opties=[
            "de eerste komt door het toeval van de trekking, de tweede door de opzet",
            "de eerste komt door de opzet, de tweede door het toeval van de trekking",
            "de eerste kan je berekenen, de tweede komt alleen bij kleine groepen voor",
            "de eerste gaat over de populatie, de tweede over de variabele",
        ],
        antwoord=0,
        uitleg="Toeval kan je inschatten en kleiner maken met meer deelnemers. Een fout in de opzet blijft ook bij duizend deelnemers bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant laat lezers online stemmen over een stelling. Welk probleem is dat?",
        opties=[
            "vrijwillige respons, want wie zich sterk betrokken voelt, stemt vaker",
            "een te kleine steekproef, want online doen er maar weinig mensen mee",
            "randomisatie, want de volgorde van de antwoorden ligt vast",
            "er is geen probleem, want iedereen kon meedoen",
        ],
        antwoord=0,
        uitleg="De groep die antwoordt, is niet toevallig samengesteld. Dat is een niet-steekproeffout, en meer stemmen lost dat niet op.",
    ),
    dict(
        type="waarofniet",
        vraag="Als twee grootheden sterk samenhangen, is de ene de oorzaak van de andere.",
        antwoord=False,
        uitleg="Samenhang kan ook komen van een derde verborgen variabele, van omgekeerde oorzaak en gevolg, of gewoon van toeval.",
    ),
    dict(
        type="invultekst",
        vraag="Tussen welke twee getallen ligt de correlatiecoëfficiënt? Schrijf het kleinste.",
        antwoord=["-1", "min 1"],
        uitleg="Ze loopt van min één tot plus één. Het teken geeft de richting, de grootte de sterkte van het lineaire verband.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de zomer worden er meer ijsjes verkocht en gebeuren er meer verdrinkingen. Wat verklaart die samenhang?",
        opties=[
            "een derde verborgen variabele, namelijk het warme weer",
            "ijsjes eten maakt zwemmen gevaarlijker",
            "verdrinkingen zetten mensen aan om meer ijsjes te kopen",
            "er is geen samenhang, het is een rekenfout",
        ],
        antwoord=0,
        uitleg="Warm weer verhoogt allebei de aantallen. Dat is het klassieke voorbeeld van samenhang zonder oorzakelijk verband.",
    ),
    dict(
        type="waarofniet",
        vraag="De nulhypothese is de uitspraak die je met je onderzoek wil aantonen.",
        antwoord=False,
        uitleg="Het is net omgekeerd: de nulhypothese is wat je probeert te verwerpen. Wat je wil aantonen, staat in de alternatieve hypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de p-waarde?",
        opties=[
            "de kans op zo'n resultaat of extremer, als de nulhypothese waar is",
            "de kans dat de nulhypothese waar is, gegeven dit ene resultaat",
            "de kans dat je onderzoek achteraf herhaalbaar blijkt te zijn",
            "het aandeel van de hele populatie dat in de steekproef zit",
        ],
        antwoord=0,
        uitleg="Ze zegt niets over de kans dat de hypothese klopt, alleen hoe verrassend je resultaat zou zijn mocht ze kloppen.",
    ),
    dict(
        type="invultekst",
        vraag="De p-waarde is nul komma nul twee en het significantieniveau nul komma nul vijf. Verwerp je de nulhypothese? Schrijf ja of nee.",
        antwoord=["ja"],
        uitleg="De p-waarde ligt onder het significantieniveau, dus het resultaat is te onwaarschijnlijk om nog bij de nulhypothese te passen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een type I-fout?",
        opties=[
            "de nulhypothese verwerpen terwijl ze eigenlijk waar is",
            "de nulhypothese behouden terwijl ze eigenlijk vals is",
            "een rekenfout maken bij het bepalen van de p-waarde",
            "de verkeerde alternatieve hypothese kiezen vooraf",
        ],
        antwoord=0,
        uitleg="De kans daarop is net het significantieniveau dat je vooraf kiest. Een vals alarm, dus.",
    ),
    dict(
        type="waarofniet",
        vraag="Een type II-fout is de nulhypothese onterecht niet verwerpen.",
        antwoord=True,
        uitleg="Er was wel degelijk een effect, maar je onderzoek vond het niet. Dat gebeurt vaker bij een kleine steekproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je een eenzijdige hypothesetoets?",
        opties=[
            "als je vooraf een richting verwacht, bijvoorbeeld een stijging",
            "als je steekproef uit maar één enkele groep mensen bestaat",
            "als de verdeling achteraf niet symmetrisch blijkt te zijn",
            "als je maar één keer kan meten in het hele onderzoek",
        ],
        antwoord=0,
        uitleg="Vermoed je alleen dat er iets verandert, zonder te weten in welke richting, dan toets je tweezijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af in een spreidingsdiagram?",
        opties=[
            "of er een verband is tussen twee numerieke grootheden",
            "hoe vaak elke afzonderlijke waarde voorkomt",
            "hoeveel procent van de metingen boven het gemiddelde ligt",
            "wat de standaardafwijking van de gegevens is",
        ],
        antwoord=0,
        uitleg="Elk punt is één waarneming met twee kenmerken. De vorm van de wolk verraadt het verband.",
    ),
    dict(
        type="waarofniet",
        vraag="Een correlatiecoëfficiënt dicht bij nul wijst op een sterk lineair verband.",
        antwoord=False,
        uitleg="Dicht bij nul betekent net dat er nauwelijks lineair verband is. Sterk is ze als ze dicht bij min één of plus één ligt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de kans die je vooraf aanvaardt om de nulhypothese onterecht te verwerpen? Schrijf het woord.",
        antwoord=["significantieniveau", "alfa"],
        uitleg="Meestal kiest men vijf procent, soms één procent als een vals alarm duur uitvalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een trendlijn in een spreidingsdiagram?",
        opties=[
            "een rechte of kromme die het patroon in de puntenwolk samenvat",
            "de lijn die alle punten van de puntenwolk met elkaar verbindt",
            "de lijn waarop precies de helft van de punten ligt",
            "de rand van het gebied waarbinnen alle punten liggen",
        ],
        antwoord=0,
        uitleg="Ze gaat meestal niet door de punten zelf, maar loopt er zo dicht mogelijk langs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verwerpt de nulhypothese niet. Wat besluit je?",
        opties=[
            "er is onvoldoende bewijs tegen de nulhypothese gevonden",
            "de nulhypothese is hiermee bewezen waar",
            "het onderzoek is mislukt en moet overgedaan worden",
            "de alternatieve hypothese is hiermee verworpen",
        ],
        antwoord=0,
        uitleg="Geen bewijs vinden is niet hetzelfde als bewijzen dat er niets is. Misschien was je steekproef gewoon te klein.",
    ),
]
