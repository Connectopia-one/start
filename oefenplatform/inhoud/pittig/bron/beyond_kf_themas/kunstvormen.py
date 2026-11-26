"""Kunst, cultuur en de kunstvormen — pittig (🌍 Beyond doorstroom,
kunstbeschouwing en filosofie). Strikt binnen beyond/bron/kfb_kunstvormen.py:
cultuur eng en breed, de kunstvormen, de middelen van vormgeving en de
bouwstenen per kunstvorm uit bijlage 1 (beeld, dans, drama, media, muziek)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL

# Prent 1: drie camerakaders --------------------------------------------------
SH = Prent("drie-kaders", "Drie kaders uit dezelfde film",
           "drie beelden naast elkaar: A een kleine figuur in een wijd landschap, B een figuur tot aan het middel, C enkel een gezicht dat het hele beeld vult")
KADERS = {}


def kader(letter, x):
    SH.rect(x, 110, 290, 400, "#eef3f8", DONKER, 8, 3)
    SH.letter(x + 145, 555, letter)
    KADERS[letter] = (x, 110, 290, 400)


kader("A", 30)
kader("B", 355)
kader("C", 680)
# A: long shot, kleine figuur, horizon, bergen
SH.pad("M 30 380 L 110 300 L 170 350 L 240 270 L 320 380 Z", "#c9d6c0", DONKER, 2)
SH.rect(30, 380, 290, 130, "#a8c98a", DONKER, 0, 0)
SH.cirkel(175, 395, 7, DONKER, DONKER, 1)
SH.lijn(175, 402, 175, 425, DONKER, 3)
# B: medium shot, figuur tot aan het middel
SH.cirkel(500, 230, 55, "#f1d9b5", DONKER, 3)
SH.pad("M 410 510 L 420 360 Q 500 300 580 360 L 590 510 Z", BLAUW, DONKER, 3)
# C: close-up, gezicht vult het beeld
SH.cirkel(825, 310, 138, "#f1d9b5", DONKER, 3)
SH.cirkel(775, 280, 14, DONKER, DONKER, 1)
SH.cirkel(875, 280, 14, DONKER, DONKER, 1)
SH.pad("M 775 370 Q 825 400 875 370", "none", DONKER, 4)

# Prent 2: vier composities ---------------------------------------------------
CO = Prent("vier-composities", "Vier schilderijen in schema",
           "vier vlakken: A drie figuren in een driehoek, B figuren in een kring, C een sterke diagonaal van linksonder naar rechtsboven, D figuren op één horizontale rij")
VLAK = {}


def vlak(letter, x, y):
    CO.rect(x, y, 440, 250, "#fbfaf5", DONKER, 8, 3)
    CO.letter(x + 30, y + 30, letter)
    VLAK[letter] = (x, y, 440, 250)


vlak("A", 40, 60)
vlak("B", 520, 60)
vlak("C", 40, 340)
vlak("D", 520, 340)
for (cx, cy) in ((260, 110), (180, 270), (340, 270)):
    CO.cirkel(cx, cy, 28, ORANJE, DONKER, 2)
import math
for i in range(6):
    a = i * math.pi / 3
    CO.cirkel(740 + 85 * math.cos(a), 190 + 75 * math.sin(a), 22, BLAUW, DONKER, 2)
for i in range(5):
    CO.cirkel(110 + i * 75, 555 - i * 42, 24, GEEL, DONKER, 2)
for i in range(5):
    CO.cirkel(590 + i * 75, 470, 24, LICHTGROEN, DONKER, 2)


def zone_kader(l):
    return [Prent.zone(*KADERS[l])]


def zone_vlak(l):
    return [Prent.zone(*VLAK[l])]


VRAGEN = [
    klik("Klik op het beeld dat een close-up is.", SH.bestand, zone_kader("C"),
         "Bij een close-up vult een gezicht of een detail bijna het hele beeld."),
    klik("Klik op het long shot.", SH.bestand, zone_kader("A"),
         "Een long shot toont de figuur klein in een wijde omgeving. Het kader is een bouwsteen van media."),
    met_prent(SH.bestand, keuze("Beeld B is een [[*medium shot|close-up|long shot]]. Wie de emotie op een gezicht wil tonen, kiest het best voor een [[*close-up|long shot|medium shot]].",
              "Een medium shot toont de figuur ongeveer tot aan het middel. Een close-up brengt je dicht bij de emotie.")),
    klik("Klik op het schilderij met een driehoekscompositie.", CO.bestand, zone_vlak("A"),
         "Bij compositie kijk je onder meer naar denkbeeldige geometrische figuren, zoals een driehoek."),
    klik("Klik op het schilderij waarin een diagonaal de compositie bepaalt.", CO.bestand, zone_vlak("C"),
         "De figuren liggen op een lijn van linksonder naar rechtsboven."),
    met_prent(CO.bestand, keuze("In schilderij B staan de figuren in een [[*cirkel|driehoek|rechthoek]]. In schilderij D liggen ze op één [[*horizontale|diagonale|verticale]] lijn.",
              "Spreiding en rangschikking van de elementen horen bij de bouwsteen compositie.")),
    tabel("Is dit cultuur in de enge of in de brede betekenis?", [
        ("een opera in een concertzaal", "eng"),
        ("de gewoonte om elkaar drie kussen te geven", "breed"),
        ("een roman die een literatuurprijs wint", "eng"),
        ("wat een familie op zondag samen eet", "breed"),
    ], "De enge betekenis gaat vooral over kunst. De brede betekenis is alles wat een groep aanleert en doorgeeft.",
       kolommen=["eng", "breed"]),
    sorteer("Bij welke kunstvorm hoort dit werk?", ["beeldende kunsten", "audiovisuele kunsten", "podiumkunsten"], [
        ["een marmeren beeld", "beeldende kunsten"],
        ["een documentaire", "audiovisuele kunsten"],
        ["een balletvoorstelling", "podiumkunsten"],
        ["een olieverfschilderij", "beeldende kunsten"],
        ["een reeks zwart-witfoto's", "audiovisuele kunsten"],
        ["een concert van een orkest", "podiumkunsten"],
    ], "Beeldend: schilder- en beeldhouwkunst. Audiovisueel: film, fotografie, videokunst. Podium: dans, theater, muziek."),
    mk("Een kunstenaar vult een lege fabriekshal met duizenden lichtjes en geluid. De bezoeker loopt erdoor. Welke kunstvorm is dit?",
       ["installatiekunst", "architectuur en design", "beeldhouwkunst", "videokunst"], 0,
       "De hele ruimte is het werk en de bezoeker staat er middenin."),
    mk("Een kunstenaar hangt enkel een bordje met de tekst 'Stel je hier een blauw vierkant voor' aan de muur. Welke kunstvorm past het best?",
       ["conceptuele kunst", "schilderkunst op doek", "installatiekunst", "literatuur en poëzie"], 0,
       "Het idee is het eigenlijke werk. Het voorwerp is bijzaak."),
    koppel("Koppel de bouwsteen van beeld aan wat je onderzoekt.", [
        ["textuur", "een ruw of glad oppervlak, met penseel of paletmes"],
        ["licht", "veel of weinig contrast tussen licht en donker"],
        ["ruimte", "perspectief en afgesneden figuren aan de rand"],
        ["lijn", "dikke of dunne, rechte of golvende omlijning"],
    ], ["het tempo waarin de toeschouwer kijkt"], "Elke bouwsteen van beeld heeft eigen aandachtspunten. Tempo hoort niet bij beeld."),
    koppel("Koppel de bouwsteen van muziek aan het voorbeeld.", [
        ["dynamiek", "het stuk gaat van zacht naar heel luid"],
        ["tempo", "de muziek versnelt naar het einde toe"],
        ["klankkleur", "een trompet speelt de hoofdmelodie"],
        ["structuur", "intro, strofe, refrein, brug en slot"],
    ], ["de camera zoomt in"], "Inzoomen is een bouwsteen van media, niet van muziek."),
    sorteer("Bij welke kunstvorm hoort deze bouwsteen?", ["dans", "drama", "media"], [
        ["kracht: vloeiende of hoekige bewegingen", "dans"],
        ["rol: het karakter van de personages", "drama"],
        ["montage: cuts of naadloze overgangen", "media"],
        ["relatie: synchroon dansen of niet", "dans"],
        ["samenspel: veel of weinig contact tussen personages", "drama"],
        ["camera: een pan- of tiltbeweging", "media"],
    ], "Dans: ruimte, tijd, kracht, vorm, relatie. Drama: rol, ruimte, tijd, structuur, samenspel. Media: kader, licht, geluid, camera, montage."),
    tabel("Klopt dit?", [
        ("Bouwstenen, materiaal en techniek zijn de drie middelen van vormgeving.", J),
        ("Ruimte en tijd zijn bouwstenen bij zowel dans als drama.", J),
        ("Compositie is een bouwsteen van muziek.", F),
        ("Fotografie hoort in deze indeling bij de beeldende kunsten.", F),
    ], "Compositie hoort bij beeld. Fotografie staat bij de audiovisuele kunsten."),
    casus(
        "In een korte film zie je eerst een wijd beeld van een donkere stad. De camera zoomt langzaam in op één verlicht raam. "
        "Er klinkt trage pianomuziek. Dan volgt een harde overgang naar een felle close-up van een gezicht, met een plotse luide knal.",
        [
            keuze("Het langzame inzoomen hoort bij de bouwsteen [[*camera|montage|geluid]]. De harde overgang naar de close-up is een [[*cut|dissolve|fade out]].",
                  "Zoomen en camerabewegingen horen bij camera. Een plotse overgang is een cut, een naadloze is een dissolve."),
            mk("Wat doet de trage pianomuziek vooral?",
               ["ze versterkt de sfeer van het verhaal", "ze vertelt de dialogen van de personages",
                "ze bepaalt welk type shot de camera kiest", "ze zorgt dat het beeld helderder wordt"], 0,
               "Bij geluid kijk je ook naar het versterkend effect van de muziek op het verhaal."),
            tabel("Over welke bouwsteen van media gaat dit?", [
                ("een donkere stad met één verlicht raam", "licht"),
                ("de plotse luide knal in het klankspoor", "geluid"),
                ("van een wijd beeld naar een close-up", "kader"),
            ], "Licht, geluid en kader zijn drie van de vijf bouwstenen van media.",
               kolommen=["licht", "geluid", "kader"]),
        ],
    ),
    sleep("Bij beeld kijk je naar [[kleur]]: primair of secundair, fel of zacht. Bij [[vorm]] kijk je of het werk twee- of driedimensionaal is, met hoekige of ronde vormen.",
          ["klankkleur", "montage"], "Kleur en vorm zijn twee bouwstenen van beeld."),
    mk("Een danser maakt grote, krachtige sprongen en daarna kleine, trage bewegingen. Welke twee bouwstenen van dans beschrijf je vooral?",
       ["kracht en vorm", "rol en samenspel", "kader en montage", "melodie en ritme"], 0,
       "Kracht gaat over de energie, vorm over grote of kleine bewegingen."),
    keuze("Bij drama gaat de bouwsteen [[*structuur|rol|samenspel]] over het begin, het verloop en het einde van het verhaal. Het gebruik van het podium en de attributen hoort bij [[*ruimte|tijd|rol]].",
          "Structuur, ruimte, tijd, rol en samenspel zijn de bouwstenen van drama."),
    tabel("Is dit materiaal of techniek?", [
        ("brons", "materiaal"),
        ("gieten in een mal", "techniek"),
        ("olieverf", "materiaal"),
        ("in dunne lagen over elkaar schilderen", "techniek"),
    ], "Materiaal is waarmee, techniek is hoe iets gemaakt wordt.",
       kolommen=["materiaal", "techniek"]),
    mk("Waarom horen architectuur en design samen in één kunstvorm?",
       ["bij beide moet de vorm ook dienen voor een gebruik", "bij beide gebruikt men altijd beton en glas",
        "bij beide gaat het enkel om de prijs van het werk", "bij beide ontstaat het werk live voor een publiek"], 0,
       "Een gebouw en een stoel moeten mooi zijn, maar ook werken."),
    inv("Hoe heet de bouwsteen van muziek die gaat over het instrument of de stem van de hoofdmelodie?", ["klankkleur"],
        "Een melodie op een viool klinkt anders dan dezelfde melodie op een tuba."),
    inv("Hoe heet de bouwsteen van media die gaat over cuts, fades en slow motion?", ["montage"],
        "Bij montage kijk je hoe de shots aan elkaar gezet zijn en aan welke snelheid."),
    volgorde("Zet de kaders van wijd naar dichtbij.", [
        "long shot", "medium shot", "close-up",
    ], "Een long shot toont veel omgeving, een close-up een detail."),
    mk("Een filmmaker filmt een reus van onderaf, zodat hij nog groter en dreigender lijkt. Welk perspectief kiest hij?",
       ["kikkerperspectief", "vogelperspectief", "ooghoogteperspectief", "centraal perspectief"], 0,
       "Van onderaf filmen heet kikkerperspectief. Van bovenaf is vogelperspectief."),
    tabel("Klopt dit over de middelen van vormgeving bij beeld?", [
        ("Een paletmes of een spons zegt iets over de textuur.", J),
        ("Afgesneden figuren aan de rand horen bij de bouwsteen ruimte.", J),
        ("Of de kleuren realistisch zijn, hoort bij de bouwsteen licht.", F),
        ("Of er weinig of veel schaduw is, hoort bij de bouwsteen kleur.", F),
    ], "Realistische kleuren horen bij kleur, schaduwen bij licht."),
    keuze("Twee dansers bewegen precies tegelijk en spiegelen elkaar. Dat hoort bij de bouwsteen [[*relatie|kracht|tijd]]. Snelle overgangen en pauzemomenten horen bij [[*tijd|vorm|ruimte]].",
          "Relatie gaat over synchroon dansen en inspelen op elkaar. Tijd gaat over tempo, cadans en pauzes."),
    mk("Een toneelstuk springt voortdurend heen en weer tussen verleden en heden, zodat het publiek goed moet opletten. Welke bouwsteen van drama speelt hier vooral?",
       ["structuur", "samenspel", "rol", "klankkleur"], 0,
       "Een moeilijke verhaallijn en het verloop van het verhaal horen bij structuur."),
    open_("Leg uit waarom kunst deel uitmaakt van een cultuur in de brede betekenis.",
          "Cultuur in de brede betekenis is alles wat een groep mensen aanleert en doorgeeft: taal, waarden, gewoonten en ook kunst. Kunst groeit uit die cultuur en toont wat een groep belangrijk vindt. Een volksdans, een kerk of een lied zegt iets over de gewoonten en het geloof van die groep. Kunst kan die cultuur ook mee vormen of in vraag stellen."),
]
