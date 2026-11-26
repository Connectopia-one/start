"""Humane wetenschappen: politiek, democratie en de rechtstaat — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen, enkel humane
wetenschappen). Eigen vragen in examenvorm en een eigen schema van de drie
machten. Strikt binnen beyond/bron/sg_hw_democratie.py."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

# De drie machten in België ----------------------------------------------------------------
DM = Prent("drie-machten", "Drie instellingen in een democratische rechtstaat",
           "drie vakken naast elkaar: links het parlement met een halfrond, in het midden de regering met een tafel, rechts de hoven en rechtbanken met een hamer; pijlen tussen de vakken")
VAK = {"A": 80, "B": 380, "C": 680}
NAMEN = {"A": (["Parlement"], "Kamer, Vlaams Parlement, ..."),
         "B": (["Regering"], "eerste minister, ministers"),
         "C": (["Hoven en", "rechtbanken"], "rechters")}
for k, x in VAK.items():
    DM.rect(x, 150, 240, 260, "#ffffff", DONKER, 18, 2)
    for i, regel in enumerate(NAMEN[k][0]):
        DM.tekst(x + 135, 195 + 28 * i, regel, 23, vet=True)
    DM.tekst(x + 120, 395, NAMEN[k][1], 16)
    DM.letter(x + 30, 180, k)
# halfrond
DM.pad("M130 340 A70 70 0 0 1 270 340 Z", LICHTGROEN, DONKER, 2)
# tafel
DM.rect(440, 290, 120, 18, GRIJS, DONKER, 4, 2)
DM.lijn(455, 308, 455, 350, DONKER, 4)
DM.lijn(545, 308, 545, 350, DONKER, 4)
for cx in (460, 500, 540):
    DM.cirkel(cx, 270, 12, "#ffffff", DONKER, 2)
# hamer
DM.rect(745, 270, 90, 34, GRIJS, DONKER, 6, 2)
DM.lijn(790, 304, 790, 360, DONKER, 8)
DM.rect(750, 360, 80, 12, GRIJS, DONKER, 3, 2)
# pijlen: controle
for x in (330, 630):
    DM.pijl(x, 265, x + 40, 265)
    DM.pijl(x + 40, 295, x, 295)
DM.pad("M200 410 Q500 560 800 410", "none", DONKER, 2)
DM.pijl(790, 418, 800, 410)
DM.pijl(210, 418, 200, 410)
DM.tekst(500, 520, "de machten controleren elkaar", 18)


def vak(k):
    return [Prent.zone(VAK[k], 150, 240, 260)]


VRAGEN = [
    klik("Klik op de instelling die de wetgevende macht uitoefent.", DM.bestand, vak("A"),
         "Parlementen maken en keuren de wetten goed. Dat is de wetgevende macht."),
    klik("Een minister zorgt ervoor dat een nieuwe wet in de praktijk wordt toegepast. Klik op de macht waartoe hij behoort.", DM.bestand, vak("B"),
         "Ministers vormen samen de regering, de uitvoerende macht."),
    klik("Klik op de macht die volgens de principes van de rechtstaat onafhankelijk en onpartijdig moet zijn bij het beoordelen van een geschil.", DM.bestand, vak("C"),
         "Hoven en rechtbanken vormen de rechterlijke macht. Ze mogen geen bevelen krijgen van de regering of het parlement."),
    met_prent(DM.bestand, keuze("De pijlen tussen de vakken tonen dat de machten elkaar [[*controleren en in evenwicht houden|vervangen als één macht uitvalt|elk jaar van plaats wisselen]].",
              "Machten die elkaar controleren, voorkomen dat één macht alles alleen kan.")),
    met_prent(DM.bestand, mk("Een president laat in vak C enkel rechters toe die lid zijn van zijn eigen partij. Wat is daar mis mee?",
              ["de rechters zijn dan niet meer onafhankelijk",
               "de rechters mogen dan geen wetten meer stemmen",
               "het parlement krijgt dan te weinig leden",
               "de regering moet dan ook rechters benoemen"], 0,
              "Rechters die van de regeringspartij afhangen, kunnen niet vrij oordelen over zaken tegen die regering.")),
    tabel("Welke staats- of regeringsvorm herken je?", [
        ("De wetten komen uit een heilig boek en worden uitgelegd door religieuze leiders.", "theocratie"),
        ("Een generaal neemt de macht over, verbiedt alle partijen en schaft de verkiezingen af.", "dictatuur"),
        ("Drie families delen de macht en duiden zelf de ministers aan.", "oligarchie"),
        ("Het staatshoofd is een president die om de vijf jaar verkozen wordt.", "republiek"),
    ], "In naam van een god, één persoon met alle macht, een kleine groep, of een verkozen staatshoofd.",
       kolommen=["theocratie", "dictatuur", "oligarchie", "republiek"]),
    keuze("Een land met een koning als staatshoofd is een [[*monarchie|republiek|oligarchie]]. Als het volk er ook vrij het parlement kiest, is het daarnaast een [[*democratie|dictatuur|theocratie]].",
          "Monarchie zegt iets over het staatshoofd, democratie over waar de macht ligt. België is beide."),
    sorteer("Directe of indirecte democratie?", ["Directe democratie", "Indirecte democratie"], [
        ["De inwoners stemmen zelf over de nieuwe begroting van hun kanton.", "Directe democratie"],
        ["De burgers kiezen 150 volksvertegenwoordigers voor de Kamer.", "Indirecte democratie"],
        ["Bij een volksraadpleging beslissen de kiezers zelf over een nieuwe brug.", "Directe democratie"],
        ["De gemeenteraad beslist in naam van de inwoners over een nieuw zwembad.", "Indirecte democratie"],
    ], "Zelf beslissen, of iemand kiezen die in jouw naam beslist."),
    koppel("Koppel elk principe van de democratische rechtstaat aan een voorbeeld.", [
        ["grondwet", "alle wetten moeten passen binnen de hoogste wet van het land"],
        ["fundamentele rechten en vrijheden", "iedereen mag zijn mening zeggen en een vereniging oprichten"],
        ["meerderheidsprincipe", "een voorstel met 80 van de 150 stemmen wordt aangenomen"],
        ["scheiding der machten", "wie wetten maakt, voert ze niet zelf uit"],
    ], ["de grootste partij mag de grondrechten afschaffen"], "Het extra voorbeeld is net in strijd met de rechtstaat."),
    tabel("Klopt dit voor een democratische rechtstaat?", [
        ("De meerderheid mag beslissen, maar niet de grondrechten van de minderheid afnemen.", J),
        ("Een minister kan een rechter ontslaan als die tegen de regering beslist.", F),
        ("Ook de regering moet zich aan de wetten houden.", J),
        ("Verkiezingen zijn genoeg om een land een rechtstaat te noemen.", F),
    ], "Meerderheid binnen grenzen, onafhankelijke rechters, niemand boven de wet, en meer dan enkel verkiezingen."),
    casus(
        "In het land Nordavia wint de partij van president Varga de verkiezingen met 55 procent. "
        "Daarna laat hij een wet goedkeuren waardoor kranten die kritiek geven, gesloten kunnen worden. "
        "Het hoogste hof vernietigt die wet. Varga verlaagt daarop de pensioenleeftijd van de rechters, zodat de helft moet vertrekken, "
        "en hij benoemt zelf hun opvolgers.",
        [
            keuze("Varga won de verkiezingen met een meerderheid. Dat volgt het [[*meerderheidsprincipe|principe van openbaarheid|principe van hoor en wederhoor]].",
                  "55 procent is een meerderheid. Dat alleen maakt het land nog geen volwaardige rechtstaat."),
            mk("Welk recht schendt de wet tegen kritische kranten vooral?",
               ["de persvrijheid en vrije meningsuiting",
                "het recht om te stemmen bij verkiezingen",
                "het recht op een eerlijk loon",
                "het recht om een eigen bedrijf te starten"], 0,
               "Kranten mogen kritiek geven. Persvrijheid hoort bij de fundamentele rechten en vrijheden."),
            mk("Welk principe schendt Varga met zijn ingreep bij de rechters?",
               ["de scheiding der machten",
                "de directe democratie",
                "het meerderheidsprincipe",
                "de monarchie"], 0,
               "De uitvoerende macht grijpt in bij de rechterlijke macht om haar eigen wet te redden."),
            keuze("Nordavia is na deze ingrepen [[*minder|meer]] een democratische rechtstaat dan ervoor.",
                  "Verkiezingen blijven, maar grondrechten en onafhankelijke rechtspraak worden uitgehold."),
        ],
    ),
    sleep("In een [[directe]] democratie beslissen de burgers zelf. In een [[representatieve]] democratie kiezen ze vertegenwoordigers.",
          ["theocratische", "oligarchische"], "Directe of rechtstreekse, en indirecte of representatieve democratie."),
    mk("Welke combinatie is mogelijk?",
       ["een republiek die geen democratie is",
        "een monarchie met een verkozen president als staatshoofd",
        "een directe democratie zonder dat burgers mogen stemmen",
        "een oligarchie waarin alle burgers evenveel macht hebben"], 0,
       "Een dictatuur kan zich republiek noemen. De andere combinaties spreken zichzelf tegen."),
    inv("Hoe heet een staatsvorm waarin geestelijken regeren in naam van een god?", ["theocratie", "een theocratie"],
        "Theos betekent god."),
    tabel("Welke macht is aan het werk?", [
        ("Het parlement keurt een wet goed die gsm-gebruik in de klas regelt.", "wetgevend"),
        ("Een rechter veroordeelt een man voor fraude.", "rechterlijk"),
        ("De minister van Onderwijs stuurt een omzendbrief naar alle scholen om de wet toe te passen.", "uitvoerend"),
        ("Het parlement stemt over een nieuwe regel voor de jacht.", "wetgevend"),
    ], "Regels maken, regels toepassen of regels gebruiken om te oordelen.",
       kolommen=["wetgevend", "uitvoerend", "rechterlijk"]),
    keuze("Een parlement dat de regering kan wegstemmen, is een voorbeeld van [[*controle tussen de machten|directe democratie|een theocratie]].",
          "De wetgevende macht controleert de uitvoerende macht."),
    volgorde("Zet van de meeste tot de minste mensen met macht.", [
        "democratie: het volk",
        "oligarchie: een kleine groep",
        "dictatuur: één persoon of partij",
    ], "Het volk, een paar mensen of één persoon."),
    mk("Waarom is een onpartijdige rechter ook belangrijk voor wie een rechtszaak verliest?",
       ["hij kan het oordeel als eerlijk aanvaarden",
        "hij krijgt dan altijd een lagere straf",
        "hij hoeft dan geen advocaat te betalen",
        "hij mag de zaak dan zelf herschrijven"], 0,
       "Wie weet dat de rechter geen kant koos, kan ook een verlies als rechtvaardig zien. Dat geeft vertrouwen in justitie."),
    tabel("Is dit een schending van de scheiding der machten?", [
        ("De regering schrijft een vonnis voor in een zaak tegen een minister.", J),
        ("Het parlement stelt vragen aan de eerste minister.", F),
        ("Een rechter legt een straf op volgens de wet.", F),
        ("De president ontbindt het hoogste hof omdat het hem tegenspreekt.", J),
    ], "Een macht die het werk of de vrijheid van een andere macht afneemt, schendt de scheiding der machten."),
    inv("Hoe noem je het principe dat een voorstel met de meeste stemmen wordt aangenomen? Het ...principe.", ["meerderheids", "meerderheidsprincipe", "meerderheid"],
        "Het meerderheidsprincipe geldt in een rechtstaat binnen de grenzen van de grondwet."),
    keuze("De rechtstaat sluit aan bij westerse waarden zoals [[*vrijheid en gelijkheid voor de wet|gehoorzaamheid aan één leider|het erven van macht]].",
          "Grondrechten en gelijkheid voor de wet zijn kernwaarden van de westerse democratieën."),
    mk("In Alvoria kan de koning de wetten van het parlement zonder uitleg tegenhouden en zelf rechters ontslaan. Wat is Alvoria zeker niet?",
       ["een democratische rechtstaat",
        "een monarchie",
        "een land met een staatshoofd",
        "een land met een parlement"], 0,
       "Er is een koning en een parlement, maar de macht is niet gescheiden en de rechters zijn niet onafhankelijk."),
    sorteer("Hoort dit bij de principes van een democratische rechtstaat?", ["Principe", "Geen principe"], [
        ["scheiding der machten", "Principe"],
        ["onafhankelijke en onpartijdige rechtspraak", "Principe"],
        ["één partij die alle ministers levert", "Geen principe"],
        ["een grondwet", "Principe"],
        ["een staatshoofd dat zijn ambt erft", "Geen principe"],
    ], "Een erfelijk staatshoofd kan in een rechtstaat, maar is er geen principe van. Eén partij met alle macht past er niet in."),
    keuze("Een bestuursvorm waarin enkele rijke families de macht hebben, is een [[*oligarchie|theocratie|directe democratie]].",
          "Oligos betekent weinig: de heerschappij van enkelen."),
    tabel("Welke soort democratie wordt hier beschreven?", [
        ("Iedere burger kan op een volksvergadering zelf meestemmen over elke wet.", "direct"),
        ("De burgers kiezen een parlement dat vijf jaar lang de wetten maakt.", "indirect"),
        ("Een gemeente laat haar inwoners zelf stemmen over een nieuw plein.", "direct"),
    ], "Zelf beslissen of via vertegenwoordigers.", kolommen=["direct", "indirect"]),
    inv("Hoe heet de hoogste wet van een land, met de grondrechten en de werking van de staat?", ["grondwet", "de grondwet", "constitutie", "de constitutie"],
        "De grondwet of constitutie staat boven alle andere wetten."),
    open_("Leg uit waarom verkiezingen alleen niet genoeg zijn om een land een democratische rechtstaat te noemen.",
          "Ook een regering die verkozen is, kan haar macht misbruiken. Een rechtstaat heeft daarom ook een grondwet, grondrechten die ook minderheden beschermen, een scheiding der machten en onafhankelijke en onpartijdige rechters. Zonder die principes kan een verkozen meerderheid kritiek verbieden of rechters aan de kant zetten."),
]
