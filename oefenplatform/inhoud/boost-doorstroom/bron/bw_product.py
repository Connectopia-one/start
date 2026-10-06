# -*- coding: utf-8 -*-
"""De vragen voor "Producten, merken, prijsstrategie en distributie" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen, "marketing", tweede stuk: de indeling van de
consumptiegoederen, diepte en breedte van een assortiment, A-merken en
winkelmerken, het merkbeleid, de productlevenscyclus, de prijsstrategieën, de
intensiteit van de distributie, e-commerce en de push- en pullstrategie. Het
marktonderzoek en de marketingmix staan in [[bw_marketing]].

Deel 1 gaat over de soorten goederen, het assortiment en de merken.
Deel 2 gaat over de productlevenscyclus, de prijsstrategieën en de distributie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een duurzaam goed?",
        opties=[
            "Een wasmachine",
            "Een brood van de bakker",
            "Een krant van deze ochtend",
            "Een fles melk uit de koelkast",
        ],
        antwoord=0,
        uitleg="Duurzame goederen gaan lang mee en je gebruikt ze meermaals. Niet-duurzame goederen zijn na één of enkele keren op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een niet-duurzaam goed?",
        opties=[
            "Een brood",
            "Een koelkast voor de keuken",
            "Een fiets om naar school te gaan",
            "Een laptop voor het schoolwerk thuis",
        ],
        antwoord=0,
        uitleg="Een brood is na een dag of twee op. Een koelkast, een fiets en een laptop gaan jaren mee en zijn dus duurzaam.",
    ),
    dict(
        type="waarofniet",
        vraag="Industriële goederen koopt een bedrijf om er zelf mee te werken.",
        antwoord=True,
        uitleg="Industriële goederen zijn grondstoffen, machines en onderdelen voor de productie. Consumentengoederen zijn voor particulieren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een convenience goed is een aankoop waarvoor je lang gaat vergelijken.",
        antwoord=False,
        uitleg="Net niet: een convenience goed koop je zonder nadenken, zoals brood of een krant. Vergelijken doe je bij een shopping goed.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je goederen die je niet zoekt en toch soms nodig hebt, zoals een brandblusser?",
        antwoord=["unsought", "unsought goederen", "unsought goods"],
        uitleg="Dat zijn unsought goederen. Een verzekering of een grafzerk horen er ook bij: niemand gaat er met plezier naar op zoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn convenience goederen? Duid alles aan wat juist is.",
        opties=[
            "Brood",
            "Een krant",
            "Melk",
            "Een eetkamertafel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Convenience goederen koop je vaak, dicht bij huis en zonder vergelijken. Voor een eetkamertafel ga je wel rondkijken: dat is een shopping goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een shopping goed?",
        opties=[
            "Een jas",
            "Een brood bij de bakker",
            "Een krant in de dagbladhandel",
            "Een brandblusser voor de garage",
        ],
        antwoord=0,
        uitleg="Voor een jas vergelijk je prijs, kleur en pasvorm in meerdere winkels. Dat is precies wat een shopping goed kenmerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een speciality goed?",
        opties=[
            "Een duur horloge",
            "Een pak koffie in de supermarkt",
            "Een paar sokken in de kledingwinkel",
            "Een brood in de bakkerij om de hoek",
        ],
        antwoord=0,
        uitleg="Voor een speciality goed wil de koper precies dat ene merk en rijdt hij er desnoods voor om. De andere drie koop je waar je toch al bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de breedte van een assortiment?",
        opties=[
            "Het aantal productgroepen",
            "Het aantal varianten binnen één groep",
            "Het aantal winkels dat het merk verkoopt",
            "Het aantal klanten dat het product koopt",
        ],
        antwoord=0,
        uitleg="Breedte is hoeveel verschillende soorten een winkel aanbiedt: brood, zuivel, groenten, drank. Diepte is hoeveel varianten er binnen één soort staan.",
    ),
    dict(
        type="waarofniet",
        vraag="De diepte van een assortiment is het aantal varianten binnen één groep.",
        antwoord=True,
        uitleg="Twaalf soorten yoghurt naast elkaar is een diep assortiment. Twaalf verschillende productgroepen is een breed assortiment.",
    ),
    dict(
        type="waarofniet",
        vraag="Een A-merk is altijd goedkoper dan een winkelmerk.",
        antwoord=False,
        uitleg="Meestal is het omgekeerd. Een A-merk is het merk van de producent, met reclame en een vaste reputatie, en kost daardoor gewoonlijk meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten winkelmerken bestaan er? Duid alles aan wat juist is.",
        opties=[
            "Standaard",
            "Budget",
            "Bio",
            "A-merk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een winkelketen zet vaak drie eigen lijnen naast elkaar: een standaardlijn, een goedkope budgetlijn en een biolijn. Een A-merk is juist geen winkelmerk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een A-merk?",
        opties=[
            "Het merk van de producent",
            "Het goedkoopste merk in het rek",
            "Het eigen merk van de winkelketen",
            "Het merk met de kleinste verpakking erbij",
        ],
        antwoord=0,
        uitleg="Een A-merk is van de fabrikant zelf, wordt in veel winkels verkocht en krijgt eigen reclame. Een winkelmerk is van de keten en staat enkel daar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een lijnextensie?",
        opties=[
            "Een nieuwe variant",
            "Een bestaand merk in een nieuwe groep",
            "Een tweede eigen merk in dezelfde groep",
            "Een nieuw merk voor een nieuwe productgroep",
        ],
        antwoord=0,
        uitleg="Bij een lijnextensie komt er onder hetzelfde merk een variant bij in dezelfde productgroep: een nieuwe smaak, een ander formaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het gebruiken van een bestaand merk in een helemaal nieuwe productgroep?",
        antwoord=["merkextensie", "een merkextensie"],
        uitleg="Dat is een merkextensie. Een chocolademerk dat ijs gaat maken onder dezelfde naam, doet precies dat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke keuzes horen bij het merkbeleid? Duid alles aan wat juist is.",
        opties=[
            "Een lijnextensie",
            "Een merkextensie",
            "Multibrands",
            "De kostprijs van de grondstof",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het merkbeleid kiest tussen een variant onder hetzelfde merk, hetzelfde merk in een nieuwe groep, meerdere eigen merken naast elkaar, of een volledig nieuw merk. Een grondstofprijs is geen merkkeuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent multibrands?",
        opties=[
            "Twee eigen merken naast elkaar",
            "Eén merk voor alle producten samen",
            "Een merk dat in meerdere landen verkocht wordt",
            "Een merk dat door twee bedrijven gedeeld wordt",
        ],
        antwoord=0,
        uitleg="Bij multibrands zet een bedrijf verschillende eigen merken in dezelfde productgroep, elk voor een andere doelgroep. Zo neemt het meer plaats in het rek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een chocolademerk brengt ijs uit onder dezelfde naam. Wat is dat?",
        opties=[
            "Een merkextensie",
            "Een lijnextensie van het merk",
            "Een multibrandstrategie van het merk",
            "Een nieuw merk voor een nieuwe groep",
        ],
        antwoord=0,
        uitleg="Het merk blijft hetzelfde, maar de productgroep is nieuw: chocolade wordt ijs. Dat is een merkextensie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel heeft twaalf soorten yoghurt van hetzelfde merk. Wat zegt dat over het assortiment?",
        opties=[
            "Het is diep",
            "Het is breed in die winkel",
            "Het is zowel breed als ondiep daar",
            "Het zegt niets over het assortiment zelf",
        ],
        antwoord=0,
        uitleg="Veel varianten binnen één productgroep is diepte. Zou de winkel ook brood, drank en groenten verkopen, dan is ze ook breed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet een winkel een budgetmerk naast een A-merk? Duid alles aan wat juist is.",
        opties=[
            "Om elke beurs te bedienen",
            "Om prijsbewuste klanten te houden",
            "Om zelf meer marge te maken",
            "Om geen btw te moeten aanrekenen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Met beide in het rek verliest de winkel geen klanten aan een goedkopere keten, en op haar eigen merk houdt ze doorgaans meer over. De btw blijft dezelfde.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke fase komt na de introductiefase van een product?",
        opties=[
            "De groeifase",
            "De neergangsfase van het product",
            "De ontwikkelingsfase van het product",
            "De volwassenheidsfase van het product",
        ],
        antwoord=0,
        uitleg="De cyclus loopt van ontwikkeling naar introductie, groei, volwassenheid en neergang. Na de introductie volgt dus de groei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is prijsdiscriminatie?",
        opties=[
            "Een andere prijs per groep klanten",
            "Een andere prijs volgens het seizoen of het uur",
            "Een prijs die uit de kostprijs met een marge volgt",
            "Een hoge prijs om kwaliteit te laten uitschijnen",
        ],
        antwoord=0,
        uitleg="Bij prijsdiscriminatie betaalt de ene groep minder dan de andere voor net hetzelfde: studenten, senioren, kinderen. Bij prijsdifferentiatie hangt de prijs af van tijd, plaats of hoeveelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="In de neergangsfase daalt de verkoop van een product.",
        antwoord=True,
        uitleg="De vraag loopt terug, vaak omdat er iets nieuwers is. Het bedrijf kiest dan tussen vernieuwen of het product stoppen.",
    ),
    dict(
        type="waarofniet",
        vraag="In de volwassenheidsfase groeit de verkoop het snelst.",
        antwoord=False,
        uitleg="Dat gebeurt in de groeifase. In de volwassenheidsfase blijft de verkoop hoog maar vlak, en wordt de concurrentie het scherpst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de fase van de productlevenscyclus waarin de verkoop het snelst stijgt?",
        antwoord=["groeifase", "de groeifase", "groei"],
        uitleg="Dat is de groeifase. Ze volgt op de introductie en gaat over in de volwassenheidsfase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fases horen bij de productlevenscyclus? Duid alles aan wat juist is.",
        opties=[
            "De introductiefase",
            "De groeifase",
            "De neergangsfase",
            "De aankoopfase",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vijf fases zijn ontwikkeling, introductie, groei, volwassenheid en neergang. Een aankoopfase hoort niet in dat rijtje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een afroomstrategie?",
        opties=[
            "Hoog beginnen en later dalen",
            "Laag beginnen om snel te groeien",
            "De prijs van de concurrent overnemen",
            "De kostprijs met een vaste marge verhogen",
        ],
        antwoord=0,
        uitleg="Een afroomstrategie vraagt eerst een hoge prijs aan wie het product als eerste wil, en verlaagt die daarna stap voor stap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een penetratiestrategie?",
        opties=[
            "Laag beginnen om snel te groeien",
            "Hoog beginnen en de prijs later verlagen",
            "Een hoge prijs houden om luxe uit te stralen",
            "Een verschillende prijs vragen per groep klanten",
        ],
        antwoord=0,
        uitleg="Met een lage introductieprijs haalt een bedrijf snel veel klanten binnen. Daarna kan het de prijs voorzichtig optrekken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een afroomstrategie past bij een nieuw product waar nog geen alternatief voor is.",
        antwoord=True,
        uitleg="Zolang niemand hetzelfde aanbiedt, zijn er kopers die de hoge prijs willen betalen. Komt er concurrentie, dan zakt de prijs.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een penetratiestrategie begin je met een hoge prijs.",
        antwoord=False,
        uitleg="Net omgekeerd: je begint laag om snel marktaandeel te pakken. Hoog beginnen is de afroomstrategie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is cost-plus pricing?",
        opties=[
            "De kostprijs plus een marge",
            "De prijs die de klant wil betalen",
            "De prijs van de sterkste concurrent",
            "Een hoge prijs om kwaliteit te tonen",
        ],
        antwoord=0,
        uitleg="Bij cost-plus rekent een bedrijf zijn kostprijs uit en zet daar een percentage winst bovenop. Simpel, maar het kijkt niet naar de klant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is consumer-based pricing?",
        opties=[
            "Wat de klant wil betalen",
            "De kostprijs met een marge erbij",
            "De prijs van de concurrent volgen",
            "Een vaste prijs voor elk product gelijk",
        ],
        antwoord=0,
        uitleg="Hier vertrekt de prijs van de waarde die de klant eraan geeft. Een bedrijf meet die met marktonderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is competitor-based pricing?",
        opties=[
            "Kijken naar de concurrent",
            "De eigen kostprijs als vertrekpunt nemen",
            "Vragen wat de klant ervoor wil betalen",
            "Een hoge prijs zetten om luxe uit te stralen",
        ],
        antwoord=0,
        uitleg="Het bedrijf bepaalt zijn prijs tegenover die van de concurrenten: er net onder, gelijk, of er bewust boven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is premium pricing?",
        opties=[
            "Een hoge prijs als signaal",
            "Een lage prijs om snel te groeien",
            "Een prijs gelijk aan die van de concurrent",
            "Een prijs die enkel de kosten moet dekken",
        ],
        antwoord=0,
        uitleg="Een bewust hoge prijs zegt tegen de klant: dit is kwaliteit. Dat werkt alleen als het product en het merk dat ook waarmaken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de strategie waarbij een producent zijn product met kortingen bij de winkelier binnenduwt?",
        antwoord=["push", "pushstrategie", "de pushstrategie"],
        uitleg="Dat is de pushstrategie: de producent richt zich op de tussenhandel. Bij een pullstrategie spreekt hij de consument aan, zodat die ernaar vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn prijsstrategieën? Duid alles aan wat juist is.",
        opties=[
            "Cost-plus pricing",
            "Consumer-based pricing",
            "Competitor-based pricing",
            "Voorraad-based pricing",
        ],
        antwoord=[0, 1, 2],
        uitleg="Naast deze drie bestaat ook premium pricing. Voorraad-based pricing bestaat niet als strategie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is intensieve distributie?",
        opties=[
            "In zoveel punten als mogelijk",
            "In een beperkt aantal gekozen winkels",
            "In één winkel per stad of per streek",
            "Enkel via de eigen webshop van het merk",
        ],
        antwoord=0,
        uitleg="Bij intensieve distributie moet het product overal liggen: supermarkt, krantenwinkel, tankstation. Dat past bij convenience goederen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van distributie-intensiteit bestaan er? Duid alles aan wat juist is.",
        opties=[
            "Intensieve distributie",
            "Selectieve distributie",
            "Exclusieve distributie",
            "Gratis distributie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Van overal verkrijgbaar, over een gekozen aantal winkels, tot één verkooppunt per gebied. Gratis distributie is geen vorm van intensiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is e-commerce?",
        opties=[
            "Verkopen via het internet",
            "Verkopen aan andere bedrijven",
            "Verkopen met een korting per stuk",
            "Verkopen via één winkel per streek",
        ],
        antwoord=0,
        uitleg="E-commerce is handel langs een website of app, met levering aan huis of ophaling in een punt. Het verandert vooral de P van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij een pullstrategie? Duid alles aan wat juist is.",
        opties=[
            "Reclame naar de consument",
            "Een sterke merknaam",
            "De klant vraagt ernaar",
            "Korting aan de winkelier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij pull trekt de producent de consument aan, zodat die het merk in de winkel komt vragen en de winkelier het wel moet aanbieden. Kortingen aan de winkelier horen bij push.",
    ),
]
