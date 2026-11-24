"""Productlabels, pictogrammen en risico's van stoffen — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Enkele pittige vragen chemie Beyond over gevarenpictogrammen (zelfde prent), verder eigen vragen binnen nwd_labels."""
from ..beyond_chem_themas import veilig as V
from ..beyond_chem_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(V.VRAGEN, [0, 1, 2, 3, 7]) + [
    casus(
        "Op het etiket van een fles ontstopper staat: het pictogram voor bijtend, de zin « Veroorzaakt ernstige brandwonden en oogletsel » "
        "en de zinnen « Draag handschoenen » en « Buiten het bereik van kinderen bewaren ». Op een verdunde versie van hetzelfde product staat enkel het uitroepteken.",
        [
            keuze("« Veroorzaakt ernstige brandwonden » is een [[*H-zin|P-zin]].", "H van hazard: het gevaar."),
            keuze("« Draag handschoenen » is een [[*P-zin|H-zin]].", "P van precaution: de voorzorg."),
            mk("Waarom staat er op de verdunde versie een ander pictogram?",
               ["Minder geconcentreerd geeft minder gevaar.", "Een verdunde stof is een heel andere stof.", "Het pictogram hangt af van de prijs van de fles.", "Verdunde stoffen hoeven eigenlijk geen etiket."], 0,
               "Dezelfde stof kan in een andere concentratie een ander pictogram krijgen."),
            keuze("Een halfvolle fles ontstopper breng je naar het [[*klein gevaarlijk afval|gft|pmd]].", "Kga, op het containerpark."),
            keuze("Je mag ontstopper en bleekwater [[*nooit|gerust]] samen in de afvoer gieten.", "Ze kunnen reageren en giftige gassen vormen."),
        ],
    ),
    koppel("Koppel elk pictogram aan zijn betekenis.", [
        ["vlam", "ontvlambaar"], ["vlam boven een cirkel", "oxiderend, voedt een brand"],
        ["gasfles", "gassen onder druk"], ["doodshoofd", "acuut giftig"],
    ], ["goed voor het milieu"], "Geen enkel gevarenpictogram betekent iets goeds."),
    sorteer("In welke afvalzak of bak hoort dit?", ["gft", "pmd", "kga"], [
        ["aardappelschillen", "gft"], ["een lege drankkarton", "pmd"], ["een restje verf", "kga"],
        ["koffiedik", "gft"], ["een conservenblik", "pmd"], ["een fles thinner met een restje", "kga"],
    ], "Gft: groente, fruit en tuin. Pmd: plastic, metaal, drankkartons. Kga: klein gevaarlijk afval."),
    tabel("Klopt dit over de recyclagecode met de driehoek van pijltjes?", [
        ("Het cijfer zegt uit welke kunststof de verpakking bestaat.", J),
        ("De code betekent dat de verpakking zeker gerecycleerd wordt.", F),
        ("Code 1 hoort bij PET, de stof van de meeste drinkflessen.", J),
    ], "De code zegt enkel welke kunststof het is."),
    mk("Je garage wordt in de zomer erg warm. Waar zet je de fles thinner het best?",
       ["gesloten in een koele kast, ver van vuur", "open op de vensterbank, in de volle zon", "naast de verwarmingsketel, lekker droog", "in een lege drankfles op het aanrecht"], 0,
       "Warmte doet een ontvlambare stof vlotter verdampen."),
    mk("Je kiest tussen twee ontvetters die even goed werken. De ene is bijtend, de andere alleen irriterend. Welke kies je?",
       ["de irriterende", "de bijtende, want die werkt sneller", "maakt niet uit, ze werken even goed", "allebei samen voor het beste resultaat"], 0,
       "Het product met het minst zware gevaar."),
    mk("Waarom is een stof met een laag kookpunt vaak gemakkelijk ontvlambaar?",
       ["Ze verdampt vlot, er hangt damp boven.", "Ze bevat altijd heel veel water.", "Ze is bij kamertemperatuur altijd vast.", "Ze kookt nooit, ook niet bij hoge temperatuur."], 0,
       "De damp vat vlam."),
    mk("Je hebt een olievlek op je trui. Waarmee krijg je die het best weg?",
       ["met een vetoplosbaar middel", "met veel koud water en verder niets", "met een emmer zout water", "met citroensap en een beetje suiker"], 0,
       "Soort lost soort: vet lost op in een vetoplosbaar middel."),
    tabel("Zuur, neutraal of basisch?", [
        ("pH 2", "zuur"), ("pH 7", "neutraal"), ("pH 12", "basisch"), ("pH 5", "zuur"),
    ], "Onder 7 is zuur, 7 is neutraal, boven 7 is basisch.", kolommen=["zuur", "neutraal", "basisch"]),
    tabel("Is dit een zuur?", [
        ("azijnzuur in huishoudazijn", J), ("citroenzuur in citroensap", J), ("zuiver water", F), ("zoutzuur in maagsap", J),
    ], "Zuiver water is neutraal."),
    inv("Welke pH heeft zuiver water? Geef het getal.", ["7", "zeven"], "Het midden van de schaal."),
    inv("Rode koolsap kleurt in een zure vloeistof rood. Hoe noem je zo'n stof die met een kleur toont of iets zuur is? Eén woord.", ["indicator", "een indicator"],
        "Een zuur-base indicator."),
    keuze("Een stof met het pictogram voor gassen onder druk mag je [[*niet in de zon|gerust in de zon]] laten staan.", "Warmte doet de druk stijgen."),
    keuze("Een stof die goed oplost in water, lost meestal [[*slecht|goed]] op in thinner.", "Soort lost soort."),
    keuze("Een partje citroen pak je beter niet in [[*aluminiumfolie|plasticfolie]].", "Het zuur tast aluminium aan."),
    keuze("Komt een bijtende stof op je huid, dan [[*spoel je meteen lang met veel water|wrijf je ze in met een doek]].", "Spoelen verdunt en voert af."),
    keuze("Een stof is bij kamertemperatuur vast als haar smeltpunt [[*boven|onder]] de kamertemperatuur ligt.", "Ze smelt pas bij een hogere temperatuur."),
    tabel("Is dit een goede voorzorg met een chemisch product?", [
        ("handschoenen dragen", J), ("het product overgieten in een lege drankfles", F),
        ("buiten het bereik van kinderen bewaren", J), ("het etiket lezen voor je begint", J),
    ], "In een drankfles kan iemand het per vergissing drinken."),
    sleep("Op een etiket vertelt de [[H-zin]] welk gevaar er is, de [[P-zin]] wat je moet doen. Het [[pictogram]] vat het gevaar samen in een beeld.",
          ["R-zin", "nutriscore"], "Hazard en precaution."),
    volgorde("Zet deze vloeistoffen van zuur naar basisch.", [
        "citroensap", "regenwater", "zuiver water", "zeepsop", "ontstopper",
    ], "Van een lage naar een hoge pH."),
    open_("Leg uit waarom je een restje chemisch product niet in de gootsteen giet.",
          "Veel van die stoffen zijn schadelijk voor het water en het leven erin. Ze horen bij het klein gevaarlijk afval.",
          "Kga naar het containerpark."),
]
