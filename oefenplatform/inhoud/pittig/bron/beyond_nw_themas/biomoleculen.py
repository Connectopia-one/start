"""Biomoleculen — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt,
aangevuld met een eigen vraag.
"""
from ..beyond_bio_themas import biomoleculen as B
from .vormen import J, F, tabel

VRAGEN = [B.VRAGEN[i] for i in range(28) if i != 24] + [
    tabel(
        "Welke bouwstenen komen vrij bij de volledige vertering?",
        [
            ("zetmeel", "glucose"),
            ("een eiwit", "aminozuren"),
            ("een triglyceride", "glycerol en vetzuren"),
        ],
        "Hydrolyse breekt de polymeren terug af tot hun bouwstenen.",
        kolommen=["glucose", "aminozuren", "glycerol en vetzuren"],
    ),
]
