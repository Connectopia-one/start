"""Bescherming en afweer — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt, aangevuld met eigen vragen.
"""
from ..beyond_bio_themas import afweer as A, immunisatie as I
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

OVER = (
    [A.VRAGEN[i] for i in (0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 14, 15, 17, 18, 19, 21, 23, 25, 26, 27)]
    + [I.VRAGEN[i] for i in (6, 7, 10, 17, 21)]
)

EIGEN = [
    casus(
        "Noor heeft keelpijn en koorts. De dokter vermoedt een virus en schrijft geen antibiotica voor.",
        [
            mk(
                "Waarom geeft de dokter geen antibiotica?",
                ["Antibiotica werken niet tegen virussen", "Antibiotica verlagen de koorts te snel", "Antibiotica doden enkel witte bloedcellen", "Antibiotica werken enkel bij kinderen"],
                0,
                "Antibiotica grijpen in op structuren die alleen bacteriën hebben.",
            ),
            tabel(
                "Klopt dit over wat er in Noors lichaam gebeurt?",
                [
                    ("Natural killer cellen doden besmette lichaamscellen.", J),
                    ("De koorts remt de vermenigvuldiging van het virus.", J),
                    ("Haar lymfeknopen in de hals kunnen opzwellen.", J),
                    ("Ze maakt pas antistoffen als ze antibiotica neemt.", F),
                ],
                "De specifieke afweer komt na enkele dagen vanzelf op gang.",
            ),
        ],
    ),
    keuze(
        "Lymfe stroomt [[*in één richting terug naar het bloed|in een gesloten kring rond]].",
        "Lymfe wordt uit het weefselvocht opgevangen en komt via de lymfevaten terug in het bloed.",
    ),
    sleep(
        "Een [[macrofaag]] verteert een bacterie en toont daarna een stukje ervan op zijn membraan. Dat heet [[antigeenpresentatie]]. Zo kan de [[specifieke]] afweer starten.",
        ["thymus", "niet-specifieke"],
        "Antigeenpresentatie is de brug tussen de twee soorten afweer.",
    ),
    mk(
        "Wat is de taak van cytokines?",
        ["afweercellen aansturen", "bacteriën rechtstreeks doorboren", "zuur maken op de huid", "rode bloedcellen aanmaken"],
        0,
        "Cytokines zijn signaalstoffen tussen afweercellen.",
    ),
]

VRAGEN = OVER + EIGEN
