"""Wetenschappelijk onderzoek, ontwerpen en STEM — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Vier schietschijven -----------------------------------------------------------
SS = Prent("schietschijven", "Vier reeksen metingen als treffers op een schijf", "vier schietschijven met telkens vijf treffers; het midden is de echte waarde; letters P tot S")
TREF = {
    "P": [(0, 0), (6, -4), (-5, 5), (4, 6), (-6, -3)],
    "Q": [(45, -40), (51, -44), (40, -35), (48, -34), (42, -46)],
    "R": [(0, -60), (55, 15), (-50, 30), (20, 55), (-35, -40)],
    "S": [(55, 40), (-20, 70), (65, -10), (30, 72), (70, 35)],
}
for i, (k, pts) in enumerate(TREF.items()):
    cx, cy = 130 + i * 245, 290
    for r, kl in ((100, "#ffffff"), (75, "#f3e3c8"), (50, "#ffffff"), (25, "#f3e3c8")):
        SS.cirkel(cx, cy, r, kl, DONKER, 2)
    SS.cirkel(cx, cy, 4, DONKER, DONKER, 1)
    for (dx, dy) in pts:
        SS.cirkel(cx + dx, cy + dy, 7, ROOD, DONKER, 1)
    SS.letter(cx, 440, k)
ZSS = {k: [Prent.rond(130 + i * 245, 290, 102), Prent.rond(130 + i * 245, 440, 22)] for i, k in enumerate(TREF)}

# Meetreeks met een uitschieter ---------------------------------------------
MR = Prent("meetreeks-magnesium", "Tijd tot een stukje magnesium in zoutzuur verdwenen is, bij verschillende temperaturen", "assenstelsel met de temperatuur horizontaal en de tijd verticaal; vijf meetpunten die dalen, één punt ligt duidelijk hoger; letters A tot E")
X, Y = assen(MR, 10, 60, 0, 200, "temperatuur (°C)", "tijd (s)", 10, 50, links=140, rechts=880)
PUNT = {"A": (20, 160), "B": (30, 110), "C": (40, 150), "D": (50, 55), "E": (60, 40)}
MR.pad("M " + " L ".join(f"{X(t):.1f} {Y(160 * 0.69 ** ((t - 20) / 10)):.1f}" for t in range(18, 62, 2)), "none", GRIJS, 2)
for k, (t, v) in PUNT.items():
    MR.cirkel(X(t), Y(v), 8, BLAUW, DONKER, 2)
    MR.letter(X(t) + 28, Y(v) - 28, k)
ZMR = {k: [Prent.rond(X(t), Y(v), 24), Prent.rond(X(t) + 28, Y(v) - 28, 22)] for k, (t, v) in PUNT.items()}

VRAGEN = [
    klik(
        "Klik op de reeks metingen die precies maar niet nauwkeurig is.",
        SS.bestand, ZSS["Q"],
        "De treffers liggen dicht bij elkaar, maar ver van het midden: een systematische fout.",
    ),
    klik(
        "Klik op de reeks die gemiddeld juist uitkomt, maar met veel spreiding.",
        SS.bestand, ZSS["R"],
        "Toevallige fouten: ze vallen weg in het gemiddelde.",
    ),
    met_prent(SS.bestand, tabel(
        "Hoe zou je deze reeks beschrijven?",
        [
            ("P", "Nauwkeurig en precies"),
            ("Q", "Precies, niet nauwkeurig"),
            ("S", "Geen van beide"),
        ],
        "Nauwkeurig: dicht bij de echte waarde. Precies: dicht bij elkaar.",
        kolommen=["Nauwkeurig en precies", "Precies, niet nauwkeurig", "Geen van beide"],
    )),
    met_prent(SS.bestand, mk(
        "Welk soort fout zit er vooral in reeks Q?",
        [
            "Een systematische fout",
            "Een toevallige fout bij elke meting",
            "Geen fout, enkel wat pech",
            "Een fout bij het noteren",
        ],
        0,
        "Alle metingen wijken naar dezelfde kant af, bijvoorbeeld door een slecht afgestelde balans.",
    )),
    klik(
        "Klik op de meting die waarschijnlijk een uitschieter is.",
        MR.bestand, ZMR["C"],
        "Bij hogere temperatuur verwacht je een kortere tijd, maar C ligt veel hoger dan B.",
    ),
    met_prent(MR.bestand, tabel(
        "Welke rol speelt deze grootheid in de proef?",
        [
            ("de temperatuur", "Onafhankelijk"),
            ("de tijd tot het magnesium weg is", "Afhankelijk"),
            ("de concentratie van het zoutzuur", "Constant"),
            ("de lengte van het stukje magnesium", "Constant"),
        ],
        "Je stelt de temperatuur in, meet de tijd en houdt de rest gelijk.",
        kolommen=["Onafhankelijk", "Afhankelijk", "Constant"],
    )),
    met_prent(MR.bestand, mk(
        "Wat doe je best met meting C?",
        [
            "Opnieuw meten en de oorzaak zoeken",
            "Ze stil weglaten uit het verslag en verder gaan",
            "Ze aanpassen tot ze netjes in de lijn past",
            "De hele proef als mislukt beschouwen en stoppen",
        ],
        0,
        "Een uitschieter noteer je en verklaar je; je mag ze niet zomaar weglaten.",
    )),
    met_prent(MR.bestand, keuze(
        "De metingen ondersteunen de hypothese dat een hogere temperatuur de reactie [[*sneller|trager]] maakt.",
        "De tijd wordt korter bij hogere temperatuur.",
    )),
    tabel(
        "Is dit een onderzoeksvraag of een ontwerpvraag?",
        [
            ("Hoe beïnvloedt de temperatuur de oplossnelheid van suiker?", "Onderzoek"),
            ("Maak een filter dat 90 % van het zand uit water haalt.", "Ontwerp"),
            ("Welk metaal reageert het snelst met zoutzuur?", "Onderzoek"),
            ("Bouw een toestel dat een ei bij een val heel houdt.", "Ontwerp"),
        ],
        "Een onderzoeksvraag zoekt kennis, een ontwerpvraag zoekt een oplossing.",
        kolommen=["Onderzoek", "Ontwerp"],
    ),
    tabel(
        "Is dit een criterium of een randvoorwaarde bij het ontwerp van een waterfilter?",
        [
            ("het filter haalt minstens 90 % van het zand eruit", "Criterium"),
            ("je hebt maar 10 euro", "Randvoorwaarde"),
            ("het water loopt er binnen 5 minuten door", "Criterium"),
            ("je mag alleen materiaal uit de klas gebruiken", "Randvoorwaarde"),
        ],
        "Een criterium is een eis aan de oplossing, een randvoorwaarde een beperking van de middelen.",
        kolommen=["Criterium", "Randvoorwaarde"],
    ),
    volgorde(
        "Zet de stappen van een onderzoek in de goede volgorde.",
        [
            "Onderzoeksvraag",
            "Hypothese",
            "Proefopzet met variabelen",
            "Meten en herhalen",
            "Besluit",
            "Rapporteren",
        ],
        "Het besluit antwoordt op de vraag en zegt of de hypothese klopt.",
    ),
    volgorde(
        "Zet de stappen van een ontwerpproces in de goede volgorde.",
        [
            "Ontwerpvraag opstellen",
            "Criteria en randvoorwaarden vastleggen",
            "Opsplitsen in deelproblemen",
            "Een prototype bouwen",
            "Testen en bijsturen",
        ],
        "Testen en bijsturen gebeurt vaak in meerdere rondes.",
    ),
    casus(
        "Lotte onderzoekt of zout het roesten van ijzer versnelt. Ze legt nagels in zout water.",
        [
            mk(
                "Welke controleproef heeft ze nodig?",
                [
                    "Nagels in water zonder zout",
                    "Nagels in nog zouter water",
                    "Geen nagels in zout water",
                    "Koperen nagels in zout water",
                ],
                0,
                "Alleen de factor zout mag verschillen.",
            ),
            keuze(
                "De onafhankelijke variabele is [[*de hoeveelheid zout|de hoeveelheid roest|het soort nagel]].",
                "Die stelt Lotte zelf in.",
            ),
            tabel(
                "Moet Lotte dit gelijk houden in alle bekers?",
                [
                    ("het soort nagel", "Ja"),
                    ("de hoeveelheid water", "Ja"),
                    ("de hoeveelheid zout", "Nee"),
                ],
                "Alles behalve de onafhankelijke variabele houd je constant.",
                kolommen=["Ja", "Nee"],
            ),
        ],
    ),
    mk(
        "Lotte meet de roesttijd vijf keer in plaats van één keer. Wat wint ze daarmee?",
        [
            "Toevallige afwijkingen vallen weg",
            "Een systematische fout verdwijnt vanzelf mee",
            "Haar hypothese klopt daardoor zeker wel",
            "Niets, één goede meting is altijd genoeg",
        ],
        0,
        "Een systematische fout verdwijnt niet door te herhalen.",
    ),
    tabel(
        "Klopt dit over een goede grafiek?",
        [
            ("Ze heeft een titel.", J),
            ("Op elke as staat een grootheid met eenheid.", J),
            ("De onafhankelijke variabele staat op de horizontale as.", J),
            ("Een uitschieter laat je weg zonder iets te zeggen.", F),
        ],
        "Een uitschieter vermeld je en verklaar je.",
    ),
    koppel(
        "Koppel elke letter van STEM aan zijn betekenis.",
        [
            ("S", "science"),
            ("T", "technology"),
            ("E", "engineering"),
            ("M", "mathematics"),
        ],
        ["economy"],
        "De vier horen samen bij een technisch probleem.",
    ),
    mk(
        "Een reactie loopt rustig in een proefbuis, maar in een reactor van 10 000 liter wordt ze te heet. Wat is een logische oorzaak?",
        [
            "Warmte raakt minder vlot weg",
            "In het groot gelden andere atoommassa's",
            "Een grote reactor bevat altijd een katalysator",
            "Grote hoeveelheden reageren volgens een andere vergelijking",
        ],
        0,
        "Een grote reactor koelt en mengt minder makkelijk dan een proefbuis.",
    ),
    sleep(
        "Een [[hypothese]] is een onderbouwd vermoeden dat je kan testen. Een [[controleproef]] toont wat er gebeurt zonder de behandeling. Vakgenoten kijken het werk na bij [[peer review]].",
        ["besluit", "prototype", "greenwashing"],
        "Zo wordt onderzoek betrouwbaar.",
    ),
    tabel(
        "Hoort deze vraag bij het beoordelen van een nieuwe chemische toepassing?",
        [
            ("Wat gebeurt er met de stof na gebruik?", "Ja"),
            ("Is het proces veilig voor de werknemers?", "Ja"),
            ("Wat kost het proces?", "Ja"),
            ("Welke kleur heeft de verpakking van de onderzoeker?", "Nee"),
        ],
        "Milieu, veiligheid en kostprijs spelen allemaal mee.",
        kolommen=["Ja", "Nee"],
    ),
    keuze(
        "Een reeks met een slecht afgestelde balans geeft een [[*systematische|toevallige]] fout.",
        "Alle metingen wijken dan op dezelfde manier af.",
    ),
    inv(
        "Vijf metingen van een tijd: 42, 40, 44, 41 en 43 s. Wat is het gemiddelde in seconden?",
        ["42", "42 s"],
        "(42 + 40 + 44 + 41 + 43) / 5 = 210 / 5 = 42.",
    ),
    open_(
        "Leg uit waarom een verworpen hypothese het onderzoek niet waardeloos maakt.",
        "Ook een verworpen hypothese is een antwoord op de onderzoeksvraag: je weet nu dat het vermoeden niet klopt. Dat is nieuwe kennis waarmee je een betere hypothese kan opstellen. Zolang de proef goed opgezet en uitgevoerd is, is het resultaat betrouwbaar en bruikbaar.",
    ),
    klik(
        "Klik op de reeks met een systematische fout én veel spreiding.",
        SS.bestand, ZSS["S"],
        "De treffers liggen allemaal rechtsboven, maar ook ver uit elkaar.",
    ),
    inv(
        "Een balans geeft voor een blokje van echt 13,0 g: 12,0 – 12,2 – 11,8 – 12,0 g. Hoeveel gram wijkt het gemiddelde af van de echte waarde?",
        ["1", "1,0", "1 g", "1,0 g"],
        "Het gemiddelde is 12,0 g, dus 1,0 g te laag: een systematische fout.",
    ),
    sorteer(
        "Gaat het om een toevallige of een systematische fout?",
        ["Toevallig", "Systematisch"],
        [
            ("je drukt de stopwatch telkens een tikje anders in", "Toevallig"),
            ("de thermometer wijst altijd 2 °C te hoog", "Systematisch"),
            ("de balans staat bij de start niet op nul", "Systematisch"),
            ("je leest de maatcilinder soms iets schuin af", "Toevallig"),
        ],
        "Een systematische fout wijkt altijd naar dezelfde kant af.",
    ),
    mk(
        "Een ander labo voert de proef uit met hetzelfde voorschrift en vindt dezelfde resultaten. Wat toont dat?",
        [
            "Dat het resultaat reproduceerbaar is",
            "Dat de hypothese voor altijd bewezen is",
            "Dat er geen controleproef meer nodig was",
            "Dat de metingen niet herhaald moesten worden",
        ],
        0,
        "Reproduceerbaar: anderen krijgen met dezelfde werkwijze hetzelfde.",
    ),
    keuze(
        "Na een test blijkt het waterfilter te traag. Je [[stopt het ontwerp|*past het prototype aan en test opnieuw|schrapt het criterium over de tijd]].",
        "Testen en bijsturen hoort bij het ontwerpproces.",
    ),
    mk(
        "Waarom splits je een groot ontwerpprobleem op in deelproblemen?",
        [
            "Kleine stukken zijn makkelijker op te lossen",
            "Dan heb je geen criteria of randvoorwaarden meer nodig",
            "Dan hoef je het prototype nooit meer te testen",
            "Zo wordt het ontwerp vanzelf goedkoper dan gepland",
        ],
        0,
        "Per deelprobleem zoek je een oplossing en daarna voeg je ze samen.",
    ),
]
