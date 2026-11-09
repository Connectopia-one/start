"""Investeringen, leningen, lonen en btw boeken — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import kaart_zone

SYNTHESE = [
    ("Brutolonen", "20 000,00", False),
    ("RSZ werknemers (13,07 %)", "− 2 614,00", False),
    ("Belastbaar loon", "17 386,00", False),
    ("Bedrijfsvoorheffing", "− 3 900,00", False),
    ("Nettolonen", "13 486,00", True),
    ("Al betaald voorschot arbeiders", "− 4 000,00", False),
    ("Nog uit te betalen", "9 486,00", True),
    ("RSZ werkgever (25 %)", "5 000,00", False),
]
N = len(SYNTHESE)

PRENTEN = [
    dict(bestand="loonsynthese.svg", zelf=True,
         wat="Loonsynthese van een maand met brutolonen, RSZ, bedrijfsvoorheffing, nettolonen, voorschot en werkgeversbijdrage.",
         vragen="klikvraag, tabel en meerkeuze over de loonsynthese"),
]

VRAGEN = [
    klik(
        "Klik op de loonsynthese op de regel met een bedrag dat de werkgever betaalt bovenop het brutoloon.",
        "loonsynthese.svg",
        [kaart_zone(7, N)],
        "De werkgeversbijdrage voor de RSZ is een extra kost voor de werkgever. Ze gaat niet van het loon van de werknemer af.",
    ),
    met_prent("loonsynthese.svg", sorteer(
        "Bekijk de loonsynthese. Staat elk bedrag debet of credit in de boeking van de loonsynthese?",
        ["Debet", "Credit"],
        [
            ["62 Bezoldigingen, 20 000 euro", "Debet"],
            ["62 Werkgeversbijdragen RSZ, 5 000 euro", "Debet"],
            ["454 RSZ, 7 614 euro", "Credit"],
            ["453 Bedrijfsvoorheffing, 3 900 euro", "Credit"],
            ["455 Bezoldigingen, 13 486 euro", "Credit"],
        ],
        "Brutoloon en werkgeversbijdrage zijn kosten. Aan de RSZ, de fiscus en het personeel is de werkgever geld schuldig.",
    )),
    met_prent("loonsynthese.svg", mk(
        "Bekijk de loonsynthese. Hoeveel is de werkgever in totaal aan de RSZ schuldig voor maart?",
        ["7 614 euro", "2 614 euro", "5 000 euro", "11 514 euro"],
        0,
        "De bijdrage van de werknemers (2 614 euro, ingehouden) plus die van de werkgever (5 000 euro).",
    )),
    met_prent("loonsynthese.svg", mk(
        "Bekijk de loonsynthese. Wat kost het personeel van maart de werkgever in totaal?",
        ["25 000 euro", "20 000 euro", "13 486 euro", "29 486 euro"],
        0,
        "Brutolonen plus werkgeversbijdrage: 20 000 + 5 000 = 25 000 euro. RSZ en voorheffing van de werknemer zitten al in het brutoloon.",
    )),
    met_prent("loonsynthese.svg", tabel(
        "Welke uitspraken over de loonsynthese kloppen?",
        [
            ("De bedrijfsvoorheffing wordt berekend op het loon na de RSZ van de werknemer.", J),
            ("Het voorschot van 4 000 euro is een extra kost.", F),
            ("Op het einde van de maand gaat er nog 9 486 euro naar het personeel.", J),
            ("De RSZ van de werknemers betaalt de werkgever uit eigen zak.", F),
        ],
        "Het voorschot is een deel van het loon dat al vooraf betaald is. De RSZ van de werknemer wordt van zijn loon ingehouden.",
    )),
    mk(
        "Brutoloon 3 200 euro, RSZ werknemer 13,07 %, bedrijfsvoorheffing 520 euro. Wat is het nettoloon?",
        ["2 261,76 euro", "2 680,00 euro", "2 781,76 euro", "2 362,56 euro"],
        0,
        "RSZ: 3 200 · 0,1307 = 418,24 euro. 3 200 − 418,24 − 520 = 2 261,76 euro.",
    ),
    mk(
        "Een arbeider kreeg halverwege de maand 700 euro voorschot. Zijn nettoloon is 1 850 euro. Hoeveel krijgt hij op het einde van de maand?",
        ["1 150 euro", "1 850 euro", "2 550 euro", "700 euro"],
        0,
        "Het voorschot wordt van het nettoloon afgetrokken: 1 850 − 700 = 1 150 euro.",
    ),
    tabel(
        "Het voorschot aan de arbeiders wordt via de bank betaald. Hoe boek je elke rekening?",
        [
            ("455 Bezoldigingen", "Debet"),
            ("55000 Kredietinstellingen", "Credit"),
            ("62 Bezoldigingen", "Geen van beide"),
        ],
        "Het voorschot verlaagt vooraf de schuld aan het personeel en de bank daalt. De kost komt pas in de loonsynthese.",
        kolommen=["Debet", "Credit", "Geen van beide"],
    ),
    inv(
        "Te betalen btw 15 200 euro, terug te vorderen btw 11 700 euro. Hoeveel euro stort de onderneming bij de btw-vereffening? Schrijf enkel het getal.",
        "3500",
        "Na de verrekening blijft 15 200 − 11 700 = 3 500 euro te betalen. De vereffening is die storting.",
    ),
    sorteer(
        "Een machine van 50 000 euro plus 21 % btw wordt op krediet gekocht. Debet of credit?",
        ["Debet", "Credit"],
        [
            ["Klasse 2 Machines, 50 000 euro", "Debet"],
            ["41100 Terug te vorderen btw, 10 500 euro", "Debet"],
            ["44000 Leveranciers, 60 500 euro", "Credit"],
        ],
        "De machine is een vast actief. De btw is terug te vorderen. De schuld aan de leverancier stijgt.",
    ),
    mk(
        "De bank stort een lening van 50 000 euro over vijf jaar op de rekening. Welke boeking klopt?",
        [
            "55000 debet, 17 credit",
            "55000 debet, 42 credit",
            "17 debet, 55000 credit",
            "Klasse 2 debet, 55000 credit",
        ],
        0,
        "De bank stijgt (debet). De lening is een schuld op meer dan een jaar (17, credit).",
    ),
    mk(
        "Een jaarlijkse aflossing bestaat uit 10 000 euro kapitaal en 2 000 euro interest. Welke boeking klopt?",
        [
            "42 debet 10 000, 65 debet 2 000, 55000 credit 12 000",
            "65 debet 12 000, 55000 credit 12 000",
            "17 debet 12 000, 55000 credit 12 000",
            "42 debet 12 000, 55000 credit 12 000",
        ],
        0,
        "Het kapitaal verlaagt de schuld die binnen het jaar vervalt (42). Enkel de interest is een kost (65).",
    ),
    keuze(
        "Op het einde van het jaar boek je het deel van de lening dat het [[*volgende jaar|vorige jaar|over vijf jaar]] terugbetaald moet worden over van groep [[*17 naar 42|42 naar 17|55 naar 17]].",
        "Zo toont de balans welk deel van de lening op korte termijn vervalt.",
    ),
    mk(
        "Lening van 40 000 euro, af te lossen in vier gelijke jaarlijkse schijven. Na de eerste aflossing en de overboeking op het einde van het jaar: hoeveel staat er dan op 17 en hoeveel op 42?",
        [
            "17: 20 000 euro, 42: 10 000 euro",
            "17: 30 000 euro, 42: 0 euro",
            "17: 30 000 euro, 42: 10 000 euro",
            "17: 10 000 euro, 42: 20 000 euro",
        ],
        0,
        "Na één aflossing blijft 30 000 euro over. Daarvan vervalt 10 000 euro volgend jaar (42), de rest blijft op 17.",
    ),
    tabel(
        "Is het een kost?",
        [
            ("De interest op een lening", J),
            ("De terugbetaling van het kapitaal van een lening", F),
            ("De werkgeversbijdrage voor de RSZ", J),
            ("Het voorschot aan arbeiders", F),
        ],
        "Kapitaal terugbetalen verlaagt een schuld. Het voorschot is een deel van het loon, dat als kost in de loonsynthese staat.",
    ),
    mk(
        "Te betalen btw 12 400 euro, terug te vorderen btw 9 100 euro. Welke boeking is de btw-verrekening?",
        [
            "45100 debet 9 100, 41100 credit 9 100",
            "45100 debet 12 400, 41100 credit 12 400",
            "41100 debet 9 100, 45100 credit 9 100",
            "45100 debet 3 300, 55000 credit 3 300",
        ],
        0,
        "Je boekt het kleinste bedrag weg aan beide kanten. Er blijft 3 300 euro te betalen op 45100. Die storting is de vereffening.",
    ),
    mk(
        "Te betalen btw 6 000 euro, terug te vorderen btw 8 500 euro. Wat blijft er na de verrekening over?",
        [
            "2 500 euro te ontvangen van de staat, op 41100",
            "2 500 euro te betalen aan de staat, op 45100",
            "14 500 euro te betalen aan de staat",
            "Niets, beide rekeningen staan op nul",
        ],
        0,
        "Er werd meer btw betaald bij aankopen dan aangerekend bij verkopen. De staat moet het verschil terugstorten.",
    ),
    volgorde(
        "Zet de boekingen rond de lonen van een maand in de juiste volgorde.",
        [
            "Het voorschot aan de arbeiders uitbetalen",
            "De loonsynthese boeken",
            "De nettolonen uitbetalen",
            "De RSZ en de bedrijfsvoorheffing doorstorten",
        ],
        "Halverwege de maand het voorschot, na de maand de synthese en de uitbetaling, en daarna het doorstorten aan RSZ en fiscus.",
    ),
    koppel(
        "Welke rekening hoort bij elk bedrag?",
        [
            ["Bedrijfsvoorheffing die de werkgever nog moet doorstorten", "453"],
            ["Bijdragen die de werkgever nog aan de RSZ moet betalen", "454"],
            ["Nettolonen die nog aan het personeel betaald moeten worden", "455"],
            ["Brutolonen als kost", "62"],
        ],
        ["61"],
        "Groep 45 bevat de schulden rond lonen: aan de fiscus, de RSZ en het personeel. Groep 62 is de kost.",
    ),
    mk(
        "Het sociaal secretariaat stuurt een factuur van 484 euro (400 euro plus btw) voor de loonadministratie. Welke boeking klopt?",
        [
            "61 debet 400, 41100 debet 84, 44000 credit 484",
            "62 debet 484, 44000 credit 484",
            "62 debet 400, 41100 debet 84, 44000 credit 484",
            "455 debet 484, 55000 credit 484",
        ],
        0,
        "Het sociaal secretariaat levert een dienst: klasse 61, niet 62. Het is geen loon.",
    ),
    sleep(
        "Bij de uitbetaling van de nettolonen daalt de schuld op [[455]] en daalt de bank op [[55000]]. Het brutoloon werd al als kost geboekt op [[62]].",
        ["61", "41100"],
        "De uitbetaling verlaagt enkel een schuld. De kost staat al in de loonsynthese.",
    ),
    tabel(
        "Waar of niet waar over arbeiders en bedienden?",
        [
            ("Arbeiders krijgen halverwege de maand een verplicht voorschot.", J),
            ("Bedienden krijgen hetzelfde verplichte voorschot.", F),
            ("Voor beiden maakt het sociaal secretariaat een loonsynthese.", J),
        ],
        "Het verplicht voorschot geldt voor arbeiders. Bedienden krijgen hun loon in één keer per maand.",
    ),
    inv(
        "Brutoloon 2 400 euro. De werkgeversbijdrage voor de RSZ is 25 %. Hoeveel euro kost die bijdrage de werkgever? Schrijf enkel het getal.",
        "600",
        "2 400 · 0,25 = 600 euro, bovenop het brutoloon.",
    ),
    mk(
        "Een leerling zegt: \"Een lening ontvangen is een opbrengst, want er komt geld op de bank.\" Wat is de beste reactie?",
        [
            "Het geld moet terugbetaald worden: het is een schuld, geen opbrengst",
            "Klopt, alles wat de bank doet stijgen is een opbrengst",
            "Klopt, maar enkel als de lening langer dan een jaar loopt",
            "Het is een kost, want je moet interest betalen",
        ],
        0,
        "Het vermogen van de onderneming stijgt niet: er komt evenveel schuld bij als geld.",
    ),
    tabel(
        "Op welke rekeninggroep boek je elk bedrag?",
        [
            ("Interest op een lening", "65"),
            ("Deel van een lening dat over drie jaar vervalt", "17"),
            ("Deel van een lening dat volgend jaar vervalt", "42"),
            ("De werkgeversbijdrage RSZ als kost", "62"),
        ],
        "65 financiële kosten, 17 schulden op meer dan een jaar, 42 het stuk dat binnen het jaar vervalt, 62 personeelskosten.",
        kolommen=["17", "42", "62", "65"],
    ),
    mk(
        "De werkgever stort de RSZ (7 614 euro) en de bedrijfsvoorheffing (3 900 euro) door via de bank. Welke boeking klopt?",
        [
            "454 debet 7 614, 453 debet 3 900, 55000 credit 11 514",
            "62 debet 11 514, 55000 credit 11 514",
            "55000 debet 11 514, 454 credit 7 614, 453 credit 3 900",
            "455 debet 11 514, 55000 credit 11 514",
        ],
        0,
        "Het doorstorten verlaagt de schulden aan de RSZ en de fiscus. De kosten werden al bij de loonsynthese geboekt.",
    ),
    open_(
        "Leg uit waarom je bij de aankoop van een machine met een banklening twee aparte boekingen maakt.",
        "Het zijn twee verrichtingen met elk een eigen stuk: de factuur van de leverancier (machine en btw tegenover een schuld aan de leverancier) en de lening van de bank (geld op de bank tegenover een schuld aan de bank). Met het geld van de lening betaal je daarna de leverancier.",
        "Elke boeking volgt een stuk: factuur, leningsovereenkomst en bankuittreksel.",
    ),
    casus(
        "Drukkerij Inkt bv koopt op 1 juli een drukpers van 80 000 euro plus 21 % btw. Ze betaalt met een lening van 80 000 euro, af te lossen in vijf gelijke jaarlijkse schijven vanaf volgend jaar, aan 4 % interest. De btw betaalt ze met eigen geld.",
        [
            mk(
                "Hoeveel btw kan Inkt terugvorderen?",
                ["16 800 euro", "3 200 euro", "0 euro", "13 884 euro"],
                0,
                "80 000 · 0,21 = 16 800 euro op 41100.",
            ),
            mk(
                "Hoeveel bedraagt de eerste jaarlijkse betaling aan de bank, als de interest berekend wordt op het volledige geleende bedrag?",
                ["19 200 euro", "16 000 euro", "3 200 euro", "83 200 euro"],
                0,
                "Kapitaal 80 000 / 5 = 16 000 euro. Interest 80 000 · 0,04 = 3 200 euro. Samen 19 200 euro.",
            ),
            tabel(
                "Hoeveel staat er op het einde van dit jaar, na de overboeking, op elke rekeninggroep?",
                [
                    ("17 Schulden op meer dan een jaar", "64 000"),
                    ("42 Schulden die binnen het jaar vervallen", "16 000"),
                    ("Klasse 2 Machines (aanschaffingswaarde)", "80 000"),
                ],
                "Er is nog niets afgelost. De machine staat aan haar aanschaffingswaarde. De schijf van volgend jaar gaat naar 42, de rest blijft op 17.",
                kolommen=["16 000", "64 000", "80 000"],
            ),
        ],
    ),
]
