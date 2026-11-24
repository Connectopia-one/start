r"""De telregels: product, som en complement — pittig
(🌍 Beyond doorstroom, statistiek). Eigen vragen en een eigen venndiagram,
zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Venndiagram van een klas van 30 -------------------------------------------------------
VN = Prent("venn-talen", "Een klas van 30 leerlingen: wie volgt Spaans, wie Italiaans?", "een rechthoek (de klas van 30) met twee overlappende cirkels: links Spaans, rechts Italiaans; enkel Spaans 9, beide 5, enkel Italiaans 7, buiten de cirkels 9")
VN.rect(80, 70, 840, 520, "#ffffff", DONKER, 8, 2)
VN.tekst(110, 110, "klas: 30 leerlingen", 20, "start")
VN.ellips(400, 340, 220, 180, "#e2eadb", DONKER, 2)
VN.ellips(600, 340, 220, 180, "#e2eadb", DONKER, 2)
VN.ellips(400, 340, 220, 180, "none", DONKER, 2)
VN.tekst(330, 150, "Spaans", 22, "middle", DONKER, True)
VN.tekst(670, 150, "Italiaans", 22, "middle", DONKER, True)
VN.tekst(300, 350, "9", 34, "middle", DONKER, True)
VN.tekst(500, 350, "5", 34, "middle", DONKER, True)
VN.tekst(700, 350, "7", 34, "middle", DONKER, True)
VN.tekst(860, 550, "9", 34, "middle", DONKER, True)
ZONE = {"enkelS": [Prent.zone(200, 230, 170, 220)], "beide": [Prent.zone(440, 230, 120, 220)],
        "enkelI": [Prent.zone(630, 230, 170, 220)], "geen": [Prent.zone(820, 500, 90, 80), Prent.zone(90, 480, 150, 100)]}

VRAGEN = [
    klik("Klik op het gebied met de leerlingen die enkel Italiaans volgen.", VN.bestand, ZONE["enkelI"],
         "In de rechtercirkel, buiten de overlap: 7 leerlingen."),
    klik("Klik op het gebied dat je bij de somregel twee keer zou tellen als je de cirkels gewoon optelt.", VN.bestand, ZONE["beide"],
         "De overlap zit in beide cirkels; die trek je er één keer af."),
    met_prent(VN.bestand, inv("Hoeveel leerlingen volgen minstens één van de twee talen? Schrijf het getal.", ["21"],
              "9 + 5 + 7 = 21, of 14 + 12 - 5 = 21.")),
    met_prent(VN.bestand, inv("Hoeveel leerlingen volgen Spaans in totaal? Schrijf het getal.", ["14"],
              "Enkel Spaans 9 plus beide 5.")),
    met_prent(VN.bestand, inv("Hoeveel leerlingen volgen geen van beide talen, berekend met de complementregel? Schrijf het getal.", ["9"],
              "30 min 21 is 9.")),
    met_prent(VN.bestand, keuze("Om het aantal leerlingen met minstens één taal te vinden, reken je 14 + 12 [[*min 5|plus 5|maal 5]].",
              "De overlap trek je er één keer af.")),
    tabel("Productregel, somregel of complementregel?", [
        ("Je kiest een broek en een trui.", "product"),
        ("Je kiest één dessert: een ijsje of een stuk taart.", "som"),
        ("Hoeveel codes hebben minstens één zeven?", "complement"),
        ("Een outfit met een jas, een sjaal en een muts.", "product"),
    ], "En wijst op vermenigvuldigen, of op optellen, minstens op het complement.",
       kolommen=["product", "som", "complement"]),
    inv("Een slot heeft drie ringen met de cijfers 0 tot 9. Hoeveel standen zijn er? Schrijf het getal.", ["1000", "1 000", "1.000"],
        "10 · 10 · 10 = 1000."),
    inv("Een broodjeszaak heeft 4 soorten brood, 7 soorten beleg en 3 sauzen. Je kiest er van elk één. Hoeveel broodjes zijn er mogelijk?", ["84"],
        "4 · 7 · 3 = 84."),
    casus(
        "Een code voor een kluisje bestaat uit twee letters (26 mogelijkheden) gevolgd door twee cijfers (0 tot 9). "
        "Letters en cijfers mogen herhalen.",
        [
            inv("Hoeveel codes zijn er in totaal? Schrijf het getal.", ["67600", "67 600", "67.600"],
                "26 · 26 · 10 · 10 = 67 600."),
            inv("Hoeveel codes bevatten geen enkele 0? Schrijf het getal.", ["54756", "54 756", "54.756"],
                "26 · 26 · 9 · 9 = 54 756."),
            inv("Hoeveel codes bevatten minstens één 0? Schrijf het getal.", ["12844", "12 844", "12.844"],
                "Complementregel: 67 600 min 54 756 = 12 844."),
        ],
    ),
    keuze("Het tegengestelde van 'minstens één' is [[*geen enkele|precies één|hoogstens één]].",
          "Daarom werkt de complementregel zo goed bij minstens-vragen."),
    keuze("Het complement van 'hoogstens drie' is [[*minstens vier|minstens drie|precies vier]].",
          "Hoogstens drie is 0, 1, 2 of 3; de rest is 4 of meer."),
    inv("Je gooit vijf keer met een munt. Hoeveel uitkomsten zijn er? Schrijf het getal.", ["32"],
        "2 tot de vijfde is 32."),
    inv("Je gooit vijf keer met een munt. Hoeveel uitkomsten hebben minstens één keer munt? Schrijf het getal.", ["31"],
        "32 min de ene uitkomst met vijf keer kop."),
    mk("Een getal van vier cijfers mag niet met 0 beginnen. Hoeveel zulke getallen zijn er?",
       ["9000", "10000", "9999", "6561"], 0,
       "9 · 10 · 10 · 10 = 9000."),
    tabel("Klopt dit?", [
        ("Bij de productregel moeten beide keuzes evenveel mogelijkheden hebben.", F),
        ("Bij de somregel mogen de groepen niet overlappen, anders trek je de overlap af.", J),
        ("De complementregel werkt alleen als je het totaal kent.", J),
        ("Na de complementregel kan het aantal groter zijn dan het totaal.", F),
    ], "Je trekt iets af van het totaal."),
    inv("Een ijssalon heeft 8 smaken. Je neemt twee bollen, de volgorde telt en dezelfde smaak mag niet twee keer. Hoeveel mogelijkheden?", ["56"],
        "8 · 7 = 56: voor de tweede bol valt één smaak weg."),
    inv("Je gooit twee dobbelstenen. Hoeveel worpen hebben geen enkele zes? Schrijf het getal.", ["25"],
        "5 · 5 = 25."),
    keuze("Bij twee dobbelstenen zijn er dus [[*11|25|12]] worpen met minstens één zes.",
          "36 min 25 is 11."),
    sleep("Het woordje [[en]] wijst meestal op vermenigvuldigen, het woordje [[of]] op optellen.",
          ["niet", "minstens"], "Productregel en somregel."),
    casus(
        "Een jeugdhuis telt 40 leden. 22 spelen gitaar, 15 spelen drum en 6 spelen allebei.",
        [
            inv("Hoeveel leden spelen minstens een van beide instrumenten?", ["31"],
                "22 + 15 - 6 = 31."),
            inv("Hoeveel leden spelen geen van beide?", ["9"],
                "40 - 31 = 9."),
            inv("Hoeveel leden spelen enkel gitaar?", ["16"],
                "22 - 6 = 16."),
        ],
    ),
    mk("Een toets heeft 8 waar-of-niet-waarvragen. Hoeveel invullingen hebben minstens één fout?",
       ["255", "256", "8", "16"], 0,
       "2 tot de achtste is 256; één invulling is helemaal juist, dus 255."),
    keuze("Een fietstocht gaat via 3 wegen naar het dorp en dan via 5 wegen naar het meer. Er zijn [[*15|8|35]] routes.",
          "Productregel: 3 · 5."),
    volgorde("Zet de stappen om 'hoeveel codes van 4 cijfers hebben minstens één 5?' op te lossen in de juiste volgorde.", [
        "het totaal tellen: 10 tot de vierde",
        "het complement tellen: codes zonder 5, 9 tot de vierde",
        "het complement van het totaal aftrekken",
        "nagaan of de uitkomst kleiner is dan het totaal",
    ], "Totaal, complement, aftrekken, reflecteren."),
    met_prent(VN.bestand, inv("Hoeveel leerlingen volgen precies één van de twee talen? Schrijf het getal.", ["16"],
              "Enkel Spaans 9 plus enkel Italiaans 7.")),
    open_("Leg uit waarom je bij 'hoeveel codes van drie cijfers hebben minstens één 7' beter de complementregel gebruikt, en reken het uit.",
          "Minstens één 7 rechtstreeks tellen vraagt veel gevallen (één, twee of drie keer 7). Het complement, geen enkele 7, is eenvoudig: 9 · 9 · 9 = 729. Het totaal is 1000. Dus 1000 - 729 = 271 codes."),
]
