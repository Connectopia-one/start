# -*- coding: utf-8 -*-
"""Wetenschappelijk onderzoek, ontwerpen en STEM — 🌍 Beyond, biologie.

Deel 1 gaat over de stappen van een onderzoek: van de probleemstelling over de
onderzoeksvraag en de hypothese naar een plan met variabelen, een
controleproef en genoeg herhalingen. Deel 2 gaat over het verwerken van de
gegevens, het lezen van een grafiek, het besluiten, het reflecteren en het
ontwerpen van een oplossing.

Op het examen krijgt de leerling een opgave waarin deze vaardigheden op een
echt probleem toegepast worden. De criteria voor een goede onderzoeksvraag
staan daar in een bijlage bij, dus hoeven ze niet uit het hoofd gekend te
worden; wat telt, is ze kunnen gebruiken. Daarom vertrekt bijna elke vraag van
een concreet opzet met planten, enzymen of bacteriën.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarmee begint een wetenschappelijk onderzoek?",
        opties=[
            "met een probleem afbakenen",
            "met de gegevens verzamelen",
            "met een besluit opschrijven",
            "met een grafiek tekenen",
        ],
        antwoord=0,
        uitleg="Eerst wordt duidelijk gemaakt wat precies onderzocht wordt en wat niet. "
        "Pas daarna volgen de vraag, de hypothese en het plan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een goede onderzoeksvraag? Kruis alles aan wat juist is.",
        opties=[
            "ze is met een meting te beantwoorden",
            "ze is nauwkeurig afgebakend",
            "ze is zo ruim mogelijk gesteld",
            "ze bevat het antwoord al",
        ],
        antwoord=[0, 1],
        uitleg="Een vraag als waarom groeien planten is te ruim om te meten. Een vraag "
        "over één factor, één soort en één omstandigheid is wel te onderzoeken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het verwachte antwoord dat je vooraf opschrijft?",
        antwoord=["hypothese", "een hypothese", "de hypothese"],
        uitleg="Een hypothese is een toetsbare verwachting, geen gok achteraf. Ze mag ook "
        "weerlegd worden: dat is evengoed een resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de onafhankelijke variabele in een proef?",
        opties=[
            "wat de onderzoeker zelf laat verschillen",
            "wat de onderzoeker meet als resultaat",
            "wat in elke opstelling gelijk blijft",
            "wat de onderzoeker vooraf verwacht",
        ],
        antwoord=0,
        uitleg="Je kiest zelf de hoeveelheid licht, de temperatuur of de concentratie. Wat "
        "daaruit volgt en gemeten wordt, is de afhankelijke variabele.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of meer licht de fotosynthese versnelt. Wat is de afhankelijke variabele?",
        opties=[
            "het aantal zuurstofbelletjes per minuut",
            "de sterkte van de lamp",
            "de afstand tussen de lamp en de plant",
            "de soort waterplant",
        ],
        antwoord=0,
        uitleg="De lichtsterkte wordt ingesteld, de zuurstofproductie wordt gemeten. Wat je "
        "meet, hangt af van wat je instelt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de factoren die je in elke opstelling gelijk houdt?",
        antwoord=[
            "constante variabelen",
            "constanten",
            "constante factoren",
        ],
        uitleg="Alleen zo weet je dat het verschil van je onafhankelijke variabele komt. "
        "Verandert er meer tegelijk, dan zegt het resultaat niets.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de reeks zonder de onderzochte factor, waarmee je je resultaat vergelijkt?",
        antwoord=["controleproef", "de controleproef", "blanco"],
        uitleg="Een reeks zonder enzym, zonder licht of zonder meststof geeft het "
        "vergelijkingspunt. Zonder dat punt weet je niet of het effect van jouw factor komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting meerdere keren?",
        opties=[
            "om toevallige afwijkingen te laten uitmiddelen",
            "om de proef langer te laten duren",
            "om de hypothese toch nog zeker juist te krijgen",
            "om minder materiaal te gebruiken",
        ],
        antwoord=0,
        uitleg="Eén meting kan een uitschieter zijn. Pas bij meerdere herhalingen zie je "
        "wat het echte verband is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die weerlegd wordt, betekent dat de proef mislukt is.",
        antwoord=False,
        uitleg="Ook een weerlegde verwachting leert je iets. Het resultaat telt, niet of je "
        "gelijk had.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je test een meststof op tien planten in de zon en tien zonder meststof in de schaduw. Wat is er fout?",
        opties=[
            "er verandert meer dan één factor tegelijk",
            "er zijn te weinig planten gebruikt in deze proef",
            "de meststof is verkeerd afgewogen",
            "de proef duurt niet lang genoeg",
        ],
        antwoord=0,
        uitleg="Groeien de bemeste planten beter, dan weet je niet of dat door de meststof "
        "of door de zon komt. Alle andere factoren moeten gelijk blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een onderzoeksplan? Kruis alles aan wat juist is.",
        opties=[
            "welk materiaal je nodig hebt",
            "hoe je gaat meten en hoe vaak",
            "welke conclusie je zult trekken",
            "welke cijfers je wilt uitkomen",
        ],
        antwoord=[0, 1],
        uitleg="Een plan beschrijft de werkwijze zo dat iemand anders ze kan overdoen. De "
        "conclusie schrijf je pas als de gegevens er zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Je noteert je waarnemingen tijdens de proef, niet achteraf uit het hoofd.",
        antwoord=True,
        uitleg="Wie achteraf noteert, vult onbewust aan wat hij verwachtte. Dat is een van "
        "de makkelijkste manieren om een onderzoek waardeloos te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je in een proef met zaden liever vijftig zaden dan drie?",
        opties=[
            "een grotere steekproef geeft een betrouwbaarder beeld",
            "vijftig zaden groeien sneller dan drie",
            "vijftig zaden hebben minder water nodig",
            "met drie zaden mag je geen grafiek meer tekenen",
        ],
        antwoord=0,
        uitleg="Bij drie zaden kan één slecht zaad het hele resultaat kantelen. Hoe groter "
        "de groep, hoe minder het toeval doorweegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een meetfout die je door beter werken kunt vermijden?",
        opties=[
            "de stopwatch telkens te laat indrukken",
            "de natuurlijke variatie tussen planten",
            "het weer dat van dag tot dag verschilt",
            "het verschil tussen twee zaadsoorten",
        ],
        antwoord=0,
        uitleg="Een systematische fout zit in de werkwijze en is te verhelpen. Natuurlijke "
        "variatie hoort bij het onderzochte materiaal zelf.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een meting die duidelijk buiten de rij van de andere valt?",
        antwoord=["uitschieter", "een uitschieter", "uitbijter"],
        uitleg="Een uitschieter gooi je niet zomaar weg. Je zoekt eerst of er een oorzaak "
        "voor was, en je vermeldt wat je ermee gedaan hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meting die niet in je verwachting past, mag je weglaten uit je verslag.",
        antwoord=False,
        uitleg="Dat is het resultaat naar je hypothese toe schrijven. Wat je weglaat of "
        "niet meerekent, vermeld je altijd met de reden erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wilt weten of een enzym sneller werkt bij hogere temperatuur. Welke opstelling past?",
        opties=[
            "vijf buizen met hetzelfde enzym bij vijf temperaturen",
            "vijf buizen met vijf enzymen bij vijf temperaturen",
            "één buis die je vijf keer opwarmt en afkoelt",
            "vijf buizen bij dezelfde temperatuur, vijf dagen na elkaar",
        ],
        antwoord=0,
        uitleg="Alleen de temperatuur mag verschillen. Verandert het enzym mee, dan meet je "
        "twee dingen tegelijk en weet je niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet iemand anders je proef kunnen overdoen? Kruis alles aan wat juist is.",
        opties=[
            "pas als het resultaat terugkomt, is het betrouwbaar",
            "zo komt een fout in je werkwijze aan het licht",
            "zo hoef jij zelf niet meer te meten",
            "zo is er maar één verslag nodig",
        ],
        antwoord=[0, 1],
        uitleg="Reproduceerbaarheid is de kern van wetenschap. Daarom beschrijf je je "
        "werkwijze zo dat ze precies te volgen is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een waarneming en een besluit?",
        opties=[
            "een waarneming is wat je ziet, een besluit wat je eruit afleidt",
            "een waarneming is wat je afleidt, een besluit juist wat je ziet",
            "een waarneming is altijd een getal",
            "een besluit komt altijd voor de meting",
        ],
        antwoord=0,
        uitleg="De plant is tien centimeter is een waarneming. De meststof werkt is een "
        "besluit, en dat mag pas als de gegevens het dragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeksvraag moet zo gesteld zijn dat een meting ze kan beantwoorden.",
        antwoord=True,
        uitleg="Anders valt er niets te toetsen. Is er geen meting denkbaar, dan is het "
        "geen onderzoeksvraag maar een mening.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zet je op de horizontale as van een grafiek?",
        opties=[
            "de variabele die je zelf instelt",
            "de variabele die je meet",
            "altijd de tijd, wat je ook onderzoekt",
            "het gemiddelde van je metingen",
        ],
        antwoord=0,
        uitleg="De onafhankelijke variabele staat horizontaal, de afhankelijke verticaal. "
        "Zo lees je af hoe het ene uit het andere volgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij elke as van een grafiek? Kruis alles aan wat juist is.",
        opties=[
            "de naam van de grootheid",
            "de eenheid waarin gemeten is",
            "de hypothese van het onderzoek",
            "het aantal herhalingen van de proef",
        ],
        antwoord=[0, 1],
        uitleg="Zonder grootheid en eenheid is een as onleesbaar. Wat je ermee besluit, "
        "hoort in de tekst en niet op de as.",
    ),
    dict(
        type="waarofniet",
        vraag="Een as van een grafiek mag je bij een willekeurige waarde laten beginnen.",
        antwoord=True,
        uitleg="Dat mag, zolang je het duidelijk aangeeft. Doe je het stilzwijgend, dan "
        "lijken kleine verschillen veel groter dan ze zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Welk soort grafiek past het best bij een groei die je in de tijd volgt?",
        antwoord=["lijngrafiek", "een lijngrafiek", "lijndiagram"],
        uitleg="Een lijn toont een verloop tussen opeenvolgende waarden. Staven passen bij "
        "losse groepen, een cirkel bij delen van één geheel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het getal dat je krijgt door alle metingen op te tellen en te delen door hun aantal?",
        antwoord=["gemiddelde", "het gemiddelde", "rekenkundig gemiddelde"],
        uitleg="Een gemiddelde vlakt het toeval van losse metingen uit. Het zegt niets over "
        "hoe sterk de metingen onderling verschilden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee reeksen hebben hetzelfde gemiddelde, maar in de ene liggen de metingen veel verder uit elkaar. Wat besluit je?",
        opties=[
            "die reeks is minder betrouwbaar",
            "die reeks is nauwkeuriger gemeten",
            "de twee reeksen zijn volledig gelijk",
            "het gemiddelde is daar verkeerd berekend",
        ],
        antwoord=0,
        uitleg="Hoe meer spreiding, hoe minder je op dat gemiddelde kunt bouwen. Daarom "
        "vermeld je naast het gemiddelde ook de spreiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grafiek toont dat er meer ijsjes verkocht worden als er meer mensen verdrinken. Wat besluit je?",
        opties=[
            "er is een verband, maar geen oorzaak en gevolg",
            "ijsjes eten maakt zwemmen gevaarlijker",
            "verdrinkingen doen de ijsverkoop stijgen",
            "de grafiek is zeker verkeerd getekend",
        ],
        antwoord=0,
        uitleg="Beide stijgen door een derde factor: warm weer. Een samenhang bewijst nooit "
        "op zichzelf dat het ene het andere veroorzaakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verband tussen twee grootheden betekent dat de ene de andere veroorzaakt.",
        antwoord=False,
        uitleg="Er kan een gemeenschappelijke oorzaak zijn, of het kan toeval zijn. Om een "
        "oorzaak aan te tonen, moet je de factor zelf kunnen variëren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een besluit? Kruis alles aan wat juist is.",
        opties=[
            "een antwoord op de onderzoeksvraag",
            "de gegevens waarop dat antwoord steunt",
            "alle metingen één voor één herhaald",
            "een belofte over een volgende proef",
        ],
        antwoord=[0, 1],
        uitleg="Een besluit beantwoordt de vraag en verwijst naar de resultaten. De ruwe "
        "cijfers staan al in de tabel en hoeven niet opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom reflecteer je achteraf over je werkwijze?",
        opties=[
            "om te zien wat het resultaat onzeker maakt",
            "om de hypothese alsnog juist te maken",
            "om de metingen te mogen aanpassen",
            "om het verslag langer te maken",
        ],
        antwoord=0,
        uitleg="Welke fouten zaten er in de opstelling, wat zou je anders doen? Die "
        "eerlijkheid maakt het verslag sterker, niet zwakker.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het herhalen van een proef om na te gaan of hetzelfde eruit komt?",
        antwoord=["reproduceren", "reproduceerbaarheid", "herhalen"],
        uitleg="Komt een resultaat bij anderen niet terug, dan wordt het niet aanvaard. "
        "Daarom moet je werkwijze volledig beschreven zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat tijdens de proef misliep, laat je beter weg uit je verslag.",
        antwoord=False,
        uitleg="Juist niet: een gebroken buis of een uitgevallen lamp verklaart een vreemd "
        "resultaat. Wie dat verzwijgt, laat anderen in het ongewisse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee begint het ontwerpen van een oplossing?",
        opties=[
            "met het probleem en de eisen vastleggen",
            "met het bouwen van een eerste model",
            "met het bestellen van materiaal",
            "met het schrijven van het verslag",
        ],
        antwoord=0,
        uitleg="Wat moet de oplossing kunnen, en binnen welke grenzen van plaats, geld en "
        "tijd? Zonder die eisen is er niets om later aan te toetsen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een eerste werkend model dat je bouwt en test?",
        antwoord=["prototype", "een prototype", "proefmodel"],
        uitleg="Een prototype hoeft niet mooi te zijn. Het dient om te zien of het idee "
        "werkt en waar het nog aangepast moet worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je prototype niet aan de eisen voldoet?",
        opties=[
            "aanpassen en opnieuw testen",
            "de eisen schrappen zodat het toch past",
            "het ontwerp zo laten en het verslag schrijven",
            "een heel ander probleem kiezen",
        ],
        antwoord=0,
        uitleg="Ontwerpen verloopt in rondes: bouwen, testen, bijsturen. Pas als de "
        "oplossing de eisen haalt, is ze af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschilt ontwerpen van onderzoeken?",
        opties=[
            "ontwerpen zoekt een oplossing, onderzoeken zoekt een antwoord",
            "ontwerpen zoekt een antwoord, onderzoeken zoekt een oplossing",
            "ontwerpen gebruikt nooit metingen",
            "onderzoeken gebruikt nooit een plan",
        ],
        antwoord=0,
        uitleg="Een onderzoek beantwoordt een vraag over hoe iets werkt. Een ontwerp lost "
        "een probleem op en wordt aan eisen getoetst, niet aan een hypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vier letters van STEM? Kruis alles aan wat juist is.",
        opties=[
            "wetenschappen en techniek",
            "technologie en wiskunde",
            "sport en muziek",
            "taal en economie",
        ],
        antwoord=[0, 1],
        uitleg="Science, technology, engineering en mathematics. Het idee is dat een echt "
        "probleem die vier samen nodig heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school wil het waterverbruik van haar serre verlagen. Wat is een goede eerste stap?",
        opties=[
            "meten hoeveel water er nu precies verbruikt wordt",
            "meteen een nieuw bewateringssysteem kopen",
            "de planten minder water geven en afwachten",
            "een verslag over waterverbruik schrijven",
        ],
        antwoord=0,
        uitleg="Zonder beginwaarde weet je achteraf niet of je iets verbeterd hebt. Meten "
        "komt dus voor ingrijpen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goede oplossing houdt ook rekening met de kosten en met het milieu.",
        antwoord=True,
        uitleg="Een ontwerp dat technisch werkt maar onbetaalbaar of vervuilend is, lost "
        "weinig op. Die randvoorwaarden horen bij de eisen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laat je je besluit door anderen nalezen?",
        opties=[
            "zij zien denkfouten die jij over het hoofd ziet",
            "zij kunnen de metingen voor je aanpassen",
            "zo hoef je zelf niet te reflecteren",
            "zo wordt het verslag korter",
        ],
        antwoord=0,
        uitleg="Wetenschappelijk werk wordt nagelezen voor het aanvaard wordt. Ook in de "
        "klas werkt dat: iemand anders leest je redenering met frisse ogen.",
    ),
]
