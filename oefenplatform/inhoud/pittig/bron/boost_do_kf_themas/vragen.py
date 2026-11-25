"""Soorten vragen en de filosofische vraag — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_vragen: weetvraag, meningsvraag en filosofische
vraag, en de vijf kenmerken van de filosofische vraag. Met een zelfgetekende
prent van zes tekstwolkjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, GEEL, LICHTGROEN

VW = Prent("zes-vragenwolkjes", "Zes vragen in de klas", "zes tekstwolkjes met een vraag, letters A tot F")
WOLK = [("A", 60, 80, "Hoe laat is het?"), ("B", 370, 80, "Wat is tijd?"), ("C", 680, 80, "Welke kleur vind jij het mooist?"),
        ("D", 60, 340, "Hoe ver staat de maan van de aarde?"), ("E", 370, 340, "Wat is vriendschap?"), ("F", 680, 340, "Welke pizza bestel jij vanavond?")]
for t, x, y, v in WOLK:
    VW.rect(x, y, 260, 160, "#ffffff", DONKER, 30, 3)
    VW.pad(f"M {x+60} {y+160} L {x+50} {y+200} L {x+100} {y+160}", "#ffffff", DONKER, 3)
    VW.lijn(x + 62, y + 160, x + 98, y + 160, "#ffffff", 4)
    woorden, regels, r = v.split(), [], ""
    for w in woorden:
        if len(r + " " + w) > 17:
            regels.append(r); r = w
        else:
            r = (r + " " + w).strip()
    regels.append(r)
    for i, rg in enumerate(regels):
        VW.tekst(x + 130, y + 70 + i * 30 - (len(regels) - 1) * 15, rg, 22)
    VW.letter(x + 220, y + 200, t)
U = "zes-vragenwolkjes.svg"
Z = {t: [Prent.zone(x, y, 260, 220)] for t, x, y, v in WOLK}

KLAS = ("Lees het gesprek.\n\n"
        "Mira: « Hoeveel leerlingen spijbelden vorig jaar in onze school? »\n"
        "Jonas: « Ik vind spijbelen eigenlijk best stoer. »\n"
        "Lien: « Maar wat is plicht eigenlijk? Moet je altijd doen wat de regels zeggen? »")

VRAGEN = [
    klik("Bekijk de zes vragen. Klik op de filosofische vraag die je kan maken van de weetvraag A.", U, Z["B"], "Hoe laat het is, zoek je op. Wat tijd is, moet je onderzoeken."),
    klik("Klik op de weetvraag over de ruimte.", U, Z["D"], "Die afstand kan je opzoeken of meten."),
    klik("Klik op de meningsvraag over eten.", U, Z["F"], "Iedereen mag iets anders kiezen."),
    klik("Klik op de filosofische vraag over hoe mensen met elkaar omgaan.", U, Z["E"], "Je komt er met argumenten, niet met een meting."),
    casus(KLAS, [
        tabel("Welk soort vraag of uitspraak?",
              [("de vraag van Mira", "weetvraag"), ("de zin van Jonas", "mening"), ("de vraag van Lien", "filosofische vraag")],
              "Mira's vraag kan je opzoeken in de cijfers van de school.", ["weetvraag", "mening", "filosofische vraag"]),
        mk("Waarom is de zin van Jonas nog geen antwoord op een filosofische vraag?",
           ["hij geeft geen argument", "hij stelt in zijn zin helemaal geen vraag aan iemand", "hij praat over iets dat al voorbij is op school", "spijbelen is een onderwerp dat niet bij filosofie past"],
           0, "Een mening volstaat niet: je moet uitleggen waarom."),
        keuze("De vraag van Lien is [[*meerduidig|empirisch op te lossen|een weetvraag]]: plicht kan over de wet, over je ouders of over je geweten gaan.", "Eerst verhelder je het begrip."),
        tabel("Heeft de vraag van Lien dit kenmerk?",
              [("open", J), ("universeel", J), ("op te lossen met een meting", F)],
              "Een filosofische vraag is niet-empirisch op te lossen."),
    ]),
    sorteer("Weetvraag, meningsvraag of filosofische vraag?", ["weetvraag", "meningsvraag", "filosofische vraag"],
            [("Wanneer werd de euro ingevoerd?", "weetvraag"), ("Wat is je favoriete seizoen?", "meningsvraag"), ("Is een belofte altijd bindend?", "filosofische vraag"), ("Hoe lang is de Schelde?", "weetvraag"), ("Welke serie kijk jij het liefst?", "meningsvraag"), ("Wat is schoonheid?", "filosofische vraag")],
            "Opzoeken, kiezen of onderzoeken met argumenten."),
    koppel("Koppel het kenmerk aan de uitleg.",
           [("fundamenteel", "de vraag raakt de grond van de zaak"), ("meerduidig", "de vraag kan je op meer manieren begrijpen"), ("open", "elk antwoord roept nieuwe vragen op"), ("universeel", "de vraag kan overal en altijd gesteld worden")],
           ["een proef geeft het antwoord"],
           "Het vijfde kenmerk: niet-empirisch op te lossen."),
    mk("Een klasgenoot zegt: 'Een filosofische vraag is open, dus elk antwoord is even goed.' Wat klopt?",
       ["argumenten blijven wegen", "dat klopt, want er is toch geen eindantwoord te vinden", "dat klopt, want het is dan eigenlijk gewoon een meningsvraag", "dat klopt niet, want er is altijd één juist antwoord"],
       0, "Open betekent geen eindantwoord, niet dat alles mag."),
    tabel("Klopt dit over de soorten vragen?",
          [("Een meningsvraag vraagt om argumenten.", F), ("Een weetvraag beslis je met een boek, een meting of een zoekmachine.", J), ("Hetzelfde woord kan in een weetvraag en in een filosofische vraag staan.", J), ("Een filosofische vraag gaat over een detail.", F)],
          "Wat is tijd, tegenover hoe laat is het."),
    sleep("Een [[weetvraag]] heeft één juist antwoord. Bij een [[meningsvraag]] mag iedereen iets anders vinden. Een [[denkvraag]] onderzoek je met argumenten.",
          ["weetwoord", "smaakvraag"], "Denkvraag is een ander woord voor filosofische vraag."),
    mk("Welke vraag is de filosofische versie van 'Hoeveel mensen zeggen dat ze gelukkig zijn?'",
       ["wat is geluk?", "hoeveel mensen zeggen dat ze heel ongelukkig zijn?", "welk land heeft vandaag de gelukkigste inwoners?", "ben jij zelf vandaag een gelukkig mens of niet?"],
       0, "Vraag naar het begrip zelf."),
    keuze("'Is een leugen om een vriend te sparen goed?' Die vraag kan je niet met een proef beslechten. Ze is dus [[*niet-empirisch op te lossen|meerduidig|een weetvraag]].", "Je komt er met argumenten."),
    keuze("'Wat is rechtvaardigheid?' werd al in het oude Griekenland gesteld en wordt nu nog in elk land gesteld. Ze is dus [[*universeel|meerduidig|empirisch]].", "Ze geldt voor elke mens."),
    tabel("Is dit een kenmerk van een filosofische vraag?",
          [("fundamenteel", J), ("meetbaar", F), ("open", J), ("eenduidig", F), ("universeel", J)],
          "Meerduidig, niet eenduidig, en niet-empirisch, niet meetbaar."),
    volgorde("Zet de stappen bij een filosofische vraag in een logische volgorde.",
             ["herken dat het een filosofische vraag is", "verhelder de begrippen in de vraag", "zoek argumenten voor en tegen een antwoord"],
             "Wie het begrip niet verheldert, praat langs de ander heen."),
    mk("Twee leerlingen discussiëren over vrijheid. De ene bedoelt 'doen wat je wil', de andere 'niet opgesloten zijn'. Welk kenmerk zie je?",
       ["meerduidig", "het kenmerk universeel, want het geldt voor iedereen", "het kenmerk empirisch, want je kan het meten", "het kenmerk fundamenteel, want het gaat over een detail"],
       0, "Eerst afspreken welke vrijheid je bedoelt."),
    inv("Een leerling vraagt: 'Wat is een vriend?' Hoe heet dit soort vraag met één ander woord dan filosofisch?", ["denkvraag", "een denkvraag"], "Een denkvraag."),
    sorteer("Hoe pak je deze vraag aan?", ["opzoeken", "zelf kiezen", "argumenteren"],
            [("Hoe hoog is de Eiffeltoren?", "opzoeken"), ("Welke smaak ijs neem jij?", "zelf kiezen"), ("Mag je een dier opsluiten in een zoo?", "argumenteren"), ("Wanneer was de Slag bij Waterloo?", "opzoeken")],
            "Daarom is het onderscheid tussen de drie soorten nuttig."),
    keuze("'Wat is kennis?' is fundamenteel omdat [[*alle weten erop steunt|ze één juist antwoord heeft|ze over een detail gaat]].", "Ze raakt de grond van de zaak."),
    tabel("Klopt dit over openheid?",
          [("Openheid maakt dat het gesprek blijft doorgaan.", J), ("Een open vraag is een vraag zonder belang.", F), ("Filosofen buigen zich al eeuwen over dezelfde vragen.", J)],
          "Openheid is geen zwakte maar net de winst."),
    keuze("Een wetenschapper meet hoeveel uur jongeren slapen. Dat beantwoordt een [[*weetvraag|filosofische vraag|meningsvraag]].", "Wat slaap voor een mens betekent, is een andere vraag."),
    mk("Waarom kan je een filosofische vraag niet beslechten met een zoekmachine?",
       ["ze vraagt naar de betekenis", "omdat zoekmachines geen moeilijke woorden kennen", "omdat de antwoorden enkel in oude Griekse boeken staan", "omdat het internet over filosofie altijd liegt"],
       0, "Je komt er door te denken."),
    tabel("Weetvraag of filosofische vraag?",
          [("Hoeveel landen telt de Europese Unie?", "weetvraag"), ("Wat maakt een land tot een land?", "filosofische vraag"), ("Hoeveel kilo weegt een olifant?", "weetvraag"), ("Heeft een olifant rechten?", "filosofische vraag")],
          "Dezelfde onderwerpen, een ander soort vraag.", ["weetvraag", "filosofische vraag"]),
    keuze("Bij een meningsvraag heeft [[*niemand|iedereen behalve één]] ongelijk, want het gaat over een smaak of voorkeur.", "Daar is geen twist over mogelijk."),
    inv("Hoeveel kenmerken heeft een filosofische vraag? Schrijf het getal.", ["5", "vijf"], "Fundamenteel, meerduidig, niet-empirisch, open en universeel."),
    tabel("Is deze vraag fundamenteel?",
          [("Wat is waarheid?", J), ("Welke bus rijdt om acht uur?", F), ("Wat is een mens?", J), ("Hoe heet de directeur?", F)],
          "Fundamenteel gaat over de basis, niet over een detail."),
    open_("Bedenk zelf een filosofische vraag over school. Leg uit welke kenmerken ze heeft.",
          "Bijvoorbeeld: 'Moet je naar school gaan om wijs te worden?' Ze is fundamenteel (ze raakt wat leren en wijsheid zijn), meerduidig (wat is wijs?), niet-empirisch op te lossen, open en universeel."),
]
