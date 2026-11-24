"""Een functie aflezen van haar grafiek — pittig (Beyond dubbele finaliteit, wiskunde).

Pittige vragen wiskunde basis Beyond (met hun prenten) binnen wi_grafiek, plus eigen vragen."""
from ..beyond_wiskunde_basis_themas import grafisch as G
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(G.VRAGEN, [0, 1, 2, 4, 5, 6, 12, 13, 14, 15, 18, 22, 23, 25, 26, 27]) + [
    sorteer("Gaat het over een \\(x\\)-waarde of over een \\(y\\)-waarde?", ["\\(x\\)-waarde", "\\(y\\)-waarde"], [
        ["een nulwaarde", "\\(x\\)-waarde"], ["het domein", "\\(x\\)-waarde"], ["een maximum", "\\(y\\)-waarde"],
        ["het bereik", "\\(y\\)-waarde"], ["het snijpunt met de \\(y\\)-as, als getal", "\\(y\\)-waarde"],
    ], "Domein en nulwaarden lees je horizontaal af, bereik en extrema verticaal."),
    koppel("Koppel elke situatie aan het kenmerk van de grafiek.", [
        ["een auto verliest elk jaar waarde, maar steeds minder", "dalend met afnemende daling"],
        ["een verkoper maakt pas winst vanaf \\(200\\) stuks", "nulwaarde"],
        ["eb en vloed komen telkens na \\(12{,}5\\) uur terug", "periode"],
        ["een bal bereikt zijn hoogste punt na \\(2\\) seconden", "maximum"],
    ], ["constante functie"], "Telkens beschrijft de situatie een kenmerk van de grafiek."),
    tabel("Klopt dit over grafieken?", [
        ("Een functie kan meerdere nulwaarden hebben.", J),
        ("Een functie kan twee snijpunten met de \\(y\\)-as hebben.", F),
        ("Een dalende functie heeft overal negatieve functiewaarden.", F),
        ("Het praktisch domein kan kleiner zijn dan het wiskundige domein.", J),
    ], "Dalen zegt iets over de richting, het teken zegt iets over boven of onder de \\(x\\)-as."),
    mk("Een verloopschema toont: stijgend tot \\(x = 2\\), daar max \\(5\\), dan dalend tot \\(x = 6\\), daar min \\(-1\\), dan weer stijgend. Hoeveel nulwaarden heeft de functie zeker tussen \\(x = 2\\) en \\(x = 6\\)?",
       ["één", "geen", "twee", "dat kan je niet weten"], 0, "Ze daalt van \\(5\\) naar \\(-1\\) en snijdt de \\(x\\)-as dus precies één keer."),
    keuze("In een tekenverloop betekent een min tussen \\(x = 1\\) en \\(x = 4\\) dat de grafiek daar [[*onder de \\(x\\)-as|boven de \\(x\\)-as|dalend]] ligt.", "Het teken gaat over de functiewaarde."),
    inv("Een grafiek loopt van \\((-3, 2)\\) omhoog tot \\((1, 7)\\) en dan omlaag tot \\((5, -4)\\), en nergens anders. Wat is de breedte van het bereik, het verschil tussen grootste en kleinste functiewaarde?", ["11", "elf"],
        "Het bereik is \\([-4, 7]\\): \\(7 - (-4) = 11\\)."),
    mk("De grafiek toont de reistijd in functie van de snelheid en daalt. Wat betekent dat?",
       ["Hoe sneller je rijdt, hoe korter de reis duurt.", "Hoe sneller je rijdt, hoe langer de reis duurt.", "De reistijd hangt niet af van de snelheid.", "De snelheid daalt tijdens de reis."], 0,
       "Dalend: grotere \\(x\\), kleinere \\(y\\)."),
    volgorde("Je maakt een grafiek uit een tabel. Zet de stappen in volgorde.", [
        "de assen tekenen en een passende schaal kiezen", "elk koppel uit de tabel als punt uitzetten", "de punten verbinden als dat in de situatie zinvol is", "de assen benoemen met grootheid en eenheid",
    ], "Benoemen mag ook vroeger, maar mag niet ontbreken."),
    tabel("Hoe stijgt of daalt deze grafiek?", [
        ("de hoogte van een plant die eerst snel en daarna steeds trager groeit", "stijgend met afnemende stijging"),
        ("het aantal volgers dat steeds sneller toeneemt", "stijgend met toenemende stijging"),
        ("de temperatuur van een kop thee die afkoelt, eerst snel en dan trager", "dalend met afnemende daling"),
    ], "Kijk of de grafiek steiler of minder steil wordt.",
        kolommen=["stijgend met toenemende stijging", "stijgend met afnemende stijging", "dalend met afnemende daling"]),
    keuze("Een grafiek die links en rechts van de \\(y\\)-as elkaars spiegelbeeld is, hoort bij een [[*even|periodieke|constante]] functie.", "De \\(y\\)-as is de symmetrieas."),
    open_("De winstgrafiek van een bedrijf snijdt de \\(x\\)-as bij \\(400\\) stuks en ligt daarna boven de as. Leg uit wat dat betekent.",
          "Bij \\(400\\) stuks is de winst nul: dat is het break-evenpunt. Vanaf meer dan \\(400\\) stuks is de winst positief, daaronder maakt het bedrijf verlies.",
          "Een nulwaarde in een situatie is vaak een omslagpunt."),
    inv("Een functie heeft periode \\(24\\) en \\(f(5) = 12\\). Hoeveel is \\(f(53)\\)?", ["12", "twaalf"], "\\(53 = 5 + 2 \\cdot 24\\)."),
]
