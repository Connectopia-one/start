"""Dramatiek en theatertekens — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VOORSTELLING = (
    "Lees de beschrijving van een voorstelling.\n\n"
    "Het toneel is leeg, op één houten stoel na. Een oude vrouw in een zwarte jas zit erop, een versleten koffer op haar schoot. "
    "Eén smalle spot schijnt op haar; de rest van de scène blijft donker. Haar zoon staat helemaal achteraan, in de schaduw. "
    "Ze spreekt traag en zacht, met lange pauzes. Op de achtergrond klinkt het geruis van een trein."
)

VRAGEN = [
    casus(
        VOORSTELLING,
        [
            tabel(
                "Welk theaterteken is elk element?",
                [
                    ("de versleten koffer", "Rekwisiet"),
                    ("de smalle spot", "Belichting"),
                    ("de zwarte jas", "Kostumering"),
                    ("het geruis van een trein", "Geluid"),
                ],
                "Alles wat de toeschouwer ziet of hoort, draagt betekenis.",
                kolommen=["Rekwisiet", "Belichting", "Kostumering", "Geluid"],
            ),
            mk(
                "Wat drukt de afstand tussen moeder en zoon vooral uit?",
                [
                    "Een kloof in hun relatie",
                    "Dat het toneel te klein is",
                    "Dat de zoon de regisseur is",
                    "Dat het stuk een klucht is",
                ],
                0,
                "Dat is proxemiek: de ruimte tussen mensen wordt een beeld van hun verhouding.",
            ),
            keuze(
                "Het trage, zachte spreken met lange pauzes hoort bij de [[*paraverbale tekens|gestiek|fysionomie]].",
                "Toonhoogte, tempo, volume en pauzes: alles aan de stem behalve de woorden.",
            ),
            tabel(
                "Wat kan de spot op enkel de vrouw betekenen?",
                [
                    ("haar eenzaamheid", J),
                    ("dat zij centraal staat", J),
                    ("dat er een technisch probleem is", F),
                ],
                "Wat in het licht staat en wat donker blijft, is een keuze met betekenis.",
            ),
            mk(
                "Als enkel de vrouw spreekt in deze scène, is het een ...",
                ["Monoloog", "Dialoog", "Polyloog", "Rekwisiet"],
                0,
                "Eén spreker: monoloog. Twee: dialoog. Meer dan twee: polyloog.",
            ),
        ],
    ),
    sorteer(
        "Middeleeuws of modern?",
        ["Middeleeuws", "Modern"],
        [
            ["het abel spel", "Middeleeuws"],
            ["de sotternie", "Middeleeuws"],
            ["het mirakelspel", "Middeleeuws"],
            ["het absurd theater", "Modern"],
            ["spoken word", "Modern"],
            ["het documentair theater", "Modern"],
        ],
        "Episch en absurd theater zijn twintigste-eeuws.",
    ),
    koppel(
        "Welke vorm hoort bij elke omschrijving?",
        [
            ["De held gaat onafwendbaar ten onder", "Tragedie"],
            ["Een grof komisch stuk vol misverstanden", "Klucht"],
            ["Abstracte figuren als Deugd en Dood beelden een les uit", "Moraliteit"],
            ["Bijbelse verhalen op het kerkplein", "Mysteriespel"],
        ],
        ["Sonnet", "Fabel"],
        "Vier dramatische vormen.",
    ),
    casus(
        "Lees het fragment uit een toneeltekst.\n\n"
        "TOM: Waar is de trein?\n"
        "LISA: Welke trein?\n"
        "TOM: De trein waar we op wachten.\n"
        "LISA: Wachten we op een trein?\n"
        "TOM: Waarom zitten we hier anders?\n"
        "LISA: Ik weet het niet. (stilte) Waar is de trein?",
        [
            mk(
                "Bij welke vorm past dit fragment het best?",
                ["Absurd theater", "Mirakelspel", "Documentair theater", "Abel spel"],
                0,
                "Het gesprek draait in cirkels en er gebeurt niets. Net die zinloosheid is het onderwerp.",
            ),
            tabel(
                "Klopt dit over het toneelfragment?",
                [
                    ("Het is een dialoog.", J),
                    ("\"(stilte)\" is een aanwijzing voor de spelers.", J),
                    ("Het is een polyloog.", F),
                ],
                "Twee sprekers maken een dialoog. Toneelaanwijzingen staan tussen haakjes.",
            ),
        ],
    ),
    tabel(
        "Speler of ruimte?",
        [
            ("mimiek", "Speler"),
            ("gestiek", "Speler"),
            ("het decor", "Ruimte"),
            ("de belichting", "Ruimte"),
        ],
        "Gezicht en gebaren horen bij de speler; decor en licht vormen de scenische ruimte.",
        kolommen=["Speler", "Ruimte"],
    ),
    mk(
        "Midden in een stuk stapt een speler naar voren en vraagt het publiek: \"Wat zou u doen?\" Welke traditie roept dat op?",
        ["Het episch theater", "De klassieke tragedie", "De klucht", "Het mysteriespel"],
        0,
        "Het episch theater doorbreekt de illusie, zodat de toeschouwer blijft nadenken.",
    ),
    tabel(
        "Klopt dit over episch theater?",
        [
            ("Het wil dat het publiek blijft nadenken.", J),
            ("Het wil volledige inleving in de personages.", F),
            ("Het doorbreekt de illusie met opzet.", J),
        ],
        "Het doet net het omgekeerde van meeleven.",
    ),
    casus(
        "Een regisseur brengt een middeleeuwse moraliteit over de dood in een modern ziekenhuis. Elckerlijc ligt in een ziekenhuisbed, de Dood is een arts in een witte jas.",
        [
            mk(
                "Wat doet die ingreep?",
                [
                    "Hij legt een verband tussen toen en nu",
                    "Hij verandert de tekst in een klucht",
                    "Hij maakt van de moraliteit een mysteriespel",
                    "Hij schrapt alle theatertekens",
                ],
                0,
                "De tekst blijft, het kader verschuift. Je leest het stuk als iets over je eigen tijd.",
            ),
            keuze(
                "Wie onderzoekt hoe zulke keuzes op scène de tekst betekenis geven, maakt een [[*opvoeringsanalyse|tekstanalyse|rijmschema]].",
                "Dezelfde tekst kan heel verschillende voorstellingen opleveren.",
            ),
        ],
    ),
    tabel(
        "Klucht of komedie?",
        [
            ("Grove grappen, typen en veel verwarring, enkel om te lachen.", "Klucht"),
            ("Lacht met de gebreken van de personages en zegt iets over de mens.", "Komedie"),
            ("Heet in het Nederlands ook een blijspel.", "Komedie"),
        ],
        "Een klucht is grover en mikt vooral op de lach.",
        kolommen=["Klucht", "Komedie"],
    ),
    sleep(
        "Een klassiek drama is verdeeld in [[bedrijven]] en die in [[tonelen]]. Een tekst waarin het tragische en het komische samengaan, heet een [[tragikomedie]].",
        ["strofen", "verzen"],
        "Bouw en vormen van het drama.",
    ),
    tabel(
        "Is dit een theaterteken?",
        [
            ("sombere muziek onder een scène", J),
            ("de lichaamsbouw van een speler", J),
            ("een brief die een speler leest", J),
            ("de prijs van een ticket", F),
        ],
        "Fysionomie, rekwisieten en geluid dragen betekenis op scène. De ticketprijs niet.",
    ),
    mk(
        "Een stuk gebruikt vaste maskers: de gierige oude man, de slimme knecht. De spelers improviseren binnen die rollen. Welke traditie?",
        ["De commedia dell'arte", "Het abel spel", "Het documentair theater", "Spoken word"],
        0,
        "Vaste typen met maskers, en daarbinnen vrije improvisatie.",
    ),
    inv(
        "Een middeleeuws toneelstuk waarin een heilige een wonder doet, heet een ... Antwoord met één woord.",
        ["mirakelspel", "mirakel", "het mirakelspel"],
        "Een mirakel is een wonder.",
    ),
    tabel(
        "Waarom is een toneeltekst op papier niet af?",
        [
            ("De opvoering voegt licht, geluid en decor toe.", J),
            ("Lichaam en stem van de spelers komen erbij.", J),
            ("De tekens op scène kunnen de tekst zelfs tegenspreken.", J),
            ("Toneelteksten hebben geen slot.", F),
        ],
        "Daarom is dramatiek een aparte hoofdgroep: geschreven om gespeeld te worden.",
    ),
    mk(
        "Een spoken word-artiest brengt een tekst over haar oma. Wat hoort er zeker bij?",
        [
            "Ritme, stem en lichaam",
            "Een decor met kasteelmuren",
            "Vaste maskers en typen",
            "Een verdeling in vijf bedrijven",
        ],
        0,
        "De tekst is gemaakt om gehoord te worden.",
    ),
    casus(
        "Lees de samenvatting van een toneelstuk.\n\n"
        "Een machtige koning weigert naar de waarschuwingen van een ziener te luisteren. Uit trots verbant hij zijn eigen dochter. "
        "Op het einde verliest hij zijn rijk, zijn familie en zijn verstand.",
        [
            mk(
                "Welke vorm is dit?",
                ["Een tragedie", "Een klucht", "Een sotternie", "Een musical"],
                0,
                "De val van een groot personage door een eigen gebrek is de kern van de tragedie.",
            ),
            keuze(
                "De oorzaak van de val ligt hier vooral bij [[*de koning zelf|de ziener|het publiek]].",
                "In een tragedie is de held meestal zelf mee de oorzaak van zijn ondergang.",
            ),
        ],
    ),
    tabel(
        "Een scène met vijf personages die door elkaar praten. Klopt dit?",
        [
            ("Het is een polyloog.", J),
            ("De regisseur moet de aandacht van het publiek sturen.", J),
            ("Het is een monoloog.", F),
        ],
        "Poly betekent veel.",
    ),
    mk(
        "Een speler fronst, knijpt zijn ogen toe en perst zijn lippen op elkaar. Welk theaterteken?",
        ["Mimiek", "Gestiek", "Proxemiek", "Decor"],
        0,
        "Mimiek is het spel van het gezicht. Gebaren heten gestiek.",
    ),
    tabel(
        "Een voorstelling gebruikt echte getuigenissen van vluchtelingen, voorgelezen door de spelers. Klopt dit?",
        [
            ("Dat past bij documentair theater.", J),
            ("Het is een middeleeuwse vorm.", F),
            ("Het blijft een vorm van dramatiek.", J),
        ],
        "Documentair theater steunt op echte bronnen en hoort bij het hedendaagse toneel.",
    ),
    keuze(
        "Een musical laat het verhaal verdergaan via [[*zang en dans|vaste maskers|een envoi]].",
        "De liedjes onderbreken het verhaal niet, ze brengen het verder.",
    ),
    mk(
        "Welke middeleeuwse vorm is een ernstig, wereldlijk toneelstuk?",
        ["Het abel spel", "Het mirakelspel", "Het mysteriespel", "Het episch theater"],
        0,
        "Abel betekent kunstig. Mirakelspel en mysteriespel zijn religieus, episch theater is twintigste-eeuws.",
    ),
    inv(
        "Een toneeltekst met één personage dat alleen aan het woord is, heet een ... Antwoord met één woord.",
        ["monoloog", "de monoloog", "een monoloog"],
        "Bij een dialoog spreken er twee.",
    ),
    open_(
        "Je regisseert een scène waarin twee broers ruziën over een erfenis. Kies twee theatertekens en leg uit wat ze moeten uitdrukken.",
        "Proxemiek: de broers staan aan de twee uiteinden van een lange tafel, zodat hun afstand zichtbaar is. Belichting: elk staat in een eigen koude lichtvlek, het midden van de tafel blijft donker, wat de breuk tussen hen toont.",
    ),
]
