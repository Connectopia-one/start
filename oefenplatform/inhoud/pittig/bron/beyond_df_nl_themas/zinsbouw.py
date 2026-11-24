"""Zinsontleding en zinsbouw — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom die binnen nl_zinsbouw van dubbele finaliteit passen, zonder de vragen over begrippen die daar niet in staan."""
from ..beyond_nederlands_themas import zinsbouw as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23])
VRAGEN += [
    tabel("Welk zinsdeel is elk deel in de zin « Mijn zus gaf de hond een koekje na het eten. »?", [
        ("Mijn zus", "onderwerp"), ("de hond", "meewerkend voorwerp"), ("een koekje", "lijdend voorwerp"), ("na het eten", "bijwoordelijke bepaling"),
    ], "Wie geeft? Aan wie? Wat? Wanneer?", kolommen=["onderwerp", "lijdend voorwerp", "meewerkend voorwerp", "bijwoordelijke bepaling"]),
    mk("Wat is de persoonsvorm in « Morgen zullen de leerlingen hun rapport krijgen »?",
       ["zullen", "krijgen", "morgen", "leerlingen"], 0, "Maak de zin vragend of verander de tijd: de persoonsvorm verandert mee."),
    keuze("In « Omdat het regende, bleven we binnen » is « omdat het regende » een [[*bijzin|hoofdzin|persoonsvorm]].", "Een bijzin kan niet op zichzelf staan en begint hier met een voegwoord."),
    sorteer("Is dit een hoofdzin of een bijzin?", ["hoofdzin", "bijzin"], [
        ["we gaan naar zee", "hoofdzin"], ["als het mooi weer is", "bijzin"], ["dat hij te laat was", "bijzin"], ["zij lachte", "hoofdzin"],
    ], "Een bijzin begint vaak met een voegwoord en heeft de persoonsvorm achteraan."),
    mk("In « De directeur vindt het voorstel goed » is « goed » deel van:",
       ["het naamwoordelijk deel van het gezegde", "het lijdend voorwerp", "het onderwerp", "de persoonsvorm"], 0,
       "« Vindt ... goed » zegt iets over het voorstel: een naamwoordelijk deel."),
]
