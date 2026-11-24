"""Van prikkel tot reactie en het zenuwstelsel — pittig (🚀 Boost doorstroom, biologie).

Pittige vragen van natuurwetenschappen Boost doorstroom (met hun prenten) die binnen bi_zenuwstelsel passen, zonder de actiepotentiaal en het autonome zenuwstelsel, plus eigen vragen over de hersendelen."""
from ..boost_do_nw_themas import zenuwstelsel as Z, prikkel as P
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

_V = {"ruggenmerg": "ruggemerg", "conductor": "zenuwbaan", "In de grensstrengen": "In de kleine hersenen"}
VRAGEN = kies(Z.VRAGEN, [0, 1, 2, 3, 4, 11, 13, 14, 15, 16, 17, 21, 24, 25, 27], _V) + kies(P.VRAGEN, [8, 9, 12, 21], _V)
VRAGEN += [
    sorteer("Welk deel van de hersenen regelt dit vooral?", ["Grote hersenen", "Kleine hersenen", "Hersenstam"],
            [("een wiskundeprobleem oplossen", "Grote hersenen"), ("je evenwicht bewaren op een fiets", "Kleine hersenen"), ("je hartslag regelen tijdens de slaap", "Hersenstam"), ("een nieuw woord leren", "Grote hersenen"), ("een vloeiende beweging bij het dansen", "Kleine hersenen"), ("je ademhaling aanhouden zonder erbij na te denken", "Hersenstam")],
            "Denken en leren in de grote hersenen, bewegingen afstemmen in de kleine hersenen, levensnoodzakelijke functies in de hersenstam."),
    mk("Na een val kan iemand nog denken en praten, maar loopt hij wankel en mist hij zijn doel als hij iets wil pakken. Welk deel is waarschijnlijk geraakt?",
       ["de kleine hersenen", "de hersenstam", "het ruggemerg onder de nek", "de sensorische zenuwen in de hand"], 0,
       "De kleine hersenen stemmen bewegingen af en bewaren het evenwicht; denken en praten gebeuren elders."),
    tabel("Centraal of perifeer zenuwstelsel?",
          [("de hersenstam", "centraal"), ("een zenuw in je been", "perifeer"), ("het ruggemerg", "centraal"), ("de zenuwen naar de vingers", "perifeer")],
          "Hersenen en ruggemerg vormen het centrale zenuwstelsel; alle zenuwen daarbuiten het perifere.", ["centraal", "perifeer"]),
    casus("Ilse ziet op straat een bal op zich afkomen en vangt hem. Even later stapt ze op een scherpe steen en trekt haar voet meteen terug.", [
        tabel("Bewuste reactie of reflex?",
              [("de bal vangen", "bewuste reactie"), ("de voet terugtrekken", "reflex"), ("de bal daarna terug naar een vriend gooien", "bewuste reactie")],
              "Bij het vangen beslissen de grote hersenen; bij de steen schakelt het ruggemerg al over.", ["bewuste reactie", "reflex"]),
        mk("Waarom is de tweede reactie sneller dan de eerste?",
           ["Het signaal schakelt al in het ruggemerg over.", "De receptoren in de voet zijn gevoeliger dan de ogen.", "De spieren in het been zijn sterker dan die in de arm.", "Licht reist trager dan een prikkel in de huid."], 0,
           "De reflexboog maakt geen omweg langs de grote hersenen."),
        mk("Welk soort neuron brengt het bevel naar de beenspier?",
           ["een motorisch neuron", "een sensorisch neuron", "een receptor in de huid", "een neuron in de kleine hersenen"], 0,
           "Motorische neuronen brengen het bevel van het centrale zenuwstelsel naar een effector."),
    ]),
    keuze("Signalen gaan van het lichaam naar het centrale zenuwstelsel langs [[*sensorische|motorische|myeline]] zenuwen.",
          "Sensorisch betekent gevoelig: die zenuwen voeren prikkels aan."),
    mk("Iemand met een dwarslaesie hoog in het ruggemerg voelt zijn benen niet meer en kan ze niet bewegen. Waarom allebei?",
       ["Het ruggemerg geleidt signalen in beide richtingen.", "De benen hebben vanaf dan geen eigen receptoren meer.", "De grote hersenen werken niet meer na de val.", "De spieren van de benen zijn helemaal verdwenen."], 0,
       "Het ruggemerg brengt gevoel naar de hersenen én bevelen naar de spieren; als het onderbroken is, valt beide weg."),
]
