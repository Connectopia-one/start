"""Veilig werken, meetinstrumenten en beduidende cijfers — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vijf gevarenpictogrammen ----------------------------------------------------
GP = Prent("gevarenpictogrammen", "Vijf gevarenpictogrammen", "vijf ruitvormige tekens met een rode rand: een vlam, een doodshoofd, een hand en oppervlak met druppels, een uitroepteken, een boom met een vis; letters A tot E")
RD = "#c8102e"
XS = [110, 300, 490, 680, 870]
for i, x in enumerate(XS):
    y = 280
    GP.pad(f"M {x} {y - 85} L {x + 85} {y} L {x} {y + 85} L {x - 85} {y} Z", "#ffffff", RD, 9)
    GP.letter(x, 420, "ABCDE"[i])
# A: vlam
x = XS[0]
GP.pad(f"M {x - 25} 315 Q {x - 35} 270 {x - 5} 240 Q {x - 5} 270 {x + 8} 275 Q {x + 5} 245 {x + 20} 230 Q {x + 40} 275 {x + 25} 315 Z", DONKER, DONKER, 1)
GP.rect(x - 32, 318, 64, 6, DONKER, DONKER, 0, 0)
# B: doodshoofd
x = XS[1]
GP.cirkel(x, 262, 26, DONKER, DONKER, 1)
GP.cirkel(x - 10, 258, 7, "#ffffff", "#ffffff", 1)
GP.cirkel(x + 10, 258, 7, "#ffffff", "#ffffff", 1)
GP.rect(x - 12, 284, 24, 10, DONKER, DONKER, 2, 0)
GP.lijn(x - 32, 300, x + 32, 330, DONKER, 7)
GP.lijn(x + 32, 300, x - 32, 330, DONKER, 7)
# C: bijtend
x = XS[2]
GP.cirkel(x - 22, 250, 5, DONKER, DONKER, 1)
GP.cirkel(x + 22, 250, 5, DONKER, DONKER, 1)
GP.lijn(x - 22, 258, x - 22, 272, DONKER, 2, stippel=True)
GP.lijn(x + 22, 258, x + 22, 272, DONKER, 2, stippel=True)
GP.pad(f"M {x - 45} 300 L {x - 5} 300 L {x - 5} 285 L {x - 30} 285 Z", DONKER, DONKER, 1)
GP.pad(f"M {x + 5} 300 L {x + 45} 300 L {x + 45} 285 Q {x + 30} 278 {x + 15} 292 Z", DONKER, DONKER, 1)
GP.rect(x - 50, 305, 100, 10, DONKER, DONKER, 0, 0)
# D: uitroepteken
x = XS[3]
GP.rect(x - 7, 235, 14, 55, DONKER, DONKER, 3, 0)
GP.cirkel(x, 310, 8, DONKER, DONKER, 1)
# E: milieu
x = XS[4]
GP.lijn(x - 20, 315, x - 20, 260, DONKER, 4)
GP.pad(f"M {x - 40} 270 L {x - 20} 235 L {x} 270 Z", DONKER, DONKER, 1)
GP.ellips(x + 18, 305, 18, 8, DONKER, DONKER, 1)
GP.pad(f"M {x + 34} 305 L {x + 44} 297 L {x + 44} 313 Z", DONKER, DONKER, 1)
ZGP = {k: [Prent.rond(x, 280, 80), Prent.rond(x, 420, 22)] for k, x in zip("ABCDE", XS)}

# Glaswerk ---------------------------------------------------------------------
GW = Prent("glaswerk", "Vijf stukken glaswerk", "vijf soorten glaswerk naast elkaar: een bekerglas, een maatcilinder, een maatkolf met één streepje, een volpipet en een buret; letters P tot T")
# P bekerglas
GW.pad("M 60 330 L 60 470 Q 60 480 70 480 L 170 480 Q 180 480 180 470 L 180 330", "#f4f9fd", DONKER, 3)
for j in range(3):
    GW.lijn(60, 440 - j * 35, 80, 440 - j * 35, DONKER, 1)
# Q maatcilinder
GW.rect(265, 130, 40, 340, "#f4f9fd", DONKER, 4, 3)
GW.rect(240, 470, 90, 10, "#d9d4c4", DONKER, 2, 2)
for j in range(15):
    GW.lijn(265, 450 - j * 20, 278 if j % 5 else 288, 450 - j * 20, DONKER, 1)
# R maatkolf
GW.pad("M 465 120 L 465 330 Q 400 360 400 420 Q 400 480 485 480 Q 570 480 570 420 Q 570 360 505 330 L 505 120", "#f4f9fd", DONKER, 3)
GW.lijn(462, 200, 508, 200, DONKER, 2)
# S volpipet
GW.lijn(660, 80, 660, 250, DONKER, 3)
GW.lijn(672, 80, 672, 250, DONKER, 3)
GW.ellips(666, 300, 22, 50, "#f4f9fd", DONKER, 3)
GW.lijn(660, 350, 663, 470, DONKER, 3)
GW.lijn(672, 350, 669, 470, DONKER, 3)
GW.lijn(655, 150, 677, 150, DONKER, 2)
# T buret
GW.rect(845, 70, 30, 360, "#f4f9fd", DONKER, 4, 3)
for j in range(17):
    GW.lijn(845, 90 + j * 20, 855 if j % 5 else 862, 90 + j * 20, DONKER, 1)
GW.rect(838, 430, 44, 12, "#7aa35c", DONKER, 3, 2)
GW.lijn(860, 442, 860, 475, DONKER, 3)
for k, x in zip("PQRST", (120, 285, 485, 666, 860)):
    GW.letter(x, 540, k)
ZGW = {"P": [Prent.zone(55, 320, 130, 165), Prent.rond(120, 540, 22)],
       "Q": [Prent.zone(240, 125, 90, 360), Prent.rond(285, 540, 22)],
       "R": [Prent.zone(395, 115, 180, 370), Prent.rond(485, 540, 22)],
       "S": [Prent.zone(640, 75, 55, 400), Prent.rond(666, 540, 22)],
       "T": [Prent.zone(835, 65, 50, 415), Prent.rond(860, 540, 22)]}

VRAGEN = [
    klik(
        "Klik op het pictogram van een stof die je nooit in de gootsteen mag gieten omdat ze het leven in het water schaadt.",
        GP.bestand, ZGP["E"],
        "De boom en de dode vis: schadelijk voor het aquatisch milieu.",
    ),
    klik(
        "Klik op het pictogram dat al in een kleine hoeveelheid dodelijk kan zijn.",
        GP.bestand, ZGP["B"],
        "Het doodshoofd: acuut giftig. Het uitroepteken is minder ernstig.",
    ),
    met_prent(GP.bestand, tabel(
        "Welke betekenis hoort bij dit pictogram?",
        [
            ("A", "Ontvlambaar"),
            ("C", "Bijtend"),
            ("D", "Schadelijk of irriterend"),
        ],
        "Bijtend: tast huid en materiaal aan. Uitroepteken: minder ernstig gevaar.",
        kolommen=["Ontvlambaar", "Bijtend", "Schadelijk of irriterend"],
    )),
    met_prent(GP.bestand, tabel(
        "Kijk naar de vorm van de pictogrammen. Klopt dit?",
        [
            ("Ze zijn ruitvormig.", J),
            ("Ze hebben een rode rand.", J),
            ("Ze zijn rond en groen.", F),
        ],
        "Ronde groene tekens zijn geen gevarenpictogrammen.",
    )),
    klik(
        "Klik op het glaswerk om precies 250,0 mL oplossing te maken.",
        GW.bestand, ZGW["R"],
        "Een maatkolf met één streepje is gemaakt voor één exact volume.",
    ),
    klik(
        "Klik op het glaswerk om tijdens een titratie het toegevoegde volume tot op honderdsten af te lezen.",
        GW.bestand, ZGW["T"],
        "De buret: de schaal loopt van boven naar onder.",
    ),
    met_prent(GW.bestand, tabel(
        "Is dit glaswerk nauwkeurig genoeg voor een volume dat je in een berekening gebruikt?",
        [
            ("P", "Nee"),
            ("R", "Ja"),
            ("S", "Ja"),
            ("T", "Ja"),
        ],
        "De streepjes op een bekerglas zijn maar een ruwe schatting.",
        kolommen=["Ja", "Nee"],
    )),
    tabel(
        "Gaat deze zin over gevaar (H-zin) of over voorzorg (P-zin)?",
        [
            ("Veroorzaakt ernstige brandwonden.", "H-zin"),
            ("Draag een veiligheidsbril.", "P-zin"),
            ("Zeer ontvlambare vloeistof.", "H-zin"),
            ("Bij contact met de ogen: spoelen met water.", "P-zin"),
        ],
        "H van hazard, P van precaution.",
        kolommen=["H-zin", "P-zin"],
    ),
    tabel(
        "Hoeveel beduidende cijfers heeft dit getal?",
        [
            ("0,0250", "3"),
            ("4,00", "3"),
            ("0,005", "1"),
            ("2,0 · 10³", "2"),
        ],
        "Nullen vooraan tellen niet, nullen achteraan na de komma wel.",
        kolommen=["1", "2", "3"],
    ),
    inv(
        "Schrijf 0,000 34 in wetenschappelijke notatie. Gebruik de vorm 3,4·10^-x.",
        ["3,4·10^-4", "3,4*10^-4", "3,4·10⁻⁴", "3,4 · 10^-4", "3.4e-4", "3,4x10^-4"],
        "De komma schuift vier plaatsen naar rechts.",
    ),
    mk(
        "Je berekent 4,2 g gedeeld door 3,00 mL. Hoe schrijf je de dichtheid?",
        ["1,4 g/mL", "1,40 g/mL", "1,400 g/mL", "1 g/mL"],
        0,
        "Bij delen volg je het kleinste aantal beduidende cijfers: twee.",
    ),
    mk(
        "Je telt 25,1 mL en 3,26 mL op. Hoe schrijf je het resultaat?",
        ["28,4 mL", "28,36 mL", "28 mL", "28,360 mL"],
        0,
        "Bij optellen volg je het kleinste aantal cijfers na de komma: één.",
    ),
    tabel(
        "Met welke macht van tien komt dit voorvoegsel overeen?",
        [
            ("mega", "10⁶"),
            ("kilo", "10³"),
            ("milli", "10⁻³"),
            ("nano", "10⁻⁹"),
        ],
        "Micro zit tussen milli en nano: 10⁻⁶.",
        kolommen=["10⁶", "10³", "10⁻³", "10⁻⁹"],
    ),
    casus(
        "Je moet 5,0 mL van een oplossing afmeten. Je hebt een maatcilinder van 500 mL en een volpipet van 5 mL.",
        [
            keuze(
                "Je kiest de [[*volpipet|maatcilinder]].",
                "De pipet is precies voor dat volume gemaakt.",
            ),
            mk(
                "Waarom is de maatcilinder van 500 mL hier slecht?",
                [
                    "De streepjes staan te ver uit elkaar",
                    "Hij is niet van glas maar van plastic gemaakt",
                    "Hij meet enkel volumes in hele liters",
                    "Hij kan geen waterige oplossing bevatten",
                ],
                0,
                "Een afleesfout van enkele mL is daar al een groot deel van 5 mL.",
            ),
            keuze(
                "Voor je pipetteert, spoel je de pipet met [[*de oplossing zelf|gedestilleerd water|alcohol]].",
                "Achtergebleven water zou de oplossing verdunnen.",
            ),
        ],
    ),
    tabel(
        "Is dit een SI-basiseenheid?",
        [
            ("kilogram", "Ja"),
            ("kelvin", "Ja"),
            ("liter", "Nee"),
            ("mol", "Ja"),
        ],
        "De liter is afgeleid van de kubieke meter.",
        kolommen=["Ja", "Nee"],
    ),
    tabel(
        "Zijn deze grootheden recht of omgekeerd evenredig?",
        [
            ("massa en volume van dezelfde stof", "Recht"),
            ("druk en volume van een gas bij gelijke T", "Omgekeerd"),
            ("aantal mol en massa van dezelfde stof", "Recht"),
        ],
        "Recht: het quotiënt is constant. Omgekeerd: het product is constant.",
        kolommen=["Recht", "Omgekeerd"],
    ),
    volgorde(
        "Zet deze voorvoegsels van groot naar klein.",
        ["mega", "kilo", "milli", "micro", "nano"],
        "10⁶, 10³, 10⁻³, 10⁻⁶, 10⁻⁹.",
    ),
    inv(
        "Hoeveel mL is 2,5 dm³?",
        ["2500", "2 500"],
        "1 dm³ = 1 L = 1000 mL.",
    ),
    mk(
        "Waarom giet je bij het verdunnen zuur bij water en niet water bij geconcentreerd zuur?",
        [
            "Er komt veel warmte vrij en het kan spatten",
            "Zuur lost alleen op deze manier op in water",
            "Water bij zuur geeft altijd een giftig gas",
            "Anders verandert de concentratie helemaal niet",
        ],
        0,
        "Een beetje water in veel zuur kan meteen koken en wegspatten.",
    ),
    sleep(
        "Het meetbereik is de [[kleinste en grootste]] waarde die een instrument kan meten. De [[resolutie]] is de kleinste stap die het kan onderscheiden. Je leest af aan de onderkant van de [[meniscus]].",
        ["gemiddelde", "kalibratie", "maatstreep"],
        "Kies een instrument waarvan het bereik past bij wat je meet.",
    ),
    tabel(
        "Klopt dit over een veiligheidsfiche?",
        [
            ("Ze vermeldt de H- en P-zinnen.", J),
            ("Ze zegt wat je bij een ongeval doet.", J),
            ("Ze is enkel nodig voor ontvlambare stoffen.", F),
        ],
        "Elke gevaarlijke stof heeft er een.",
    ),
    inv(
        "Hoeveel micrometer gaan er in 1 meter? Schrijf als macht van tien, 10^x.",
        ["10^6", "10⁶", "1000000", "1 000 000"],
        "Micro is 10⁻⁶.",
    ),
    tabel(
        "Welk glaswerk kies je voor deze taak?",
        [
            ("ongeveer 100 mL water opwarmen", "Bekerglas"),
            ("precies 10,00 mL afmeten om over te brengen", "Volpipet"),
            ("precies 100,0 mL oplossing maken", "Maatkolf"),
        ],
        "Hoe nauwkeuriger de taak, hoe gespecialiseerder het glaswerk.",
        kolommen=["Bekerglas", "Volpipet", "Maatkolf"],
    ),
    mk(
        "Je meet de massa van een stof op een balans met resolutie 0,01 g. Welke notatie past?",
        ["12,35 g", "12,3 g", "12,350 g", "12 g"],
        0,
        "Je noteert tot op de resolutie van het toestel.",
    ),
    keuze(
        "Een gemorst zuur neutraliseer je eerst met een [[*zwakke base|sterke base|sterk zuur]] voor je het opkuist.",
        "Een sterke base zou zelf veel warmte en gevaar geven.",
    ),
    tabel(
        "Welke grafiek hoort bij deze evenredigheid?",
        [
            ("recht evenredig", "Rechte door de oorsprong"),
            ("omgekeerd evenredig", "Dalende kromme"),
            ("massa tegen volume van ijzer", "Rechte door de oorsprong"),
            ("druk tegen volume van een gas", "Dalende kromme"),
        ],
        "Bij omgekeerd evenredig blijft het product constant: een dalende kromme.",
        kolommen=["Rechte door de oorsprong", "Dalende kromme"],
    ),
    mk(
        "Waarom heeft de buret een schaal die van boven naar onder loopt?",
        [
            "Je leest af hoeveel eruit gelopen is",
            "Zo kan je de buret ondersteboven gebruiken",
            "De vloeistof stijgt tijdens een titratie",
            "Het is een gewoonte zonder reden",
        ],
        0,
        "Begin- en eindstand aflezen geeft meteen het verbruikte volume.",
    ),
    open_(
        "Leg uit waarom je een meetresultaat niet met alle cijfers van je rekenmachine opschrijft.",
        "Een meetresultaat kan nooit nauwkeuriger zijn dan de minst nauwkeurige meting waarmee je rekent. De rekenmachine weet niet hoe nauwkeurig je gemeten hebt en geeft gewoon veel cijfers. Je rondt daarom af op het juiste aantal beduidende cijfers, zodat het resultaat niet nauwkeuriger lijkt dan het is.",
    ),
]
