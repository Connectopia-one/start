"""Taalvariëteiten, registers en beleefdheid — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

MAIL = (
    "Lees de mail van een leerling.\n\n"
    "Onderwerp: (leeg)\n\n"
    "\"Hey meneer,\n"
    "ik ga morgen ni kunnen komen want ik heb een afspraak bij den tandarts 😬. Kunde gij de taak doorsturen? Thx!!\n"
    "Groetjes\n"
    "Yasmine\""
)

VRAGEN = [
    casus(
        MAIL,
        [
            tabel(
                "Wat past niet bij een mail aan een leerkracht?",
                [
                    ("\"Hey\" als aanspreking", J),
                    ("de emoji", J),
                    ("\"Thx!!\"", J),
                    ("de reden van afwezigheid", F),
                ],
                "De inhoud is in orde. De aanspreking, de emoji en de afkorting horen bij een informeel register.",
            ),
            keuze(
                "\"Ni\", \"den tandarts\" en \"Kunde gij\" zijn voorbeelden van [[*tussentaal|standaardtaal|vakjargon]].",
                "Tussentaal zit tussen dialect en standaardtaal in.",
            ),
            mk(
                "Welke slotgroet past beter?",
                [
                    "Met vriendelijke groeten",
                    "Heel veel groetjes en tot morgen!",
                    "Doei, xx",
                    "Later!",
                ],
                0,
                "Bij een leerkracht hoort een neutrale, verzorgde formule.",
            ),
            tabel(
                "Hoe maak je de mail formeler?",
                [
                    ("\"Kunt u de taak doorsturen?\" schrijven", J),
                    ("een onderwerpregel invullen", J),
                    ("meer uitroeptekens gebruiken", F),
                    ("volledige zinnen in standaardtaal schrijven", J),
                ],
                "U gebruiken en volledige zinnen schrijven verhogen de formaliteit.",
            ),
            mk(
                "Wat is het effect van deze mail op de leerkracht?",
                [
                    "De toon botst met hun verhouding",
                    "Hij begrijpt de reden van afwezigheid niet",
                    "Hij denkt dat Yasmine geen Nederlands kent",
                    "Hij krijgt de indruk dat het een officiële brief is",
                ],
                0,
                "Er is geen fout tegen de inhoud gemaakt, wel tegen de verwachting die bij de verhouding hoort.",
            ),
        ],
    ),
    tabel(
        "Welke soort variëteit is elk voorbeeld?",
        [
            ("het Limburgs", "Regionaal"),
            ("jongerentaal", "Sociaal"),
            ("het Nederlands in België", "Nationaal"),
            ("de taal van een sollicitatiegesprek", "Situationeel"),
        ],
        "Streek, groep, land of situatie.",
        kolommen=["Regionaal", "Sociaal", "Nationaal", "Situationeel"],
    ),
    casus(
        "Een arts schrijft aan een patiënt: \"Uw bloedwaarden tonen een lichte hypercholesterolemie. Wij adviseren een lipidogram binnen drie maanden en een aanpassing van het voedingspatroon.\"",
        [
            mk(
                "Wat is het grootste probleem van deze brief?",
                [
                    "Het jargon sluit de patiënt uit",
                    "De brief is te informeel",
                    "De arts gebruikt tussentaal",
                    "De brief heeft geen aanspreking of slotgroet",
                ],
                0,
                "Binnen de groep is jargon handig en precies; daarbuiten wordt het een muur.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("Vakjargon kan gezag uitstralen.", J),
                    ("Vakjargon is altijd fout.", F),
                    ("De arts kan beter zijn taal aanpassen aan de ontvanger.", J),
                ],
                "Je register aanpassen is een vorm van respect.",
            ),
        ],
    ),
    sorteer(
        "Formeel of informeel register?",
        ["Formeel", "Informeel"],
        [
            ["een sollicitatiebrief", "Formeel"],
            ["een klacht bij de gemeente", "Formeel"],
            ["een appje aan je zus", "Informeel"],
            ["een kaartje aan je grootouders", "Informeel"],
            ["een mail aan de schooldirectie", "Formeel"],
        ],
        "De verhouding met de ontvanger bepaalt het register.",
    ),
    mk(
        "Je doet vakantiewerk aan de kassa. Een klant van ongeveer twintig vraagt iets. Wat doe je het best?",
        [
            "Je spreekt de klant aan met u",
            "Je spreekt in je eigen dialect",
            "Je gebruikt jongerentaal om er snel bij te horen",
            "Je zegt niets en wijst naar het bord",
        ],
        0,
        "In een zakelijke verhouding met onbekenden is u de gangbare keuze.",
    ),
    tabel(
        "Klopt dit over taalvariëteiten?",
        [
            ("Eén spreker kan verschillende variëteiten afwisselen.", J),
            ("Een dialect is slordige standaardtaal.", F),
            ("Tussen streekgenoten kan dialect duidelijker zijn.", J),
            ("Beleefdheidsconventies zijn overal ter wereld dezelfde.", F),
        ],
        "Duidelijkheid hangt af van de situatie en van wie er luistert.",
    ),
    casus(
        "Lees de zin uit een brief van de gemeente.\n\n"
        "\"Ingevolge de bepalingen van het reglement wordt u ter kennis gebracht dat de aanvraag tot het bekomen van een parkeervergunning niet in aanmerking kan worden genomen.\"",
        [
            mk(
                "Waarom leest deze zin zo moeilijk?",
                [
                    "Ze is lang, passief en onpersoonlijk",
                    "Ze bevat dialectwoorden en tussentaal",
                    "Ze bevat spelfouten tegen de regels",
                    "Ze is in jongerentaal geschreven",
                ],
                0,
                "Lange zinnen, passieve vormen en vaste formules maken een ambtelijke tekst stroef.",
            ),
            keuze(
                "In gewone woorden staat er: [[*u krijgt geen parkeervergunning|u krijgt een boete|het reglement verandert]].",
                "De boodschap is eenvoudig: de aanvraag is afgewezen.",
            ),
        ],
    ),
    mk(
        "Tussen vrienden begin je plots heel verzorgd standaardtaal te spreken. Wat is het effect?",
        [
            "Je schept afstand",
            "Je wordt beter begrepen",
            "Je klinkt vertrouwelijker",
            "Er verandert niets",
        ],
        0,
        "Een te formeel register tussen vrienden klinkt koel of zelfs spottend.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["De variëteit die overal in het taalgebied aanvaard is", "Standaardtaal"],
            ["Taal tussen dialect en standaardtaal in", "Tussentaal"],
            ["De taal van één beroep", "Jargon"],
            ["De toon die je kiest naargelang de situatie", "Register"],
        ],
        ["Metafoor", "Enjambement"],
        "Vier begrippen uit taal en samenleving.",
    ),
    keuze(
        "\"Zou je het raam willen sluiten?\" in plaats van \"Sluit het raam\" hoort bij de [[*beleefdheidsconventies|dialecten|nationale variëteiten]].",
        "Vragen in plaats van bevelen laat de ander zijn ruimte.",
    ),
    tabel(
        "Waarom gebruiken het onderwijs en het bestuur standaardtaal?",
        [
            ("Iedereen in het taalgebied kan ze begrijpen.", J),
            ("Ze werkt over streek- en groepsgrenzen heen.", J),
            ("Dialecten zijn wettelijk verboden.", F),
        ],
        "Een gemeenschappelijke variëteit maakt dat mensen uit alle streken elkaar volgen.",
    ),
    mk(
        "Je twijfelt of je een onbekende ouder van een vriend met je of met u moet aanspreken. Wat doe je?",
        [
            "Je kiest u",
            "Je kiest je",
            "Je vermijdt elk gesprek",
            "Je spreekt dialect",
        ],
        0,
        "Te formeel valt zelden verkeerd, te informeel wel.",
    ),
    sleep(
        "Een rapper gebruikt woorden die veel ouderen niet kennen. Zo'n [[sociale]] variëteit sluit een groep [[in]] en een andere [[uit]].",
        ["regionale", "standaard"],
        "Wie de woorden kent, hoort erbij.",
    ),
    tabel(
        "Een juridische tekst. Klopt dit?",
        [
            ("Precisie weegt zwaarder dan leesbaarheid.", J),
            ("Elk woord moet in een rechtszaal standhouden.", J),
            ("Juristen schrijven zo om lezers te pesten.", F),
        ],
        "Daardoor is de tekst betrouwbaar voor de vakman en moeilijk voor de leek.",
    ),
    casus(
        "Twee gesprekken van dezelfde leerling, Bram.\n\n"
        "Op het sollicitatiegesprek: \"Goedemiddag, ik ben Bram. Ik heb uw vacature gelezen en ik zou graag deze zomer bij u werken.\"\n\n"
        "Even later tegen zijn vriend: \"Ej, 't was echt nice, ik denk da'k die job heb, man!\"",
        [
            tabel(
                "Klopt dit over Bram?",
                [
                    ("Hij wisselt tussen variëteiten naargelang de situatie.", J),
                    ("Hij spreekt slecht Nederlands.", F),
                    ("Het tweede gesprek bevat jongerentaal en tussentaal.", J),
                ],
                "Dat is net de regel: elke situatie vraagt haar eigen taal.",
            ),
            keuze(
                "De manier waarop Bram spreekt naargelang de situatie, heet een [[*situationele|regionale|nationale]] variëteit.",
                "Dezelfde spreker praat anders aan tafel, in de klas en op een sollicitatie.",
            ),
            mk(
                "Wat zegt Brams taal over hoe anderen hem inschatten?",
                [
                    "Ze kleurt mee het beeld dat anderen hebben",
                    "Ze heeft geen enkele invloed op hoe hij overkomt",
                    "Ze bepaalt of hij de job krijgt, los van de rest",
                    "Ze toont enkel uit welke streek hij komt",
                ],
                0,
                "Je taalgebruik is een deel van je identiteit.",
            ),
        ],
    ),
    tabel(
        "Nationale of regionale variëteit?",
        [
            ("het Nederlands zoals het in Nederland gesproken wordt", "Nationaal"),
            ("het West-Vlaams", "Regionaal"),
            ("het Belgisch-Nederlands", "Nationaal"),
            ("het Antwerps", "Regionaal"),
        ],
        "Nationaal gaat over een land, regionaal over een streek.",
        kolommen=["Nationaal", "Regionaal"],
    ),
    mk(
        "Een programmeur legt zijn grootmoeder iets uit in vaktaal. Waarom loopt dat mis?",
        [
            "Wie de woorden niet kent, haakt af",
            "Vaktaal bevat altijd veel spelfouten",
            "Vaktaal is een regionale variëteit",
            "Vaktaal wordt enkel gesproken",
        ],
        0,
        "Daarbuiten wordt het een muur.",
    ),
    tabel(
        "Welke signalen maken een tekst informeel?",
        [
            ("afkortingen zoals thx", J),
            ("aanspreking met jij", J),
            ("\"Met vriendelijke groeten\"", F),
            ("korte, losse zinnen", J),
        ],
        "Een formele slotgroet hoort bij het andere register.",
    ),
    keuze(
        "Iemand die in een andere cultuur iemand meteen bij de voornaam noemt, kan [[*opdringerig|formeel|ambtelijk]] overkomen.",
        "Beleefdheidsconventies verschillen per cultuur.",
    ),
    mk(
        "Een tv-presentator leest het nieuws. Welke variëteit verwacht je?",
        ["Standaardtaal", "Dialect", "Jongerentaal", "Medisch vakjargon"],
        0,
        "De media gebruiken standaardtaal, zodat iedereen in het taalgebied kan volgen.",
    ),
    inv(
        "Met welk voornaamwoord spreek je in een formele brief de ontvanger aan? Antwoord met één woord.",
        ["u", "U"],
        "Met u hou je afstand en toon je respect.",
    ),
    open_(
        "Herschrijf de mail van Yasmine in een gepast formeel register.",
        "Onderwerp: Afwezigheid morgen\n\nGeachte meneer,\nMorgen kan ik niet naar school komen, omdat ik een afspraak heb bij de tandarts. Kunt u mij de taak doorsturen?\nAlvast bedankt.\nMet vriendelijke groeten\nYasmine",
    ),
]
