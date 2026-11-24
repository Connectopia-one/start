"""Organische stoffen — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen chemie Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt, aangevuld met eigen vragen.
"""
from ..beyond_chem_themas import organisch as O, eigenschappen as E
from .vormen import J, F, mk, tabel, koppel, sleep, casus

OVER = (
    [O.VRAGEN[i] for i in (0, 1, 3, 6, 7, 8, 14, 15, 16, 19, 21, 25, 27)]
    + [E.VRAGEN[i] for i in (4, 5, 10, 11, 12, 17, 24, 27)]
)

EIGEN = [
    casus(
        "Na een barbecue zit er een vette vlek op een T-shirt. Water alleen haalt ze niet weg; met zeep lukt het wel.",
        [
            mk(
                "Waarom lost water de vetvlek niet op?",
                ["Vet is apolair en water polair", "Vet is polair en water apolair", "Water vormt geen waterstofbruggen", "Vet heeft een te laag kookpunt"],
                0,
                "Gelijk lost op in gelijk.",
            ),
            sleep(
                "Een zeepmolecule heeft een lange [[apolaire]] staart die in het vet gaat zitten, en een [[polaire]] kop die naar het water wijst. Rond de vetdruppel ontstaat zo een [[micel]].",
                ["ion", "ester"],
                "Zo kan het water de vetdruppel meenemen.",
            ),
        ],
    ),
    koppel(
        "Koppel de gebruiksnaam aan de stof.",
        [
            ("aardgas", "methaan"),
            ("brandspiritus", "methanol"),
            ("formol", "methanal"),
            ("mierenzuur", "methaanzuur"),
        ],
        ["propanon"],
        "Vier stoffen met één koolstofatoom, elk uit een andere stofklasse.",
    ),
    tabel(
        "Klopt dit over etheen?",
        [
            ("Het is een alkeen.", J),
            ("Het heeft een dubbele binding tussen de twee koolstofatomen.", J),
            ("Het is een verzadigde koolwaterstof.", F),
        ],
        "Door de dubbele binding is etheen onverzadigd.",
    ),
    mk(
        "Je moet een vlek van kaarsvet uit een tafelkleed halen. Welk oplosmiddel kies je?",
        ["wasbenzine", "water", "azijn", "zout water"],
        0,
        "Kaarsvet is apolair, dus een apolair oplosmiddel.",
    ),
]

VRAGEN = OVER + EIGEN
