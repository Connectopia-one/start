"""Mutaties, mutagenen en kanker — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

KL = {"A": "#f3c6d0", "B": "#f5d9a8", "C": "#f2c14e", "D": "#9fd39a", "E": "#cfe5f3", "F": "#c8a8e0", "G": "#e8a0b0",
      "x": "#d9d9d9", "y": "#bcbcbc"}

# Chromosoommutaties -------------------------------------------------------
CM = Prent("chromosoommutaties", "Een normaal chromosoom en vier veranderde versies", "bovenaan het normale chromosoom met stukken A tot G, daaronder vier versies P, Q, R en S")


def _chromosoom(p, x, y, stukken, b=48):
    for i, s in enumerate(stukken):
        p.rect(x + i * b, y, b, 44, KL[s], DONKER, 6, 1.5)
        p.tekst(x + i * b + b / 2, y + 29, s, 17, vet=True)


CM.tekst(70, 117, "normaal", 17, "start", vet=True)
_chromosoom(CM, 250, 90, "ABCDEFG")
RIJEN = [("P", "ABDEFG"), ("Q", "ABCCDEFG"), ("R", "ADCBEFG"), ("S", "ABCDxyy")]
for i, (k, st) in enumerate(RIJEN):
    y = 190 + i * 95
    CM.letter(110, y + 22, k)
    _chromosoom(CM, 250, y, st)
CM.tekst(500, 580, "x en y: stukken van een ander, niet-homoloog chromosoom", 15)
ZCM = {k: [Prent.zone(80, 175 + i * 95, 600, 75)] for i, (k, st) in enumerate(RIJEN)}

# Karyogram (uitsnede) -----------------------------------------------------
KG = Prent("karyogram-uitsnede", "Uitsnede uit het karyogram van een kind", "chromosomenparen 19, 20, 21, 22 en de geslachtschromosomen")


def _kchrom(x, y, h, kl="#d8cce8"):
    KG.rect(x - 9, y, 18, h, kl, DONKER, 9, 1.5)
    KG.lijn(x - 9, y + h * 0.35, x + 9, y + h * 0.35, DONKER, 1.5)
    for k in range(1, 4):
        KG.lijn(x - 9, y + h * k / 4 + 6, x + 9, y + h * k / 4 + 6, "#9a8ab0", 1)


GROEPEN = [("19", 2, 120), ("20", 2, 115), ("21", 3, 80), ("22", 2, 85), ("X  Y", 0, 0)]
for i, (n, aantal, h) in enumerate(GROEPEN):
    cx = 140 + i * 180
    if aantal:
        for j in range(aantal):
            _kchrom(cx - (aantal - 1) * 15 + j * 30, 380 - h, h)
    else:
        _kchrom(cx - 15, 240, 140)
        _kchrom(cx + 15, 320, 60)
    KG.lijn(cx - 55, 395, cx + 55, 395, DONKER, 1.5)
    KG.tekst(cx, 425, n, 18, vet=True)
ZKG = {n: [Prent.zone(140 + i * 180 - 70, 220, 140, 220)] for i, (n, a, h) in enumerate(GROEPEN)}

VRAGEN = [
    klik(
        "Klik op het chromosoom met een inversie.",
        CM.bestand, ZCM["R"],
        "Het stuk BCD is losgebroken en omgekeerd teruggeplaatst: DCB.",
    ),
    klik(
        "Klik op het chromosoom met een translocatie.",
        CM.bestand, ZCM["S"],
        "Een stuk van een niet-homoloog chromosoom is erop terechtgekomen.",
    ),
    met_prent(CM.bestand, tabel(
        "Welke chromosoommutatie zie je?",
        [
            ("P", "Deletie"),
            ("Q", "Duplicatie"),
            ("R", "Inversie"),
            ("S", "Translocatie"),
        ],
        "Bij P is C verdwenen, bij Q staat C er twee keer.",
        kolommen=["Deletie", "Duplicatie", "Inversie", "Translocatie"],
    )),
    klik(
        "Klik op het chromosomenpaar met de fout.",
        KG.bestand, ZKG["21"],
        "Drie keer chromosoom 21: trisomie 21, het syndroom van Down.",
    ),
    met_prent(KG.bestand, tabel(
        "Kijk naar het karyogram. Klopt dit?",
        [
            ("Het kind is een jongen.", J),
            ("Het kind heeft 47 chromosomen.", J),
            ("Dit is een genoommutatie.", J),
            ("Deze fout ontstaat door UV-straling op de huid.", F),
        ],
        "Een extra chromosoom komt meestal door non-disjunctie bij de meiose.",
    )),
    tabel(
        "Genmutatie, chromosoommutatie of genoommutatie?",
        [
            ("één base wordt vervangen", "Gen"),
            ("een stuk chromosoom draait om", "Chromosoom"),
            ("een chromosoom te veel", "Genoom"),
            ("sikkelcelanemie", "Gen"),
            ("het syndroom van Turner", "Genoom"),
        ],
        "Turner: één X-chromosoom te weinig.",
        kolommen=["Gen", "Chromosoom", "Genoom"],
    ),
    tabel(
        "Een gen leest AUG GCU UGG UAA. Wat doet deze puntmutatie met het eiwit?",
        [
            ("GCU wordt GCC", "Niets"),
            ("UGG wordt UGA", "Te kort"),
            ("de U van GCU valt weg", "Leesraam verschoven"),
            ("GCU wordt GCA", "Niets"),
        ],
        "GCU, GCC en GCA geven allemaal alanine. UGA is een stopcodon.",
        kolommen=["Niets", "Te kort", "Leesraam verschoven"],
    ),
    mk(
        "Waarom is een deletie van drie nucleotiden vaak minder erg dan een deletie van één?",
        [
            "Het leesraam blijft, één aminozuur valt weg",
            "Drie nucleotiden zijn altijd samen een stopcodon",
            "Het ribosoom vult de drie gaten zelf weer op",
            "Een deletie van drie wordt nooit doorgegeven",
        ],
        0,
        "Drie nucleotiden zijn precies één codon.",
    ),
    tabel(
        "Erfelijk of niet erfelijk?",
        [
            ("een mutatie in een eicel", "Erfelijk"),
            ("een mutatie in een huidcel door zonlicht", "Niet erfelijk"),
            ("een mutatie in een zaadcel", "Erfelijk"),
            ("een mutatie in een longcel door roken", "Niet erfelijk"),
        ],
        "Alleen mutaties in geslachtscellen gaan naar de kinderen.",
        kolommen=["Erfelijk", "Niet erfelijk"],
    ),
    koppel(
        "Koppel elk mutageen aan hoe het schade doet.",
        [
            ("UV-straling", "doet twee thyminen aan elkaar plakken"),
            ("vrije radicalen", "reageren met de basen en beschadigen ze"),
            ("benzopyreen", "een stof uit tabaksrook die het DNA aantast"),
        ],
        ["zet een gen aan met een acetylgroep", "maakt het leesraam altijd langer"],
        "Acetylgroepen horen bij de epigenetica, niet bij mutaties.",
    ),
    tabel(
        "Klopt dit over mutaties?",
        [
            ("Veel mutaties zijn stil of onschadelijk.", J),
            ("Een mutatie kan soms een voordeel geven.", J),
            ("Herstelenzymen repareren de meeste schade.", J),
            ("Elke mutatie maakt het organisme ziek.", F),
        ],
        "Zonder mutaties zou er geen variatie en geen evolutie zijn.",
    ),
    casus(
        "Bij sikkelcelanemie is in het gen voor hemoglobine één base vervangen. Daardoor staat er één ander aminozuur in het eiwit.",
        [
            keuze(
                "Dit is een [[*substitutie|deletie|insertie]].",
                "Eén base door een andere vervangen.",
            ),
            mk(
                "Waarom heeft één ander aminozuur zo'n groot gevolg?",
                [
                    "De vorm van het eiwit en dus zijn werking verandert",
                    "Het hele leesraam van het gen schuift daardoor mee op",
                    "Het eiwit wordt dan meteen afgebroken in de kern",
                    "Het DNA verlaat daardoor de kern van de cel",
                ],
                0,
                "Het hemoglobine klontert samen en de rode bloedcellen worden sikkelvormig.",
            ),
            tabel(
                "Klopt dit over deze mutatie?",
                [
                    ("Het is een genmutatie.", J),
                    ("Je ziet ze niet op een karyogram.", J),
                    ("Ze kan erfelijk zijn.", J),
                    ("Het leesraam is verschoven.", F),
                ],
                "Bij een substitutie blijft het leesraam gelijk.",
            ),
        ],
    ),
    tabel(
        "Proto-oncogen of tumorsuppressorgen?",
        [
            ("stuurt normaal de celdeling aan", "Proto-oncogen"),
            ("legt de celcyclus stil bij schade", "Tumorsuppressor"),
            ("wordt door een mutatie te actief", "Proto-oncogen"),
            ("laat een beschadigde cel afsterven", "Tumorsuppressor"),
        ],
        "Kanker ontstaat vaak als het gaspedaal vastzit en de rem kapot is.",
        kolommen=["Proto-oncogen", "Tumorsuppressor"],
    ),
    volgorde(
        "Zet de stappen van carcinogenese in een logische volgorde.",
        ["Een eerste mutatie in een gen voor groei", "Een tweede mutatie schakelt een remgen uit", "De cel deelt ongeremd", "Telomerase wordt weer aangezet", "De tumor laat bloedvaten groeien"],
        "Kanker vraagt een opeenstapeling van mutaties, vaak over jaren.",
    ),
    mk(
        "Waarom komt kanker vaker voor bij oudere mensen?",
        [
            "Er moeten zich meerdere mutaties opstapelen",
            "Oudere mensen hebben geen herstelenzymen meer",
            "Bij ouderen verdubbelt het aantal chromosomen",
            "Bij ouderen worden alle telomeren langer",
        ],
        0,
        "Hoe langer je leeft, hoe meer kans dat één cellijn genoeg mutaties verzamelt.",
    ),
    tabel(
        "Klopt dit over telomeren?",
        [
            ("Ze zitten aan de uiteinden van een chromosoom.", J),
            ("Ze worden bij elke deling korter.", J),
            ("Een kankercel bouwt ze weer op met telomerase.", J),
            ("Ze bevatten de genen voor hemoglobine.", F),
        ],
        "Zijn ze te kort, dan stopt een gewone cel met delen.",
    ),
    tabel(
        "Hoe werkt deze behandeling tegen kanker?",
        [
            ("angiogeneseremmer", "Bloedvaten"),
            ("een klein RNA legt een te actief gen stil", "Gen stilleggen"),
            ("een geneesmiddel dat nieuwe vaten naar de tumor tegenhoudt", "Bloedvaten"),
            ("genrepressie van een oncogen", "Gen stilleggen"),
        ],
        "Zonder nieuwe bloedvaten krijgt de tumor te weinig zuurstof en voeding.",
        kolommen=["Bloedvaten", "Gen stilleggen"],
    ),
    sleep(
        "Bij [[non-disjunctie]] gaan twee chromosomen bij de meiose niet uit elkaar. Een gameet krijgt er dan één te veel. Na de bevruchting heeft het kind een [[trisomie]]. Heeft het er één te weinig, dan is het een [[monosomie]].",
        ["crossing-over", "mozaïek", "translocatie"],
        "Tri is drie, mono is één.",
    ),
    inv(
        "Een kind heeft het syndroom van Turner: één X en geen tweede geslachtschromosoom. Hoeveel chromosomen telt een lichaamscel?",
        ["45"],
        "Eén minder dan 46.",
    ),
    keuze(
        "Als niet alle cellen van een persoon dezelfde chromosomenfout hebben, spreekt men van [[*mozaïcisme|translocatie|duplicatie]].",
        "De fout ontstond dan pas bij een mitose na de bevruchting.",
    ),
    mk(
        "Waarom ziet een arts sikkelcelanemie niet op een karyogram, maar het syndroom van Down wel?",
        [
            "Down is een extra chromosoom, sikkelcel één base",
            "Sikkelcelanemie zit alleen in de rode bloedcellen",
            "Een karyogram toont enkel de geslachtschromosomen",
            "Down ontstaat pas na de geboorte van het kind",
        ],
        0,
        "Eén base is veel te klein om onder de microscoop te zien.",
    ),
    tabel(
        "Spontaan of geïnduceerd?",
        [
            ("een fout van DNA-polymerase bij de replicatie", "Spontaan"),
            ("schade door röntgenstraling", "Geïnduceerd"),
            ("schade door tabaksrook", "Geïnduceerd"),
            ("een fout die toevallig bij de celdeling ontstaat", "Spontaan"),
        ],
        "Een geïnduceerde mutatie komt door een invloed van buitenaf.",
        kolommen=["Spontaan", "Geïnduceerd"],
    ),
    keuze(
        "Het Philadelphiachromosoom bij een vorm van leukemie ontstaat door een [[*translocatie|inversie|trisomie]] tussen chromosoom 9 en 22.",
        "Daarbij komt een te actief gen voor groei tot stand.",
    ),
    tabel(
        "Verliesmutatie of winstmutatie?",
        [
            ("het enzym werkt niet meer", "Verlies"),
            ("het eiwit doet iets nieuws", "Winst"),
            ("een gen voor groei staat altijd aan", "Winst"),
            ("een remgen tegen kanker valt uit", "Verlies"),
        ],
        "Bij een verliesmutatie werkt het eiwit minder of niet meer.",
        kolommen=["Verlies", "Winst"],
    ),
    mk(
        "Waarom raden artsen zonnecrème aan, ook al geeft een zonnebrand geen erfelijke mutatie?",
        [
            "UV-mutaties in huidcellen kunnen kanker geven",
            "UV verandert het DNA in de eicellen en zaadcellen",
            "UV maakt een extra chromosoom aan in elke huidcel",
            "UV zet de telomerase in alle cellen van het lichaam uit",
        ],
        0,
        "Een mutatie in een lichaamscel kan de persoon zelf wel ziek maken.",
    ),
    tabel(
        "Klopt dit over een angiogeneseremmer?",
        [
            ("Hij gaat de groei van nieuwe bloedvaten naar de tumor tegen.", J),
            ("De tumor krijgt zo minder zuurstof en voeding.", J),
            ("Hij herstelt de mutaties in de kankercel.", F),
        ],
        "De mutaties blijven, maar de tumor groeit moeilijker.",
    ),
    keuze(
        "Een stof of straling die mutaties veroorzaakt, heet een [[*mutageen|inductor|teratogeen]].",
        "Röntgenstraling, UV-licht en benzopyreen zijn voorbeelden.",
    ),
    open_(
        "Leg uit waarom een insertie van één nucleotide meestal veel erger is dan een substitutie.",
        "Het ribosoom leest het mRNA per drie nucleotiden. Bij een substitutie verandert hoogstens één codon, en soms zelfs geen aminozuur. Bij een insertie van één nucleotide schuift het leesraam op: alle codons erna veranderen. Het eiwit krijgt dan een heel andere volgorde of stopt te vroeg.",
    ),
]
