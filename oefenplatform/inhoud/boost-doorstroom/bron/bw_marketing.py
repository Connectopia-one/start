# -*- coding: utf-8 -*-
"""De vragen voor "Marktonderzoek, doelgroep en de marketingmix" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen, "marketing": het doel en de vormen van marktonderzoek
(primair, secundair, kwantitatief en kwalitatief), het bepalen van een doelgroep
via marktsegmentatie, het verschil tussen B2B, C2B, B2C en C2C, en de
onderdelen van de marketingmix (de 4 P's en de 4 C's). De producten, merken,
prijsstrategieën en distributie staan in [[bw_product]].

Deel 1 gaat over marktonderzoek, segmentatie en doelgroep.
Deel 2 gaat over de vier soorten handelsrelaties en over de marketingmix.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van een marktonderzoek?",
        opties=[
            "De markt leren kennen",
            "De boekhouding van het jaar afsluiten",
            "De lonen van het personeel vastleggen",
            "De belastingen van het bedrijf berekenen",
        ],
        antwoord=0,
        uitleg="Een marktonderzoek brengt in kaart wie de klanten zijn, wat ze willen en wat de concurrenten doen. Zo kan een bedrijf beslissen met minder gokwerk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is primair marktonderzoek?",
        opties=[
            "Zelf gegevens verzamelen",
            "Cijfers gebruiken die al bestaan",
            "Een rapport van een studiebureau lezen",
            "De jaarverslagen van de concurrenten bekijken",
        ],
        antwoord=0,
        uitleg="Bij primair onderzoek haalt het bedrijf de gegevens zelf op: een enquête, een gesprek, een test. Het kost meer tijd en geld, maar past precies bij de vraag.",
    ),
    dict(
        type="waarofniet",
        vraag="Secundair marktonderzoek gebruikt gegevens die al bestaan.",
        antwoord=True,
        uitleg="Bij secundair onderzoek werk je met cijfers van anderen: de overheid, een studiebureau, een vakblad. Dat is sneller en goedkoper.",
    ),
    dict(
        type="waarofniet",
        vraag="Kwalitatief onderzoek werkt met grote aantallen cijfers.",
        antwoord=False,
        uitleg="Dat is net kwantitatief onderzoek. Kwalitatief onderzoek werkt met weinig mensen maar diepe gesprekken, om te weten waarom iemand iets doet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je onderzoek waarbij een bedrijf de gegevens zelf gaat ophalen?",
        antwoord=["primair", "primair marktonderzoek", "primair onderzoek"],
        uitleg="Dat is primair marktonderzoek. Werkt het met bestaande gegevens, dan is het secundair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn primair marktonderzoek? Duid alles aan wat juist is.",
        opties=[
            "Een eigen enquête",
            "Een gesprek met klanten",
            "Een test in de winkel",
            "Cijfers van de overheid lezen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat het bedrijf zelf opzet, is primair. Bestaande overheidscijfers gebruiken is secundair onderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn secundair marktonderzoek? Duid alles aan wat juist is.",
        opties=[
            "Cijfers van de overheid",
            "Een rapport van een studiebureau",
            "Een artikel in een vakblad",
            "Zelf een enquête afnemen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Secundair onderzoek leunt op wat anderen al verzameld hebben. Een eigen enquête is primair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kwantitatief onderzoek?",
        opties=[
            "Onderzoek met cijfers",
            "Een lang gesprek met enkele klanten",
            "Een groepsgesprek over een nieuw product",
            "Een observatie van hoe mensen door de winkel gaan",
        ],
        antwoord=0,
        uitleg="Kwantitatief onderzoek meet: hoeveel mensen, hoeveel procent, hoeveel keer. Het antwoord is een getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is kwalitatief onderzoek?",
        opties=[
            "Een diepte-interview",
            "Een enquête bij duizend mensen",
            "Een telling van de klanten per uur",
            "Een vergelijking van de omzetcijfers per maand",
        ],
        antwoord=0,
        uitleg="Een diepte-interview zoekt naar het waarom achter een keuze. Dat levert geen cijfers op, maar inzicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een enquête bij duizend mensen is kwantitatief onderzoek.",
        antwoord=True,
        uitleg="Met zoveel antwoorden kan je percentages berekenen en groepen vergelijken. Dat is meten, dus kwantitatief.",
    ),
    dict(
        type="waarofniet",
        vraag="Primair onderzoek is altijd goedkoper dan secundair onderzoek.",
        antwoord=False,
        uitleg="Het is meestal net duurder, want het bedrijf moet alles zelf opzetten. Secundair onderzoek gebruikt werk dat al gedaan is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is marktsegmentatie?",
        opties=[
            "De markt in groepen delen",
            "De prijs van een product vastleggen",
            "De winkel over meer steden spreiden",
            "De omzet per maand in een tabel zetten",
        ],
        antwoord=0,
        uitleg="Segmenteren is de markt opsplitsen in groepen die op elkaar lijken. Daarna kiest het bedrijf welke groep het wil bedienen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke kenmerken kan een bedrijf segmenteren? Duid alles aan wat juist is.",
        opties=[
            "Leeftijd",
            "Woonplaats",
            "Levensstijl",
            "De kleur van de verpakking",
        ],
        antwoord=[0, 1, 2],
        uitleg="Segmenteren gebeurt op kenmerken van mensen: leeftijd, gezinssamenstelling, woonplaats, inkomen, levensstijl, gedrag. De verpakking is een keuze van het bedrijf zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een doelgroep?",
        opties=[
            "De groep die je wil bereiken",
            "Alle inwoners van het hele land",
            "Het personeel dat in de winkel werkt",
            "De leveranciers waarmee je samenwerkt",
        ],
        antwoord=0,
        uitleg="Uit de segmenten kiest een bedrijf er één of enkele uit: dat is de doelgroep. Daarop stemt het zijn product, prijs, plaats en promotie af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het opdelen van een markt in groepen met dezelfde kenmerken?",
        antwoord=["marktsegmentatie", "segmentatie"],
        uitleg="Dat is marktsegmentatie. De groep die het bedrijf daarna kiest, is de doelgroep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kiest een bedrijf een doelgroep? Duid alles aan wat juist is.",
        opties=[
            "De boodschap past beter",
            "Het reclamegeld rendeert meer",
            "Het product sluit beter aan",
            "Zo moet het geen btw betalen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wie weet voor wie hij werkt, maakt een scherper product en een scherpere boodschap, en verspilt minder reclamegeld. Met de btw heeft het niets te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een merk maakt schoenen speciaal voor lopers. Wat is dat?",
        opties=[
            "Een gekozen doelgroep",
            "Een vorm van secundair onderzoek",
            "Een kwalitatief onderzoek bij klanten",
            "Een handelsrelatie tussen twee bedrijven",
        ],
        antwoord=0,
        uitleg="Het merk kiest één segment, de lopers, en stemt zijn product daarop af. Dat is een doelgroepkeuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als een bedrijf geen doelgroep kiest?",
        opties=[
            "De boodschap raakt niemand echt",
            "Het verkoopt automatisch aan iedereen",
            "Het moet geen marktonderzoek meer doen",
            "Het kan zijn prijzen vrij bepalen per klant",
        ],
        antwoord=0,
        uitleg="Een boodschap voor iedereen is een boodschap voor niemand in het bijzonder. Het bedrijf valt dan nergens op en verspilt zijn reclamebudget.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer doet een bedrijf het best marktonderzoek?",
        opties=[
            "Voor het een nieuw product start",
            "Pas nadat het product gefaald heeft",
            "Alleen bij het afsluiten van het boekjaar",
            "Enkel wanneer de belastingdienst dat vraagt",
        ],
        antwoord=0,
        uitleg="Onderzoek vooraf kost geld, maar een mislukte lancering kost veel meer. Daarom test een bedrijf eerst of er vraag is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel vraagt vijftig klanten een cijfer van 1 tot 10 voor de service. Welk soort onderzoek is dat?",
        opties=[
            "Kwantitatief",
            "Kwalitatief, want het gaat over een mening",
            "Secundair, want de cijfers bestonden al eerder",
            "Geen onderzoek, want vijftig mensen is te weinig",
        ],
        antwoord=0,
        uitleg="Er komen cijfers uit die je kan samenvatten in een gemiddelde, dus is het kwantitatief. En omdat de winkel ze zelf ophaalt, is het ook primair.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent B2B?",
        opties=[
            "Bedrijf aan bedrijf",
            "Bedrijf aan consument",
            "Consument aan consument",
            "Consument aan bedrijf",
        ],
        antwoord=0,
        uitleg="B2B staat voor business to business: een bedrijf verkoopt aan een ander bedrijf, bijvoorbeeld een groothandel aan een winkel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent B2C?",
        opties=[
            "Bedrijf aan consument",
            "Bedrijf aan bedrijf",
            "Consument aan bedrijf",
            "Consument aan consument",
        ],
        antwoord=0,
        uitleg="B2C staat voor business to consumer: een bedrijf verkoopt rechtstreeks aan particulieren, zoals een bakker aan een gezin.",
    ),
    dict(
        type="waarofniet",
        vraag="C2C is handel tussen twee consumenten.",
        antwoord=True,
        uitleg="Consumer to consumer: twee particulieren onder elkaar, bijvoorbeeld via een tweedehandsplatform.",
    ),
    dict(
        type="waarofniet",
        vraag="C2B betekent dat een bedrijf aan een consument verkoopt.",
        antwoord=False,
        uitleg="Dat is net B2C. Bij C2B levert de consument iets aan een bedrijf, bijvoorbeeld iemand die zijn foto's of zijn mening verkoopt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke afkorting gebruik je voor handel tussen twee consumenten?",
        antwoord=["C2C", "c2c"],
        uitleg="C2C, van consumer to consumer. Het bekendste voorbeeld zijn de tweedehandsplatformen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn B2B? Duid alles aan wat juist is.",
        opties=[
            "Een groothandel levert aan een winkel",
            "Een drukkerij print voor een school",
            "Een poetsbedrijf werkt voor een kantoor",
            "Een bakker verkoopt brood aan een gezin",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij B2B zijn beide partijen organisaties. Zodra er een particulier koopt, is het B2C.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een voorbeeld van C2C?",
        opties=[
            "Een tweedehandsplatform",
            "Een webshop van een groot merk",
            "Een groothandel die winkels bedient",
            "Een school die drukwerk laat maken",
        ],
        antwoord=0,
        uitleg="Op een tweedehandsplatform verkoopt een particulier aan een andere particulier. Het platform zelf is enkel de tussenschakel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een voorbeeld van C2B?",
        opties=[
            "Een klant verkoopt zijn foto's",
            "Een merk verkoopt schoenen in zijn webshop",
            "Een groothandel levert dranken aan een café",
            "Een gezin koopt brood in de bakkerij om de hoek",
        ],
        antwoord=0,
        uitleg="Bij C2B biedt een particulier iets aan een bedrijf aan: foto's, een mening in een panel, of werk als freelancer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de vier P's van de marketingmix? Duid alles aan wat juist is.",
        opties=[
            "Product",
            "Prijs",
            "Promotie",
            "Personeel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vier P's zijn product, prijs, plaats en promotie. Personeel hoort er niet bij in deze indeling.",
    ),
    dict(
        type="waarofniet",
        vraag="De P van plaats gaat over waar de klant het product kan krijgen.",
        antwoord=True,
        uitleg="Plaats is het hele kanaal: de winkel, de webshop, de levering aan huis, de automaat. De vraag is hoe het product bij de klant komt.",
    ),
    dict(
        type="waarofniet",
        vraag="De vier C's bekijken de marketingmix vanuit het bedrijf.",
        antwoord=False,
        uitleg="Ze bekijken dezelfde mix juist vanuit de klant: wat is het mij waard, wat kost het mij, hoe makkelijk kom ik eraan, hoe praat je met mij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke C hoort bij de P van prijs?",
        opties=[
            "Cost",
            "Customer value",
            "Convenience voor de klant",
            "Communication met de klant",
        ],
        antwoord=0,
        uitleg="Cost is wat het de klant kost. Dat is meer dan de prijs alleen: ook de verplaatsing, de tijd en het gebruik erna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke C hoort bij de P van plaats?",
        opties=[
            "Convenience",
            "Cost voor de klant",
            "Customer value voor de klant",
            "Communication met de klant erover",
        ],
        antwoord=0,
        uitleg="Convenience is het gemak waarmee de klant eraan komt. Een webshop met levering aan huis scoort daar hoger dan één winkel ver weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke C hoort bij de P van promotie?",
        opties=[
            "Communication",
            "Cost voor de klant",
            "Convenience voor de klant",
            "Customer value voor de klant",
        ],
        antwoord=0,
        uitleg="Promotie vertrekt van het bedrijf dat zendt, communication van een gesprek in twee richtingen, waarin de klant ook antwoordt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke C hoort bij de P van product? Schrijf het Engelse woord.",
        antwoord=["customer", "customer value", "consumer"],
        uitleg="Customer value: niet wat het bedrijf maakt, maar wat het voor de klant waard is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de P van promotie? Duid alles aan wat juist is.",
        opties=[
            "Reclame",
            "Sociale media",
            "Een actie in de winkel",
            "De ligging van de winkel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Promotie is alles waarmee een bedrijf zijn aanbod bekendmaakt: reclame, sociale media, kortingsacties, een beurs. De ligging hoort bij de P van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom spreken marketeers naast de vier P's ook van de vier C's?",
        opties=[
            "Ze kijken door de ogen van de klant",
            "Omdat de vier P's verboden zijn geraakt",
            "Omdat er vier letters bij moesten komen",
            "Omdat de vier C's enkel voor webshops gelden",
        ],
        antwoord=0,
        uitleg="Het is dezelfde mix, maar van de andere kant bekeken. Dat helpt een bedrijf om niet enkel aan zijn eigen product te denken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de P van plaats? Duid alles aan wat juist is.",
        opties=[
            "De winkel",
            "De webshop",
            "De levering aan huis",
            "De prijs per stuk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Plaats gaat over alle manieren waarop het product bij de klant komt. De prijs is een eigen P.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bepaalt een bedrijf eerst zijn strategie en dan zijn marketingmix?",
        opties=[
            "De mix volgt uit de keuzes",
            "Omdat de mix niets met de klant doet",
            "Omdat de wet die orde voorschrijft aan bedrijven",
            "Omdat de prijs pas na het boekjaar vastgelegd mag worden",
        ],
        antwoord=0,
        uitleg="Eerst kiest het bedrijf zijn doelgroep en zijn eigen plaats in de markt. Pas dan weet het welk product, welke prijs, welk kanaal en welke boodschap daarbij horen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een webshop verkoopt kleren rechtstreeks aan gezinnen. Welke vorm is dat?",
        opties=[
            "B2C",
            "B2B tussen twee bedrijven",
            "C2C tussen twee particulieren",
            "C2B van particulier naar bedrijf",
        ],
        antwoord=0,
        uitleg="Een bedrijf verkoopt aan particulieren, dus business to consumer. Of dat in een winkel of online gebeurt, verandert daar niets aan.",
    ),
]
