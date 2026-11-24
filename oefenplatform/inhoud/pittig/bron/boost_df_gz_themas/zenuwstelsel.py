"""Het zenuwstelsel en de reflexen — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_zenuwstelsel, met een zelfgetekend schema van de
hersenen en het ruggenmerg, aangevuld met de neuronprent en enkele vragen uit
biologie Boost doorstroom."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL
from ..boost_do_bi_themas import zenuwstelsel as _z

HS = Prent("hersenen-schema", "Schema van de hersenen en het ruggenmerg", "zijaanzicht met grote hersenen, hersenbalk, kleine hersenen, hersenstam, ruggenmerg en een zenuw, met letters A tot F")
HS.ellips(470, 230, 300, 185, "#f6d6d0", DONKER, 3)                       # grote hersenen
HS.pad("M 300 260 Q 470 190 640 260", "none", "#b07a70", 14)               # hersenbalk
HS.ellips(650, 420, 120, 70, "#e8c0b8", DONKER, 3)                        # kleine hersenen
HS.rect(470, 360, 70, 150, "#dca89e", DONKER, 12, 3)                      # hersenstam
HS.rect(482, 505, 46, 90, "#f0e0b0", DONKER, 8, 3)                        # ruggenmerg
HS.lijn(528, 560, 700, 590, "#c0763a", 5)                                  # zenuw
LET = {"A": (250, 120), "B": (190, 320), "C": (850, 430), "D": (330, 430), "E": (330, 560), "F": (820, 590)}
for t, (x, y) in LET.items():
    HS.letter(x, y, t)
HS.lijn(212, 320, 320, 255, DONKER, 1); HS.lijn(828, 430, 770, 425, DONKER, 1); HS.lijn(352, 430, 470, 430, DONKER, 1)
HS.lijn(352, 560, 482, 560, DONKER, 1); HS.lijn(798, 590, 690, 588, DONKER, 1)
U = "hersenen-schema.svg"
Z = {t: Prent.rond(x, y, 30) for t, (x, y) in LET.items()}

VRAGEN = [_z.VRAGEN[i] for i in (0, 1, 2, 3, 4, 9, 13, 19)] + [
    klik("Klik op de letter bij het deel waar je denkt en taal maakt.", U, [Z["A"]],
         "De grote hersenen zijn het grootste deel."),
    klik("Klik op de letter bij de brug tussen de linker en de rechter hersenhelft.", U, [Z["B"]],
         "De hersenbalk verbindt de twee helften."),
    klik("Klik op de letter bij het deel dat je evenwicht bewaart.", U, [Z["C"]],
         "De kleine hersenen liggen achteraan onder de grote hersenen."),
    klik("Klik op de letter bij het deel dat je ademhaling en hartslag regelt.", U, [Z["D"]],
         "De hersenstam regelt wat altijd door moet lopen."),
    klik("Klik op de letter bij het deel dat in de wervelkolom loopt en ook bij het centraal zenuwstelsel hoort.", U, [Z["E"]],
         "Het ruggenmerg loopt in de wervelkolom."),
    klik("Klik op de letter bij het deel van het perifere zenuwstelsel.", U, [Z["F"]],
         "Een zenuw buiten hersenen en ruggenmerg hoort bij het perifere zenuwstelsel."),
    tabel("Hoort dit deel bij het centraal zenuwstelsel?",
          [("de kleine hersenen", J), ("een ruggenmergzenuw", F), ("het ruggenmerg", J), ("een hersenzenuw", F)],
          "Enkel de hersenen en het ruggenmerg vormen het centraal zenuwstelsel."),
    koppel("Koppel de soort zenuw aan wat ze doet.",
           [("sensibele zenuw", "voert de impuls van de receptor naar binnen"), ("motorische zenuw", "voert de impuls naar een spier of klier"), ("gemengde zenuw", "bevat beide soorten vezels")],
           ["verbindt de twee hersenhelften"],
           "De hersenbalk verbindt de helften, dat is geen zenuw."),
    volgorde("Zet de weg van de impuls in de reflexboog in de juiste volgorde.",
             ["receptor", "sensorisch neuron", "schakelneuron", "motorisch neuron", "effector"],
             "Het schakelneuron ligt in het ruggenmerg."),
    sleep("Een impuls komt binnen via de [[dendriet]], loopt door het [[cellichaam]] en gaat via het [[axon]] naar de [[eindknop]].",
          ["hersenbalk", "spierbuik"],
          "Dendrieten vangen op, het axon geeft door."),
    keuze("De impuls gaat sneller doordat hij van [[*knoop naar knoop|dendriet naar dendriet|synaps naar synaps]] springt.",
          "De knopen van Ranvier zijn de onderbrekingen in de myelineschede."),
    keuze("De stof die de eindknop in de synaps afgeeft, heet een [[*neurotransmitter|myelineschede|receptor]].",
          "Ze steekt de kleine spleet over."),
    inv("Hoe heten de cellen die de myelineschede rond het axon maken? Hoogstens twee woorden.",
        ["schwann-cellen", "schwanncellen", "cellen van schwann", "schwann cellen"],
        "Elke Schwann-cel wikkelt zich rond een stuk van het axon."),
    sorteer("Loopt deze reflex via het ruggenmerg of via de hersenstam?", ["ruggenmerg", "hersenstam"],
            [("de kniepeesreflex", "ruggenmerg"), ("de pupilreflex", "hersenstam"), ("de terugtrekreflex bij een hete plaat", "ruggenmerg"), ("de slikreflex", "hersenstam"), ("de speekselreflex", "hersenstam")],
            "Pupil-, slik- en speekselreflex lopen via de hersenstam."),
    mk("Waarom trek je je hand van een hete plaat weg nog voor je de pijn voelt?",
       ["de reflexboog via het ruggenmerg is korter", "de grote hersenen werken altijd trager dan de spieren", "de huid stuurt de spier zelf aan zonder zenuw", "de pijnprikkel bereikt nooit de hersenen"],
       0, "De impuls gaat pas daarna ook naar de grote hersenen, waar je de pijn voelt."),
    mk("Wat is het verschil tussen een reflex en een gewilde beweging?",
       ["bij een gewilde beweging beslissen de grote hersenen", "bij een reflex werkt er helemaal geen enkele spier mee", "een gewilde beweging loopt altijd via de hersenstam", "een reflex kan alleen in je benen voorkomen"],
       0, "Bij een reflex beslis je niet zelf."),
    tabel("Bewust of onbewust?",
          [("een boek kiezen in de bib", "bewust"), ("je hart dat sneller klopt", "onbewust"), ("zweten als het warm is", "onbewust"), ("de straat oversteken", "bewust")],
          "Onbewuste reacties gebeuren zonder dat je beslist.", ["bewust", "onbewust"]),
    casus("Bij de huisarts tikt de dokter met een hamertje net onder de knie van Wout. Zijn onderbeen schiet naar voren.", [
        inv("Hoe heet deze reflex? Hoogstens twee woorden.", ["kniepeesreflex", "de kniepeesreflex", "kniereflex"], "De kniepeesreflex."),
        keuze("De spier van het bovenbeen is hier de [[*effector|receptor|synaps]].", "De effector voert de reactie uit."),
        keuze("Het schakelneuron van deze reflex ligt in [[*het ruggenmerg|de grote hersenen|de kleine hersenen]].", "De reflexboog loopt via het ruggenmerg."),
        mk("Waarom test de dokter deze reflex?",
           ["om na te gaan of de reflexboog goed werkt", "om de spier van het bovenbeen sterker te maken", "om te meten hoe groot de grote hersenen zijn", "om het kraakbeen in de knie extra in te smeren"],
           0, "Een reflex die ontbreekt of te sterk is, kan op een probleem in de zenuwen wijzen."),
    ]),
    open_("Leg uit waarom een reflex je lichaam beschermt. Geef een voorbeeld.",
          "Een reflex is een snelle reactie zonder dat je beslist. Als je een hete plaat raakt, trek je je hand al terug voor je de pijn voelt. Zo is de schade kleiner."),
]
