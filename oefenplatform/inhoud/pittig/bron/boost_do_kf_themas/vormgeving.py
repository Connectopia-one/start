"""Richtvragen en de middelen van vormgeving — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen kb_vormgeving: de richtvragen en de middelen van
vormgeving bij beeldende kunst (bouwstenen, materiaal, technieken) en bij
architectuur. Met zelfgetekende compositieschetsen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW, ROOD, LICHTGROEN, ORANJE

CS = Prent("vier-composities", "Vier schetsen van een compositie", "vier vakjes met figuren in een andere schikking, letters A tot D")
KD = [("A", 60, 80), ("B", 520, 80), ("C", 60, 350), ("D", 520, 350)]
for t, x, y in KD:
    CS.rect(x, y, 420, 220, "#ffffff", DONKER, 6, 3)


def figuur(p, x, y, kl):
    p.cirkel(x, y - 28, 12, "#f3dcc2", DONKER, 2)
    p.rect(x - 12, y - 16, 24, 40, kl, DONKER, 6, 2)


# A: driehoek
x, y = 60, 80
for fx, fy in ((210, 95), (150, 185), (270, 185)):
    figuur(CS, x + fx, y + fy, ROOD)
CS.pad(f"M {x+210} {y+50} L {x+120} {y+210} L {x+300} {y+210} Z", "none", GRIJS, 2)
# B: horizontaal
x, y = 520, 80
for k in range(5):
    figuur(CS, x + 70 + k * 70, y + 140, BLAUW)
CS.lijn(x + 40, y + 165, x + 380, y + 165, GRIJS, 2)
# C: diagonaal
x, y = 60, 350
for k in range(4):
    figuur(CS, x + 90 + k * 80, y + 190 - k * 45, ORANJE)
CS.lijn(x + 60, y + 210, x + 370, y + 40, GRIJS, 2)
# D: verticaal
x, y = 520, 350
for k in range(3):
    figuur(CS, x + 210, y + 60 + k * 62, LICHTGROEN)
CS.lijn(x + 210, y + 15, x + 210, y + 210, GRIJS, 2)
for t, x, y in KD:
    CS.letter(x + 25, y + 25, t)
U = "vier-composities.svg"
Z = {t: [Prent.zone(x, y, 420, 220)] for t, x, y in KD}

ZAAL = ("Lees de beschrijving.\n\n"
        "Het nieuwe stadsbad is een langwerpig gebouw met een geraamte van staal. De wanden zijn helemaal uit glas, zodat het "
        "daglicht van alle kanten binnenvalt en weerspiegelt in het water. Het dak hangt aan kabels. Binnen is alles wit, "
        "en de vloer is van gepolijste natuursteen.")

VRAGEN = [
    klik("Bekijk de schetsen. Klik op de compositie met een driehoek als grondvorm.", U, Z["A"], "Drie figuren in een driehoek: veel gebruikt in de renaissance."),
    klik("Klik op de diagonale compositie.", U, Z["C"], "De figuren staan langs een schuine lijn: veel beweging."),
    klik("Klik op de verticale compositie.", U, Z["D"], "De figuren staan boven elkaar."),
    klik("Klik op de horizontale compositie.", U, Z["B"], "De figuren staan naast elkaar: rust."),
    casus(ZAAL, [
        keuze("Een langwerpig gebouw heeft als compositiegrondvorm de [[*langsbouw|centraalbouw]].", "Centraalbouw is rond om een midden."),
        keuze("Een geraamte van staal dat de glazen wanden draagt, is [[*skeletbouw|een dragende muur|boetseren]].", "Daardoor kan de wand helemaal uit glas bestaan."),
        keuze("Een dak dat aan kabels hangt, is een [[*hangende|dragende]] constructie.", "Het gewicht hangt aan kabels."),
        sorteer("Natuurlijk of niet-natuurlijk materiaal?", ["natuurlijk", "niet-natuurlijk"],
                [("staal", "niet-natuurlijk"), ("glas", "niet-natuurlijk"), ("natuursteen", "natuurlijk")],
                "Baksteen, beton, glas en staal maken mensen zelf."),
        keuze("Een interieur dat helemaal wit is, noem je [[*monochroom|polychroom]].", "Eén kleur."),
        mk("Welk middel uit de architectuur speelt in dit bad de grootste rol?",
           ["het licht: lichtinval en reflectie", "de dikke muren en de kleine vensters", "de vele kleuren op de gevel van het bad", "de compositie in een driehoek"],
           0, "Daglicht van alle kanten dat weerspiegelt in het water."),
    ]),
    sorteer("Bouwsteen, materiaal of techniek?", ["bouwsteen", "materiaal", "techniek"],
            [("kleur", "bouwsteen"), ("compositie", "bouwsteen"), ("olieverf", "materiaal"), ("brons", "materiaal"), ("boetseren", "techniek"), ("fresco", "techniek")],
            "Materiaal is waarmee, techniek is hoe."),
    sorteer("Welk kleurgebruik?", ["symbolisch", "expressief", "impressief"],
            [("blauw voor de mantel van Maria", "symbolisch"), ("een rood gezicht omdat de schilder woedend was", "expressief"), ("de kleuren van het licht op een ogenblik", "impressief")],
            "Symbolisch: de kleur staat voor iets."),
    tabel("Is dit een kleurcontrast uit de lijst?",
          [("licht-donker", J), ("warm-koud", J), ("complementair", J), ("primair-secundair", F)],
          "Primair en secundair zijn soorten kleuren."),
    keuze("Je kijkt van heel laag naar een reus omhoog: dat is het [[*kikvorsperspectief|vogelperspectief|lijnperspectief]].", "Als een kikker in het gras."),
    keuze("De schaduw die een vaas op de tafel werpt, is [[*slagschaduw|eigen schaduw]].", "Eigen schaduw zit op het voorwerp zelf."),
    sorteer("Tweedimensionale of driedimensionale techniek?", ["2D", "3D"],
            [("hakken", "3D"), ("boetseren", "3D"), ("collage", "2D"), ("fresco", "2D"), ("construeren", "3D")],
            "Hakken, boetseren en construeren maken iets ruimtelijks."),
    koppel("Koppel de richtvraag aan waarover ze gaat.",
           [("hoe en waarmee", "de middelen van vormgeving"), ("wat", "het onderwerp"), ("waarvoor", "de functie"), ("wie, waar en wanneer", "de context")],
           ["de prijs"],
           "Vier richtvragen."),
    volgorde("Zet de richtvragen in de volgorde waarin je ze beantwoordt.",
             ["hoe en waarmee", "wat", "waarvoor", "wie, waar en wanneer"],
             "Van zien naar begrijpen."),
    inv("Hoe noem je de drie kleuren rood, geel en blauw? Eén woord.", ["primair", "primaire", "primaire kleuren"], "Door mengen krijg je de secundaire en tertiaire kleuren."),
    tabel("Hoort het bij de beeldhouwkunst als materiaal?",
          [("steen", J), ("klei", J), ("olieverf", F), ("ivoor", J), ("aquarel", F)],
          "Olieverf en aquarel horen bij de schilderkunst."),
    mk("Een gevel heeft rode, gele en blauwe tegels. Hoe benoem je dat?",
       ["polychroom", "monochroom", "asymmetrisch gebouwd", "een hangende constructie"],
       0, "Meerdere kleuren: polychroom."),
    keuze("Een werk waarin de figuren over het hele doek verspreid staan, zonder midden, heeft een [[*overall|centrale|symmetrische]] schikking.", "Overall: overal even belangrijk."),
    sleep("Bij ruimte noemt men drie dimensies: [[hoogte]], breedte en [[diepte]]. Een gebouw kan open, gesloten of [[omsloten]] zijn.",
          ["kleur", "licht"], "Ruimte bij beeldende kunst en bij architectuur."),
    tabel("Klopt dit over de middelen van vormgeving?",
          [("Materiaal en techniek zijn hetzelfde middel.", F), ("Een fresco is een techniek van de schilderkunst.", J), ("Natuursteen is een natuurlijk materiaal.", J), ("Licht staat niet bij de middelen van architectuur.", F)],
          "Natuurlijk licht, lichtinval en reflectie staan er wel bij."),
    mk("Waarom zeg je bij een analyse 'diagonale compositie' en niet 'de figuren staan schuin'?",
       ["met de juiste woorden is je analyse precies", "schuin is een verboden woord op elk examen", "diagonaal klinkt gewoon veel mooier dan schuin", "het aantal woorden telt mee voor de punten"],
       0, "De lijst met middelen is de woordenlijst voor je analyse."),
    keuze("Een rond gebouw rond een midden, zoals een koepelkerk, is [[*centraalbouw|langsbouw|skeletbouw]].", "Langsbouw is langwerpig."),
    open_("Beschrijf een schilderij of foto die je kent met drie middelen van vormgeving.",
          "Op de foto staan drie mensen in een driehoek: dat is de compositie. Er is een sterk licht-donkercontrast. En de foto is genomen van onderaf, in kikvorsperspectief."),
    keuze("Wie met de kleur vooral een gevoel van de maker toont, gebruikt kleur [[*expressief|symbolisch|cerebraal]].", "De kleur volgt de emotie, niet de werkelijkheid."),
    inv("Hoe heet het perspectief waarbij je van bovenaf kijkt? Eén woord.", ["vogelperspectief", "het vogelperspectief"], "Van heel laag naar boven is het kikvorsperspectief."),
    tabel("Hoort het bij structuur en textuur van een gebouw?",
          [("grof", J), ("gepolijst", J), ("ruw", J), ("monochroom", F)],
          "Monochroom gaat over kleur."),
]
