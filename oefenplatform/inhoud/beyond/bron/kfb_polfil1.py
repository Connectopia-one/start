# -*- coding: utf-8 -*-
"""Politieke filosofie: individu, gemeenschap en legitimiteit.

Thema filosofie dat enkel in kunstbeschouwing en filosofie (fiche 3DDO)
staat:

    individu of gemeenschap: het belang van individu of gemeenschap in een
    voorbeeld en in het politiek debat; de ideologieën egalitair liberalisme,
    liberalisme, socialisme en communitarisme, met grondlegger, tijd en
    ruimte; de visies van John Locke en Jean-Jacques Rousseau
    legitimiteit van de macht: het begrip, en de visies van Aristoteles,
    Thomas Hobbes en Carl Schmitt, geplaatst in tijd en ruimte

Grondleggers zoals in de gangbare handboeken: John Locke voor het
liberalisme, Karl Marx (met Friedrich Engels) voor het socialisme, John Rawls
voor het egalitair liberalisme, en Michael Sandel, Charles Taylor en
Alasdair MacIntyre voor het communitarisme.

Deel 1: individu of gemeenschap. Deel 2: legitimiteit van de macht.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat centraal in het klassieke liberalisme?",
        opties=[
            "de vrijheid en de rechten van het individu",
            "de gemeenschap en haar gedeelde tradities",
            "het gemeenschappelijk bezit van de fabrieken",
            "de absolute macht van één sterke vorst",
        ],
        antwoord=0,
        uitleg="Het liberalisme beschermt het individu tegen een te sterke staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie geldt als grondlegger van het liberalisme?",
        opties=["John Locke", "Karl Marx", "Michael Sandel", "Carl Schmitt"],
        antwoord=0,
        uitleg="Locke schreef in de 17de eeuw in Engeland over natuurlijke rechten: leven, vrijheid en eigendom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wil het socialisme vooral bereiken?",
        opties=[
            "meer gelijkheid, door de ongelijkheid tussen klassen weg te werken",
            "zo weinig mogelijk staat, zodat elk individu vrij kan ondernemen",
            "een terugkeer naar de oude tradities van een gemeenschap",
            "een staat geleid door één leider die beslist wie de vijand is",
        ],
        antwoord=0,
        uitleg="Het socialisme ontstond in de 19de eeuw, tijdens de industriële revolutie, met Karl Marx als belangrijkste denker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor het egalitair liberalisme van John Rawls?",
        opties=[
            "het verdedigt vrijheid, maar ook een eerlijke verdeling van kansen",
            "het wil alle eigendom afschaffen en de staat helemaal laten verdwijnen",
            "het vindt dat de gemeenschap altijd boven elke vrijheid gaat",
            "het vindt dat de staat zich nooit met armoede mag bemoeien",
        ],
        antwoord=0,
        uitleg="Rawls schreef in 1971 in de Verenigde Staten A Theory of Justice.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kritiek geeft het communitarisme op het liberalisme?",
        opties=[
            "het individu is geen los wezen, zijn gemeenschap vormt hem",
            "het liberalisme geeft het individu veel te weinig vrijheid",
            "het liberalisme besteedt veel te veel aandacht aan oude tradities",
            "het liberalisme wil alle eigendom gelijk verdelen over de burgers",
        ],
        antwoord=0,
        uitleg="Communitaristen zoals Sandel, Taylor en MacIntyre benadrukken gedeelde waarden en tradities.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke denkers horen bij het communitarisme?",
        opties=["Michael Sandel", "Charles Taylor", "John Locke", "Karl Marx"],
        antwoord=[0, 1],
        uitleg="Het communitarisme ontstond in de jaren 1980, vooral in Noord-Amerika, als reactie op Rawls.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet John Locke de mens in de natuurtoestand, vóór er een staat is?",
        opties=[
            "vrij en gelijk, met natuurlijke rechten op leven, vrijheid en eigendom",
            "in een oorlog van allen tegen allen, zonder enige rechten",
            "goed en vrij, maar later bedorven door het bezit en de samenleving",
            "zonder rede, enkel geleid door angst en de wil om te overleven",
        ],
        antwoord=0,
        uitleg="De staat moet volgens Locke die rechten beschermen. Doet hij dat niet, dan mag het volk in verzet komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Rousseau met de algemene wil?",
        opties=[
            "de wil van de burgers samen, gericht op het algemeen belang",
            "de optelsom van alle eigenbelangen van de burgers",
            "de wil van de koning, die voor iedereen beslist",
            "de wil van de rijkste burgers, die het meeste belasting betalen",
        ],
        antwoord=0,
        uitleg="Voor Rousseau is de algemene wil meer dan de som van de eigenbelangen: het is wat goed is voor iedereen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een belangrijk verschil tussen Locke en Rousseau?",
        opties=[
            "Locke benadrukt het individu, Rousseau de gemeenschap en de algemene wil",
            "Locke legt de nadruk op de gemeenschap, Rousseau op het eigendom van elk individu",
            "Locke wil een absolute vorst, Rousseau wil helemaal geen staat of wetten",
            "Locke en Rousseau verschillen niet, ze verdedigen allebei de absolute vorst",
        ],
        antwoord=0,
        uitleg="Locke staat aan de basis van het liberalisme, Rousseau legt meer nadruk op de gemeenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad wil een park omvormen tot parking. Buurtbewoners vinden het park belangrijk voor de buurt, een winkelier wil meer klanten. Welke spanning zie je hier?",
        opties=[
            "tussen eigenbelang en het belang van de gemeenschap",
            "tussen schijn en werkelijkheid in wat de buurt waarneemt",
            "tussen worden en zijn van het park in de loop der jaren",
            "tussen deugdethiek en zorgethiek bij de bewoners",
        ],
        antwoord=0,
        uitleg="In het politiek debat botsen het eigen belang en het gedeelde belang vaak.",
    ),
    dict(
        type="invultekst",
        vraag="De ideologie die vindt dat het individu gevormd wordt door zijn gemeenschap, heet het ...",
        antwoord=["communitarisme"],
        uitleg="Communitaristen plaatsen de gemeenschap en haar waarden centraal.",
    ),
    dict(
        type="invultekst",
        vraag="De Duitse denker die in de 19de eeuw met Engels het Communistisch Manifest schreef, heet Karl ...",
        antwoord=["Marx"],
        uitleg="Het manifest verscheen in 1848.",
    ),
    dict(
        type="waarofniet",
        vraag="Het socialisme ontstond als reactie op de harde omstandigheden van arbeiders tijdens de industriële revolutie.",
        antwoord=True,
        uitleg="Lange werkdagen, kinderarbeid en armoede leidden tot de vraag naar meer gelijkheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Het communitarisme ontstond al in de oudheid, lang voor het liberalisme.",
        antwoord=False,
        uitleg="Het communitarisme ontstond in de jaren 1980, als reactie op het liberalisme van Rawls.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Locke mag het volk in verzet komen als de regering de natuurlijke rechten schendt.",
        antwoord=True,
        uitleg="Het recht op verzet volgt uit het idee dat de staat er is om de rechten te beschermen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het klassieke liberalisme wil een staat die zich met zo veel mogelijk zaken van de burgers bemoeit.",
        antwoord=False,
        uitleg="Het klassieke liberalisme wil net een beperkte staat, die vooral de vrijheid beschermt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partij zegt: 'Iedereen moet vrij zijn, maar de sterkste schouders moeten de zwaarste lasten dragen, zodat ook wie arm geboren wordt, eerlijke kansen krijgt.' Bij welke ideologie past dit het best?",
        opties=["egalitair liberalisme", "klassiek liberalisme", "communitarisme", "absolutisme"],
        antwoord=0,
        uitleg="Vrijheid en eerlijke kansen samen: dat is het egalitair liberalisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: 'Een samenleving moet haar gedeelde waarden en tradities beschermen, want daar halen mensen hun identiteit uit.' Bij welke ideologie past dit het best?",
        opties=["communitarisme", "klassiek liberalisme", "socialisme", "egalitair liberalisme"],
        antwoord=0,
        uitleg="De nadruk op gemeenschap, tradities en identiteit past bij het communitarisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke volgorde ontstonden deze vier ideologieën?",
        opties=[
            "liberalisme (17de eeuw), socialisme (19de eeuw), egalitair liberalisme (1971), communitarisme (jaren 1980)",
            "socialisme (17de eeuw), liberalisme (19de eeuw), communitarisme (1971), egalitair liberalisme (jaren 1980)",
            "communitarisme (17de eeuw), egalitair liberalisme (19de eeuw), liberalisme (1971), socialisme (jaren 1980)",
            "egalitair liberalisme (17de eeuw), communitarisme (19de eeuw), socialisme (1971), liberalisme (jaren 1980)",
        ],
        antwoord=0,
        uitleg="Locke, dan Marx, dan Rawls, dan de communitaristen die op Rawls reageerden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zeggen communitaristen dat het individu bij Rawls 'los' staat?",
        opties=[
            "Rawls laat mensen kiezen zonder te weten tot welke gemeenschap ze horen",
            "Rawls wil dat iedereen alleen op een eiland gaat wonen, ver van de stad",
            "Rawls vindt dat mensen geen rechten mogen hebben tegenover de staat",
            "Rawls schreef enkel over dieren en machines, niet over mensen",
        ],
        antwoord=0,
        uitleg="Bij Rawls kiezen mensen principes achter een sluier van onwetendheid. Communitaristen vinden dat te abstract.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent politieke legitimiteit?",
        opties=[
            "de burgers zien de macht als terecht en aanvaardbaar",
            "de macht is in handen van de sterkste groep in het land",
            "de macht hoort altijd bij wie in het land het meeste geld heeft",
            "de macht ligt vast in de natuur en kan nooit veranderen",
        ],
        antwoord=0,
        uitleg="Een legitieme macht heeft gezag: mensen gehoorzamen niet enkel uit angst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vindt Thomas Hobbes een sterke staat nodig?",
        opties=[
            "zonder staat leven mensen in een oorlog van allen tegen allen",
            "mensen zijn van nature goed en hebben een staat nodig om te feesten",
            "de staat moet vooral de tradities van de kerk bewaren",
            "de staat moet het eigendom van iedereen gelijk verdelen",
        ],
        antwoord=0,
        uitleg="In de natuurtoestand is het leven volgens Hobbes eenzaam, arm, gemeen, wreed en kort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet het boek waarin Hobbes de sterke staat beschrijft, naar een zeemonster?",
        opties=["Leviathan", "De staat", "Politica", "Het sociaal contract"],
        antwoord=0,
        uitleg="Leviathan verscheen in 1651, in de tijd van de Engelse burgeroorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar haalt de macht volgens Hobbes haar legitimiteit?",
        opties=[
            "uit een contract: vrijheid afstaan aan een vorst voor veiligheid",
            "uit de wil van God, die de koning rechtstreeks gekozen heeft",
            "uit de deugd en de wijsheid van de beste en oudste burgers",
            "uit de beslissing over wie in een crisis vriend en wie vijand is",
        ],
        antwoord=0,
        uitleg="De macht is legitiem omdat ze vrede en veiligheid brengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een bestuur volgens Aristoteles goed en legitiem?",
        opties=[
            "wanneer het het algemeen belang dient, niet het eigenbelang",
            "wanneer het altijd door één koning uit dezelfde familie geleid wordt",
            "wanneer het door de rijkste families van de stad geleid wordt",
            "wanneer het snel en duidelijk de vijand van de stad kan aanwijzen",
        ],
        antwoord=0,
        uitleg="Aristoteles onderscheidt goede vormen (koningschap, aristocratie, politeia) en ontaarde vormen (tirannie, oligarchie, democratie in slechte zin).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is voor Carl Schmitt de kern van het politieke?",
        opties=[
            "het onderscheid tussen vriend en vijand",
            "het onderscheid tussen goed en kwaad",
            "het onderscheid tussen mooi en lelijk",
            "het onderscheid tussen arm en rijk",
        ],
        antwoord=0,
        uitleg="Schmitt was een Duitse rechtsgeleerde uit de 20ste eeuw. Hij werkte ook mee met het naziregime.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie is volgens Carl Schmitt de soeverein?",
        opties=[
            "wie beslist over de uitzonderingstoestand",
            "wie de meeste stemmen haalt",
            "wie het oudste lid van het parlement is",
            "wie de grondwet heeft geschreven",
        ],
        antwoord=0,
        uitleg="Voor Schmitt toont de echte macht zich in crisis: wie dan beslist, heeft de soevereiniteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over Hobbes en Schmitt kloppen?",
        opties=[
            "allebei geven ze een sterke staat veel macht",
            "allebei leggen ze de nadruk op orde en veiligheid",
            "allebei vinden ze dat de burgers het algemeen belang moeten dienen via deugd",
            "allebei leefden ze in de klassieke oudheid",
        ],
        antwoord=[0, 1],
        uitleg="Het algemeen belang via deugd past bij Aristoteles. Hobbes leefde in de 17de, Schmitt in de 20ste eeuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verschil tussen Aristoteles en Hobbes klopt?",
        opties=[
            "Aristoteles: de mens is sociaal; Hobbes: de mens beschermt vooral zichzelf",
            "Aristoteles ziet de mens als egoïst, Hobbes als een van nature politiek wezen",
            "Aristoteles wil een absolute vorst, Hobbes wil helemaal geen staat meer",
            "Aristoteles leefde in de 20ste eeuw in Duitsland, Hobbes in de oudheid",
        ],
        antwoord=0,
        uitleg="Voor Aristoteles is de mens een zoön politikon, een politiek dier. Voor Hobbes is de staat een kunstmatig contract.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke situatie toont een gebrek aan legitimiteit?",
        opties=[
            "een leger neemt de macht en burgers gehoorzamen uit angst",
            "een parlement wordt na eerlijke verkiezingen samengesteld",
            "een regering legt verantwoording af aan het parlement",
            "een rechter beslist volgens de wet over een conflict",
        ],
        antwoord=0,
        uitleg="Macht door geweld zonder aanvaarding is wel macht, maar geen legitieme macht.",
    ),
    dict(
        type="invultekst",
        vraag="Hobbes noemt de toestand zonder staat de oorlog van allen tegen ...",
        antwoord=["allen"],
        uitleg="In het Latijn: bellum omnium contra omnes.",
    ),
    dict(
        type="invultekst",
        vraag="Aristoteles noemt de mens een zoön politikon, een ... dier.",
        antwoord=["politiek", "sociaal"],
        uitleg="De mens leeft van nature in een gemeenschap, de polis.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor Hobbes is de macht van de vorst legitiem zolang hij vrede en veiligheid brengt.",
        antwoord=True,
        uitleg="Veiligheid is het doel van het contract.",
    ),
    dict(
        type="waarofniet",
        vraag="Carl Schmitt leefde in het oude Griekenland, net als Aristoteles.",
        antwoord=False,
        uitleg="Schmitt leefde van 1888 tot 1985 in Duitsland. Aristoteles leefde in de 4de eeuw voor Christus.",
    ),
    dict(
        type="waarofniet",
        vraag="Een macht die mensen enkel met geweld doet gehoorzamen, is volgens de meeste filosofen niet legitiem.",
        antwoord=True,
        uitleg="Legitimiteit vraagt aanvaarding of een goede grond, niet alleen dwang.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor Aristoteles is elk bestuur van één persoon automatisch slecht.",
        antwoord=False,
        uitleg="Koningschap is voor hem een goede vorm, zolang de koning het algemeen belang dient. Tirannie is de slechte vorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een regering roept een noodtoestand uit en schort enkele rechten op. Iemand zegt: 'Nu zie je wie echt de macht heeft.' Bij welke denker past dit?",
        opties=["Carl Schmitt", "Aristoteles", "John Locke", "Jean-Jacques Rousseau"],
        antwoord=0,
        uitleg="Voor Schmitt toont de uitzonderingstoestand wie de soeverein is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: 'Ik geef liever een deel van mijn vrijheid op aan een sterke staat, dan dat ik elke dag bang moet zijn voor mijn leven.' Bij welke denker past dit?",
        opties=["Thomas Hobbes", "Carl Schmitt", "Aristoteles", "Michael Sandel"],
        antwoord=0,
        uitleg="Vrijheid ruilen voor veiligheid is het sociaal contract van Hobbes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke plaatsing in tijd en ruimte klopt?",
        opties=[
            "Aristoteles: oud-Griekenland; Hobbes: Engeland, 17de eeuw; Schmitt: Duitsland, 20ste eeuw",
            "Aristoteles: Engeland, 17de eeuw; Hobbes: Duitsland, 20ste eeuw; Schmitt: oud-Griekenland",
            "Aristoteles: Duitsland, 20ste eeuw; Hobbes: oud-Griekenland; Schmitt: Engeland, 17de eeuw",
            "Aristoteles: oud-Griekenland; Hobbes: Duitsland, 20ste eeuw; Schmitt: Engeland, 17de eeuw",
        ],
        antwoord=0,
        uitleg="Aristoteles in de 4de eeuw voor Christus, Hobbes ten tijde van de Engelse burgeroorlog, Schmitt in Duitsland in de 20ste eeuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is legitimiteit belangrijk voor een stabiele samenleving?",
        opties=[
            "als burgers de macht aanvaarden, volgen ze de regels ook zonder dwang",
            "omdat een legitieme regering nooit belastingen hoeft te heffen",
            "omdat een legitieme regering geen wetten meer moet maken",
            "omdat legitimiteit betekent dat er nooit verkiezingen nodig zijn",
        ],
        antwoord=0,
        uitleg="Zonder legitimiteit moet een macht steeds meer geweld gebruiken om te blijven bestaan.",
    ),
]
