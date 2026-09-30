# -*- coding: utf-8 -*-
"""De vragen voor "Beeldvorming en het verleden vandaag".

Uit de vakfiche: historische beeldvorming en de invloed van
standplaatsgebondenheid, en de relatie verleden - heden - toekomst. Hoe een
beeld van het verleden een constructie is, hoe een maatschappelijke en
persoonlijke context dat beeld kleurt, welke betekenissen personen en groepen
aan hetzelfde fenomeen geven, en hoe zulke fenomenen meespelen in lagen van
identiteit: Vlaams, Belgisch, westers en niet-westers, sociaaleconomisch en
levensbeschouwelijk. Daarbij hoort ook het analyseren van kunst- en
cultuuruitingen met het stappenplan.

Deel 1 gaat over beeldvorming en standplaatsgebondenheid. Deel 2 over het
verleden vandaag, en over kunst als venster op mens en wereld.

De fiche noemt zelf twee voorbeelden: de inname van Jeruzalem in 1099 vanuit
Arabisch en westers oogpunt, en de betekenis die Vlaamsgezinden aan de
Guldensporenslag geven.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is historische beeldvorming?",
        opties=[
            "het beeld van het verleden dat iemand opbouwt uit bronnen",
            "het verleden zoals het werkelijk en onveranderlijk geweest is",
            "het tekenen en schilderen van historische figuren en taferelen",
            "het bewaren en tentoonstellen van bronnen in een museum",
        ],
        antwoord=0,
        uitleg="Het verleden zelf ligt achter ons en komt niet terug. Wat we hebben, is een beeld dat iemand ervan gemaakt heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een historisch beeld is altijd een constructie van iemand, vanuit een bepaald perspectief.",
        antwoord=True,
        uitleg="Die persoon kiest bronnen, leidt informatie af, interpreteert en zoekt samenhang. Elk van die stappen is een keuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan het beeld van een gebeurtenis in de loop van de tijd veranderen?",
        opties=[
            "er komen nieuwe bronnen bij, en nieuwe vragen aan die bronnen",
            "het verleden zelf verandert mee met de tijd waarin men leeft",
            "de kalender verandert, zodat de jaartallen niet meer kloppen",
            "de bronnen over die gebeurtenis verdwijnen na een tijd allemaal",
        ],
        antwoord=0,
        uitleg="Elke generatie stelt haar eigen vragen. Zo kan één en dezelfde bron opeens iets vertellen waar niemand eerder naar keek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke keuzes maakt een historicus die een beeld construeert?",
        opties=[
            "welke bronnen hij gebruikt",
            "welke informatie hij eruit afleidt",
            "welk verband hij tussen de gegevens legt",
            "wat er destijds gebeurd is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wat er gebeurd is, ligt vast; alleen is het niet volledig kenbaar. De drie andere zijn wel keuzes van de historicus zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Als twee historici tot een verschillend beeld komen, heeft er zeker één slecht gewerkt.",
        antwoord=False,
        uitleg="Ze kunnen andere bronnen gebruiken of andere vragen stellen. Pas als een beeld de bronnen tegenspreekt, is er een echt probleem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan de persoonlijke context van een maker met zijn beeld van het verleden doen?",
        opties=[
            "zijn afkomst, geloof en beroep kleuren wat hij belangrijk vindt",
            "die heeft op zijn beeld van het verleden geen enkele invloed",
            "die bepaalt enkel zijn taalgebruik en niet wat hij vertelt",
            "die bepaalt enkel zijn handschrift en niet wat hij opschrijft",
        ],
        antwoord=0,
        uitleg="Een geestelijke die over de Beeldenstorm schrijft, ziet iets anders dan een wever uit dezelfde stad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk beeld van de Franken geven de Arabische bronnen over de inname van Jeruzalem in 1099?",
        opties=[
            "dat van ruwe, gewelddadige indringers van ver weg",
            "dat van beschaafde bevrijders die orde kwamen brengen",
            "dat van vreedzame handelaars die enkel goederen kwamen ruilen",
            "dat van gewone pelgrims die de heilige plaatsen wilden bezoeken",
        ],
        antwoord=0,
        uitleg="Westerse kronieken vertellen hetzelfde bloedbad als een door God gewild succes. Twee beelden, één gebeurtenis, twee standplaatsen.",
    ),
    dict(
        type="waarofniet",
        vraag="Arabische en westerse bronnen over 1099 verschillen vooral omdat hun makers aan een andere kant stonden.",
        antwoord=True,
        uitleg="Wat voor de ene een heilige overwinning was, was voor de andere een ramp. Dat is standplaatsgebondenheid, niet leugen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gevolg als je maar één kant van een conflict leest?",
        opties=[
            "je neemt de blik van die kant over zonder het te merken",
            "je krijgt vanzelf het juiste en volledige beeld van het conflict",
            "je leert niets van wat er in dat conflict gebeurd is",
            "je begrijpt juist de andere kant van het conflict beter",
        ],
        antwoord=0,
        uitleg="Daarom vraagt de fiche uitdrukkelijk om bronnen van beide kanten naast elkaar te leggen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de invloed van iemands eigen plaats, tijd en belangen op wat hij vertelt?",
        antwoord="standplaatsgebondenheid",
        uitleg="Ze geldt voor een middeleeuwse kroniekschrijver, maar evengoed voor een historicus van vandaag en voor jou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan de maatschappelijke context met een beeld van het verleden doen?",
        opties=[
            "een land in oorlog vertelt zijn verleden anders dan een land in vrede",
            "een schoolboek van vandaag legt andere accenten dan dat van honderd jaar geleden",
            "wie het geld voor het onderzoek geeft, bepaalt mee welke vragen gesteld worden",
            "de maatschappelijke context speelt bij beeldvorming geen enkele rol van betekenis",
        ],
        antwoord=[0, 1, 2],
        uitleg="Beeldvorming gebeurt niet in het luchtledige. De drie andere voorbeelden tonen hoe de tijd van de verteller meekomt.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook een geschiedenisboek van vandaag is standplaatsgebonden.",
        antwoord=True,
        uitleg="Het is geschreven in een bepaald land, in een bepaalde tijd, voor een bepaald publiek. Dat maakt het niet onbetrouwbaar, wel leesbaar als bron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan het beeld van Karel de Grote zo verschillen?",
        opties=[
            "de vraag bepaalt het antwoord: vader van Europa, veroveraar of Duits keizer",
            "er is over Karel de Grote geen enkele geschreven bron bewaard gebleven",
            "Karel de Grote heeft als persoon in werkelijkheid nooit bestaan",
            "alle bronnen over hem zeggen precies hetzelfde en spreken elkaar nooit tegen",
        ],
        antwoord=0,
        uitleg="Frankrijk en Duitsland claimden hem allebei, en na 1945 werd hij het symbool van Europese eenheid. Elke tijd maakte hem opnieuw.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bron die zeldzaam of pas ontdekt is, kan het bestaande beeld in beweging brengen.",
        antwoord=True,
        uitleg="Eén scheepswrak of één archiefvondst kan jarenlange zekerheden op losse schroeven zetten. Daarom is geschiedenis nooit af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je beeldvorming met voorzichtigheid bekijken?",
        opties=[
            "omdat een beeld altijd door iemand gemaakt is, met keuzes en blinde vlekken",
            "omdat alle historici liegen over wat er in het verleden gebeurd is",
            "omdat het verleden in werkelijkheid helemaal niet bestaan heeft",
            "omdat bronnen uit het verleden nooit lang genoeg bewaard blijven",
        ],
        antwoord=0,
        uitleg="Voorzichtig zijn is niet hetzelfde als niets geloven. Je vraagt je af wie het beeld maakte, met welke bronnen en met welk doel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je bij een historisch beeld dat je voorgeschoteld krijgt?",
        opties=[
            "wie maakte dit, en wanneer?",
            "welke bronnen liggen eraan ten grondslag?",
            "wat wordt er niet verteld?",
            "hoeveel bladzijden telt het?",
        ],
        antwoord=[0, 1, 2],
        uitleg="De omvang zegt niets. De drie andere vragen brengen je bij de keuzes achter het beeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stereotype in een oude bron kan je gewoon overnemen, want het hoorde nu eenmaal bij die tijd.",
        antwoord=False,
        uitleg="Je benoemt het als stereotype en analyseert het. Dat het gewoon was, verklaart het; het maakt het niet waar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de redeneerwijze 'veralgemening analyseren' bij beeldvorming?",
        opties=[
            "nagaan of een uitspraak over een hele groep op meer dan enkele gevallen steunt",
            "een lange tekst korter maken zonder de inhoud ervan te veranderen",
            "alle beschikbare bronnen samenvoegen tot één doorlopend verhaal",
            "uit wat je gelezen hebt een besluit over iedereen samen trekken",
        ],
        antwoord=0,
        uitleg="'De middeleeuwer geloofde dat de aarde plat was' is zo'n uitspraak. Ze klopt niet, en ze wordt toch voortdurend herhaald.",
    ),
    dict(
        type="waarofniet",
        vraag="Enkel teksten doen aan beeldvorming; een schilderij of een standbeeld niet.",
        antwoord=False,
        uitleg="Ook een beeld kiest en ordent. Wie wordt afgebeeld, hoe groot en in welke houding? Een standbeeld van een held vertelt vooral iets over wie het liet zetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig te weten wie de opdracht voor een bron gaf?",
        opties=[
            "de opdrachtgever bepaalt vaak mee wat er verteld en verzwegen wordt",
            "de opdrachtgever betaalde de verf, en dus ook de kleuren die gebruikt zijn",
            "dat bepaalt het formaat waarop het werk uiteindelijk gemaakt is",
            "dat heeft op de inhoud van de bron geen enkele invloed gehad",
        ],
        antwoord=0,
        uitleg="Een kroniek in opdracht van een vorst zal zijn nederlagen zelden breed uitsmeren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke betekenis geven Vlaamsgezinden aan de Guldensporenslag?",
        opties=[
            "die van een Vlaamse overwinning op een vreemde overheerser",
            "die van een gewone veldslag zonder verdere betekenis erna",
            "die van een Franse overwinning op de opstandige Vlaamse steden",
            "die van een godsdienstoorlog tussen twee christelijke partijen",
        ],
        antwoord=0,
        uitleg="In de 19de eeuw, toen men een Vlaamse identiteit zocht, kreeg 1302 die rol. Dat is een betekenis van later, niet van toen.",
    ),
    dict(
        type="waarofniet",
        vraag="De betekenis die men aan de Guldensporenslag geeft, is sinds 1302 altijd dezelfde gebleven.",
        antwoord=False,
        uitleg="Voor de tijdgenoten was het een sociale en politieke strijd. De taalkundige en nationale betekenis komt er pas vijfhonderd jaar later bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een herdenking iets over het heden vertelt?",
        opties=[
            "wát men herdenkt en hóé, hangt af van wat men nu belangrijk vindt",
            "een herdenking verandert achteraf wat er in het verleden gebeurd is",
            "een herdenking is altijd een leugen over wat er echt gebeurd is",
            "een herdenking is een bron uit de tijd van de gebeurtenis zelf",
        ],
        antwoord=0,
        uitleg="Hetzelfde jaartal kan de ene eeuw als strijd en de volgende als feest gevierd worden. De gebeurtenis bleef intussen dezelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen van identiteit noemt de vakfiche?",
        opties=[
            "de Vlaamse en de Belgische laag",
            "de westerse en niet-westerse laag",
            "de sociaaleconomische positie en de levensbeschouwing",
            "de laag van je lievelingssport",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een sport hoort daar niet bij. De drie andere antwoorden geven samen de vijf lagen uit de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mens heeft maar één identiteit tegelijk.",
        antwoord=False,
        uitleg="Je kan tegelijk Vlaming, Belg, Europeaan, gelovig of niet en lid van een gezin zijn. Die lagen sluiten elkaar niet uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan een historisch fenomeen mee vorm geven aan een groepsidentiteit?",
        opties=[
            "door een gedeelde herinnering te worden waarin een groep zich herkent",
            "door de bevolking van die groep in enkele jaren te doen groeien",
            "door het klimaat van het gebied waar die groep woont te veranderen",
            "door de taal die die groep spreekt stilaan te doen verdwijnen",
        ],
        antwoord=0,
        uitleg="Een feestdag, een standbeeld, een lied op school: zo wordt een verhaal van iedereen, ook van wie het pas eeuwen later hoort.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke datum valt de feestdag van de Vlaamse Gemeenschap?",
        antwoord="11 juli",
        uitleg="Naar de Guldensporenslag van 1302. Dat de keuze pas in de 20ste eeuw gemaakt werd, hoort bij het verhaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Verschillende personen kunnen aan hetzelfde historische fenomeen een verschillende betekenis geven.",
        antwoord=True,
        uitleg="Voor de ene is 1302 een feest, voor de andere een gewone werkdag, voor een derde een pijnlijk verhaal. Alle drie kijken ze naar hetzelfde jaartal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je het verleden niet met de maatstaf van vandaag beoordelen?",
        opties=[
            "je begrijpt dan niet waarom iets toen vanzelfsprekend leek",
            "het verleden was in alle opzichten beter dan onze eigen tijd",
            "het verleden was in alle opzichten slechter dan onze eigen tijd",
            "er zijn over het verleden geen bruikbare bronnen bewaard gebleven",
        ],
        antwoord=0,
        uitleg="Begrijpen is niet hetzelfde als goedkeuren. Je kan slavernij verwerpen en tegelijk onderzoeken waarom tijdgenoten ze gewoon vonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verzamel je in stap 1 van het stappenplan voor een kunst- of cultuuruiting?",
        opties=[
            "de tijd en de ruimte waarin ze gemaakt is",
            "de maker en de maatschappelijke context",
            "de titel en de soort uiting",
            "de huidige verkoopprijs",
        ],
        antwoord=[0, 1, 2],
        uitleg="De prijs van vandaag hoort er niet bij. De drie andere punten zijn de context waarin je alles wat volgt leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat noemt de vakfiche géén kunst- of cultuuruiting?",
        opties=[
            "een rekening of een wetstekst",
            "een schilderij of een bouwwerk",
            "een film of een game",
            "graffiti of een lied",
        ],
        antwoord=0,
        uitleg="Een rekening is een bron, maar geen cultuuruiting in deze zin. De drie andere horen wel in de lijst van de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook een game of graffiti kan je als cultuuruiting analyseren.",
        antwoord=True,
        uitleg="De fiche noemt ze uitdrukkelijk. Dezelfde vragen gelden: wie maakte het, voor wie, en waarom?",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschrijf je in stap 2 van dat stappenplan?",
        opties=[
            "wat je letterlijk ziet of hoort: materialen, figuren, kleuren en klank",
            "wat het werk betekent en welke boodschap de maker erin gelegd heeft",
            "wie het werk gekocht heeft en hoeveel er destijds voor betaald werd",
            "waar het werk vandaag hangt en in welk museum je het kan gaan bekijken",
        ],
        antwoord=0,
        uitleg="Eerst kijken, dan pas duiden. Wie meteen begint te interpreteren, ziet alleen nog wat hij verwachtte te zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bepaal je in stap 3, bij het interpreteren?",
        opties=[
            "het onderwerp: waarover het gaat",
            "het doelpubliek: voor wie het gemaakt is",
            "de bedoeling: waarom het gemaakt is",
            "het gewicht en de afmetingen van het werk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het gewicht zegt niets. De drie andere brengen je bij de betekenis die vorm en inhoud samen dragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kunstwerk kan bedoeld zijn om te bekritiseren, te bevestigen, te informeren of gewoon om schoonheid te maken.",
        antwoord=True,
        uitleg="De fiche somt die bedoelingen op. Vaak zijn er trouwens meerdere tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ondersteunt de vorm van een barokschilderij zijn bedoeling?",
        opties=[
            "beweging, licht en grote gebaren moeten de kijker meeslepen en overtuigen",
            "de rustige verhoudingen en het evenwicht moeten de kijker net kalmeren",
            "de kleine afmetingen en de sobere lijst moeten bescheidenheid tonen",
            "het volledige gebrek aan kleur moet de soberheid van het geloof tonen",
        ],
        antwoord=0,
        uitleg="De Contrareformatie wilde het geloof niet uitleggen maar laten voelen. De vorm doet daar precies aan mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Kunst uit het verleden zegt alleen iets over kunst, niet over de samenleving.",
        antwoord=False,
        uitleg="Ze toont wat men mooi vond, wie kon betalen, wat men wilde uitstralen en wat men liever niet liet zien. Dat is geschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kijk je bij een cultuuruiting ook naar de maatschappelijke context?",
        opties=[
            "die verklaart mee waarom juist dit onderwerp en deze bedoeling gekozen werden",
            "die bepaalt het formaat waarop het werk gemaakt moest worden",
            "die bepaalt de bewaarplaats waar het werk vandaag te zien is",
            "die heeft op het onderwerp en de bedoeling geen enkele invloed",
        ],
        antwoord=0,
        uitleg="Een Mariabeeld uit 1650 in Antwerpen staat er niet toevallig: het is een antwoord op de Beeldenstorm van bijna een eeuw eerder.",
    ),
    dict(
        type="waarofniet",
        vraag="Nadenken over beeldvorming helpt je ook bij nieuws en sociale media van vandaag.",
        antwoord=True,
        uitleg="Wie maakte dit, met welke bronnen, voor wie en waarom? Dat zijn precies dezelfde vragen, alleen is de bron van gisteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van wat je uit dit vak meeneemt?",
        opties=[
            "dat een beeld van het verleden gemaakt is, en dat je mag vragen door wie",
            "dat het verleden op geen enkele manier gekend kan worden",
            "dat alle bronnen uit het verleden liegen over wat er gebeurd is",
            "dat enkel de jaartallen tellen en al de rest bijzaak is",
        ],
        antwoord=0,
        uitleg="Niet alles is even waar, en niet niets is kenbaar. Maar wat je te horen krijgt, komt altijd ergens vandaan.",
    ),
]
