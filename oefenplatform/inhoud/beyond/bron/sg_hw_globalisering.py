# -*- coding: utf-8 -*-
"""Humane wetenschappen: globalisering in de politiek.

Het zesde van zes thema's over politieke wetenschappen, enkel voor humane
wetenschappen (fiche 3DDO, onderdeel "Globalisering in de politiek").

De lijstjes staan letterlijk in de fiche:

    supranationale organisaties: EU, Europees Hof van de Rechten van de Mens,
        G7, Internationaal Strafhof, NAVO, VN, WHO
    de Europese instellingen: Europees Parlement, Europese Commissie, Raad
        van de Europese Unie, Europese Raad (samenstelling, functie,
        bevoegdheid, werking)
    het belang van supranationale instellingen bij maatschappelijke thema's
    de invloed van Europese wetgeving en Europees recht op België
    maatschappelijke thema's die een Europese en mondiale aanpak vragen, met
        de link naar het lokale niveau: ecologie, gezondheid, klimaat,
        migratie, voedselveiligheid, vrede en veiligheid

Deel 1 zijn de supranationale organisaties.
Deel 2 zijn de Europese instellingen en de invloed van Europa op België.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een supranationale organisatie?",
        opties=[
            "een organisatie boven de landen, die een deel van hun macht krijgt",
            "een organisatie die enkel binnen één gemeente werkt en beslist",
            "een politieke partij die in meerdere provincies kandidaten heeft",
            "een bedrijf dat in veel verschillende landen tegelijk producten verkoopt",
        ],
        antwoord=0,
        uitleg="Supra betekent boven. Landen werken samen in zo'n organisatie en aanvaarden dat ze over sommige zaken samen beslissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze organisaties werken over de grenzen van landen heen?",
        opties=["de VN", "de NAVO", "de WHO", "de G7", "de Raad van State", "het Vlaams Parlement"],
        antwoord=[0, 1, 2, 3],
        uitleg="De VN, de NAVO, de WHO en de G7 zijn internationale organisaties. De Raad van State en het Vlaams Parlement zijn Belgische instellingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kernopdracht van de Verenigde Naties (VN)?",
        opties=[
            "de vrede en veiligheid in de wereld bewaren en samenwerking bevorderen",
            "een gemeenschappelijke munt beheren voor alle landen die lid zijn",
            "een militair bondgenootschap vormen van Europa en Noord-Amerika",
            "de economie van de zeven rijkste landen van de wereld op elkaar afstemmen",
        ],
        antwoord=0,
        uitleg="De VN werden in 1945 opgericht, na de Tweede Wereldoorlog. Bijna alle landen van de wereld zijn lid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de NAVO?",
        opties=[
            "een militair bondgenootschap waarin de leden elkaar verdedigen bij een aanval",
            "een organisatie die zorgt voor de gezondheid van alle mensen in de wereld",
            "een rechtbank voor oorlogsmisdaden en genocide",
            "een overleg van de zeven grootste economieën",
        ],
        antwoord=0,
        uitleg="In de NAVO geldt dat een aanval op één lid als een aanval op allemaal geldt. België is lid sinds de oprichting in 1949.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de opdracht van de WHO, de Wereldgezondheidsorganisatie?",
        opties=[
            "de gezondheid wereldwijd bevorderen en landen helpen bij ziektes en pandemieën",
            "landen verdedigen als ze militair aangevallen worden door een buurland",
            "oordelen over klachten van burgers over schendingen van hun mensenrechten",
            "regels maken over de handel in landbouwproducten binnen Europa",
        ],
        antwoord=0,
        uitleg="De WHO is een organisatie van de VN. Ze gaf onder meer advies en richtlijnen tijdens de coronapandemie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de G7?",
        opties=[
            "een overleg tussen zeven grote industrielanden",
            "een militair bondgenootschap van zeven Europese landen",
            "de zeven belangrijkste instellingen van de Europese Unie",
            "een rechtbank met zeven rechters in Den Haag",
        ],
        antwoord=0,
        uitleg="De G7 zijn de Verenigde Staten, Canada, Japan, Duitsland, Frankrijk, Italië en het Verenigd Koninkrijk. De EU zit mee aan tafel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het Internationaal Strafhof?",
        opties=[
            "personen berechten voor de zwaarste misdaden, zoals genocide",
            "conflicten tussen buren uit verschillende Europese landen beslechten",
            "nagaan of Belgische wetten in overeenstemming zijn met de grondwet",
            "beslissen welke landen lid mogen worden van de Europese Unie",
        ],
        antwoord=0,
        uitleg="Het Internationaal Strafhof in Den Haag vervolgt personen, ook leiders, voor genocide, misdaden tegen de menselijkheid en oorlogsmisdaden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het Europees Hof van de Rechten van de Mens?",
        opties=[
            "oordelen of een land de mensenrechten van het Europees Verdrag schond",
            "oorlogsmisdadigers uit de hele wereld berechten en straffen",
            "de wetten van de Europese Unie samen met het Europees Parlement maken",
            "de begroting van de Europese Unie elk jaar opnieuw goedkeuren",
        ],
        antwoord=0,
        uitleg="Het Hof zetelt in Straatsburg. Een burger die in eigen land geen gelijk kreeg, kan er klagen tegen een staat die zijn mensenrechten schond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land wordt aangevallen en vraagt de andere leden van zijn bondgenootschap om militaire hulp. Over welke organisatie gaat het hier het meest waarschijnlijk?",
        opties=["de NAVO", "de WHO", "de G7", "het Internationaal Strafhof"],
        antwoord=0,
        uitleg="De NAVO is een militair bondgenootschap. De leden beloven elkaar te verdedigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voormalige legerleider wordt beschuldigd van genocide in zijn land. Welke organisatie kan hem berechten als zijn eigen land dat niet doet?",
        opties=["het Internationaal Strafhof", "het Europees Hof van de Rechten van de Mens", "de Europese Commissie", "de WHO"],
        antwoord=0,
        uitleg="Het Internationaal Strafhof berecht personen voor de zwaarste misdaden. Het Europees Hof van de Rechten van de Mens oordeelt over staten, niet over personen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgische gedetineerde vindt dat de overvolle gevangenis zijn mensenrechten schendt. Hij kreeg in België geen gelijk. Waar kan hij nog terecht?",
        opties=[
            "bij het Europees Hof van de Rechten van de Mens",
            "bij het Internationaal Strafhof",
            "bij de Raad van de Europese Unie",
            "bij de Verenigde Naties in New York",
        ],
        antwoord=0,
        uitleg="Het Europees Hof van de Rechten van de Mens kan oordelen dat België het Europees Verdrag voor de Rechten van de Mens schond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vragen thema's zoals klimaat en pandemieën een aanpak over de grenzen heen?",
        opties=[
            "omdat vervuiling en ziektes zich niets aantrekken van landsgrenzen",
            "omdat elk land deze thema's volgens de grondwet alleen mag aanpakken",
            "omdat gemeenten er niets aan kunnen of mogen doen",
            "omdat supranationale organisaties de enige zijn die wetten mogen maken",
        ],
        antwoord=0,
        uitleg="Uitstoot in één land verwarmt de hele aarde en een virus verspreidt zich met reizigers. Eén land alleen kan het niet oplossen. Toch zijn er ook lokale acties nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Een organisatie boven de landen, waaraan landen een deel van hun macht afstaan, heet een ... organisatie.",
        antwoord=["supranationale"],
        uitleg="Supra betekent boven, nationaal slaat op de natie.",
    ),
    dict(
        type="waarofniet",
        vraag="België is lid van de NAVO.",
        antwoord=True,
        uitleg="België was een van de stichtende leden in 1949. Het hoofdkwartier van de NAVO ligt zelfs in Brussel.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Europees Hof van de Rechten van de Mens is hetzelfde als het Internationaal Strafhof.",
        antwoord=False,
        uitleg="Het Europees Hof oordeelt in Straatsburg over staten die mensenrechten schenden. Het Internationaal Strafhof in Den Haag berecht personen voor de zwaarste misdaden.",
    ),
    dict(
        type="waarofniet",
        vraag="De WHO is een militaire organisatie.",
        antwoord=False,
        uitleg="De WHO is de Wereldgezondheidsorganisatie van de VN. Ze werkt rond gezondheid, niet rond defensie.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook een gemeente kan iets doen aan een mondiaal thema zoals klimaat.",
        antwoord=True,
        uitleg="Een gemeente kan bijvoorbeeld fietspaden aanleggen of gebouwen isoleren. Zo hangen het mondiale en het lokale niveau samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk maatschappelijk thema vraagt vooral samenwerking rond grenscontrole, opvang en asiel?",
        opties=["migratie", "voedselveiligheid", "ecologie", "gezondheid"],
        antwoord=0,
        uitleg="Mensen op de vlucht reizen door verschillende landen. Daarom zoekt de EU naar gemeenschappelijke afspraken over asiel en opvang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partij besmet vlees wordt in één Europees land ontdekt, maar werd al naar tien andere landen verkocht. Welk thema vraagt hier een Europese aanpak?",
        opties=["voedselveiligheid", "migratie", "vrede en veiligheid", "klimaat"],
        antwoord=0,
        uitleg="Voedsel wordt over heel Europa verhandeld. Daarom zijn er Europese regels en een waarschuwingssysteem voor voedselveiligheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan landen een deel van hun macht af aan supranationale organisaties?",
        opties=[
            "omdat ze samen meer kunnen bereiken bij problemen die geen grenzen kennen",
            "omdat ze dan geen eigen regering of eigen parlement meer nodig hebben",
            "omdat de grondwet van elk land dat uitdrukkelijk zo verplicht",
            "omdat ze dan zelf geen belastingen meer moeten heffen bij hun burgers",
        ],
        antwoord=0,
        uitleg="Samenwerken geeft meer slagkracht bij vrede, handel, gezondheid of klimaat. In ruil aanvaarden landen gemeenschappelijke regels.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn instellingen van de Europese Unie?",
        opties=[
            "het Europees Parlement",
            "de Europese Commissie",
            "de Raad van de Europese Unie",
            "de Europese Raad",
            "de Veiligheidsraad",
            "het Internationaal Strafhof",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="De Veiligheidsraad hoort bij de VN en het Internationaal Strafhof is geen instelling van de EU.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt het Europees Parlement samengesteld?",
        opties=[
            "de burgers kiezen de leden rechtstreeks, om de vijf jaar",
            "elke regering duidt één minister aan die het land vertegenwoordigt",
            "de staatshoofden en regeringsleiders van de lidstaten komen samen",
            "elke lidstaat stuurt één commissaris met een eigen bevoegdheid",
        ],
        antwoord=0,
        uitleg="Het Europees Parlement is de enige EU-instelling die rechtstreeks door de burgers gekozen wordt. Grotere landen hebben meer zetels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de rol van de Europese Commissie?",
        opties=[
            "nieuwe Europese wetten voorstellen en nagaan of de lidstaten de regels naleven",
            "de algemene politieke richting van de EU bepalen als top van regeringsleiders",
            "rechtstreeks de stem van de Europese burgers vertegenwoordigen",
            "als enige instelling de Europese wetten goedkeuren zonder anderen",
        ],
        antwoord=0,
        uitleg="De Commissie heeft het recht om wetten voor te stellen en voert het beleid uit. Ze is de hoedster van de verdragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie zit in de Raad van de Europese Unie?",
        opties=[
            "de ministers van de lidstaten, per thema, bijvoorbeeld de ministers van Landbouw",
            "de staatshoofden en regeringsleiders, onder leiding van een vaste voorzitter",
            "rechtstreeks verkozen volksvertegenwoordigers uit alle lidstaten",
            "één commissaris per lidstaat, die niet het eigen land verdedigt",
        ],
        antwoord=0,
        uitleg="In de Raad van de EU zitten de vakministers van de lidstaten. Samen met het Europees Parlement keurt de Raad de Europese wetten goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie zit in de Europese Raad?",
        opties=[
            "de staatshoofden en regeringsleiders van de lidstaten",
            "de ministers van de lidstaten die per beleidsdomein samenkomen",
            "de leden die de burgers om de vijf jaar rechtstreeks kiezen",
            "de rechters van het Hof van Justitie van de Europese Unie",
        ],
        antwoord=0,
        uitleg="De Europese Raad bepaalt de grote lijnen en prioriteiten van de EU. Hij maakt zelf geen wetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee instellingen keuren samen de Europese wetten goed?",
        opties=[
            "het Europees Parlement en de Raad van de Europese Unie",
            "de Europese Commissie en de Europese Raad",
            "de Europese Raad en het Europees Parlement",
            "de Europese Commissie en de Raad van de Europese Unie",
        ],
        antwoord=0,
        uitleg="De Commissie stelt voor, het Parlement en de Raad van de EU beslissen samen. Zo spreken zowel de burgers als de lidstaten mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="De regeringsleiders van alle lidstaten komen samen in Brussel en spreken af dat klimaat de komende jaren een topprioriteit wordt. Welke instelling is dit?",
        opties=["de Europese Raad", "de Raad van de Europese Unie", "de Europese Commissie", "het Europees Parlement"],
        antwoord=0,
        uitleg="De staatshoofden en regeringsleiders vormen de Europese Raad. Die bepaalt de grote politieke richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="De Europese Commissie stelt een nieuwe regel voor over de herbruikbaarheid van verpakkingen. Wat gebeurt er daarna meestal?",
        opties=[
            "het Europees Parlement en de Raad van de EU beslissen er samen over",
            "de Commissie keurt haar eigen voorstel meteen goed en het geldt de volgende dag",
            "elke gemeente in Europa stemt afzonderlijk over het nieuwe voorstel",
            "het Europees Hof van de Rechten van de Mens beslist of het voorstel doorgaat",
        ],
        antwoord=0,
        uitleg="Bij de gewone wetgevingsprocedure moeten Parlement en Raad allebei akkoord gaan voor een voorstel een Europese wet wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan Europese wetgeving invloed hebben op de politiek in België?",
        opties=[
            "België moet Europese richtlijnen omzetten in eigen wetten of decreten",
            "Europese regels gelden enkel voor de landen buiten de Europese Unie",
            "België mag zelf kiezen of het een Europese verordening volgt",
            "Europese wetten gelden enkel in Brussel, waar de instellingen liggen",
        ],
        antwoord=0,
        uitleg="Een richtlijn legt een doel vast dat elk land in eigen regels moet omzetten. Een verordening geldt meteen in alle lidstaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Europa legt een grens vast voor de hoeveelheid fijn stof in de lucht. Vlaanderen moet daarom maatregelen nemen in de steden. Wat toont dit voorbeeld?",
        opties=[
            "Europese regels werken door tot op het regionale en lokale niveau",
            "Vlaanderen beslist volledig zelf over de luchtkwaliteit, los van Europa",
            "de NAVO bepaalt de milieuregels voor België",
            "milieu is een bevoegdheid van de federale rechtbanken",
        ],
        antwoord=0,
        uitleg="Europese doelen over klimaat en milieu moeten in België door gewesten en gemeenten worden uitgevoerd. Zo hangen de niveaus samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar zetelen de meeste instellingen van de Europese Unie?",
        opties=["in Brussel", "in Genève", "in New York", "in Den Haag"],
        antwoord=0,
        uitleg="De Commissie, de Raad van de EU en de Europese Raad zitten in Brussel. Het Europees Parlement vergadert in Brussel en Straatsburg.",
    ),
    dict(
        type="invultekst",
        vraag="De enige instelling van de EU die rechtstreeks door de burgers gekozen wordt, is het Europees ...",
        antwoord=["Parlement", "parlement"],
        uitleg="De Europese verkiezingen vinden om de vijf jaar plaats, de laatste keer in juni 2024.",
    ),
    dict(
        type="waarofniet",
        vraag="De Europese Raad en de Raad van de Europese Unie zijn dezelfde instelling.",
        antwoord=False,
        uitleg="De Europese Raad bestaat uit de staatshoofden en regeringsleiders. De Raad van de Europese Unie bestaat uit de vakministers van de lidstaten.",
    ),
    dict(
        type="waarofniet",
        vraag="De Europese Commissie heeft het recht om nieuwe Europese wetten voor te stellen.",
        antwoord=True,
        uitleg="Dat heet het initiatiefrecht. Parlement en Raad beslissen daarna over het voorstel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Belgische rechter moet rekening houden met het Europees recht.",
        antwoord=True,
        uitleg="Europees recht gaat voor op nationaal recht. Een Belgische rechter moet een Belgische regel die ermee in strijd is, buiten toepassing laten.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Europees Parlement wordt samengesteld door de regeringen van de lidstaten.",
        antwoord=False,
        uitleg="De leden van het Europees Parlement worden rechtstreeks door de burgers gekozen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instelling vertegenwoordigt vooral de belangen van de lidstaten in de Europese wetgeving?",
        opties=[
            "de Raad van de Europese Unie",
            "het Europees Parlement",
            "de Europese Commissie",
            "het Europees Hof van de Rechten van de Mens",
        ],
        antwoord=0,
        uitleg="In de Raad zitten de ministers van de lidstaten. Het Parlement vertegenwoordigt de burgers en de Commissie het algemeen Europees belang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vertegenwoordigt de Europese Commissie?",
        opties=[
            "het algemeen belang van de hele Europese Unie",
            "de belangen van het land waar elke commissaris vandaan komt",
            "de standpunten van de grootste partij in het Europees Parlement",
            "de belangen van de landen buiten de Europese Unie",
        ],
        antwoord=0,
        uitleg="Elke lidstaat levert één commissaris, maar die moet het belang van heel de EU dienen en niet dat van zijn eigen land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Europees land wordt bedreigd door een buurland buiten de EU. Welke organisatie zorgt het meest voor de militaire verdediging?",
        opties=["de NAVO", "de Europese Commissie", "de WHO", "het Europees Parlement"],
        antwoord=0,
        uitleg="De EU werkt ook rond veiligheid, maar de gezamenlijke militaire verdediging van de meeste Europese landen loopt via de NAVO.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een Europese verordening en een Europese richtlijn?",
        opties=[
            "een verordening geldt meteen overal, een richtlijn moet elk land eerst in eigen regels omzetten",
            "een richtlijn geldt meteen overal, een verordening moet elk land eerst in eigen regels omzetten",
            "een verordening geldt enkel voor Brussel, een richtlijn voor de rest van de Europese Unie",
            "een verordening is een advies zonder gevolgen, een richtlijn is een straf voor een lidstaat",
        ],
        antwoord=0,
        uitleg="Een verordening is meteen bindend in alle lidstaten. Een richtlijn legt een doel vast, en elk land kiest zelf hoe het dat in zijn wetten of decreten bereikt.",
    ),
]
