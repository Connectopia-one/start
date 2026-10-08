# -*- coding: utf-8 -*-
"""Spreidingsdiagrammen, trendlijn en correlatie.

De fiche vraagt hier het verband tussen twee numerieke grootheden, en ze noemt
de begrippen bij naam: spreidingsdiagram (ook scatterdiagram of puntenwolk),
onafhankelijke en afhankelijke variabele, de verbanden recht evenredig,
omgekeerd evenredig, lineair en kwadratisch, een informeel begrip van
trendlijn en van correlatiecoëfficiënt, en het onderscheid tussen correlatie
en causaliteit.

De vuistregels voor r staan in het formularium, dus een kind krijgt ze op het
examen. Ze staan hier letterlijk zo:
    r kleiner dan −0,7           sterke negatieve samenhang
    tussen −0,7 en −0,3          matige negatieve samenhang
    tussen −0,3 en 0             zwakke negatieve samenhang
    r gelijk aan 0               geen samenhang
    tussen 0 en 0,3              zwakke positieve samenhang
    tussen 0,3 en 0,7            matige positieve samenhang
    r groter dan 0,7             sterke positieve samenhang
Gebruik geen andere drempels, ook al staan die in sommige handboeken.

Correlatie en causaliteit is het leerdoel waar de examencommissie het vaakst
op doorvraagt, en terecht: het is de ene statistische vaardigheid die een
kind ook buiten de wiskundeles nodig heeft. Daarom staat ze in deel 2 met
voorbeelden die niet uit een handboek komen maar uit het nieuws.

Deel 1 is het spreidingsdiagram en de soorten verbanden.
Deel 2 is de trendlijn, de correlatiecoëfficiënt en causaliteit.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zet je in een spreidingsdiagram?",
        opties=[
            "voor elk element één punt met twee gemeten waarden",
            "voor elke klasse één staaf met de frequentie erin",
            "voor elke waarde één stip boven de getallenas",
            "voor elke groep één vakje met de kwartielen erin",
        ],
        antwoord=0,
        uitleg="Elke leerling wordt één punt: zijn lengte horizontaal en zijn gewicht verticaal, bijvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke variabele zet je op de horizontale as van een spreidingsdiagram?",
        opties=[
            "de onafhankelijke variabele",
            "de afhankelijke variabele",
            "de variabele met de grootste spreiding",
            "de variabele met de kleinste waarden",
        ],
        antwoord=0,
        uitleg="De onafhankelijke variabele is de oorzaak of de verklarende grootheid. De afhankelijke komt verticaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of meer studietijd een hoger punt geeft. Wat is de afhankelijke variabele?",
        opties=[
            "het punt op de toets",
            "de studietijd in uren",
            "het aantal leerlingen",
            "de dag van de week",
        ],
        antwoord=0,
        uitleg="Het punt hangt af van de studietijd, dus het punt komt op de verticale as.",
    ),
    dict(
        type="waarofniet",
        vraag="Met een ander woord heet een spreidingsdiagram ook een puntenwolk.",
        antwoord=True,
        uitleg="De fiche noemt drie namen voor hetzelfde: spreidingsdiagram, scatterdiagram en puntenwolk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een verband recht evenredig?",
        opties=[
            "als de ene grootheid verdubbelt wanneer de andere verdubbelt",
            "als de ene grootheid halveert wanneer de andere verdubbelt",
            "als de punten in een parabool liggen in het diagram",
            "als de punten geen enkel patroon vormen in het diagram",
        ],
        antwoord=0,
        uitleg="De grafiek is dan een rechte door de oorsprong. Dubbel zoveel brood kost dubbel zoveel geld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een verband omgekeerd evenredig?",
        opties=[
            "als de ene grootheid halveert wanneer de andere verdubbelt",
            "als de ene grootheid verdubbelt wanneer de andere verdubbelt",
            "als het product van de twee grootheden steeds groter wordt",
            "als de punten rond een horizontale rechte liggen in het diagram",
        ],
        antwoord=0,
        uitleg="Het product van de twee blijft dan constant. Twee keer zo snel rijden, half zoveel tijd nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Welk soort verband hoort bij een puntenwolk in de vorm van een parabool? Eén woord.",
        antwoord=["kwadratisch", "kwadratische", "kwadraat"],
        uitleg="De fiche noemt vier soorten verbanden: recht evenredig, omgekeerd evenredig, lineair en kwadratisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lineair verband hoeft niet door de oorsprong te gaan.",
        antwoord=True,
        uitleg="Dat is net het verschil met recht evenredig. Een taxirit met een opstapprijs is lineair maar niet recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="De punten in een puntenwolk liggen rond een rechte die van links onder naar rechts boven loopt. Wat besluit je?",
        opties=[
            "er is een positief lineair verband tussen de twee grootheden",
            "er is een negatief lineair verband tussen de twee grootheden",
            "er is een kwadratisch verband tussen de twee grootheden",
            "er is geen enkel verband tussen de twee grootheden",
        ],
        antwoord=0,
        uitleg="Stijgen de twee samen, dan is het verband positief. Daalt de ene terwijl de andere stijgt, dan is het negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je volgens de fiche een spreidingsdiagram?",
        opties=[
            "met ICT, dus met de rekenapps van de examencommissie",
            "met de hand op millimeterpapier, want ICT mag niet",
            "door de punten in een frequentietabel te groeperen",
            "door de twee variabelen eerst te standaardiseren",
        ],
        antwoord=0,
        uitleg="De fiche zegt letterlijk: je tekent een spreidingsdiagram met ICT. Daarna interpreteer je het zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een puntenwolk zonder enig patroon betekent dat er zeker geen enkel verband bestaat.",
        antwoord=False,
        uitleg="Er is dan geen lineair verband, maar een ander verband is niet uitgesloten. Kijk altijd eerst naar de vorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een puntenwolk in de vorm van een omgekeerde U. Wat is de beste beschrijving?",
        opties=[
            "een kwadratisch verband met een maximum in het midden",
            "een sterk positief lineair verband over het hele bereik",
            "een sterk negatief lineair verband over het hele bereik",
            "twee groepen punten zonder enig onderling verband",
        ],
        antwoord=0,
        uitleg="Zo'n vorm komt vaak voor: eerst stijgt het, dan daalt het. Een rechte zou hier een slechte trendlijn zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom teken je eerst een spreidingsdiagram vóór je een correlatiecoëfficiënt berekent?",
        opties=[
            "omdat r enkel iets zegt over een lineair verband en je de vorm wil zien",
            "omdat een rekenapp zonder diagram geen r kan uitrekenen",
            "omdat je de uitschieters eerst moet verwijderen uit de gegevens",
            "omdat r anders groter dan één kan uitkomen in de berekening",
        ],
        antwoord=0,
        uitleg="Een perfecte parabool kan r dicht bij nul geven. Het getal alleen zou je dan misleiden.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke as van een spreidingsdiagram staat de afhankelijke variabele? Eén woord.",
        antwoord=["verticale", "verticaal", "y-as"],
        uitleg="De afhankelijke variabele staat verticaal, de onafhankelijke horizontaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spreidingsdiagram is geschikt om één variabele in groepen weer te geven.",
        antwoord=False,
        uitleg="Daarvoor dient een histogram of een staafdiagram. Een spreidingsdiagram heeft altijd twee variabelen nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet bij vijftig auto's de snelheid en de remafstand. De remafstand groeit sneller dan de snelheid. Welk verband past?",
        opties=[
            "een kwadratisch verband tussen snelheid en remafstand",
            "een recht evenredig verband tussen snelheid en remafstand",
            "een omgekeerd evenredig verband tussen de twee grootheden",
            "een lineair verband met een negatieve richtingscoëfficiënt",
        ],
        antwoord=0,
        uitleg="De remafstand hangt af van het kwadraat van de snelheid. Twee keer zo snel is vier keer zo ver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een punt ligt heel ver van de rest van de puntenwolk. Wat doe je?",
        opties=[
            "je onderzoekt of het een meetfout of een echt bijzonder geval is",
            "je verwijdert het altijd, want het verstoort de trendlijn",
            "je houdt het altijd bij, want data mag je nooit aanpassen",
            "je vervangt het door het gemiddelde van de andere punten",
        ],
        antwoord=0,
        uitleg="Een uitschieter kan een tikfout zijn of juist de interessantste meting. Beslis dat nooit zonder te kijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spreidingsdiagram kan ook een verband tonen dat niet rechtlijnig is.",
        antwoord=True,
        uitleg="Daarom is het diagram zelf vaak leerrijker dan het getal r, dat enkel het lineaire deel meet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel numerieke variabelen heb je nodig voor een spreidingsdiagram? Geef het getal in cijfers.",
        antwoord=["2", "twee"],
        uitleg="Twee: een onafhankelijke op de horizontale as en een afhankelijke op de verticale.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zet in een diagram de schoolresultaten horizontaal en de studietijd verticaal. Wat zou je aanpassen?",
        opties=[
            "de assen omwisselen, want de studietijd is hier de onafhankelijke variabele",
            "niets, de keuze van de assen is volledig vrij bij een puntenwolk",
            "de schoolresultaten eerst in groepen verdelen voor het diagram",
            "de twee variabelen standaardiseren voor hij ze uitzet",
        ],
        antwoord=0,
        uitleg="Je verwacht dat de studietijd het resultaat beïnvloedt, dus die hoort op de horizontale as.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een trendlijn in een spreidingsdiagram?",
        opties=[
            "de lijn die het verloop van de puntenwolk het best weergeeft",
            "de lijn die alle punten van de wolk verbindt in volgorde",
            "de lijn door het kleinste en het grootste punt van de wolk",
            "de lijn die de wolk in twee gelijke helften verdeelt",
        ],
        antwoord=0,
        uitleg="Bij een lineair verband is dat een rechte. Een rekenapp geeft je haar voorschrift.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tussen welke twee waarden ligt de correlatiecoëfficiënt r altijd?",
        opties=["tussen min één en plus één", "tussen nul en plus één", "tussen min honderd en plus honderd", "tussen nul en plus honderd"],
        antwoord=0,
        uitleg="Komt er een waarde buiten dat bereik, dan is er iets fout ingetikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke samenhang hoort volgens het formularium bij r gelijk aan 0,85?",
        opties=[
            "sterke positieve samenhang",
            "matige positieve samenhang",
            "zwakke positieve samenhang",
            "sterke negatieve samenhang",
        ],
        antwoord=0,
        uitleg="Boven 0,7 spreekt het formularium van sterke positieve samenhang.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens het formularium hoort r gelijk aan min 0,5 bij een matige negatieve samenhang.",
        antwoord=True,
        uitleg="Min 0,5 ligt tussen min 0,7 en min 0,3, dus matig negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke samenhang hoort volgens het formularium bij r gelijk aan 0,2?",
        opties=[
            "zwakke positieve samenhang",
            "matige positieve samenhang",
            "sterke positieve samenhang",
            "helemaal geen samenhang",
        ],
        antwoord=0,
        uitleg="Tussen nul en 0,3 is de samenhang zwak positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent r gelijk aan min 0,9?",
        opties=[
            "een sterk verband waarbij de ene daalt als de andere stijgt",
            "een sterk verband waarbij de twee grootheden samen stijgen",
            "een zwak verband waarbij de ene daalt als de andere stijgt",
            "helemaal geen verband tussen de twee grootheden",
        ],
        antwoord=0,
        uitleg="Het minteken geeft de richting, de grootte geeft de sterkte. Min 0,9 is sterk en dalend.",
    ),
    dict(
        type="invultekst",
        vraag="Welke waarde heeft r als er volgens het formularium geen samenhang is? Geef het getal in cijfers.",
        antwoord=["0", "nul"],
        uitleg="r gelijk aan nul betekent geen lineaire samenhang.",
    ),
    dict(
        type="waarofniet",
        vraag="Een correlatiecoëfficiënt van nul betekent dat er zeker geen enkel verband is.",
        antwoord=False,
        uitleg="r meet enkel het lineaire verband. Een mooie parabool kan r bijna nul geven en toch een sterk verband zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen correlatie en causaliteit?",
        opties=[
            "correlatie is samenhang, causaliteit is oorzaak en gevolg",
            "correlatie is oorzaak en gevolg, causaliteit is samenhang",
            "correlatie geldt bij twee variabelen, causaliteit bij drie of meer",
            "correlatie is een getal, causaliteit is er de wortel van",
        ],
        antwoord=0,
        uitleg="Twee grootheden kunnen samen bewegen zonder dat de ene de andere veroorzaakt. Dat is de kern van dit leerdoel.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de zomer worden er meer ijsjes verkocht en verdrinken er meer mensen. Wat besluit je?",
        opties=[
            "er is correlatie, maar de warmte verklaart beide en dus geen causaliteit",
            "ijsjes eten maakt mensen onvoorzichtiger in het water",
            "er is geen correlatie tussen de twee aantallen gemeten",
            "verdrinkingen doen de verkoop van ijsjes stijgen",
        ],
        antwoord=0,
        uitleg="De warmte is hier de verborgen derde factor. Dit is het schoolvoorbeeld van correlatie zonder causaliteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sterke correlatie bewijst dat de ene grootheid de andere veroorzaakt.",
        antwoord=False,
        uitleg="Nooit. Er kan een derde factor zijn, of het verband kan omgekeerd lopen, of het kan toeval zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoek vindt dat kinderen met grotere voeten beter kunnen lezen. Wat is de verklaring?",
        opties=[
            "de leeftijd verklaart beide, oudere kinderen zijn groter en lezen beter",
            "grote voeten helpen bij het evenwicht tijdens het lezen",
            "kinderen die goed lezen bewegen meer en krijgen grotere voeten",
            "er is geen correlatie, het onderzoek is verkeerd uitgevoerd",
        ],
        antwoord=0,
        uitleg="Ook dit is een verborgen derde factor. Zoek bij een vreemde correlatie altijd eerst naar zo'n factor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bepaal je het voorschrift van de trendlijn volgens de fiche?",
        opties=[
            "met ICT, de rekenapp geeft je de vergelijking",
            "door twee punten uit de wolk te kiezen en de rechte erdoor te berekenen",
            "door het gemiddelde van alle x en alle y met de hand te berekenen",
            "door de puntenwolk op ruitjespapier na te tekenen",
        ],
        antwoord=0,
        uitleg="De fiche zegt: je bepaalt het voorschrift van een trendlijn met ICT. Daarna interpreteer je ze.",
    ),
    dict(
        type="invultekst",
        vraag="Boven welke waarde van r spreekt het formularium van een sterke positieve samenhang? Geef het getal als decimaal.",
        antwoord=["0,7", "0.7"],
        uitleg="Boven 0,7 is de samenhang sterk positief; onder min 0,7 sterk negatief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een trendlijn mag je gebruiken om buiten het bereik van je gegevens te voorspellen.",
        antwoord=False,
        uitleg="Buiten je meetbereik weet je niet of het verband doorloopt. Zo'n voorspelling is onbetrouwbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="De trendlijn van een onderzoek is y gelijk aan 2x plus 5. Wat betekent de 2?",
        opties=[
            "per eenheid die x stijgt, stijgt y met twee eenheden",
            "de waarde van y is altijd twee keer zo groot als x",
            "er zijn twee variabelen in het onderzoek betrokken",
            "de correlatiecoëfficiënt is gelijk aan twee",
        ],
        antwoord=0,
        uitleg="De richtingscoëfficiënt geeft de verandering van y per eenheid x. De 5 is de waarde bij x gelijk aan nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt r gelijk aan 0,35 tussen twee grootheden. Hoe beschrijf je dat?",
        opties=[
            "een matige positieve samenhang volgens de vuistregels",
            "een sterke positieve samenhang volgens de vuistregels",
            "een zwakke negatieve samenhang volgens de vuistregels",
            "een perfect lineair verband tussen de twee grootheden",
        ],
        antwoord=0,
        uitleg="Tussen 0,3 en 0,7 is de samenhang matig positief. Dat is net boven de grens van zwak.",
    ),
    dict(
        type="waarofniet",
        vraag="De vuistregels voor r staan in het formularium dat je bij het examen krijgt.",
        antwoord=True,
        uitleg="Je moet ze dus niet uit het hoofd kennen, wel kunnen toepassen en kunnen uitleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee onderzoekers vinden r gelijk aan 0,8 maar hun puntenwolken zien er anders uit. Kan dat?",
        opties=[
            "ja, hetzelfde getal kan bij verschillende vormen horen, daarom kijk je altijd naar het diagram",
            "nee, hetzelfde getal betekent altijd dezelfde vorm van de wolk",
            "nee, een van de twee heeft een rekenfout gemaakt bij de berekening",
            "ja, maar enkel als de ene wolk meer punten bevat dan de andere",
        ],
        antwoord=0,
        uitleg="Enkele uitschieters kunnen r sterk optrekken terwijl de rest geen verband vertoont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft: wie meer melk drinkt, haalt hogere punten, dus drink melk. Wat zeg je?",
        opties=[
            "uit samenhang volgt geen oorzaak, misschien ontbijten die leerlingen simpelweg beter",
            "de krant heeft gelijk, een sterke samenhang bewijst het verband",
            "de krant moet eerst de correlatiecoëfficiënt in procent omzetten",
            "er kan geen samenhang zijn tussen melk en schoolresultaten",
        ],
        antwoord=0,
        uitleg="Het hele leerdoel zit in deze vraag: correlatie is geen causaliteit, en een derde factor is bijna altijd mogelijk.",
    ),
]
