"""De cel, de organellen en de biologische membranen — pittig (🧬 Beyond doorstroom, biologie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Plantencel -------------------------------------------------------------
PC = Prent("plantencel-organellen", "Een plantencel (schematisch)", "rechthoekige plantencel met celwand, vacuole, kern, chloroplasten, mitochondrion en ER, letters A tot G")
PC.rect(150, 80, 700, 520, "#cfe3b4", "#4f7a2a", 30, 12)
PC.rect(170, 100, 660, 480, "#eef6e2", DONKER, 22, 2)
PC.ellips(560, 340, 210, 170, "#d6e8f5", BLAUW, 2)
PC.cirkel(300, 210, 70, "#e8d8ef", PAARS, 3)
PC.cirkel(310, 215, 22, "#b38bc8", "none", 0)
for x, y, r in ((260, 450, 0), (300, 520, 20), (760, 150, -15), (780, 520, 30)):
    PC.svg(f'<g transform="rotate({r} {x} {y})"><ellipse cx="{x}" cy="{y}" rx="38" ry="18" fill="#6aa84f" stroke="#2f4a22" stroke-width="2"/><line x1="{x-26}" y1="{y}" x2="{x+26}" y2="{y}" stroke="#2f4a22" stroke-width="1.5"/><line x1="{x-18}" y1="{y-7}" x2="{x+18}" y2="{y-7}" stroke="#2f4a22" stroke-width="1"/><line x1="{x-18}" y1="{y+7}" x2="{x+18}" y2="{y+7}" stroke="#2f4a22" stroke-width="1"/></g>')
PC.svg('<g><ellipse cx="660" cy="130" rx="40" ry="20" fill="#f2a66a" stroke="#2f4a22" stroke-width="2"/><path d="M630 130 q 7 -14 14 0 q 7 14 14 0 q 7 -14 14 0 q 7 14 14 0" fill="none" stroke="#2f4a22" stroke-width="1.5"/></g>')
for i in range(4):
    PC.pad(f"M{400 + i * 6} {150 + i * 16} q 40 -12 80 0", "none", ORANJE, 3)
for i in range(6):
    PC.cirkel(410 + i * 13, 146 + (i % 2) * 18, 2.5, DONKER, "none", 0)
LPC = {"A": (150, 330), "B": (560, 340), "C": (300, 140), "D": (240, 470), "E": (660, 175), "F": (460, 200), "G": (310, 215)}
for k, (x, y) in LPC.items():
    PC.letter(x, y, k)
ZPC = {"A": [Prent.zone(150, 80, 20, 520), Prent.rond(*LPC["A"], 26)],
       "B": [Prent.zone(400, 220, 320, 240), Prent.rond(*LPC["B"], 26)],
       "C": [Prent.rond(300, 210, 72)],
       "D": [Prent.rond(260, 450, 42), Prent.rond(300, 520, 42), Prent.rond(760, 150, 42), Prent.rond(780, 520, 42)],
       "E": [Prent.rond(660, 130, 44), Prent.rond(*LPC["E"], 26)],
       "F": [Prent.zone(395, 135, 100, 75)]}

# Membraan ---------------------------------------------------------------
MB = Prent("membraan-mozaiek", "Een stukje celmembraan (vloeibaar mozaïekmodel)", "fosfolipide dubbellaag met een kanaaleiwit P, een perifeer eiwit Q, suikerketens R en cholesterol S")
MB.tekst(80, 110, "buiten de cel", 16, "start")
MB.tekst(80, 590, "cytoplasma", 16, "start")
for laag, (yk, ys) in enumerate(((240, 336), (440, 344))):
    for i in range(24):
        x = 70 + i * 37
        if 410 < x < 520:
            continue
        MB.lijn(x - 5, yk, x - 5, ys, "#d9a441", 2)
        MB.lijn(x + 5, yk, x + 5, ys, "#d9a441", 2)
        MB.cirkel(x, yk, 12, "#4f8bc9", DONKER, 1)
MB.rect(420, 190, 90, 300, "#c86b8e", DONKER, 30, 2)
MB.rect(452, 190, 26, 300, "#ffffff", "none", 0, 0)
MB.ellips(740, 470, 60, 30, "#c86b8e", DONKER, 2)
MB.rect(630, 262, 12, 70, "#888", DONKER, 3, 1)
for x0 in (430, 470, 500):
    MB.pad(f"M{x0} 190 l -10 -30 l 12 -20 l -8 -25", "none", GROEN, 4)
MB.pad("M170 228 l -8 -30 l 10 -20 l -6 -25", "none", GROEN, 4)
LMB = {"P": (465, 560), "Q": (740, 540), "R": (520, 110), "S": (690, 300)}
MB.lijn(465, 535, 465, 495, DONKER, 1)
MB.lijn(740, 515, 740, 502, DONKER, 1)
for k, (x, y) in LMB.items():
    MB.letter(x, y, k)
ZMB = {"P": [Prent.zone(420, 190, 90, 300), Prent.rond(*LMB["P"], 26)],
       "Q": [Prent.zone(680, 440, 120, 60), Prent.rond(*LMB["Q"], 26)],
       "R": [Prent.zone(150, 120, 380, 75), Prent.rond(*LMB["R"], 26)],
       "S": [Prent.zone(622, 258, 28, 80), Prent.rond(*LMB["S"], 22)]}

VRAGEN = [
    klik(
        "Klik op het organel waar de fotosynthese gebeurt.",
        PC.bestand, ZPC["D"],
        "In de chloroplasten zit bladgroen.",
    ),
    klik(
        "Klik op het organel dat met zijn waterdruk de cel stevig houdt.",
        PC.bestand, ZPC["B"],
        "De grote centrale vacuole duwt tegen de celwand: turgor.",
    ),
    klik(
        "Klik op het organel waar de Krebscyclus gebeurt.",
        PC.bestand, ZPC["E"],
        "Het mitochondrion, met zijn ingeplooide binnenmembraan.",
    ),
    met_prent(PC.bestand, tabel(
        "Kijk naar de plantencel. Welke letter hoort bij welk onderdeel?",
        [
            ("celwand", "A"),
            ("vacuole", "B"),
            ("kern", "C"),
            ("ruw endoplasmatisch reticulum", "F"),
            ("nucleolus", "G"),
        ],
        "G ligt in de kern: daar worden de ribosomen gemaakt.",
        kolommen=["A", "B", "C", "F", "G"],
    )),
    met_prent(PC.bestand, tabel(
        "Kijk naar de plantencel. Zou je dit onderdeel ook in een dierlijke cel vinden?",
        [
            ("A", F),
            ("C", J),
            ("D", F),
            ("E", J),
        ],
        "Celwand en chloroplasten zijn typisch voor planten.",
    )),
    klik(
        "Klik op het kanaaleiwit dat helemaal door het membraan steekt.",
        MB.bestand, ZMB["P"],
        "Een transmembraaneiwit kan een kanaal vormen.",
    ),
    klik(
        "Klik op de suikerketens waarmee cellen elkaar herkennen.",
        MB.bestand, ZMB["R"],
        "Samen vormen ze de glycocalyx.",
    ),
    met_prent(MB.bestand, tabel(
        "Kijk naar het stukje membraan. Klopt dit?",
        [
            ("De blauwe koppen zijn hydrofiel.", J),
            ("De gele staarten wijzen naar elkaar toe.", J),
            ("S regelt mee hoe vloeibaar het membraan is.", J),
            ("Q steekt door beide lagen heen.", F),
        ],
        "Q is een perifeer eiwit: het ligt tegen één kant aan.",
    )),
    tabel(
        "Prokaryoot of eukaryoot?",
        [
            ("heeft een kern met kernmembraan", "Eukaryoot"),
            ("een bacterie", "Prokaryoot"),
            ("heeft mitochondria", "Eukaryoot"),
            ("heeft geen membraanorganellen", "Prokaryoot"),
        ],
        "Ribosomen hebben ze allebei.",
        kolommen=["Prokaryoot", "Eukaryoot"],
    ),
    koppel(
        "Koppel elk organel aan zijn taak.",
        [
            ("lysosoom", "breekt versleten celonderdelen af"),
            ("Golgi-apparaat", "werkt eiwitten af en verpakt ze"),
            ("centriool", "maakt de spoeldraden vast bij een celdeling"),
            ("vesikel", "brengt stoffen van plaats naar plaats in de cel"),
        ],
        ["maakt glucose uit CO2 en water"],
        "Dat laatste doet de chloroplast.",
    ),
    tabel(
        "Welke plastide is dit?",
        [
            ("slaat zetmeel op in een aardappel", "amyloplast"),
            ("kleurt een rijpe tomaat rood", "chromoplast"),
            ("doet aan fotosynthese", "chloroplast"),
        ],
        "Amylum is zetmeel, chroma is kleur, chloros is groen.",
        kolommen=["amyloplast", "chromoplast", "chloroplast"],
    ),
    tabel(
        "Waaruit bestaat de celwand?",
        [
            ("plant", "cellulose"),
            ("schimmel", "chitine"),
            ("bacterie", "peptidoglycaan"),
        ],
        "Chitine zit ook in het skelet van insecten.",
        kolommen=["cellulose", "chitine", "peptidoglycaan"],
    ),
    casus(
        "Een cel uit de alvleesklier maakt grote hoeveelheden verteringsenzymen die ze naar buiten stuurt.",
        [
            tabel(
                "Is dit organel in die cel extra goed ontwikkeld?",
                [
                    ("ruw endoplasmatisch reticulum", J),
                    ("Golgi-apparaat", J),
                    ("chloroplast", F),
                ],
                "Eiwitten maken, afwerken en verpakken.",
            ),
            volgorde(
                "Zet de weg van zo'n enzym in volgorde.",
                [
                    "Ribosoom op het ruw ER",
                    "Transportblaasje",
                    "Golgi-apparaat",
                    "Blaasje dat met het celmembraan versmelt",
                ],
                "Zo komt het enzym buiten de cel.",
            ),
        ],
    ),
    mk(
        "Een spiercel heeft veel meer mitochondria dan een vetcel. Waarom?",
        [
            "Ze verbruikt veel meer energie",
            "Ze moet veel meer vet opslaan",
            "Ze maakt veel meer eiwitten voor export",
            "Ze heeft geen kern en dus extra ruimte",
        ],
        0,
        "Mitochondria leveren ATP.",
    ),
    tabel(
        "Pleit dit voor de endosymbiosetheorie?",
        [
            ("een mitochondrion heeft eigen DNA", J),
            ("een chloroplast heeft een dubbel membraan", J),
            ("mitochondria delen zich zelf", J),
            ("een lysosoom bevat enzymen", F),
        ],
        "Mitochondria en chloroplasten waren ooit vrijlevende bacteriën.",
    ),
    sleep(
        "Fosfolipiden hebben een [[hydrofiele]] kop en [[hydrofobe]] staarten. In water vormen ze vanzelf een [[dubbellaag]].",
        ["hydrofobe kop", "eiwitrijke", "enkele laag"],
        "De staarten vermijden het water.",
    ),
    tabel(
        "Microtubuli of microfilamenten?",
        [
            ("holle buisjes van tubuline", "Microtubuli"),
            ("bestaan uit actine", "Microfilamenten"),
            ("vormen de spoeldraden", "Microtubuli"),
            ("liggen vooral net onder het celmembraan", "Microfilamenten"),
        ],
        "Samen met de intermediaire filamenten vormen ze het cytoskelet.",
        kolommen=["Microtubuli", "Microfilamenten"],
    ),
    volgorde(
        "Zet deze organisatieniveaus van klein naar groot.",
        ["Molecule", "Organel", "Cel", "Weefsel", "Orgaan"],
        "Daarna volgen orgaanstelsel en organisme.",
    ),
    mk(
        "Hoe verlaat mRNA de kern?",
        [
            "Langs de kernporiën",
            "Door het kernmembraan heen te diffunderen",
            "Via een lysosoom dat het naar buiten brengt",
            "Het verlaat de kern nooit en wordt daar vertaald",
        ],
        0,
        "Kernporiën zijn openingen in het dubbele kernmembraan.",
    ),
    tabel(
        "Klopt dit over de celwand van een plant?",
        [
            ("Ze geeft stevigheid.", J),
            ("Ze laat water en opgeloste stoffen vlot door.", J),
            ("Ze bepaalt welke stoffen de cel in mogen.", F),
            ("Plasmodesmata verbinden naburige cellen erdoorheen.", J),
        ],
        "Het celmembraan erachter is halfdoorlaatbaar, niet de wand.",
    ),
    keuze(
        "De inplooiingen van het binnenmembraan van een mitochondrion heten [[*cristae|cisternen|plasmodesmata]].",
        "Ze vergroten het oppervlak voor de eindoxidaties.",
    ),
    tabel(
        "Heeft een ribosoom dit?",
        [
            ("rRNA", J),
            ("eiwitten", J),
            ("een membraan", F),
        ],
        "Daarom hebben ook bacteriën ribosomen.",
    ),
    mk(
        "Waarom is het nuttig dat een membraan vloeibaar is?",
        [
            "De eiwitten erin kunnen bewegen",
            "Zo kan elke stof er vrij door",
            "Zo lost het membraan op in water",
            "Zo hoeft de cel geen cytoskelet te maken",
        ],
        0,
        "Bijvoorbeeld bij het versmelten van blaasjes met het membraan.",
    ),
    keuze(
        "Het cytoplasma is alles binnen het celmembraan [[*buiten de kern|met de kern erbij|buiten de organellen]].",
        "De kern telt niet mee.",
    ),
    tabel(
        "Klopt dit over een receptoreiwit?",
        [
            ("Het zit in het membraan.", J),
            ("Het past op één bepaalde signaalstof.", J),
            ("Het geeft een signaal door aan de binnenkant.", J),
            ("Het breekt de signaalstof meteen af.", F),
        ],
        "Zo reageert een cel op een hormoon.",
    ),
    inv(
        "Een cel is 20 micrometer breed. Hoeveel van die cellen leg je naast elkaar op 1 mm?",
        ["50"],
        "1 mm = 1 000 micrometer; 1 000 : 20 = 50.",
    ),
    tabel(
        "Klopt dit over een dierlijke cel?",
        [
            ("Ze heeft kleine vacuolen of blaasjes.", J),
            ("Ze heeft centriolen.", J),
            ("Ze heeft één grote centrale vacuole.", F),
            ("Ze heeft een celwand.", F),
        ],
        "Wat ze mist, is de grote centrale vacuole en de wand.",
    ),
    tabel(
        "Klopt dit over de nucleolus?",
        [
            ("Ze ligt in de kern.", J),
            ("Daar worden de ribosomen gemaakt.", J),
            ("Ze heeft een eigen membraan.", F),
        ],
        "Het is een dicht gebied in de kern, geen organel met een membraan.",
    ),
    open_(
        "Leg met een voorbeeld uit dat de bouw van een organel past bij zijn functie.",
        "Een mitochondrion heeft een sterk ingeplooid binnenmembraan, de cristae. Daardoor is er veel oppervlak voor de eindoxidaties, zodat er veel ATP gemaakt kan worden. Of: het ruw ER draagt ribosomen, omdat het eiwitten maakt.",
    ),
]
