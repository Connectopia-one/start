# -*- coding: utf-8 -*-
"""Veilig werken, meetinstrumenten en beduidende cijfers — 🌍 Beyond, chemie.

Deel 1 gaat over veilig werken in het labo: de H-zinnen en P-zinnen op een
etiket, waar de gevarenpictogrammen voor staan, welk glaswerk je voor welke maat
gebruikt en wat het meetbereik van een instrument betekent. Deel 2 gaat over het
rekenen met meetresultaten: de SI-eenheden, de voorvoegsels van mega tot nano,
beduidende cijfers, de wetenschappelijke notatie en het verschil tussen recht en
omgekeerd evenredig.

De pictogrammen worden in woorden beschreven: een vlam, een doodshoofd, een hand
waar een druppel een gat in bijt. Zo blijft elke vraag leesbaar zonder tekening.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarover gaat een H-zin op een etiket?",
        opties=[
            "over het gevaar dat de stof zelf oplevert",
            "over de voorzorg die je moet nemen",
            "over de hoeveelheid die in de fles zit",
            "over de houdbaarheid van het product",
        ],
        antwoord=0,
        uitleg="De H komt van hazard, dus gevaar. De P-zinnen ernaast zeggen wat je er "
        "tegen doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover gaat een P-zin op een etiket?",
        opties=[
            "over de voorzorg en wat je bij een ongeval doet",
            "over het gevaar dat de stof zelf oplevert",
            "over de prijs en de herkomst van het product",
            "over de plaats waar de stof gemaakt werd",
        ],
        antwoord=0,
        uitleg="De P komt van precaution. Zo'n zin zegt bijvoorbeeld dat je een "
        "veiligheidsbril draagt of de huid grondig spoelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een pictogram toont een hand en een oppervlak waar een druppel een gat in bijt. Wat betekent het?",
        opties=[
            "de stof is bijtend voor huid en materiaal",
            "de stof is licht ontvlambaar in de open lucht",
            "de stof is giftig bij het inslikken ervan",
            "de stof is schadelijk voor het waterleven",
        ],
        antwoord=0,
        uitleg="Dat is het pictogram voor corrosief. Daarom hoort er een bril en "
        "handschoenen bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een pictogram toont een doodshoofd met twee gekruiste beenderen. Wat betekent het?",
        opties=[
            "de stof is giftig, ook in een kleine hoeveelheid",
            "de stof is bijtend voor huid en voor materiaal",
            "de stof kan ontploffen bij een harde schok",
            "de stof is schadelijk voor dieren in het water",
        ],
        antwoord=0,
        uitleg="Bij acute toxiciteit volstaat een kleine dosis. Een stof die enkel "
        "schadelijk is, krijgt het uitroepteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk glaswerk gebruik je om precies 250,0 mL oplossing te maken?",
        opties=[
            "een maatkolf van 250 mL",
            "een maatcilinder van 250 mL",
            "een bekerglas van 250 mL",
            "een erlenmeyer van 250 mL",
        ],
        antwoord=0,
        uitleg="Een maatkolf heeft één streepje en is daarvoor gekalibreerd. De "
        "streepjes op een bekerglas zijn maar een ruwe aanduiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk glaswerk is nauwkeurig genoeg voor een volume dat je in een berekening gebruikt? Kruis alles aan wat juist is.",
        opties=[
            "de maatkolf",
            "de volumetrische pipet",
            "het bekerglas",
            "de erlenmeyer",
        ],
        antwoord=[0, 1],
        uitleg="Een bekerglas en een erlenmeyer dienen om in te werken, niet om in te "
        "meten. Een maatcilinder zit ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af bij een buret?",
        opties=[
            "het volume dat eruit gelopen is",
            "het volume dat er nog in zit",
            "de massa van de vloeistof erin",
            "de concentratie van de oplossing",
        ],
        antwoord=0,
        uitleg="Daarom loopt de schaal van boven naar onder. Je noteert het begin en het "
        "einde en neemt het verschil.",
    ),
    dict(
        type="invultekst",
        vraag="Waar lees je het volume van een vloeistof in glaswerk af?",
        antwoord=["de meniscus", "meniscus", "onderkant meniscus"],
        uitleg="Je kijkt op ooghoogte naar de onderkant van die holle kromming. Van "
        "boven of onder kijken geeft een afleesfout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met het meetbereik van een instrument?",
        opties=[
            "de kleinste en de grootste waarde die het kan meten",
            "de kleinste stap die het nog kan onderscheiden",
            "de afwijking tussen de meting en de echte waarde",
            "het aantal metingen dat je ermee kan doen",
        ],
        antwoord=0,
        uitleg="Buiten dat bereik is de waarde onbetrouwbaar. De kleinste stap heet de "
        "resolutie of de schaalverdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom meet je 5 mL niet af in een maatcilinder van 500 mL?",
        opties=[
            "de streepjes staan daar veel te ver van elkaar",
            "de cilinder is te groot om goed vast te houden",
            "het glas van zo'n cilinder is veel te dik",
            "de vloeistof reageert anders in een grote cilinder",
        ],
        antwoord=0,
        uitleg="Een afleesfout van één streepje is daar al 5 mL. Kies altijd het "
        "instrument waarvan het bereik bij je volume past.",
    ),
    dict(
        type="waarofniet",
        vraag="Je spoelt een pipet eerst met de oplossing die je gaat pipetteren.",
        antwoord=True,
        uitleg="Water dat achterblijft, zou de oplossing verdunnen. Bij een maatkolf is "
        "het net omgekeerd: die mag wel nat zijn van water.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met het uitroeptekenpictogram is altijd dodelijk giftig.",
        antwoord=False,
        uitleg="Dat teken staat voor schadelijk of irriterend. Acuut giftig heeft het "
        "doodshoofd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuur verdun je door het zuur bij het water te gieten, niet omgekeerd.",
        antwoord=True,
        uitleg="Het verdunnen geeft veel warmte. Water bij geconcentreerd zuur kan "
        "spatten of koken.",
    ),
    dict(
        type="waarofniet",
        vraag="De gevarenpictogrammen zijn ronde groene tekens.",
        antwoord=False,
        uitleg="Ze zijn ruitvormig, met een rode rand en een wit vlak. Groene ronde "
        "tekens zijn gebodstekens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een veiligheidsfiche zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze vermeldt de H- en P-zinnen van de stof",
            "ze zegt wat je bij een ongeval moet doen",
            "ze vermeldt wie de stof gekocht heeft",
            "ze vervangt het etiket op de fles",
        ],
        antwoord=[0, 1],
        uitleg="Het etiket blijft nodig op de fles zelf. De fiche staat erbij voor wie "
        "meer wil weten over opslag, blussen en eerste hulp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een pictogram toont een boom en een dode vis. Wat betekent het?",
        opties=[
            "de stof is schadelijk voor het leven in het water",
            "de stof is giftig bij het inademen van de damp",
            "de stof tast de huid en de ogen zwaar aan",
            "de stof vat gemakkelijk vuur in open lucht",
        ],
        antwoord=0,
        uitleg="Daarom mag die stof nooit in de gootsteen. Zulk afval gaat in een aparte "
        "afvalfles.",
    ),
    dict(
        type="invultekst",
        vraag="Wat betekent de H in H-zin?",
        antwoord=["hazard", "gevaar", "hazard of gevaar"],
        uitleg="Het is het Engelse woord voor gevaar. De P van P-zin staat voor "
        "precaution, dus voorzorg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het veilig opruimen van een gemorst zuur? Kruis alles aan wat juist is.",
        opties=[
            "eerst neutraliseren met een zwakke base",
            "daarna opnemen en afvoeren bij het juiste afval",
            "eerst uitspoelen met een sterke base",
            "daarna gewoon in de gootsteen laten lopen",
        ],
        antwoord=[0, 1],
        uitleg="Een sterke base maakt er een tweede probleem van. Natriumwaterstofcarbonaat "
        "is zwak genoeg om veilig te blijven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kleinste stap die een meetinstrument kan onderscheiden?",
        antwoord=["de resolutie", "resolutie", "schaalverdeling"],
        uitleg="Het meetbereik is iets anders: dat zijn de kleinste en de grootste waarde "
        "die het instrument aankan.",
    ),
    dict(
        type="invultekst",
        vraag="Welk glaswerk gebruik je om een volume tot op honderdsten af te lezen bij een titratie?",
        antwoord=["een buret", "buret", "de buret"],
        uitleg="De schaal loopt van boven naar onder, want je leest af hoeveel eruit "
        "gelopen is. Een maatcilinder is daarvoor veel te grof.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van massa?",
        opties=[
            "de kilogram",
            "de gram",
            "de newton",
            "de mol",
        ],
        antwoord=0,
        uitleg="Het is de enige basiseenheid met een voorvoegsel erin. De mol is de "
        "eenheid van stofhoeveelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheden zijn SI-basiseenheden? Kruis alles aan wat juist is.",
        opties=[
            "de seconde",
            "de kelvin",
            "de liter",
            "de celsiusgraad",
        ],
        antwoord=[0, 1],
        uitleg="De liter is een afgeleide eenheid van volume en de celsiusgraad is geen "
        "basiseenheid. De zeven basiseenheden zijn meter, kilogram, seconde, ampère, "
        "kelvin, mol en candela.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke factor vermenigvuldigt het voorvoegsel mega?",
        opties=[
            "een miljoen",
            "een duizend",
            "een miljard",
            "een honderd",
        ],
        antwoord=0,
        uitleg="Mega is 10⁶, kilo is 10³ en giga is 10⁹. De voorvoegsels gaan telkens "
        "drie machten van tien verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorvoegsel staat voor 10⁻⁶?",
        opties=[
            "micro",
            "milli",
            "nano",
            "centi",
        ],
        antwoord=0,
        uitleg="Milli is 10⁻³ en nano is 10⁻⁹. Micro zit er precies tussen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel micrometer gaan er in één millimeter?",
        antwoord=["1000", "duizend", "1 000"],
        uitleg="Milli is 10⁻³ en micro is 10⁻⁶, dus er zitten drie machten van tien "
        "tussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel beduidende cijfers heeft 0,00450?",
        opties=[
            "drie",
            "twee",
            "vijf",
            "zes",
        ],
        antwoord=0,
        uitleg="De nullen vooraan dienen enkel om de komma te plaatsen. De nul achteraan "
        "telt wel mee: ze zegt dat er echt tot daar gemeten is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke getallen hebben drie beduidende cijfers? Kruis alles aan wat juist is.",
        opties=[
            "2,40",
            "0,00106",
            "0,0012",
            "12 000",
        ],
        antwoord=[0, 1],
        uitleg="0,0012 heeft er twee. Bij 12 000 weet je het niet: schrijf het als "
        "1,20·10⁴ als je er drie bedoelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vermenigvuldigt 2,5 met 3,142. Hoeveel beduidende cijfers heeft het antwoord?",
        opties=[
            "twee",
            "drie",
            "vier",
            "vijf",
        ],
        antwoord=0,
        uitleg="Bij vermenigvuldigen en delen volg je de factor met het minste aantal "
        "beduidende cijfers. Dus 7,9 en niet 7,855.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je telt 12,11 g en 0,2 g op. Hoe schrijf je het resultaat?",
        opties=[
            "12,3 g",
            "12,31 g",
            "12 g",
            "12,310 g",
        ],
        antwoord=0,
        uitleg="Bij optellen en aftrekken kijk je naar het aantal decimalen, niet naar "
        "het aantal beduidende cijfers. De minst nauwkeurige term heeft er één.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel beduidende cijfers heeft 1,0·10³?",
        antwoord=["2", "twee"],
        uitleg="De wetenschappelijke notatie maakt dat ondubbelzinnig: enkel de cijfers "
        "voor de macht tellen mee. Daarom schrijf je 1000 zo als je er twee bedoelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je 0,000 072 in wetenschappelijke notatie?",
        opties=[
            "7,2·10⁻⁵",
            "7,2·10⁻⁴",
            "72·10⁻⁶",
            "0,72·10⁻⁴",
        ],
        antwoord=0,
        uitleg="Er staat één cijfer voor de komma, van 1 tot 9. De komma schuift vijf "
        "plaatsen naar rechts, dus de exponent is min vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de wetenschappelijke notatie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er staat precies één cijfer voor de komma",
            "ze maakt het aantal beduidende cijfers duidelijk",
            "de exponent is altijd een positief getal",
            "ze mag enkel bij heel grote getallen gebruikt worden",
        ],
        antwoord=[0, 1],
        uitleg="Een negatieve exponent hoort bij een klein getal. Juist bij kleine "
        "getallen is de notatie het handigst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat twee grootheden recht evenredig zijn?",
        opties=[
            "als de ene verdubbelt, verdubbelt de andere ook",
            "als de ene verdubbelt, halveert de andere juist",
            "als de ene verdubbelt, blijft de andere gelijk",
            "als de ene verdubbelt, verviervoudigt de andere",
        ],
        antwoord=0,
        uitleg="Hun quotiënt blijft dan constant. In een grafiek geeft dat een rechte "
        "door de oorsprong.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat twee grootheden omgekeerd evenredig zijn?",
        opties=[
            "als de ene verdubbelt, halveert de andere",
            "als de ene verdubbelt, verdubbelt de andere",
            "als de ene verdubbelt, blijft de andere gelijk",
            "als de ene verdubbelt, verdrievoudigt de andere",
        ],
        antwoord=0,
        uitleg="Hun product blijft dan constant, zoals bij druk en volume van een gas. In "
        "een grafiek geeft dat een hyperbool.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte door de oorsprong in een grafiek wijst op recht evenredig.",
        antwoord=True,
        uitleg="Door de oorsprong is de voorwaarde: bij nul van de ene hoort nul van de "
        "andere. Een rechte die hoger begint, is wel lineair maar niet evenredig.",
    ),
    dict(
        type="waarofniet",
        vraag="Nullen vooraan een getal tellen mee als beduidend cijfer.",
        antwoord=False,
        uitleg="Ze plaatsen enkel de komma. In 0,0045 zijn er dus twee beduidende "
        "cijfers.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rekenmachine geeft vaak meer cijfers dan je mag opschrijven.",
        antwoord=True,
        uitleg="Het toestel weet niet hoe nauwkeurig je gemeten hebt. Jij rondt af op het "
        "aantal beduidende cijfers dat je metingen toelaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het optellen van meetwaarden volg je het aantal beduidende cijfers.",
        antwoord=False,
        uitleg="Bij optellen en aftrekken kijk je naar het aantal decimalen. Het aantal "
        "beduidende cijfers geldt bij vermenigvuldigen en delen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke eenheid krijg je als je massa in gram deelt door volume in milliliter?",
        antwoord=["g/mL", "gram per milliliter", "g per mL"],
        uitleg="Dat is de massadichtheid. In SI-eenheden zou dat kg/m³ zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verband waarbij het product van twee grootheden constant blijft?",
        antwoord=["omgekeerd evenredig", "omgekeerd", "inverse"],
        uitleg="Bij recht evenredig blijft juist het quotiënt constant. Druk en volume "
        "van een gas bij vaste temperatuur zijn omgekeerd evenredig.",
    ),
]
