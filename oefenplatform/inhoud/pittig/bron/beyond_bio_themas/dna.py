"""DNA, RNA en de replicatie — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Stukje DNA als ladder ----------------------------------------------------
DL = Prent("dna-ladder", "Een stukje DNA, uitgerold als ladder", "twee strengen met fosfaat en suiker, basenparen in het midden; letters A tot E")
BASEN = [("A", "T"), ("C", "G"), ("G", "C"), ("T", "A")]
KL = {"A": "#e8a0b0", "T": "#f2c14e", "C": "#8fc1e3", "G": "#9fd39a"}
for i, (l, r) in enumerate(BASEN):
    y = 150 + i * 110
    DL.cirkel(220, y, 22, "#f5d9a8", DONKER, 1.5)
    DL.tekst(220, y + 6, "P", 15, vet=True)
    DL.svg(f'<polygon points="290,{y-28} 330,{y-10} 320,{y+28} 260,{y+28} 250,{y-10}" fill="#dde6ee" stroke="{DONKER}" stroke-width="1.5"/>')
    DL.lijn(242, y, 252, y, DONKER, 2)
    DL.rect(330, y - 18, 140, 36, KL[l], DONKER, 6, 1.5)
    DL.tekst(400, y + 6, l, 18, vet=True)
    DL.rect(530, y - 18, 140, 36, KL[r], DONKER, 6, 1.5)
    DL.tekst(600, y + 6, r, 18, vet=True)
    n = 2 if l in "AT" else 3
    for k in range(n):
        yy = y - 10 + k * (20 / max(1, n - 1))
        DL.lijn(472, yy, 528, yy, DONKER, 1.5, stippel=True)
    DL.svg(f'<polygon points="710,{y-28} 750,{y-10} 740,{y+28} 680,{y+28} 670,{y-10}" fill="#dde6ee" stroke="{DONKER}" stroke-width="1.5"/>')
    DL.cirkel(780, y, 22, "#f5d9a8", DONKER, 1.5)
    DL.tekst(780, y + 6, "P", 15, vet=True)
    DL.lijn(748, y, 758, y, DONKER, 2)
    if i < 3:
        DL.lijn(220, y + 22, 220, y + 88, DONKER, 2)
        DL.lijn(780, y + 22, 780, y + 88, DONKER, 2)
LDL = {"A": (120, 150), "B": (290, 595), "C": (400, 595), "D": (500, 595), "E": (880, 370)}
DL.lijn(142, 150, 196, 150, DONKER, 1)
DL.lijn(290, 573, 290, 510, DONKER, 1)
DL.lijn(400, 573, 400, 498, DONKER, 1)
DL.lijn(500, 573, 500, 485, DONKER, 1)
DL.svg(f'<rect x="200" y="100" width="150" height="100" rx="14" fill="none" stroke="{PAARS}" stroke-width="3" stroke-dasharray="8 5"/>')
DL.lijn(858, 370, 805, 370, DONKER, 1)
for k, (x, y) in LDL.items():
    DL.letter(x, y, k)
ZDL = {"A": [Prent.rond(220, 150, 26), Prent.rond(*LDL["A"], 22)],
       "B": [Prent.zone(250, 450, 80, 60), Prent.rond(*LDL["B"], 22)],
       "C": [Prent.zone(330, 462, 140, 36), Prent.rond(*LDL["C"], 22)],
       "D": [Prent.zone(472, 455, 56, 40), Prent.rond(*LDL["D"], 22)],
       "E": [Prent.zone(670, 100, 140, 440), Prent.rond(*LDL["E"], 22)]}

# Replicatievork -----------------------------------------------------------
RV = Prent("replicatievork", "De replicatievork (schematisch)", "ouderlijk DNA rechts, de vork opent naar links; bovenaan een doorlopende nieuwe streng, onderaan stukjes; letters P tot T")
RV.lijn(620, 300, 940, 300, DONKER, 4)
RV.lijn(620, 330, 940, 330, DONKER, 4)
RV.pad("M620 300 C 560 280 480 200 80 200", "none", DONKER, 4)
RV.pad("M620 330 C 560 350 480 430 80 430", "none", DONKER, 4)
def _bz(p0, p1, p2, p3, t):
    return tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t * t * c + t ** 3 * d for a, b, c, d in zip(p0, p1, p2, p3))


_BOV = ((590, 300), (530, 270), (470, 215), (110, 215))
_OND = ((590, 330), (530, 345), (460, 415), (110, 415))
_q = [_bz(*_BOV, i / 30) for i in range(31)]
RV.pad("M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in _q[::-1][:-2]), "none", BLAUW, 4)
RV.svg(f'<polygon points="{_q[2][0]:.0f},{_q[2][1]:.0f} {_q[5][0]-4:.0f},{_q[5][1]-12:.0f} {_q[5][0]+6:.0f},{_q[5][1]+10:.0f}" fill="{BLAUW}"/>')
_STUK = []
for t0, t1 in ((0.20, 0.42), (0.50, 0.72), (0.80, 0.98)):
    pts = [_bz(*_OND, t0 + (t1 - t0) * i / 12) for i in range(13)]
    RV.pad("M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts[2:]), "none", ROOD, 4)
    RV.svg(f'<polygon points="{pts[12][0]:.0f},{pts[12][1]:.0f} {pts[10][0]:.0f},{pts[10][1]-10:.0f} {pts[10][0]:.0f},{pts[10][1]+10:.0f}" fill="{ROOD}"/>')
    RV.pad(f"M{pts[0][0]:.0f} {pts[0][1]:.0f} L{pts[2][0]:.0f} {pts[2][1]:.0f}", "none", ORANJE, 9)
    _STUK.append(pts)
RV.ellips(620, 315, 34, 40, "#c8a8e0", DONKER, 2)
RV.ellips(_q[3][0], _q[3][1], 24, 18, "#9fd39a", DONKER, 1.5)
LRV = {"P": (620, 230), "Q": (300, 150), "R": (300, 500), "S": (90, 500), "T": (520, 160)}
RV.lijn(620, 252, 620, 275, DONKER, 1)
RV.lijn(300, 172, 300, 208, DONKER, 1)
RV.lijn(300, 478, _STUK[1][6][0], _STUK[1][6][1] + 6, DONKER, 1)
RV.lijn(105, 480, _STUK[2][1][0], _STUK[2][1][1] + 6, DONKER, 1)
RV.lijn(522, 182, _q[3][0] - 8, _q[3][1] - 16, DONKER, 1)
for k, (x, y) in LRV.items():
    RV.letter(x, y, k)
RV.tekst(780, 280, "ouderlijk DNA", 15)
RV.tekst(500, 560, "de vork beweegt naar rechts  →", 15)
ZRV = {"P": [Prent.rond(620, 315, 40), Prent.rond(*LRV["P"], 22)],
       "Q": [Prent.zone(150, 198, 300, 30), Prent.rond(*LRV["Q"], 22)],
       "R": [Prent.rond(*_STUK[1][6], 30), Prent.rond(*_STUK[0][6], 30), Prent.rond(*LRV["R"], 22)],
       "S": [Prent.rond(*_STUK[2][1], 16), Prent.rond(*LRV["S"], 22)],
       "T": [Prent.rond(*_q[3], 28), Prent.rond(*LRV["T"], 22)]}

VRAGEN = [
    klik(
        "Klik op een stikstofbase.",
        DL.bestand, ZDL["C"],
        "De basen zitten aan de binnenkant van de ladder, als sporten.",
    ),
    klik(
        "Klik op de waterstofbruggen tussen twee basen.",
        DL.bestand, ZDL["D"],
        "Tussen T en A liggen twee waterstofbruggen.",
    ),
    met_prent(DL.bestand, tabel(
        "Kijk naar de ladder. Klopt dit?",
        [
            ("Het paarse kader omvat een fosfaat en een suiker, maar nog geen base.", J),
            ("B is een suiker, desoxyribose.", J),
            ("Tussen C en G liggen drie waterstofbruggen.", J),
            ("E is een tweede, identieke streng met dezelfde basenvolgorde.", F),
        ],
        "E is de complementaire streng: tegenover A staat T, tegenover C staat G.",
    )),
    klik(
        "Klik op het enzym dat de twee strengen uit elkaar haalt.",
        RV.bestand, ZRV["P"],
        "Helicase verbreekt de waterstofbruggen aan de vork.",
    ),
    klik(
        "Klik op een okazakifragment.",
        RV.bestand, ZRV["R"],
        "De lagging strand wordt in stukjes gebouwd.",
    ),
    met_prent(RV.bestand, tabel(
        "Kijk naar de replicatievork. Klopt dit?",
        [
            ("Q is de leading strand.", J),
            ("S is een kort stukje RNA.", J),
            ("De stukjes onderaan worden later door ligase verbonden.", J),
            ("Onderaan bouwt polymerase in dezelfde richting als de vork beweegt.", F),
        ],
        "Bovenaan bouwt polymerase mee met de vork, onderaan ertegenin. Daarom komen er onderaan stukjes.",
    )),
    tabel(
        "Hoeveel waterstofbruggen liggen er tussen deze basen?",
        [
            ("A en T", "2"),
            ("C en G", "3"),
            ("T en A", "2"),
            ("G en C", "3"),
        ],
        "Een stuk DNA met veel C-G-paren is daardoor stabieler.",
        kolommen=["2", "3"],
    ),
    inv(
        "Een DNA-molecule bevat 30 % adenine. Hoeveel procent guanine bevat ze?",
        ["20", "20 %", "20%"],
        "A = T = 30 %, samen 60 %. Er blijft 40 % over voor C en G, dus 20 % G.",
    ),
    inv(
        "Geef de complementaire DNA-streng van ATTGCA.",
        ["TAACGT"],
        "A tegenover T, C tegenover G.",
    ),
    inv(
        "Een stukje DNA heeft 10 basenparen: 6 A-T-paren en 4 C-G-paren. Hoeveel waterstofbruggen zijn dat samen?",
        ["24"],
        "6 x 2 + 4 x 3 = 12 + 12 = 24.",
    ),
    tabel(
        "DNA, RNA of allebei?",
        [
            ("bevat ribose", "RNA"),
            ("bevat thymine", "DNA"),
            ("bevat adenine", "Allebei"),
            ("is meestal een dubbele helix", "DNA"),
            ("bevat uracil", "RNA"),
        ],
        "Adenine, cytosine en guanine komen in beide voor.",
        kolommen=["DNA", "RNA", "Allebei"],
    ),
    koppel(
        "Koppel elk enzym of eiwit aan zijn taak bij de replicatie.",
        [
            ("helicase", "scheidt de twee strengen"),
            ("primase", "legt een RNA-beginpunt"),
            ("DNA-polymerase", "hangt nucleotiden aan"),
            ("ligase", "plakt de fragmenten aan elkaar"),
            ("topoisomerase", "haalt de spanning voor de vork weg"),
        ],
        ["leest het DNA af naar mRNA"],
        "Een gen naar mRNA overschrijven is transcriptie, geen replicatie.",
    ),
    volgorde(
        "Zet de stappen aan de lagging strand in volgorde.",
        ["Helicase opent de helix", "Primase legt een primer", "Polymerase bouwt een okazakifragment", "De primer wordt door DNA vervangen", "Ligase sluit het gaatje"],
        "Pas als de primer weg is, kan ligase de stukjes verbinden.",
    ),
    mk(
        "Een cel mist het enzym ligase. Wat merk je na de replicatie?",
        [
            "De lagging strand blijft uit stukjes bestaan",
            "De twee strengen van de helix gaan niet open",
            "Er worden nergens nog primers gelegd",
            "De leading strand krijgt overal uracil",
        ],
        0,
        "De leading strand is één stuk en heeft geen ligase nodig.",
    ),
    mk(
        "Waarom kan DNA-polymerase niet zonder primase?",
        [
            "Polymerase bouwt enkel verder aan een bestaand stuk",
            "Polymerase kan de waterstofbruggen niet zelf verbreken",
            "Primase levert alle energie voor de nieuwe streng van DNA",
            "Primase leest af welke base tegenover welke hoort",
        ],
        0,
        "De primer is een kort RNA-stukje waar polymerase op aansluit.",
    ),
    tabel(
        "Leading strand of lagging strand?",
        [
            ("in één stuk gebouwd", "Leading"),
            ("bestaat uit okazakifragmenten", "Lagging"),
            ("heeft veel primers nodig", "Lagging"),
            ("loopt mee met de vork", "Leading"),
        ],
        "Beide worden van 5' naar 3' gebouwd, maar in tegengestelde richting.",
        kolommen=["Leading", "Lagging"],
    ),
    casus(
        "In een labo laat men bacteriën lang groeien met zwaar stikstof. Hun DNA is dan zwaar. Daarna groeien ze één generatie verder met gewoon, licht stikstof.",
        [
            mk(
                "Hoe ziet het DNA van de nieuwe bacteriën eruit?",
                [
                    "Telkens één zware en één lichte streng",
                    "De helft van de moleculen is volledig zwaar",
                    "Elke molecule is nu volledig licht geworden",
                    "Elke streng is half zwaar en half licht",
                ],
                0,
                "De oude streng blijft en dient als matrijs voor een nieuwe streng.",
            ),
            keuze(
                "Zo'n replicatie, met telkens één oude en één nieuwe streng, heet [[*semiconservatief|conservatief|gefragmenteerd]].",
                "Semi betekent half: de helft blijft bewaard.",
            ),
            inv(
                "Na nog één generatie op licht stikstof: hoeveel van de 4 DNA-moleculen bevatten nog een zware streng?",
                ["2", "twee"],
                "De twee zware strengen zitten elk in één molecule, de andere twee zijn volledig licht.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over de bouw van het chromosoom?",
        [
            ("DNA windt zich rond acht histonen.", J),
            ("Histonen zijn positief geladen.", J),
            ("Heterochromatine ligt opgerold en wordt weinig gelezen.", J),
            ("Een chromosoom is het best te zien als het helemaal ontrold is.", F),
        ],
        "Tijdens de celdeling condenseert het chromatine sterk.",
    ),
    tabel(
        "Waar of niet waar voor homologe chromosomen?",
        [
            ("Ze dragen dezelfde genen op dezelfde loci.", J),
            ("Ze komen van dezelfde ouder.", F),
            ("De allelen kunnen verschillen.", J),
            ("Het zijn zusterchromatiden.", F),
        ],
        "Zusterchromatiden zijn identieke kopieën na de replicatie. Homologen komen van vader en moeder.",
    ),
    mk(
        "Een lichaamscel heeft 46 chromosomen. Hoeveel chromatiden telt ze vlak na de S-fase?",
        [
            "92 chromatiden",
            "23 chromatiden",
            "46 chromatiden",
            "184 chromatiden",
        ],
        0,
        "Na de replicatie heeft elk van de 46 chromosomen twee zusterchromatiden.",
    ),
    keuze(
        "Een suiker met een base, maar zonder fosfaatgroep, heet een [[*nucleoside|nucleotide|nucleosoom]].",
        "Met een fosfaatgroep erbij wordt het een nucleotide.",
    ),
    tabel(
        "Klopt dit over de replicatie bij de mens?",
        [
            ("Er zijn honderden startpunten per chromosoom.", J),
            ("Polymerase kijkt zijn eigen werk na.", J),
            ("Ze gebeurt tijdens de S-fase.", J),
            ("Ze gebeurt net zoals bij bacteriën in het cytoplasma.", F),
        ],
        "Bij de mens gebeurt de replicatie in de kern.",
    ),
    sleep(
        "De twee strengen van DNA zijn [[antiparallel]]: de ene loopt van 5' naar 3', de andere van [[3' naar 5']]. Polymerase bouwt altijd van [[5' naar 3']].",
        ["parallel", "links naar rechts", "boven naar onder"],
        "Daardoor moet de lagging strand in stukjes gebouwd worden.",
    ),
    mk(
        "Waarom is het belangrijk dat een cel haar DNA vóór de deling volledig kopieert?",
        [
            "Elke dochtercel heeft de volledige set nodig",
            "Anders kan de cel geen ATP meer maken",
            "Anders worden de chromosomen haploïd en vruchtbaar",
            "Anders verdwijnen de histonen uit de kern",
        ],
        0,
        "Zonder kopie zou elke dochtercel maar een deel van de informatie krijgen.",
    ),
    keuze(
        "Een geordende foto van alle chromosomen van één cel, per paar gerangschikt, heet een [[*karyogram|nucleosoom|centromeer]].",
        "Zo kan men het aantal chromosomen tellen en grote afwijkingen zien.",
    ),
    tabel(
        "Autosoom of heterosoom?",
        [
            ("chromosoom 1", "Autosoom"),
            ("het X-chromosoom", "Heterosoom"),
            ("chromosoom 21", "Autosoom"),
            ("het Y-chromosoom", "Heterosoom"),
        ],
        "De mens heeft 22 paar autosomen en één paar heterosomen.",
        kolommen=["Autosoom", "Heterosoom"],
    ),
    mk(
        "Waarom kunnen de enzymen het euchromatine wel lezen en het heterochromatine bijna niet?",
        [
            "Euchromatine ligt los, zodat de enzymen erbij kunnen",
            "Heterochromatine bevat helemaal geen genen meer",
            "Euchromatine ligt buiten de kern in het cytoplasma",
            "Heterochromatine is gemaakt van RNA in plaats van DNA",
        ],
        0,
        "Hoe strakker het DNA rond de histonen gewonden is, hoe moeilijker het te lezen is.",
    ),
    open_(
        "Leg uit waarom de replicatie zo weinig fouten maakt.",
        "De basen passen maar op één manier bij elkaar: A met T en C met G. Daardoor ligt de nieuwe streng vast door de oude. Bovendien kijkt DNA-polymerase zijn eigen werk na en vervangt het een verkeerde base meteen.",
    ),
]
