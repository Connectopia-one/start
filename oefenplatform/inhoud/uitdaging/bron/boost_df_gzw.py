# -*- coding: utf-8 -*-
"""Uitdaging Gezondheid, zorg en welzijn 🚀 Boost dubbele finaliteit (25
november 2026), in de vormen van het examen van de Examencommissie: 40 vragen
die alle hoofdstukken door elkaar halen, van waarnemen, het oog en het
zenuwstelsel tot Gordon, het ICF, eerste hulp, voeding, voedselveiligheid,
interieurzorg en linnenzorg. Een doorsnede van het oog en zes verzonnen
situaties om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde, een casus en een open vraag. Geen nieuwe leerstof: alles
staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_gzw.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Gezondheid, zorg en welzijn"
BESTAND = "boost-df-gzw-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/gzw-boost-df-uitdaging"
OOG = "oog-doorsnede.svg"
SIT = "zes-situaties.svg"
# klikvakken: zie maak_prenten_boost_df_gzw.py (randen bijgeknipt zodat ze niet overlappen)
NETVLIES = [61.0, 22.6, 15.0, 64.5]
LENS = [42.5, 30.6, 6.5, 38.7]
HOORNVLIES = [26.0, 33.1, 11.0, 38.7]
OOGZENUW = [76.4, 40.3, 20.0, 19.4]
IRIS = [37.2, 25.8, 5.2, 48.4]
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Oog
    klik("Bekijk de doorsnede van het oog. Klik op het deel waar het licht het eerst op valt.",
         OOG, [HOORNVLIES],
         "Het licht valt eerst op het hoornvlies, de doorzichtige bolling vooraan (3)."),
    klik("Klik op het deel dat de lichtstralen bundelt, zodat er een scherp beeld ontstaat.",
         OOG, [LENS],
         "De lens (2) breekt de lichtstralen en zorgt voor een scherp beeld op het netvlies."),
    klik("Klik op het deel waar de staafjes en de kegeltjes zitten.",
         OOG, [NETVLIES],
         "Staafjes en kegeltjes zijn de lichtgevoelige cellen in het netvlies (1), achteraan in het oog."),
    klik("Klik op het deel dat de impulsen van het oog naar de hersenen brengt.",
         OOG, [OOGZENUW],
         "De oogzenuw (4) voert de impulsen van het netvlies naar de hersenen."),
    met_prent(OOG, keuze(
        "Deel 5 is de [[*iris|lens|oogzenuw]]. De opening ertussen heet de [[*pupil|papil]]. In het donker wordt die opening [[*groter|kleiner]].",
        "De iris regelt hoeveel licht er binnenkomt via de pupil. In het donker gaat de pupil wijder open.")),

    # Situaties
    klik("Bekijk de zes situaties. Klik op de situatie waarbij je meteen 112 belt.",
         SIT, [Z[3]],
         "Iemand die in elkaar zakt en niet normaal ademt, heeft dringend hulp nodig: bel 112 en start de reanimatie."),
    klik("Klik op de situatie waarin je 1733 belt en niet 112.",
         SIT, [Z[4]],
         "1733 is de huisarts of de huisartsenwachtpost, voor klachten die geen 112 vragen."),
    klik("Klik op de situatie met kruisbesmetting.",
         SIT, [Z[2]],
         "Bij kruisbesmetting gaan kiemen van rauw voedsel over naar ander voedsel, hier via de snijplank."),
    klik("Klik op de situatie met secundaire preventie.",
         SIT, [Z[1]],
         "Een bevolkingsonderzoek spoort een ziekte vroeg op. Dat is secundaire preventie."),
    met_prent(SIT, keuze(
        "Bij situatie 6 [[*koel|verwarm|masseer]] je de enkel. Bij situatie 5 lees je het etiket en draag je zo nodig [[*handschoenen|een schort zonder mouwen]].",
        "Een verstuiking koel je om zwelling en pijn te beperken. Een gevarenpictogram zegt dat je je moet beschermen.")),

    # Waarnemen en zenuwstelsel
    volgorde(
        "Zet de stappen van een reflex in de juiste volgorde.",
        ["Een receptor vangt de prikkel op.",
         "Een sensibele zenuw brengt de impuls naar het ruggenmerg.",
         "In het ruggenmerg gaat de impuls naar een motorische zenuw.",
         "De spier trekt samen."],
        "Bij een reflex loopt de impuls via de reflexboog: receptor, sensibele zenuw, ruggenmerg, motorische zenuw, effector."),
    tabel(
        "Klopt dit over het zenuwstelsel?",
        [
            ("Het ruggenmerg hoort bij het centraal zenuwstelsel.", J),
            ("In de synaps springt de impuls rechtstreeks over.", F),
            ("Een reflex gebeurt onbewust.", J),
            ("De kleine hersenen regelen het evenwicht.", J),
        ],
        "In de synaps brengt een stof de boodschap over naar de volgende cel. Een reflex verloopt zonder dat je erover nadenkt."),
    koppel(
        "Koppel het zintuig aan zijn receptoren.",
        [
            ["huid", "tast-, druk-, warmte- en pijnreceptoren"],
            ["tong", "smaakknoppen in de papillen"],
            ["oor", "het orgaan van Corti in het slakkenhuis"],
        ],
        ["staafjes en kegeltjes"],
        "Elk zintuig heeft eigen receptoren. Staafjes en kegeltjes zitten in het oog."),
    inv("Boven hoeveel decibel kan lang luisteren je gehoor beschadigen? Een getal.",
        ["80"],
        "Boven tachtig decibel kan lang luisteren je gehoor beschadigen."),

    # Spieren en beenderen
    tabel(
        "Willekeurig of onwillekeurig spierweefsel?",
        [
            ("skeletspieren", "willekeurig"),
            ("glad spierweefsel in de darmen", "onwillekeurig"),
            ("de hartspier", "onwillekeurig"),
        ],
        "Skeletspieren stuur je zelf. Glad spierweefsel en de hartspier werken vanzelf.",
        kolommen=["willekeurig", "onwillekeurig"]),
    keuze(
        "Als je je arm buigt, trekt de [[*biceps|triceps]] samen. Twee botten worden met elkaar verbonden door [[*ligamenten|pezen]].",
        "De biceps buigt de arm, de triceps strekt hem. Pezen verbinden een spier met een bot, ligamenten een bot met een bot."),

    # Gordon en ICF
    sorteer(
        "Waar hoort dit in het ICF?",
        ["lichaam", "doen", "samen", "externe factoren"],
        [
            ["zijn longen werken minder goed", "lichaam"],
            ["hij kan zich zelf aankleden", "doen"],
            ["hij speelt mee in de voetbalploeg", "samen"],
            ["de school heeft een lift", "externe factoren"],
        ],
        "Lichaam gaat over de werking van de organen, doen over wat iemand zelf doet, samen over meedoen. De omgeving hoort bij de externe factoren."),
    tabel(
        "Klopt dit over de patronen van Gordon?",
        [
            ("Gordon onderscheidt elf patronen.", J),
            ("De patronen hangen met elkaar samen.", J),
            ("Gordon gebruik je om een medische diagnose te stellen.", F),
        ],
        "Met de elf patronen leer je iemand kennen en kijk je naar het geheel. Een diagnose stelt de arts."),

    # Eerste hulp en preventie
    koppel(
        "Koppel de soort preventie aan een voorbeeld.",
        [
            ["primaire preventie", "een vaccinatie tegen mazelen"],
            ["secundaire preventie", "een bevolkingsonderzoek naar kanker"],
            ["tertiaire preventie", "een hartpatiënt helpen om herval te voorkomen"],
        ],
        ["een ziekenwagen bellen"],
        "Primair voorkomt ziekte, secundair spoort ze vroeg op, tertiair beperkt de gevolgen."),
    keuze(
        "AED staat voor automatische externe [[*defibrillator|dokter|diagnose]]. Bij een brandwonde koel je met lauw [[*water|ijs]].",
        "Een AED geeft een schok bij een hartstilstand. Een brandwonde koel je met lauw stromend water, nooit met ijs."),

    # Gezondheid bevorderen en voeding
    inv("Eiwitten en vetten zijn er twee. Hoeveel soorten voedingsstoffen zijn er in totaal? Een getal.",
        ["7"],
        "Eiwitten, vetten, koolhydraten, vitaminen, mineralen, voedingsvezels en water: zeven."),
    sorteer(
        "Is dit een voedingsmiddel of een voedingsstof?",
        ["voedingsmiddel", "voedingsstof"],
        [
            ["een appel", "voedingsmiddel"],
            ["eiwitten", "voedingsstof"],
            ["een boterham", "voedingsmiddel"],
            ["vitaminen", "voedingsstof"],
        ],
        "Een voedingsmiddel is wat je eet. Het bevat meerdere voedingsstoffen."),
    mk("Een jongere drinkt bij elke maaltijd frisdrank. Hoe pas je dat het best aan?",
       ["Water drinken in plaats van frisdrank",
        "Een extra glas frisdrank bij het ontbijt nemen",
        "Een groter glas frisdrank, maar alleen 's avonds",
        "De frisdrank vervangen door een zakje chips"],
       0,
       "Frisdrank levert lege calorieën. Water is de beste dorstlesser."),

    mk("Een oudere vrouw kan niet meer alleen naar de winkel, maar een buurvrouw gaat samen met haar. Wat is die buurvrouw in het ICF?",
       ["Een externe factor die het functioneren helpt",
        "Een persoonlijke factor van de persoon zelf",
        "Een deel van de gezondheidstoestand, bij lichaam",
        "Een stoornis in het onderdeel doen van het ICF"],
       0,
       "Mensen en dingen rond iemand zijn externe factoren. Ze kunnen helpen of hinderen."),
    tabel(
        "Klopt dit over het oor?",
        [
            ("Het orgaan van Corti zit in het slakkenhuis.", J),
            ("De buis van Eustachius verbindt het middenoor met de keel.", J),
            ("Geluidssterkte meet je in hertz.", F),
        ],
        "In het slakkenhuis zetten de zintuigcellen trillingen om in impulsen. Geluidssterkte meet je in decibel."),
    koppel(
        "Koppel de tafeltaak aan de juiste plaats.",
        [
            ["de vork", "links van het bord"],
            ["het mes, met de snijkant naar het bord", "rechts van het bord"],
            ["het dessertbestek", "boven het bord"],
        ],
        ["onder het bord"],
        "Vork links, mes rechts met de snijkant naar het bord, dessertbestek boven het bord."),
    inv("Hoeveel tussendoortjes horen bij een gezond dagmenu? Antwoord met 'twee à drie' of een getal.",
        ["twee à drie", "twee a drie", "2 à 3", "2 a 3", "twee of drie", "2", "3"],
        "Een dagmenu heeft drie hoofdmaaltijden en twee à drie tussendoortjes."),
    sleep(
        "Bij interieurzorg werk je van [[droog]] naar nat. De werkvolgorde is opruimen, schoonmaken en [[nazorg]].",
        ["warm", "ontsmetten"],
        "Eerst droog werken (stof) en dan nat. Nazorg sluit de werkvolgorde af."),
    keuze(
        "Primaire preventie komt [[*voor|nadat]] de ziekte er is. Iemand die gezonde voeding en beweging stimuleert, doet aan [[*gezondheidsbevordering|tertiaire preventie]].",
        "Primaire preventie voorkomt ziekte. Gezondheidsbevordering helpt mensen gezonder te leven."),

    # Voedselveiligheid en bewaren
    tabel(
        "Klopt dit over bewaren?",
        [
            ("Na de TGT-datum gooi je het product weg.", J),
            ("Na de THT-datum kijk en ruik je eerst.", J),
            ("Ontdooid vlees mag je opnieuw invriezen.", F),
            ("Je ontdooit vlees het veiligst in de koelkast.", J),
        ],
        "TGT is te gebruiken tot: daarna niet meer eten. THT is ten minste houdbaar tot. Ontdooid vlees vries je niet opnieuw in."),
    keuze(
        "Een schimmel op confituur mag je er [[*niet|gewoon]] afscheppen. Restjes van gisteren bewaar je in een [[*afgesloten doos|open schaal]].",
        "Schimmeldraden zitten dieper dan je ziet. Een afgesloten doos houdt kiemen buiten en geur binnen."),

    # Kwaliteitsbewust handelen
    volgorde(
        "Je krijgt een nieuwe opdracht in de zorg en werkt volgens OVUR. Zet de vier stappen in de juiste volgorde.",
        ["oriënteren", "voorbereiden", "uitvoeren", "reflecteren"],
        "Je oriënteert je eerst, bereidt voor, voert uit en blikt tot slot terug."),
    sleep(
        "Bij de Sinner-cirkel werken chemie, [[temperatuur]], tijd en de [[mechanische handeling]] samen. Minder chemie vul je aan met meer tijd, warmte of wrijving.",
        ["kleur", "geur"],
        "De vier factoren van de Sinner-cirkel kan je tegen elkaar inruilen."),
    tabel(
        "Klopt dit over veilig schoonmaken?",
        [
            ("Bleekwater meng je niet met een ander product.", J),
            ("Ontsmetten doe je nadat je hebt schoongemaakt.", J),
            ("Je werkt met een sterk product best met het raam dicht.", F),
        ],
        "Bleekwater met een ander product kan giftige dampen geven. Je ontsmet een proper oppervlak. Met een sterk product zet je het raam open."),

    # Woonomgeving en linnenzorg
    mk("In de badkamer groeit schimmel op de muur. Wat helpt het meest?",
       ["Na het douchen kort en krachtig verluchten",
        "De deur van de badkamer altijd goed dicht laten",
        "Alleen in de zomer het raam eens openzetten",
        "De verwarming in de badkamer helemaal uitzetten"],
       0,
       "Schimmel groeit op een muur die vochtig blijft. Door kort en krachtig te verluchten, gaat de vochtige lucht naar buiten."),
    volgorde(
        "Zet de stappen van de was in de juiste volgorde.",
        ["verzamelen", "sorteren", "controleren", "wassen", "drogen"],
        "Je verzamelt en sorteert de was, controleert zakken, ritsen en vlekken, en wast en droogt daarna. Kastklaar maken en strijken komen als laatste."),
    keuze(
        "Een doorstreept symbool op het onderhoudsetiket betekent dat de behandeling [[*niet mag|verplicht is]]. Een overladen trommel wast [[*minder goed|beter]].",
        "Doorstreept betekent: niet doen. In een te volle trommel kan het wasgoed niet goed bewegen."),

    casus(
        "Noor (16) voelt zich al weken moe. Ze slaapt slecht door haar gsm in bed, slaat het ontbijt over en eet 's middags vaak chips en een frisdrank. Ze sport niet meer sinds ze van school veranderde, en heeft er nog geen nieuwe vrienden.",
        [
            sorteer(
                "Onder welk patroon van Gordon valt dit?",
                ["slaap en rust", "voeding", "activiteiten", "rol en relatie"],
                [
                    ["slecht slapen door de gsm", "slaap en rust"],
                    ["ontbijt overslaan", "voeding"],
                    ["niet meer sporten", "activiteiten"],
                    ["nog geen nieuwe vrienden", "rol en relatie"],
                ],
                "Elke klacht hoort bij een patroon, en de patronen hangen samen: slecht slapen maakt moe en minder actief."),
            mk("Welk advies past het best bij Noors voeding?",
               ["Elke dag ontbijten en chips vervangen door fruit",
                "Een extra frisdrank om energie te krijgen 's middags",
                "Het middageten overslaan en 's avonds meer eten",
                "Alleen nog eiwitten eten en geen koolhydraten meer"],
               0,
               "Het ontbijt levert een flink deel van de energie voor de dag. Fruit is een gezond tussendoortje, chips en frisdrank leveren lege calorieën."),
        ]),

    open_("Geef Noor twee concrete tips voor een betere slaaphygiëne en leg bij elke tip uit waarom die helpt.",
          "Tip 1: leg je gsm een uur voor het slapen weg, buiten je slaapkamer. Het licht en de berichten houden je wakker. Tip 2: ga elke dag op hetzelfde uur slapen en verlucht je kamer. Een vast ritme en frisse, koele lucht helpen je sneller in slaap te vallen.",
          "Een goed antwoord geeft twee haalbare tips (bv. schermen weg, vast slaapritme, frisse kamer) met telkens een reden."),
]
