"""De btw en de btw-aangifte — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_btw, met een zelfgetekend, vereenvoudigd stuk van
een btw-aangifte om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, GRIJS

BA = Prent("btw-aangifte-stuk", "Btw-aangifte (vereenvoudigd stuk)", "zes vakken van een btw-aangifte met letters A tot F")
VAK = [
    ("A", 60, 80, "rooster 81", "aankopen van handelsgoederen,", "grond- en hulpstoffen"),
    ("B", 60, 240, "rooster 82", "aankopen van diensten", "en diverse goederen"),
    ("C", 60, 400, "rooster 83", "aankopen van", "bedrijfsmiddelen"),
    ("D", 520, 80, "verschuldigde btw", "", ""),
    ("E", 520, 240, "aftrekbare btw", "", ""),
    ("F", 520, 400, "saldo", "", ""),
]
for t, x, y, kop, r1, r2 in VAK:
    BA.rect(x, y, 420, 140, "#ffffff", DONKER, 10, 2)
    BA.rect(x, y, 420, 44, LICHTGROEN, DONKER, 10, 2)
    BA.letter(x + 32, y + 22, t)
    BA.tekst(x + 66, y + 30, kop, 20, "start", vet=True)
    BA.tekst(x + 30, y + 80, r1, 19, "start"); BA.tekst(x + 30, y + 108, r2, 19, "start")
    BA.rect(x + 270, y + 88, 130, 36, "#ffffff", GRIJS, 4, 2)
U = "btw-aangifte-stuk.svg"
Z = {t: Prent.zone(x, y, 420, 140) for t, x, y, *_ in VAK}

VRAGEN = [
    klik("Een fietsenwinkel koopt een nieuwe bestelwagen. In welk vak komt het bedrag zonder btw?", U, [Z["C"]],
         "Een bestelwagen is een investering: een bedrijfsmiddel, rooster 83."),
    klik("De fietsenwinkel krijgt de factuur van haar boekhouder. In welk vak komt het bedrag zonder btw?", U, [Z["B"]],
         "Het werk van de boekhouder is een dienst: rooster 82."),
    klik("De fietsenwinkel koopt fietsen om door te verkopen. In welk vak komt het bedrag zonder btw?", U, [Z["A"]],
         "Handelsgoederen: rooster 81."),
    klik("In welk vak komt de btw die de fietsenwinkel aan haar klanten aanrekende?", U, [Z["D"]],
         "Btw op de verkopen is verschuldigde btw: die moet ze doorstorten."),
    klik("In welk vak komt de btw die de fietsenwinkel aan haar leveranciers betaalde?", U, [Z["E"]],
         "Btw op de aankopen is aftrekbaar: die mag ze terugvragen."),
    casus("Lees de cijfers van een fietsenwinkel voor het derde kwartaal.\n\nverkopen: 50 000 euro, btw 21 %\naankopen fietsen: 30 000 euro, btw 21 %\nfactuur boekhouder: 2 000 euro, btw 21 %", [
        inv("Hoe groot is de verschuldigde btw, in euro? Schrijf enkel het getal.", ["10500", "10 500", "10.500"],
            "50 000 × 0,21 = 10 500 euro."),
        inv("Hoe groot is de aftrekbare btw, in euro? Schrijf enkel het getal.", ["6720", "6 720", "6.720"],
            "(30 000 + 2 000) × 0,21 = 6 720 euro."),
        inv("Hoe groot is het btw-saldo, in euro? Schrijf enkel het getal.", ["3780", "3 780", "3.780"],
            "10 500 − 6 720 = 3 780 euro."),
        keuze("Dat saldo moet de winkel [[*betalen aan de staat|terugkrijgen van de staat]].",
              "De verschuldigde btw is groter dan de aftrekbare."),
    ]),
    casus("Volg de btw door de bedrijfskolom van een houten tafel (btw 21 %).\n\nDe zagerij verkoopt hout aan de meubelmaker: 100 euro + 21 euro btw.\nDe meubelmaker verkoopt de tafel aan een winkel: 300 euro + 63 euro btw.\nDe winkel verkoopt de tafel aan Lisa, een particulier: 500 euro + 105 euro btw.", [
        tabel("Hoeveel btw stort deze schakel door aan de staat, in euro?",
              [("de zagerij", "21"), ("de meubelmaker", "42"), ("de winkel", "42")],
              "Verschuldigde min aftrekbare btw: 63 − 21 = 42 en 105 − 63 = 42.",
              kolommen=["21", "42", "63"]),
        inv("Hoeveel btw ontvangt de staat in totaal, in euro? Schrijf enkel het getal.", ["105"],
            "21 + 42 + 42 = 105 euro: precies de btw die Lisa betaalde."),
        mk("Wie draagt de btw van 105 euro uiteindelijk?",
           ["Lisa", "de winkel", "de meubelmaker", "de zagerij"], 0,
           "De eindklant kan de btw niet terugvragen; de ondernemingen schuiven ze door."),
        keuze("Elke schakel betaalt enkel btw op de waarde die ze zelf [[*toevoegt|verkoopt|aankoopt]].",
              "Daarom heet het een belasting op de toegevoegde waarde."),
    ]),
    tabel("Verschuldigde of aftrekbare btw voor een bakker?",
          [("btw op het brood dat hij verkoopt", "verschuldigd"), ("btw op de bloem die hij koopt", "aftrekbaar"), ("btw op een nieuwe oven", "aftrekbaar"), ("btw op de taarten voor een restaurant", "verschuldigd")],
          "Btw op verkopen moet je doorstorten; btw op aankopen mag je aftrekken.",
          kolommen=["verschuldigd", "aftrekbaar"]),
    tabel("Te betalen, terug te krijgen of nul?",
          [("verschuldigd 5 000, aftrekbaar 3 000", "te betalen"), ("verschuldigd 2 000, aftrekbaar 9 000", "terug te krijgen"), ("verschuldigd 4 000, aftrekbaar 4 000", "nul")],
          "Saldo = verschuldigd min aftrekbaar.",
          kolommen=["te betalen", "terug te krijgen", "nul"]),
    mk("Een bouwbedrijf koopt dit kwartaal een grote kraan. Wat gebeurt er wellicht met zijn btw-saldo?",
       ["Het krijgt btw terug van de staat.", "Het moet dubbel zoveel btw betalen.", "Het saldo is precies gelijk aan zijn winst.", "Het mag geen aangifte indienen."], 0,
       "De aftrekbare btw op die investering kan groter zijn dan de verschuldigde."),
    tabel("Klopt dit over de btw?",
          [("Btw is een belasting op de winst.", F), ("Een particulier kan de btw niet terugvragen.", J), ("Een onderneming int de btw voor de staat.", J), ("Het btw-saldo is hetzelfde als de winst.", F)],
          "Btw hangt aan de omzet, niet aan de winst. De onderneming is een doorgeefluik."),
    keuze("Om btw te mogen aftrekken heb je een geldige [[*factuur|offerte|leverbon]] nodig.",
          "Zonder factuur met de juiste vermeldingen is er geen aftrek."),
    keuze("Een Belgisch btw-nummer begint met [[*BE|BTW|NL]], gevolgd door tien cijfers.",
          "Het kenmerk van een btw-plichtige."),
    sorteer("Welk btw-tarief geldt in België meestal?", ["6 %", "21 %"],
            [("brood", "6 %"), ("een laptop", "21 %"), ("groenten", "6 %"), ("een fiets", "21 %"), ("melk", "6 %"), ("een gsm", "21 %")],
            "Voeding valt meestal onder het verlaagde tarief van 6 %, de meeste andere goederen onder 21 %."),
    inv("Hoeveel btw betaal je aan 21 % op 80 euro? Schrijf het getal met een komma.", ["16,8", "16,80", "16.8", "16.80"],
        "80 × 0,21 = 16,80 euro."),
    tabel("Rekent deze persoon of onderneming btw aan?",
          [("een supermarkt", J), ("een zelfstandige loodgieter", J), ("een particulier die zijn oude fiets verkoopt", F), ("een groothandel", J)],
          "Een particulier is geen btw-plichtige."),
    keuze("Een gewone btw-plichtige dient zijn aangifte in [[*elke maand of elk kwartaal|één keer per jaar|elke week]].",
          "Welk van de twee hangt af van de omzet."),
    mk("Wat gebeurt er als een onderneming haar btw-aangifte te laat indient?",
       ["Er volgt een boete.", "De btw vervalt dan helemaal.", "Ze krijgt automatisch btw terug.", "Er gebeurt niets bijzonders."], 0,
       "De termijnen liggen vast; te laat indienen kost geld."),
    sleep("De btw op je verkopen is de [[verschuldigde]] btw. De btw op je aankopen is de [[aftrekbare]] btw.",
          ["toegevoegde", "betaalde winst"], "Twee kanten van de btw-aangifte."),
    open_("Waarom betaalt een onderneming niet de volle btw op haar omzet aan de staat?",
          "Ze mag de btw die ze zelf op haar aankopen betaalde, aftrekken van de btw die ze op haar verkopen aanrekende. Zo betaalt ze enkel btw op de waarde die ze zelf toevoegt; de eindklant draagt de volle btw.",
          "Dat is de kern van het btw-systeem."),
    keuze("Je moet de roosternummers [[*niet uit het hoofd kennen|wel uit het hoofd kennen]], want je krijgt de aangifte erbij; je moet wel weten welk bedrag waar hoort.",
          "Je mag de aangifte raadplegen."),
    klik("In welk vak lees je of de onderneming deze periode btw moet betalen of terugkrijgt?", U, [Z["F"]],
         "Het saldo: verschuldigde min aftrekbare btw."),
    keuze("Een zaak is 3 600 euro btw verschuldigd en mag 4 100 euro aftrekken. Ze [[*krijgt 500 euro terug|moet 500 euro betalen|moet 7 700 euro betalen]].",
          "3 600 − 4 100 = −500: een negatief saldo krijg je terug."),
    inv("Een kapper rekent 2 100 euro btw aan en betaalde 700 euro btw op zijn aankopen. Hoeveel btw stort hij door, in euro? Schrijf enkel het getal.", ["1400", "1 400", "1.400"],
        "2 100 − 700 = 1 400 euro."),
]
