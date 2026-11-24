"""Persoonlijkheid: wat ze is en hoe een brein reageert — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
grafiek, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Arousal van twee personen in rust -------------------------------------------------------
AR = Prent("arousal-rust", "Hoe sterk het brein in rust al in gang staat", "een staafdiagram met twee staven: persoon A heeft een hoge staaf, persoon B een lage staaf; de verticale as heet activatieniveau van het brein in rust")
AR.lijn(200, 540, 820, 540, DONKER, 3)
AR.lijn(200, 540, 200, 90, DONKER, 3)
AR.tekst(210, 80, "activatie in rust", 20, "start", DONKER, False)
AR.rect(300, 160, 160, 380, "#c4d5b5", DONKER, 0, 2)
AR.rect(580, 400, 160, 140, "#c4d5b5", DONKER, 0, 2)
AR.letter(380, 590, "A")
AR.letter(660, 590, "B")

VRAGEN = [
    klik("Klik op de persoon die volgens Eysenck eerder extravert is.", AR.bestand, [Prent.zone(560, 380, 200, 240)],
         "Een lage arousal in rust: van buiten zijn meer prikkels nodig."),
    klik("Klik op de persoon voor wie een drukke fuif volgens Eysenck sneller te veel wordt.", AR.bestand, [Prent.zone(280, 140, 200, 480)],
         "Bij een hoge arousal is drukte snel te veel: eerder introvert."),
    met_prent(AR.bestand, keuze("Persoon A zoekt volgens Eysenck [[*minder|meer]] prikkels op dan persoon B.",
              "Zijn brein staat al hoog in arousal.")),
    met_prent(AR.bestand, inv("Welk begrip van Eysenck staat in deze grafiek op de verticale as? Eén woord.", ["arousal"],
              "Arousal is het activatieniveau van het brein.")),
    tabel("Welk element van persoonlijkheid zie je hier vooral?", [
        ("Een baby schrikt van elk geluid en huilt lang.", "temperament"),
        ("Arne vindt zichzelf lelijk, al zegt iedereen het omgekeerde.", "zelfbeeld"),
        ("Fien wil per se arts worden en studeert daarvoor elke avond.", "motivatie"),
        ("Tom is in elke situatie, thuis, op school en op kamp, heel zorgvuldig.", "trekken"),
    ], "Aangeboren aard, beeld van jezelf, drijfveer, of een vaste eigenschap.",
       kolommen=["temperament", "zelfbeeld", "motivatie", "trekken"]),
    sorteer("Element van persoonlijkheid of niet?", ["Element", "Geen element"], [
        ["karakter", "Element"],
        ["temperament", "Element"],
        ["stemming van vandaag", "Geen element"],
        ["zelfbeeld", "Element"],
        ["lichaamslengte", "Geen element"],
    ], "De vijf elementen: karakter, motivatie, temperament, trekken of disposities en zelfbeeld."),
    keuze("Een trek verschilt van een stemming doordat ze [[*in veel situaties terugkomt|maar één dag duurt|enkel bij baby's voorkomt]].",
          "Een stemming is van vandaag, een trek zie je ook morgen."),
    tabel("BIS of BAS?", [
        ("reageert op beloning en winst", "BAS"),
        ("remt gedrag af bij gevaar", "BIS"),
        ("Zoë schrijft zich meteen in voor een wedstrijd met een mooie prijs.", "BAS"),
        ("Kobe durft zijn hand niet op te steken uit angst voor een fout antwoord.", "BIS"),
    ], "BIS remt af bij dreiging en straf, BAS zet in gang bij beloning.",
       kolommen=["BIS", "BAS"]),
    koppel("Koppel elke afkorting of begrip aan de juiste uitleg.", [
        ["BIS", "Behavioral Inhibition System"],
        ["BAS", "Behavioral Activation System"],
        ["arousal", "activatieniveau van het brein"],
    ], ["aangeboren aard van reageren"], "Gray en Eysenck."),
    casus(
        "Twee zussen, Lore en Margo, groeien op in hetzelfde gezin. Lore zoekt na school altijd drukte op: sport, "
        "vrienden, muziek. Margo trekt zich na een drukke dag graag terug met een boek, maar durft in de klas "
        "makkelijk te spreken. Lore stort zich op elke kans om iets te winnen, Margo denkt eerst na over wat kan mislopen.",
        [
            keuze("Volgens Eysenck heeft Lore in rust een [[*lage|hoge]] arousal.",
                  "Wie veel prikkels zoekt, heeft van nature een lage arousal."),
            mk("Margo is introvert maar durft in de klas te spreken. Wat toont dat?",
               ["introvert is niet hetzelfde als verlegen",
                "introverte mensen hebben helemaal geen arousal",
                "Margo heeft een heel sterk BAS van Gray",
                "Margo heeft geen enkel zelfbeeld"], 0,
               "Introversie gaat over hoeveel prikkels iemand nodig heeft, niet over durven."),
            keuze("Bij Margo is het [[*BIS|BAS]] van Gray sterker.",
                  "Ze denkt eerst aan wat kan mislopen: gevoelig voor dreiging."),
            mk("Wat volgt uit het feit dat twee zussen uit hetzelfde gezin zo verschillen?",
               ["persoonlijkheid komt niet alleen van de omgeving",
                "persoonlijkheid ligt helemaal vast in het gezin",
                "persoonlijkheid hangt enkel af van de opvoeding",
                "persoonlijkheid ontstaat pas op volwassen leeftijd"], 0,
               "Ook aangeboren verschillen spelen mee."),
        ],
    ),
    tabel("Klopt dit over persoonlijkheid?", [
        ("Temperament en karakter betekenen hetzelfde.", F),
        ("Persoonlijkheid ligt bij de geboorte helemaal vast.", F),
        ("Iedereen heeft zowel een BIS als een BAS.", J),
        ("Gray en Eysenck zoeken de verklaring in de werking van het brein.", J),
    ], "Temperament is aangeboren, karakter wordt ook gevormd."),
    mk("Gray en Eysenck verklaren vooral welk element van persoonlijkheid?",
       ["temperament", "het zelfbeeld", "de motivatie", "het karakter"], 0,
       "Temperament is de aangeboren aard van reageren."),
    keuze("Cross-cultureel onderzoek gaat na of een theorie [[*ook buiten één cultuur opgaat|alleen voor baby's klopt|in het brein te zien is]].",
          "Een theorie die alleen in één land getest is, kan elders anders uitvallen."),
    inv("Welk ander woord gebruik je voor trekken? Eén woord.", ["disposities", "dispositie"],
        "Trekken of disposities."),
    sleep("Volgens Eysenck staat het brein van een [[introvert]] iemand al hoog in arousal. Bij een [[extravert]] iemand staat het laag.",
          ["verlegen", "assertief"], "Daarom zoekt de ene minder en de andere meer prikkels."),
    mk("Een onderzoeker verklaart persoonlijkheid helemaal vanuit het brein. Wat kan je hem tegenwerpen?",
       ["hij vergeet ervaring en cultuur",
        "te veel aandacht voor het zelfbeeld",
        "ze kan geen enkel verschil meten",
        "ze werkt enkel met vijf fasen"], 0,
       "Wie alles in het brein zoekt, vergeet wat ervaring en cultuur doen."),
    tabel("Welke naam hoort bij het begrip?", [
        ("arousal", "Eysenck"),
        ("Behavioral Activation System", "Gray"),
        ("introversie en extraversie", "Eysenck"),
    ], "BIS en BAS van Gray, arousal van Eysenck.", kolommen=["Gray", "Eysenck"]),
    keuze("Dat een samenleving bescheidenheid meer waardeert dan opvallen, is een voorbeeld van [[*culturele factoren|temperament|arousal]].",
          "Welke eigenschappen gewaardeerd worden, verschilt per cultuur."),
    mk("Welke omschrijving past het best bij persoonlijkheid?",
       ["wat iemand kenmerkt en stabiel blijft",
        "hoe iemand zich vandaag toevallig voelt",
        "de manier waarop een groep beslissingen neemt",
        "de lichaamskenmerken die je erft van je ouders"], 0,
       "Persoonlijkheid blijft vrij stabiel doorheen situaties en jaren."),
    inv("Hoeveel elementen van persoonlijkheid zijn er? Schrijf het getal.", ["5", "vijf"],
        "Karakter, motivatie, temperament, trekken of disposities en zelfbeeld."),
    keuze("Het BAS van Gray reageert vooral op [[*beloning|straf|dreiging]].",
          "Het BIS reageert op dreiging en straf."),
    tabel("Welke benadering of factor zie je?", [
        ("Een onderzoeker meet hoe sterk het brein reageert op geluid.", "biologisch"),
        ("Een onderzoeker vergelijkt welke eigenschappen in drie landen gewaardeerd worden.", "cultureel"),
        ("Een onderzoeker kijkt of iemand sneller reageert op winst dan op verlies.", "biologisch"),
    ], "Brein en lichaam of de cultuur.", kolommen=["biologisch", "cultureel"]),
    inv("Hoe heet het element van persoonlijkheid dat over de drijfveer achter gedrag gaat?", ["motivatie", "de motivatie"],
        "Motivatie zet iemand in beweging."),
    keuze("Een zelfbeeld [[*hoeft niet te kloppen|klopt altijd|is altijd negatief]] met hoe anderen iemand zien.",
          "Het zelfbeeld is hoe iemand zichzelf ziet."),
    keuze("Volgens Eysenck is introvert zijn [[*niet hetzelfde als|precies hetzelfde als]] verlegen zijn.",
          "Introversie gaat over prikkels, niet over durven."),
    mk("Welk systeem is sterk bij iemand die bij elk voorstel eerst aan de risico's denkt?",
       ["Behavioral Inhibition System", "Behavioral Activation System", "het chronosysteem", "het mesosysteem"], 0,
       "Het BIS remt af bij dreiging."),
    open_("Leg met de theorie van Gray uit waarom twee leerlingen heel anders reageren op een moeilijke wedstrijd met een mooie prijs.",
          "Bij de ene leerling is het BAS sterker: hij reageert op de beloning en schrijft zich meteen in. Bij de andere is het BIS sterker: hij ziet vooral de kans om te verliezen en houdt zich in. Iedereen heeft beide systemen, maar niet even sterk."),
]
