"""De oorsprong van de westerse filosofie — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_oorsprong: mythologie, de stap naar de
natuurfilosofie, Thales, Heraclitus, Parmenides en Pythagoras, en de westerse
filosofie in tijd en ruimte. Met vier zelfgetekende zinnebeelden."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, ORANJE

ZB = Prent("vier-zinnebeelden", "Vier zinnebeelden", "vier vakjes met een tekening, letters A tot D")
KD = [("A", 60, 90), ("B", 290, 90), ("C", 520, 90), ("D", 750, 90)]
for t, x, y in KD:
    ZB.rect(x, y, 200, 420, "#ffffff", DONKER, 12, 3)
    ZB.letter(x + 100, y + 460, t)
# A: rivier die stroomt
ZB.pad("M 90 140 C 180 200 80 280 170 340 S 120 440 200 480", "none", BLAUW, 26)
ZB.pad("M 120 220 l 18 10 l -4 -18", "none", "#ffffff", 3); ZB.pad("M 140 380 l 18 10 l -4 -18", "none", "#ffffff", 3)
# B: druppel water
ZB.pad("M 390 170 C 330 270 320 330 390 360 C 460 330 450 270 390 170 Z", "#9ec7e6", DONKER, 3)
ZB.pad("M 370 300 q 5 30 30 40", "none", "#ffffff", 4)
# C: driehoek van tien punten (getallen)
for rij in range(4):
    for k in range(rij + 1):
        ZB.cirkel(620 - rij * 28 + k * 56, 200 + rij * 60, 14, ORANJE, DONKER, 2)
ZB.lijn(560, 430, 680, 430, DONKER, 3); ZB.lijn(575, 410, 575, 450, DONKER, 2); ZB.lijn(665, 410, 665, 450, DONKER, 2)
# D: één volle, gesloten bol die nooit verandert
ZB.cirkel(850, 290, 80, GRIJS, DONKER, 4)
ZB.pad("M 790 270 Q 850 230 910 270", "none", "#ffffff", 4)
U = "vier-zinnebeelden.svg"
Z = {t: [Prent.zone(x, y, 200, 480)] for t, x, y in KD}

DONDER = ("Lees de twee verklaringen.\n\n"
          "Verklaring 1: « De donder rolt omdat de oppergod boos is op de mensen. Hij slingert zijn bliksems naar wie hem niet eert. »\n\n"
          "Verklaring 2: « Als de wolken tegen elkaar botsen, ontstaat er een harde knal. Wie goed kijkt, ziet dat het altijd donderen kan als er donkere wolken zijn. »")

VRAGEN = [
    klik("Bekijk de vier zinnebeelden. Klik op het zinnebeeld dat bij Heraclitus past.", U, Z["A"], "Alles stroomt: je stapt nooit twee keer in dezelfde rivier."),
    klik("Klik op het zinnebeeld bij Thales van Milete.", U, Z["B"], "Water is voor Thales de oerstof."),
    klik("Klik op het zinnebeeld bij Pythagoras.", U, Z["C"], "Getallen en verhoudingen, ook in de muziek."),
    klik("Klik op het zinnebeeld bij Parmenides.", U, Z["D"], "Het zijnde is één en verandert niet."),
    casus(DONDER, [
        sorteer("Mythe of natuurfilosofie?", ["mythe", "natuurfilosofie"],
                [("verklaring 1", "mythe"), ("verklaring 2", "natuurfilosofie")],
                "De mythe zoekt de oorzaak buiten de natuur, de natuurfilosofie in de natuur zelf."),
        mk("Wat is het grootste verschil tussen de twee verklaringen?",
           ["de eerste zoekt een wil, de tweede een natuurlijke oorzaak", "de eerste verklaring is veel korter en dus ook veel duidelijker", "de tweede verklaring gaat over bliksem, de eerste helemaal niet", "de eerste verklaring is Grieks en de tweede komt uit Egypte"],
           0, "Van god naar natuur, van verhaal naar argument."),
        tabel("Klopt dit over verklaring 1?",
              [("Ze is niet te weerleggen.", J), ("Ze geeft een beeld in plaats van een bewijs.", J), ("Ze steunt op wat je kan waarnemen.", F)],
              "Een mythe gebruikt goden en wordt verteld en doorgegeven."),
        keuze("Ook als de tweede verklaring niet helemaal klopt, is ze een stap naar de filosofie, omdat ze [[*een natuurlijke oorzaak zoekt|langer is|over het weer gaat]].", "Je kan ze controleren en verbeteren."),
    ]),
    koppel("Koppel de filosoof aan zijn antwoord.",
           [("Thales", "alles komt uit water"), ("Heraclitus", "alles stroomt en verandert"), ("Parmenides", "verandering is schijn"), ("Pythagoras", "alles is getal")],
           ["alles is vuur van de goden"],
           "Vier antwoorden op dezelfde vraag: waaruit bestaat alles?"),
    mk("Welke vraag stelden alle natuurfilosofen?",
       ["waaruit bestaat alles?", "welke god is de sterkste van allemaal?", "hoe word je rijk door handel op zee?", "wie wint de oorlog tussen de steden?"],
       0, "Ze zochten een oerstof of grondbeginsel."),
    keuze("De westerse filosofie begon in de [[*zesde eeuw voor Christus|eerste eeuw na Christus|middeleeuwen]].", "In de Griekse steden van Klein-Azië."),
    keuze("Milete was een [[*Griekse havenstad aan de kust van Klein-Azië|stad in het midden van Egypte|Romeinse stad in Italië]].", "Handel bracht er ideeën samen."),
    mk("Een zeeman uit Milete hoort in Egypte een ander scheppingsverhaal dan het zijne. Wat helpt dat volgens deze uitleg?",
       ["hij gaat zijn eigen verhaal in vraag stellen", "hij bouwt thuis meteen een tempel voor de Egyptische goden", "hij vergeet al zijn eigen mythen en verhalen voor altijd", "hij besluit dat alle verhalen over de wereld precies even waar zijn"],
       0, "Handel bracht die ontmoeting."),
    tabel("Klopt dit over de eerste filosofen?",
          [("Een mythe heeft geen enkele waarde.", F), ("De natuurfilosofen gaven allemaal hetzelfde antwoord.", F), ("Het woord fysica komt van physis, natuur.", J), ("Ook India en China kennen oude filosofische tradities.", J)],
          "Een mythe geeft zin en samenhang aan een gemeenschap."),
    sorteer("Past dit bij de stap van mythe naar filosofie?", ["mythe", "filosofie"],
            [("verhaal", "mythe"), ("argument", "filosofie"), ("gezag", "mythe"), ("reden", "filosofie"), ("geloven", "mythe"), ("onderzoeken", "filosofie")],
            "Van verhaal naar argument, van gezag naar reden."),
    keuze("Iemand zegt: 'Je kan nooit twee keer in dezelfde rivier stappen.' Hij sluit aan bij [[*Heraclitus|Parmenides|Thales]].", "Panta rhei: alles stroomt."),
    keuze("Iemand zegt: 'Wat we zien veranderen, bedriegt ons.' Hij sluit aan bij [[*Parmenides|Heraclitus|Pythagoras]].", "Het zijnde kan niet ontstaan of vergaan."),
    mk("Waarom koos Thales water als oerstof?",
       ["leven heeft overal water nodig", "hij woonde ver van de zee en kende het water nauwelijks", "de goden van Milete hadden het hem zo in een droom verteld", "water is het zwaarste en hardste van alle bekende stoffen"],
       0, "Hij zocht een beginsel in de natuur zelf."),
    inv("Welke filosoof verbond de filosofie met wiskunde en muziek? Eén naam.", ["Pythagoras", "pythagoras"], "Mooie samenklanken volgen eenvoudige getalverhoudingen."),
    keuze("Het woord 'westers' in westerse filosofie [[*plaatst deze lijn, zonder haar boven andere tradities te zetten|betekent dat het de enige echte filosofie is|zegt dat ze uit Amerika komt]].", "Er bestaan ook andere tradities."),
    volgorde("Zet in de juiste volgorde.",
             ["mythen verklaren de wereld met goden", "Thales zoekt één natuurlijke oerstof", "de natuurfilosofen geven elk een ander antwoord"],
             "De stap van mythe naar filosofie."),
    mk("Waarom noemt men Thales vaak de eerste westerse filosoof?",
       ["hij liet de goden als verklaring vallen", "hij schreef het allereerste dikke boek over de Griekse goden", "hij bouwde de eerste grote filosofenschool midden in Athene", "hij was de oudste en dus de wijste Griek van zijn tijd"],
       0, "Hij zocht één natuurlijk beginsel."),
    tabel("Is dit een natuurfilosoof?",
          [("Thales", J), ("Heraclitus", J), ("Aristoteles", F), ("Pythagoras", J), ("Parmenides", J)],
          "Aristoteles komt veel later."),
    keuze("Heraclitus en Parmenides staan tegenover elkaar: [[*verandering tegen rust|water tegen vuur|goden tegen mensen]].", "De een ziet alles stromen, de ander niets veranderen."),
    sleep("De natuurfilosofen zochten de [[oerstof]] van alles. Thales zei [[water]], Pythagoras zei [[getal]].",
          ["god", "lucht"], "Elk een ander antwoord."),
    keuze("Pythagoras zag dat een snaar die half zo lang is, een toon hoger klinkt die mooi samenklinkt. Voor hem bewees dat: [[*alles is getal|alles stroomt|alles is water]].", "Muziek volgt getalverhoudingen."),
    mk("Wat is een oerstof?",
       ["het ene beginsel waaruit alles bestaat", "de oudste stof die men in een grot vond", "een stof die enkel de goden mochten gebruiken", "een verhaal over hoe de eerste mensen leefden"],
       0, "Thales zei water, anderen zochten iets anders."),
    tabel("Klopt dit over Parmenides en Heraclitus?",
          [("Voor Heraclitus is verandering het wezen van alles.", J), ("Voor Parmenides tonen de zintuigen ons de ware werkelijkheid.", F), ("Parmenides vertrouwt op het denken boven de zintuigen.", J)],
          "Wat we zien veranderen, is voor Parmenides schijn."),
    sorteer("Welk woord past bij welke filosoof?", ["Thales", "Heraclitus", "Parmenides", "Pythagoras"],
            [("vocht", "Thales"), ("vuur en strijd", "Heraclitus"), ("het zijnde", "Parmenides"), ("verhouding", "Pythagoras")],
            "Elk zocht een ander grondbeginsel."),
    open_("Leg in je eigen woorden uit waarom de stap van mythe naar natuurfilosofie zo belangrijk was.",
          "In een mythe ligt de oorzaak bij een god, en dat kan je niet controleren. De natuurfilosofen zochten de oorzaak in de natuur zelf. Zo kon je over een verklaring redeneren, ze vergelijken en verbeteren. Dat is het begin van filosofie en wetenschap."),
]
