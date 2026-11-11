"""De arbeidsmarkt, werkloosheid en arbeidsmarktindicatoren — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

G = venster("arbeid-minimumloon", 0, 16, 0, 24, 2, 4)
PUNTEN = {"E": (8, 12), "F": (5, 15), "G": (11, 15)}

GRAFIEKEN = [
    dict(naam=G, titel="Arbeidsmarkt (arbeid in honderden personen, loon in euro per uur)",
         krommen=[(lambda l: 20 - l, "groen", "vraag", (0, 16)), (lambda l: 4 + l, "blauw", "aanbod", (0, 16))],
         stippel=[("h", 15)],
         labelplek={"vraag": (15, 5), "aanbod": (14.5, 18.5)},
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="arbeid", ylabel="loon", ijk_x=2, ijk_y=4),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"] + ", minimumloon 15", vragen="klikvragen over werkloosheid door een minimumloon")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "Er geldt een minimumloon van 15 euro per uur. Klik op het punt dat toont hoeveel mensen werkgevers dan in dienst nemen.",
        P, [punt_zone(G, *PUNTEN["F"])],
        "Werkgevers vragen arbeid: bij 15 euro lees je op de vraagcurve 5, dus 500 mensen. Dat is punt F.",
    ),
    klik(
        "Bij hetzelfde minimumloon: klik op de plaats die de werkloosheid toont.",
        P, [vak_zone(G, 6, 10, 14, 16)],
        "De werkloosheid is het stuk tussen de vraag (F) en het aanbod (G) bij 15 euro: van 5 tot 11.",
    ),
    met_prent(P, inv(
        "Hoeveel werklozen zijn er bij het minimumloon van 15 euro? Schrijf het aantal personen.",
        "600",
        "Aanbod 1 100, vraag 500: 1 100 − 500 = 600 werklozen.",
    )),
    met_prent(P, mk(
        "Wat stelt punt E voor?",
        ["Het evenwichtsloon en de evenwichtstewerkstelling", "Het minimumloon en het aantal werklozen",
         "Het hoogste loon dat werkgevers kunnen betalen", "Het aantal mensen op arbeidsleeftijd"],
        0,
        "In het snijpunt van vraag en aanbod van arbeid: loon 12 en 800 werkenden.",
    )),
    met_prent(P, mk(
        "Het minimumloon zakt naar 10 euro per uur. Wat gebeurt er?",
        ["Niets: een minimumloon onder het evenwichtsloon van 12 heeft geen effect",
         "Er ontstaat een tekort aan arbeidskrachten, want 10 ligt onder het evenwicht",
         "De werkloosheid stijgt, want werknemers verdienen minder",
         "Het loon wordt 10, want werkgevers betalen altijd het minimum"],
        0,
        "Een minimumloon legt enkel een ondergrens. Ligt die onder 12, dan blijft de markt in het evenwicht.",
    )),
    keuze(
        "Op de arbeidsmarkt [[*vragen|bieden]] de werkgevers arbeid, en de [[*werknemers|werkgevers]] bieden arbeid aan. De prijs van arbeid is het [[*loon|kapitaal]].",
        "Het is een beetje omgekeerd ten opzichte van een goederenmarkt: bedrijven zijn hier de kopers.",
    ),
    tabel(
        "Ligt het loon boven of onder het evenwichtsloon? Wat is het gevolg?",
        [
            ("Loon boven het evenwichtsloon", "Werkloosheid"),
            ("Loon onder het evenwichtsloon", "Tekort aan arbeidskrachten"),
            ("Loon gelijk aan het evenwichtsloon", "Evenwicht"),
        ],
        "Boven het evenwicht willen meer mensen werken dan er gevraagd worden; eronder is het omgekeerd.",
        kolommen=["Werkloosheid", "Tekort aan arbeidskrachten", "Evenwicht"],
    ),
    casus(
        "Een land telt 2 000 000 mensen op arbeidsleeftijd. Er zijn 1 360 000 werkenden en 240 000 werklozen.",
        [
            inv("Hoe groot is de beroepsbevolking? Schrijf het getal zonder spaties.", "1600000",
                "Werkenden + werklozen = 1 360 000 + 240 000 = 1 600 000."),
            inv("Bereken de activiteitsgraad in procent. Schrijf enkel het getal.", "80",
                "1 600 000 / 2 000 000 = 80 %."),
            inv("Bereken de werkzaamheidsgraad in procent. Schrijf enkel het getal.", "68",
                "1 360 000 / 2 000 000 = 68 %."),
            inv("Bereken de werkloosheidsgraad in procent. Schrijf enkel het getal.", "15",
                "240 000 / 1 600 000 = 15 %. Je deelt door de beroepsbevolking, niet door de hele bevolking."),
        ],
    ),
    mk(
        "Een leerling berekent de werkloosheidsgraad als werklozen gedeeld door de bevolking op arbeidsleeftijd. Wat is er mis?",
        ["Hij moet delen door de beroepsbevolking, niet door de bevolking op arbeidsleeftijd",
         "Hij moet delen door het aantal werkenden, want werklozen tellen niet mee",
         "Hij moet de werklozen optellen bij de gepensioneerden en dan delen door de bevolking",
         "Er is niets mis: zo bereken je de werkloosheidsgraad in België"],
        0,
        "Werkloosheidsgraad = werklozen / beroepsbevolking.",
    ),
    sorteer(
        "Hoort deze persoon bij de beroepsbevolking?",
        ["Wel", "Niet"],
        [
            ["Een verpleegster die voltijds werkt", "Wel"],
            ["Een werkloze die actief een job zoekt", "Wel"],
            ["Een gepensioneerde leerkracht", "Niet"],
            ["Een voltijdse student", "Niet"],
            ["Een ontmoedigde werkloze die gestopt is met zoeken", "Niet"],
        ],
        "De beroepsbevolking zijn de werkenden en de werklozen. Wie stopt met zoeken, telt niet meer mee.",
    ),
    mk(
        "Veel ontmoedigde werklozen stoppen met zoeken. Wat gebeurt er met de werkloosheidsgraad?",
        ["Ze kan dalen, zonder dat er meer mensen werken", "Ze stijgt, want er zijn meer mensen zonder werk",
         "Ze blijft altijd gelijk, want het aantal werkenden verandert niet", "Ze wordt nul, want niemand zoekt nog werk"],
        0,
        "Wie stopt met zoeken, telt niet meer mee in de beroepsbevolking en niet meer als werkloze.",
    ),
    tabel(
        "Waar of niet waar over de arbeidsmarktindicatoren?",
        [
            ("De werkzaamheidsgraad kan hoger zijn dan de activiteitsgraad.", F),
            ("Bij de werkloosheidsgraad deel je door de beroepsbevolking.", J),
            ("Een gepensioneerde hoort bij de beroepsbevolking.", F),
            ("Beroepsbevolking 5 miljoen en 400 000 werklozen geeft een werkloosheidsgraad van 8 %.", J),
        ],
        "De werkenden zijn een deel van de beroepsbevolking, dus de werkzaamheidsgraad is nooit hoger dan de activiteitsgraad.",
    ),
    tabel(
        "Welke soort werkloosheid is dit?",
        [
            ("Kassiers worden vervangen door zelfscankassa's", "Technische"),
            ("Een strandredder heeft in de winter geen werk", "Seizoens"),
            ("In een recessie ontslaan bedrijven mensen", "Conjuncturele"),
            ("Veel werklozen, maar ook veel vacatures voor lassers", "Structurele"),
            ("Iemand neemt ontslag en begint volgende maand elders", "Frictie"),
        ],
        "Machines: technisch. Een deel van het jaar: seizoen. Recessie: conjunctureel. Profiel past niet: structureel. Tussen twee jobs: frictie.",
        kolommen=["Frictie", "Seizoens", "Conjuncturele", "Structurele", "Technische"],
    ),
    tabel(
        "Welke maatregel helpt het best tegen deze soort werkloosheid?",
        [
            ("Structurele werkloosheid", "Omscholing van werkzoekenden"),
            ("Frictiewerkloosheid", "Een betere vacaturedatabank"),
            ("Conjuncturele werkloosheid", "De bestedingen stimuleren"),
        ],
        "Omscholing past het profiel aan, een databank versnelt het zoeken, meer bestedingen doen de vraag naar arbeid stijgen.",
        kolommen=["Omscholing van werkzoekenden", "Een betere vacaturedatabank", "De bestedingen stimuleren"],
    ),
    sorteer(
        "Werkt deze maatregel op de vraag naar arbeid of op het aanbod van arbeid?",
        ["Vraag naar arbeid", "Aanbod van arbeid"],
        [
            ["Lagere werkgeversbijdragen voor sociale zekerheid", "Vraag naar arbeid"],
            ["Een loonsubsidie bij aanwerving van een langdurig werkloze", "Vraag naar arbeid"],
            ["Een hogere werkbonus, zodat werken meer oplevert dan een uitkering", "Aanbod van arbeid"],
            ["Omscholing en opleiding van werkzoekenden", "Aanbod van arbeid"],
        ],
        "Wat de loonkost voor werkgevers verlaagt, werkt op de vraag. Wat werken aantrekkelijker maakt of werkzoekenden beter voorbereidt, werkt op het aanbod.",
    ),
    mk(
        "Er zijn tegelijk veel werklozen en veel openstaande vacatures. Kan dat?",
        ["Ja, als het profiel van de werkzoekenden niet past bij de vacatures",
         "Nee, want dan zouden de werklozen meteen die vacatures invullen",
         "Ja, maar enkel tijdens een recessie, als bedrijven minder verkopen",
         "Nee, want vacatures bestaan enkel als er geen werklozen zijn"],
        0,
        "Dat is structurele werkloosheid. Een beroep waarvoor werkgevers moeilijk mensen vinden, heet een knelpuntberoep.",
    ),
    sleep(
        "Een beroep waarvoor werkgevers moeilijk mensen vinden, heet een [[knelpuntberoep]].",
        ["vacaturedatabank", "loonnorm"],
        "Bij knelpuntberoepen staan vacatures lang open.",
    ),
    mk(
        "Wat is de loonnorm?",
        ["De maximale loonstijging bovenop de index, om de concurrentiekracht te beschermen",
         "Het laagste loon dat een werkgever in België mag betalen voor een voltijdse job",
         "De automatische aanpassing van alle lonen aan de stijging van de prijzen",
         "Het gemiddelde loon van alle werknemers in België, berekend door de overheid"],
        0,
        "De loonnorm beschermt de concurrentiekracht van Belgische bedrijven tegenover de buurlanden.",
    ),
    keuze(
        "De automatische loonindexering beschermt vooral de [[*koopkracht van werknemers|concurrentiekracht van bedrijven]]. De loonnorm beschermt vooral de [[*concurrentiekracht van bedrijven|koopkracht van werknemers]].",
        "De index laat lonen meestijgen met de prijzen. De loonnorm beperkt de loonstijging daarbovenop.",
    ),
    mk(
        "Waarom kan de automatische loonindexering bij hoge inflatie een probleem zijn voor bedrijven?",
        ["Hun loonkosten stijgen mee, en dat raakt hun concurrentiekracht",
         "Hun werknemers verliezen koopkracht en werken daardoor minder hard",
         "Ze moeten de lonen verlagen om de inflatie tegen te gaan",
         "Ze mogen hun prijzen niet meer verhogen zolang de index stijgt"],
        0,
        "Indexering beschermt de koopkracht van werknemers, maar maakt arbeid duurder voor de werkgever.",
    ),
    open_(
        "Leg uit waarom een hoog minimumloon tot werkloosheid kan leiden. Gebruik de begrippen vraag en aanbod van arbeid.",
        "Ligt het minimumloon boven het evenwichtsloon, dan vragen werkgevers minder arbeid (dalende vraagcurve) en willen meer mensen werken (stijgende aanbodcurve). Het aanbod is groter dan de vraag: het verschil zijn de werklozen.",
    ),
    inv(
        "Bij 18 euro per uur bieden 1 400 mensen arbeid aan en vragen werkgevers er 950. Hoeveel werklozen zijn er? Schrijf enkel het getal.",
        "450",
        "1 400 − 950 = 450.",
    ),
    mk(
        "Waarom daalt de vraagcurve naar arbeid?",
        ["Bij een hoger loon vragen werkgevers minder arbeid", "Bij een hoger loon willen minder mensen werken",
         "Bij een lager loon stijgt de werkloosheid", "Bij een hoger loon stijgt de beroepsbevolking"],
        0,
        "Werkgevers zijn de vragers. Arbeid wordt duurder, dus ze nemen minder mensen in dienst.",
    ),
    inv(
        "Een land heeft 800 000 werkenden, 50 000 werklozen en 1 250 000 mensen op arbeidsleeftijd. Bereken de activiteitsgraad in procent. Schrijf enkel het getal.",
        "68",
        "Beroepsbevolking 850 000. 850 000 / 1 250 000 = 68 %.",
    ),
    volgorde(
        "Een recessie begint. Zet de gevolgen in de juiste volgorde.",
        ["Gezinnen en bedrijven geven minder uit", "Bedrijven verkopen minder",
         "Bedrijven ontslaan mensen", "De conjuncturele werkloosheid stijgt"],
        "In een laagconjunctuur dalen de verkopen, en daarmee de vraag naar arbeid.",
    ),
    koppel(
        "Koppel elke indicator aan haar formule.",
        [
            ["Activiteitsgraad", "Beroepsbevolking / bevolking op arbeidsleeftijd"],
            ["Werkzaamheidsgraad", "Werkenden / bevolking op arbeidsleeftijd"],
            ["Werkloosheidsgraad", "Werklozen / beroepsbevolking"],
        ],
        ["Werklozen / bevolking op arbeidsleeftijd"],
        "Enkel bij de werkloosheidsgraad deel je door de beroepsbevolking.",
    ),
    mk(
        "Bij 9 euro per uur willen 600 mensen werken en vragen werkgevers 900 werknemers. Wat is er aan de hand?",
        ["Een tekort van 300 arbeidskrachten: het loon ligt onder het evenwichtsloon",
         "Werkloosheid van 300 mensen: het loon van 9 euro ligt boven het evenwichtsloon",
         "Een tekort van 900 arbeidskrachten: niemand wil nog voor 9 euro per uur werken",
         "Werkloosheid van 600 mensen: het loon van 9 euro ligt onder het evenwichtsloon"],
        0,
        "Er worden meer werknemers gevraagd (900) dan er aangeboden worden (600).",
    ),
]
