# -*- coding: utf-8 -*-
"""De vragen voor "Fictie, personages, verhaallijn, tijd en ruimte".

Nieuw geschreven voor dubbele finaliteit. Doorstroom heeft hierover twee
thema's, met verteller, verteltijd, vertelde tijd, rijmschema, enjambement,
toneel en literaire stromingen. Daar vraagt de DF-fiche niets van.

Wat ze wél vraagt: "Je leest, beluistert of bekijkt tijdens het examen
literaire teksten, zoals een strip, een lied, een gedicht, een verhaal, een
blog." En: "Om je mening te verwoorden, kan je gebruikmaken van een aantal
begrippen zoals fictie, non-fictie, personages, verhaallijn, tijd en ruimte."
Daarnaast moet je twee boeken van de boekenlijst gelezen hebben en je eigen
beleving en interpretatie kunnen verwoorden; de literaire competentie komt aan
bod in een van de gesprekken.

Deel 1 gaat over de begrippen zelf, deel 2 over wat je ermee doet als je over
een boek vertelt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is fictie?",
        opties=[
            "een verhaal dat verzonnen is, ook al lijkt het echt",
            "een verhaal dat helemaal echt gebeurd is",
            "een verhaal dat in de toekomst speelt",
            "een verhaal dat korter is dan honderd bladzijden",
        ],
        antwoord=0,
        uitleg="Fictie kan best over herkenbare mensen en plaatsen gaan. Wat telt is dat de schrijver het bedacht heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn non-fictie?",
        opties=[
            "een biografie van een wielrenner",
            "een reisverslag van een echte reis",
            "een boek over de geschiedenis van je stad",
            "een fantasyroman over een school voor tovenaars",
        ],
        antwoord=[0, 1, 2],
        uitleg="Non-fictie gaat over wat echt bestaat of gebeurd is. De laatste is verzonnen en dus fictie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een roman die op ware feiten gebaseerd is, blijft fictie zodra de schrijver er gesprekken en personages bij bedenkt.",
        antwoord=True,
        uitleg="Een ware aanleiding maakt een boek nog geen non-fictie. Zodra er verzonnen wordt, lees je fictie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teksten horen bij de literaire teksten die je op het examen kan tegenkomen?",
        opties=[
            "een strip",
            "een gedicht",
            "een lied",
            "een bijsluiter bij een geneesmiddel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een bijsluiter is een prescriptieve tekst: die geeft instructies. Literaire teksten hebben een esthetische waarde en spelen in op emoties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een personage?",
        opties=[
            "iemand die in het verhaal voorkomt en er iets doet",
            "de persoon die het boek geschreven heeft",
            "de lezer die zich in het verhaal herkent",
            "de uitgeverij die het boek op de markt bracht",
        ],
        antwoord=0,
        uitleg="De schrijver staat buiten het verhaal; de personages staan erin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de verhaallijn?",
        opties=[
            "de lijn van gebeurtenissen die het verhaal aflegt",
            "de eerste zin waarmee het boek begint",
            "het aantal bladzijden dat het boek telt",
            "de lijn tekst die op de achterflap staat",
        ],
        antwoord=0,
        uitleg="De verhaallijn is wat er gebeurt, van het begin tot het einde, en in welke volgorde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verhaal kan maar één verhaallijn hebben.",
        antwoord=False,
        uitleg="Veel boeken volgen twee of drie personages afwisselend. Die lijnen komen vaak op het einde samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een verhaal dat verzonnen is?",
        antwoord=["fictie"],
        uitleg="Het tegendeel is non-fictie: teksten over wat echt bestaat of gebeurd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de ruimte van een verhaal?",
        opties=[
            "de plaats of plaatsen waar het verhaal zich afspeelt",
            "de witte marge rond de tekst op de bladzijde",
            "de tijd die de lezer nodig heeft om het uit te lezen",
            "het aantal personages dat tegelijk aanwezig is",
        ],
        antwoord=0,
        uitleg="Een zolderkamer, een dorp aan zee, een ruimteschip: dat is de ruimte waarin het verhaal speelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de tijd van een verhaal?",
        opties=[
            "wanneer het verhaal speelt en hoeveel tijd het beslaat",
            "hoe lang jij erover doet om het boek te lezen",
            "het jaar waarin het boek is uitgegeven",
            "de tijd waarin de werkwoorden staan",
        ],
        antwoord=0,
        uitleg="Speelt het in de middeleeuwen of vandaag, en beslaat het één nacht of twintig jaar? Dat zijn allebei vragen over de tijd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verhaal moet zijn gebeurtenissen altijd in chronologische volgorde vertellen.",
        antwoord=False,
        uitleg="Veel verhalen springen terug naar vroeger of beginnen bij het einde. Dat is een keuze van de schrijver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men een strip een literaire tekst?",
        opties=[
            "omdat hij met beeld en taal een verhaal vertelt dat je raakt",
            "omdat er tekeningen in staan en tekeningen altijd kunst zijn",
            "omdat een strip korter is dan een roman",
            "omdat een strip altijd over verzonnen figuren gaat",
        ],
        antwoord=0,
        uitleg="Literaire teksten hebben een esthetische waarde en spelen in op emoties. Dat kan met tekst en met beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hoofdpersonage?",
        opties=[
            "het personage rond wie het verhaal vooral draait",
            "het personage dat het eerst genoemd wordt",
            "het personage met de langste naam",
            "het personage dat op de kaft staat afgebeeld",
        ],
        antwoord=0,
        uitleg="Een hoofdpersonage hoeft niet aardig of dapper te zijn: het is degene wiens verhaal je volgt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de plaats waar een verhaal zich afspeelt?",
        antwoord=["de ruimte", "ruimte"],
        uitleg="Ruimte en tijd samen vertellen je waar en wanneer je bent in een verhaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een blog kan zowel non-fictie als literatuur zijn.",
        antwoord=True,
        uitleg="Een blog waarin iemand met zorg over zijn eigen leven schrijft, kan allebei tegelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen gaan over de personages van een boek?",
        opties=[
            "wie verandert er in de loop van het verhaal?",
            "wie staat er tegenover wie?",
            "wie neemt de beslissing waar alles op draait?",
            "in welk jaar is het boek verschenen?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het verschijningsjaar zegt iets over het boek, niet over wie erin voorkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een verhaal speelt volledig in één huis tijdens één storm. Wat zeg je daarover?",
        opties=[
            "de ruimte is beperkt en de tijd is kort",
            "de ruimte is beperkt en de tijd is lang",
            "de ruimte is ruim en de tijd is kort",
            "de ruimte is ruim en de tijd is lang",
        ],
        antwoord=0,
        uitleg="Eén huis is een kleine ruimte, één storm is een korte tijd. Dat maakt zo'n verhaal vaak benauwd en gespannen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een gedicht en een lied?",
        opties=[
            "een lied is gemaakt om gezongen te worden, een gedicht niet per se",
            "een gedicht rijmt altijd, een lied nooit",
            "een lied is altijd korter dan een gedicht",
            "een gedicht is fictie, een lied is non-fictie",
        ],
        antwoord=0,
        uitleg="Veel liedteksten zijn gedichten op muziek. Rijm komt in allebei voor, of net niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor het examen lees of beluister je twee boeken die je kiest uit de boekenlijst in de bijlage.",
        antwoord=True,
        uitleg="Je mag ze ook beluisteren. De literaire competentie komt aan bod in een van de gesprekken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je teksten over wat echt bestaat of echt gebeurd is?",
        antwoord=["non-fictie", "nonfictie"],
        uitleg="Een biografie, een reisverslag en een geschiedenisboek zijn non-fictie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je moet je eigen beleving bij een boek verwoorden. Wat hoort daarbij?",
        opties=[
            "zeggen wat je raakte en waarom precies",
            "de samenvatting van de achterflap navertellen",
            "opsommen hoeveel bladzijden je per dag las",
            "vertellen hoeveel het boek gekost heeft",
        ],
        antwoord=0,
        uitleg="Beleving is wat het boek met jou deed. Dat kan niemand nakijken, maar je moet het wel kunnen uitleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen helpen je om over je boek na te denken?",
        opties=[
            "waarom spreken bepaalde aspecten van het boek me aan, of net niet?",
            "welke boodschap zit er in de tekst?",
            "hoe zou ik zelf reageren in een gelijkaardige situatie?",
            "hoeveel exemplaren zijn er van dit boek verkocht?",
        ],
        antwoord=[0, 1, 2],
        uitleg="De verkoopcijfers zeggen iets over het boek als product, niet over wat het met jou doet.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag zeggen dat een boek je niet aansprak, zolang je uitlegt waarom.",
        antwoord=True,
        uitleg="Een eerlijk en onderbouwd oordeel is meer waard dan geforceerde bewondering. Het gaat om het waarom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de boodschap van een verhaal?",
        opties=[
            "wat de tekst je over mensen of de wereld wil laten inzien",
            "de brief die een van de personages in het verhaal verstuurt",
            "de eerste zin van het laatste hoofdstuk",
            "de opdracht die vooraan in het boek staat",
        ],
        antwoord=0,
        uitleg="Die boodschap staat er zelden letterlijk. Je leidt ze af uit wat er gebeurt en hoe het verteld wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je herkent jezelf in een personage. Wat is een goede manier om dat te verwoorden?",
        opties=[
            "zeggen in welke situatie je dat voelde en wat je zelf zou doen",
            "zeggen dat je het personage gewoon leuk vindt",
            "de naam van het personage een paar keer herhalen",
            "de hele verhaallijn van dat personage nog eens navertellen",
        ],
        antwoord=0,
        uitleg="Herkenning wordt pas interessant als je er een voorbeeld bij geeft. Anders blijft het bij een woord.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee lezers kunnen hetzelfde boek heel anders interpreteren, en allebei een goed antwoord geven.",
        antwoord=True,
        uitleg="Interpretatie is niet vrijblijvend, maar er is ruimte. Wat telt is dat je je lezing aan de tekst kan ophangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover gaat een vraag naar het taalgebruik in een boek?",
        opties=[
            "of de zinnen kort of lang zijn en of de woorden vlot lazen",
            "of er spelfouten in het boek zijn blijven staan",
            "in welke taal het boek oorspronkelijk geschreven werd en door wie",
            "hoeveel woorden het boek in totaal telt",
        ],
        antwoord=0,
        uitleg="Het gaat over hoe het boek klinkt en leest, en of die stijl bij het verhaal past.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de lijn van gebeurtenissen die een verhaal aflegt?",
        antwoord=["de verhaallijn", "verhaallijn"],
        uitleg="Wat er gebeurt, van begin tot eind, en in welke volgorde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boek speelt in een dorp waar iedereen elkaar kent. Wat doet die ruimte met het verhaal?",
        opties=[
            "ze maakt dat een geheim moeilijk te bewaren is",
            "ze zorgt dat het verhaal sneller vooruitgaat",
            "ze bepaalt wie het hoofdpersonage is",
            "ze maakt van het boek meteen non-fictie",
        ],
        antwoord=0,
        uitleg="De ruimte is niet zomaar een decor: ze legt vast wat er kan gebeuren en wat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een boek zijn interpretaties en geen feiten?",
        opties=[
            "het einde laat open of ze elkaar terugzien",
            "de schrijver wil laten zien dat zwijgen ook schade doet",
            "het hoofdpersonage groeit doorheen het boek",
            "het boek telt achtentwintig hoofdstukken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het aantal hoofdstukken kan je tellen. De drie andere moet je uit de tekst afleiden en verdedigen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een gesprek over je boek volstaat het om de verhaallijn na te vertellen.",
        antwoord=False,
        uitleg="Navertellen laat vooral zien dát je het gelezen hebt. Er wordt gevraagd wat je ervan vond en waarom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een verhaal springt geregeld terug naar de jeugd van het hoofdpersonage. Wat zegt dat over de tijd?",
        opties=[
            "het verhaal wordt niet in chronologische volgorde verteld",
            "het verhaal speelt zich af in de middeleeuwen",
            "het verhaal beslaat maar één enkele dag",
            "het verhaal is daardoor automatisch non-fictie",
        ],
        antwoord=0,
        uitleg="Zulke sprongen laten je begrijpen waarom iemand vandaag doet wat hij doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk begrip gebruik je om te zeggen waar en wanneer een verhaal speelt?",
        opties=[
            "tijd en ruimte",
            "fictie en non-fictie",
            "feit en mening",
            "zender en ontvanger",
        ],
        antwoord=0,
        uitleg="Tijd en ruimte horen samen: ze zetten het verhaal ergens neer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een personage dat in het hele boek precies hetzelfde blijft, kan ook een goed personage zijn.",
        antwoord=True,
        uitleg="Soms is juist dat het punt: iedereen om hem heen verandert en hij niet. Dan zegt het stilstaan iets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een kortverhaal op het examen dat je nog nooit las. Wat doe je eerst?",
        opties=[
            "lezen wie erin voorkomt, waar het speelt en wat er gebeurt",
            "meteen opschrijven of je het mooi vindt of niet",
            "de moeilijke woorden allemaal opzoeken voor je begint",
            "tellen hoeveel alinea's de tekst heeft",
        ],
        antwoord=0,
        uitleg="Personages, ruimte en verhaallijn geven je meteen houvast. Je oordeel komt daarna.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je iemand die in een verhaal voorkomt en er iets doet?",
        antwoord=["een personage", "personage"],
        uitleg="De schrijver staat buiten het verhaal, de personages staan erin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt een tekst literair?",
        opties=[
            "hij heeft een esthetische waarde en speelt in op emoties",
            "hij is langer dan tweehonderd bladzijden",
            "hij is minstens vijftig jaar oud",
            "hij is geschreven door een bekende schrijver",
        ],
        antwoord=0,
        uitleg="Een stand-upcomedyfragment kan literair zijn en een dik boek niet. Het gaat om wat de tekst doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt men je naar je eigen reactie op een boek, en niet enkel naar de inhoud?",
        opties=[
            "omdat lezen ook over jezelf gaat en je dat moet kunnen verwoorden",
            "omdat de inhoud van een boek niet te controleren is",
            "omdat een mening sneller te beoordelen is dan kennis",
            "omdat er anders te weinig vragen over het boek zijn",
        ],
        antwoord=0,
        uitleg="Literatuur lezen laat je kennismaken met andere mensen, ideeën en zienswijzen. Wat dat met jou doet, is het punt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een strip kan nooit over een ernstig onderwerp gaan.",
        antwoord=False,
        uitleg="Er bestaan strips over oorlog, ziekte en rouw. De vorm zegt niets over het gewicht van het onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil zeggen wat het boek met je deed. Welke zin is het bruikbaarst in een gesprek?",
        opties=[
            "het slot liet me verward achter, omdat ik niet wist wie ik gelijk moest geven",
            "het was een heel goed boek en ik raad het echt aan",
            "het boek was spannend van de eerste tot de laatste bladzijde",
            "ik heb het in drie avonden uitgelezen zonder te stoppen",
        ],
        antwoord=0,
        uitleg="De eerste zegt wát je voelde en waardoor. De drie andere zijn oordelen zonder uitleg.",
    ),
]
