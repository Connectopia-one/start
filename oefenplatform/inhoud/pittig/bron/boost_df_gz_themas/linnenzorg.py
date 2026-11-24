"""Linnenzorg: sorteren, wassen en strijken — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_linnenzorg, met een zelfgetekend
onderhoudsetiket."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

ET = Prent("onderhoudsetiket", "Een onderhoudsetiket", "een wit etiket met vijf symbolen: een kuipje met 40, een doorstreepte driehoek, een vierkant met een cirkel, een strijkijzer met één puntje en een cirkel, met letters A tot E")
ET.rect(60, 120, 880, 260, "white", DONKER, 18, 3)
# A wastobbe met 40
ET.pad("M 90 200 L 110 300 L 230 300 L 250 200", "none", DONKER, 5); ET.pad("M 90 200 Q 130 180 170 200 Q 210 220 250 200", "none", DONKER, 5)
ET.tekst(170, 272, "40", 40, vet=True)
# B doorstreepte driehoek
ET.pad("M 370 180 L 440 300 L 300 300 Z", "none", DONKER, 5); ET.lijn(300, 180, 440, 310, DONKER, 5); ET.lijn(440, 180, 300, 310, DONKER, 5)
# C vierkant met cirkel
ET.rect(500, 180, 120, 120, "none", DONKER, 0, 5); ET.cirkel(560, 240, 45, "none", DONKER, 5)
# D strijkijzer met één puntje
ET.pad("M 680 300 L 820 300 L 820 230 Q 820 190 770 190 L 720 190 Q 690 230 680 300 Z", "none", DONKER, 5); ET.pad("M 730 190 L 735 160 L 805 160 L 810 190", "none", DONKER, 5)
ET.cirkel(760, 255, 8, DONKER, DONKER, 1)
# E cirkel
ET.cirkel(880, 240, 40, "none", DONKER, 5)
LET = {"A": (170, 430), "B": (370, 430), "C": (560, 430), "D": (750, 430), "E": (880, 430)}
for t, (x, y) in LET.items():
    ET.letter(x, y, t)
U = "onderhoudsetiket.svg"
ZS = {"A": Prent.rond(170, 245, 85), "B": Prent.rond(370, 245, 80), "C": Prent.rond(560, 240, 70), "D": Prent.rond(750, 245, 80), "E": Prent.rond(880, 240, 50)}
def zones(t):
    return [ZS[t], Prent.rond(*LET[t], 30)]

VRAGEN = [
    klik("Klik op het symbool dat de hoogste wastemperatuur geeft.", U, zones("A"),
         "Het getal in het kuipje is de hoogste temperatuur. Koeler mag altijd."),
    klik("Klik op het symbool van een behandeling die verboden is.", U, zones("B"),
         "Een kruis door een symbool betekent altijd: deze behandeling mag niet."),
    klik("Klik op het symbool dat zegt hoe heet je mag strijken.", U, zones("D"),
         "De puntjes in het strijkijzer geven aan hoe heet het mag."),
    mk("Op het etiket staat een kuipje met 40. Mag je dit stuk op 30 graden wassen?",
       ["ja, koeler mag altijd", "nee, het moet precies op 40", "nee, enkel hoger dan 40", "enkel als je meer product neemt"],
       0, "Het getal is de bovengrens."),
    tabel("Is dit een taak van de linnenzorg?",
          [("de was sorteren", J), ("de strijk doen", J), ("de tafel dekken", F), ("klein verstelwerk", J)],
          "De tafel dekken hoort bij de maaltijdzorg."),
    volgorde("Zet de vuilgraden van licht naar zwaar.",
             ["licht bevuild", "normaal bevuild", "sterk bevuild", "zeer sterk bevuild"],
             "Half bevuild bestaat niet."),
    mk("Een werkbroek zit vol olie en aarde. Wat vraagt die volgens de Sinner-cirkel?",
       ["meer product, warmte of tijd", "een kortere wasbeurt", "een lager toerental", "minder beweging in de trommel"],
       0, "Meer vuil vraagt meer van een van de vier factoren."),
    koppel("Koppel het etiket aan wat het zegt.",
           [("textieletiket", "waaruit het stuk bestaat"), ("onderhoudsetiket", "hoe je het stuk verzorgt")],
           ["hoeveel het stuk kostte"],
           "Het textieletiket geeft de samenstelling, zoals katoen of wol."),
    tabel("Is dit een groep onderhoudsbehandelingen?",
          [("wassen", J), ("bleken", J), ("drogen", J), ("strijken", J), ("vouwen", F)],
          "De vijfde groep is professionele reiniging."),
    inv("Hoeveel groepen onderhoudsbehandelingen staan er op een onderhoudsetiket? Een getal.", ["5", "vijf"], "Wassen, bleken, drogen, strijken en professionele reiniging."),
    mk("Je wast op 30 in plaats van 60 graden. Wat moet je volgens de Sinner-cirkel aanpassen?",
       ["meer tijd, product of beweging", "minder product en minder tijd", "een kleinere trommel kiezen", "niets, het resultaat blijft gelijk"],
       0, "Minder warmte vul je aan met een andere factor."),
    tabel("Sorteer je wasgoed hierop?",
          [("de kleur", J), ("het soort textiel", J), ("de vuilgraad", J), ("de prijs van het kledingstuk", F)],
          "Ook de wastemperatuur."),
    volgorde("Zet de werkvolgorde van de was in de juiste volgorde.",
             ["verzamelen en bewaren", "sorteren", "controleren", "wassen", "drogen", "kastklaar maken"],
             "Strijken komt erna, indien nodig."),
    tabel("Controleer je dit voor het wassen?",
          [("of de zakken leeg zijn", J), ("of de ritsen dicht zijn", J), ("of er vlekken zijn", J), ("of de kleren gestreken zijn", F)],
          "Vlekken behandel je eerst."),
    mk("Waarom sorteer je een rode sok uit de witte was?",
       ["kleuren geven af", "rode sokken krimpen", "witte was is zwaarder", "de sok is sterk bevuild"],
       0, "Een rode sok kleurt een hele witte was roze."),
    mk("Waarom stop je de trommel niet te vol?",
       ["het wasgoed moet kunnen bewegen", "de machine wordt veel te zwaar", "het water raakt veel te snel op", "het toerental gaat dan omhoog"],
       0, "Zonder beweging valt een factor van de Sinner-cirkel weg."),
    keuze("Je kiest het wasprogramma volgens het [[*onderhoudsetiket|textieletiket|kassaticket]].",
          "Het etiket geeft de temperatuur en de behandeling."),
    tabel("Klopt dit over het toerental?",
          [("Het is de snelheid bij het zwieren.", J), ("Hoe hoger, hoe droger de was.", J), ("Hoe hoger, hoe minder kreuken.", F)],
          "Een hoog toerental geeft meer kreuken."),
    mk("Op het etiket van een wollen trui staat het droogsymbool doorstreept. Wat doe je?",
       ["aan een droogrek laten drogen", "in de droogtrommel op een lage stand", "op de verwarming leggen", "nat in de kast leggen"],
       0, "Wol krimpt in de droogtrommel."),
    tabel("Zie je dit aan een goed gestreken stuk?",
          [("geen kreuken", J), ("een nette vouwlijn", J), ("een schroeiplek", F), ("geen glimplekken", J)],
          "Een schroeiplek betekent dat het strijkijzer te heet stond."),
    keuze("Een schroeiplek betekent dat het strijkijzer [[*te heet|te koud|te zwaar]] stond.", "Kies de temperatuur volgens het etiket."),
    casus("Thomas doet in de leefgroep de was. Hij gooit alles samen in de machine: witte T-shirts, een nieuwe rode trui, een wollen sjaal en een modderige voetbalbroek. Hij wast op 60 graden en stopt de trommel propvol.", [
        tabel("Wat doet Thomas fout?",
              [("hij sorteert niet op kleur", J), ("hij stopt de trommel te vol", J), ("hij wast wol op 60 graden", J), ("hij gebruikt een wasmachine", F)],
              "Sorteren op kleur, textiel, temperatuur en vuilgraad."),
        mk("Wat gebeurt er waarschijnlijk met de witte T-shirts?",
           ["ze kleuren roze", "ze worden extra wit", "ze krimpen tot kindermaat", "ze worden waterdicht"],
           0, "De nieuwe rode trui geeft af."),
        keuze("De modderige voetbalbroek is [[*sterk bevuild|licht bevuild|normaal bevuild]].", "Zwaar bevuild wasgoed vuilt de rest mee."),
        inv("Welke stap sloeg Thomas over voor het wassen? Eén woord.", ["sorteren", "het sorteren"], "Sorteren."),
    ]),
    sleep("Na het [[verzamelen]] van het wasgoed komt het [[sorteren]], daarna het [[controleren]] en pas dan het [[wassen]].",
          ["strijken", "bleken"],
          "Strijken komt helemaal op het einde, indien nodig."),
    keuze("Een kruis door het strijkijzer op het etiket betekent: [[*niet strijken|strijken op de hoogste stand|strijken met stoom]].", "Een kruis verbiedt die behandeling."),
    tabel("Lees je dit af van het onderhoudsetiket?",
          [("de wastemperatuur", J), ("of je mag bleken", J), ("of het in de droogtrommel mag", J), ("in welk land het gemaakt is", F)],
          "Ook of het professioneel gereinigd moet worden."),
    keuze("Wol en zijde verdragen [[*veel minder warmte|veel meer warmte|evenveel warmte]] dan katoen.", "Je mag niet elk stuk op zestig graden wassen."),
    open_("Leg uit wat het verschil is tussen een textieletiket en een onderhoudsetiket.",
          "Een textieletiket zegt waaruit het stuk bestaat, zoals katoen of wol. Een onderhoudsetiket toont met symbolen hoe je het wast, bleekt, droogt, strijkt en of het professioneel gereinigd moet worden."),
]
