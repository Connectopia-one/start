# -*- coding: utf-8 -*-
"""Het bbp, economische groei en welvaartsindicatoren.

Fiche: begrip bbp; drie berekeningswijzen (bestedings-, inkomens- en
productiebenadering); bruto en netto toegevoegde waarde; bijdrage aan het
bbp via de bedrijfskolom; bbp tegen factorprijzen en marktprijzen; nominaal
en reëel bbp; bbp, bnp en nationaal inkomen; statistieken van de NBB; bbp
per capita als welvaartsindicator en zijn tekortkomingen; innovatie als
motor en als disruptieve factor; HDI, BNG, SDG Dashboard en SDG Index, MEW,
Better Life Index.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het bruto binnenlands product (bbp)?",
        opties=[
            "de waarde van alle finale goederen en diensten die een jaar lang in een land gemaakt worden",
            "de waarde van alle goederen die een land in een jaar uitvoert naar het buitenland",
            "het totale inkomen van alle inwoners van een land, ook als ze in het buitenland werken",
            "de waarde van alle goederen en diensten die gezinnen in een jaar kopen in een land",
        ],
        antwoord=0,
        uitleg="Binnenlands: op het grondgebied. Finaal: tussenproducten tellen niet apart mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de drie berekeningswijzen van het bbp?",
        opties=[
            "de bestedingsbenadering, de inkomensbenadering en de productiebenadering",
            "de vraagbenadering, de aanbodbenadering en de evenwichtsbenadering",
            "de nominale, de reële en de potentiële benadering",
            "de gezinsbenadering, de bedrijfsbenadering en de overheidsbenadering",
        ],
        antwoord=0,
        uitleg="Ze geven in principe hetzelfde resultaat, want elke productie levert inkomen op en wordt besteed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij de bestedingsbenadering?",
        opties=["bbp = C + I + G + (X − M)", "bbp = lonen + winsten + rente + huur", "bbp = som van de toegevoegde waarden", "bbp = T + C + S"],
        antwoord=0,
        uitleg="Je telt op wat gezinnen, bedrijven, overheid en buitenland besteden aan de binnenlandse productie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat tel je op bij de inkomensbenadering?",
        opties=[
            "de lonen, interesten, huren en winsten",
            "de uitgaven van gezinnen, bedrijven, overheid en buitenland",
            "de toegevoegde waarde van elke schakel in de bedrijfskolom",
            "de export min de import van goederen en diensten",
        ],
        antwoord=0,
        uitleg="Wat geproduceerd wordt, wordt als inkomen verdeeld over wie meewerkte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat tel je op bij de productiebenadering?",
        opties=[
            "de toegevoegde waarde van alle bedrijven",
            "de omzet van alle bedrijven",
            "de lonen van alle werknemers",
            "de aankopen van alle gezinnen",
        ],
        antwoord=0,
        uitleg="Wie de omzet optelt, telt grondstoffen en tussenproducten meer dan één keer.",
    ),
    dict(
        type="invultekst",
        vraag="Een bakker verkoopt brood voor 50 000 euro en kocht voor 20 000 euro bloem en andere grondstoffen. Hoeveel is zijn bruto toegevoegde waarde in euro?",
        antwoord=["30000", "30 000", "30.000"],
        uitleg="Bruto toegevoegde waarde = omzet − aankopen van grondstoffen en diensten = 30 000.",
    ),
    dict(
        type="invultekst",
        vraag="Die bakker heeft 5 000 euro afschrijvingen op zijn oven. Hoeveel is zijn netto toegevoegde waarde in euro?",
        antwoord=["25000", "25 000", "25.000"],
        uitleg="Netto = bruto − afschrijvingen = 30 000 − 5 000.",
    ),
    dict(
        type="waarofniet",
        vraag="Het verschil tussen bruto en netto toegevoegde waarde zijn de afschrijvingen.",
        antwoord=True,
        uitleg="Afschrijvingen zijn de slijtage van kapitaalgoederen zoals machines en gebouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bedrijfskolom van een houten tafel: de boswachter verkoopt hout voor 100, de zagerij planken voor 250, de meubelmaker de tafel voor 600. Hoeveel draagt deze kolom bij aan het bbp?",
        opties=["600", "950", "350", "250"],
        antwoord=0,
        uitleg="100 + 150 + 350 = 600: de som van de toegevoegde waarden is de prijs van het eindproduct.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je in de bedrijfskolom de omzet van elke schakel optelt, vind je de bijdrage aan het bbp.",
        antwoord=False,
        uitleg="Dan tel je het hout en de planken dubbel. Je telt de toegevoegde waarden op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je van het bbp tegen factorprijzen naar het bbp tegen marktprijzen?",
        opties=[
            "indirecte belastingen erbij tellen en subsidies aftrekken",
            "afschrijvingen erbij tellen en belastingen aftrekken",
            "de inflatie eraf halen",
            "de inkomens uit het buitenland erbij tellen",
        ],
        antwoord=0,
        uitleg="Marktprijzen bevatten btw en accijnzen, en worden verlaagd door subsidies.",
    ),
    dict(
        type="invultekst",
        vraag="Bbp tegen factorprijzen = 480, indirecte belastingen = 70, subsidies = 10. Hoeveel is het bbp tegen marktprijzen?",
        antwoord=["540"],
        uitleg="480 + 70 − 10 = 540.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het reëel bbp?",
        opties=[
            "het bbp in constante prijzen",
            "het bbp in lopende prijzen van het jaar zelf",
            "het bbp zonder de productie van de overheid",
            "het bbp na aftrek van de afschrijvingen",
        ],
        antwoord=0,
        uitleg="Zo zie je of er echt meer geproduceerd werd, en niet alleen duurder.",
    ),
    dict(
        type="waarofniet",
        vraag="Het nominaal bbp stijgt enkel als er meer geproduceerd wordt.",
        antwoord=False,
        uitleg="Als de prijzen stijgen, stijgt het bbp in lopende prijzen ook zonder extra productie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het nominaal bbp steeg met 5 %, de prijzen met 3 %. Hoeveel groeide het reëel bbp ongeveer?",
        opties=["ongeveer 2 %", "ongeveer 8 %", "ongeveer 5 %", "ongeveer 3 %"],
        antwoord=0,
        uitleg="Reële groei ≈ nominale groei − inflatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat telt het bnp wel en het bbp niet?",
        opties=[
            "inkomens die inwoners verdienen in het buitenland",
            "de productie van buitenlandse bedrijven in België",
            "de productie van de overheid",
            "de export van goederen",
        ],
        antwoord=0,
        uitleg="Bnp is nationaal: het telt inkomens van inwoners, waar ze ook verdiend worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule klopt?",
        opties=[
            "bnp = bbp + primaire inkomens uit het buitenland − primaire inkomens naar het buitenland",
            "bnp = bbp + export − import van goederen en diensten",
            "bnp = bbp − afschrijvingen − indirecte belastingen + subsidies",
            "bnp = bbp + uitkeringen − belastingen van de gezinnen",
        ],
        antwoord=0,
        uitleg="Primaire inkomens zijn lonen, interesten, dividenden en huren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Nederlander die in Antwerpen werkt, draagt bij aan het Belgische bbp.",
        antwoord=True,
        uitleg="Het werk gebeurt in België. Zijn loon telt wel mee voor het Nederlandse bnp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitgaven tellen mee in de bestedingsbenadering? Duid alle juiste antwoorden aan.",
        opties=[
            "een gezin koopt een nieuwe fiets",
            "een bedrijf koopt een nieuwe machine",
            "de overheid betaalt een kinderbijslag",
            "een gezin koopt een tweedehandse auto van een ander gezin",
        ],
        antwoord=[0, 1],
        uitleg="Kinderbijslag is een overdracht, geen besteding aan productie. Een tweedehandse auto werd vroeger al geteld.",
    ),
    dict(
        type="waarofniet",
        vraag="De Nationale Bank van België publiceert de officiële cijfers over het Belgische bbp.",
        antwoord=True,
        uitleg="Via haar statistiekenportaal stat.nbb.be.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men het bbp per capita en niet het totale bbp om welvaart te vergelijken?",
        opties=[
            "omdat landen verschillend veel inwoners hebben",
            "omdat het totale bbp niet nauwkeurig berekend kan worden",
            "omdat het bbp per capita de inflatie wegneemt",
            "omdat het totale bbp enkel de export meet",
        ],
        antwoord=0,
        uitleg="Een groot land heeft een groot bbp, maar daarom niet meer welvaart per inwoner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn tekortkomingen van het bbp per capita als welvaartsindicator? Duid alle juiste antwoorden aan.",
        opties=[
            "het zegt niets over hoe het inkomen verdeeld is",
            "onbetaald werk zoals vrijwilligerswerk telt niet mee",
            "het meet de productie op het grondgebied",
            "het houdt rekening met het aantal inwoners",
        ],
        antwoord=[0, 1],
        uitleg="Ook milieuschade, vrije tijd en de zwarte economie blijven buiten beeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Het opruimen na een overstroming doet het bbp stijgen.",
        antwoord=True,
        uitleg="Herstelwerk is productie. Toch is het land er niet welvarender door: dat is een tekortkoming van het bbp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie onderdelen meet de HDI (Human Development Index)?",
        opties=[
            "levensverwachting, onderwijs en inkomen per inwoner",
            "geluk, vrije tijd en gezondheid van de inwoners, via een grote enquête",
            "export, import en werkloosheid",
            "milieu, veiligheid en woonkwaliteit",
        ],
        antwoord=0,
        uitleg="De HDI van de Verenigde Naties ligt tussen 0 en 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk land werd bekend met de indicator Bruto Nationaal Geluk (BNG)?",
        opties=["Bhutan", "Noorwegen", "Japan", "Nieuw-Zeeland"],
        antwoord=0,
        uitleg="Bhutan meet welzijn naast welvaart, met onder meer cultuur, natuur en goed bestuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de MEW (Measure of Economic Welfare)?",
        opties=[
            "ze past het bbp aan voor vrije tijd, onbetaald werk en schade",
            "het geluk van de inwoners meten met een enquête",
            "de vooruitgang op de 17 SDG's per land en per jaar in kaart brengen",
            "de levensverwachting en het onderwijsniveau combineren",
        ],
        antwoord=0,
        uitleg="De MEW vertrekt van het bbp en corrigeert het.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is eigen aan de Better Life Index van de OESO?",
        opties=[
            "je kiest zelf hoe zwaar elk onderdeel doorweegt",
            "hij meet enkel het bbp per inwoner",
            "hij geldt enkel voor ontwikkelingslanden",
            "hij wordt berekend uit het aantal patenten in een land",
        ],
        antwoord=0,
        uitleg="De index bundelt elf domeinen van welzijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat tonen het SDG Dashboard en de SDG Index?",
        opties=[
            "hoe ver een land staat met het halen van de duurzame ontwikkelingsdoelen",
            "hoeveel een land elk jaar uitgeeft aan ontwikkelingshulp en noodhulp in het buitenland",
            "de groei van het reëel bbp per kwartaal",
            "de evolutie van de beurskoersen in een land",
        ],
        antwoord=0,
        uitleg="Het dashboard kleurt per doel: groen gehaald, rood nog ver weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Welvaart en welzijn betekenen in de economie hetzelfde.",
        antwoord=False,
        uitleg="Welvaart gaat over de materiële middelen, welzijn ook over gezondheid, geluk en relaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke indicatoren meten meer dan alleen materiële welvaart? Duid alle juiste antwoorden aan.",
        opties=["de HDI", "het BNG", "het nominaal bbp", "de omzet van de bedrijven"],
        antwoord=[0, 1],
        uitleg="Het bbp en de omzet meten enkel productie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet innovatie een motor van economische groei?",
        opties=[
            "nieuwe technieken laten toe met dezelfde middelen meer of betere producten te maken",
            "innovatie verhoogt automatisch de prijzen en dus het nominaal bbp",
            "innovatie zorgt ervoor dat er minder belastingen betaald moeten worden",
            "innovatie vermindert de export en dus de afhankelijkheid van het buitenland",
        ],
        antwoord=0,
        uitleg="Hogere productiviteit is de belangrijkste bron van groei op lange termijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met innovatie als disruptieve factor?",
        opties=[
            "een vernieuwing die bestaande bedrijven of beroepen overbodig maakt",
            "een vernieuwing die de productie tijdelijk stillegt voor onderhoud",
            "een vernieuwing die enkel in laboratoria gebruikt wordt",
            "een vernieuwing die de overheid verplicht voor alle bedrijven",
        ],
        antwoord=0,
        uitleg="Denk aan streamingdiensten tegenover videotheken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoger bbp per capita betekent altijd dat de meeste inwoners er beter aan toe zijn.",
        antwoord=False,
        uitleg="Als een kleine groep de groei opstrijkt, merkt de meerderheid er weinig van.",
    ),
    dict(
        type="invultekst",
        vraag="Een land heeft een bbp van 600 miljard euro en 12 miljoen inwoners. Hoeveel is het bbp per capita in euro?",
        antwoord=["50000", "50 000", "50.000"],
        uitleg="600 000 000 000 / 12 000 000 = 50 000.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het nationaal inkomen?",
        opties=[
            "het netto nationaal product tegen factorkosten",
            "het bbp tegen marktprijzen, met de btw en de accijnzen erin",
            "het totale bedrag van de belastingen die de overheid in een jaar ontvangt",
            "de som van alle lonen in een land, zonder de winsten van de bedrijven",
        ],
        antwoord=0,
        uitleg="Bnp − afschrijvingen − indirecte belastingen + subsidies.",
    ),
    dict(
        type="waarofniet",
        vraag="De HDI kan hoog zijn in een land met een gemiddeld bbp per capita, als levensverwachting en onderwijs goed scoren.",
        antwoord=True,
        uitleg="Inkomen is maar een van de drie onderdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een jaar heeft een nominaal bbp van 520 miljard. Hoe ga je na of de economie echt groeide tegenover vorig jaar?",
        opties=[
            "je vergelijkt het reëel bbp van beide jaren",
            "je vergelijkt de nominale bbp's zonder meer",
            "je kijkt hoeveel belastingen de overheid ontving",
            "je deelt het bbp door de werkloosheidsgraad",
        ],
        antwoord=0,
        uitleg="Enkel in constante prijzen zie je de echte toename van de productie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bbp tegen marktprijzen is meestal groter dan het bbp tegen factorprijzen.",
        antwoord=True,
        uitleg="Er komen indirecte belastingen bij, en die zijn meestal groter dan de subsidies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke activiteit telt niet mee in het bbp?",
        opties=[
            "een ouder die thuis voor de kinderen zorgt",
            "een kinderdagverblijf dat kinderen opvangt",
            "een school die les geeft",
            "een kapper die haar knipt",
        ],
        antwoord=0,
        uitleg="Onbetaald werk heeft geen marktprijs en verschijnt niet in het bbp.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bbp per capita houdt rekening met de schade aan het milieu.",
        antwoord=False,
        uitleg="Vervuiling wordt niet afgetrokken. Soms doet ze het bbp zelfs stijgen, via opruimwerk.",
    ),
]
