# -*- coding: utf-8 -*-
"""De vragen voor "Feit en mening, stelling, argument en conclusie".

Nieuw geschreven voor dubbele finaliteit. De doorstroomversie van dit thema
gaat in deel 2 bijna helemaal over drogredenen: cirkelredenering, vals dilemma,
hellend vlak, beroep op autoriteit, persoonlijke aanval. Geen van die begrippen
staat op de DF-fiche.

Wat er wél op staat: "Als je een argumentatieve tekst leest of hoort, kan je
feiten en meningen van elkaar onderscheiden. Je kan stelling en standpunt
bepalen, argumenten herkennen en de conclusie bepalen. Je kan ook zelf
argumenteren: je kan je eigen standpunt bepalen, dit onderbouwen met goede
argumenten en een correcte conclusie formuleren." En bij spreken en interactie:
"Je gaat in dialoog over een maatschappelijk thema. Op basis van één of enkele
bronnen kan je argumenten geven. Je reageert respectvol en oplossingsgericht op
je gesprekspartner."

Deel 1 gaat over herkennen in een tekst van iemand anders, deel 2 over het zelf
doen en over het gesprek.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een feit en een mening?",
        opties=[
            "een feit kan je nagaan, een mening is wat iemand ervan vindt",
            "een feit staat in een krant, een mening staat op sociale media",
            "een feit is altijd waar, een mening is altijd onwaar",
            "een feit is kort geschreven, een mening is lang geschreven",
        ],
        antwoord=0,
        uitleg="Of iets een feit is, hangt niet af van waar het staat of hoe het klinkt, maar van de vraag of je het kan controleren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze uitspraken zijn feiten?",
        opties=[
            "de bus van 7.12 uur was gisteren elf minuten te laat",
            "in België geldt een maximumsnelheid van 120 km per uur op de autosnelweg",
            "de gemeente telde vorig jaar 412 nieuwe inwoners",
            "de gemeente doet veel te weinig voor jongeren",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie kan je opzoeken of meten. De laatste is een oordeel: 'veel te weinig' is wat iemand vindt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mening is altijd onbetrouwbaar en dus waardeloos in een tekst.",
        antwoord=False,
        uitleg="Een mening is prima, zolang je ziet dát het er een is. Een goede opiniërende tekst onderbouwt zijn mening zelfs met feiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een stelling?",
        opties=[
            "de uitspraak waarover de discussie gaat en die verdedigd wordt",
            "het eerste argument dat iemand in zijn tekst naar voren brengt",
            "de vraag die de schrijver aan het einde van zijn tekst stelt",
            "de titel die een schrijver boven zijn tekst zet om te lokken",
        ],
        antwoord=0,
        uitleg="De stelling is het punt zelf: 'De schooldag moet later beginnen.' Daar kan je het mee eens of oneens zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het standpunt van een schrijver?",
        opties=[
            "of hij voor of tegen de stelling is, en waarom",
            "de plaats waar hij stond toen hij de tekst schreef",
            "het aantal argumenten dat hij in de tekst gebruikt",
            "de krant of het platform waarin de tekst verscheen",
        ],
        antwoord=0,
        uitleg="Stelling en standpunt zijn niet hetzelfde: de stelling is de uitspraak, het standpunt is de kant die jij kiest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een argument?",
        opties=[
            "een reden die je geeft om je standpunt te onderbouwen",
            "een uitspraak waar je het niet mee eens bent",
            "een vraag die je aan je gesprekspartner stelt",
            "een gevoel dat je bij het onderwerp hebt",
        ],
        antwoord=0,
        uitleg="Een argument beantwoordt de vraag 'waarom vind je dat?'. Zonder argument is een standpunt enkel een uitroep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de conclusie van een argumentatieve tekst?",
        opties=[
            "wat er uit de argumenten volgt, meestal in het slot",
            "de allerlaatste zin van de tekst, wat er ook staat",
            "de samenvatting van alle feiten die vermeld werden",
            "de bronnenlijst die de schrijver achteraan toevoegt",
        ],
        antwoord=0,
        uitleg="Een conclusie is geen samenvatting. Ze trekt de lijn door: omdat dit en dat waar is, moet dit gebeuren.",
    ),
    dict(
        type="waarofniet",
        vraag="De conclusie van een tekst hoort meestal in het slot van de IMS-structuur.",
        antwoord=True,
        uitleg="Inleiding, midden, slot. In het slot vind je vaak het besluit terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de uitspraak waarover de hele discussie gaat?",
        antwoord=["de stelling", "stelling"],
        uitleg="De stelling is het punt dat verdedigd of aangevallen wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Jongeren moeten meer bewegen. Uit onderzoek blijkt dat slechts één op vijf de norm haalt.' Wat is de tweede zin?",
        opties=[
            "een argument bij de stelling uit de eerste zin",
            "de conclusie van de hele redenering",
            "een tweede, andere stelling van de schrijver",
            "een mening die niets met de eerste zin te maken heeft",
        ],
        antwoord=0,
        uitleg="De tweede zin geeft de reden waarom de eerste zin zou kloppen. Dat maakt er een argument van.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke soort tekst verwacht je een stelling met argumenten?",
        opties=[
            "een argumentatieve tekst, zoals een betoog of een pleidooi",
            "een prescriptieve tekst, zoals een handleiding of een recept",
            "een narratieve tekst, zoals een reisverslag of een podcast",
            "een informatieve tekst, zoals een stukje uit een leerboek",
        ],
        antwoord=0,
        uitleg="In een argumentatieve tekst geeft iemand argumenten ter ondersteuning van een standpunt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een opiniërende tekst en een argumentatieve tekst zijn precies hetzelfde.",
        antwoord=False,
        uitleg="In allebei komt een mening voor, maar een argumentatieve tekst is gebouwd om te overtuigen, met argumenten in een redenering. Een recensie mag bij een oordeel blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke signaalwoorden kondigen een argument aan?",
        opties=[
            "want",
            "omdat",
            "daarom",
            "ondertussen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Want, omdat en daarom verbinden een reden met een standpunt. Ondertussen zegt enkel iets over tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Het zwembad moet open blijven, want het is het enige in de gemeente.' Wat is de stelling?",
        opties=[
            "het zwembad moet open blijven",
            "het is het enige zwembad in de gemeente",
            "de gemeente heeft te weinig zwembaden",
            "zwemmen is gezond voor iedereen",
        ],
        antwoord=0,
        uitleg="Het stuk vóór 'want' is de uitspraak die verdedigd wordt. Wat erna komt, is de reden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schrijver kan zijn standpunt onderbouwen met feiten én met voorbeelden uit zijn eigen leven.",
        antwoord=True,
        uitleg="Allebei kunnen. Een cijfer uit een onderzoek weegt bij veel lezers zwaarder dan één voorbeeld, maar een voorbeeld maakt het wel levend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om in een tekst feiten van meningen te scheiden?",
        opties=[
            "omdat je dan ziet wat je kan nagaan en wat de schrijver vindt",
            "omdat meningen in een tekst eigenlijk verboden zijn",
            "omdat een tekst met meningen nooit een bron vermeldt",
            "omdat feiten altijd achteraan in de tekst staan",
        ],
        antwoord=0,
        uitleg="Wie dat onderscheid maakt, laat zich niet meeslepen door een mening die als feit gebracht wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reden die iemand geeft om zijn standpunt te onderbouwen?",
        antwoord=["een argument", "argument"],
        uitleg="Het argument beantwoordt de vraag waarom iemand dat vindt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekst opent met: 'Moet de gemeente een skatepark bouwen?' Wat doet die zin?",
        opties=[
            "hij zet het onderwerp van de discussie neer",
            "hij geeft meteen het standpunt van de schrijver",
            "hij is de conclusie van de hele tekst",
            "hij is een argument voor het skatepark",
        ],
        antwoord=0,
        uitleg="Een vraag is nog geen standpunt. Pas als de schrijver antwoordt, weet je aan welke kant hij staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tegenargument in een tekst betekent altijd dat de schrijver van mening veranderd is.",
        antwoord=False,
        uitleg="Veel schrijvers noemen juist het sterkste bezwaar om het daarna te weerleggen. Dat maakt hun tekst sterker, niet zwakker.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je wat er aan het eind uit alle argumenten volgt?",
        antwoord=["de conclusie", "conclusie", "het besluit"],
        uitleg="De conclusie trekt de lijn door van de argumenten naar wat er zou moeten gebeuren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je moet je eigen standpunt bepalen over een maatschappelijk thema. Waarmee begin je?",
        opties=[
            "uitzoeken wat je al weet en wat de bronnen erover zeggen",
            "meteen opschrijven wat je erover voelt en dat verdedigen",
            "kijken wat de meeste mensen in je klas ervan vinden",
            "de langste bron kiezen en die woord voor woord overnemen",
        ],
        antwoord=0,
        uitleg="Een standpunt dat je eerst onderzoekt, kan je ook verdedigen als iemand tegenwerpingen heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt een argument sterk?",
        opties=[
            "het is te controleren",
            "het gaat echt over de stelling",
            "het geldt voor meer mensen dan jij alleen",
            "het staat in hoofdletters getypt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hoofdletters typen wordt op een forum als schreeuwen gelezen en maakt je argument niet beter.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén sterk argument is meer waard dan vijf argumenten die niets met de stelling te maken hebben.",
        antwoord=True,
        uitleg="Een lezer telt geen argumenten, die weegt ze. Vijf keer iets naast de kwestie overtuigt niemand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een opiniestuk. Waar hoort je conclusie?",
        opties=[
            "in het slot, na de argumenten",
            "in de inleiding, nog voor de argumenten",
            "midden tussen de argumenten in",
            "in de titel boven de tekst",
        ],
        antwoord=0,
        uitleg="Inleiding, midden, slot. In het slot laat je zien wat er uit je argumenten volgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gaat in dialoog over een maatschappelijk thema. Wat hoort daarbij?",
        opties=[
            "luisteren naar wat je gesprekspartner zegt en erop ingaan",
            "respectvol reageren, ook als je het oneens bent",
            "zoeken naar een oplossing in plaats van naar gelijk",
            "je gesprekspartner onderbreken zodra hij fout zit",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche vraagt uitdrukkelijk dat je respectvol en oplossingsgericht reageert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gesprekspartner geeft een argument dat je nog niet kende en dat klopt. Wat doe je?",
        opties=[
            "je erkent het en past zo nodig je standpunt aan",
            "je doet alsof je het niet gehoord hebt",
            "je wisselt snel van onderwerp voor hij doorgaat",
            "je herhaalt je eigen argument luider dan daarnet",
        ],
        antwoord=0,
        uitleg="Van mening veranderen als het argument goed is, is geen verlies. Dat is wat een gesprek voor heeft op een ruzie.",
    ),
    dict(
        type="waarofniet",
        vraag="In een gesprek over een maatschappelijk thema mag je argumenten uit een bron halen.",
        antwoord=True,
        uitleg="De fiche vraagt dat net: op basis van één of enkele bronnen kan je argumenten geven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kant die jij zelf kiest in een discussie?",
        antwoord=["je standpunt", "standpunt", "het standpunt"],
        uitleg="De stelling is de uitspraak, je standpunt is of je voor of tegen bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Ik vind dat het skatepark er moet komen, want ik vind dat het er moet komen.' Wat is er mis?",
        opties=[
            "het argument herhaalt enkel het standpunt",
            "het standpunt is te kort geformuleerd",
            "er staat geen bron bij het argument",
            "de zin bevat een spelfout",
        ],
        antwoord=0,
        uitleg="Na 'want' hoort een réden te staan, iets nieuws. Hetzelfde nog eens zeggen brengt de lezer niet verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft over de vraag of de gemeente gratis bussen moet inleggen. Welke zin is een feit?",
        opties=[
            "een dagpas kost vandaag 7,50 euro",
            "de bus is veel te duur voor jongeren",
            "de gemeente denkt enkel aan auto's",
            "gratis bussen zijn de beste oplossing",
        ],
        antwoord=0,
        uitleg="Enkel de prijs kan je opzoeken. De drie andere zijn oordelen, hoe redelijk ze ook klinken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goede conclusie voegt nog een nieuw argument toe dat nergens eerder stond.",
        antwoord=False,
        uitleg="Een conclusie sluit af: ze laat zien wat er uit het voorgaande volgt. Een nieuw argument hoort in het midden thuis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent oplossingsgericht reageren in een gesprek?",
        opties=[
            "samen zoeken naar iets waar jullie allebei mee verder kunnen",
            "de ander laten praten en zelf niets meer inbrengen",
            "je eigen voorstel herhalen tot de ander het overneemt",
            "het gesprek afbreken als jullie er niet uit geraken",
        ],
        antwoord=0,
        uitleg="Het doel van zo'n gesprek is niet winnen, maar samen verder raken dan jullie afzonderlijk waren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest twee bronnen die elkaar tegenspreken over hetzelfde cijfer. Wat doe je?",
        opties=[
            "nagaan wie de zender is, wanneer het geschreven is en welke bron hij gebruikt",
            "de bron nemen die het best bij jouw standpunt past",
            "allebei de bronnen weglaten en zonder cijfers schrijven",
            "het gemiddelde van de twee cijfers nemen en dat vermelden",
        ],
        antwoord=0,
        uitleg="Dat zijn precies de criteria waarmee je beoordeelt of een tekst betrouwbaar, correct en bruikbaar is.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag in een opiniestuk je eigen ervaring gebruiken als argument.",
        antwoord=True,
        uitleg="Het mag, en het maakt je tekst levendig. Alleen: één ervaring zegt nog niets over iedereen, dus zet er iets naast dat breder geldt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke opbouw hoort bij een argumentatieve tekst?",
        opties=[
            "stelling, argumenten, conclusie",
            "conclusie, titel, argumenten",
            "argumenten, inleiding, stelling",
            "titel, bronnenlijst, stelling",
        ],
        antwoord=0,
        uitleg="Eerst weten waarover het gaat, dan waarom, dan wat eruit volgt. Die volgorde kan de lezer volgen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een uitspraak die je kan nagaan en controleren?",
        antwoord=["een feit", "feit"],
        uitleg="Een feit kan je opzoeken of meten; een mening niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil iemand overtuigen in een mail. Welk register kies je bij een onbekende volwassene?",
        opties=[
            "formeel, met u en een nette slotgroet",
            "informeel, met jij en een paar smileys",
            "dialect, want dat klinkt het eerlijkst",
            "jongerentaal, want dat valt meer op",
        ],
        antwoord=0,
        uitleg="Een formele mail sluit je niet af met 'groetjes', en smileys horen er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je jezelf als je je eigen argumentatieve tekst nog eens naleest?",
        opties=[
            "staat mijn stelling er duidelijk in?",
            "onderbouwt elk argument echt mijn standpunt?",
            "volgt mijn conclusie uit wat ervoor staat?",
            "heb ik meer woorden gebruikt dan gevraagd?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Lengte is geen kwaliteit. De drie eerste vragen gaan over of je tekst doet wat hij moet doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie in een gesprek de ander laat uitspreken, geeft daarmee toe dat de ander gelijk heeft.",
        antwoord=False,
        uitleg="Laten uitspreken is een beleefdheidsconventie, geen toegeving. Je kan daarna nog altijd antwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil je standpunt onderbouwen over afval in het park. Welk argument is het bruikbaarst?",
        opties=[
            "de gemeente haalde er vorig jaar twaalf ton zwerfvuil weg",
            "het is daar echt vreselijk vuil, dat ziet toch iedereen",
            "ik vind vuil op straat gewoon niet kunnen",
            "mijn buurman zegt ook al jaren hetzelfde",
        ],
        antwoord=0,
        uitleg="Een cijfer dat je kan nagaan, staat sterker dan drie keer hetzelfde oordeel in andere woorden.",
    ),
]
