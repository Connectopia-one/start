# -*- coding: utf-8 -*-
"""Cognitieve dissonantie en processen in een groep.

Het tweede van drie thema's over sociale psychologie. De cognitieve dissonantie
is het derde mentale proces van de sociale cognitie uit het vorige thema; de
groepsprocessen vormen een eigen blok in de fiche.

De lijstjes staan letterlijk in de fiche:

    cognitieve consonantie en dissonantie: Leon Festinger
    dissonantie verminderen kan op drie manieren: attitude veranderen,
        gedrag veranderen, cognitie toevoegen
    dissonantie in het dagelijks leven: na het maken van een keuze, na het
        instemmen met een verzoek, na het leveren van inspanningen
    fasen in groepsvorming: Tuckman
        oriëntatiefase (forming), machtsfase (storming),
        normeringsfase (norming), prestatiefase (performing),
        afscheidsfase (adjourning)
    groepsprocessen: groepslidmaatschap (ingroup en outgroup), sociale
        facilitatie, social loafing of sociaal parasiteren, sociale
        belemmering, groepsdenken

Let op het verschil tussen sociale facilitatie en sociale belemmering. Publiek
maakt een eenvoudige, goed ingeoefende taak beter en een moeilijke, nieuwe
taak slechter. Die twee kanten zijn hier allebei gevraagd.

Deel 1 is de cognitieve dissonantie.
Deel 2 zijn de groepsprocessen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de theorie van de cognitieve dissonantie?",
        opties=[
            "Leon Festinger",
            "Fritz Heider",
            "Bruce Tuckman",
            "Solomon Asch",
        ],
        antwoord=0,
        uitleg="Festinger. Hij zette consonantie en dissonantie naast elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is cognitieve dissonantie?",
        opties=[
            "de spanning tussen twee dingen die niet samengaan",
            "de rust als je denken en doen bij elkaar passen",
            "de druk die een groep op een lid uitoefent",
            "de oorzaak die je aan gedrag toeschrijft",
        ],
        antwoord=0,
        uitleg="Dissonantie is wanklank. Je denkt het ene en doet het andere, en dat wringt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is cognitieve consonantie?",
        opties=[
            "de rust als je denken en je doen bij elkaar passen",
            "de spanning als je denken en je doen wringen",
            "de twijfel voor je een keuze maakt",
            "de spijt na een verkeerde keuze",
        ],
        antwoord=0,
        uitleg="Consonantie is samenklank: wat je denkt en wat je doet, kloppen met elkaar. Dan is er geen spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie manieren noemt de fiche om cognitieve dissonantie te verminderen?",
        opties=[
            "je attitude veranderen",
            "je gedrag veranderen",
            "een cognitie toevoegen",
            "de groep verlaten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie: je houding aanpassen, je gedrag aanpassen, of een nieuwe gedachte toevoegen die de spanning verklaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een roker die weet dat roken schadelijk is, stopt met roken. Welke manier van dissonantiereductie is dit?",
        opties=[
            "zijn gedrag veranderen",
            "zijn attitude veranderen",
            "een cognitie toevoegen",
            "een attributie maken",
        ],
        antwoord=0,
        uitleg="Hij past zijn doen aan bij zijn denken. Dat is gedrag veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een roker die weet dat roken schadelijk is, zegt: mijn opa rookte en werd negentig. Welke manier van dissonantiereductie is dit?",
        opties=[
            "een cognitie toevoegen",
            "zijn gedrag veranderen",
            "zijn attitude veranderen",
            "een attributie maken",
        ],
        antwoord=0,
        uitleg="Hij voegt een nieuwe gedachte toe die de spanning verzacht, zonder zijn gedrag of zijn houding echt te veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een roker die weet dat roken schadelijk is, besluit dat het gevaar sterk overdreven wordt. Welke manier van dissonantiereductie is dit?",
        opties=[
            "zijn attitude veranderen",
            "zijn gedrag veranderen",
            "een cognitie toevoegen",
            "een groepsnorm volgen",
        ],
        antwoord=0,
        uitleg="Hij past zijn houding tegenover roken aan, zodat ze bij zijn gedrag past.",
    ),
    dict(
        type="invultekst",
        vraag="De spanning die ontstaat als je iets doet wat niet bij je overtuiging past, heet cognitieve ...",
        antwoord=["dissonantie"],
        uitleg="Cognitieve dissonantie. Het tegendeel is cognitieve consonantie.",
    ),
    dict(
        type="waarofniet",
        vraag="Cognitieve dissonantie is een spanning die mensen graag kwijt willen, en daarom verandert ze gedrag of houding.",
        antwoord=True,
        uitleg="Waar. Dat is precies het verband met gedrag dat de fiche vraagt: de spanning drijft iemand tot een aanpassing.",
    ),
    dict(
        type="waarofniet",
        vraag="De eenvoudigste manier om dissonantie weg te werken is altijd het gedrag veranderen.",
        antwoord=False,
        uitleg="Niet waar. Gedrag veranderen is vaak het moeilijkst. Daarom veranderen mensen vaker hun houding of voegen ze een gedachte toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke drie situaties uit het dagelijks leven speelt dissonantiereductie volgens de fiche?",
        opties=[
            "na het maken van een keuze",
            "na het instemmen met een verzoek",
            "na het leveren van inspanningen",
            "na het verlaten van een groep",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie noemt de fiche met naam. Na elke keuze, elk ja en elke inspanning gaan wij praten goedmaken wat we deden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Elias twijfelde lang tussen twee richtingen, koos er een, en vertelt sindsdien vooral wat er mis is met de andere. Wat gebeurt hier?",
        opties=[
            "dissonantiereductie na het maken van een keuze",
            "dissonantiereductie na het leveren van inspanningen",
            "dissonantiereductie na het instemmen met een verzoek",
            "een fundamentele attributiefout over zijn keuze",
        ],
        antwoord=0,
        uitleg="Na een moeilijke keuze gaan mensen de gekozen kant mooier maken en de afgewezen kant slechter. Dat haalt de twijfel weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hanne heeft drie maanden zwaar getraind voor een loop die ze eigenlijk niet leuk vond, en zegt nu dat het de beste beslissing van haar jaar was. Wat gebeurt hier?",
        opties=[
            "dissonantiereductie na het leveren van inspanningen",
            "dissonantiereductie na het maken van een keuze",
            "dissonantiereductie na het instemmen met een verzoek",
            "sociale facilitatie tijdens het trainen",
        ],
        antwoord=0,
        uitleg="Wie veel moeite in iets steekt, gaat het waardevoller vinden. Anders was al die inspanning voor niets.",
    ),
    dict(
        type="invultekst",
        vraag="De rust die ontstaat als je denken en je doen bij elkaar passen, heet cognitieve ...",
        antwoord=["consonantie"],
        uitleg="Cognitieve consonantie. Consonant betekent samenklinkend, dissonant betekent wanklinkend.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie ja zegt op een verzoek waar hij eigenlijk niet achter staat, gaat het verzoek achteraf vaak redelijker vinden.",
        antwoord=True,
        uitleg="Waar. De fiche noemt dat dissonantiereductie na het instemmen met een verzoek. Het is ook de reden dat beïnvloedingstechnieken werken.",
    ),
    dict(
        type="waarofniet",
        vraag="Cognitieve dissonantie is het enige mentale proces dat de fiche bij de sociale cognitie rekent.",
        antwoord=False,
        uitleg="Niet waar. Er staan er drie: de attitude, de attributie en de cognitieve dissonantie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vrijwilliger die een hele zaterdag heeft helpen opruimen, zegt achteraf dat ze zich zelden zo nuttig voelde. Welk verschijnsel verklaart dat mee?",
        opties=[
            "dissonantiereductie na inspanning",
            "het omstandereffect in een groep",
            "de fundamentele attributiefout",
            "de normeringsfase van Tuckman",
        ],
        antwoord=0,
        uitleg="Veel moeite en weinig opbrengst wringt. Door de ervaring waardevoller te maken, verdwijnt die spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de theorie van Festinger nuttig om reclame te begrijpen?",
        opties=[
            "omdat een klant zijn aankoop achteraf goed wil praten",
            "omdat een klant altijd de goedkoopste keuze maakt",
            "omdat een klant nooit twijfelt tussen twee merken",
            "omdat een klant zich door een groep laat sturen",
        ],
        antwoord=0,
        uitleg="Na een duurdere aankoop zoekt een klant zelf argumenten dat het de goede keuze was. Dat is dissonantiereductie na een keuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een attitude en een cognitieve dissonantie?",
        opties=[
            "de eerste is een houding, de tweede een spanning",
            "de eerste is een spanning, de tweede een houding",
            "de eerste geldt voor groepen, de tweede voor personen",
            "de eerste kan veranderen, de tweede nooit",
        ],
        antwoord=0,
        uitleg="Een attitude is hoe je over iets denkt. Een dissonantie is de spanning als twee van die dingen niet samengaan.",
    ),
    dict(
        type="invultekst",
        vraag="Een nieuwe gedachte toevoegen om de spanning te verzachten, heet in de fiche een ... toevoegen.",
        antwoord=["cognitie"],
        uitleg="Een cognitie toevoegen. Dat is de derde manier, naast de attitude en het gedrag veranderen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de fasen in groepsvorming?",
        opties=[
            "Bruce Tuckman",
            "Leon Festinger",
            "Philip Zimbardo",
            "Muzafer Sherif",
        ],
        antwoord=0,
        uitleg="Tuckman. Zijn vijf fasen zijn forming, storming, norming, performing en adjourning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel fasen in groepsvorming noemt de fiche?",
        opties=[
            "vijf",
            "drie",
            "vier",
            "zes",
        ],
        antwoord=0,
        uitleg="Vijf, van de oriëntatiefase tot de afscheidsfase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet de eerste fase van Tuckman in het Nederlands?",
        opties=[
            "de oriëntatiefase",
            "de machtsfase",
            "de normeringsfase",
            "de prestatiefase",
        ],
        antwoord=0,
        uitleg="De oriëntatiefase, in het Engels forming. De leden kennen elkaar nog niet en zoeken hun plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nieuwe klas zit drie weken samen en er zijn botsingen over wie de leiding neemt. In welke fase zit de groep?",
        opties=[
            "de machtsfase",
            "de oriëntatiefase",
            "de normeringsfase",
            "de prestatiefase",
        ],
        antwoord=0,
        uitleg="De machtsfase, in het Engels storming. Daar wordt uitgevochten wie welke plaats krijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een team spreekt af hoe ze gaan werken en wat ze van elkaar verwachten. In welke fase zit de groep?",
        opties=[
            "de normeringsfase",
            "de machtsfase",
            "de prestatiefase",
            "de afscheidsfase",
        ],
        antwoord=0,
        uitleg="De normeringsfase, in het Engels norming. De groep maakt haar eigen regels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep werkt vlot samen en haalt haar doelen zonder veel overleg. In welke fase zit ze?",
        opties=[
            "de prestatiefase",
            "de normeringsfase",
            "de machtsfase",
            "de oriëntatiefase",
        ],
        antwoord=0,
        uitleg="De prestatiefase, in het Engels performing. De afspraken staan en de groep kan aan het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet de laatste fase van Tuckman?",
        opties=[
            "de afscheidsfase",
            "de prestatiefase",
            "de normeringsfase",
            "de oriëntatiefase",
        ],
        antwoord=0,
        uitleg="De afscheidsfase, in het Engels adjourning. De groep valt uiteen en neemt afscheid.",
    ),
    dict(
        type="invultekst",
        vraag="De Engelse naam van de machtsfase van Tuckman is ...",
        antwoord=["storming"],
        uitleg="Storming. De vijf Engelse namen zijn forming, storming, norming, performing en adjourning.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Tuckman is de machtsfase een probleem dat een goede groep overslaat.",
        antwoord=False,
        uitleg="Niet waar. De machtsfase hoort bij de ontwikkeling van een groep. Zonder die fase komen de afspraken van de normeringsfase er niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De normeringsfase komt bij Tuckman na de machtsfase en voor de prestatiefase.",
        antwoord=True,
        uitleg="Waar. Eerst botsen, dan afspreken, dan presteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ingroup?",
        opties=[
            "de groep waar iemand zichzelf bij rekent",
            "de groep waar iemand buiten valt",
            "de groep die de beslissingen neemt",
            "de groep die het werk uitvoert",
        ],
        antwoord=0,
        uitleg="De ingroup is wij, de outgroup is zij. Mensen beoordelen hun eigen groep bijna altijd gunstiger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is sociale facilitatie?",
        opties=[
            "beter presteren omdat anderen meekijken",
            "slechter presteren omdat anderen meekijken",
            "minder doen omdat de groep het overneemt",
            "meedoen omdat de groep het verwacht",
        ],
        antwoord=0,
        uitleg="Bij een eenvoudige of goed ingeoefende taak maakt publiek je beter. Dat heet sociale facilitatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is sociale belemmering?",
        opties=[
            "slechter presteren omdat anderen meekijken",
            "beter presteren omdat anderen meekijken",
            "minder doen omdat de groep het overneemt",
            "zwijgen omdat de groep het anders ziet",
        ],
        antwoord=0,
        uitleg="Bij een moeilijke of nieuwe taak maakt publiek je juist slechter. Dat heet sociale belemmering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gevorderde pianist speelt beter voor publiek, een beginner net slechter. Welke twee begrippen zie je hier?",
        opties=[
            "sociale facilitatie",
            "sociale belemmering",
            "social loafing",
            "groepsdenken",
        ],
        antwoord=[0, 1],
        uitleg="Bij de gevorderde werkt het publiek faciliterend, bij de beginner belemmerend. Het hangt af van hoe goed de taak al zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is social loafing?",
        opties=[
            "minder inzet leveren omdat je in een groep werkt",
            "beter presteren omdat je in een groep werkt",
            "je mening niet zeggen in een groep",
            "de groep volgen in haar beslissing",
        ],
        antwoord=0,
        uitleg="Social loafing of sociaal parasiteren: in een groep leunt iemand achterover, omdat zijn eigen bijdrage niet opvalt.",
    ),
    dict(
        type="invultekst",
        vraag="Het Nederlandse woord dat de fiche naast social loafing zet, is sociaal ...",
        antwoord=["parasiteren"],
        uitleg="Sociaal parasiteren. Het is het tegendeel van sociale facilitatie: in een groep neemt de inzet af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is groepsdenken?",
        opties=[
            "een groep neemt een slechte beslissing om eensgezind te blijven",
            "een groep neemt een goede beslissing door goed te overleggen",
            "een groep laat elk lid afzonderlijk beslissen",
            "een groep verdeelt het werk over al haar leden",
        ],
        antwoord=0,
        uitleg="Bij groepsdenken weegt de eensgezindheid zwaarder dan de kwaliteit van de beslissing. Twijfel wordt niet meer gezegd.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een vergadering denkt iemand dat het plan niet gaat lukken, maar zwijgt omdat iedereen enthousiast is. Welk verschijnsel is dit?",
        opties=[
            "groepsdenken",
            "social loafing",
            "sociale facilitatie",
            "sociale belemmering",
        ],
        antwoord=0,
        uitleg="Twijfel inslikken om de eensgezindheid niet te breken, is precies het risico van groepsdenken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een manier om groepsdenken tegen te gaan is iemand uitdrukkelijk de rol geven om tegen te spreken.",
        antwoord=True,
        uitleg="Waar. Als tegenspraak een officiële rol is, hoeft niemand zijn twijfel meer in te slikken.",
    ),
    dict(
        type="waarofniet",
        vraag="Social loafing en sociale belemmering betekenen hetzelfde.",
        antwoord=False,
        uitleg="Niet waar. Bij social loafing doet iemand minder omdat zijn aandeel niet opvalt. Bij sociale belemmering presteert hij slechter door de druk van publiek.",
    ),
]
