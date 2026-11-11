"""De balans voor financiële analyse — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import balans_zone

PRENTEN = [
    dict(bestand="balans-velo.svg", zelf=True,
         wat="Balans voor financiële analyse van Velo nv met zeven posten.",
         vragen="klikvragen en rekenvragen over de balans"),
]

VRAGEN = [
    klik(
        "Klik op de balans van Velo nv op de post die samen met het eigen vermogen het permanent vermogen vormt.",
        "balans-velo.svg",
        [balans_zone("vvlt")],
        "Permanent vermogen is het vermogen dat lang in de onderneming blijft: eigen vermogen plus vreemd vermogen op lange termijn.",
    ),
    klik(
        "Klik op de post van de activa die het minst snel in geld omgezet kan worden.",
        "balans-velo.svg",
        [balans_zone("langdurend")],
        "Langdurende activa, zoals gebouwen en machines, blijven jaren in de onderneming.",
    ),
    met_prent("balans-velo.svg", mk(
        "Bekijk de balans van Velo nv. Hoe groot is het permanent vermogen?",
        ["700 000 euro", "450 000 euro", "550 000 euro", "1 000 000 euro"],
        0,
        "450 000 + 250 000 = 700 000 euro.",
    )),
    met_prent("balans-velo.svg", mk(
        "Bekijk de balans van Velo nv. Hoe groot is het nettobedrijfskapitaal?",
        ["100 000 euro", "− 100 000 euro", "400 000 euro", "150 000 euro"],
        0,
        "Permanent vermogen min langdurende activa: 700 000 − 600 000 = 100 000 euro. Of: courante activa min vreemd vermogen op korte termijn, 400 000 − 300 000.",
    )),
    met_prent("balans-velo.svg", tabel(
        "Maak de verticale analyse van de passiva van Velo nv. Welk percentage hoort bij elke post?",
        [
            ("Eigen vermogen", "45 %"),
            ("Vreemd vermogen op lange termijn", "25 %"),
            ("Vreemd vermogen op korte termijn", "30 %"),
        ],
        "Elke post gedeeld door het balanstotaal van 1 000 000 euro.",
        kolommen=["25 %", "30 %", "45 %", "55 %"],
    )),
    met_prent("balans-velo.svg", tabel(
        "Welke uitspraken over Velo nv kan je staven met de balans?",
        [
            ("De langdurende activa zijn volledig gefinancierd met permanent vermogen.", J),
            ("Meer dan de helft van het vermogen komt van schuldeisers.", J),
            ("De liquide middelen volstaan om de schulden op korte termijn te betalen.", F),
            ("Velo nv heeft meer vorderingen dan voorraden.", J),
        ],
        "Permanent vermogen (700 000) is groter dan langdurende activa (600 000). Vreemd vermogen is 550 000 euro. Met 70 000 euro liquide middelen betaal je geen 300 000 euro schulden.",
    )),
    met_prent("balans-velo.svg", mk(
        "Velo nv koopt een nieuwe machine van 120 000 euro en betaalt die met geld van een lening op korte termijn. Wat wordt het nettobedrijfskapitaal?",
        ["− 20 000 euro", "100 000 euro", "220 000 euro", "− 120 000 euro"],
        0,
        "Langdurende activa worden 720 000 euro, het permanent vermogen blijft 700 000 euro. 700 000 − 720 000 = − 20 000 euro.",
    )),
    mk(
        "Een onderneming heeft een negatief nettobedrijfskapitaal. Wat betekent dat?",
        [
            "Een deel van de langdurende activa is gefinancierd met kortlopende schulden",
            "De onderneming heeft meer eigen vermogen dan vreemd vermogen",
            "De courante activa zijn groter dan de schulden op korte termijn",
            "De onderneming maakte dit jaar verlies",
        ],
        0,
        "Het permanent vermogen is kleiner dan de langdurende activa. Dat is riskant: kortlopende schulden moeten snel terugbetaald worden.",
    ),
    sorteer(
        "Hoort de post bij de langdurende activa of bij de courante activa?",
        ["Langdurende activa", "Courante activa"],
        [
            ["Een magazijn in eigendom", "Langdurende activa"],
            ["Handelsvorderingen op klanten", "Courante activa"],
            ["Een vrachtwagen", "Langdurende activa"],
            ["Geld op de zichtrekening", "Courante activa"],
            ["Een vordering die over drie jaar vervalt", "Langdurende activa"],
            ["Voorraad handelsgoederen", "Courante activa"],
        ],
        "Wat langer dan een jaar in de onderneming blijft, is langdurend. Een vordering op meer dan een jaar hoort daar ook bij.",
    ),
    sorteer(
        "Hoort de post bij het permanent vermogen of bij het vreemd vermogen op korte termijn?",
        ["Permanent vermogen", "Vreemd vermogen op korte termijn"],
        [
            ["Kapitaal", "Permanent vermogen"],
            ["Reserves", "Permanent vermogen"],
            ["Een lening die over zes jaar vervalt", "Permanent vermogen"],
            ["Schulden aan leveranciers", "Vreemd vermogen op korte termijn"],
            ["Het deel van een lening dat volgend jaar vervalt", "Vreemd vermogen op korte termijn"],
            ["Te betalen btw", "Vreemd vermogen op korte termijn"],
        ],
        "Het deel van een lange lening dat binnen het jaar vervalt, verhuist naar de korte termijn.",
    ),
    mk(
        "Horizontale analyse: de handelsvorderingen stijgen van 160 000 euro naar 200 000 euro. Hoeveel procent is de stijging?",
        ["25 %", "20 %", "40 %", "80 %"],
        0,
        "(200 000 − 160 000) / 160 000 · 100 = 25 %. Je deelt door het bedrag van het vorige jaar.",
    ),
    mk(
        "Horizontale analyse: een post daalt met 20 % en is nu 64 000 euro. Hoeveel was hij vorig jaar?",
        ["80 000 euro", "76 800 euro", "51 200 euro", "84 000 euro"],
        0,
        "64 000 is 80 % van het vorige bedrag: 64 000 / 0,80 = 80 000 euro.",
    ),
    tabel(
        "Gaat het om een horizontale of een verticale analyse?",
        [
            ("De voorraad is 15 % van het balanstotaal.", "Verticaal"),
            ("Het eigen vermogen steeg met 8 % tegenover vorig jaar.", "Horizontaal"),
            ("De schulden op korte termijn zijn bijna een derde van de passiva.", "Verticaal"),
            ("De omzet daalt al drie jaar op rij.", "Horizontaal"),
        ],
        "Verticaal: een deel van het totaal in één jaar. Horizontaal: een evolutie over de jaren.",
        kolommen=["Horizontaal", "Verticaal"],
    ),
    keuze(
        "Het nettobedrijfskapitaal is het [[*permanent vermogen|eigen vermogen|vreemd vermogen]] min de [[*langdurende activa|courante activa|liquide middelen]].",
        "Hetzelfde getal vind je als courante activa min vreemd vermogen op korte termijn.",
    ),
    mk(
        "Courante activa 520 000 euro, vreemd vermogen op korte termijn 380 000 euro, langdurende activa 900 000 euro. Hoe groot is het permanent vermogen?",
        ["1 040 000 euro", "760 000 euro", "1 420 000 euro", "900 000 euro"],
        0,
        "Nettobedrijfskapitaal 520 000 − 380 000 = 140 000 euro. Permanent vermogen = langdurende activa + NBK = 1 040 000 euro.",
    ),
    tabel(
        "Waar of niet waar?",
        [
            ("Een positief nettobedrijfskapitaal betekent dat er permanent vermogen overblijft voor de courante activa.", J),
            ("Een lening op lange termijn aangaan verhoogt het nettobedrijfskapitaal, als je het geld op de bank laat staan.", J),
            ("Een langdurend actief betalen met geld van de zichtrekening verhoogt het nettobedrijfskapitaal.", F),
        ],
        "Een lening op lange termijn verhoogt het permanent vermogen. Een aankoop van een langdurend actief met liquide middelen verlaagt het nettobedrijfskapitaal.",
    ),
    mk(
        "Bij een verticale analyse is de voorraad 12 % van het balanstotaal van 2 500 000 euro. Hoe groot is de voorraad?",
        ["300 000 euro", "208 333 euro", "30 000 euro", "120 000 euro"],
        0,
        "2 500 000 · 0,12 = 300 000 euro.",
    ),
    sleep(
        "Bij de balans voor analyse herschik je de jaarrekening: de activa in [[langdurende]] en [[courante]] activa, en de passiva in [[permanent]] vermogen en vreemd vermogen op korte termijn.",
        ["liquide", "tijdelijk"],
        "Zo zie je meteen welk vermogen lang in de onderneming blijft en welk snel moet terugbetaald worden.",
    ),
    mk(
        "Waarom zet je bij de balans voor analyse het deel van een lening dat volgend jaar vervalt bij het vreemd vermogen op korte termijn?",
        [
            "Omdat het binnen het jaar terugbetaald moet worden",
            "Omdat het een kost is van het volgende jaar",
            "Omdat leningen nooit bij het permanent vermogen horen",
            "Omdat de bank dat zo vraagt",
        ],
        0,
        "Voor de analyse telt wanneer het geld terug moet, niet hoe het oorspronkelijk geleend werd.",
    ),
    koppel(
        "Welke berekening hoort bij elk resultaat, met de balans van Velo nv?",
        [
            ["450 000 + 250 000", "Permanent vermogen"],
            ["250 000 + 300 000", "Vreemd vermogen"],
            ["150 000 + 180 000 + 70 000", "Courante activa"],
            ["700 000 − 600 000", "Nettobedrijfskapitaal"],
        ],
        ["Eigen vermogen"],
        "Telkens dezelfde posten, anders gegroepeerd.",
    ),
    inv(
        "Horizontale analyse: het eigen vermogen stijgt van 400 000 euro naar 450 000 euro. Hoeveel procent is de stijging? Schrijf het getal met een komma.",
        "12,5",
        "50 000 / 400 000 · 100 = 12,5 %.",
    ),
    mk(
        "Bij een verticale analyse stijgt het aandeel van het vreemd vermogen op korte termijn van 20 % naar 35 %, bij een gelijk balanstotaal. Wat besluit je?",
        [
            "De onderneming steunt meer op schulden die snel terug moeten",
            "De onderneming werd rendabeler in de loop van het jaar en verdiende meer",
            "Het eigen vermogen is zeker gestegen",
            "De onderneming verkocht een deel van haar machines",
        ],
        0,
        "Een groter deel van de financiering moet binnen het jaar terugbetaald worden. Dat drukt op de liquiditeit.",
    ),
    tabel(
        "Een onderneming betaalt een leverancier van 50 000 euro met geld van de bank. Wat gebeurt er?",
        [
            ("De courante activa dalen met 50 000 euro.", J),
            ("Het vreemd vermogen op korte termijn daalt met 50 000 euro.", J),
            ("Het nettobedrijfskapitaal verandert niet.", J),
            ("Het permanent vermogen daalt.", F),
        ],
        "Beide kanten van het nettobedrijfskapitaal dalen evenveel: het verschil blijft gelijk.",
    ),
    met_prent("balans-velo.svg", mk(
        "Velo nv verkoopt voorraad die 50 000 euro kostte, contant en aan kostprijs. Wat gebeurt er met het nettobedrijfskapitaal?",
        [
            "Het blijft 100 000 euro",
            "Het stijgt naar 150 000 euro",
            "Het daalt naar 50 000 euro",
            "Het stijgt naar 120 000 euro",
        ],
        0,
        "De voorraad daalt en de liquide middelen stijgen evenveel. De courante activa blijven 400 000 euro.",
    )),
    volgorde(
        "Rangschik de activa van Velo nv van minst naar meest liquide.",
        ["Langdurende activa", "Voorraden", "Vorderingen op ten hoogste een jaar", "Liquide middelen"],
        "Een voorraad moet eerst verkocht worden, een vordering enkel nog geïnd. Liquide middelen zijn al geld.",
    ),
    mk(
        "Een onderneming heeft langdurende activa van 800 000 euro, eigen vermogen 300 000 euro en vreemd vermogen op lange termijn 400 000 euro. Wat is het grootste probleem?",
        [
            "100 000 euro langdurende activa zijn met kortlopende schulden gefinancierd",
            "Er is te veel eigen vermogen tegenover het vreemd vermogen op lange termijn",
            "Het nettobedrijfskapitaal is te groot",
            "De onderneming heeft geen langdurende activa nodig",
        ],
        0,
        "Permanent vermogen 700 000 euro tegenover 800 000 euro langdurende activa: het nettobedrijfskapitaal is − 100 000 euro.",
    ),
    open_(
        "Leg uit waarom langdurende activa gefinancierd horen te worden met permanent vermogen.",
        "Langdurende activa blijven jaren in de onderneming en worden maar langzaam terugverdiend. Als je ze met kortlopende schulden betaalt, moet je die schulden terugbetalen voor de activa het geld hebben opgebracht. Permanent vermogen blijft lang genoeg ter beschikking.",
        "De looptijd van de financiering moet passen bij hoe lang het geld vastzit.",
    ),
    casus(
        "Balans van Bakker bv (in euro). Vorig jaar: langdurende activa 500 000, courante activa 300 000, eigen vermogen 320 000, vreemd vermogen lange termijn 200 000, vreemd vermogen korte termijn 280 000. Dit jaar: langdurende activa 560 000, courante activa 340 000, eigen vermogen 360 000, vreemd vermogen lange termijn 180 000, vreemd vermogen korte termijn 360 000.",
        [
            mk(
                "Hoe evolueerde het nettobedrijfskapitaal?",
                [
                    "Van 20 000 euro naar − 20 000 euro",
                    "Van 20 000 euro naar 60 000 euro",
                    "Van − 20 000 euro naar 20 000 euro",
                    "Het bleef 20 000 euro",
                ],
                0,
                "Vorig jaar 300 000 − 280 000 = 20 000 euro. Dit jaar 340 000 − 360 000 = − 20 000 euro.",
            ),
            mk(
                "Welk percentage van de passiva is dit jaar eigen vermogen?",
                ["40 %", "36 %", "45 %", "60 %"],
                0,
                "Balanstotaal 900 000 euro. 360 000 / 900 000 · 100 = 40 %.",
            ),
            mk(
                "Met hoeveel procent stegen de langdurende activa?",
                ["12 %", "10,7 %", "60 %", "6 %"],
                0,
                "(560 000 − 500 000) / 500 000 · 100 = 12 %.",
            ),
        ],
    ),
]
