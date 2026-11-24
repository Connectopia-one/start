"""DNA-technologie en gentechnologie — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Gel met DNA-fingerprints -------------------------------------------------
GE = Prent("gel-fingerprint", "Gelelektroforese: spoor van een misdrijf en drie verdachten", "gel met vijf banen: stukken van bekende lengte, spoor, verdachte 1, 2 en 3; min bovenaan, plus onderaan")
GE.rect(150, 110, 700, 430, "#eef3f7", DONKER, 10, 2)
GE.tekst(110, 140, "−", 34, vet=True)
GE.tekst(110, 530, "+", 34, vet=True)
BANEN = [("ladder", [180, 240, 300, 360, 420, 480]), ("spoor", [220, 330, 455]),
         ("1", [205, 330, 400]), ("2", [220, 330, 455]), ("3", [250, 290, 455])]
for i, (n, ys) in enumerate(BANEN):
    x = 220 + i * 140
    GE.rect(x - 35, 120, 70, 14, "#c9d3dc", DONKER, 2, 1)
    for y in ys:
        GE.rect(x - 35, y, 70, 10, "#3b5f8a", "none", 3, 0)
    GE.tekst(x, 90, n if n != "ladder" else "M", 18, vet=True)
GE.tekst(500, 580, "M = stukken DNA met een gekende lengte", 15)
GE.tekst(910, 190, "lang", 15)
GE.tekst(910, 480, "kort", 15)
GE.pijl(910, 210, 910, 455, GRIJS, 2)
ZGE = {n: [Prent.zone(220 + i * 140 - 50, 70, 100, 470)] for i, (n, ys) in enumerate(BANEN)}

# Bacterie met plasmiden ---------------------------------------------------
BA = Prent("bacterie-plasmide", "Twee bacteriën wisselen DNA uit", "twee staafvormige bacteriën verbonden door een buisje; in de linkse een grote kluwen en kleine ringetjes; letters A tot C")
for cx in (260, 720):
    BA.rect(cx - 170, 220, 340, 180, "#e6f0d8", DONKER, 90, 2.5)
BA.pad("M180 300 C 210 250 280 260 300 300 C 320 340 260 360 230 340 C 200 320 250 290 270 320 C 290 350 200 360 180 330 Z", "none", BLAUW, 3)
for x, y in ((360, 260), (370, 340)):
    BA.cirkel(x, y, 16, "none", ROOD, 3)
BA.cirkel(650, 340, 16, "none", ROOD, 3)
BA.pad("M690 300 C 720 260 780 270 790 300 C 800 330 740 350 720 330 C 700 310 760 290 770 320", "none", BLAUW, 3)
BA.rect(430, 302, 120, 16, "#e6f0d8", DONKER, 8, 2)
BA.pijl(440, 290, 540, 290, ROOD, 2)
LBA = {"A": (240, 160), "B": (390, 470), "C": (490, 220)}
BA.lijn(240, 182, 240, 268, DONKER, 1)
BA.lijn(385, 448, 370, 358, DONKER, 1)
BA.lijn(490, 242, 490, 300, DONKER, 1)
for k, (x, y) in LBA.items():
    BA.letter(x, y, k)
ZBA = {"A": [Prent.zone(175, 250, 130, 110), Prent.rond(*LBA["A"], 22)],
       "B": [Prent.rond(360, 260, 22), Prent.rond(370, 340, 22), Prent.rond(650, 340, 22), Prent.rond(*LBA["B"], 22)],
       "C": [Prent.zone(430, 298, 120, 24), Prent.rond(*LBA["C"], 22)]}

VRAGEN = [
    klik(
        "Klik op de verdachte van wie het DNA past bij het spoor.",
        GE.bestand, ZGE["2"],
        "Alle bandjes van verdachte 2 liggen op dezelfde hoogte als die van het spoor.",
    ),
    met_prent(GE.bestand, tabel(
        "Kijk naar de gel. Klopt dit?",
        [
            ("De bandjes onderaan zijn de kortste stukken DNA.", J),
            ("Het DNA is van min naar plus gewandeld.", J),
            ("Verdachte 3 deelt één bandje met het spoor, maar is niet de dader.", J),
            ("De bovenste bandjes zijn het verst gewandeld.", F),
        ],
        "Kleine stukken glippen sneller door de gel en geraken het verst.",
    )),
    klik(
        "Klik op een plasmide.",
        BA.bestand, ZBA["B"],
        "Een plasmide is een klein los ringetje DNA naast het chromosoom.",
    ),
    met_prent(BA.bestand, tabel(
        "Kijk naar de bacteriën. Klopt dit?",
        [
            ("A is het ringvormige chromosoom.", J),
            ("Langs C gaat er een plasmide naar de rechtse bacterie.", J),
            ("Dit heet conjugatie.", J),
            ("A ligt in een kern met een kernmembraan.", F),
        ],
        "Een bacterie is een prokaryoot: haar chromosoom ligt vrij in het cytoplasma.",
    )),
    tabel(
        "Transformatie, conjugatie of transductie?",
        [
            ("een bacterie neemt vrij DNA uit haar omgeving op", "Transformatie"),
            ("DNA gaat via een brug van de ene bacterie naar de andere", "Conjugatie"),
            ("een faag neemt bacterieel DNA mee naar een andere bacterie", "Transductie"),
            ("een plasmide gaat langs een pilus", "Conjugatie"),
        ],
        "Bij transductie is een virus de koerier.",
        kolommen=["Transformatie", "Conjugatie", "Transductie"],
    ),
    tabel(
        "Lytische of lysogene cyclus?",
        [
            ("de bacterie barst open", "Lytisch"),
            ("het faag-DNA wordt ingebouwd in het chromosoom", "Lysogeen"),
            ("het faag-DNA gaat bij elke deling mee", "Lysogeen"),
            ("de cel maakt meteen nieuwe fagen", "Lytisch"),
        ],
        "In de lysogene cyclus blijft het faag-DNA een tijd rustig zitten.",
        kolommen=["Lytisch", "Lysogeen"],
    ),
    volgorde(
        "Zet de stappen in volgorde om een bacterie menselijke insuline te laten maken.",
        ["Insulinegen en plasmide knippen met hetzelfde restrictie-enzym", "De sticky ends laten samenkomen", "Ligase hecht de stukken vast", "Het recombinant plasmide in een bacterie brengen", "De bacteriën laten delen en insuline oogsten"],
        "Elke dochterbacterie krijgt het plasmide mee en maakt insuline.",
    ),
    koppel(
        "Koppel elk hulpmiddel aan zijn taak in de gentechnologie.",
        [
            ("restrictie-enzym", "knipt DNA op een vaste plaats"),
            ("ligase", "hecht geknipte stukken definitief vast"),
            ("plasmide", "dient als vector om DNA in een cel te brengen"),
            ("Cas-enzym", "knipt op de plaats die een stukje RNA aanwijst"),
        ],
        ["maakt van mRNA een eiwit"],
        "Dat laatste doet een ribosoom.",
    ),
    mk(
        "Waarom knipt men het gen en het plasmide met hetzelfde restrictie-enzym?",
        [
            "Dan passen hun sticky ends op elkaar",
            "Dan wordt het plasmide vanzelf groter dan de bacterie",
            "Dan hoeft er nadien geen bacterie meer te delen",
            "Dan verandert het gen in een stuk RNA",
        ],
        0,
        "Een schuine knip laat enkelstrengige uiteinden achter die complementair zijn.",
    ),
    inv(
        "Een PCR verdubbelt het DNA bij elke cyclus. Met hoeveel kopieën zit je na 10 cycli als je met 1 molecule begint?",
        ["1024"],
        "2 tot de tiende = 1024.",
    ),
    volgorde(
        "Zet de stappen van één PCR-cyclus in volgorde.",
        ["Verhitten tot de strengen loskomen", "Afkoelen zodat de primers binden", "Polymerase bouwt de nieuwe strengen"],
        "Daarna begint de volgende cyclus opnieuw met verhitten.",
    ),
    mk(
        "Een speurder vindt één haar op een plaats delict. Waarom laat het labo eerst een PCR lopen?",
        [
            "Er is te weinig DNA om meteen mee te werken",
            "Een PCR maakt het DNA positief geladen voor de gel",
            "Een PCR knipt het DNA op de juiste plaatsen",
            "Een PCR verandert het DNA in RNA voor de test",
        ],
        0,
        "Met een PCR maak je van een piepklein staal miljoenen kopieën.",
    ),
    tabel(
        "Klopt dit over gelelektroforese?",
        [
            ("DNA is negatief geladen door de fosfaatgroepen.", J),
            ("Kleine stukken wandelen het verst.", J),
            ("DNA wandelt naar de pluspool.", J),
            ("Lange stukken gaan sneller dan korte.", F),
        ],
        "De gel werkt als een zeef.",
    ),
    tabel(
        "Waarvoor gebruikt men deze techniek?",
        [
            ("vaderschap vaststellen", "DNA-fingerprint"),
            ("een gen op zijn plaats aanpassen", "CRISPR-Cas"),
            ("van een piepklein staal genoeg DNA maken", "PCR"),
            ("een spoor vergelijken met een verdachte", "DNA-fingerprint"),
        ],
        "Een PCR gaat meestal aan een fingerprint vooraf.",
        kolommen=["PCR", "DNA-fingerprint", "CRISPR-Cas"],
    ),
    casus(
        "Een onderzoeker wil een maïsplant maken die beter tegen insecten bestand is.",
        [
            keuze(
                "Hij bouwt een gen uit een [[*bodembacterie|insect|virus van de mens]] in dat een gifstof voor insecten maakt.",
                "Het gen uit de bacterie laat de plant zelf de gifstof maken.",
            ),
            keuze(
                "Omdat het gen uit een andere soort komt, is de plant [[*transgeen|cisgeen|gekloond]].",
                "Cisgeen blijft binnen soorten die zich ook zo kunnen kruisen.",
            ),
            tabel(
                "Is dit een vraag die men maatschappelijk over zo'n ggo bespreekt?",
                [
                    ("Wat zijn de gevolgen op lange termijn voor de natuur?", J),
                    ("Wie mag het zaad verkopen?", J),
                    ("Is het veilig om te eten?", J),
                    ("Kan de plant gaan wandelen?", F),
                ],
                "Het gaat over gezondheid, natuur, economie en ethiek.",
            ),
        ],
    ),
    tabel(
        "Welk soort klonen is dit?",
        [
            ("een eeneiige tweeling", "Natuurlijk"),
            ("een kern van een lichaamscel in een ontkernde eicel, tot een nieuw dier", "Reproductief"),
            ("weefsel kweken om een patiënt te behandelen", "Therapeutisch"),
            ("een stekje van een plant", "Natuurlijk"),
        ],
        "Bij reproductief klonen ontstaat een volledig nieuw individu.",
        kolommen=["Natuurlijk", "Reproductief", "Therapeutisch"],
    ),
    mk(
        "Een gekloonde hond gedraagt zich anders dan de oorspronkelijke hond. Hoe komt dat?",
        [
            "De omgeving en de opvoeding verschillen",
            "Het DNA van een kloon is altijd half anders",
            "Een kloon krijgt nooit een eigen kern",
            "Klonen verandert alle genen voor gedrag",
        ],
        0,
        "Een kloon is als een eeneiige tweeling, die later geboren wordt.",
    ),
    sleep(
        "CRISPR-Cas komt uit het [[afweersysteem]] van bacteriën. Een stukje [[RNA]] wijst de plaats in het DNA aan, en het [[Cas]]-enzym knipt daar.",
        ["spijsverteringsstelsel", "eiwit", "ligase"],
        "Bacteriën bewaren stukjes faag-DNA om een volgende besmetting te herkennen.",
    ),
    tabel(
        "Klopt dit over een DNA-fingerprint?",
        [
            ("Iedereen heeft een eigen aantal herhalingen op bepaalde plaatsen.", J),
            ("Een eeneiige tweeling heeft dezelfde fingerprint.", J),
            ("Een kind heeft van elk bandje de helft van de moeder en de helft van de vader.", F),
        ],
        "Een kind heeft elk bandje van de moeder of van de vader, per locus één van elk.",
    ),
    tabel(
        "Klopt dit over een vector?",
        [
            ("Een plasmide kan als vector dienen.", J),
            ("Ook een virus kan als vector dienen.", J),
            ("Een liposoom kan DNA in een cel brengen.", J),
            ("Een vector is het gen dat men wil inbrengen.", F),
        ],
        "De vector is de drager, niet de lading.",
    ),
    mk(
        "Waarom kan een bacterie een menselijk gen gewoon aflezen?",
        [
            "De genetische code is bijna universeel",
            "Bacteriën hebben net als mensen een kern",
            "Het menselijke gen bevat geen codons",
            "Bacteriën maken zelf ook altijd insuline",
        ],
        0,
        "Wel moeten introns eerst weg, want bacteriën knippen geen introns.",
    ),
    tabel(
        "Rechtstreeks in de cel of met een vector?",
        [
            ("micro-injectie met een fijne naald", "Rechtstreeks"),
            ("het Ti-plasmide van een bodembacterie", "Met een vector"),
            ("elektroporatie met een stroomstoot", "Rechtstreeks"),
            ("een onschadelijk gemaakt virus", "Met een vector"),
        ],
        "Bij elektroporatie gaan er kort gaatjes in het membraan open.",
        kolommen=["Rechtstreeks", "Met een vector"],
    ),
    keuze(
        "Een PCR die ook de hoeveelheid DNA meet, heet een [[*kwantitatieve|lytische|recombinante]] PCR.",
        "Zo kan men bv. meten hoeveel virus er in een staal zit.",
    ),
    tabel(
        "Klopt dit over antibioticumresistentie?",
        [
            ("Een resistentiegen kan op een plasmide liggen.", J),
            ("Plasmiden kunnen van bacterie naar bacterie gaan.", J),
            ("Zo verspreidt resistentie zich snel.", J),
            ("Een plasmide kan alleen naar dochtercellen gaan.", F),
        ],
        "Door conjugatie gaat een plasmide ook naar bacteriën ernaast.",
    ),
    keuze(
        "Een virus dat bacteriën besmet, heet een [[*bacteriofaag|plasmide|vector]].",
        "Een faag kan zich alleen in een levende bacterie vermenigvuldigen.",
    ),
    tabel(
        "Klopt dit over recombinant DNA?",
        [
            ("Het bevat stukken DNA van verschillende herkomst.", J),
            ("Een plasmide met een menselijk gen is recombinant DNA.", J),
            ("Ligase is nodig om het te maken.", J),
            ("Het ontstaat door DNA in gelijke stukken te knippen.", F),
        ],
        "Recombinant betekent: opnieuw samengesteld.",
    ),
    keuze(
        "Het uitlezen van de volledige basenvolgorde van een stuk DNA heet [[*sequencing|klonen|transductie]].",
        "Zo kan men een mutatie in een gen precies terugvinden.",
    ),
    open_(
        "Leg uit hoe men met gelelektroforese kan nagaan wie de vader van een kind is.",
        "Men vermenigvuldigt met een PCR het DNA van moeder, kind en mogelijke vader en knipt of selecteert de plaatsen met herhalingen. In de gel wandelen de stukken volgens hun lengte. Elk bandje van het kind moet bij de moeder of bij de vader te vinden zijn. Bandjes die niet van de moeder komen, moeten dus bij de echte vader passen.",
    ),
]
