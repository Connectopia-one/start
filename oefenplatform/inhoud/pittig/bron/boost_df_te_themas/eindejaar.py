"""Van proefbalans tot eindbalans — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_eindejaar: proef- en saldibalans, afschrijvingen,
regularisatie van schulden, overdracht van het resultaat en de eindbalans, met een
zelfgetekende voorlopige proef- en saldibalans om rekeningen aan te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS

PS = Prent("proef-en-saldibalans", "Voorlopige proef- en saldibalans", "tabel met acht rekeningen, hun totalen in debet en credit en hun saldo, met letters A tot F")
KOL = [("rekening", 270, "start"), ("totaal debet", 140, "end"), ("totaal credit", 140, "end"), ("saldo debet", 130, "end"), ("saldo credit", 130, "end")]
X0, Y0, RH = 90, 60, 46
def rij(y, waarden, vul="#ffffff", vet=False):
    x = X0
    for (k, b, a), w in zip(KOL, waarden):
        PS.rect(x, y, b, RH, vul, DONKER, 0, 1)
        PS.tekst(x + 10 if a == "start" else x + b - 10, y + 30, w, 16, a, vet=vet)
        x += b
rij(Y0, [k for k, _, _ in KOL], "#e8efe0", True)
DATA = [("230 Machines", "20 000", "", "20 000", ""), ("550 Bank", "18 000", "11 500", "6 500", ""),
        ("570 Kas", "2 000", "1 400", "600", ""), ("100 Kapitaal", "", "15 000", "", "15 000"),
        ("440 Leveranciers", "6 000", "9 000", "", "3 000"), ("604 Aankopen handelsgoederen", "9 000", "", "9 000", ""),
        ("613 Diensten", "300", "800", "", "500"), ("700 Verkopen handelsgoederen", "", "17 600", "", "17 600")]
for i, d in enumerate(DATA):
    rij(Y0 + RH * (i + 1), d)
rij(Y0 + RH * 9, ["Totaal", "55 300", "55 300", "36 100", "36 100"], "#f4f2ec", True)
RX = X0 + sum(b for _, b, _ in KOL)
def ry(i): return Y0 + RH * i + RH / 2
LET = {"A": (RX + 40, ry(1)), "B": (RX + 40, ry(2)), "C": (RX + 40, ry(4)), "D": (RX + 40, ry(5)), "E": (RX + 40, ry(7)), "F": (RX + 40, ry(8)), "G": (RX + 40, ry(9))}
for t, (x, y) in LET.items():
    PS.letter(x, y, t)
U = "proef-en-saldibalans.svg"
Z = {t: Prent.rond(x, y, 22) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Klik op de letter bij de rij die toont dat er evenveel in debet als in credit geboekt is.", U, [Z["G"]],
         "De totalen van debet en credit zijn gelijk, en ook de totalen van de saldo's."),
    klik("Klik op de letter bij de kostenrekening met een saldo dat op een fout wijst.", U, [Z["E"]],
         "Een kostenrekening hoort een debetsaldo te hebben; 613 Diensten heeft een creditsaldo."),
    klik("Klik op de letter bij de rekening waarop de jaarlijkse afschrijving inwerkt.", U, [Z["A"]],
         "Een machine verliest waarde; de afschrijving verlaagt haar boekwaarde."),
    klik("Klik op de letter bij de opbrengstrekening die bij de afsluiting naar nul gaat.", U, [Z["F"]],
         "Kosten en opbrengsten worden afgesloten; hun verschil is het resultaat."),
    klik("Klik op de letter bij de schuld die aan de leveranciers overblijft.", U, [Z["D"]],
         "440 Leveranciers heeft een creditsaldo van 3 000 euro: dat moet de zaak nog betalen."),
    casus("Bekijk de voorlopige proef- en saldibalans.", [
        inv("Wat is het verschil tussen de verkopen en de aankopen in deze balans? Schrijf enkel het getal.", ["8600"],
            "17 600 min 9 000 is 8 600 euro."),
        tabel("Klopt dit volgens de tabel?",
              [("Het saldo van de bank is 6 500 euro in debet.", J), ("De proefbalans toont de totalen, de saldibalans de verschillen.", J), ("Dit is de balans na de eindejaarsverrichtingen.", F), ("De machine is in deze tabel nog niet afgeschreven.", J)],
              "Een voorlopige proef- en saldibalans komt voor de eindejaarsverrichtingen."),
        keuze("Kloppen de totalen, dan is er [[*geen fout waardoor debet en credit verschillen|helemaal geen enkele fout]], want een boeking aan de verkeerde kant van een rekening kan toch kloppen.",
              "Daarom kijk je ook of elk saldo logisch is."),
    ]),
    inv("Een rekening heeft 7 400 euro in debet en 2 950 euro in credit. Hoe groot is het saldo? Schrijf enkel het getal.", ["4450"],
        "7 400 min 2 950 is 4 450 euro, in debet."),
    volgorde("Zet de stappen bij het afsluiten van het boekjaar in de juiste volgorde.",
             ["de voorlopige proef- en saldibalans maken", "de eindejaarsverrichtingen boeken", "de definitieve proef- en saldibalans maken", "de eindbalans opstellen"],
             "Eerst controleren, dan rechtzetten, opnieuw controleren en dan de eindbalans."),
    tabel("Is dit een eindejaarsverrichting?",
          [("de jaarlijkse afschrijving van de bestelwagen", J), ("het deel van een lening dat volgend jaar vervalt verschuiven", J), ("de winst overdragen", J), ("een factuur van een leverancier van 12 juni", F)],
          "Een gewone aankoop boek je tijdens het jaar."),
    casus("Een bakkerij koopt op 1 januari een oven van 24 000 euro. Ze gaat 8 jaar mee en wordt lineair afgeschreven.", [
        inv("Hoeveel euro schrijft de bakkerij elk jaar af? Schrijf enkel het getal.", ["3000"],
            "24 000 gedeeld door 8 is 3 000 euro."),
        inv("Wat is de boekwaarde na vijf jaar? Schrijf enkel het getal.", ["9000"],
            "5 maal 3 000 is 15 000; 24 000 min 15 000 is 9 000 euro."),
        tabel("Klopt dit?",
              [("De afschrijving is een kost van klasse 6.", J), ("Bij het boeken van de afschrijving gaat er geld van de bank.", F), ("Na acht jaar is de boekwaarde nul.", J)],
              "Het geld ging al buiten bij de aankoop."),
    ]),
    sorteer("Wordt dit afgeschreven?", ["ja", "nee"],
            [("een bestelwagen", "ja"), ("een bouwgrond", "nee"), ("een computer", "ja"), ("een magazijngebouw", "ja")],
            "Grond slijt niet en wordt niet afgeschreven."),
    inv("Een machine wordt afgeschreven aan 2 500 euro per jaar over 6 jaar. Wat was de aankoopprijs? Schrijf enkel het getal.", ["15000"],
        "6 maal 2 500 is 15 000 euro."),
    casus("Een zaak heeft een lening van 50 000 euro die ze in vijf gelijke jaarlijkse stukken terugbetaalt. Het eerste stuk vervalt volgend jaar.", [
        inv("Hoeveel euro verhuist naar de schulden op ten hoogste één jaar? Schrijf enkel het getal.", ["10000"],
            "50 000 gedeeld door 5 is 10 000 euro."),
        keuze("Na de regularisatie blijft er [[*40 000|50 000|10 000]] euro bij de schulden op meer dan één jaar.",
              "50 000 min 10 000."),
        mk("Waarom maakt de zaak die verschuiving?",
           ["De lezer ziet zo wat binnen het jaar betaald moet worden.", "Zo daalt het totaal van alle schulden met 10 000 euro.", "De bank eist dat de lening elk jaar opnieuw herberekend wordt.", "Anders telt de hele lening niet meer mee in de eindbalans."], 0,
           "Het totaal van de schulden blijft gelijk; enkel de verdeling verandert."),
    ]),
    tabel("Staat deze rekening op de eindbalans?",
          [("550 Bank", J), ("700 Verkopen handelsgoederen", F), ("440 Leveranciers", J), ("604 Aankopen handelsgoederen", F)],
          "Kosten en opbrengsten gaan naar nul; hun verschil komt bij het eigen vermogen."),
    keuze("De winst van het boekjaar [[*versterkt|verkleint]] het eigen vermogen; een verlies [[*verkleint|versterkt]] het.",
          "Het resultaat komt bij het eigen vermogen op de balans."),
    keuze("De eindbalans van 2027 wordt de [[*beginbalans van 2028|proefbalans van 2028|resultatenrekening van 2027]].",
          "Het nieuwe boekjaar start waar het vorige eindigt."),
    sleep("Het verschil tussen debet en credit van één rekening is het [[saldo]]. De waarde van een machine na de afschrijvingen is de [[boekwaarde]].",
          ["totaal", "eindbalans"], "Twee begrippen uit dit hoofdstuk."),
    klik("Klik op de letter bij de rekening die het geld toont dat de eigenaar in de zaak inbracht.", U, [Z["C"]],
         "100 Kapitaal hoort bij het eigen vermogen en heeft een creditsaldo."),
    tabel("Proefbalans of saldibalans?",
          [("per rekening het totaal in debet en het totaal in credit", "proefbalans"), ("per rekening het verschil tussen debet en credit", "saldibalans"), ("550 Bank: 18 000 en 11 500", "proefbalans"), ("550 Bank: 6 500 in debet", "saldibalans")],
          "De proefbalans geeft de totalen, de saldibalans de verschillen.",
          kolommen=["proefbalans", "saldibalans"]),
    mk("De kas heeft 3 100 euro in debet en 3 400 euro in credit. Wat besluit je?",
       ["Er zit een fout, want een kas kan niet negatief zijn.", "De kas heeft dan gewoon een creditsaldo van 300 euro.", "De zaak heeft deze maand 300 euro meer contant geld gekregen.", "Dat is normaal na het boeken van de afschrijvingen."], 0,
       "Je kan niet meer contant geld uitgeven dan erin zit."),
    inv("Een computer van 1 800 euro wordt over 3 jaar lineair afgeschreven. Wat is de boekwaarde na één jaar? Schrijf enkel het getal.", ["1200"],
        "1 800 gedeeld door 3 is 600 per jaar; 1 800 min 600 is 1 200 euro."),
    keuze("Het verschil tussen de voorlopige en de definitieve proef- en saldibalans zijn [[*de eindejaarsverrichtingen|de beginbalans|de btw-aangiften]].",
          "De voorlopige komt ervoor, de definitieve erna."),
    tabel("Klopt dit over de eindbalans?",
          [("Ze toont de toestand op het einde van het boekjaar.", J), ("Activa en passiva zijn er even groot.", J), ("Ze wordt opgesteld voor de afschrijvingen geboekt zijn.", F)],
          "De eindbalans komt na alle eindejaarsverrichtingen."),
    open_("Een leerling zegt: 'de proefbalans klopt, dus de boekhouding is foutloos'. Heeft hij gelijk? Leg uit met een voorbeeld.",
          "Nee. Als een boeking aan de verkeerde kant van een rekening staat of op een verkeerde rekening, zijn debet en credit nog altijd gelijk. Een kostenrekening met een creditsaldo is zo'n teken. Daarom kijk je ook of elk saldo logisch is.",
          "Gelijke totalen tonen enkel dat debet en credit even groot zijn."),
]
