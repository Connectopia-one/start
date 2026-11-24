"""Semantiek: betekenisrelaties, gevoelswaarde en herkomst — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    tabel(
        "Welke betekenisrelatie hebben de twee woorden?",
        [
            ("fiets en rijwiel", "Synoniemen"),
            ("vroeg en laat", "Antoniemen"),
            ("bank (om op te zitten) en bank (voor geld)", "Homoniemen"),
            ("roos en bloem", "Hyponiem en hyperoniem"),
        ],
        "Zelfde betekenis, tegengestelde betekenis, zelfde vorm met andere betekenis, en enger tegenover ruimer.",
        kolommen=["Synoniemen", "Antoniemen", "Homoniemen", "Hyponiem en hyperoniem"],
    ),
    casus(
        "Twee krantenberichten over hetzelfde voorval.\n\n"
        "A. \"Honderd betogers trokken zaterdag door de straten.\"\n"
        "B. \"Honderd relschoppers trokken zaterdag door de straten.\"",
        [
            mk(
                "Wat is het verschil tussen de twee berichten?",
                [
                    "De connotatie van één woord",
                    "Het aantal mensen in de straten",
                    "De dag waarop het gebeurde",
                    "De denotatie van het werkwoord",
                ],
                0,
                "Allebei kunnen ze naar dezelfde mensen verwijzen, maar het beeld verschilt.",
            ),
            keuze(
                "\"Relschoppers\" heeft een [[*negatieve|neutrale|positieve]] connotatie.",
                "Het woord draagt een afkeurende bijklank mee.",
            ),
            tabel(
                "Klopt dit over de betekenis van deze woorden?",
                [
                    ("Denotatie is de kale betekenis.", J),
                    ("Connotatie is de bijklank van een woord.", J),
                    ("De woordkeuze stuurt het oordeel van de lezer.", J),
                    ("Synoniemen hebben altijd dezelfde gevoelswaarde.", F),
                ],
                "Woning en krot verwijzen allebei naar een huis, maar roepen een ander gevoel op.",
            ),
        ],
    ),
    sorteer(
        "Pleonasme, tautologie of contaminatie?",
        ["Pleonasme", "Tautologie", "Contaminatie"],
        [
            ["een witte schimmel", "Pleonasme"],
            ["nooit en te nimmer", "Tautologie"],
            ["duur kosten", "Contaminatie"],
            ["uitprinten", "Contaminatie"],
            ["altijd en eeuwig", "Tautologie"],
            ["een ronde cirkel", "Pleonasme"],
        ],
        "Een pleonasme voegt toe wat al in het woord zit; een tautologie zegt hetzelfde twee keer; een contaminatie kruist twee uitdrukkingen.",
    ),
    casus(
        "Een bedrijf schrijft in een persbericht: \"Door een herstructurering nemen we afscheid van tweehonderd medewerkers.\"",
        [
            mk(
                "Wat staat er eigenlijk?",
                [
                    "Tweehonderd mensen worden ontslagen",
                    "Tweehonderd mensen gaan met pensioen",
                    "Er komen tweehonderd mensen bij",
                    "Tweehonderd mensen krijgen een feest",
                ],
                0,
                "Het harde woord wordt vervangen door vagere, zachtere woorden.",
            ),
            keuze(
                "\"Herstructurering\" en \"afscheid nemen\" zijn hier [[*eufemismen|dysfemismen|archaïsmen]].",
                "Een eufemisme verzacht iets onaangenaams.",
            ),
        ],
    ),
    tabel(
        "Eufemisme of dysfemisme?",
        [
            ("heengaan voor sterven", "Eufemisme"),
            ("creperen voor sterven", "Dysfemisme"),
            ("senioren voor oude mensen", "Eufemisme"),
            ("een hok voor een kleine kamer", "Dysfemisme"),
        ],
        "Een dysfemisme maakt iets ruwer dan nodig.",
        kolommen=["Eufemisme", "Dysfemisme"],
    ),
    koppel(
        "Welk begrip over herkomst hoort bij elk woord?",
        [
            ["computer", "Leenwoord"],
            ["googelen", "Neologisme"],
            ["immer", "Archaïsme"],
            ["droogkuis", "Belgicisme"],
        ],
        ["Hyperoniem", "Antoniem"],
        "Overgenomen, nieuw, verouderd of enkel in België.",
    ),
    mk(
        "Wat is het hyperoniem van stoel, tafel en kast?",
        ["Meubel", "Keuken", "Hout", "Huisraad van de keuken"],
        0,
        "Het ruimere begrip waar alle drie onder vallen.",
    ),
    tabel(
        "Klopt dit over pleonasmen en woordherkomst?",
        [
            ("Een pleonasme kan bewust gebruikt worden voor nadruk.", J),
            ("Een archaïsme is een woord dat pas ontstaan is.", F),
            ("Een anglicisme komt uit het Engels.", J),
            ("Een bastaardwoord is altijd een inheems woord.", F),
        ],
        "Een bastaardwoord is een leenwoord dat zich deels aan onze spelling aanpaste.",
    ),
    casus(
        "Lees het zinnetje uit een sportverslag.\n\n\"Na de rode kaart nam de trainer de benen, en zijn spelers lieten de moed niet zakken.\"",
        [
            tabel(
                "Letterlijk of figuurlijk?",
                [
                    ("de benen nemen", "Figuurlijk"),
                    ("de moed niet laten zakken", "Figuurlijk"),
                    ("de rode kaart", "Letterlijk"),
                ],
                "Vaste uitdrukkingen lees je figuurlijk.",
                kolommen=["Letterlijk", "Figuurlijk"],
            ),
            keuze(
                "\"De benen nemen\" betekent: [[*er snel vandoor gaan|gaan lopen voor de sport|zijn benen laten verzorgen]].",
                "Wie het letterlijk leest, krijgt een onzinnig beeld.",
            ),
        ],
    ),
    mk(
        "Je schrijft een zakelijke brief en twijfelt tussen \"overlijden\" en \"creperen\". Waar let je op?",
        [
            "Gevoelswaarde en register",
            "Het aantal letters",
            "Welk woord het oudst is",
            "Welk woord een homoniem is",
        ],
        0,
        "Twee woorden kunnen hetzelfde betekenen en toch niet allebei passen.",
    ),
    sleep(
        "\"Optelefoneren\" is een [[contaminatie]] van opbellen en telefoneren. \"Rekentuig\" voor computer is een [[purisme]]. \"Confituur\" is in België gangbaar en dus een [[belgicisme]].",
        ["tautologie", "neologisme"],
        "Fouten en herkomst.",
    ),
    tabel(
        "Waarom helpt kennis van betekenisrelaties bij het schrijven?",
        [
            ("Je kan variëren met synoniemen.", J),
            ("Je herhaalt je minder.", J),
            ("Je vermijdt fouten als pleonasmen.", J),
            ("Je hoeft geen woordenboek meer te gebruiken.", F),
        ],
        "Wie de relaties kent, schrijft gevarieerder en preciezer.",
    ),
    casus(
        "Lees de zinnen.\n\n"
        "1. \"Ik heb het met mijn eigen ogen gezien.\"\n"
        "2. \"Hij keerde weer terug naar huis.\"\n"
        "3. \"Dat valt niet te ontkennen of te loochenen.\"",
        [
            tabel(
                "Welke fout of stijlfiguur is elke zin?",
                [
                    ("zin 1", "Pleonasme"),
                    ("zin 2", "Pleonasme"),
                    ("zin 3", "Tautologie"),
                ],
                "Eigen ogen en weer terug voegen toe wat al in het woord zit; ontkennen en loochenen betekenen hetzelfde.",
                kolommen=["Pleonasme", "Tautologie", "Contaminatie"],
            ),
            keuze(
                "Zin 1 is geen fout als je de [[*nadruk|denotatie|herkomst]] bewust wil versterken.",
                "Een pleonasme kan een stijlmiddel zijn.",
            ),
        ],
    ),
    tabel(
        "Hyponiem van \"fruit\" of niet?",
        [
            ("appel", J),
            ("peer", J),
            ("wortel", F),
            ("banaan", J),
        ],
        "Een wortel is een groente.",
    ),
    mk(
        "Een tekst spreekt over \"het probleem\" in plaats van \"de uitdaging\". Wat doet die keuze?",
        [
            "Ze kleurt het oordeel van de lezer",
            "Ze verandert de feiten zelf",
            "Ze maakt de tekst korter en zakelijker",
            "Ze is een contaminatie",
        ],
        0,
        "Hetzelfde gegeven, een andere bijklank.",
    ),
    tabel(
        "Leenwoord uit welke taal?",
        [
            ("weekend", "Engels"),
            ("paraplu", "Frans"),
            ("überhaupt", "Duits"),
        ],
        "Anglicisme, gallicisme, germanisme.",
        kolommen=["Engels", "Frans", "Duits"],
    ),
    keuze(
        "Woorden als \"appen\" en \"streamen\" zijn [[*neologismen|archaïsmen|purismen]].",
        "Ze ontstonden met de technologie waarnaar ze verwijzen.",
    ),
    tabel(
        "Klopt dit over synoniemen?",
        [
            ("Ze zijn zelden volledig gelijk.", J),
            ("Ze verschillen vaak in toon of gebruik.", J),
            ("Je kan ze altijd zomaar uitwisselen.", F),
        ],
        "Overlijden en creperen betekenen hetzelfde, maar passen in heel andere situaties.",
    ),
    mk(
        "\"Een woning\" en \"een krot\" verwijzen allebei naar een huis. Waarin verschillen ze?",
        ["In de connotatie", "In de denotatie", "In de herkomst", "In het aantal klanken"],
        0,
        "De kale betekenis is gelijk; de bijklank niet.",
    ),
    inv(
        "Twee woorden met dezelfde vorm maar een andere, onverwante betekenis, zoals \"slot\": hoe heten die? Antwoord met één woord.",
        ["homoniemen", "homoniem"],
        "Een slot op de deur en het slot van een verhaal.",
    ),
    keuze(
        "\"Gij\" en \"immer\" klinken in een hedendaagse tekst [[*verouderd|modern|Engels]].",
        "Archaïsmen duiken nog op in oudere teksten of plechtige stijl.",
    ),
    tabel(
        "Gaat het begrip over betekenis of over herkomst?",
        [
            ("hyperoniem", "Betekenis"),
            ("leenwoord", "Herkomst"),
            ("antoniem", "Betekenis"),
            ("dialectisme", "Herkomst"),
        ],
        "Sommige begrippen zeggen wat een woord betekent, andere waar het vandaan komt.",
        kolommen=["Betekenis", "Herkomst"],
    ),
    mk(
        "In \"de mond van de rivier\" is \"mond\":",
        ["Figuurlijk gebruikt", "Een homoniem van mond", "Een antoniem", "Een archaïsme"],
        0,
        "Een rivier heeft geen mond zoals een mens; het beeld is ingeburgerd.",
    ),
    keuze(
        "\"Optelefoneren\" verbeter je tot [[*opbellen of telefoneren|optelefoneren met een koppelteken|optelefonen]].",
        "Bij een contaminatie kies je een van de twee correcte uitdrukkingen.",
    ),
    open_(
        "Geef zelf een voorbeeld van een pleonasme, een tautologie en een contaminatie, en verbeter ze.",
        "Pleonasme: een natte regen; verbetering: regen. Tautologie: enkel en alleen; verbetering: alleen. Contaminatie: dat kost duur; verbetering: dat is duur of dat kost veel.",
    ),
]
