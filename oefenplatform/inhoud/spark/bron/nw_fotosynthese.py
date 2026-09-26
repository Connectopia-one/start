# -*- coding: utf-8 -*-
"""De vragen voor "Fotosynthese en de plant" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel biologie, "Belang van fotosynthese": welke
energieomzetting, stofomzetting en stofuitwisseling er bij fotosynthese
gebeurt, het verschil tussen autotrofe en heterotrofe organismen, de
plantendelen die erbij betrokken zijn, de weg die stoffen in de plant afleggen,
en het belang van fotosynthese voor de plant, voor mens en dier en voor het
leven op aarde.

Deel 1 houdt het bij de grondstoffen, de producten en de plantendelen. Deel 2
gaat over de weg van de stoffen, over dag en nacht, over reservestoffen en over
het verband met CO₂ in de lucht en het klimaat.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat maakt een plant zelf aan met behulp van zonlicht?",
        opties=["Suiker (glucose)", "Zout", "IJzer"],
        antwoord=0,
        uitleg="Bij de fotosynthese maakt een plant glucose. Dat is een energierijke stof: er zit energie in die uit het zonlicht komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee stoffen heeft een plant nodig om aan fotosynthese te doen?",
        opties=["Water", "Koolstofdioxide", "Zuurstofgas", "Glucose"],
        antwoord=[0, 1],
        uitleg="Water (H₂O) en koolstofdioxide (CO₂) zijn de grondstoffen. Glucose (C₆H₁₂O₆) en zuurstofgas (O₂) zijn net de producten die eruit komen.",
    ),
    dict(
        type="invultekst",
        vraag="Het gas dat een plant bij de fotosynthese afgeeft, is ___.",
        antwoord=["zuurstofgas", "zuurstof"],
        uitleg="Planten geven zuurstofgas (O₂) af. Daardoor blijft er zuurstof in de lucht om in te ademen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk plantendeel gebeurt de fotosynthese vooral?",
        opties=["In het blad", "In de wortel", "In de bloem"],
        antwoord=0,
        uitleg="Bladeren liggen breed uitgespreid in het licht en zitten vol bladgroenkorrels. Daar gebeurt het grootste deel van de fotosynthese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzetting gebeurt er bij de fotosynthese?",
        opties=[
            "Lichtenergie wordt chemische energie",
            "Chemische energie wordt lichtenergie",
            "Warmte wordt elektrische energie",
        ],
        antwoord=0,
        uitleg="De stralingsenergie van de zon wordt vastgelegd als chemische energie in de glucose. Die energie kan later weer vrijkomen bij de verbranding van die suiker.",
    ),
    dict(
        type="waarofniet",
        vraag="Bladgroen is nodig om zonlicht op te vangen.",
        antwoord=True,
        uitleg="Het bladgroen in de bladgroenkorrels vangt het licht op. Zonder bladgroen kan er geen fotosynthese gebeuren; een witte plek op een blad maakt dus geen suiker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een autotroof organisme?",
        opties=[
            "Een organisme dat zijn eigen voedsel maakt",
            "Een organisme dat andere organismen opeet",
            "Een organisme dat geen energie nodig heeft",
        ],
        antwoord=0,
        uitleg="Autotroof betekent letterlijk 'zichzelf voedend'. Planten maken hun eigen energierijke stoffen. Heterotrofe organismen, zoals dieren en de mens, moeten die uit hun voedsel halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn heterotrofe organismen?",
        opties=["Een koe", "Een paddenstoel", "Een eik", "Gras"],
        antwoord=[0, 1],
        uitleg="Een koe en een paddenstoel moeten hun energierijke stoffen uit ander materiaal halen. Een eik en gras maken die zelf en zijn dus autotroof.",
    ),
    dict(
        type="invultekst",
        vraag="Met haar ___ neemt een plant water uit de bodem op.",
        antwoord=["wortels", "wortel", "wortelharen"],
        uitleg="De wortels nemen water en opgeloste mineralen op. Via het transportweefsel in de stengel gaat dat water naar de bladeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Langs welke openingen neemt een blad koolstofdioxide op?",
        opties=["Langs de huidmondjes", "Langs de nerven", "Langs de wortelharen"],
        antwoord=0,
        uitleg="Huidmondjes zijn kleine openingen, vooral aan de onderkant van het blad. Ze laten CO₂ binnen en O₂ en waterdamp naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de stengel van een plant?",
        opties=[
            "Ze draagt de bladeren en vervoert stoffen",
            "Ze neemt zonlicht op",
            "Ze maakt zaden",
        ],
        antwoord=0,
        uitleg="De stengel houdt de bladeren in het licht en bevat het transportweefsel dat water omhoog en suikers naar beneden brengt.",
    ),
    dict(
        type="waarofniet",
        vraag="Planten geven bij fotosynthese koolstofdioxide af.",
        antwoord=False,
        uitleg="Bij de fotosynthese verbruiken planten net koolstofdioxide; ze geven zuurstofgas af. Koolstofdioxide geven ze wel af bij hun celademhaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is fotosynthese belangrijk voor mens en dier?",
        opties=["Ze levert de zuurstof en het voedsel waar wij van leven", "Ze maakt de lucht rondom de plant warmer en veel vochtiger", "Ze zorgt voor regen"],
        antwoord=0,
        uitleg="Alle voedsel begint bij planten, en de zuurstof die wij inademen komt ervan. Zonder fotosynthese is er op aarde geen leven zoals wij het kennen.",
    ),
    dict(
        type="invultekst",
        vraag="De stof waarin een plant haar suiker opslaat als reserve, heet ___.",
        antwoord="zetmeel",
        uitleg="Zetmeel is een reservestof. De plant maakt het van glucose en slaat het op in bladeren, knollen of zaden, bijvoorbeeld in een aardappel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gas is een broeikasgas dat planten uit de lucht halen?",
        opties=["Koolstofdioxide", "Zuurstofgas", "Waterstofgas"],
        antwoord=0,
        uitleg="Koolstofdioxide (CO₂) is een broeikasgas. Planten nemen het op bij de fotosynthese, en daarom helpen bossen tegen de klimaatverandering.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder licht kan een plant geen fotosynthese doen.",
        antwoord=True,
        uitleg="Licht levert de energie voor de omzetting. In het donker staat de fotosynthese stil, terwijl de celademhaling van de plant gewoon doorgaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke plantendelen spelen een rol bij de fotosynthese?",
        opties=["Het blad", "De bladgroenkorrels", "De huidmondjes", "De bloem"],
        antwoord=[0, 1, 2],
        uitleg="Het blad vangt licht op, de bladgroenkorrels doen de omzetting en de huidmondjes laten de gassen door. De bloem dient voor de voortplanting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een plant met de glucose die ze maakt?",
        opties=["Ze gebruikt die als brandstof en bouwstof en slaat de rest op", "Ze geeft die via haar wortels aan de bodem en aan de buurplanten", "Ze ademt die uit"],
        antwoord=0,
        uitleg="Een deel van de glucose verbrandt de plant zelf voor energie, een deel bouwt ze om tot cellulose voor haar celwanden, en de rest bewaart ze als zetmeel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant gebruikt zelf ook zuurstof.",
        antwoord=True,
        uitleg="Een plant ademt: in haar mitochondriën verbrandt ze glucose met zuurstof. Overdag maakt ze meer zuurstof dan ze verbruikt, 's nachts alleen maar verbruikt ze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar in het blad zitten de bladgroenkorrels?",
        opties=["In de cellen van het blad", "Tussen de bladeren", "Op de wortels"],
        antwoord=0,
        uitleg="Bladgroenkorrels zijn celonderdelen: ze liggen in het cytoplasma van de bladcellen. Daarom moet je een microscoop gebruiken om ze te zien.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke weg legt water af in een plant?",
        opties=[
            "Van de wortels via de stengel naar de bladeren",
            "Van de bladeren via de stengel naar de wortels",
            "Van de bloem rechtstreeks naar de wortels",
        ],
        antwoord=0,
        uitleg="Water gaat omhoog: opgenomen door de wortels, door het transportweefsel van de stengel, tot in de bladeren. Daar wordt het gebruikt of het verdampt via de huidmondjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke weg legt de glucose af die in het blad gemaakt wordt?",
        opties=["Van het blad naar de rest van de plant, ook de wortels", "Van het blad rechtstreeks de lucht in via de huidmondjes", "Van de wortels naar het blad"],
        antwoord=0,
        uitleg="De suikers gaan via het transportweefsel naar alle plantendelen die zelf geen fotosynthese doen, zoals de wortels, de bloemen en de vruchten.",
    ),
    dict(
        type="waarofniet",
        vraag="'s Nachts geeft een plant netto zuurstof af.",
        antwoord=False,
        uitleg="'s Nachts ligt de fotosynthese stil en blijft alleen de celademhaling over. De plant verbruikt dan zuurstof en geeft koolstofdioxide af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stofomzetting hoort bij de fotosynthese?",
        opties=[
            "Koolstofdioxide en water worden glucose en zuurstofgas",
            "Glucose en zuurstofgas worden koolstofdioxide en water",
            "Water wordt waterstofgas en zuurstofgas",
        ],
        antwoord=0,
        uitleg="Fotosynthese: CO₂ + H₂O → C₆H₁₂O₆ + O₂, met licht als energiebron. De celademhaling is precies de omgekeerde omzetting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan huidmondjes vooral aan de onderkant van een blad?",
        opties=["Zo verdampt er minder water dan in de volle zon bovenaan", "Zo vangen ze meer licht op dan aan de bovenkant van het blad", "Zo kunnen insecten er beter bij"],
        antwoord=0,
        uitleg="De onderkant is koeler en schaduwrijker. De plant kan er gassen uitwisselen zonder te veel water te verliezen: een aanpassing aan haar omgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden de bladeren van een plant in een donkere kast na een tijd geel?",
        opties=["Zonder licht maakt de plant geen suikers en breekt bladgroen af", "Zonder licht krijgt de plant te veel water binnen via haar wortels", "Zonder licht worden de wortels te warm"],
        antwoord=0,
        uitleg="Bladgroen heeft licht nodig om zin te hebben. Zonder licht stopt de fotosynthese, teert de plant in op haar reserves en verdwijnt de groene kleur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over fotosynthese en celademhaling kloppen?",
        opties=[
            "Fotosynthese legt energie vast, celademhaling maakt ze vrij",
            "Planten doen allebei",
            "Dieren doen alleen celademhaling",
            "Celademhaling gebeurt enkel in het donker",
        ],
        antwoord=[0, 1, 2],
        uitleg="De twee zijn elkaars omgekeerde. Een plant doet ze allebei, een dier alleen de celademhaling, en die loopt dag en nacht door.",
    ),
    dict(
        type="invultekst",
        vraag="Organismen die hun eigen energierijke stoffen maken, noem je ___.",
        antwoord=["autotroof", "autotrofe", "autotrofen"],
        uitleg="Planten, algen en sommige bacteriën zijn autotroof. In een voedselketen zijn zij daarom de producenten waar alles mee begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boer zet zijn serre vol extra koolstofdioxide. Waarom?",
        opties=[
            "Omdat de planten dan meer fotosynthese doen en sneller groeien",
            "Omdat planten koolstofdioxide inademen om energie te maken",
            "Omdat de planten er warmer van worden",
        ],
        antwoord=0,
        uitleg="CO₂ is een grondstof voor de fotosynthese. Meer grondstof betekent meer glucose, dus meer groei — zolang licht en water niet tekortschieten.",
    ),
    dict(
        type="waarofniet",
        vraag="Ontbossing zorgt ervoor dat er minder koolstofdioxide uit de lucht gehaald wordt.",
        antwoord=True,
        uitleg="Minder bomen betekent minder fotosynthese, dus minder opname van CO₂. Omdat CO₂ een broeikasgas is, versnelt ontbossing de klimaatverandering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stofuitwisseling gebeurt er bij de fotosynthese tussen plant en omgeving?",
        opties=[
            "Opname van CO₂ en water, afgifte van O₂",
            "Opname van O₂, afgifte van CO₂",
            "Opname van zetmeel, afgifte van glucose",
        ],
        antwoord=0,
        uitleg="Stofuitwisseling is wat er in en uit gaat: koolstofdioxide langs de huidmondjes, water langs de wortels, en zuurstofgas weer naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zit er zetmeel in een aardappel?",
        opties=[
            "De plant slaat er haar suikerreserve in op",
            "De aardappel doet zelf fotosynthese onder de grond",
            "Het zetmeel komt uit de bodem",
        ],
        antwoord=0,
        uitleg="Een aardappel is een knol: een ondergrondse voorraadkast. De bladeren maken de glucose en de plant slaat die als zetmeel op om later uit te lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is fotosynthese belangrijk voor de plant zelf?",
        opties=["Ze levert de energierijke stoffen om te groeien en te leven", "Ze zorgt dat de plant bloemen krijgt zonder energie te gebruiken", "Ze houdt de plant koel"],
        antwoord=0,
        uitleg="De plant heeft glucose nodig als brandstof voor haar celademhaling en als bouwstof voor nieuwe cellen. Zonder fotosynthese heeft ze geen van beide.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant kan zonder mineralen uit de bodem perfect groeien.",
        antwoord=False,
        uitleg="Naast water en CO₂ heeft een plant mineralen nodig, zoals stikstof. Die komen mee met het water uit de bodem; zonder blijft ze klein en verkleuren de bladeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn producten van de fotosynthese?",
        opties=["Glucose", "Zuurstofgas", "Koolstofdioxide", "Water"],
        antwoord=[0, 1],
        uitleg="Wat eruit komt, zijn glucose en zuurstofgas. Koolstofdioxide en water gaan er net in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee identieke planten staan op de vensterbank. Bij één plak je alle bladeren onderaan af, zodat de huidmondjes dicht zitten. Wat verwacht je?",
        opties=[
            "Die plant groeit trager, want ze krijgt minder CO₂ binnen",
            "Die plant groeit sneller, want ze verliest geen water",
            "Er verandert niets",
        ],
        antwoord=0,
        uitleg="De huidmondjes zijn de deur voor de gassen. Gaan ze dicht, dan stokt de aanvoer van koolstofdioxide en valt de fotosynthese grotendeels stil.",
    ),
    dict(
        type="invultekst",
        vraag="De kleine openingen in een blad waarlangs gassen in en uit gaan, heten ___.",
        antwoord="huidmondjes",
        uitleg="Een huidmondje is een spleetje tussen twee sluitcellen. Bij droogte gaan die sluitcellen dicht, zodat de plant geen water verliest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemen we glucose een energierijke stof?",
        opties=[
            "Omdat er bij de verbranding ervan energie vrijkomt",
            "Omdat ze zwaar is",
            "Omdat ze licht uitstraalt",
        ],
        antwoord=0,
        uitleg="De energie van het zonlicht zit opgeslagen in de bindingen van de glucose. Verbrandt een cel die suiker met zuurstof, dan komt die energie weer vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="De energie in het vlees dat je eet, komt oorspronkelijk van de zon.",
        antwoord=True,
        uitleg="Het dier at planten (of dieren die planten aten), en die planten legden zonne-energie vast in suikers. Zo goed als alle energie in ons voedsel begint bij de fotosynthese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over autotroof en heterotroof kloppen?",
        opties=[
            "Een plant is autotroof",
            "Een mens is heterotroof",
            "Een schimmel is autotroof",
            "Autotrofe organismen hebben geen energie nodig",
        ],
        antwoord=[0, 1],
        uitleg="Planten maken hun eigen voedsel, mensen en schimmels niet. Ook een autotroof organisme heeft energie nodig; het haalt ze alleen rechtstreeks uit het licht.",
    ),
]
