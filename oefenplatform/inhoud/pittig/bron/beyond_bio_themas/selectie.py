"""Selectie, soortvorming en de menswording — pittig (🧬 Beyond doorstroom, biologie)."""
import random

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Flessenhals ---------------------------------------------------------------
FH = Prent("flessenhals", "Een populatie kevers voor en na een ramp", "een fles: bovenaan veel kevers in vier kleuren, in de hals enkele, onderaan een nieuwe populatie; letters P, Q en R")
FH.pad("M300 90 L 700 90 L 700 230 C 700 270 560 270 560 300 L 560 360 C 560 390 760 390 760 440 L 760 560 L 240 560 L 240 440 C 240 390 440 390 440 360 L 440 300 C 440 270 300 270 300 230 Z", "#f5f8fb", DONKER, 2.5)
KLEUREN = [ROOD, BLAUW, GROEN, GEEL]
rnd = random.Random(7)
for i in range(40):
    FH.cirkel(320 + rnd.random() * 360, 110 + rnd.random() * 120, 8, KLEUREN[i % 4], DONKER, 1)
for x, y, k in ((480, 300, 0), (520, 320, 0), (500, 345, 2)):
    FH.cirkel(x, y, 8, KLEUREN[k], DONKER, 1)
for i in range(34):
    FH.cirkel(270 + rnd.random() * 460, 450 + rnd.random() * 95, 8, KLEUREN[0] if i % 5 else KLEUREN[2], DONKER, 1)
LFH = {"P": (800, 160), "Q": (640, 320), "R": (830, 500)}
FH.lijn(778, 160, 702, 160, DONKER, 1)
FH.lijn(618, 320, 562, 320, DONKER, 1)
FH.lijn(808, 500, 762, 500, DONKER, 1)
for k, (x, y) in LFH.items():
    FH.letter(x, y, k)
FH.tekst(150, 170, "voor", 17, vet=True)
FH.tekst(150, 330, "ramp", 17, vet=True)
FH.tekst(150, 505, "later", 17, vet=True)
ZFH = {"P": [Prent.zone(300, 90, 400, 160), Prent.rond(*LFH["P"], 22)],
       "Q": [Prent.zone(440, 270, 120, 100), Prent.rond(*LFH["Q"], 22)],
       "R": [Prent.zone(240, 420, 520, 140), Prent.rond(*LFH["R"], 22)]}

# Kaart met isolatie -------------------------------------------------------
KA = Prent("kaart-soortvorming", "Een gebied met muizen", "land met een brede rivier in het midden, links en rechts muizen, een eiland in zee rechtsboven; letters A tot D")
KA.rect(60, 90, 880, 480, "#cfe5f3", DONKER, 14, 2)
KA.pad("M90 130 L 700 120 C 740 250 720 420 690 540 L 100 540 Z", "#e6f0d8", DONKER, 2)
KA.pad("M380 120 C 420 220 360 330 420 420 C 450 470 430 520 440 540 L 500 540 C 490 500 510 460 480 410 C 430 330 480 220 440 120 Z", "#8fc1e3", DONKER, 1.5)
KA.pad("M800 170 C 860 150 900 200 880 250 C 860 290 790 280 780 240 C 770 210 780 180 800 170 Z", "#e6f0d8", DONKER, 2)
for x, y in ((200, 250), (250, 330), (180, 420), (300, 460)):
    KA.ellips(x, y, 14, 9, "#a08060", DONKER, 1.5)
for x, y in ((560, 220), (600, 330), (620, 450), (540, 400)):
    KA.ellips(x, y, 14, 9, "#d8c0a0", DONKER, 1.5)
for x, y in ((830, 210), (850, 235)):
    KA.ellips(x, y, 14, 9, "#f0e6d0", DONKER, 1.5)
LKA = {"A": (240, 180), "B": (590, 160), "C": (450, 600), "D": (840, 320)}
KA.lijn(450, 578, 460, 545, DONKER, 1)
KA.lijn(840, 298, 840, 275, DONKER, 1)
for k, (x, y) in LKA.items():
    KA.letter(x, y, k)
