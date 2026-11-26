"""Inhoud, functies en context van een kunstuiting — pittig (🌍 Beyond
doorstroom, kunstbeschouwing en filosofie). Strikt binnen
beyond/bron/kfb_inhoud.py: onderwerp, de zeven functies (decoratief,
economisch, filosofisch, maatschappijkritisch, narratief, ontspannend,
politiek) en de context (tijd, ruimte, politieke, sociale en culturele
context, persoonlijke context van de kunstenaar)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL, ROOD

# Prent 1: drie werken met een andere functie ----------------------------------
DW = Prent("drie-functies", "Drie werken in schema",
           "A een affiche met een grote leider die zijn arm heft boven een menigte, met een vlag; B een herhalend patroon van tegels met bloemen; C een strip van vier vakjes die een verhaal vertelt")
WERK = {}


def werk(letter, x):
    DW.rect(x, 80, 290, 440, "#fbfaf5", DONKER, 8, 3)
    DW.letter(x + 145, 570, letter)
    WERK[letter] = (x, 80, 290, 440)


werk("A", 30)
werk("B", 355)
werk("C", 680)
# A: affiche met leider en menigte
DW.rect(30, 80, 290, 440, "#f3dcd6", DONKER, 8, 3)
DW.cirkel(175, 170, 38, "#f1d9b5", DONKER, 3)
DW.pad("M 125 330 L 135 215 Q 175 195 215 215 L 225 330 Z", ROOD, DONKER, 3)
DW.lijn(205, 225, 265, 140, DONKER, 8)
DW.lijn(80, 110, 80, 250, DONKER, 4)
DW.rect(80, 110, 60, 40, ROOD, DONKER, 0, 2)
for i in range(7):
    DW.cirkel(55 + i * 40, 400, 16, GRIJS, DONKER, 2)
    DW.cirkel(70 + i * 38, 450, 16, GRIJS, DONKER, 2)
DW.rect(50, 470, 250, 36, DONKER, DONKER, 4, 1)
# B: tegelpatroon
for r in range(4):
    for k in range(3):
        x, y = 375 + k * 85, 100 + r * 100
        DW.rect(x, y, 80, 95, "#eef3f8", BLAUW, 4, 2)
        for dx, dy in ((0, -18), (18, 0), (0, 18), (-18, 0)):
            DW.cirkel(x + 40 + dx, y + 47 + dy, 11, BLAUW, BLAUW, 1)
        DW.cirkel(x + 40, y + 47, 8, GEEL, DONKER, 1)
# C: strip in vier vakjes
for i, (x, y) in enumerate(((695, 95), (830, 95), (695, 305), (830, 305))):
    DW.rect(x, y, 125, 195, "#ffffff", DONKER, 4, 2)
    DW.cirkel(x + 45, y + 110, 18, "#f1d9b5", DONKER, 2)
    DW.lijn(x + 45, y + 128, x + 45, y + 175, DONKER, 3)
    DW.rect(x + 15, y + 15, 95, 40, "#ffffff", DONKER, 14, 2)
    DW.tekst(x + 62, y + 42, ["Hé!", "Kijk!", "Oei...", "Hoera!"][i], 18)

# Prent 2: de context rond een kunstwerk --------------------------------------
CX = Prent("context-rond-werk", "De context van een kunstwerk",
           "in het midden een kader met het woord kunstwerk; rondom vier vakken: A tijd, B ruimte, C politieke, sociale en culturele context, D persoonlijke context van de kunstenaar")
VAK = {}
CX.rect(380, 250, 240, 140, LICHTGROEN, DONKER, 12, 3)
CX.tekst(500, 330, "kunstwerk", 28, vet=True)


def cvak(letter, x, y, regels):
    CX.rect(x, y, 300, 130, "#fbfaf5", DONKER, 12, 3)
    CX.letter(x + 30, y + 30, letter)
    for i, r in enumerate(regels):
        CX.tekst(x + 165, y + 80 - (len(regels) - 1) * 15 + i * 30, r, 21, vet=True)
    VAK[letter] = (x, y, 300, 130)


cvak("A", 40, 70, ["tijd"])
cvak("B", 660, 70, ["ruimte"])
cvak("C", 40, 450, ["politieke, sociale", "en culturele context"])
cvak("D", 660, 450, ["persoonlijke context", "van de kunstenaar"])
for x1, y1, x2, y2 in ((340, 150, 400, 250), (660, 150, 600, 250), (340, 500, 400, 390), (660, 500, 600, 390)):
    CX.pijl(x1, y1, x2, y2, DONKER, 3)


def wz(l):
    return [Prent.zone(*WERK[l])]


def cz(l):
    return [Prent.zone(*VAK[l])]


VRAGEN = [
    klik("Klik op het werk met vooral een politieke functie.", DW.bestand, wz("A"),
         "De leider staat groot boven de menigte, met een vlag: het werk wil macht tonen en mensen overtuigen."),
    klik("Klik op het werk met vooral een decoratieve functie.", DW.bestand, wz("B"),
         "Een herhalend patroon versiert een muur of voorwerp. Het vertelt geen verhaal."),
    klik("Klik op het werk met vooral een narratieve functie.", DW.bestand, wz("C"),
         "Een strip vertelt een verhaal in opeenvolgende beelden."),
    met_prent(DW.bestand, keuze("In werk A is de leider veel groter dan de mensen. Die keuze in de [[*vormgeving|context|techniek]] versterkt de [[*politieke|ontspannende|decoratieve]] functie.",
              "Vorm en functie hangen samen: groot afbeelden toont macht.")),
    klik("Een schilder maakte zijn somberste werken kort na de dood van zijn vrouw. Klik op het deel van de context dat dit verklaart.", CX.bestand, cz("D"),
         "Wat de kunstenaar zelf meemaakte, hoort bij de persoonlijke context."),
    klik("Een beeld werd gemaakt voor een tempel in Egypte, dicht bij de Nijl. Klik op het deel van de context dat over de plaats gaat.", CX.bestand, cz("B"),
         "De plaats of streek waar en waarvoor het werk gemaakt werd, is de ruimte."),
    klik("Een kunstenaar maakt in een dictatuur geheime tekeningen tegen de censuur. Klik op het deel van de context dat dit vooral verklaart.", CX.bestand, cz("C"),
         "Een dictatuur en censuur horen bij de politieke context."),
    met_prent(CX.bestand, keuze("Wie nagaat in welke eeuw een werk gemaakt werd en wat er toen gewoon of nieuw was, kijkt naar vak [[*A|B|C|D]]. De zeden en waarden van een samenleving horen bij vak [[*C|A|B|D]].",
              "Tijd is vak A. Sociale en culturele gewoonten horen bij vak C.")),
    tabel("Welke functie staat voorop?", [
        ("een spotprent die de rijkdom van bankiers aanklaagt", "maatschappijkritisch"),
        ("een vrolijke popsong om op te dansen", "ontspannend"),
        ("een schilderij dat de vraag stelt wat de zin van het leven is", "filosofisch"),
        ("een kunstwerk dat vooral gemaakt wordt om met winst te verkopen", "economisch"),
    ], "Kritiek, plezier, nadenken over grote vragen en geld verdienen zijn vier verschillende functies.",
       kolommen=["maatschappijkritisch", "ontspannend", "filosofisch", "economisch"]),
    sorteer("Hoort dit bij het onderwerp of bij de functie van het werk?", ["onderwerp", "functie"], [
        ["een moeder met een kind in een keuken", "onderwerp"],
        ["de kijker doen nadenken over armoede", "functie"],
        ["een storm op zee met een klein bootje", "onderwerp"],
        ["de macht van een koning tonen", "functie"],
        ["drie appels en een kan op een tafel", "onderwerp"],
        ["een ruimte gezellig aankleden", "functie"],
    ], "Het onderwerp is wat je ziet of hoort. De functie is waarvoor het werk dient."),
    mk("Een graffitikunstenaar schildert op een muur een kind dat vastzit achter een barcode, als kritiek op de consumptiemaatschappij. Welke functie staat voorop?",
       ["maatschappijkritisch", "decoratief en versierend", "ontspannend en grappig", "economisch voordeel"], 0,
       "Het werk klaagt iets aan in de samenleving."),
    mk("Waarom kan één werk meerdere functies hebben?",
       ["een werk kan tegelijk vertellen, versieren en kritiek geven", "elke kunstvorm heeft precies zeven functies tegelijk",
        "de functie verandert telkens als het werk verkocht wordt", "functies zijn hetzelfde als bouwstenen en vallen daarom samen"], 0,
       "Een glasraam vertelt een verhaal en versiert de kerk. Een spotprent ontspant en geeft kritiek."),
    koppel("Koppel het voorbeeld aan de context.", [
        ["een werk uit de 15de eeuw, toen olieverf nieuw was", "tijd"],
        ["een fresco geschilderd voor één bepaalde kapel in Rome", "ruimte"],
        ["een lied geschreven tijdens een oorlog tegen de bezetter", "politieke context"],
        ["een portret van de eigen moeder van de schilder", "persoonlijke context"],
    ], ["de techniek"], "De techniek is een middel van vormgeving, geen deel van de context."),
    tabel("Klopt dit over inhoud en context?", [
        ("Het onderwerp en de functies samen vormen de inhoud.", J),
        ("De context van een werk kan verklaren waarom het een bepaalde functie heeft.", J),
        ("De ruimte als context gaat over de lege plekken op een schilderij.", F),
        ("De persoonlijke context van de kunstenaar verklaart altijd alles over een werk.", F),
    ], "Ruimte gaat over de plaats waar en waarvoor het werk gemaakt werd. Ook tijd, plaats en samenleving tellen mee."),
    casus(
        "In 1937 bombardeerden vliegtuigen tijdens de Spaanse Burgeroorlog het stadje Guernica. Picasso, die toen in Parijs woonde, "
        "maakte er een enorm schilderij over voor het Spaanse paviljoen op de wereldtentoonstelling. Hij gebruikte enkel zwart, wit en grijs.",
        [
            tabel("Over welk deel van de context gaat dit?", [
                ("het jaar 1937", "tijd"),
                ("het Spaanse paviljoen op de wereldtentoonstelling", "ruimte"),
                ("de Spaanse Burgeroorlog", "politieke context"),
            ], "Tijd, ruimte en politieke context helpen het werk te begrijpen.",
               kolommen=["tijd", "ruimte", "politieke context"]),
            mk("Welke functie staat in dit werk voorop?",
               ["maatschappijkritisch", "decoratief, voor het paviljoen", "ontspannend voor bezoekers", "economisch, om te verkopen"], 0,
               "Het werk klaagt de gruwel van het bombardement aan."),
            keuze("De keuze voor enkel zwart, wit en grijs is een keuze in de [[*vormgeving|context|functie]]. Ze past bij de sombere [[*inhoud|ruimte|techniek]] van het werk.",
                  "Inhoud, functie, context en vormgeving hangen hier sterk samen."),
        ],
    ),
    sleep("Een groot ruiterstandbeeld van een koning op een plein heeft vooral een [[politieke]] functie. Een kleine snuisterij op een kast heeft eerder een [[decoratieve]] functie.",
          ["narratieve", "filosofische"], "Macht tonen is politiek, versieren is decoratief."),
    mk("Een stripverhaal over een ridder die een draak verslaat, met grappen voor kinderen. Welke twee functies passen het best?",
       ["narratief en ontspannend", "politiek en economisch", "filosofisch en decoratief", "maatschappijkritisch en politiek"], 0,
       "Het vertelt een verhaal en is bedoeld om te ontspannen."),
    keuze("Een filmmaker maakt een documentaire over de armoede in zijn eigen geboortestad. De armoede in die stad hoort bij de [[*sociale context|persoonlijke techniek|decoratieve functie]]. Dat het zijn geboortestad is, hoort bij de [[*persoonlijke context|politieke context|ruimte van het museum]].",
          "Eén werk kan uit meerdere soorten context tegelijk ontstaan."),
    mk("Een kunstenaar maakt duizend kleine beeldjes die meteen online verkocht worden. Welke functie staat hier voorop?",
       ["economisch", "filosofisch", "narratief", "maatschappijkritisch"], 0,
       "Het werk dient vooral om geld te verdienen."),
    inv("Hoe heet de functie van een werk dat vooral een verhaal vertelt?", ["narratief", "narratieve", "de narratieve functie", "narratieve functie"],
        "Narratief komt van het Latijnse narrare, vertellen."),
    inv("Hoe heet de functie van een werk dat vooral een ruimte of voorwerp mooier maakt?", ["decoratief", "decoratieve", "decoratieve functie", "de decoratieve functie"],
        "Decoratief betekent versierend."),
    volgorde("Zet de stappen in een logische volgorde om de inhoud en de context van een werk te onderzoeken.", [
        "beschrijven wat je ziet of hoort: het onderwerp",
        "nagaan waarvoor het werk dient: de functie",
        "opzoeken wanneer, waar en door wie het gemaakt werd: de context",
        "uitleggen hoe de context de functie en het onderwerp verklaart",
    ], "Eerst kijken, dan de functie, dan de context, en dan verbanden leggen."),
    mk("Een beeldhouwer werkt in een cultuur waar men geen mensen afbeeldt in heilige gebouwen. Hij maakt geometrische patronen. Welk deel van de context verklaart dit?",
       ["culturele context", "persoonlijke context", "de tijd alleen", "de economische functie"], 0,
       "Wat in een cultuur gebruikelijk of verboden is, hoort bij de culturele context."),
    tabel("Is dit een filosofische of een maatschappijkritische functie?", [
        ("een beeld dat vraagt wat het betekent om mens te zijn", "filosofisch"),
        ("een affiche tegen kinderarbeid", "maatschappijkritisch"),
        ("een installatie over vergankelijkheid en de dood", "filosofisch"),
        ("een lied dat de vervuiling door fabrieken aanklaagt", "maatschappijkritisch"),
    ], "Filosofisch gaat over grote vragen. Maatschappijkritisch klaagt iets concreets in de samenleving aan.",
       kolommen=["filosofisch", "maatschappijkritisch"]),
    mk("Een kerk bestelt in de middeleeuwen een glasraam met het leven van een heilige, voor gelovigen die niet kunnen lezen. Welke functie staat voorop?",
       ["narratief", "economisch", "ontspannend", "maatschappijkritisch"], 0,
       "Het glasraam vertelt een verhaal en legt het geloof uit. Het versiert de kerk ook, maar dat is niet het enige."),
    tabel("Klopt dit over de tijd als context?", [
        ("Wat in een tijd gewoon, nieuw of verboden was, verklaart keuzes van de kunstenaar.", J),
        ("Hoe lang een film duurt, is de tijd als element van de context.", F),
        ("Hoe lang een werk al in een museum hangt, is de tijd als element van de context.", F),
    ], "De tijd als context is de periode waarin het werk gemaakt werd, met wat er toen speelde."),
    keuze("Een hofschilder maakt een portret van de koning in harnas, voor de troonzaal. De koning als opdrachtgever hoort bij de [[*politieke context|persoonlijke context|tijd]]. Het portret heeft vooral een [[*politieke|ontspannende|filosofische]] functie.",
          "Wie het werk bestelt en waarom, verklaart vaak de functie."),
    open_("Leg met een voorbeeld uit hoe de context van een werk de functie ervan kan verklaren.",
          "Een werk uit een dictatuur, zoals een groot schilderij van een leider tussen juichende mensen, heeft vaak een politieke functie: het moet de macht van de leider tonen. Die functie volgt uit de politieke context: de leider bestelde het werk en wilde het volk overtuigen. Zonder die context zou je misschien gewoon een feest zien."),
]
