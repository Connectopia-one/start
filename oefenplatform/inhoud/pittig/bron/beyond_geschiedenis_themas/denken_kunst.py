"""Denken, kunst en emancipatie — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvraag op 1948"),
]

VRAGEN = [
    mk(
        "Wat is het verschil tussen emancipatie en dekolonisatie?",
        [
            "Emancipatie gaat over een groep in een samenleving, dekolonisatie over een land",
            "Emancipatie gaat over landen in Afrika, dekolonisatie over landen in Azië",
            "Emancipatie is gewelddadig, dekolonisatie gebeurt altijd via onderhandelingen",
            "Er is geen verschil: het zijn twee woorden voor hetzelfde proces",
        ],
        0,
        "Bij emancipatie verwerft een groep gelijke rechten binnen de eigen samenleving. Zulke bewegingen lopen vaak over meerdere generaties.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin vrouwen in België stemrecht kregen voor de nationale verkiezingen.",
        "tijdlijn-1750-2030.svg",
        [[63.6, 25, 6.2, 55]],
        "1948, net voor het streepje van 1950: dertig jaar na de mannen.",
    ),
    keuze(
        "Sommige vrouwen mochten al vanaf [[*1921|1966|1893]] stemmen, maar enkel voor de [[*gemeenteraad|Kamer|Senaat]].",
        "Voor de gemeenteraad kon het al in 1921, voor het parlement pas veel later.",
    ),
    mk(
        "In 1966 legden de vrouwen van de wapenfabriek FN in Herstal twaalf weken lang het werk neer. Wat eisten ze?",
        [
            "Gelijk loon voor gelijk werk",
            "Het recht om als soldaat in het leger te gaan",
            "Een verbod op de uitvoer van wapens naar het buitenland",
            "Kortere werkdagen voor alle mannen in de fabriek",
        ],
        0,
        "Gelijk loon voor gelijk werk. De staking werd een symbool van de vrouwenbeweging in België.",
    ),
    tabel(
        "Juist of fout? De emancipatie van de vrouw in België.",
        [
            ("In 1976 werd de man als wettelijk hoofd van het gezin afgeschaft.", J),
            ("Het aantal vrouwen in het hoger onderwijs steeg sterk.", J),
            ("De loonkloof tussen mannen en vrouwen is vandaag volledig verdwenen.", F),
            ("Vrouwen kregen tegelijk met de mannen stemrecht voor het parlement.", F),
        ],
        "De wettelijke achterstelling verdween stap voor stap, maar een loonkloof bestaat nog. Het stemrecht kwam voor vrouwen veel later dan voor mannen.",
    ),
    mk(
        "In een groot bedrijf is de helft van het personeel vrouw, maar in de directie zit geen enkele vrouw. Welk begrip past daarbij?",
        ["Het glazen plafond", "De loonkloof", "De verzuiling", "Het cijnskiesrecht"],
        0,
        "Een onzichtbare grens houdt vrouwen weg van de hoogste functies. Daarom kwamen er quota voor de raden van bestuur.",
    ),
    mk(
        "Waarom speelde de anticonceptiepil zo'n grote rol in de seksuele revolutie van de jaren zestig?",
        [
            "Vrouwen konden voor het eerst zelf bepalen of en wanneer ze kinderen kregen",
            "De pil maakte het huwelijk wettelijk verplicht voor alle volwassenen in België",
            "De pil werd door de kerk aangeraden en maakte zo een einde aan de verzuiling",
            "Met de pil kregen vrouwen meteen stemrecht bij alle verkiezingen",
        ],
        0,
        "Voor het eerst lag die keuze bij de vrouw zelf. Seksualiteit werd ook bespreekbaarder.",
    ),
    mk(
        "Wat gebeurde er toen in België de wet die abortus uit het strafrecht haalde, getekend moest worden?",
        [
            "Koning Boudewijn weigerde te tekenen en werd één dag in de onmogelijkheid tot regeren gesteld",
            "Het parlement keurde de wet af, waarna er een volksraadpleging over georganiseerd werd in het hele land",
            "De wet werd door de Europese Unie tegengehouden en pas tien jaar later goedgekeurd",
            "De koning tekende meteen, maar de regering viel nog dezelfde dag over de kwestie",
        ],
        0,
        "Het was 1990. De regering loste het op door de koning één dag buiten spel te zetten.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak.",
        [
            ("De afkorting lgbtqia+ verwijst naar mensen met uiteenlopende seksuele oriëntaties en genderidentiteiten.", J),
            ("De plus in lgbtqia+ staat er bewust bij.", J),
            ("Een politieoptreden in een café in New York werd het begin van de holebibeweging.", J),
            ("België was het eerste land ter wereld dat het huwelijk openstelde voor koppels van hetzelfde geslacht.", F),
        ],
        "België was het tweede land, na Nederland.",
    ),
    volgorde(
        "Zet deze stappen in de strijd voor gelijke rechten in de juiste volgorde.",
        ["De mars op Washington", "Het verzet in de Stonewall Inn", "België opent het huwelijk voor koppels van hetzelfde geslacht", "Koppels van hetzelfde geslacht mogen in België adopteren", "Black Lives Matter groeit wereldwijd uit"],
        "1963, 1969, 2003, 2006 en 2020.",
    ),
    mk(
        "Een zwarte reiziger in het zuiden van de Verenigde Staten moest rond 1950 apart zitten op de bus, en zijn kinderen gingen naar een aparte school. Op grond waarvan?",
        ["De Jim Crow-wetten", "De Civil Rights Act", "De Voting Rights Act", "De Brezjnevdoctrine"],
        0,
        "De Jim Crow-wetten scheidden zwarte en witte Amerikanen in het openbare leven.",
    ),
    casus(
        "Montgomery, 1955. Een zwarte vrouw weigert haar zitplaats op de bus af te staan aan een witte reiziger. Ze wordt gearresteerd.",
        [
            inv(
                "Hoe heet deze vrouw? Schrijf voornaam en familienaam.",
                "Rosa Parks",
                "Rosa Parks.",
            ),
            mk(
                "Wat volgde er op haar arrestatie?",
                [
                    "Een busboycot van meer dan een jaar, geleid door Martin Luther King",
                    "Een gewapende opstand die het leger met tanks en soldaten moest neerslaan",
                    "Een volksraadpleging over het openbaar vervoer in heel de VS",
                    "De onmiddellijke afschaffing van alle aparte scholen",
                ],
                0,
                "De zwarte inwoners van Montgomery lieten de bus meer dan een jaar links liggen.",
            ),
            keuze(
                "Dat één vrouw met haar keuze een beweging in gang zette, is een voorbeeld van [[*agency|continuïteit|stereotypering]]: de redeneerwijze menselijke actoren benoemen.",
                "Mensen maken keuzes die geschiedenis maken. Dat noemt men agency.",
            ),
        ],
    ),
    sorteer(
        "Koos de leider of de actie voor geweldloos verzet, of sloot ze gewapende zelfverdediging niet uit?",
        ["Geweldloos verzet", "Gewapende zelfverdediging niet uitgesloten"],
        [
            ["Martin Luther King", "Geweldloos verzet"],
            ["Malcolm X", "Gewapende zelfverdediging niet uitgesloten"],
            ["De Black Panthers", "Gewapende zelfverdediging niet uitgesloten"],
            ["De mars op Washington", "Geweldloos verzet"],
        ],
        "Niet alle leiders kozen hetzelfde. King stond voor geweldloos verzet, Malcolm X en de Black Panthers niet.",
    ),
    keuze(
        "De beroemdste zin van Martin Luther King begint met [[*I have a dream|We shall overcome|Yes we can]]. Hij werd in [[*1968|1963|1955]] vermoord.",
        "I have a dream, bij de mars op Washington. Vijf jaar later werd hij vermoord.",
    ),
    tabel(
        "Een leerling somt op wat de Amerikaanse burgerrechtenbeweging bereikte. Wat noemt ze terecht?",
        [
            ("Een wet die discriminatie in het openbare leven verbood", J),
            ("Een wet die het stemrecht van zwarte kiezers beschermde", J),
            ("Het einde van de wettelijke scheiding in scholen en openbare plaatsen", J),
            ("Een einde aan elke vorm van racisme in de Verenigde Staten", F),
        ],
        "De Civil Rights Act en de Voting Rights Act. Racisme verdween daarmee niet.",
    ),
    mk(
        "Waartegen komt de beweging Black Lives Matter op?",
        [
            "Tegen politiegeweld en racisme tegenover zwarte mensen",
            "Tegen de klimaatopwarming en de vervuiling van de oceanen",
            "Tegen grensoverschrijdend gedrag op de werkvloer",
            "Tegen de hoge prijzen van huizen in de grote steden",
        ],
        0,
        "Ontstaan in 2013, ook in Belgische steden actief. De andere opties passen bij de klimaatmarsen en MeToo.",
    ),
    mk(
        "Vanaf de jaren vijftig vormden jongeren een eigen groep met een eigen smaak. Wat maakte dat mogelijk?",
        [
            "Ze studeerden langer en verdienden zelf geld",
            "De overheid verplichtte hen om eigen verenigingen op te richten",
            "Ze mochten vanaf hun twaalfde stemmen",
            "De zuilen stuurden hen naar aparte jeugdkampen",
        ],
        0,
        "Langer studeren en eigen geld maakten van jongeren een groep met eigen muziek en kleding.",
    ),
    keuze(
        "Het geluid van de nieuwe jongerencultuur van de jaren vijftig werd de [[*rock-'n-roll|klassieke muziek|hiphop]].",
        "De rock-'n-roll was de muziek van de eerste echte jongerencultuur.",
    ),
    tabel(
        "Juist of fout? Mei 1968.",
        [
            ("Studenten protesteerden in Parijs en elders tegen het gezag van de oude orde.", J),
            ("Het protest ging alleen over muziek en kleding.", F),
            ("In België viel in hetzelfde jaar Leuven Vlaams.", J),
            ("Het protest speelde zich zowel op de universiteit als in de maatschappij af.", J),
        ],
        "De jongerencultuur had wel degelijk een politieke kant.",
    ),
    sorteer(
        "Protestbeweging of politieke partij?",
        ["Beweging", "Partij"],
        [
            ["Voert actie rond één thema", "Beweging"],
            ["Komt op bij verkiezingen", "Partij"],
            ["De klimaatmarsen van jongeren", "Beweging"],
            ["De MeToo-beweging tegen grensoverschrijdend gedrag", "Beweging"],
        ],
        "Een beweging mobiliseert rond een thema, vaak via sociale media. Een partij wil verkozen worden.",
    ),
    tabel(
        "Aan welke kunstenaar doet elk werk het meest denken?",
        [
            ("Zes keer hetzelfde soepblik naast elkaar, telkens in een andere felle kleur", "Warhol"),
            ("Een stripbeeld van een huilende vrouw, sterk vergroot, met grote zichtbare drukstippen", "Lichtenstein"),
            ("Een wasknijper van meer dan tien meter hoog op een stadsplein", "Oldenburg"),
            ("Vier identieke grijze blokken, op gelijke afstand naast elkaar op de vloer", "Geen popart"),
        ],
        "Herhaalde blikken, een stripbeeld met drukstippen, een reusachtig alledaags voorwerp. Eenvoudige blokken in serie zijn minimal art.",
        kolommen=["Warhol", "Lichtenstein", "Oldenburg", "Geen popart"],
    ),
    mk(
        "Welk werk toont het best dat de popart de grens tussen hoge en lage cultuur laat vervagen?",
        [
            "Een strip uit de krant, vergroot tot schilderij in een museum",
            "Een portret van een koning in olieverf, voor in zijn paleis",
            "Een landschap met een dorpskerk, geschilderd in de stijl van de 17de eeuw",
            "Een marmeren beeld van een Griekse god, in klassieke stijl",
        ],
        0,
        "Iets uit de alledaagse, lage cultuur krijgt een plaats in het museum: daar vervaagt de grens.",
    ),
    tabel(
        "Hoort het kenmerk bij de popart?",
        [
            ("Felle, vlakke kleuren", J),
            ("Veel herhaling van hetzelfde beeld", J),
            ("De grens tussen hoge en lage cultuur vervaagt", J),
            ("Enkel religieuze en mythologische onderwerpen", F),
        ],
        "Popart komt van popular. Ze kijkt met een zekere ironie naar de consumptiemaatschappij.",
    ),
    inv(
        "Met welke druktechniek kon Warhol hetzelfde beeld snel in reeksen herhalen? (één woord)",
        "zeefdruk",
        "De zeefdruk.",
    ),
    mk(
        "Waarom kon de popart pas na de Tweede Wereldoorlog ontstaan?",
        [
            "De naoorlogse welvaart bracht reclame, merken en massaproductie in elk huis",
            "Voor de oorlog was het bij wet verboden om kunst te maken over alledaagse dingen uit de winkel",
            "Voor de oorlog bestond er nog geen enkele vorm van kleurendruk",
            "Na de oorlog wilden de musea enkel nog Amerikaanse kunst tonen",
        ],
        0,
        "Zonder supermarkt, televisiereclame en filmsterren bestaat de popart niet.",
    ),
    koppel(
        "Welke stroming hoort bij elke omschrijving?",
        [
            ["Ontstond in 1948 in drie hoofdsteden, met spontane, bijna kinderlijke beelden", "Cobra"],
            ["Vormen en kleuren laten het oog denken dat er beweging in het vlak zit", "Optical art"],
            ["Het werk wordt rechtstreeks in een landschap in de natuur gemaakt", "Land art"],
            ["Het idee achter het werk telt meer dan het voorwerp dat je ziet", "Conceptuele kunst"],
        ],
        ["Postmodernisme"],
        "Vier stromingen naast de popart. Het postmodernisme past bij geen van deze vier.",
    ),
    mk(
        "Een nieuw gebouw combineert Griekse zuilen, een glazen gevel en een gotisch torentje. Welke stroming herken je?",
        ["Het postmodernisme", "De minimal art", "De land art", "De popart van Warhol"],
        0,
        "Stijlen uit verschillende tijden worden door elkaar gebruikt en geciteerd.",
    ),
    open_(
        "Leg uit hoe de emancipatiebewegingen en de kunst van de jaren zestig met elkaar samenhangen.",
        "Ze staan niet los van elkaar: in dezelfde jaren eisten jongeren, vrouwen en minderheden een plaats op, en tegelijk brak de kunst met wat hoort en niet hoort. De popart haalde bijvoorbeeld reclame en strips het museum binnen.",
    ),
]