ZKA = {"A": [Prent.zone(100, 200, 270, 300), Prent.rond(*LKA["A"], 22)],
       "B": [Prent.zone(510, 180, 180, 320), Prent.rond(*LKA["B"], 22)],
       "C": [Prent.zone(380, 120, 130, 420), Prent.rond(*LKA["C"], 22)],
       "D": [Prent.zone(775, 150, 115, 140), Prent.rond(*LKA["D"], 22)]}

VRAGEN = [
    klik(
        "Klik op het moment van het flessenhalseffect.",
        FH.bestand, ZFH["Q"],
        "Na de ramp blijven er maar enkele kevers over.",
    ),
    met_prent(FH.bestand, tabel(
        "Kijk naar de kevers. Klopt dit?",
        [
            ("In R zijn er minder kleuren dan in P.", J),
            ("De overlevenden in Q waren niet per se de best aangepaste.", J),
            ("Blauwe en gele kevers zijn later verdwenen door toeval.", J),
            ("R is genetisch even divers als P.", F),
        ],
        "Een flessenhals verkleint de genetische diversiteit.",
    )),
    klik(
        "Klik op de barrière die de muizen geografisch scheidt.",
        KA.bestand, ZKA["C"],
        "De rivier belet de uitwisseling van allelen tussen A en B.",
    ),
    met_prent(KA.bestand, tabel(
        "Kijk naar de kaart. Klopt dit?",
        [
            ("Tussen A en B kan allopatrische soortvorming optreden.", J),
            ("De muizen op D zijn een voorbeeld van het stichterseffect.", J),
            ("Zolang de rivier er is, is er weinig gene flow tussen A en B.", J),
            ("A en B worden zeker dezelfde soort, omdat ze dicht bij elkaar wonen.", F),
        ],
        "Zonder uitwisseling stapelen de verschillen zich op.",
    )),
    met_prent(KA.bestand, mk(
        "Na duizenden jaren zet men muizen van A en B samen. Wanneer zijn het twee verschillende soorten?",
        [
            "Als ze samen geen vruchtbare jongen meer krijgen",
            "Als hun vachtkleur een klein beetje anders is",
            "Als ze aan een andere kant van de rivier wonen",
            "Als ze elk een ander voedsel verkiezen dan vroeger",
        ],
        0,
        "Het gaat om vruchtbare nakomelingen, niet om het uitzicht.",
    )),
    tabel(
        "Welke vorm van isolatie is dit?",
        [
            ("twee kikkersoorten kwaken anders en paren niet", "Gedrag"),
            ("twee planten bloeien in een ander seizoen", "Tijd"),
            ("een zaadcel kan de eicel van de andere soort niet bevruchten", "Gameten"),
            ("twee vogels balderen met een andere dans", "Gedrag"),
        ],
        "Temporeel betekent: in de tijd.",
        kolommen=["Gedrag", "Tijd", "Gameten"],
    ),
    tabel(
        "Prezygotische of postzygotische isolatie?",
        [
            ("een andere paartijd", "Prezygotisch"),
            ("een muildier is onvruchtbaar", "Postzygotisch"),
            ("een andere leefplek in hetzelfde gebied", "Prezygotisch"),
            ("het embryo sterft vroeg af", "Postzygotisch"),
        ],
        "Prezygotisch werkt al voor er een zygote is.",
        kolommen=["Prezygotisch", "Postzygotisch"],
    ),
    tabel(
        "Selectie, drift of gene flow?",
        [
            ("na een storm blijven toevallig vijf hagedissen over", "Drift"),
            ("hennen kiezen hanen met de mooiste staart", "Selectie"),
            ("wolven trekken van de ene vallei naar de andere", "Gene flow"),
            ("een kleine groep vogels sticht een kolonie op een eiland", "Drift"),
            ("een roofdier eet vooral de opvallende prooien", "Selectie"),
        ],
        "Het flessenhals- en het stichterseffect zijn vormen van genetische drift.",
        kolommen=["Selectie", "Drift", "Gene flow"],
    ),
    mk(
        "Waarom houdt een pauwenhaan een staart die hem bij het vluchten hindert?",
        [
            "Hennen kiezen de hanen met de grootste staart",
            "De staart beschermt hem tegen de kou in de winter",
            "Een grote staart maakt hem sneller bij het vliegen",
            "De staart houdt roofdieren op een afstand",
        ],
        0,
        "Seksuele selectie: meer partners kan opwegen tegen een kleinere overlevingskans.",
    ),
    mk(
        "Waarom heeft genetische drift weinig invloed in een populatie van een miljoen dieren?",
        [
            "Het toeval van enkele dieren telt er nauwelijks",
            "In grote populaties ontstaan er nooit mutaties",
            "Grote populaties hebben maar één allel per gen",
            "Grote populaties leven altijd op een eiland",
        ],
        0,
        "Bij tien dieren kan één toevallige dood de allelfrequentie sterk doen schuiven.",
    ),
    koppel(
        "Koppel elk begrip uit de populatiegenetica aan zijn betekenis.",
        [
            ("fitness", "het gemiddeld aantal nakomelingen van een fenotype"),
            ("competitie", "de strijd om voedsel, ruimte of een partner"),
            ("gene flow", "allelen komen binnen of gaan weg door migratie"),
            ("kunstmatige selectie", "de mens kiest de ouderdieren"),
        ],
        ["een verandering in één base van het DNA"],
        "Dat laatste is een puntmutatie.",
    ),
    tabel(
        "Allopatrisch of sympatrisch?",
        [
            ("een gebergte scheidt twee groepen", "Allopatrisch"),
            ("twee groepen in hetzelfde meer eten ander voedsel en paren apart", "Sympatrisch"),
            ("een groep raakt op een eiland afgezonderd", "Allopatrisch"),
            ("twee groepen in hetzelfde bos bloeien op een ander moment", "Sympatrisch"),
        ],
        "Allo betekent ander, sym betekent samen: in hetzelfde gebied.",
        kolommen=["Allopatrisch", "Sympatrisch"],
    ),
    casus(
        "Kwekers kiezen al eeuwen de honden uit die het best kunnen jagen of herders helpen. Zo ontstonden heel verschillende rassen.",
        [
            keuze(
                "Dit heet [[*kunstmatige|natuurlijke|seksuele]] selectie.",
                "De mens, niet de omgeving, kiest de ouderdieren.",
            ),
            tabel(
                "Klopt dit over de hondenrassen?",
                [
                    ("Alle rassen horen nog tot één soort.", J),
                    ("Een chihuahua en een herdershond kunnen vruchtbare jongen krijgen.", J),
                    ("De rassen verschillen in allelfrequenties.", J),
                    ("Elk ras is een aparte soort.", F),
                ],
                "Rassen verschillen in uitzicht, maar blijven vruchtbaar met elkaar.",
            ),
            mk(
                "Waarom hebben sommige rassen veel erfelijke ziekten?",
                [
                    "Ze stammen af van weinig ouderdieren",
                    "Kunstmatige selectie maakt altijd nieuwe mutaties aan",
                    "Rashonden krijgen minder voedsel dan gewone honden",
                    "Honden kunnen geen herstelenzymen voor hun DNA maken",
                ],
                0,
                "Weinig stamouders werkt als een stichterseffect.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van allopatrische soortvorming in volgorde.",
        ["Een populatie met variatie", "Een barrière scheidt twee groepen", "Elke groep evolueert in een eigen omgeving", "De verschillen stapelen zich op", "Ze kunnen geen vruchtbare jongen meer samen krijgen"],
        "Isolatie en tijd zijn nodig.",
    ),
    tabel(
        "Klopt dit over de menswording?",
        [
            ("Rechtop lopen wordt als de eerste grote stap gezien.", J),
            ("Een kommervormig bekken hoort bij het rechtop lopen.", J),
            ("Een groter brein vroeg veel energie.", J),
            ("De mens stamt af van de chimpansee van vandaag.", F),
        ],
        "Mens en chimpansee hebben een gemeenschappelijke, uitgestorven voorouder.",
    ),
    tabel(
        "Delen mens en mensapen dit kenmerk?",
        [
            ("een grijpbare hand met een duim", J),
            ("leven in sociale groepen met banden", J),
            ("een S-vormige wervelkolom om rechtop te lopen", F),
            ("ogen vooraan in het hoofd", J),
        ],
        "De S-vormige wervelkolom hoort bij het rechtop lopen van de mens.",
    ),
    sleep(
        "Een groter brein had ook een prijs: [[hersenen]] gebruiken veel [[energie]] en een groter hoofd maakt de [[geboorte]] moeilijker.",
        ["spieren", "zuurstofloos", "spijsvertering"],
        "Selectie weegt voordelen en nadelen tegen elkaar af.",
    ),
    keuze(
        "Kunnen inschatten wat een ander denkt of voelt, heet [[*theory of mind|gene flow|survival of the fittest]].",
        "Dat hielp onze voorouders om samen te werken.",
    ),
    mk(
        "Waarom verdwijnt een nadelig recessief allel zelden helemaal uit een grote populatie?",
        [
            "Dragers geven het door zonder het te tonen",
            "Het wordt bij elke generatie opnieuw aangemaakt",
            "Recessieve allelen kunnen niet geselecteerd worden",
            "Grote populaties kennen geen natuurlijke selectie",
        ],
        0,
        "Een heterozygoot heeft er geen last van, dus selecteert de omgeving er niet tegen.",
    ),
    tabel(
        "Waarom evolueren bacteriën sneller dan zoogdieren?",
        [
            ("ze hebben heel korte generaties", J),
            ("ze zijn met enorm veel", J),
            ("ze kunnen genen uitwisselen met andere bacteriën", J),
            ("ze leven langer dan zoogdieren", F),
        ],
        "Meer generaties per jaar betekent meer kansen voor selectie.",
    ),
    inv(
        "Een bacterie deelt elke 20 minuten. Hoeveel generaties zijn dat in één dag?",
        ["72"],
        "60 / 20 = 3 per uur, 3 x 24 = 72.",
    ),
    tabel(
        "Klopt dit over het stichterseffect?",
        [
            ("Een kleine groep sticht elders een nieuwe populatie.", J),
            ("De stichters dragen maar een deel van de allelen mee.", J),
            ("Een zeldzaam allel kan in de nieuwe populatie veel voorkomen.", J),
            ("De nieuwe populatie is altijd beter aangepast.", F),
        ],
        "Het is toeval wie meereist, geen selectie.",
    ),
    mk(
        "Hoe kan natuurlijke selectie verklaren dat onze voorouders steeds beter rechtop liepen?",
        [
            "Wie beter liep, liet gemiddeld meer jongen na",
            "Onze voorouders kozen zelf hoe hun lichaam zou veranderen",
            "Elke generatie werd groter doordat ze meer trainde",
            "Selectie speelde geen rol, alleen het toeval telde",
        ],
        0,
        "De variatie was er al, de omgeving selecteerde.",
    ),
    tabel(
        "Klopt dit over fitness?",
        [
            ("Fitness zegt hoeveel nakomelingen een fenotype gemiddeld nalaat.", J),
            ("Een klein, goed gecamoufleerd dier kan een hoge fitness hebben.", J),
            ("Fitness meet vooral hoe gespierd een dier is.", F),
        ],
        "Wat telt, is hoeveel jongen er volgen.",
    ),
    keuze(
        "Twee soorten in hetzelfde gebied die elk een andere leefplek bewonen, zijn gescheiden door [[*habitatisolatie|gametische isolatie|gene flow]].",
        "Ze komen elkaar daardoor zelden tegen.",
    ),
    tabel(
        "Wat is nodig voor soortvorming?",
        [
            ("variatie in de oorspronkelijke populatie", J),
            ("isolatie tussen de groepen", J),
            ("veel tijd en veel generaties", J),
            ("dat alle dieren precies gelijk zijn", F),
        ],
        "Zonder variatie heeft selectie niets om op te werken.",
    ),
    keuze(
        "Gene flow tussen twee populaties maakt ze met de tijd [[*meer gelijk|meer verschillend|onvruchtbaar]].",
        "De allelen worden gemengd.",
    ),
    open_(
        "Leg uit waarom genetische drift en natuurlijke selectie allebei de allelfrequenties veranderen, maar op een andere manier.",
        "Bij natuurlijke selectie bevoordeelt de omgeving de individuen die het best passen: zij krijgen meer jongen en hun allelen worden vaker. Bij genetische drift is het toeval: wie overleeft of meereist, hangt niet af van aanpassing. Drift weegt vooral door in kleine populaties, bv. na een flessenhals of bij een stichterseffect.",
    ),
]
