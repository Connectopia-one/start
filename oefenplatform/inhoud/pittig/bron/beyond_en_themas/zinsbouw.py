"""Zinsbouw, indirecte rede en de passieve vorm — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the news report.\n\n"
    "MUSEUM PAINTING STOLEN\n"
    "A valuable painting was stolen from the Ashmore Museum last night. The theft was discovered by a cleaner at 6 a.m. "
    "The police said that they were questioning two men. A spokesperson told reporters that the painting had been insured, "
    "but she added that it could never be replaced. The museum will be closed until further notice. "
    "The painting is said to be worth more than £2 million."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Waarom staat de kop « Museum painting stolen » in de passieve vorm?",
                ["De nadruk ligt op het schilderij", "De naam van de dief is al bekend", "De kop is eigenlijk een bevel", "Het is een vraag aan de lezer"],
                0,
                "In een kop valt de nadruk op wat er gebeurde, niet op de dader.",
            ),
            inv(
                "Wie ontdekte de diefstal? Antwoord met het Engelse woord uit de tekst.",
                ["a cleaner", "cleaner", "the cleaner"],
                "Discovered by a cleaner: de dader staat na by.",
            ),
            keuze(
                "« The police said that they were questioning two men » is [[*indirecte rede|een letterlijk citaat]].",
                "Said that + verschoven tijd.",
            ),
            keuze(
                "De woordvoerster zei letterlijk: « The painting [[*has been|had been]] insured. »",
                "In de indirecte rede schuift has been naar had been.",
            ),
            mk(
                "Wat betekent « is said to be worth more than £2 million »?",
                ["Men zegt dat het zoveel waard is", "Het is zeker zoveel waard", "Het werd voor dat bedrag verkocht", "De dief zei hoeveel het waard is"],
                0,
                "Passief zonder dader: men zegt.",
            ),
        ],
    ),
    tabel(
        "Actief of passief?",
        [
            ("The bridge was opened by the king.", "Passief"),
            ("The children are tired.", "Actief"),
            ("The car is being repaired.", "Passief"),
            ("Somebody has taken my bike.", "Actief"),
        ],
        "Passief: to be + voltooid deelwoord, met het lijdend voorwerp als onderwerp.",
        kolommen=["Actief", "Passief"],
    ),
    tabel(
        "Welke conditional is dit?",
        [
            ("If you mix red and blue, you get purple.", "Zero"),
            ("If it's sunny tomorrow, we'll go to the beach.", "First"),
            ("If you press this button, the machine stops.", "Zero"),
            ("If you don't hurry, you'll miss the bus.", "First"),
        ],
        "Zero: altijd waar (present + present). First: mogelijk (present + will).",
        kolommen=["Zero", "First"],
    ),
    sleep(
        "The new library [[was opened]] last week. More than 500 books [[were donated]] by local families. Coffee [[is served]] every morning.",
        ["opened", "donated", "is serving"],
        "Passief: to be in de juiste tijd + voltooid deelwoord.",
    ),
    mk(
        "Zet in de passieve vorm: « Shakespeare wrote Hamlet. »",
        ["Hamlet was written by Shakespeare.", "Hamlet was wrote by Shakespeare.", "Hamlet is writing by Shakespeare.", "Shakespeare was written by Hamlet."],
        0,
        "Was + written + by.",
    ),
    mk(
        "« Where do you live? » she asked. Welke indirecte rede is juist?",
        ["She asked where I lived.", "She asked where did I live.", "She asked where do you live.", "She asked me where lived I."],
        0,
        "In een indirecte vraag: gewone woordorde, tijd een stap terug.",
    ),
    mk(
        "« Don't be late, » the teacher said to us. Welke indirecte rede is juist?",
        ["The teacher told us not to be late.", "The teacher told us don't be late.", "The teacher said us not be late.", "The teacher told to us we not late."],
        0,
        "Een verbod wordt told + not to.",
    ),
    mk(
        "« I will call you, » he said. Hoe zeg je dit in de indirecte rede?",
        ["He said he would call me.", "He said he will call you.", "He said he calls me.", "He said would he call me."],
        0,
        "Will wordt would; you wordt me.",
    ),
    mk(
        "« Are you hungry? » Mum asked. Welke indirecte rede is juist?",
        ["Mum asked if I was hungry.", "Mum asked was I hungry.", "Mum asked are you hungry.", "Mum asked that I am hungry."],
        0,
        "Ja-neevraag: if of whether.",
    ),
    keuze(
        "« Neither the teacher nor the pupils [[*were|was]] ready. »",
        "Het werkwoord volgt het dichtstbijzijnde onderwerp: pupils.",
    ),
    keuze(
        "« A number of students [[*have|has]] complained. »",
        "A number of = verscheidene: meervoud. The number of = het aantal: enkelvoud.",
    ),
    keuze(
        "« If it [[*rains|will rain]] tomorrow, the match will be cancelled. »",
        "Na if in de first conditional: geen will.",
    ),
    keuze(
        "« We won't go out [[*unless|until]] the rain stops. » We gaan enkel als het ophoudt.",
        "Unless: tenzij.",
    ),
    inv(
        "Vul aan met één voegwoord: « She passed the exam ___ she hadn't studied much. » (hoewel)",
        ["although", "though", "even though"],
        "Although: toegeving.",
    ),
    inv(
        "Vul aan met één voegwoord: « Wait here ___ I come back. » (totdat)",
        ["until", "till"],
        "Until: totdat.",
    ),
    inv(
        "Vul aan met de passieve vorm van to grow: « Rice ___ in many Asian countries. »",
        ["is grown"],
        "Present simple passief: is + grown.",
    ),
    mk(
        "Wat is het lijdend voorwerp in « The company sent all its customers a new catalogue »?",
        ["a new catalogue", "all its customers", "the company", "sent"],
        0,
        "Wat werd er gestuurd? Een catalogus. All its customers is het meewerkend voorwerp.",
    ),
    mk(
        "Welke zin heeft de juiste woordorde?",
        ["We usually have dinner at seven.", "We have usually dinner at seven.", "Usually we dinner have at seven.", "We have dinner usually at seven o'clock."],
        0,
        "Onderwerp, werkwoord, voorwerp; usually voor het werkwoord.",
    ),
    tabel(
        "Juist of fout (over zinsbouw)?",
        [
            ("He asked me where the station was.", J),
            ("The house was build in 1920.", F),
            ("Each of the players has a number.", J),
            ("If you will need help, call me.", F),
        ],
        "Built is het deelwoord; na if geen will.",
    ),
    koppel(
        "Koppel elk voegwoord aan zijn betekenis.",
        [
            ("because", "omdat"),
            ("unless", "tenzij"),
            ("whereas", "terwijl, daarentegen"),
            ("so that", "zodat"),
        ],
        ["toch"],
        "Voegwoorden verbinden zinnen.",
    ),
    sorteer(
        "Nevenschikkend of onderschikkend voegwoord?",
        ["Nevenschikkend", "Onderschikkend"],
        [
            ("and", "Nevenschikkend"),
            ("although", "Onderschikkend"),
            ("but", "Nevenschikkend"),
            ("because", "Onderschikkend"),
            ("or", "Nevenschikkend"),
        ],
        "Nevenschikkend verbindt gelijke delen; onderschikkend leidt een bijzin in.",
    ),
    volgorde(
        "Zet de zinsdelen in de juiste Engelse volgorde.",
        ["My sister", "bought", "a new phone", "in Brussels", "last week"],
        "Onderwerp, werkwoord, voorwerp, plaats, tijd.",
    ),
    mk(
        "« What a beautiful day! » Wat voor zin is dit?",
        ["Een uitroep", "Een vraag", "Een bevel", "Een mededeling"],
        0,
        "Uitroepende zinnen beginnen vaak met what of how.",
    ),
    keuze(
        "« The results [[*will be published|will publish]] next week. »",
        "Passief in de toekomst: will be + deelwoord.",
    ),
    mk(
        "« The road is being repaired. » Wanneer gebeurt de herstelling?",
        ["Nu", "Vorig jaar", "Volgende maand", "Elke dag opnieuw"],
        0,
        "Is being + deelwoord: passief van de present continuous.",
    ),
    open_(
        "Zet in de indirecte rede en leg uit wat er verandert: « I am leaving tomorrow, » Tom said.",
        "Tom said that he was leaving the next day. I wordt he, am wordt was (de tijd schuift een stap terug) en tomorrow wordt the next day.",
    ),
]
