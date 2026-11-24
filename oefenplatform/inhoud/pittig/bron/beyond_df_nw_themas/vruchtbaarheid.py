"""Vruchtbaarheid, anticonceptie en kinderwens — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen biologie Beyond (zelfde prenten), enkel wat in nwd_vruchtbaarheid staat, plus eigen vragen."""
from ..beyond_bio_themas import vruchtbaarheid as V
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

_V = {"vasectomie": "sterilisatie bij de man", "Vasectomie": "Sterilisatie bij de man",
      "spermatogenese": "aanmaak van zaadcellen", "hormoonimplantaat": "hormoonstaafje"}

VRAGEN = kies(V.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 16, 17, 19, 21, 22, 25, 26, 27], _V) + [
    tabel("Natuurlijke methode of niet?", [
        ("de temperatuurmethode", "natuurlijk"), ("de combinatiepil", "niet natuurlijk"),
        ("de ovulatiemethode", "natuurlijk"), ("het koperspiraal", "niet natuurlijk"),
    ], "Natuurlijke methoden gebruiken geen middel of ingreep.", kolommen=["natuurlijk", "niet natuurlijk"]),
    mk("Een koppel probeert al acht maanden zwanger te worden. Spreekt men al van onvruchtbaarheid?",
       ["Nee, pas na ongeveer een jaar onbeschermd vrijen", "Ja, na zes maanden spreekt men altijd van onvruchtbaarheid",
        "Ja, als het na drie maanden niet lukt", "Nee, pas na vijf jaar zonder zwangerschap"], 0,
       "De afspraak is een jaar regelmatig onbeschermd vrijen."),
    tabel("Verlaagt dit de vruchtbaarheid?", [
        ("roken", J), ("zware stress gedurende lange tijd", J), ("een onbehandelde chlamydia-infectie", J), ("gezond en gevarieerd eten", F),
    ], "Roken, stress en een onbehandelde soa kunnen de vruchtbaarheid verlagen."),
    keuze("De minipil bevat [[*alleen een progestageen|oestrogeen en progestageen]].", "De combinatiepil bevat er twee."),
    inv("Een prikpil werkt ongeveer drie maanden. Hoeveel prikken heeft een vrouw nodig voor een heel jaar?", ["4", "vier"],
        "12 maanden : 3 = 4."),
    volgorde("Zet de stappen van een IVF in de juiste volgorde.", [
        "hormonen laten meerdere follikels rijpen", "de eicellen worden opgehaald", "eicel en zaadcellen samen in het labo",
        "een embryo wordt in de baarmoeder teruggeplaatst",
    ], "Enkel de bevruchting en de eerste dagen gebeuren in het labo."),
    open_("Leg uit waarom een condoom aangeraden blijft, ook als iemand de pil neemt.",
          "De pil houdt de eisprong tegen, maar beschermt niet tegen soa's. Een condoom doet dat wel.",
          "Alleen condooms en onthouding beschermen tegen soa's."),
]
