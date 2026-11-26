"""Van romantiek tot popart: moderne en hedendaagse kunst — pittig
(🌍 Beyond doorstroom, kunstbeschouwing en filosofie). Strikt binnen
beyond/bron/kfb_modern.py: neoclassicisme, romantiek, realisme,
impressionisme, modernisme (expressionisme, kubisme, abstracte kunst),
popart en postmodernisme, en stromingen als reactie op elkaar."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL, ROOD, PAARS
import random

# Prent 1: vier stijlen in schema --------------------------------------------------
VS = Prent("vier-stijlen", "Vier schilderijen in schema",
           "A een stripgezicht met dikke zwarte lijn en rasterstippen; B een gezicht uit hoekige vlakken, neus van opzij en ogen van voren; C rechte zwarte lijnen met vlakken rood, geel en blauw; D een tuin uit losse kleurtoetsen naast elkaar")
VAK = {}


def vak(letter, x, y):
    VS.rect(x, y, 440, 250, "#ffffff", DONKER, 6, 3)
    VS.letter(x + 28, y + 28, letter)
    VAK[letter] = (x, y, 440, 250)


vak("A", 40, 60)
vak("B", 520, 60)
vak("C", 40, 340)
vak("D", 520, 340)
# A: popart-strip
for i in range(9):
    for j in range(5):
        VS.cirkel(140 + i * 30, 90 + j * 45, 6, "#f4b9b2", "#f4b9b2", 0)
VS.ellips(260, 190, 70, 85, "#f9d9c4", DONKER, 6)
VS.ellips(235, 175, 12, 8, "#ffffff", DONKER, 4)
VS.ellips(285, 175, 12, 8, "#ffffff", DONKER, 4)
VS.pad("M 238 230 Q 260 245 282 230", "none", ROOD, 6)
VS.pad("M 300 200 q 6 14 0 24", "none", BLAUW, 4)
# B: kubistisch gezicht
VS.pad("M 680 90 L 800 80 L 830 180 L 780 290 L 670 280 L 640 170 Z", "#c8b79a", DONKER, 3)
VS.pad("M 740 90 L 800 80 L 830 180 L 760 170 Z", "#a89377", DONKER, 2)
VS.pad("M 760 170 L 830 180 L 780 290 L 745 230 Z", "#8f7c63", DONKER, 2)
VS.pad("M 700 150 L 735 140 L 735 165 L 700 170 Z", "#ffffff", DONKER, 2)
VS.cirkel(718, 156, 5, DONKER, DONKER, 1)
VS.pad("M 795 150 L 820 190 L 790 200", "none", DONKER, 3)
VS.lijn(700, 240, 750, 245, DONKER, 3)
# C: Mondriaan-achtig raster
for (x, y, b, h, kl) in ((60, 360, 150, 120, ROOD), (210, 360, 210, 120, "#ffffff"), (420, 360, 40, 210, BLAUW),
                          (60, 480, 90, 90, "#ffffff"), (150, 480, 150, 90, GEEL), (300, 480, 120, 90, "#ffffff")):
    VS.rect(x, y, b, h, kl, DONKER, 0, 8)
VS.letter(68, 368, "C")
# D: losse kleurtoetsen
rnd = random.Random(7)
for _ in range(170):
    x, y = rnd.uniform(560, 940), rnd.uniform(380, 570)
    kl = rnd.choice([LICHTGROEN, "#7fae6b", GEEL, "#f0d98a", "#a7c7e7", PAARS, "#e9a3b4"])
    VS.svg(f'<rect x="{x:.0f}" y="{y:.0f}" width="16" height="7" rx="3" fill="{kl}" transform="rotate({rnd.uniform(-40, 40):.0f} {x:.0f} {y:.0f})"/>')

# Prent 2: tijdlijn --------------------------------------------------------------------
TL = Prent("tijdlijn-stromingen", "Vijf stromingen op een tijdlijn",
           "een tijdlijn van 1780 tot 1980 met vijf genummerde punten A tot E, rond 1790, 1820, 1850, 1875 en 1960")
X0, X1, J0, J1 = 80, 920, 1780, 1980


def xj(jaar):
    return X0 + (jaar - J0) / (J1 - J0) * (X1 - X0)


TL.pijl(X0 - 20, 330, X1 + 30, 330, DONKER, 4)
for jaar in range(1780, 1981, 20):
    TL.lijn(xj(jaar), 318, xj(jaar), 342, DONKER, 2)
    TL.tekst(xj(jaar), 375, str(jaar), 16)
PUNT = {}
for letter, jaar in (("A", 1790), ("B", 1820), ("C", 1850), ("D", 1875), ("E", 1960)):
    TL.lijn(xj(jaar), 330, xj(jaar), 250, DONKER, 2)
    TL.letter(xj(jaar), 228, letter)
    PUNT[letter] = xj(jaar)


def vz(l):
    return [Prent.zone(*VAK[l])]


def pz(l):
    return [Prent.rond(PUNT[l], 228, 40)]


VRAGEN = [
    klik("Klik op het schilderij in de stijl van de popart.", VS.bestand, vz("A"),
         "Een stripgezicht met dikke lijnen en rasterstippen is typisch voor de popart, zoals bij Lichtenstein."),
    klik("Klik op het kubistische schilderij.", VS.bestand, vz("B"),
         "Hoekige vlakken en meerdere standpunten tegelijk wijzen op het kubisme."),
    klik("Klik op het impressionistische schilderij.", VS.bestand, vz("D"),
         "Losse kleurtoetsen naast elkaar en licht op een tuin zijn typisch voor het impressionisme."),
    met_prent(VS.bestand, keuze("Schilderij C met rechte zwarte lijnen en vlakken in rood, geel en blauw doet denken aan [[*Mondriaan|Monet|Warhol]]. Het is [[*abstract|realistisch|romantisch]].",
              "Mondriaan herleidde alles tot lijnen en primaire kleuren, zonder herkenbaar onderwerp.")),
    klik("Klik op de tijd waarin de popart ontstond.", TL.bestand, pz("E"),
         "De popart ontstond in de jaren 1950 en 1960."),
    klik("Klik op de tijd waarin het realisme opkwam.", TL.bestand, pz("C"),
         "Het realisme kwam op in het midden van de 19de eeuw."),
    met_prent(TL.bestand, keuze("Punt A, rond 1790, past bij het [[*neoclassicisme|impressionisme|kubisme]]. Punt D, rond 1875, past bij het [[*impressionisme|neoclassicisme|popart]].",
              "Rond 1800 neoclassicisme, vanaf 1870 impressionisme.")),
    met_prent(TL.bestand, keuze("De romantiek, rond punt [[*B|D|E]], ontstond als reactie op het [[*neoclassicisme|impressionisme|realisme]].",
              "Tegenover de strakke regels van het neoclassicisme zette de romantiek gevoel en verbeelding.")),
    koppel("Koppel de stroming aan de reactie waaruit ze ontstond.", [
        ["romantiek", "tegen het verstand en de strakke regels van het neoclassicisme"],
        ["realisme", "tegen het dromerige van de romantiek"],
        ["modernisme", "op de industriële revolutie en nieuwe technologie"],
        ["postmodernisme", "tegen de strenge zoektocht naar één zuivere vorm"],
    ], ["tegen de grotschilderingen van Lascaux"], "Stromingen reageren op eerdere stromingen of op veranderingen in de samenleving."),
    koppel("Koppel het werk uit de 19de of 20ste eeuw aan de schilder.", [
        ["De vrijheid leidt het volk", "Delacroix"],
        ["De wandelaar boven de nevelzee", "Friedrich"],
        ["De arenlezeressen", "Millet"],
        ["Impressie, opkomende zon", "Monet"],
        ["De Schreeuw", "Munch"],
    ], ["Warhol"], "Warhol is popart, met soepblikken en Marilyn Monroe."),
    sorteer("Bij welke stroming hoort dit kenmerk?", ["romantiek", "realisme", "impressionisme", "popart"], [
        ["stormen, ruïnes en de macht van de natuur", "romantiek"],
        ["boeren en arbeiders zonder opsmuk", "realisme"],
        ["licht van één moment, buiten geschilderd", "impressionisme"],
        ["soepblikken en filmsterren in zeefdruk", "popart"],
        ["de eenzame mens tegenover de grote natuur", "romantiek"],
        ["schaduwen in blauw of paars in plaats van zwart", "impressionisme"],
    ], "Elke stroming heeft eigen onderwerpen en vormelijke kenmerken."),
    tabel("Klopt dit over de 19de eeuw en de popart?", [
        ("Verf in tubes maakte het makkelijker om buiten te schilderen.", J),
        ("De naam impressionisme kwam van een criticus die spottend een titel van Monet gebruikte.", J),
        ("Het realisme wilde de werkelijkheid mooier tonen dan ze was.", F),
        ("Popart maakte een strikt onderscheid tussen hoge kunst en alledaagse producten.", F),
    ], "Het realisme toonde de werkelijkheid zoals ze is. Popart vervaagde het onderscheid tussen kunst en product."),
    casus(
        "Je ziet een ongezien schilderij. Een man schreeuwt op een brug. De lucht kleurt fel oranje en rood, het water draait in golvende lijnen. "
        "Het gezicht is vervormd en lijkt op een schedel. Niets ziet eruit zoals in het echt.",
        [
            mk("Bij welke stroming past dit schilderij van de brug het best?",
               ["expressionisme", "realisme", "neoclassicisme", "impressionisme"], 0,
               "Felle, onnatuurlijke kleuren en vervorming om een gevoel te tonen zijn typisch voor het expressionisme."),
            keuze("De kunstenaar toont vooral [[*wat hij voelt|hoe iets er echt uitziet|een verhaal uit de oudheid]]. Een bekend voorbeeld van zo'n werk is De Schreeuw van [[*Munch|Monet|Millet]].",
                  "Het expressionisme drukt een innerlijk gevoel uit."),
            tabel("Gaat dit over de vorm of over de context van het werk?", [
                ("golvende lijnen en vervormde figuren", "vorm"),
                ("de angst en onrust van de moderne mens rond 1900", "context"),
                ("felle, onnatuurlijke kleuren", "vorm"),
            ], "Het modernisme reageerde op een snel veranderende wereld.",
               kolommen=["vorm", "context"]),
        ],
    ),
    mk("Waarom zochten schilders na de uitvinding van de fotografie andere dingen dan een exacte kopie?",
       ["een foto kon de werkelijkheid al vastleggen", "foto's waren goedkoper dan verf en doeken",
        "schilderijen mochten niet meer realistisch zijn", "de fotografie verbood het schilderen van mensen"], 0,
       "Schilders gingen op zoek naar licht, indruk, gevoel en nieuwe vormen."),
    mk("Waarom maakte Warhol vaak hetzelfde beeld vele keren in zeefdruk?",
       ["om herhaling in de massacultuur te tonen", "omdat hij geen andere techniek kende of leerde",
        "om het licht van één moment buiten te vangen", "omdat de kerk hem dat opdroeg voor een altaar"], 0,
       "Zijn atelier heette The Factory: het werkte zoals een fabriek."),
    tabel("Modernisme of postmodernisme?", [
        ("op zoek naar één nieuwe, zuivere vorm", "modernisme"),
        ("stijlen mengen en oude kunst citeren met humor", "postmodernisme"),
        ("breken met oude regels door de nieuwe tijd", "modernisme"),
        ("niet geloven in één juiste weg", "postmodernisme"),
    ], "Het postmodernisme reageerde op het ernstige modernisme met spel en mengvormen.",
       kolommen=["modernisme", "postmodernisme"]),
    volgorde("Zet deze stromingen in de juiste volgorde in de tijd.", [
        "neoclassicisme", "romantiek", "realisme", "impressionisme", "kubisme", "popart",
    ], "Rond 1800 neoclassicisme, dan romantiek, realisme rond 1850, impressionisme vanaf 1870, kubisme rond 1910, popart na 1950."),
    sleep("Het kubisme van [[Picasso]] en Braque toont een onderwerp van [[verschillende]] kanten tegelijk, in hoekige vlakken.",
          ["Monet", "één"], "Het kubisme brak het ene standpunt van het perspectief open."),
    keuze("De Discuswerper en de strakke helden van David horen bij een kunst die terugblikt op de [[*klassieke oudheid|middeleeuwen|prehistorie]]. Die stroming rond 1800 heet het [[*neoclassicisme|realisme|expressionisme]].",
          "Neo betekent nieuw: men greep opnieuw terug naar de Grieken en Romeinen."),
    mk("Welke ontwikkeling in de samenleving verklaart mee de opkomst van het realisme?",
       ["fabrieken, arbeiders en sociale onrust", "de bouw van de piramiden in Egypte",
        "de bloei van de kloosters in de middeleeuwen", "televisie en reclame na 1950"], 0,
       "De industriële revolutie bracht harde omstandigheden voor gewone mensen."),
    inv("Hoe heet de stroming die beelden uit reclame, strips en massacultuur gebruikt?", ["popart", "pop-art", "pop art"],
        "Popart komt van popular art."),
    inv("Hoe heet de stroming van Picasso en Braque met hoekige vlakken?", ["kubisme"],
        "Een criticus vond de werken op blokjes lijken."),
    mk("Je ziet een ongezien schilderij: een eenzame figuur op de rug gezien, op een rots, boven een woeste zee in de mist. Welke stroming?",
       ["romantiek", "impressionisme", "popart", "neoclassicisme"], 0,
       "De kleine mens tegenover de grote natuur is een typisch beeld van de romantiek."),
    tabel("Klopt dit over de impressionisten?", [
        ("Ze schilderden vaak buiten, snel en met losse toetsen.", J),
        ("Ze wilden een perfect afgewerkt beeld zonder zichtbare penseelstreek.", F),
        ("Monet schilderde hetzelfde onderwerp vaak opnieuw in ander licht.", J),
    ], "Het licht van het moment was belangrijker dan een gladde afwerking."),
    mk("Een schilder rond 1800 maakt strakke, heldhaftige taferelen uit de Romeinse geschiedenis. Wie past daarbij?",
       ["Jacques-Louis David", "Gustave Courbet", "Roy Lichtenstein", "Caspar David Friedrich"], 0,
       "David schilderde strakke, heldhaftige taferelen zoals De eed van de Horatii."),
    tabel("Hoort deze kunstenaar bij het realisme of bij het impressionisme?", [
        ("Courbet", "realisme"),
        ("Monet", "impressionisme"),
        ("Millet", "realisme"),
        ("Renoir", "impressionisme"),
    ], "Courbet en Millet schilderden het harde leven, Monet en Renoir het licht.",
       kolommen=["realisme", "impressionisme"]),
    keuze("Van Gogh werkte na het impressionisme, met [[*felle kleuren en dikke, draaiende toetsen|zachte grijze tinten zonder toetsen|strakke rechte lijnen en vlakken]]. Hij wordt vaak genoemd bij het begin van het [[*expressionisme|neoclassicisme|realisme]].",
          "Zijn kleuren en lijnen drukken vooral gevoel uit."),
    open_("Leg uit waarom het realisme een reactie was op de romantiek, en verbind het met de context.",
          "De romantiek zette gevoel, verbeelding en dromen centraal, met stormen, ruïnes en helden. Realisten zoals Courbet en Millet vonden dat te dromerig. Ze wilden het echte leven tonen, ook armoede en zwaar werk. Dat past bij de context van de industriële revolutie, toen veel arbeiders en boeren in harde omstandigheden leefden."),
]
