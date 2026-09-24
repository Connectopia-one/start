# -*- coding: utf-8 -*-
"""De vragen voor "Literatuur en beeldspraak" (✨ Spark, Nederlands).

Uit de vakfiche, deel Literatuur: je eigen beleving en interpretatie van
literaire teksten verwoorden (een strip, een lied, een gedicht, een verhaal,
een blog) met begrippen als fictie, non-fictie, personages, verhaallijn, tijd
en ruimte. Voor het mondelinge examen lees je twee boeken en denk je na over
wat je aansprak, in welk personage je jezelf herkent en welke emotie de tekst
oproept. Daarbij horen ook de betekenisrelaties letterlijk en figuurlijk, en
beeldspraak en vergelijking.

Deel 1 legt de begrippen vast aan de hand van korte voorbeelden. Deel 2 vraagt
je te interpreteren en je mening te verwoorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Een boek vertelt het verzonnen verhaal van een meisje dat op een onbewoond eiland belandt. Wat is dat?",
        opties=["Fictie", "Non-fictie", "Een handleiding", "Een verslag"],
        antwoord=0,
        uitleg="Fictie is verzonnen. Non-fictie gaat over de werkelijkheid, zoals een biografie of een informatief boek.",
    ),
    dict(
        type="invultekst",
        vraag="Een boek over de echte geschiedenis van de Titanic is ___.",
        antwoord="non-fictie",
        uitleg="Non-fictie vertelt over wat echt gebeurd is of echt bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de personages van een verhaal?",
        opties=[
            "De figuren die in het verhaal voorkomen",
            "De plaatsen waar het verhaal speelt",
            "De hoofdstukken",
            "De woorden die rijmen",
        ],
        antwoord=0,
        uitleg="Het hoofdpersonage staat centraal; de andere figuren zijn nevenpersonages.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met de ruimte van een verhaal?",
        opties=[
            "De plaats waar het verhaal zich afspeelt",
            "De tijd die het verhaal duurt",
            "Het aantal bladzijden",
            "De naam van de schrijver",
        ],
        antwoord=0,
        uitleg="Een school, een bos, een schip: de ruimte bepaalt mee de sfeer van het verhaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke begrippen gebruik je om over een verhaal te praten?",
        opties=["personages", "verhaallijn", "tijd en ruimte", "voegwoord"],
        antwoord=[0, 1, 2],
        uitleg="Die drie horen bij literatuur. Een voegwoord is een woordsoort en hoort bij het taalsysteem.",
    ),
    dict(
        type="invultekst",
        vraag="De rode draad van gebeurtenissen in een verhaal noem je de ___.",
        antwoord="verhaallijn",
        uitleg="De verhaallijn loopt van de beginsituatie over een probleem naar de oplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="Een strip is ook een literaire tekst.",
        antwoord=True,
        uitleg="Een strip, een lied, een gedicht, een verhaal en een blog staan allemaal in de vakfiche als literaire tekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Hij at zijn bord leeg.' Is dat letterlijk of figuurlijk?",
        opties=["Letterlijk", "Figuurlijk", "Allebei", "Geen van beide"],
        antwoord=0,
        uitleg="Hij at wat op zijn bord lag: precies wat de woorden zeggen. Dat is letterlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Hij is door het lint gegaan.' Wat betekent die zin?",
        opties=[
            "Hij is heel kwaad geworden",
            "Hij is door een lint gelopen",
            "Hij heeft een lint gekocht",
            "Hij is gevallen",
        ],
        antwoord=0,
        uitleg="Dat is figuurlijk taalgebruik: de woorden betekenen samen iets anders dan wat er letterlijk staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vergelijking in taal?",
        opties=[
            "Twee dingen naast elkaar zetten met 'als' of 'zoals'",
            "Twee woorden die rijmen",
            "Een woord met twee betekenissen",
            "Een zin zonder werkwoord",
        ],
        antwoord=0,
        uitleg="'Zo koud als ijs', 'hij rent als een haas': het vergelijkingswoord staat er nog bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen bevatten een vergelijking?",
        opties=[
            "Ze zwom als een vis.",
            "Zijn handen waren zo koud als ijs.",
            "Hij zong zoals een vogel in de lente.",
            "De zon ging onder.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie gebruiken 'als' of 'zoals'. De laatste zin is gewoon een vaststelling.",
    ),
    dict(
        type="invultekst",
        vraag="Taalgebruik waarbij je iets anders bedoelt dan wat er letterlijk staat, noem je ___ taalgebruik.",
        antwoord="figuurlijk",
        uitleg="Uitdrukkingen, spreekwoorden en beeldspraak zijn figuurlijk.",
    ),
    dict(
        type="waarofniet",
        vraag="'Beeldspraak' betekent dat je met woorden een beeld oproept.",
        antwoord=True,
        uitleg="'Een zee van tijd', 'de avond van zijn leven': je gebruikt het ene beeld om iets anders te tonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt een dichter rijm en ritme?",
        opties=[
            "Om zijn tekst te laten klinken en beter te laten hangen",
            "Omdat dat verplicht is in een gedicht",
            "Om de tekst korter te maken",
            "Om moeilijke woorden te vermijden",
        ],
        antwoord=0,
        uitleg="Klank hoort bij de vorm van een literaire tekst. Niet elk gedicht rijmt trouwens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een blog waarin iemand vertelt over zijn reis door Noorwegen. Wat is dat?",
        opties=[
            "Non-fictie, verteld als een verhaal",
            "Fictie",
            "Een handleiding",
            "Een recensie",
        ],
        antwoord=0,
        uitleg="Het is echt gebeurd, dus non-fictie, maar de vorm is verhalend en persoonlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de tijd van een verhaal?",
        opties=[
            "In welke periode het speelt",
            "Hoe lang de gebeurtenissen duren",
            "Of er sprongen in de tijd zijn",
            "Hoeveel personages er zijn",
        ],
        antwoord=[0, 1, 2],
        uitleg="Tijd gaat over de periode, de duur en de volgorde. Het aantal personages hoort daar niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor het mondelinge deel van het examen lees je twee boeken uit de lectuurlijst.",
        antwoord=True,
        uitleg="Je moet ze niet meebrengen, maar je moet er wel over kunnen vertellen: wat sprak je aan en waarom?",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag helpt je om je beleving van een boek te verwoorden?",
        opties=[
            "Waarom herken je je wel of niet in een personage?",
            "Hoeveel bladzijden telt het boek?",
            "In welk jaar is het gedrukt?",
            "Wie is de uitgever?",
        ],
        antwoord=0,
        uitleg="Je beleving gaat over wat het boek met jou doet, niet over de technische gegevens.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Het regende pijpenstelen.' Wat voor taalgebruik is dat?",
        opties=["Beeldspraak", "Een vergelijking met 'als'", "Letterlijk", "Jargon"],
        antwoord=0,
        uitleg="Er vallen geen pijpenstelen uit de lucht. Het beeld van rechte, dikke stralen vervangt de gewone woorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je literatuur, volgens de vakfiche?",
        opties=[
            "Om kennis te maken met andere mensen, ideeën en ervaringen",
            "Om sneller te leren typen",
            "Om je spelling te verbeteren",
            "Om nieuwe vakwoorden te leren",
        ],
        antwoord=0,
        uitleg="Verhalen lezen laat je kijken door de ogen van iemand anders.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In een verhaal blijft het hoofdpersonage rustig terwijl iedereen in paniek raakt. Wat leer je daaruit over dat personage?",
        opties=[
            "Iets over zijn karakter, zonder dat het er letterlijk staat",
            "Niets",
            "Dat het verhaal fictie is",
            "Dat het verhaal in de zomer speelt",
        ],
        antwoord=0,
        uitleg="Schrijvers tonen karakters vaak via gedrag in plaats van het te benoemen. Als lezer leid je het af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een verhaal begint met de laatste gebeurtenis en vertelt daarna hoe het zover kwam. Wat doet de schrijver?",
        opties=[
            "Hij speelt met de tijd, met een terugblik",
            "Hij verandert de ruimte",
            "Hij gebruikt beeldspraak",
            "Hij schrijft non-fictie",
        ],
        antwoord=0,
        uitleg="Een terugblik of flashback is een sprong in de tijd. De volgorde van het vertellen is niet altijd de volgorde van de gebeurtenissen.",
    ),
    dict(
        type="waarofniet",
        vraag="In fictie mogen plaatsen en personen bestaan die in het echt ook bestaan.",
        antwoord=True,
        uitleg="Een verzonnen verhaal kan zich afspelen in een echte stad. Het verhaal zelf is dan nog altijd fictie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over je eigen mening over een boek kloppen?",
        opties=[
            "Je mag een boek saai vinden, zolang je uitlegt waarom",
            "Je mening wordt sterker met voorbeelden uit het boek",
            "Twee lezers mogen hetzelfde boek anders beleven",
            "Alleen een positieve mening is een goede mening",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het gaat om je beleving én je onderbouwing, niet om het juiste oordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Mijn broer is een beer.' Wat wil die zin zeggen?",
        opties=[
            "Hij is groot en sterk, of knorrig: het is beeldspraak",
            "Hij is echt een dier",
            "Hij heet Beer",
            "Hij houdt van beren",
        ],
        antwoord=0,
        uitleg="Hier wordt het beeld zonder 'als' gebruikt. Dat maakt het sterker dan de vergelijking 'sterk als een beer'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een vergelijking en beeldspraak zonder vergelijkingswoord?",
        opties=[
            "Bij een vergelijking staat er 'als' of 'zoals', bij beeldspraak niet",
            "Beeldspraak rijmt altijd",
            "Een vergelijking is altijd langer",
            "Er is geen verschil",
        ],
        antwoord=0,
        uitleg="'Hij is zo sterk als een beer' is een vergelijking. 'Hij is een beer' zet het beeld in de plaats van de zaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen zijn figuurlijk bedoeld?",
        opties=[
            "Ze heeft een hart van goud.",
            "Hij zit in zak en as.",
            "Dat kost een fortuin.",
            "De kast staat in de gang.",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uitdrukkingen zijn figuurlijk. De laatste zin bedoelt precies wat ze zegt.",
    ),
    dict(
        type="invultekst",
        vraag="Het personage dat in een verhaal centraal staat, is het ___.",
        antwoord="hoofdpersonage",
        uitleg="Rond het hoofdpersonage draait de verhaallijn; de andere figuren zijn nevenpersonages.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gedicht gebruikt korte regels, witruimte en herhaling. Waarover gaat dat?",
        opties=[
            "Over de vorm, die de betekenis mee draagt",
            "Over de spelling",
            "Over de spreektaal",
            "Over de bronvermelding",
        ],
        antwoord=0,
        uitleg="In poëzie is de lay-out zelf betekenisvol: waar een regel afbreekt, hoor je een pauze.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lied kan je op dezelfde manier bespreken als een gedicht.",
        antwoord=True,
        uitleg="Een liedtekst heeft ook beelden, rijm, ritme en een boodschap. Alleen komt er muziek bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vertelt op het examen over een boek. Welke uitspraak is het sterkst?",
        opties=[
            "Ik herkende mezelf in Sam, omdat hij ook niet durfde te zeggen wat hij dacht.",
            "Het was wel oké.",
            "Ik vond het niks.",
            "Het boek telt 224 bladzijden.",
        ],
        antwoord=0,
        uitleg="Je beleving verwoorden betekent: zeggen wat je raakte en waarom, met een voorbeeld erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een verhaal verandert de ruimte van een drukke stad naar een verlaten huis. Wat doet dat met het verhaal?",
        opties=[
            "Het verandert de sfeer en de spanning",
            "Het verandert de spelling",
            "Het maakt het verhaal non-fictie",
            "Het verandert niets",
        ],
        antwoord=0,
        uitleg="Ruimte en sfeer hangen samen. Schrijvers kiezen hun decor bewust.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen kan je jezelf stellen tijdens het lezen van je examenboek?",
        opties=[
            "Waarom roept deze tekst bij mij een bepaalde emotie op?",
            "Hoe zou ik in die situatie reageren?",
            "Hoe zou ik het boek laten eindigen?",
            "Hoeveel exemplaren zijn er verkocht?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie vragen staan in de vakfiche. Verkoopcijfers zeggen niets over jouw beleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een strip vertelt veel zonder woorden. Waarmee doet hij dat?",
        opties=[
            "Met beeld: gezichten, kaders en kleuren",
            "Met voetnoten",
            "Met tussentitels",
            "Met een inhoudstafel",
        ],
        antwoord=0,
        uitleg="In een strip dragen tekening en tekst samen het verhaal. Wie alleen de tekstballonnen leest, mist de helft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verhaal dat in de ik-vorm geschreven is, is daarom waargebeurd.",
        antwoord=False,
        uitleg="De ik-verteller kan een verzonnen personage zijn. Vorm en werkelijkheid zijn twee verschillende dingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Hij kreeg het op zijn heupen.' Wat doe je als je deze uitdrukking niet kent?",
        opties=[
            "Je leidt de betekenis af uit de situatie in de tekst",
            "Je leest de zin letterlijk",
            "Je slaat het hoofdstuk over",
            "Je verandert de zin",
        ],
        antwoord=0,
        uitleg="Figuurlijke taal versta je meestal uit de context. Wie letterlijk leest, komt bij onzin uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden beschrijven de sfeer van een tekst?",
        opties=["spannend", "melancholisch", "grappig", "alfabetisch"],
        antwoord=[0, 1, 2],
        uitleg="Sfeerwoorden zeggen hoe een tekst aanvoelt. 'Alfabetisch' gaat over volgorde, niet over gevoel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de verhaallijn en de samenvatting van een boek?",
        opties=[
            "De verhaallijn is de opbouw van de gebeurtenissen, de samenvatting is jouw korte weergave ervan",
            "Er is geen verschil",
            "Een samenvatting bevat altijd het einde niet",
            "De verhaallijn staat op de achterflap",
        ],
        antwoord=0,
        uitleg="De verhaallijn zit in het boek; de samenvatting maak jij ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zeggen twee lezers soms iets heel anders over hetzelfde gedicht?",
        opties=[
            "Omdat een literaire tekst ruimte laat voor interpretatie",
            "Omdat een van de twee zich vergist",
            "Omdat gedichten geen betekenis hebben",
            "Omdat het gedicht fout geschreven is",
        ],
        antwoord=0,
        uitleg="Interpreteren mag, zolang je je lezing kan steunen op wat er staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft zelf een kort verhaal. Welke bouwstenen heb je zeker nodig?",
        opties=[
            "Personages",
            "Een plaats en een tijd",
            "Een probleem dat de verhaallijn op gang brengt",
            "Een bronnenlijst",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zonder probleem geen verhaal. Een bronnenlijst hoort bij een informatieve tekst.",
    ),
]
