# -*- coding: utf-8 -*-
"""Een nieuwe wereldorde: de Verenigde Naties en de Koude Oorlog.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de wereld na
1945, met de Verenigde Naties, de verdeling in twee blokken, de crisissen van de
Koude Oorlog en het einde ervan rond 1989.

Deel 1 gaat over de nieuwe orde en over het begin van de Koude Oorlog. Deel 2
gaat over de crisissen, de ontspanning en de val van het Oostblok.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke twee mogendheden bepaalden na 1945 de wereldpolitiek?",
        opties=[
            "de Verenigde Staten en de Sovjet-Unie",
            "het Verenigd Koninkrijk en Frankrijk",
            "de Duitse Bondsrepubliek en Japan",
            "de Volksrepubliek China en India",
        ],
        antwoord=0,
        uitleg="Men spreekt van een bipolaire wereld: twee polen waar al de rest zich naar moest verhouden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organisatie werd in 1945 opgericht om oorlogen te voorkomen?",
        opties=[
            "de Verenigde Naties",
            "de Volkenbond",
            "de Noord-Atlantische Verdragsorganisatie",
            "de Europese Economische Gemeenschap",
        ],
        antwoord=0,
        uitleg="Zij nam de taak over van de Volkenbond, die daar tussen de twee oorlogen in gefaald had.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk orgaan van de Verenigde Naties kan dwingende beslissingen nemen?",
        opties=[
            "de Veiligheidsraad",
            "de Algemene Vergadering",
            "het secretariaat",
            "de Wereldgezondheidsorganisatie",
        ],
        antwoord=0,
        uitleg="Vijf leden hebben er een vast zitje en een vetorecht. Daardoor kan één van hen elk besluit blokkeren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het recht van een vast lid van de Veiligheidsraad om een besluit te blokkeren?",
        antwoord=["het vetorecht", "vetorecht", "veto"],
        uitleg="Tijdens de Koude Oorlog is daar zo vaak gebruik van gemaakt dat de raad vaak verlamd lag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de Universele Verklaring van de Rechten van de Mens van 1948?",
        opties=[
            "rechten die voor alle mensen, overal, gelden",
            "regels voor de handel tussen de lidstaten",
            "grenzen van de staten na de Tweede Wereldoorlog",
            "voorwaarden voor de herstelbetalingen van Duitsland",
        ],
        antwoord=0,
        uitleg="Zij is geen verdrag met een rechtbank erachter, maar wel de maatstaf waaraan staten afgemeten worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het ijzeren gordijn?",
        opties=[
            "de scheidingslijn tussen west en oost in Europa",
            "de grens tussen de Verenigde Staten en de Sovjet-Unie",
            "de muur die rond de stad Berlijn werd gebouwd",
            "de verdedigingslinie van de Duitsers in 1944",
        ],
        antwoord=0,
        uitleg="Churchill gebruikte dat beeld in 1946. De lijn liep van de Oostzee tot de Adriatische Zee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het Marshallplan?",
        opties=[
            "Amerikaanse steun voor de heropbouw van West-Europa",
            "Sovjetsteun voor de heropbouw van Oost-Europa",
            "een plan om Duitsland in vier zones te verdelen",
            "een plan om de Verenigde Naties op te richten",
        ],
        antwoord=0,
        uitleg="Het hielp de economie weer op de been en bond die landen tegelijk aan de Verenigde Staten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke militaire bondgenootschappen stonden in de Koude Oorlog tegenover elkaar?",
        opties=[
            "de NAVO in het westen",
            "het Warschaupact in het oosten",
            "de Volkenbond in Genève",
            "de Entente van de Eerste Wereldoorlog",
        ],
        antwoord=[0, 1],
        uitleg="Een aanval op één lid gold als een aanval op allemaal. Zo stond heel Europa in twee kampen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er met Duitsland na de Tweede Wereldoorlog?",
        opties=[
            "het werd verdeeld en in 1949 twee staten",
            "het bleef één staat met één regering in Berlijn",
            "het werd volledig bij de Sovjet-Unie ingelijfd",
            "het werd onder bestuur van de Verenigde Naties geplaatst",
        ],
        antwoord=0,
        uitleg="Uit de westelijke zones kwam de Bondsrepubliek, uit de sovjetzone de Duitse Democratische Republiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed het westen tijdens de blokkade van Berlijn in 1948 en 1949?",
        opties=[
            "het bracht de stad maandenlang per vliegtuig voorraden",
            "het verliet de stad en liet ze aan de Sovjet-Unie",
            "het verklaarde de Sovjet-Unie daarvoor de oorlog",
            "het liet de Verenigde Naties de stad besturen",
        ],
        antwoord=0,
        uitleg="Die luchtbrug hield West-Berlijn in leven. De Sovjet-Unie hief de blokkade uiteindelijk op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werd in 1961 de Berlijnse Muur gebouwd?",
        opties=[
            "om de vlucht van inwoners naar het westen te stoppen",
            "om West-Berlijn tegen een aanval te beschermen",
            "om de stad tegen een overstroming te beveiligen",
            "om de grens met Polen vast te leggen",
        ],
        antwoord=0,
        uitleg="Honderdduizenden mensen waren via Berlijn naar het westen vertrokken, vaak jong en goed opgeleid.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar werd de Berlijnse Muur gebouwd?",
        antwoord=["1961"],
        uitleg="Hij viel in november 1989, dus hij heeft bijna dertig jaar dwars door de stad gestaan.",
    ),
    dict(
        type="waarofniet",
        vraag="De Koude Oorlog was een oorlog waarin de Verenigde Staten en de Sovjet-Unie rechtstreeks tegen elkaar vochten.",
        antwoord=False,
        uitleg="Zij vochten niet rechtstreeks, wel langs bondgenoten, wapens, spionage en propaganda.",
    ),
    dict(
        type="waarofniet",
        vraag="De Verenigde Naties werden opgericht met een Veiligheidsraad waarin vijf leden een vetorecht hebben.",
        antwoord=True,
        uitleg="Het zijn de overwinnaars van 1945. Dat die samenstelling verouderd is, wordt al decennia besproken.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Marshallplan was bedoeld voor West-Europa en versterkte de band met de Verenigde Staten.",
        antwoord=True,
        uitleg="De landen van het Oostblok mochten er van de Sovjet-Unie niet op ingaan.",
    ),
    dict(
        type="waarofniet",
        vraag="De NAVO en het Warschaupact werden in hetzelfde jaar opgericht.",
        antwoord=False,
        uitleg="De NAVO kwam er in 1949, het Warschaupact pas in 1955, als antwoord daarop.",
    ),
    dict(
        type="waarofniet",
        vraag="Berlijn lag volledig in de sovjetzone van Duitsland.",
        antwoord=True,
        uitleg="Toch werd de stad zelf in vier sectoren verdeeld. Daardoor lag West-Berlijn als een eiland in het oosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de twee blokken van de Koude Oorlog kloppen?",
        opties=[
            "het westen koos voor een markteconomie en verkiezingen",
            "het oosten koos voor een planeconomie en één partij",
            "beide blokken hadden dezelfde economische orde",
            "beide blokken lieten vrije verkiezingen toe",
        ],
        antwoord=[0, 1],
        uitleg="Niet enkel legers stonden tegenover elkaar, maar twee manieren om een samenleving in te richten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de afschrikking van de Koude Oorlog?",
        opties=[
            "wie aanvalt, wordt zelf ook vernietigd",
            "wie aanvalt, komt er zonder schade van af",
            "wie zijn kernwapens afschaft, is veilig",
            "wie het eerst aanvalt, verliest nooit",
        ],
        antwoord=0,
        uitleg="Beide kampen hielden zoveel kernwapens dat een aanval zinloos werd. Die logica heeft de angst van een halve eeuw bepaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een kaart van Europa uit 1960 met een dikke lijn van de Oostzee tot de Adriatische Zee. Wat stelt die voor?",
        opties=[
            "het ijzeren gordijn tussen de twee blokken",
            "de frontlijn van de Tweede Wereldoorlog",
            "de grens van het Romeinse Rijk",
            "de taalgrens van het Europese vasteland",
        ],
        antwoord=0,
        uitleg="Die lijn liep dwars door Duitsland en sneed Europa decennia in twee delen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in Korea tussen 1950 en 1953?",
        opties=[
            "noord en zuid vochten een oorlog uit",
            "het land werd door de Verenigde Naties tot één staat gemaakt",
            "het land werd een kolonie van de Sovjet-Unie",
            "het land bleef volledig buiten de Koude Oorlog",
        ],
        antwoord=0,
        uitleg="Elk van hen werd door een van de twee blokken gesteund. De wapenstilstand van 1953 geldt nog altijd; een echte vrede is er niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een stellingenoorlog langs bondgenoten, zoals in Korea en Vietnam?",
        opties=[
            "de grootmachten steunen elk een kant zonder zelf te verklaren",
            "de grootmachten vechten rechtstreeks op hun eigen gebied",
            "de grootmachten laten de Verenigde Naties de oorlog voeren",
            "de grootmachten sluiten vrede en geven hun wapens af",
        ],
        antwoord=0,
        uitleg="Men noemt dat ook een proxyoorlog. De slachtoffers vielen ver van Washington en Moskou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in oktober 1962 tijdens de Cubacrisis?",
        opties=[
            "de Sovjet-Unie plaatste raketten op Cuba",
            "de Verenigde Staten vielen Cuba binnen en bezetten het eiland",
            "Cuba verklaarde de Sovjet-Unie en de Verenigde Staten de oorlog",
            "Cuba werd lid van de NAVO en van de Verenigde Naties",
        ],
        antwoord=0,
        uitleg="Na dertien dagen werd een akkoord gevonden. Daarna kwam er een directe telefoonlijn tussen de leiders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1956 in Hongarije en in 1968 in Tsjechoslowakije?",
        opties=[
            "pogingen tot hervorming werden door sovjettroepen beëindigd",
            "beide landen verlieten het Warschaupact zonder gevolgen",
            "beide landen werden lid van de NAVO en van de EEG",
            "beide landen kregen van Moskou een eigen koers toegewezen",
        ],
        antwoord=0,
        uitleg="De Praagse Lente wilde socialisme met een menselijk gezicht. Tanks maakten er een einde aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de ontspanning of détente van de jaren zeventig?",
        opties=[
            "de twee blokken zochten afspraken over wapens en handel",
            "de twee blokken schaften hun bondgenootschappen af",
            "de twee blokken verklaarden elkaar openlijk de oorlog",
            "de twee blokken verbraken alle onderlinge betrekkingen",
        ],
        antwoord=0,
        uitleg="Er kwamen verdragen over kernwapens en de slotakte van Helsinki over grenzen en mensenrechten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de niet-gebonden landen?",
        opties=[
            "landen die bij geen van de twee blokken hoorden",
            "landen die tot beide blokken tegelijk wilden toetreden",
            "landen die geen lid van de Verenigde Naties waren",
            "landen die nog altijd door Europa bestuurd werden",
        ],
        antwoord=0,
        uitleg="Veel pas onafhankelijke staten kozen die weg, al werden ze door beide kampen het hof gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hervormingen voerde Gorbatsjov na 1985 in de Sovjet-Unie in?",
        opties=[
            "glasnost, meer openheid in het publieke leven",
            "perestrojka, een hervorming van de economie",
            "de afschaffing van de Verenigde Naties",
            "de oprichting van het Warschaupact",
        ],
        antwoord=[0, 1],
        uitleg="Hij wilde het stelsel redden door het te hervormen. Het is er juist aan uiteengevallen.",
    ),
    dict(
        type="invultekst",
        vraag="Wie was de laatste leider van de Sovjet-Unie, die glasnost en perestrojka invoerde?",
        antwoord=["Gorbatsjov", "Michail Gorbatsjov"],
        uitleg="Onder hem greep Moskou niet meer in toen het Oostblok in 1989 zijn eigen weg ging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in november 1989 in Berlijn?",
        opties=[
            "de Muur ging open naar het westen",
            "de Muur werd hoger gemaakt om de vlucht te stoppen",
            "de stad werd opnieuw in vier sectoren verdeeld",
            "de stad werd de hoofdstad van de Sovjet-Unie",
        ],
        antwoord=0,
        uitleg="Minder dan een jaar later was Duitsland weer één staat.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar viel de Berlijnse Muur?",
        antwoord=["1989"],
        uitleg="Datzelfde jaar wisselden de regimes in heel Oost-Europa, in de meeste landen zonder bloedvergieten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1991 met de Sovjet-Unie?",
        opties=[
            "zij viel uiteen in vijftien onafhankelijke staten",
            "zij veranderde haar naam in Russische Federatie",
            "zij trad toe tot de NAVO en de Europese Unie",
            "zij bezette opnieuw de landen van Oost-Europa",
        ],
        antwoord=0,
        uitleg="Rusland werd de grootste opvolger. De Koude Oorlog was daarmee ten einde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen had het einde van de Koude Oorlog voor Europa?",
        opties=[
            "Duitsland werd opnieuw één staat",
            "landen uit het Oostblok sloten later bij de Europese Unie aan",
            "het ijzeren gordijn werd nog dertig jaar langer gehandhaafd",
            "het Warschaupact werd uitgebreid met westerse landen",
        ],
        antwoord=[0, 1],
        uitleg="Het Warschaupact verdween juist. De uitbreiding van de Europese Unie naar het oosten volgde na 2004.",
    ),
    dict(
        type="waarofniet",
        vraag="De Cubacrisis van 1962 bracht de wereld dicht bij een kernoorlog.",
        antwoord=True,
        uitleg="Raketten op negentig mijl van de Amerikaanse kust lieten geen van beide leiders veel ruimte.",
    ),
    dict(
        type="waarofniet",
        vraag="De Sovjet-Unie liet de landen van het Oostblok in 1956 en 1968 vrij hun eigen koers kiezen.",
        antwoord=False,
        uitleg="In Hongarije en in Tsjechoslowakije zijn de hervormingen met tanks beëindigd.",
    ),
    dict(
        type="waarofniet",
        vraag="De détente van de jaren zeventig bracht verdragen over kernwapens.",
        antwoord=True,
        uitleg="Ook de slotakte van Helsinki hoort daarbij, waarin de mensenrechten mee werden ingeschreven.",
    ),
    dict(
        type="waarofniet",
        vraag="De val van de Berlijnse Muur werd door de Sovjet-Unie met geweld beantwoord.",
        antwoord=False,
        uitleg="Moskou greep deze keer niet in. Juist daardoor konden de regimes vreedzaam wisselen.",
    ),
    dict(
        type="waarofniet",
        vraag="Na 1991 bleef de wereld in twee militaire blokken verdeeld zoals tijdens de Koude Oorlog.",
        antwoord=False,
        uitleg="Het Warschaupact verdween en de NAVO bleef. Men sprak toen van een wereld met één overheersende macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de Verenigde Naties kloppen?",
        opties=[
            "zij werden in 1945 opgericht na de Tweede Wereldoorlog",
            "haar Veiligheidsraad kan door een veto geblokkeerd worden",
            "zij namen de plaats in van de Europese Unie",
            "zij hebben geen enkele lidstaat uit Afrika of Azië",
        ],
        antwoord=[0, 1],
        uitleg="Bijna elke staat ter wereld is lid. Door de dekolonisatie is de Algemene Vergadering sterk gegroeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een Amerikaanse affiche uit 1950 waarop het communisme als een dreiging wordt getekend. Hoe lees je die?",
        opties=[
            "als propaganda die het eigen kamp moest verenigen",
            "als een objectieve beschrijving van de Sovjet-Unie",
            "als een bron over het dagelijks leven in Moskou",
            "als een officieel document van de Verenigde Naties",
        ],
        antwoord=0,
        uitleg="Beide kampen hebben zo gewerkt. Een affiche vertelt je over de vijandbeelden van haar eigen kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen de Tweede Wereldoorlog en de Koude Oorlog?",
        opties=[
            "de twee overwinnaars werden na 1945 rivalen om Europa",
            "de twee oorlogen hebben niets met elkaar te maken",
            "de Koude Oorlog begon al voor de Tweede Wereldoorlog",
            "de Koude Oorlog werd in Jalta met een verdrag beëindigd",
        ],
        antwoord=0,
        uitleg="In 1945 stonden hun legers in het midden van Europa. Waar zij stopten, kwam de scheidingslijn te liggen.",
    ),
]
