"""Genexpressie: transcriptie en translatie — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Ribosoom aan het werk ----------------------------------------------------
RB = Prent("ribosoom-translatie", "Een ribosoom tijdens de translatie (schematisch)", "mRNA horizontaal, ribosoom erover met twee plaatsen, tRNA's met aminozuren; letters A tot E")
RB.lijn(60, 420, 940, 420, BLAUW, 6)
RB.tekst(70, 455, "5'", 18, vet=True)
RB.tekst(930, 455, "3'", 18, vet=True)
RB.pad("M300 420 C 300 300 380 260 500 260 C 620 260 700 300 700 420 Z", "#f5d9a8", DONKER, 2.5)
RB.pad("M310 420 C 310 470 360 500 500 500 C 640 500 690 470 690 420 Z", "#f0c98e", DONKER, 2.5)
for x in (420, 510):
    RB.rect(x, 300, 80, 115, "#fbf6ea", DONKER, 10, 1.5)
for x, c in ((370, "AUG"), (460, "GCU"), (550, "UUC"), (640, "UAA")):
    RB.tekst(x, 448, c, 17, vet=True, kleur=BLAUW)
# tRNA op P-plaats met keten
RB.rect(440, 330, 40, 60, "#c8a8e0", DONKER, 6, 1.5)
RB.tekst(460, 410, "CGA", 14, vet=True, kleur=PAARS)
for i, (x, y) in enumerate(((460, 315), (420, 250), (380, 200), (330, 170))):
    RB.cirkel(x, y, 17, ("#9fd39a", "#f3c6d0", "#cfe5f3", "#f2c14e")[i], DONKER, 1.5)
    if i:
        RB.lijn(px, py, x, y, DONKER, 2)
    px, py = x, y
# tRNA op A-plaats
RB.rect(530, 330, 40, 60, "#c8a8e0", DONKER, 6, 1.5)
RB.tekst(550, 410, "AAG", 14, vet=True, kleur=PAARS)
RB.cirkel(550, 315, 17, "#fff3d6", DONKER, 1.5)
# vertrekkend tRNA
RB.rect(760, 230, 40, 60, "#e6d9f0", DONKER, 6, 1.5)
RB.pijl(610, 300, 745, 262, GRIJS, 2)
LRB = {"A": (460, 545), "B": (550, 545), "C": (240, 160), "D": (850, 520), "E": (850, 230)}
RB.lijn(460, 522, 460, 456, DONKER, 1)
RB.lijn(550, 522, 550, 456, DONKER, 1)
RB.lijn(262, 166, 312, 170, DONKER, 1)
RB.lijn(828, 513, 800, 430, DONKER, 1)
RB.lijn(828, 230, 802, 250, DONKER, 1)
for k, (x, y) in LRB.items():
    RB.letter(x, y, k)
ZRB = {"A": [Prent.zone(420, 300, 80, 115), Prent.rond(*LRB["A"], 22)],
       "B": [Prent.zone(510, 300, 80, 115), Prent.rond(*LRB["B"], 22)],
       "C": [Prent.zone(310, 150, 170, 185), Prent.rond(*LRB["C"], 22)],
       "D": [Prent.zone(700, 405, 240, 30), Prent.rond(*LRB["D"], 22)],
       "E": [Prent.zone(755, 225, 50, 70), Prent.rond(*LRB["E"], 22)]}

# Van gen tot rijp mRNA ----------------------------------------------------
RM = Prent("pre-mrna-rijp", "Van pre-mRNA tot rijp mRNA bij een eukaryoot", "bovenaan het pre-mRNA met blokjes 1 tot 3 en stukken ertussen, onderaan het rijpe mRNA; letters P tot S")
RM.tekst(60, 150, "pre-mRNA", 17, "start", vet=True)
xs = [(180, 300, "1"), (300, 430, None), (430, 540, "2"), (540, 700, None), (700, 820, "3")]
for x0, x1, n in xs:
    if n:
        RM.rect(x0, 130, x1 - x0, 40, "#9fd39a", DONKER, 4, 2)
        RM.tekst((x0 + x1) / 2, 158, n, 18, vet=True)
    else:
        RM.rect(x0, 140, x1 - x0, 20, "#e0e0e0", DONKER, 2, 1.5)
RM.pijl(500, 200, 500, 300, DONKER, 3)
RM.tekst(520, 258, "in de kern", 16, "start")
RM.tekst(60, 400, "rijp mRNA", 17, "start", vet=True)
RM.cirkel(250, 400, 22, "#f2c14e", DONKER, 2)
for i, (n, x0) in enumerate((("1", 272), ("2", 392), ("3", 502))):
    RM.rect(x0, 380, (120, 110, 120)[i], 40, "#9fd39a", DONKER, 4, 2)
    RM.tekst(x0 + (60, 55, 60)[i], 408, n, 18, vet=True)
RM.tekst(700, 408, "AAAAAAAA", 18, vet=True, kleur=ORANJE)
LRM = {"P": (240, 80), "Q": (365, 220), "R": (180, 470), "S": (700, 470)}
RM.lijn(240, 102, 240, 128, DONKER, 1)
RM.lijn(365, 198, 365, 162, DONKER, 1)
RM.lijn(195, 455, 232, 418, DONKER, 1)
RM.lijn(700, 448, 700, 420, DONKER, 1)
for k, (x, y) in LRM.items():
    RM.letter(x, y, k)
ZRM = {"P": [Prent.zone(180, 130, 120, 40), Prent.zone(430, 130, 110, 40), Prent.zone(700, 130, 120, 40), Prent.rond(*LRM["P"], 22)],
       "Q": [Prent.zone(300, 140, 130, 20), Prent.zone(540, 140, 160, 20), Prent.rond(*LRM["Q"], 22)],
       "R": [Prent.rond(250, 400, 26), Prent.rond(*LRM["R"], 22)],
       "S": [Prent.zone(630, 385, 150, 30), Prent.rond(*LRM["S"], 22)]}

VRAGEN = [
    klik(
        "Klik op de plaats waar het nieuwe tRNA met zijn aminozuur binnenkomt.",
        RB.bestand, ZRB["B"],
        "Het nieuwe tRNA komt op de A-plaats, de keten hangt op de P-plaats.",
    ),
    klik(
        "Klik op de groeiende keten van aminozuren.",
        RB.bestand, ZRB["C"],
        "Peptidyltransferase hangt de keten telkens aan het nieuwe aminozuur.",
    ),
    met_prent(RB.bestand, tabel(
        "Kijk naar het ribosoom. Klopt dit?",
        [
            ("Het anticodon CGA past op het codon GCU.", J),
            ("E is een tRNA dat zijn aminozuur al afgegeven heeft.", J),
            ("Na nog één stap komt het stopcodon UAA op de A-plaats.", J),
            ("Op het stopcodon UAA past een tRNA met anticodon AUU.", F),
        ],
        "Op een stopcodon past geen tRNA. Een release factor maakt de keten los.",
    )),
    met_prent(RB.bestand, inv(
        "Hoeveel aminozuren telt het eiwit dat van dit mRNA gemaakt wordt?",
        ["3", "drie"],
        "AUG, GCU en UUC geven elk een aminozuur. UAA is een stopcodon.",
    )),
    klik(
        "Klik op de stukken die eruit geknipt worden.",
        RM.bestand, ZRM["Q"],
        "Introns worden uit het pre-mRNA geknipt, exonen blijven.",
    ),
    met_prent(RM.bestand, tabel(
        "Kijk naar het pre-mRNA en het rijpe mRNA. Klopt dit?",
        [
            ("P zijn exonen.", J),
            ("R is de cap aan het begin van het mRNA.", J),
            ("S is de staart van A-nucleotiden.", J),
            ("Een bacterie maakt van haar mRNA ook eerst zo'n rijp mRNA.", F),
        ],
        "Prokaryoten hebben vrijwel geen introns en geen kern.",
    )),
    inv(
        "De matrijsstreng van het DNA leest TAC GGA. Geef het mRNA.",
        ["AUGCCU", "AUG CCU"],
        "T geeft A, A geeft U, C geeft G, G geeft C.",
    ),
    inv(
        "Het codon op het mRNA is UUC. Welk anticodon past daarop?",
        ["AAG"],
        "U past bij A, C bij G.",
    ),
    inv(
        "Een eiwit telt 150 aminozuren. Hoeveel nucleotiden heeft het stuk mRNA dat ervoor codeert, zonder het stopcodon?",
        ["450"],
        "Drie nucleotiden per aminozuur: 3 x 150 = 450.",
    ),
    tabel(
        "Transcriptie of translatie?",
        [
            ("gebeurt bij een eukaryoot in de kern", "Transcriptie"),
            ("gebruikt RNA-polymerase", "Transcriptie"),
            ("gebeurt op de ribosomen", "Translatie"),
            ("tRNA brengt aminozuren aan", "Translatie"),
            ("begint aan de promotor", "Transcriptie"),
        ],
        "Transcriptie maakt RNA, translatie maakt een eiwit.",
        kolommen=["Transcriptie", "Translatie"],
    ),
    koppel(
        "Koppel elk soort RNA aan zijn rol.",
        [
            ("mRNA", "brengt de code van het gen naar het ribosoom"),
            ("tRNA", "brengt een aminozuur aan"),
            ("rRNA", "vormt samen met eiwitten het ribosoom"),
        ],
        ["kopieert het DNA voor de celdeling", "knipt de introns weg"],
        "Het DNA kopiëren is replicatie, met DNA-polymerase.",
    ),
    volgorde(
        "Zet de stappen van gen tot eiwit in volgorde.",
        ["Polymerase bindt op de promotor", "Pre-mRNA wordt gebouwd", "Introns worden eruit geknipt", "mRNA verlaat de kern", "Ribosoom leest vanaf AUG", "Keten wordt afgewerkt en geplooid"],
        "De posttranslationele bewerkingen komen pas na de translatie.",
    ),
    mk(
        "Vooraan een gen valt één nucleotide weg. Waarom verandert dat bijna het hele eiwit?",
        [
            "Het leesraam schuift: alle codons erna veranderen",
            "Het ribosoom slaat dan het startcodon helemaal over en stopt",
            "De promotor wordt onleesbaar voor de polymerase",
            "Er komt een intron extra in het rijpe mRNA terecht",
        ],
        0,
        "De nucleotiden worden per drie gelezen.",
    ),
    mk(
        "Een menselijk gen voor insuline werkt ook in een bacterie. Welke eigenschap van de code maakt dat mogelijk?",
        [
            "Ze is universeel",
            "Ze is gedegenereerd",
            "Ze heeft drie stopcodons",
            "Ze start altijd met methionine",
        ],
        0,
        "Bijna alle organismen lezen dezelfde codons als hetzelfde aminozuur.",
    ),
    tabel(
        "Klopt dit over de genetische code?",
        [
            ("Er zijn 64 codons voor 20 aminozuren.", J),
            ("Een aminozuur kan door meerdere codons gevraagd worden.", J),
            ("Een codon kan voor twee verschillende aminozuren staan.", F),
            ("AUG codeert voor methionine en start de translatie.", J),
        ],
        "Gedegenereerd betekent: meerdere codons per aminozuur, niet omgekeerd.",
    ),
    casus(
        "In een stuk mRNA verandert één base: GCU wordt GCC. Toch is het eiwit precies hetzelfde.",
        [
            keuze(
                "Dat kan omdat de genetische code [[*gedegenereerd|universeel|eenrichtingsverkeer]] is.",
                "GCU en GCC vragen allebei alanine.",
            ),
            mk(
                "Een andere verandering maakt van UGG het codon UGA. Wat gebeurt er?",
                [
                    "De translatie stopt daar te vroeg",
                    "Het ribosoom slaat dat codon gewoon over",
                    "Er komt een extra aminozuur bij het einde",
                    "De keten wordt langer dan normaal",
                ],
                0,
                "UGA is een stopcodon: het eiwit wordt te kort.",
            ),
            tabel(
                "Welk gevolg heeft deze verandering in het mRNA?",
                [
                    ("GCU wordt GCC", "Zelfde eiwit"),
                    ("UGG wordt UGA", "Eiwit te kort"),
                    ("één base valt weg vooraan", "Leesraam verschoven"),
                ],
                "Een verschuiving van het leesraam verandert alle volgende codons.",
                kolommen=["Zelfde eiwit", "Eiwit te kort", "Leesraam verschoven"],
            ),
        ],
    ),
    sleep(
        "Bij de [[activatie]] koppelt een enzym met behulp van [[ATP]] het juiste aminozuur aan zijn tRNA. Het tRNA herkent het codon met zijn [[anticodon]].",
        ["splicing", "glucose", "promotor"],
        "Zo komt elk aminozuur op de juiste plaats in de keten.",
    ),
    tabel(
        "Klopt dit over een polysoom?",
        [
            ("Meerdere ribosomen lezen hetzelfde mRNA.", J),
            ("Zo komen er snel veel eiwitten.", J),
            ("Elk ribosoom maakt een ander eiwit van hetzelfde mRNA.", F),
        ],
        "Elk ribosoom leest dezelfde code en maakt dus hetzelfde eiwit.",
    ),
    mk(
        "Een levercel en een spiercel van dezelfde persoon maken andere eiwitten. Hoe komt dat?",
        [
            "Ze lezen andere genen af uit hetzelfde DNA",
            "Ze hebben een ander DNA in hun kern",
            "Ze gebruiken een andere genetische code",
            "Hun ribosomen lezen het mRNA in omgekeerde richting",
        ],
        0,
        "Transcriptiefactoren beslissen welke genen gelezen worden.",
    ),
    tabel(
        "Hoe kan één gen toch meerdere eiwitten opleveren?",
        [
            ("de exonen worden op verschillende manieren aan elkaar gezet", J),
            ("het eiwit wordt na de translatie anders afgewerkt", J),
            ("het ribosoom kiest zelf een andere code", F),
        ],
        "Dat heet alternatieve splicing.",
    ),
    keuze(
        "Het enzym van het ribosoom dat de peptidebinding legt, heet [[*peptidyltransferase|RNA-polymerase|ligase]].",
        "Het verbindt het nieuwe aminozuur met de keten.",
    ),
    tabel(
        "Klopt dit over posttranslationele modificatie?",
        [
            ("Er kunnen sacharidegroepen aangehangen worden.", J),
            ("De keten kan ingekort worden.", J),
            ("Het eiwit krijgt zijn juiste vorm.", J),
            ("De volgorde van de codons in het mRNA verandert.", F),
        ],
        "Dat gebeurt onder meer in het ER en het golgiapparaat.",
    ),
    mk(
        "Waarom blijft het DNA in de kern, terwijl een mRNA de kern verlaat?",
        [
            "Zo blijft het origineel veilig, alleen een kopie gaat",
            "Het DNA is veel te klein om de kern uit te geraken",
            "De ribosomen liggen allemaal binnen in de kern",
            "Het mRNA moet eerst in het cytoplasma gerepliceerd worden",
        ],
        0,
        "Het mRNA is de boodschapper: het mag na gebruik afgebroken worden.",
    ),
    tabel(
        "Exon of intron?",
        [
            ("wordt uit het pre-mRNA geknipt", "Intron"),
            ("blijft in het rijpe mRNA", "Exon"),
            ("komt niet in het eiwit terecht", "Intron"),
            ("kan bij alternatieve splicing anders gecombineerd worden", "Exon"),
        ],
        "Exonen blijven staan, introns verdwijnen voor het mRNA de kern verlaat.",
        kolommen=["Exon", "Intron"],
    ),
    keuze(
        "De aanlegplaats van RNA-polymerase vooraan een gen heet de [[*promotor|terminator|ribosoom]].",
        "Transcriptiefactoren binden daar mee.",
    ),
    tabel(
        "Klopt dit over RNA-polymerase?",
        [
            ("Het leest de matrijsstreng.", J),
            ("Het bouwt het mRNA van 5' naar 3'.", J),
            ("Het heeft geen primer nodig.", J),
            ("Het zet thymine tegenover adenine.", F),
        ],
        "In RNA komt uracil tegenover adenine.",
    ),
    inv(
        "Hoeveel verschillende codons zijn er met vier soorten nucleotiden en drie nucleotiden per codon?",
        ["64"],
        "4 x 4 x 4 = 64.",
    ),
    open_(
        "Leg uit hoe de volgorde van de nucleotiden in een gen de vorm en de werking van een eiwit bepaalt.",
        "De volgorde van de nucleotiden wordt overgeschreven in het mRNA. Per codon van drie nucleotiden zet het ribosoom een bepaald aminozuur in de keten. De volgorde van de aminozuren bepaalt hoe de keten plooit, en dus de vorm. Alleen met de juiste vorm past een eiwit op zijn partner, zoals een enzym op zijn substraat.",
    ),
]
