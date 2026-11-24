"""Taal en identiteit: stereotypering, inclusie en non-verbale communicatie — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "In een tv-reeks spreekt de enige boer met een zwaar dialect. Hij snapt de grappen nooit, praat traag en doet altijd domme dingen. De stadsmensen in de reeks spreken verzorgd standaardtaal.",
        [
            mk(
                "Wat gebeurt hier?",
                [
                    "Taal wordt aan een karaktertrek gekoppeld",
                    "Het dialect wordt correct beschreven",
                    "De reeks toont alle perspectieven op het platteland",
                    "Er wordt elitair taalgebruik bestreden",
                ],
                0,
                "Het accent moet de kijker meteen iets over de persoon doen denken.",
            ),
            tabel(
                "Waarop berust zo'n stereotype?",
                [
                    ("versimpeling", J),
                    ("overdrijving", J),
                    ("veralgemening", J),
                    ("zorgvuldig onderzoek", F),
                ],
                "Eén trek wordt uitvergroot en op een hele groep geplakt.",
            ),
            keuze(
                "Zo'n stereotype zegt vaak meer over [[*wie het gebruikt|de groep zelf|het dialect]].",
                "Het vertelt meer over de maker dan over de boeren.",
            ),
        ],
    ),
    sorteer(
        "Sluit deze taalkeuze in of uit?",
        ["Inclusie", "Exclusie"],
        [
            ["een gemeentebrief in eenvoudige taal", "Inclusie"],
            ["genderneutrale woorden in een vacature", "Inclusie"],
            ["dialect in een vergadering met iemand uit een andere streek", "Exclusie"],
            ["jargon in een uitleg voor buitenstaanders", "Exclusie"],
            ["elitair taalgebruik in een openbaar debat", "Exclusie"],
        ],
        "Taal kan mensen samenbrengen of buitensluiten, ook zonder kwade bedoeling.",
    ),
    casus(
        "Sara zegt tegen haar vriendin: \"Nee hoor, alles is in orde.\" Ze kijkt weg, haar stem trilt en ze houdt haar armen gekruist.",
        [
            tabel(
                "Welk signaal is wat?",
                [
                    ("\"alles is in orde\"", "Verbaal"),
                    ("haar stem trilt", "Paraverbaal"),
                    ("ze kijkt weg", "Non-verbaal"),
                    ("gekruiste armen", "Non-verbaal"),
                ],
                "Paraverbaal is alles aan de stem behalve de woorden; non-verbaal is lichaam, blik en uiterlijk.",
                kolommen=["Verbaal", "Paraverbaal", "Non-verbaal"],
            ),
            mk(
                "Wat doet de vriendin het best?",
                [
                    "De woorden tegen de signalen afwegen",
                    "Enkel geloven wat Sara met woorden zegt",
                    "Het gesprek meteen afbreken",
                    "Luider praten zodat Sara luistert",
                ],
                0,
                "Spreken verbaal en non-verbaal elkaar tegen, dan gelooft een luisteraar meestal het lichaam.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over taal en identiteit?",
        [
            ("Je taalgebruik is een deel van wie je bent.", J),
            ("Een accent zegt iets over iemands verstand.", F),
            ("Je oordeelt zelf ook over anderen op hun taal.", J),
            ("Een andere variëteit betekent andere ideeën.", F),
        ],
        "Dat verband leggen is zelf een stereotype.",
    ),
    mk(
        "Je merkt dat je een sollicitant meteen minder slim vond door haar accent. Wat doe je?",
        [
            "Je stelt je oordeel bij op wat ze zegt",
            "Je volgt je eerste indruk, die klopt meestal",
            "Je vraagt haar om zonder accent te praten",
            "Je laat het gesprek over aan een collega",
        ],
        0,
        "Het oordeel komt vanzelf; wat je ermee doet, is een keuze.",
    ),
    tabel(
        "Paraverbaal of non-verbaal?",
        [
            ("intonatie", "Paraverbaal"),
            ("tempo", "Paraverbaal"),
            ("oogcontact", "Non-verbaal"),
            ("kleding", "Non-verbaal"),
        ],
        "Paraverbaal zit in de stem, non-verbaal in de rest.",
        kolommen=["Paraverbaal", "Non-verbaal"],
    ),
    casus(
        "Je leest in een groepschat: \"WAAROM HEEFT NIEMAND DE SLIDES GEMAAKT\". Een minuut later: \"Top, echt super van jullie.\"",
        [
            keuze(
                "De hoofdletters werken in geschreven taal als [[*schreeuwen|fluisteren|een emoji]].",
                "Hoofdletters zijn het equivalent van volume.",
            ),
            mk(
                "Waarom wordt het tweede bericht makkelijk verkeerd begrepen?",
                [
                    "Toon en gezicht ontbreken",
                    "Het bevat te veel hoofdletters",
                    "Het is geschreven in dialect",
                    "Het heeft geen slotgroet",
                ],
                0,
                "Zonder stem en gezicht zegt de tekst letterlijk het tegenovergestelde.",
            ),
            tabel(
                "Welke middelen werken als non-verbale signalen in geschreven taal?",
                [
                    ("emoji's", J),
                    ("hoofdletters", J),
                    ("interpunctie", J),
                    ("de betekenis van de woorden", F),
                ],
                "De woorden zelf zijn verbaal.",
            ),
        ],
    ),
    mk(
        "Tijdens zijn spreekbeurt kijkt Ilias geen enkele keer op van zijn blad. Wat gebeurt er met de zaal?",
        [
            "Hij verliest de band met de zaal",
            "De zaal verstaat hem duidelijker en beter",
            "De zaal onthoudt meer van zijn tekst",
            "De zaal hoort zijn intonatie beter",
        ],
        0,
        "Zonder oogcontact wordt de zaal een muur.",
    ),
    tabel(
        "Welke signalen horen bij een open houding tijdens een gesprek?",
        [
            ("oogcontact maken", J),
            ("je naar de spreker toe draaien", J),
            ("op je telefoon kijken", F),
            ("knikken terwijl de ander spreekt", J),
        ],
        "Op je telefoon kijken doet net het omgekeerde.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["De melodie en toonhoogte van een zin", "Intonatie"],
            ["Het duidelijk uitspreken van de klanken", "Articulatie"],
            ["De uitdrukking op iemands gezicht", "Mimiek"],
            ["De afstand die je tot de ander bewaart", "Proxemiek"],
        ],
        ["Register", "Jargon"],
        "Vier signalen naast de woorden.",
    ),
    mk(
        "Een spreker praat snel en zonder één pauze. Wat is het risico?",
        [
            "De luisteraar kan niet volgen",
            "De luisteraar voelt zich ingesloten",
            "De spreker klinkt meer ontspannen",
            "De woorden worden formeler",
        ],
        0,
        "Zonder pauzes krijgt de luisteraar geen tijd om te verwerken.",
    ),
    keuze(
        "Twee collega's spreken dialect terwijl een nieuwe collega uit een andere streek erbij zit. Zonder het te willen, zorgen ze voor [[*exclusie|inclusie|intonatie]].",
        "Niemand bedoelt het kwaad, en toch sluit de taalkeuze iemand buiten.",
    ),
    tabel(
        "Een spreker wil nadruk leggen. Welk paraverbaal middel kan hij gebruiken?",
        [
            ("een pauze laten vallen", J),
            ("het volume verhogen", J),
            ("vette letters", F),
        ],
        "Vette letters horen bij geschreven taal.",
    ),
    sleep(
        "Te dichtbij staan voelt [[opdringerig]], te ver voelt [[koel]]. Wat gepast is, verschilt per [[cultuur]].",
        ["formeel", "dialect"],
        "Proxemiek in een gesprek.",
    ),
    casus(
        "Een vacature van een ziekenhuis luidt: \"Wij zoeken een verpleegkundige (m/v/x). Je werkt in een warm team waar iedereen welkom is.\" Een andere vacature: \"Wij zoeken een stevige kerel die van aanpakken weet.\"",
        [
            tabel(
                "Klopt dit?",
                [
                    ("De eerste vacature probeert iedereen aan te spreken.", J),
                    ("De tweede vacature sluit een deel van de lezers uit.", J),
                    ("Woordkeuze heeft geen invloed op wie solliciteert.", F),
                ],
                "Genderneutrale taal wil iedereen aangesproken laten voelen.",
            ),
            keuze(
                "\"(m/v/x)\" is een voorbeeld van [[*genderneutrale taal|elitair taalgebruik|vakjargon]].",
                "Zo laat men niemand buiten.",
            ),
        ],
    ),
    mk(
        "Een gemeente herschrijft haar brieven in eenvoudige taal. Wat wil ze vooral bereiken?",
        [
            "Dat meer inwoners de brief begrijpen",
            "Dat de brieven korter en goedkoper worden",
            "Dat de brieven formeler gaan klinken",
            "Dat de ambtenaren minder werk hebben",
        ],
        0,
        "Heldere taal is een vorm van toegankelijkheid.",
    ),
    tabel(
        "Klopt dit over kleding en uiterlijk?",
        [
            ("Ze horen bij de non-verbale signalen.", J),
            ("Ze kleuren mee hoe serieus je genomen wordt.", J),
            ("Ze dragen niets bij aan je boodschap.", F),
        ],
        "Ook wat je draagt, vertelt iets.",
    ),
    mk(
        "Je gesprekspartner leunt achteruit en kijkt weg terwijl jij praat. Wat doe je het best?",
        [
            "Je past je tempo of onderwerp aan",
            "Je praat gewoon in hetzelfde tempo verder",
            "Je spreekt luider en met meer vakjargon",
            "Je stopt meteen en verlaat het gesprek",
        ],
        0,
        "Lichaamstaal geeft je het signaal om op je gesprekspartner in te spelen.",
    ),
    keuze(
        "Een strip laat alle Fransen met een baguette en een baret rondlopen. Dat is een [[*stereotype|register|dialect]].",
        "Een versimpeld, overdreven beeld van een hele groep.",
    ),
    tabel(
        "Wat win je als je weet hoe stereotypering werkt?",
        [
            ("Je merkt sneller wanneer je zelf te snel oordeelt.", J),
            ("Je kan erop terugkomen.", J),
            ("Je hoeft dan nooit meer na te denken over anderen.", F),
        ],
        "Wie het mechanisme kent, betrapt zichzelf sneller.",
    ),
    inv(
        "Het buitensluiten van mensen door taal heet ... Antwoord met één woord.",
        ["exclusie", "uitsluiting"],
        "Het tegendeel is inclusie.",
    ),
    tabel(
        "Een spreker voor een groep. Wat helpt de aandacht vasthouden?",
        [
            ("een open houding", J),
            ("een gebaar op het juiste moment", J),
            ("een blik in de zaal", J),
            ("met de rug naar het publiek staan", F),
        ],
        "Lichaamstaal brengt je boodschap beter over.",
    ),
    keuze(
        "Wie slecht [[*articuleert|intoneert|gestikuleert]], wordt moeilijk verstaan, hoe goed de tekst ook is.",
        "Articulatie is het duidelijk uitspreken van de klanken.",
    ),
    open_(
        "Geef een voorbeeld van een situatie waarin taal iemand uitsluit, en leg uit hoe je dat kan vermijden.",
        "Op een familiefeest praten neven en nichten in jongerentaal en met veel Engelse woorden, terwijl grootmoeder erbij zit. Zij volgt niet meer en voelt zich buitengesloten. Door af en toe in gewone taal te praten en haar mee in het gesprek te betrekken, sluit je haar weer in.",
    ),
]
