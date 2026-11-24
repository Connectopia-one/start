"""Woordvelden: school, werk, geld en verkeer — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the job advert.\n\n"
    "TRAINEE SHOP ASSISTANT – Greenway Supermarkets\n"
    "Are you 18 or over and looking for your first job? We offer a six-month training programme with a weekly wage of £320. "
    "You will work shifts, including some weekends, and help customers at the till. "
    "No degree is required, but you must be friendly and reliable. "
    "To apply, send your CV and a cover letter to jobs@greenway.co.uk before 30 June. "
    "Please include the name of one reference, for example a teacher or a former employer."
)

TEKST2 = (
    "Read the text.\n\n"
    "Every morning, Priya commutes from Brighton to London. The single fare is £32, so she bought a season ticket, "
    "which saves her almost £2,000 a year. Yesterday her train was delayed by forty minutes because of a signal failure. "
    "As the delay was longer than thirty minutes, she can claim a partial refund online. "
    "She also had to take a taxi from the station, which she cannot really afford: since prices went up, she has been almost broke at the end of each month."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat dit in de vacature (over school, werk en geld)?",
                [
                    ("Je moet een universitair diploma hebben.", F),
                    ("Je werkt soms ook in het weekend.", J),
                    ("Je krijgt elke week betaald.", J),
                    ("Je moet een aanbevelingsbrief meesturen.", F),
                ],
                "No degree is required; alleen de naam van een referentie.",
            ),
            mk(
                "Wat moet je opsturen om te solliciteren?",
                ["Een cv en een motivatiebrief", "Alleen je diploma en een foto", "Een ingevuld formulier van de winkel", "Een brief van je ouders"],
                0,
                "Send your CV and a cover letter.",
            ),
            keuze(
                "« You will work shifts » betekent dat je [[*in ploegen|alleen 's morgens]] werkt.",
                "A shift is een ploeg of een beurt.",
            ),
            mk(
                "Wie kan je opgeven als « reference »?",
                ["Een leraar", "Een vriend van je leeftijd", "Een klant van de winkel", "Jezelf, met een korte uitleg"],
                0,
                "A teacher or a former employer.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Waarom kocht Priya een abonnement?",
                ["Het is goedkoper", "Ze reist maar af en toe", "Een enkel ticket bestaat niet", "Haar baas betaalt het"],
                0,
                "It saves her almost £2,000 a year.",
            ),
            mk(
                "Waarom kan Priya een deel van haar geld terugvragen?",
                ["Meer dan een halfuur vertraging", "Haar trein was helemaal afgeschaft", "Ze moest daarna een dure taxi nemen", "Haar abonnement was eigenlijk te duur"],
                0,
                "As the delay was longer than thirty minutes, she can claim a partial refund.",
            ),
            keuze(
                "Priya kan de taxi [[*eigenlijk niet betalen|makkelijk betalen]].",
                "She cannot really afford it.",
            ),
            inv(
                "Hoeveel minuten vertraging had haar trein? Schrijf het getal.",
                ["40", "veertig"],
                "Delayed by forty minutes.",
            ),
        ],
    ),
    koppel(
        "Koppel elk Engels woord aan zijn betekenis (over school, werk en geld).",
        [
            ("a receipt", "een kasticket"),
            ("a discount", "een korting"),
            ("a loan", "een lening"),
            ("a fare", "de prijs van een rit"),
        ],
        ["een boete"],
        "Een boete is a fine.",
    ),
    sorteer(
        "Hoort dit bij school of bij verkeer?",
        ["School", "Verkeer"],
        [
            ("a term", "School"),
            ("a roundabout", "Verkeer"),
            ("a lecture", "School"),
            ("a traffic jam", "Verkeer"),
            ("a pedestrian crossing", "Verkeer"),
        ],
        "A term is een trimester, a lecture een hoorcollege.",
    ),
    tabel(
        "Klopt deze betekenis in het Brits Engels (over school, werk en geld)?",
        [
            ("the pavement – het voetpad", J),
            ("a public school – een gratis overheidsschool", F),
            ("a return ticket – heen en terug", J),
            ("a pupil – een student aan de universiteit", F),
        ],
        "Een Britse public school is een dure privéschool; a pupil zit op school.",
    ),
    mk(
        "« I scraped through the maths exam. » Hoe deed de spreker het?",
        ["Net geslaagd", "Met grote onderscheiding", "Niet geslaagd", "Hij deed niet mee"],
        0,
        "To scrape through is er net door geraken.",
    ),
    mk(
        "« The factory closed and 200 workers were made redundant. » Wat gebeurde er met de arbeiders?",
        ["Ontslagen", "Ze kregen opslag", "Ze gingen met pensioen", "Ze werden overgeplaatst"],
        0,
        "To be made redundant: om economische redenen ontslagen worden.",
    ),
    mk(
        "« Sorry, that size is out of stock. » Wat betekent dat?",
        ["Niet in voorraad", "Die maat is in solden", "Die maat is te duur", "Die maat is besteld"],
        0,
        "Out of stock: niet in voorraad.",
    ),
    mk(
        "« We missed the deadline by one day. » Wat gebeurde er?",
        ["Een dag te laat", "Een dag te vroeg ingediend", "De datum werd verschoven", "Het werk was op tijd klaar"],
        0,
        "To miss a deadline: de uiterste datum niet halen.",
    ),
    mk(
        "« Prices include VAT. » Wat zit er in de prijs?",
        ["De btw", "De verzendkosten", "Een korting", "Een terugbetaling"],
        0,
        "VAT is value added tax: onze btw.",
    ),
    mk(
        "« I'm broke until payday. » Wat zegt de spreker?",
        ["Platzak", "Ik heb iets gebroken", "Ik ben ziek tot de betaaldag", "Ik heb veel spaargeld"],
        0,
        "To be broke: geen geld meer hebben.",
    ),
    keuze(
        "Een « commuter » reist elke dag naar zijn [[*werk|vakantieadres]].",
        "To commute: pendelen.",
    ),
    keuze(
        "Op een bankrekening betekent « interest » de [[*rente|interesse]].",
        "Interest is hier rente.",
    ),
    keuze(
        "« Mind the gap » waarschuwt voor de ruimte tussen [[*perron en trein|twee treinen]].",
        "The gap is de opening.",
    ),
    inv(
        "Vul aan met één Engels woord: « Please ___ in your essay by Friday. »",
        ["hand"],
        "To hand in: inleveren.",
    ),
    inv(
        "Vul aan met één Engels woord: « I'd like to ___ for the job of receptionist. »",
        ["apply"],
        "To apply for: solliciteren naar.",
    ),
    tabel(
        "Gaat dit over geld dat je terugkrijgt?",
        [
            ("a refund", J),
            ("a debt", F),
            ("change", J),
            ("a bargain", F),
        ],
        "Change is wisselgeld; a bargain is een koopje.",
    ),
    mk(
        "« Our English seminar has only twelve students. » Wat is a seminar?",
        ["Een les in kleine groep", "Een hoorcollege in een grote zaal", "Een examen op het einde van het jaar", "Een uitstap met de hele klas"],
        0,
        "A lecture is groot, a seminar klein.",
    ),
    mk(
        "« I'm on a tight schedule this week. » Wat betekent dat?",
        ["Mijn week zit vol", "Ik heb deze week vakantie", "Ik moet deze week strenger zijn", "Mijn uurrooster is kwijt"],
        0,
        "A tight schedule: een strak tijdschema.",
    ),
    keuze(
        "« That jacket was a real bargain. » De jas was [[*een koopje|veel te duur]].",
        "A bargain is iets goedkoops.",
    ),
    inv(
        "Vul aan met één Engels woord: « There's a long ___ jam on the motorway. »",
        ["traffic"],
        "A traffic jam is een file.",
    ),
    volgorde(
        "Zet de stappen van een sollicitatie in de juiste volgorde.",
        ["een vacature lezen", "een cv en een cover letter sturen", "uitgenodigd worden voor een job interview", "de job krijgen"],
        "To apply, then an interview, then the job.",
    ),
    sleep(
        "Ik kan me geen nieuwe auto [[afford]]. Daarom vraag ik een [[loan]] aan bij de bank. Ik moet daar [[interest]] op betalen.",
        ["refund", "discount"],
        "Lenen kost rente.",
    ),
    open_(
        "Schrijf in het Engels twee zinnen voor een klacht: je kocht een jas die na een week scheurde en je wil je geld terug.",
        "I bought this coat in your shop last week, but it has already torn. I would like a full refund, please; here is my receipt.",
    ),
]
