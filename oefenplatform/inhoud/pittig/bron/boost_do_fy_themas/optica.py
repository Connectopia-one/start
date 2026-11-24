"""Licht: weerkaatsing, breking en lenzen — pittig (🚀 Boost doorstroom, fysica).

Eigen vragen strikt binnen fy_optica, met een zelfgetekende bolle lens met optische as om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL

# Bolle lens met optische as: F op 150 px, 2F op 300 px -------------------------
LENS = Prent("bolle-lens", "Bolle lens met optische as", "dunne bolle lens met de optische as en vijf letters op de as, links een voorwerp als pijl")
LENS.lijn(40, 330, 960, 330, DONKER, 2)
LENS.ellips(500, 330, 22, 220, "#dcebf7", BLAUW, 3)
LENS.pijl(110, 330, 110, 210, ORANJE, 5)
LENS.tekst(110, 195, "voorwerp", 18)
for x in (200, 350, 500, 650, 800):
    LENS.lijn(x, 320, x, 340, DONKER, 3)
LENS.pijl(110, 210, 500, 210, GEEL, 3)
for x, t in [(200, "A"), (350, "B"), (500, "C"), (650, "D"), (800, "E")]:
    LENS.letter(x, 390, t)
U = "bolle-lens.svg"
Z = {t: Prent.zone(x - 45, 300, 90, 120) for x, t in [(200, "A"), (350, "B"), (500, "C"), (650, "D"), (800, "E")]}
# A = 2F links, B = F links, C = optisch middelpunt, D = F rechts, E = 2F rechts

VRAGEN = [
    klik("De gele straal loopt parallel met de optische as naar de lens. B en D liggen even ver van de lens, A en E dubbel zo ver. Klik op het punt waar die straal na de lens door de as gaat.", U, [Z["D"]],
         "Een straal parallel met de as gaat na de lens door het brandpunt aan de andere kant."),
    klik("Klik op het punt waar een straal rechtdoor gaat zonder van richting te veranderen.", U, [Z["C"]],
         "Door het optisch middelpunt breekt een straal niet."),
    klik("Op welk punt moet je het voorwerp zetten om een omgekeerd beeld te krijgen dat even groot is? Klik erop.", U, [Z["A"]],
         "Op 2F staat het beeld op 2F aan de andere kant, omgekeerd en even groot."),
    klik("Een straal komt van links door dit punt en loopt na de lens parallel met de as. Klik op het punt.", U, [Z["B"]],
         "Een straal door het brandpunt voor de lens gaat na de lens parallel met de as."),
    casus("Een lichtstraal valt onder een hoek van 40° met het spiegeloppervlak op een vlakke spiegel.", [
        inv("Hoe groot is de invalshoek in graden?", ["50", "50°"],
            "De invalshoek meet je tegenover de normaal: 90° − 40° = 50°."),
        inv("Hoe groot is de hoek tussen de invallende en de weerkaatste straal, in graden?", ["100", "100°"],
            "Invalshoek plus weerkaatsingshoek: 50° + 50° = 100°."),
    ]),
    sorteer("Is het voorwerp doorzichtig, doorschijnend of ondoorschijnend?", ["doorzichtig", "doorschijnend", "ondoorschijnend"],
            [("een helder raam", "doorzichtig"), ("matglas in een badkamer", "doorschijnend"), ("een houten deur", "ondoorschijnend"), ("bakpapier", "doorschijnend"), ("een bakstenen muur", "ondoorschijnend"), ("helder water", "doorzichtig")],
            "Doorzichtig: scherp beeld; doorschijnend: licht maar geen scherp beeld; ondoorschijnend: geen licht."),
    tabel("Lien staat 1,5 m voor een vlakke spiegel. Klopt dit?",
          [("Haar beeld staat 1,5 m achter de spiegel.", J), ("De afstand tussen Lien en haar beeld is 3,0 m.", J), ("Haar beeld is kleiner dan zijzelf.", F), ("Haar beeld kan je op een scherm opvangen.", F)],
          "Het beeld is virtueel en even groot, even ver achter als voor de spiegel."),
    keuze("Een straal die van water naar lucht gaat, buigt [[*van de normaal weg|naar de normaal toe|helemaal niet af]].",
          "Van optisch dicht naar optisch ijl wordt de hoek met de normaal groter."),
    tabel("Een voorwerp van 2,0 cm geeft door een bolle lens een beeld van 6,0 cm. Klopt dit?",
          [("De vergrotingsfactor is 3.", J), ("Het voorwerp staat dichter bij de lens dan 2F.", J), ("De beeldafstand is drie keer de voorwerpsafstand.", J), ("Het voorwerp staat verder dan 2F.", F)],
          "Een vergroot reëel beeld krijg je tussen F en 2F; verder dan 2F wordt het beeld kleiner."),
    mk("Bij een maansverduistering staat:",
       ["de aarde tussen de zon en de maan", "de maan tussen de zon en de aarde", "de zon tussen de aarde en de maan", "de maan achter de zon"], 0,
       "De maan komt in de schaduw van de aarde."),
    koppel("Welk beeld hoort bij welke plaats van het voorwerp voor een bolle lens?",
           [("verder dan 2F", "reëel, omgekeerd, kleiner"), ("op 2F", "reëel, omgekeerd, even groot"), ("tussen F en 2F", "reëel, omgekeerd, groter"), ("tussen F en de lens", "virtueel, rechtop, groter")],
           ["virtueel, omgekeerd, kleiner"], "Hoe dichter bij F, hoe groter en verder het beeld."),
    sleep("Bij weerkaatsing liggen de invallende straal, de weerkaatste straal en de [[normaal]] in één vlak. De [[invalshoek]] is gelijk aan de [[weerkaatsingshoek]].",
          ["brandpunt", "brekingshoek"], "De twee terugkaatsingswetten."),
    tabel("Een lamp schijnt op een bal voor een muur. Klopt dit?",
          [("Met een grote lamp krijg je een bijschaduw rond de kernschaduw.", J), ("Hoe dichter de bal bij de lamp, hoe groter de schaduw op de muur.", J), ("Met een kleine puntbron is er een brede bijschaduw.", F)],
          "Een puntbron geeft bijna enkel kernschaduw; een grote bron ook bijschaduw."),
    mk("Een vis lijkt in het water hoger te zitten dan hij echt zit. Hoe komt dat?",
       ["De stralen breken van de normaal weg als ze het water verlaten.", "Het licht kaatst diffuus terug tegen het ruwe wateroppervlak.", "De stralen breken naar de normaal toe als ze uit het water gaan.", "Het wateroppervlak werkt als een vlakke spiegel boven de vis."], 0,
       "Je oog volgt de gebroken straal terug in een rechte lijn en ziet de vis hoger."),
    volgorde("Rangschik de stappen om het beeld van een voorwerp bij een bolle lens te construeren.",
             ["Teken de optische as, de lens en de brandpunten.", "Teken een straal vanuit de top van het voorwerp parallel met de as.", "Laat die straal na de lens door het brandpunt gaan.", "Teken een tweede straal door het optisch middelpunt.", "Het snijpunt van de twee stralen is de top van het beeld."],
             "Twee kenmerkende stralen volstaan om het beeldpunt te vinden."),
    mk("Waarom zie je een wit blad papier van op elke plaats in de klas?",
       ["Het papier kaatst het licht diffuus terug, in alle richtingen.", "Het papier zendt zelf licht uit, net als een lamp.", "Het papier breekt het licht naar de normaal toe.", "Het papier kaatst het licht regelmatig terug, zoals een spiegel."], 0,
       "Een ruw oppervlak verstrooit het licht naar alle kanten."),
    tabel("Welke beelden kan je op een scherm opvangen?",
          [("het beeld van een diaprojector", J), ("je spiegelbeeld in de badkamer", F), ("het beeld door een loep", F), ("het beeld van een lens in een fototoestel", J)],
          "Enkel reële beelden vang je op; een spiegel en een loep geven virtuele beelden."),
    inv("Het beeld van een kaars door een lens is 4 keer kleiner dan de kaars van 12 cm. Hoe groot is het beeld in cm?", ["3", "3,0", "3 cm"],
        "12 / 4 = 3,0 cm; de vergrotingsfactor is 0,25."),
    tabel("Klopt dit over de breking van licht?",
          [("Bij breking verandert de richting van de straal aan het grensvlak.", J), ("Een straal die loodrecht invalt, breekt niet.", J), ("Van lucht naar glas wordt de brekingshoek groter dan de invalshoek.", F)],
          "Naar een optisch dichtere stof buigt de straal naar de normaal toe."),
    casus("Ruben bekijkt een postzegel door een loep met een brandpuntsafstand van 10 cm.", [
        mk("Waar moet de postzegel liggen om een vergroot, rechtopstaand beeld te zien?",
           ["dichter bij de loep dan 10 cm", "tussen 10 cm en 20 cm van de loep", "verder dan 20 cm van de loep", "precies op 20 cm van de loep"], 0,
           "Tussen het brandpunt en de lens krijg je een virtueel, rechtopstaand en vergroot beeld."),
        tabel("Klopt dit over het beeld dat Ruben ziet?",
              [("Het beeld is virtueel.", J), ("Hij kan het beeld op een blad opvangen.", F), ("Het beeld staat aan dezelfde kant van de loep als de postzegel.", J)],
              "Een loep geeft een virtueel beeld aan de kant van het voorwerp."),
    ]),
    inv("Een lichtstraal valt in op een spiegel met een invalshoek van 25°. Hoe groot is de hoek tussen de weerkaatste straal en het spiegeloppervlak, in graden?", ["65", "65°"],
        "De weerkaatsingshoek is 25°, dus met het oppervlak 90° − 25° = 65°."),
    sorteer("Is het een voorbeeld van weerkaatsing of van breking?", ["weerkaatsing", "breking"],
            [("je spiegelbeeld in een vijver", "weerkaatsing"), ("een stok die geknikt lijkt in het water", "breking"), ("een vergrootglas dat zonlicht bundelt", "breking"), ("de achteruitkijkspiegel van een auto", "weerkaatsing"), ("een zwembad dat ondieper lijkt", "breking")],
            "Weerkaatsing: het licht keert terug; breking: het gaat door naar een andere stof."),
    keuze("Een bolle lens is in het midden [[*dikker|dunner|even dik]] dan aan de rand en bundelt evenwijdige stralen in het [[*brandpunt|optisch middelpunt|invalspunt]].",
          "Daarom heet een bolle lens ook een convergerende lens."),
    tabel("Een voorwerp staat 30 cm voor een bolle lens met F = 10 cm. Klopt dit?",
          [("Het voorwerp staat verder dan 2F.", J), ("Het beeld is reëel en omgekeerd.", J), ("Het beeld is groter dan het voorwerp.", F)],
          "2F ligt op 20 cm; verder dan 2F geeft een verkleind, omgekeerd, reëel beeld."),
    mk("Je verschuift het voorwerp van ver weg naar het brandpunt van een bolle lens. Wat gebeurt er met het reële beeld?",
       ["Het komt verder van de lens en wordt groter.", "Het komt dichter bij de lens en wordt kleiner.", "Het blijft op dezelfde plaats en wordt groter.", "Het wordt virtueel zodra het voorwerp verschuift."], 0,
       "Hoe dichter het voorwerp bij F komt, hoe verder en groter het beeld."),
    koppel("Welk woord hoort bij welke beschrijving?",
           [("normaal", "lijn loodrecht op het oppervlak in het invalspunt"), ("invalshoek", "hoek tussen invallende straal en normaal"), ("brekingshoek", "hoek tussen gebroken straal en normaal"), ("optische as", "lijn loodrecht door het midden van de lens")],
           ["brandpuntsafstand"], "Alle hoeken meet je tegenover de normaal."),
    inv("Een voorwerp van 5,0 cm geeft een beeld met vergrotingsfactor 2,5. Hoe groot is het beeld in cm?", ["12,5", "12.5", "12,5 cm"],
        "5,0 · 2,5 = 12,5 cm."),
    tabel("Klopt dit over het stralenmodel?",
          [("Een lichtstraal teken je als een rechte met een pijl.", J), ("De pijl toont de zin waarin het licht gaat.", J), ("Licht gaat in lucht in een boog rond een voorwerp.", F)],
          "In een doorzichtige stof plant licht zich rechtlijnig voort."),
]
