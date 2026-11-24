"""Fotosynthese en celademhaling — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt, aangevuld met eigen vragen.
"""
from ..beyond_bio_themas import energie as E
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

OVER = [E.VRAGEN[i] for i in (0, 4, 5, 9, 10, 11, 13, 14, 16, 17, 19, 20, 24, 25, 26)]

EIGEN = [
    casus(
        "Een leerling zet een geraniumplant een nacht in het donker. Daarna bedekt ze één blad half met aluminiumfolie en zet ze de plant een dag in de zon. "
        "Ze kookt het blad, ontkleurt het in warme alcohol en druppelt er een oplossing op.",
        [
            keuze(
                "Ze druppelt [[*joodoplossing|kalkwater|fenolftaleïne]] op het blad.",
                "Jood kleurt zetmeel blauwzwart.",
            ),
            tabel(
                "Welke kleur verwacht je na het druppelen?",
                [
                    ("het deel dat in de zon lag", "blauwzwart"),
                    ("het deel onder de folie", "bruingeel"),
                    ("een blad van een tweede plant die de hele dag in de kast stond", "bruingeel"),
                ],
                "Enkel waar licht viel, werd glucose gemaakt en als zetmeel opgeslagen.",
                kolommen=["blauwzwart", "bruingeel"],
            ),
            mk(
                "Waarom stond de plant eerst een nacht in het donker?",
                ["om het oude zetmeel op te gebruiken", "om de huidmondjes in het blad te laten openen", "om nieuw chlorofyl in het blad te laten groeien", "om de plant extra water te laten opnemen"],
                0,
                "Zo weet je zeker dat het zetmeel dat je ziet, die dag gemaakt is.",
            ),
        ],
    ),
    sorteer(
        "Is dit organisme autotroof of heterotroof?",
        ["Autotroof", "Heterotroof"],
        [
            ("een eik", "Autotroof"),
            ("een champignon", "Heterotroof"),
            ("een koe", "Heterotroof"),
            ("een groene alg", "Autotroof"),
            ("gist", "Heterotroof"),
        ],
        "Autotroof maakt zelf organische stof uit anorganische stoffen.",
    ),
    tabel(
        "Exo-energetisch of endo-energetisch?",
        [
            ("de fotosynthese", "endo-energetisch"),
            ("de celademhaling", "exo-energetisch"),
            ("ATP wordt ADP en fosfaat", "exo-energetisch"),
            ("ADP en fosfaat worden ATP", "endo-energetisch"),
        ],
        "Wat energie vastlegt, is endo-energetisch; wat ze vrijgeeft, exo-energetisch.",
        kolommen=["exo-energetisch", "endo-energetisch"],
    ),
    keuze(
        "Een cel [[*maakt ATP voortdurend opnieuw aan|slaat ATP op voor weken]].",
        "ATP is een werkmunt, geen voorraad.",
    ),
    volgorde(
        "Zet de weg van het water in een plant in volgorde.",
        ["wortelhaar", "schors van de wortel", "xyleem in de stengel", "blad", "huidmondje"],
        "Opwaarts transport, aangetrokken door de verdamping.",
    ),
    mk(
        "Op een warme, winderige dag stijgt het water sneller in de houtvaten. Waarom?",
        ["De verdamping trekt harder", "Het floëem duwt het water dan extra omhoog", "De wortel maakt dan veel meer glucose aan", "De huidmondjes gaan dicht door de sterke wind"],
        0,
        "Meer verdamping geeft meer zuigkracht.",
    ),
    tabel(
        "Klopt dit over melkzuurgisting in een spier?",
        [
            ("Ze treedt op bij te weinig zuurstof.", J),
            ("Melkzuur kan de spier verzuren.", J),
            ("Ze levert meer ATP dan de aerobe celademhaling.", F),
            ("Het pyrodruivenzuur wordt omgezet in melkzuur.", J),
        ],
        "Gisting breekt glucose maar gedeeltelijk af.",
    ),
    mk(
        "Wat gebeurt er met overtollige glucose in een plant?",
        ["Ze wordt als zetmeel opgeslagen", "Ze wordt als ATP bewaard", "Ze wordt als zuurstof afgegeven", "Ze wordt terug CO2 en water"],
        0,
        "Bijvoorbeeld in een aardappelknol.",
    ),
    koppel(
        "Koppel het product aan het proces dat het maakt.",
        [
            ("yoghurt", "melkzuurgisting door bacteriën"),
            ("brood dat rijst", "alcoholische gisting door gist"),
            ("zuurstofgas", "lichtreactie van de fotosynthese"),
            ("glucose", "donkerreactie van de fotosynthese"),
        ],
        ["glycolyse in de chloroplast"],
        "Elk proces heeft zijn eigen eindproduct.",
    ),
    inv(
        "Bij de fotosynthese zijn 6 moleculen CO2 nodig voor 1 molecule glucose. Hoeveel moleculen CO2 zijn nodig voor 4 moleculen glucose?",
        ["24"],
        "4 x 6 = 24.",
    ),
    open_(
        "Leg uit waarom een plant in een afgesloten glazen stolp in het licht langer overleeft dan in het donker.",
        "In het licht maakt de plant met fotosynthese glucose en zuurstof, meer dan ze zelf met celademhaling verbruikt. In het donker loopt enkel de celademhaling: de zuurstof raakt op en er wordt geen nieuwe glucose meer gemaakt.",
    ),
]

VRAGEN = OVER + EIGEN
