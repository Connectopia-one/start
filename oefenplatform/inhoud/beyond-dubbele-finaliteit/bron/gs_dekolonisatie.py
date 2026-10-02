# -*- coding: utf-8 -*-
"""De dekolonisatie van Congo.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de dekolonisatie
na 1945 in het algemeen, en Congo in het bijzonder, van de eerste eisen over de
onafhankelijkheid van 1960 tot de nasleep in België van vandaag.

Deel 1 loopt tot 30 juni 1960. Deel 2 gaat over de crisis, over Mobutu en over
hoe er in België nu naar dit verleden gekeken wordt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent dekolonisatie?",
        opties=[
            "kolonies worden onafhankelijke staten",
            "staten veroveren nieuwe kolonies",
            "kolonies worden onder elkaar verdeeld",
            "kolonies worden door de Verenigde Naties bestuurd",
        ],
        antwoord=0,
        uitleg="Het grootste deel van Azië en Afrika werd tussen 1945 en 1975 onafhankelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oorzaken had de dekolonisatie na 1945?",
        opties=[
            "de Europese mogendheden waren door de oorlog verzwakt",
            "in de kolonies groeiden bewegingen die zelfbestuur eisten",
            "de Verenigde Naties verboden elke vorm van zelfbestuur",
            "de kolonies vroegen zelf om een langer Europees bestuur",
        ],
        antwoord=[0, 1],
        uitleg="Het handvest van de Verenigde Naties sprak juist van het zelfbeschikkingsrecht van volken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk jaar wordt het Afrikaanse jaar genoemd?",
        opties=[
            "1960",
            "1945",
            "1914",
            "1989",
        ],
        antwoord=0,
        uitleg="Een hele reeks Afrikaanse staten werd dat jaar onafhankelijk, Congo op 30 juni.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde de Koude Oorlog in de dekolonisatie?",
        opties=[
            "de twee blokken dongen naar de gunst van de nieuwe staten",
            "de twee blokken lieten de nieuwe staten volledig met rust",
            "de twee blokken verdeelden Afrika onder elkaar",
            "de twee blokken hielden de kolonies in Europese handen",
        ],
        antwoord=0,
        uitleg="Steun, wapens en leningen kwamen met verwachtingen. Veel staten raakten daardoor in conflicten verwikkeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe dacht men in België nog in de jaren vijftig over de onafhankelijkheid van Congo?",
        opties=[
            "dat ze nog tientallen jaren weg was",
            "dat ze binnen één jaar moest worden doorgevoerd",
            "dat ze nooit zou komen, want Congo bleef Belgisch",
            "dat de Verenigde Naties ze al hadden opgelegd",
        ],
        antwoord=0,
        uitleg="Een Belgische hoogleraar stelde in 1955 nog een plan van dertig jaar voor, en dat lag toen al gevoelig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie waren de eerste Congolese voormannen die zelfbestuur eisten?",
        opties=[
            "Joseph Kasavubu met zijn beweging in Leopoldstad",
            "Patrice Lumumba met zijn nationale beweging",
            "Mobutu Sese Seko met zijn eigen partij",
            "Leopold II met zijn Vrijstaat",
        ],
        antwoord=[0, 1],
        uitleg="Mobutu kwam later en langs het leger. Leopold II was de kolonisator zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in januari 1959 in Leopoldstad?",
        opties=[
            "er braken zware rellen uit tegen het koloniale bestuur",
            "de onafhankelijkheid van Congo werd er uitgeroepen",
            "de Ronde Tafelconferentie werd er geopend",
            "Mobutu nam er met het leger de macht over",
        ],
        antwoord=0,
        uitleg="Die rellen maakten in Brussel duidelijk dat uitstellen niet meer ging. Alles ging daarna heel snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat werd op de Ronde Tafelconferentie in Brussel in 1960 beslist?",
        opties=[
            "Congo zou op 30 juni van dat jaar onafhankelijk worden",
            "Congo zou over dertig jaar onafhankelijk worden",
            "Congo zou een provincie van België worden",
            "Congo zou door de Verenigde Naties bestuurd worden",
        ],
        antwoord=0,
        uitleg="Enkele maanden voorbereiding voor een land zo groot als West-Europa. Dat was bijzonder krap.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke datum werd Congo onafhankelijk?",
        antwoord=["30 juni 1960", "30 juni"],
        uitleg="Het is nog altijd de nationale feestdag van de Democratische Republiek Congo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie werd in 1960 de eerste premier van onafhankelijk Congo?",
        opties=[
            "Patrice Lumumba",
            "Joseph Kasavubu",
            "Moïse Tshombe",
            "Mobutu Sese Seko",
        ],
        antwoord=0,
        uitleg="Kasavubu werd staatshoofd. Hun samenwerking hield geen half jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stond Congo er in 1960 slecht voor om zichzelf te besturen?",
        opties=[
            "er waren amper Congolezen met een universitair diploma",
            "er waren geen scholen voor Congolese kinderen geweest",
            "er waren geen grondstoffen in de bodem te vinden",
            "er was geen enkele politieke partij in het land",
        ],
        antwoord=0,
        uitleg="Lager onderwijs was er ruim, hoger onderwijs amper. Daar had de kolonisator niet in voorzien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je over de toespraak van Lumumba op de plechtigheid van 30 juni 1960?",
        opties=[
            "hij sprak openlijk over het onrecht van de koloniale tijd",
            "hij bedankte België voor zijn beschavingswerk in Congo",
            "hij vroeg België om nog dertig jaar te blijven besturen",
            "hij kondigde er de afscheiding van Katanga aan",
        ],
        antwoord=0,
        uitleg="Die toespraak was niet voorzien in het programma en heeft in Brussel zwaar gewogen.",
    ),
    dict(
        type="waarofniet",
        vraag="Congo werd onafhankelijk in hetzelfde jaar als een hele reeks andere Afrikaanse staten.",
        antwoord=True,
        uitleg="Daarom heet 1960 het Afrikaanse jaar. Zeventien staten werden dat jaar onafhankelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De onafhankelijkheid van Congo werd jarenlang zorgvuldig voorbereid.",
        antwoord=False,
        uitleg="Tussen de rellen van januari 1959 en de onafhankelijkheid lag maar anderhalf jaar.",
    ),
    dict(
        type="waarofniet",
        vraag="In Congo waren er voor 1960 politieke bewegingen die zelfbestuur eisten.",
        antwoord=True,
        uitleg="Vooral uit de kringen van de évolués. Het manifest van Conscience africaine uit 1956 is een voorbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="België was in de jaren vijftig van plan Congo snel onafhankelijk te maken.",
        antwoord=False,
        uitleg="Men dacht nog in tientallen jaren. De gebeurtenissen hebben dat tempo volledig overhoop gegooid.",
    ),
    dict(
        type="waarofniet",
        vraag="De dekolonisatie na 1945 betrof zowel Azië als Afrika.",
        antwoord=True,
        uitleg="India werd in 1947 onafhankelijk, Indonesië in 1949, en het grootste deel van Afrika na 1956.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemde men de Congolezen met een opleiding die als eersten politieke rechten vroegen?",
        antwoord=["de évolués", "évolués", "evolues"],
        uitleg="Letterlijk de ontwikkelden. Het woord zegt zelf al hoe de kolonisator naar de rest keek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de dekolonisatie kloppen?",
        opties=[
            "de Tweede Wereldoorlog had het prestige van Europa aangetast",
            "soldaten uit de kolonies hadden in Europa meegevochten",
            "de kolonies hadden geen enkele eigen politieke beweging",
            "Europa gaf zijn kolonies zonder enig conflict op",
        ],
        antwoord=[0, 1],
        uitleg="In Algerije, Indochina en Kenia zijn er juist lange en bloedige oorlogen aan voorafgegaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een foto van 30 juni 1960 met de Belgische koning en Congolese leiders samen. Wat stelt die voor?",
        opties=[
            "de plechtigheid van de onafhankelijkheid",
            "de Ronde Tafelconferentie in Brussel",
            "de staatsgreep van Mobutu in 1965",
            "de wereldtentoonstelling van Brussel in 1958",
        ],
        antwoord=0,
        uitleg="Diezelfde dag droeg de Belgische staat het bestuur van een enorm gebied over.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er kort na de onafhankelijkheid van Congo in juli 1960?",
        opties=[
            "het leger kwam in opstand en Katanga scheidde zich af",
            "het land werd meteen een stabiele democratie",
            "België nam het bestuur van het land weer over",
            "de Verenigde Naties maakten Congo hun mandaatgebied",
        ],
        antwoord=0,
        uitleg="Het land viel in enkele weken uiteen. Die periode wordt de Congocrisis genoemd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom was de afscheiding van Katanga voor Congo zo zwaar?",
        opties=[
            "daar lagen de mijnen van het land",
            "daar woonde het grootste deel van de bevolking",
            "daar lag de hoofdstad met alle overheidsdiensten",
            "daar lag de enige haven aan de Atlantische Oceaan",
        ],
        antwoord=0,
        uitleg="Het koper van Katanga was de rijkdom van het land. Belgische belangen speelden in die afscheiding mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelden de Verenigde Naties in de Congocrisis?",
        opties=[
            "zij stuurden troepen om de orde te bewaren",
            "zij erkenden Katanga als een onafhankelijke staat",
            "zij gaven het bestuur van Congo aan België terug",
            "zij weigerden zich met de zaak te bemoeien",
        ],
        antwoord=0,
        uitleg="Hun opdracht was ook de eenheid van het land te bewaren. Het werd een van de moeilijkste zendingen uit hun geschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er begin 1961 met Patrice Lumumba?",
        opties=[
            "hij werd afgezet, gevangengenomen en vermoord",
            "hij vluchtte naar België en bleef daar wonen",
            "hij bleef tot 1965 de premier van het land",
            "hij werd door de Verenigde Naties beschermd",
        ],
        antwoord=0,
        uitleg="Een Belgische parlementaire onderzoekscommissie stelde in 2001 een Belgische betrokkenheid vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie nam in 1965 met een staatsgreep de macht in Congo over?",
        opties=[
            "Mobutu Sese Seko",
            "Patrice Lumumba",
            "Joseph Kasavubu",
            "Laurent-Désiré Kabila",
        ],
        antwoord=0,
        uitleg="Hij bleef meer dan dertig jaar aan de macht, met steun uit het westen tijdens de Koude Oorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke naam gaf Mobutu aan het land in 1971?",
        opties=[
            "Zaïre",
            "Congo-Vrijstaat",
            "Belgisch Congo",
            "Katanga",
        ],
        antwoord=0,
        uitleg="Ook steden en namen van personen werden veranderd. Die politiek heette de authenticiteit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heette Congo tussen 1971 en 1997?",
        antwoord=["Zaïre", "Zaire"],
        uitleg="Na de val van Mobutu kreeg het land zijn naam Congo terug, als Democratische Republiek Congo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hield het westen Mobutu zo lang de hand boven het hoofd?",
        opties=[
            "hij was in de Koude Oorlog een bondgenoot tegen het communisme",
            "hij bestuurde het land volgens de regels van de rechtsstaat",
            "hij voerde vrije verkiezingen met meerdere partijen in",
            "hij gaf de mijnen van Katanga aan de bevolking terug",
        ],
        antwoord=0,
        uitleg="Pas na 1990, toen die logica wegviel, raakte hij zijn steun kwijt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkte het bestuur van Mobutu?",
        opties=[
            "één partij, geen vrije pers en geen vrije verkiezingen",
            "grote rijkdom voor hemzelf en zijn omgeving",
            "een snelle groei van de welvaart van de bevolking",
            "een onafhankelijke rechtspraak en een vrije oppositie",
        ],
        antwoord=[0, 1],
        uitleg="De infrastructuur verviel en de staatskas werd leeggehaald. Men spreekt van een kleptocratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1997 in Zaïre?",
        opties=[
            "Mobutu werd afgezet en het land heette weer Congo",
            "Mobutu werd met vrije verkiezingen opnieuw verkozen",
            "België nam het bestuur van het land weer over",
            "Katanga werd een onafhankelijke staat",
        ],
        antwoord=0,
        uitleg="Daarna volgden oorlogen waarin buurlanden en gewapende groepen betrokken waren, vooral in het oosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke problemen kent het oosten van Congo tot vandaag?",
        opties=[
            "gewapende groepen vechten er om gebied en om mijnen",
            "miljoenen mensen zijn er op de vlucht geweest",
            "het gebied heeft geen enkele grondstof in de bodem",
            "het gebied is sinds 1997 volledig in vrede",
        ],
        antwoord=[0, 1],
        uitleg="Juist de rijkdom aan erts is er een deel van het probleem. Grondstoffen voor onze toestellen komen van daar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed het Belgische parlement in 2020 met het koloniale verleden?",
        opties=[
            "het richtte een commissie op om dat verleden te onderzoeken",
            "het besliste de kolonie opnieuw onder bestuur te nemen",
            "het verbood het onderwijs over de koloniale tijd",
            "het sloot het museum over Centraal-Afrika",
        ],
        antwoord=0,
        uitleg="De werkzaamheden hebben veel materiaal opgeleverd, maar geen gezamenlijk besluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed koning Filip in 2020 over de koloniale tijd?",
        opties=[
            "hij sprak in een brief zijn diepste spijt uit",
            "hij verklaarde dat België niets te verwijten valt",
            "hij vroeg Congo om herstelbetalingen aan België",
            "hij gaf Congo zijn vroegere naam Zaïre terug",
        ],
        antwoord=0,
        uitleg="Bij zijn bezoek in 2022 herhaalde hij die spijt. Een formele verontschuldiging was het niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Congo was vanaf 1960 meteen een rustig en stabiel land.",
        antwoord=False,
        uitleg="Binnen weken volgden een muiterij, twee afscheidingen en een crisis van jaren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Belgische onderzoekscommissie stelde een Belgische betrokkenheid bij de moord op Lumumba vast.",
        antwoord=True,
        uitleg="Dat gebeurde in 2001, veertig jaar na de feiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Mobutu kwam met vrije verkiezingen aan de macht.",
        antwoord=False,
        uitleg="Hij kwam er met een staatsgreep van het leger, in 1965.",
    ),
    dict(
        type="waarofniet",
        vraag="Het koloniale verleden wordt in België vandaag onderzocht en besproken.",
        antwoord=True,
        uitleg="Er is een parlementaire commissie geweest, en standbeelden en straatnamen liggen onder de loep.",
    ),
    dict(
        type="waarofniet",
        vraag="De grondstoffen van Congo spelen in de wereldeconomie van vandaag geen rol meer.",
        antwoord=False,
        uitleg="Kobalt en coltan uit Congo zitten in batterijen en in elektronica over de hele wereld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt Belgisch Congo van 1950 met Congo van 1965. Welk verschil valt op?",
        opties=[
            "het bestuur lag eerst in Brussel en daarna bij één man in het land",
            "het bestuur lag in beide jaren bij een verkozen parlement",
            "het bestuur lag in beide jaren volledig bij de Verenigde Naties",
            "het bestuur lag eerst bij de Congolezen en daarna bij België",
        ],
        antwoord=0,
        uitleg="Van kolonie over een korte republiek naar een eenpartijstaat: dat alles in vijf jaar tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt gezegd dat de koloniale tijd in Congo tot vandaag doorwerkt?",
        opties=[
            "grenzen, economie en bestuur dragen er nog de sporen van",
            "de koloniale tijd is sinds 1960 volledig uitgewist",
            "Congo heeft sinds 1960 geen eigen regering meer gehad",
            "België bestuurt het land nog altijd in de praktijk",
        ],
        antwoord=0,
        uitleg="Een economie op de uitvoer van ertsen, grenzen uit Berlijn en een zwakke staat: dat erf je niet weg.",
    ),
]
