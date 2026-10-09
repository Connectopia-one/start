# -*- coding: utf-8 -*-
"""Opvoeden: milieus, dimensies, stijlen en middelen.

Het eerste van twee thema's over pedagogiek, het vierde onderdeel van
gedragswetenschappen. Hier staat het gereedschap: wie opvoedt, waar het
gebeurt, met welke houding en met welke middelen.

De lijstjes staan letterlijk in de fiche:

    actoren: kind, opvoeder(s), omgeving
    opvoedingsmilieus: primair, secundair, tertiair
    opvoedingsdimensies: responsiviteit, gedragsmatige controle,
        psychologische controle
    opvoedingsstijlen: autoritair, democratisch-autoritatief, permissief of
        toegeeflijk, onverschillig of laissez-faire
    opvoedingsmiddelen: aanmoedigen of stimuleren, afleiden, belonen,
        gewoontevorming, informatieoverdracht, negeren en time-out, regels en
        grenzen stellen, straffen, voorbeeldgedrag of modelleren

De fiche zegt uitdrukkelijk dat een opvoedingsstijl een combinatie van
opvoedingsdimensies is. Daarom staan de dimensies in deel 1 en de stijlen in
deel 2: zonder de dimensies kan je de stijlen niet uit elkaar houden.

Deel 1 is opvoeding als proces, de actoren, de milieus en de dimensies.
Deel 2 zijn de stijlen en de middelen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met opvoeding als een transactioneel proces?",
        opties=[
            "kind en opvoeder beïnvloeden elkaar voortdurend",
            "de opvoeder beïnvloedt het kind, niet omgekeerd",
            "het kind beïnvloedt de opvoeder, niet omgekeerd",
            "opvoeding verloopt in vaste, afgesloten stappen",
        ],
        antwoord=0,
        uitleg="Transactioneel betekent heen en weer. Het gedrag van het kind verandert de aanpak van de ouder, en die aanpak verandert het kind weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie actoren zijn volgens de fiche bij opvoeding betrokken?",
        opties=[
            "het kind",
            "de opvoeder of opvoeders",
            "de omgeving",
            "de school",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het kind, de opvoeders en de omgeving. De school is een onderdeel van de omgeving, en meer bepaald van het secundaire milieu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het primaire opvoedingsmilieu?",
        opties=[
            "het gezin waarin een kind opgroeit",
            "de school en de opvang van een kind",
            "de media en de vrije tijd van een kind",
            "de buurt waarin een kind woont",
        ],
        antwoord=0,
        uitleg="Het primaire milieu is het gezin: het eerste en meest nabije milieu, waar de basis gelegd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij het secundaire opvoedingsmilieu?",
        opties=[
            "de school, de opvang en de jeugdbeweging",
            "het gezin en de naaste familie",
            "de reclame en de sociale media",
            "de wetten van een land",
        ],
        antwoord=0,
        uitleg="Het secundaire milieu bestaat uit plaatsen met een eigen opvoedingsopdracht, buiten het gezin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij het tertiaire opvoedingsmilieu?",
        opties=[
            "de media, de buurt en de vrije tijd",
            "het gezin en de ouders",
            "de school en de leerkrachten",
            "de opvang en de onthaalmoeder",
        ],
        antwoord=0,
        uitleg="Het tertiaire milieu voedt mee op zonder dat het de opdracht heeft: wat een kind ziet op straat, op het scherm en bij vrienden.",
    ),
    dict(
        type="invultekst",
        vraag="Het opvoedingsmilieu van het gezin heet het ... opvoedingsmilieu.",
        antwoord=["primaire", "primair"],
        uitleg="Het primaire opvoedingsmilieu. Daarna komen het secundaire en het tertiaire.",
    ),
    dict(
        type="waarofniet",
        vraag="De drie opvoedingsmilieus beïnvloeden elkaar: wat op school gebeurt, werkt thuis door en omgekeerd.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk naar de samenhang tussen de milieus.",
    ),
    dict(
        type="waarofniet",
        vraag="Het tertiaire opvoedingsmilieu heeft volgens de fiche geen invloed, omdat het geen opvoedingsopdracht heeft.",
        antwoord=False,
        uitleg="Niet waar. Het heeft geen opdracht, maar wel invloed. Een kind leert veel van wat het op een scherm of op straat ziet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel opvoedingsdimensies noemt de fiche?",
        opties=[
            "drie",
            "twee",
            "vier",
            "negen",
        ],
        antwoord=0,
        uitleg="Drie: responsiviteit, gedragsmatige controle en psychologische controle.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is responsiviteit als opvoedingsdimensie?",
        opties=[
            "warm ingaan op wat een kind nodig heeft",
            "duidelijke regels stellen en erop toezien",
            "een kind sturen via schuld en afkeuring",
            "een kind volledig zijn gang laten gaan",
        ],
        antwoord=0,
        uitleg="Responsief betekent antwoordend: je ziet wat een kind nodig heeft en je gaat er warm op in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is gedragsmatige controle als opvoedingsdimensie?",
        opties=[
            "regels stellen en toezien op wat een kind doet",
            "warm ingaan op wat een kind nodig heeft",
            "een kind sturen via schuldgevoel",
            "een kind alles zelf laten uitzoeken",
        ],
        antwoord=0,
        uitleg="Gedragsmatige controle gaat over grenzen, afspraken en toezicht op het gedrag zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is psychologische controle als opvoedingsdimensie?",
        opties=[
            "een kind sturen via schuld, afkeuring of liefde intrekken",
            "een kind sturen via duidelijke regels en toezicht",
            "een kind sturen via warmte en nabijheid",
            "een kind helemaal niet sturen",
        ],
        antwoord=0,
        uitleg="Psychologische controle werkt op het gevoel van het kind in plaats van op zijn gedrag. Daarom is ze de ongunstigste van de drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder zegt: als je dat doet, hou ik niet meer van je. Welke dimensie is dit?",
        opties=[
            "psychologische controle",
            "gedragsmatige controle",
            "responsiviteit",
            "gewoontevorming",
        ],
        antwoord=0,
        uitleg="De liefde van een ouder als voorwaarde gebruiken is psychologische controle. Het raakt het kind in zijn gevoel van eigenwaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder spreekt af dat de gsm om negen uur beneden ligt en kijkt dat ook na. Welke dimensie is dit?",
        opties=[
            "gedragsmatige controle",
            "psychologische controle",
            "responsiviteit",
            "informatieoverdracht",
        ],
        antwoord=0,
        uitleg="Een duidelijke afspraak over gedrag, met toezicht erop, is gedragsmatige controle.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder merkt dat zijn dochter stil is na school en gaat erbij zitten om te vragen wat er is. Welke dimensie is dit?",
        opties=[
            "responsiviteit",
            "gedragsmatige controle",
            "psychologische controle",
            "een opvoedingsmiddel",
        ],
        antwoord=0,
        uitleg="Zien wat een kind nodig heeft en er warm op ingaan, is responsiviteit.",
    ),
    dict(
        type="invultekst",
        vraag="De dimensie die een kind stuurt via schuldgevoel in plaats van via regels, heet ... controle.",
        antwoord=["psychologische", "psychologisch"],
        uitleg="Psychologische controle. De andere twee dimensies zijn responsiviteit en gedragsmatige controle.",
    ),
    dict(
        type="waarofniet",
        vraag="Een opvoedingsstijl is volgens de fiche een combinatie van opvoedingsdimensies.",
        antwoord=True,
        uitleg="Waar. Dat staat met zoveel woorden in de fiche, en het is de sleutel om de vier stijlen uit elkaar te houden.",
    ),
    dict(
        type="waarofniet",
        vraag="Gedragsmatige en psychologische controle zijn twee woorden voor dezelfde dimensie.",
        antwoord=False,
        uitleg="Niet waar. De eerste richt zich op het gedrag van een kind, de tweede op zijn gevoelens. Ze staan apart in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de omgeving volgens de fiche een actor in de opvoeding en niet alleen een decor?",
        opties=[
            "omdat ze mee bepaalt wat een kind leert en meemaakt",
            "omdat ze het gedrag van het kind volledig vastlegt",
            "omdat ze alleen in het tertiaire milieu een rol speelt",
            "omdat ze de opvoeders van elke keuze ontlast",
        ],
        antwoord=0,
        uitleg="De buurt, de school en de beelden rond een kind voeden mee op. Daarom staat de omgeving naast het kind en de opvoeders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind met een moeilijk temperament maakt een ouder ongeduldiger, en die ongeduldigheid maakt het kind nog moeilijker. Welk begrip past hier?",
        opties=[
            "opvoeding als transactioneel proces",
            "opvoeding in het tertiaire milieu",
            "psychologische controle",
            "gewoontevorming",
        ],
        antwoord=0,
        uitleg="De twee werken op elkaar in, in een kringetje. Dat is precies wat transactioneel betekent.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel opvoedingsstijlen noemt de fiche?",
        opties=[
            "vier",
            "drie",
            "vijf",
            "twee",
        ],
        antwoord=0,
        uitleg="Vier: autoritair, democratisch-autoritatief, permissief of toegeeflijk, en onverschillig of laissez-faire.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinatie van dimensies hoort bij de autoritaire opvoedingsstijl?",
        opties=[
            "veel controle en weinig responsiviteit",
            "veel controle en veel responsiviteit",
            "weinig controle en veel responsiviteit",
            "weinig controle en weinig responsiviteit",
        ],
        antwoord=0,
        uitleg="Autoritair betekent strenge regels zonder uitleg en met weinig warmte. Het is gehoorzamen omdat het moet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinatie hoort bij de democratisch-autoritatieve opvoedingsstijl?",
        opties=[
            "veel controle en veel responsiviteit",
            "veel controle en weinig responsiviteit",
            "weinig controle en veel responsiviteit",
            "weinig controle en weinig responsiviteit",
        ],
        antwoord=0,
        uitleg="Duidelijke grenzen én warmte, met uitleg erbij. Dat is de stijl die in onderzoek het gunstigst uitkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinatie hoort bij de permissieve of toegeeflijke stijl?",
        opties=[
            "weinig controle en veel responsiviteit",
            "veel controle en veel responsiviteit",
            "veel controle en weinig responsiviteit",
            "weinig controle en weinig responsiviteit",
        ],
        antwoord=0,
        uitleg="Veel warmte, weinig grenzen. De ouder wil geen conflict en geeft toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinatie hoort bij de onverschillige of laissez-faire stijl?",
        opties=[
            "weinig controle en weinig responsiviteit",
            "veel controle en weinig responsiviteit",
            "weinig controle en veel responsiviteit",
            "veel controle en veel responsiviteit",
        ],
        antwoord=0,
        uitleg="Geen grenzen en geen warmte. Van de vier is dit de stijl met de ongunstigste gevolgen voor een kind.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder zegt: dat doe je omdat ik het zeg, en verder geen discussie. Welke stijl is dit?",
        opties=[
            "autoritair",
            "democratisch-autoritatief",
            "permissief",
            "onverschillig",
        ],
        antwoord=0,
        uitleg="Een regel zonder uitleg en zonder gesprek is de autoritaire stijl.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder legt uit waarom de gsm om negen uur beneden ligt, luistert naar het bezwaar, en houdt de afspraak toch. Welke stijl is dit?",
        opties=[
            "democratisch-autoritatief",
            "autoritair",
            "permissief",
            "onverschillig",
        ],
        antwoord=0,
        uitleg="Grens én gesprek: de regel blijft, maar het kind wordt gehoord en krijgt uitleg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder vindt elke afspraak lastig en laat de gsm maar op de kamer liggen om ruzie te vermijden. Welke stijl is dit?",
        opties=[
            "permissief of toegeeflijk",
            "autoritair",
            "democratisch-autoritatief",
            "onverschillig of laissez-faire",
        ],
        antwoord=0,
        uitleg="De ouder is wel betrokken maar stelt geen grens. Dat is de permissieve of toegeeflijke stijl.",
    ),
    dict(
        type="invultekst",
        vraag="De opvoedingsstijl met veel warmte en veel duidelijke grenzen heet democratisch-...",
        antwoord=["autoritatief", "autoritatieve"],
        uitleg="Democratisch-autoritatief. Let op het verschil met autoritair: daar zijn er wel grenzen maar geen warmte.",
    ),
    dict(
        type="waarofniet",
        vraag="Van de vier stijlen komt de democratisch-autoritatieve in onderzoek het gunstigst uit voor de ontwikkeling van een kind.",
        antwoord=True,
        uitleg="Waar. Grenzen met warmte en uitleg geven kinderen zowel houvast als ruimte om zelfstandig te worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Autoritair en autoritatief betekenen hetzelfde.",
        antwoord=False,
        uitleg="Niet waar, en dat is de klassieke valkuil. Autoritair is streng zonder warmte, autoritatief is streng met warmte en uitleg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken noemt de fiche een opvoedingsmiddel?",
        opties=[
            "belonen",
            "negeren en time-out",
            "voorbeeldgedrag of modelleren",
            "responsiviteit",
            "psychologische controle",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opvoedingsmiddelen zijn concrete manieren van aanpakken. Responsiviteit en psychologische controle zijn dimensies, geen middelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder laat een peuter elke avond in dezelfde orde tanden poetsen, pyjama aandoen en voorlezen. Welk opvoedingsmiddel is dit?",
        opties=[
            "gewoontevorming",
            "informatieoverdracht",
            "belonen",
            "afleiden",
        ],
        antwoord=0,
        uitleg="Een vast ritme opbouwen zodat iets vanzelf gaat, is gewoontevorming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een peuter wil iets dat niet mag, en de ouder wijst hem iets anders aan dat even leuk is. Welk opvoedingsmiddel is dit?",
        opties=[
            "afleiden",
            "negeren",
            "straffen",
            "belonen",
        ],
        antwoord=0,
        uitleg="Afleiden werkt vooral bij jonge kinderen: je haalt de aandacht weg in plaats van een discussie te beginnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder legt uit waarom je je handen moet wassen voor je eet. Welk opvoedingsmiddel is dit?",
        opties=[
            "informatieoverdracht",
            "gewoontevorming",
            "aanmoedigen",
            "regels en grenzen stellen",
        ],
        antwoord=0,
        uitleg="Uitleg en kennis geven is informatieoverdracht. Elke dag samen handen wassen zou gewoontevorming zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ouder ruimt zelf altijd zijn bord af, zonder er iets over te zeggen, en het kind doet het na. Welk opvoedingsmiddel is dit?",
        opties=[
            "voorbeeldgedrag of modelleren",
            "informatieoverdracht",
            "gewoontevorming",
            "aanmoedigen of stimuleren",
        ],
        antwoord=0,
        uitleg="Voorbeeldgedrag of modelleren. Het sluit aan bij het imitatieleren van Bandura uit het derde thema.",
    ),
    dict(
        type="invultekst",
        vraag="Het opvoedingsmiddel waarbij een kind even uit de situatie gehaald wordt om af te koelen, heet een ...",
        antwoord=["time-out", "timeout", "time out"],
        uitleg="Een time-out. De fiche zet negeren en time-out samen als één opvoedingsmiddel.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche vraagt niet alleen welk opvoedingsmiddel iemand gebruikt, maar ook waarom dat middel in die situatie het meest geschikte is.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk om het meest geschikte middel te kiezen en de keuze te verantwoorden.",
    ),
    dict(
        type="waarofniet",
        vraag="Straffen is volgens de fiche geen opvoedingsmiddel.",
        antwoord=False,
        uitleg="Niet waar. Straffen staat in de lijst van negen opvoedingsmiddelen. De vraag is wanneer het geschikt is, niet of het bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een opvoedingsdimensie en een opvoedingsmiddel?",
        opties=[
            "een dimensie is een houding, een middel is een aanpak",
            "een middel is een houding, een dimensie is een aanpak",
            "een dimensie geldt thuis, een middel op school",
            "een dimensie geldt bij peuters, een middel bij tieners",
        ],
        antwoord=0,
        uitleg="Er zijn drie dimensies die een houding beschrijven en negen middelen die concreet zeggen wat je doet. De stijl is de combinatie van de dimensies.",
    ),
]
