# -*- coding: utf-8 -*-
"""Mediatisering en de functies van de massamedia.

Het vierde van vijf thema's over sociale wetenschappen. Mediatisering is het
verschijnsel dat steeds meer van het maatschappelijke leven langs de media
loopt, van de politiek tot de vrije tijd.

De lijstjes staan letterlijk in de fiche:

    functies van massamedia voor het individu: informatieve, educatieve,
        ontspannende, persuasieve en commerciële functie, plus de mengvormen
        infotainment en edutainment
    functies voor de samenleving: de politieke functie (informerende functie,
        woordvoerder- of spreekbuisfunctie, onderzoeksfunctie,
        commentaarfunctie, controlerende of waakhondfunctie), de
        cultuuroverdrachtfunctie, de vrijetijdsfunctie en de sociale functie
    het begrip media als vierde macht

Let op het verschil tussen de functies voor het individu en die voor de
samenleving. Dezelfde uitzending kan voor jou ontspanning zijn en voor de
samenleving cultuuroverdracht. Dat onderscheid is hier meermaals gevraagd.

Deel 1 is mediatisering en de functies voor het individu.
Deel 2 zijn de functies voor de samenleving en de vierde macht.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is mediatisering?",
        opties=[
            "steeds meer van het leven loopt langs de media",
            "steeds meer mensen werken bij de media",
            "steeds meer media gaan samen in één bedrijf",
            "steeds meer media verdwijnen uit de samenleving",
        ],
        antwoord=0,
        uitleg="Mediatisering betekent dat de media niet alleen verslag uitbrengen maar mee bepalen hoe politiek, sport en zelfs familieleven verlopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke functies van massamedia voor het individu noemt de fiche?",
        opties=[
            "de informatieve functie",
            "de ontspannende functie",
            "de commerciële functie",
            "de waakhondfunctie",
            "de cultuuroverdrachtfunctie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voor het individu noemt de fiche vijf functies plus de mengvormen. De waakhond en de cultuuroverdracht zijn functies voor de samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de informatieve functie van media voor het individu?",
        opties=[
            "je op de hoogte brengen van wat er gebeurt",
            "je iets bijleren over een onderwerp",
            "je overtuigen van een standpunt",
            "je een product doen kopen",
        ],
        antwoord=0,
        uitleg="Informeren is weten wat er gebeurt. Een nieuwsuitzending vult vooral die functie in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de educatieve functie van media voor het individu?",
        opties=[
            "je iets bijleren of een vaardigheid aanreiken",
            "je op de hoogte houden van het nieuws",
            "je een paar uur bezighouden",
            "je een product doen kopen",
        ],
        antwoord=0,
        uitleg="Educatief is leren: een documentaire over de ruimte, een kookprogramma, een uitlegvideo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de persuasieve functie van media voor het individu?",
        opties=[
            "je van een standpunt proberen te overtuigen",
            "je op de hoogte brengen van het nieuws",
            "je een paar uur bezighouden",
            "je iets bijleren over een onderwerp",
        ],
        antwoord=0,
        uitleg="Persuasief betekent overtuigend. Een opiniestuk of een campagne wil je mening doen kantelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de commerciële functie van media voor het individu?",
        opties=[
            "je aanzetten tot het kopen van iets",
            "je overtuigen van een politiek standpunt",
            "je iets bijleren over een onderwerp",
            "je op de hoogte brengen van het nieuws",
        ],
        antwoord=0,
        uitleg="Commercieel gaat over verkopen. Reclame vult vooral die functie in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is infotainment?",
        opties=[
            "een mengvorm van informatie en ontspanning",
            "een mengvorm van onderwijs en ontspanning",
            "een mengvorm van reclame en informatie",
            "een mengvorm van politiek en reclame",
        ],
        antwoord=0,
        uitleg="Infotainment komt van information en entertainment: nieuws dat ook amuseert, zoals een praatprogramma over de actualiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is edutainment?",
        opties=[
            "een mengvorm van onderwijs en ontspanning",
            "een mengvorm van informatie en ontspanning",
            "een mengvorm van reclame en onderwijs",
            "een mengvorm van politiek en ontspanning",
        ],
        antwoord=0,
        uitleg="Edutainment komt van education en entertainment: een leerzaam programma dat ook leuk is om te zien.",
    ),
    dict(
        type="invultekst",
        vraag="De mengvorm van informatie en ontspanning heet ...",
        antwoord=["infotainment"],
        uitleg="Infotainment. De mengvorm van onderwijs en ontspanning heet edutainment.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén programma kan voor een kijker meerdere functies tegelijk vervullen.",
        antwoord=True,
        uitleg="Waar. Daar komen de mengvormen juist uit: een praatprogramma informeert en vermaakt tegelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De persuasieve en de commerciële functie zijn twee namen voor dezelfde functie.",
        antwoord=False,
        uitleg="Niet waar. Persuasief wil je mening veranderen, commercieel wil je iets doen kopen. Ze staan apart in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling kijkt na school een reeks om tot rust te komen. Welke functie staat hier voorop?",
        opties=[
            "de ontspannende functie",
            "de informatieve functie",
            "de educatieve functie",
            "de commerciële functie",
        ],
        antwoord=0,
        uitleg="Ontspanning is een van de vijf functies voor het individu, en voor veel mediagebruik de belangrijkste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin kijkt een documentaire over de Eerste Wereldoorlog. Welke functie staat hier voorop?",
        opties=[
            "de educatieve functie",
            "de commerciële functie",
            "de persuasieve functie",
            "de ontspannende functie",
        ],
        antwoord=0,
        uitleg="Er wordt kennis aangereikt. Dat is de educatieve functie. Als het ook amuseert, spreek je van edutainment.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een filmpje op sociale media wil je doen stemmen voor een bepaalde partij. Welke functie staat hier voorop?",
        opties=[
            "de persuasieve functie",
            "de informatieve functie",
            "de educatieve functie",
            "de ontspannende functie",
        ],
        antwoord=0,
        uitleg="Het doel is je mening sturen, niet je informeren. Dat is de persuasieve functie.",
    ),
    dict(
        type="invultekst",
        vraag="De functie die je van een standpunt wil overtuigen, heet de ... functie.",
        antwoord=["persuasieve", "persuasief"],
        uitleg="De persuasieve functie, van het Latijnse persuadere, overtuigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Mediatisering betekent volgens de fiche dat media in verschillende maatschappelijke velden meespelen, niet alleen in de politiek.",
        antwoord=True,
        uitleg="Waar. De fiche spreekt uitdrukkelijk over de verschillende maatschappelijke velden: politiek, sport, cultuur, onderwijs, het gezin.",
    ),
    dict(
        type="waarofniet",
        vraag="Infotainment en edutainment staan in de fiche bij de functies voor de samenleving.",
        antwoord=False,
        uitleg="Niet waar. Ze staan bij de functies voor het individu, als mengvormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt de fiche infotainment en edutainment mengvormen?",
        opties=[
            "omdat ze twee functies in één programma combineren",
            "omdat ze door twee zenders samen gemaakt worden",
            "omdat ze voor twee leeftijdsgroepen bedoeld zijn",
            "omdat ze op twee kanalen tegelijk uitgezonden worden",
        ],
        antwoord=0,
        uitleg="Ze mengen informeren met vermaken, of leren met vermaken. Daarom zijn ze geen aparte zesde en zevende functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een risico van infotainment?",
        opties=[
            "de informatie wordt ondergeschikt aan het vermaak",
            "de informatie wordt te moeilijk voor de kijker",
            "het vermaak wordt ondergeschikt aan de reclame",
            "het programma wordt te kort om iets te zeggen",
        ],
        antwoord=0,
        uitleg="Wat goed bekijkt, krijgt meer tijd dan wat belangrijk is. Dat is het klassieke bezwaar tegen infotainment.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schoolreportage over een nieuwe gsm staat vol merknamen en links. Welke twee functies lopen hier door elkaar?",
        opties=[
            "de informatieve functie",
            "de commerciële functie",
            "de educatieve functie",
            "de ontspannende functie",
        ],
        antwoord=[0, 1],
        uitleg="Er wordt geïnformeerd en er wordt verkocht. Dat door elkaar lopen is precies waarom de fiche vraagt functies te herkennen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke functies van massamedia voor de samenleving noemt de fiche?",
        opties=[
            "de politieke functie",
            "de cultuuroverdrachtfunctie",
            "de sociale functie",
            "de persuasieve functie",
            "de commerciële functie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voor de samenleving noemt de fiche vier functies: de politieke, de cultuuroverdracht, de vrijetijd en de sociale functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel onderdelen heeft de politieke functie volgens de fiche?",
        opties=[
            "vijf",
            "drie",
            "vier",
            "zes",
        ],
        antwoord=0,
        uitleg="Vijf: de informerende, de woordvoerder- of spreekbuisfunctie, de onderzoeksfunctie, de commentaarfunctie en de controlerende of waakhondfunctie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de waakhondfunctie van de media?",
        opties=[
            "de macht in het oog houden en misbruik aan het licht brengen",
            "de burger op de hoogte houden van het nieuws van de dag",
            "de mening van groepen in de samenleving laten horen",
            "de gewoonten van een samenleving doorgeven",
        ],
        antwoord=0,
        uitleg="De controlerende of waakhondfunctie. Juist daarom spreken we van de media als vierde macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de spreekbuisfunctie van de media?",
        opties=[
            "groepen in de samenleving aan het woord laten",
            "de macht in het oog houden en controleren",
            "zelf op onderzoek gaan naar feiten",
            "een standpunt in een commentaar geven",
        ],
        antwoord=0,
        uitleg="De woordvoerder- of spreekbuisfunctie: wie anders niet gehoord wordt, krijgt via de media een stem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de onderzoeksfunctie van de media?",
        opties=[
            "zelf feiten opzoeken die nog niet bekend zijn",
            "doorgeven wat anderen al hebben meegedeeld",
            "een eigen mening over het nieuws geven",
            "de kijker een paar uur bezighouden",
        ],
        antwoord=0,
        uitleg="Onderzoeksjournalistiek brengt naar buiten wat iemand liever verborgen hield. Daar begint de waakhondfunctie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de commentaarfunctie van de media?",
        opties=[
            "het nieuws van een standpunt en uitleg voorzien",
            "het nieuws zonder enige uitleg erbij doorgeven",
            "nieuwe feiten zelf opzoeken",
            "groepen aan het woord laten komen",
        ],
        antwoord=0,
        uitleg="Een commentaar of editoriaal geeft een eigen beoordeling. Dat hoort bij de politieke functie, naast het informeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de cultuuroverdrachtfunctie?",
        opties=[
            "gewoonten, taal en waarden van een samenleving doorgeven",
            "de macht van een land in het oog houden",
            "de burger bezighouden in zijn eigen vrije tijd",
            "mensen onderling met elkaar in contact brengen",
        ],
        antwoord=0,
        uitleg="Via media leren mensen de taal, de verhalen en de gewoonten van hun samenleving. Dat sluit aan bij de tertiaire socialisatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de sociale functie van massamedia?",
        opties=[
            "mensen verbinden en gespreksstof geven",
            "mensen een paar uur bezighouden",
            "mensen een standpunt doen innemen",
            "mensen iets doen kopen",
        ],
        antwoord=0,
        uitleg="Over dezelfde uitzending praten verbindt mensen. Media geven een samenleving gemeenschappelijke onderwerpen.",
    ),
    dict(
        type="invultekst",
        vraag="De functie waarmee media de macht controleren, heet de controlerende of ...functie.",
        antwoord=["waakhond", "waakhondfunctie"],
        uitleg="De waakhondfunctie. Ze ligt aan de basis van het begrip media als vierde macht.",
    ),
    dict(
        type="waarofniet",
        vraag="Dezelfde uitzending kan voor het individu ontspanning zijn en voor de samenleving cultuuroverdracht.",
        antwoord=True,
        uitleg="Waar. De twee lijsten kijken van een andere kant naar hetzelfde programma. Daarom staan ze apart in de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="De vrijetijdsfunctie staat in de fiche bij de functies voor het individu.",
        antwoord=False,
        uitleg="Niet waar. De vrijetijdsfunctie staat bij de samenleving. Bij het individu heet de verwante functie de ontspannende functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden de media de vierde macht genoemd?",
        opties=[
            "omdat ze de drie staatsmachten in het oog houden",
            "omdat ze zelf wetten kunnen maken",
            "omdat ze zelf rechters kunnen benoemen",
            "omdat ze de vierde grootste sector van het land zijn",
        ],
        antwoord=0,
        uitleg="Naast de wetgevende, de uitvoerende en de rechterlijke macht houden de media die drie in het oog. Ze hebben zelf geen wettelijke macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant onthult dat een schepen overheidsgeld voor zichzelf gebruikte. Welke functies zie je hier aan het werk?",
        opties=[
            "de onderzoeksfunctie",
            "de controlerende of waakhondfunctie",
            "de cultuuroverdrachtfunctie",
            "de commerciële functie",
        ],
        antwoord=[0, 1],
        uitleg="De krant zocht zelf de feiten op en controleerde daarmee de macht. Onderzoek en waakhond gaan hier samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reportage laat bewoners van een wijk zelf vertellen wat er misloopt. Welke functie is dit vooral?",
        opties=[
            "de spreekbuisfunctie",
            "de commentaarfunctie",
            "de onderzoeksfunctie",
            "de vrijetijdsfunctie",
        ],
        antwoord=0,
        uitleg="De bewoners komen aan het woord. Dat is de woordvoerder- of spreekbuisfunctie.",
    ),
    dict(
        type="invultekst",
        vraag="Naast de wetgevende, de uitvoerende en de rechterlijke macht worden de media de ... macht genoemd.",
        antwoord=["vierde"],
        uitleg="De vierde macht, omdat ze de andere drie in het oog houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is volgens de fiche de rol van media en sociale media in de politieke communicatie?",
        opties=[
            "burgers informeren zich ermee en politici bereiken er kiezers",
            "burgers gebruiken ze, politici niet",
            "politici gebruiken ze, burgers niet",
            "ze spelen in de politiek van vandaag geen rol van betekenis",
        ],
        antwoord=0,
        uitleg="De fiche noemt uitdrukkelijk beide richtingen: het individu informeert zich via media, en politici gebruiken media om kiezers te bereiken.",
    ),
    dict(
        type="waarofniet",
        vraag="De media hebben als vierde macht geen wettelijk vastgelegde bevoegdheid.",
        antwoord=True,
        uitleg="Waar. Hun kracht komt van openbaarheid en van publiek vertrouwen, niet van een wet die hun een bevoegdheid geeft.",
    ),
    dict(
        type="waarofniet",
        vraag="De onderzoeksfunctie en de commentaarfunctie betekenen hetzelfde.",
        antwoord=False,
        uitleg="Niet waar. De onderzoeksfunctie brengt nieuwe feiten boven, de commentaarfunctie geeft er een beoordeling bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een politicus zet dagelijks korte video's op sociale media in plaats van interviews te geven. Welk verschijnsel zie je hier?",
        opties=[
            "mediatisering van de politiek",
            "de cultuuroverdrachtfunctie",
            "de waakhondfunctie",
            "edutainment",
        ],
        antwoord=0,
        uitleg="De politiek past zich aan wat op media werkt. Dat is precies wat mediatisering betekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een risico als politici de media rechtstreeks omzeilen via hun eigen kanalen?",
        opties=[
            "de waakhondfunctie van de pers valt weg",
            "de cultuuroverdracht valt weg",
            "de ontspannende functie van media valt weg",
            "de educatieve functie valt weg",
        ],
        antwoord=0,
        uitleg="Zonder journalist tussen zender en publiek is er niemand die de boodschap nakijkt. Dan verdwijnt de controle.",
    ),
]
