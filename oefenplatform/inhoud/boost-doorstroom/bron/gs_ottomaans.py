# -*- coding: utf-8 -*-
"""De vragen voor "Het Ottomaanse Rijk en samenlevingen vergelijken".

Uit de vakfiche: de vroegmoderne niet-westerse samenleving. De politieke,
sociale, culturele en economische kenmerken van het Ottomaanse Rijk, zijn bloei
en verval in tijd en ruimte, zijn houding tegenover minderheden, en de aard van
de contacten met Europa (de handel in het Middellandse Zeegebied en de strijd
tussen Suleyman I en Karel V). Daarnaast het vergelijken van samenlevingen: de
politieke, sociale, culturele en economische kenmerken die als
vergelijkingspunten dienen, binnen eenzelfde periode en over periodes heen.

Deel 1 gaat over het Ottomaanse Rijk. Deel 2 over het vergelijken zelf.

De fiche vraagt uitdrukkelijk twee vergelijkingen: het absolutisme van de sultan
naast dat van Lodewijk XIV, en de middeleeuwse gelaagde samenleving naast de
Egyptische.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar lag het zwaartepunt van het Ottomaanse Rijk?",
        opties=[
            "rond de oostelijke Middellandse Zee, met Constantinopel als hoofdstad",
            "rond de Oostzee in Noord-Europa, met Stockholm als belangrijkste stad",
            "in het binnenland van Afrika, ten zuiden van de Sahara en de Sahel",
            "in Oost-Azië, met het zwaartepunt in de valleien van China en Korea",
        ],
        antwoord=0,
        uitleg="Van daaruit reikte het over de Balkan, Anatolië, het Nabije Oosten en Noord-Afrika. Een rijk op drie werelddelen tegelijk.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar veroverden de Ottomanen Constantinopel?",
        antwoord="1453",
        uitleg="Daarmee eindigt het Byzantijnse Rijk. Veel historici nemen dat jaar als een van de grenzen tussen middeleeuwen en vroegmoderne tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemde men de heerser van het Ottomaanse Rijk?",
        opties=["de sultan", "de tsaar", "de farao", "de doge"],
        antwoord=0,
        uitleg="Hij was ook kalief, dus wereldlijk en godsdienstig hoofd tegelijk. Die dubbele rol versterkt zijn gezag nog.",
    ),
    dict(
        type="waarofniet",
        vraag="De sultan was zowel het wereldlijke als het godsdienstige hoofd van zijn rijk.",
        antwoord=True,
        uitleg="Bij Lodewijk XIV was dat anders: die stelde de godsdienst in dienst van zijn macht, maar het hoofd van de Kerk was de paus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben het absolutisme van de sultan en dat van Lodewijk XIV gemeen?",
        opties=[
            "alle macht ligt bij één persoon, die aan niemand verantwoording schuldig is",
            "de heerser wordt bij elke troonopvolging door de adel van het land verkozen",
            "er is een geschreven grondwet die de bevoegdheden van de heerser begrenst",
            "er is een parlement dat mee beslist over wetten en over de belastingen",
        ],
        antwoord=0,
        uitleg="Verkiezing, grondwet en parlement zijn precies wat er bij géén van beide is. Het verschil zit elders: de sultan is ook godsdienstig hoofd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het millet-stelsel?",
        opties=[
            "godsdienstige minderheden besturen hun eigen gemeenschap, met eigen recht en scholen",
            "alle inwoners van het rijk moeten zich binnen de generatie tot de islam bekeren",
            "minderheden worden zonder uitzondering het land uitgezet naar de buurlanden",
            "iedereen in het rijk valt onder één en dezelfde wet, zonder enig onderscheid",
        ],
        antwoord=0,
        uitleg="Christenen en joden betaalden een aparte belasting, maar mochten hun geloof behouden en hun zaken zelf regelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Joden die uit Spanje verdreven werden, vonden in het Ottomaanse Rijk een nieuwe thuis.",
        antwoord=True,
        uitleg="Na 1492 vestigden velen zich in Saloniki en Constantinopel. Het is een van de duidelijkste voorbeelden van dat verschil in houding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de houding tegenover minderheden in het Ottomaanse Rijk en in het christelijke Europa van die tijd?",
        opties=[
            "in het Ottomaanse Rijk mochten andere godsdiensten bestaan, in Europa werd afwijking vervolgd",
            "in de twee gebieden was elke andere godsdienst dan die van de heerser streng verboden bij wet",
            "in Europa was er volledige godsdienstvrijheid, in het Ottomaanse Rijk helemaal geen enkele",
            "in het Ottomaanse Rijk werd iedereen tot de islam gedwongen, in het christelijke Europa niemand",
        ],
        antwoord=0,
        uitleg="Gelijkheid was het niet: er was een aparte belasting en minder aanzien. Maar er was wel een plaats, en dat is in Europa lang niet zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over de Ottomaanse economie klopt níét?",
        opties=[
            "er werd geen handel gedreven met christelijke landen",
            "het rijk beheerste de landroutes naar Azië",
            "handel en ambacht bloeiden in grote steden",
            "de staat hield toezicht op prijzen en voorraden",
        ],
        antwoord=0,
        uitleg="Met christelijke landen werd juist volop gehandeld, Venetië en Frankrijk voorop. De drie andere uitspraken tekenen de Ottomaanse economie wel.",
    ),
    dict(
        type="waarofniet",
        vraag="De Ottomanen beheersten geen enkele handelsroute tussen Europa en Azië.",
        antwoord=False,
        uitleg="Ze beheersten net de landroutes, en elke tussenhandelaar nam zijn deel. Wie zelf tot bij de bron voer, omzeilde dat: daar beginnen de ontdekkingsreizen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Ottomaanse sultan noemde men in het Westen 'de Prachtlievende'?",
        antwoord="Suleyman",
        uitleg="Suleyman I regeerde van 1520 tot 1566. In eigen land noemde men hem vooral de Wetgever.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie stond er tegenover Suleyman I in de strijd om Europa?",
        opties=[
            "Karel V",
            "Lodewijk XIV",
            "Filips II",
            "Willem van Oranje",
        ],
        antwoord=0,
        uitleg="Twee heersers van twee wereldrijken, in dezelfde jaren. Wenen werd in 1529 belegerd en hield stand.",
    ),
    dict(
        type="waarofniet",
        vraag="De Franse koning sloot een verstandhouding met de sultan, hoewel die een andere godsdienst had.",
        antwoord=True,
        uitleg="Frans I zocht een bondgenoot tegen de Habsburgers. Politiek belang woog daar zwaarder dan geloof, en dat zegt veel over die tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de capitulaties?",
        opties=[
            "handelsvoorrechten die de sultan aan Europese kooplui gaf",
            "overgaven van een stad of een leger na een verloren veldslag",
            "belastingen die christenen in het rijk jaarlijks moesten betalen",
            "verdragen tussen twee Europese landen over hun onderlinge grenzen",
        ],
        antwoord=0,
        uitleg="Franse en later andere kooplui kregen eigen rechten in Ottomaanse havens. De naam heeft niets met overgave te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verliep het contact tussen het Ottomaanse Rijk en Europa?",
        opties=[
            "door oorlog, aan de grenzen in de Balkan en op zee",
            "door handel in het Middellandse Zeegebied",
            "door diplomatie, met vaste gezanten aan het hof",
            "door een volledige afsluiting van elke grens",
        ],
        antwoord=[0, 1, 2],
        uitleg="Afgesloten was er niets. Oorlog, handel en diplomatie liepen tegelijk, soms tussen dezelfde partijen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Ottomaanse Rijk begon al in de 16de eeuw snel te verzwakken.",
        antwoord=False,
        uitleg="De 16de eeuw is juist zijn hoogtepunt. Het verval zet pas veel later in, en duurt dan nog eeuwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oorzaken droegen bij tot het latere verval van het Ottomaanse Rijk?",
        opties=[
            "de handel verlegde zich naar de oceanen, weg van de landroutes",
            "Europa liep voor op het gebied van techniek en leger",
            "het rijk was zo groot dat het moeilijk te besturen was",
            "de bevolking van het rijk verdween door ziekte en hongersnood",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bevolking verdween niet. De drie andere oorzaken samen verklaren waarom het rijk stilaan terrein verloor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je Ottomaanse bouwkunst?",
        opties=[
            "grote koepels en slanke minaretten",
            "sierschrift en geometrische patronen in plaats van mensenfiguren",
            "tegelwerk in blauw en wit",
            "beelden van heiligen boven de ingang",
        ],
        antwoord=[0, 1, 2],
        uitleg="Mensen afbeelden in een gebedshuis doet men er juist niet. De Süleymaniye in Istanbul toont de drie andere kenmerken samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het rijk van Suleyman I en dat van Karel V volgden elkaar op, met bijna een eeuw ertussen.",
        antwoord=False,
        uitleg="Ze bestonden net tegelijk, allebei op hun hoogtepunt in de 16de eeuw en allebei heersend over vele volkeren en talen. Daarom kan je ze zinvol naast elkaar leggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je het Ottomaanse Rijk niet enkel als vijand van Europa beschrijven?",
        opties=[
            "er werd ook handel gedreven, en er waren verdragen over de geloofsgrens heen",
            "er is tussen het rijk en Europa nooit enige oorlog of veldslag geweest",
            "het rijk lag helemaal niet in de buurt van Europa maar ver daarbuiten",
            "er zijn over de betrekkingen met Europa geen enkele bronnen bewaard",
        ],
        antwoord=0,
        uitleg="Wie enkel de belegeringen vertelt, laat de Franse verdragen en de Venetiaanse handel weg. Dat is een keuze, en ze kleurt het beeld.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken gebruik je om samenlevingen met elkaar te vergelijken?",
        opties=[
            "politieke kenmerken, zoals de bestuurlijke organisatie",
            "sociale kenmerken, zoals ongelijkheid en migratie",
            "culturele en economische kenmerken",
            "de afstand tot de evenaar en de hoogte boven zeeniveau",
        ],
        antwoord=[0, 1, 2],
        uitleg="De ligging kan iets verklaren, maar ze is geen kenmerk van de samenleving zelf. De vier domeinen zijn dat wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is imperialisme?",
        opties=[
            "het streven van een staat om zijn macht over andere gebieden uit te breiden",
            "het bestuur van een stad door haar eigen burgers, zonder vorst boven zich",
            "een economisch systeem waarin winst opnieuw geïnvesteerd wordt",
            "een kunststroming uit de 19de eeuw met veel licht en losse toetsen",
        ],
        antwoord=0,
        uitleg="Het is een politiek kenmerk, en je vindt het zowel bij Rome als bij het Ottomaanse Rijk en bij de Europese koloniale rijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Kolonialisme en imperialisme betekenen precies hetzelfde.",
        antwoord=False,
        uitleg="Imperialisme is het streven naar macht over andere gebieden; kolonialisme is één vorm daarvan, met vestiging en bestuur ter plaatse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vergelijk je als je naar de gelaagde samenleving kijkt?",
        opties=[
            "wie bovenaan en wie onderaan staat, en waardoor dat bepaald wordt",
            "hoeveel inwoners er in totaal in die samenleving geleefd hebben",
            "welke taal men er sprak en hoeveel talen er naast elkaar bestonden",
            "hoe warm het er was en hoeveel neerslag er per jaar viel",
        ],
        antwoord=0,
        uitleg="In Egypte bepaalt het ambt de plaats, in de middeleeuwen de stand waarin je geboren wordt. De vorm verschilt, de ongelijkheid zelf niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de Egyptische en de middeleeuwse gelaagde samenleving gemeen?",
        opties=[
            "een kleine groep bovenaan leeft van het werk van een grote groep onderaan",
            "godsdienst rechtvaardigt de ordening",
            "de plaats waarin je geboren wordt, bepaalt je leven grotendeels",
            "iedereen kan door hard werken bovenaan geraken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opklimmen kon in beide nauwelijks. De drie andere punten maken de vergelijking juist zinvol.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee samenlevingen vergelijken betekent zowel gelijkenissen als verschillen benoemen.",
        antwoord=True,
        uitleg="Enkel gelijkenissen noemen maakt alles hetzelfde, enkel verschillen maakt alles uniek. Je hebt de twee nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen zijn géén historische periodes?",
        opties=[
            "de ijstijd en de ruimtetijd",
            "prehistorie en klassieke oudheid",
            "middeleeuwen en vroegmoderne tijd",
            "moderne tijd en hedendaagse tijd",
        ],
        antwoord=0,
        uitleg="De ijstijd is een klimaatbegrip, de ruimtetijd hoort bij de natuurkunde. De indeling in periodes is trouwens een afspraak van historici, geen natuurwet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het in stukken verdelen van de tijd, met namen en grenzen?",
        antwoord="periodisering",
        uitleg="Handig om over te spreken, maar altijd een keuze. Wie de grens elders legt, vertelt een ander verhaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een periodegrens altijd voor discussie vatbaar?",
        opties=[
            "de verandering gebeurt niet overal tegelijk en niet in alle domeinen samen",
            "historici kennen de juiste jaartallen van die eeuwen vandaag niet meer",
            "er zijn over de overgang tussen twee periodes geen bronnen bewaard gebleven",
            "de kalender is in de loop van de eeuwen veel te vaak gewijzigd geweest",
        ],
        antwoord=0,
        uitleg="Voor een boer in 1500 veranderde er op één dag niets. De grens ligt waar een historicus vindt dat het zwaartepunt verschuift.",
    ),
    dict(
        type="waarofniet",
        vraag="Continuïteit betekent dat er in een hele periode helemaal niets verandert.",
        antwoord=False,
        uitleg="Het gaat over wat blijft duren terwijl er elders wel verandert. De landbouw werkt in 1600 nog grotendeels als in 1300, terwijl geloof, kunst en wereldbeeld ondertussen grondig veranderden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke economische systemen kan je met elkaar vergelijken?",
        opties=[
            "een zelfvoorzienend domein in de middeleeuwen",
            "het handelskapitalisme van de vroegmoderne tijd",
            "de industriële productie van de 19de eeuw",
            "de landbouw op de maan en op de andere planeten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het laatste bestaat niet. De drie andere tonen hoe verschillend het antwoord op dezelfde vraag kan zijn: wie maakt wat, en voor wie?",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een multiculturele samenleving als cultureel vergelijkingspunt?",
        opties=[
            "een samenleving waarin mensen met verschillende culturen en godsdiensten samenleven",
            "een samenleving met bijzonder veel kunstenaars, schrijvers, musici en geleerden",
            "een samenleving waarin helemaal geen enkele godsdienst nog beleden wordt",
            "een samenleving waarin iedereen precies dezelfde taal spreekt, schrijft en leest",
        ],
        antwoord=0,
        uitleg="Het Ottomaanse Rijk en het middeleeuwse Al-Andalus zijn er voorbeelden van. Hoe men met dat naast elkaar omging, verschilt sterk.",
    ),
    dict(
        type="waarofniet",
        vraag="Slavernij komt in meerdere bestudeerde samenlevingen voor, niet enkel in de koloniale tijd.",
        antwoord=True,
        uitleg="In de klassieke oudheid, in het Arabische Rijk en in de Amerikaanse koloniën. De vorm en de schaal verschillen wel sterk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vergelijk je bij het kenmerk 'bestuurlijke organisatie'?",
        opties=[
            "wie beslist, hoe die aan de macht komt en hoe ver die macht reikt",
            "hoeveel wegen en bruggen er aangelegd zijn in het hele gebied",
            "welke kleren men droeg en welke stoffen daarvoor gebruikt werden",
            "welke dieren er in het gebied voorkwamen en welke gehouden werden",
        ],
        antwoord=0,
        uitleg="Een sultan, een absolute koning, een parlement en een stadsbestuur van patriciërs: telkens een ander antwoord op dezelfde vraag.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee samenlevingen uit dezelfde periode vergelijken heeft geen zin, want ze lijken vanzelf op elkaar.",
        antwoord=False,
        uitleg="Het Ottomaanse Rijk en Frankrijk bestonden tegelijk en verschilden grondig. Juist die vergelijking laat zien dat het ook anders kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vergelijk je samenlevingen op vaste kenmerken en niet zomaar op wat opvalt?",
        opties=[
            "met vaste punten vergelijk je hetzelfde met hetzelfde",
            "omdat het met een vaste lijst sneller gaat dan zonder",
            "omdat er over de meeste samenlevingen geen bronnen zijn",
            "omdat de vakfiche dat voor elk examen zo verplicht",
        ],
        antwoord=0,
        uitleg="Wat opvalt, is vaak wat vreemd is aan ons. Vaste punten behoeden je ervoor enkel het exotische te zien.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vergelijking tussen samenlevingen is ook een vergelijking tussen bronnen.",
        antwoord=True,
        uitleg="Over de ene samenleving heb je archieven, over de andere enkel scherven. Wat je kan vergelijken, hangt af van wat er bewaard is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een anachronisme?",
        opties=[
            "iets in de verkeerde tijd plaatsen, of oordelen met de maatstaf van nu",
            "een fout jaartal in een geschiedenisboek dat door niemand opgemerkt wordt",
            "een bron waarop geen datum staat en die je dus niet kan situeren in de tijd",
            "een woord dat bij het vertalen van een oude bron verkeerd begrepen werd",
        ],
        antwoord=0,
        uitleg="Spreken over 'de Belgen' in 1302 is er een. Bij vergelijken ligt die valkuil altijd op de loer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het vermogen om je in te leven in de tijd van de mensen die je bestudeert?",
        antwoord="historische empathie",
        uitleg="Niet hetzelfde als goedkeuren. Het betekent begrijpen waarom iets toen vanzelfsprekend leek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat leer je uit een vergelijking tussen twee samenlevingen?",
        opties=[
            "dat er meerdere antwoorden mogelijk zijn op dezelfde menselijke vragen",
            "dat de ene samenleving in alle opzichten beter is dan de andere twee",
            "dat er door de eeuwen heen eigenlijk nooit iets van betekenis verandert",
            "dat vergelijken tussen samenlevingen weinig of niets bruikbaars oplevert",
        ],
        antwoord=0,
        uitleg="Hoe ordenen mensen macht, hoe verdelen ze werk, hoe gaan ze om met wie anders is? Elke samenleving antwoordt anders.",
    ),
]
