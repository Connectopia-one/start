"""De vraagcurve en de prijselasticiteit van de vraag — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G = venster("vraag-bewegen-verschuiven", 0, 24, 0, 14, 2, 2)
PUNTEN = {"A": (8, 6), "B": (12, 4), "C": (14, 6), "D": (4, 8)}

GRAFIEKEN = [
    dict(naam=G, titel="Vraag naar koffie: V1 en V2",
         krommen=[(lambda q: 10 - 0.5 * q, "groen", "V1", (0, 20)), (lambda q: 13 - 0.5 * q, "blauw", "V2", (0, 24))],
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="hoeveelheid", ylabel="prijs", ijk_x=4, ijk_y=2),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen over bewegen op en verschuiven van de vraagcurve")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "De markt staat in punt A. Koffie is een normaal goed en het inkomen van de consumenten stijgt, terwijl de prijs gelijk blijft. Klik op het nieuwe punt.",
        P, [punt_zone(G, *PUNTEN["C"])],
        "Een hoger inkomen verschuift de hele vraagcurve naar rechts: van V1 naar V2, bij dezelfde prijs van 6.",
    ),
    klik(
        "De markt staat in punt A. De prijs van koffie stijgt, en verder verandert er niets. Klik op het nieuwe punt.",
        P, [punt_zone(G, *PUNTEN["D"])],
        "Verandert de prijs van het goed zelf, dan beweeg je op dezelfde curve: van A naar D op V1.",
    ),
    met_prent(P, mk(
        "Van A naar B: wat is er gebeurd?",
        ["De prijs van koffie daalde: een beweging op de vraagcurve",
         "Het inkomen steeg: een verschuiving van de vraagcurve naar rechts",
         "Thee werd goedkoper: een verschuiving naar links",
         "Koffie raakte uit de mode: een verschuiving naar links"],
        0,
        "A en B liggen op dezelfde curve V1. Enkel de prijs van koffie zelf veranderde.",
    )),
    met_prent(P, tabel(
        "Welke verandering geeft een beweging van A naar C, welke een beweging van A naar B, en welke past bij geen van beide?",
        [
            ("Een grote reclamecampagne voor koffie", "Van A naar C"),
            ("Koffie wordt goedkoper", "Van A naar B"),
            ("Het inkomen daalt (koffie is een normaal goed)", "Geen van beide"),
            ("Thee, een substituut, wordt duurder", "Van A naar C"),
        ],
        "Reclame en een duurder substituut verschuiven de curve naar rechts. Een lager inkomen verschuift ze naar links, en dat punt staat niet op de tekening.",
        kolommen=["Van A naar C", "Van A naar B", "Geen van beide"],
    )),
    met_prent(P, inv(
        "Bereken de prijselasticiteit van de vraag op V1 van A (prijs 6, hoeveelheid 8) naar B (prijs 4, hoeveelheid 12), met A als vertrekpunt. Schrijf het getal met een komma.",
        "-1,5",
        "Hoeveelheid: +4 / 8 = +50 %. Prijs: −2 / 6 = −33,3 %. E = 50 / −33,3 = −1,5.",
    )),
    tabel(
        "Bereken de prijselasticiteit van de vraag.",
        [
            ("Prijs +10 %, hoeveelheid −5 %", "−0,5"),
            ("Prijs −20 %, hoeveelheid +30 %", "−1,5"),
            ("Prijs +4 %, hoeveelheid −4 %", "−1"),
        ],
        "E = procentuele verandering van de hoeveelheid / procentuele verandering van de prijs.",
        kolommen=["−0,5", "−1", "−1,5", "−2"],
    ),
    mk(
        "De prijs van een concertticket daalt van 50 naar 40 euro en de verkoop stijgt van 2 000 naar 2 600 tickets. Hoe groot is de prijselasticiteit?",
        ["−1,5", "−0,67", "−0,3", "−3"],
        0,
        "Hoeveelheid +600 / 2 000 = +30 %. Prijs −10 / 50 = −20 %. E = 30 / −20 = −1,5.",
    ),
    inv(
        "De prijselasticiteit van de vraag is −0,4 en de prijs stijgt met 15 %. Met hoeveel procent daalt de gevraagde hoeveelheid? Schrijf enkel het getal.",
        "6",
        "−0,4 · 15 = −6 %: de hoeveelheid daalt met 6 %.",
    ),
    mk(
        "Een bioscoop verhoogt de ticketprijs en ziet dat de omzet daalt. Wat besluit je over de vraag?",
        ["De vraag is elastisch: |E| is groter dan 1", "De vraag is inelastisch: |E| is kleiner dan 1",
         "De vraag is perfect inelastisch: E = 0", "De vraag is unitair elastisch: E = −1"],
        0,
        "Bij een elastische vraag daalt de hoeveelheid procentueel sterker dan de prijs stijgt, dus de omzet daalt.",
    ),
    tabel(
        "De prijs stijgt. Wat gebeurt er met de omzet?",
        [
            ("Elasticiteit −2,5", "Daalt"),
            ("Elasticiteit −0,3", "Stijgt"),
            ("Elasticiteit −1", "Blijft ongeveer gelijk"),
            ("Elasticiteit 0", "Stijgt"),
        ],
        "Elastisch: omzet daalt. Inelastisch of perfect inelastisch: omzet stijgt. Unitair: ongeveer gelijk.",
        kolommen=["Stijgt", "Daalt", "Blijft ongeveer gelijk"],
    ),
    mk(
        "Een leerling zegt: 'Een perfect inelastische vraag heeft een elasticiteit van −1.' Wat klopt?",
        ["Fout: een perfect inelastische vraag heeft elasticiteit 0 en een verticale curve",
         "Juist: −1 is de laagste waarde die een prijselasticiteit van de vraag kan hebben",
         "Fout: een perfect inelastische vraag heeft een horizontale curve en E is oneindig",
         "Juist: bij −1 reageert de hoeveelheid helemaal niet"],
        0,
        "Bij E = 0 verandert de hoeveelheid niet, wat de prijs ook doet. E = −1 is unitair elastisch.",
    ),
    sorteer(
        "Is de vraag eerder elastisch of eerder inelastisch?",
        ["Eerder elastisch", "Eerder inelastisch"],
        [
            ["Een merk frisdrank met veel concurrenten in de winkel", "Eerder elastisch"],
            ["Insuline voor een diabetespatiënt", "Eerder inelastisch"],
            ["Een citytrip naar Rome", "Eerder elastisch"],
            ["Zout", "Eerder inelastisch"],
            ["Sigaretten voor een verslaafde roker", "Eerder inelastisch"],
            ["Benzine op lange termijn, als mensen een zuinigere auto kunnen kopen", "Eerder elastisch"],
        ],
        "Veel alternatieven, luxe, een groot deel van het budget en lange termijn maken de vraag elastischer.",
    ),
    mk(
        "Waarom brengt een hogere accijns op sigaretten de overheid veel geld op?",
        ["De vraag is inelastisch, dus rokers blijven grotendeels kopen",
         "De vraag is elastisch, dus rokers kopen meer als de prijs stijgt",
         "De vraag is perfect elastisch, dus de prijs blijft gelijk",
         "Rokers schakelen massaal over naar een goedkoper substituut"],
        0,
        "Door het verslavingseffect daalt de hoeveelheid maar weinig, dus de ontvangsten stijgen.",
    ),
    keuze(
        "Bij dezelfde schaal wijst een [[*steilere|vlakkere]] vraagcurve op een [[*minder|meer]] elastische vraag.",
        "Bij een steile curve verandert de hoeveelheid weinig bij een prijsverandering.",
    ),
    mk(
        "Een producent heeft heel veel concurrenten met precies hetzelfde product. Hoe ziet zijn vraagcurve eruit?",
        ["Horizontaal: perfect elastisch", "Verticaal: perfect inelastisch", "Steil dalend: inelastisch", "Stijgend: hoe duurder, hoe meer"],
        0,
        "Vraagt hij meer dan de marktprijs, dan verliest hij al zijn klanten.",
    ),
    casus(
        "Op de markt van speculoos zijn er drie kopers. Bij 4 euro per pak vraagt An 3 pakken, Bram 5 en Charlotte 2. Bij 3 euro vraagt An 4 pakken, Bram 7 en Charlotte 3.",
        [
            inv("Hoe groot is de collectieve vraag bij 3 euro? Schrijf enkel het getal.", "14",
                "4 + 7 + 3 = 14 pakken."),
            mk("Hoe groot is de prijselasticiteit van de collectieve vraag van 4 naar 3 euro, met 4 euro als vertrekpunt?",
               ["−1,6", "−0,4", "−1", "−2,5"], 0,
               "Hoeveelheid van 10 naar 14: +40 %. Prijs van 4 naar 3: −25 %. E = 40 / −25 = −1,6."),
            mk("Wat gebeurt er met de omzet van de verkopers bij die prijsdaling?",
               ["Ze stijgt van 40 naar 42 euro", "Ze daalt van 40 naar 36 euro, want de prijs daalt", "Ze blijft 40 euro", "Ze daalt van 42 naar 40 euro"], 0,
               "4 · 10 = 40 euro en 3 · 14 = 42 euro. Bij een elastische vraag doet een prijsdaling de omzet stijgen."),
        ],
    ),
    sleep(
        "De collectieve vraagcurve vind je door bij elke [[prijs]] de gevraagde [[hoeveelheden]] van alle consumenten [[op te tellen]].",
        ["te vermenigvuldigen", "inkomens", "kosten"],
        "Je telt horizontaal op: per prijs de hoeveelheden.",
    ),
    tabel(
        "De vraagcurve van een normaal goed: verschuift ze naar rechts of naar links?",
        [
            ("Het inkomen van de consumenten daalt", "Naar links"),
            ("De prijs van een complementair goed daalt", "Naar rechts"),
            ("Het goed raakt uit de mode", "Naar links"),
            ("De prijs van een substituut daalt", "Naar links"),
        ],
        "Een goedkoper complementair goed (zoals printers voor inkt) doet de vraag stijgen. Een goedkoper substituut doet ze dalen.",
        kolommen=["Naar rechts", "Naar links"],
    ),
    mk(
        "De prijs van printers daalt sterk. Wat gebeurt er op de markt van inktpatronen?",
        ["De vraagcurve van inkt verschuift naar rechts", "Je beweegt op de vraagcurve van inkt naar een lagere prijs",
         "De vraagcurve van inkt verschuift naar links", "Er verandert niets, want inkt is een ander goed"],
        0,
        "Printers en inkt zijn complementair: meer printers betekent meer vraag naar inkt bij elke prijs.",
    ),
    mk(
        "Hoe leid je de individuele vraagcurve af?",
        ["Uit de optimale goederencombinatie van één consument, terwijl je de prijs van het goed laat veranderen",
         "Door de vraag van alle consumenten bij elke prijs op te tellen en dat totaal te delen door het aantal consumenten",
         "Uit de marginale kosten van alle producenten van het goed bij verschillende mogelijke marktprijzen",
         "Door het inkomen van de consument te laten veranderen bij een vaste prijs van het goed"],
        0,
        "Bij elke prijs noteer je hoeveel de consument kiest: dat geeft de punten van zijn vraagcurve.",
    ),
    inv(
        "De prijselasticiteit van de vraag is −1,5. De prijs daalt met 8 %. Met hoeveel procent stijgt de gevraagde hoeveelheid? Schrijf enkel het getal.",
        "12",
        "−1,5 · −8 = +12 %.",
    ),
    mk(
        "Een busmaatschappij verlaagt haar prijs met 10 %, en het aantal reizigers stijgt met 4 %. Wat gebeurt er met de omzet?",
        ["Ze daalt, want de vraag is inelastisch", "Ze stijgt, want de vraag is elastisch",
         "Ze blijft gelijk, want de vraag is unitair elastisch", "Ze stijgt, want er zijn meer reizigers"],
        0,
        "E = 4 / −10 = −0,4: inelastisch. Een prijsdaling doet de omzet dan dalen.",
    ),
    tabel(
        "Waar of niet waar over de prijselasticiteit van de vraag?",
        [
            ("De uitkomst is meestal negatief.", J),
            ("Een elasticiteit van −0,2 betekent een elastische vraag.", F),
            ("Op lange termijn is de vraag meestal elastischer dan op korte termijn.", J),
            ("Bij een perfect elastische vraag is de curve verticaal.", F),
        ],
        "Prijs en hoeveelheid bewegen tegengesteld. −0,2 is inelastisch. Perfect elastisch is horizontaal.",
    ),
    volgorde(
        "Zet de stappen om de prijselasticiteit van de vraag te berekenen in de juiste volgorde.",
        ["De procentuele verandering van de hoeveelheid berekenen", "De procentuele verandering van de prijs berekenen",
         "De eerste delen door de tweede", "Het resultaat duiden: elastisch, inelastisch of unitair"],
        "Eerst de twee percentages, dan de deling, dan de betekenis.",
    ),
    koppel(
        "Welke curve hoort bij welke elasticiteit?",
        [
            ["Verticale vraagcurve", "Perfect inelastisch"],
            ["Horizontale vraagcurve", "Perfect elastisch"],
            ["De omzet blijft ongeveer gelijk als de prijs verandert", "Unitair elastisch"],
        ],
        ["Inferieur"],
        "E = 0 is verticaal, E oneindig is horizontaal, |E| = 1 houdt de omzet ongeveer gelijk.",
    ),
    open_(
        "Een gemeente wil met een hogere parkeerprijs minder auto's in het centrum. Leg uit waarom dat op korte termijn minder goed werkt dan op lange termijn.",
        "Op korte termijn hebben mensen weinig alternatieven en is de vraag inelastisch. Op lange termijn kunnen ze zich aanpassen (fiets, bus, elders winkelen), dus de vraag wordt elastischer en daalt het aantal auto's sterker.",
    ),
    mk(
        "Een leerling zegt: 'Als het inkomen van de consumenten daalt, beweeg je op de vraagcurve van een normaal goed naar links.' Wat klopt?",
        ["Fout: de hele vraagcurve verschuift naar links, want het inkomen is niet de prijs van het goed zelf",
         "Juist: een lager inkomen doet de gevraagde hoeveelheid dalen, en dat is een beweging op de curve",
         "Fout: je beweegt op de curve naar rechts, want het goed wordt relatief goedkoper voor de consument",
         "Juist: alleen bij een verandering van de reclame of de mode verschuift de hele vraagcurve"],
        0,
        "Enkel een verandering van de prijs van het goed zelf geeft een beweging op de curve. Al de rest verschuift de curve.",
    ),
    keuze(
        "Als de prijs van boter stijgt, [[*stijgt|daalt]] de vraag naar margarine, want het zijn [[*substituten|complementaire goederen]].",
        "Een duurder substituut doet de vraagcurve van het andere goed naar rechts verschuiven.",
    ),
]
