# -*- coding: utf-8 -*-
"""Spreken, gesprekken en de beoordeling van een mondelinge opdracht.

Dit thema bestaat alleen bij dubbele finaliteit. Op de doorstroomfiches weegt
het mondelinge deel ook mee, maar hier is het bijna een kwart van het examen:
spreken 8 %, mondelinge interactie 1 nog eens 8 % en mondelinge interactie 2
nog eens 8 %. Daar hoort leerstof bij die je wél achter een scherm kan leren,
ook al oefen je het gesprek zelf aan tafel: wat je zegt om een gesprek te
beginnen, gaande te houden en te beëindigen, wat een gepast register is, en
waarop een examinator je mondelinge opdracht beoordeelt.

De vakfiche zet bij de vereisten drie rijen die alleen voor het mondelinge
deel gelden: lichaamstaal, spreektempo en vlotheid, en uitspraak en intonatie.
Die drie staan hier in deel 2, naast de vijf rijen die ook voor schrijven
gelden.

Deel 1 gaat over wat je zegt: sociale contacten, informatie, mening en het
gesprek zelf. Deel 2 gaat over hoe het beoordeeld wordt, welke strategieën
helpen, en hoe het examen in elkaar zit.

Het ERK-niveau is A2, dus de voorbeeldzinnen blijven eenvoudig.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Je spreekt op een cursus iemand aan die je niet kent. Welke opening is gepast?",
         opties=["Excuse me, is this seat free?",
                 "Hey you, move over a bit.",
                 "Give me that seat please now.",
                 "You there, I want to sit down."],
         antwoord=0,
         uitleg="'Excuse me' is de gewone manier om een onbekende aan te spreken. De andere drie "
                "klinken als een bevel, en dat past niet bij iemand die je niet kent."),
    dict(type="meerkeuze",
         vraag="Welke zinnen gebruik je om afscheid te nemen?",
         opties=["See you tomorrow, then.",
                 "It was nice talking to you.",
                 "Have a good evening, bye.",
                 "What do you do for a living?"],
         antwoord=[0, 1, 2],
         uitleg="De eerste drie sluiten een gesprek af. De vierde opent er net een: je vraagt "
                "iemand wat voor werk hij of zij doet."),
    dict(type="invultekst",
         vraag="Vul het ontbrekende werkwoord in: 'Nice to … you.' Je zegt dit als je iemand "
               "voor het eerst de hand schudt.",
         antwoord=["meet"],
         uitleg="'Nice to meet you' zeg je bij een eerste kennismaking. Zie je iemand terug, dan "
                "zeg je 'Nice to see you'."),
    dict(type="meerkeuze",
         vraag="Je wil aan een vriend voorstellen om samen te gaan zwemmen. Welke zin past?",
         opties=["Why don't we go to the pool?",
                 "You go to the pool with me.",
                 "I order you to the pool now.",
                 "The pool is where you go now."],
         antwoord=0,
         uitleg="'Why don't we …?' of 'How about a swim?' zijn de gewone manieren om iets voor te "
                "stellen. De andere drie zijn bevelen, geen voorstellen."),
    dict(type="waarofniet",
         vraag="Bij een spreekopdracht ben je alleen aan het woord, bij een gesprek moet je "
               "reageren op je gesprekspartner.",
         antwoord=True,
         uitleg="Dat is precies het verschil. Bij spreken bouw je zelf een verhaaltje op; bij een "
                "gesprek hangt wat je zegt af van wat de ander net zei."),
    dict(type="meerkeuze",
         vraag="Waarom kan je een gesprek niet volledig op voorhand uitschrijven?",
         opties=["omdat je moet reageren op wat je gesprekspartner zegt",
                 "omdat je geen kladpapier krijgt bij het gesprek",
                 "omdat het gesprek te kort duurt om iets te zeggen",
                 "omdat je bij een gesprek geen Engels mag gebruiken"],
         antwoord=0,
         uitleg="Je krijgt voorbereidingstijd en je mag een plan maken, maar je weet niet wat de "
                "ander zal zeggen. Spontaan kunnen reageren hoort erbij."),
    dict(type="waarofniet",
         vraag="Je mag bij het gesprek je antwoorden woord voor woord van een blad voorlezen.",
         antwoord=False,
         uitleg="Voorlezen is geen gesprek. Je mag kernwoorden op papier zetten, maar je moet "
                "zelf formuleren en op de ander inspelen."),
    dict(type="meerkeuze",
         vraag="Welke zinnen vragen om informatie?",
         opties=["Could you tell me when the shop opens?",
                 "Do you know how much it costs?",
                 "Where can I find the station?",
                 "I think the shop opens at nine."],
         antwoord=[0, 1, 2],
         uitleg="De eerste drie zijn vragen. De vierde geeft net informatie in plaats van ze te "
                "vragen."),
    dict(type="meerkeuze",
         vraag="Iemand zegt 'I'm sorry I'm late.' Hoe reageer je het best?",
         opties=["That's all right, don't worry.",
                 "Yes, you really are late.",
                 "I do not accept that at all.",
                 "You always come late to this."],
         antwoord=0,
         uitleg="Reageren op een verontschuldiging hoort bij de alledaagse sociale contacten. Je "
                "neemt de spanning weg in plaats van ze groter te maken."),
    dict(type="invultekst",
         vraag="Vul één woord in: '… you very much for your help.' Je bedankt iemand.",
         antwoord=["thank", "thanks"],
         uitleg="'Thank you very much' is de volle vorm. 'Thanks' alleen is korter en informeler."),
    dict(type="meerkeuze",
         vraag="Je wil je mening geven over een film. Welke zin doet dat het duidelijkst?",
         opties=["I think the film was too long.",
                 "The film lasted two hours.",
                 "The film came out last year.",
                 "The film is about a family."],
         antwoord=0,
         uitleg="Alleen de eerste zegt wat jij ervan vindt. De drie andere geven feiten over de "
                "film, geen mening."),
    dict(type="waarofniet",
         vraag="'Tell me when the bus leaves' is beleefder dan 'Could you tell me when the bus "
               "leaves?'",
         antwoord=False,
         uitleg="Het is net omgekeerd. 'Could you …?' maakt van een bevel een vraag, en dat is de "
                "beleefde vorm tegenover iemand die je niet kent."),
    dict(type="meerkeuze",
         vraag="Je gesprekspartner spreekt te snel en je volgt niet meer. Wat zeg je?",
         opties=["Could you speak more slowly, please?",
                 "Stop talking so fast right now.",
                 "I will not listen to you anymore.",
                 "Your English is far too fast here."],
         antwoord=0,
         uitleg="Vragen om trager te spreken of om te herhalen is een strategie, geen zwakte. Je "
                "houdt het gesprek er net mee gaande."),
    dict(type="meerkeuze",
         vraag="Welke zinnen houden een gesprek gaande?",
         opties=["What happened next?",
                 "Really? Tell me more.",
                 "And what did you think of it?",
                 "Well, that was all I wanted."],
         antwoord=[0, 1, 2],
         uitleg="De eerste drie geven de ander een reden om verder te vertellen. De vierde sluit "
                "het gesprek juist af."),
    dict(type="meerkeuze",
         vraag="Hoe beëindig je een gesprek beleefd?",
         opties=["Thanks for your time, I have to go now.",
                 "Right, I am leaving, goodbye to you.",
                 "This talk is over, I stop listening.",
                 "I go away now because of the time."],
         antwoord=0,
         uitleg="Je bedankt en je geeft een reden. Zo laat je de ander niet met een afgebroken "
                "gesprek achter."),
    dict(type="invultekst",
         vraag="Vul één woord in: 'I'm … I'm late.' Je verontschuldigt je.",
         antwoord=["sorry", "afraid"],
         uitleg="'I'm sorry I'm late' is de gewone verontschuldiging. 'I'm afraid I'm late' kan "
                "ook en klinkt wat formeler."),
    dict(type="waarofniet",
         vraag="Je krijgt voor de mondelinge opdrachten voorbereidingstijd.",
         antwoord=True,
         uitleg="Je krijgt vijftien minuten voorbereidingstijd voor twee opdrachten. Spontaan "
                "reageren blijft daarnaast nodig."),
    dict(type="meerkeuze",
         vraag="Je kent het Engelse woord voor 'kruk' niet, maar je moet het zeggen. Wat doe je?",
         opties=["je omschrijft het: the stick you walk with",
                 "je zwijgt tot de examinator verder gaat",
                 "je zegt het Nederlandse woord gewoon luid",
                 "je begint helemaal opnieuw aan de opdracht"],
         antwoord=0,
         uitleg="Je doel bereiken met de woorden die je wél kent, is zelf een strategie. Zwijgen "
                "of overschakelen op het Nederlands brengt je boodschap niet over."),
    dict(type="meerkeuze",
         vraag="Je wil iemand uitnodigen voor je verjaardag. Welke zin past?",
         opties=["Would you like to come to my party?",
                 "You are coming to my party then.",
                 "My party is on Saturday, be there.",
                 "I have a party and you know that."],
         antwoord=0,
         uitleg="'Would you like to …?' laat de ander vrij om ja of nee te zeggen. Dat is wat een "
                "uitnodiging doet; de andere drie veronderstellen het antwoord al."),
    dict(type="meerkeuze",
         vraag="Welke vraag toont dat je echt belangstelling hebt in wat de ander vertelt?",
         opties=["How did you feel about that?",
                 "Can we talk about me now?",
                 "Is this story going to end?",
                 "Why are you telling me this?"],
         antwoord=0,
         uitleg="Interesse tonen in de ander hoort bij een geslaagd gesprek. De drie andere zetten "
                "de ander juist stil."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Wat betekent taakvoltooiing bij een mondelinge opdracht?",
         opties=["je doel is bereikt en je opdracht is volledig uitgevoerd",
                 "je hebt geen enkele grammaticale fout gemaakt",
                 "je hebt sneller gesproken dan de andere kandidaten",
                 "je hebt alle woorden uit het woordenboek gebruikt"],
         antwoord=0,
         uitleg="Taakvoltooiing kijkt naar je boodschap: is ze volledig, helder en ter zake, en "
                "heb je gedaan wat er gevraagd werd?"),
    dict(type="meerkeuze",
         vraag="Welke vereisten gelden alleen voor het mondelinge deel en niet voor een schrijfopdracht?",
         opties=["lichaamstaal",
                 "spreektempo en vlotheid",
                 "uitspraak en intonatie",
                 "tekststructuur en samenhang"],
         antwoord=[0, 1, 2],
         uitleg="Die drie kan je alleen beoordelen als iemand spreekt. Tekststructuur en samenhang "
                "wordt bij allebei bekeken."),
    dict(type="waarofniet",
         vraag="Een valse start of een herformulering maakt je spreekopdracht meteen onvoldoende.",
         antwoord=False,
         uitleg="Onderbrekingen, valse starts en herformuleringen zijn aanvaardbaar. Ook mensen die "
                "hun moedertaal spreken doen dat voortdurend."),
    dict(type="meerkeuze",
         vraag="Wat hoort bij 'register en beleefdheidsconventies'?",
         opties=["je taal aanpassen aan wie voor je zit",
                 "zo veel mogelijk moeilijke woorden kiezen",
                 "altijd even luid en even snel spreken",
                 "elke zin met een vraag laten eindigen"],
         antwoord=0,
         uitleg="Een gepast register is neutraal of informeel, naargelang de situatie. Tegen een "
                "onbekende klink je anders dan tegen een vriend."),
    dict(type="invultekst",
         vraag="Vul één woord in: je gebruikt een gepast …, neutraal of informeel.",
         antwoord=["register"],
         uitleg="Het register is de toon waarop je spreekt of schrijft. Scheldwoorden horen er in "
                "geen enkel register van een examen bij."),
    dict(type="waarofniet",
         vraag="Je uitspraak moet klinken als die van iemand die in Londen geboren is.",
         antwoord=False,
         uitleg="Je uitspraak moet helder genoeg zijn om je boodschap niet in de weg te staan. Een "
                "accent is geen fout."),
    dict(type="meerkeuze",
         vraag="Welke vragen stel je jezelf volgens het communicatiemodel voor je begint te spreken?",
         opties=["waarom spreek ik?",
                 "voor wie is mijn boodschap?",
                 "wat wil ik precies vertellen?",
                 "hoeveel woorden ken ik al?"],
         antwoord=[0, 1, 2],
         uitleg="Het communicatiemodel vraagt naar zender, doel, ontvanger, boodschap en kanaal. "
                "Hoeveel woorden je kent, staat daar los van."),
    dict(type="meerkeuze",
         vraag="Wat is een spreekplan met kernwoorden?",
         opties=["een lijstje van wat je in welke volgorde wil zeggen",
                 "de volledige tekst die je gaat voorlezen",
                 "een lijst met alle werkwoorden die je kent",
                 "het schema van hoe het examen verloopt"],
         antwoord=0,
         uitleg="Met kernwoorden hou je de draad vast zonder voor te lezen. Een uitgeschreven tekst "
                "klinkt meteen als een tekst."),
    dict(type="waarofniet",
         vraag="Lichaamstaal helpt je om je boodschap beter over te brengen en zegt je ook iets over "
               "je gesprekspartner.",
         antwoord=True,
         uitleg="Je gebruikt ze zelf, en je leest ze bij de ander af om te weten of je begrepen "
                "wordt. Daarom wordt ze mee beoordeeld."),
    dict(type="meerkeuze",
         vraag="Je hebt de indruk dat je gesprekspartner je niet begrijpt. Wat doe je?",
         opties=["je zegt het nog eens op een andere manier",
                 "je herhaalt dezelfde zin maar veel luider",
                 "je gaat verder met het volgende onderwerp",
                 "je wacht zwijgend tot de ander iets zegt"],
         antwoord=0,
         uitleg="Herformuleren is de strategie die werkt. Luider spreken verandert niets aan de "
                "woorden die niet aankwamen."),
    dict(type="invultekst",
         vraag="Vul het ontbrekende werkwoord in: 'Could you … that, please?' Je hebt iets niet "
               "begrepen en vraagt om het nog eens te zeggen.",
         antwoord=["repeat", "say"],
         uitleg="'Could you repeat that, please?' of 'Could you say that again, please?' Allebei "
                "vragen ze beleefd om een herhaling."),
    dict(type="meerkeuze",
         vraag="Hoe lang duurt het gesprek op het examen?",
         opties=["10 minuten", "30 minuten", "60 minuten", "90 minuten"],
         antwoord=0,
         uitleg="Het gesprek zelf duurt tien minuten. Daarvoor krijg je vijftien minuten om je "
                "twee opdrachten voor te bereiden."),
    dict(type="meerkeuze",
         vraag="Hoeveel voorbereidingstijd krijg je voor het gesprek, en voor hoeveel opdrachten?",
         opties=["15 minuten voor 2 opdrachten",
                 "15 minuten voor 6 opdrachten",
                 "45 minuten voor 2 opdrachten",
                 "45 minuten voor 6 opdrachten"],
         antwoord=0,
         uitleg="Je logt in het voorbereidingslokaal in, krijgt je twee opdrachten digitaal en mag "
                "op papier voorbereiden."),
    dict(type="waarofniet",
         vraag="De spreekopdracht neem je thuis op en dien je in vóór je naar het examencentrum gaat.",
         antwoord=True,
         uitleg="Je kan ze indienen tot drie dagen voor je digitale examen. Doe je dat niet, dan "
                "mag je niet deelnemen."),
    dict(type="meerkeuze",
         vraag="Wat gebeurt er als je je spreekopdracht niet op tijd indient?",
         opties=["je mag niet deelnemen aan het examen in het centrum",
                 "je krijgt een nul voor dat ene onderdeel",
                 "je legt die opdracht af na het gesprek",
                 "je krijgt een week uitstel om ze te maken"],
         antwoord=0,
         uitleg="Het tijdig indienen is de voorwaarde om aan het examen in het examencentrum deel "
                "te nemen."),
    dict(type="meerkeuze",
         vraag="Welke onderdelen maak je op de computer in het examencentrum?",
         opties=["lezen", "luisteren", "schrijven", "het gesprek"],
         antwoord=[0, 1, 2],
         uitleg="Het digitale examen bundelt lezen, luisteren en schrijven. Het gesprek voer je "
                "daarna met een examinator."),
    dict(type="invultekst",
         vraag="Hoeveel minuten duurt het digitale examen? Antwoord met het getal.",
         antwoord=["150", "150 minuten"],
         uitleg="Honderdvijftig minuten, dus tweeënhalf uur, voor lezen, luisteren en schrijven "
                "samen."),
    dict(type="meerkeuze",
         vraag="Spreken weegt 8 %, en de twee mondelinge interacties elk ook 8 %. Hoeveel is dat samen?",
         opties=["24 %", "16 %", "30 %", "8 %"],
         antwoord=0,
         uitleg="Samen is het mondelinge deel bijna een kwart van je punten. Lezen en luisteren "
                "zijn elk 30 %."),
    dict(type="waarofniet",
         vraag="Er is giscorrectie: voor een fout antwoord gaan er punten af.",
         antwoord=False,
         uitleg="Er is geen giscorrectie. Een vraag openlaten levert dus nooit meer op dan ze "
                "proberen."),
    dict(type="meerkeuze",
         vraag="Je zit vast en weet niet hoe je iets moet formuleren. Wat is de beste houding?",
         opties=["verder proberen met de woorden die je wél kent",
                 "wachten tot de examinator het woord geeft",
                 "overschakelen op het Nederlands tot het lukt",
                 "de opdracht overslaan en naar de volgende gaan"],
         antwoord=0,
         uitleg="Je doel bereiken telt, niet of je het mooiste woord vond. Laat je niet "
                "ontmoedigen en bouw je zin anders op."),
]
