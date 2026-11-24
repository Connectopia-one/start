"""Tekstsoorten en teksttypes — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

SOORTEN = ["Informatief", "Persuasief", "Prescriptief", "Argumentatief", "Opiniërend", "Narratief", "Literair"]

VRAGEN = [
    tabel(
        "Welk hoofddoel heeft elke tekst?",
        [
            ("een bijsluiter bij een geneesmiddel", "Prescriptief"),
            ("een lemma in een naslagwerk", "Informatief"),
            ("een reclamefilmpje voor een sportdrank", "Persuasief"),
            ("een videoblog over een weekend in Gent", "Narratief"),
            ("een protestlied", "Opiniërend"),
        ],
        "Het doel van de zender bepaalt de soort, niet de vorm van de tekst.",
        kolommen=["Informatief", "Persuasief", "Prescriptief", "Narratief", "Opiniërend"],
    ),
    casus(
        "Lees de tekst.\n\n\"Elke ochtend sleuren we tienduizenden jongeren om half acht uit bed. Slaaponderzoek toont dat tieners pas laat in slaap vallen en dus te kort slapen. Scholen die later begonnen, zagen betere resultaten en minder afwezigheden. Daarom moeten onze scholen om negen uur beginnen. Schrijf vandaag nog naar je directie.\"",
        [
            tabel(
                "Welke doelen vind je in deze tekst terug?",
                [
                    ("Argumentatief", J),
                    ("Opiniërend", J),
                    ("Persuasief", J),
                    ("Narratief", F),
                ],
                "De schrijver geeft zijn mening, onderbouwt die met onderzoek en sluit af met een oproep. Een verhaal vertelt hij niet.",
            ),
            mk(
                "Welke zin maakt de tekst ook persuasief?",
                [
                    "\"Schrijf vandaag nog naar je directie.\"",
                    "\"Slaaponderzoek toont dat tieners pas laat in slaap vallen.\"",
                    "\"Elke ochtend sleuren we jongeren uit bed.\"",
                    "\"Scholen die later begonnen, zagen betere resultaten.\"",
                ],
                0,
                "Een oproep tot actie wil je iets laten doen. Dat is beïnvloeden.",
            ),
            mk(
                "Wat is het standpunt van de schrijver?",
                [
                    "Scholen moeten om negen uur beginnen",
                    "Tieners vallen laat in slaap",
                    "Afwezigheden van leerlingen moeten bestraft worden",
                    "Slaaponderzoek bij tieners is onbetrouwbaar",
                ],
                0,
                "Het slaaponderzoek en de resultaten zijn argumenten. Het standpunt staat na \"daarom\".",
            ),
        ],
    ),
    mk(
        "Een publireportage over een nieuw hotel staat in de krant, met foto's en citaten van gasten. Onderaan staat klein \"in samenwerking met\". Wat is de tekst vooral?",
        [
            "Persuasief, in een informatieve vorm",
            "Informatief, want hij staat in de krant",
            "Narratief, want er staan getuigenissen in",
            "Prescriptief, want je moet boeken",
        ],
        0,
        "De vorm lijkt op een artikel, maar een merk betaalt. Het doel is overtuigen.",
    ),
    sorteer(
        "Zet elke tekst bij de juiste soort.",
        ["Prescriptief", "Argumentatief", "Literair"],
        [
            ["een schoolreglement", "Prescriptief"],
            ["een handleiding bij een telefoon", "Prescriptief"],
            ["een pleidooi van een advocaat", "Argumentatief"],
            ["een debat over kernenergie", "Argumentatief"],
            ["een kortverhaal", "Literair"],
            ["een gedicht over een grootvader", "Literair"],
        ],
        "Voorschrijven, onderbouwen of raken met de vorm: drie verschillende doelen.",
    ),
    tabel(
        "Klopt dit over tekstsoorten?",
        [
            ("Bovenaan een tekst staat welke soort het is.", F),
            ("Eén tekst kan meer dan één doel tegelijk hebben.", J),
            ("Een tekst met feiten is altijd informatief.", F),
            ("Ook reclame kan juiste informatie bevatten.", J),
        ],
        "De soort zegt wat de zender wil, niet of het waar is.",
    ),
    casus(
        "Lees de tekst.\n\n\"Verwijder eerst de band van de velg met twee bandenlichters. Pomp de binnenband een beetje op en houd hem onder water. Waar luchtbellen opstijgen, zit het gat. Maak die plek droog, schuur ze op en smeer er een dun laagje solutie op.\"",
        [
            mk(
                "Welke soort is deze tekst?",
                ["Prescriptief", "Narratief", "Informatief", "Argumentatief"],
                0,
                "De gebiedende wijs (verwijder, pomp, houd) verraadt een voorschrift.",
            ),
            mk(
                "Welk taalkenmerk wijst daar het sterkst op?",
                [
                    "De gebiedende wijs",
                    "De verleden tijd",
                    "De vele bijvoeglijke naamwoorden",
                    "De ik-vorm",
                ],
                0,
                "Een voorschrift spreekt je rechtstreeks aan met wat je moet doen.",
            ),
            keuze(
                "Als dezelfde tekst als instructiefilmpje op YouTube staat, blijft hij [[*prescriptief|narratief|literair]].",
                "Of je hem leest of bekijkt: het hoofddoel blijft voorschrijven.",
            ),
        ],
    ),
    mk(
        "Wat onderscheidt een argumentatieve tekst van een opiniërende?",
        [
            "Argumenten onderbouwen het standpunt",
            "Er staat een mening van de schrijver in",
            "Er komt een ik-verteller in voor",
            "Hij is altijd geschreven",
        ],
        0,
        "Een mening geven is opiniërend. Die mening onderbouwen met argumenten maakt het argumentatief.",
    ),
    casus(
        "Lees de recensie.\n\n\"In 'De zomer van Lien' volgen we een meisje van vijftien dat haar vader verliest. Het boek telt 240 bladzijden en verscheen bij een kleine uitgeverij. De schrijfster vindt prachtige, sobere zinnen voor groot verdriet. Een aanrader, al is het einde wat te zoet.\"",
        [
            tabel(
                "Welke zin hoort bij welk doel?",
                [
                    ("\"Het boek telt 240 bladzijden.\"", "Informatief"),
                    ("\"Een aanrader, al is het einde wat te zoet.\"", "Opiniërend"),
                    ("\"We volgen een meisje dat haar vader verliest.\"", "Informatief"),
                ],
                "Een recensie informeert eerst en geeft daarna een oordeel.",
                kolommen=["Informatief", "Opiniërend"],
            ),
            mk(
                "Waarom is het geen literaire tekst, al gaat hij over een roman?",
                [
                    "Hij wil vooral informeren en beoordelen",
                    "Hij is te kort voor een literaire tekst",
                    "Er staat geen rijm in",
                    "Hij gaat over een echt bestaand boek",
                ],
                0,
                "Het onderwerp is literatuur, maar het doel van de recensie zelf is niet esthetisch.",
            ),
        ],
    ),
    mk(
        "Een stand-upcomedian vertelt vijf minuten over zijn eerste schooldag, vol woordspelingen. Wat is de beste typering?",
        [
            "Narratief en literair",
            "Enkel informatief",
            "Prescriptief en argumentatief",
            "Geen van de zeven soorten",
        ],
        0,
        "Hij vertelt een verhaal en speelt bewust met taal.",
    ),
    tabel(
        "Klopt dit over lees- en luisterteksten op het examen?",
        [
            ("Een interview kan je zowel lezen als beluisteren.", J),
            ("Bij een luistertekst stel je andere vragen over zender en doel.", F),
            ("Een reclameboodschap komt enkel geschreven voor.", F),
            ("Er komen ook teksten in tussentaal of dialect voor.", J),
        ],
        "Dezelfde soort komt in beide vormen voor, en niet alles is Standaardnederlands.",
    ),
    casus(
        "Een fabrikant van sportdrank maakt een filmpje. Een dokter in witte jas legt uit waarom je na het sporten moet bijtanken. Op het einde zie je het logo van de drank.",
        [
            mk(
                "Wie is de echte zender?",
                ["De fabrikant", "De dokter", "De kijker", "Het videoplatform"],
                0,
                "Wie spreekt en wie betaalt, zijn twee verschillende dingen.",
            ),
            mk(
                "Waarom laat de fabrikant een dokter spreken?",
                [
                    "Om met autoriteit te overtuigen",
                    "Omdat dokters de drank uitvonden",
                    "Om het filmpje prescriptief te maken",
                    "Omdat dat wettelijk verplicht is",
                ],
                0,
                "De witte jas wekt vertrouwen. Zo wordt een persuasieve boodschap geloofwaardiger.",
            ),
            keuze(
                "Het filmpje is vooral [[*persuasief|informatief|narratief]].",
                "Er wordt informatie gegeven, maar het doel is je de drank laten kopen.",
            ),
        ],
    ),
    mk(
        "Een partij zet op haar eigen site een artikel over hoe andere partijen de polarisatie aanwakkeren. Hoe lees je dat?",
        [
            "Als partijcommunicatie met een belang",
            "Als neutrale en onafhankelijke journalistiek",
            "Als een literaire tekst",
            "Als een voorschrift",
        ],
        0,
        "De zender spreekt over zijn tegenstanders op zijn eigen kanaal. Dat is propaganda, ook al lijkt het een artikel.",
    ),
    sleep(
        "Een recept is [[prescriptief]], een reisverslag is [[narratief]] en reclame, propaganda en nepnieuws zijn [[persuasief]].",
        ["literair", "argumentatief"],
        "Drie doelen: voorschrijven, vertellen en beïnvloeden.",
    ),
    casus(
        "Lees de column.\n\n\"Mijn buurman heeft een nieuwe hobby: bladblazen. Om zeven uur. Op zondag. Het blad waait netjes van zijn oprit naar de mijne. Gemeenten, verbied die toestellen toch eindelijk. Wie twee armen heeft, kan een hark vasthouden.\"",
        [
            tabel(
                "Welke doelen vind je terug?",
                [
                    ("Narratief", J),
                    ("Opiniërend", J),
                    ("Persuasief", J),
                    ("Prescriptief", F),
                ],
                "Een anekdote, een mening en een oproep aan de gemeenten. Een handleiding is het niet.",
            ),
            mk(
                "Wat doe je best met de soort van zo'n column?",
                [
                    "Je noemt alle doelen die erin zitten",
                    "Je kiest het eerste doel",
                    "Je kiest het laatste doel",
                    "Je zegt dat het geen tekstsoort heeft",
                ],
                0,
                "Veel teksten combineren doelen. Ze allemaal benoemen is juister dan er één kiezen.",
            ),
        ],
    ),
    mk(
        "Waarom bepaal je bij het lezen best eerst de tekstsoort?",
        [
            "Je weet dan wat de zender van je wil",
            "Je hoeft dan de titel niet te lezen",
            "Je weet dan wie de tekst schreef",
            "Je kan dan alle moeilijke woorden overslaan",
        ],
        0,
        "Wie weet dat een tekst wil overtuigen, leest hem kritischer.",
    ),
    tabel(
        "Juist of fout over een essay van een filosoof over vriendschap?",
        [
            ("Het kan argumentatief zijn.", J),
            ("Het kan tegelijk literair zijn.", J),
            ("Het is per definitie prescriptief.", F),
        ],
        "Een essay onderbouwt en is vaak mooi geschreven. Het schrijft je geen handelingen voor.",
    ),
    inv(
        "Een toespraak van een advocaat voor de rechter, waarin hij met argumenten de onschuld van zijn cliënt verdedigt, heet een ...",
        ["pleidooi", "het pleidooi", "een pleidooi"],
        "Een pleidooi is een argumentatieve tekst.",
    ),
    mk(
        "Een tekst over de haven van Antwerpen, gemaakt door het havenbedrijf zelf. Wat is je eerste vraag?",
        [
            "Wie maakte dit en waarom?",
            "Hoeveel woorden telt de tekst?",
            "Staan er foto's bij?",
            "Wanneer is de haven gebouwd?",
        ],
        0,
        "Zender en doel komen eerst. Een milieugroep zou een ander beeld geven.",
    ),
    koppel(
        "Welk voorbeeld hoort bij welke soort?",
        [
            ["een true crime podcast", "Narratief"],
            ["een hotelbeoordeling online", "Opiniërend"],
            ["een veiligheidsvoorschrift", "Prescriptief"],
            ["een stukje uit een leerboek", "Informatief"],
        ],
        ["Literair", "Argumentatief"],
        "Vier voorbeelden, vier doelen.",
    ),
    mk(
        "Een bericht op sociale media meldt met een foto dat een bekende brug is ingestort. Het blijkt verzonnen, om kliks te lokken. Bij welke soort hoort het?",
        [
            "Persuasief",
            "Informatief",
            "Narratief",
            "Literair",
        ],
        0,
        "Nepnieuws doet zich voor als informatie, maar wil je beïnvloeden. Het staat bij de persuasieve teksten.",
    ),
    tabel(
        "Een documentaire over plastic in de zee. Welke doelen kan ze hebben?",
        [
            ("Informatief", J),
            ("Narratief", J),
            ("Persuasief", J),
            ("Prescriptief, want er is altijd een stappenplan", F),
        ],
        "Een documentaire informeert, vertelt vaak een verhaal en wil soms overtuigen.",
    ),
    open_(
        "Een recensie, een documentaire en een column zitten vaak op twee soorten tegelijk. Kies er één en leg uit welke twee doelen erin zitten.",
        "Een recensie vertelt eerst waar een boek of film over gaat (informatief) en geeft daarna het oordeel van de schrijver (opiniërend). Een documentaire informeert, maar vertelt vaak ook een verhaal (narratief) of wil je overtuigen (persuasief). Een column geeft een mening (opiniërend) en is vaak ook grappig of mooi geschreven (literair).",
    ),
]
