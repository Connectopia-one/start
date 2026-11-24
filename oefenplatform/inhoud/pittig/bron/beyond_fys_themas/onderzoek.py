"""Onderzoeken en ontwerpen — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Meetreeks slinger met uitschieter --------------------------------------------------
SL = Prent("slinger-meetreeks", "Meetresultaten: de periode van een slinger bij verschillende lengtes", "grafiek van de periode T in s tegen de lengte L in m; zes meetpunten die op een stijgende, afvlakkende kromme liggen (L = 0,2; 0,4; 0,6; 0,8; 1,0; 1,2 m) en één punt P bij L = 0,6 m dat veel te hoog ligt; de meetpunten zijn A tot en met F")
X, Y = assen(SL, 0, 1.4, 0, 3, "L (m)", "T (s)", 0.2, 0.5, links=130, rechts=900)
PTS = {}
for i, L in enumerate((0.2, 0.4, 0.6, 0.8, 1.0, 1.2)):
    T = 2 * math.pi * math.sqrt(L / 9.81)
    if L == 0.6:
        T = 2.35
    PTS["ABCDEF"[i]] = (L, T)
SL.pad("M " + " L ".join(f"{X(l / 100):.1f} {Y(2 * math.pi * math.sqrt(l / 100 / 9.81)):.1f}" for l in range(5, 136)), "none", GRIJS, 2)
LSL = {}
for k, (L, T) in PTS.items():
    SL.cirkel(X(L), Y(T), 9, ORANJE, DONKER, 2)
    LSL[k] = (X(L) - 26, Y(T) - 30)
    SL.letter(*LSL[k], k)
ZSL = {k: [Prent.rond(X(L), Y(T), 22), Prent.rond(*LSL[k], 22)] for k, (L, T) in PTS.items()}

# Drie koeltassen getest -------------------------------------------------------------
KT = Prent("koeltassen-test", "Drie ontwerpen van een koeltas getest", "grafiek van de temperatuur van het drankje in °C tegen de tijd in uur, van 0 tot 6 h; alle drie starten bij 4 °C; een rode stippellijn bij 8 °C en een verticale stippellijn bij 4 h (criterium); ontwerp A stijgt snel en is na 2 h al 8 °C, ontwerp B is na 4 h 6 °C, ontwerp C is na 4 h ongeveer 9,5 °C")
X2, Y2 = assen(KT, 0, 6, 0, 20, "t (h)", "temperatuur (°C)", 1, 2, links=130, rechts=880)
KT.lijn(X2(0), Y2(8), X2(6), Y2(8), ROOD, 2, stippel=True)
KT.lijn(X2(4), Y2(0), X2(4), Y2(20), ROOD, 2, stippel=True)
KT.tekst(X2(0.1), Y2(8) - 10, "8 °C", 16, anker="start", kleur=ROOD, vet=True)
KT.tekst(X2(4) + 8, Y2(19.3), "4 h", 16, anker="start", kleur=ROOD, vet=True)
def kromme(tau):
    return lambda t: 20 - 16 * math.exp(-t / tau)
KR = {"A": (kromme(6.95), BLAUW), "B": (kromme(30), GROEN), "C": (kromme(9.4), PAARS)}
LKT = {}
for k, (f, kl) in KR.items():
    KT.pad("M " + " L ".join(f"{X2(t / 20):.1f} {Y2(f(t / 20)):.1f}" for t in range(121)), "none", kl, 4)
    LKT[k] = (X2(6) + 30, Y2(f(6)) + {"A": -16, "C": 12, "B": 0}[k])
    KT.letter(*LKT[k], k)
ZKT = {k: [Prent.zone(X2(4.5) - 10, Y2(f(5)) - 18, X2(6) - X2(4.5) + 20, 36), Prent.rond(*LKT[k], 24)] for k, (f, kl) in KR.items()}

VRAGEN = [
    klik(
        "Klik op de meting die je verder moet onderzoeken.",
        SL.bestand, ZSL["C"],
        "Ze ligt ver van de lijn door de andere metingen.",
    ),
    met_prent(SL.bestand, mk(
        "Wat doe je best met meting C?",
        ["De oorzaak zoeken en opnieuw meten", "Ze zonder uitleg uit de tabel weglaten", "De kromme toch door dat punt laten gaan", "De andere metingen een beetje aanpassen"],
        0,
        "Je vermeldt ook in je verslag wat je ermee gedaan hebt.",
    )),
    met_prent(SL.bestand, keuze(
        "Op de horizontale as staat de [[*onafhankelijke|afhankelijke]] variabele: de lengte die je zelf kiest.",
        "De periode hangt ervan af en staat verticaal.",
    )),
    met_prent(SL.bestand, tabel(
        "Klopt deze conclusie uit de grafiek?",
        [
            ("Hoe langer de slinger, hoe groter de periode.", J),
            ("De periode is recht evenredig met de lengte.", F),
            ("Bij een slinger van 5 m is de periode zeker 4,5 s.", F),
        ],
        "De kromme is geen rechte, en buiten je meetgebied mag je niets zeker besluiten.",
    )),
    met_prent(SL.bestand, mk(
        "Welke grootheid moet je in deze proef constant houden?",
        ["De massa van het gewichtje", "De lengte van het touw", "De periode", "Het aantal metingen per lengte"],
        0,
        "Je verandert enkel de lengte; de rest blijft gelijk.",
    )),
    klik(
        "Klik op het ontwerp dat aan het criterium voldoet.",
        KT.bestand, ZKT["B"],
        "Alleen B blijft na 4 h onder 8 °C.",
    ),
    met_prent(KT.bestand, inv(
        "Na hoeveel uur bereikt ontwerp A 8 °C?",
        ["2", "2 h", "2 uur"],
        "Lees af waar kromme A de rode lijn kruist.",
    )),
    met_prent(KT.bestand, mk(
        "Ontwerp C haalt het criterium net niet. Wat is de beste volgende stap?",
        ["C bijsturen en opnieuw testen", "C goedkeuren, het scheelt maar weinig", "Het criterium verhogen tot 10 °C zodat het past", "Meteen het snellere ontwerp A kiezen"],
        0,
        "Evalueren en bijsturen gaat in rondes.",
    )),
    met_prent(KT.bestand, keuze(
        "Om de drie ontwerpen eerlijk te vergelijken, start je ze allemaal bij [[*dezelfde|een andere]] temperatuur en in dezelfde ruimte.",
        "Verander maar één ding tegelijk: het ontwerp.",
    )),
    tabel(
        "Is dit een goede onderzoeksvraag?",
        [
            ("Hoe hangt de remweg van een fiets af van haar snelheid?", J),
            ("Waarom is fysica zo interessant?", F),
            ("Hoe hangt de stroom door een draad af van de spanning?", J),
            ("Wat is de beste auto?", F),
        ],
        "Een goede vraag noemt twee meetbare grootheden.",
    ),
    mk(
        "Wat is de afhankelijke variabele in de vraag 'Hoe hangt de valtijd af van de valhoogte?'",
        ["De valtijd", "De valhoogte", "De massa", "De zwaarteveldsterkte"],
        0,
        "Die meet je; de hoogte kies je zelf.",
    ),
    mk(
        "Welke hypothese is weerlegbaar?",
        ["Dubbele massa geeft dubbele uitrekking", "Veren zijn een interessant onderwerp", "Er bestaat misschien ergens een verband", "De proef zal er heel mooi uitzien"],
        0,
        "Ze maakt een concrete voorspelling die je kan nagaan.",
    ),
    casus(
        "Een groep wil weten of een plant in licht sneller groeit dan in het donker. Ze zetten tien plantjes in het licht en tien in een kast.",
        [
            keuze(
                "De plantjes in de kast vormen de [[*controlegroep|proefgroep]].",
                "Daarmee vergelijk je het effect van licht.",
            ),
            mk(
                "Wat moet voor beide groepen gelijk zijn?",
                ["Het water en de soort plant", "De hoeveelheid licht die ze krijgen", "De plaats waar ze in de klas staan", "Het uur waarop ze uitgezaaid zijn"],
                0,
                "Alleen het licht mag verschillen.",
            ),
            keuze(
                "Ze nemen tien plantjes per groep om [[*toevallige verschillen uit te middelen|het sneller af te hebben]].",
                "Eén plantje kan toevallig sneller of trager groeien.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van een wetenschappelijk onderzoek in de juiste volgorde.",
        ["onderzoeksvraag opstellen", "hypothese formuleren", "onderzoeksplan maken", "metingen uitvoeren", "conclusie trekken"],
        "Daarna volgen reflecteren en communiceren.",
    ),
    volgorde(
        "Zet de stappen van een ontwerpproces in de juiste volgorde.",
        ["probleem definiëren", "criteria opstellen", "opsplitsen in deelproblemen", "oplossingen samenvoegen", "evalueren en bijsturen"],
        "Na bijsturen test je opnieuw.",
    ),
    koppel(
        "Koppel elke STEM-letter aan wat ze bijdraagt bij een fietsverlichting op een dynamo.",
        [
            ("wetenschappen", "elektromagnetische inductie begrijpen"),
            ("technologie", "een led kiezen die weinig stroom vraagt"),
            ("techniek", "de dynamo stevig op het frame bouwen"),
            ("wiskunde", "uitrekenen hoeveel vermogen er nodig is"),
        ],
        ["een kleur voor de fiets kiezen"],
        "Elke discipline brengt een stuk van de oplossing.",
    ),
    sorteer(
        "Hoort dit bij onderzoeken of bij ontwerpen?",
        ["Onderzoeken", "Ontwerpen"],
        [
            ("een hypothese nagaan", "Onderzoeken"),
            ("criteria opstellen voor een koeltas", "Ontwerpen"),
            ("een controleproef uitvoeren", "Onderzoeken"),
            ("een prototype bijsturen", "Ontwerpen"),
        ],
        "Onderzoeken zoekt een antwoord, ontwerpen een oplossing.",
    ),
    mk(
        "Een leerling meet dat een veer 4,0 cm uitrekt bij 2 N en 8,0 cm bij 4 N. Welke conclusie mag ze trekken?",
        ["Tot 4 N is de uitrekking evenredig", "Elke veer ter wereld rekt 2 cm per newton", "Bij 100 N rekt deze veer zeker 200 cm uit", "De veer zal breken zodra je boven 4 N gaat"],
        0,
        "Een conclusie blijft binnen wat je gemeten hebt.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een hypothese die niet klopt, maakt je onderzoek waardeloos.", F),
            ("Een ander moet met jouw plan hetzelfde kunnen vinden.", J),
            ("Een criterium moet je achteraf kunnen nagaan.", J),
            ("Een deelprobleem los je op zonder naar het geheel te kijken.", F),
        ],
        "Ook een weerlegde hypothese is een resultaat.",
    ),
    mk(
        "Welk criterium voor een spaghettibrug is meetbaar?",
        ["Ze draagt 2 kg over 40 cm", "De brug is heel erg sterk", "De brug ziet er echt mooi uit", "De brug is netjes en goed gemaakt"],
        0,
        "Een getal met een eenheid kan je achteraf nagaan.",
    ),
    keuze(
        "Je herhaalt een meting vijf keer en neemt het [[*gemiddelde|grootste resultaat]].",
        "Zo vlakken toevallige afwijkingen uit.",
    ),
    mk(
        "Waarom laat je een verslag nalezen door iemand die de proef niet deed?",
        ["Die ziet fouten die jij mist", "Om zelf sneller klaar te zijn", "Om de cijfers wat mooier te maken", "Omdat het altijd verplicht is"],
        0,
        "Communiceren en reflecteren horen bij onderzoek.",
    ),
    inv(
        "Een leerling meet de periode van een slinger vijf keer: 1,52 s, 1,48 s, 1,50 s, 1,49 s en 1,51 s. Hoe groot is het gemiddelde, in s?",
        ["1,5", "1,50", "1,50 s"],
        "Som 7,50 s gedeeld door 5.",
    ),
    keuze(
        "Een meting die je hypothese tegenspreekt, is [[*een geldig resultaat|een mislukte proef]].",
        "Je past je besluit aan de data aan, niet omgekeerd.",
    ),
    mk(
        "Waarom schrijf je in je verslag precies welke instrumenten je gebruikte?",
        ["Zodat een ander het kan herhalen", "Zodat het verslag wat langer wordt", "Omdat de leraar dat graag leest", "Zodat je geen grafiek moet maken"],
        0,
        "Een onderzoek moet herhaalbaar zijn.",
    ),
    mk(
        "Je ontwerpt een zonneoven. Welke fysicakennis helpt het meest?",
        ["Hoe straling wordt opgenomen", "Hoe een slinger heen en weer trilt", "Hoe een atoomkern spontaan vervalt", "Hoe geluid zich door lucht voortplant"],
        0,
        "Een zwarte binnenkant neemt straling op, spiegels kaatsen ze naar binnen.",
    ),
    sleep(
        "De grootheid die je zelf verandert, is de [[onafhankelijke]] variabele. Wat je meet, is de [[afhankelijke]] variabele. Een opstelling waarin je niets verandert, is een [[controleproef]].",
        ["hypothese", "criterium"],
        "Verander maar één grootheid tegelijk.",
    ),
    open_(
        "Leg uit waarom je in een proef maar één grootheid tegelijk verandert, met een voorbeeld.",
        "Verander je twee grootheden tegelijk, dan weet je niet welke van de twee het verschil veroorzaakte. Voorbeeld: wil je weten of de lengte van een slinger de periode beïnvloedt, dan verander je alleen de lengte en houd je de massa en de uitwijking gelijk.",
    ),
]
