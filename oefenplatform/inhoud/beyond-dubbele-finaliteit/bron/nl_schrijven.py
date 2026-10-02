# -*- coding: utf-8 -*-
"""Schrijven en schriftelijke interactie — dubbele finaliteit.

De fiche vraagt: teksten schrijven met een duidelijk doel en publiek
(verslag, mail, sollicitatiebrief, instructie, opiniestuk), het schrijfproces
doorlopen (plannen, schrijven, nalezen, herwerken), en schriftelijk reageren op
iemand anders: een mail beantwoorden, een reactie plaatsen, een klacht
formuleren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bepaal je als eerste voor je een tekst begint te schrijven?",
        opties=[
            "je doel en je publiek",
            "het aantal woorden dat je nodig hebt",
            "het lettertype van je tekst",
            "de titel van je tekst",
        ],
        antwoord=0,
        uitleg="Wie gaat dit lezen en wat moet die daarna weten of doen? Alles volgt daaruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het schrijfproces?",
        opties=[
            "plannen voor je begint te schrijven",
            "nalezen en herwerken na de eerste versie",
            "de tekst in één keer af hebben",
            "de tekst meteen naar de ontvanger sturen",
        ],
        antwoord=[0, 1],
        uitleg="Een eerste versie is nooit de laatste. Het nalezen hoort bij het werk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bepalen van je lezer voor je begint te schrijven?",
        antwoord=["je publiek bepalen", "het publiek bepalen", "je doelgroep bepalen"],
        uitleg="Samen met je doel bepaalt dat je toon en je woordkeuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een verslag van een vergadering?",
        opties=[
            "wat beslist werd en wie wat doet",
            "de meningen van de schrijver over de beslissingen",
            "alles wat er letterlijk gezegd werd",
            "de namen van wie niets gezegd heeft",
        ],
        antwoord=0,
        uitleg="Een verslag dient om later terug te lezen wat er is afgesproken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een sollicitatiebrief?",
        opties=[
            "waarom je deze job wil en wat je ervoor meebrengt",
            "een opsomming van alles wat je ooit deed",
            "je mening over het bedrijf waar je solliciteert",
            "een lijst van je hobby's en interesses",
        ],
        antwoord=0,
        uitleg="Je cv geeft de lijst. De brief legt het verband met deze ene vacature.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft een goede instructie?",
        opties=[
            "de stappen staan in de orde waarin ze uitgevoerd worden",
            "elke stap bevat één handeling, in de gebiedende wijs",
            "de instructie legt eerst de hele theorie uit",
            "de instructie gebruikt zo veel vaktermen als mogelijk",
        ],
        antwoord=[0, 1],
        uitleg="Wie een instructie leest, staat met zijn handen aan het werk. Hou het kort en in orde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst nalezen op spelling en een tekst herwerken zijn twee verschillende stappen.",
        antwoord=True,
        uitleg="Herwerken gaat over de opbouw en de inhoud. Spelling komt daarna.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goede schrijver maakt in zijn eerste versie geen fouten.",
        antwoord=False,
        uitleg="Een eerste versie mag rommelig zijn. Het nalezen is er juist voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mail aan een onbekende begint het best formeel.",
        antwoord=True,
        uitleg="Je kan altijd informeler worden. Omgekeerd is moeilijker goed te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een opiniestuk?",
        opties=[
            "een tekst die een standpunt verdedigt met argumenten",
            "een tekst die enkel feiten weergeeft over een onderwerp",
            "een tekst die een gebeurtenis verslaat voor een krant",
            "een tekst die een handleiding geeft bij een toestel",
        ],
        antwoord=0,
        uitleg="De lezer mag weten wat je vindt, en moet kunnen volgen waarom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je een alinea-indeling in een langere tekst?",
        opties=[
            "één gedachte per alinea, met de kerngedachte vooraan",
            "elke alinea even lang maken als de vorige",
            "een nieuwe alinea na elke vijf regels tekst",
            "alle alinea's met hetzelfde signaalwoord beginnen",
        ],
        antwoord=0,
        uitleg="De lezer ziet de structuur dan al voor hij leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je klacht over een product niet opgelost wordt?",
        opties=[
            "je schrijft een klacht met de feiten, de data en wat je verwacht",
            "je schrijft een boze mail zonder verdere uitleg erbij",
            "je plaatst meteen een negatieve reactie op sociale media",
            "je wacht af tot de verkoper zelf contact met je opneemt",
        ],
        antwoord=0,
        uitleg="Een klacht die de feiten en een concrete vraag bevat, krijgt veel sneller antwoord.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een tekst die een standpunt verdedigt met argumenten?",
        antwoord=["een opiniestuk", "opiniestuk", "een betoog"],
        uitleg="De lezer moet kunnen volgen waarom je het vindt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functie van een inleiding?",
        opties=[
            "de lezer binnenhalen en zeggen waarover de tekst gaat",
            "de hele inhoud van de tekst samenvatten",
            "de bronnen van de tekst op een rij zetten",
            "de mening van de schrijver al volledig geven",
        ],
        antwoord=0,
        uitleg="Ze opent en richt. Het samenvatten komt in het slot, en dan korter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een mail met een vraag en een deadline. Waar zet je de deadline?",
        opties=[
            "duidelijk apart, zodat ze niet in de tekst verdwijnt",
            "achteraan, na je ondertekening",
            "in de onderwerpregel alleen",
            "midden in de langste alinea",
        ],
        antwoord=0,
        uitleg="Wat de ontvanger moet doen en wanneer, hoort op een eigen regel te staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst door iemand anders laten nalezen levert minder op dan hem zelf nog eens lezen.",
        antwoord=False,
        uitleg="Je leest in je eigen tekst wat je bedoelde. Een ander leest wat er staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in de onderwerpregel van een mail?",
        opties=[
            "in enkele woorden waarover de mail gaat",
            "een begroeting voor de ontvanger",
            "de datum waarop je de mail stuurt",
            "je volledige naam en functie",
        ],
        antwoord=0,
        uitleg="De ontvanger moet in zijn lijst meteen zien of hij nu moet openen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schriftelijk antwoord hoort elke vraag van de ander te behandelen.",
        antwoord=True,
        uitleg="Wie één vraag overslaat, krijgt die gewoon opnieuw. Dat kost twee mails extra.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe reageer je schriftelijk op iemand met wie je niet akkoord gaat?",
        opties=[
            "je benoemt waar je het oneens bent en zegt waarom",
            "je herhaalt je eigen standpunt luider dan daarvoor",
            "je laat het onderwerp liggen en schrijft over iets anders",
            "je gaat ervan uit dat de ander jou wel begrijpt",
        ],
        antwoord=0,
        uitleg="De inhoud scherp, de toon rustig. Dan blijft het gesprek mogelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zakelijke mail hoort altijd minstens een halve bladzijde lang te zijn.",
        antwoord=False,
        uitleg="Drie regels kunnen genoeg zijn. Lengte is geen teken van zorg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je moet een verslag schrijven van een gesprek met een klant. Wat doe je eerst?",
        opties=[
            "je zet je notities in de orde van wat besproken werd",
            "je begint met de inleiding uit te schrijven",
            "je zoekt een voorbeeldverslag van iemand anders",
            "je kiest het lettertype en de bladspiegel",
        ],
        antwoord=0,
        uitleg="Van losse notities naar een lijn: dat is plannen. Schrijven gaat daarna veel sneller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een verslag en een opiniestuk?",
        opties=[
            "een verslag geeft weer wat er gebeurde, een opiniestuk wat je vindt",
            "een verslag is langer en een opiniestuk altijd korter",
            "een verslag staat in de verleden tijd en een opiniestuk in het heden",
            "een verslag is voor intern gebruik en een opiniestuk voor extern",
        ],
        antwoord=0,
        uitleg="Een verslag met een mening erin verborgen is niet meer bruikbaar als verslag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stap waarin je de opbouw van je tekst nog wijzigt?",
        antwoord=["herwerken", "het herwerken", "reviseren"],
        uitleg="Spelling nalezen komt daarna, niet ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke keuzes hangen af van je publiek?",
        opties=[
            "hoeveel voorkennis je veronderstelt",
            "of je vaktermen uitlegt of gewoon gebruikt",
            "hoeveel bronnen je in totaal gebruikt",
            "in welk programma je de tekst typt",
        ],
        antwoord=[0, 1],
        uitleg="Dezelfde inhoud voor een vakgenoot of voor een buitenstaander is een andere tekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een instructie voor iemand die het toestel nooit zag. Wat doe je?",
        opties=[
            "je benoemt elk onderdeel voor je het gebruikt",
            "je gebruikt de vaktermen uit de handleiding",
            "je begint bij de moeilijkste stap van het geheel",
            "je verwijst naar de tekening zonder uitleg erbij",
        ],
        antwoord=0,
        uitleg="Wie het onderdeel niet kan benoemen, kan de stap niet uitvoeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een klacht wint kracht door de feiten met data en bedragen te noemen.",
        antwoord=True,
        uitleg="Een klacht die te controleren is, is moeilijker af te wimpelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een klacht hoort je gevoel over de zaak zo scherp mogelijk uit te drukken.",
        antwoord=False,
        uitleg="Noem één keer wat het je kostte en vraag dan wat je verwacht. Scherp in de vraag, rustig in de toon.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst hoort bij elke lezer op dezelfde manier over te komen.",
        antwoord=False,
        uitleg="Daarom kies je één publiek. Een tekst voor iedereen werkt voor niemand echt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je tekst te lang is geworden?",
        opties=[
            "je schrapt wat de lezer niet nodig heeft voor je doel",
            "je maakt de zinnen korter maar laat alles staan",
            "je zet de helft in een bijlage achteraan",
            "je verkleint het lettertype van de tekst",
        ],
        antwoord=0,
        uitleg="Schrappen is kiezen. Comprimeren zonder schrappen maakt een tekst enkel moeilijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je een zakelijke mail makkelijk te beantwoorden?",
        opties=[
            "je stelt je vragen apart en genummerd",
            "je zet al je vragen in één lange alinea",
            "je stelt één brede vraag over het geheel",
            "je laat de ontvanger zelf de vragen zoeken",
        ],
        antwoord=0,
        uitleg="Genummerde vragen krijgen genummerde antwoorden. Een lange alinea krijgt er één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke middelen maken een tekst beter leesbaar?",
        opties=[
            "tussenkoppen boven de delen van de tekst",
            "korte alinea's met één gedachte per alinea",
            "zo veel vaktermen als het onderwerp toelaat",
            "zo lange zinnen als grammaticaal mogelijk is",
        ],
        antwoord=[0, 1],
        uitleg="De vorm doet de helft van het werk. De lezer ziet de lijn nog voor hij begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een mail met drie vragen en je kent het antwoord op één. Wat doe je?",
        opties=[
            "je antwoordt op die ene en zegt wanneer de rest volgt",
            "je wacht tot je alle drie de antwoorden hebt",
            "je antwoordt op die ene en laat de rest onvermeld",
            "je stuurt de mail door naar iemand anders",
        ],
        antwoord=0,
        uitleg="De ander weet dan dat zijn mail aankwam en waar hij aan toe is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de eerste regel van een mail die zegt waarover hij gaat?",
        antwoord=["de onderwerpregel", "onderwerpregel", "het onderwerp"],
        uitleg="De ontvanger beslist daarop of hij nu opent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je in het slot van een opiniestuk?",
        opties=[
            "je conclusie, en wat er volgens jou moet gebeuren",
            "een nieuw argument dat je nog niet gaf",
            "een samenvatting van alle tegenargumenten",
            "een vraag die je zelf niet beantwoordt",
        ],
        antwoord=0,
        uitleg="Het slot is waar je de rekening maakt. Nieuwe argumenten horen daar niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je je tekst het best luidop na?",
        opties=[
            "je hoort waar een zin niet loopt",
            "je ziet daardoor de spelfouten sneller",
            "je onthoudt je eigen tekst dan beter",
            "je leest de tekst dan trager dan anders",
        ],
        antwoord=0,
        uitleg="Wat je niet in één adem kan voorlezen, leest je lezer ook niet in één keer.",
    ),
    dict(
        type="waarofniet",
        vraag="In een sollicitatiebrief hoort te staan wat jij voor de werkgever kan doen.",
        antwoord=True,
        uitleg="Niet enkel wat jij wil. De lezer zoekt iemand voor een taak die vastligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft dezelfde boodschap voor een mail en voor een affiche. Wat verandert?",
        opties=[
            "de lengte, de vorm en de toon van de boodschap",
            "alleen het lettertype van de tekst",
            "alleen de ondertekening onderaan",
            "niets, want de boodschap blijft dezelfde",
        ],
        antwoord=0,
        uitleg="Een affiche wordt in drie seconden gelezen. Een mail krijgt dertig.",
    ),
    dict(
        type="waarofniet",
        vraag="Schrijven is één handeling en valt niet in stappen op te delen.",
        antwoord=False,
        uitleg="Plannen, schrijven, herwerken, nalezen. Wie ze door elkaar doet, blijft steken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het schrijfproces kloppen?",
        opties=[
            "plannen kost tijd en levert tijd op bij het schrijven",
            "een tekst wordt beter door hem opnieuw op te bouwen",
            "een goede schrijver schrijft zijn tekst in één keer af",
            "spelling nalezen hoort voor het herwerken te gebeuren",
        ],
        antwoord=[0, 1],
        uitleg="Herwerken komt voor het nalezen. Een alinea die sneuvelt, hoef je niet gespeld te hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mail die geen antwoord vraagt, hoort dat ook te zeggen.",
        antwoord=True,
        uitleg="Eén regel zoals 'je hoeft hier niet op te antwoorden' spaart de ander werk.",
    ),
]
