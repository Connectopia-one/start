"""Het zenuwstelsel — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Een neuron, zonder namen ----------------------------------------------
NEU = Prent("neuron", "Een zenuwcel", "neuron met dendrieten, cellichaam met kern, axon met myelineschede en knopen van Ranvier, eindknopjes")
for (x, y) in [(80, 230), (65, 320), (85, 410), (140, 220), (140, 420)]:
    NEU.lijn(180, 320, x, y, DONKER, 4)
    NEU.lijn(x, y, x - 25, y - 18, DONKER, 2)
    NEU.lijn(x, y, x - 22, y + 16, DONKER, 2)
NEU.cirkel(180, 320, 50, "#f1d9a8")
NEU.cirkel(180, 320, 18, PAARS)
NEU.lijn(230, 320, 820, 320, DONKER, 6)
SEG = [260 + i * 110 for i in range(5)]
for x in SEG:
    NEU.rect(x, 300, 90, 40, "#f7f0c8", DONKER, 18)
for (x, y) in [(880, 250), (895, 320), (880, 390)]:
    NEU.lijn(820, 320, x, y, DONKER, 4)
    NEU.cirkel(x, y, 14, ORANJE)
NEU.tekst(500, 470, "Het signaal loopt van links naar rechts.", 18)
Z_DENDRIET = Prent.zone(35, 200, 100, 240)
Z_CELLICHAAM = Prent.rond(180, 320, 52)
Z_KNOPEN = [Prent.zone(x + 88, 296, 24, 48) for x in SEG[:-1]]
Z_MYELINE = [Prent.zone(x + 4, 296, 82, 48) for x in SEG]
Z_EIND = [Prent.rond(x, y, 24) for (x, y) in [(880, 250), (895, 320), (880, 390)]]

# Een actiepotentiaal ---------------------------------------------------
def X(t):
    return 120 + t * 133.3
def Y(v):
    return 560 - (v + 90) * (460 / 130)
AP = Prent("actiepotentiaal", "Spanning over het membraan van een neuron", "grafiek van een actiepotentiaal met rustpotentiaal, depolarisatie, repolarisatie en herstelfase")
AP.lijn(120, 560, 930, 560, DONKER, 2)
AP.lijn(120, 560, 120, 90, DONKER, 2)
for v in (-70, 0, 30):
    AP.lijn(112, Y(v), 120, Y(v), DONKER, 2)
    AP.tekst(105, Y(v) + 6, f"{v:+d}".replace("+0", "0").replace("-", "−"), 16, "end")
AP.lijn(120, Y(-55), 930, Y(-55), "#999999", 2, True)
AP.tekst(925, Y(-55) - 8, "drempelwaarde", 16, "end", "#666666")
AP.tekst(60, 80, "spanning (mV)", 16, "start")
AP.tekst(925, 595, "tijd (ms)", 16, "end")
pts = [(0, -70), (1.5, -70), (1.8, -55), (2.3, 30), (3.0, -70), (3.3, -82), (4.5, -70), (6, -70)]
AP.pad("M" + " L ".join(f"{X(t):.1f} {Y(v):.1f}" for t, v in pts), "none", BLAUW, 4)
Z_RUST = Prent.zone(X(0), Y(-62), X(1.5) - X(0), Y(-78) - Y(-62))
Z_DEPOL = Prent.zone(X(1.75), Y(32), X(2.3) - X(1.75), Y(-58) - Y(32))
Z_REPOL = Prent.zone(X(2.3), Y(32), X(2.98) - X(2.3), Y(-66) - Y(32))
Z_HERSTEL = Prent.zone(X(3.0), Y(-68), X(4.5) - X(3.0), Y(-88) - Y(-68))

VRAGEN = [
    klik(
        "Klik op het deel van de zenuwcel dat signalen opvangt.",
        NEU.bestand, [Z_DENDRIET],
        "De dendrieten vangen signalen op, het axon geeft ze door.",
    ),
    klik(
        "Klik op het deel waar de celkern ligt.",
        NEU.bestand, [Z_CELLICHAAM],
        "De celkern ligt in het cellichaam, niet in het axon.",
    ),
    klik(
        "Klik op een plek waar de impuls naartoe springt, tussen twee cellen van Schwann.",
        NEU.bestand, Z_KNOPEN,
        "Een knoop van Ranvier is een onbeklede plek tussen twee cellen van Schwann.",
    ),
    klik(
        "Klik op een plek waar de neurotransmitter vrijkomt.",
        NEU.bestand, Z_EIND,
        "In de eindknopjes liggen blaasjes met neurotransmitter klaar.",
    ),
    klik(
        "Klik op het isolerende, vetachtige omhulsel rond het axon.",
        NEU.bestand, Z_MYELINE,
        "De myelineschede wordt gemaakt door de cellen van Schwann.",
    ),
    klik(
        "Klik op het deel van de grafiek waar de binnenkant van het neuron even positief wordt.",
        AP.bestand, [Z_DEPOL],
        "Bij depolarisatie slaat het spanningsverschil kortstondig om.",
    ),
    klik(
        "Klik op het deel van de grafiek waar het neuron nog niet opnieuw kan vuren.",
        AP.bestand, [Z_HERSTEL],
        "In de herstelfase moet het membraan eerst zijn rustpotentiaal terugkrijgen.",
    ),
    klik(
        "Klik op het deel van de grafiek waar het neuron in rust is.",
        AP.bestand, [Z_RUST],
        "In rust is de binnenkant negatief ten opzichte van de buitenkant: de rustpotentiaal.",
    ),
    met_prent(AP.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("Pas boven de stippellijn ontstaat een impuls.", J),
            ("De rustpotentiaal ligt rond −70 mV.", J),
            ("Na de top keert de spanning terug: repolarisatie.", J),
            ("Een sterkere prikkel maakt de top hoger.", F),
        ],
        "De amplitude ligt vast. Een sterkere prikkel geeft meer impulsen per seconde.",
    )),
    tabel(
        "Hoort dit bij het centrale of het perifere zenuwstelsel?",
        [
            ("de hersenen", "Centraal"),
            ("het ruggenmerg", "Centraal"),
            ("de ruggenmergzenuwen", "Perifeer"),
            ("de grensstrengen", "Perifeer"),
            ("de hersenzenuwen", "Perifeer"),
        ],
        "Alles buiten de hersenen en het ruggenmerg hoort bij het perifere stelsel.",
        kolommen=["Centraal", "Perifeer"],
    ),
    tabel(
        "Sympathisch of parasympathisch?",
        [
            ("De hartslag versnelt voor een examen.", "Sympathisch"),
            ("De pupillen verwijden bij schrik.", "Sympathisch"),
            ("De spijsvertering komt op gang na het eten.", "Parasympathisch"),
            ("De hartslag vertraagt als je rust.", "Parasympathisch"),
        ],
        "Het sympathische deel zet het lichaam klaar voor actie, het parasympathische is het rustsysteem.",
        kolommen=["Sympathisch", "Parasympathisch"],
    ),
    volgorde(
        "Zet de weg van een terugtrekreflex in de juiste volgorde.",
        ["Receptor in de huid", "Sensorisch neuron", "Schakelneuron in het ruggenmerg", "Motorisch neuron", "Spier"],
        "Het signaal wordt in het ruggenmerg overgeschakeld en gaat niet eerst naar de grote hersenen.",
    ),
    volgorde(
        "Zet de fasen van een actiepotentiaal in de juiste volgorde.",
        ["Rustpotentiaal", "Depolarisatie", "Repolarisatie", "Herstelfase"],
        "Daarna staat het neuron weer klaar voor een nieuwe impuls.",
    ),
    casus(
        "Tijdens het koken raakt Jonas een hete ovenschaal. Zijn hand schiet weg. Een fractie later voelt hij de pijn.",
        [
            mk(
                "Waar wordt het signaal van zijn reflex overgeschakeld?",
                ["In het ruggenmerg", "In de grote hersenen", "In de grensstrengen", "In de hand zelf"],
                0,
                "Een schakelneuron in het ruggenmerg verbindt het sensorische met het motorische neuron.",
            ),
            mk(
                "Waarom voelt Jonas de pijn pas na het wegtrekken?",
                [
                    "Pijn ontstaat in de hersenen en die weg is langer",
                    "Het motorische neuron is trager dan het sensorische",
                    "De pijnreceptoren in de huid reageren altijd te laat",
                    "De spier stuurt het pijnsignaal pas na de beweging",
                ],
                0,
                "De reflexboog is korter en al klaar voor het signaal de hersenen bereikt.",
            ),
            tabel(
                "Klopt dit over de reflex van Jonas?",
                [
                    ("Ze loopt via een reflexboog.", J),
                    ("Zijn armspier is de effector.", J),
                    ("Hij besliste zelf bewust om weg te trekken.", F),
                ],
                "Een reflex gaat vanzelf, zonder dat de hersenschors eerst beslist.",
            ),
        ],
    ),
    sorteer(
        "Is dit een reflex of een gewilde beweging?",
        ["Reflex", "Gewild"],
        [
            ["de pupil die kleiner wordt bij fel licht", "Reflex"],
            ["het been dat opveert na een tik onder de knie", "Reflex"],
            ["melk die toeschiet als de baby zuigt", "Reflex"],
            ["je veters knopen", "Gewild"],
            ["een bal gooien naar een vriend", "Gewild"],
        ],
        "Een gewilde beweging vertrekt in de hersenschors.",
    ),
    sleep(
        "In de synaps stort het [[eindknopje]] blaasjes met [[neurotransmitter]] leeg in de [[synaptische spleet]]. De stof past op [[receptoren]] aan de overkant.",
        ["myelineschede", "dendrietkern"],
        "In de synaps wordt het elektrische signaal even chemisch.",
    ),
    mk(
        "Waarom gaat een signaal in een synaps maar één kant op?",
        [
            "Zender en ontvanger zijn anders gebouwd",
            "De neurotransmitter is zwaarder dan bloed",
            "De myelineschede blokkeert de andere kant",
            "Het axon is langer dan de dendrieten samen",
        ],
        0,
        "Alleen het eindknopje heeft blaasjes en alleen de overkant heeft receptoren.",
    ),
    koppel(
        "Koppel het soort neuron aan zijn taak.",
        [
            ("sensorisch neuron", "Brengt het signaal van een zintuig naar binnen."),
            ("schakelneuron", "Verbindt binnen het ruggenmerg twee neuronen."),
            ("motorisch neuron", "Brengt een bevel naar een spier of klier."),
        ],
        ["Maakt de myelineschede rond een axon."],
        "De myelineschede wordt gemaakt door de cellen van Schwann.",
    ),
    tabel(
        "Klopt dit over zenuwen?",
        [
            ("Een zenuw is een bundel uitlopers van veel cellen.", J),
            ("Een gemengde zenuw bevat sensorische en motorische vezels.", J),
            ("Een zenuw is één heel lange cel.", F),
            ("De meeste ruggenmergzenuwen zijn gemengd.", J),
            ("De grensstrengen horen bij het animale stelsel.", F),
        ],
        "De grensstrengen horen bij het autonome stelsel.",
    ),
    keuze(
        "Een prikkel wordt sterker. In één zenuwvezel volgen er dan [[*meer impulsen per seconde|grotere impulsen|tragere impulsen]].",
        "De amplitude ligt vast. Zo weten de hersenen hoe sterk de prikkel is.",
    ),
    mk(
        "Waarom gaat een impuls sneller over een vezel met myeline?",
        [
            "Hij springt van knoop tot knoop",
            "Er zitten geen dendrieten op die vezel",
            "Er komt daar meer neurotransmitter vrij",
            "Het cellichaam ligt dichter bij de spier",
        ],
        0,
        "Dat springen heet saltatoire geleiding.",
    ),
    mk(
        "Een prikkel blijft net onder de drempelwaarde. Wat gebeurt er?",
        [
            "Er ontstaat geen impuls",
            "Er ontstaat een kleine impuls",
            "Er ontstaat een trage impuls langs de dendrieten",
            "De impuls gaat enkel naar het ruggenmerg",
        ],
        0,
        "Het is alles of niets: pas boven de drempelwaarde vuurt het neuron.",
    ),
    klik(
        "Klik op het deel van de grafiek waar de rusttoestand terugkeert na de top.",
        AP.bestand, [Z_REPOL],
        "Bij repolarisatie keert de spanning terug naar negatief.",
    ),
    tabel(
        "Animaal of autonoom zenuwstelsel?",
        [
            ("je arm optillen om een vraag te stellen", "Animaal"),
            ("je hartslag die versnelt bij het lopen", "Autonoom"),
            ("een woord op je blad schrijven", "Animaal"),
            ("de spijsvertering na het middagmaal", "Autonoom"),
        ],
        "Het animale deel staat onder je wil, het autonome regelt wat vanzelf doorgaat.",
        kolommen=["Animaal", "Autonoom"],
    ),
    keuze(
        "Een motorisch neuron brengt een bevel naar een [[*spier of klier|receptor in de huid|zintuigcel in het oog]].",
        "Spieren en klieren zijn de effectoren.",
    ),
    tabel(
        "Klopt dit over de impuls?",
        [
            ("Binnen het neuron is het signaal elektrisch.", J),
            ("In de synaps wordt het signaal even chemisch.", J),
            ("Neuronen raken elkaar in de synaps rechtstreeks.", F),
            ("Een neurotransmitter past maar op bepaalde receptoren.", J),
        ],
        "De neurotransmitter zwemt door de spleet naar de overkant.",
    ),
    mk(
        "Welk hormoon laat bij de toeschietreflex de melk vrijkomen?",
        ["Oxytocine", "Auxine", "Neurotransmitter", "Myeline"],
        0,
        "Het zuigen van de baby is de prikkel, oxytocine laat de melk toeschieten.",
    ),
    open_(
        "Leg uit wat er in een synaps gebeurt, van de aankomst van de impuls tot het signaal in het volgende neuron. Gebruik de woorden eindknopje, neurotransmitter en receptor.",
        "De impuls komt aan in het eindknopje. Daar lopen blaasjes leeg en komt neurotransmitter vrij in de synaptische spleet. De stof zwemt naar de overkant en past volgens het sleutel-slotprincipe op receptoren in het membraan van het volgende neuron. Daar wordt het signaal weer elektrisch.",
    ),
]
