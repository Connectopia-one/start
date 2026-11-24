"""Veilig werken, meten en levensreddend handelen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS

GLAS = "#e3f0f7"
WATER = "#a9d2ec"

# Labo-glaswerk -----------------------------------------------------------
GW = Prent("labo-glaswerk", "Vier stukken glaswerk", "bekerglas A, erlenmeyer B, maatcilinder C en volpipet D")
GW.pad("M90 260 L 90 500 Q 90 520 110 520 L 250 520 Q 270 520 270 500 L 270 260", GLAS, DONKER, 3)
GW.rect(92, 400, 176, 118, WATER, "none", 0)
for y in (330, 380, 430):
    GW.lijn(100, y, 125, y, DONKER, 2)
GW.pad("M370 260 L 370 340 L 300 510 Q 296 520 310 520 L 500 520 Q 514 520 510 510 L 440 340 L 440 260", GLAS, DONKER, 3)
GW.pad("M325 450 L 485 450 L 507 508 L 303 508 Z", WATER, "none", 0)
GW.pad("M590 130 L 590 500 L 560 520 L 680 520 L 650 500 L 650 130", GLAS, DONKER, 3)
GW.rect(592, 330, 56, 170, WATER, "none", 0)
for i in range(0, 18):
    y = 170 + i * 18
    GW.lijn(592, y, 610 if i % 5 else 625, y, DONKER, 2)
GW.lijn(825, 90, 825, 260, DONKER, 3); GW.lijn(845, 90, 845, 260, DONKER, 3)
GW.ellips(835, 330, 40, 70, GLAS, DONKER, 3)
GW.lijn(825, 400, 825, 500, DONKER, 3); GW.lijn(845, 400, 845, 500, DONKER, 3)
GW.lijn(825, 500, 832, 525, DONKER, 3); GW.lijn(845, 500, 838, 525, DONKER, 3)
GW.lijn(815, 160, 855, 160, ROOD, 3)
LG = {"A": (180, 580), "B": (405, 580), "C": (620, 580), "D": (835, 580)}
for k, (x, y) in LG.items():
    GW.letter(x, y, k)
ZGW = {"A": [Prent.zone(80, 250, 200, 280)], "B": [Prent.zone(290, 250, 230, 280)],
       "C": [Prent.zone(550, 120, 140, 410)], "D": [Prent.zone(780, 80, 110, 450)]}
for k, (x, y) in LG.items():
    ZGW[k].append(Prent.rond(x, y, 26))

# Borstkas voor hartmassage ---------------------------------------------
BK = Prent("borstkas-drukpunt", "Waar duw je bij een hartmassage?", "romp van een liggend slachtoffer met vier plaatsen A tot D")
BK.ellips(500, 128, 55, 60, "#f3d9c4", DONKER, 3)
BK.rect(475, 185, 50, 30, "#f3d9c4", DONKER, 0)
BK.pad("M300 220 Q 500 190 700 220 L 690 600 L 310 600 Z", "#f3d9c4", DONKER, 3)
BK.lijn(500, 240, 500, 400, "#c9a88d", 6)
BK.pad("M380 300 Q 410 330 440 300", "none", "#c9a88d", 2)
BK.pad("M560 300 Q 590 330 620 300", "none", "#c9a88d", 2)
BK.cirkel(500, 540, 6, "#c9a88d", "#c9a88d")
PLA = {"A": (500, 245), "B": (500, 375), "C": (590, 300), "D": (500, 520)}
for k, (x, y) in PLA.items():
    BK.cirkel(x, y, 14, ORANJE, DONKER)
    BK.letter(x + (60 if k != "C" else 60), y, k)
ZBK = {k: [Prent.rond(x, y, 30), Prent.rond(x + 60, y, 26)] for k, (x, y) in PLA.items()}

VRAGEN = [
    klik(
        "Klik op het glaswerk waarmee je één bepaald volume het nauwkeurigst afmeet.",
        GW.bestand, ZGW["D"],
        "Een volpipet heeft één ijkstreep en meet precies dat ene volume af.",
    ),
    klik(
        "Klik op het glaswerk met een schaalverdeling waarop je een volume redelijk nauwkeurig afleest.",
        GW.bestand, ZGW["C"],
        "Een maatcilinder is smal en heeft een fijne schaal. Een bekerglas is bedoeld om te mengen.",
    ),
    met_prent(GW.bestand, tabel(
        "Kijk naar het glaswerk. Klopt dit?",
        [
            ("A is een bekerglas, geschikt om te mengen en te verwarmen.", J),
            ("De streepjes op A geven een ruwe schatting van het volume.", J),
            ("B is een erlenmeyer, die je goed kan rondzwenken zonder te morsen.", J),
            ("A is nauwkeuriger dan D om 25 ml af te meten.", F),
        ],
        "Hoe smaller het glas bij de streep, hoe nauwkeuriger.",
    )),
    klik(
        "Klik op de plaats waar je bij een volwassene duwt tijdens een hartmassage.",
        BK.bestand, ZBK["B"],
        "Midden op de borstkas, op het onderste deel van het borstbeen.",
    ),
    met_prent(BK.bestand, tabel(
        "Kijk naar de romp. Klopt dit?",
        [
            ("Op plaats D duwen pompt nauwelijks bloed rond.", J),
            ("Plaats C, boven het hart links, is de juiste plaats om te duwen.", F),
            ("Je duwt met de hiel van je hand recht naar beneden.", J),
            ("Na elke duw laat je de borstkas volledig terugkomen.", J),
        ],
        "Je drukt het hart samen tussen borstbeen en rug, dus in het midden.",
    )),
    tabel(
        "H-zin of P-zin?",
        [
            ("Ontvlambare vloeistof en damp.", "H-zin"),
            ("Draag beschermende handschoenen.", "P-zin"),
            ("Giftig bij inslikken.", "H-zin"),
            ("Verwijderd houden van open vuur.", "P-zin"),
            ("Veroorzaakt ernstige oogirritatie.", "H-zin"),
        ],
        "H: het gevaar. P: de voorzorg.",
        kolommen=["H-zin", "P-zin"],
    ),
    koppel(
        "Koppel elk instrument aan wat je ermee meet.",
        [
            ("balans", "massa"),
            ("pH-meter", "zuurtegraad"),
            ("dynamometer", "kracht"),
            ("chronometer", "tijdsduur"),
        ],
        ["volume"],
        "Volume meet je met glaswerk, zoals een maatcilinder.",
    ),
    tabel(
        "Reken om.",
        [
            ("3,2 km", "3200 m"),
            ("450 mg", "0,45 g"),
            ("0,005 m", "5 mm"),
            ("2 µs", "0,000002 s"),
        ],
        "Kilo = 1000, milli = een duizendste, micro = een miljoenste.",
        kolommen=["3200 m", "0,45 g", "5 mm", "0,000002 s"],
    ),
    tabel(
        "Schrijf in wetenschappelijke notatie.",
        [
            ("0,00032 m", "3,2 · 10⁻⁴ m"),
            ("45 000 J", "4,5 · 10⁴ J"),
            ("0,032 m", "3,2 · 10⁻² m"),
        ],
        "Een getal tussen 1 en 10 maal een macht van tien.",
        kolommen=["3,2 · 10⁻⁴ m", "4,5 · 10⁴ J", "3,2 · 10⁻² m"],
    ),
    tabel(
        "Hoeveel beduidende cijfers heeft dit meetresultaat?",
        [
            ("4,56 cm", "3"),
            ("0,8 kg", "1"),
            ("12,0 °C", "3"),
            ("25 ml", "2"),
        ],
        "Nullen vooraan tellen niet mee, een nul achter de komma wel.",
        kolommen=["1", "2", "3"],
    ),
    tabel(
        "Veilig of duurzaam werken in het labo, of geen van beide?",
        [
            ("een veiligheidsbril dragen bij het verwarmen", "Veilig"),
            ("niet meer stof nemen dan je nodig hebt", "Duurzaam"),
            ("met natte handen een stekker uittrekken", "Geen van beide"),
            ("de multimeter uitzetten na de proef", "Duurzaam"),
        ],
        "Veilig beschermt jou en anderen, duurzaam spaart stoffen en energie.",
        kolommen=["Veilig", "Duurzaam", "Geen van beide"],
    ),
    casus(
        "Tijdens de les zakt een leerkracht plots in elkaar. Hij reageert niet als je hem aanspreekt en aan zijn schouders schudt.",
        [
            volgorde(
                "Zet de eerste stappen in de juiste volgorde.",
                [
                    "Roep luid om hulp",
                    "Kijk of hij normaal ademt",
                    "Laat 112 bellen, met de telefoon op de luidspreker",
                    "Begin met hartmassage als hij niet normaal ademt",
                ],
                "Eerst roepen en kijken, dan hulp laten komen en onmiddellijk duwen.",
            ),
            tabel(
                "Hij ademt niet normaal. Klopt dit?",
                [
                    ("Je geeft 30 hartmassages en dan 2 beademingen.", J),
                    ("Je duwt ongeveer 100 tot 120 keer per minuut.", J),
                    ("Je duwt ongeveer 5 tot 6 cm diep.", J),
                    ("Na tien minuten mag je stoppen, ook zonder hulp.", F),
                ],
                "Je gaat door tot de hulpdiensten overnemen of hij weer normaal ademt.",
            ),
            keuze(
                "Een paar happende bewegingen zijn [[*geen normale ademhaling|een teken dat alles goed is|een reden om te stoppen]].",
                "Ook dan reanimeer je.",
            ),
        ],
    ),
    tabel(
        "Wat doe je bij iemand die zich verslikt?",
        [
            ("hij hoest krachtig", "Hoesten aanmoedigen"),
            ("hij kan niet meer spreken of hoesten", "Rugslagen en buikstoten"),
            ("hij verliest het bewustzijn", "Reanimeren"),
        ],
        "Zolang hoesten lukt, is dat het krachtigst.",
        kolommen=["Hoesten aanmoedigen", "Rugslagen en buikstoten", "Reanimeren"],
    ),
    volgorde(
        "Zet de hulp bij een ernstige verslikking in de juiste volgorde.",
        [
            "Laat de persoon voorover buigen",
            "Geef vijf rugslagen tussen de schouderbladen",
            "Ga achter de persoon staan",
            "Geef vijf buikstoten schuin naar boven",
        ],
        "Rugslagen en buikstoten wissel je af tot het voorwerp loskomt.",
    ),
    tabel(
        "Klopt dit over hulp bij een verdrinking?",
        [
            ("Je springt meteen zelf in het water, ook als je slecht zwemt.", F),
            ("Je reikt eerst iets aan, zoals een stok of een boei.", J),
            ("Het grootste gevaar is zuurstoftekort.", J),
            ("Bij een verdrinking begin je met beademen.", J),
        ],
        "Je eigen veiligheid gaat voor. Een tweede slachtoffer helpt niemand.",
    ),
    mk(
        "Iemand reageert niet, maar ademt wel normaal. Wat doe je?",
        [
            "Je legt hem in stabiele zijligging en volgt zijn ademhaling",
            "Je begint meteen met hartmassage, want hij reageert helemaal niet",
            "Je legt hem op zijn rug met een kussen onder zijn hoofd en wacht",
            "Je geeft hem een glas water zodat hij weer bij bewustzijn komt",
        ],
        0,
        "Wie zelf ademt, reanimeer je niet. In zijligging blijft de luchtweg vrij.",
    ),
    sleep(
        "Op een flesje met een sterk zuur staat het pictogram voor [[bijtende]] stoffen. Je draagt dan [[handschoenen]] en een [[veiligheidsbril]].",
        ["ontvlambare", "oorbeschermers"],
        "Een sterk zuur tast huid en ogen aan.",
    ),
    tabel(
        "Klopt dit over het meetbereik?",
        [
            ("Een thermometer tot 50 °C is ongeschikt voor kokend water.", J),
            ("Buiten het meetbereik kan een toestel stukgaan.", J),
            ("Een balans tot 200 g is geschikt om een tas van 3 kg te wegen.", F),
            ("Je kiest een instrument dat bij de te meten waarde past.", J),
        ],
        "Het meetbereik gaat van de kleinste tot de grootste meetbare waarde.",
    ),
    inv(
        "Je meet vijf keer de valtijd van een bal: 0,62 s, 0,60 s, 0,64 s, 0,61 s en 0,63 s. Wat is het gemiddelde, in seconden?",
        ["0,62", "0.62"],
        "3,10 : 5 = 0,62 s. Herhalen verkleint de invloed van toevallige fouten.",
    ),
    tabel(
        "Waar hoort dit afval?",
        [
            ("een gebroken reageerbuis", "Bak voor scherp afval"),
            ("een gebruikte papieren handdoek zonder chemicaliën", "Gewone vuilbak"),
            ("de rest van een organisch oplosmiddel", "Inzamelfles voor chemisch afval"),
        ],
        "Glas en chemicaliën horen nooit bij het gewone afval of in de gootsteen.",
        kolommen=["Bak voor scherp afval", "Gewone vuilbak", "Inzamelfles voor chemisch afval"],
    ),
    met_prent(GW.bestand, tabel(
        "Kijk naar het glaswerk. Welk stuk kies je?",
        [
            ("precies 10,0 ml oplossing overbrengen", "D"),
            ("ongeveer 200 ml water opwarmen", "A"),
            ("een oplossing rondzwenken bij een proef", "B"),
            ("37 ml water afmeten voor een mengsel", "C"),
        ],
        "Elk glaswerk heeft zijn eigen doel en nauwkeurigheid.",
        kolommen=["A", "B", "C", "D"],
    )),
    klik(
        "Klik op de plaats waar het borstbeen begint, net onder de hals.",
        BK.bestand, ZBK["A"],
        "Daar duw je niet: te hoog. Je duwt lager, op het onderste deel van het borstbeen.",
    ),
    keuze(
        "Het noodnummer [[*112|101|1307]] werkt in heel Europa en is gratis.",
        "Zet de telefoon op de luidspreker zodat je handen vrij blijven.",
    ),
    tabel(
        "Klopt dit over veilig werken met een bunsenbrander?",
        [
            ("Je houdt ontvlambare stoffen uit de buurt van de vlam.", J),
            ("Lang haar bind je samen.", J),
            ("Je verwarmt een reageerbuis met de opening naar je gezicht.", F),
            ("Je laat een brandende brander niet alleen.", J),
        ],
        "Een vlam en ontvlambare stoffen gaan nooit samen.",
    ),
    tabel(
        "Grootte schatten: welke waarde is het meest realistisch?",
        [
            ("de massa van een volwassene", "70 kg"),
            ("de massa van een appel", "0,2 kg"),
            ("de massa van een personenwagen", "1200 kg"),
        ],
        "Een schatting vooraf helpt je om een onzinnige uitkomst te herkennen.",
        kolommen=["0,2 kg", "70 kg", "1200 kg"],
    ),
    inv(
        "Hoeveel milliliter is 0,25 liter?",
        ["250"],
        "Milli is een duizendste: 0,25 · 1000 = 250 ml.",
    ),
    tabel(
        "Klopt dit over handschoenen in het labo?",
        [
            ("Bij biologisch materiaal draag je handschoenen.", J),
            ("Na het werk was je toch nog je handen.", J),
            ("Met handschoenen aan mag je in je ogen wrijven.", F),
            ("Gebruikte handschoenen leg je terug in de doos voor later.", F),
        ],
        "Hygiënisch werken voorkomt dat je micro-organismen of stoffen overbrengt.",
    ),
    open_(
        "Leg uit waarom je bij een hartstilstand zo snel mogelijk moet beginnen met hartmassage.",
        "Bij een hartstilstand pompt het hart geen bloed meer rond. De hersenen krijgen dan geen zuurstof en raken na enkele minuten blijvend beschadigd. Met hartmassage pomp je zelf bloed rond tot de hulpdiensten er zijn. Elke minuut wachten kost overlevingskans.",
    ),
]
