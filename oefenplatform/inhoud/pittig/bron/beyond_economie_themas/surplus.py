"""Consumenten- en producentensurplus en het welvaartsoptimum — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, vak_zone, punt_zone

G = venster("surplus-twee-vlakken", 0, 90, 0, 100, 10, 10)

GRAFIEKEN = [
    dict(naam=G, titel="Markt van fietslampjes: vraag P = 90 − Q, aanbod P = 30 + 0,5Q",
         vlakken=[(lambda q: 90 - q, 0, 40, "#b5651d", lambda q: 50), (lambda q: 50, 0, 40, "#7a4b8c", lambda q: 30 + 0.5 * q)],
         krommen=[(lambda q: 90 - q, "groen", "V", (0, 85)), (lambda q: 30 + 0.5 * q, "blauw", "A", (0, 90))],
         stippel=[("h", 50)],
         punten=[(40, 50, "E")],
         xlabel="hoeveelheid", ylabel="prijs", ijk_x=10, ijk_y=10),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat="Vraag en aanbod met twee gekleurde vlakken (oranje en paars)", vragen="klikvragen en rekenvragen over het surplus")]
P = f"{G}.svg"

# Het oranje vlak (CS) ligt tussen prijs 50 en de vraagcurve, het paarse (PS) tussen de aanbodcurve en prijs 50.
CS_ZONE = vak_zone(G, 0, 25, 51, 65)
PS_ZONE = vak_zone(G, 0, 20, 41, 49.5)

VRAGEN = [
    klik(
        "Klik op het vlak dat het consumentensurplus voorstelt.",
        P, [CS_ZONE],
        "Het consumentensurplus ligt onder de vraagcurve en boven de marktprijs: het oranje vlak.",
    ),
    klik(
        "Klik op het vlak dat het producentensurplus voorstelt.",
        P, [PS_ZONE],
        "Het producentensurplus ligt boven de aanbodcurve en onder de marktprijs: het paarse vlak.",
    ),
    klik(
        "In welk punt is de totale welvaart op deze markt het grootst? Klik erop.",
        P, [punt_zone(G, 40, 50)],
        "Bij volkomen concurrentie is de totale welvaart het grootst in het marktevenwicht E.",
    ),
    met_prent(P, inv(
        "Bereken het consumentensurplus op deze markt. Schrijf enkel het getal.",
        "800",
        "Evenwicht: 90 − Q = 30 + 0,5Q, dus Q = 40 en P = 50. CS = ½ · 40 · (90 − 50) = 800.",
    )),
    met_prent(P, inv(
        "Bereken het producentensurplus op deze markt. Schrijf enkel het getal.",
        "400",
        "PS = ½ · 40 · (50 − 30) = 400.",
    )),
    met_prent(P, mk(
        "Hoe groot is de totale welvaart op deze markt?",
        ["1 200", "800", "2 000", "3 600"],
        0,
        "Totale welvaart = CS + PS = 800 + 400 = 1 200.",
    )),
    casus(
        "Op de markt van rugzakken is de vraag Qv = 150 − 3P en het aanbod Qa = 2P − 20.",
        [
            inv("Bereken de evenwichtsprijs. Schrijf enkel het getal.", "34",
                "150 − 3P = 2P − 20, dus 5P = 170 en P = 34."),
            inv("Bereken de evenwichtshoeveelheid. Schrijf enkel het getal.", "48",
                "Qv = 150 − 3 · 34 = 48."),
            mk("Bij welke prijs wil niemand nog rugzakken kopen?",
               ["50", "34", "10", "150"], 0,
               "Qv = 0 als 150 = 3P, dus P = 50."),
            inv("Bereken het consumentensurplus. Schrijf enkel het getal.", "384",
                "CS = ½ · 48 · (50 − 34) = 384."),
            inv("Bereken het producentensurplus. Het aanbod is nul bij een prijs van 10. Schrijf enkel het getal.", "576",
                "PS = ½ · 48 · (34 − 10) = 576."),
        ],
    ),
    mk(
        "Je wilt maximaal 25 euro betalen voor een festivalticket en je koopt het voor 18 euro. Hoe groot is jouw consumentensurplus?",
        ["7 euro", "18 euro", "25 euro", "43 euro"],
        0,
        "Consumentensurplus = maximale betalingsbereidheid − marktprijs = 25 − 18 = 7 euro.",
    ),
    mk(
        "Een kunstenaar wil een schilderij minimaal voor 300 euro verkopen en krijgt er 420 euro voor. Wat is zijn producentensurplus?",
        ["120 euro", "420 euro", "300 euro", "720 euro"],
        0,
        "Producentensurplus = marktprijs − minimale verkoopprijs = 420 − 300 = 120 euro.",
    ),
    tabel(
        "Waar of niet waar over consumenten- en producentensurplus?",
        [
            ("Het producentensurplus is hetzelfde als de winst van de producenten.", F),
            ("Een consument die net de marktprijs wil betalen, heeft een surplus van nul.", J),
            ("Het consumentensurplus is het bedrag dat consumenten aan producenten betalen.", F),
            ("Op een markt zonder overheid is de totale welvaart de som van CS en PS.", J),
        ],
        "Van het producentensurplus zijn de vaste kosten niet afgetrokken, dus het is geen winst. Wat consumenten betalen is de uitgave, niet het surplus.",
    ),
    mk(
        "Wie gebruikte het begrip consumentensurplus als eerste?",
        ["Alfred Marshall", "Adam Smith", "Vilfredo Pareto", "John Maynard Keynes"],
        0,
        "Alfred Marshall introduceerde het begrip consumentensurplus.",
    ),
    tabel(
        "Wat gebeurt er met het surplus?",
        [
            ("De marktprijs daalt en er wordt meer verhandeld: het consumentensurplus ...", "Stijgt"),
            ("De vraagcurve verschuift naar rechts: het producentensurplus ...", "Stijgt"),
            ("De aanbodcurve verschuift naar links: de totale welvaart ...", "Daalt"),
            ("De marktprijs stijgt: het consumentensurplus ...", "Daalt"),
        ],
        "Een lagere prijs is goed voor de kopers, een hogere vraag goed voor de verkopers. Minder aanbod doet de totale welvaart meestal dalen.",
        kolommen=["Stijgt", "Daalt"],
    ),
    mk(
        "Een nieuwe techniek maakt de productie van zonnepanelen veel goedkoper, waardoor het aanbod stijgt. Wie kan daar meer surplus door krijgen?",
        ["Zowel de consumenten als de producenten", "Enkel de producenten, want hun kosten dalen",
         "Enkel de consumenten, want de prijs daalt", "Niemand, want de totale welvaart blijft altijd gelijk"],
        0,
        "Een technologische vooruitgang die het aanbod vergroot, kan beide groepen meer surplus geven.",
    ),
    mk(
        "De marktprijs ligt boven de evenwichtsprijs. Waarom gaat er welvaart verloren?",
        ["Er vinden ruilen niet plaats waarbij koper en verkoper allebei voordeel zouden hebben",
         "De producenten verdienen minder per stuk dan in het marktevenwicht, dus PS daalt altijd",
         "De consumenten betalen meer, en dat geld verdwijnt uit de economie zonder dat iemand het krijgt",
         "Er wordt meer verhandeld dan in het evenwicht, waardoor er te veel geproduceerd wordt"],
        0,
        "Bij een te hoge prijs wordt er minder verhandeld. De ruilen die niet doorgaan, waren voor beide partijen voordelig.",
    ),
    tabel(
        "Is dit een Pareto-verbetering?",
        [
            ("Anna krijgt er 5 euro bij en niemand verliest iets.", "Wel"),
            ("Bram wint 100 euro, Charlotte verliest 1 euro.", "Niet"),
            ("Twee buren ruilen vrijwillig hun fiets, en allebei vinden ze het beter zo.", "Wel"),
            ("Iedereen behalve één persoon gaat erop vooruit; die ene verliest een beetje.", "Niet"),
        ],
        "Een Pareto-verbetering maakt minstens één persoon beter af zonder iemand slechter af te maken.",
        kolommen=["Wel", "Niet"],
    ),
    mk(
        "Wat is een Pareto-optimum?",
        ["Een toestand waarin niemand beter kan worden zonder dat iemand anders slechter wordt",
         "Een toestand waarin de welvaart zo eerlijk mogelijk over iedereen verdeeld is",
         "Een toestand waarin de producenten de grootst mogelijke winst halen op de markt",
         "Een toestand waarin de overheid de prijs vastlegt op het niveau van de laagste kosten"],
        0,
        "Pareto-optimaal betekent efficiënt: er is geen verbetering meer mogelijk zonder dat iemand verliest.",
    ),
    mk(
        "Een leerling zegt: 'Elk Pareto-optimum is ook rechtvaardig.' Wat klopt?",
        ["Fout: ook een zeer ongelijke verdeling kan Pareto-efficiënt zijn",
         "Juist: in een Pareto-optimum heeft iedereen evenveel welvaart, anders kan het beter",
         "Fout: een Pareto-optimum komt bij volkomen concurrentie nooit voor, enkel bij een monopolie",
         "Juist: daarom grijpt de overheid nooit in als een markt in een Pareto-optimum is"],
        0,
        "Efficiëntie zegt niets over hoe eerlijk de welvaart verdeeld is.",
    ),
    keuze(
        "Bij volkomen concurrentie is het marktevenwicht [[*wel|geen]] Pareto-optimum, en is de totale welvaart daar het [[*grootst|kleinst]].",
        "In het evenwicht worden alle voordelige ruilen gedaan.",
    ),
    mk(
        "Wat bedoelde Adam Smith met de onzichtbare hand?",
        ["Wie zijn eigenbelang volgt, dient via de markt ook het algemeen belang",
         "De overheid moet overal ongemerkt ingrijpen om de prijzen eerlijk te houden",
         "Grote bedrijven sturen in het geheim de prijzen op de markt",
         "Consumenten kopen zonder het te beseffen altijd het goedkoopste product"],
        0,
        "Volgens Smith zorgt de markt voor het welvaartsoptimum, niet een overheid die overal ingrijpt.",
    ),
    sleep(
        "Het consumentensurplus ligt [[onder]] de vraagcurve en [[boven]] de marktprijs. Het producentensurplus ligt [[boven]] de aanbodcurve en [[onder]] de marktprijs.",
        ["naast", "op"],
        "Teken het voor jezelf: CS is de driehoek bovenaan, PS de driehoek eronder.",
    ),
    mk(
        "De marktprijs is 40, de vraagcurve snijdt de prijsas bij 70 en er worden 24 stuks verhandeld. Hoe groot is het consumentensurplus?",
        ["360", "720", "480", "960"],
        0,
        "CS = ½ · 24 · (70 − 40) = 360.",
    ),
    open_(
        "Leg in je eigen woorden uit waarom het producentensurplus niet hetzelfde is als de winst van een bedrijf.",
        "Het producentensurplus is het verschil tussen de marktprijs en de minimumprijs waarvoor de producent wil verkopen. Daar zijn de vaste kosten niet van afgetrokken. De winst houdt wel rekening met alle kosten, ook de vaste.",
    ),
    mk(
        "De marktprijs is 30, de aanbodcurve snijdt de prijsas bij 12 en er worden 50 stuks verhandeld. Hoe groot is het producentensurplus?",
        ["450", "900", "750", "300"],
        0,
        "PS = ½ · 50 · (30 − 12) = 450.",
    ),
    volgorde(
        "Zet de stappen om het consumentensurplus te berekenen bij rechte curven in de juiste volgorde.",
        ["Het evenwicht berekenen: vraag gelijk aan aanbod", "De prijs zoeken waarbij de vraag nul wordt",
         "De hoogte bepalen: die prijs min de marktprijs", "½ · hoeveelheid · hoogte uitrekenen"],
        "Eerst het evenwicht, dan het snijpunt met de prijsas, dan de hoogte, en dan de oppervlakte van de driehoek.",
    ),
    koppel(
        "Koppel elk begrip aan zijn omschrijving.",
        [
            ["Consumentensurplus", "Maximale betalingsbereidheid min marktprijs"],
            ["Producentensurplus", "Marktprijs min minimale verkoopprijs"],
            ["Totale welvaart", "Consumentensurplus plus producentensurplus"],
            ["Pareto-verbetering", "Minstens één persoon beter af, niemand slechter af"],
        ],
        ["Marktprijs maal verhandelde hoeveelheid"],
        "Prijs maal hoeveelheid is de omzet, geen surplus.",
    ),
    open_(
        "Een student zegt: 'In het marktevenwicht winnen enkel de verkopers, want zij krijgen het geld.' Leg uit waarom dat niet klopt.",
        "Ook consumenten winnen: wie meer wilde betalen dan de marktprijs, heeft een consumentensurplus. In het evenwicht winnen dus de kopers die meer wilden betalen en de verkopers die voor minder wilden verkopen.",
    ),
]
