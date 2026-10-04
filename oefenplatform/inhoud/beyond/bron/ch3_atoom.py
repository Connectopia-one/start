# -*- coding: utf-8 -*-
"""Atoombouw, orbitalen en het periodiek systeem — 🌍 Beyond, chemie.

Deel 1 gaat over het atoom zelf: de verfijning van schil naar subniveau en
orbitaal, de vier kwantumgetallen, de diagonaalregel, de regel van Hund en het
uitsluitingsprincipe van Pauli, en de elektronenconfiguratie in de volle, de
hokjes- en de verkorte notatie. Deel 2 gaat over het periodiek systeem: de
opbouw in perioden, groepen en blokken, de namen van de hoofdgroepen, en de
verbanden tussen de plaats in het systeem en de afmeting, het metaalkarakter,
de elektronegatieve waarde en het oxidatiegetal.

Het periodiek systeem zelf krijgt het kind op het examen, dus hoeft het niet
van buiten gekend te zijn. De vragen geven het nodige getal of symbool mee en
vragen wat je eruit afleidt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat stelt een orbitaal voor?",
        opties=[
            "het gebied waar een elektron zich met grote kans bevindt",
            "de vaste cirkelbaan die een elektron rond de kern volgt",
            "de plaats waar een elektron precies stilstaat in het atoom",
            "de ruimte tussen twee schillen van het atoom van Bohr",
        ],
        antwoord=0,
        uitleg="In het model van Schrödinger ligt de plaats van een elektron niet vast. "
        "Een orbitaal is dus een kansgebied, geen baan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen passen er in één orbitaal?",
        opties=[
            "twee, met tegengestelde spin",
            "een, met een vrije spin",
            "vier, twee per spinrichting",
            "acht, zoals de octetregel zegt",
        ],
        antwoord=0,
        uitleg="Het uitsluitingsprincipe van Pauli zegt dat twee elektronen nooit "
        "dezelfde vier kwantumgetallen hebben. De spin is dus het enige verschil.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel kwantumgetallen beschrijven één elektron volledig?",
        antwoord=["vier", "4"],
        uitleg="Het hoofdniveau, het subniveau, het magnetisch niveau en de spin. Samen "
        "wijzen ze één elektron aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geeft het hoofdkwantumgetal n aan?",
        opties=[
            "het hoofdniveau of de schil waarin het elektron zit",
            "de vorm van het orbitaal waarin het elektron zit",
            "de richting van het orbitaal in de ruimte rond de kern",
            "de draairichting van het elektron om zijn eigen as",
        ],
        antwoord=0,
        uitleg="n is 1, 2, 3 … Hoe groter n, hoe verder van de kern en hoe hoger de "
        "energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het nevenkwantumgetal bepaalt of een elektron in een s-, p-, d- of f-orbitaal zit.",
        antwoord=True,
        uitleg="Dat getal staat voor het subniveau, en elk subniveau heeft zijn eigen "
        "vorm: s is bolvormig, p heeft twee lobben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen passen er in totaal in een p-subniveau?",
        opties=[
            "zes",
            "twee",
            "tien",
            "veertien",
        ],
        antwoord=0,
        uitleg="Een p-subniveau heeft drie orbitalen van twee elektronen. s heeft er 2, "
        "d 10 en f 14.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de regel van Hund?",
        opties=[
            "orbitalen van dezelfde energie vullen eerst elk met één elektron",
            "orbitalen van dezelfde energie vullen eerst helemaal vol per orbitaal",
            "elektronen met dezelfde spin stoten elkaar altijd af in een orbitaal",
            "elektronen vullen altijd eerst het subniveau met de laagste energie",
        ],
        antwoord=0,
        uitleg="Pas als elk orbitaal van dat subniveau één elektron heeft, komt het "
        "tweede erbij. Die eerste elektronen hebben dezelfde spin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de diagonaalregel?",
        opties=[
            "om de volgorde te vinden waarin de subniveaus gevuld worden",
            "om het aantal elektronen in een subniveau te berekenen",
            "om de lading van een mono-atomisch ion te voorspellen",
            "om de vorm van een orbitaal in de ruimte te bepalen",
        ],
        antwoord=0,
        uitleg="Daarom komt 4s vóór 3d: de diagonaal loopt niet gewoon van laag naar "
        "hoog hoofdniveau.",
    ),
    dict(
        type="invultekst",
        vraag="Welk subniveau wordt gevuld vlak voor 3d?",
        antwoord=["4s", "het 4s", "4s-subniveau"],
        uitleg="Volgens de diagonaalregel heeft 4s een iets lagere energie dan 3d. "
        "Daarom eindigt de configuratie van calcium op 4s².",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elektronenconfiguratie hoort bij een zuurstofatoom, met acht elektronen?",
        opties=[
            "1s² 2s² 2p⁴",
            "1s² 2s² 2p⁶",
            "1s² 2s⁴ 2p²",
            "1s² 2s² 2p² 3s²",
        ],
        antwoord=0,
        uitleg="Twee in 1s, twee in 2s en de laatste vier in 2p. Zuurstof heeft dus zes "
        "valentie-elektronen en komt twee tekort voor een octet.",
    ),
    dict(
        type="waarofniet",
        vraag="In de verkorte notatie vervang je het begin van de configuratie door het symbool van het vorige edelgas.",
        antwoord=True,
        uitleg="Kalium schrijf je als [Ar] 4s¹. Zo zie je direct hoeveel "
        "valentie-elektronen er nog bij komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont de hokjesvoorstelling dat de exponentennotatie niet toont?",
        opties=[
            "hoe de elektronen over de orbitalen verdeeld zijn, met hun spin",
            "hoeveel elektronen er in elk subniveau van het atoom zitten",
            "in welk blok van het periodiek systeem het element staat",
            "hoeveel protonen er in de kern van het atoom aanwezig zijn",
        ],
        antwoord=0,
        uitleg="In de hokjes zie je of een orbitaal één of twee elektronen heeft, en dus "
        "of de regel van Hund gevolgd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het ion Na⁺ zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het heeft tien elektronen",
            "het heeft de configuratie van neon",
            "het heeft elf elektronen",
            "het is groter dan het natriumatoom",
        ],
        antwoord=[0, 1],
        uitleg="Natrium staat één elektron af. Wat overblijft is 1s² 2s² 2p⁶, en dat is "
        "de configuratie van het edelgas neon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom eindigt de configuratie van chroom op 3d⁵ 4s¹ en niet op 3d⁴ 4s²?",
        opties=[
            "een halfgevuld d-subniveau is stabieler dan een gewone vulling",
            "een volledig gevuld s-subniveau is onmogelijk bij een metaal",
            "het 4s-subniveau ligt bij chroom hoger in energie dan 4p",
            "het d-subniveau van chroom heeft maar vijf orbitalen vrij",
        ],
        antwoord=0,
        uitleg="Bij chroom en koper schuift er daarom één elektron van 4s naar 3d. Dat "
        "zijn de stabiliteitsregels voor het d-blok.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee waarden kan het spinkwantumgetal hebben?",
        antwoord=["+½ en −½", "+1/2 en -1/2", "een half"],
        uitleg="De twee elektronen van één orbitaal hebben een tegengestelde spin. In de "
        "hokjesvoorstelling tekent men dat als een pijl omhoog en een pijl omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke atoommodellen gaan verder dan de schillen van Bohr? Kruis alles aan wat juist is.",
        opties=[
            "het model van Bohr-Sommerfeld, met subniveaus",
            "het model van Schrödinger, met orbitalen",
            "het model van Bohr, met enkel schillen",
            "het model van Rutherford, met enkel een kern",
        ],
        antwoord=[0, 1],
        uitleg="Bohr had enkel schillen, Bohr-Sommerfeld voegde subniveaus en magnetische "
        "subniveaus toe, en Schrödinger kwam met de golfmechanica en de orbitalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee elektronen in hetzelfde atoom kunnen alle vier hun kwantumgetallen gelijk hebben.",
        antwoord=False,
        uitleg="Dat verbiedt het uitsluitingsprincipe van Pauli. Minstens één van de vier "
        "moet verschillen, en dat is vaak de spin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel valentie-elektronen heeft een atoom met de configuratie [Ne] 3s² 3p³?",
        opties=[
            "vijf",
            "drie",
            "twee",
            "acht",
        ],
        antwoord=0,
        uitleg="De valentie-elektronen zijn die van het hoogste hoofdniveau: 2 plus 3 is "
        "5. Dat is fosfor, uit de stikstofgroep.",
    ),
    dict(
        type="waarofniet",
        vraag="Het magnetisch kwantumgetal zegt hoeveel elektronen er in een subniveau passen.",
        antwoord=False,
        uitleg="Het zegt in welk orbitaal van dat subniveau het elektron zit. Een "
        "p-subniveau heeft drie magnetische subniveaus, dus drie orbitalen van elk twee "
        "elektronen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel elektronen passen er in een volledig d-subniveau?",
        antwoord=["tien", "10"],
        uitleg="Vijf orbitalen van twee elektronen. Daarom heeft een rij van het d-blok "
        "tien elementen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat hebben alle elementen van dezelfde groep in het periodiek systeem gemeen?",
        opties=[
            "het aantal elektronen in het buitenste hoofdniveau",
            "het aantal protonen in de kern van hun atoom",
            "het hoofdniveau waarin hun buitenste elektronen zitten",
            "de massa van hun atoom, uitgedrukt in atomaire eenheden",
        ],
        antwoord=0,
        uitleg="Daarom reageren ze op dezelfde manier. Het periodenummer zegt in welk "
        "hoofdniveau die elektronen zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet groep 17 van het periodiek systeem?",
        opties=[
            "de halogenen",
            "de edelgassen",
            "de alkalimetalen",
            "de aardalkalimetalen",
        ],
        antwoord=0,
        uitleg="Fluor, chloor, broom en jood. Ze hebben zeven valentie-elektronen en "
        "nemen er dus graag één op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de groep met lithium, natrium en kalium?",
        antwoord=["alkalimetalen", "de alkalimetalen", "alkalimetaal"],
        uitleg="Groep 1, met één valentie-elektron. Ze reageren heftig met water en "
        "vormen daarbij een hydroxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk blok staan de overgangselementen?",
        opties=[
            "in het d-blok",
            "in het s-blok",
            "in het p-blok",
            "in het f-blok",
        ],
        antwoord=0,
        uitleg="IJzer, koper en zink zijn nevengroepelementen uit het d-blok. De zeldzame "
        "aarden staan in het f-blok.",
    ),
    dict(
        type="waarofniet",
        vraag="De atoomradius van de hoofdgroepelementen neemt toe naar beneden in een groep.",
        antwoord=True,
        uitleg="Elk nieuw hoofdniveau ligt verder van de kern. Daarom is kalium groter "
        "dan natrium.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de atoomradius als je in een periode naar rechts gaat?",
        opties=[
            "hij wordt kleiner, want de kern trekt sterker aan",
            "hij wordt groter, want er komen elektronen bij",
            "hij blijft gelijk, want het hoofdniveau verandert niet",
            "hij wordt eerst groter en daarna weer kleiner",
        ],
        antwoord=0,
        uitleg="Er komt elke keer een proton bij, terwijl de elektronen in hetzelfde "
        "hoofdniveau blijven. Die sterkere aantrekking trekt de wolk samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een positief ion zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is kleiner dan het atoom waaruit het ontstond",
            "het heeft minder elektronen dan protonen",
            "het is groter dan het atoom waaruit het ontstond",
            "het heeft meer elektronen dan protonen in de kern",
        ],
        antwoord=[0, 1],
        uitleg="Bij het afstaan van een elektron verdwijnt vaak een heel hoofdniveau, en "
        "de overblijvende elektronen worden sterker aangetrokken.",
    ),
    dict(
        type="invultekst",
        vraag="Welk element heeft de hoogste elektronegatieve waarde?",
        antwoord=["fluor", "F"],
        uitleg="Fluor trekt het hardst aan elektronen van een binding. Naar links en naar "
        "beneden in het systeem wordt die waarde kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar staan de elementen met het sterkste metaalkarakter?",
        opties=[
            "linksonder in het periodiek systeem",
            "rechtsboven in het periodiek systeem",
            "in het midden van de tweede periode",
            "in de laatste groep van het systeem",
        ],
        antwoord=0,
        uitleg="Een metaal staat zijn elektronen makkelijk af. Dat gaat het best als ze "
        "ver van de kern zitten en er maar één of twee zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn de edelgassen zo weinig reactief?",
        opties=[
            "hun buitenste hoofdniveau is helemaal volgevuld",
            "hun kern bevat te veel protonen om te reageren",
            "hun elektronen zitten in een f-subniveau vast",
            "hun atomen zijn te groot om te kunnen binden",
        ],
        antwoord=0,
        uitleg="Acht valentie-elektronen, bij helium twee: dat is de "
        "edelgasconfiguratie waar de octetregel naar verwijst.",
    ),
    dict(
        type="waarofniet",
        vraag="Het groepsnummer van een hoofdgroepelement heeft niets te maken met het aantal valentie-elektronen.",
        antwoord=False,
        uitleg="Het heeft er net alles mee te maken: groep 1 heeft er één, groep 2 twee, "
        "groep 16 zes en groep 17 zeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal verwacht je bij een element uit groep 2?",
        opties=[
            "+II",
            "+I",
            "−II",
            "+III",
        ],
        antwoord=0,
        uitleg="Twee valentie-elektronen afstaan geeft de configuratie van het vorige "
        "edelgas. Magnesium wordt dus Mg²⁺.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een periode in het periodiek systeem zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een periode is een rij in het systeem",
            "het nummer geeft het hoogste hoofdniveau",
            "een periode is een kolom in het systeem",
            "het nummer geeft het aantal valentie-elektronen",
        ],
        antwoord=[0, 1],
        uitleg="Een groep is de kolom, en die geeft het aantal valentie-elektronen. Een "
        "periode is de rij, en die geeft het hoofdniveau.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de groep met zuurstof, zwavel en selenium?",
        antwoord=["zuurstofgroep", "de zuurstofgroep", "zuurstofgroep 16"],
        uitleg="Groep 16, met zes valentie-elektronen. Ze nemen er dus graag twee op en "
        "vormen een ion met lading 2−.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een atoom heeft de configuratie [Ar] 4s² 3d¹⁰ 4p⁵. In welke groep staat het?",
        opties=[
            "in groep 17, bij de halogenen",
            "in groep 15, bij de stikstofgroep",
            "in groep 13, bij de aardmetalen",
            "in groep 18, bij de edelgassen",
        ],
        antwoord=0,
        uitleg="Tel de elektronen van het hoogste hoofdniveau: 2 in 4s en 5 in 4p is 7. "
        "Dat is broom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een negatief ion groter dan het atoom waaruit het ontstond?",
        opties=[
            "de extra elektronen stoten elkaar af en de kernlading blijft gelijk",
            "de kern krijgt er een proton bij en wordt zwaarder",
            "er komt een volledig nieuw hoofdniveau bij het ion",
            "de elektronen gaan in een d-subniveau zitten in plaats van p",
        ],
        antwoord=0,
        uitleg="Het chloride-ion Cl⁻ is daarom duidelijk groter dan het chlooratoom. Bij "
        "een positief ion gebeurt het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="De zeldzame aarden staan in het f-blok van het periodiek systeem.",
        antwoord=True,
        uitleg="Dat zijn de twee rijen die onder het systeem apart staan. Ze zitten in "
        "magneten en in de elektronica van een gsm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het d-blok zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een volledige rij heeft tien elementen",
            "het bevat de overgangselementen",
            "een volledige rij heeft veertien elementen",
            "het bevat de zeldzame aarden",
        ],
        antwoord=[0, 1],
        uitleg="Een d-subniveau heeft vijf orbitalen en dus tien plaatsen, en die rijen "
        "bevatten de nevengroepelementen. De zeldzame aarden staan in het f-blok, dat er "
        "veertien heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Helium volgt de octetregel met acht valentie-elektronen.",
        antwoord=False,
        uitleg="Helium heeft er twee, en daarmee is zijn enige hoofdniveau vol. Voor het "
        "eerste hoofdniveau is twee dus al de edelgasconfiguratie.",
    ),
    dict(
        type="invultekst",
        vraag="In welk blok staat een element waarvan het buitenste elektron in een p-orbitaal zit?",
        antwoord=["p-blok", "het p-blok", "p"],
        uitleg="Het blok draagt de naam van het subniveau dat als laatste gevuld wordt. "
        "Groep 13 tot 18 vormen samen het p-blok.",
    ),
]
