"""Het oog — pittig (🚀 Boost doorstroom, biologie).

Klikvragen op het oog van natuurwetenschappen Boost doorstroom (met hun prenten) en eigen vragen over netvlies, pupilreflex en de afwijkingen uit bi_oog."""
from ..boost_do_nw_themas import prikkel as P
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(P.VRAGEN, [0, 1, 2, 3, 4, 6, 7, 15, 16, 17, 18, 22, 23, 24, 27], {"ooglens": "lens", "Ooglens": "Lens"})
VRAGEN += [
    tabel("Staafjes of kegeltjes?",
          [("zien kleuren", "kegeltjes"), ("werken vooral in het halfduister", "staafjes"), ("liggen het dichtst opeen in de gele vlek", "kegeltjes"), ("zijn heel gevoelig voor weinig licht", "staafjes")],
          "Kegeltjes geven kleur en scherpte, staafjes laten je in het halfduister nog iets zien.", ["staafjes", "kegeltjes"]),
    mk("Waarom zie je bij maanlicht bijna geen kleuren?",
       ["Dan werken vooral de staafjes, en die zien geen kleur.", "De pupil is dan zo klein dat er geen kleur binnenkomt.", "De kegeltjes liggen enkel in de blinde vlek van het oog.", "Maanlicht bevat geen enkele kleur van het spectrum."], 0,
       "Kegeltjes hebben veel licht nodig; in het halfduister nemen de staafjes het over."),
    casus("Tijdens een oogonderzoek schijnt de dokter met een lampje in het linkeroog van Yara. Beide pupillen worden kleiner.", [
        mk("Hoe heet die reactie?",
           ["de pupilreflex", "de accommodatie", "astigmatisme", "de blinde vlek"], 0,
           "De pupil vernauwt vanzelf bij fel licht: een reflex."),
        tabel("Klopt dit over de pupilreflex?",
              [("De iris regelt hoe groot de pupil is.", J), ("Yara moet zelf beslissen om haar pupil kleiner te maken.", F), ("Een kleinere pupil beschermt het netvlies tegen te veel licht.", J)],
              "De iris knijpt de pupil dicht zonder dat je erover nadenkt."),
    ]),
    sorteer("Welke afwijking is dit?", ["Bijziendheid", "Verziendheid", "Astigmatisme"],
            [("Je ziet dichtbij scherp en ver weg wazig.", "Bijziendheid"), ("Je ziet ver weg scherp en dichtbij wazig.", "Verziendheid"), ("Het hoornvlies is onregelmatig gekromd.", "Astigmatisme"), ("De oogbol is te lang.", "Bijziendheid"), ("De oogbol is te kort.", "Verziendheid")],
            "Bij bijziendheid valt het beeld vóór het netvlies, bij verziendheid erachter; bij astigmatisme buigt het licht ongelijk."),
    mk("Opa van zestig heeft altijd scherp gezien, maar moet nu zijn krant verder van zich af houden. Wat is er aan de hand?",
       ["Zijn lens is stijver, zodat accommoderen moeilijker gaat.", "Zijn oogbol is de laatste jaren veel langer geworden.", "Zijn kegeltjes zijn met de jaren allemaal kleurenblind geworden.", "Zijn blinde vlek is over de gele vlek geschoven."], 0,
       "Ouderdomsverziendheid: de lens kan niet meer bol genoeg worden voor dichtbij."),
    koppel("Welk deel van het oog hoort bij elke taak?",
           [("geeft het oog zijn kleur en regelt de pupil", "iris"), ("doorzichtige gelei die de oogbol vorm geeft", "glasachtig lichaam"), ("voedt het oog met zijn vele bloedvaten", "vaatvlies"), ("stevige, witte buitenlaag van de oogbol", "harde oogvlies")],
           ["blinde vlek", "kamervocht"], "Vier delen van het oog met elk hun taak."),
    keuze("Bij kleurenblindheid werken een of meer soorten [[*kegeltjes|staafjes|vaatvliescellen]] niet goed.",
          "Vaak gaat het om de kegeltjes voor rood of groen."),
    tabel("Klopt dit over de blinde en de gele vlek?",
          [("Op de blinde vlek liggen geen staafjes en geen kegeltjes.", J), ("In de gele vlek zie je het scherpst.", J), ("Op de blinde vlek vertrekt de oogzenuw.", J), ("In de gele vlek liggen vooral staafjes.", F)],
          "De gele vlek zit vol kegeltjes; de blinde vlek is de plek waar de oogzenuw het oog verlaat."),
    mk("Welke lens krijgt iemand met verziendheid?",
       ["een bolle lens", "een holle lens", "een lens met een gekleurd filter", "geen lens, want verziendheid geneest vanzelf"], 0,
       "Een bolle lens bundelt het licht al wat, zodat het beeld op het netvlies valt."),
    volgorde("Zet de lagen van de oogwand van buiten naar binnen.",
             ["harde oogvlies", "vaatvlies", "netvlies"],
             "Buiten de stevige beschermlaag, dan de laag met bloedvaten, binnenin de lichtgevoelige laag."),
    mk("Waarom zie je je eigen blinde vlek in het dagelijks leven niet?",
       ["De hersenen vullen het gat aan met wat het andere oog ziet.", "De blinde vlek ligt helemaal buiten het netvlies.", "De pupil sluit zich telkens als licht op de blinde vlek valt.", "Je kijkt nooit met het deel van het oog waar die vlek ligt."], 0,
       "Twee ogen en slimme hersenen: het gat valt op een andere plek in elk oog."),
    sleep("Het licht gaat door het [[hoornvlies]], de pupil en de [[lens]] en valt dan op het [[netvlies]].",
          ["vaatvlies", "iris"], "De weg van het licht door het oog."),
    tabel("Kamervocht of glasachtig lichaam?",
          [("vult de ruimte tussen hoornvlies en lens", "kamervocht"), ("vult de grote ruimte achter de lens", "glasachtig lichaam"), ("is een doorzichtige gelei", "glasachtig lichaam")],
          "Vooraan het vloeibare kamervocht, achter de lens het geleiachtige glasachtig lichaam.", ["kamervocht", "glasachtig lichaam"]),
]
