"""Middeleeuwen, renaissance en barok — pittig (🌍 Beyond doorstroom,
kunstbeschouwing en filosofie). Strikt binnen beyond/bron/kfb_middeleeuwen.py:
romaans, gotiek, Vlaamse primitieven, renaissance en barok, met context,
vormelijke kenmerken en de bekendste namen en werken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL, ROOD

# Prent 1: twee kerken -----------------------------------------------------------
KE = Prent("twee-kerken", "Twee kerken in schema",
           "A een lage kerk met dikke muren, kleine ronde ramen en een rondboog als deur; B een hoge kerk met spitse torens, een groot rond roosvenster, spitsboogramen en schuine steunbogen aan de buitenkant")
ZONES = {}
# A: romaans
KE.rect(60, 300, 340, 250, "#e9e2cf", DONKER, 0, 3)
KE.pad("M 60 300 L 230 200 L 400 300 Z", "#d8cdb2", DONKER, 3)
KE.pad("M 200 550 L 200 470 A 30 30 0 0 1 260 470 L 260 550 Z", "#8a6d4b", DONKER, 3)
for x in (110, 330):
    KE.pad(f"M {x} 420 L {x} 385 A 12 12 0 0 1 {x + 24} 385 L {x + 24} 420 Z", "#4a5a6a", DONKER, 2)
KE.letter(230, 605, "A")
ZONES["A"] = (50, 190, 360, 370)
# B: gotisch
KE.rect(610, 230, 220, 320, "#efe9da", DONKER, 0, 3)
KE.pad("M 610 230 L 640 90 L 670 230 Z", "#d8cdb2", DONKER, 3)
KE.pad("M 770 230 L 800 90 L 830 230 Z", "#d8cdb2", DONKER, 3)
KE.cirkel(720, 300, 42, BLAUW, DONKER, 3)
for a in range(8):
    import math
    KE.lijn(720, 300, 720 + 42 * math.cos(a * math.pi / 4), 300 + 42 * math.sin(a * math.pi / 4), "#ffffff", 2)
KE.pad("M 690 550 L 690 440 L 720 395 L 750 440 L 750 550 Z", "#8a6d4b", DONKER, 3)
for x in (630, 790):
    KE.pad(f"M {x} 470 L {x} 380 L {x + 10} 360 L {x + 20} 380 L {x + 20} 470 Z", BLAUW, DONKER, 2)
# luchtbogen rechts
KE.rect(905, 330, 40, 220, "#d8cdb2", DONKER, 0, 3)
KE.pad("M 905 360 Q 870 300 830 290", "none", DONKER, 6)
KE.pad("M 905 450 Q 870 400 830 390", "none", DONKER, 6)
KE.letter(720, 605, "B")
ZONES["B"] = (600, 80, 360, 480)
ZONES["luchtboog"] = (820, 280, 135, 280)
ZONES["roos"] = (670, 250, 100, 100)

# Prent 2: perspectief ---------------------------------------------------------
PS = Prent("lijnperspectief", "Een zaal met zuilen in lijnperspectief",
           "een vloer met tegels en twee rijen zuilen; alle lijnen lopen samen naar één punt in het midden van de achterwand")
VX, VY = 500, 280
PS.rect(60, 80, 880, 500, "#fbfaf5", DONKER, 0, 3)
for x0 in range(60, 941, 110):
    PS.lijn(x0, 580, VX, VY, GRIJS, 2)
for y in (330, 380, 440, 510):
    t = (y - VY) / (580 - VY)
    PS.lijn(VX - 440 * t, y, VX + 440 * t, y, GRIJS, 2)
for t in (1.0, 0.7, 0.5, 0.35):
    for kant in (-1, 1):
        x = VX + kant * 330 * t
        PS.rect(x - 18 * t, VY - 190 * t, 36 * t, 490 * t, "#e9e2cf", DONKER, 0, 2)
PS.lijn(60, 80, VX, VY, ORANJE, 2, stippel=True)
PS.lijn(940, 80, VX, VY, ORANJE, 2, stippel=True)


def kz(n):
    return [Prent.zone(*ZONES[n])]


VRAGEN = [
    klik("Klik op de romaanse kerk.", KE.bestand, kz("A"),
         "Dikke muren, kleine ramen en rondbogen zijn typisch romaans."),
    klik("Klik op de luchtbogen die de druk van het gewelf aan de buitenkant opvangen.", KE.bestand, kz("luchtboog"),
         "Dankzij luchtbogen en steunberen konden gotische muren dunner worden, met grotere ramen."),
    met_prent(KE.bestand, keuze("Het grote ronde raam van kerk B heet een [[*roosvenster|oculus|kapiteel]]. De ramen van kerk B eindigen in een [[*spitsboog|rondboog|hoefijzerboog]].",
              "Roosvensters en spitsbogen zijn kenmerken van de gotiek.")),
    met_prent(KE.bestand, mk("Waarom is kerk A binnen wellicht donkerder dan kerk B?",
              ["dikke muren dragen alles, dus kleine ramen", "romaanse kerken kregen nooit glasramen in kleur",
               "romaanse kerken werden enkel 's nachts gebruikt", "de rondboog houdt het licht van de zon tegen"], 0,
              "Bij romaanse kerken dragen de muren het gewicht. Grote ramen zouden de muur verzwakken.")),
    klik("Klik op het verdwijnpunt.", PS.bestand, [Prent.rond(VX, VY, 40)],
         "Alle lijnen die de diepte in lopen, komen samen in één verdwijnpunt."),
    met_prent(PS.bestand, keuze("Dit is een [[*lijnperspectief|sfumato|clair-obscur]] met één verdwijnpunt. Het werd uitgewerkt in de [[*renaissance|gotiek|barok]].",
              "Het lijnperspectief geeft een plat vlak diepte. Het werd in Florence in de renaissance uitgewerkt.")),
    sorteer("Romaans, gotiek, renaissance of barok?", ["romaans", "gotiek", "renaissance", "barok"], [
        ["dikke muren en rondbogen", "romaans"],
        ["spitsbogen en grote glasramen", "gotiek"],
        ["rust, symmetrie en één verdwijnpunt", "renaissance"],
        ["beweging, diagonalen en drama", "barok"],
        ["kleine ramen, eerder donker", "romaans"],
        ["luchtbogen aan de buitenkant", "gotiek"],
        ["de mens als middelpunt, met juiste verhoudingen", "renaissance"],
        ["fel licht uit een donkere achtergrond", "barok"],
    ], "Elke stijl heeft eigen vormelijke kenmerken."),
    koppel("Koppel het werk aan de kunstenaar.", [
        ["het Lam Gods", "Jan van Eyck"],
        ["de Mona Lisa", "Leonardo da Vinci"],
        ["het plafond van de Sixtijnse Kapel", "Michelangelo"],
        ["de Nachtwacht", "Rembrandt"],
        ["de Kruisafneming in Antwerpen", "Rubens"],
    ], ["Myron"], "Myron is een Griekse beeldhouwer uit de oudheid."),
    tabel("Klopt dit over de Vlaamse primitieven?", [
        ("Primitief betekent bij de Vlaamse primitieven ongeschoold.", F),
        ("De Vlaamse primitieven werkten met dunne lagen olieverf.", J),
        ("In de bolle spiegel van het Arnolfiniportret zie je de kamer weerspiegeld.", J),
        ("Het Lam Gods hangt in een kathedraal in Brugge.", F),
    ], "Primitief betekent hier de eersten. Het Lam Gods staat in de Sint-Baafskathedraal in Gent."),
    casus(
        "Je ziet een ongezien schilderij. Een heilige zit in een kamer. Door een open raam zie je een stad met piepkleine huizen, een rivier en bootjes. "
        "Elke plooi in de mantel, het glas van de kan en het metaal van een kandelaar glanzen. Het werk is in heldere olieverf op een houten paneel.",
        [
            mk("Bij welke stroming past dit werk het best?",
               ["Vlaamse primitieven", "barok", "romaanse kunst", "renaissance in Florence"], 0,
               "De fijne details in olieverf en het doorkijkje naar een stad zijn typisch voor de Vlaamse primitieven."),
            keuze("Het onderwerp is [[*religieus|mythologisch|een landschap zonder mensen]], maar de wereld errond is [[*realistisch en gedetailleerd|vlak met een gouden achtergrond|abstract]].",
                  "Het onderwerp bleef vaak religieus, de wereld errond werd herkenbaar."),
            tabel("Gaat dit over de context of over de vorm van het paneel?", [
                ("glans op glas en metaal in dunne lagen olieverf", "vorm"),
                ("rijke burgers in handelssteden als Brugge en Gent", "context"),
                ("een doorkijkje naar een stad", "vorm"),
            ], "Rijke handelssteden bestelden kunst. De glans en details zijn vormelijke kenmerken.",
               kolommen=["vorm", "context"]),
        ],
    ),
    casus(
        "Je ziet een ongezien groot altaarstuk. Gespierde figuren tillen een kruis in een sterke diagonaal omhoog. Hun kleren wapperen, "
        "de gezichten tonen inspanning en pijn. Een fel licht valt op de figuren, de achtergrond is bijna zwart.",
        [
            mk("Bij welke stroming past dit altaarstuk het best?",
               ["barok", "renaissance", "gotiek", "Vlaamse primitieven"], 0,
               "Diagonale beweging, emotie en clair-obscur zijn typisch voor de barok."),
            keuze("Het sterke contrast tussen licht en donker heet [[*clair-obscur|sfumato|perspectief]]. Een Antwerpse meester van zulke werken is [[*Rubens|Van Eyck|Leonardo da Vinci]].",
                  "Rubens schilderde de Kruisoprichting en de Kruisafneming in de kathedraal van Antwerpen."),
            mk("Waarom koos de kerk in die tijd voor zulke dramatische werken?",
               ["om gelovigen te ontroeren, tegen de reformatie", "om de kerk zo sober en eenvoudig mogelijk te houden",
                "omdat schilders geen rustige werken meer konden maken", "om de werken snel te verkopen aan musea en verzamelaars"], 0,
               "Dat heet de contrareformatie: kunst moest het gevoel aanspreken."),
        ],
    ),
    volgorde("Zet deze stijlen in de juiste volgorde in de tijd.", [
        "romaans", "gotiek", "renaissance", "barok",
    ], "Romaans en gotiek zijn middeleeuws, daarna komen renaissance en barok."),
    tabel("Renaissance of barok?", [
        ("de Mona Lisa met zachte, wazige overgangen", "renaissance"),
        ("bewogen marmeren beelden van Bernini", "barok"),
        ("de Nachtwacht met sterk licht en donker", "barok"),
        ("de David van Michelangelo", "renaissance"),
    ], "Renaissance: rust en evenwicht. Barok: beweging en drama.",
       kolommen=["renaissance", "barok"]),
    sleep("De renaissance begon in [[Italië]], vooral in Florence, waar rijke families zoals de [[Medici]] kunst bestelden. De denkwijze erachter heet het [[humanisme]].",
          ["Brugge", "barok"], "De renaissance greep terug naar de klassieke oudheid en zette de mens centraal."),
    mk("Waarom vertelden kerken in de middeleeuwen bijbelverhalen in glasramen en beelden?",
       ["de meeste mensen konden niet lezen", "boeken bestonden helemaal nog niet",
        "praten was verboden in de kerk", "beelden waren goedkoper dan kaarsen"], 0,
       "Kunst had een verhalende functie. Men noemde ze de bijbel van de armen."),
    inv("Hoe heet de techniek van Leonardo da Vinci met zachte, wazige overgangen zonder harde lijnen?", ["sfumato"],
        "Sfumato betekent als rook."),
    inv("Hoe heet de beweging waarmee de katholieke kerk reageerde op de reformatie?", ["contrareformatie", "de contrareformatie"],
        "De barokkunst was een belangrijk middel van de contrareformatie."),
    mk("Wat bedoelt men met renaissance als reactie op de middeleeuwse kunst?",
       ["men keerde terug naar de oudheid en de mens", "men bouwde opnieuw met dikke muren",
        "men schilderde opnieuw op goud zonder diepte", "men stopte helemaal met religieuze kunst"], 0,
       "Tegenover de middeleeuwse gerichtheid op God zette de renaissance de mens en de klassieke kunst centraal."),
    tabel("Klopt dit over de barok?", [
        ("De barok kan je zien als reactie op de rust van de renaissance.", J),
        ("Caravaggio is bekend voor zijn clair-obscur.", J),
        ("Barokkunst is meestal sober en zonder versiering.", F),
    ], "Barok is bewogen, dramatisch en rijk versierd."),
    mk("Je ziet een ongezien fresco: een symmetrische groep figuren in een zaal met klassieke zuilen. Alle lijnen lopen naar het hoofd van de centrale figuur. Waar past dit het best?",
       ["renaissance", "barok", "romaanse kunst", "gotiek"], 0,
       "Symmetrie, klassieke zuilen en één verdwijnpunt wijzen op de renaissance."),
    keuze("Wie in de middeleeuwen vóór de Vlaamse primitieven een heilige schilderde, gebruikte vaak een [[*gouden achtergrond|realistisch landschap|verdwijnpunt]]. Dat toont een [[*hemelse, tijdloze wereld|gewone straat in de stad|grote veldslag]].",
          "Diepte was niet het doel. Het goud stond voor het goddelijke."),
    mk("Welke uitvinding of techniek hoort bij de Vlaamse primitieven?",
       ["olieverf in dunne, doorschijnende lagen", "beton voor grote koepels en gewelven",
        "verf in tubes om buiten te schilderen", "zeefdruk om beelden te herhalen"], 0,
       "Met dunne lagen olieverf toonden ze glans en de kleinste details."),
    tabel("Hoort dit bij de romaanse kunst of bij de gotiek?", [
        ("de Notre-Dame van Parijs", "gotiek"),
        ("tongewelven en zware pijlers", "romaans"),
        ("de kathedraal van Chartres", "gotiek"),
        ("rondbogen boven deuren en ramen", "romaans"),
    ], "De Notre-Dame en Chartres zijn schoolvoorbeelden van gotiek.",
       kolommen=["romaans", "gotiek"]),
    keuze("Bernini was een barokke [[*beeldhouwer en architect|schilder van kleine portretten|glazenier]] in Rome. Hij ontwierp onder meer het [[*Sint-Pietersplein|Pantheon|Lam Gods]].",
          "Bernini maakte bewogen marmeren beelden en ontwierp het Sint-Pietersplein."),
    mk("Wie waren in de renaissance, naast de kerk, belangrijke opdrachtgevers?",
       ["rijke families en vorsten", "fabrieksbazen en spoorwegen",
        "musea en galerieën in Parijs", "het volk via een stemming"], 0,
       "Families zoals de Medici in Florence bestelden schilderijen, beelden en paleizen."),
    open_("Leg uit hoe de functie van een gotische kathedraal samenhangt met haar vorm.",
          "Een gotische kathedraal moest de gelovigen naar God laten opkijken. Daarom bouwde men zo hoog mogelijk, met spitsbogen. Licht stond voor het goddelijke, dus kwamen er grote, gekleurde glasramen. Die waren mogelijk omdat luchtbogen de druk van het gewelf opvangen. De glasramen vertelden ook bijbelverhalen aan mensen die niet konden lezen."),
]
