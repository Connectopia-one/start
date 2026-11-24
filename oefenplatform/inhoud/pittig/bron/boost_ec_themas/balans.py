"""De balans en de resultatenrekening — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen bw_balans, met een zelfgetekende balans om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GROEN, BLAUW

BA = Prent("balans-fietsplus", "Balans van bv Fietsplus op 31 december", "balans met vijf posten aan het actief en vijf aan het passief, elk met een letter")
BA.rect(60, 70, 880, 520, "#ffffff", DONKER, 8, 2)
BA.lijn(500, 70, 500, 590, DONKER, 2); BA.lijn(60, 120, 940, 120, DONKER, 2); BA.lijn(60, 530, 940, 530, DONKER, 2)
BA.tekst(280, 105, "ACTIEF", 22, vet=True); BA.tekst(720, 105, "PASSIEF", 22, vet=True)
ACT = [("A", "Gebouwen", "120 000"), ("B", "Machines", "40 000"), ("C", "Voorraad handelsgoederen", "15 000"), ("D", "Handelsvorderingen", "10 000"), ("E", "Liquide middelen", "5 000")]
PAS = [("F", "Kapitaal", "80 000"), ("G", "Overgedragen winst", "20 000"), ("H", "Lening op 10 jaar", "60 000"), ("I", "Te betalen leveranciers", "25 000"), ("J", "Te betalen btw", "5 000")]
Z = {}
for kol, rij in ((0, ACT), (440, PAS)):
    for i, (l, naam, bedrag) in enumerate(rij):
        y = 170 + i * 75
        BA.letter(100 + kol, y - 6, l)
        BA.tekst(135 + kol, y, naam, 19, "start")
        BA.tekst(480 + kol, y, bedrag, 19, "end")
        Z[l] = Prent.zone(75 + kol, y - 40, 420, 62)
BA.tekst(135, 568, "Totaal", 20, "start", vet=True); BA.tekst(480, 568, "190 000", 20, "end", vet=True)
BA.tekst(575, 568, "Totaal", 20, "start", vet=True); BA.tekst(920, 568, "190 000", 20, "end", vet=True)
U = "balans-fietsplus.svg"

VRAGEN = [
    klik("Klik op een vlottend actief dat een klant nog moet betalen.", U, [Z["D"]],
         "Handelsvorderingen: geld dat klanten nog verschuldigd zijn."),
    klik("Klik op alle vaste activa.", U, [Z["A"], Z["B"]],
         "Gebouwen en machines blijven langer dan een jaar in de onderneming."),
    klik("Klik op een post die bij het eigen vermogen hoort.", U, [Z["F"], Z["G"]],
         "Kapitaal en overgedragen winst zijn het geld van de eigenaars."),
    klik("Klik op de schuld op meer dan één jaar.", U, [Z["H"]],
         "De lening op tien jaar."),
    casus("Gebruik de balans van bv Fietsplus.", [
        inv("Hoe groot is het eigen vermogen, in euro? Schrijf enkel het getal.", ["100000", "100 000", "100.000"],
            "80 000 + 20 000 = 100 000 euro."),
        inv("Hoe groot zijn de schulden op ten hoogste één jaar, in euro? Schrijf enkel het getal.", ["30000", "30 000", "30.000"],
            "25 000 + 5 000 = 30 000 euro."),
        inv("Hoe groot zijn de vlottende activa samen, in euro? Schrijf enkel het getal.", ["30000", "30 000", "30.000"],
            "15 000 + 10 000 + 5 000 = 30 000 euro."),
        keuze("Een klant betaalt een factuur van 4 000 euro. Dan [[*dalen de handelsvorderingen en stijgen de liquide middelen|stijgen de handelsvorderingen en dalen de liquide middelen|stijgt het eigen vermogen]].",
              "Het ene vlottend actief wordt een ander; het totaal blijft 190 000."),
    ]),
    tabel("Actief of passief?",
          [("een bestelwagen", "actief"), ("een banklening", "passief"), ("het geld in de kas", "actief"), ("het kapitaal", "passief"), ("een softwarelicentie", "actief"), ("te betalen lonen", "passief")],
          "Actief is wat je bezit; passief is waarmee het gefinancierd is.",
          kolommen=["actief", "passief"]),
    sorteer("Vast of vlottend actief?", ["vast actief", "vlottend actief"],
            [("een gebouw", "vast actief"), ("de voorraad", "vlottend actief"), ("een machine", "vast actief"), ("geld op de zichtrekening", "vlottend actief"), ("een merknaam die het bedrijf kocht", "vast actief"), ("een vordering op een klant", "vlottend actief")],
            "Vaste activa blijven langer dan een jaar."),
    inv("Een bedrijf heeft 250 000 euro activa en 170 000 euro schulden. Hoe groot is het eigen vermogen? Schrijf enkel het getal.", ["80000", "80 000", "80.000"],
        "Actief = eigen vermogen + schulden: 250 000 − 170 000 = 80 000."),
    keuze("Een balans is een foto op [[*één dag|een heel jaar|een maand]].",
          "Meestal 31 december."),
    keuze("Een resultatenrekening gaat over [[*een hele periode|één dag|één factuur]].",
          "Meestal een boekjaar."),
    casus("Lees de resultatenrekening van een winkel (in euro).\n\nomzet 600 000\naankoop handelsgoederen 380 000\nlonen 120 000\nafschrijvingen 30 000\nontvangen intrest 2 000\nbetaalde intrest 12 000\nbelastingen 25 %", [
        inv("Hoe groot is het bedrijfsresultaat? Schrijf enkel het getal.", ["70000", "70 000", "70.000"],
            "600 000 − 380 000 − 120 000 − 30 000 = 70 000 euro."),
        inv("Hoe groot is het financieel resultaat? Schrijf het getal met het teken.", ["-10000", "−10000", "-10 000", "−10 000", "-10.000"],
            "2 000 − 12 000 = −10 000 euro."),
        inv("Hoe groot is het resultaat na belastingen? Schrijf enkel het getal.", ["45000", "45 000", "45.000"],
            "Voor belastingen 60 000; 25 % = 15 000; na belastingen 45 000 euro."),
    ]),
    tabel("Bedrijfskost of financiële kost?",
          [("de lonen van het personeel", "bedrijfskost"), ("intrest op een lening", "financiële kost"), ("de afschrijving van een machine", "bedrijfskost"), ("de aankoop van handelsgoederen", "bedrijfskost")],
          "Intrest hoort bij het financieel resultaat.",
          kolommen=["bedrijfskost", "financiële kost"]),
    mk("Waarom is een afschrijving een kost, ook al vertrekt er dat jaar geen geld?",
       ["De machine slijt en verliest waarde.", "De bank rekent dat bedrag elk jaar aan.", "De klant betaalt die kost elk jaar terug.", "De overheid verplicht een betaling per jaar."], 0,
       "De aankoopprijs wordt over de gebruiksjaren gespreid."),
    inv("Een machine kost 60 000 euro en gaat 5 jaar mee. Hoe groot is de jaarlijkse afschrijving, lineair? Schrijf enkel het getal.", ["12000", "12 000", "12.000"],
        "60 000 / 5 = 12 000 euro per jaar."),
    keuze("Kapitaal staat op de balans bij het [[*passief|actief]].",
          "Het is financiering, geen bezit."),
    koppel("Welke MAR-klasse hoort bij welke soort rekening?",
           [("klasse 6", "kosten"), ("klasse 7", "opbrengsten"), ("klasse 2", "vaste activa")],
           ["klasse 9"], "Het minimum algemeen rekeningstelsel deelt de rekeningen in klassen in."),
    tabel("Klopt dit over de jaarrekening?",
          [("Het totaal van het actief is altijd gelijk aan het totaal van het passief.", J), ("Een hoge omzet betekent altijd winst.", F), ("Liquide middelen zijn kas en bank.", J), ("Een lening op vijf jaar is een schuld op ten hoogste één jaar.", F)],
          "Winst hangt ook af van de kosten."),
    sleep("Op de balans staat links het [[actief]] en rechts het [[passief]]. De [[resultatenrekening]] zet de kosten en de opbrengsten van een periode naast elkaar.",
          ["omzet", "kas"], "De twee jaarrekeningdelen."),
    keuze("Een bedrijf maakt verlies als de [[*kosten groter zijn dan de opbrengsten|schulden groter zijn dan het eigen vermogen|vaste activa groter zijn dan de vlottende]].",
          "Verlies gaat over de resultatenrekening."),
    klik("Klik op het meest liquide actief: geld dat meteen beschikbaar is.", U, [Z["E"]],
         "Liquide middelen zijn kas en bank."),
    klik("Klik op een schuld op ten hoogste één jaar aan de overheid.", U, [Z["J"]],
         "De btw moet binnen het jaar aan de overheid doorgestort worden."),
    keuze("Bv Fietsplus koopt een machine van 4 000 euro en betaalt meteen met de bank. Het totaal van de balans [[*blijft 190 000 euro|stijgt tot 194 000 euro|daalt tot 186 000 euro]].",
          "Machines stijgen met 4 000, liquide middelen dalen met 4 000: het ene actief wordt een ander."),
    inv("Het resultaat voor belastingen is 80 000 euro en de belasting is 25 %. Wat blijft er over? Schrijf enkel het getal.", ["60000", "60 000", "60.000"],
        "25 % van 80 000 = 20 000; 80 000 − 20 000 = 60 000."),
    keuze("De omzet is een [[*bedrijfsopbrengst|financiële opbrengst|schuld]].",
          "Ze komt uit de gewone werking van de onderneming."),
    open_("Leg uit waarom het totaal van het actief altijd gelijk is aan het totaal van het passief.",
          "Elk bezit aan de actiefzijde is ergens mee gefinancierd: met eigen geld van de eigenaars, met winst of met schulden. Die bronnen staan aan de passiefzijde.",
          "Elk bezit heeft een bron."),
]
