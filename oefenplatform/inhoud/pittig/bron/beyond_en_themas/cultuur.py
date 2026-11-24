"""Woordvelden: kunst, literatuur, politiek en reizen — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the review.\n\n"
    "The Silent River, the award-winning first novel by Grace Owen, is set in a Welsh mining village in the 1920s. "
    "The narrator is Tom, a twelve-year-old boy whose father goes on strike with the other miners. "
    "The plot moves slowly in the first chapters, but the last part is gripping. "
    "Owen describes the poverty of the village without ever becoming sentimental. "
    "The novel is being adapted for the screen, and filming starts next year. Highly recommended."
)

TEKST2 = (
    "Read the text.\n\n"
    "In last week's election, turnout was only 52%, the lowest in twenty years. "
    "Many young voters said they did not trust any of the candidates. "
    "The new Prime Minister has promised a bill to reduce poverty and to make the voting age sixteen. "
    "However, the bill still has to be approved by both the House of Commons and the House of Lords before it can become law."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Wie vertelt het verhaal?",
                ["Tom", "Grace Owen", "Toms vader", "Een anonieme mijnwerker uit het dorp"],
                0,
                "The narrator is Tom.",
            ),
            tabel(
                "Staat dit in de recensie?",
                [
                    ("Het boek speelt in de jaren 1920.", J),
                    ("Het is het tweede boek van Grace Owen.", F),
                    ("Het begin van het boek gaat traag.", J),
                    ("De film is al in de bioscoop.", F),
                ],
                "First novel; filming starts next year.",
            ),
            mk(
                "Wat vindt de recensent van het boek?",
                ["Een aanrader", "Het is te sentimenteel", "Het is te kort", "Het einde is saai"],
                0,
                "Highly recommended en gripping.",
            ),
            keuze(
                "« The setting » van dit boek is [[*een mijndorp in Wales|een stad in Engeland]].",
                "Set in a Welsh mining village.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Wat zegt de tekst over de opkomst?",
                ["Ze was laag", "Ze was de hoogste in twintig jaar", "Ze was gewoon zoals altijd", "Ze was niet gemeten"],
                0,
                "Turnout was only 52%, the lowest in twenty years.",
            ),
            mk(
                "Wat moet er nog gebeuren voor het voorstel wet wordt?",
                ["Beide Kamers keuren het goed", "De koning ondertekent het meteen", "Er komt een nieuwe verkiezing", "De jongeren stemmen erover"],
                0,
                "Approved by both the House of Commons and the House of Lords.",
            ),
            keuze(
                "« A bill » is hier een [[*wetsontwerp|rekening]].",
                "Zodra het goedgekeurd is, heet het an act.",
            ),
        ],
    ),
    koppel(
        "Koppel elk Engels woord aan zijn betekenis.",
        [
            ("heritage", "erfgoed"),
            ("a quotation", "een citaat"),
            ("a chapter", "een hoofdstuk"),
            ("a century", "een eeuw"),
        ],
        ["een bibliotheek"],
        "A library is een bibliotheek.",
    ),
    sorteer(
        "Hoort dit bij literatuur of bij politiek?",
        ["Literatuur", "Politiek"],
        [
            ("a protagonist", "Literatuur"),
            ("a ballot", "Politiek"),
            ("a sonnet", "Literatuur"),
            ("a candidate", "Politiek"),
            ("a polling station", "Politiek"),
        ],
        "A ballot is een stembiljet, a polling station een stembureau.",
    ),
    tabel(
        "Hoort dit land bij het Verenigd Koninkrijk?",
        [
            ("Scotland", J),
            ("Ireland (de republiek)", F),
            ("Wales", J),
            ("Northern Ireland", J),
        ],
        "Het VK is Engeland, Schotland, Wales en Noord-Ierland.",
    ),
    mk(
        "« Sorry, we're fully booked tonight. » Wat zegt de receptionist?",
        ["Er is geen plaats meer", "We hebben veel boeken", "Je reservatie is bevestigd", "Het hotel is vanavond gesloten"],
        0,
        "Fully booked: volzet.",
    ),
    mk(
        "« Next year I'd like to study abroad. » Waar wil de spreker studeren?",
        ["In het buitenland", "Aan een hogeschool in de buurt", "Thuis, via het internet", "Op een boot"],
        0,
        "Abroad, zonder voorzetsel: in of naar het buitenland.",
    ),
    mk(
        "« The teachers went on strike for higher pay. » Wat deden de leraars?",
        ["Staken", "Ze sloegen de leerlingen", "Ze gaven extra lessen", "Ze stapten op"],
        0,
        "To go on strike: gaan staken.",
    ),
    mk(
        "« The campaign aims to raise awareness of loneliness. » Wat wil de campagne?",
        ["Mensen bewust maken", "Geld inzamelen voor een nieuw ziekenhuis", "Eenzame mensen een huis geven", "Mensen wakker maken in de ochtend"],
        0,
        "To raise awareness: aandacht vragen.",
    ),
    mk(
        "« Thousands of refugees crossed the border. » Wie staken de grens over?",
        ["Vluchtelingen", "Toeristen op vakantie", "Soldaten van het leger", "Grenswachters"],
        0,
        "A refugee is een vluchteling.",
    ),
    mk(
        "Wat is het verschil tussen Great Britain en the United Kingdom?",
        ["Bij het VK hoort ook Noord-Ierland", "Er is geen enkel verschil tussen beide", "Great Britain is groter dan het VK", "Het VK is enkel Engeland"],
        0,
        "Great Britain is het eiland met Engeland, Schotland en Wales.",
    ),
    keuze(
        "In het Engels schrijf je « the works of Shakespeare » met een meervoud omdat het over [[*zijn werken|zijn werkuren]] gaat.",
        "Work is ontelbaar als arbeid, maar telbaar als kunstwerk.",
    ),
    keuze(
        "« An MP » is een [[*parlementslid|militair politieagent]].",
        "Member of Parliament.",
    ),
    keuze(
        "« A charity shop » verkoopt [[*tweedehands spullen voor een goed doel|dure merkkleren]].",
        "A charity is een goed doel.",
    ),
    inv(
        "Vul aan met één Engels woord: « The museum has a new ___ about Roman Britain. » (tentoonstelling)",
        ["exhibition"],
        "An exhibition is een tentoonstelling.",
    ),
    inv(
        "Vul aan met één Engels woord: « Shakespeare was born in the sixteenth ___. »",
        ["century"],
        "The sixteenth century: de zestiende eeuw.",
    ),
    tabel(
        "Klopt deze vertaling?",
        [
            ("a bookshop – een boekwinkel", J),
            ("a library – een boekwinkel", F),
            ("a review – een recensie", J),
            ("a novel – een nieuwtje", F),
        ],
        "A novel is een roman.",
    ),
    volgorde(
        "Zet deze periodes in de juiste volgorde, oudste eerst.",
        ["the Middle Ages", "the Victorian era", "the twenty-first century"],
        "Middeleeuwen, dan de 19de eeuw onder koningin Victoria, dan nu.",
    ),
    mk(
        "« Monday is a bank holiday. » Wat betekent dat?",
        ["Een officiële feestdag", "Een dag waarop enkel de banken open zijn", "Een dag om je bankzaken te regelen", "Een vakantiedag voor bankbedienden"],
        0,
        "In het VK heten de wettelijke feestdagen bank holidays.",
    ),
    mk(
        "« The film is an adaptation of a Jane Austen novel. » Wat is de film?",
        ["Een verfilming", "Een documentaire over haar leven", "Een parodie op haar stijl", "Een toneelstuk over haar"],
        0,
        "An adaptation: een bewerking.",
    ),
    mk(
        "« Voter turnout was very low. » Wat was er laag?",
        ["De opkomst", "Het aantal kandidaten", "De lonen van de politici", "Het aantal partijen"],
        0,
        "Turnout: het deel van de kiezers dat ging stemmen.",
    ),
    keuze(
        "« Poverty » betekent [[*armoede|rijkdom]].",
        "Rijkdom is wealth.",
    ),
    inv(
        "Vul aan met één Engels woord: « Wordsworth was a famous English ___ who wrote about nature. » (dichter)",
        ["poet"],
        "A poet schrijft poems.",
    ),
    sleep(
        "Een stad bezoeken is [[sightseeing]]. Een hotelkamer reserveren is to [[book]] a room. Een begeleid bezoek aan een museum is a guided [[tour]].",
        ["trip", "visit"],
        "The sights zijn de bezienswaardigheden.",
    ),
    open_(
        "Schrijf in het Engels twee zinnen over een boek of film die je aanraadt: waar speelt het en wie is de hoofdpersoon?",
        "I would recommend Wonder. It is set in New York, and the protagonist is a boy called Auggie who goes to school for the first time.",
    ),
]
