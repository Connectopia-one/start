# -*- coding: utf-8 -*-
"""Communicatieve vaardigheden: kaders en gesprekstechnieken.

Het laatste van dertien thema's over gedragswetenschappen, en het enige dat
niet uitlegt maar laat doen: de fiche vraagt om een gesprek te voeren met een
empathische basishouding en je in het perspectief van de ander te verplaatsen.

De lijstjes staan letterlijk in de fiche:

    een empathische basishouding bestaat uit: actief luisteren,
        inlevingsvermogen, open houding, echtheid, respect, emotionele
        beschikbaarheid
    interpersoonlijke communicatiekaders: verbindend communiceren van
        Marshall B. Rosenberg, de geen-verliesmethode van Thomas Gordon,
        geweldloze communicatie
    verbindend communiceren en een geweldloze boodschap: waarneming, gevoel,
        behoefte, verzoek
    kenmerken van geweldloze communicatie: direct, doeltreffend, emotioneel,
        empathisch, respectvol
    de LSD-methode: luisteren (non-verbaal en verbaal), samenvatten
        (papegaaien, parafraseren, reflecteren), doorvragen (open en gesloten
        vragen)
    een ik-boodschap: het gedrag, het gevolg, het gevoel, een alternatief
    het 4G-model voor feedback: gedrag, gevoel, gevolg, gewenst gedrag

De vier stappen van verbindend communiceren en van een geweldloze boodschap
zijn in de fiche dezelfde vier. Het ik-boodschap en het 4G-model lijken ook
sterk op elkaar: ze noemen hetzelfde viertal, met een andere orde. Daarom
vragen de vragen hieronder uit welke delen ze bestaan, en niet wie de orde het
best kent.

Deel 1 zijn de basisbegrippen en de drie communicatiekaders.
Deel 2 zijn de gesprekstechnieken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen verbale en non-verbale communicatie?",
        opties=[
            "verbaal is met woorden, non-verbaal zonder woorden",
            "verbaal is gesproken, non-verbaal is geschreven",
            "verbaal is bewust, non-verbaal is altijd onbewust",
            "verbaal is in een gesprek, non-verbaal in een brief",
        ],
        antwoord=0,
        uitleg="Verbaal gaat over de woorden zelf. Non-verbaal is alles daarnaast: houding, gezicht, blik, stem en afstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is lichaamstaal zo belangrijk in een gesprek?",
        opties=[
            "omdat ze de woorden kan bevestigen of tegenspreken",
            "omdat ze altijd precies hetzelfde zegt als de woorden",
            "omdat ze bij iedereen in elke cultuur gelijk is",
            "omdat ze nooit opgemerkt wordt door de ander",
        ],
        antwoord=0,
        uitleg="Iemand die ja zegt maar wegkijkt, stuurt twee boodschappen. De ander gelooft dan meestal de lichaamstaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aspecten horen volgens de fiche bij een empathische basishouding?",
        opties=[
            "actief luisteren",
            "echtheid",
            "emotionele beschikbaarheid",
            "doorvragen met gesloten vragen",
            "een ik-boodschap formuleren",
        ],
        antwoord=[0, 1, 2],
        uitleg="De zes aspecten zijn actief luisteren, inlevingsvermogen, open houding, echtheid, respect en emotionele beschikbaarheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent echtheid in een empathische basishouding?",
        opties=[
            "je doet je niet anders voor dan je bent",
            "je zegt alles wat je over de ander denkt",
            "je houdt je gevoelens volledig voor jezelf",
            "je neemt de mening van de ander over",
        ],
        antwoord=0,
        uitleg="Echtheid of congruentie betekent dat wat je laat zien overeenkomt met wat er in je omgaat. Het betekent niet dat je alles zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een persoonlijk referentiekader?",
        opties=[
            "het geheel van wat jouw blik op de wereld bepaalt",
            "het geheel van afspraken in een gesprek",
            "de lijst van vragen die je mag stellen",
            "het verslag dat je na een gesprek maakt",
        ],
        antwoord=0,
        uitleg="Je referentiekader is wat je meebrengt: je opvoeding, je ervaringen, je cultuur en je waarden. Daardoor hoor je een verhaal op jouw manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beïnvloedt een persoonlijk referentiekader een gesprek?",
        opties=[
            "het bepaalt mee wat je opmerkt en hoe je het begrijpt",
            "het maakt elk gesprek onmogelijk",
            "het zorgt dat twee mensen hetzelfde horen",
            "het speelt alleen bij een moeilijk gesprek mee",
        ],
        antwoord=0,
        uitleg="Twee mensen horen hetzelfde verhaal anders, omdat elk het door zijn eigen kader leest. Dat beseffen is de eerste stap naar een gesprek.",
    ),
    dict(
        type="invultekst",
        vraag="Het geheel van ervaringen en waarden waarmee jij naar de wereld kijkt, heet je persoonlijk ...",
        antwoord=["referentiekader", "kader"],
        uitleg="Je persoonlijk referentiekader. Een interpersoonlijk communicatiekader is iets anders: dat is een manier van spreken met iemand.",
    ),
    dict(
        type="waarofniet",
        vraag="Een empathische basishouding betekent dat je het altijd eens moet zijn met de ander.",
        antwoord=False,
        uitleg="Niet waar. Je kan heel goed meevoelen en begrijpen en toch iets anders vinden. Empathie is geen instemming.",
    ),
    dict(
        type="waarofniet",
        vraag="Non-verbaal gedrag kan een gesprek evenveel richting geven als de woorden zelf.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk naar de effecten van non-verbaal gedrag, want een blik of een houding verandert een gesprek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie interpersoonlijke communicatiekaders noemt de fiche?",
        opties=[
            "verbindend communiceren",
            "de geen-verliesmethode",
            "geweldloze communicatie",
            "de LSD-methode",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie. De LSD-methode is geen kader maar een gesprekstechniek om actief te luisteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij verbindend communiceren?",
        opties=[
            "Marshall B. Rosenberg",
            "Thomas Gordon",
            "Carl Rogers",
            "Albert Bandura",
        ],
        antwoord=0,
        uitleg="Rosenberg. Zijn vier stappen zijn waarneming, gevoel, behoefte en verzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke vier stappen bestaat een verbindende boodschap?",
        opties=[
            "waarneming, gevoel, behoefte, verzoek",
            "gedrag, gevoel, gevolg, gewenst gedrag",
            "luisteren, samenvatten, doorvragen, besluiten",
            "waarneming, oordeel, eis, besluit",
        ],
        antwoord=0,
        uitleg="Eerst beschrijven zonder oordeel, dan je gevoel, dan je behoefte, en pas dan een verzoek dat geen eis is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een verzoek en een eis in verbindend communiceren?",
        opties=[
            "bij een verzoek mag de ander nee zeggen",
            "bij een eis mag de ander nee zeggen",
            "een verzoek wordt luider gezegd dan een eis",
            "een verzoek bevat geen gevoel, een eis wel",
        ],
        antwoord=0,
        uitleg="Een verzoek laat de ander vrij. Zodra er een straf of een verwijt aan hangt, is het een eis geworden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke boodschap is volgens Rosenberg een waarneming zonder oordeel?",
        opties=[
            "je hebt deze week drie keer de vaat laten staan",
            "je bent echt de luiste persoon van dit huis",
            "je doet nooit iets in huis, dat weet je zelf ook",
            "je hebt blijkbaar geen enkel respect voor mij",
        ],
        antwoord=0,
        uitleg="Een waarneming is wat een camera zou zien: drie keer de vaat laten staan. De andere drie zijn oordelen over de persoon.",
    ),
    dict(
        type="invultekst",
        vraag="De vier stappen van verbindend communiceren zijn waarneming, gevoel, verzoek en ...",
        antwoord=["behoefte"],
        uitleg="De behoefte. De orde is waarneming, gevoel, behoefte, verzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de geen-verliesmethode?",
        opties=[
            "Thomas Gordon",
            "Marshall B. Rosenberg",
            "Carl Rogers",
            "Jacobus E. Rink",
        ],
        antwoord=0,
        uitleg="Gordon. Zijn methode zoekt een oplossing waarin geen van de twee partijen verliest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet de methode van Gordon de geen-verliesmethode?",
        opties=[
            "omdat je samen zoekt tot niemand moet toegeven",
            "omdat de sterkste partij altijd gelijk krijgt",
            "omdat je het conflict gewoon laat liggen",
            "omdat elke partij de helft moet opgeven",
        ],
        antwoord=0,
        uitleg="Niet jij wint of ik win, maar samen zoeken naar een oplossing waarin de behoeften van beiden aan bod komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen volgens de fiche bij de geen-verliesmethode?",
        opties=[
            "je behoeften zeggen met een ik-boodschap",
            "met actief luisteren de behoeften van de ander zoeken",
            "samen oplossingen bedenken en afwegen",
            "de ander laten beslissen en je erbij neerleggen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Daarna volgen nog: een keuze maken, de oplossing uitproberen en nagaan of het conflict echt opgelost is.",
    ),
    dict(
        type="waarofniet",
        vraag="De geen-verliesmethode eindigt met nagaan of het conflict echt opgelost is.",
        antwoord=True,
        uitleg="Waar. De laatste stap is de evaluatie. Zonder die stap weet je niet of de gekozen oplossing werkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Geweldloze communicatie betekent dat je je gevoelens niet mag laten zien.",
        antwoord=False,
        uitleg="Niet waar. De fiche noemt emotioneel juist een kenmerk van geweldloze communicatie. Je gevoel benoemen is een van de vier stappen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is actief luisteren?",
        opties=[
            "laten merken dat je hoort en begrijpt wat de ander zegt",
            "wachten tot de ander stopt om zelf te kunnen antwoorden",
            "zwijgen tot de ander helemaal uitgepraat is",
            "noteren wat de ander zegt om het later te gebruiken",
        ],
        antwoord=0,
        uitleg="Bij actief luisteren doe je iets: je houding, je blik, je samenvatting en je vragen laten zien dat je volgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen oppervlakkig, inhoudelijk en actief luisteren?",
        opties=[
            "het verschil zit in hoeveel je met het verhaal doet",
            "het verschil zit in hoe lang het gesprek duurt",
            "het verschil zit in wie het gesprek begint",
            "het verschil zit in waar het gesprek doorgaat",
        ],
        antwoord=0,
        uitleg="Oppervlakkig is horen, inhoudelijk is de woorden volgen, actief is ook het gevoel erachter teruggeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de drie letters van de LSD-methode?",
        opties=[
            "luisteren, samenvatten en doorvragen",
            "luisteren, spreken en discussiëren",
            "lezen, schrijven en doen",
            "luisteren, steunen en doorverwijzen",
        ],
        antwoord=0,
        uitleg="Luisteren, samenvatten, doorvragen. Dat is de methode van de fiche om actief te luisteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zaken horen volgens de fiche bij non-verbaal actief luisteren?",
        opties=[
            "een actieve lichaamshouding",
            "oogcontact",
            "je gelaatsuitdrukking",
            "kleine aanmoedigingen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie zijn non-verbaal. Kleine aanmoedigingen en stiltes staan bij het verbaal actief luisteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie manieren van samenvatten noemt de fiche?",
        opties=[
            "papegaaien, parafraseren en reflecteren",
            "herhalen, oordelen en besluiten",
            "doorvragen, uitleggen en samenvatten",
            "luisteren, stilvallen en aanmoedigen",
        ],
        antwoord=0,
        uitleg="Papegaaien is letterlijk herhalen, parafraseren is in je eigen woorden zeggen, reflecteren is het gevoel erachter benoemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: ik weet niet of ik dit nog volhoud. Jij zegt: je klinkt echt moe. Welke manier van samenvatten is dit?",
        opties=[
            "reflecteren",
            "papegaaien",
            "parafraseren",
            "doorvragen",
        ],
        antwoord=0,
        uitleg="Je benoemt het gevoel achter de woorden. Dat is reflecteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: ik weet niet of ik dit nog volhoud. Jij zegt: je weet niet of je het nog volhoudt. Welke manier van samenvatten is dit?",
        opties=[
            "papegaaien",
            "parafraseren",
            "reflecteren",
            "aanmoedigen",
        ],
        antwoord=0,
        uitleg="Je herhaalt de woorden bijna letterlijk. Dat is papegaaien. Spaarzaam gebruiken, anders klinkt het als spotten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een open en een gesloten vraag?",
        opties=[
            "op een open vraag kan je niet met ja of nee antwoorden",
            "op een gesloten vraag kan je niet met ja of nee antwoorden",
            "een open vraag is langer dan een gesloten vraag",
            "een open vraag stel je enkel aan het begin",
        ],
        antwoord=0,
        uitleg="Een open vraag begint met hoe, wat of waarom en laat ruimte. Een gesloten vraag is met ja of nee af te doen.",
    ),
    dict(
        type="invultekst",
        vraag="In de LSD-methode staat de S voor ...",
        antwoord=["samenvatten"],
        uitleg="Samenvatten. De L staat voor luisteren en de D voor doorvragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stilte laten vallen hoort volgens de fiche bij verbaal actief luisteren.",
        antwoord=True,
        uitleg="Waar. De fiche zet kleine aanmoedigingen en stiltes bij het verbaal actief luisteren. Een stilte geeft de ander ruimte.",
    ),
    dict(
        type="waarofniet",
        vraag="Veel gesloten vragen stellen is de beste manier om een moeilijk gesprek te openen.",
        antwoord=False,
        uitleg="Niet waar. Gesloten vragen laten weinig ruimte. Een gesprek open je met open vragen en sluit je af met gesloten vragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke delen bestaat een ik-boodschap volgens de fiche?",
        opties=[
            "het gedrag dat je ziet",
            "het gevolg van dat gedrag",
            "het gevoel dat het bij je oproept",
            "het oordeel dat je over de ander hebt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie, en dan nog een alternatief voor het gewenste gedrag. Een oordeel over de persoon hoort er juist niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke boodschap is een ik-boodschap?",
        opties=[
            "als de vaat blijft staan, moet ik alles alleen doen, en dat maakt me moe",
            "jij laat de vaat altijd staan, dat is typisch voor jou",
            "iedereen hier vindt dat jij te weinig doet in huis",
            "je zou beter eens leren hoe een huishouden werkt",
        ],
        antwoord=0,
        uitleg="Een ik-boodschap vertelt over het gedrag, het gevolg en jouw gevoel. De andere drie zijn jij-boodschappen met een verwijt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt een ik-boodschap vaak beter dan een jij-boodschap?",
        opties=[
            "omdat de ander zich minder aangevallen voelt",
            "omdat de ander dan verplicht moet antwoorden",
            "omdat de ander het gedrag niet meer kan ontkennen",
            "omdat de ander er geen gevoel bij hoort",
        ],
        antwoord=0,
        uitleg="Een jij-boodschap begint met een verwijt, en dan gaat de ander zich verdedigen. Een ik-boodschap houdt het gesprek open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vier G's van het 4G-model?",
        opties=[
            "gedrag, gevoel, gevolg en gewenst gedrag",
            "gedrag, geduld, gevolg en gesprek",
            "gevoel, geduld, gevolg en grens",
            "gedrag, gevoel, grens en gesprek",
        ],
        antwoord=0,
        uitleg="Het gedrag dat je ziet, het gevoel dat het geeft, het gevolg ervan, en wat je liever zou zien.",
    ),
    dict(
        type="invultekst",
        vraag="Het model om feedback in vier stappen te geven, heet in de fiche het ...-model.",
        antwoord=["4G", "4g", "vier G"],
        uitleg="Het 4G-model: gedrag, gevoel, gevolg, gewenst gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een goede manier om feedback te ontvangen?",
        opties=[
            "eerst laten uitspreken en doorvragen wat precies bedoeld wordt",
            "onmiddellijk uitleggen waarom het niet jouw fout was",
            "zwijgen en er daarna niet meer op terugkomen",
            "de feedback doorgeven aan iemand anders",
        ],
        antwoord=0,
        uitleg="Feedback ontvangen begint met luisteren en begrijpen. Je hoeft er niet onmiddellijk op te antwoorden of mee in te stemmen.",
    ),
    dict(
        type="waarofniet",
        vraag="Feedback kan volgens de fiche zowel verbaal als non-verbaal en zowel positief als negatief zijn.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk dat onderscheid te maken. Een zucht is ook feedback.",
    ),
    dict(
        type="waarofniet",
        vraag="Goede feedback zegt wat er mis is met de persoon, niet met zijn gedrag.",
        antwoord=False,
        uitleg="Niet waar, net omgekeerd. Het 4G-model begint bij het gedrag dat je ziet, juist om de persoon buiten de kritiek te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je begeleidt een gesprek met iemand die boos binnenkomt. Welke techniek zet je als eerste in?",
        opties=[
            "actief luisteren, zodat de ander zich gehoord voelt",
            "een ik-boodschap, zodat je grens duidelijk is",
            "feedback met het 4G-model over zijn toon",
            "doorvragen met gesloten vragen naar de feiten",
        ],
        antwoord=0,
        uitleg="Zolang iemand boos is, komt niets anders binnen. Eerst laten uitspreken en samenvatten, daarna de rest.",
    ),
]
