"""Bijvoeglijke naamwoorden, bijwoorden en voorzetsels — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text.\n\n"
    "My elder brother Jack is two years older than me, but I am taller than him. "
    "He is good at maths and he always works hard, whereas I hardly ever do my homework on time. "
    "Last week he drove us to Brighton. He drives more carefully than Dad, so it took a bit longer. "
    "We arrived in Brighton at noon. It was the hottest day of the year, and luckily the sea was calm."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat dit in de tekst?",
                [
                    ("Jack is ouder dan de verteller.", J),
                    ("Jack is groter dan de verteller.", F),
                    ("De verteller maakt zijn huiswerk bijna nooit op tijd.", J),
                    ("Jack rijdt sneller dan papa.", F),
                ],
                "Taller than him; hardly ever; more carefully: dus trager.",
            ),
            keuze(
                "« Elder » staat hier vóór het naamwoord; na to be zeg je [[*older|elder]] than.",
                "He is older than me, nooit elder than.",
            ),
            mk(
                "Waarom staat er « carefully » en niet « careful »?",
                ["Het hoort bij het werkwoord", "Het staat na het werkwoord to be", "Het is een overtreffende trap", "Het zegt iets over Dad zelf"],
                0,
                "Bij een werkwoord hoort een bijwoord: he drives carefully.",
            ),
            inv(
                "Welk voorzetsel staat in de tekst voor « Brighton » na arrived?",
                ["in"],
                "To arrive in bij een stad of land.",
            ),
        ],
    ),
    tabel(
        "Vergrotende trap: juist of fout?",
        [
            ("hotter", J),
            ("more easy", F),
            ("worse", J),
            ("more beautiful", J),
            ("gooder", F),
        ],
        "Easier en better; korte woorden -er, lange woorden more.",
    ),
    sleep(
        "Today is [[colder]] than yesterday, but tomorrow will be the [[coldest]] day of the week. It's not as cold [[as]] in Norway, though.",
        ["more cold", "than", "most cold"],
        "Cold, colder, the coldest; not as … as.",
    ),
    mk(
        "« The film was so ___ that I fell asleep. » Welke vorm past?",
        ["boring", "bored", "boringly", "bore"],
        0,
        "-ing is de eigenschap van de film; -ed het gevoel van de kijker.",
    ),
    mk(
        "« I was really ___ when I heard the news. » Welke vorm past?",
        ["shocked", "shocking", "shockingly", "shock"],
        0,
        "-ed beschrijft het gevoel van de persoon.",
    ),
    mk(
        "Welke volgorde is juist?",
        ["a lovely old wooden table", "a wooden old lovely table", "an old lovely wooden table", "a lovely wooden old table"],
        0,
        "Mening, leeftijd, materiaal.",
    ),
    mk(
        "« The harder you train, ___ you'll be. » Welke vorm past?",
        ["the fitter", "fitter", "the more fit than", "the fittest"],
        0,
        "The … -er, the … -er: hoe meer, hoe beter.",
    ),
    mk(
        "« She speaks English very ___. » Welke vorm past?",
        ["well", "good", "goodly", "best"],
        0,
        "Het bijwoord van good is well.",
    ),
    mk(
        "« Turn left ___ the traffic lights. » Welk voorzetsel past?",
        ["at", "on", "in", "by"],
        0,
        "At bij een punt.",
    ),
    tabel(
        "In, on of at?",
        [
            ("___ Christmas", "at"),
            ("___ 25 December", "on"),
            ("___ December", "in"),
            ("___ the morning", "in"),
            ("___ midnight", "at"),
        ],
        "At bij een tijdstip of feest, on bij een dag, in bij een maand of dagdeel.",
        kolommen=["in", "on", "at"],
    ),
    tabel(
        "For of since?",
        [
            ("I've known her ___ ten years.", "for"),
            ("They've lived here ___ 2015.", "since"),
            ("We've been waiting ___ an hour.", "for"),
            ("She's been ill ___ Monday.", "since"),
        ],
        "For bij een duur, since bij een beginpunt.",
        kolommen=["for", "since"],
    ),
    koppel(
        "Koppel het werkwoord aan zijn vaste voorzetsel.",
        [
            ("to depend", "on"),
            ("to listen", "to"),
            ("to be interested", "in"),
            ("to be afraid", "of"),
        ],
        ["with"],
        "Vaste voorzetsels leer je met het werkwoord samen.",
    ),
    keuze(
        "« He [[*hardly|hard]] slept last night, so he's exhausted. »",
        "Hardly is amper.",
    ),
    keuze(
        "« She [[*is always|always is]] late for school. »",
        "Bij to be staat always erna.",
    ),
    keuze(
        "« He [[*often forgets|forgets often]] his keys. »",
        "Bij een gewoon werkwoord staat het frequentiebijwoord ervoor.",
    ),
    keuze(
        "« The train arrived [[*late|lately]] because of the snow. »",
        "Late is ook een bijwoord; lately betekent onlangs.",
    ),
    inv(
        "Maak een bijwoord van « angry »: « She slammed the door ___. »",
        ["angrily"],
        "-y wordt -ily.",
    ),
    inv(
        "Vul de overtreffende trap in van « bad »: « That was the ___ meal I've ever had. »",
        ["worst"],
        "Bad, worse, worst.",
    ),
    inv(
        "Vul het voorzetsel in: « My sister is married ___ an Irishman. »",
        ["to"],
        "Married to.",
    ),
    mk(
        "« This is by far the ___ question on the test. » Welke vorm past?",
        ["most difficult", "difficultest", "more difficult", "difficult"],
        0,
        "Lange woorden: the most.",
    ),
    mk(
        "Welke zin over de auto's is juist?",
        ["We've got two new cars.", "We've got two news cars.", "We've got two cars new.", "We've got two car news."],
        0,
        "Een bijvoeglijk naamwoord krijgt geen s en staat voor het naamwoord.",
    ),
    tabel(
        "Is dit een bijwoord zonder -ly dat juist gebruikt is?",
        [
            ("He runs fast.", J),
            ("She works hardly every day.", F),
            ("We got up early.", J),
        ],
        "Fast, hard, early en late blijven zonder -ly.",
    ),
    mk(
        "« I'm not very good ___ remembering names. » Welk voorzetsel past?",
        ["at", "in", "on", "for"],
        0,
        "To be good at something.",
    ),
    keuze(
        "« This exercise is [[*easier|more easy]] than the last one. »",
        "Easy wordt easier.",
    ),
    volgorde(
        "Zet deze bijwoorden van vaak naar zelden.",
        ["always", "usually", "sometimes", "rarely", "never"],
        "Frequentiebijwoorden staan vaak vóór het werkwoord.",
    ),
    mk(
        "« Her story sounded rather far-fetched. » Wat vond men van het verhaal?",
        ["Ongeloofwaardig", "Heel boeiend en spannend", "Erg lang en saai", "Heel grappig"],
        0,
        "Far-fetched: vergezocht.",
    ),
    open_(
        "Leg in het Nederlands uit waarom het « She looks happy » is, maar « She smiled happily ».",
        "Look is hier een koppelwerkwoord, net als to be: het zegt hoe ze eruitziet, dus volgt er een bijvoeglijk naamwoord. Smile is een gewoon werkwoord, en hoe ze glimlacht zeg je met een bijwoord op -ly.",
    ),
]
