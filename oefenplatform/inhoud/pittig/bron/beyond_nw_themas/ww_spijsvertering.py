"""Welzijnswetenschappen: het spijsverteringsstelsel — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen biologie Beyond (osmose en transport,
zelfde prenten), aangevuld met eigen vragen over bouw, verteringssappen,
absorptie, voedingsstoffen, darmflora en aandoeningen.
"""
from ..beyond_bio_themas import enzymen as E
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, open_

OVER = [E.VRAGEN[i] for i in (3, 4, 5, 6, 13, 19, 21, 24)]

EIGEN = [
    casus(
        "Na een maaltijd met spaghetti, kaas en olijfolie volgt een verpleegkundige "
        "in de les wat er met de voedingsstoffen gebeurt. Zetmeel, eiwitten en vetten "
        "worden stap voor stap afgebroken en daarna opgenomen.",
        [
            tabel("Welk eindproduct ontstaat bij de volledige vertering?", [
                ("zetmeel uit de spaghetti", "glucose"),
                ("eiwitten uit de kaas", "aminozuren"),
                ("vetten uit de olie", "glycerol en vetzuren"),
            ], "Pas als kleine bouwstenen kunnen ze door de darmwand.",
               kolommen=["glucose", "aminozuren", "glycerol en vetzuren"]),
            keuze("De vetten worden eerst door [[*galzouten|lipase|zoutzuur]] in kleine druppeltjes verdeeld.",
                  "Gal emulgeert vet zonder het chemisch af te breken. Daarna kan lipase beter werken."),
            mk("Hoe bereiken de glycerol en vetzuren na opname het bloed?",
               ["Als vetbolletjes via de lymfevaten",
                "Rechtstreeks via de leverpoortader naar de lever",
                "Via de galgang terug naar de galblaas",
                "Door osmose langs de wand van de dikke darm"], 0,
               "In de darmcel worden het weer vetten die in de lymfe terechtkomen. Glucose en aminozuren gaan via de leverpoortader."),
        ],
    ),
    tabel("Hoort dit deel bij de dunne of bij de dikke darm?", [
        ("twaalfvingerige darm", "dunne darm"),
        ("blinde darm met wormvormig aanhangsel", "dikke darm"),
        ("kronkeldarm", "dunne darm"),
        ("endeldarm", "dikke darm"),
    ], "De dunne darm bestaat uit twaalfvingerige, nuchtere en kronkeldarm.", kolommen=["dunne darm", "dikke darm"]),
    koppel("Koppel elk orgaan aan wat het afgeeft of doet.", [
        ["lever", "maakt gal"],
        ["galblaas", "slaat gal op en dikt ze in"],
        ["alvleesklier", "geeft natriumwaterstofcarbonaat en enzymen af"],
        ["pariëtale cellen van de maag", "maken zoutzuur"],
    ], ["blinde darm"], "Lever en galblaas werken samen; de alvleesklier neutraliseert en verteert."),
    volgorde("Zet de delen in de volgorde waarin het voedsel ze passeert.", [
        "mondholte", "slokdarm", "maag", "twaalfvingerige darm", "dikke darm",
    ], "De maagportier laat de voedselbrij beetje bij beetje in de twaalfvingerige darm."),
    mk("Waarom is het zure maagsap nuttig?",
       ["Het doodt bacteriën en maakt pepsine actief",
        "Het breekt zetmeel af tot glucose",
        "Het verdeelt vetten in kleine druppeltjes zodat ze oplossen",
        "Het neemt het meeste water op uit de voedselbrij"], 0,
       "Zetmeel wordt in mond en darm verteerd, vet door gal en lipase."),
    tabel("Klopt dit over de bouw van de darmwand?", [
        ("De slijmvlieslaag ligt aan de binnenkant.", J),
        ("De spierlaag zorgt voor de peristaltiek.", J),
        ("Microvilli verkleinen het oppervlak om water te sparen.", F),
        ("Plooien en darmvlokken vergroten het opnameoppervlak.", J),
    ], "Hoe groter het oppervlak, hoe meer voedingsstoffen tegelijk opgenomen worden."),
    sleep("Amylase knipt zetmeel tot [[maltose]]. Maltase knipt dat verder tot [[glucose]]. Lactase splitst melksuiker in glucose en [[galactose]].",
          ["fructose", "aminozuren"], "Sacharase splitst gewone suiker in glucose en fructose."),
    keuze("Endopeptidasen knippen eiwitketens [[*in het midden|aan de uiteinden|in vetdruppels]].",
          "Exopeptidasen knippen telkens een aminozuur van het uiteinde."),
    sorteer("Is dit een vetoplosbare of een wateroplosbare vitamine?", ["Vetoplosbaar", "Wateroplosbaar"], [
        ["vitamine A", "Vetoplosbaar"],
        ["vitamine C", "Wateroplosbaar"],
        ["vitamine D", "Vetoplosbaar"],
        ["vitamine B12", "Wateroplosbaar"],
    ], "A, D, E en K zijn vetoplosbaar. B en C lossen op in water."),
    mk("Wat is een essentieel aminozuur?",
       ["Een aminozuur dat je via de voeding moet binnenkrijgen",
        "Een aminozuur dat de lever in grote hoeveelheden aanmaakt",
        "Een aminozuur dat enkel in plantaardige voeding voorkomt",
        "Een aminozuur dat de darmflora in de dikke darm verteert"], 0,
       "Het lichaam kan het niet zelf maken, dus moet het uit het voedsel komen."),
    tabel("Klopt dit over de darmflora?", [
        ("Bacteriën in de dikke darm maken vitamine K.", J),
        ("Een antibioticakuur kan de darmflora verstoren.", J),
        ("Voedingsvezels zijn voor de darmflora nutteloos.", F),
    ], "Vezels zijn voedsel voor nuttige bacteriën en houden de stoelgang vlot."),
    koppel("Koppel elke aandoening aan haar kenmerk.", [
        ["coeliakie", "gluten beschadigen de darmvlokken"],
        ["maagzweer", "vaak veroorzaakt door Helicobacter pylori"],
        ["ziekte van Crohn", "chronische ontsteking overal in het kanaal"],
        ["lactose-intolerantie", "te weinig lactase in de dunne darm"],
    ], ["blindedarmontsteking door gal"], "Elke aandoening treft een ander deel of een andere stap."),
    mk("Waarom heeft iemand na het wegnemen van de galblaas vaak last na een vette maaltijd?",
       ["Er komt minder gal tegelijk vrij voor vet",
        "De lever maakt dan helemaal geen gal meer",
        "De alvleesklier stopt met het maken van lipase",
        "Het maagzuur kan niet meer geneutraliseerd worden"], 0,
       "De lever maakt nog gal, maar zonder opslag komt ze in kleine porties."),
    keuze("Het meeste water wordt opgenomen in de [[*dunne darm|dikke darm|maag]].",
          "De dikke darm neemt het overige water op en dikt de ontlasting in."),
    tabel("Waar wordt dit vooral opgenomen?", [
        ("glucose en aminozuren", "dunne darm"),
        ("het overige water na de dunne darm", "dikke darm"),
        ("vitamine K gemaakt door bacteriën", "dikke darm"),
        ("vetzuren en glycerol", "dunne darm"),
    ], "De dunne darm neemt de meeste voedingsstoffen op, de dikke darm vooral het restwater en wat de darmflora maakt.",
       kolommen=["dunne darm", "dikke darm"]),
    mk("Wat beschermt de maagwand tegen het eigen zoutzuur?",
       ["Een dikke laag slijm op het slijmvlies",
        "Het strottenklepje dat het zuur tegenhoudt",
        "De gal die vanuit de galblaas in de maag stroomt",
        "De darmflora die het zuur meteen opeet"], 0,
       "Slijm vormt een beschermende laag. Is die beschadigd, dan kan een maagzweer ontstaan."),
    sleep("Bij het slikken sluit het [[strottenklepje]] de luchtpijp af. Daarna duwt de [[peristaltiek]] het voedsel door de slokdarm naar de maag.",
          ["maagportier", "galblaas"], "De maagportier ligt aan de uitgang van de maag, niet aan de ingang."),
    tabel("Is dit transport passief of actief?", [
        ("glucose die tegen het concentratieverschil in de darmcel gaat", "actief"),
        ("water dat door osmose de darmwand passeert", "passief"),
        ("fructose die via een transporteiwit met het verschil meegaat", "passief"),
    ], "Actief transport kost ATP en gaat tegen het verschil in. Gefaciliteerde diffusie gaat mee met het verschil.",
       kolommen=["passief", "actief"]),
    keuze("Opgenomen glucose gaat via de [[*leverpoortader|longader|aorta]] eerst naar de lever.",
          "De lever regelt zo wat er naar de rest van het lichaam gaat."),
    open_("Leg uit waarom de dunne darm zo een groot binnenoppervlak heeft en wat dat met opname te maken heeft.",
          "Door plooien, darmvlokken en microvilli is het oppervlak enorm. Zo kunnen veel voedingsstoffen tegelijk door diffusie en actief transport opgenomen worden, en dicht bij de bloedvaten in de vlokken."),
]

VRAGEN = OVER + EIGEN
