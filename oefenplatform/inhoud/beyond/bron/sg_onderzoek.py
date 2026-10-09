# -*- coding: utf-8 -*-
"""De onderzoekscyclus van oriënteren tot rapporteren.

Het laatste thema van het vak. Het blok onderzoekscyclus weegt tien procent
van het examen, en de fiche zegt erbij dat alle leerinhouden van het onderdeel
sociale wetenschappen in dat deel van het examen verwerkt kunnen zijn.

De lijstjes staan letterlijk in de fiche:

    de vier fasen: oriënteren, voorbereiden, uitvoeren, rapporteren
    de zes criteria van een goede onderzoeksvraag: open, enkelvoudig,
        objectief, haalbaar, onderzoekbaar, relevant
    soorten onderzoek: deskresearch en fieldresearch, kwalitatief en
        kwantitatief

De zes criteria van een onderzoeksvraag krijgt het kind volgens de fiche ook
op het examen zelf. Ze moeten dus niet van buiten gekend zijn, maar wel
toegepast kunnen worden op een gegeven onderzoeksvraag. Daarom staan er
hieronder veel vragen waarin je een vraag aan één criterium moet toetsen.

Deel 1 zijn oriënteren en voorbereiden.
Deel 2 zijn uitvoeren en rapporteren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier fasen heeft de onderzoekscyclus volgens de fiche?",
        opties=[
            "oriënteren, voorbereiden, uitvoeren, rapporteren",
            "lezen, schrijven, meten en daarna besluiten",
            "vragen, antwoorden, controleren en besluiten",
            "plannen, meten, rekenen, voorstellen",
        ],
        antwoord=0,
        uitleg="Die vier, in die orde. Pas als de vraag staat, mag je aan de methode beginnen denken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de fase oriënteren?",
        opties=[
            "je kiest een onderzoeksvraag of een hypothese",
            "je verzamelt de gegevens die je nodig hebt",
            "je schrijft het besluit van je onderzoek",
            "je kiest de methode waarmee je gaat werken",
        ],
        antwoord=0,
        uitleg="In de oriëntatiefase bepaal je wat je precies wil weten. De methode volgt pas in de volgende fase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel criteria van een goede onderzoeksvraag noemt de fiche?",
        opties=[
            "zes",
            "vier",
            "vijf",
            "zeven",
        ],
        antwoord=0,
        uitleg="Zes: open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium enkelvoudig bij een onderzoeksvraag?",
        opties=[
            "de vraag gaat over één onderwerp of één probleem",
            "de vraag is met één woord te beantwoorden",
            "de vraag is door één persoon te onderzoeken",
            "de vraag heeft één juist antwoord",
        ],
        antwoord=0,
        uitleg="Enkelvoudig betekent niet twee vragen in één. Vraag je naar twee dingen tegelijk, dan kan je geen van beide goed beantwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium objectief bij een onderzoeksvraag?",
        opties=[
            "de vraag verraadt geen eigen mening of overtuiging",
            "de vraag is met cijfers te beantwoorden",
            "de vraag gaat over een goed meetbaar onderwerp",
            "de vraag is door iedereen te begrijpen",
        ],
        antwoord=0,
        uitleg="Objectief betekent dat het antwoord nog beide kanten uit kan. In de vraag mag al geen conclusie zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium onderzoekbaar bij een onderzoeksvraag?",
        opties=[
            "de vraag is geen opzoekvraag en niet direct oplosbaar",
            "de vraag is met een zoekmachine op te lossen",
            "de vraag is binnen de beschikbare tijd uit te voeren",
            "de vraag draagt bij aan bestaande kennis",
        ],
        antwoord=0,
        uitleg="Een vraag waarop het antwoord al ergens staat, is een opzoekvraag. Onderzoekbaar betekent dat er echt onderzoek voor nodig is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium relevant bij een onderzoeksvraag?",
        opties=[
            "het antwoord draagt bij aan de bestaande kennis",
            "het antwoord is binnen de gegeven tijd te vinden",
            "het antwoord is met één woord te geven",
            "het antwoord verraadt geen eigen mening",
        ],
        antwoord=0,
        uitleg="Relevant betekent dat het de moeite waard is. Een vraag waarvan het antwoord niemand verder helpt, haalt dit criterium niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag haalt het criterium open niet?",
        opties=[
            "wonen er in Genk veel alleenstaanden?",
            "hoe is het aantal alleenstaanden in Genk geëvolueerd?",
            "waarom stijgt het aantal alleenstaanden in Genk?",
            "welke factoren verklaren het aantal alleenstaanden?",
        ],
        antwoord=0,
        uitleg="Op de eerste kan je ja of nee antwoorden. Een open vraag begint met hoe, wat, waarom of welke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag haalt het criterium objectief niet?",
        opties=[
            "waarom is het onrechtvaardige schoolbeleid zo schadelijk?",
            "welke gevolgen heeft het schoolbeleid voor de leerlingen?",
            "hoe beoordelen leerlingen het schoolbeleid van hun school?",
            "welke factoren verklaren de keuze van dat schoolbeleid?",
        ],
        antwoord=0,
        uitleg="De eerste vraag zegt al dat het beleid onrechtvaardig en schadelijk is. Het antwoord zit in de vraag, en dat is niet objectief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag haalt het criterium enkelvoudig niet?",
        opties=[
            "hoe werkt het rookverbod en wat vinden jongeren van alcohol?",
            "hoe beïnvloedt het rookverbod het gedrag van jonge mensen?",
            "welke factoren verklaren het rookgedrag van jongeren?",
            "hoe is het rookgedrag van jongeren geëvolueerd?",
        ],
        antwoord=0,
        uitleg="De eerste stelt twee vragen over twee onderwerpen in één zin. Dat is niet enkelvoudig.",
    ),
    dict(
        type="invultekst",
        vraag="Een vraag waarop je met ja of nee kan antwoorden, haalt het criterium ... niet.",
        antwoord=["open"],
        uitleg="Het criterium open. Een open vraag begint met hoe, wat, waarom of welke.",
    ),
    dict(
        type="waarofniet",
        vraag="De zes criteria van een goede onderzoeksvraag krijgt het kind volgens de fiche ook tijdens het examen.",
        antwoord=True,
        uitleg="Waar. De fiche zegt dat uitdrukkelijk. Je moet ze dus kunnen toepassen, niet opsommen uit het hoofd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese en een onderzoeksvraag zijn hetzelfde.",
        antwoord=False,
        uitleg="Niet waar. Een onderzoeksvraag is een vraag, een hypothese is een verwachting die je nog gaat nagaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de fase voorbereiden?",
        opties=[
            "je kiest je bronnen, je methode en je maakt een plan",
            "je kiest je onderzoeksvraag en ook je hypothese",
            "je verzamelt en analyseert je gegevens",
            "je schrijft je conclusie en kijkt terug",
        ],
        antwoord=0,
        uitleg="In de voorbereiding bepaal je welke gegevens je nodig hebt, waar je ze haalt, met welke methode en in welke stappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is deskresearch?",
        opties=[
            "onderzoek met gegevens die al bestaan",
            "onderzoek met gegevens die je zelf gaat opmeten",
            "onderzoek met open gesprekken met mensen",
            "onderzoek met cijfers in plaats van woorden",
        ],
        antwoord=0,
        uitleg="Desk is bureau. Bij deskresearch werk je met bestaande cijfers, rapporten en literatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is fieldresearch?",
        opties=[
            "onderzoek waarbij je zelf gegevens gaat ophalen",
            "onderzoek waarbij je bestaande rapporten leest",
            "onderzoek met cijfers in plaats van woorden",
            "onderzoek met woorden in plaats van cijfers",
        ],
        antwoord=0,
        uitleg="Field is veld. Bij fieldresearch doe je zelf een enquête, een interview of een observatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen kwalitatief en kwantitatief onderzoek?",
        opties=[
            "het eerste zoekt diepte, het tweede zoekt aantallen",
            "het eerste zoekt aantallen, het tweede zoekt diepte",
            "het eerste gebruikt bronnen, het tweede niet",
            "het eerste is altijd beter dan het tweede",
        ],
        antwoord=0,
        uitleg="Kwalitatief werkt met gesprekken en observaties bij weinig mensen. Kwantitatief werkt met cijfers bij veel mensen.",
    ),
    dict(
        type="invultekst",
        vraag="Onderzoek waarbij je werkt met gegevens die al bestaan, heet ...",
        antwoord=["deskresearch", "desk research"],
        uitleg="Deskresearch. Zelf gegevens ophalen is fieldresearch.",
    ),
    dict(
        type="waarofniet",
        vraag="Fieldresearch kan zowel kwalitatief als kwantitatief zijn.",
        antwoord=True,
        uitleg="Waar. Een enquête bij duizend mensen is kwantitatief fieldresearch, tien diepte-interviews is kwalitatief fieldresearch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeker moet volgens de fiche de betrouwbaarheid van zijn bronnen niet nagaan.",
        antwoord=False,
        uitleg="Niet waar. De fiche zegt uitdrukkelijk dat je bronnen krijgt en hun betrouwbaarheid moet evalueren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de fase uitvoeren?",
        opties=[
            "je verzamelt de gegevens en je analyseert ze",
            "je kiest je onderzoeksvraag en ook je hypothese",
            "je schrijft je conclusie en kijkt terug",
            "je kiest je methode en je bronnen",
        ],
        antwoord=0,
        uitleg="Uitvoeren is twee stappen: eerst de gegevens verzamelen, dan ze analyseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort volgens de fiche bij de fase rapporteren?",
        opties=[
            "het resultaat, het besluit en de terugblik op je verloop",
            "het resultaat en niets meer",
            "de keuze van je onderzoeksmethode en van al je bronnen",
            "het verzamelen van je gegevens",
        ],
        antwoord=0,
        uitleg="De fiche noemt drie dingen: wat het resultaat is, wat je kan besluiten, en een reflectie over het verloop van je onderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een reeks vragen en moet er de bruikbare uit kiezen. In welke fase zit je?",
        opties=[
            "uitvoeren",
            "oriënteren",
            "voorbereiden",
            "rapporteren",
        ],
        antwoord=0,
        uitleg="De fiche zet het selecteren van bruikbare vragen en bruikbare data in de fase uitvoeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een goede conclusie bij een onderzoek?",
        opties=[
            "een antwoord op de onderzoeksvraag, uit de gegevens zelf",
            "een samenvatting van alle gegevens die je verzamelde",
            "een mening over het onderwerp van het onderzoek",
            "een lijst van bronnen die je gebruikt hebt",
        ],
        antwoord=0,
        uitleg="Een conclusie antwoordt op de vraag en blijft binnen wat de gegevens toelaten. Niets meer en niets minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt op het examen verschillende conclusies bij één onderzoek. Wat moet je doen?",
        opties=[
            "de meest volledige kiezen en je keuze verantwoorden",
            "de kortste kiezen, want die is het duidelijkst",
            "ze alle vier overnemen in je antwoord",
            "een eigen conclusie schrijven in de plaats",
        ],
        antwoord=0,
        uitleg="De fiche vraagt de conclusie te kiezen die het meest volledig is of het best bij de verzamelde gegevens past, en die keuze te verantwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoek levert een onverwacht resultaat op. Wat vraagt de fiche dan?",
        opties=[
            "noteren welke elementen het resultaat beïnvloed hebben",
            "het onderzoek van begin tot eind opnieuw uitvoeren",
            "het resultaat uit het verslag weglaten",
            "een andere onderzoeksvraag kiezen",
        ],
        antwoord=0,
        uitleg="Een onverwacht resultaat is geen fout. Je kijkt wat het beïnvloed kan hebben: de steekproef, de vraagstelling, de periode of de methode.",
    ),
    dict(
        type="invultekst",
        vraag="De laatste fase van de onderzoekscyclus heet ...",
        antwoord=["rapporteren", "rapportage"],
        uitleg="Rapporteren. De vier fasen zijn oriënteren, voorbereiden, uitvoeren en rapporteren.",
    ),
    dict(
        type="waarofniet",
        vraag="Reflecteren over het verloop van je eigen onderzoek hoort volgens de fiche bij de fase rapporteren.",
        antwoord=True,
        uitleg="Waar. De fiche noemt die reflectie uitdrukkelijk bij het rapporteren, naast het resultaat en het besluit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een conclusie mag verder gaan dan wat de gegevens aantonen, zolang ze logisch klinkt.",
        antwoord=False,
        uitleg="Niet waar. Een conclusie moet binnen de gegevens blijven. Verder gaan is de klassieke fout in een onderzoeksverslag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een grafiek in plaats van een tabel?",
        opties=[
            "om een verloop of een verschil snel te laten zien",
            "om elke afzonderlijke waarde precies te kunnen aflezen",
            "om de bronnen van je gegevens te vermelden",
            "om de onderzoeksvraag te formuleren",
        ],
        antwoord=0,
        uitleg="Een grafiek toont de vorm: stijgt het, daalt het, wie ligt hoger. Een tabel is beter als het om de exacte getallen gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort er altijd bij een grafiek die je zelf maakt?",
        opties=[
            "een titel en een naam bij elke as",
            "een titel en de kleur van elke staaf",
            "de naam van de onderzoeker",
            "de volledige dataset eronder",
        ],
        antwoord=0,
        uitleg="Zonder titel en zonder asnamen weet een lezer niet wat hij ziet. De eenheid hoort er ook bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop kijk je als je de betrouwbaarheid van een bron evalueert?",
        opties=[
            "wie de bron maakte en met welk belang",
            "hoeveel mensen de bron al deelden",
            "hoe mooi de bron vormgegeven is",
            "hoe lang de bron precies is",
        ],
        antwoord=0,
        uitleg="Auteur, belang, datum, methode en of de gegevens elders terug te vinden zijn. Dat is wat een bron betrouwbaar maakt of niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten informatiebronnen kan je bij een maatschappelijk vraagstuk gebruiken?",
        opties=[
            "wetenschappelijke literatuur",
            "officiële statistieken",
            "een interview met een betrokkene",
            "een anonieme post op sociale media",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche vraagt drie soorten bronnen te noteren. Een anonieme post kan een aanleiding zijn, maar niet het bewijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten hoeveel jongeren in Limburg dagelijks met de bus naar school gaan. Welke methode past het best?",
        opties=[
            "kwantitatief onderzoek met een enquête",
            "kwalitatief onderzoek met vijf diepte-interviews",
            "een observatie van één bushalte gedurende een dag",
            "een gesprek met twee buschauffeurs",
        ],
        antwoord=0,
        uitleg="Je vraag gaat over een aantal. Dan heb je cijfers bij veel mensen nodig, dus kwantitatief onderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten hoe leerlingen hun eerste week in het middelbaar beleven. Welke methode past het best?",
        opties=[
            "kwalitatief onderzoek met diepte-interviews",
            "kwantitatief onderzoek met een enquête bij duizend leerlingen",
            "deskresearch in de statistieken van de overheid",
            "een vergelijking van twee schoolreglementen",
        ],
        antwoord=0,
        uitleg="Beleving vraagt diepte en eigen woorden. Dat haal je uit gesprekken, niet uit een cijferlijst.",
    ),
    dict(
        type="invultekst",
        vraag="Onderzoek met gesprekken en observaties bij weinig mensen, gericht op diepte, heet ... onderzoek.",
        antwoord=["kwalitatief", "kwalitatieve"],
        uitleg="Kwalitatief onderzoek. Werken met cijfers bij veel mensen is kwantitatief onderzoek.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche zegt dat alle leerinhouden van het onderdeel sociale wetenschappen in het deel over de onderzoekscyclus kunnen voorkomen.",
        antwoord=True,
        uitleg="Waar. Dat staat er met zoveel woorden. Het onderzoek gaat altijd over een van de maatschappelijke vraagstukken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een enquête bij tien mensen volstaat om uitspraken te doen over heel Vlaanderen.",
        antwoord=False,
        uitleg="Niet waar. Tien antwoorden zeggen iets over die tien. Voor uitspraken over een hele bevolking heb je een voldoende grote en goed gekozen steekproef nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort een reflectie over het verloop bij een onderzoek?",
        opties=[
            "omdat je zo ziet waar je resultaat zwak of sterk staat",
            "omdat je zo je conclusie kan weglaten",
            "omdat je zo je onderzoeksvraag kan wijzigen",
            "omdat je dan geen enkele bron meer hoeft te vermelden",
        ],
        antwoord=0,
        uitleg="Wie zelf zegt waar zijn onderzoek wrikt, geeft de lezer de kans het resultaat juist te wegen. Dat is sterker, niet zwakker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een volledig uitgewerkt onderzoek en moet beoordelen wat beter kon. Waar kijk je naar?",
        opties=[
            "de vraag, de methode, de bronnen en het besluit",
            "alleen naar de spelling en naar de opmaak ervan",
            "alleen naar het aantal bronnen",
            "alleen naar de conclusie",
        ],
        antwoord=0,
        uitleg="Alle vier de fasen kunnen wrikken: een vraag die niet enkelvoudig is, een methode die niet past, zwakke bronnen of een te ruim besluit.",
    ),
]
