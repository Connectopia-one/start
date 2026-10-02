# -*- coding: utf-8 -*-
"""Beeldvorming, standplaatsgebondenheid en betekenisgeving.

Uit de leerinhoud over beeldvorming en over de relatie verleden, heden en
toekomst: hoe een beeld van het verleden ontstaat, waarom twee mensen hetzelfde
verleden anders zien, en welke betekenis een samenleving aan haar verleden geeft
met monumenten, herdenkingen en erfgoed.

Deel 1 gaat over beeldvorming en standplaatsgebondenheid. Deel 2 gaat over
herinnering, monumenten, misbruik van geschiedenis en de blik vooruit.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is beeldvorming over het verleden?",
        opties=[
            "het beeld dat mensen van een tijd of een groep hebben",
            "het aantal bronnen dat van een periode bewaard is",
            "de juiste volgorde van de gebeurtenissen",
            "de wetenschap die munten en zegels onderzoekt",
        ],
        antwoord=0,
        uitleg="Dat beeld komt uit handboeken, films, verhalen thuis en beelden op straat, en het verandert mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waardoor wordt je beeld van het verleden gevormd?",
        opties=[
            "door handboeken, films en reeksen",
            "door verhalen in je gezin en je omgeving",
            "door uitsluitend wetenschappelijk onderzoek",
            "door uitsluitend bronnen uit die tijd zelf",
        ],
        antwoord=[0, 1],
        uitleg="Wie zich dat niet bewust is, houdt zijn eigen beeld voor de geschiedenis zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt de blik van een mens op de wereld standplaatsgebonden?",
        opties=[
            "zijn tijd, zijn afkomst, zijn geloof en zijn belang",
            "de taal waarin hij de bronnen heeft gelezen",
            "de plaats waar hij zijn eigen boeken bewaart",
            "het aantal bronnen dat van die tijd bewaard is",
        ],
        antwoord=0,
        uitleg="Die vier bepalen mee wat je ziet en wat je vanzelfsprekend vindt, ook als je eerlijk wil zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beschrijven twee ooggetuigen dezelfde gebeurtenis anders?",
        opties=[
            "elk van hen stond elders en had een ander belang",
            "een van de twee moet noodzakelijk liegen",
            "een ooggetuige vergeet na een tijd altijd alles",
            "de gebeurtenis is twee keer gebeurd",
        ],
        antwoord=0,
        uitleg="Verschil tussen getuigen is geen bewijs van leugen, maar een aanwijzing dat je verder moet kijken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bekijken van een gebeurtenis vanuit verschillende standpunten?",
        antwoord=["multiperspectiviteit", "meerdere perspectieven", "multiperspectivisme"],
        uitleg="Een staking bekijk je dan door de ogen van de arbeider, de fabrikant en de burgemeester samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is eurocentrisme in de geschiedschrijving?",
        opties=[
            "Europa als maatstaf voor het hele verhaal nemen",
            "Europa volledig uit het verhaal weglaten",
            "alle werelddelen evenveel plaats in het verhaal geven",
            "enkel over de eigen streek en stad schrijven",
        ],
        antwoord=0,
        uitleg="Zo wordt de dekolonisatie het verhaal van Europa dat weggaat, in plaats van volken die zichzelf bevrijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een stereotype?",
        opties=[
            "een vast, vereenvoudigd beeld van een hele groep",
            "een bron waarvan de auteur onbekend gebleven is",
            "een gebeurtenis die zich steeds blijft herhalen",
            "een oude drukletter uit een letterkast",
        ],
        antwoord=0,
        uitleg="Het is handig voor je hoofd en gevaarlijk voor je besluit, want het wist alle verschillen uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over historische empathie kloppen?",
        opties=[
            "je probeert te begrijpen waarom mensen toen zo handelden",
            "je plaatst hun keuzes in de kennis en de normen van hun tijd",
            "je keurt daarmee alles goed wat zij toen gedaan hebben",
            "je beoordeelt hen enkel met de normen van vandaag",
        ],
        antwoord=[0, 1],
        uitleg="Begrijpen is niet goedkeuren. Je kan iets verklaren en het tegelijk scherp afkeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verandert het beeld van een periode in de loop van de tijd?",
        opties=[
            "nieuwe vragen en nieuwe bronnen leveren een ander beeld",
            "het verleden zelf verandert met de jaren mee",
            "historici veranderen de bronnen die ze willen gebruiken",
            "oude handboeken verdwijnen uit de bibliotheken",
        ],
        antwoord=0,
        uitleg="Over het koloniale verleden wordt vandaag anders geschreven dan vijftig jaar geleden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een handboek geschiedenis kloppen?",
        opties=[
            "het maakt keuzes over wat er in en uit gaat",
            "het is geschreven in een bepaalde tijd met bepaalde vragen",
            "het geeft het verleden volledig en neutraal weer",
            "het is nooit bruikbaar om het verleden te leren kennen",
        ],
        antwoord=[0, 1],
        uitleg="Een oud handboek is daarom zelf een bron over de beeldvorming van zijn eigen tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een film over de Tweede Wereldoorlog uit 1960. Waarvoor is die vooral een bron?",
        opties=[
            "voor de manier waarop men in 1960 naar die oorlog keek",
            "voor de precieze toedracht van de veldslagen in die oorlog",
            "voor de aantallen slachtoffers van de oorlog",
            "voor de teksten van de verdragen van die jaren",
        ],
        antwoord=0,
        uitleg="Wie in zo'n film de held is en wie ontbreekt, zegt alles over het jaar waarin hij gemaakt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig te weten wie een geschiedenis geschreven heeft?",
        opties=[
            "de auteur kiest wat hij vertelt en van welke kant",
            "de auteur bepaalt wat er in het verleden gebeurd is",
            "de auteur maakt het boek daardoor altijd onbetrouwbaar",
            "de auteur mag dan geen bronnen meer gebruiken",
        ],
        antwoord=0,
        uitleg="Een Belgisch en een Congolees handboek over 1960 vertellen hetzelfde jaar met een andere nadruk.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee eerlijke getuigen kunnen dezelfde gebeurtenis verschillend beschrijven.",
        antwoord=True,
        uitleg="Zij stonden elders, zagen iets anders en onthielden iets anders. Dat hoort bij menselijke getuigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het beeld dat men van een periode heeft, blijft door de eeuwen gelijk.",
        antwoord=False,
        uitleg="Nieuwe vragen, nieuwe bronnen en een nieuwe tijd leveren telkens een ander beeld op.",
    ),
    dict(
        type="waarofniet",
        vraag="Historische empathie betekent dat je het gedrag van mensen uit het verleden goedkeurt.",
        antwoord=False,
        uitleg="Het betekent begrijpen waarom zij zo handelden. Beoordelen mag en moet daarnaast gebeuren.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook een historicus van vandaag is standplaatsgebonden.",
        antwoord=True,
        uitleg="Daarom legt hij zijn vragen, zijn bronnen en zijn werkwijze open voor anderen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een handboek geschiedenis geeft het verleden volledig weer.",
        antwoord=False,
        uitleg="Het moet kiezen: wat in een paragraaf past, blijft; de rest valt weg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een vast en vereenvoudigd beeld van een hele groep mensen?",
        antwoord=["een stereotype", "stereotype", "stereotiep"],
        uitleg="Wordt er ook nog een waardeoordeel aan gekoppeld, dan spreekt men van een vooroordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest twee handboeken over de onafhankelijkheid van Congo, een Belgisch en een Congolees. Wat verwacht je?",
        opties=[
            "dezelfde feiten met een andere nadruk",
            "volledig dezelfde tekst in beide boeken",
            "een van de twee boeken die alles verzint",
            "geen enkele overeenkomst tussen de twee boeken",
        ],
        antwoord=0,
        uitleg="Ook de hoofdrollen verschillen. Wie het verhaal vertelt, kiest het middelpunt; daarom lees je het van beide kanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over beeldvorming in de reclame en de media kloppen?",
        opties=[
            "beelden van groepen mensen kunnen stereotypen versterken",
            "wie beelden maakt, kiest wat je te zien krijgt",
            "beelden in de media zijn altijd volledig neutraal",
            "beelden hebben op het denken van mensen geen invloed",
        ],
        antwoord=[0, 1],
        uitleg="Daarom hoort het lezen van beelden bij dit vak, en niet enkel het lezen van teksten.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is betekenisgeving aan het verleden?",
        opties=[
            "de waarde die een samenleving aan haar verleden toekent",
            "de volgorde waarin de gebeurtenissen zich voordeden",
            "het aantal bronnen dat van een periode bestaat",
            "de taal waarin een bron geschreven werd",
        ],
        antwoord=0,
        uitleg="Je ziet ze in feestdagen, monumenten, straatnamen, musea en in wat op school aan bod komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je hoe een samenleving haar verleden waardeert?",
        opties=[
            "aan haar feestdagen en herdenkingen",
            "aan haar standbeelden en straatnamen",
            "aan het aantal archieven dat verloren is",
            "aan de taal van haar oudste documenten",
        ],
        antwoord=[0, 1],
        uitleg="Ook erfgoed dat beschermd wordt, zegt wat een samenleving van haar verleden wil bewaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is 11 november in België een feestdag?",
        opties=[
            "het is de dag van de wapenstilstand van 1918",
            "het is de dag van de bevrijding in 1944",
            "het is de dag van de onafhankelijkheid van 1830",
            "het is de dag van de troonsafstand van 1951",
        ],
        antwoord=0,
        uitleg="Zo'n dag houdt een gebeurtenis in het geheugen van een land. Dat is betekenisgeving in de praktijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen geschiedenis en herinnering?",
        opties=[
            "geschiedenis onderzoekt, herinnering wordt beleefd",
            "geschiedenis gaat over mensen, herinnering over gebouwen",
            "geschiedenis is altijd juist, herinnering altijd fout",
            "er is tussen die twee geen enkel verschil",
        ],
        antwoord=0,
        uitleg="Een herdenking is geen onderzoek. Toch is herinnering zelf een onderwerp voor onderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen sommige standbeelden vandaag onder vuur?",
        opties=[
            "de persoon wordt nu anders beoordeeld dan vroeger",
            "de beelden zijn te oud om nog te kunnen blijven staan",
            "de beelden zijn van een materiaal dat niet duurzaam is",
            "de beelden staan altijd op de verkeerde plaats in de stad",
        ],
        antwoord=0,
        uitleg="Een standbeeld eert iemand. Verandert de beoordeling, dan verandert de vraag of dat eren nog past.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oplossingen worden voorgesteld voor een omstreden standbeeld?",
        opties=[
            "een bord met uitleg bij het beeld plaatsen",
            "het beeld naar een museum verplaatsen",
            "het beeld van alle foto's laten verwijderen",
            "het beeld door een groter beeld vervangen",
        ],
        antwoord=[0, 1],
        uitleg="Weghalen, uitleggen of laten staan: dat debat gaat niet over het verleden maar over ons.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover gaat de vraag naar teruggave van voorwerpen uit koloniale musea?",
        opties=[
            "over voorwerpen die in de koloniale tijd zijn weggehaald",
            "over voorwerpen die musea aan elkaar uitlenen",
            "over voorwerpen die bij opgravingen hier gevonden zijn",
            "over voorwerpen die in de oorlog verloren zijn gegaan",
        ],
        antwoord=0,
        uitleg="België heeft daarvoor een wettelijk kader gemaakt. Elk stuk vraagt onderzoek naar zijn herkomst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het ontkennen van de Holocaust, dat in België strafbaar is?",
        antwoord=["negationisme", "het negationisme", "holocaustontkenning"],
        uitleg="Een wet van 1995 stelt het strafbaar. Het is geen mening maar het ontkennen van vastgestelde feiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan geschiedenis politiek misbruikt worden?",
        opties=[
            "door het verleden te vervormen om een eis te onderbouwen",
            "door bronnen uit verschillende kanten naast elkaar te leggen",
            "door een onderzoek voor iedereen controleerbaar te maken",
            "door toe te geven dat een vraag nog open staat",
        ],
        antwoord=0,
        uitleg="Een uitgezochte of verzonnen gouden eeuw is al vaak gebruikt om een aanspraak te rechtvaardigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over herdenken kloppen?",
        opties=[
            "een herdenking kiest wie en wat herdacht wordt",
            "wat een land herdenkt, kan in de tijd veranderen",
            "een herdenking is hetzelfde als een onderzoek",
            "elk land herdenkt dezelfde gebeurtenissen",
        ],
        antwoord=[0, 1],
        uitleg="De slachtoffers van de kolonisatie komen pas sinds kort in de Belgische herdenkingen voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is erfgoed?",
        opties=[
            "wat uit het verleden bewaard en doorgegeven wordt",
            "wat een familie na een overlijden geërfd heeft",
            "wat een museum jaarlijks aankoopt",
            "wat in een archief verloren is gegaan",
        ],
        antwoord=0,
        uitleg="Het kan gaan om gebouwen, voorwerpen, landschappen, maar ook om gebruiken en ambachten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom studeren we geschiedenis als het over voorbije tijden gaat?",
        opties=[
            "om te begrijpen hoe het heden geworden is wat het is",
            "om de gebeurtenissen van de toekomst te voorspellen",
            "om vast te stellen dat niets ooit verandert",
            "om enkel data en namen te kunnen opsommen",
        ],
        antwoord=0,
        uitleg="Grenzen, instellingen, ongelijkheden en gevoeligheden van nu hebben alle een voorgeschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is continuïteit in de geschiedenis?",
        opties=[
            "wat over een lange periode hetzelfde blijft",
            "wat van het ene jaar op het andere verandert",
            "wat in één gebeurtenis samenvalt",
            "wat nooit in bronnen terug te vinden is",
        ],
        antwoord=0,
        uitleg="Naast de breuken zie je lijnen die doorlopen. Beide samen maken het verhaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een monument zegt evenveel over de tijd waarin het geplaatst werd als over wie het eert.",
        antwoord=True,
        uitleg="Wie in 1900 een standbeeld oprichtte, maakte daarmee een uitspraak over zijn eigen tijd.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat een land herdenkt, blijft altijd hetzelfde.",
        antwoord=False,
        uitleg="Nieuwe inzichten en nieuwe stemmen veranderen de lijst van wat herdacht wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het ontkennen van de Holocaust is in België bij wet strafbaar.",
        antwoord=True,
        uitleg="Sinds 1995. Het gaat niet om een mening over feiten, maar om het ontkennen van de feiten zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Geschiedenis kan de gebeurtenissen van de toekomst voorspellen.",
        antwoord=False,
        uitleg="Zij helpt het heden begrijpen en vragen scherper stellen. Voorspellen doet ze niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een debat over een standbeeld gaat vooral over hoe wij vandaag naar het verleden kijken.",
        antwoord=True,
        uitleg="Het verleden verandert niet. Wat verandert, is wat wij ervan willen eren of uitleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een standbeeld van een koloniale figuur met een nieuw bord met uitleg erbij. Wat is dat?",
        opties=[
            "een poging om het beeld in zijn context te plaatsen",
            "een poging om het verleden helemaal uit te wissen",
            "een bewijs dat het beeld nooit betwist werd",
            "een manier om het beeld te laten verdwijnen",
        ],
        antwoord=0,
        uitleg="Uitleg bij een beeld laat het staan en zegt er iets over. Dat is één van de mogelijke antwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband leg je tussen dit thema en de rest van het vak?",
        opties=[
            "bronnen, standpunten en beeldvorming horen samen",
            "beeldvorming geldt enkel voor de hedendaagse tijd",
            "beeldvorming staat los van het werken met bronnen",
            "beeldvorming is enkel van belang bij kunstwerken",
        ],
        antwoord=0,
        uitleg="Van Wenen tot Congo: wie de bron leest, leest ook wie ze maakte en met welke bedoeling.",
    ),
]
