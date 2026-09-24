# -*- coding: utf-8 -*-
"""De vragen voor "Register, taalvariatie en non-verbale communicatie" (✨ Spark, Nederlands).

Uit de vakfiche, deel Taalbeschouwing: overeenkomsten en verschillen tussen
variëteiten binnen de standaardtaal (Belgisch-Nederlands en
Nederlands-Nederlands), tussen Standaardnederlands, tussentaal en dialect, de
invloed van de communicatieve situatie (formeel of informeel register) en van
sociale factoren (jargon, jongerentaal), overeenkomsten tussen talen, en de
effecten van non-verbale communicatie en van stereotypering.

Deel 1 legt de begrippen vast. Deel 2 past ze toe op echte situaties: welk
register kies je, en wat doet je lichaamstaal of een emoji met je boodschap?
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je stuurt een bericht naar je beste vriend en een mail naar de directeur. Wat verandert er?",
        opties=[
            "De toon en de woordkeuze: het register",
            "Alleen de lengte",
            "Niets",
            "Alleen de spelling",
        ],
        antwoord=0,
        uitleg="Het register is de toon die bij de situatie past: informeel bij vrienden, formeel bij wie je niet goed kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is Standaardnederlands?",
        opties=[
            "De taal die overal in het taalgebied begrepen en aanvaard wordt",
            "De taal van één streek",
            "De taal van jongeren onderling",
            "Een taal zonder regels",
        ],
        antwoord=0,
        uitleg="Standaardnederlands gebruik je op school, in het nieuws en in officiële teksten: iedereen begrijpt het.",
    ),
    dict(
        type="invultekst",
        vraag="De taal die je alleen in één streek of dorp hoort, noem je ___.",
        antwoord="dialect",
        uitleg="Dialect is streekgebonden. Het is niet fout of slordig, maar het hoort in een andere situatie thuis dan de standaardtaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is tussentaal?",
        opties=[
            "Taal die tussen dialect en standaardtaal in zit",
            "Een taal uit een ander land",
            "De taal van een vertaling",
            "Geschreven taal zonder leestekens",
        ],
        antwoord=0,
        uitleg="'Ge gaat da nie doen, hè' is tussentaal: geen zuiver dialect, maar ook geen Standaardnederlands.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Ge' en 'gij' zijn de tussentalige varianten van welke woorden?",
        opties=["je en jij", "hij en zij", "wij en ons", "u en uw"],
        antwoord=0,
        uitleg="In het Standaardnederlands schrijf en zeg je 'je' en 'jij'. 'Ge/gij' hoor je vooral in Vlaanderen.",
    ),
    dict(
        type="waarofniet",
        vraag="Belgisch-Nederlands en Nederlands-Nederlands zijn allebei vormen van de standaardtaal.",
        antwoord=True,
        uitleg="Het zijn variëteiten binnen één standaardtaal. Vlamingen en Nederlanders spreken sommige woorden anders uit of kiezen andere woorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke situaties vragen om een formeel register?",
        opties=[
            "Een sollicitatiemail voor een vakantiejob",
            "Een brief aan de gemeente",
            "Een gesprek met een arts die je niet kent",
            "Een appje naar je zus",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij onbekenden en in officiële situaties kies je het formele register, met 'u' en verzorgde zinnen.",
    ),
    dict(
        type="invultekst",
        vraag="In een gesprek met een volwassene met wie je geen nauwe band hebt, gebruik je het woord ___ in plaats van 'jij'.",
        antwoord="u",
        uitleg="'U' hoort bij de beleefdheidsconventies van het formele register.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is jargon?",
        opties=[
            "De vaktaal van een bepaalde groep of een bepaald beroep",
            "Taal met veel fouten",
            "Een oude vorm van het Nederlands",
            "Een geheime taal",
        ],
        antwoord=0,
        uitleg="Een arts spreekt van 'een fractuur', een voetballer van 'een tegenaanval'. Onder elkaar is dat handig; tegen een leek niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waardoor wordt jongerentaal sterk beïnvloed?",
        opties=[
            "Door andere talen, zoals het Engels",
            "Door de spellingregels",
            "Door het woordenboek",
            "Door de grammatica van het Latijn",
        ],
        antwoord=0,
        uitleg="Jongerentaal leent volop uit het Engels, het Marokkaans en het Surinaams, en verandert snel.",
    ),
    dict(
        type="waarofniet",
        vraag="Welke taalvariëteit je kiest, hangt af van de situatie waarin je communiceert.",
        antwoord=True,
        uitleg="Op de speelplaats praat je anders dan in een sollicitatiegesprek. Dat is geen fout, dat is passend taalgebruik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij non-verbale communicatie?",
        opties=[
            "Je lichaamstaal en je houding",
            "Je gezichtsuitdrukking en je oogcontact",
            "Je intonatie, je tempo en je volume",
            "De lengte van je zinnen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat je zegt zonder woorden: gebaren, mimiek, afstand, kledij, maar ook hoe je stem klinkt.",
    ),
    dict(
        type="invultekst",
        vraag="Iemand aankijken terwijl je spreekt, noem je ___ maken.",
        antwoord="oogcontact",
        uitleg="Voldoende oogcontact met je gesprekspartner wordt bij een spreekopdracht mee beoordeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je typt op een forum een hele zin IN HOOFDLETTERS. Hoe komt dat over?",
        opties=["Schreeuwerig en storend", "Vriendelijk", "Grappig", "Formeel"],
        antwoord=0,
        uitleg="Hoofdletters worden online gelezen als roepen. Dat is een effect van non-verbale communicatie in geschreven taal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een smiley in een formele mail is ongepast.",
        antwoord=True,
        uitleg="In een appje met vrienden ondersteunt een smiley je boodschap. In een formele mail hoort hij niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het effect van stereotypering rond taal?",
        opties=[
            "Wie een bepaald dialect spreekt, wordt soms onterecht minder slim gevonden",
            "Dialect maakt je daadwerkelijk minder slim",
            "Standaardtaal is de enige juiste taal",
            "Stereotypen hebben geen gevolgen",
        ],
        antwoord=0,
        uitleg="Zo'n oordeel zegt niets over de spreker en alles over de vooroordelen van de luisteraar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke Nederlandse woorden lijken sterk op het Engels of het Frans?",
        opties=["water – water", "restaurant – restaurant", "kat – cat", "brood – szal"],
        antwoord=[0, 1, 2],
        uitleg="Verwante talen delen veel woorden. Die gelijkenis kan je helpen om een onbekend woord te begrijpen.",
    ),
    dict(
        type="waarofniet",
        vraag="In het nieuws op tv wordt meestal Standaardnederlands gesproken.",
        antwoord=True,
        uitleg="Het nieuws richt zich tot iedereen, dus kiest het de variëteit die overal begrepen wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft aan je oma die niets van computers weet, over een probleem met haar tablet. Wat doe je?",
        opties=[
            "Je vermijdt vaktaal en legt uit in gewone woorden",
            "Je gebruikt alle technische termen",
            "Je schrijft in jongerentaal",
            "Je schrijft in dialect",
        ],
        antwoord=0,
        uitleg="Je taalgebruik aanpassen aan je ontvanger is een strategie: jargon werkt alleen bij wie het kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen formeel en informeel taalgebruik?",
        opties=[
            "Formeel is afstandelijk en verzorgd, informeel is vertrouwd en losser",
            "Formeel is langer",
            "Informeel is altijd fout",
            "Formeel gebruik je alleen op papier",
        ],
        antwoord=0,
        uitleg="Allebei zijn ze juist. Het hangt af van wie je ontvanger is en van de situatie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je solliciteert per mail voor een vakantiejob. Welke aanhef kies je?",
        opties=["Geachte heer of mevrouw", "Hey!", "Dag maat", "Hallo jullie"],
        antwoord=0,
        uitleg="Een sollicitatie is de formeelste situatie die je op dit niveau tegenkomt: aanhef, 'u' en een nette slotgroet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke slotgroeten passen bij een formele mail?",
        opties=[
            "Met vriendelijke groeten",
            "Hoogachtend",
            "Met dank bij voorbaat",
            "Xxx",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn formeel of neutraal. Kusjes horen bij familie en vrienden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee vrienden spreken onder elkaar dialect, maar schakelen over op Standaardnederlands als er iemand bijkomt die het niet begrijpt. Wat tonen ze daarmee?",
        opties=[
            "Dat je je taalvariëteit aanpast aan je gesprekspartner",
            "Dat dialect fout is",
            "Dat standaardtaal moeilijker is",
            "Dat ze geen dialect kennen",
        ],
        antwoord=0,
        uitleg="Wie tussen variëteiten kan schakelen, communiceert net sterk. De situatie bepaalt de keuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Ik heb mijn gsm in de auto laten liggen' tegenover 'Ik heb mijn mobieltje in de auto laten liggen'. Wat is hier aan de hand?",
        opties=[
            "Een verschil tussen Belgisch-Nederlands en Nederlands-Nederlands",
            "Een spellingfout",
            "Een verschil tussen dialect en standaardtaal",
            "Jongerentaal",
        ],
        antwoord=0,
        uitleg="Allebei standaardtaal, maar 'gsm' hoor je in Vlaanderen en 'mobieltje' in Nederland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden zijn voorbeelden van vakjargon?",
        opties=[
            "buitenspel (voetbal)",
            "diagnose (geneeskunde)",
            "debet (boekhouding)",
            "tafel (dagelijks leven)",
        ],
        antwoord=[0, 1, 2],
        uitleg="Jargon is vaktaal binnen een beroep of hobby. 'Tafel' kent iedereen.",
    ),
    dict(
        type="waarofniet",
        vraag="Jargon gebruiken tegenover iemand die het vak niet kent, maakt je boodschap duidelijker.",
        antwoord=False,
        uitleg="Net omgekeerd: voor een leek is vaktaal een muur. Leg uit in gewone woorden.",
    ),
    dict(
        type="invultekst",
        vraag="De manier waarop je stem stijgt en daalt terwijl je spreekt, heet je ___.",
        antwoord="intonatie",
        uitleg="Intonatie, articulatie, tempo en volume horen bij je non-verbale communicatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je geeft een spreekbeurt en kijkt de hele tijd naar je blad. Welk effect heeft dat?",
        opties=[
            "Je publiek haakt af, want er is geen contact",
            "Je klinkt deskundiger",
            "Je spreekt vlotter",
            "Het maakt geen verschil",
        ],
        antwoord=0,
        uitleg="Oogcontact houdt je publiek erbij. Werk daarom met kernwoorden in plaats van een volledige tekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over emoji's kloppen?",
        opties=[
            "Ze kunnen je toon verduidelijken in een informeel bericht",
            "Ze zijn ongepast in formele communicatie",
            "Ze kunnen ook verkeerd begrepen worden",
            "Ze vervangen de leestekens",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een emoji is non-verbale communicatie op papier: handig onder vrienden, riskant bij onbekenden, en geen vervanging voor punten en komma's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand staat tijdens een gesprek heel dicht bij je. Waarover gaat dat?",
        opties=[
            "Over afstand, een onderdeel van non-verbale communicatie",
            "Over intonatie",
            "Over register",
            "Over articulatie",
        ],
        antwoord=0,
        uitleg="Hoeveel afstand je houdt, hoort bij je lichaamstaal en verschilt zelfs van land tot land.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kleding en je uiterlijk horen ook bij de boodschap die je uitstuurt.",
        antwoord=True,
        uitleg="De vakfiche noemt kleding en uiterlijk uitdrukkelijk bij de non-verbale communicatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in een appgroep: 'ok.' met een punt erachter. Waarom kan dat kil overkomen?",
        opties=[
            "Omdat een punt in een kort appbericht afstandelijk aanvoelt",
            "Omdat een punt daar fout is",
            "Omdat er geen hoofdletter staat",
            "Omdat 'ok' geen Nederlands is",
        ],
        antwoord=0,
        uitleg="Wat correct is, kan in een bepaald kanaal toch een andere toon krijgen. Dat is het effect van het medium.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke situaties kies je het informele register?",
        opties=[
            "Een berichtje naar een klasgenoot",
            "Een verjaardagskaartje voor je neef",
            "Een babbel met je trainer die je al jaren kent",
            "Een mail naar een onbekend bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij mensen met wie je een nauwe band hebt, mag het losser. Bij een onbekend bedrijf niet.",
    ),
    dict(
        type="invultekst",
        vraag="De taalvorm die tussen dialect en standaardtaal in ligt en die je vaak in Vlaamse tv-series hoort, heet ___.",
        antwoord="tussentaal",
        uitleg="Tussentaal klinkt vertrouwd, maar is geen standaardtaal. Op je examen spreek je Standaardnederlands.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om te weten dat talen op elkaar lijken?",
        opties=[
            "Omdat je de betekenis van een onbekend woord soms kan afleiden uit een andere taal",
            "Omdat je dan geen woordenboek meer nodig hebt",
            "Omdat alle talen dezelfde grammatica hebben",
            "Omdat je dan sneller spreekt",
        ],
        antwoord=0,
        uitleg="'Information', 'informatie', 'information': wie het verband ziet, raadt de betekenis.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie tussentaal spreekt, maakt daarmee automatisch spelfouten.",
        antwoord=False,
        uitleg="Spreken en schrijven zijn twee verschillende dingen. Tussentaal is gesproken taal, spelling gaat over geschreven taal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerkracht zegt met een glimlach: 'Dat is dan weer prachtig gedaan.' Wat kan er aan de hand zijn?",
        opties=[
            "De toon verandert de betekenis: het kan ironisch bedoeld zijn",
            "De zin is fout gespeld",
            "De zin is altijd een compliment",
            "Er ontbreekt een signaalwoord",
        ],
        antwoord=0,
        uitleg="Intonatie en gezichtsuitdrukking kunnen de betekenis van dezelfde woorden omkeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je merkt tijdens een gesprek dat je gesprekspartner zijn armen kruist en wegkijkt. Wat doe je?",
        opties=[
            "Je speelt erop in: je vraagt of iets niet duidelijk is",
            "Je praat gewoon sneller door",
            "Je zegt dat hij onbeleefd is",
            "Je stopt meteen met praten",
        ],
        antwoord=0,
        uitleg="De lichaamstaal van je gesprekspartner inschatten en erop reageren hoort bij mondelinge interactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over taalvariatie kloppen?",
        opties=[
            "Elke variëteit heeft haar eigen plaats in de maatschappij",
            "Dialect is niet minderwaardig aan standaardtaal",
            "Welke variëteit past, hangt af van de situatie",
            "Er bestaat maar één juiste vorm van het Nederlands",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vakfiche vertrekt van gelijkwaardige variëteiten met elk hun eigen gebruikssituatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet een tekst herschrijven van informeel naar formeel. Wat verander je?",
        opties=[
            "Je vervangt 'je' door 'u', schrapt emoji's en schrijft volledige zinnen",
            "Je maakt de tekst korter",
            "Je zet alles in het vet",
            "Je voegt jongerentaal toe",
        ],
        antwoord=0,
        uitleg="Formeel maken is: aanspreekvorm, woordkeuze en zinsbouw verzorgen, en alles wat te los klinkt weghalen.",
    ),
]
